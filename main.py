# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from super_base_class import *
set_my_logger("test_group_worker_integrations")
from test_case_1 import *

test_case1 = test_same_group(int_sys_id_09, action_wid_09)
test_case1.run_testcase()

test_case2 = test_same_group(int_sys_id_08, action_wid_08)
test_case2.run_testcase()

test_case3 = test_same_group(int_sys_id_230, action_wid_230)
test_case3.run_testcase()

test_case4 = test_same_group(int_sys_id_11, action_wid_11)
test_case4.run_testcase()

#test_grp.run_testcase()
