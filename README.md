from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>3سام</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(45deg, #000, #222, #000);
                color: white;
                font-family: Tahoma;
            }

            h1 {
                font-size: 120px;
                animation: glow 2s infinite alternate;
            }

            @keyframes glow {
                from {
                    text-shadow: 0 0 10px #00ffcc, 0 0 20px #00ffcc;
                    transform: scale(1);
                }
                to {
                    text-shadow: 0 0 30px #ff00ff, 0 0 60px #ff00ff;
                    transform: scale(1.1);
                }
            }

            button {
                position: absolute;
                bottom: 50px;
                padding: 10px 20px;
                font-size: 20px;
                border: none;
                cursor: pointer;
                border-radius: 10px;
            }
        </style>
    </head>
    <body>
        <h1>3سام</h1>

        <button onclick="alert('سلام 3سام 😎')">
            کلیک کن
        </button>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
