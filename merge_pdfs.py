#!/usr/bin/env python3

from PyPDF2 import PdfFileMerger
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--directory", required=True) #directory where pdf files are located
parser.add_argument("--output", required=True) #output file location
args = vars(parser.parse_args())

directory = args["directory"]
output = args["output"]

##Make sure directory ends in /
if directory[-1] != "/":
    print ("Directory needs to end with '/', exiting...")
    exit()

##List all of the files in the directory:
print ("Attempting to merge files:")
for fname in sorted(os.listdir(directory)):
    if fname.endswith(".pdf"):
        print(directory + fname)

##Verify the output file doesn't exist or quit
if os.path.exists(output):
    print ("Output File already exists, exiting...")
    exit()
else:
    #We can merge the two files
    merger = PdfFileMerger()
    for fname in sorted(os.listdir(directory)):
        if fname.endswith(".pdf"):
            merger.append(directory + fname)
    merger.write(output)
    merger.close()
