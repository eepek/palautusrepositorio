*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  drevil  1billiondollars
    Output Should Contain  New user registered


Register With Already Taken Username And Valid Password
    Input Credentials  apowers  groovy4life
    Output Should Contain  User with username apowers already exists

Register With Too Short Username And Valid Password
    Input Credentials  dr  1billiondollars
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  DrEvil1  1billiondollars
    Output Should Contain  Username must contain only lowercase letters [a-z]

Register With Valid Username And Too Short Password
    Input Credentials  drevil  only
    Output Should Contain  Password must be at least 8 characters long and contain atleast non-alphabet character

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  drevil  onebilliondollars
    Output Should Contain  Password must be at least 8 characters long and contain atleast non-alphabet character

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  apowers  groovy4life