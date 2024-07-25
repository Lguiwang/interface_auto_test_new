# -*- coding:utf-8 -*-
"""
======================
    Time  ：2024/7/24 16:59
    Author: Liuguiwang
    File  : ExcelReadMethod2.py.py, 将测试用例的每个字段与表头对应，形成字典，再放入列表中
======================
"""
import os
import xlrd2

from utils.LogUtil import MyLog

log = MyLog().getLog()


# 自定义异常
class SheetTypeError:
    pass


# 验证文件是否存在，存在读取，不存在报错
class ExcelReader:
    def __init__(self, excel_file, sheet_by):
        if os.path.exists(excel_file):
            self.excel_file = excel_file
            self.sheet_by = sheet_by
            self._cases_list = list()
        else:
            raise FileNotFoundError("文件不存在")

    # 读取sheet方式，名称或索引
    def get_all_cases(self):
        # 存在不读取，不存在读取
        if not self._cases_list:
            workbook = xlrd2.open_workbook(self.excel_file)
            if type(self.sheet_by) not in [str, int]:
                raise SheetTypeError("请输入str或int类型数据")
            elif type(self.sheet_by) == int:
                sheet = workbook.sheet_by_index(self.sheet_by)
            elif type(self.sheet_by) == str:
                sheet = workbook.sheet_by_name(self.sheet_by)
            # 获取首行信息
            title = sheet.row_values(0)
            # 遍历测试行，与首行组成Dict,放入list
            # 循环，过滤首行，从1开始
            for row in range(1, sheet.nrows):
                row_value = sheet.row_values(row)
                # 与首行组成字典，放入list
                self._cases_list.append(dict(zip(title, row_value)))
        # 结果返回
        return self._cases_list

if __name__ == '__main__':
    print(ExcelReader(os.path.dirname(os.getcwd()) + '//data//test_excel.xlsx',
                      'Sheet1').get_all_cases())