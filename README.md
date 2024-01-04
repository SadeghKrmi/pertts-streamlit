## pertts (persian text-to-speech)
This is implementation of web interface for pertts (persian text-to-speech)


How to run?
```bash
docker build --no-cache -t pertts:1.0 .
docker container run --name st --rm -it -p 8501:8501 pertts:1.0
```
