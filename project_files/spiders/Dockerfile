FROM python:3.8.5-buster

LABEL author="korov" email="korov9@163.com" date="2020-08-29"

ENV PATH /usr/local/bin:$PATH

COPY . /spider

WORKDIR /spider

RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r requirements.txt

RUN rm /usr/local/lib/python3.8/site-packages/scrapyd/default_scrapyd.conf
COPY ./default_scrapyd.conf /usr/local/lib/python3.8/site-packages/scrapyd

RUN chmod +x /spider/entrypoint.sh

ENTRYPOINT ["bash", "/spider/entrypoint.sh"]

CMD [ "python3" , "begin.py" ]