from login import Login
import requests
from showping import showping
from sql import Mysql
class order(object):
    #product_sku_id=9867
   # product_num=1
   # daily_sale_id=228

    # def __init__(self,product_sku_id=product_sku_id,product_num=product_num,daily_sale_id=daily_sale_id):
    #    self.product_sku_id=product_sku_id
    #    self.product_num=product_num
    #    self.daily_sale_id=daily_sale_id
     #  self.token = Login().login()
    def bulidorder(self,token): #创建订单
        product=showping().indexshowping(token)
        product_sku_id=showping().showpinginfo(product[0],token)[1]
        daily_sale_id=showping().showpinginfo(product[0],token)[0]
        url="https://hotfix.shuixiongkeji.net/app/GenerateDailySaleOrder"
        headers = {
            "cookie": "token=" + token
        }
        data={
            'area_code':'110101',
            'product_sku_id':product_sku_id,
            'product_num':1,#购买数量
            'daily_sale_id':daily_sale_id,
            'contacter':'谢冶',
            'province':'北京市',
            'city':'北京市',
            'area':'东城区',
            'address':'Lucie小店区',
            'mobile':'18000000417',
            'remark':'快点发货',
            'freight':"",
            'freight_template_id':'0',
            'is_gift':'0',
            'gift_text':'',
            'selected_order_label_array':'0',
            'product_attr_val_id':'0'
        }
        order=requests.post(url,data=data,headers=headers).json()

        if (order['status'] == 200):
            print('创建成功:' + str(order))
            trade_no = order['data']['trade_no']
            short_no = order['data']['short_no']
            return trade_no, short_no
        else:
            print('创建失败:' + str(order))

    def payorder(self,token,trade_no): #余额支付
    #    print(self.token)
   #     trade_no=self.bulidorder()
        print(trade_no)

        url="https://hotfix.shuixiongkeji.net/app/PayBySystem"
        headers = {
            "cookie": "token=" + token
        }
        data={
            'sense':'5',
            'trade_no':trade_no,
            'password':''
        }
        res=requests.post(url,data=data,headers=headers)
        if(res.json()['status']==200):
         print('支付成功:'+res.text)
        else: print('支付失败:'+res.text)

    def qxzhifuorder(self,token,short_no): #取消已支付订单
        url="https://hotfix.shuixiongkeji.net/app/CancelRetailOrder"
        headers={
            "cookie": "token=" + token
        }
        data={
            'short_no':short_no
        }
        res=requests.post(url,data=data,headers=headers)
        if (res.json()['status'] == 200):
            print('取消成功:' + res.text)
        else:
            print('取消失败:' + res.text)

        #获取自己的订单
    def myorder(self,token,status=0,page=1,keyword='',limit=15): # status -1全部，-2待付款，0待发货，1已发货待收货，4已完成，5已关闭,想要调用发货函数建议0
            url='https://hotfix.shuixiongkeji.net/app/MrdRetailOrder?status={0}&page={1}&keyword={2}&limit={3}'.format(
                status,page,keyword,limit
            )
            headers = {
                "cookie": "token=" + token
            }
            res=requests.get(url,headers=headers).json()
            if(res['data']['data']==[]):
                print('没有数据')
            else:
                # 取到列表第一个商品
                sub_order_id = res['data']['data'][0]['sub_order_id']
                daily_sale_order_short_no = res['data']['data'][0]['daily_sale_order_short_no']
                dailysale_order_price = res['data']['data'][0]['dailysale_order_price']
                sql = 'SELECT * FROM sub_orders WHERE id=%d; ' % sub_order_id
                #order_id
                sql_sub_order_id = Mysql().sqlclien(sql)[0][1]
                threa_order_status = 'SELECT d.status,s.status,o.status FROM daily_sale_orders d LEFT JOIN sub_orders s ON d.order_id=s.order_id LEFT JOIN orders o ON d.order_id=o.id WHERE d.order_id=%d;' % sql_sub_order_id
                order_status_total = Mysql().sqlclien(threa_order_status)
                print('商品信息：' + '订单号： ' + str(daily_sale_order_short_no) + '  ' + '价格; ' + str(
                    dailysale_order_price) + ' ' + 'sub_order_status: ' + str(
                    order_status_total[0][1]) + ' ' + 'daily_sale_orders_status: ' + str(
                    order_status_total[0][0]) + ' ' + 'order_status: ' + str(order_status_total[0][2]))
            return sub_order_id, sql_sub_order_id



     #未支付取消订单
    def nopayquxiao(self,token,trade_no):
        url='https://hotfix.shuixiongkeji.net/app/DailySaleOrderCancel'
        headers = {
            "cookie": "token=" + token
        }
        data = {
            'trade_no': trade_no
        }
        res=requests.post(url,data=data,headers=headers)
        if(res.status_code==200):
            print('未支付取消成功:'+ str(res.json()))
        else:
            print('未支付取消失败:'+ str(res.json()))














