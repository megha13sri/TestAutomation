from workday_api import *
from downloadFile import *
from super_base_class import *

class test_same_group:

    def __init__(self, int_sys_id, action_wid):
        self.int_sys_id = int_sys_id
        self.action_wid = action_wid

    def remove_existing_file(self):

        file_path = os.getcwd() + "/Output_File.xml"
        logger.debug(file_path)

        try:
            os.remove(file_path)
            logger.debug("old XML File is removed successfully")
        except Exception as e:
            logger.error("File is not present")


    def launch_apis(self):

        a = workday_api(work_day_usname, work_day_password)
        res = a.get_api(tenant_name, "Action_Event", "Get_-WIN_and_Timestamp", self.action_wid)
        logger.debug("this is get API output")
        logger.debug(res)


        report_entry = res['Report_Entry'][0]
        effective_date = report_entry['Effective_Date']
        entry_date = report_entry['Entry_Date']
        action = report_entry["Action"]
        associate_id = report_entry["Associate_ID"]
        location_proposed = report_entry["Location_Proposed"]
        proposed_pos_id = report_entry["Proposed_Pos_ID"]


        updated_from = a.get_update_from_date(entry_date)
        logger.debug("this is new update from :" + updated_from)
        updated_through, current_date = a.get_current_time_stamp()
        logger.debug("this is new updated through :" + updated_through)
        logger.debug("this is current date :" + current_date)

        #this is only meant for this integration 9 script .


        #Getting updated XML payload for soap request to launch integration
        xml_data = a.get_updated_xml("integration_launch_xml.txt", updated_from,
                                 associate_id, effective_date, self.int_sys_id,
                                 updated_through, current_date)

        logger.info("this is launching XML file")
        logger.info("--------------------------")
        logger.info(xml_data)
        logger.info("--------------------------")

        # launching the integration
        xml_resp = a.launch_integration_api(integration_launch_url, xml_data)
        int_wid_id = a.get_wid_id_from_resp(xml_resp)
        logger.debug("This is Integration wid after launch " + int_wid_id)

        #wait time to complete the integration.
        logger.debug("Waiting 40 secs for integration to complete...")
        time.sleep(40)

        updated_xml_data = a.get_updated_xml_for_event_doc(int_wid_id)
        logger.debug("this XML data for 2nd SOAP request")
        logger.debug(updated_xml_data)
        xml_data = a.launch_integration_api(integration_launch_url, updated_xml_data)

        wid = a.check_file_wid_from_xml(xml_data)
        logger.debug("This is wid from file response " + wid)

        document_id = a.get_document_id_from_xml(xml_data)

        time.sleep(10)
        #########################################################

        #driver = Login_Workday.get_driver()

        #d = Login_Workday(work_day_url, work_day_usname, work_day_password)
        #d.do_login(driver)
        #wid_number = wid
        #d.get_file_from_wid(driver, wid_number)

        #time.sleep(10)

        api_url = file_download_url + document_id
        xml_data = a.get_file_from_document_id(api_url)

        ###validation of downloaded file
        #fd = open("Output_File.xml", "r")
        #xml_data = fd.read()
        xml_data = a.get_pretty_print_xml(xml_data)

        logger.info("this is downloaded file data")
        logger.info(xml_data)
        emp_id = a.get_tag_vale_from_xml(xml_data, "Employee_ID")
        pos_id = a.get_tag_vale_from_xml(xml_data, "Position_ID")
        business_site = a.get_tag_vale_from_xml(xml_data, "Business_Site")
        action_name = a.get_tag_vale_from_xml(xml_data, "Transaction_Log_Type")

        if business_site == location_proposed:
            logger.debug("validation for location is passed")
        else:
            logger.error("validation for location is failed")

        if emp_id == associate_id:
            logger.debug("validation for emp_id is passed")
        else:
            logger.error("validation for emp_id is failed")


        if pos_id == proposed_pos_id:
            logger.debug("validation for position ID is passed")
        else:
            logger.error("validation for position ID is failed")

        if business_site == location_proposed:
            logger.debug("validation for business site is passed")
        else:
            logger.error("validation for business site is failed")

        if action_name == action:
            logger.debug("validation for action name is passed")
        else:
            logger.error("validation for action name is failed")


    def run_testcase(self):

        try:
            self.remove_existing_file()
            self.launch_apis()
        except Exception as e:
            print("arjunn gupta")
            logger.exception("Testcase is failed because of below error\n\n" + str(e))




