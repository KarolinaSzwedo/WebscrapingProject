# -*- coding: utf-8 -*-
import scrapy

class Links(scrapy.Item):
    link = scrapy.Field()

class LinkListSpider(scrapy.Spider):
    name = 'link_list' # name of the Spider
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/movies-coming-soon/']

    def parse(self, response):
        # get links for each month of "coming soon" movies
        xpath = '//select[@class = "sort_field date_select"]/following::option/@value'
        selection = response.xpath(xpath)
        for s in selection:
            l = Links()
            l['link'] = 'https://www.imdb.com' + s.get()

            yield l
