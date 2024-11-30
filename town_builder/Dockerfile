FROM python:3.11

WORKDIR /app

COPY ./town_builder/requirements.txt /app
RUN pip install -r requirements.txt

COPY .town_builder /app
EXPOSE 8000:8000
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]