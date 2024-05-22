# Emission Ledger API

This is an example of API that handles purchase authorizations for cardholders, interacting with the Dock system to validate and process transactions.

## Installation

To install this project, you will need [Poetry](https://python-poetry.org/).

Once you have Poetry installed, follow these steps:

1. Clone the repository

2. Install dependencies:

```sh
poetry install
```

## Run API

Once you install dependencies, you can run the API with this command:

```sh
poetry run uvicorn src.main:app --reload
```

## Test endpoints

Open the API documentation "localhost:8000/docs" and test authorizations/purchase endpoint. In examples folder you can find an example of body for this EP.
