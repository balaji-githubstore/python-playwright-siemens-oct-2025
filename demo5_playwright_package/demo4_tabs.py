from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,channel="chrome",
                                         executable_path=r"D:\Balaji\Components\chrome-win64\chrome-win64\chrome.exe")
    context = browser.new_context()
    page = context.new_page()
    # page - 1st tab
    page.goto("https://www.db4free.net/")

    with context.expect_page() as new_page_info:
        page.locator("xpath=//b[contains(text(),'phpMyAdmin')]").click()

    # new_page --> will refer to second tab
    #new tab or window --> page details
    new_page=new_page_info.value

    # enter username
    new_page.locator("xpath=//input[@id='input_username']").fill("admin")

    # click on Log in documentation
    with context.expect_page() as new_page3_info:
        new_page.locator("xpath=//img[@alt='Documentation']").click()
    new_page3=new_page3_info.value

    print(new_page3.title())

    # print(len(context.pages))

    time.sleep(5)

    # page1= context.pages[0]
    # page2=context.pages[1]


