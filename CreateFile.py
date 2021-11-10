import base64
import csv

def encodeB64(originalStr):
  stringBytes = originalStr.encode("ascii")
  base64Bytes = base64.b64encode(stringBytes)
  base64String = base64Bytes.decode("ascii")
  return base64String

dayList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
mainDict = {}

mainDict["user"] = [input("Access ID: ")]

mainDict["pass"] = [encodeB64(input("Password: "))]

mainDict["phone"] = [input("Phone Number: ")]

for item in dayList:
  classList = []
  classNum = int(input("Number of buildings on " + str(item) + ": "))

  for i in range(classNum):
    classList.append(input("Enter building " + str(i + 1) + " for " + str(item) + ": "))

  mainDict[item] = classList

file = open("screenerData.csv", "w")
csvFile = csv.writer(file)

for item in mainDict:
  i = 0
  # put building check here

  file.write(item)

  if mainDict[item]:
    file.write(",")

  for value in mainDict[item]:
    if "," in value:
      print("\nPlease check building name and try again")
      file.close
      exit()

    i += 1

    file.write(str(value))

    if i != len(mainDict[item]):
      file.write(",")

  file.write("\n")

file.close()
