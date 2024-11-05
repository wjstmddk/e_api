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

def getdata(username):
    print(username)
    userurl=f'https://open-api.bser.io/v1/user/nickname?query={username}'
    userres=requests.get(userurl, headers=header).json()
    userdf=pd.DataFrame(userres)
    userNum=userdf.user.userNum
    user_url=f'https://open-api.bser.io/v1/user/games/{userNum}'
    usergameres = requests.get(user_url, headers=header).json()
    usergamedf=pd.DataFrame(usergameres)
    gamedata=usergamedf.userGames
    gamelist=gamedata.values
    gamedf=gamelist
    # print(gamedf[0])
    usergames=[]
    for j in range(len(gamedf)):
        insertdf=[]
        insertdf.append(gamedf[j]['gameId']) 
        insertdf.append(gamedf[j]['userNum']) 
        insertdf.append(gamedf[j]['nickname'])
        # insertdf.append(gamedf[j][0]['mmr'])
        insertdf.append(gamedf[j]['matchingMode'])
        insertdf.append(gamedf[j]['seasonId'])
        insertdf.append(gamedf[j]['skinCode'])
        insertdf.append(gamedf[j]['characterLevel'])
        insertdf.append(gamedf[j]['playerKill'])
        insertdf.append(gamedf[j]['playerAssistant'])
        try:insertdf.append(gamedf[j]['equipment']['0'])
        except:insertdf.append(0)
        try:insertdf.append(gamedf[j]['equipment']['1'])
        except:insertdf.append(0)
        try:insertdf.append(gamedf[j]['equipment']['2'])
        except:insertdf.append("none")
        try:insertdf.append(gamedf[j]['equipment']['3'])
        except:insertdf.append("none")
        try:insertdf.append(gamedf[j]['equipment']['4'])
        except:insertdf.append("none")
        insertdf.append(gamedf[j]['serverName'])
        insertdf.append(gamedf[j]['teamNumber'])
        insertdf.append(gamedf[j]['victory'])
        insertdf.append(gamedf[j]['giveUp'])
        insertdf.append(gamedf[j]['killer'])
        try:
            insertdf.append(gamedf[j]['killerCharacter'])
        except:
            insertdf.append("none")
        insertdf.append(gamedf[j]['routeIdOfStart'])
        usergames.append(insertdf)
        column=['gameId','userNum','nickname','matchingMode','seasonId','skinCode','characterLevel','playerKill','playerAssistant','equipment1','equipment2','equipment3','equipment4','equipment5','serverName','teamNumber','victory','giveUp','killer','killerCharacter','routeIdOfStart']
        rdatadf=pd.DataFrame(usergames,columns=column)
        runiquedf = rdatadf.drop_duplicates(subset=['gameId', 'userNum'])
    return usergames
    # print(rdatadf)