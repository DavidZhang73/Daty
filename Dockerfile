FROM python:alpine
LABEL author="DavidZ"
# 创建工作目录
RUN mkdir /daty/
# 更改工作目录
WORKDIR /daty/
# 更改alpine, pip镜像源
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# 安装python依赖
COPY ./Pipfile /daty/Pipfile
COPY ./Pipfile.lock /daty/Pipfile.lock
RUN pip install pipenv \
    && pipenv install
# 安装uwsgi
RUN apk add -U --no-cache gcc linux-headers musl-dev \
    && pipenv install uwsgi \
    && apk del gcc linux-headers musl-dev
# 暴露端口
EXPOSE 8002
# 启动服务
CMD pipenv run uwsgi --ini /config/uwsgi.ini
