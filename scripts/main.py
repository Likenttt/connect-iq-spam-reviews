# -*- coding: UTF-8 -*-
import argparse
from connect_iq_operations import get_html_text_from_url, get_single_page_review_json_using_bs4, analyse_remote_reviews_data, analyse_local_reviews_data, get_multi_page_review_json_using_bs4


import os

os.environ["http_proxy"] = ''
os.environ["https_proxy"] = ''
print(os.environ["http_proxy"])
print(os.environ["http_proxy"])

# get_occurance_of_some_keyword(
#     '', 'https://apps.garmin.cn/en-US/apps/a24870e3-b1ea-40a4-aea9-655cdf1d3ee2')

# 下载json评论数据
# get_multi_page_review_json_using_bs4(
#     'https://apps.garmin.cn/en-US/apps/6c5b540e-32f3-40b3-9913-9ba196739fab')
# analyse_local_reviews_data(os.path.join(os.getcwd(),
#                                         '2022_11_27_Quatro 中文版_23194_1580.json'))
# analyse_local_reviews_data(os.path.join(os.getcwd(),
#                                         '2022_11_27_GRun中文版_62278_208.json'))
# 离线分析数据
# analyse_local_reviews_data(os.path.join(os.getcwd(),
#                                         '2022_11_27_动感世界_24352_676.json'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # https://apps.garmin.cn/zh-CN/apps/dc6ceca8-6ec6-49f2-b711-4ebc0d347177
    parser.add_argument(
        "app_url", help="e.g. https://apps.garmin.cn/en-US/apps/02d16e10-84dc-46aa-8edb-c42834c9b907")
    options = parser.parse_args()
    analyse_remote_reviews_data(options.app_url)
