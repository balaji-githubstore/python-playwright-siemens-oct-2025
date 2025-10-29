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
    # page - 1st tab
    page.goto("https://netbanking.hdfcbank.com/netbanking/IpinResetUsingOTP.htm")

    # register the event handler to handle the alert (dialog)
    page.on("dialog", handle_dialog123)

    page.locator("xpath=//img[@alt='Go']").click()
    # button[data-testid="minimize-button"]
    time.sleep(5)

