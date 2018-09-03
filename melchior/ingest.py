#!/usr/bin/env python3

""" run.py: Runs the various components that comprise the Melchior tool """

__author__ = "Drew Hynes"
__copyright__ = "Copyright 2018"
__credits__ = ["Drew Hynes"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Drew Hynes"
__email__ = "drew.hynes@gmail.com"
__status__ = "In Development"

"""
    The idea for now is to have one class per Ingest type, as it expands it may be necessary to move to separate files
"""

import os

class IngestFile(object):

    def loadFile(self, filename):
        if os.path.isfile(filename) == False:
            # cannot find the file
            # need to handle errors better, since this is not a try/catch exceptions
            # dont want to raise cleanly
            print("Failed to find the file:"+filename)
        else:
            # file is there, proceed
            fileSize = os.path.getsize(filename)
            maxFileSize = 1073741824 # this needs to be configuration driven later, currently 1G limit for testing
            if fileSize > maxFileSize:
                print("File is too large!")
            else:
                # file is ok, continue
                file = open(filename, "r")
                fh = file.read()
                file.close()


            pass
        return fh
