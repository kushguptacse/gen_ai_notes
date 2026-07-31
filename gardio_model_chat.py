import openai
import gradio as gr
import config

openai.api_key = config.CHAT_COMPLETIONS_API_KEY
openai.base_url = config.API_URL

system_message ="You are an helpful ai assistant."

message_input = gr.Textbox(label="Your message:", info="Enter a message for GPT-4.1-mini", lines=7)
message_output = gr.Textbox(label="Response:", lines=8)

def message_gpt(message_input):
    response = openai.chat.completions.create(
        model=config.LLM_MODEL_NAME,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": message_input},
        ]
    )
    return response.choices[0].message.content

view = gr.Interface(
    fn=message_gpt,
    title="My Assistant", 
    inputs=[message_input], 
    outputs=[message_output], 
    examples=["hello", "howdy"], 
    flagging_mode="never"
    )
view.launch()