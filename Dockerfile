FROM alpine

COPY . /flaskfight-app
WORKDIR /flaskfight-app

EXPOSE 5000

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]
