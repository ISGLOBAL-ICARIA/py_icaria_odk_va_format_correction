from datetime import datetime
import pandas as pd
from pyodk.client import Client

def csv_cleaning(file_path, final_path):
    """
    We detected a problem when editing ODK entries dates, that gets wrong format
    for those edited ODK entries. This script corrects these rerors, changing the
    format of Id100023 deceased date variable and the autocaclucated field ageInDays.
    The field ageInDays2 is set as empty too.

    :return: csv file with the corrected format
    """

    print(str(datetime.now())+"CLEANING FORMAT FOR THOSE EDITED ODK ENTRIES")
    df = pd.read_csv(file_path)
    affected_df,norm = [],[]
    for k, el in df.T.items():
        try:
            if len(el['consented-deceased_CRVS-info_on_deceased-Id10023']) != 24 and len(el['consented-deceased_CRVS-info_on_deceased-Id10021']) > 4:
                affected_df.append(True)
                norm.append(False)
            else:
                affected_df.append(False)
                norm.append(True)
        except:
            affected_df.append(False)
            norm.append(True)
    new_df = pd.DataFrame(columns=df.columns)
    for k, el in df[affected_df].T.items():
        born_date = datetime.strptime(el['consented-deceased_CRVS-info_on_deceased-Id10021'], '%Y-%m-%d')
        list_affected = []
        for c,l in el.items():
            if c == 'consented-deceased_CRVS-info_on_deceased-Id10023':
                deceased_date = datetime.strptime(l, '%Y-%m-%d')
                id10023 = l + str('T00:00:00.000Z')
                list_affected.append(id10023)
            elif c == 'consented-deceased_CRVS-info_on_deceased-ageInDays':
                ageInDays = deceased_date - born_date
                ageInDays = ageInDays.days
                list_affected.append(ageInDays)
            elif c == 'consented-deceased_CRVS-info_on_deceased-ageInDays2':
                ageInDays2 = ''
                list_affected.append(ageInDays2)
            else:
                list_affected.append(l)
        new_df.loc[len(new_df)] = list_affected

    final_df = pd.concat([df[norm],new_df])
    final_df.to_csv(final_path,index=False)
    print(str(datetime.now())+" FINISHED .")
