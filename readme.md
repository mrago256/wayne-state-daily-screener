Auto Daily Screener
===================

Introduction
------------

The intended purpose of these scripts is to make it easier to fill out the daily
screener at Wayne State. They get the information once and when configured, fill
out the daily screener everyday without user input. It should be used at your
own risk, and if some health issue comes up, fill out the daily screener manually
to notify the university of these changes.

Note: This only works on Linux currently. Windows support is being developed.

## Setup

### Prerequisites:

In order to run this program, you msut have Python 3 and pip installed.

Note: When installing python on Windows, make sure to check option to add
Python to PATH.

The installer will warn the user and not proceed if this condition is not met.

### Automatic Install:

#### Windows:

Run **Windows-Installer.bat** and choose install type.

Note: When installing and running CreateFily.py the following warning will appear:

```
UserWarning: Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning
```

This is fine.

#### Linux:

    $ ./Linux-Installer.sh

This will prompt for the type of install or to uninstall. It will also run the
CreateFile.py script.

### Manual Install for Linux:

Follow these steps to install the autoscreener manually. It is recommended
to use the installer.

### Install python dependencies:

    $ pip install -r requirements.txt

from the main folder

### Driver files:

Note: This step can be omitted if host system is running linux

Refer to [Section 1.5](https://selenium-python.readthedocs.io/installation.html#drivers)
of the Selenium documentation. Driver file must match browser version.

[Chrome Driver Link](https://sites.google.com/chromium.org/driver/downloads)

Make sure the driver file is in the same directory as AutoScreener.py.

The Autoscreener only works with Google Chrome. Google Chrome must be installed
for it to function.

### Create user file

    $ python3 CreateFile.py

This asks for user login information and buildings that
will be entered. The university ID password is obfuscated for *some* level of security but it is
**not** encrypted.

CreateFile.py only needs to be run if buildings change.

### Fill out screener

    $ AutoScreener.py

This is the script which loads the screener and inputs information. Add it to
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

Browser automation is managed by the selenium python module.

Documentation for the library can be found [here](https://pypi.org/project/selenium/).

### Fuzzy String Matching

Fuzzy string matching is managed by the fuzzywuzzy python module.

Documentation for the library can be found [here](https://pypi.org/project/fuzzywuzzy/).

### Windows Toast

Windows toast notifications are handled by the win10toast python module.

Documentation for the library can be found [here](https://pypi.org/project/win10toast/).

## License

[MIT License](https://opensource.org/licenses/mit-license.html)
