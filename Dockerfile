FROM python:3.10-slim

WORKDIR /app/

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \  
    software-properties-common \
    git \
    espeak-ng \
    && apt-get clean \ 
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/SadeghKrmi/pertts-streamlit.git .

RUN curl -LO https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_amd64.tar.gz \
    && tar -xvzf piper_amd64.tar.gz \
    && rm -rf ./piper/espeak-ng-data \
    && rm -rf piper_amd64.tar.gz

RUN curl -LO https://github.com/SadeghKrmi/espeak-ng/releases/download/v1.0.0/espeak-ng-data.tar.gz \
    && mkdir espeak-ng-data && tar -xzvf espeak-ng-data.tar.gz -C espeak-ng-data \
    && mv espeak-ng-data ./piper/ \
    && rm -rf espeak-ng-data.tar.gz 

RUN pip3 install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
