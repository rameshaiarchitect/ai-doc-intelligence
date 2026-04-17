# AI Document Intelligence System -- RAG Pipeline

AI-powered system that enables semantic search and question answering
over documents using a Retrieval-Augmented Generation (RAG)
architecture.

------------------------------------------------------------------------

## Overview

This system processes unstructured documents (PDFs) and allows users to
ask questions based on their content.

It combines:

-   Document ingestion and preprocessing
-   Semantic search using vector embeddings
-   LLM-based answer generation grounded in retrieved context

------------------------------------------------------------------------

## Architecture

PDF Documents → Ingestion → Cleaning → Chunking → Embeddings → FAISS\
User Query → Embedding → Vector Search → Top-K Chunks → LLM → Answer

------------------------------------------------------------------------

## Key Features

### Document Ingestion Pipeline

-   Loads PDFs from local directory
-   Converts each page into structured Document objects

### Intelligent Chunking Strategy

-   Recursive splitting with overlap and semantic awareness

### Semantic Search (Vector Retrieval)

-   FAISS-based similarity search

### RAG-based Answer Generation

-   LLM generates answers using retrieved context

### Modular Design

-   ingestion/, embeddings/, retrieval/, llm/, main.py

------------------------------------------------------------------------

## Tech Stack

-   Python 3.11+
-   uv
-   LangChain
-   OpenAI
-   FAISS
-   Pydantic

------------------------------------------------------------------------

## Setup & Run

### Install Dependencies

uv sync

### Set Environment Variables

OPENAI_API_KEY=your_api_key

### Run Application

uv run main.py

------------------------------------------------------------------------

## How It Works

1.  Load PDFs
2.  Clean text
3.  Chunk documents
4.  Generate embeddings
5.  Store in FAISS
6.  Query + retrieve
7.  LLM generates answer

------------------------------------------------------------------------

## Summary

End-to-end RAG pipeline with modular, production-oriented design.
