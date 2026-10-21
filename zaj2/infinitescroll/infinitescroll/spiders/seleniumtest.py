if __name__ == "__main__":
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.common.exceptions import TimeoutException

    SCROLL_ROUNDS = 8
    driver = webdriver.Chrome()

    driver.get("https://quotes.toscrape.com/scroll")

    wait = WebDriverWait(driver, timeout=10)
    seen = len(driver.find_elements(By.CSS_SELECTOR, ".quote"))

    title = driver.title
    print(title)
    driver.implicitly_wait(0.5)

    
    for _ in range(SCROLL_ROUNDS):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                try:
                    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, ".quote")) > seen)
                except TimeoutException:
                    break
                seen = len(driver.find_elements(By.CSS_SELECTOR, ".quote"))
    print(seen)
    quotes = driver.find_element(by=By.CLASS_NAME, value="quotes")
    for quote in quotes.find_elements(By.CLASS_NAME,"quote"):
        print(quote.text)
    
    
    driver.quit()
