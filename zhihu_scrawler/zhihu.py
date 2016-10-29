#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

root_homepage = "http://m.zhihu.com/people/zhang-jia-wei"
LOWER_BOUND_FOLLOWER_BIG_V = 5000
MAX_BIG_V = 100

big_v_dict = {}
visited = set()

def parse_start():
    r = requests.get(root_homepage)
    parse_homepage(root_homepage, r.text)

def parse_homepage(homepage_url, html_unicode_str):
    soup = BeautifulSoup(html_unicode_str, "html.parser")
    
    # 0 for followee
    followee_tag = soup.find_all("div", "zm-profile-side-following zg-clear")[0].find_all("a")[0] 

    # 1 for follower
    follower_tag = soup.find_all("div", "zm-profile-side-following zg-clear")[0].find_all("a")[1] 

    num_follower = int(follower_tag.find("strong").text)
    if num_follower > LOWER_BOUND_FOLLOWER_BIG_V and homepage_url not in big_v_dict:
        big_v_dict[homepage_url] = num_follower

    followers_url = homepage_url + '/followers' 

    form = {}
    method:next
    params:{"offset":20,"order_by":"created","hash_id":"f9de84865e3e8455a09af78bfe4d1da5"}
    _xsrf:f666abb1119b562a670bdf32e02178c1

    method:next
    params:{"offset":20,"order_by":"created","hash_id":"de1451e4c42a0df4b4235cfa541a1950"}
    _xsrf:f666abb1119b562a670bdf32e02178c1


def get_all_big_name_follower:
    current_queue = # how to init a queue?
    current_queue.add(root)
    while i < 500 and len(current_queue) > 0:
        next_queue = # init a queue again
        for user in current_queue:
            visited.add(user)
            next_queue.add(user.followers)
            if user.followers > LOWER_BOUND_FOLLOWER_BIG_V:
                big_v_dict[user.url] = user.followers
        current_queue = next_queue
        i = i + 1


if __name__ == '__main__':
    parse_start()
