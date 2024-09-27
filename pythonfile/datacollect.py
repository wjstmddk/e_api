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
header={'accept': 'application/json','x-api-key': api_key}
engine = create_engine('mysql+pymysql://takealook:tmddk0908@localhost:3308/apidb')
print("setcomplet")
rankdata=f'https://open-api.bser.io/v1/rank/top/27/3'
rankres=requests.get(rankdata,headers=header).json()
rankdf=pd.DataFrame(rankres)
rankuser=pd.DataFrame(rankdf.topRanks)
# time.sleep
print("rankload complet")
for n in range(len(rankuser.topRanks)):
    print("dataload start")
    try:
        print(rankuser.topRanks[n]['nickname'])
        userNum=rankuser.topRanks[n]['userNum']
        user_url=f'https://open-api.bser.io/v1/user/games/{userNum}'
        res = requests.get(user_url, headers=header).json()
        df=pd.DataFrame(res)
        gamedata=df.userGames
        gamedf=pd.DataFrame(gamedata)
        games=gamedf.userGames[0]
        gamesdata=gamedata.values
        datas=[]
        for k in range(len(gamesdata)):
            datas.append(gamesdata[k].values())
        gamedf=pd.DataFrame(datas,columns=gamesdata[9].keys())
        time.sleep(1)   
        gamedatalist=[]
        for a in tqdm(range(len(gamedf.gameId))):
            user_url=f'https://open-api.bser.io/v1/games/{gamedf.gameId[a]}'
            gamedatalist.append(requests.get(user_url, headers=header).json())
            time.sleep(1)
        gamelist=pd.DataFrame(gamedatalist)
        gamelist=gamelist.userGames
        finalgamedf=[]
        for j in range(len(gamelist)):
            for i in range(len(gamelist[j])):
                insertdf=[]
                # print(j,i)
                insertdf.append(gamelist[j][i]['gameId'])
                insertdf.append(gamelist[j][i]['userNum'])
                insertdf.append(gamelist[j][i]['nickname'])
                insertdf.append(gamelist[j][i]['mmrAfter'])
                insertdf.append(gamelist[j][i]['matchingMode'])
                insertdf.append(gamelist[j][i]['seasonId'])
                insertdf.append(gamelist[j][i]['skinCode'])
                insertdf.append(gamelist[j][i]['characterLevel'])
                insertdf.append(gamelist[j][i]['playerKill'])
                insertdf.append(gamelist[j][i]['playerAssistant'])
                insertdf.append(gamelist[j][i]['equipment']['0'])
                insertdf.append(gamelist[j][i]['equipment']['1'])
                insertdf.append(gamelist[j][i]['equipment']['2'])
                insertdf.append(gamelist[j][i]['equipment']['3'])
                insertdf.append(gamelist[j][i]['equipment']['4'])
                insertdf.append(gamelist[j][i]['serverName'])
                insertdf.append(gamelist[j][i]['teamNumber'])
                insertdf.append(gamelist[j][i]['victory'])
                insertdf.append(gamelist[j][i]['giveUp'])
                insertdf.append(gamelist[j][i]['killer'])
                try:
                    insertdf.append(gamelist[j][i]['killerCharacter'])
                except:
                    insertdf.append("none")
                insertdf.append(gamelist[j][i]['routeIdOfStart'])
                finalgamedf.append(insertdf)
            column=['gameId','userNum','nickname','mmrAfter','matchingMode','seasonId','skinCode','characterLevel','playerKill','playerAssistant','equipment1','equipment2','equipment3','equipment4','equipment5','serverName','teamNumber','victory','giveUp','killer','killerCharacter','routeIdOfStart']
            rdatadf=pd.DataFrame(finalgamedf,columns=column)
            runiquedf = rdatadf.drop_duplicates(subset=['gameId', 'userNum'])
            runiquedf.to_sql('e_data', con=engine, if_exists='append', index=False)
            print(len(gamelist))
            print("complet",j,i)
        time.sleep(30)
    except:
        print("error")
        pass
