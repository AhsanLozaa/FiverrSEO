from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from seleniumwire import webdriver as wiredriver
from fake_useragent import UserAgent
from dataclasses import dataclass, field
import undetected_chromedriver as uc

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
    
    
    
    def create_web_driver_for_the_current_active_chrome_tab(self, chrome_driver_path, port='9222'):
        # custom_port_address = f'127.0.0.1:{port}'

        chrome_options = Options()
        # chrome_options.add_experimental_option("debuggerAddress", custom_port_address)

        # service = Service(executable_path=chrome_driver_path)  # Create a service with the executable path
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
        if (self.port != ""):
            self.create_web_driver_for_the_current_active_chrome_tab(chrome_driver_path="/Users/ahsanilyas/Documents/FiverrSEO/scraper/chromedriver", port=self.port)
        # Call create_web_driver after the instance is initialized
        else:
            self.create_web_driver()

