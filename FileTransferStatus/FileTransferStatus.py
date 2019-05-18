#Reconcilation of File transfer
from datetime import datetime

sourceLog= 'Source.csv'
destLog = 'Dest.csv'
fileList=[]

#Search whether the file is present at the destination log
def searchInDestLog():
    for fileObject in fileList:
        with open(destLog) as destLogFile:
            for line in destLogFile:
                line=line.rstrip()
                columns = line.split(',')
                if(fileObject['FileName']==columns[0]):
                    fileObject['ReceivedTimestamp']=columns[1]

#Calculate transfer time
def calculateTransferTime():
    timeFormat = '%Y-%m-%d %H:%M:%S'
    for fileObject in fileList:
        sendingTimeStamp = datetime.strptime(fileObject['SendingTimeStamp'],timeFormat)
        if('ReceivedTimestamp' in fileObject.keys()):
            receivedTimeStamp = datetime.strptime(fileObject['ReceivedTimestamp'],timeFormat)
            transferTime = receivedTimeStamp - sendingTimeStamp
            fileObject['TransferTime'] = str(transferTime)
        else:
            fileObject['ReceivedTimestamp'] = 'NULL'
            fileObject['TransferTime'] = 'NULL'

#Generate Report
def generateReport():
    report = open('TransferReport.csv','w')
    report.write('File Name,Sending Timestamp,Received Timestamp,Transfer Time \n')
    for fileObject in fileList:
        report.write(fileObject['FileName'] + ',' + fileObject['SendingTimeStamp'] + ',' + fileObject['ReceivedTimestamp'] + ',' + fileObject['TransferTime'] + '\n')



print('Starting the utility...')
print('Start time : ' + str(datetime.now().time()))
with open(sourceLog) as sourceLogFile:
    for line in sourceLogFile:
        line=line.rstrip()
        columns = line.split(',')
        if(columns[0]=='FileName'):
            continue
        fileObject = {'FileName':columns[0], 'SendingTimeStamp':columns[1]}
        fileList.append(fileObject)
searchInDestLog()
calculateTransferTime()
generateReport()
print('Report generated...')
print('End time : ' + str(datetime.now().time()))
