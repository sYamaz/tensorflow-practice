FROM python:3.11-bookworm
RUN pip install --upgrade pip
RUN pip install tensorflow==2.13.*
