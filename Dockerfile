FROM python:3.8.3-slim

RUN pip install --no-cache-dir numpy pandas tqdm timeout-decorator
COPY . /home/aicrowd
WORKDIR /home/aicrowd
