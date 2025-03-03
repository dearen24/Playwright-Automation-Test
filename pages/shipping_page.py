import re
from playwright.async_api import Page, expect
from utils.config import CONFIG


class ShippingPage:
    def __init__(self, page: Page):
        self.page = page
        self.address = page.locator('fieldset.field div._required input')
        self.city = page.locator('input[name="city"]')
        self.postcode = page.locator('input[name="postcode"]')
        self.phone = page.locator('input[name="telephone"]')
        self.next_button = page.locator('button.continue')
        self.shipping_method = page.locator('tbody tr:nth-child(1) span.price span.price')

    async def fill_shipping_address(self):
        await self.page.select_option('select[name="country_id"]',"Indonesia")
        await self.address.fill(CONFIG["shipping_address"])
        await self.city.fill(CONFIG["shipping_city"])
        await self.postcode.fill(CONFIG["shipping_postcode"])
        await self.phone.fill(CONFIG["shipping_phone"])
        await self.page.wait_for_timeout(6000)

    async def get_shipping_price(self):
        shipping_price =  await self.shipping_method.inner_text()
        return shipping_price
    
    async def checkout(self):
        await self.shipping_method.click()
        await self.next_button.click()

