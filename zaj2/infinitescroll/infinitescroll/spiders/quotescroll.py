import scrapy


class QuotescrollSpider(scrapy.Spider):
    name = "quotescroll"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/scroll"]

    def parse(self, response):
        pass

from scrapy_selenium4 import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ReviewsSpider(scrapy.Spider):
    name = "reviews"
    allowed_domains = ["web-scraping.dev"]

    async def start(self):
        yield SeleniumRequest(
            url="https://web-scraping.dev/reviews",
            callback=self.parse,
            wait_time=20,
            wait_until=EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-testid='review']")
            ),
        )

    def parse(self, response):
        reviews = response.css("[data-testid='review']")
        yield {
            "title": response.css("title::text").get(),
            "reviews_rendered": len(reviews),
            "first_review": reviews.css("[data-testid='review-text']::text").get(),
        }

from scrapy.selector import Selector
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

class TestimonialsSpider(scrapy.Spider):
    name = "testimonials"
    allowed_domains = ["web-scraping.dev","quotes.toscrape.com"]
    SCROLL_ROUNDS = 2

    async def start(self):
        yield SeleniumRequest(
            url="https://quotes.toscrape.com/scroll",
            callback=self.parse,
            wait_time=20,
            wait_until=EC.presence_of_element_located((By.CSS_SELECTOR, ".quote")),
        )
    def parse(self, response):
        driver = response.request.meta["driver"]
        wait = WebDriverWait(driver, timeout=10)
        seen = len(driver.find_elements(By.CSS_SELECTOR, ".quote"))

        for _ in range(self.SCROLL_ROUNDS):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, ".quote")) > seen)
            except TimeoutException:
                break
            seen = len(driver.find_elements(By.CSS_SELECTOR, ".quote"))

        for card in Selector(text=driver.page_source).css(".quote"):
            yield {
                "text": card.css("span::text").get(),
                "author": card.css("small::text").get(),
            }