FROM python:3.11

WORKDIR /app

COPY ./website/requirements.txt /app
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y \
    iputils-ping \
    dnsutils \
  && rm -rf /var/lib/apt/lists/*

COPY ./website/ /app
EXPOSE 5000:5000
CMD [ "python3", "pages.py", "--port", "5000"]
