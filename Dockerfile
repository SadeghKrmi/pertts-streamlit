FROM python:3.10-slim

WORKDIR /app/

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    build-essential \
    curl \  
    git \
    make \
    autoconf \
    automake \
    libtool \
    pkg-config && \
    apt clean && \ 
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/SadeghKrmi/pertts-streamlit.git . && \
    curl -LO https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_amd64.tar.gz && \
    tar -xvzf piper_amd64.tar.gz && \
    rm -rf ./piper/espeak-ng-data && \
    rm -rf piper_amd64.tar.gz


RUN git clone https://github.com/SadeghKrmi/espeak-ng.git && \
    cd ./espeak-ng && \
    chmod +x ./autogen.sh && \
    ./autogen.sh && \
    ./configure --prefix=/usr && \
    make && \
    make install && \
    cp -r espeak-ng-data /app/piper/ && \
    cd /app && \
    pip3 install --no-cache-dir -r requirements.txt

RUN apt autoremove -y \
    && apt clean -y \
    && apt-get purge -y \
        build-essential \
        curl \
        git \
        make \
        autoconf \
        automake \
        libtool \
        pkg-config && \
    rm -rf /app/espeak-ng

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
