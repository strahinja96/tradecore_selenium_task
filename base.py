from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
import unittest
import random


class base_test(unittest.TestCase):
    # First page

    first_name = 'form-first_name'
    last_name = 'form-last_name'
    email = 'form-email'
    password = 'form-password'
    confirm_password = 'form-password2'
    telephone = 'form-telephone'
    date_of_birth = 'form-date_of_birth'
    address_country = 'form-addr_country'
    address_zip = 'form-addr_zip'
    address1 = 'form-addr_street'
    address2 = 'form-addr_line_2'
    city = 'form-addr_city'
    finish = 'button-step'

    # Second page

    shares = '(//B)[2]'
    shares_items = '//select[@id="form-shares"]/following-sibling::div/div/ul/li'
    forex = '(//B)[3]'
    forex_items = '//select[@id="form-forex"]/following-sibling::div/div/ul/li'
    cfds = '(//B)[4]'
    cfds_items = '//select[@id="form-cfds"]/following-sibling::div/div/ul/li'
    spread_betting = '(//B)[5]'
    spread_betting_items = '//select[@id="form-spread_betting"]/following-sibling::div/div/ul/li'
    relevant_experience = '(//B)[6]'
    relevant_experience_items = '//div[@field-id="relevant_experience"]/div/div/div/ul/li'
    trading_accounts = '(//B)[7]'
    trading_accounts_items = '//select[@id="form-trading_accounts"]/following-sibling::div/div/ul/li'
    trading_currency = '(//B)[8]'
    trading_currency_items = '//select[@id="form-currency"]/following-sibling::div/div/ul/li'
    annual_income = '(//B)[9]'
    annual_income_items = '//select[@id="form-approx_annual_income"]/following-sibling::div/div/ul/li'
    employment_status = '(//B)[10]'
    employment_status_items = '//select[@id="form-employment_status"]/following-sibling::div/div/ul/li'
    liquid_savings = '(//B)[11]'
    liquid_savings_items = '//select[@id="form-liquid_savings"]/following-sibling::div/div/ul/li'
    terms_and_conditions = '//div[@label="I have read, understood and accepted the Privacy Policy, Risk Disclosures and Terms & Conditions"]'

    def setUp(self):
        self.driver = webdriver.Chrome(
            'C:\Users\Strahinja\PycharmProjects\TradecoreSeleniumTask\Driver\chromedriver.exe')
        self.driver.get('https://demo-biq.dev.tradecore.io/#/')
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

    # first name inputs

    def leave_first_name_empty(self):
        first_name_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.first_name))
        first_name_input.clear()

    def fill_first_name_with_trailing_and_leading_spaces(self):
        first_name_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.first_name))
        first_name_input.clear()
        first_name_input.send_keys('  John  ')

    def fill_first_name_with_numbers(self):
        first_name_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.first_name))
        first_name_input.clear()
        first_name_input.send_keys('John12345')

    def fill_first_name_with_special_characters(self):
        first_name_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.first_name))
        first_name_input.clear()
        first_name_input.send_keys('!@#$%^*.,";:')

    def fill_first_name_with_bool(self):
        first_name_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.first_name))
        first_name_input.clear()
        first_name_input.send_keys(bool)

    def fill_first_name_with_capital_letters(self):
        first_name_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.first_name))
        first_name_input.clear()
        first_name_input.send_keys('JoHn')

    def fill_first_name_with_one_character(self):
        first_name_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.first_name))
        first_name_input.clear()
        first_name_input.send_keys('J')

    def fill_first_name_with_javascript_alert(self):
        first_name_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.first_name))
        first_name_input.clear()
        first_name_input.send_keys('javascript:alert(document.cookie)')

    def fill_first_name_with_javascript_propmt(self):
        first_name_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.first_name))
        first_name_input.clear()
        first_name_input.send_keys('javascript:prompt(document.cookie)')

    def fill_first_name_with_javascript_confirm(self):
        first_name_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.first_name))
        first_name_input.clear()
        first_name_input.send_keys('javascript:confirm(document.cookie)')

    def fill_first_name(self):
        first_name_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.first_name))
        first_name_input.clear()
        first_name_input.send_keys('John')

    # last name inputs

    def leave_last_name_empty(self):
        last_name_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.last_name))
        last_name_input.clear()

    def fill_last_name_with_trailing_and_leading_spaces(self):
        last_name_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.last_name))
        last_name_input.clear()
        last_name_input.send_keys('  Doe  ')

    def fill_last_name_with_numbers(self):
        last_name_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.last_name))
        last_name_input.clear()
        last_name_input.send_keys('Doe12345')

    def fill_last_name_with_various_symbols(self):
        last_name_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.last_name))
        last_name_input.clear()
        last_name_input.send_keys('!@#$%^*.,";:')

    def fill_last_name_with_bool(self):
        last_name_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.last_name))
        last_name_input.clear()
        last_name_input.send_keys(bool)

    def fill_last_name_with_capital_letters(self):
        last_name_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.last_name))
        last_name_input.clear()
        last_name_input.send_keys('DoE')

    def fill_last_name_with_one_character(self):
        last_name_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.last_name))
        last_name_input.clear()
        last_name_input.send_keys('D')

    def fill_last_name_with_javascript_alert(self):
        last_name_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.last_name))
        last_name_input.clear()
        last_name_input.send_keys('javascript:alert(document.cookie)')

    def fill_last_name_with_javascript_propmt(self):
        last_name_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.last_name))
        last_name_input.clear()
        last_name_input.send_keys('javascript:prompt(document.cookie)')

    def fill_last_name_with_javascript_confirm(self):
        last_name_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.last_name))
        last_name_input.clear()
        last_name_input.send_keys('javascript:confirm(document.cookie)')

    def fill_last_name(self):
        last_name_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.last_name))
        last_name_input.clear()
        last_name_input.send_keys('Doe')

    # email inputs

    def leave_email_empty(self):
        email_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.email))
        email_input.clear()

    def fill_email_with_trailing_and_leading_spaces(self):
        email_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.email))
        email_input.clear()
        email_input.send_keys('  test'+str(random.randint(10,1000))+'@tradecore.com  ')

    def fill_email_with_missing_at_sign_and_domain(self):
        email_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.email))
        email_input.clear()
        email_input.send_keys('test'+str(random.randint(10,1000)))

    def fill_email_with_missing_at_sign(self):
        email_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.email))
        email_input.clear()
        email_input.send_keys('test'+str(random.randint(10,1000))+'tradecore.com')

    def fill_email_with_missing_username(self):
        email_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.email))
        email_input.clear()
        email_input.send_keys('@tradecore.com')

    def fill_email_with_missing_domain(self):
        email_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.email))
        email_input.clear()
        email_input.send_keys('test'+str(random.randint(10,1000))+'@tradecore')

    def fill_email_with_special_characters(self):
        email_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.email))
        email_input.clear()
        email_input.send_keys('!@#$%^*.,";:@tradecore.com')

    def fill_email_with_trailing_dot(self):
        email_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.email))
        email_input.clear()
        email_input.send_keys('test'+str(random.randint(10,1000))+'.@tradecore.com')

    def fill_email_with_multiple_dots(self):
        email_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.email))
        email_input.clear()
        email_input.send_keys('test'+str(random.randint(10,1000))+'.@tradecore..com')

    def fill_email_with_follow_up_text(self):
        email_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.email))
        email_input.clear()
        email_input.send_keys('test'+str(random.randint(10,1000))+'@tradecore.com John Doe')

    def fill_email_with_numbers(self):
        email_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.email))
        email_input.clear()
        email_input.send_keys('123123123')

    def fill_email_with_space(self):
        email_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.email))
        email_input.clear()
        email_input.send_keys('test '+str(random.randint(10,1000))+'@ tradecore.com')

    def fill_email_with_bool(self):
        email_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.email))
        email_input.clear()
        email_input.send_keys(bool)

    def fill_email_with_one_character(self):
        email_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.email))
        email_input.clear()
        email_input.send_keys('t')

    def fill_email_with_javascript_alert(self):
        email_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.email))
        email_input.clear()
        email_input.send_keys('javascript:alert(document.cookie)')

    def fill_email_with_javascript_propmt(self):
        email_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.email))
        email_input.clear()
        email_input.send_keys('javascript:prompt(document.cookie)')

    def fill_email_with_javascript_confirm(self):
        email_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.email))
        email_input.clear()
        email_input.send_keys('javascript:confirm(document.cookie)')

    def fill_email(self):
        email_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.email))
        email_input.clear()
        email_input.send_keys('test'+str(random.randint(10,1000))+'@tradecore.com')

    # password inputs

    def leave_password_empty(self):
        password_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.password))
        password_input.clear()

    def fill_password_with_trailing_and_leading_spaces(self):
        password_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.password))
        password_input.clear()
        password_input.send_keys('  password1234  ')

    def fill_password_with_one_character(self):
        password_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.password))
        password_input.clear()
        password_input.send_keys('p')

    def fill_password_with_bool(self):
        password_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.password))
        password_input.clear()
        password_input.send_keys(bool)

    def fill_password_with_numbers_only(self):
        password_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.password))
        password_input.clear()
        password_input.send_keys('12345678')

    def fill_password_with_letters_only(self):
        password_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.password))
        password_input.clear()
        password_input.send_keys('password')

    def fill_password_with_javascript_alert(self):
        password_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.password))
        password_input.clear()
        password_input.send_keys('javascript:alert(document.cookie)')

    def fill_password_with_javascript_propmt(self):
        password_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.password))
        password_input.clear()
        password_input.send_keys('javascript:prompt(document.cookie)')

    def fill_password_with_javascript_confirm(self):
        password_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.password))
        password_input.clear()
        password_input.send_keys('javascript:confirm(document.cookie)')

    def fill_password(self):
        password_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.password))
        password_input.clear()
        password_input.send_keys('password1234')

    # password confirmation inputs

    def leave_password_confirmation_empty(self):
        password_2_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.confirm_password))
        password_2_input.clear()

    def fill_password_confirmation_differently_than_password(self):
        password_2_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.confirm_password))
        password_2_input.clear()
        password_2_input.send_keys('password')

    def fill_password_confirmation_with_javascript_alert(self):
        password_2_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.confirm_password))
        password_2_input.clear()
        password_2_input.send_keys('javascript:alert(document.cookie)')

    def fill_password_confirmation_with_javascript_propmt(self):
        password_2_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.confirm_password))
        password_2_input.clear()
        password_2_input.send_keys('javascript:prompt(document.cookie)')

    def fill_password_confirmation_with_javascript_confirm(self):
        password_2_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.confirm_password))
        password_2_input.clear()
        password_2_input.send_keys('javascript:confirm(document.cookie)')

    def fill_password_conformation(self):
        password_2_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.confirm_password))
        password_2_input.clear()
        password_2_input.send_keys('password1234')

    # telephone inputs

    def leave_telephone_empty(self):
        telephone_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.telephone))
        telephone_input.clear()

    def fill_telephone_with_bool(self):
        telephone_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.telephone))
        telephone_input.send_keys(bool)

    def fill_telephone_with_letters(self):
        telephone_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.telephone))
        telephone_input.send_keys('asdasdasd')

    def fill_telephone_with_numbers_and_letters(self):
        telephone_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.telephone))
        telephone_input.send_keys('65as111a')

    def fill_telephone_with_special_characters(self):
        telephone_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.telephone))
        telephone_input.send_keys('!@#$%^*.,";:')

    def fill_telephone_with_too_short_number(self):
        telephone_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.telephone))
        telephone_input.send_keys('6511')

    def fill_telephone_with_spaces(self):
        telephone_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.telephone))
        telephone_input.send_keys('  65 111 1 1')

    def fill_telephone_with_wrong_mobile_code(self):
        telephone_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.telephone))
        telephone_input.send_keys('671111111')

    def fill_telephone_with_javascript_alert(self):
        telephone_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.telephone))
        telephone_input.send_keys('javascript:alert(document.cookie)')

    def fill_telephone_with_javascript_propmt(self):
        telephone_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.telephone))
        telephone_input.send_keys('javascript:prompt(document.cookie)')

    def fill_telephone_with_javascript_confirm(self):
        telephone_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.telephone))
        telephone_input.send_keys('javascript:confirm(document.cookie)')

    def fill_telephone(self):
        telephone_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.telephone))
        telephone_input.send_keys('651111111')

    # birth date inputs

    def leave_birth_date_empty(self):
        birth_date_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.date_of_birth))
        birth_date_input.clear()

    def fill_birth_date_with_wrong_format_year_first(self):
        birth_date_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.date_of_birth))
        birth_date_input.clear()
        birth_date_input.send_keys('1991/11/01')

    def fill_birth_date_with_wrong_format_with_dots(self):
        birth_date_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.date_of_birth))
        birth_date_input.clear()
        birth_date_input.send_keys('01.11.1991')

    def fill_birth_date_with_wrong_format_with_dashes(self):
        birth_date_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.date_of_birth))
        birth_date_input.clear()
        birth_date_input.send_keys('01-11-1991')

    def fill_birth_date_with_wrong_format_with_spaces(self):
        birth_date_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.date_of_birth))
        birth_date_input.clear()
        birth_date_input.send_keys('01 11 1991')

    def fill_birth_date_with_wrong_format_no_separator(self):
        birth_date_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.date_of_birth))
        birth_date_input.clear()
        birth_date_input.send_keys('01111991')

    def fill_birth_date_with_unexisting_day(self):
        birth_date_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.date_of_birth))
        birth_date_input.clear()
        birth_date_input.send_keys('99/11/1991')

    def fill_birth_date_with_unexisting_month(self):
        birth_date_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.date_of_birth))
        birth_date_input.clear()
        birth_date_input.send_keys('01/111/1991')

    def fill_birth_date_with_future_year(self):
        birth_date_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.date_of_birth))
        birth_date_input.clear()
        birth_date_input.send_keys('01/11/11991')

    def fill_birth_date_with_bool(self):
        birth_date_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.date_of_birth))
        birth_date_input.clear()
        birth_date_input.send_keys(bool)

    def fill_birth_date_with_javascript_alert(self):
        birth_date_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.birth_date))
        birth_date_input.clear()
        birth_date_input.send_keys('javascript:alert(document.cookie)')

    def fill_birth_date_with_javascript_propmt(self):
        birth_date_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.birth_date))
        birth_date_input.clear()
        birth_date_input.send_keys('javascript:prompt(document.cookie)')

    def fill_birth_date_with_javascript_confirm(self):
        birth_date_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.birth_date))
        birth_date_input.clear()
        birth_date_input.send_keys('javascript:confirm(document.cookie)')

    def fill_birth_date(self):
        dateInput = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.date_of_birth))
        dateInput.clear()
        dateInput.send_keys('01/11/1991')

    # country inputs

    def select_country(self):
        country_input = WebDriverWait(self.driver, 10).until(
            lambda driver: Select(driver.find_element_by_id(self.address_country)))
        country_input.select_by_value('RS')

    # postcode inputs

    def leave_postcode_empty(self):
        postcode_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.address_zip))
        postcode_input.clear()

    def fill_postcode_with_bool(self):
        postcode_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.address_zip))
        postcode_input.clear()
        postcode_input.send_keys(bool)

    def fill_postcode_with_letters_only(self):
        postcode_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.address_zip))
        postcode_input.clear()
        postcode_input.send_keys('asdasd')

    def fill_postcode_with_letters_and_numbers(self):
        postcode_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.address_zip))
        postcode_input.clear()
        postcode_input.send_keys('1215asd')

    def fill_postcode_with_special_characters(self):
        postcode_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.address_zip))
        postcode_input.clear()
        postcode_input.send_keys('11!23.4@5')

    def fill_postcode_with_trailing_and_leading_spaces(self):
        postcode_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.address_zip))
        postcode_input.clear()
        postcode_input.send_keys('  12345  ')

    def fill_postcode_with_spaces(self):
        postcode_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.address_zip))
        postcode_input.clear()
        postcode_input.send_keys('12 3 45')

    def fill_postcode_with_too_long_number(self):
        postcode_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.address_zip))
        postcode_input.clear()
        postcode_input.send_keys('1111111111111111111111111111111')

    def fill_postcode_with_one_number(self):
        postcode_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.address_zip))
        postcode_input.clear()
        postcode_input.send_keys('1')

    def fill_postcode_with_javascript_alert(self):
        postcode_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address_zip))
        postcode_input.clear()
        postcode_input.send_keys('javascript:alert(document.cookie)')

    def fill_postcode_with_javascript_propmt(self):
        postcode_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address_zip))
        postcode_input.clear()
        postcode_input.send_keys('javascript:prompt(document.cookie)')

    def fill_postcode_with_javascript_confirm(self):
        postcode_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address_zip))
        postcode_input.clear()
        postcode_input.send_keys('javascript:confirm(document.cookie)')

    def fill_postcode(self):
        postcode_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.address_zip))
        postcode_input.clear()
        postcode_input.send_keys('11311')

    # adress inputs

    def leave_address_empty(self):
        address_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address1))
        address_input.clear()

    def fill_address_with_bool(self):
        address_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address1))
        address_input.clear()
        address_input.send_keys(bool)

    def fill_address_with_one_character(self):
        address_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address1))
        address_input.clear()
        address_input.send_keys('1')

    def fill_address_with_special_characters(self):
        address_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address1))
        address_input.clear()
        address_input.send_keys('Street!@#$%^*"')

    def fill_address_with_upper_cases(self):
        address_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address1))
        address_input.clear()
        address_input.send_keys('StREeT 1')

    def fill_address_with_trailing_and_leading_spaces(self):
        address_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address1))
        address_input.clear()
        address_input.send_keys('  Street 1  ')

    def fill_address_with_only_numbers(self):
        address_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address1))
        address_input.clear()
        address_input.send_keys('123123')

    def fill_address_with_javascript_alert(self):
        address_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address1))
        address_input.clear()
        address_input.send_keys('javascript:alert(document.cookie)')

    def fill_address_with_javascript_propmt(self):
        address_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address1))
        address_input.clear()
        address_input.send_keys('javascript:prompt(document.cookie)')

    def fill_address_with_javascript_confirm(self):
        address_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address1))
        address_input.clear()
        address_input.send_keys('javascript:confirm(document.cookie)')

    def fill_address(self):
        address_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address1))
        address_input.clear()
        address_input.send_keys('Street 1')

    # second adress inputs

    def leave_address_2_empty(self):
        address_2_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address2))
        address_2_input.clear()

    def fill_address_2_with_bool(self):
        address_2_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address2))
        address_2_input.clear()
        address_2_input.send_keys(bool)

    def fill_address_2_with_one_character(self):
        address_2_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address2))
        address_2_input.clear()
        address_2_input.send_keys('S')

    def fill_address_2_with_special_characters(self):
        address_2_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address2))
        address_2_input.clear()
        address_2_input.send_keys('Street2!@#$%^*"')

    def fill_address_2_with_upper_cases(self):
        address_2_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address2))
        address_2_input.clear()
        address_2_input.send_keys('StREeT 2')

    def fill_address_2_with_trailing_and_leading_spaces(self):
        address_2_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address2))
        address_2_input.clear()
        address_2_input.send_keys('  Street 2  ')

    def fill_address_2_with_only_numbers(self):
        address_2_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address2))
        address_2_input.clear()
        address_2_input.send_keys('123123')

    def fill_address_2_with_javascript_alert(self):
        address_2_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address2))
        address_2_input.clear()
        address_2_input.send_keys('javascript:alert(document.cookie)')

    def fill_address_2_with_javascript_propmt(self):
        address_2_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address2))
        address_2_input.clear()
        address_2_input.send_keys('javascript:prompt(document.cookie)')

    def fill_address_2_with_javascript_confirm(self):
        address_2_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address2))
        address_2_input.clear()
        address_2_input.send_keys('javascript:confirm(document.cookie)')

    def fill_address_2(self):
        address_2_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.address2))
        address_2_input.clear()
        address_2_input.send_keys('Street 2')

    # city inputs

    def leave_city_empty(self):
        city_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.city))
        city_input.clear()

    def fill_city_with_bool(self):
        city_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.city))
        city_input.clear()
        city_input.send_keys(bool)

    def fill_city_with_numbers(self):
        city_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.city))
        city_input.clear()
        city_input.send_keys('123456')

    def fill_city_with_one_letter(self):
        city_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.city))
        city_input.clear()
        city_input.send_keys('C')

    def fill_city_with_trailing_and_leading_spaces(self):
        city_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.city))
        city_input.clear()
        city_input.send_keys('  City  ')

    def fill_city_with_various_symbols(self):
        city_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.city))
        city_input.clear()
        city_input.send_keys('City!@#$%^*"')

    def fill_city_with_javascript_alert(self):
        city_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.city))
        city_input.clear()
        city_input.send_keys('javascript:alert(document.cookie)')

    def fill_city_with_javascript_propmt(self):
        city_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.city))
        city_input.clear()
        city_input.send_keys('javascript:prompt(document.cookie)')

    def fill_city_with_javascript_confirm(self):
        city_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id(self.city))
        city_input.clear()
        city_input.send_keys('javascript:confirm(document.cookie)')

    def fill_city(self):
        city_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.city))
        city_input.clear()
        city_input.send_keys('City')

        # Finish button

    def click_finish_button(self):
        button = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(self.finish))
        button.click()

    def select_shares(self):
        shares_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(self.shares))
        shares_input.click()

        time.sleep(0.1)

        shares_item = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(
            self.shares_items + '[1]'))
        shares_item.click()

    def select_forex(self):
        forex_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(self.forex))
        forex_input.click()

        time.sleep(0.1)

        forex_item = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(
            self.forex_items + '[1]'))
        forex_item.click()

    def select_cfds(self):
        cfds_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(self.cfds))
        cfds_input.click()

        time.sleep(0.1)

        cfds_item = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(
            self.cfds_items + '[1]'))
        cfds_item.click()

    def select_spread_betting(self):
        spread_betting_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_xpath(self.spread_betting))
        spread_betting_input.click()

        time.sleep(0.1)

        spread_betting_item = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(
            self.spread_betting_items + '[1]'))
        spread_betting_item.click()

    def select_relevant_experience(self):
        relevant_experience_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_xpath(self.relevant_experience))
        relevant_experience_input.click()

        time.sleep(0.1)

        relevant_experience_item = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_xpath(self.relevant_experience_items + '[1]'))
        relevant_experience_item.click()

    def select_trading_accounts(self):
        trading_accounts_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_xpath(self.trading_accounts))
        trading_accounts_input.click()

        time.sleep(0.1)

        trading_accounts_item = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(
            self.trading_accounts_items + '[1]'))
        trading_accounts_item.click()

    def select_trading_currency(self):
        trading_currency_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_xpath(self.trading_currency))
        trading_currency_input.click()

        time.sleep(0.1)

        trading_currency_item = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(
            self.trading_currency_items + '[1]'))  # can't find li[2]
        trading_currency_item.click()

    def select_annual_income(self):
        annual_income_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_xpath(self.annual_income))
        annual_income_input.click()

        time.sleep(0.1)

        annual_income_item = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(
            self.annual_income_items + '[1]'))
        annual_income_item.click()

    def select_employment_status(self):
        employment_status_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_xpath(self.employment_status))
        employment_status_input.click()

        time.sleep(0.1)

        employment_status_item = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(
            self.employment_status_items + '[1]'))
        employment_status_item.click()

    def select_liquid_savings(self):
        liquid_savings_input = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_xpath(self.liquid_savings))
        liquid_savings_input.click()

        time.sleep(0.1)

        liquid_savings_item = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(
            self.liquid_savings_items + '[1]'))
        liquid_savings_item.click()

    def check_terms_and_conditions(self):
        terms_and_conditions_input = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(
            self.terms_and_conditions))
        terms_and_conditions_input.click()