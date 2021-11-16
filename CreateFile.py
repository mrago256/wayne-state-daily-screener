import base64
import csv
from fuzzywuzzy import process

# using a list for testing purposes. Might change it if too unoptimized
buildingList = []
dayList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
mainDict = {}

# converting user password to base64 to avoid storing in plaintext
def encodeB64(originalStr):
  stringBytes = originalStr.encode("ascii")
  base64Bytes = base64.b64encode(stringBytes)
  base64String = base64Bytes.decode("ascii")
  return base64String

def getResult(building):
  result = process.extractOne(building, buildingList)

  # using the rlevance to determine if correct approximation
  if result[1] >= 75:
    return result[0]

  else:
    return False

def loadBuildings():
  buildingFile = open("buildingList.txt", "r")

  for line in buildingFile:
    buildingList.append(line[:-1])

  buildingFile.close()

def setDictionary():
  print("\nPress [Enter] after each building")
  print("Press [Enter] on blank space to advance the day")
  for day in dayList:
    classList = []
    userDone = False

    while not userDone:
      building = input("Enter building for " + str(day) + ": ")

      if building != "":

        if getResult(building):
          building = getResult(building)
          classList.append(building)

        else:
          print("That building doesn't exist. Please be more clear")

      else:
        userDone = True
    classList.sort()
    mainDict[day] = classList


mainDict["user"] = [input("Access ID: ")]
mainDict["pass"] = [encodeB64(input("Password: "))]
mainDict["phone"] = [input("Phone Number: ")]
loadBuildings()
setDictionary()

file = open("screenerData.csv", "w")
csvFile = csv.writer(file)

for key in mainDict:

  file.write(key)

  if mainDict[key]:
    file.write(",")

  for value in mainDict[key]:
    if "," in value:
      print("\nRerun script and remove commas from credentials")
      file.close
      exit()

    file.write(str(value))

    if mainDict[key].index(value) != len(mainDict[key]) - 1:
      file.write(",")

  file.write("\n")

file.close()
