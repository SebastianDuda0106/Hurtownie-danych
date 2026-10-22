import scrapy
from ..items import book

class GutenspiderSpider(scrapy.Spider):
    name = "gutenspider"
    allowed_domains = ["www.gutenberg.org"]
    start_urls = ["https://www.gutenberg.org/ebooks/bookshelf/671"]

    def parse(self, response):
        maxitem=100
        links=response.css(".booklink a::attr('href')").getall()
        yield{
                    "links":links
                }
        print("\n"*67,len(links))
        for link in links:
            yield response.follow(link,callback=self.parsebook)
        
    
    def parsebook(self,response):
        title=response.css("tr:nth-child(4) td::text").get()
        book1=book()
        book1["Title"]=title
        return book1
    
    def parseinsidebook(self,response):
        pass
