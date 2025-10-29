from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,channel="chrome",
                                         executable_path=r"D:\Balaji\Components\chrome-win64\chrome-win64\chrome.exe")
    context = browser.new_context()
    page = context.new_page()
    # page - 1st tab
    page.goto("https://www.ilovepdf.com/pdf_to_word")

    # driver.FindElement(By.XPath("//input[@type='file']")).SendKeys( @ "D:\Balaji\Profile.pdf");

    page.locator("xpath=//input[@type='file']").set_input_files(r"D:\Balaji\Profile.pdf")

    time.sleep(5)
