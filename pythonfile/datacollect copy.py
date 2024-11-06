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
for n in tqdm(range(len(rankuser.topRanks))):
    # print("dataload start")
    try:
        # print(rankuser.topRanks[n]['nickname'])
        userNum=rankuser.topRanks[n]['userNum']
        user_url=f'https://open-api.bser.io/v1/user/games/{userNum}'
        res = requests.get(user_url, headers=header).json()
        df=pd.DataFrame(res)
        gamedata=df.userGames
        gamedf=pd.DataFrame(gamedata)
        games=gamedf.userGames[0]
        gamesdata=gamedata.values
        try:
            while res['userGames'][9]['seasonId']==27:
                # print("n",n)
                next=res['next']
                datas=[]
                for k in range(len(gamesdata)):
                    datas.append(gamesdata[k].values())
                max=0
                for b in range(len(gamesdata)):
                    if(len(gamesdata[max].keys())<len(gamesdata[b].keys())):
                        max=b
                gamedf=pd.DataFrame(datas,columns=gamesdata[max].keys())
                gamelist=gamedf
                # gamedf=gamelist
                # print(gamedf[0])
                usergames=[]
                # print(gamelist)
                finalgamedf=[]
                for j in range(len(gamelist)):
                    # for i in range(len(gamelist[j])):
                    insertdf=[]
                    # print(j,i)
                    insertdf.append(gamelist['gameId'][j])
                    insertdf.append(gamelist['userNum'][j])
                    insertdf.append(gamelist['nickname'][j])
                    try:
                        insertdf.append(gamelist['mmrAfter'][j])
                    except:
                        insertdf.append(0)
                    insertdf.append(gamelist['matchingMode'][j])
                    insertdf.append(gamelist['seasonId'][j])
                    insertdf.append(gamelist['skinCode'][j])
                    insertdf.append(gamelist['characterLevel'][j])
                    insertdf.append(gamelist['playerKill'][j])
                    insertdf.append(gamelist['playerAssistant'][j])
                    try:insertdf.append(gamelist['equipment']['0'][j])
                    except:
                        insertdf.append(0)
                        # print(gamelist['equipment'][j])
                    try:insertdf.append(gamelist['equipment']['1'][j])
                    except:
                        insertdf.append(0)
                    try:insertdf.append(gamelist['equipment']['2'][j])
                    except:
                        insertdf.append(0)
                    try:insertdf.append(gamelist['equipment']['3'][j])
                    except:
                        insertdf.append(0)
                    try:insertdf.append(gamelist['equipment']['4'][j])
                    except:
                        insertdf.append(0)
                    insertdf.append(gamelist['serverName'][j])
                    insertdf.append(gamelist['teamNumber'][j])
                    insertdf.append(gamelist['victory'][j])
                    insertdf.append(gamelist['giveUp'][j])
                    insertdf.append(gamelist['killer'][j])
                    try:
                        insertdf.append(gamelist['killerCharacter'][j])
                    except:
                        insertdf.append("none")
                    insertdf.append(gamelist['routeIdOfStart'][j])
                    finalgamedf.append(insertdf)
                column=['gameId','userNum','nickname','mmrAfter','matchingMode','seasonId','skinCode','characterLevel','playerKill','playerAssistant','equipment1','equipment2','equipment3','equipment4','equipment5','serverName','teamNumber','victory','giveUp','killer','killerCharacter','routeIdOfStart']
                rdatadf=pd.DataFrame(finalgamedf,columns=column)
                runiquedf = rdatadf.drop_duplicates(subset=['gameId', 'userNum'])
                runiquedf.to_sql('e_data', con=engine, if_exists='append', index=False)
                time.sleep(10)
                # print("next", next)
                user_url = f'https://open-api.bser.io/v1/user/games/{userNum}?next={next}'
                res = requests.get(user_url, headers=header).json()
                df = pd.DataFrame(res)
                gamedata = df.userGames
                gamedf = pd.DataFrame(gamedata)
                games = gamedf.userGames[0]
                gamesdata = gamedata.values
                # print(gamesdata)
        except Exception as e:
            print("error",e)
            print("username",rankuser.topRanks[n]['nickname'])
            pass
    except Exception as e:
        print("error",e)
        print("username",rankuser.topRanks[n]['nickname'])
        pass