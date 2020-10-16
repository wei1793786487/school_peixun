
FROM python

RUN pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD mkdir /python/

COPY *.py /python/

WORKDIR /python/

ENV FLASK_APP=web.py

CMD flask run --host=0.0.0.0

EXPOSE 5000

