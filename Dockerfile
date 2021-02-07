FROM python:3.7
ENV PYTHONUNBUFFERED=1
WORKDIR /E-Health-Care
COPY requirements.txt /E-Health-Care/
RUN pip3 install -r requirements.txt
COPY . /E-Health-Care/