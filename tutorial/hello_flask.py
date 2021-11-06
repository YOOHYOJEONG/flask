from flask import Flask

#local host가 필요한데 컨테이너환경인 가상머신에선 접속 할 수 없으므로 ngrok를 이용해 공용 url 할당 받음.
from flask_ngrok import run_with_ngrok


app = Flask(__name__)
run_with_ngrok(app)

@app.route("/")
def hello() :
    return "플라스크 동작 확인!"

if __name__ == "__main__" :
    app.run()
