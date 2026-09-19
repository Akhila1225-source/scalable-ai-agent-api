# Scalable AI Agent API

## Overview

This project is a prototype of a scalable Agentic AI system designed to work with a large number of API tools.

The system accepts a natural language request, searches the available API catalog, selects a relevant tool, executes the tool, maintains execution state, and returns the result.

PayPal APIs are used as the demonstration scenario. The architecture can be extended from a small set of APIs to 50+ APIs and eventually 500+ APIs from different services.

## Problem Statement

When an agent has access to a large number of tools, directly providing all tools to the agent can make tool selection slower and less accurate.

This project addresses this problem by using a searchable API catalog and routing the user request to relevant tools.

## Architecture

User Request
|
v
FastAPI Interface
|
v
Agent Router
|
+----------------------+
|                      |
v                      v
Tool Search          Special Tools
|               /            
|              /              
v             v                v
Relevant API    RAG Pipeline    System Search
|
v
Tool Selection
|
v
Parameter Handling
|
v
Tool Execution
|
v
State Management
|
v
Response

## Key Features

### 1. Scalable Tool Catalog

The available APIs are stored in a structured JSON catalog.

Each tool contains:

* Tool name
* Category
* HTTP method
* API endpoint
* Description
* Required parameters

This makes it easier to add more APIs without changing the core routing logic.

### 2. Tool Search and Routing

The system searches the API catalog based on the user's request.

The search considers:

* Tool name
* Category
* Description
* Endpoint

The most relevant tools are returned for execution.

### 3. RAG Pipeline Tool

A local knowledge base is used to retrieve information related to:

* PayPal
* Payments
* Invoices
* Disputes
* Agentic systems
* Scalability

This provides a separate knowledge retrieval path from API execution.

### 4. System Search Tool

The System Search Tool searches the available API catalog and returns matching tools along with their:

* Name
* Category
* HTTP method
* Endpoint

It can also list all available tools in the system.

### 5. State Management

The agent maintains state information such as:

* User request
* Selected tool
* Parameters
* Execution history

This allows the system to keep track of tool executions.

### 6. Error Handling

The system handles situations such as:

* No suitable tool found
* Missing required input
* Unsupported tool
* Tool execution errors

### 7. Automated Testing

The project includes automated tests for important agent operations.

The test suite checks:

* Refund payment
* Get payment details
* Create payment
* Missing parameter handling

## Demonstration API Tools

The current prototype contains the following PayPal API tools:

1. Get Payment
2. Create Payment
3. Refund Payment
4. Get Customer
5. Create Invoice
6. Send Invoice
7. Get Invoice
8. Get Dispute
9. List Disputes
10. Get Sales Report

## Project Structure

scalable-ai-agent-api/
│
├── app/
│   ├── main.py
│   ├── agent.py
│   ├── tools.py
│   ├── search.py
│   ├── rag.py
│   ├── system_search.py
│   └── state.py
│
├── data/
│   └── api_catalog.json
│
├── tests/
│   └── test_agent.py
│
├── .gitignore
├── requirements.txt
└── README.md


## Technologies Used

* Python
* FastAPI
* Uvicorn
* JSON
* Pytest
* Agentic AI concepts
* Tool Routing
* RAG
* State Management
* Automated Testing

## Running the Project

Install the required packages:

pip install -r requirements.txt

Run the agent:

python -m app.agent


Run the FastAPI application:


python -m uvicorn app.main:app --reload


Open the API documentation:


http://127.0.0.1:8000/docs


## API Example

Example request:


/ask?query=I%20want%20to%20refund%20a%20payment&input_value=P123


Example response:


{
    "response": {
        "payment_id": "P123",
        "status": "REFUNDED"
    }
}


## Testing

Run the automated tests using:

python -m pytest


The test suite verifies the main agent functions and error handling.

Example result:

4 passed


## Scalability

The current prototype demonstrates the architecture using a small number of APIs.

The same architecture can be extended to support:

10 APIs
    ↓
50+ APIs
    ↓
100+ APIs
    ↓
500+ APIs

Instead of passing every available API to the agent, the system first searches the tool catalog and retrieves relevant tools.

This reduces the number of tools that need to be considered during tool selection.

For further scaling, the search layer can be extended with:

* Embedding-based semantic search
* Vector databases
* Top-K retrieval
* Domain-based routing
* Confidence thresholds
* Multiple API services
* Observability and monitoring

## Design Approach

The project separates the major responsibilities into different modules:

* agent.py handles routing and execution.
* search.py handles API tool retrieval.
* rag.py handles knowledge retrieval.
* system_search.py handles system/tool discovery.
* state.py handles agent state.
* tools.py contains mock API functions.
* main.py provides the FastAPI interface.

This modular design makes the system easier to maintain and extend.

## Future Improvements

The prototype can be extended with:

1. Real API integration
2. LLM-based natural language understanding
3. Semantic tool retrieval using embeddings
4. Vector database integration
5. Support for multiple external services
6. Advanced parameter extraction
7. Tool execution retries
8. Logging and observability
9. Authentication and authorization
10. Cloud deployment

## Note

This is a local prototype using mock PayPal API functions for demonstration and testing purposes. No real PayPal transactions are performed.
