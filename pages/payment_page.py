import re
from playwright.async_api import Page, expect

class PaymentPage:
    def __init__(self, page: Page):
        self.page = page
        self.placeorder_button = page.locator('button.checkout')
        self.product_name = page.locator('strong.product-item-name')
        self.product_price = page.locator('span.cart-price')
        self.total_price = page.locator('tr.grand span.price')
        self.item_dropdown = page.locator('div.items-in-cart')

    async def proceed_to_checkout(self):
        await self.placeorder_button.click()
        await self.page.wait_for_timeout(5000)

    async def check_total_price(self,product_name,product_total_price):
        await self.item_dropdown.click()
        await expect(self.product_name).to_have_text(product_name)
        await expect(self.total_price).to_have_text(product_total_price)

