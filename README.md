## 개발 언어 및 활용 기술

### Tech
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=black"> <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=black">

### Tool

<img src="https://img.shields.io/badge/vscode-007ACC?style=for-the-badge&logo=vscode&logoColor=black">


## 개발환경

### Version

- Python: 3.12

### 환경 설정

    git clone https://github.com/Kdoby/Summarization_AI

    -- fastAPI (패키지 파일은 가상환경에 설치) --
    .venv\Scripts\activate # 가상환경 활성화 (Windows PowerShell)
    source .venv/bin/activate # 가상환경 활성화 (MacOS bash)
    pip install transformers
    pip install torch torchvision torchaudio
    pip install nltk
    -- run (#port:8000) --
    .venv\Scripts\activate
    uvicorn [파일명]:app --host 0.0.0.0 --port 8000 --reload

## Acknowledgements

This Project refrences or uses code from the following open-source projects:

- <https://huggingface.co/philschmid/bart-large-cnn-samsum> - Licensed under the MIT License   
