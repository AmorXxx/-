import pymysql


# 用来操作数据库的类
class MySQLCommand(object):
    # 类的初始化
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306  # 端口号
        self.user = 'root'  # 用户名
        self.password = "www708626"  # 密码
        self.db = "jiaowuwang"  # 库
        self.table_s = "student"  # 表
        self.table_t = "teacher"
        self.tableid = "jiaogonghao"

    # 链接数据库
    def connectMysql(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                        passwd=self.password, db=self.db, charset='utf8')
            self.cursor = self.conn.cursor()
        except BaseException:
            print('connect mysql error.')

    # 插入数据，插入之前先查询是否存在，如果存在就不再插入
    def insertData_s(self, my_dict):
        table = "student"  # 要操作的表格
        # 注意，这里查询的sql语句url=' %s '中%s的前后要有空格
        sqlExit = "SELECT id FROM student  WHERE idcard = ' %s '" % (
            my_dict['idcard'])
        res = self.cursor.execute(sqlExit)
        if res:  # res为查询到的数据条数如果大于0就代表数据已经存在
            print("数据已存在")
            return 0
        # 数据不存在才执行下面的插入操作
        try:
            cols = ', '.join(my_dict.keys())  # 用，分割
            values = '"," '.join(my_dict.values())
            sql = "INSERT INTO student (%s) VALUES (%s)" % (
                cols, '"' + values + '"')
            # 拼装后的sql如下
            # INSERT INTO home_list (img_path, url, id, title) VALUES
            # ("https://img.huxiucdn.com.jpg"," https://www.huxiu.com90.html","
            # 12"," ")
            try:
                result = self.cursor.execute(sql)
                insert_id = self.conn.insert_id()  # 插入成功后返回的id
                self.conn.commit()
                # 判断是否执行成功
                if result:
                    print("插入成功", insert_id)
                    return insert_id + 1
            except pymysql.Error as e:
                # 发生错误时回滚
                self.conn.rollback()
                # 主键唯一，无法插入
                if "key 'PRIMARY'" in e.args[1]:
                    print("数据已存在，未插入数据")
                else:
                    print("插入数据失败，原因 %d: %s" % (e.args[0], e.args[1]))
        except pymysql.Error as e:
            print("数据库错误，原因%d: %s" % (e.args[0], e.args[1]))

    def insertData_t(self, my_dict):
        table = "teacher"  # 要操作的表格
        # 注意，这里查询的sql语句url=' %s '中%s的前后要有空格
        sqlExit = "SELECT idcard FROM teacher  WHERE idcard = ' %s '" % (
            my_dict['idcard'])
        res = self.cursor.execute(sqlExit)

        if res:  # res为查询到的数据条数如果大于0就代表数据已经存在
            print("数据已存在")
            return 0
        # 数据不存在才执行下面的插入操作
        try:
            cols = ', '.join(my_dict.keys())  # 用，分割
            values = '"," '.join(my_dict.values())
            sql = "INSERT INTO teacher (%s) VALUES (%s)" % (
                cols, '"' + values + '"')
            try:
                result = self.cursor.execute(sql)
                insert_id = self.conn.insert_id()  # 插入成功后返回的id
                self.conn.commit()
                # 判断是否执行成功
                if result:
                    print("插入成功", insert_id)
                    return insert_id + 1
            except pymysql.Error as e:
                # 发生错误时回滚
                self.conn.rollback()
                # 主键唯一，无法插入
                if "key 'PRIMARY'" in e.args[1]:
                    print("数据已存在，未插入数据")
                else:
                    print("插入数据失败，原因 %d: %s" % (e.args[0], e.args[1]))
        except pymysql.Error as e:
            print("数据库错误，原因%d: %s" % (e.args[0], e.args[1]))

    # 查询最后一条数据的id值
    def getLastId_s(self):
        sql = "SELECT max(id) FROM " + self.table_s
        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchone()  # 获取查询到的第一条数据
            if row[0]:
                return row[0]  # 返回最后一条数据的id
            else:
                return 0  # 如果表格为空就返回0
        except BaseException:
            print(sql + ' execute failed.')

    def getLastId_t(self):
        sql = "SELECT max(id) FROM " + self.table_t
        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchone()  # 获取查询到的第一条数据
            if row[0]:
                return row[0]  # 返回最后一条数据的id
            else:
                return 0  # 如果表格为空就返回0
        except BaseException:
            print(sql + ' execute failed.')

    def closeMysql(self):
        self.cursor.close()
        self.conn.close()  # 创建数据库操作类的实例

    def insertData_id(self, id):

        try:
            sql = "INSERT INTO jiaogonghao  VALUES (%s)" % (id)
            try:
                result = self.cursor.execute(sql)
                self.conn.commit()
                # 判断是否执行成功
                if result:
                    print("插入成功")

            except pymysql.Error as e:
                # 发生错误时回滚
                self.conn.rollback()
                # 主键唯一，无法插入
                if "key 'PRIMARY'" in e.args[1]:
                    print("数据已存在，未插入数据")
                else:
                    print("插入数据失败，原因 %d: %s" % (e.args[0], e.args[1]))
        except pymysql.Error as e:
            print("数据库错误，原因%d: %s" % (e.args[0], e.args[1]))
