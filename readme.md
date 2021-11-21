Auto Daily Screener
===================

Introduction
------------

The intended purpose of these scripts is to make it easier to fill out the daily
screener at Wayne State. They get the information once and when configured, fill
out the daily screener everyday without user input. It should be used at your
own risk, and if some health issue comes up, fill out the daily screener manually
to notify the university of these changes.

## Setup

### Install Selenium using:

    $ pip install selenium

#### Driver files:

Refer to [Section 1.5](https://selenium-python.readthedocs.io/installation.html#drivers)
of the Selenium documentation. Driver file must match browser version.

[Chrome](https://sites.google.com/chromium.org/driver/downloads)

[Firefox](https://github.com/mozilla/geckodriver/releases)

Make sure the driver file is in the same directory as AutoScreener.py.

### Install FuzzyWuzzy using:

    $ pip install fuzzywuzzy

Note:If the error Install python-Levenshtein to remove this warning appears at runtime:

    $ pip install python-Levenshtein

and run the rile again

### Create user file

    $ python3 CreateFile.py

This asks for user login information and buildings that
will be entered. The password is obfuscated for *some* level of security.

CreateFile.py only needs to be run if buildings change.

### Fill out screener

    $ AutoScreener.py

This is the script which loads the screener and inputs informaton. Add it to
computer autorun directory for full automation. It is recommended to run this
manually at least once to check for errors.

## Runtime Errors

### CreateFile.py

```
Rerun script and remove commas from credentials
```

This occurs when the user inputs commas in either their username, password, or
phone number.

### AutoScreener.py

```
The data file does not exist. Try running CreateFile.py first
```
Make sure that CreateFile.py has been run and the screenerData.csv file is in the
same directory as AutoScreener.py

```
Driver file not found. Please refer to readme
```
Verify the driver file is in the same directory as AutoScreener.py

This error also occurs if the browser version does not match the driver version.

```
Building error. Rerun CreateFile.py
```

This error occurs if the screenerData file somehow gets edited externally.
Re-running CreateFile.py should fix it.

## Libraries

### Browser Automation

Browser automation is managed by the Selenium python module.

Documentation for the library can be found [here](https://pypi.org/project/selenium/).

### Fuzzy String Matching

Fuzzy string matching is managed by the FuzzyWuzzy python module.

Documentation for the library can be found [here](https://pypi.org/project/fuzzywuzzy/).

