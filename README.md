## 개발 언어 및 활용 기술

### Tech
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=black"> <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=black">

### Tool

<img src="https://img.shields.io/badge/vscode-007ACC?style=for-the-badge&logo=vscode&logoColor=black">


## 개발환경

### Version

- Python: 3.12

### 환경 설정

- vscode에서 https://github.com/Kdoby/Summarization_AI 레포지토리 복제
- vscode extensions에 python 설치

       -- 가상 환경 생성 --
       # Windows
       python -m venv .venv
       # Mac
       python3 -m venv .venv
       ctrl + shift + p > Python: Select Interpreter 에서 .venv의 python.exe 선택
  
       -- 가상 환경 활성화 --
        # Windows PowerShell
        .venv\Scripts\activate
        # MacOS bash
        source .venv/bin/activate

        -- 패키지 파일 설치 --
        pip install transformers
        pip install torch torchvision torchaudio
        pip install fastapi[all]
        pip install uvicorn
  
        -- run (#port:8000) --
        .venv\Scripts\activate (활성화 안 된 경우에만)
        uvicorn bart_large_cnn_samsum:app --host 0.0.0.0 --port 8000 --reload

        

## Acknowledgements

This Project refrences or uses code from the following open-source projects:

- <https://huggingface.co/philschmid/bart-large-cnn-samsum> - Licensed under the MIT License   
