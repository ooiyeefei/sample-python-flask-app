FROM python:3.9-slim

COPY ./app /Octank
WORKDIR /Octank
RUN pip3 install -r requirements.txt
EXPOSE 80
EXPOSE 8080
ENTRYPOINT ["python3"]
CMD ["main.py"]