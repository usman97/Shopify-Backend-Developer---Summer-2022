import json
import csv
import CURD 

def exportDataToCSV():
    data = CURD.readEntireInventoryData()

    # We will create a CSV file where data will be stored
    fileName = "./Data/productsInventory.csv"

    csvFile = open(fileName, "w")

    csvWriter = csv.writer(csvFile)

    count = 0

    for details in data:
        if count == 0:

            header = details.keys()
            csvWriter.writerow(header)
            count += 1

        
        csvWriter.writerow(details.values())
    csvFile.close()
