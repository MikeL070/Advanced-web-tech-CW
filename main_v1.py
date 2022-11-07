from flask import Flask, render_template
app = Flask(__name__, static_url_path = "", static_folder = "static")

@app.route('/')
def title_page():
    return render_template('title_page.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
