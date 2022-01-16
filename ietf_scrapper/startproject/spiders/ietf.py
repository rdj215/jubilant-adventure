from turtle import title
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from startproject.items import Article

# class IetfSpider(scrapy.Spider):
#     name = 'ietf'
#     allowed_domains = ['pythonscraping.com']
#     start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

#     def parse(self, response):
#         title = response.xpath('//span[@class="title"]/text()').get()
#         author = response.xpath('//span[@class="author-name"]/text()').get()
#         date = response.xpath('//span[@class="date"]/text()').get()
#         body = response.xpath('//div[@class="text"]/text()').get()
#         return {"title":title, "author":author, "date":date, "body":body }


class WikipediaSpider(CrawlSpider):
    name = 'wikipedia'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Chadwick_Boseman']

    rules = [Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'), callback='parse_info', follow=True)]

    def parse_info(self,response):
        article = Article()  
        article['title'] = response.xpath('//h1/text()').get()
        article['url'] = response.url
        article['lastUpdated'] = response.xpath('//li[@id="footer-info-lastmod"]/text()').get()
        return article
        
        
