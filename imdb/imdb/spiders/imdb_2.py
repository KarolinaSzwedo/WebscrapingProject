# -*- coding: utf-8 -*-
import scrapy

class Links(scrapy.Item):
    link = scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'links' # name of the Spider
    allowed_domains = ['imdb.com']
    try:
        # link_list.csv - list with months
        with open("link_list.csv", "rt") as file:
            # read each line from the file without the first one
            start_urls = [url.strip() for url in file.readlines()][1:]
    except:
        start_urls = []

    # call DuplicatesPipelineLinks class from pipelines.py file
    # this will filter duplicated links in coming soon movies
    custom_settings = {'ITEM_PIPELINES': {'imdb.pipelines.DuplicatesPipelineLinks': 300} }

    # get links to coming soon movies
    def parse(self, response):
        # I am using response.css beacuse response.xpath doesn't get all links (problem with $0)
        selection = response.css('td.overview-top > h4 > a::attr(href)')
        for s in selection:
            l = Links()
            l['link'] = 'https://www.imdb.com' + s.get()

            yield l
