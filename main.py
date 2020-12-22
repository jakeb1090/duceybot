from flask import Flask, request, render_template
from flask import Flask
import t_models
from database import Base, session, engine

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#create new tables
Base.metadata.create_all(bind=engine)



@app.route('/', methods=['GET', 'POST'])
def bot():
    if request.method == 'GET':
        t_models.get_tweets()
#         return {
#             "status": "retweets okay",

#             }
        print('doing manual check')        
        print({'status': 'checking walmart'})
        time.sleep(3)
        print({'status': 'checking best buy'})
        time.sleep(3)
        print({'status': 'checking target'})
        time.sleep(3)
        print({'inventory status': 'sold out'})
        time.sleep(1)
        print({'message type': 'text'})
        time.sleep(1)
        print({'text mae': false})
    
    
    else:
        title = request.form['title']
        poster_url = m.build_imgurl(title)
        r = requests.get(poster_url)
        if r.status_code != 200:
            message = "No match"
            return {"status": "no retweets"}

        # return render_template("photo.html", image=poster_url)

        
        
                
        
if __name__ == "__main__":
    app.run()
