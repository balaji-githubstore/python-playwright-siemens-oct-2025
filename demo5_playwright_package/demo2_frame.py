from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,channel="chrome",
                                         executable_path=r"D:\Balaji\Components\chrome-win64\chrome-win64\chrome.exe")
    context = browser.new_context()

    # page --> points to 1st tab in the context
    page = context.new_page()
    page.goto("https://netbanking.hdfcbank.com/netbanking/")

    #get control of frame using xpath or css
    # //frame[contains(@src,'RSNBLogin')]
    login_frame1_section= page.frame_locator("xpath=//frame[@name='login_page']")
    login_frame1_section.locator("xpath=//input[@name='fldLoginUserId']").fill("john123")
    login_frame1_section.locator("xpath=//a[text()='CONTINUE']").click()

    time.sleep(5)
