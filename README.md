# Samurai02 API RAG

based on: Flask Starter Website 03

![Flask and DashAndData Logo](https://venturer.dashanddata.com/website_assets_images/dd_and_flask_02-400x209.png)

## Description

This is a RAG app using the Samurai02 API.

## How to run

`flask run`

## How to run with .flaskenv and .env on the server and locally

`flask run`

### set up .env

- see .env.example
- the key variables for running the Flask portion of the app are:

```
FLASK_RUN_HOST="0.0.0.0"
FLASK_RUN_PORT=8003
```

### set up .flaskenv

the server has not been responding well to placiing variables in the .flaskenv file.

- these are the only ones that seem to matter and even that i'm not sure.

```
FLASK_APP=run
FLASK_DEBUG=1
```

## test endpoint

`curl -v http://127.0.0.1:5050/ping`
