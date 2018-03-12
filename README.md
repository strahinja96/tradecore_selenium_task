# Tradecore Selenium Task

Python version: 2.7.14  
Selenium version: 3.10.0  
Google Chrome driver: 2.33  

The purpose of this task was to write automated test for a given sign up form. 
The tests are declared in file 'base.py' and there is a method for each test case covered in exel file 'Test_Cases_Documentation.xlsx'.
Different test case scenarios can be achieved by calling a corresponding method which contains a desired test combination. 
Example: 

        `self.fill_first_name()
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

        time.sleep(2)

        self.select_shares()
        self.select_forex()
        self.select_cfds()
        self.select_spread_betting()
        self.select_relevant_experience()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.select_trading_accounts()
        self.select_trading_currency()
        self.select_annual_income()
        self.select_employment_status()
        self.select_liquid_savings()
        self.check_terms_and_conditions()

        self.click_finish_button()`
        
This is an example of test where all inputs are valid (like in test case 'TC_001'. 
If you want to test another scenario, you simply switch one of the method calls with another.

Example: 

        `self.fill_first_name_with_trailing_and_leading_spaces()
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

        time.sleep(2)

        self.select_shares()
        self.select_forex()
        self.select_cfds()
        self.select_spread_betting()
        self.select_relevant_experience()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.select_trading_accounts()
        self.select_trading_currency()
        self.select_annual_income()
        self.select_employment_status()
        self.select_liquid_savings()
        self.check_terms_and_conditions()

        self.click_finish_button()`
        
This test will fill first name with string with trailing and leading spaces, and fill all other fields with valid data like in test case 'TC_001'.
