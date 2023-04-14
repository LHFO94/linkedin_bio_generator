FROM python:3.10-slim-buster
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5500
ENV FLASK_APP=app.py
CMD ["flask", "run", "--port", "5500"]