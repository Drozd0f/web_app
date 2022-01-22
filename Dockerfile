FROM python:3.8 as base
WORKDIR web_app
COPY web_app/requirements.txt .
RUN pip install -r requirements.txt
COPY web_app/ .
EXPOSE 4444


FROM base as dev
RUN pip install aiohttp-devtools
