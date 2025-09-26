from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# 대화 요약 모델 로드
summarizer = pipeline("summarization", model="philschmid/bart-large-cnn-samsum")

class Message(BaseModel):
    text: str

@app.post("/summarize")
async def summarize_message(message: Message):
    # prompt = f'I want you to act as an essay writer. You will need to research a given topic, formulate a thesis statement, and create a persuasive piece of work that is both informative and engaging. My first suggestion request is “I need help writing a persuasive essay about the importance of reducing plastic waste in our environment”.\n\n{message.text}'
    prompt = (
        "Summarize the following conversation as if writing a diary entry. "
        "Use ONLY past tense verbs (finished, prepared, finalized, decided, tested). "
        "Do not use 'will'.\n\n"
        f"{message.text}"
    )
    summary = summarizer(prompt, max_length=60, min_length=10, do_sample=False)
    return {"summary": summary[0]['summary_text']}  