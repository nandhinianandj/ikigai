# -*- coding: utf-8 -*-
# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.#

#* File Name : pmot_crawler.py
#
#* Purpose :
#
#* Creation Date : 17-01-2023
#
#* Last Modified : Friday 10 February 2023 10:02:05 PM
#
#* Created By : Yaay Nands
#_._._._._._._._._._._._._._._._._._._._._.#

from selenium import webdriver
from selenium.webdriver.common.by import By
chrome = webdriver.Chrome('/home/nands/Downloads/chromium-latest-linux/latest/chrome')
import pdb; pdb.set_trace()
chrome.get('https://www.leadingwithpride.com/')
chrome.find_element(By.CLASS_NAME, value='menuToggle')


#import scrapy
#from scrapy.http import FormRequest, Request
#
#class pmotsSpider(scrapy.Spider):
#    name = "quotes"
#    start_urls = [
#        'https://leadingwithpride.com/',
#    ]
#
#    def start_requests(self):
#        import requests
#        from bs4 import BeautifulSoup
#        login_sess = requests.session()
#        import pdb; pdb.set_trace()
#        res = login_sess.post("https://leadingwithpride.com/login", data={"user": "nandhini.jeyahar@gmail.com",
#                                                                    "password": "Korra@45"})
#        with open('login_res.html', 'w') as f:
#            f.write(res.text)
#        # check login succeed before going on
#        # Just list the PMOTs page and see if we get the table
#        resp = login_sess.get('https://leadingwithpride.com/user/module/180/activity/1')
#        if resp.status_code==302:
#            print("Login failed")
#            return
#        else:
#            pmots_page = BeautifulSoup(resp.text, 'html.parser')
#            rows = pmots_page.find_all('table')
#            with open('test.html', 'w') as f:
#                f.write(pmots_page.prettify())
#            yield rows
#
#
#    def parse(self, response):
#        for quote in response.css('div.quote'):
#            yield {
#                'text': quote.css('span.text::text').get(),
#                'author': quote.css('small.author::text').get(),
#                'tags': quote.css('div.tags a.tag::text').getall(),
#            }
#
#        next_page = response.css('li.next a::attr(href)').get()
#        if next_page is not None:
#            next_page = response.urljoin(next_page)
#            yield scrapy.Request(next_page, callback=self.parse)
