# import pytest
# from playwright.sync_api import sync_playwright

# def test_search():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()

#         # 打開網站
#         page.goto("http://demowebshop.tricentis.com/")

#         # 搜尋商品
#         search_query = "laptop"
#         page.fill("input[name='q']", search_query)
#         page.click("input[value='Search']")

#         # 驗證搜尋結果
#         try:
#             assert page.is_visible(f"text={search_query}")
#             print(f" 搜尋成功：{search_query} 顯示在結果中")
#         except AssertionError:
#             # 如果搜尋失敗，截圖保存
#             page.screenshot(path=f"../reports/screenshots/search_failed.png")
#             print(f"搜尋失敗：無法找到 {search_query}")
#             raise
#         finally:
#             browser.close()

import pytest
from playwright.async_api import async_playwright
import asyncio

@pytest.mark.asyncio
@pytest.mark.parametrize("search_query, expected", [
    ("laptop", "Laptop"),
    ("randomitem", "No products were found that matched your criteria.")
])
async def test_search(search_query, expected):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # 打開網站
        await page.goto("http://demowebshop.tricentis.com/")

        # 搜尋商品
        await page.fill("input[name='q']", search_query)
        await page.click("input[value='Search']")

        # 驗證搜尋結果
        try:
            assert await page.is_visible(f"text={expected}")
            print(f" 搜尋成功：{search_query} => {expected}")
        except AssertionError:
            # 搜尋錯誤時截圖
            await page.screenshot(path=f"../reports/screenshots/search_{search_query}_failed.png")
            print(f" 錯誤截圖已保存：search_{search_query}_failed.png")
            raise
        finally:
            await browser.close()
