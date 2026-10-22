# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from dataclasses import dataclass
from scrapy.item import Item, Field


@dataclass
class GutenbergscraperItem(Item):
    # define the fields for your item here like:
    # name: str | None = None
    Title = Field()
    pass

class book(Item):
    Title = Field()
    Category = Field()
    ISBN = Field()
    URL = Field()
    NumOfWords = Field()
    NumOfLetters = Field()
    TenCommonWords = Field()
    pass
