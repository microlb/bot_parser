# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ParsSearchV10Item(scrapy.Item):
    title = scrapy.Field()
    body = scrapy.Field()
    image = scrapy.Field()
    video = scrapy.Field()
    company = scrapy.Field()
    city = scrapy.Field()
    salary = scrapy.Field()
    domain = scrapy.Field()
    pass
