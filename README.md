# PythonTestingFrameworks
This repository has been created to assess the performance, usability, and maintenance aspects of frameworks specifically designed for Python language testing.
Within this README, you will find a brief explanation for each available framework, along with an example for each.

These frameworks are sort in terms of usability and popularity, each of them contains three files:
`install.sh`: this is to install the package with pip3
`run.sh`: to run the example
`output.log`: saves the output (stdout and stderr) of executing 'run.sh'

##### pytest #####
URL: https://docs.pytest.org/en/7.4.x/
Licence: MIT
Observations:

##### unittest #####
URL: https://docs.python.org/3/library/unittest.html
Licence: Python Software Foundation License (PSF License)
Observations:
*** PSF License is similar to MIT License


##### hyphotesis #####
URL: https://hypothesis.readthedocs.io/en/latest/
Licence: Mozilla Public License 2.0 (MPL-2.0)
Observations:

##### doctest #####
URL: https://docs.python.org/3/library/doctest.html
Licence: Python Software Foundation License (PSF License)
Observations: 
*** PSF License is similar to MIT License

##### nose #####
URL: https://pypi.org/project/nose/
Licence: GNU Lesser General Public License (LGPL) version 2.1
Observations:

##### nose2 #####
URL: https://docs.nose2.io/en/latest/
Licence: MIT License
Observations:

##### playwright #####
URL: https://playwright.dev/
Licence: Apache License 2.0
Observations:




Creating a comprehensive comparison table for testing frameworks can be quite extensive, as there are numerous testing frameworks with different features and capabilities. However, I can provide a simplified comparison table for some popular testing frameworks in Python to help you get started. Keep in mind that this table provides a basic overview and may not cover all aspects of each framework. Features and capabilities can vary over time as frameworks evolve.

| Framework           | Type              | Ease of Use      | Test Discovery | Fixture Support | Parameterized Tests | Mocking Capabilities | BDD Support |
|---------------------|-------------------|------------------|-----------------|-----------------|----------------------|-----------------------|-------------|
| `unittest`          | Unit Testing      | Medium           | Yes             | Yes             | Limited              | Limited               | No          |
| `pytest`            | Unit Testing      | Easy             | Yes             | Yes             | Yes                  | Yes                   | No          |
| `nose`              | Unit Testing      | Easy             | Yes             | Yes             | Yes                  | Limited               | No          |
| `doctest`           | Docstring Testing | Easy             | Yes             | No              | No                   | Limited               | No          |
| `nose2`             | Unit Testing      | Medium           | Yes             | Yes             | Yes                  | Limited               | No          |
| `Hypothesis`        | Property-based    | Medium           | Yes             | No              | Yes                  | No                    | No          |
| `tox`               | Test Automation   | Medium           | Yes             | Yes             | No                   | No                    | No          |
| `Behave`            | BDD               | Medium           | Yes             | Yes             | No                   | No                    | Yes         |
| `Robot Framework`   | BDD               | Medium           | Yes             | Yes             | No                   | No                    | Yes         |

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
