# Assignment 8 

## Weiyu Feng

## Software Requirements Specification

### Introduction

#### Project Name

- CHAOSS

#### Purpose

-  The purpose of this document is to specify the requirements and details of the software architecture for OpenSourceHealth, which is CHAOSS, a Linux Foundation project focused on creating analytics and metrics to help define community health. The project aims to: 
	1. Establish standard implementation-agnostic metrics for measuring community activity, contributions, and health
    
	2. Produce integrated open source software for analyzing software community development
    
	3.  Build reproducible project health reports/containers

#### Scope

-   This tool is built for technology companies and IT organizations and open software contributers. Basically, this software is for everyone who wants to assess the health and sustainability of the open source software.

#### Assumption
-  It is assumed that the companies/ communicties/ orgniazations/ developers are willing to provide data to the software.

### Software Product Overview

#### System Scope

-  OpenSourceHealth will use an automated algorithm to make sustainability predictions for projects. It will be available for both web and mobile applications. The system will let users be able to search the open source project they are interestde in and see how healthy and sustainable they are. 
 
#### System Architecture
 
 -  External view of software product<br>
	  the user interface communicate with database and servers through management system. The management system get data from the database based on what users search for, and then convey the data to the user interfaces to display the data in a good format.

-  Internal view of software product<br>
	Search module, sustainability analyzing module, and health analyzing module communicates with the management module.

#### Feature Overview

-  Input and manage customer information<br>
	This feature allows users to store all customer information such as name, address, telephone and email.
-  Collect and Analysis data<br>
	This feature make the system able to collect data from open source software and assesses their health and sustainability.
-  Generate reports<br>
	This feature allows users to get a report regarding how healthy and sustainable a specific open source software is according to the OpenSourceHealth system.

### System Use

#### Actor Survey

-  Owner/Proprietor<br>
	Owner and proprietor are responsible foridentifying new clientele, selling the service, and improve the system. This actor will interact with the system to identify the health and sustainability of open source software.<br>
	System Feature: View reports
	
- Customers<br>
	Customers are main users of the system. They will be able to search the open source software they are interested in and get report from the system to know about the open source software's health and sustainability. They will make decision based on the reports provided by the system.<br>
	System Feature: View reports

- Manager/Employee<br>
	Manager and Employee are the administer of the system. They have the access to the core alogrithm and data used in the system. They could enter customers information and improve the algorith of the system to achieve a better, precise report.<br>
	System Feature: Collect and Analysis data; Input and manage customer information

### System Requirements

#### System Use-Cases

-  Use Case 1: Input and Manage Customer Information<br>

![](https://github.com/0WeiyuFeng0/wfghd/blob/master/assignment-eight/UseCase1.png)
	
|Use-case name|Input and Manage Customer Information |
|--|--|
|Actors|Employee|
|Brief Description|This use case explains how an employee enters and stores all customer information such as name, address, telephone, email and customer's landscaping needs.|
|Basic flow of events|1.System displays customer entry; 2.Employee enter customers' info; 3.Save and update system|
|pre-conditions|The employees must be authoticated to do so|
|Extensition Point|Search customer|

-  User Case 2: Create Open Source Software Health and Sustainability Report<br>

![](https://github.com/0WeiyuFeng0/wfghd/blob/master/assignment-eight/UseCase2.png)

|Use-case Name|Create Open Source Software Health and Sustainability Report|
|--|--|
|Actors|Customer|
|Brief Description|This use case explains how a customer let system generate a report for assessing the health and sustainability of a specific open source software after logging in to the system and searching for a specific open source software|
|Basic flow of events|1.Customer log in to the system; 2.Customer search for a specific open source software 3.System generate report after customer click "generate report" button 4.Customer view the report regarding health and sustainability of the open source software|
|pre-conditions|Customers havr already signed up|

#### System Functional Specification

-  The system algorithm of assessing health and sustainability of open source software should be good enough to provide precise prediction
- The system data should be updated in time
- Customers should login first before require reports

#### Non-functional Requirements

-  System should be stable enough to support multiple users requring reports at the same time
- System should be able to handle big data
- System should have good hardware which support it to assess data in real time 
- The system shall support a minimum of 10,000 simultaneous
- The typical search for any information should be within 2 seconds.
- All system responses shall occur within 30 seconds.
interactions.
-  User interface is user-friendly

### Design Constraints

-  The system will run as a web application with access via an ecrypted SSL login. 
- The application will run on all major web browsers - Internet Explorer, FireFox, Chrome, Safari and their mobile counterparts. 
-  The system should use such technologies as Java, Spring, MySQL, Apache and Windows.

### Purchased Components

-  Software used to develop this application should be open source
-  Data used by this application: $10000 / month
-  Web Server/ Database Server: $5000
-  Computers: $100000 

### Interfaces

- User interface:
	1. Home page: login / Sign up<br>
	2. Search Page: Search Open Source Software by name<br>
	3. Search Result Page: Show Software basic info and a button for requesting report<br>
	4. Report Page: Show data related to the open source software and assess of the data regarding health and sustainability<br>
