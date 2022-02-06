# # Python code to illustrate with()
# with open("file.txt") as file:
#     data = file.read()
# # do something with data
#
# # Python code to illustrate with() alongwith write()
# with open("file.txt", "a") as f:
#     f.write("Hello World!!!")
#
# # >>> f.read(4)    # read the next 4 data
# #
# # >>> f.read()     # read in the rest till end of file
# #
# # >>> f.tell()    # get the current file position
# # 56
# #
# # >>> f.seek(0)   # bring file cursor to initial position
# # 0
#
# # >>> f.readlines()  #readlines() method returns a list of remaining lines of the entire file. All these reading methods return empty values when the end of file (EOF) is reached.
#
#
# # Python code to illustrate split() function
# with open("/home/hadoop/PyCharm/Python-Practice/file.txt", "r") as file:
#     data = file.readlines()
#     for line in data:
#         word = line.split()
#         print(word)

# Reading CSV Files With csv
import csv

with open("/home/hadoop/datasets/people.csv", "r+") as file:
    csv_data_reader = csv.reader(file, delimiter=';')
    line_cnt = 1
    for row in csv_data_reader:
        if line_cnt > 0:
            print(row)
            line_cnt += 1

# Reading CSV Files Into a Dictionary With csv

with open("/home/hadoop/datasets/people.csv", "r+") as file:
    csv_data_reader = csv.reader(file, delimiter=';')
    line_cnt = 1
    user_infos = []
    for row in csv_data_reader:
        if line_cnt > 0 and (row[1] != 'age'):
            user_infos.append({'name': row[0], 'age': row[1], 'job': row[2]})
            line_cnt += 1

for userinfo in user_infos:
    print(userinfo)

import pandas

df = pandas.read_csv('/home/hadoop/datasets/people.csv')
print(df)

# Reading json file

import json

with open('/home/hadoop/datasets/orders.json') as f:
    data = json.load(f)

print(data)

print(data["orders"][0]["toppings"])

# write json file

with open('/home/hadoop/datasets/zips.json') as f:
    data = json.load(f)

for zip in data['zips']:
    del zip['loc']  # deleting loc from data
    city = zip['city']  # get specific element
    state = zip['state']
    print(city, state)

with open('/media/hadoop/SOFTWARE/Saurabh/PyCharm/Python-Practice/resources/new_zip.json', 'w') as f:
    json.dump(data, f, indent=2)  # saving new jason without loc to new file
