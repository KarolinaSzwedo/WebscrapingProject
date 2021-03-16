# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class Movie(scrapy.Item):
    # define all items to scrape
    title       = scrapy.Field()
    genres      = scrapy.Field()
    when        = scrapy.Field()
    director    = scrapy.Field()
    stars       = scrapy.Field()
    country     = scrapy.Field()
    language    = scrapy.Field()
    writer      = scrapy.Field()
    url         = scrapy.Field()
    time        = scrapy.Field()

class MovieSpider(scrapy.Spider):
    name = 'movies' # name of the Spider
    allowed_domains = ['imdb.com']
    try:
        # links.csv - list with coming soon movies
        with open("links.csv", "rt") as file:
            # read each line from the file without the first one
            start_urls = [url.strip() for url in file.readlines()][1:]
    except:
        start_urls = []

    # 'imdb.pipelines.DuplicatesPipelineItems': 300 - calls DuplicatesPipelineItems class from pipelines.py file (this will filter duplicated links in all movies)
    # 'CLOSESPIDER_PAGECOUNT': 100 - sets limit pages to 100 (delay in scrapy respone - more information in project description)
    # 'DEPTH_LIMIT': 1 - allows scrapy to go only to one next page
    custom_settings = {'ITEM_PIPELINES': {'imdb.pipelines.DuplicatesPipelineItems': 300}, 'CLOSESPIDER_PAGECOUNT': 100, 'DEPTH_LIMIT': 1}

    def parse(self, response):
        # scrape all information about movie
        f = Movie()
        # get xpaths to items
        title_xpath        = '//h1/text()'
        genres_xpath       = '//div[@class="subtext"]/a[re:test(@href, "(genres){1}")]/text()'
        when_xpath         = '//div[@class="subtext"]/a[re:test(text(), "[0-9]+\s+[A-Za-z]+\s+[0-9]+")]/text()'
        director_xpath     = '//h4[re:test(text(), "(Director)")]/following-sibling::a/text()'
        stars_xpath        = '//h4[text()="Stars:"]/following-sibling::a[re:test(@href, "name")]/text()'
        country_xpath      = '//h4[text()="Country:"]/following-sibling::a/text()'
        language_xpath     = '//h4[text()="Language:"]/following-sibling::a/text()'
        writer_xpath       = '//h4[re:test(text(), "(Writer)")]/following-sibling::a[re:test(@href, "name")]/text()'
        time_xpath         = '//h4[text()="Runtime:"]/following-sibling::time/text()'

        f['url']           = response.url
        f['title']         = [x.strip() for x in response.xpath(title_xpath).getall()]
        f['genres']        = response.xpath(genres_xpath).getall()
        f['when']          = [x.strip() for x in response.xpath(when_xpath).getall()]
        f['director']      = response.xpath(director_xpath).getall()
        f['stars']         = response.xpath(stars_xpath).getall()
        f['country']       = response.xpath(country_xpath).getall()
        f['language']      = response.xpath(language_xpath).getall()
        f['writer']        = response.xpath(writer_xpath).getall()
        f['time']          = response.xpath(time_xpath).getall()

        yield f

        # after scraping page of "coming soon" movie go to the first movie from "more like this" section

        # get link to movie from "more like this" section
        next_page = response.xpath('//div[re:test(@data-tconst, "tt")]/div/a/@href').extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            # go to the next page and call parse function to get all items from page
            yield scrapy.Request(url=next_page, callback = self.parse)
