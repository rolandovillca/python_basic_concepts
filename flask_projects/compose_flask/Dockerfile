FROM python:2.7
WORKDIR /code
COPY . .
#RUN apk add --no-cache gcc musl-dev linux-headers
#COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]
