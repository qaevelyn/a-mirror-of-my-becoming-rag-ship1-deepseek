#!/usr/bin/env python3
# ============================================================
# Copyright (c) 2026 Evelyn Caro. All rights reserved.
# A Mirror of My Becoming
# https://evelynacaro.github.io
# For licensing inquiries: evelyn.caro.cloud@gmail.com
# ============================================================

# coding: utf-8

# Ship 1: AWS + DeepSeek Agentic RAG Pipeline
# 
# Built for: A Mirror of My Becoming - Sovereign personal archive Author: Evelyn Caro (@qaevelyn) Date: 2026-08-12 LLM: DeepSeek 1.5B (via Ollama) Type: Agentic RAG with tool-calling

# About This Notebook
# 
# This notebook builds an agentic RAG pipeline for A Mirror of My Becoming - a sovereign personal archive.
# 
# What this notebook does:
# 
# Loads Mirror documents (Markdown, text files)
# Splits them into chunks
# Creates embeddings using Nomic-embed-text (via Ollama)
# Stores them in a vector database (ChromaDB)
# Uses an agent to decide when to retrieve context
# Answers questions with tool-calling
# LLM: DeepSeek 1.5B (via Ollama) Author: Evelyn Caro (@qaevelyn) Mission: Sovereign data ownership for Foundational Black Americans and Freedmen

# 1. Set Up Environment

# 1a. Install Dependencies

# In[1]:


# get_ipython().system('pip install langchain langchain-community langchain-text-splitters langchain-ollama chromadb langchain-chroma')
print("✅ Dependencies installed")


# 2. Imports

# In[11]:


from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_classic.tools import tool
from langchain_classic.tools.render import render_text_description_and_args
from langchain_classic.agents.output_parsers import JSONAgentOutputParser
from langchain_classic.agents.format_scratchpad import format_log_to_messages
from langchain_classic.agents import AgentExecutor
from langchain_classic.memory import ConversationBufferMemory
from langchain_core.runnables import RunnablePassthrough

print("✅ Imports ready")


# 3. Set Up Model

# In[12]:


llm = ChatOllama(
    model="deepseek-r1:1.5b",
    temperature=0.7,
)

embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
)

print("✅ Model and embeddings ready")


# 4. Load Data — Mirror Log or Fallback

# In[13]:


import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

file_path = "/Users/evelyn/Documents/Mirror-Project/MIRROR_LOG.md"

if os.path.exists(file_path):
    print(f"✅ Loading: {file_path}")
    loader = TextLoader(file_path)
    documents = loader.load()
else:
    print(f"❌ File not found: {file_path}")
    import wget
    url = "https://raw.githubusercontent.com/IBM/watson-machine-learning-samples/master/cloud/data/foundation_models/state_of_the_union.txt"
    filename = "state_of_the_union.txt"
    if not os.path.exists(filename):
        wget.download(url, out=filename)
    loader = TextLoader(filename)
    documents = loader.load()

text_splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separator="\n",
)

texts = text_splitter.split_documents(documents)

print(f"✅ Created {len(texts)} chunks")


# 5. Create Vector Store

# In[14]:


from langchain_chroma import Chroma

vector_store = Chroma.from_documents(
    documents=texts,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

retriever = vector_store.as_retriever(search_kwargs={"k": 4})

print("✅ Vector store created")


# 6. Define the RAG Tool

# In[15]:


@tool
def get_deepseek_context(question: str) -> str:
    """Retrieve relevant context from the Mirror archive."""
    docs = retriever.invoke(question)
    context = "\n\n".join([doc.page_content for doc in docs])
    return context

tools = [get_deepseek_context]


# 7. Set Up the Agent Prompt

# In[16]:


from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate

template = """You are a helpful assistant with access to a document retrieval tool.

You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought: {agent_scratchpad}"""

prompt = PromptTemplate.from_template(template)
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=3,
    handle_parsing_errors=True,
)


# 8. Set Up Agent Memory and Chain

# In[9]:


from langchain_classic.tools.render import render_text_description_and_args
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

system_prompt = """You are a helpful AI assistant. You have access to a tool that can retrieve relevant context from a personal archive.

Use the tool to answer questions when you don't have the information.

Provide only ONE action per JSON blob.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
]).partial(
    tools=render_text_description_and_args(tools),
    tool_names=", ".join([t.name for t in tools]),
)


# 9. Run the Agentic RAG Query

# In[17]:


response = agent_executor.invoke({
    "input": "What is MIRROR_LOG.md?"
})
print(response["output"])

