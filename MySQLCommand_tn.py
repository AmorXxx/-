import pymysql


# 用来操作数据库的类
class MySQLCommand(object):
    # 类的初始化
    def __init__(self):
        self.host = 'http://39.107.114.21'
        self.port = 3306  # 端口号
        self.user = 'root'  # 用户名
        self.password = "9f0842a42589d71a"  # 密码
        self.db = "JGH"  # 库
        self.tableid = "jiaogonghao"

    # 链接数据库
    def connectMysql(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                        passwd=self.password, db=self.db, charset='utf8')
            self.cursor = self.conn.cursor()
        except BaseException:
            print('connect mysql error.')

    def closeMysql(self):
        self.cursor.close()
        self.conn.close()  # 创建数据库操作类的实例

    def insertData(self, tid):

        try:
            sql = "INSERT INTO `JGH`.`jiaogonghao` (`id`, `jg-id`) VALUES ('0', %s)"%tid
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
