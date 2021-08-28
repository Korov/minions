FROM python:3.8.10

LABEL author="korov" email="korov9@163.com" date="2021-08-28"

ENV SPIDER_HOME /spiders

RUN mkdir $SPIDER_HOME

WORKDIR $SPIDER_HOME

COPY . $SPIDER_HOME/

RUN rm -rf $SPIDER_HOME/logs && rm -rf $SPIDER_HOME/venv && \
    pip install pipenv && cd $SPIDER_HOME/ && \
    pipenv install --system --deploy --ignore-pipfile

CMD ["pipenv", "run", "scrapy", "list" ]