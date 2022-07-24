# Projet 1CS backend

Back-end du projet 1CS `E-tourisme` avec FastAPI, PostgreSQL, Docker and Heroku.


## Features
- Docker with [FastAPI](https://fastapi.tiangolo.com/) and [PostgresSQL](https://www.postgresql.org/).
- Authentication and securing routes with [JWT tokens](https://jwt.io/)
- Fastapi which means an interactive API documentation.

Built on Python: 3.8.


## File Structure
```
.
├── app
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   ├── .env
│   └── src
│       ├── api
│           ├── endpoints
│           ├── api.py
│           └── deps.py
│       ├── core
│           ├── config.py
│           └── security.py
│       ├── crud
│           ├── base.py
│       ├── db
│           ├── base_class.py
│           ├── base.py
│           ├── init_db.py
│           └── session.py
│       ├── models
│       └── schemas
└── docker-compose.yml
```

## Installation and usage
- clone the repository
```bash
git clone git@github.com:m0kr4n3/fastapi_projetct_template.git
cd fastapi_projetct_template/app/
```
1) Using python
- use `venv` virtual environment
```bash
pip install venv
python -m venv venv
source $PWD/venv/bin/activate
```
- Install dependencies
```bash
pip install -r requirements.txt
```
- Create env from env template:
```bash
cp example.env .env #only once
```
- Put there the necessary info
- Run main.py
```bash
python main.py
```
2) Using docker
Install docker-compose if it's not  done already
```bash
sudo apt install docker-compose
```
- Run docker-compose in the repo root directory :
```bash
sudo docker-compose up
```

#### Used this template  [FastAPI Project Template](https://github.com/m0kr4n3/fastapi_project_template)
