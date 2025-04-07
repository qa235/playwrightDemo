import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        # 使用環境變數控制是否為 Headless 模式
        headless = True  # 如果要顯示瀏覽器，改為 False
        browser = p.chromium.launch(headless=headless)
        yield browser
        browser.close()

def test_basic(browser):
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    assert "Playwright" in page.title()
    page.close()
