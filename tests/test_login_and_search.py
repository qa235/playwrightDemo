import pytest
from playwright.async_api import async_playwright
import asyncio

@pytest.mark.asyncio
async def test_login_and_search():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # 1. 打開網站
        await page.goto("http://demowebshop.tricentis.com/")

        # 2. 登入操作
        await page.click("a.ico-login")
        await page.fill("input[name='Email']", "testeleanor@test.com")
        await page.fill("input[name='Password']", "password123")
        await page.click("input[value='Log in']")
        
        # 3. 等待登入成功
        try:
            await page.wait_for_selector("text=Log out", timeout=5000)
            print(" 登入成功")
        except:
            print(" 登入失敗")
            await page.screenshot(path="../reports/screenshots/login_failed.png")
            raise

        # 4. 搜尋商品
        search_query = "laptop"
        await page.fill("input[name='q']", search_query)
        await page.click("input[value='Search']")

        # 5. 驗證搜尋結果
        try:
            await page.wait_for_selector(f"text={search_query}", timeout=3000)
            print(f" 搜尋成功：{search_query}")
        except:
            print(f" 搜尋失敗：{search_query}")
            await page.screenshot(path=f"../reports/screenshots/search_{search_query}_failed.png")
            raise

        # 關閉瀏覽器
        await browser.close()

# 執行測試
asyncio.run(test_login_and_search())
