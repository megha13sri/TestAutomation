import re
import xml.dom.minidom

import requests

from super_base_class import *


class workday_api(object):
    def __init__(self, username , password):
        self.username = username
        self.password = password

    def get_api(self, tenant_name, event_parameter,
                service_name, option_param_val, retry_count = 3):
        if event_parameter == "Action_Event":
            api_url = "https://wd5-impl-services1.workday.com/ccx/service/\
customreport2/{}/{}/{}?Action_Event%21WID={}&\
format=json".format(tenant_name, self.username, service_name, option_param_val)

        logger.debug(api_url)
        while retry_count > 0:
            try:
                response = requests.get(api_url, auth=(self.username, self.password))
                logger.debug(response.status_code)
                return response.json()
            except Exception as e:
                logger.error("Request is not connected trying again")
                retry_count -= 1

    def get_file_from_document_id(self, api_url):
        """
        this method is used to downlod the file from document id
        :param document_id:
        :return:
        """
        user_name = "{}@walmart{}".format(self.username, tenant_number)

        response = requests.get(api_url, auth=(user_name, self.password))
        logger.debug(response.status_code)
        return response.text


    @staticmethod
    def get_update_from_date(entry_date):
        pat  = re.match("(.*)-(.*)$", entry_date)
        temp = pat.groups()[0]
        #to handle time stamp string
        date_obj = datetime.datetime.strptime(temp, "%Y-%m-%dT%H:%M:%S.%f")

        # to get the epoch value
        epoch = datetime.datetime(1970, 1, 1)
        epoch_time = date_obj - epoch
        time_diff = int(epoch_time.total_seconds())
        new_epoch_time = time_diff - 1

        date_new = datetime.datetime.fromtimestamp(new_epoch_time-GMT_TIME_ZONE_DIFF)
        final_time_stamp = date_new.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return final_time_stamp


    @staticmethod
    def get_current_time_stamp():
        time_ob = datetime.datetime.fromtimestamp(datetime.datetime.now().timestamp() - PST_TIME_ZONE_DIFF)
        current_timestamp = time_ob.strftime('%Y-%m-%dT%H:%M:%S.%f')
        current_date = current_timestamp.split("T")[0]
        return current_timestamp, current_date


    def launch_integration_api(self, url, xml_data):
        header = {
            "Content-Type": "application/xml"
        }
        res = requests.post(url, data = xml_data, headers= header)

        logger.debug(res.status_code)
        logger.debug(res.text)
        return res.text

    def get_updated_xml(self, xml_file_name, updated_from,
                        associate_id, effective_date, int_sys_id, updated_through, current_date):
        fd = open(xml_file_name, "r")
        xml_data = fd.read()
        xml_data = xml_data.replace("$Username", self.username + "@walmart" + tenant_number)
        xml_data = xml_data.replace("$Password", self.password)
        xml_data = xml_data.replace("$Associate_ID", associate_id)
        xml_data = xml_data.replace("$Effective_Through", current_date)
        xml_data = xml_data.replace("$Effective_From", effective_date)
        xml_data = xml_data.replace("$INT_Sys_ID", int_sys_id)
        xml_data = xml_data.replace("$Updated_From", updated_from)
        xml_data = xml_data.replace("$Updated_Through", updated_through)

        return xml_data

    def get_wid_id_from_resp(self, xml_resp):
        pat = "wd:ID wd:type=\"WID\">(.*?)</wd:ID"
        if re.search(pat,xml_resp):
            return re.search(pat,xml_resp).groups()[0]


    def get_updated_xml_for_event_doc(self, wid_value):
        fd = open("get_event_document.txt", "r")
        xml_data = fd.read()
        xml_data = xml_data.replace("$Username", self.username + "@walmart" + tenant_number)
        xml_data = xml_data.replace("$Password", self.password)
        xml_data = xml_data.replace("$WID_Integration_event", wid_value)

        return xml_data


    def get_pretty_print_xml(self, xml_data):

        dom1 = xml.dom.minidom.parseString(xml_data)
        b = dom1.toprettyxml(indent='    ')

        return b

    def check_file_wid_from_xml(self, xml_data):

        dom1 = xml.dom.minidom.parseString(xml_data)
        b = dom1.toprettyxml(indent='    ')

        find_rep_doc_ref = False
        find_rep_doc_ref_line = 0
        current_wid = ""
        counter = 0

        for line in b.split("\n"):
            if line.strip() == "<wd:Repository_Document>":
                find_rep_doc_ref = True
                find_rep_doc_ref_line = counter
            if counter == find_rep_doc_ref_line + 2 and find_rep_doc_ref:
                pat = re.search(">(.*)<", line)
                if pat:
                    current_wid = pat.groups()[0]
            if "text/xml" in line:
                break
            if "</wd:Repository_Document>" == line.strip():
                find_rep_doc_ref = False
                find_rep_doc_ref_line = 0
                current_wid = ""

            counter += 1

        return current_wid

    def get_document_id_from_xml(self, xml_data):

        dom1 = xml.dom.minidom.parseString(xml_data)
        b = dom1.toprettyxml(indent='    ')

        find_rep_doc_ref = False
        find_rep_doc_ref_line = 0
        current_document = ""
        counter = 0

        for line in b.split("\n"):
            if line.strip() == "<wd:Repository_Document>":
                find_rep_doc_ref = True
                find_rep_doc_ref_line = counter
            if counter == find_rep_doc_ref_line + 3 and find_rep_doc_ref:
                pat = re.search(">(.*)<", line)
                if pat:
                    current_document = pat.groups()[0]
            if "text/xml" in line:
                break
            if "</wd:Repository_Document>" == line.strip():
                find_rep_doc_ref = False
                find_rep_doc_ref_line = 0
                current_document = ""

            counter += 1

        return current_document


    def get_tag_vale_from_xml(self, xml_data, tag):
        patt = "ws:{}>(.*)<".format(tag)
        for line in xml_data.split("\n"):
            pt = re.search(patt, line)
            if pt:
                return pt.groups()[0]

        return None

