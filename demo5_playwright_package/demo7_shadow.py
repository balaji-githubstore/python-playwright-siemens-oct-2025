from playwright.sync_api import sync_playwright
import time

def handle_dialog123(dialog):
    print(dialog.message)
    dialog.accept()

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,channel="chrome",
                                         executable_path=r"D:\Balaji\Components\chrome-win64\chrome-win64\chrome.exe")
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.salesforce.com/in/form/signup/sales-ee/")

    page.locator("css=button[data-testid='minimize-button']").click()

    # using text to find
    page.locator("text=Create an account").click()

    page.locator("a:has-text('Create an account')").click()

    page.locator("a",has_text='Create an account').click()


    time.sleep(5)

