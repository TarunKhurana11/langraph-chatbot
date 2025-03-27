# LangGraph Chatbot

A simple AI chatbot built with LangGraph, Groq's Gemma-2-9b-it model, and Streamlit.

## Features

- Clean and intuitive Streamlit interface
- Powered by Groq's Gemma-2-9b-it model
- Built using LangGraph for workflow management
- Simple graph structure for message handling

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/langraph-chatbot.git
cd langraph-chatbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your API keys:
```
GROQ_API_KEY=your_groq_api_key
LANGSMITH_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=StreamlitChatbot
```

4. Run the application:
```bash
streamlit run chatbot_app.py
```

## Project Structure

```
langraph-chatbot/
├── chatbot_app.py    # Main application file
├── requirements.txt  # Project dependencies
├── .env             # Environment variables (not included in repo)
└── README.md        # Project documentation
```

## Technologies Used

- Python
- Streamlit
- LangGraph
- Groq API
- LangSmith

## License

MIT License 