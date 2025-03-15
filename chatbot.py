# -*- coding: utf-8 -*-
"""Chatbot

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12yuzU3xiwp8GBJrPGSrDNbvePy6PVIPO
"""

!pip install transformers gradio

from transformers import pipeline
import gradio as gr

# Load the conversational model
chatbot = pipeline("text2text-generation", model="google/flan-t5-small")

# Chat function with a government assistant persona
def chat_with_bot(user_input, history=[]):
    prompt = f"You are a helpful government assistant chatbot. Answer the user's question clearly and concisely.\nUser: {user_input}\nBot:"
    response = chatbot(prompt, max_length=100, do_sample=True)
    bot_response = response[0]['generated_text'].strip()
    return bot_response, history + [(user_input, bot_response)]

# Gradio interface
interface = gr.Interface(
    fn=chat_with_bot,
    inputs=[
        gr.Textbox(lines=2, placeholder="Ask your government-related question..."),
        gr.State([])
    ],
    outputs=[
        gr.Textbox(label="Chatbot Response"),
        gr.State([])
    ],
    title="Government Services Chatbot",
    description="Chat with the AI for government-related queries."
)

interface.launch()