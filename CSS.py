from playwright.sync_api import sync_playwright


def test_register():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Mở trang login
        page.goto("https://automationexercise.com/")
        # Nghỉ 2 giây để quan sát
        page.wait_for_timeout(500)
        #click link sign up
        page.get_by_role("link", name="Signup / Login").click()
        page.wait_for_timeout(500)

        signup_title = page.locator("div.signup-form h2").inner_text()
        print(signup_title)

        #enter name, email
        page.get_by_placeholder("Name").fill("A")
        page.wait_for_timeout(500)
        page.locator(".signup-form").get_by_placeholder("Email Address").fill("abc@gmail.com")
        page.wait_for_timeout(500)

        # click button sign up
        page.get_by_role("button", name="Signup").click()
        page.wait_for_timeout(500)