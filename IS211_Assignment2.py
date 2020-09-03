import urllib.request
import csv
import os, ssl
import datetime
import logging



# This is needed to avoid CERTIFICATE ERRORS
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
     ssl._create_default_https_context = ssl._create_unverified_context
# DO NOT DELETE ABOVE


#import urllib.request
#with urllib.request.urlopen('https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv') as response:
#   html = response.read()


# This is the link address for the assignment
# https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv


# This gets the URL
import urllib.request

getTheUrl = urllib.request.urlopen('https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv').read()\
   .decode('utf-8')

newDict = {}
csv_reader = csv.reader(getTheUrl, delimiter=',')

index = 2

for eachLine in csv_reader:
   try:
      birthdate = datetime.datetime.strptime(eachLine[2], '%d/%m/%y').date()
      newDict[eachLine[0]] = (eachLine[1], birthdate)
   except:
      logging.error('Error in {} for {}'.format(index, eachLine[0]))
   finally:
      index += 1
