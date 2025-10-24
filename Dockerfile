# Using Python 3.12 slim image as it is less bloated 
# and neither have I done much work in later versions > 3.12
FROM python:3.12-slim

RUN apt update && apt install -y git ca-certificates build-essential

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

RUN chmod +x /code/entrypoint.sh

ENTRYPOINT ["/bin/sh", "/code/entrypoint.sh"]