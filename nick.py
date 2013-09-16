#!/usr/bin/env/python

import sys
import os
import csv
import time

# On Cardstore, we use multiple redirect .csv files to load key/values into a master redirect
# ConcurrentHashMap. This script iterates through the combination of those files.  It sanitizes the file
# by removing duplicate entries.  Since the ordering of the entries is important, we can't just
# quickyly sort the file.  We need to iterate though the file line by line by line to check
# that the entry included later is the effective entry.  The default list.sort in python might
# do this way more efficiently, but this script is just being used for an initial load of a
# db table....

DEBUG = True


def statusUpdate(startTime, currentIndex, totalRecords, duplicateCount):
    seconds = time.time() - startTime
    minutes = int(seconds / 60)
    seconds = int(seconds - minutes * 60)

    if seconds < 10:
        seconds = '0' + str(seconds)
    if minutes < 10:
        minutes = '0' + str(minutes)

    statusMsg = 'Writing entry {0}/{1} {3}% {4}:{5} elapsed ({2} duplicates found)'
    statusMsg = statusMsg.format(currentIndex, totalRecords, duplicateCount, round(100 * float(currentIndex) / float(totalRecords), 1), minutes, seconds)

    sys.stdout.write('\b' * statusUpdate.previousLength)
    sys.stdout.flush()

    sys.stdout.write(statusMsg)

    statusUpdate.previousLength = len(statusMsg)
statusUpdate.previousLength = 0


def removeDuplicatesAndWrite(inputList, outputFileName):
    duplicateDict = {}
    totalRecords = len(inputList)
    currentIndex = 0

    startTime = time.time()

    with open(outputFileName, 'wb') as fout:
        writer = csv.writer(fout)
        for index, record in enumerate(inputList):
            currentIndex += 1
            effectiveEntry = record

            if duplicateDict.get(record[0].lower()) != None:
                continue

            for recordToCompare in inputList[index+1:]:
                if effectiveEntry[0].lower() == recordToCompare[0].lower():
                    effectiveEntry = recordToCompare
                    duplicateDict[effectiveEntry[0].lower()] = True

            writer.writerow(effectiveEntry)
            statusUpdate(startTime, currentIndex, totalRecords, len(duplicateDict))

    print ""


def readCsv(input):
    entries = []
    with open(input, 'rb') as fin:
        reader = csv.reader(fin)
        for row in reader:
            entries.append(row)
    return entries


def main():
    print "======================="
    print "CSV duplicate sanitizer"
    print "======================="

    print "PURPOSE: Removes duplicate entries from .csv files.  If duplicate entries are found, \
the last entry is used. Output files are named $inputfile_sanitized.csv"

    print ""

    inputFileName = ""

    if len(sys.argv) < 2:
        if DEBUG:
            inputFileName = raw_input('input file: ')
        else:
            print "USAGE: " + sys.argv[0] + " {input file .csv}"
            print ""
            return


    inputFileName = inputFileName if inputFileName is not None else sys.argv[1]
    name, extension = os.path.splitext(inputFileName)
    outputFileName = os.path.basename(name) + "_sanitized" + extension

    print ""
    print "Input filename: " + inputFileName
    print "Output filename: " + outputFileName
    print ""

    print "Reading csv: " + inputFileName
    print ""

    inputCsv = readCsv(inputFileName)
    print "Writing csv: " + outputFileName
    removeDuplicatesAndWrite(inputCsv, outputFileName)

main()