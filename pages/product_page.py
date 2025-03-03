import re
import logging
import sys
LOGGER = logging.getLogger(__name__)
from playwright.async_api import Page, expect
from utils.config import CONFIG


class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.xl_size = page.locator('div[aria-labelledby="option-label-size-143"] div[index="4"]')
        self.blue_color = page.locator('div[aria-labelledby="option-label-color-93"] div[index="0"]')
        self.product_qty = page.locator('input[name="qty"]')
        self.add_to_cart_button = page.locator('button.tocart span')
        self.cart = page.locator('a.showcart')
        self.cart_count = page.locator('a.showcart span.counter-number')
        self.item_qty = CONFIG["product_qty"]
        self.modal_cart_button_checkout = page.locator('button.checkout')
        self.product_name = page.locator('div.product h1 span')
        self.product_price = page.locator('div.product-info-main span.price')

    async def choose_product_option(self):
        await self.xl_size.click()
        await self.blue_color.click()
        await self.product_qty.fill(self.item_qty)
        await self.add_to_cart_button.click()
        await expect(self.add_to_cart_button).to_have_text("Add to Cart")

    async def check_cart(self):
        await expect(self.cart_count).to_have_text(self.item_qty)
        await self.cart.click()
        await self.page.wait_for_timeout(1000)
        await self.modal_cart_button_checkout.click()

    async def get_product_name_and_price(self):
        product_name = await self.product_name.inner_text()
        product_price = await self.product_price.inner_text()
        return product_name, product_price