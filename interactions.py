from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Session :
    def __init__(self, headless = False):
        options = Options()
        options.add_argument("--log-level=3") 
        prefs = {
            "profile.managed_default_content_settings.images": 2,
            "profile.managed_default_content_settings.stylesheets": 2,
            "profile.managed_default_content_settings.fonts": 2,
        }
        options.add_experimental_option("prefs", prefs) 
        if headless :
            options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")  
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=options)  
        self.driver.get('https://goalieup.com/en/user')

    def connect(self) :
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "name"))).send_keys("yarnogrenier@gmail.com")
        self.driver.find_element(By.NAME, "pass").send_keys("9jaz84P6&abc")
        self.driver.find_element(By.NAME, "op").click() 
        print("Connected")

    def get_html(self) :
        return self.driver.page_source
    
    def click_on_game(self, link) :
        self.driver.find_element(By.XPATH, f"//a[@href='{link}']").click()

    def sign_up(self) :
        pass

    def quit(self) :
        self.driver.quit()

if __name__ == "__main__" :
    s = Session(True)
    s.connect()
    print(s.get_html())
    print("Got html")
    s.quit()
