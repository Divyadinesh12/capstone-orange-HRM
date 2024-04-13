class Web_Locator:
    """
    This class is used to contain all the data that are required to perform the testing for the orange HRM header and main menu validation on admin page

        """

    def __init__(self):
        self.Forget_password_Locator="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p"
        self.Reset_UserName_Input_Locator="/html/body/div/div[1]/div[1]/div/form/div[1]/div/div[2]/input"
        self.Reset_Button_Locator="/html/body/div/div[1]/div[1]/div/form/div[2]/button[2]"
        self.UserName_Locator="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        self.Password_Input_Locator="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        self.Login_Button_Locator="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
        self.Admin_Locator="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"

