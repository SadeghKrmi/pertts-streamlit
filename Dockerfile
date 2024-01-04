FROM python:3.10-slim

WORKDIR /app/

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \  
    software-properties-common \
    git \
    espeak-ng \
    make \
    autoconf \
    automake \
    libtool \
    pkg-config \
    && apt-get clean \ 
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/SadeghKrmi/pertts-streamlit.git .

RUN curl -LO https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_amd64.tar.gz \
    && tar -xvzf piper_amd64.tar.gz \
    && rm -rf ./piper/espeak-ng-data \
    && rm -rf piper_amd64.tar.gz


RUN git clone https://github.com/SadeghKrmi/espeak-ng.git && \
    cd ./espeak-ng && \
    chmod +x ./autogen.sh && \
    ./autogen.sh && \
    ./configure --prefix=/usr && \
    make && \
    make install && \
    cp -r espeak-ng-data /app/piper/

RUN cd /app && \
    pip3 install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
