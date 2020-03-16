# FastAPI experiment

experimenting with [FastAPI](https://github.com/tiangolo/fastapi)

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

