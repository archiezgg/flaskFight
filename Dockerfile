FROM alpine

COPY . .

EXPOSE 5000

RUN ["apk", "add", "py-pip"]
RUN ["pip", "install", "-r", "requirements.txt", "--user", "--upgrade"]
CMD ["python", "app.py"]
