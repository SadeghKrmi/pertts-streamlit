## pertts (persian text-to-speech)
This is implementation of web interface for pertts (persian text-to-speech)


![image](https://github.com/SadeghKrmi/pertts-streamlit/assets/5988663/e2475995-7d06-4af0-a57e-e3b834b88617)


How to run?
```bash
docker build --no-cache -t pertts:1.0 .
docker container run --name st --rm -it -p 8501:8501 pertts:1.0
```
