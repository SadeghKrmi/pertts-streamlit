from time import time
import streamlit as st
import subprocess
import io

# Function to inject custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.set_page_config(
    page_title='DataCula perTTS',
    page_icon=':rocket:'
)




# Sidebar
st.sidebar.image('./img/datacula.png', width=32)

st.sidebar.markdown(
    "Let's explore data science with [DataCula!](https://datacula.com)"
)


st.sidebar.header("Voice")
st.sidebar.markdown(
    "We are using an AI based TTS system ;)"
)



st.sidebar.header("Repository")
st.sidebar.markdown(
    "pertts-streamlit @ [github](https://github.com/SadeghKrmi/pertts-streamlit.git)"
)


st.sidebar.header("Contact")
st.sidebar.markdown(
    "sadegh.krmi@gmail.com"
    "support@datacula.com"
)


st.title(":speech_balloon: Persian AI text-to-speech")
"""
We're very excited to release `DataCula perTTS`, which coverts text to speech in persian/farsi using piper.
"""

tab1, tab2, tab3 = st.tabs([
    ":loudspeaker: Convert text",
    ":keyboard: Check a word",
    ":information_source: Information",
])

# Injecting the CSS
local_css("style.css")


with tab1:
    # txt = st.text_area("Let us convert your text, we try not to disappoint you ;)","لطفا متن خود را وارد نمایید")
    txt = st.text_area("Let us convert your text, we try not to disappoint you ;)","علت اصلیِ بارشِ باران جابجایی هوای مرطوب به‌ علت اختلاف دما و رطوبت است که به جبهه‌های هواشناسی معروف است.")
    
    
    
    col1, col2 = st.columns(2)
    
    with col2:
        modelname = st.selectbox(
            'Please select the model to generate audio.',
            (
                'ganji',
                'amir',
            ),
            label_visibility = "collapsed",    
        )
        models = {
            'ganji': 'ganji/epoch=5719-step=2609600-ganji.onnx',
            'amir': 'amir/epoch=5261-step=2455712.onnx'
        }
        model = models.get(modelname)
    
    with col1:
        if st.button('generate'):
            epoch = time()
            wav_filename = str(epoch).replace('.', '') + ".wav"
            wav_filepath = "./audio-out/" + wav_filename
            gCommand = ['bash', '-c', 'echo "{txt}" | /root/piper/build/piper --data-dir /usr/share/espeak-ng-data --model ./model/{model} --output_file {wav_filepath} --sentence_silence 0.3'.format(txt=txt, model=model,wav_filepath=wav_filepath)]

            with st.spinner('Wait for it...'):
                try:
                    process = subprocess.run(gCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
                    audio_file = open(wav_filepath, 'rb')
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format='audio/wav')
                    
                    rCommand = ['bash', '-c', 'rm -rf {wav_filepath}'.format(wav_filepath=wav_filepath) ]
                    process = subprocess.run(rCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
                    
                except subprocess.CalledProcessError as e:
                    print(f"Error executing the command for audio geneation: {e}")
                    rCommand = ['bash', '-c', 'rm -rf {wav_filepath}'.format(wav_filepath=wav_filepath) ]
                    process = subprocess.run(rCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
                    st.write("Error generating the audio, please contact us at support@datacula.com")

    


with tab2:
    word = st.text_input('Check word(s) spelling in phoneme format', 'نمایش واج آرایی کلمه ها')
    if st.button('check'):
        command = [
                "/usr/bin/espeak-ng",
                "-v", "fa",
                "-q", "--ipa",
                word
            ]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            stdout = stdout.decode('utf-8')
            st.write(word, '\u2194', stdout)

with tab3:
    """
    Please use the diacritics to generate moe sensible pronounciations. \n
        shift+d --> کسره  \n
        shift+s --> ضمه   \n
        shift+a --> فتح   \n
        shift+f --> تشدید \n
    """
