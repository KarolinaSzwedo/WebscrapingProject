# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

# this class filter duplicated links for "coming soon" movies
class DuplicatesPipelineLinks(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):

        if item['link'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['link'])
            return item

# this class filter duplicated links for all movies (coming soon and recommended)
class DuplicatesPipelineItems(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):

        if item['url'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['url'])
            return item
