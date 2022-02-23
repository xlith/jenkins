# Build and run python build script

FROM python:3.7-alpine
WORKDIR /opt/build/
COPY build.py ./
CMD ["python3", "./build.py"]