FROM python:3.6-slim
WORKDIR /app
ADD . /app
RUN apt update && apt install procps htop curl nano -y && pip install -r /app/requirements.txt
EXPOSE 8000
CMD ["python", "main.py"]
