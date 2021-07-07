from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/healthcheck")
def health_check():
    return "OK"

# @app.route("/api")
# def api_portal():
#     return redirect("https://d2ml88kygckruo.cloudfront.net/")

if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0',
        port=80
    )
