from flask import Flask,render_template,request
import os
from detect import detect_currency
from blockchain import Blockchain

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
blockchain = Blockchain()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload",methods=["POST"])
def upload():

    file = request.files["image"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"],file.filename)

    file.save(filepath)

    result = detect_currency(filepath)

    blockchain.add_block(result)

    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)