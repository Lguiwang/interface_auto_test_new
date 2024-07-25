import time
import os

# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ui元素对象库config.ini文件所在目录
CONF_PATH = os.path.join(ROOT_DIR, 'config', 'config.ini')
# 测试数据所在目录
DATA_Path = os.path.join(ROOT_DIR, 'data', 'tcData.xlsx')
# 上传文件数据所在目录
upload_data = os.path.join(ROOT_DIR, 'data', f'Upload\\files')
# 上传文件夹数据所在目录
upload_dir = os.path.join(ROOT_DIR, 'data', f'Upload\\folder')
# 测试用例所在目录
cases_dir = os.path.join(ROOT_DIR, 'TestCases')
# 当前时间
CURRENT_TIME = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
# 报告目录
cur_path = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(cur_path, f'Report\\{CURRENT_TIME}')

# 切换被测系统的登录地址
URL = 'http://172.16.60.173:9180/'