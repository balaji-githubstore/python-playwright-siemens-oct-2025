from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,channel="chrome",
                                         executable_path=r"D:\Balaji\Components\chrome-win64\chrome-win64\chrome.exe")
    context = browser.new_context()

    # page --> points to 1st tab in the context
    page = context.new_page()
    page.goto("https://demo.openemr.io/b/openemr")

    page.locator("xpath=//input[@id='authUser']").fill("admin")
    page.locator("css=input[name='clearPass']").fill("pass")
    page.locator("xpath=//button[@id='login-button']").click()

    # click on patient menu
    # click on new search

    # <frame name=pat>
    pat_frame_section= page.frame_locator("xpath=//iframe[@name='pat']")
    pat_frame_section.locator("xpath=//input[@name='form_fname']").fill("jack")
    pat_frame_section.locator("xpath=//input[@id='form_DOB']").fill("2025-10-29")

    pat_frame_section.locator("").click()

    # <frame id=modalframe>
    modal_frame_section= page.frame_locator("xpath=//iframe[@id='modalframe']")
    modal_frame_section.locator("").click()


    time.sleep(5)
