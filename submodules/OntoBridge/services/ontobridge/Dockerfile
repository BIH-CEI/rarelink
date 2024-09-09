FROM ubuntu:22.04

RUN apt-get update && \
		apt-get install -y python3.11 python3-pip openjdk-11-jdk && \
		apt-get install bash-completion && \
		apt-get install -y python3-pip

WORKDIR /app

COPY requirements.txt .

RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt

COPY . .


EXPOSE 5000

CMD ["python3", "main.py"]
