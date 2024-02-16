# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_discount = scrapy.Field()
    original_price = scrapy.Field()
    merchant_name = scrapy.Field()
    merchant_loc = scrapy.Field()
    rating = scrapy.Field()
    product_sold = scrapy.Field()
    product_image = scrapy.Field()
    product_detail_link = scrapy.Field()
