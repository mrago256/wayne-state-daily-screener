import base64
import csv
import datetime
from notification import sendNotif
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def checkDate():
  currentDate = datetime.date.today()

  try:
    file = open("lastRun.txt", "r")

    if file.readline() == str(currentDate):
      file.close()
      exit()
  except IOError:
    pass

  file = open("lastRun.txt", "w")
  file.write(str(currentDate))
  file.close()

  return currentDate.strftime('%A')

def decodeB64(encodedStr):
  base64Bytes = encodedStr.encode("ascii")
  stringBytes = base64.b64decode(base64Bytes)
  originalString = stringBytes.decode("ascii")
  return originalString

def readFile():
  try:
    file = open("screenerData.csv", "r")
  except FileNotFoundError:
    errMessage = "The data file does not exist. Try running CreateFile.py first"
    print(errMessage)
    sendNotif(errMessage)
    exit()

  csvFile = csv.reader(file)

  for line in csvFile:
    mainDict[line[0]] = line[1:]

  file.close()

mainDict = {}
dayOfWeek = checkDate()

readFile()

# quit if there are no buildings
try:
  mainDict[dayOfWeek]
except KeyError:
  exit()

mainDict["pass"] = decodeB64(mainDict["pass"][0])

# make it run headlessly
chrome_options = Options()
chrome_options.add_argument("--headless")

try:
  ser = Service("chromedriver.exe")
  driver = webdriver.Chrome(service=ser, options=chrome_options)
except selenium.common.exceptions.WebDriverException:
  errMessage = "Driver file not found. Attempting update..."
  print(errMessage)
  sendNotif(errMessage)
  os.system("updater.bat")

  try:
    driver = webdriver.Chrome(service=ser, options=chrome_options)
    errMessage = "Update Successful"
    print(errMessage)
    sendNotif(errMessage)
  except selenium.common.exceptions.WebDriverException:
    errMessage = "chromedriver updated; Error still presists. Refer to readme"
    print(errMessage)
    sendNotif(errMessage)
    exit()

driver.get("https://forms.wayne.edu/covid-19-screening")

# log into screener
accessID = driver.find_element(By.NAME, "accessid")
passwd = driver.find_element(By.NAME, "passwd")
accessID.clear()
passwd.clear()
accessID.send_keys(mainDict["user"])
passwd.send_keys(mainDict["pass"])
passwd.send_keys(Keys.RETURN)

# input phone number
try:
  phoneBox = driver.find_element(By.NAME, "f_253006")
  phoneBox.send_keys(mainDict["phone"])
except selenium.common.exceptions.NoSuchElementException:
  errMessage = "User credentials incorrect"
  print(errMessage)
  sendNotif(errMessage)
  driver.close()
  driver.quit()
  exit()

# add current buildings
buildingSearch = driver.find_element(By.CLASS_NAME, "select2-search__field")

for item in mainDict[dayOfWeek]:
  buildingSearch.send_keys(item)
  searchText = driver.find_element(By.CLASS_NAME, "select2-results__options").text

  if searchText != "No results found":
    driver.find_element(By.CLASS_NAME, "select2-results__options").click()

  else:
    errMessage = "Building error. Rerun CreateFile.py"
    print(errMessage)
    sendNotif(errMessage)
    driver.close()
    driver.quit()

# click no on all boxes
driver.find_element(By.ID, "f_251741_no").click()
driver.find_element(By.ID, "f_251742_no").click()
driver.find_element(By.ID, "f_255927_no").click()

# click submit
driver.find_element(By.ID, "formy-button").click()

driver.close()
driver.quit()
