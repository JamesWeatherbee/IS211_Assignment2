import urllib.request
import csv
import os, ssl
import datetime
import logging
from io import StringIO
import argparse


# This is needed to avoid CERTIFICATE ERRORS
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
     ssl._create_default_https_context = ssl._create_unverified_context
# DO NOT DELETE ABOVE


dataDict = {}
url = "https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv"


def downloadData(url):
   """Opens a user-provided URL

   Args:
      url(str): A user's URL.

   Returns:
      content(str): The data from the user's URL file.
   """
   content = urllib.request.urlopen(url).read().decode("ascii", "ignore")
   return content


def processData(file):
   """Checks the user provided URL data for format errors.

   Args:
      content(str): The data from the user's URL in .CSV format.

   Returns:
      newDict(dict): A dictionary with the .csv file's names and birth dates.
   """
   data = StringIO(file)
   csv_reader = csv.reader(data, delimiter=',')
   next(csv_reader)
   index = 2
   for lines in csv_reader:
      try:
         birthday = datetime.datetime.strptime(lines[2], '%d/%m/%y').date()
         dataDict[lines[0]] = (lines[1], birthday)
      except:
         logger.error("Error in line {} for {}".format(index, lines[0]))
      finally:
         index += 1


def displayPerson(id, personData=dataDict):
   """Using the ID number, returns the name and birth date associated with the ID.

   Args:
      id(int): The number to find the name and birthdate.
      personData(dict): The dictionary containing the ID, name, and birth date data.

   Returns:
      (str): The name and birth date affiliated with the ID number.
   """
   if id in personData.keys():
      print("{} is {} with the birthdate of {}". format(id, personData[id][0], personData[id][1]))
   else:
      print("No ID for that user.")

def main():
   global logger
   logger=logging.getLogger("IS211_Assignment2")
   f = logging.FileHandler('error.log')
   f.setLevel(logging.ERROR)
   logger.addHandler(f)

   commandParser = argparse.ArgumentParser(description = 'Send url parameter to the script')
   commandParser.add_argument('--url', type = str, help = 'Link to the CSV file.')
   args = commandParser.parse_args()
   if not args.url:
      exit()
   try:
      csvData = downloadData(args.url)
   except:
      print('An Error has occured.')
      exit()
   personData = processData(csvData)

   isTrue = True
   while isTrue:
      ask = input('Enter ID:')
      if int(ask) > 0:
         displayPerson(ask)
      else:
         isTrue = False


if __name__ == "__main__":
   main()

