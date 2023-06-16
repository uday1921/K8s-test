FROM  python

ARG APP_DIR=/app/eks/

RUN mkdir -p $APP_DIR

WORKDIR $APP_DIR

COPY manager.py ./manager.py

COPY requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "python3", "/app/eks/manager.py" ]