# encoding:utf-8
"""
@author: 
@time: 
@desc: 获取excel中的数据
"""
from data_processing.operation_excel import OperationExcel
from data import test_data
import settings

class GetData:

    def __init__(self):
        self.operation_excel = OperationExcel(file_path=settings.ALIYUN_CASE_FILE_PATH, sheet_name=settings.ALIYUN_CASE_FILE_SHEET_NAME_1)

    def excel_lines(self):
        """
        获取表格总行数
        :return:
        """
        return self.operation_excel.get_excel_lines()

    def get_case_id(self, row):
        """
        获取case id
        :param row:行号
        :return:
        """
        col = settings.dict_col_name["case_id"]
        return self.operation_excel.get_cell_value(row, col)

    def get_is_run(self, row):
        """
        是否执行该条用例
        :param row:
        :return:
        """
        col = settings.dict_col_name["is_run"]
        is_run = self.operation_excel.get_cell_value(row, col)
        if is_run:
            return is_run
        return None

    def get_header(self, row):
        """
        获取请求头部信息
        :param row:
        :return:
        """
        col = settings.dict_col_name["header"]
        headers = self.operation_excel.get_cell_value(row, col)
        if headers == 'yes':
            return headers
        return None

    def get_request_method(self, row):
        """
        获取请求方式
        :param row:
        :return:
        """
        col = settings.dict_col_name["method"]
        return self.operation_excel.get_cell_value(row, col)

    def get_request_url(self, row):
        """
        获取url
        :param row:
        :return:
        """
        col = settings.dict_col_name["request_url"]
        url_key = self.operation_excel.get_cell_value(row, col)
        if url_key:
            url = test_data.dict_urls[url_key]
            return url, url_key
        return

    def get_request_data(self, row):
        """
        获取测试数据
        :param row:
        :return:
        """
        col = settings.dict_col_name["test_data"]
        data_name = self.operation_excel.get_cell_value(row, col)
        if data_name:
            return test_data.dict_test_data[data_name]
        return

    def get_expected_result(self, row):
        """
        获取预期结果
        :param row:
        :return:
        """
        col = settings.dict_col_name["expected_result"]
        return self.operation_excel.get_cell_value(row, col)

    def write_result(self, row, value):
        """
        写入实际结果
        :param row:
        :param value:
        :return:
        """
        col = settings.dict_col_name["real_result"]
        return self.operation_excel.write_result_value(row, col, value)
