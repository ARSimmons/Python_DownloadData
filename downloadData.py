import urllib2
import os
import subprocess
import csv
import string

def unzipFile(downloadPath, unzipPath):
    extension = downloadPath[downloadPath.rfind('.')+1:len(downloadPath)]

    if extension == 'exe':
        subprocess.Popen([downloadPath, '/auto', unzipPath])

    elif extension == 'zip':
        print 'todo'
        
    else:
        print 'Error: invalid extension:  ' + extension

# Directory to save the file
rawDataDirectory = r'C:\Users\Ari\Desktop\code'

# Open csv file
f = open('ADDRESS_LIST.csv', 'rb')

# Get csv reader
reader = csv.reader(f)

# Skip the header row
reader.next()

# Loop through each row in the csv file reader and download the file
for row in reader:

    townName = row[0]
    link = row[1]

    # The name of the file that will be downloaded and saved
    downloadFileName = link[link.rfind('/')+1:len(link)]

    # The name of the file once unzipped
    unzippedFileName = downloadFileName[0:downloadFileName.rfind('.')]

    individualDirectory = rawDataDirectory + '\\' + townName

    # Full path to the downloaded and unzipped files
    downloadFilePath = individualDirectory + '\\' + downloadFileName
    unzippedFilePath = individualDirectory + '\\' + unzippedFileName

    # Create the directory for the file if it doesn't already exist
    if not os.path.exists(individualDirectory):
        os.makedirs(individualDirectory)

    # Open the remote file from a URL
    remoteFile = urllib2.urlopen(link)

    # Write the remote file out to a local file
    localFile = open(downloadFilePath, 'wb')
    localFile.write(remoteFile.read())
    localFile.close()

    # Unzip the Winzip self-extracting exe
    unzipFile(downloadFilePath, unzippedFilePath)





