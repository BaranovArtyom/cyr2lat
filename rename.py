#!/usr/bin/python
import os
import shutil
import stat
import sys
import time
import subprocess
from transliterate import translit, get_available_language_codes, detect_language
import argparse


def space2_(directory):

    # parse through file list in the current directory
    for filename in os.listdir(directory):
        print("checking %s" % filename)
        if filename.find(".git") >= 0:
            continue
        if detect_language(filename) == 'ru':
            newfilename = translit(filename, 'ru', reversed=True)
            if newfilename.find(" ") >= 0:  # if a space is found
                # convert spaces to underscores
                newfilename = newfilename.replace(" ", "_")
            os.chmod(os.path.join(directory, filename), stat.S_IWRITE)
            os.rename(os.path.join(directory, filename),
                      os.path.join(directory, newfilename))
            filename = newfilename
        if os.path.isdir(os.path.join(directory, filename)):
            os.chdir(os.path.join(directory, filename))
            space2_(".")
            os.chdir("..")


# Initiate the parser
# parser = argparse.ArgumentParser()
# parser.add_argument("--folder", "-f", help="set source folder")

# # Read arguments from the command line
# args = parser.parse_args()

# # Check for --width
# if args.folder:
#     print("Source folder set to %s" % args.folder)
#     directory = args.folder
#     space2_(directory)  # parse through file list in the directory
# else:
#     print("Set source folder")
#     exit

space2_(".")  # parse through file list in the CURRENT directory
