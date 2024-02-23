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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    
    
    def click(self, web_element: WebElement, info: str = ""):
        if (info != ""):
            print(f"Executing click -> {info}")
        web_element.click()
                
    
    def handle_exception(self, locator: str, locator_type: str, exception: Exception) -> None:
        print(f"Element with {locator_type} '{locator}' not found or not interactable: {exception}")


    def find_elements_by_locator(self, locator_type: str, locator: str, multiple: bool = False, wait_time: int = 0, parent_element: WebElement = None) -> Union[WebElement, List[WebElement]]:
        try:
            # Wait for the element to be present
            WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((getattr(By, locator_type.upper()), locator))
            )

            if locator_type == "id":
                
                if multiple:
                    if parent_element:
                        return parent_element.find_elements(By.Id, locator)
                    else:
                        return self.driver.find_elements(By.ID, locator)
                else:
                    if parent_element:
                        return parent_element.find_element(By.ID, locator)
                    else:
                        return self.driver.find_element(By.ID, locator)
            elif locator_type == "xpath":
                if multiple:
                    if parent_element:
                        return parent_element.find_elements(By.XPATH, locator)
                    else:
                        return self.driver.find_elements(By.XPATH, locator)
                else:
                    if parent_element:
                        return parent_element.find_element(By.XPATH, locator)
                    else:
                        return self.driver.find_element(By.XPATH, locator)
            elif locator_type == "class_name":
                if multiple:
                    if parent_element:
                        return parent_element.find_elements(By.CLASS_NAME, locator)
                    else:
                        return self.driver.find_elements(By.CLASS_NAME, locator)
                else:
                    if parent_element:
                        return parent_element.find_element(By.CLASS_NAME, locator)
                    else:
                        return self.driver.find_element(By.CLASS_NAME, locator)
            elif locator_type == "tag_name":
                if multiple:
                    if parent_element:
                        return parent_element.find_elements(By.TAG_NAME, locator)
                    else:
                        return self.driver.find_elements(By.TAG_NAME, locator)
                else:
                    if parent_element:
                        return parent_element.find_element(By.TAG_NAME, locator)
                    else:
                        return self.driver.find_element(By.TAG_NAME, locator)
            elif locator_type == "css_selector":
                if multiple:
                    if parent_element:
                        return parent_element.find_elements(By.CSS_SELECTOR, locator)
                    else:
                        return self.driver.find_elements(By.CSS_SELECTOR, locator)
                else:
                    if parent_element:
                        return parent_element.find_element(By.CSS_SELECTOR, locator)
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

    
    def find_element_by_id(self, element_id: str, parent_element: WebElement = None, wait_time: int = 0) -> WebElement:
        return self.find_elements_by_locator(locator_type="id", locator=element_id, parent_element=parent_element, wait_time=wait_time)

    def find_element_by_xpath(self, xpath: str, parent_element: WebElement = None, wait_time: int = 0) -> WebElement:
        return self.find_elements_by_locator(locator_type="xpath", locator=xpath, parent_element=parent_element, wait_time=wait_time)

    def find_element_by_class_name(self, class_name: str, parent_element: WebElement = None, wait_time: int = 0) -> WebElement:
        return self.find_elements_by_locator(locator_type="class_name", locator=class_name, parent_element=parent_element, wait_time=wait_time)

    def find_element_by_tag_name(self, tag_name: str, parent_element: WebElement = None, wait_time: int = 0) -> WebElement:
        return self.find_elements_by_locator(locator_type="tag_name", locator=tag_name, parent_element=parent_element, wait_time=wait_time)

    def find_element_by_css_selector(self, css_selector: str, parent_element: WebElement = None, wait_time: int = 0) -> WebElement:
        return self.find_elements_by_locator(locator_type="css_selector", locator=css_selector, parent_element=parent_element, wait_time=wait_time)

    def find_elements_by_id(self, element_id: str, parent_element: WebElement = None, wait_time: int = 0) -> List[WebElement]:
        return self.find_elements_by_locator(locator_type="id", locator=element_id, parent_element=parent_element, wait_time=wait_time, multiple=True)

    def find_elements_by_xpath(self, xpath: str, parent_element: WebElement = None, wait_time: int = 0) -> List[WebElement]:
        return self.find_elements_by_locator(locator_type="xpath", locator=xpath, parent_element=parent_element, wait_time=wait_time, multiple=True)

    def find_elements_by_class_name(self, class_name: str, parent_element: WebElement = None, wait_time: int = 0) -> List[WebElement]:
        return self.find_elements_by_locator(locator_type="class_name", locator=class_name, parent_element=parent_element, wait_time=wait_time, multiple=True)

    def find_elements_by_tag_name(self, tag_name: str, parent_element: WebElement = None, wait_time: int = 0) -> List[WebElement]:
        return self.find_elements_by_locator(locator_type="tag_name", locator=tag_name, parent_element=parent_element, wait_time=wait_time, multiple=True)

    def find_elements_by_css_selector(self, css_selector: str, parent_element: WebElement = None, wait_time: int = 0) -> List[WebElement]:
        return self.find_elements_by_locator(locator_type="css_selector",locator= css_selector, parent_element=parent_element, wait_time=wait_time, multiple=True)

    

    def navigate(self, url, idle: int = randint(10, 15)):
        print("Navigating to ", url)
        self.driver.get(url=url)
        custom_sleep_func_3(message="Idle after navigating to url", time_in_seconds=idle)
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
    
    
    # def make_a_scroll(driver: any, type: str = '', web_element: str='', try_scroll_for: int=1):
    #     # method scroll modal window (followers modal window)
    #     # params driver
    #     # params type
        
    #     # random_sleep(2, 4)  # Going idle for a few seconds
    #     # random_sleep(1, 2)  # Going idle for a few seconds

    #     if (type == 'modal_window_scroll'): # modal window scroll
    #         custom_print('Scrolling modal window.', bg_colors.OKBLUE)
    #         WebDriverWait(driver, 10).until(lambda d: d.find_element(By.CSS_SELECTOR, 'div[role="dialog"]'))
    #         driver.execute_script('''var fDialog = document.querySelector('div[role="dialog"] .isgrP');fDialog.scrollTop = fDialog.scrollHeight''')
    #         random_sleep(3,4)

    #     if (type == 'main_window_scroll'):  # main window scroll
    #         custom_print('Scrolling main window', bg_colors.OKBLUE)
    #         driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #         random_sleep(1, 2)
            
        
    #     if (type == 'make_scroll_by_web_element'):
    #         custom_print('Scrolling window', bg_colors.OKBLUE)
    #         driver.execute_script("arguments[0].scrollIntoView()",web_element)
    #         random_sleep(3, 4)
            
    #     if (type == "make_smooth_scroll_by_web_element"):
    #         for i in range(1, try_scroll_for+1):
    #             custom_print(f'Scrolling window (try->{i}/{try_scroll_for})', bg_colors.OKBLUE)
    #             driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'end', inline: 'end' });", web_element)
    #             random_sleep(2, 3)
                
                
    def __post_init__(self):
        
        if self.un_detectable:
            self.create_undetectable_chrome_driver()
        elif(self.port != ""):
            self.create_undetectable_chrome_driver(chrome_driver_path="/Users/ahsanilyas/Documents/FiverrSEO/scraper/chromedriver", port=self.port)
        # Call create_web_driver after the instance is initialized
        else:
            self.create_web_driver()

