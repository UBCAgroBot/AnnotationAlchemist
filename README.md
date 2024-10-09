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
uvicorn app.main:app --reload # It is important to run this command from within the AAApi directory
~~~

### Temp
initial idea for cluster setup using [k3s](https://docs.k3s.io/)
<img width="1175" alt="Screenshot 2024-09-16 at 21 31 18" src="https://github.com/user-attachments/assets/19f930bc-3354-4aab-aaae-b22ec26d8d95">

