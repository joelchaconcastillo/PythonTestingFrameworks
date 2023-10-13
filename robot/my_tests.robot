*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
My First Test
    Open Browser    https://www.example.com    chrome
    Page Should Contain    Example Domain
    Close Browser
