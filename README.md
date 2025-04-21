# End to end working prototype of Daily + Pipecat + HeyGen

## Setup
Python 3.11 is required. pyenv can be used to manage python versions.

```bash
# Recommend using a python virtual environment before doing this
pip install -r requirements.txt
```

## Run Server

```bash
export ELEVENLABS_API_KEY=YOUR_ELEVENLABS_API_KEY
export OPENAI_API_KEY=YOUR_OPENAI_API_KEY
export DEEPGRAM_API_KEY=YOUR_DEEPGRAM_API_KEY
python main.py
```

## Run Client

0. Update Heygen API key in ui/index.html
1. Open ui/index.html in a browser
2. Press 'Start' button
3. When you see the video playing, press 'RecordAudio' button
