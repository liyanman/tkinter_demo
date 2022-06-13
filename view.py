from tkinter import *


class selectPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.createPage()

    def createPage(self):
        Label(self).grid(row=0, stick=E + W)  # 空一行
        Label(self, text='欢迎您', font=('Microsoft YaHei', 14)).grid(row=1, stick=E + W)
        Label(self).grid(row=2, stick=E + W)  # 空一行
        Label(self).grid(row=3, stick=E + W)  # 空一行



class window1_Frame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.root = master
        self.createPage()

    def createPage(self):
        Label(self).grid(stick=E + W)  # 空一行
        Label(self, text='欢迎来到窗口1', font=('Microsoft YaHei', 10)).grid(stick=E + W)
        Label(self).grid(stick=E + W)  # 空一行
        Label(self).grid( stick=E + W)  # 空一行


class window2_Frame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()

    def createPage(self):
        Label(self).grid(stick=E + W)  # 空一行
        Label(self, text='欢迎来到窗口2', font=('Microsoft YaHei', 10)).grid(stick=E + W)
        Label(self).grid( stick=E + W)  # 空一行
        Label(self).grid(stick=E + W)  # 空一行


class AboutFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()

    def createPage(self):
        Label(self).pack()  # 空一行
        Label(self, text='关于界面').pack()
        Label(self).pack()  # 空一行
        Label(self, text='xxxxxxx系统').pack()
        Label(self).pack()  # 空一行
        Label(self, text='锂盐块').pack()
        Label(self).pack()  # 空一行
        Label(self, text='2022年6月').pack()
