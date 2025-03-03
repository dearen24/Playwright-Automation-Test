import re
from playwright.async_api import Page, expect
from utils.config import CONFIG


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.header_sign_in = page.locator('div.panel ul.header li:nth-child(2) a')
        self.page_title = page.locator('h1.page-title span')
        self.nav_bar_men = page.locator('li.nav-3')
        self.nav_bar_men_tops = page.locator('li.nav-3-1')

    async def go_to_login(self):
        await self.page.goto(CONFIG["base_url"])
        await expect(self.page_title).to_have_text("Home Page")
        await self.header_sign_in.click()

    async def go_to_men_section(self):
        await self.nav_bar_men.hover()
        await self.nav_bar_men_tops.click()