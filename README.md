[![Lint](https://github.com/Drozd0f/web_app/actions/workflows/linter.yml/badge.svg)](https://github.com/Drozd0f/web_app/actions/workflows/linter.yml)
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0D76A8)](https://www.linkedin.com/in/daniil-drozdov-a5393521b/)


# Виконання другого тестового завдання в EVO Python Lab 2022

## Practice project

### Dependencies
* Docker
* docker-compose
* Make

#### Quick start

First of all, set environment variables
```shell
export APP_DB_USERNAME="username"
export APP_DB_PASSWORD="password"
export APP_DB_DATABASE="database"
```

---

To run
```shell
make
```

Application will be hosted on http://localhost:80

---

To display container logs
```shell
make logs
```

---

To remove containers
```shell
make rm
```
