# docker image
FROM python:3.10
# copy pyproject.toml
COPY pyproject.toml pyproject.toml
# install libraries
RUN pip install poetry==1.8.0
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install -r requirements.txt
RUN apt-get update -y && apt-get install -y curl
# copy files
COPY . /app
# set work directory
WORKDIR /app
# run program [exec]
CMD ["python","cli.py"]
