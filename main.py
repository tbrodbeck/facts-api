from fastapi import FastAPI
from modelTrainer.abstractive_summarizer import AbstractiveSummarizer
from typing import Optional

app = FastAPI()

print("importing...")
summarizer = AbstractiveSummarizer("saved_model", "german", status="fine-tuned")
print("imported")

@app.get("/")
def read_root():
    return {"This is an awesome API presented by C. Lohse and B. Schaper"}

@app.get("/input:{input_text}")
def read_input(input_text: str):
    return {"input_text": input_text, "Output_text": summarizer.predict(input_text)}
