from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1 style="
        text-align:center;
        font-size:120px;
        margin-top:200px;
    ">3سام</h1>
    """

if __name__ == "__main__":
    app.run()
    
