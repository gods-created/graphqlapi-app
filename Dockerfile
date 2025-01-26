FROM python:3
COPY . /app
WORKDIR /app 
RUN chmod 777 -R /app/*
RUN chmod +x /app/entrypoint.sh
RUN pip install -r requirements.txt
ENTRYPOINT ["sh", "/app/entrypoint.sh"]