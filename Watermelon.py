from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from openpyxl import load_workbook


class Watermelon_Page(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.title('西瓜')
        self.root.geometry('%dx%d' % (600, 400))  # 设置窗口大小

        self.data_path = '西瓜.xlsx'  # 初始西瓜数据集路径
        self.sheet_index = 0  # 默认获取第1张sheet
        self.header = ('序号', '密度', '含糖率', '是否是好瓜')  # 显示数据的表头

        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()

        # 原始数据显示
        Label(self.page, text="初始样本数据").grid(row=0, sticky=W)
        self.listBox = ttk.Treeview(self.page, height=15, columns=self.header, show='headings')  # 创建表格
        self.VScroll = ttk.Scrollbar(self.page, orient='vertical', command=self.listBox.yview)  # 创建滚动条
        self.listBox.configure(yscrollcommand=self.VScroll.set)  # 滚动条与表格控件关联
        self.VScroll.grid(row=1, column=5, sticky=NS)  # 滚动条放置位置
        for col in self.header:  # 显示表头以及设置列宽
            self.listBox.column(col, width=100, anchor='center')
            self.listBox.heading(col, text=col)
        self.listBox.grid(row=1, column=0, columnspan=4)

        # tempList = self.readDataSet()  # 表格显示初始数据
        # for i, row in enumerate(tempList, start=1):
        #     self.listBox.insert("", "end", values=(i, row[1], row[2], row[3]))

        self.show()  # 表格显示初始数据

        Button(self.page, text='更改文件', width=10, command=self.open_file).grid(row=16, column=0)  # 重新导入数据按钮
        Button(self.page, text="显示", width=10, command=self.show).grid(row=16, column=1)  # 显示当前文件数据的按钮
        Button(self.page, text="关闭", width=10, command=self.page.destroy).grid(row=16, column=2)  # 显示当前文件数据的按钮

    # 读取excel文件函数
    def open_file(self):
        filepath = filedialog.askopenfilename(title='打开Excel文件', filetypes=[('Excel Files', '*.xlsx')])
        if filepath != '':
            self.data_path = filepath
        print(self.data_path)

    # 读取当前文件的数据
    def readDataSet(self):
        content = []  # 存放不包含表头的数据内容
        wb = load_workbook(self.data_path)
        sheet1 = wb.worksheets[self.sheet_index]
        # 迭代读取所有的行
        cnt = 0
        for row in sheet1.rows:
            row_val = [col.value for col in row]
            if cnt == 0:
                pass
            else:
                content.append(row_val)
            cnt = cnt + 1
        print(content)
        return content

    # 显示当前文件的轨道电路数据集
    def show(self):
        self.listBox.delete(*self.listBox.get_children())  # 清空原先表格
        tempList = self.readDataSet()  # 导入当前文件数据
        for i, row in enumerate(tempList, start=1):
            self.listBox.insert("", "end", values=(i, row[1], row[2], row[3]))
