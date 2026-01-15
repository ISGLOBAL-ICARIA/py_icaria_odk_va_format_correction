#!/usr/bin/env python

import odk_clean
import tokens
from datetime import datetime

"""
We detected a problem when editing ODK entries dates, that gets wrong format 
for those edited ODK entries. This script corrects these rerors, changing the
format of Id100023 deceased date variable and the autocaclucated field ageInDays.
The field ageInDays2 is set as empty too.
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