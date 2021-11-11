import base64
import csv

dayList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
mainDict = {}

# converting user password to base64 to avoid storing in plaintext
def encodeB64(originalStr):
  stringBytes = originalStr.encode("ascii")
  base64Bytes = base64.b64encode(stringBytes)
  base64String = base64Bytes.decode("ascii")
  return base64String

def setDictionary():
  print("\nPress [Enter] after each building")
  print("Press [Enter] on blank space to advance the day")
  for day in dayList:
    classList = []
    userDone = False

    while not userDone:
      building = input("Enter building for " + str(day) + ": ")

      if building != "":
        classList.append(building)

      else:
        userDone = True

    mainDict[day] = classList


mainDict["user"] = [input("Access ID: ")]
mainDict["pass"] = [encodeB64(input("Password: "))]
mainDict["phone"] = [input("Phone Number: ")]
setDictionary()

file = open("screenerData.csv", "w")
csvFile = csv.writer(file)

for key in mainDict:

  # TODO: put building check here

  file.write(key)

  if mainDict[key]:
    file.write(",")

  for value in mainDict[key]:
    if "," in value:
      print("\nPlease check building name and try again")
      file.close
      exit()

    file.write(str(value))

    if mainDict[key].index(value) != len(mainDict[key]) - 1:
      file.write(",")

  file.write("\n")

file.close()
