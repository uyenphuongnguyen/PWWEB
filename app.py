from playwright.sync_api import sync_playwright


def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Mở trang login
        page.goto("https://cms.anhtester.com/users/login")

        # Nghỉ 2 giây để quan sát
        page.wait_for_timeout(2000)

        # Đóng popup
        page.locator("button[data-key='website-popup']").click()

        # Chờ một chút để quan sát
        page.wait_for_timeout(1000)

        # Nhập username
        page.locator("input[id='email']").fill("customer@example.com")

        page.wait_for_timeout(1000)

        # Nhập password
        page.locator("input[id='password']").fill("123456")

        page.wait_for_timeout(1000)

        # Click Login
        page.locator("//button[normalize-space()='Login']").click()

        # Nghỉ 3 giây để quan sát kết quả
        page.wait_for_timeout(3000)

        # Kiểm tra login thành công
        # assert page.locator("text=Welcome").is_visible()

        browser.close()