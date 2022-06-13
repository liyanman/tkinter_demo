from tkinter.messagebox import *
import pymysql
from MainPage import *


class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (300, 180))  # 设置窗口大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='账户：').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='密码：').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='登录', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=E)

    def loginCheck(self):
        entry_uname = self.username.get()
        entry_psw = self.password.get()

        db = pymysql.connect(host='localhost', user='root', password='man160038', database='MyDB_one', port=3306)
        cur = db.cursor()  # 获取操作游标
        sql = 'SELECT * FROM user_login'
        flag = True
        # try:
        cur.execute(sql)  # 对用户数据表进行查询
        results = cur.fetchall()  # 获取所有查询数据
        for row in results:
            db_username = row[0]  # 用户名
            db_password = row[1]  # 密码
            # 判断输入的用户名和密码是否匹配
            if db_username == entry_uname and db_password == entry_psw:
                print('登陆成功')
                db_username = row[0]
                self.success_tip(db_username)
                flag = True
                break
            else:
                flag = False
        if flag == False:
            self.fail_tip()
        # except Exception as e:
        #     print('登录异常')

    def success_tip(self, username):
        showinfo(title='消息提示框', message=username + '登录成功')
        self.page.destroy()
        MainPage(self.root)
        # self.root.mainloop()

    def fail_tip(self):
        showerror(title='错误消息框', message='用户名或密码错误')
