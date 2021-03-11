## Billogram Discount Codes
Small application built for creating and retrieving discount codes for a certain brand

**Requirements**: Python 3.6+

## Documentation
When the application is started automatically generated swagger documentation will be available at http://127.0.0.1:8000/docs


## Quickstart
Create a venv and install the dependencies using `pip`:

```shell
$ pip install -r requirements.txt
```
This will install the application with the needed dependencies for using the api

Start the application:

```shell
$ uvicorn billogram_app.main:app
```

This will start the application and create a sqlite-database that will store the generated discount codes

## Usage

There are two available endpoints:
- /discount_codes/generate_codes/{brand_id}
    - curl -X GET "http://127.0.0.1:8000/discount_codes/generate_codes/7?no_of_codes=3" -H  "accept: application/json"
- /discount_codes/get_code/{brand_id}
    - curl -X GET "http://127.0.0.1:8000/discount_codes/get_code/2" -H  "accept: application/json"