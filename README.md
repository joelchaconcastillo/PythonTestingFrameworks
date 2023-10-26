# Exploring Python Testing Frameworks: A Comprehensive Review

```mermaid
flowchart
	TB["Test Begin"] --> TD1["Test Design"]
	TD1 --> DI["Data Input"]
	TD1 --> DO["Data Output"]
	TD1 --> TE["Test Execution"]
	TE --> TP["Test Pass"]
	TE --> TF["Test Fail"]
	TF --> TD2["Test Debug and Fix"]
	TD2 --> TE
	TE --> TR["Test Review"]
	TR --> TT["Test Termination"]

%% Mermaid Flow Diagram Link
%% Keep this link to make future edits to your diagram
%% https://www.mermaidflow.app/flowchart#N4IgZgNg9g7iBcoB2UAmBTAzgg2qGAlqgC4AWCAjACxUA0Ip6BA5qcQgBwAM9RCIAFQBCIegAcomAsQJQkCUAA8EVAEwd6AT0pcuAX3qoAhsSMKQAYwhHMmLLgC69TMU0R78HE5DWARugh+ASxiAAIhdGYCeUMCACd0Cxk5IJF6OKMkAGtMABEMmHlEAxAxIwSkYgAlTKyEHhBUAoBlV3cEYjiAV3QS1zF0fgSkzOZ3ADk0QfFJaVkkAEFfTCgILuJBxBBleDUNEG14Cl09A3wiMkoaekYWNk4GvnhBXIpRUtnkoqUVdS0EVQAZlUJWMpnMVhsdmwnm8LjcHi89D8ASCIVCuSwLBijXiiS+qXeGWyeQK3xKZQq1Vq9UMLTam06PT6mgGQ3xowmU3eEikXyWKzWG3MOz2-3gQJBZxAhBI5CO1wYTFY7Hg3F4qH4uQAkjzPvMRb99ocqFwqKCTGYtpDbIi4QyYUifEZ-IFnrlLaFtUgxOt3qg8UkDc9hETaqSjIUFBTyuhKjVsrTGvSER1ur16P1NiBhqYkGN0JMMHq+fMBat1psfrs-gcVGbTrRznKrnQlXdVeqQE8QLkAPIluYpLY7VS6cWm82GS0Q6y2x32hEL5Eu1Huz199a+9ixXPBwRpHPh-KR8niWPxmnwBpNSOtVPwJkZkBZ9kjfNc4szUtyctCqvbAC451rsDbSrKlwKgArDcyr3GqjyaiGACig4EiOCAAGxQZhE4NtO4LWnO0KOM4Dqkc6rpoi4oTIYoiTrAau74vuobpMeZLRueVIJnU150neDJpsymastmuacoW3LfkOizLBWwoYfA2G4SBk6Ns2kHUG2twqg8GpBAACmhwbVphY4AHSAuKUEAJyYRahGgDaJGwmRS4USibqCOihlQv6gboQeYYkieUbFNxcbUom-HJoJD5PiybLPBJH5SV+Hw-nJgqVoaymWdZIF2Q54EXPK2mwR2+ndkhggAGImcO1YcFQHBWTZ9mOVaznEXa7nuMulFrj5NF1UYBCBMxQbDsF7GhZxEWlBe0V8TeKbtI+6ZJeJHJpUW0yZbJf65UpLVtYVhzFRpMplZQXa6fBXY9gIuSqI13yAcpHCAhZADsgIA4DQMA+Kv2YRwXWzlCfUgPCA2eau3nBDRmK+F0zChJkqChHVBDKFNQVsUe82nlxS08Vea3xRtiWiclOa7QW+3vcdilmd9f3A1zF0IGDEOlS2Co6XBnaIUEVTvXlgK2RQFmqLZCuK0rCswUVnUEd1li9YNcMw151FhFU6AAG4EOgcAE6xh7EjkYVnuTUW8Umt4wPeNNbXTO3vkz0mHfy8n-lLMty8roe2arl2dQLWmYRQlV6QhBkhgIktKWODSHMc+ga1D84Ubrg36yG6LBHEAC20QmExuJ7jNRM2xG4XADGFMxVTrtCZtIkvmJb55j7GW8kdAcndW6filnpzeOgqDMIioCvs8FhdC4UBl+8ZflFk6BxK05SqiAUADDim9xNvcTIUgtUSNEO7dpUO9GNNSAAOq3RKDS6+YLhxFA29v4LCgJQewzzngAWigtwKCAMoIUF+qoGg7wVhdDiBYbMRNTBxDngfF6bxMzlGwQACSxhtEAeDYZQBQWg4hV9SHkLBJrIuIB3juHzFpa6i9LAr2IGvDeW8d57ziAfI+cY+Fnx3pfa+UBb7vFvo-Z+ADIJjn6gBH+f90CKPKsA2qoD0BgIQb9WyLUoKqHlhQDgSDKGoPQa8d4mDsFal1PgrB6BiA0NQHQyxVD0DuM8TnLYTCWFxmYOw6UnDl6r3XvQU+59BHCOPmI8+kj+A30qLIh+GQFHv2UbDTuoA1H-3fkApOIBdFgKoP9DgUEoJcCqZhQEUEvHWKCLY5xDj3QDjaa43x2ZyHIOsT0-g9CZwBMRvwIJbCtFhN7kvbhvDon8N3pg+JoiFniIvlfFJ0i0m8AyU-L4migIqO-p0dRhyjjaP4GUqgmFML-TUK1Cgqg+lWLQS08h9jXFBFQl0txJDelNOof8oZ-oRmgECciYJoSmw93phEnhUSQAxIEcs-gIiT6LOSc8VJd85GZIOdkz+eTcm-0KYAy5zwynHAQZhLghjnlUEBIC9BPyXwEK+SGYyvzBnPBed4nlZDQVOSGt5CZISpkwvCXMxFyKln7zRQktZSTNnYu2bivZWTBY5K-lsApGiikUtKbPPRFB7LhwoDUjgY43rOFeSyux7KcENW5cC3lzKBXDOFRCnwUKJULxmVwyJiSUXyueOi4NGypEyN2RsfF8xznauJXq85xSapXONWA8GgJfocDBqobCANmVBGdWylxODXoOrLR691rrBX+PBWM54YroX+rhdKiNcSFWrKRZilVHxo331jfs+NhLjm6tOWS9hJSynZrNP9Z5tlWpUCLSGCtvzvmVqIbWvlAzt1CsYY25hkLJmUA4QG+F8ye3rM7WGxVV7lVRp2YO+RBKtVEofPkid+ryXTozS1VqtlfpcBwjmpltrvEbvXSGCWLraEAvA7uuDIL60ivGce8Vp7pltqDUqkNQiu0YvWVi-tT68XDrkAm99G1P2ku-VOtNlKM2GNzeDSBcDVC-RXYIGDpb2mCBTrBjx8GKH8r3Sh71rCMMXL0N4U25sJD4aUmAwETyLJ0u+oBkx5lpY83gPotQFkoI5oVphWygIOD1PUIVAAXlAXh14-rVN+nZeyVALUcAoBQQEjZcRGGYBkMuABZVxRgPTCrAL-SogWTCxvMDIYgpCQCgkClbAKe5jYwwsGvMuUVBouTtMAzAdEFPED8kgAIfYEld3QPQMYUBfBGAgMhY1AgZmgFQF0RrCAwCNbsMiaI6BWv00FHwegujovrKG9mcN9AsvQDiPwAAxL4CgK3fCYSS7V6ADWID7Sm3FgNqUB4HTm1ABbzxFu6Cu1wd4DWLBZH85Qq+ABhVYZ2ltgE+1927Z2MBxFe-Npb13dA-biH9gQpACD3fK7YfgI3NS8DyDYRgSEesQDsKcIAA

```

This repository has been created to assess the performance, usability, and maintenance aspects of frameworks specifically designed for Python language testing.
Within this README, you will find a brief explanation for each available framework, along with an example for each.

These frameworks are sort in terms of usability and popularity, each of them contains three files:

`install.sh`: this bash facilitates installation for each framework with pip3

`run.sh`: this bash is aimed to run the example by typing ./run.sh (before grant execution permissions)

`output.log`: saves the output (stdout and stderr) of executing 'run.sh' (it already has an example, note that some frameworks don't have output when all test are ok)


## Observations
*** unittest is the primary unit testing framework in Python, and it is available in Python versions 2.7 and later. unittest2 serves as a compatibility layer for users of Python 2.4-2.6 who want to access some of the features available in the standard unittest module introduced in Python 2.7.

**While both nose and nose2 serve similar purposes and share some common features, nose2 is a more modern and actively maintained framework. If you are starting a new project or working with Python 3 and later versions, nose2 is likely a better choice. However, if you have an existing project that relies on nose, it may be more practical to continue using nose for backward compatibility



## Framework Feature Comparison: A Detailed Analysis

Creating a comprehensive comparison table for testing frameworks can be quite extensive, as there are numerous testing frameworks with different features and capabilities. However, this place provides several comparison tables for some popular testing frameworks in Python. Keep in mind that these table provides a basic overview and may not cover all aspects of each framework. Features and capabilities can vary over time as frameworks evolve.

| Framework           | Type              | Ease of Use      | Test Discovery | Fixture Support | Parameterized Tests | Mocking Capabilities |  Date first release |
|---------------------|-------------------|------------------|-----------------|-----------------|----------------------|-----------------------|-----------------------|
| `pytest`            | Unit Testing      | Easy             | Yes             | Yes             | Yes                  | Yes                   | 2004                  |
| `unittest (a.k.a. pyunit)`          | Unit Testing      | Medium           | Yes             | Yes             | Limited              | Limited               | 2001                  |
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
| `Lettuce`           | BDD               | NA           | NA             | Na             | NA                  | NA                   | NA                  |


Note:
- "Type" indicates the type of testing the framework is primarily designed for (e.g., unit testing, property-based testing, BDD).
- "Ease of Use" is a general indication of how user-friendly the framework is.
- "Test Discovery" refers to the framework's ability to automatically discover and run test cases.
- "Fixture Support" relates to the framework's support for setup and teardown fixtures for tests.
- "Parameterized Tests" indicates whether the framework supports running tests with different input parameters.
- "Mocking Capabilities" assesses the framework's support for mocking and stubbing during testing.
- "BDD Support" shows whether the framework is designed for Behavior-Driven Development (BDD).

The table previously shown provides a simplified comparison. 

### Comparison of most popular frameworks:

| Feature                               | `unittest`                 | `pytest`                    | `nose`                     |
|---------------------------------------|-----------------------------|-----------------------------|-----------------------------|
| Test Discovery                        | Limited (manual test discovery) | Automatic test discovery   | Automatic test discovery   |
| Test Organization                     | Class-based test cases       | Function-based test cases  | Function-based test cases  |
| Assertions                            | Basic assertions             | Rich set of built-in and custom assertions | Basic assertions   |
| Fixture Support                       | Basic test setup/teardown methods | Powerful fixtures and plugins | Basic test |


### Description of some popular frameworks:


| Framework            | Description                                                                 | Key Features                           | Popularity                                   |
|----------------------|-----------------------------------------------------------------------------|----------------------------------------|---------------------------------------------|
| unittest (Built-in)  | Part of the Python Standard Library, inspired by Java's JUnit.             | Test discovery, test fixtures, test discovery, test parametrization.   | Widely used, but often considered verbose.   |
| pytest               | A third-party framework that simplifies testing and is highly extensible. | Concise test code, fixtures, plugins, parametrization, advanced features. | Extremely popular, large community.        |
| nose                 | An older, third-party framework with test discovery and test running.     | Test discovery, plugins, test attributes, better test discovery.        | Less popular in recent years.               |
| doctest              | Part of the Python Standard Library, allows embedding tests in docstrings. | Simple test setup, minimalistic.                                      | Useful for documentation testing.           |
| nose2                | An improved version of the `nose` framework.                               | Test discovery, test attributes, plugins, parallel test execution.   | Gaining popularity, but less known.         |
| Robot Framework      | A generic open-source automation framework for acceptance testing.       | Keyword-driven testing, test data-driven, easy-to-read test cases.   | Primarily used for acceptance testing.       |
| Hypothesis           | A property-based testing framework that generates test data automatically. | Automatically generates test cases, wide test coverage, complex test scenarios. | Gaining popularity in property-based testing. |

### Framework Foresight: Exploring the Advantages and Drawbacks

Certainly, here are the advantages and disadvantages of several popular Python testing frameworks and tools:

| Framework Name | Advantages              | Disadvantages |
|-----------------|----------------------|----------------------|
| `unittest`     |    - Built-in to Python's Standard Library. <br>- Supports test discovery. <br>- Offers test fixtures for setup and teardown.  |- Often considered verbose, leading to more code. <br>- Less concise syntax compared to other frameworks. <br>  - Limited advanced features compared to some third-party frameworks.|
| `unittest2`     | - Provides some advanced features and bug fixes over the original `unittest` in Python 2.      |   - No longer necessary or maintained in Python 3 and above.|
| `pytest`       |  - Concise and readable test code. <br> - Rich ecosystem of plugins for extending functionality. <br> - Powerful fixtures system for better test organization. <br> - Advanced features like parameterized testing.|  - Requires installation as it's not part of the Python Standard Library.<br> - Learning curve for advanced features, but it's worth it for complex testing.  |
| `nose`         |   - Supports test discovery and test running. <br>  - Allows the use of test attributes and offers better test discovery.<br> - Extensible through various plugins.             | - Less popular and maintained compared to `pytest`. <br>  - Limited features for advanced testing. <br>  - Somewhat dated and less extensible.|
| `nose2`        |   - An improved version of `nose` with better test discovery. <br>  - Supports test attributes and offers plugins. <br> - Provides support for parallel test execution.        |   - Less popular compared to `pytest`. <br>  - Still less known in the testing community. <br>  - Less extensible and feature-rich than `pytest`.|
| `doctest`      |   - Part of the Python Standard Library, so no need for additional installation.  <br>  - Allows embedding tests within documentation, making it great for documentation testing. <br>  - Offers simple test setup.      |   - Limited to testing docstrings. <br> - May not be suitable for complex test scenarios. <br>  - Less flexible compared to other frameworks.|
| `Behave`       |   - A Python implementation of the Gherkin language, making it suitable for behavior-driven development. <br>  - Easy to write human-readable test cases in plain text.      |   - Primarily designed for behavior-driven testing, not low-level unit testing. <br>  - May require additional libraries for integration with specific frameworks.
| `Robot Framework` |  - Keyword-driven testing approach for easier test case design. <br>  - Support for acceptance testing and integration with Selenium for web testing. <br>  - High-level test cases are easy to read and write.|  - Primarily used for acceptance and end-to-end testing, not low-level unit testing. <br>  - May require additional libraries for specific test cases.|
| `tox`          |   - Provides a way to manage and automate the testing of different Python environments. <br> - Useful for ensuring cross-version and cross-environment compatibility.          |   - May require additional configuration for specific project needs.<br>  - Not a testing framework itself but a tool for test automation.
| `Testify`      |  - A lightweight testing framework that supports test discovery. <br>- Offers fixtures and simple test case definitions. |  - Less feature-rich compared to some other frameworks like `pytest`. <br>  - Smaller community and less extensibility.
| `Hypothesis`   |  - Enables property-based testing, which automatically generates a wide range of test cases.  <br> - Helps discover edge cases and uncover unexpected issues. <br>  - Can generate complex test data for unbiased testing.        |   - Requires an understanding of property-based testing concepts.  <br>- May not be suitable for all types of testing. <br>  - Learning curve for those new to property-based testing.|
| `Playwright`   |  - Offers a Python library for end-to-end testing of web applications. <br>  - Supports multiple browsers.  <br> - Provides capabilities for automating web interactions. |   - Primarily designed for web application testing, not low-level unit testing. <br> - Requires web application setup and access to a browser.|


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




## Some Assitional Suggestions

* AI-Enhanced Static Code Analysis
  * DeepCode
  * Kite
* Mutation Testing 
  * MutPy
  * Pitest
* AI-Based Code Review
  * CodeClimate
  * DeepCode
## Other Frameworks of Python used in Test Automation
* UI automation
  * selenium webdriver
  * Toolium
  * webdriver_manager
  * gauge
  * splinter
  * Mailosaur
  * wtframework
  * Needle
  * PyPOM
  * pypom_form
  * Golem
  * Pylenium.io

## Taxonomy of Testing
* Unit Testing Frameworks: Unit testing is a fundamental aspect of software testing, verifying individual units or components of code to ensure they work as intended. 
  * pytest
  * unittest
* Functional Testing Frameworks: Functional testing involves testing the functionality and behavior of an application as a whole, simulating user interactions, and validating expected outcomes.
  * Selenium
  * testRigor
  * Robot Framework
* Integration Testing Frameworks: Integration testing involves testing the interaction and communication between different components or modules of an application.
  * PyTest-BDD

## References:

https://www.thoughtworks.com/radar

https://www.softwaretestinghelp.com/python-testing-frameworks/

https://www.browserstack.com/guide/top-python-testing-frameworks

https://www.testgrid.io/blog/python-testing-framework/

https://svitla.com/blog/testing-frameworks-for-python

https://www.learnenough.com/blog/python-unit-testing-frameworks

https://testautomationtools.dev/top-5-python-testing-frameworks/

https://www.lambdatest.com/blog/top-python-testing-frameworks/

https://medium.com/@arnabroyy/best-python-testing-frameworks-bb7ab1b3d366

https://www.testscenario.com/python-testing-frameworks/













<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyMzc1MTc5OSw3NzE4ODA2MTMsLTEyMT
IzMzEwMDldfQ==
-->




graph LR
  linkStyle default fill:#ffffff

  subgraph diagram[True North Services diagram]
    style diagram fill:#ffffff,stroke:#ffffff

    idEndUser["fa:fa-user<div style='font-weight: bold'>End User</div><div style='font-size: 70%; margin-top: 0px'>[Person]</div>"]
    style idEndUser fill:#08427b,stroke:#052e56,color:#ffffff

    subgraph CSP
        idFrontend("<div style='font-weight: bold'>Frontend</div><div style='font-size: 70%; margin-top: 0px'>[OJET]</div>")
        style idFrontend fill:#1168bd,stroke:#0b4884,color:#ffffff

        idBFF("<div style='font-weight: bold'>Backend-for-Frontend (BFF)</div><div style='font-size: 70%; margin-top: 0px'>[Apollo GraphQL (JS)]</div>")
        style idBFF fill:#1168bd,stroke:#0b4884,color:#ffffff

        idCSPIdentity("<div style='font-weight: bold'>Identity</div><div style='font-size: 70%; margin-top: 0px'>[<mark>TODO</mark>]</div>")
        style idCSPIdentity fill:#1168bd,stroke:#0b4884,color:#ffffff

        idCSPIdentityDataStore[(SpiceDB)]

        idBFF("<div style='font-weight: bold'>Backend-for-Frontend (BFF)</div><div style='font-size: 70%; margin-top: 0px'>[Apollo GraphQL (JS)]</div>")
        style idBFF fill:#1168bd,stroke:#0b4884,color:#ffffff

        idAuthorization("<div style='font-weight: bold'>Authorization</div><div style='font-size: 70%; margin-top: 0px'>[<mark>TODO</mark>]</div>")
        style idAuthorization fill:#1168bd,stroke:#0b4884,color:#ffffff

        idCSPPlaceholder("<div style='font-weight: bold'><mark>Placeholder</mark></div><div style='font-size: 70%; margin-top: 0px'>[<mark>TODO</mark>]</div>")
        style idCSPPlaceholder fill:#1168bd,stroke:#0b4884,color:#ffffff
    end

    subgraph True North
        idUser("<i class='fa-brands fa-python'></i><div style='font-weight: bold'>User</div><div style='font-size: 70%; margin-top: 0px'>[FastAPI]</div>")
        style idUser fill:#1168bd,stroke:#0b4884,color:#ffffff

        idOrganization("<i class='fa-brands fa-python'></i><div style='font-weight: bold'>Organization</div><div style='font-size: 70%; margin-top: 0px'>[FastAPI]</div>")
        style idOrganization fill:#1168bd,stroke:#0b4884,color:#ffffff

        idRecommendation("<i class='fa-brands fa-python'></i><div style='font-weight: bold'>Recommendation</div><div style='font-size: 70%; margin-top: 0px'>[FastAPI]</div>")
        style idRecommendation fill:#1168bd,stroke:#0b4884,color:#ffffff

        idProduct("<i class='fa-brands fa-python'></i><div style='font-weight: bold'>Product</div><div style='font-size: 70%; margin-top: 0px'>[FastAPI]</div>")
        style idProduct fill:#1168bd,stroke:#0b4884,color:#ffffff

        idNotification("<i class='fa-brands fa-python'></i><div style='font-weight: bold'>Notification</div><div style='font-size: 70%; margin-top: 0px'>[FastAPI]</div>")
        style idNotification fill:#1168bd,stroke:#0b4884,color:#ffffff

        idUserDataStore[(Data Store)]
        idOrganizationDataStore[(Data Store)]
        idRecommendationDataStore[(Data Store)]
        idProductDataStore[(Data Store)]

        idMyLearn("<i class='fa-brands fa-js'></i><div style='font-weight: bold'>MyLearn</div><div style='font-size: 70%; margin-top: 0px'>[Nest, Typescript & OJET]</div>")
    end

    idOCIStreamming("<div style='font-weight: bold'>OCI Streamming</div>")

    idEndUser-. "<div>HTTP request</div><div style='font-size: 70%'></div>" .->idFrontend
    idFrontend-. "<div>HTTP request</div><div style='font-size: 70%'></div>" .->idBFF
    idBFF-. "<div>HTTP request</div><div style='font-size: 70%'></div>" .->idUser
    idBFF-. "<div>HTTP request</div><div style='font-size: 70%'></div>" .->idOrganization
    idBFF-. "<div>HTTP request</div><div style='font-size: 70%'></div>" .->idRecommendation
    idBFF-. "<div>HTTP request</div><div style='font-size: 70%'></div>" .->idProduct
    idOrganization-. "<div>Produces Event</div><div style='font-size: 70%'></div>" .->idOCIStreamming
    idOCIStreamming-. "<div>Consumes Event</div><div style='font-size: 70%'></div>" .->idNotification

    idUser<-. "<div>I/O</div><div style='font-size: 70%'></div>" .->idUserDataStore
    idOrganization<-. "<div>I/O</div><div style='font-size: 70%'></div>" .->idOrganizationDataStore
    idRecommendation<-. "<div>I/O</div><div style='font-size: 70%'></div>" .->idRecommendationDataStore
    idProduct<-. "<div>I/O</div><div style='font-size: 70%'></div>" .->idProductDataStore

    idRecommendation-. "<div>HTTP Request</div><div style='font-size: 70%'></div>" .->idMyLearn

    idCSPIdentity-. "<div>I/O</div><div style='font-size: 70%'></div>" .->idCSPIdentityDataStore
    idUser-. "<div>HTTP Request</div><div style='font-size: 70%'></div>" .->idCSPIdentity
    idRecommendation-. "<div>HTTP Request</div><div style='font-size: 70%'></div>" .->idCSPIdentity
    idOrganization-. "<div>HTTP Request</div><div style='font-size: 70%'></div>" .->idCSPIdentity
    idProduct-. "<div>HTTP Request</div><div style='font-size: 70%'></div>" .->idCSPIdentity
    idBFF-. "<div>HTTP Request</div><div style='font-size: 70%'></div>" .->idAuthorization
    idCSPPlaceholder-. "<div>Produces Event</div><div style='font-size: 70%'></div>" .->idOCIStreamming
  end
