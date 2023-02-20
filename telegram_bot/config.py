import keyring

TOKEN = keyring.get_password("TELEGRAM_BOT_RASA", "TOKEN")

RASA_MODEL_PATH = "../RASA MODELS/models/20230128-170349-parallel-proof.tar.gz"
RASA_MODEL_ABSOLUTE_PATH = r"C:\Users\00052497\Desktop\chatbot_for_uni\RASA " \
                           r"MODELS\models\20230128-170349-parallel-proof.tar.gz "

if __name__ == "__main__":
    print(f"TOKEN: {TOKEN}")