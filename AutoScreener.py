import base64
import csv
import datetime
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def decodeB64(encodedStr):
  base64Bytes = encodedStr.encode("ascii")
  stringBytes = base64.b64decode(base64Bytes)
  originalString = stringBytes.decode("ascii")
  return originalString

def readFile():
  try:
    file = open("screenerData.csv", "r")
  except FileNotFoundError:
    print("The data file does not exist. Try running CreateFile.py first")
    exit()

  csvFile = csv.reader(file)

  for line in csvFile:
    mainDict[line[0]] = line[1:]

  file.close()

mainDict = {}
dayOfWeek = datetime.datetime.today().strftime('%A')

readFile()

# quit if there are no buildings
try:
  mainDict[dayOfWeek]
except KeyError:
  exit()

mainDict["pass"] = decodeB64(mainDict["pass"][0])

# make it run headlessly
chrome_options = Options()
# chrome_options.add_argument("--headless")

try:
  driver = webdriver.Chrome("./chromedriver", options=chrome_options)
except selenium.common.exceptions.WebDriverException:
  print("Driver file not found. Attempting update...")
  os.system("./updater.sh")

  try:
    driver = webdriver.Chrome("./chromedriver", options=chrome_options)
    print("Update Successful")
  except selenium.common.exceptions.WebDriverException:
    print("chromedriver updated; Error still presists. Refer to readme")
    exit()

driver.get("https://forms.wayne.edu/covid-19-screening")

# log into screener
accessID = driver.find_element_by_name("accessid")
passwd = driver.find_element_by_name("passwd")
accessID.clear()
passwd.clear()
accessID.send_keys(mainDict["user"])
passwd.send_keys(mainDict["pass"])
passwd.send_keys(Keys.RETURN)

# input phone number
phoneBox = driver.find_element_by_name("f_253006")
phoneBox.send_keys(mainDict["phone"])

# add current buildings
buildingSearch = driver.find_element_by_class_name("select2-search__field")

for item in mainDict[dayOfWeek]:
  buildingSearch.send_keys(item)
  searchText = driver.find_element_by_class_name("select2-results__options").text

  if searchText != "No results found":
    driver.find_element_by_class_name("select2-results__options").click()

  else:
    print("Building error. Rerun CreateFile.py")
    driver.close()
    exit()

# click no on all boxes
driver.find_element_by_id("f_251741_no").click()
driver.find_element_by_id("f_251742_no").click()
driver.find_element_by_id("f_255927_no").click()

# click submit
# driver.find_element_by_id("formy-button").click()

# driver.close()
