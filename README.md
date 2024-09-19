# AnnotationAlchemist
Site to convert between image labeling formats

## AAClient

### Getting started:
~~~
cd AAClient
pnpm i
pnpm dev
~~~

## AAApi

### Getting started:
~~~
cd AAApi
conda env create -f environment.yml
uvicorn app.main.py --reload # It is important to run this command from within the AAApi directory
~~~
