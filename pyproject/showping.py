from http_method import Http
import  json
import requests
from  sql import Mysql
class showping:


    def indexshowping(self,token):
        url='https://hotfix.shuixiongkeji.net/app/MrdGetDailySale'
        headers = {
            "cookie": "token=" + token
        }
        # res=Http.get(url,None,token)
        # resjson=json.loads(res.text)
        res=requests.get(url,headers=headers)
        print(res.json())
        product_id=res.json()['data']['products'][0]['product_id']
        price=res.json()['data']['products'][0]['price']
        id = res.json()['data']['products'][0]['id']# 首页第几个商品，0，1，....
        if(id!=None):
            sql = "SELECT * FROM products WHERE id=%d;" % product_id
        else:
            print('悟空图还没有商品')
        exesql=Mysql().sqlclien(sql)
        businessid=exesql[0][1]
        stock=exesql[0][16]
        if(res.status_code==200):
             return id,product_id,price,businessid,stock
        else:
          print('请求错误'+res.json())
    #我的订单页面
    def showpinginfo(self,id,token):
        url='https://hotfix.shuixiongkeji.net/app/DailySaleDetail?id=%d'%id
        headers = {
             "cookie": "token=" + token
       }
        res=requests.get(url,headers=headers).json()
       # print(res['data']['buy']['attr'])
        daily_sale_id =res['data']['daily_sale_id']
        #default_sku_stock
        #总剩余库存
        total_stock = res['data']['stock']

        if (res['data']['buy']['attr'] == []):
            # 单规格库存
            one_sku_stock = res['data']['buy']['default_sku_stock']
            one__sku_id = res['data']['buy']['default_sku_id']
            return daily_sale_id, one__sku_id, total_stock, one_sku_stock



        else:
            # 多规格库存
            moer_sku_stock = res['data']['buy']['sku'][0]['sku_stock']
            moer_sku_stock_id = res['data']['buy']['sku'][0]['sku_id']
            return daily_sale_id, moer_sku_stock, total_stock, moer_sku_stock_id
