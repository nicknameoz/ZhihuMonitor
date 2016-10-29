#!/usr/bin/env python
# -*- coding: utf-8 -*-

from robobrowser import RoboBrowser
import json
import pdb
import requests
from bs4 import BeautifulSoup

URL_PREFIX = "https://www.zhihu.com"

class Question(object):
    """ Zhihu parser, question obj"""
    def __init__(self, page_url):
        self.url = page_url
        self.browser = RoboBrowser(history=True,user_agent='nemo1')
        self.browser.open(self.url)


    def get_answer_count(self):
        if self.browser.find("h3",id="zh-question-answer-num") != None:
            return int(self.browser.find("h3",id="zh-question-answer-num")["data-num"])

    def get_all_answer_url_list(self):
        results = []
        if self.get_answer_count() <= 10:
            for answer_div in self.browser.find_all("div", class_="zm-item-answer  zm-item-expanded"):
                results.append(URL_PREFIX + answer_div.find("link")["href"])
        else:
            for i in range(0, (self.get_answer_count() / 10) + 1): 
                offset = i * 10
                if i  == 0:
                    for answer_div in self.browser.find_all("div", class_="zm-item-answer  zm-item-expanded"):
                        results.append(URL_PREFIX + answer_div.find("link")["href"])
                    # print results
                else:
                    # pass
                    post_url = "http://www.zhihu.com/node/QuestionAnswerListV2"
                    _xsrf = self.browser.find("input", attrs={'name': '_xsrf'})["value"]
                    params = json.dumps({"url_token": int(self.url[-8:-1] + self.url[-1]), "pagesize": 10, "offset": offset})
                    data = {'_xsrf': _xsrf, 'method': "next", 'params': params}
                    header = {
                        'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
                        'Host': "www.zhihu.com",
                        'Referer': self.url
                    }
                    r = requests.post(post_url, data=data, headers=header, verify=False)
                    answers = r.json()["msg"]
                    # print len(answers)
                    # pdb.set_trace()
                    for ans in answers:
                        soup = BeautifulSoup(ans, 'html.parser')
                        results.append(URL_PREFIX + soup.find("link")["href"])
        return results
        # 点一次加10个，一开始10个 