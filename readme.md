# Using the Nexus API in Python and Ansible

Last updated: 10.19.2020

## Purpose

Generates code for the Nexus API in Python, shows examples using Python tests, 
and will have custom ansible modules

## Prerequisites

A working knowledge of Docker.

A working knowledge of Python.

A working knowledge of Ansible if you plan on using the custom modules.  
You can learn about Ansible by reading this 
[repo](https://github.com/bretmullinix/ansible-for-beginners).

## Instructions

:construction:  Currently the repo is under construction.  If you wish, you
may **"follow"** the repo and see the repo develop.

### Generate and Install the Swagger Nexus API Client Code
1. cd swagger-codegen
1. mvn clean package
1. Run the following shell command to generate the code in the **nexus_stub_output_folder**

    ```shell script
    java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate   \
    -i ../nexus_swagger.json   \
    -l python  \
     -o ../nexus_stub_output_folder
    ```
    
    Let's explain the code:
    
    1. We are running the Java Swagger Code Generator located in the **swagger-codegen-cli.jar**
       archive file.
       
    1. **generate** --> Tells Swagger to generate code
    
    1. **\-i** --> The Nexus Server **swagger.json** file.  On my Nexus server, the file location is 
      `https://[host name]:8443/service/rest/swagger.json`
       
       Replace **[host name]** with your host name or ip address.
       
    1. **\-l** --> The programming language to generate code for.  Code can be generated in
       several languages.  Python was chosen because the custom Ansible module uses Python.
       
    1. **\-o** --> The output folder for the generated code.
    
1. cd **nexus_stub_output_folder**

1. Make sure you have a Python virtual environment activated.  You don't want to install any
   software using your System Python because it could corrupt your system.
   
1. Install Ansible 2.9 by running the following command:  `pip install ansible==2.9`

1. Run `python setup.py install`

### Execute some code against the Nexus repository.

1. Open the **tests/test_swagger_nexus_api.py** file. Replace the following:

   1. For the following variable declaration, replace "\<your user name\>" with
      your nexus user name that is allowed to perform API calls.
      
      ```python
      username = "<your user name>"
      ```
      
   1. For the following variable declaration, replace "\<your password\>" with
      your nexus user name that is allowed to perform API calls.
      
      ```python
      password = "<your password>"
      ```
   
   1. In the setup method, replace the variable value of **self.configuration.host**
      to your nexus server host URL.
   
   1. Change the appropriate properties for the Python tests to fit what you plan on
      doing.

Once you are finished, you should be able to run the Python tests in the **test** folder.
These tests can list, delete, and create blob stores.  The blob stores are the backing
stores needed to store the repository data.

The Python tests will be expanded over the next couple of weeks.