from flask import Flask
from Utils import SCORES_FILE_NAME

app = Flask(__name__)
SCORE = open(SCORES_FILE_NAME, "r").read()

@app.route("/")
def score_server():
   return f"""<html>
                <head>
                <style>
                     body {{
                          font-size: 40px;
                          background-color: lightblue;
                          padding: 300px 650px 500px;        
                        }}
               </style>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>The score is <div id="score">{SCORE}</div></h1>
                </body>
               </html>"""
app.run(port=5000)