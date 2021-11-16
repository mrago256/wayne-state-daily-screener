Auto Daily Screener
===================

Introduction
------------

The intended purpose of these scripts is to make it easier to fill out the daily
screener at wayne state. They get the information once and when configured, fill
out the daily screener everyday without user input. It should be used at your
own risk, and if some health issue comes up, fill out the daily screener manually
to notify the university of these changes.

## Setup

Install Selenium using:

    $ pip install selenium

Make sure the file "chromedriver" is in the same directory as the rest of the files.

Install FuzzyWuzzy using:

    $ pip install fuzzywuzzy

Note: If the error Install python-Levenshtein to remove this warning appears at runtime,
run:

    $ pip install python-Levenshtein

and run the rile again

## Libraries

### Browser Automation

Browser automation is managed by the Selenium python module.

Documentation for the library can be found [here](https://pypi.org/project/selenium/).

### Fuzzy String Matching

Fuzzy string matching is managed by the FuzzyWuzzy python module.

Documentation for the library can be found [here](https://pypi.org/project/fuzzywuzzy/).

