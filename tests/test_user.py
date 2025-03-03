import pytest
from utils.config import CONFIG
from playwright.async_api import Page, expect, async_playwright
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.men_top_page import MenTopPage
from pages.product_page import ProductPage
from pages.shipping_page import ShippingPage
from pages.payment_page import PaymentPage
from pages.after_checkout_page import AfterCheckoutPage

@pytest.mark.asyncio
async def test_e2e_user():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(record_video_dir="videos/",record_video_size={"width":1280,"height":720},viewport={"width":1280,"height":720})
        # context = await browser.new_context()
        page = await context.new_page()
        home_page = HomePage(page)
        login_page = LoginPage(page)
        men_top_page = MenTopPage(page)
        product_page = ProductPage(page)
        shipping_page = ShippingPage(page)
        payment_page = PaymentPage(page)
        after_checkout_page = AfterCheckoutPage(page)

        await home_page.go_to_login()
        await login_page.login()
        await home_page.go_to_men_section()
        await men_top_page.click_first_product()

        product_name, product_price = await product_page.get_product_name_and_price()
        product_price = product_price.replace("$", "").strip()
        product_price = float(product_price)*float(CONFIG["product_qty"])

        await product_page.choose_product_option()
        await product_page.check_cart()
        await shipping_page.fill_shipping_address()

        shipping_price = await shipping_page.get_shipping_price()
        shipping_price = shipping_price.replace("$", "").strip()
        shipping_price = float(shipping_price)

        product_total_price = "{:.2f}".format(shipping_price+product_price)
        product_total_price = "$"+product_total_price

        await shipping_page.checkout()
        await payment_page.check_total_price(product_name,product_total_price)
        await payment_page.proceed_to_checkout()
        await after_checkout_page.log_out()

        await context.close()


