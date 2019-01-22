import scrapy


class MySpider(scrapy.Spider):
    name = 'mech27'
    allowed_domains = ['mech27.com']
    start_urls = [
        'https://mech27.com/index.php/product/tribosys-3204/',
    ]