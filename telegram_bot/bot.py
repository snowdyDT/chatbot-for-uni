import flask
import util

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'POST':
        msg = flask.request.get_json()
        chat_id, txt = util.parse_message(msg)

        if txt.lower() == "hello":
            util.tel_send_message(chat_id, 'hello')
        else:
            util.tel_send_message(chat_id, 'testtesttest')

        return flask.Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"


if __name__ == '__main__':
    app.run(debug=True)
