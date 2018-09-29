# -*- coding: utf-8 -*-
# @Project : POM_demo 
# @Time    : 2018/5/29 17:36
# @Author  : 
# @File    : database_action.py
# @Software: PyCharm Community Edition
import psycopg2

class PostgreSQL_Connect():
    def __init__(self,database,user,password,host,port='5432'):
        self.database=database
        self.user=user
        self.password=password
        self.host=host
        self.port=port
        try:
            self.conn = psycopg2.connect(database=self.database,
                                    user=self.user,
                                    password=self.password,
                                    host=self.host,
                                    port=self.port)
            print('connect success!')
        except psycopg2.DatabaseError as e:
            exit(e)
        except Exception as e:
            exit(e)

    def executesql(self,sql) ->list:
        __cur=self.conn.cursor()
        __cur.execute(sql)
        __results=__cur.fetchall()
        return __results
    def close_connection(self):
        self.conn.close()
        print('connection closed!')

