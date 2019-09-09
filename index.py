from datetime import datetime
import csv

## VARS REFERENCE: 
## Timestamp[0], user-agent[1], IP[2], mime_type_length[3], plugins_length[4], Headers[5], path[6]

## UNCOMMENT TO PRINT ALL OF THE DATA ------------------------------> HELPER 1

# with open('test_20180320.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} IS TIMESTAMP, {row[1]} IS USER AGENT, {row[2]} IS IP,{row[3]} IS MIME TYPE LENGTH,{row[4]} IS PLUGINS LENGTH,{row[5]} ARE HEADERS,{row[6]} IS PATH')
#             line_count += 1
# print(f'Processed {line_count} lines.')


## UNCOMMENT TO GROUP VARS IN SEPARATE ARRAYS ------------------------------> HELPER 2.1

# timestamps = []
# user_agents = []
# ips = []
# mtl = []
# plugins = []
# headers = []
# path = []

# with open('test_20180320.csv', mode='r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if row[0] == 'Timestamp' or row[0]:
#             timestamps.append(row[0])
#         if row[1] == 'user-agent' or row[1]:
#             user_agents.append(row[1])  
#         if row[2] == 'IP' or row[2]:
#             ips.append(row[2])  
#         if row[3] == 'mime_type_length' or row[3]:
#             mtl.append(row[3])  
#         if row[4] == 'plugins_length' or row[4]:
#             plugins.append(row[4])
#         if row[5] == 'Headers' or row[5]:
#             headers.append(row[5]) 
#         if row[6] == 'path' or row[6]:
#             path.append(row[6])
#         line_count += 1

## UNCOMMENT TO PRINT WHICH ARRAY OF VARS WANTED IN PARTICULAR
# print(timestamps)
# print(user_agents)
# print(ips)
# print(mtl)
# print(plugins)
# print(headers)
# print(path)
# print(line_count)

## UNCOMMENT TO PRINT CONVERTED TIMESTAMPS ------------------------------> HELPER 3

# converted_timestamps = []
# all_ips = []

# f = open('test_20180320.csv')
# csv_f = csv.reader(f)

# line_count = 0
# for row in csv_f:
#     if line_count == 0:
#         print(f'Column names are {"".join(row)}')
#         line_count += 1
#     else:
#         dt_obj = float(row[0])
#         converted_timestamp = datetime.fromtimestamp(dt_obj)
#         # CONVERTED TIMESTAMP WITH DATE AND TIME
#         new_conv_ts = converted_timestamp.strftime("%m/%d/%Y, %H:%M:%S")
#         # CONVERTED TIMESTAMP WITH ONLY TIME
#         # new_conv_ts = converted_timestamp.strftime("%H:%M:%S")
#         converted_timestamps.append(new_conv_ts)
#         line_count += 1

# print(converted_timestamps)


