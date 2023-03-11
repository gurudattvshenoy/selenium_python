# selenium python automation framework
Example UI automation framework using Selenium Python. This framework uses pytest to write script and selenium to perform action against browser.


# Features
1. Abilty to automate website.
2. Shows results in html reports.
3. Test execution logging. 

# Configure and run tests:
To install the framework follow below steps:

## 1. Download the project or clone the project.
git clone https://github.com/gurudattvshenoy/selenium_python.git

## 2. Change the directory to selenium_python.

Eg: cd selenium_python/

## 3.Install dependencies for the framework using requirements.txt.

pip install requirements.txt

## 4.Navigate to tests folder and run the below command to execute the tests:

 pytest -v --html=reports/report-sauselab-login.html
