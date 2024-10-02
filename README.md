## pertts (persian text-to-speech)
This is the implementation and a web interface for pertts (Persian text-to-speech)

powered by [piper](https://github.com/rhasspy/piper)

the live version of persian tts called [pertts](https://tts.datacula.com/)

![image](https://github.com/SadeghKrmi/pertts-streamlit/assets/5988663/9b8c751b-d5e7-42eb-9c7f-2516aed6baa6)
with love from datacula.com


**Voices**: We are using an AI-based TTS system, trained with 
- amir: Amir Sooakhsh's voice from [rokhpodcast](https://rokhpodcast.ir/), Special thanks to Amir :)
- ganji: Ahmad Ganji voice


### dataset
https://huggingface.co/datasets/SadeghK/datacula-pertts-amir


### 🛠️ Installation

#### docker
Build with docker from scratch and run
```bash
docker build --no-cache -t pertts:1.0 .
docker container run --name st --rm -it -p 8501:8501 pertts:1.0
```

Run the latest version of the docker image from docker hub
```bash
docker image pull sadeghk/pertts
docker container run --name st --rm -it -p 8501:8501 sadeghk/pertts
```

#### python
install piper-tts using pip and download the model in pertts-streamlit/model directory

``
pip install piper-tts
```
and then run
```bash
echo 'سلام و درود بر همه فارسی زبانان' | piper \
  --model epoch=5261-step=2455712.onnx \
  --output_file dorood.wav
```

#### Windows
download the executables for windows _piper_windows_amd64.zip_ from [piper](https://github.com/rhasspy/piper/releases), and unzip
go to the piper directory where piper.exe exists and create a folder with the name models. Download the model for Persian/Farsi from [huggingface](https://huggingface.co/rhasspy/piper-voices/tree/main/fa/fa_IR/amir/medium) with name _fa_IR-amir-medium.onnx_ and _fa_IR-amir-medium.onnx.json_ to models directory.

open a PowerShell and `cd` to the directory where piper.exe exists, and run
```bash
echo "سلام و درود بر شما" | .\piper.exe --model .\models\fa_IR-amir-medium.onnx --output_dir .\outputs
```


