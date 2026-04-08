# GreenCity events page testing

## Project Overview
This repository contains a set of test cases for the **Events** page of the GreenCity web application. 

## Task Description 
The goal of the task is to get acquainted with the basic principles of creating test cases. 
The objective is to analyze the GreenCity events page and document at least 3 structured test cases in Markdown format.

## Tested Page
* **URL:** [GreenCity Events](https://www.greencity.cx.ua/#/greenCity/events)

## Repository Structure
* `test-cases/events-page-tests.md` — Contains 3 detailed test cases in Markdown format.
* `tests/test_events_page.py` — Contains 3 implemented test cases with Selenium.
* `requirements.txt` - requirements for the project


## Known Issues:

test_status_checkbox may fail
When both "Open" and "Closed" checkboxes are deselected, the UI does not select "Any status".


## Execution instructions
1. Clone repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `python -m unittest discover tests`


## Author
* **Name:** Andrii Doroshuk
