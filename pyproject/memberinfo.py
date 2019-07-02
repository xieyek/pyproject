from login import Login
import requests
import json
from datetime import *
from http_method import Http
import math

class member():

    #  Authorization
 def userinfo(self,token):

        url = "https://hotfix.shuixiongkeji.net/app/MrdMemberInfo"
        headers = {
                            "cookie": "token=" + token
                        }
       # res = requests.request("GET",url, headers=headers)
        res = requests.get(url=url,headers=headers)
        resdata=res.json()['data']
       # res=Http.get(url,None,token)
        if (res.status_code==200):
            print('用户信息获取成功：'+ str(resdata) )
            return resdata['id'],resdata['balance'],resdata['agent_level'],resdata['stock'],resdata['rec_member_id'],resdata['member_card_profit'],resdata['current_level_name']

        else:
            print('用户信息获取失败：' + str(res))

 def memberuplv(self):
     c =10000000
     a=[[0,100,1],[101,300,2],[301,1000,3],[1001,2500,4],[2501,5000,5],[5001,15000,6],[15001,25000,7],[25001,40000,8],
        [40001,60000,9],[60001,100000,10],[100001,150000,11],[150001,170000,12],[170001,250000,13],[250001,350000,14],
        [350001,500000,15],[500001,700000,16],[700001,1000000,17],[1000001,2000000,18],[2000001,5000000,19],[5000001,8880000,20]]
     if(c<=8880000):
      for b in a:
        if ( c >= b[0]<= b[1]):
            if(c<=b[1]):
                  print(b[2])
     else:
                print(20)

 def time(self):
    url = 'https://hotfix.shuixiongkeji.net/admin/DailySales?order=desc&orderField=&start_at=2019-6-1&end_at=&page=1&pageSize=15'
    pay=150.00000




    n = 158.00

    print(math.ceil(n))

member().time()



