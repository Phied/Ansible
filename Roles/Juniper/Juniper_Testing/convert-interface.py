import json
import csv
import sys

#with open('data.json') as json_file:
#  data = json.load(json_file)
#  print(data)


data = json.loads(sys.argv[1])

return_data = data["gathered"]

# now we will open a file for writing
data_file = open(sys.argv[2], 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

#print("STUFF:" + return_data)

for interface in return_data:
    if count == 0:

        # Writing headers of CSV file
        header = interface.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(interface.values())

data_file.close()
