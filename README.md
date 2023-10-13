# PythonTestingFrameworks
This repository has been created to assess the performance, usability, and maintenance aspects of frameworks specifically designed for Python language testing.
Within this README, you will find a brief explanation for each available framework, along with an example for each.

These frameworks are sort in terms of usability and popularity, each of them contains three files:
`install.sh`: this is to install the package with pip3
`run.sh`: to run the example
`output.log`: saves the output (stdout and stderr) of executing 'run.sh'

##### pytest #####
URL: https://docs.pytest.org/en/7.4.x/

License: MIT

Observations:

##### unittest #####
URL: https://docs.python.org/3/library/unittest.html

License: Python Software Foundation License (PSF License)

Observations:

*** PSF License is similar to MIT License

#### unittest2 ####
URL: https://pypi.org/project/unittest2/

License: Python Software Foundation License (PSF License)


Observations:
*** unittest is the primary unit testing framework in Python, and it is available in Python versions 2.7 and later. unittest2 serves as a compatibility layer for users of Python 2.4-2.6 who want to access some of the features available in the standard unittest module introduced in Python 2.7.

##### hyphotesis #####
URL: https://hypothesis.readthedocs.io/en/latest/

License: Mozilla Public License 2.0 (MPL-2.0)

Observations:

##### doctest #####
URL: https://docs.python.org/3/library/doctest.html

License: Python Software Foundation License (PSF License)

Observations: 

*** PSF License is similar to MIT License

##### nose #####
URL: https://pypi.org/project/nose/

License: GNU Lesser General Public License (LGPL) version 2.1

Observations:

##### nose2 #####
URL: https://docs.nose2.io/en/latest/

License: MIT License

Observations:

**While both nose and nose2 serve similar purposes and share some common features, nose2 is a more modern and actively maintained framework. If you are starting a new project or working with Python 3 and later versions, nose2 is likely a better choice. However, if you have an existing project that relies on nose, it may be more practical to continue using nose for backward compatibility

##### testify #####
URL: https://pypi.org/project/testify/

License: MIT License

Observations:

**It is commonly used alongside other testing tools.

##### playwright #####
URL: https://playwright.dev/

License: Apache License 2.0

Observations:


##Frameworks type Behave Driven Development (BDD)##

##### behave #####
URL: https://behave.readthedocs.io/en/latest/

License: MIT License

Observations:

##### robot #####
URL: https://robotframework.org/

License: MIT License

Observations: Apache License 2.0


Creating a comprehensive comparison table for testing frameworks can be quite extensive, as there are numerous testing frameworks with different features and capabilities. However, I can provide a simplified comparison table for some popular testing frameworks in Python to help you get started. Keep in mind that this table provides a basic overview and may not cover all aspects of each framework. Features and capabilities can vary over time as frameworks evolve.

| Framework           | Type              | Ease of Use      | Test Discovery | Fixture Support | Parameterized Tests | Mocking Capabilities |
|---------------------|-------------------|------------------|-----------------|-----------------|----------------------|-----------------------|
| `unittest`          | Unit Testing      | Medium           | Yes             | Yes             | Limited              | Limited               | 
| `unittest2`         | Unit Testing      | Medium           | Yes             | Yes             | Limited              | Limited               | 
| `testify`           | Unit Testing      | Medium           | Yes             | No              | Limited              | Limited               | 
| `pytest`            | Unit Testing      | Easy             | Yes             | Yes             | Yes                  | Yes                   |
| `nose`              | Unit Testing      | Easy             | Yes             | Yes             | Yes                  | Limited               |
| `nose2`             | Unit Testing      | Medium           | Yes             | Yes             | Yes                  | Limited               |
| `doctest`           | Docstring Testing | Easy             | Yes             | No              | No                   | Limited               |
| `Hypothesis`        | Property-based    | Medium           | Yes             | No              | Yes                  | No                    |
| `tox`               | Test Automation   | Medium           | Yes             | Yes             | No                   | No                    |
| `Behave`            | BDD               | Medium           | Yes             | Yes             | No                   | No                    |
| `Robot Framework`   | BDD               | Medium           | Yes             | Yes             | No                   | No                    |
| `playwright`        | BDD               | Medium           | Yes             | Yes             | Yes                  | Yes                   |


Note:
- "Type" indicates the type of testing the framework is primarily designed for (e.g., unit testing, property-based testing, BDD).
- "Ease of Use" is a general indication of how user-friendly the framework is.
- "Test Discovery" refers to the framework's ability to automatically discover and run test cases.
- "Fixture Support" relates to the framework's support for setup and teardown fixtures for tests.
- "Parameterized Tests" indicates whether the framework supports running tests with different input parameters.
- "Mocking Capabilities" assesses the framework's support for mocking and stubbing during testing.
- "BDD Support" shows whether the framework is designed for Behavior-Driven Development (BDD).

The table provides a simplified comparison. Depending on your project's specific needs, you may want to consider other factors like community support, available plugins and extensions, and integration with other tools in your development and testing stack.

Selecting the right testing framework depends on your project requirements and personal preferences. Consider the type of testing you'll be doing, the complexity of your tests, and the tools that work well with your development environment.







###################Suggestions##############################

AI-Enhanced Static Code Analysis
====DeepCode
====Kite
Mutation Testing 
====MutPy
====Pitest
AI-Based Code Review
====CodeClimate
====DeepCode


