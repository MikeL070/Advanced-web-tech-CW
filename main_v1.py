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

@app.route('/forrestSearch/')
def forrestSearch():
    return render_template('forrestSearch.html')

@app.route('/bandit1NoKnow/')
def bandit1NoKnow():
    return render_template('bandit1NoKnow.html')

@app.route('/runAway/')
def runAway():
    return render_template('runAway.html')

@app.route('/bandit1/')
def bandit1():
    return render_template('bandit1.html')

@app.route('/bandit1Conclusion/')
def bandit1Conclusion():
    return render_template('bandit1Conclusion.html')

@app.route('/bandit2/')
def bandit2():
    return render_template('bandit2.html')

@app.route('/bandit2Def/')
def bandit2Def():
    return render_template('bandit2Def.html')

@app.route('/finalBoss1/')
def finalBoss1():
    return render_template('finalBoss1.html')

@app.route('/finalBossDef/')
def finalBossDef():
    return render_template('finalBossDef.html')
  
@app.route('/finishIt/')
def finishIt():
    return render_template('finishIt.html')

@app.route('/winPage/')
def winPage():
    return render_template('winPage.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
