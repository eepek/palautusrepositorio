*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Click Login Link
    Click Link  Login
    Login Page Should Be Open

Click Register Link
    Click Link  Register new user
    Register Page Should Be Open

*** Keywords ***

Go To Main Page
    Go To  ${HOME_URL}

Register Page Should Be Open
    Title Should Be  Register