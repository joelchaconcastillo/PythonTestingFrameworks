# PythonTestingFrameworks
This repository has been created to assess the performance, usability, and maintenance aspects of frameworks specifically designed for Python language testing.
Within this README, you will find a brief explanation for each available framework, along with an example for each.

These frameworks are sort in terms of usability and popularity, each of them contains three files:
`install.sh`: this is to install the package with pip3
`run.sh`: to run the example
`output.log`: saves the output (stdout and stderr) of executing 'run.sh'


Observations:
*** unittest is the primary unit testing framework in Python, and it is available in Python versions 2.7 and later. unittest2 serves as a compatibility layer for users of Python 2.4-2.6 who want to access some of the features available in the standard unittest module introduced in Python 2.7.

**While both nose and nose2 serve similar purposes and share some common features, nose2 is a more modern and actively maintained framework. If you are starting a new project or working with Python 3 and later versions, nose2 is likely a better choice. However, if you have an existing project that relies on nose, it may be more practical to continue using nose for backward compatibility





Creating a comprehensive comparison table for testing frameworks can be quite extensive, as there are numerous testing frameworks with different features and capabilities. However, I can provide a simplified comparison table for some popular testing frameworks in Python to help you get started. Keep in mind that this table provides a basic overview and may not cover all aspects of each framework. Features and capabilities can vary over time as frameworks evolve.

| Framework           | Type              | Ease of Use      | Test Discovery | Fixture Support | Parameterized Tests | Mocking Capabilities |  Date first release |
|---------------------|-------------------|------------------|-----------------|-----------------|----------------------|-----------------------|-----------------------|
| `pytest`            | Unit Testing      | Easy             | Yes             | Yes             | Yes                  | Yes                   | 2004                  |
| `unittest`          | Unit Testing      | Medium           | Yes             | Yes             | Limited              | Limited               | 2001                  |
| `unittest2`         | Unit Testing      | Medium           | Yes             | Yes             | Limited              | Limited               | 2019                  |
| `testify`           | Unit Testing      | Medium           | Yes             | No              | Limited              | Limited               | 2010                  |
| `nose`              | Unit Testing      | Easy             | Yes             | Yes             | Yes                  | Limited               | 2005                  |
| `nose2`             | Unit Testing      | Medium           | Yes             | Yes             | Yes                  | Limited               | 2013                  |
| `doctest`           | Docstring Testing | Easy             | Yes             | No              | No                   | Limited               | 1997                  | 
| `Hypothesis`        | Property-based    | Medium           | Yes             | No              | Yes                  | No                    | 2016                  | 
| `tox`               | Test Automation   | Medium           | Yes             | Yes             | No                   | No                    | 2013                  |
| `Behave`            | BDD               | Medium           | Yes             | Yes             | No                   | No                    | 2010                  |
| `Robot Framework`   | BDD               | Medium           | Yes             | Yes             | No                   | No                    | 2008                  |
| `playwright`        | BDD               | Medium           | Yes             | Yes             | Yes                  | Yes                   | 2020                  |


Note:
- "Type" indicates the type of testing the framework is primarily designed for (e.g., unit testing, property-based testing, BDD).
- "Ease of Use" is a general indication of how user-friendly the framework is.
- "Test Discovery" refers to the framework's ability to automatically discover and run test cases.
- "Fixture Support" relates to the framework's support for setup and teardown fixtures for tests.
- "Parameterized Tests" indicates whether the framework supports running tests with different input parameters.
- "Mocking Capabilities" assesses the framework's support for mocking and stubbing during testing.
- "BDD Support" shows whether the framework is designed for Behavior-Driven Development (BDD).

The table previously shown provides a simplified comparison. 

Comparison of most popular frameworks:

| Feature                               | `unittest`                 | `pytest`                    | `nose`                     |
|---------------------------------------|-----------------------------|-----------------------------|-----------------------------|
| Test Discovery                        | Limited (manual test discovery) | Automatic test discovery   | Automatic test discovery   |
| Test Organization                     | Class-based test cases       | Function-based test cases  | Function-based test cases  |
| Assertions                            | Basic assertions             | Rich set of built-in and custom assertions | Basic assertions   |
| Fixture Support                       | Basic test setup/teardown methods | Powerful fixtures and plugins | Basic test |


Some description of the most popular frameworks:


| Framework            | Description                                                                 | Key Features                           | Popularity                                   |
|----------------------|-----------------------------------------------------------------------------|----------------------------------------|---------------------------------------------|
| unittest (Built-in)  | Part of the Python Standard Library, inspired by Java's JUnit.             | Test discovery, test fixtures, test discovery, test parametrization.   | Widely used, but often considered verbose.   |
| pytest               | A third-party framework that simplifies testing and is highly extensible. | Concise test code, fixtures, plugins, parametrization, advanced features. | Extremely popular, large community.        |
| nose                 | An older, third-party framework with test discovery and test running.     | Test discovery, plugins, test attributes, better test discovery.        | Less popular in recent years.               |
| doctest              | Part of the Python Standard Library, allows embedding tests in docstrings. | Simple test setup, minimalistic.                                      | Useful for documentation testing.           |
| nose2                | An improved version of the `nose` framework.                               | Test discovery, test attributes, plugins, parallel test execution.   | Gaining popularity, but less known.         |
| Robot Framework      | A generic open-source automation framework for acceptance testing.       | Keyword-driven testing, test data-driven, easy-to-read test cases.   | Primarily used for acceptance testing.       |
| Hypothesis           | A property-based testing framework that generates test data automatically. | Automatically generates test cases, wide test coverage, complex test scenarios. | Gaining popularity in property-based testing. |


Please keep in mind that `doctest` is primarily designed for testing code examples embedded within docstrings, while `Robot Framework` is predominantly employed for acceptance testing purposes.

Licenses of each framework

| Framework Name | License              |
|-----------------|----------------------|
| `unittest`     | Python License       |
| `unittest2`     | Python License       |
| `pytest`       | MIT License          |
| `nose`         | GNU LGPL              |
| `nose2`        | GNU LGPL              |
| `doctest`      | Python License       |
| `Behave`       | MIT License          |
| `Robot Framework` | Apache License 2.0 |
| `tox`          | MIT License          |
| `Testify`      | Apache License 2.0 |
| `Hypothesis`   | MIT License          |
| `Playwright`   | Apache License 2.0 |

URL of each frameaork

Here's a table of popular testing frameworks in Python, along with their respective official links:

| Framework Name   | Official Link                                        |
|------------------|-----------------------------------------------------|
| `unittest`       | [Official `unittest` Documentation](https://docs.python.org/3/library/unittest.html) |
| `unittest2`       | [Official `unittest` Documentation](https://pypi.org/project/unittest2/) |
| `pytest`         | [Official `pytest` Documentation](https://docs.pytest.org/en/latest/) |
| `nose`           | [Official `nose` Documentation](https://nose.readthedocs.io/en/latest/) |
| `nose2`          | [Official `nose2` Repository](https://github.com/nose-devs/nose2) |
| `doctest`        | [Official `doctest` Documentation](https://docs.python.org/3/library/doctest.html) |
| `Behave`         | [Official Behave Documentation](https://behave.readthedocs.io/en/latest/index.html) |
| `Robot Framework` | [Official Robot Framework Website](https://robotframework.org/) |
| `tox`            | [Official `tox` Documentation](https://tox.readthedocs.io/en/latest/) |
| `Testify`        | [Official Testify Repository](https://github.com/Yelp/Testify) |
| `Hypothesis`     | [Official Hypothesis Documentation](https://hypothesis.readthedocs.io/en/latest/) |
| `Playwright`     | [Official Playwright Documentation](https://playwright.dev/python/docs/intro) |

Please note that the provided links lead to the official documentation or repositories for each testing framework. You can find detailed information, documentation, and resources at these links.


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


