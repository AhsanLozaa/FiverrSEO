from dataclasses import dataclass, field
from enum import Enum

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from scraper.custom_web_driver import CustomWebDriver

class PlanType(Enum):
    BASIC = "basic"
    STANDARD = "standard"
    PREMIUM = "premium"

@dataclass
class Plan:
    name: PlanType
    text: str = field(default="")
    html: str = field(default="")
    

@dataclass
class PricingData:
    plans: list[Plan] = field(default_factory=list)
    
    def set_pricing_data(self, custom_web_driver: CustomWebDriver) -> None:
        
        package_elements = []
        try:
            package_elements = custom_web_driver.driver.find_element(By.CLASS_NAME, "nav-container").find_elements(By.TAG_NAME, "label")
            for elem in package_elements:
                try:
                    elem_text = elem.text.lower() # where elem_text = "basic"
                    existing_plan = next((plan for plan in self.plans if plan.name.value == elem_text), None)

                    if existing_plan is None:
                        # Plan doesn't exist, create a new one and append it to the list
                        text = custom_web_driver.driver.find_element(By.CLASS_NAME, "package-content").text
                        html = custom_web_driver.driver.find_element(By.CLASS_NAME, "package-content").get_attribute('outerHTML')
                        new_plan = Plan(name=PlanType[elem_text.upper()], text=text, html=html)
                        self.plans.append(new_plan)

                except Exception as e:
                    continue
            # return if success
            return
        except NoSuchElementException as e:
            pass
            
            
        try:
            text = custom_web_driver.driver.find_element(By.CLASS_NAME, "packages-tabs, single").text
            html = custom_web_driver.driver.find_element(By.CLASS_NAME, "packages-tabs, single").get_attribute("outerHTML")
            new_plan = Plan(name=PlanType.BASIC, text=text, html=html)
            
            # return if success
            return
        except Exception as e:
            print(e)
            print("Failed to fetch the pricing data")
            
        
            
    
    def get_plan(self, plan_type: PlanType) -> PlanType:
        
        try:
            plan_obj = [plan for plan in self.plans if plan.name == plan_type][0]
            modified_dict = {
                'name': plan_obj.name.value,  # Get the actual value using .value
                'text': plan_obj.text,
                'html': plan_obj.html
            }
            
            return modified_dict

        except Exception as e:
            return None
        