# Build and run python build script

FROM python:3.7-alpine
COPY build.py /opt/build
CMD ["python3", "/opt/build/build.py"]