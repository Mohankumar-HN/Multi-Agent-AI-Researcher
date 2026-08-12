# 🔬 Multi-Agent AI Researcher

A multi-agent AI research system built with **LangChain, Gemini, Tavily, and Streamlit**.

The system takes a research topic, searches the web for relevant information, reads useful sources, generates a structured research report, and then evaluates the report using a critic chain.

---

## 🚀 Features

- 🤖 **Multi-Agent Architecture**
  - Search Agent
  - Reader Agent

- 🔎 **Web Research**
  - Uses Tavily for web search
  - Finds recent and relevant information

- 🌐 **Web Content Extraction**
  - Extracts content from URLs
  - Uses multiple scraping strategies for better reliability

- 📝 **AI Report Generation**
  - Generates structured research reports using Gemini

- 🧐 **AI-Powered Critic**
  - Reviews the generated report
  - Provides a score, strengths, and areas for improvement

- 🔗 **LangChain Expression Language (LCEL)**
  - Writer and Critic are implemented using LCEL chains

- 🎨 **Streamlit UI**
  - Simple interactive interface for running research

---

## 🏗️ Architecture

```text
                        👤 User
                           │
                           ▼
                  ┌─────────────────┐
                  │    Streamlit    │
                  │     app.py      │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │    Pipeline     │
                  │   pipeline.py   │
                  └────────┬────────┘
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
      ┌────────────┐ ┌────────────┐ ┌────────────┐
      │   Search   │ │   Reader   │ │   Writer   │
      │   Agent    │ │   Agent    │ │    Chain   │
      └─────┬──────┘ └─────┬──────┘ └─────┬──────┘
            │              │              │
            ▼              ▼              ▼
         Tavily        Web Scraper      Gemini
            │              │              │
            └──────────────┼──────────────┘
                           │
                           ▼
                    Research Report
                           │
                           ▼
                  ┌─────────────────┐
                  │  Critic Chain   │
                  │      LCEL       │
                  └────────┬────────┘
                           │
                           ▼
                    Critic Feedback
