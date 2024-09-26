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
rankres=requests.get(rankdata,headers=header).json()
rankdf=pd.DataFrame(rankres)
rankuser=pd.DataFrame(rankdf.topRanks)
time.sleep(5)
for i in tqdm(range(len(rankuser.topRanks))):
    userNum=rankuser.topRanks[i]['userNum']
    user_url=f'https://open-api.bser.io/v1/user/games/{userNum}'
    res = requests.get(user_url, headers=header).json()
    df=pd.DataFrame(res)
    gamedata=df.userGames
    gamedf=pd.DataFrame(gamedata)
    games=gamedf.userGames[0]
    gamesdata=gamedata.values
    datas=[]
    for j in range(len(gamesdata)):
        datas.append(gamesdata[j].values())
    gamedf=pd.DataFrame(datas,columns=gamesdata[3].keys())
    time.sleep(1)   

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
        insertdf.append(gamedf.serverName[i])
        insertdf.append(gamedf.teamNumber[i])
        insertdf.append(gamedf.victory[i])
        insertdf.append(gamedf.giveUp[i])
        insertdf.append(gamedf.killer[i])
        insertdf.append(gamedf.killerCharacter[i])
        insertdf.append(gamedf.routeIdOfStart[i])
        insert.append(insertdf)
    column=['gameId','userNum','nickname','mmrAfter','matchingMode','seasonId','skinCode','characterLevel','playerKill','playerAssistant','equipment1','equipment2','equipment3','equipment4','equipment5','serverName','teamNumber','victory','giveUp','killer','killerCharacter','routeIdOfStart']
    rdatadf=pd.DataFrame(insert,columns=column)
    runiquedf = rdatadf.drop_duplicates(subset=['gameId', 'userNum'])
    insert.to_sql('e_data', con=engine, if_exists='append', index=False)
    time.sleep(30)