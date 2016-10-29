#!/usr/bin/env python
# -*- coding: utf-8 -*-

from robobrowser import RoboBrowser

class Author(object):
    def __init__(self,page_url):
       self.url = page_url
       self.answers_url = self.url + "/answers"
       self.followers_url = self.url + "/followers"
       self.followees_url = self.url + "/followees"

       self.browser = RoboBrowser(history=True,user_agent='nemo1')
       self.browser.open(self.url)

    def get_followers_num(self):
        div_tag = browser.find("div", class_="zm-profile-side-following zg-clear")
        return int(div_tag.contents[0].find("strong").get_text())

    