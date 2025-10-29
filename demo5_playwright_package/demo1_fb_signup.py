from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,channel="chrome",
                                         executable_path=r"D:\Balaji\Components\chrome-win64\chrome-win64\chrome.exe")
    context = browser.new_context()

    # page --> points to 1st tab in the context
    page = context.new_page()
    page.goto("https://www.facebook.com/")

    page.locator("xpath=//a[text()='Create new account']").click()
    #enter firstname as john
    page.locator("xpath=//input[@name='firstname']").fill("john")
    # enter lastname as wick
    page.locator("css=input[name='lastname']").fill("wick")
    # click on custom radio button
    page.locator("xpath=//input[@value='-1']").click()

    #check() method works only for type=checkbox and type=radio otherwise use click()

    # 20 Dec 2000
    # select --> label or value or index
    page.locator("xpath=//select[@id='day']").select_option(label="20")

    page.locator("xpath=//select[@id='month']").select_option(label="Dec")
    # page.locator("xpath=//select[@id='month']").select_option(value="12")
    # page.locator("xpath=//select[@id='month']").select_option(index=11)

    #select year as 2000
    page.locator("xpath=//select[@id='year']").select_option(label="2000")

    actual_header= page.locator("xpath=//div[contains(text(),'new account')]").inner_text()

    print(actual_header)
    time.sleep(5)

















