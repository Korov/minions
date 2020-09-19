FROM python:3.8.5-buster

LABEL author="korov" email="korov9@163.com" date="2020-08-29"

COPY . /

WORKDIR /

RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "begin.py" ]