import json

import requests
import pytest
from com.common import TestCom
from com.file_tools import FileTools
from com.logger import logger


class TestArt(TestCom):
    art_data = FileTools().excel_file("../data/test_art.xlsx", "Sheet1")

    @pytest.mark.parametrize("case_id,res_method,url_path,art_body,status_code,msg,is_run", art_data)
    def test_art(self, case_id, res_method, url_path, art_body, status_code, msg, is_run):
        if is_run == "是":  # 只执行标记“是”的用例
            res_url = self.base_url + url_path

            r_art = self.request(method=res_method, url=res_url, data=json.loads(art_body))
            if r_art.status_code == status_code and r_art.json()["error_description"] == json.loads(msg)[
                "error_description"]:  # 使用if…else做断言
                real_result = "Pass"
            else:
                real_result = "Fail"
            # 保存填写测试结果后的Excel文件
            FileTools().write_excel("../data/test_art.xlsx", case_id, real_result)


if __name__ == '__main__':
    pytest.main(["-sv", "test_art.py"])
