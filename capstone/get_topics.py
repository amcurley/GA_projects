# https://stackoverflow.com/questions/58053067/how-to-install-geckodriver-in-mac-terminal-permission-operation-not-permitted
# https://github.com/mozilla/geckodriver/releases

import time
import scrapy
from selenium import webdriver
browser = webdriver.Firefox(executable_path='/Users/aidancurley/Documents/dsir/capstone/geckodriver')


# Innovation and Tech
tech = ['accessibility'
# , 'android-development'
# , 'artificial-intelligence', 'blockchain',
#         'cryptocurrency', 'data-science', 'digital-life', 'gadgets', 'ios-development',
#         'javascript', 'machine-learning', 'math', 'neuroscience', 'programming', 'science',
#         'self-driving-cars', 'software-engineering', 'space', 'technology', 'ux', 'visual-design'
        ]



for n in tech:
    browser.get('https://medium.com/topic/' + str(n))
    post_link = browser.find_element_by_tag_name('h1')
    post_link.click()






# get_link = browser.tag_name('a')
#
# count = 3
# while count > 0 :
#     get_link.click()
#     count -= 1
