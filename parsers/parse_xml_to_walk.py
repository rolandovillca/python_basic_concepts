import sys

# os.path.dirname(os.path.realpath(__file__))

# Open a file
file_object = open('xml_file.xml', 'r')
oid = ''
value_type = ''
count_objects = 0
new_file = []

for line in file_object:
  line_to_save = ''

  if 'oid' in line:
    oid = line.split('\"')[1]

  if 'valueType' in line:
    valueType = line.split('\"')[1]
    default_oid_value = '0'

    if 'String' in valueType:
      default_oid_value = 'String value'

    line_to_save = oid + ' = ' + valueType + ': ' + default_oid_value
    new_file.append(line_to_save)
    #print line_to_save

    oid = ''
    value_type = ''
    count_objects = count_objects + 1
file_object.close()
#print 'Total rows parsed: ' + count_objects

new_file_object = open('walk_file.wkl', 'a')

for line in new_file:
  new_file_object.write('%s\n' % line)
  print line

new_file_object.close()