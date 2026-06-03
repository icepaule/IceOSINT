FROM python:3.12-slim

WORKDIR /app

# System Dependencies
RUN apt-get update && apt-get install -y \
    git \
    dnsutils \
    whois \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Python Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# OSINT Tools
RUN git clone --depth=1 https://github.com/laramies/theHarvester.git /opt/theHarvester && \
    git clone --depth=1 https://github.com/aboul3la/Sublist3r.git /opt/Sublist3r

# App
COPY . /app

ENV PYTHONUNBUFFERED=1
ENV PATH="/opt/theHarvester:/opt/Sublist3r:$PATH"

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
