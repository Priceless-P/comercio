FROM python:3.11.7-slim
COPY . /user_service
WORKDIR /user_service
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]
