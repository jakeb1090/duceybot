from flask import Flask, request, render_template
import model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bot():
    if request.method == 'GET':
        model.get_tweets()
        return {"status": "retweets okay"}
    else:
        title = request.form['title']
        poster_url = m.build_imgurl(title)
        r = requests.get(poster_url)
        if r.status_code != 200:
            message = "No match"
            return {"status: "no retweet"}
        # return render_template("photo.html", image=poster_url)

        
        
                
        
if __name__ == "__main__":
    app.run()