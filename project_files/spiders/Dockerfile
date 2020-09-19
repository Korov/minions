FROM python:3.8.5-buster

LABEL author="korov" email="korov9@163.com" date="2020-08-29"

ENV PATH /usr/local/bin:$PATH

COPY . /spider

WORKDIR /spider

RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r requirements.txt

CMD [ "python3" , "begin.py" ]