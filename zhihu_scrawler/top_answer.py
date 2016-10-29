#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 抓取一个问题下的所有图片
# 抓取一个话题
# 抓取用户
# 如果出错怎么办

from robobrowser import RoboBrowser
import re
import pdb
import os

TOP_ANSWER_URL = 'https://www.zhihu.com/topic/19551388/top-answers?page=%s'
write_dir = "/Users/nemo/Pictures/zhihu"
answer_list_url = "/Users/nemo/Pictures/zhihu/answer_list_url.txt"
# title_set = set()

def parse_page(page_url):
    browser.open(page_url)
    # print browser.parsed.title
    
    # get the title of the topic
    topic_tag = browser.find(class_="zm-editable-content")
    
    print topic_tag.get_text().encode('utf-8')

    answer_list = browser.find_all("div", class_="feed-item feed-item-hook folding")
    for answer in answer_list:
        answer_url = answer.link['href']
        answer_url = "https://www.zhihu.com" + answer_url
        parse_answer_page(answer_url)
        # print answer_url

def parse_answer_page(page_url):
    ans_browser = RoboBrowser(history=True,user_agent='nemo1')
    ans_browser.open(page_url)
    title = ans_browser.find(class_="zm-item-title").a
    # pdb.set_trace()
    title_text = title.get_text()
    print title_text.encode('utf-8')
    title_id = title["href"].split("/")[-1]
    directory = "/Users/nemo/Pictures/zhihu/" + title_text
    if not os.path.exists(directory):
        os.makedirs(directory)
        with open(directory + "/url_record.txt", "a") as output:
            output.write(page_url + "\n")

    content_div = ans_browser.find("div", class_="zm-editable-content clearfix")
    count = 0
    for img_tag in content_div.find_all("img"):
        count = count + 1
        try:
            img_src_url = img_tag["data-original"]
            print count, img_src_url
        except:
            pdb.set_trace()
            print "No data original " + img_tag
            continue
        # br_t = RoboBrowser(history=True,user_agent='nemo1')
        # br_t.open(img_src_url)
        # content = br_t.response.content
        # img_file_write_to_path = directory + "/" + img_src_url.split("/")[-1]
        # with open(img_file_write_to_path, "wb") as output:
        #     output.write(content)
        # pdb.set_trace()
    



if __name__ == '__main__':
    browser = RoboBrowser(history=True,user_agent='nemo')
    # with open(answer_list_url, 'r') as f:
        # for line in f:

    # for i in range(1,51):
    #     answer_url = TOP_ANSWER_URL % str(i)  
    #     # print answer_url
    #     parse_page(answer_url)
    parse_page(TOP_ANSWER_URL % str(1))
        
