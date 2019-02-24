#!/usr/bin/python
import sys
import os
from sty import fg
from googleapiclient.discovery import build

key = open(os.path.join(sys.path[0], './key.txt')).read().strip()
service = build('youtube', 'v3', developerKey=key)

pewdiepiesubs = service.channels().list(
    part='statistics',
    id='UC-lHJZR3Gqxm24_Vd_AJ5Yw'
).execute()['items'][0]['statistics']['subscriberCount']

tseriessubs = service.channels().list(
    part='statistics',
    id='UCq-Fj5jknLsUf-MWSy4_brA'
).execute()['items'][0]['statistics']['subscriberCount']

print(fg.magenta + "PewDiePie is at " + str(pewdiepiesubs) + " subs")
print(fg.red + "T-Series is at " + str(tseriessubs) + " subs")
print(fg.white + "Sub gap is " + str(int(pewdiepiesubs) - int(tseriessubs)) + " subs")
