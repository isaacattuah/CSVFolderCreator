import os
import csv

#Function for reading .csv file
def csvReader(filename, array):
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            array.append(row[0])

#Function for creating folders
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

      

# Example
patients = []
csvReader('patientlist.csv',patients)
for patient in range(len(patients)):
    createFolder('./%s/'%(patients[patient])) 
# Creates a folder in the current directory called data
