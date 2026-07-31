import openai
import gradio as gr
import config

openai.api_key = config.CHAT_COMPLETIONS_API_KEY
openai.base_url = config.API_URL

system_message ="You are a helpful assistant that responds in markdown without code blocks"


def message_gpt(message_input):
    response = openai.chat.completions.create(
        model=config.LLM_MODEL_NAME,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": message_input},
        ]
    )
    return response.choices[0].message.content

def stream_gpt(message_input, history):
    messages = [{"role": "system", "content": system_message}]
    if history:
        for msg in history:
            messages.append({"role": msg["role"], "content": msg["content"]})

    messages.append({"role": "user", "content": message_input})
    
    stream_resp = openai.chat.completions.create(
        model=config.LLM_MODEL_NAME,
        messages=messages,
        stream=True,
    )
    result = ""
    for chunk in stream_resp:
        result += chunk.choices[0].delta.content or ""
        yield result

view = gr.ChatInterface(fn=stream_gpt, title="My LLM Chatbot" ) 
view.launch()