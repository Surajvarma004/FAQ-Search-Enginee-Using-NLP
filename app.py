import json
from flask import Flask, request, jsonify
import pandas as pd
from utils import *
from flask_cors import CORS


logger = log_setup("main", LOGFILE)

app = Flask(__name__)
CORS(app)

logger.debug("[INFO] - Model loaded successfully..")

# load embedding dataframe
df = pd.read_csv(DATA)
df["embd"] = df["embd"].apply(lambda x: eval(x))


@app.route("/")
def ping():
    return "hello world"


@app.route("/find_question", methods=["POST"])
def paraphrase():
    if request.method == "POST":
        try:

            data = json.loads(request.data)
            logger.debug("[Request] - {}".format(data))
            ques = data["ques"]
            confidence = data["conf"]

            logger.debug("[INFO] Searching Questions...")
            final_output = question_search(ques, df, confidence)

            logger.debug("[Response] - {}".format(final_output))
            response = {"similar_questions": final_output}
            return response
        except Exception as e:
            response = {"Error": str(e)}
            logger.exception("[ERROR] - {}".format(str(e)))
            return response


if __name__ == "__main__":
    app.run(host=SERVER, port=PORT, debug=False)
