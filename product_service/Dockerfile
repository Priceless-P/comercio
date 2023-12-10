FROM python:3.11.7-slim
COPY . /product_service
WORKDIR /product_service
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]
