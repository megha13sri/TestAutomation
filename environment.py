import os

##########
# env variables
##########
log_level: str = "DEBUG"
automation_log_dir = os.getcwd() + "/logs/"
tenant_number = "7"
CHROM_DRIVER_PATH = "D:/chrom_driver/chromedriver.exe"
work_day_url = "https://wd5-impl.workday.com/wday/authgwy/walmart{}/" \
               "login.htmld?returnTo=%2fwalmart{}%2fd%2fhome.htmld/".format(tenant_number, tenant_number)
work_day_usname = "n0s01nx"
work_day_password = "Walmart@2024"
# currently laptpn time is in IST so time diff with GMT is 5:50 hr which is in Sec 19800
GMT_TIME_ZONE_DIFF = 19800
PST_TIME_ZONE_DIFF = 45000
file_download_url = "https://wd5-impl-services1.workday.com/ccx/cc-blobitory/walmart{}/".format(tenant_number)
tenant_name = "walmart{}".format(tenant_number)


#######################
# Xpath variable
#######################
integration_launch_url = "https://wd5-impl-services1.workday.com/ccx/service/walmart{}/Integrations/v40.2".format(tenant_number)
Xpath_Native = "//div[@class='gwt-Label GDPVGE1BM1' and @data-automation-id='authSelectorOptionLabel' and text()='Native Login']"
Xpath_UserName = "//input[@class='gwt-TextBox GDPVGE1BC3B' and @aria-label='Username']"
Xpath_Password = "//input[@class='gwt-PasswordTextBox GDPVGE1BC3B' and @aria-label='Password']"
Xpath_SignIn = "//button[@class='GDPVGE1BOSC' and text() = 'Sign In']"
Xpath_Sibling_Quest = "//input[@aria-label='In what city does your nearest sibling live?']"
Xpath_Telephone_Quest = "//input[@aria-label='What were the last four digits of your childhood telephone number?']"
Xpath_Submit = "//button[text() = 'Submit']"
Xpath_Search_Box = "//input[@data-automation-id='globalSearchInput' and @placeholder='Search']"
Xpath_Search_Input = "//input[@data-automation-id='globalSearchInput' and @type='search']"
Xpath_Click_File = "//a[@data-automation-id='pex-search-results-header-title-link' and text()='Output_File.xml']"
Xpath_File_Details = "//span[@title='Details' and text()='Details']"
Xpath_File_Image = "//div[@data-automation-id='promptOption' and text()='Output_File.xml']"
Xpath_Integration_link = "//a[@data-automation-id='pex-search-results-header-title-link']"

###################
# integration variables
##################
int_sys_id_09 = "INT009-Stronghold_Critical_Transaction-SI-Outbound/INT009-Stronghold_Critical_Transaction-SI-Outbound/Start-INT009-Adhoc"
action_wid_09 = "a6bdab8bdecd1022a5271c168e790000"

int_sys_id_08 = "INT008-Stronghold_Demographic_Changes-SI-Outbound/INT008-Stronghold_Demographic_Changes-SI-Outbound/Start-INT008-Adhoc"
action_wid_08 = "236b69c820b1101caaf633f1535e0000"

int_sys_id_230 = "INT230-GBL-WorkdaytoStronghold-Rescinds-SI/INT230-GBL-WorkdaytoStronghold-Rescinds-SI/Adhoc-Start-INT230"
action_wid_230 = "0e9b26ef71911022aae134410da40000"

int_sys_id_11 = "INT011-Stronghold_Future_Transacation-SI-Outbound/INT011-Stronghold_Future_Transacation-SI-Outbound/Start-INT011"
action_wid_11 = "06a84c99c07c101b4672119009220000"



