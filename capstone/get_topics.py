# https://stackoverflow.com/questions/58053067/how-to-install-geckodriver-in-mac-terminal-permission-operation-not-permitted
# https://github.com/mozilla/geckodriver/releases

import time
import scrapy
from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Firefox(executable_path='/Users/aidancurley/Documents/dsir/capstone/geckodriver')


# Innovation and Tech
tech = ['accessibility'
# , 'artificial-intelligence', 'blockchain',
#         'cryptocurrency', 'data-science', 'digital-life', 'gadgets', 'ios-development',
#         'javascript', 'machine-learning', 'math', 'neuroscience', 'programming', 'science',
#         'self-driving-cars', 'software-engineering', 'space', 'technology', 'ux', 'visual-design'
        ]


urls = ['hi']

for n in tech:
    browser.get('https://medium.com/topic/' + str(n))

    # This will get to the part of the website that gets us the link to click to a specific blog
    post_link = browser.find_element_by_tag_name('h1')

    # This finds us the 'a' tag that contains the string of the link
    get_post_link = post_link.find_element_by_tag_name('a')

    # This gets us the exact link we are clicking
    get_post_link = get_post_link.get_attribute('href')

    # Adding the link we are clicking to urls to bring it onto the scraping process
    urls.append(get_post_link)

    # Clicking the link to go to the page
    post_link.click()


print(urls)





# get_link = browser.tag_name('a')
#
# count = 3
# while count > 0 :
#     get_link.click()
#     count -= 1
