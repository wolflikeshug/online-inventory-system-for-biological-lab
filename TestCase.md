

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
| W01     | Test Dashboard buttom  | Website opened | Manually Click on **Dashboard** buttom  | **Dashboard** webpage will be shown on right-side  |
| W02     | Test Inventory buttom  | Website opened | Manually Click on **Inventory** buttom  | **Inventory** webpage will be shown on right-side  |
| W03     | Test People buttom     | Website opened | Manually Click on **People** buttom     | **People** webpage will be shown on right-side     |
| W04     | Test Rooms buttom      | Website opened | Manually Click on  **Rooms** buttom     | **Rooms** webpage will be shown on right-side      |
| W05     | Test Containers buttom | Website opened | Manually Click on **Containers** buttom | **Containers** webpage will be shown on right-side |
| W06     | Test Samples buttom    | Website opened | Manually Click on **Samples** buttom    | **Samples**  webpage will be shown on right-side   |

### Test Analysis Report

This part of the test report will contain test ids for successful tests, and test ids for failed tests. And record the test results of failed tests for developers to debug.



## Test B: Search Function

Test whether the search function meets the design requirements

### Test specification

The test will focus on the speed of the search function and how accurate the search function is. This part of the test will be checked automaticly.

### Test Description

| case_id | test_project                                | precondition                        | test_step                                                 | expected_outcome                                             |
| ------- | ------------------------------------------- | ----------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------ |
| S01     | Ignore capitalization                       | Open the web and type in search bar | user search “**hyBrideOma**”                              | system provide result: “**Hybridoma**” from database         |
| S02     | Ignore capitalization                       | Open the web and type in search bar | user search “**1.8ml**”                                   | system provide result: “**1.8ML**” from database             |
| S03     | Fuzzy search (1-2 letter typo tolerance)    | Open the web and type in search bar | user search “**ZZbrideoma**”                              | system provide result: “**Hybridoma**” from database         |
| S04     | Fuzzy search (more space mistake tolerance) | Open the web and type in search bar | user search “**1.8   ml**”                                | system provide result: “**1.8ML**” from database             |
| S05     | Fuzzy search (no tolerance to number)       | Open the web and type in search bar | user search “**2.8ML**”                                   | no result provided since there is no matching data           |
| S06     | Fuzzy search (no tolerance to units)        | Open the web and type in search bar | user search “**1.8CC**”                                   | no result provided since there is no matching data           |
| S07     | search suggestion                           | Open the web and type in search bar | user type “**4G2 Hybridoma (From 2018)”** into search bar | we expect to see suggestion:  " **4G2 Hybridoma (From 2018) ~3.2X10^6 [1.8ML] Batch 1 2021**" and "**4G2 Hybridoma (From 2018) ~2.9X10^6 [1.8ML] Batch 2 2021**" under search bar |

### Test Analysis Report

This part of the test report will contain test ids for successful tests, and test ids for failed tests. And record the test results of failed tests for developers to debug.



## Test C: User Management System

In this part, the test will focus on testing the reliability of the user management system (UMS in short) to ensure that the management system will not have errors during actual use. 

### Test specification

We will simulate some operations of administrators and ordinary users to test whether the user management system works as expected.This part of the test will be manual

### Test Description

| case_id | test_project                                              | precondition                          | test_step                                                    | expected_outcome                                             |
| ------- | --------------------------------------------------------- | ------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| UMS01   | Password reset                                            | login UMS as admin                    | press passwd reset buttom                                    | pop up window for entering new passwd                        |
| UMS02   | Password reset                                            | login UMS as regular user             | press passwd reset buttom                                    | pop up window for entering new passwd                        |
| UMS03   | Password reset (success)                                  | pop up window for entering new passwd | enter a valid new passwd and press enter                     | pop up window says success                                   |
| UMS04   | Password reset (fail for not valid new passwd)            | pop up window for entering new passwd | enter a invalid new passwd and press enter                   | pop up window says not valid passwd                          |
| UMS05   | Password reset (fail for entering same passwd as current) | pop up window for entering new passwd | enter current passwd and press enter                         | pop up window says passwd is the same                        |
| UMS06   | setting usr as group "**staff**"                          | login UMS as admin                    | press group buttom besides user's id and select group staff  | usr's group will change to staff after operation             |
| UMS06   | setting usr as group "**student**"                        | login UMS as admin                    | press group buttom besides user's id and select group student | usr's group will change to student after operation           |
| UMS07   | adding new usr                                            | login UMS as admin                    | press add new usr buttom and enter usr's id                  | pop up window says new usr added, and new usr will appear in usr list |
| UMS08   | remove usr                                                | login UMS as admin                    | press remove usr buttom besides usr's id                     | pop up window says usr removed, and usr will disappear from usr list |

### Test Analysis Report

This part of the test report will contain test ids for successful tests, and test ids for failed tests. And record the test results of failed tests for developers to debug.



## Test D: Database

In this part, the test will revolve around the import of new data in the database and the addition, deletion and modification of existing data.

### Test specification

<<测试规范列出了满足的要求 将通过测试来证明。  它列出了测试的方法，并描述了 测试条件。>> 



### Test Description

| case_id | test_project | precondition | test_step | expected_outcome |
| ------- | ------------ | ------------ | --------- | ---------------- |
|         |              |              |           |                  |
|         |              |              |           |                  |
|         |              |              |           |                  |
|         |              |              |           |                  |
|         |              |              |           |                  |

<<测试说明用作执行测试的指南。 它列出了每个测试的输入数据和输入命令，以及预期的 输出和系统消息。  如果您发现无法描述 预期的数字输出，使用自然语言描述。  一个测试 描述包括 

-   测试位置（测试的超链接） 

-   控制手段：描述如何输入数据（手动或自动 与测试驱动程序） 

-   数据 

-   -   输入数据 
    -   输入命令 
    -   输出数据 
    -   系统消息 

-   程序：测试程序通常以测试脚本的形式指定。 

-   

### Test Analysis Report

<<测试分析报告列出了功能和性能特点 要演示的内容，并描述实际的测试结果。  这 结果的描述必须包括以下内容： 

-   功能 
-   表现 
-   数据措施，包括是否满足目标要求 

如果发现错误或缺陷，报告将讨论其 影响。>>



## Test E: Log

<<测试A的介绍和概述>> 



### Test specification

<<测试规范列出了满足的要求 将通过测试来证明。  它列出了测试的方法，并描述了 测试条件。>> 



### Test Description

| case_id | test_project | precondition | test_step | expected_outcome |
| ------- | ------------ | ------------ | --------- | ---------------- |
|         |              |              |           |                  |
|         |              |              |           |                  |
|         |              |              |           |                  |
|         |              |              |           |                  |
|         |              |              |           |                  |

<<测试说明用作执行测试的指南。 它列出了每个测试的输入数据和输入命令，以及预期的 输出和系统消息。  如果您发现无法描述 预期的数字输出，使用自然语言描述。  一个测试 描述包括 

-   测试位置（测试的超链接） 

-   控制手段：描述如何输入数据（手动或自动 与测试驱动程序） 

-   数据 

-   -   输入数据 
    -   输入命令 
    -   输出数据 
    -   系统消息 

-   程序：测试程序通常以测试脚本的形式指定。 

-   

### Test Analysis Report

<<测试分析报告列出了功能和性能特点 要演示的内容，并描述实际的测试结果。  这 结果的描述必须包括以下内容： 

-   功能 
-   表现 
-   数据措施，包括是否满足目标要求 

如果发现错误或缺陷，报告将讨论其 影响。>>



## Test F: Overall Testing

<<测试A的介绍和概述>> 



### Test specification

<<测试规范列出了满足的要求 将通过测试来证明。  它列出了测试的方法，并描述了 测试条件。>> 



### Test Description

| case_id | test_project | precondition | test_step | expected_outcome |
| ------- | ------------ | ------------ | --------- | ---------------- |
|         |              |              |           |                  |
|         |              |              |           |                  |
|         |              |              |           |                  |
|         |              |              |           |                  |
|         |              |              |           |                  |

<<测试说明用作执行测试的指南。 它列出了每个测试的输入数据和输入命令，以及预期的 输出和系统消息。  如果您发现无法描述 预期的数字输出，使用自然语言描述。  一个测试 描述包括 

-   测试位置（测试的超链接） 

-   控制手段：描述如何输入数据（手动或自动 与测试驱动程序） 

-   数据 

-   -   输入数据 
    -   输入命令 
    -   输出数据 
    -   系统消息 

-   程序：测试程序通常以测试脚本的形式指定。 

-   

### Test Analysis Report

<<测试分析报告列出了功能和性能特点 要演示的内容，并描述实际的测试结果。  这 结果的描述必须包括以下内容： 

-   功能 
-   表现 
-   数据措施，包括是否满足目标要求 如果发现错误或缺陷，报告将讨论其 影响。>>
