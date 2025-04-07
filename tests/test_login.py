
import pytest
from playwright.async_api import async_playwright
import asyncio

@pytest.mark.asyncio
@pytest.mark.parametrize("username, password, expected", [
    ("testeleanor@test.com", "password123", "Log out"),
    ("invalid@user.com", "wrongpassword", "Login was unsuccessful.")
])
async def test_login(username, password, expected):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # 打開網站
        await page.goto("http://demowebshop.tricentis.com/")

        # 點擊登入
        await page.click("a.ico-login")

        # 輸入帳號密碼
        await page.fill("input[name='Email']", username)
        await page.fill("input[name='Password']", password)

        # 點擊登入按鈕
        await page.click("input[value='Log in']")

        # 驗證結果
        try:
            if expected == "Log out":
                assert await page.is_visible("text=Log out")
                print(f" 登入成功：{username}")
            else:
                assert await page.is_visible("text=Login was unsuccessful.")
                print(f" 登入失敗：{username}")
        except AssertionError:
            # 錯誤時截圖
            await page.screenshot(path=f"../reports/screenshots/{username}_login_failed.png")
            print(f" 錯誤截圖已保存：{username}_login_failed.png")
            raise
        finally:
            await browser.close()


