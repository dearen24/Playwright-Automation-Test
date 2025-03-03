import re
from playwright.async_api import Page, expect
from utils.config import CONFIG


class AfterCheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.thankyou_text = page.locator('h1.page-title span')
        self.customer_name = page.locator('div.panel ul.header li.customer-welcome')
        self.sign_out = page.locator('div.panel div.customer-menu ul.header li.authorization-link')

    async def log_out(self):
        await expect(self.thankyou_text).to_have_text("Thank you for your purchase!")
        await self.customer_name.click()
        await self.sign_out.click()
