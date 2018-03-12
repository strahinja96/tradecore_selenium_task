import time
import unittest
from base import base_test

class tc_001 (base_test):
    def test_base_case(self):
        driver = self.driver

        self.fill_first_name()
        self.fill_last_name()
        self.fill_email()
        self.fill_password()
        self.fill_password_conformation()
        self.fill_telephone()
        self.fill_birth_date()
        self.select_country()
        self.fill_postcode()
        self.fill_address()
        self.fill_city()
        self.click_finish_button()

        # Wait for next step page to load
        time.sleep(2)

        self.select_shares()
        self.select_forex()
        self.select_cfds()
        self.select_spread_betting()
        self.select_relevant_experience()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scrolls to the bottom of the page
        self.select_trading_accounts()
        self.select_trading_currency()
        self.select_annual_income()
        self.select_employment_status()
        self.select_liquid_savings()
        self.check_terms_and_conditions()

        self.click_finish_button()
        time.sleep(7)

if __name__ == '__main__':
    unittest.main()