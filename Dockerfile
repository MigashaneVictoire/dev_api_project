FROM python:3.12.11-slim-bookworm

WORKDIR /workspace
COPY . .

RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt

CMD ["pytest"]