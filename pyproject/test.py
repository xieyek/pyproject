#流程测试脚本
from memberinfo import member
from showping import showping
from  order import order
from login import Login
from business import Business
import json

# token=Login().login()
#Bearer
#token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvaG90Zml4LnNodWl4aW9uZ2tlamkubmV0XC9hcHBcL0xvZ2luQnlINSIsImlhdCI6MTU1OTIxNzM5NSwiZXhwIjoxNTU5MjE3OTk1LCJuYmYiOjE1NTkyMTczOTUsImp0aSI6ImtZYTQ0bWdYTk45bHJEYnAiLCJzdWIiOjQwOTA3LCJwcnYiOiI2ZDliZGYzYTkwNTc2YTdhNjJmOGNjNWQyYzViYjZmOGVhY2FkODE3IiwiaWQiOjQwOTA3LCJyb2xlIjoiVVNFUiIsImlzX3VzZXIiOnRydWUsInJvbGVfaWQiOjAsInJlc2V0X3RpbWUiOiIyMDE5LTA1LTA1IDE2OjE3OjEyIiwib3BlbmlkIjoib0hGWEkxQXgydVBLWWFYWXVqSjZpQlR4elVScyIsInRoaXJkX3BhcnRfaWQiOjEzNTkyNH0.cDc6CXnfCXQ9MOf2hdQbDEA4wI6HjIZ0geNff5BULnA'
businesstoken='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvaG90Zml4LnNodWl4aW9uZ2tlamkubmV0XC9CdXNpbmVzc0F1dGhzIiwiaWF0IjoxNTU5MzA5MDE4LCJleHAiOjE1NjA1MTg2MTgsIm5iZiI6MTU1OTMwOTAxOCwianRpIjoiZmNEaUNkR2JoMEdESlJWYyIsInN1YiI6MzUsInBydiI6IjQ4NTA2NTc3M2QxNTAzNGQ0MjU1YWY2MzQwMzFhNGQyYzQyYTU1NGUiLCJpZCI6MzUsInJvbGUiOiJCVVNJTkVTUyIsImFjY291bnRfaWQiOjM1LCJyZXNldF90aW1lIjpudWxsLCJyb2xlX2lkIjozNSwiaXNfYnVzaW5lc3MiOnRydWUsImJ1c2luZXNzX2lkIjozNX0.oQDaZkrjEo-GmAecinSlfWdk8Vr8QUQ5SECy_IM28fM'
# memberinfo=member()
# info=memberinfo.userinfo(token)  #用户信息

# show=showping()
# indexshow=show.indexshowping(token)
# shownoe=show.showpinginfo(indexshow[0],token)
# print(shownoe)

# order=order()
# sub_order_id=order.myorder(token)[0]
# order_id=order.myorder(token)[1]

# bulidorder=order.bulidorder(token) #创建订单
# trade_no=bulidorder[0]
#short_no=bulidorder[1]
#pyorder=order.payorder(token,trade_no) #余额购买
# qxzhifuorder=order.qxzhifuorder(token,short_no) # 取消已支付订单
# s=order.myorder(token)
# s=order.nopayquxiao(token,trade_no)
businessadmin=Business()
#take=businessadmin.takeshoping(businesstoken,my)
# fahuo=businessadmin.fahuo(businesstoken,order_id,sub_order_id)
buildshoping=businessadmin.post_products_keyattr(businesstoken)
