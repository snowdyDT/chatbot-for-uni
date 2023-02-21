import config
import asyncio
from rasa.core.agent import Agent
from rasa.shared.utils.io import json_to_string


class Model:

    def __init__(self, model_path: str) -> None:
        self.agent = Agent.load(model_path)
        print("NLU model loaded")

    def message(self, message: str) -> str:
        message = message.strip()
        result = asyncio.run(self.agent.parse_message(message))

        return json_to_string(result)


mdl = Model(config.RASA_MODEL_PATH)

sentence = "как получить справку"
result = mdl.message(sentence)

print(result)
