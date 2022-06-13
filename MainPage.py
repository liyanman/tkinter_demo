from view import *
from Watermelon import *


class MainPage(object):
    def __init__(self, master):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (600, 400))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        # 创建不同的界面frame
        self.selectPage = selectPage(self.root)  # 子系统选择界面
        self.window1Page = window1_Frame(self.root)  # 窗口1界面
        self.window2Page = window2_Frame(self.root)  # 窗口2界面
        self.aboutPage = AboutFrame(self.root)  # 关于信息界面

        # 窗口选择界面的按钮布局
        Button(self.selectPage, text='窗口1', font=('Microsoft YaHei', 12), command=self.window1_Disp).grid(stick=E + W)
        Label(self.selectPage).grid(stick=E + W)  # 空一行
        Label(self.selectPage).grid(stick=E + W)  # 空一行
        Button(self.selectPage, text='窗口2', font=('Microsoft YaHei', 12), command=self.window2_Disp).grid(stick=E + W)

        # 窗口1界面的按钮布局
        Button(self.window1Page, text='西瓜数据', font=('Microsoft YaHei', 12), command=self.Watermelon_Disp).grid(
            stick=E + W, padx=10)
        Label(self.window1Page).grid(stick=E + W)  # 空一行
        Label(self.window1Page).grid(stick=E + W)  # 空一行
        Button(self.window1Page, text='返回', font=('Microsoft YaHei', 12), command=self.selcetmodel).grid(stick=E + W,
                                                                                                         padx=10)

        # 窗口2系统界面的按钮布局
        Button(self.window2Page, text='其他界面', font=('Microsoft YaHei', 12)).grid(stick=E + W, padx=10)
        Label(self.window2Page).grid(stick=E + W)  # 空一行
        Label(self.window2Page).grid(stick=E + W)  # 空一行
        Button(self.window2Page, text='返回', font=('Microsoft YaHei', 12), command=self.selcetmodel).grid(stick=E + W,
                                                                                                         padx=10)

        self.selectPage.pack()  # 默认显示诊断子系统选择界面
        menubar = Menu(self.root)
        menubar.add_command(label='窗口选择', command=self.selcetmodel)
        menubar.add_command(label='窗口1', command=self.window1_Disp)
        menubar.add_command(label='窗口2', command=self.window2_Disp)
        menubar.add_command(label='关于', command=self.about_Disp)
        self.root['menu'] = menubar  # 设置菜单栏

    def selcetmodel(self):
        self.selectPage.pack()
        self.window1Page.pack_forget()
        self.window2Page.pack_forget()
        self.aboutPage.pack_forget()

    def window1_Disp(self):
        self.selectPage.pack_forget()
        self.window1Page.pack()
        self.window2Page.pack_forget()
        self.aboutPage.pack_forget()

    def window2_Disp(self):
        self.selectPage.pack_forget()
        self.window1Page.pack_forget()
        self.window2Page.pack()
        self.aboutPage.pack_forget()

    def about_Disp(self):
        self.selectPage.pack_forget()
        self.window1Page.pack_forget()
        self.window2Page.pack_forget()
        self.aboutPage.pack()

    def Watermelon_Disp(self):  # FDT界面显示
        self.subroot = Tk()  # 定义子窗口root
        Watermelon_Page(self.subroot)
