# -*- coding: UTF-8 -*-

import regex
import re
import argparse
import os
import requests

from bs4 import BeautifulSoup
import json
from datetime import datetime


def get_app_info_tuple_using_bs4(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    app_name = soup.find(
        'h1', attrs={'class': 'media-heading h2'}).get_text()
    downloads = soup.find(
        'span', attrs={'class': 'stat-adds'}).find('span', {'class': ''}).get_text()
    reviews_cnt = soup.find('a', attrs={'id': 'activateReviewsTab'}).find(
        'span', attrs={'class': 'badge'}).get_text()
    print('App:{} downloads:{} reviews count: {} '.format(
        app_name, downloads, reviews_cnt))
    return app_name, downloads, reviews_cnt


def write_file(file, data):
    with open(file, 'w+', encoding='UTF-8') as f:
        f.write(data)
        f.close()


def get_multi_page_review_json_using_bs4(app_url):
    initial_html = get_html_text_from_url(app_url)
    pagination_url_template = '{}?tab=reviews&criteria=createdDate&ascending=false&displayCurrentVersion=false&start={}'
    app_name, downloads, reviews_cnt = get_app_info_tuple_using_bs4(
        initial_html)
    reviews = get_single_page_review_json_using_bs4(
        initial_html)  # the first page
    page_cnt = int(int(reviews_cnt) / 25)
    for i in range(1, page_cnt):
        pagination_url = pagination_url_template.format(app_url, i * 25)
        html_text = get_html_text_from_url(pagination_url)
        # the first page
        try:
            page_i_review = get_single_page_review_json_using_bs4(html_text)
            print("review at page:{} is:{}".format(i+1, page_i_review))
            reviews.extend(page_i_review)
        except:
            print("An exception occurred at page:{} using url:{}".format(
                i + 1, pagination_url))
    date = datetime.now().strftime("%Y_%m_%d")
    pwd = os.getcwd()
    filename = '{}_{}_{}_{}.json'.format(date, app_name,
                                         downloads, reviews_cnt)
    path = os.path.join(pwd, filename)
    write_file(path, json.dumps(reviews, indent=2, ensure_ascii=False))
    return path


def read_file(file):
    with open(file, encoding='UTF-8') as f:
        read_all = f.read()
        f.close()
    return read_all


def load_json(path):
    f = open(path, encoding='UTF-8')
    jsonInfo = json.load(f)
    f.close()
    return jsonInfo


def analyse_remote_reviews_data(app_url):
    filepath = get_multi_page_review_json_using_bs4(app_url)
    analyse_local_reviews_data(filepath)


def analyse_local_reviews_data(path):
    reviews = load_json(path)
    analyse_reviews_data(reviews)


def analyse_reviews_data(reviews):
    user_review_times_dict = {}  # record per user comment times
    comment_dict = {}
    comment_date_dict = {}

    for review in reviews:
        review_user = review['user_name']
        if review_user in user_review_times_dict.keys():
            user_review_times_dict[review_user] = user_review_times_dict[review_user] + 1
        else:
            user_review_times_dict[review_user] = 1

        review_content = review['content']

        if review_content in comment_dict.keys():
            comment_dict[review_content] = comment_dict[review_content] + 1
        else:
            comment_dict[review_content] = 1

        review_date = review['date']

        if review_date in comment_date_dict.keys():
            comment_date_dict[review_date] = comment_date_dict[review_date] + 1
        else:
            comment_date_dict[review_date] = 1

    sorted_user_review_times_dict = sorted(
        user_review_times_dict.items(), key=lambda x: x[1], reverse=True)
    converted_user_review_times_dict = dict(sorted_user_review_times_dict)

    sorted_comment_dict = sorted(
        comment_dict.items(), key=lambda x: x[1], reverse=True)
    converted_sorted_comment_dict = dict(sorted_comment_dict)

    sorted_comment_date_dict = sorted(
        comment_date_dict.items(), key=lambda x: x[1], reverse=True)
    converted_comment_date_dict = dict(sorted_comment_date_dict)

    print('------------------------日期评论次数排名----------------------------')
    hasMoreThan3CommentsPerday = False
    for k, v in converted_comment_date_dict.items():
        if int(v) >= 3:
            hasMoreThan3CommentsPerday = True
            print("{}  \t产生了:{}条评论".format(k.split('|')[0], v))
    if not hasMoreThan3CommentsPerday:
        print('竟然没有一天内超过三条评论')

    hasMoreThan3CommentsPerday = False

    print('---------------------“狂热粉丝”排行榜 这得多爱你才能浪费生命写这么多评价-------------------------------')

    for k, v in converted_user_review_times_dict.items():
        if int(v) > 3:
            hasMoreThan3CommentsPerday = True
            print("「{}」\t累计评价 \t「{}」次 ".format(k, v))

    if not hasMoreThan3CommentsPerday:
        print('竟然没有一位粉丝评论超过3次')
    hasMoreThan3CommentsPerday = False

    print('-----------------------重复垃圾评论,真有你的-----------------------------')

    for k, v in converted_sorted_comment_dict.items():
        if int(v) > 3:
            hasMoreThan3CommentsPerday = True
            print("出现「{}」次的评论:「{}」".format(v, k))
    if not hasMoreThan3CommentsPerday:
        print('竟然没有重复垃圾评论')


def get_single_page_review_json_using_bs4(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    reviews = soup.findAll('div', attrs={'class': 'review'})
    reviews_array = []
    for review in reviews:
        reviews_dict = {}
        rating = review.find(
            'span', {'class': 'rating top-xs'})
        pTags = review.findAll('p')
        for pTag in pTags:
            comment_user_name_may_none = pTag.find('strong')
            if comment_user_name_may_none:
                reviews_dict['user_name'] = comment_user_name_may_none.get_text()
                reviews_dict['date'] = pTag.find(
                    'small').get_text()

            else:
                reviews_dict['content'] = pTag.get_text(
                ).replace('\n', '').replace('\t', '')
                reviews_dict['id'] = pTag.find(
                    'a', attrs={'id': 'flagInappropriateId'}).get('href')
        reviews_dict['star'] = rating.get('title')
        reviews_array.append(reviews_dict)
    return reviews_array


# badge_pattern like CIQ_Store_downloads-{}-green
def replace_readme_comments(file_name, badge_pattern, downloads):
    with open(file_name, "r+") as f:
        text = f.read()
        badge_pattern_regex = badge_pattern.format('\\d{1,10}')
        # regrex sub from github readme comments
        text = re.sub(badge_pattern_regex,
                      badge_pattern.format(downloads),
                      text,
                      flags=re.DOTALL,
                      )
        f.seek(0)
        f.write(text)
        f.truncate()


def extract_downloads_from_html(html_text):
    searchObj = regex.search(r'[^><]+(?<=\d+)(?=<\/span>)', html_text)
    assert searchObj, 'Nothing found!!'
    return searchObj[0]


def extract_app_name_from_html(html_text):
    searchObj = regex.search(r'[^><]+(?<=\d+)(?=<\/span>)', html_text)
    assert searchObj, 'Nothing found!!'
    return searchObj[0]


def get_developers_app_total_downloads(developer_id):
    developer_home_page_url = 'https://apps.garmin.com/en-US/developer/{}/apps'.format(
        developer_id)
    html_text = get_html_text_from_url(developer_home_page_url)
    apps_uri_set = extract_app_url_from_homepage(html_text)
    count = 0
    for uri in apps_uri_set:
        if uri is not None:
            ciq_download_intl = get_downloads_from_url(
                'https://apps.garmin.com' + uri)
            ciq_download_china = get_downloads_from_url(
                'https://apps.garmin.cn' + uri)
            if ciq_download_intl and ciq_download_china:
                downloads = int(ciq_download_intl) + int(ciq_download_china)
                count += downloads

    print('result is:{}'.format(count))
    return count


def get_html_text_from_url(url):
    print('requesting {}'.format(url))
    res = requests.get(url)
    res.encoding = 'utf-8'

    html_text = res.text
    print('html text is \n {}'.format(html_text))
    return html_text  # .decode('utf-8')


def get_downloads_from_url(url):
    html_text = get_html_text_from_url(url)
    return extract_downloads_from_html(html_text)


def get_app_info(html_text):
    app_name = extract_app_name_from_html(html_text)
    downloads = extract_downloads_from_html(html_text)


def main(ciq_id, badge_pattern, readme_file_name):
    ciq_download_intl = get_downloads_from_url(
        'https://apps.garmin.com/zh-CN/apps/' + ciq_id)
    ciq_download_china = get_downloads_from_url(
        'https://apps.garmin.cn/zh-CN/apps/' + ciq_id)
    if ciq_download_intl and ciq_download_china:
        downloads = int(ciq_download_intl) + int(ciq_download_china)
        print('app download is {}'.format(downloads))
        replace_readme_comments(readme_file_name, badge_pattern, downloads)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # https://apps.garmin.cn/zh-CN/apps/dc6ceca8-6ec6-49f2-b711-4ebc0d347177
    parser.add_argument("ciq_id", help="ciq_id")
    parser.add_argument("badge_pattern", help="badge_pattern")
    parser.add_argument("readme_file_name", help="readme_file_name")

    options = parser.parse_args()
    main(options.ciq_id, options.badge_pattern, options.readme_file_name)