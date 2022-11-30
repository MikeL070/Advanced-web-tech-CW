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

@app.route('/village/')
def village():
    return render_template('village.html')

@app.route('/knights/')
def knights():
    return render_template('knights.html')

@app.route('/tavern/')
def tavern():
    return render_template('tavern.html')

@app.route('/blacksmith/')
def blacksmith():
    return render_template('blacksmith.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
