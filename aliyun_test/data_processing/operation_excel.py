# encoding:utf-8
"""
@author: 
@time: 
@desc: 操作Excel文件
"""
import settings
import xlrd
import xlutils.copy


class OperationExcel:
    def __init__(self, file_path=None, sheet_name=None):
        if not all([file_path, sheet_name]):
            self.file_path = settings.PROJECT_PATH + 'data/aliyun_test_case.xlsx'
            self.sheet_name = 'Sheet1'
        else:
            self.file_path = file_path
            self.sheet_name = sheet_name
        self.data = self.open_excel()

    def open_excel(self):
        """
        读取文件
        :return:
        """
        return xlrd.open_workbook(self.file_path).sheet_by_name(self.sheet_name)

    def get_excel_lines(self):
        """
        获取行数
        :return:
        """
        return self.data.nrows

    def get_excel_rows(self):
        """
        获取列数
        :return:
        """
        return self.data.ncols

    def get_cell_value(self, row, col):
        """
        获取指定行和列的内容
        :param row: 行号
        :param col: 列号
        :return:
        """
        # print(self.data)
        # return self.data.table.row(row)[col].value
        return self.data.cell_value(row, col)

    def write_result_value(self, row, col, value):
        """
        向aliyun_test_case.xlsx表格中写入实际结果
        :return:
        """
        read_data = xlrd.open_workbook(self.file_path)
        write_data = xlutils.copy.copy(read_data)
        sheet_data = write_data.get_sheet(settings.ALIYUN_CASE_FILE_SHEET_INDEX_1)
        sheet_data.write(row, col, value)
        write_data.save(self.file_path)



