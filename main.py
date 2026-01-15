#!/usr/bin/env python

import odk_clean
import tokens
from datetime import datetime

"""
This script corrects a slight problem that appears with ODK mortality survey entries,
modified through ODK web. Format of several fields was altered when field is saved 
again (even without any changes) once data is already retrieved. It gets wrong format 
for some specific fields. This script corrects these errors, changing the format 
some fields (Id100023 deceased date variable,autocaclucated field ageInDays or field
ageInDays2).
"""

__author__ = "Andreu Bofill"
__copyright__ = "Copyright 2024, ISGlobal Maternal, Child and Reproductive Health"
__credits__ = ["Andreu Bofill"]
__license__ = "MIT"
__version__ = "0.0.1"
__date__ = "20241111"
__maintainer__ = "Andreu Bofill"
__email__ = "andreu.bofill@isglobal.org"
__status__ = "Finished"

if __name__ == '__main__':
    odk_clean.csv_cleaning(tokens.initial_file_path,tokens.final_path)

    print('\nFINISHED.\t',datetime.today())