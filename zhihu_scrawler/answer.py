#!/usr/bin/env python
# -*- coding: utf-8 -*-

from robobrowser import RoboBrowser

class Answer(object):
    """ Zhihu parser, answer obj"""
    def __init__(self, page_url):
        self.url = page_url
        self.ans_browser = RoboBrowser(history=True,user_agent='nemo1')
        self.ans_browser.open(self.url)

    def get_related_question_url(self):
        h2_tag = self.ans_browser.find("h2", class_="zm-item-title")
        return "https://www.zhihu.com" + h2_tag.a["href"]

    def get_related_question_title(self):
        h2_tag = self.ans_browser.find("h2", class_="zm-item-title")
        return h2_tag.a.get_text()


    def get_img_url_list(self):
        content_div = self.ans_browser.find("div", class_="zm-editable-content clearfix")
        results = []
        for img_tag in content_div.find_all("img"):
            if "data-original" in img_tag:
                results.append(img_tag["data-original"])
            elif "src" in img_tag:
                results.append(img_tag["src"])
        return results

    def get_thumbs_up_count(self): 
        div = self.ans_browser.find("div", class_="zm-item-vote-info")
        if div:
            return int(div["data-votecount"])



