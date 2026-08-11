from playwright.sync_api import expect


class BasePage:

    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def check(self, locator):
        self.page.locator(locator).check()

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def wait(self):
        self.page.wait_for_load_state("networkidle")

    def visible(self, locator):
        expect(self.page.locator(locator)).to_be_visible()