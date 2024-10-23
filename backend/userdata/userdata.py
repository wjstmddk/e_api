import pymysql
import pandas as pd
import requests
from tqdm import tqdm
tqdm.pandas()
import pandas as pd
import random
import time
import numpy as np

api_key='WpHBwNY0OhnyduM02i3Ca2xD9Wv63uI7eHA0imZ2'
header={'accept': 'application/json','x-api-key': api_key}

def getnum(username):
    userurl=f'https://open-api.bser.io/v1/user/nickname?query={username}'
    userres=requests.get(user_url, headers=header).json()
    userdf=pd.dataFrame(userres)
    next=userdf.next[0]
    gamelist=