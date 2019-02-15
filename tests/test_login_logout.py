"""
The login and logout test for the Qxf2 trainer application.
This test will:
a) Visit the Qxf2 trainer app
b) Login
c) Logout
"""

import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.login_logout_conf as conf 


def test_login_logout(base_url,browser,browser_version,os_version,os_name,remote_flag,testrail_flag,tesults_flag,test_run_id,remote_project_name,remote_build_name):
    "Test the login and logout action"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1

        #Create a test object and fill the example form.
        print(base_url)
        test_obj = PageFactory.get_page_object("Login Page",base_url=base_url)

        #Setup and register a driver
        start_time = int(time.time())	#Set start_time with current time
        test_obj.register_driver(remote_flag,os_name,os_version,browser,browser_version,remote_project_name,remote_build_name)

        #Get test data from conf file
        username = conf.USERNAME
        password = conf.PASSWORD

        result_flag = test_obj.login(username,password)
        test_obj.log_result(result_flag,
        positive='PASS: Logged into the applcation',
        negative='FAIL: Could not log in to the applciation')

        test_obj.write_test_summary()

        #Teardown
        test_obj.wait(3)
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter
        test_obj.teardown()
        
    except Exception as e:
        print("Exception when trying to run test:%s"%__file__)
        print("Python says:%s"%str(e))

    assert expected_pass == actual_pass, "Test failed: %s"%__file__
       
    
#---START OF SCRIPT   
if __name__=='__main__':
    print("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()
                
    #Run the test only if the options provided are valid
    if options_obj.check_options(options): 
        test_login_logout(base_url=options.url,
                        browser=options.browser,
                        browser_version=options.browser_version,
                        os_version=options.os_version,
                        os_name=options.os_name,
                        remote_flag=options.remote_flag,
                        testrail_flag=options.testrail_flag,
                        tesults_flag=options.tesults_flag,
                        test_run_id=options.test_run_id,
                        remote_project_name=options.remote_project_name,
                        remote_build_name=options.remote_build_name) 
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(option_obj.print_usage())
