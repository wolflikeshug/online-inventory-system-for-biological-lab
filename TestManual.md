

<center>
	<h1>
        Biological Sample Database Project
    </h1>
</center>
<center>
	<h1>
        Test Manual
    </h1>
    <p>
        <h2>
       		Fall 2022
        </h2>
    </p>
	<h2>
		The University of Western Australia
	</h2>
</center>






**Table of Contents**

[toc]



# Objectives

The objective of this document is to set up a sequence of testing to check and test the project's robustness, to ensure our product will keep a low failure rate when our client actually put it into work. Overall Test will combine automatic test and manual test. Most of the unit tests and integation test will be done by test script, while system test will be done by manually.



# Test Summary

This document will focus on the accuracy and ease of use of the data search function, the completeness of the database, the timeliness of data updates, and data security around the logging function, and test the sanity of user management designed for administrators. Since the project is designed without the server hosting the website, there are no web security tests designed for the website server. However, it is strongly recommended that after the project is officially launched, the follow-up operation and maintenance personnel further improve the security of the server, such as encrypting data.

Many functions are still under discussion when this manual is written, but this test manual will still include tests arround these functions to be implemented, and more functions may be added to this project in the future. New tests will be designed and added after the functions are implemented. .



# Test Strategy

In this test manual, we will focus on testing several major subsystems of the project: including the search function, web page, database, user management system, operation log, and at the end, test the project as a whole. For the search function, we will test whether the search function can accurately query the expected value and the response speed of the search, and most of this part will be completed by the test script. The test of the web page will focus on testing whether the web page is complete and error-free, and this part will be done manually. The addition, deletion, and edition of data through the website will also be part of the test project. Also, after all, activities are performed, the operation log will be checked to see that all operations are recorded correctly. As the last of the test, the project as a whole will be manually tested to simulate user usage.

<img src="TestCase.assets/System%20Overview-16603149538121.jpg" alt="System Overview" style="zoom: 50%;" />

# Test Cases

## Test A: Website

Test A will revolve around testing the website, and the test will focus on the web page itself. 

### Test specification

This test will basically be based on checking the elements of the web page and whether the web page responds as expected. This part of the test will be checked manually.

### Test Description

| case_id | test_project           | precondition   | test_step                               | expected_outcome                                   |
| ------- | ---------------------- | -------------- | --------------------------------------- | -------------------------------------------------- |
| W-01    | Test Dashboard buttom  | Website opened | Manually Click on **Dashboard** buttom  | **Dashboard** webpage will be shown on right-side  |
| W-02    | Test Inventory buttom  | Website opened | Manually Click on **Inventory** buttom  | **Inventory** webpage will be shown on right-side  |
| W-03    | Test People buttom     | Website opened | Manually Click on **People** buttom     | **People** webpage will be shown on right-side     |
| W-04    | Test Rooms buttom      | Website opened | Manually Click on  **Rooms** buttom     | **Rooms** webpage will be shown on right-side      |
| W-05    | Test Containers buttom | Website opened | Manually Click on **Containers** buttom | **Containers** webpage will be shown on right-side |
| W-06    | Test Samples buttom    | Website opened | Manually Click on **Samples** buttom    | **Samples**  webpage will be shown on right-side   |

### Test Analysis Report

This part of the test report will contain test ids for successful tests, and test ids for failed tests. And record the test results of failed tests for developers to debug.



## Test B: Search Function

Test whether the search function meets the design requirements

### Test specification

The test will focus on the speed of the search function and how accurate the search function is. This part of the test will be checked automaticly.

### Test Description

| case_id | test_project                                | precondition                        | test_step                                                 | expected_outcome                                             |
| ------- | ------------------------------------------- | ----------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------ |
| S-01-1  | Ignore capitalization                       | Open the web and type in search bar | user search “**hyBrideOma**”                              | system provide result: “**Hybridoma**” from database         |
| S-01-2  | Ignore capitalization                       | Open the web and type in search bar | user search “**1.8ml**”                                   | system provide result: “**1.8ML**” from database             |
| S-02-1  | Fuzzy search (1-2 letter typo tolerance)    | Open the web and type in search bar | user search “**ZZbrideoma**”                              | system provide result: “**Hybridoma**” from database         |
| S-02-1  | Fuzzy search (more space mistake tolerance) | Open the web and type in search bar | user search “**1.8   ml**”                                | system provide result: “**1.8ML**” from database             |
| S-02-3  | Fuzzy search (no tolerance to number)       | Open the web and type in search bar | user search “**2.8ML**”                                   | no result provided since there is no matching data           |
| S-02-4  | Fuzzy search (no tolerance to units)        | Open the web and type in search bar | user search “**1.8CC**”                                   | no result provided since there is no matching data           |
| S07     | search suggestion                           | Open the web and type in search bar | user type “**4G2 Hybridoma (From 2018)”** into search bar | we expect to see suggestion:  " **4G2 Hybridoma (From 2018) ~3.2X10^6 [1.8ML] Batch 1 2021**" and "**4G2 Hybridoma (From 2018) ~2.9X10^6 [1.8ML] Batch 2 2021**" under search bar |

### Test Analysis Report

This part of the test report will contain test ids for successful tests, and test ids for failed tests. And record the test results of failed tests for developers to debug.



## Test C: User Management System

In this part, the test will focus on testing the reliability of the user management system (UMS in short) to ensure that the management system will not have errors during actual use. 

### Test specification

We will simulate some operations of administrators and ordinary users to test whether the user management system works as expected.This part of the test will be manual

### Test Description

| case_id  | test_project                                              | precondition                          | test_step                                                    | expected_outcome                                             |
| -------- | --------------------------------------------------------- | ------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| UMS-01   | Password reset                                            | login UMS as admin                    | press passwd reset buttom                                    | pop up window for entering new passwd                        |
| UMS-02   | Password reset                                            | login UMS as regular user             | press passwd reset buttom                                    | pop up window for entering new passwd                        |
| UMS-03-1 | Password reset (success)                                  | pop up window for entering new passwd | enter a valid new passwd and press enter                     | pop up window says success                                   |
| UMS-03-2 | Password reset (fail for not valid new passwd)            | pop up window for entering new passwd | enter a invalid new passwd and press enter                   | pop up window says not valid passwd                          |
| UMS-03-3 | Password reset (fail for entering same passwd as current) | pop up window for entering new passwd | enter current passwd and press enter                         | pop up window says passwd is the same                        |
| UMS-04-1 | setting usr as group "**staff**"                          | login UMS as admin                    | press group buttom besides user's id and select group staff  | usr's group will change to staff after operation             |
| UMS-04-2 | setting usr as group "**student**"                        | login UMS as admin                    | press group buttom besides user's id and select group student | usr's group will change to student after operation           |
| UMS-05   | adding new usr                                            | login UMS as admin                    | press add new usr buttom and enter usr's id                  | pop up window says new usr added, and new usr will appear in usr list |
| UMS-06   | remove usr                                                | login UMS as admin                    | press remove usr buttom besides usr's id                     | pop up window says usr removed, and usr will disappear from usr list |

### Test Analysis Report

This part of the test report will contain test ids for successful tests, and test ids for failed tests. And record the test results of failed tests for developers to debug.



## Test D: Database

The test arround database will be to test the reliability and ease of use of the database for users

### Test specification

In this part, the test will revolve around the import of new data in the database and the addition, deletion and modification of existing data.

### Test Description

| case_id | test_project                                  | precondition                      | test_step                                 | expected_outcome                                             |
| ------- | --------------------------------------------- | --------------------------------- | ----------------------------------------- | ------------------------------------------------------------ |
| D-01    | adding new data file into system              | no precondition                   | create a new excel file in system         | the data in new file can be  checked in system immediately   |
| D-02-1  | add new data line in current system (success) | login to a privileged account     | press add buttom on webpage               | pop up a window for entering details of new data             |
| D-02-2  | add new data line in current system (fail)    | login to a non-privileged account | press add buttom on webpage               | pop up a window says not permitted to make change            |
| D-03-1  | remove data from current system (success)     | login to a privileged account     | press remove buttom besides the data line | pop up a window for double checking and data will be deleted after double checked |
| D-03-2  | remove data from current system (fail)        | login to a non-privileged account | press remove buttom besides the data line | pop up a window says not permitted to make change            |
| D-04-1  | edit data line in current system (success)    | login to a privileged account     | press edit buttom besides the data line   | pop up a window for editing details of data                  |
| D-04-2  | edit data line in current system (fail)       | login to a non-privileged account | press edit buttom besides the data line   | pop up a window says not permitted to make change            |

### Test Analysis Report

This part of the test report will contain test ids for successful tests, and test ids for failed tests. And record the test results of failed tests for developers to debug.



## Test E: Log

The log has always been one of the functions that customers care about most, so the log will record the behavior of all users as detailed as possible.

### Test specification

We will manually simulate most of the user's actions, and then check that the log records the actions correctly

### Test Description

| case_id | test_project                                              | precondition                                                 | test_step                             | expected_outcome                                             |
| ------- | --------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------- | ------------------------------------------------------------ |
| L-01    | Log example for **user successful login**                 | working on device with ip_address 192.168.4.128(as example) at time [22:52 10/08/2022] (as example) | login as 23001234 with correct passwd | In log, new line added: “[22:52 10/08/2022], 192.168.4.128, 23001234, login, “login success” |
| L-02    | Log example for **user failed login** due to wrong passwd | working on device with ip_address 192.168.4.128(as example) at time [22:52 10/08/2022] (as example) | login as 23001234 with wrong passwd   | In log, new line added: “[22:52 10/08/2022], 192.168.4.128, 23001234, login, “login fail, wrong passwd” |
| L-03    | Log example for **user failed login**                     | working on device with ip_address 192.168.4.128(as example) at time [22:52 10/08/2022] (as example) | logined as helloworld                 | In log, new line added: “[22:52 10/08/2022], 192.168.4.128, helloworld, login, “login fail, account not exist” |
| L-04    | Log example for **user logout** due to account not exsit  | working on device with ip_address 192.168.4.128(as example) at time [22:52 10/08/2022] (as example) logined as 23001234 | logout                                | In log, new line added: “[22:52 10/08/2022], 192.168.4.128, 23001234, logout, “logout success” |
| L-05    | log example for **user searching**                        | working on device with ip_address 192.168.4.128(as example) at time [22:52 10/08/2022] (as example) logined as 23001234 | search                                | In log, new line added: “[22:52 10/08/2022], 192.168.4.128, 23001234, search, “The SQL Query” |
| L-06    | Log example for **user editing**                          | working on device with ip_address 192.168.4.128(as example) at time [22:52 10/08/2022] (as example) logined as 23001234 | edit data                             | In log, new line added: “[22:52 10/08/2022], 192.168.4.128, 23001234, edit, “The SQL Query” |
| L-07    | Log example for **user adding line**                      | working on device with ip_address 192.168.4.128(as example) at time [22:52 10/08/2022] (as example)  logined as 23001234 | adding data                           | In log, new line added: “[22:52 10/08/2022], 192.168.4.128, 23001234, add, “The SQL Query ” |
| L-08    | Log example for **remove data from database**             | working on device with ip_address 192.168.4.128(as example) at time [22:52 10/08/2022] (as example) logined as 23001234 | remove data                           | In log, new line added: “[22:52 10/08/2022], 192.168.4.128, 23001234, remove, “The SQL Query” |
| L-09    | Log example for **admin add new accounts**                | working on device with ip_address 192.168.4.128(as example) at time [22:52 10/08/2022] (as example) login as 23001111 (admin) | adding new usr 23001234               | In log, new line added: “[22:52 10/08/2022], 192.168.4.128, 23001111(admin), usrchange, “user 23001234 has been created” |
| L-10    | Log example for **admin delet account**                   | working on device with ip_address 192.168.4.128(as example) at time [22:52 10/08/2022] (as example) login as 23001111 (admin) | deleting usr 23001234                 | In log, new line added: “[22:52 10/08/2022], 192.168.4.128, 23001111, usrchange, “user 23001234 has been deleted” |
| L-11    | Log example for **reset password**                        | working on device with ip_address 192.168.4.128(as example) at time [22:52 10/08/2022] (as example) logined as 23001234 | reset passwd                          | In log, new line added: “[22:52 10/08/2022], 192.168.4.128, 23001234, usrchange, “user 23001234 password has been reseted” |

### Test Analysis Report

This part of the test report will contain test ids for successful tests, and test ids for failed tests. And record the test results of failed tests for developers to debug.



## Test F: Overall Testing

In this step, the test will simulate a normal user to use the system

### Test specification

There will be no new operations in this part, but the operations in the previous steps will be combined to simulate the user's daily operations

### Test Description

| case_id | test_project                                        | precondition                                                 | test_step                  | expected_outcome                                             |
| ------- | --------------------------------------------------- | ------------------------------------------------------------ | -------------------------- | ------------------------------------------------------------ |
| OT-01   | simulate usr login and messing arround with website | working on device with ip_address 192.168.4.128(as example) at time [22:52 10/08/2022] (as example) | L-01, W-02, W-06, W-04     | In log, new line added: “[22:52 10/08/2022], 192.168.4.128, 23001234, login, “login success” and no error pop up |
| OT-02   | user search and edit target data                    | working on device with ip_address 192.168.4.128(as example) at time [22:52 10/08/2022] (as example)  logined as 23001234 | S-03, D-04-1, L-06         | In log, new line added: “[22:52 10/08/2022], 192.168.4.128, 23001234, edit, “The SQL Query” and data does changed |
| OT-03   | user reset its passwd and then signout              | working on device with ip_address 192.168.4.128(as example) at time [22:52 10/08/2022] (as example)  logined as 23001234 | W-03, UMS-03-1, L-11, L-04 | In log, new line added: “[22:52 10/08/2022], 192.168.4.128, 23001234, usrchange, “user 23001234 password has been reseted”,  “[22:52 10/08/2022], 192.168.4.128, 23001234, logout, “logout success” |

### Test Analysis Report

This part of the test report will contain test ids for successful tests, and test ids for failed tests. And record the test results of failed tests for developers to debug.
