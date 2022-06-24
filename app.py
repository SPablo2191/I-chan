from I__Chan import i_chan_Bot

from flask import Flask, render_template, request
app = Flask(__name__)
app.static_folder = 'static'
i_bot=i_chan_Bot()
@app.route("/")

def home():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(i_bot.RespuestasPeronistas(userText))
if __name__ == "__main__":
    app.run() 