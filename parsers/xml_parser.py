import sys

# Open a file
file_object = open("E:\SCIENCE-LOGIC\CCC.XML", 'r')
oid = ''
vaueType = ''
countObjects = 0
new_file = []

for line in file_object:
  lineToSave = ''

  if "oid" in line:
    oid = line.split('\"')[1]

  if "valueType" in line:
    valueType = line.split('\"')[1]
    defaultOidValue = "0"

    if "String" in valueType:
      defaultOidValue = "String value"

    lineToSave = oid + ' = ' + valueType + ': ' + defaultOidValue
    new_file.append(lineToSave)
    #print lineToSave

    oid = ''
    vaueType = ''
    countObjects = countObjects + 1
file_object.close()
#print "Total rows parsed: " + countObjects


new_file_object = open("E:SCIENCE-LOGIC\WALKS\RESULT.WKL", 'a')

for line in new_file:
  new_file_object.write("%s\n" % line)
  print line

new_file_object.close()