from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from seleniumwire import webdriver as wiredriver
from fake_useragent import UserAgent
from dataclasses import dataclass, field
import undetected_chromedriver as uc
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List, Union
from selenium.common.exceptions import (
    NoSuchElementException, 
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    ElementNotSelectableException,
    ElementNotVisibleException
)

from utils import custom_sleep_func_3

@dataclass
class CustomWebDriver:
    
    headless: bool = field(default=False)
    user_agent: str = field(default="")
    port: str = field(default="")
    driver: webdriver.Chrome = field(default=None)
    allow_proxy: bool = field(default=True)
    proxy_address: str = field(default="38.154.227.167")
    proxy_port: str = field(default="5868")
    proxy_username: str = field(default="eyteicsm")
    proxy_password: str = field(default="9c3q3ath8l6u")

    un_detectable: bool = field(default=False)
    user_data_dir: str = field(default="")
    
    def handle_exception(self, locator: str, locator_type: str, exception: Exception) -> None:
        print(f"Element with {locator_type} '{locator}' not found or not interactable: {exception}")


    def find_elements_by_locator(self, locator_type: str, locator: str, multiple: bool = False) -> Union[WebElement, List[WebElement]]:
        try:
            if locator_type == "id":
                if multiple:
                    return self.driver.find_elements(By.ID, locator)
                else:
                    return self.driver.find_element(By.ID, locator)
            elif locator_type == "xpath":
                if multiple:
                    return self.driver.find_elements(By.XPATH, locator)
                else:
                    return self.driver.find_element(By.XPATH, locator)
            elif locator_type == "class_name":
                if multiple:
                    return self.driver.find_elements(By.CLASS_NAME, locator)
                else:
                    return self.driver.find_element(By.CLASS_NAME, locator)
            elif locator_type == "tag_name":
                if multiple:
                    return self.driver.find_elements(By.TAG_NAME, locator)
                else:
                    return self.driver.find_element(By.TAG_NAME, locator)
            elif locator_type == "css_selector":
                if multiple:
                    return self.driver.find_elements(By.CSS_SELECTOR, locator)
                else:
                    return self.driver.find_element(By.CSS_SELECTOR, locator)
            else:
                raise ValueError(f"Unsupported locator type: {locator_type}")
        except (
            NoSuchElementException, 
            TimeoutException,
            StaleElementReferenceException,
            ElementClickInterceptedException,
            ElementNotInteractableException,
            ElementNotSelectableException,
            ElementNotVisibleException
        ) as e:
            self.handle_exception(locator, locator_type, e)
            return [] if multiple else None


    
    def find_element_by_id(self, element_id: str) -> WebElement:
        return self.find_elements_by_locator("id", element_id)

    def find_element_by_xpath(self, xpath: str) -> WebElement:
        return self.find_elements_by_locator("xpath", xpath)

    def find_element_by_class_name(self, class_name) -> WebElement:
        return self.find_elements_by_locator("class_name", class_name)
    
    def find_element_by_tag_name(self, tag_name) -> WebElement:
        return self.find_elements_by_locator("tag_name", tag_name)

    def find_element_by_css_selector(self, css_selector) -> WebElement:
        return self.find_elements_by_locator("css_selector", css_selector)
    

    def find_elements_by_id(self, element_id: str) -> list[WebElement]:
        return self.find_elements_by_locator("id", element_id)

    def find_elements_by_xpath(self, xpath: str) -> list[WebElement]:
        return self.find_elements_by_locator("xpath", xpath)

    def find_elements_by_class_name(self, class_name: str) -> list[WebElement]:
        return self.find_elements_by_locator("class_name", class_name)
    
    def find_elements_by_tag_name(self, tag_name: str) ->  list[WebElement]:
        return self.find_elements_by_locator("tag_name", tag_name)

    def find_elements_by_css_selector(self, css_selector: str) -> list[WebElement]:
        return self.find_elements_by_locator("css_selector", css_selector)
    

    def navigate(self, url):
        print("Navigating to ", url)
        self.driver.get(url=url)
        custom_sleep_func_3(message="Idle after navigating to url", time_in_seconds=randint(10, 15))
        print("Navigated to ", url)
    
    def create_undetectable_chrome_driver(self):
        chrome_options = Options()
        if self.user_data_dir and self.user_data_dir != "":
            # chrome_options.add_argument("user-data-dir={self.user_data_dir}")
            # chrome_options.add_argument('--profile-directory=Profile 2')
            chrome_options.add_argument(f"--user-data-dir={self.user_data_dir}") #Path to your chrome profile

        # port = "9222"
        # custom_port_address = f'127.0.0.1:{port}'
        # chrome_options.add_experimental_option("debuggerAddress", custom_port_address)
        driver = uc.Chrome(options=chrome_options)
        self.driver = driver

    def create_web_driver(self):
        try:
            chrome_options = Options()
            
            if self.headless:
                chrome_options.add_argument("--headless")
                
            # Other options and settings
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            chrome_options.add_argument('--disable-blink-features=AutomationControlled')
            
            # User agent
            if not self.user_agent:
                ua = UserAgent()
                self.user_agent = ua.random
            chrome_options.add_argument(f"user-agent={self.user_agent}")
            
            if (self.allow_proxy):
                
                # Proxy options
                proxy_options = {
                    'proxy': {
                        'http': f'http://{self.proxy_username}:{self.proxy_password}@{self.proxy_address}:{self.proxy_port}',
                        'https': f'https://{self.proxy_username}:{self.proxy_password}@{self.proxy_address}:{self.proxy_port}',
                        'no_proxy': 'localhost,127.0.0.1'
                    }
                }

                # Set up Selenium Chrome driver and assign it to self.driver
                self.driver = wiredriver.Chrome(seleniumwire_options=proxy_options, options=chrome_options)
            else:
                self.driver = wiredriver.Chrome(options=chrome_options)

        except Exception as e:
            print(e)
    
    def __post_init__(self):
        
        if self.un_detectable:
            self.create_undetectable_chrome_driver()
        elif(self.port != ""):
            print("fa kmsf askf aksf safkask f")
            self.create_undetectable_chrome_driver(chrome_driver_path="/Users/ahsanilyas/Documents/FiverrSEO/scraper/chromedriver", port=self.port)
        # Call create_web_driver after the instance is initialized
        else:
            print("fa kmsf askf aksf safkask f")
            self.create_web_driver()

