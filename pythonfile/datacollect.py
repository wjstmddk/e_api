import pymysql
import pandas as pd
import requests
from tqdm import tqdm
tqdm.pandas()
import pandas as pd
import random
import time
import numpy as np
from sqlalchemy import create_engine, text
api_key='WpHBwNY0OhnyduM02i3Ca2xD9Wv63uI7eHA0imZ2'
nickname='sdkk003'
header={'accept': 'application/json','x-api-key': api_key}
engine = create_engine('mysql+pymysql://takealook:tmddk0908@localhost:3308/apidb')
rankdata=f'https://open-api.bser.io/v1/rank/top/27/3'
for i in range 
username=f'https://open-api.bser.io/v1/user/nickname?query={nickname}'
userinfo=requests.get(username,headers=header).json()
userdf=pd.DataFrame(userinfo)
userNum=userdf.user.userNum
user_url=f'https://open-api.bser.io/v1/user/games/{userNum}'
res = requests.get(user_url, headers=header).json()
df=pd.DataFrame(res)
gamedata=df.userGames
gamedf=pd.DataFrame(gamedata)
games=gamedf.userGames[0]
gamesdata=gamedata.values
datas=[]
for i in range(len(gamesdata)):
    datas.append(gamesdata[i].values())
gamedf=pd.DataFrame(datas,columns=gamesdata[3].keys())
time.sleep(1)   
gamedatalist=[]
for j in tqdm(range(len(gamedf.gameId))):
    user_url=f'https://open-api.bser.io/v1/games/{gamedf.gameId[j]}'
    gamedatalist.append(requests.get(user_url, headers=header).json())
    time.sleep(1)
gamelist=pd.DataFrame(gamedatalist)
gamelist=gamelist.userGames
insert=[]
for i in range(len(gamedf)):
    insertdf=[]
    insertdf.append(gamedf.gameId[i])
    insertdf.append(gamedf.nickname[i])
    insertdf.append(gamedf.mmrAfter[i])
    insertdf.append(gamedf.matchingMode[i])
    insertdf.append(gamedf.seasonId[i])
    insertdf.append(gamedf.skinCode[i])
    insertdf.append(gamedf.characterLevel[i])
    insertdf.append(gamedf.playerKill[i])
    insertdf.append(gamedf.playerAssistant[i])
    insertdf.append(gamedf.equipment[i]['0'])
    insertdf.append(gamedf.equipment[i]['1'])
    insertdf.append(gamedf.equipment[i]['2'])
    insertdf.append(gamedf.equipment[i]['3'])
    insertdf.append(gamedf.equipment[i]['4'])
    # insertdf.append(gamedf.skillLevelInfo)
    insertdf.append(gamedf.serverName[i])
    insertdf.append(gamedf.teamNumber[i])
    insertdf.append(gamedf.victory[i])
    insertdf.append(gamedf.giveUp[i])
    insertdf.append(gamedf.killer[i])
    insertdf.append(gamedf.killerCharacter[i])
    insert.append(insertdf)
column=['gameId','nickname','mmrAfter','matchingMode','seasonId','skinCode','characterLevel','playerKill','playerAssistant','equipment1','equipment2','equipment3','equipment4','equipment5','serverName','teamNumber','victory','giveUp','killer','killerCharacter']
insert=pd.DataFrame(insert,columns=column)