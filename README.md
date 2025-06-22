# AI Chatbot with Vector Search & RAG (Exploration Project)

This project is an exploration of building an AI-powered chatbot using hybrid Retrieval-Augmented Generation (RAG) techniques with vector search capabilities.

## Project Overview

- **Goal**: Explore the integration of vector search and retrieval-augmented generation (RAG) for building intelligent product search chatbots.
- **Stack**: React (frontend), Python + FastAPI (backend), OpenAI API (embedding & language model)
- **Dataset**: [Fashion Clothing Products Catalog](https://www.kaggle.com/datasets/shivamb/fashion-clothing-products-catalog)

## Key Features

- Rule-based and LLM-based attribute extraction
- Full semantic vector search using product embeddings
- Hybrid scoring with soft filtering to combine semantic relevance with extracted attributes
- Modular architecture suitable for future extension into full RAG pipelines

## Data Analysis Process

The project includes detailed exploratory data analysis (EDA) and data preparation stages:

1. **Data Cleaning**

   - Handle missing fields, duplicates, and normalize key attributes.
   - Ensure consistent product metadata for downstream embedding.

2. **Exploratory Data Analysis (EDA)**

   - Distribution analysis for categories, colors, brands, and pricing.
   - Identify data patterns to guide embedding and search design.

3. **Embedding Preparation**

   - Generate OpenAI embeddings for product names and descriptions.
   - Store embeddings along with metadata for hybrid retrieval.

4. **Vector Search Pipeline**
   - Compute query embeddings.
   - Perform cosine similarity search across full embedding space.
   - Apply optional soft filtering bonus based on extracted filters.

---

This project is part of hands-on exploration of AI chatbot architecture with modern LLM-powered search techniques.
