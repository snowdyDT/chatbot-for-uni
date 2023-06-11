import gradio as gr
import requests

rasa_api_endpoint = "http://localhost:5005/webhooks/rest/webhook"

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]


def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})

        payload = {
            "sender": "user",
            "message": input
        }

        response = requests.post(rasa_api_endpoint, json=payload)
        rasa_response = response.json()

        reply = rasa_response[0]['text'] if rasa_response else "I'm sorry, I didn't understand."
        messages.append({"role": "assistant", "content": reply})
        return reply


inputs = gr.inputs.Textbox(lines=7, label="Smart Student IITU")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="DEVELOPMENT OF AUTONOMOUS INTELLIGENT CONSULTANT "
                                                               "“SMART STUDENT”",
             description="Ask a question",
             theme="compact").launch(share=True)
