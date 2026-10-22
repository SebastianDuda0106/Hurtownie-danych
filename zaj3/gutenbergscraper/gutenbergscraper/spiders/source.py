import scrapy


class SourceSpider(scrapy.Spider):
    name = "source"
    allowed_domains = [""]
    start_urls = ["c:/Users/s-A014-19/Desktop/Hurtownie-danych/.venv/Scripts/activate"]

    def parse(self, response):
        pass
