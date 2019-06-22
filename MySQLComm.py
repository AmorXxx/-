# -*- coding: utf-8 -*

"""
author: Amor

finished: 2019-5-30
"""
import pymysql


# 用来操作数据库的类
class MySQLCommand(object):
    # 类的初始化
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306  # 端口号
        self.user = 'root'  # 用户名
        self.password = "www708626"  # 密码
        self.db = "technew_study"  # 库
    # noinspection PyBroadException

    # 链接数据库
    def connectMysql(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                        passwd=self.password, db=self.db, charset='utf8')
            self.cursor = self.conn.cursor()
        except BaseException:
            print('connect mysql error.')

    # 插入数据，插入之前先查询是否存在，如果存在就不再插入
    def insertData(self, my_dict):
        for d in my_dict:
            sqlexist = "SELECT id FROM send_grade  WHERE stu_no = '%s' and course_no = '%s'" % (
                d['stu_no'], d['course_no'])
            res = self.cursor.execute(sqlexist)

            if res:  # res为查询到的数据条数如果大于0就代表数据已经存在
                #数据存在执行更新操作
                try:
                    updsql = """UPDATE send_grade SET score = '%s' WHERE stu_no = '%s' and course_no = '%s'""" % (d['score'], d['stu_no'], d['course_no'])
                    re = self.cursor.execute(updsql)
                    if re:
                            print('Update score successfully!')
                    else:
                            print('Data has not changed')
                except pymysql.Error as e:
                    # 发生错误时回滚
                    self.conn.rollback()
                    print("Update data failed，because %d: %s" % (e.args[0], e.args[1]))
                except pymysql.Error as e:
                    print("DBError，because %d: %s" % (e.args[0], e.args[1]))
                self.conn.commit()


        # 数据不存在才执行下面的插入操作
            else:
                try:
                    sql = """INSERT INTO send_grade VALUES (%d,'%s','%s','%s','%s','%s',%s,'%d')""" % (
                        d['id'], d['stu_no'], d['course_no'], d['score'], d['course_type'],  d['course_name'], d['count'], d['send'])
                    result = self.cursor.execute(sql)
                    insert_id = self.conn.insert_id()  # 插入成功后返回的id
                    self.conn.commit()
                    # 判断是否执行成功
                    if result:
                        print("Inserted successfully! ", insert_id)
                except pymysql.Error as e:
                    # 发生错误时回滚
                    self.conn.rollback()
                    print("Interrupt data failed，because %d: %s" % (e.args[0], e.args[1]))
                except pymysql.Error as e:
                    print("DBError，because %d: %s" % (e.args[0], e.args[1]))
                self.conn.commit()

    def getStuNo(self):
        sql = "SELECT stu_no FROM user"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    def closeMysql(self):
        self.cursor.close()
        self.conn.close()  # 创建数据库操作类的实例
