# Flask API Example

A simple Flask API with two endpoints that accept JSON input and return JSON output.

## Endpoints

1. `/sum`: Accepts a JSON object containing a list of numbers and returns the sum of the numbers.
2. `/concat`: Accepts a JSON object containing two strings and returns the concatenated result.

## Installation

1. Clone this repository:

git clone https://github.com/SyedhasnatHaiderShah/Math-String-API.git


## Running the API

1. Run the Flask app:

python app.py


2. Test the API using `curl` or an API client like Postman.

# For /sum endpoint:

curl -X POST -H "Content-Type: application/json" -d '{"numbers": [1, 2, 3, 4, 5]}' http://localhost:5000/sum

# For /concat endpoint:

curl -X POST -H "Content-Type: application/json" -d '{"string1": "Hello, ", "string2": "World!"}' http://localhost:5000/concat

