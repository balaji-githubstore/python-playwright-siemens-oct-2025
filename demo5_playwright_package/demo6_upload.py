from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,channel="chrome",
                                         executable_path=r"D:\Balaji\Components\chrome-win64\chrome-win64\chrome.exe")
    context = browser.new_context()
    page = context.new_page()
    # page - 1st tab
    page.goto("https://www.ilovepdf.com/pdf_to_word")

    with page.expect_file_chooser() as file_chooser_info:
        page.locator("xpath=//span[text()='Select PDF file']").click()

    file_chooser= file_chooser_info.value

    file_chooser.set_files(r"D:\Balaji\Profile.pdf")
    time.sleep(5)
