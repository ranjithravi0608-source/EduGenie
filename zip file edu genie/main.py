from fastapi import FastAPI

app = FastAPI()

# 1. QA Endpoint
@app.get("/qa")
async def answer_question(question: str = ""):
    return {"question": question, "answer": "This is a sample AI answer."}

# 2. Explain Endpoint
@app.post("/explain")
async def explain_topic(data: dict):
    return {"topic": data.get("topic"), "explanation": "Sample explanation for the topic."}

# 3. Quiz Endpoint
@app.get("/quiz")
async def get_quiz():
    return {"quiz": "Sample quiz question?"}

# 4. Summarize Endpoint
@app.post("/summarize")
async def summarize_text(data: dict):
    return {"summary": "Summary of the provided text."}