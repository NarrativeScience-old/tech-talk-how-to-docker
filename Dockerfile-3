FROM python:3.7-rc-alpine

RUN pip install aiohttp

RUN mkdir -p /app
WORKDIR /app
COPY server.py server.py

EXPOSE 8080

CMD ["python", "server.py"]
