import socket
import pymysql
import array

class Mysql():
    sql = 'SELECT * FROM members WHERE mobile=18000000400;'
    # sql服务端配置
    def serverdatabass(self):

        server = socket.socket()
        server.bind('wukong-php-test.rwlb.rds.aliyuncs.com', 3306)
        server.listen(100)
        while True:
            conn, addr = server.accept()
            conn.send("服务器信息".encode())
            print(conn.recv(1024))
        conn.close()

    # 客户端sql配置

    def sqlclien(self,sql):

            conn = pymysql.connect('wukong-php-test.rwlb.rds.aliyuncs.com', 'xieye', "xieye#*&_1237", "wukong_hotfix")
            cur = conn.cursor()
            try:
             cur.execute(sql)
             conn.commit()

            except:
             conn.rollback()
            results = cur.fetchall()
            conn.close()
            cur.close()
            return results



