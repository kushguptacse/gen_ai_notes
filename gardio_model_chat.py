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

def stream_gpt(message_input):
    stream_resp = openai.chat.completions.create(
        model=config.LLM_MODEL_NAME,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": message_input},
        ],
        stream=True,
    )
    result = ""
    for chunk in stream_resp:
        result += chunk.choices[0].delta.content or ""
        yield result

message_input = gr.Textbox(label="Your message:", info="Enter a message for chatting", lines=7)
message_output = gr.Markdown(label="Response:")

view = gr.Interface(
    fn=stream_gpt,
    title="My Assistant", 
    inputs=[message_input], 
    outputs=[message_output], 
    examples=["Explain the Transformer architecture to a layperson",
        "Explain the Transformer architecture to an aspiring AI engineer"],
    flagging_mode="never"
    )
view.launch()