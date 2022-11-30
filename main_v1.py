from flask import Flask, render_template
app = Flask(__name__, static_url_path = "", static_folder = "static")

@app.route('/')
def title_page():
    return render_template('title_page.html')

@app.route('/charChoice/')
def charChoice():
    return render_template('charClassChoice.html')

@app.route('/storyIntro/')
def storyIntro():
    return render_template('introStory.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
