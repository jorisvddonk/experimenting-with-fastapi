# FastAPI experiment

experimenting with [FastAPI](https://github.com/tiangolo/fastapi) and asyncio in Python3

This project implements a very simple API exposing the number of confirmed Coronavirus cases, sourced from each country's official data.

Data is not cached at the moment, so whenever a request is made, outbound requests are made.

## Running

via docker:

```
docker build . -t fastapi-experiment-test
docker run -it --rm --publish-all=true fastapi-experiment-test
```

otherwise:

```
pyenv install 3.8.2
pyenv global 3.8.2
pip install -r requirements.txt
uvicorn src.main:app --reload
```

