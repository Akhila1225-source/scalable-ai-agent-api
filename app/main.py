from fastapi import FastAPI, Query
from app.agent import run_agent

app = FastAPI(
    title="Scalable AI Agent API",
    description="Scalable Agentic AI system for intelligent API tool selection and execution.",
    version="1.0"
)


@app.get("/")
def home():
    return {"message": "Scalable AI Agent API is running"}


@app.get("/ask")
def ask_agent(
    query: str = Query(
        description="Describe what you want to do. Example: I want refund payment"
    ),
    input_value: str = Query(
        description="Enter the required value. For refund/payment details: Payment ID. For create payment: Amount. For customer details: Customer ID."
    )
):
    result = run_agent(query, input_value)
    return {"response": result}