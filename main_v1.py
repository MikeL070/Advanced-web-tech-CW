from flask import Flask, render_template, session
app = Flask(__name__, static_url_path = "", static_folder = "static")
app.secret_key = 'thisisasecret'

@app.route('/')
def title_page():
    return render_template('title_page.html')

@app.route('/charChoice/')
def charChoice():
    return render_template('charClassChoice.html')

@app.route('/storyIntro/')
def storyIntro():
    return render_template('introStory.html')

@app.route('/storyIntroKnight/')
def storyIntroKnight():
    session['class'] = 'knight'
    session['armour'] = 'no'
    session['training'] = 'no'
    session['weapopn'] = 'no'
    session['hitpoints'] = '50'
    session['knowledge'] = 'no'
    session['silver'] = '100'
    return render_template('introStory.html') 

@app.route('/storyIntroScribe/')
def storyIntroScribe():
    session['class'] = 'scribe'
    session['armour'] = 'no'
    session['training'] = 'no'
    session['weapopn'] = 'no'
    session['hitpoints'] = '30'
    session['knowledge'] = 'no'
    session['silver'] = '100'
    return render_template('introStory.html')

@app.route('/storyIntroBrute/')
def storyIntroBrute():
    session['class'] = 'brute'
    session['armour'] = 'no'
    session['training'] = 'no'
    session['weapopn'] = 'no'
    session['hitpoints'] = '50'
    session['knowledge'] = 'no'
    session['silver'] = '100'
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
