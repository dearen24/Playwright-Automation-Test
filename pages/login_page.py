import re
from playwright.async_api import Page, expect
from utils.config import CONFIG

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.page_title = page.locator('h1.page-title span')
        self.input_email = page.locator('input#email')
        self.input_password = page.locator('input#pass')
        self.sign_in_button = page.locator('button.login')

    async def login(self):
        await expect(self.page_title).to_have_text("Customer Login")
        await self.input_email.fill(CONFIG["user_email"])
        await self.input_password.fill(CONFIG["user_password"])
        await self.sign_in_button.click()
        await self.page.wait_for_timeout(2000)

