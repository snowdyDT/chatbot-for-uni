#from rasa.nlu import components, utils
#from rasa.nlu.classifiers.classifier import IntentClassifier
#from rasa.nlu.components import Component, ComponentBuilder
#from rasa.nlu.config import RasaNLUModelConfig, component_config_from_pipeline
#from rasa.nlu.extractors.extractor import EntityExtractor

import config
from rasa.nlu.model import Interpreter

# path of your model
rasa_model_path = config.RASA_MODEL_ABSOLUTE_PATH

# create an interpreter object
interpreter = Interpreter.load(rasa_model_path)

"""
Function to get model output
Args:
  text  (string)  --  input text string to be passed)
For example: if you are interested in entities, you can just write result['entities']
Returns:
  json  --  json output to used for accessing model output
"""


def rasa_output(text):
    message = str(text).strip()
    result = interpreter.parse(message)
    return result


test = "Привет"
res = rasa_output(test)
print(res)
