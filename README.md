# ResearchAI

## AI-Powered Research Paper Simplification System

ResearchAI is an AI-powered application that converts complex research papers into simple and understandable insights.

Users can upload a research paper in PDF format and receive an AI-generated summary, key insights, technical term explanations, research gaps, and answers to questions based only on the uploaded paper.

## Features

- PDF Research Paper Upload
- Automatic PDF Text Extraction
- Text Cleaning and Section Detection
- Intelligent Text Chunking
- Semantic Search
- Research Paper Summarization
- Key Insight Extraction
- Technical Term Simplification
- Research Gap Detection
- Question Answering
- Evidence-Based AI Responses
- Local AI using Ollama

## Technologies Used

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask
- Flask-CORS

### AI / NLP
- Sentence Transformers
- Semantic Search
- Cosine Similarity
- Ollama
- Llama 3.2 3B

### PDF Processing
- PyMuPDF

## How It Works

1. User uploads a research paper PDF.
2. The backend extracts the text from the PDF.
3. The text is cleaned and divided into sections and chunks.
4. Sentence Transformer generates embeddings.
5. Semantic search retrieves relevant paper content.
6. Local Llama 3.2 generates summaries and insights.
7. Users can ask questions about the paper.
8. Answers are generated using evidence from the uploaded paper.

## Project Structure

```text
ml project/
│
├── ai/
│   ├── pdf_extractor.py
│   ├── cleaner.py
│   ├── section_detector.py
│   ├── chunker.py
│   ├── pipeline.py
│   ├── encoder.py
│   ├── retriever.py
│   ├── search.py
│   ├── evidence.py
│   ├── llm.py
│   ├── summary_generator.py
│   ├── insights_generator.py
│   ├── terms_generator.py
│   └── gaps_generator.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── research-paper-ai/
│   ├── backend/
│   │   ├── app.py
│   │   └── routes/
│   └── uploads/
│
├── frontend/
│
├── requirements.txt
└── README.md