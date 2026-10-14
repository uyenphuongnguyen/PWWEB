from playwright.sync_api import sync_playwright
from faker import Faker

# Khởi tạo đối tượng Faker (có thể truyền 'vi_VN' nếu muốn tên tiếng Việt, hoặc để trống mặc định là tiếng Anh)
fake = Faker()

def test_register(page):
    # Sinh dữ liệu ngẫu nhiên mỗi lần chạy test
    random_name = fake.name()
    random_email = fake.email()

    # with sync_playwright() as p:
    #     browser = p.chromium.launch(headless=False)
    #     page = browser.new_page()

    # Mở trang login
    page.goto("https://automationexercise.com/")
    #click link sign up
    page.get_by_role("link", name="Signup / Login").click()
    # page.wait_for_timeout(500)

    signup_title = page.locator("div.signup-form h2").inner_text()
    print(signup_title)

    #enter name, email
    page.get_by_placeholder("Name").fill(random_name)
    page.locator(".signup-form").get_by_placeholder("Email Address").fill(random_email)

    # click button sign up
    page.get_by_role("button", name="Signup").click()

def test_fill_register():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        test_register(page)

        #click checkbox có id
        page.locator("#id_gender1").click()

        #fill password
        page.locator("#password").fill("Phuong123")
        page.wait_for_timeout(500)

        #select date time
        # Chọn ngày '15'
        page.locator("#days").select_option("15")
        # Chọn tháng 'May' (hoặc '5' tùy theo giá trị value của trang web)
        page.locator("#months").select_option(label="May")
        # Chọn năm '1995'
        page.locator("#years").select_option("1995")
        page.wait_for_timeout(500)

        # click checkbox có id
        page.locator("#newsletter").click()

        #fill first name, last name, company, address
        random_first_name = fake.first_name()
        random_last_name = fake.last_name()
        random_company = fake.company()
        random_address = fake.address()
        page.locator("#first_name").fill(random_first_name)
        page.locator("#last_name").fill(random_last_name)
        page.locator("#company").fill(random_company)
        page.locator("#address1").fill(random_address)

        # select country
        page.locator("#country").select_option("United States")
        page.wait_for_timeout(500)

        #fill state, city, zipcode, phone
        random_state = fake.state()
        random_city = fake.city()
        random_zipcode = fake.zipcode()
        random_phone = fake.phone()
        page.locator("#state").fill(random_state)
        page.locator("#city").fill(random_city)
        page.locator("#zipcode").fill(random_zipcode)
        page.locator("#mobile_number").fill(random_phone)

        #click create account
        page.get_by_role("button",name = "Create Account").click()
        page.wait_for_timeout(500)




# def test_login_success():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#
#         # Mở trang login
#         page.goto("https://automationexercise.com/signup")
#         # Nghỉ 2 giây để quan sát
#         page.wait_for_timeout(500)