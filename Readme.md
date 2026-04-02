
# GitHub CI/CD Integration Demo: SauceDemo & RosarioSIS

## 📌 Project Overview

This repository demonstrates a robust **CI/CD pipeline** integrating automated testing for two distinct web environments. By utilizing **GitHub Actions**, this project showcases the ability to manage testing lifecycles for both a streamlined demo application and a complex, real-world Open Source system.

### Tested Applications:

1.  **[SauceDemo](https://www.google.com/search?q=https://www.saucedemo.com/):** A standardized, "perfect" environment used to validate baseline automation scripts.
2.  **[RosarioSIS](https://www.rosariosis.org/demonstration/):** A complex Student Information System (SIS) used to test deep logic, data integrity, and multi-module navigation.

-----

## 🧠 Reflection: The Psychology of Testing

Testing these two platforms required a significant shift in cognitive approach:

  * **SauceDemo (The Controlled Script):** My mindset here was **Verification**. Because the environment is highly predictable, the psychological focus was on the efficiency and speed of the automation scripts. It felt like a "safe" space to practice syntax and CI/CD triggers.
  * **RosarioSIS (The Critical Evaluation):** My mindset shifted to **Validation and Exploration**. Testing an ERP system involves high stakes—errors in school management software impact users, data, and schedules. This environment triggered a more skeptical, "destructive" testing approach, where I looked for edge cases in form submissions and navigation flows that simpler sites don't possess.

-----

## 🔄 STLC Implementation

Applying the **Software Testing Life Cycle (STLC)** was the backbone of this project. It ensured that testing wasn't just "clicking buttons" but a professional, repeatable process:

| STLC Phase | Application in this Project |
| :--- | :--- |
| **Requirement Analysis** | Identifying specific user stories for SauceDemo (Login/Cart) vs. RosarioSIS (Data entry). |
| **Test Planning** | Defining the scope of what to automate in the GitHub Action workflow. |
| **Test Case Development** | Writing scripts that could handle the simple DOM of SauceDemo and the complex structure of RosarioSIS. |
| **Environment Setup** | Configuring the CI/CD YAML to ensure the correct dependencies were installed in the GitHub runner. |
| **Test Execution** | Triggering the pipeline on every `push` or `pull_request`. |
| **Test Closure** | Analyzing the logs and artifact reports to verify system stability. |

-----

## 🛠️ Professional QA Lessons Learned

If I were applying these lessons as a QA Engineer in a corporate environment, I would focus on:

1.  **Context-Aware Automation:** Not all apps are created equal. I learned to build **resilient locators** for complex systems like RosarioSIS that are less likely to break during UI updates compared to the "easy" targets in SauceDemo.
2.  **The Value of Shift-Left Testing:** By integrating these tests into GitHub Actions, I’ve learned that catching a bug during the build phase is significantly more efficient than manual discovery.
3.  **Data Integrity Focus:** RosarioSIS taught me that UI testing is only the surface. In a professional setting, I would apply the lesson of verifying the *back-end state* after a front-end action is performed.
4.  **Scalability of CI/CD:** This project proves that a single pipeline can manage multiple, diverse test suites, a critical skill for maintaining large-scale microservices or enterprise platforms.


