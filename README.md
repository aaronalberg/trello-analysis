# trello-analysis
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![docs](https://img.shields.io/badge/docs-yes-brightgreen)](docs/README.md)

**Aaron Alberg** - [`aalberg2@illinois.edu`](mailto:aalberg2@illinois.edu)

## Overview
trello-analysis was born because I realized I couldn't count the number of cards in each list in the Trello Board I was using to track job applications.

## Dependencies
- `Trello API`  https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/
- `python-dotenv`  https://pypi.org/project/python-dotenv/

## Usage
- Clone this repository on your machine using the link at the top right of this page
- Make sure you have python3 and the python-dotenv package installed
  - You can use `pip install -U python-dotenv`
- Populate your .env file in the root of the project with the following values
  - `API_KEY` ![Trello tutorial](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/)
  - `API_TOKEN` ![Trello tutorial](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/)
  - `BOARD_ID` The ID of the Trello board you want to analyze (you can find this by adding `.json` to the end of your 
  board URL)
  - `FULL_DETAILS` Whether or not you want the names of the cards printed along with the summaries of each list
- That's it! Use `python3 trello.py` from the project directory to run the script
