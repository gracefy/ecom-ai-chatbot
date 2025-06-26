# AI Chatbot with Vector Search & RAG (Exploration Project)

**🟢 [Live Demo](https://chatbot.graceye.ca)**

This project is an exploration to build an AI-powered chatbot that answers product-related questions using Retrieval-Augmented Generation (RAG) and vector search.

## Project Overview

- **Goal**: Explore the integration of vector search and RAG for intelligent e-commerce product chatbots.
- **Stack**: React (frontend), Python + FastAPI (backend), OpenAI API (embedding & language model)

- Frontend: React
- Backend: FastAPI (Python)
- LLM: OpenAI API (embedding + chat completion)
- Vector Search:
  - Local embedding search using cosine similarity
  - Azure AI Search with vector + hybrid scoring
- **Dataset**: [Fashion Clothing Products Catalog (Kaggle)](https://www.kaggle.com/datasets/shivamb/fashion-clothing-products-catalog)

## Key Features

- Rule-based and LLM-powered product attribute extraction
- Two vector search modes:
  - Local vector store with cosine similarity
  - Azure AI Search with hybrid scoring + soft filtering
- Modular backend suitable for future upgrade to full RAG pipeline
- Clean and accessible frontend with simple chatbot interface
- Full data analysis pipeline: cleaning, EDA, and embedding preparation for downstream vector search

## Setup Locally

To run the chatbot locally, follow these steps:

### Prerequisites

- Python 3.10+
- Node.js 18+
- OpenAI API key
- Azure AI Search

### 1. Clone the Repo

```bash
git clone https://github.com/gracefy/ecom-ai-chatbot
cd ecom-ai-chatbot
```

### 2. Backend Setup

**Python Environment**:

```bash
pyenv install 3.11.13
pyenv local 3.11.13
```

**macOS/Linux**:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Windows (PowerShell)**:

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Environment Configuration**

Before creating .env files, you must configure:

- OpenAI API key
- Azure AI Search credentials (if using Azure)

Create a `.env` file in the root directory with the following variables:

```env
OPENAI_API_KEY=your_openai_api_key
AZURE_SEARCH_ENDPOINT=your_azure_search_endpoint
AZURE_SEARCH_API_KEY=your_azure_search_api_key
AZURE_SEARCH_INDEX=your_azure_search_index_name
```

### 3. Frontend Setup

**Install Dependencies**:

```bash
cd frontend
npm install
```

**Environment Configuration**
Create a `.env` file in the `frontend` directory with the following variables:

```env
VITE_API_BASE_URL=http://localhost:8000
VITE_FRONTEND_URL=http://localhost:5173
```

### 4. Run the Application

**Backend**:

```bash
uvicorn backend.app.main:app --reload
```

**Frontend**:

```bash
cd frontend
npm run dev
```

Now you can access the chatbot at `http://localhost:5173`.

### 5. Testing

You can test the chatbot by asking product-related questions in the chat interface. The backend will handle the requests and return relevant product information using vector search.
