import re
from playwright.async_api import Page, expect
from utils.config import CONFIG


class MenTopPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_product_image = page.locator('ol.product-items li:nth-child(1) span.product-image-container')

    async def click_first_product(self):
        await self.first_product_image.click()