# own package
from Data import data
from Locators import locator
from Methods import methods
# common
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# Exception
from selenium.common.exceptions import NoSuchElementException

# sleep
from time import sleep
# pytest
import pytest
class Test_Header_Main_menu:

    @pytest.fixture()
    def boot(self):
        """
        This method open the url and maximize window
        :return: None
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        #  close the browser
        self.driver.quit()

    @pytest.mark.html
    def test_forget_password_link(self,boot):
       """
       This method validate forget password link on login page
       :param boot:
       :return:
       """
       try:
          # click forget password link
          methods.WebMethods().clickButton(self.driver,locator.Web_Locator().Forget_password_Locator)
          # sent username and click reset password button
          methods.WebMethods().enterText(self.driver,locator.Web_Locator().Reset_UserName_Input_Locator,data.WebData().Reset_Password)
          methods.WebMethods().clickButton(self.driver,locator.Web_Locator().Reset_Button_Locator)
          sleep(5)
          print("successfully Reset Password")
          # check it navigate to send password reset page
          assert self.driver.current_url == data.WebData().Reset_Password_url

       except NoSuchElementException as e:
           print("Error: Element is not present in the webpage")

    @pytest.fixture()
    def login(self):
        """
        This method login page and navigate home page
        :return: move to Home page
        """
        # sent username and password and click login button
        methods.WebMethods().enterText(self.driver,locator.Web_Locator().UserName_Locator,data.WebData().User_Name)
        methods.WebMethods().enterText(self.driver,locator.Web_Locator().Password_Input_Locator,data.WebData().Pass_Word)
        methods.WebMethods().clickButton(self.driver,locator.Web_Locator().Login_Button_Locator)
        print("Login Success full")
        # ensure that we move to home page
        assert self.driver.current_url == data.WebData().DashBoardUrl

    @pytest.mark.html
    def test_HeaderValidation_OnAdminPage(self,boot,login):
      """
      This method validate Header on admin page
      :param boot:
      :param login:
      """
      try:
        sleep(5)
        # go to admin page and validate title of the page as  orange HRM
        methods.WebMethods().clickButton(self.driver,locator.Web_Locator().Admin_Locator)
        sleep(3)
        assert self.driver.title == data.WebData().title
        # validate below options are displaying on admin page
        Header_span_option=["User Management","Job","Organization","Configuration"]
        # we loop through each option and check its displayed
        for option in Header_span_option:
            # check each option is displayed on the admin page
            methods.WebMethods().Displayed(self.driver,f"//span[normalize-space()='{option}']")
            sleep(3)
            # this method give web text from web page
            web_text = self.driver.find_element(By.XPATH,f"//span[normalize-space()='{option}']").text
            # check web text is  equal to Header span options
            assert web_text == option
        print("All Option displayed")
        # validate below options are displaying on admin page
        Header_anchor_options=["Nationalities","Corporate Branding"]
        # we loop through each option and check its displayed
        for anchor_option in Header_anchor_options:
            # check each option is displayed on the admin page
                 methods.WebMethods().Displayed(self.driver,f"//a[normalize-space()='{anchor_option}']")
                 sleep(3)
                # this method give web text from web page
                 anchor_web_text=self.driver.find_element(By.XPATH,f"//a[normalize-space()='{anchor_option}']").text
            # check web text is  equal to header on admin page
                 assert anchor_web_text == anchor_option
        print("All Option displayed")
      except NoSuchElementException as e:
          print("Error:Element is not present in the webpage")

    @pytest.mark.html
    def test_Main_Menu_validation(self,boot,login):
        """
        This method validate Main menu on Admin page
        :param boot:
        :param login:
        """
        try:
            sleep(5)
            # go to admin page
            methods.WebMethods().clickButton(self.driver, locator.Web_Locator().Admin_Locator)
           # check below options are displaying on admin page
            Menu_options = ["Admin","PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory","Maintenance", "Buzz"]
           #  loop through each option and check its displayed
            for menu in Menu_options:
                # check each option is displayed on the admin page
                 methods.WebMethods().Displayed(self.driver,f"//span[normalize-space()='{menu}']")
                # this method give web text from web page
                 Menu_text=self.driver.find_element(By.XPATH,f"//span[normalize-space()='{menu}']").text
                 sleep(2)
                # ensure that web text is equal to main menu on admin page
                 assert Menu_text == menu
            print("All Option displayed")

        except NoSuchElementException as e:
            print("Error: Element is not present in the web page")






