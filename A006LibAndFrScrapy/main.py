import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://innercalmserenejoke.neverssl.com/online']

    def parse(self, response):
        # Extracting the entire HTML body using XPath
        body_content = response.xpath('//body').get()
        # Alternatively, using CSS selectors:
        # body_content = response.css('body').get()
        yield {'body': body_content}
