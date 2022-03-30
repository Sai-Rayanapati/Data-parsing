# import csv

# headings =["message"]
# filepath = "dialogueText_301.csv" # This should be relative to the directory this py is in
# with open(filepath, "r") as csvFile:
#     temp = csv.reader(csvFile)
#     csv_writer = csv.writer(open("Sorted"+filepath, 'w'))
#     next(temp)
#     csv_writer.writerow(headings)
#     for row in temp:  
#         csv_writer.writerow([row[5]])


# #headings =["date", "text"]
# filepath = "discordchat1.csv" # This should be relative to the directory this py is in
# with open(filepath, "r" , delimiter='/t') as csvFile:
#     temp = csv.reader(csvFile)
#     csv_writer = csv.writer(open("SortedDiscordChat1.csv, 'w'))
#     #csv_writer.writerow(headings)
#     for row in temp:  
#         csv_writer.writerow([row[1]])

import csv, json, sys
#if you are not using utf-8 files, remove the next line
sys.setdefaultencoding("UTF-8") #set the encode to utf8
#check if you pass the input file and output file
if sys.argv[1] is not None and sys.argv[2] is not None:
    fileInput = sys.argv[1]
    fileOutput = sys.argv[2]
    inputFile = open(fileInput) #open json file
    outputFile = open(fileOutput, 'w') #load csv file
    data = json.load(inputFile) #load json content
    inputFile.close() #close the input file
    output = csv.writer(outputFile) #create a csv.write
    output.writerow(data[0].keys())  # header row
    for row in data:
        output.writerow(row.values()) #values row