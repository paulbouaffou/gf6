from flask import Flask, render_template, redirect, url_for, jsonify
import requests

app = Flask(__name__)

# Define the URL for each button's link
URL_NO_IMAGE = "https://petscan.wmflabs.org/?show%5Fdisambiguation%5Fpages=both&minlinks=&show%5Fsoft%5Fredirects=both&wikidata%5Fprop%5Fitem%5Fuse=&links%5Fto%5Fno=&sitelinks%5Fany=&sitelinks%5Fyes=&wikidata%5Fitem=no&format=json&search%5Ffilter=&langs%5Flabels%5Fyes=&links%5Fto%5Fall=&maxlinks=&templates%5Fyes=&before=&wikidata%5Fsource%5Fsites=&negcats=&manual%5Flist=&output%5Fcompatability=catscan&langs%5Flabels%5Fno=&sortby=none&edits%5Bflagged%5D=both&wikidata%5Flabel%5Flanguage=&pagepile=&depth=0&sortorder=ascending&cb%5Flabels%5Fno%5Fl=1&outlinks%5Fany=&combination=subset&doit=Do%20it%21&links%5Fto%5Fany=&active%5Ftab=tab%5Foutput&larger=&templates%5Fany=Infobox%0D%0AInfobox%20Monument%0D%0AInfobox%20Localit%C3%A9%0D%0AInfobox%20Footballeur%0D%0AInfobox%20Organisation%0D%0AInfobox%20Biographie2&manual%5Flist%5Fwiki=&labels%5Fany=&max%5Fsitelink%5Fcount=&sparql=&subpage%5Ffilter=either&source%5Fcombination=&categories=Portail%3AC%C3%B4te%20d%27Ivoire%2FArticles%20li%C3%A9s&langs%5Flabels%5Fany=&edits%5Banons%5D=both&labels%5Fno=&rxp%5Ffilter=&min%5Fredlink%5Fcount=1&outlinks%5Fyes=&edits%5Bbots%5D=both&outlinks%5Fno=&min%5Fsitelink%5Fcount=&output%5Flimit=&project=wikipedia&language=fr&templates%5Fno=&ns%5B0%5D=1&max%5Fage=&search%5Fmax%5Fresults=500&wpiu=any&referrer%5Furl=&common%5Fwiki%5Fother=&referrer%5Fname=&after=&interface%5Flanguage=en&cb%5Flabels%5Fyes%5Fl=1&cb%5Flabels%5Fany%5Fl=1&ores%5Fprediction=any&namespace%5Fconversion=keep&ores%5Fprob%5Fto=&ores%5Ftype=any&smaller=&ores%5Fprob%5Ffrom=&since%5Frev0=&page%5Fimage=no&show%5Fredirects=both&search%5Fwiki=&labels%5Fyes=&search%5Fquery=&sitelinks%5Fno=&common%5Fwiki=auto"

URL_REFERENCE_NEEDED = "https://petscan.wmflabs.org/?wikidata%5Fitem=no&larger=&smaller=&project=wikipedia&common%5Fwiki=auto&cb%5Flabels%5Fany%5Fl=1&search%5Fquery=&show%5Fredirects=both&search%5Fwiki=&langs%5Flabels%5Fany=&outlinks%5Fany=&negcats=&edits%5Bbots%5D=both&pagepile=&sitelinks%5Fany=&since%5Frev0=&after=&edits%5Banons%5D=both&ns%5B0%5D=1&before=&langs%5Flabels%5Fno=&maxlinks=&format=json&depth=0&manual%5Flist%5Fwiki=&output%5Flimit=&sitelinks%5Fno=&language=fr&links%5Fto%5Fall=&edits%5Bflagged%5D=both&referrer%5Fname=&namespace%5Fconversion=keep&active%5Ftab=tab%5Foutput&common%5Fwiki%5Fother=&show%5Fsoft%5Fredirects=both&links%5Fto%5Fany=&interface%5Flanguage=en&subpage%5Ffilter=either&wpiu=any&show%5Fdisambiguation%5Fpages=both&sortorder=ascending&links%5Fto%5Fno=&cb%5Flabels%5Fno%5Fl=1&search%5Ffilter=&cb%5Flabels%5Fyes%5Fl=1&labels%5Fany=&min%5Fsitelink%5Fcount=&max%5Fage=&search%5Fmax%5Fresults=500&wikidata%5Flabel%5Flanguage=&rxp%5Ffilter=&wikidata%5Fsource%5Fsites=&manual%5Flist=&ores%5Ftype=any&source%5Fcombination=&combination=subset&sitelinks%5Fyes=&sparql=&sortby=none&referrer%5Furl=&outlinks%5Fyes=&ores%5Fprob%5Fto=&templates%5Fno=&output%5Fcompatability=catscan&doit=Do%20it%21&minlinks=&page%5Fimage=any&ores%5Fprob%5Ffrom=&langs%5Flabels%5Fyes=&ores%5Fprediction=any&min%5Fredlink%5Fcount=1&outlinks%5Fno=&wikidata%5Fprop%5Fitem%5Fuse=&labels%5Fyes=&templates%5Fyes=&categories=Portail%3AC%C3%B4te%20d%27Ivoire%2FArticles%20li%C3%A9s&labels%5Fno=&templates%5Fany=r%C3%A9f%C3%A9rence%20n%C3%A9cessaire%0D%0Ar%C3%A9f%C3%A9rence%20souhait%C3%A9e&max%5Fsitelink%5Fcount="

def fetch_articles(url):
    try:
        response = requests.get(url)
        data = response.json()
        # Extraire les titres des articles
        titles = [page["title"] for page in data["*"][0]["a"]["*"]]
        return titles
    except Exception as e:
        print("Erreur de récupération:", e)
        return []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/articles/no-image")
def articles_no_image():
    articles = fetch_articles(URL_NO_IMAGE)
    return render_template("articles.html", articles=articles, title="articles sans image")

@app.route("/articles/reference-needed")
def articles_reference_needed():
    articles = fetch_articles(URL_REFERENCE_NEEDED)
    return render_template("articles.html", articles=articles, title="articles à sourcer")

if __name__ == "__main__":
    app.run(debug=True)


