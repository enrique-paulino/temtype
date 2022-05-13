from flask import render_template, url_for, request, redirect, flash, Flask
from temtype import app
from temtype.scrape_data import ScrapeMatchup, ScrapePicture, FindTem, ScrapeType

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/search', methods =["GET", "POST"])
def matchup():
    temtem = request.args.get('temtem').lower()

    try:
        types = [x.lower() for x in ScrapeType(temtem)]
        images = ScrapePicture(temtem)
        matchups = ScrapeMatchup(temtem)
    except Exception:
        error="temtem not found"
        return render_template('home.html', error=error)
    return render_template('temtem.html', reg=images[0], luma=images[1], temtem=temtem.capitalize(), types=types, matchups=matchups)
