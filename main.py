from flask import Flask, request, render_template
from flask import Flask
from t_models import bot
from database import Base, session, engine


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#create new tables
Base.metadata.create_all(bind=engine)


@app.route('/', methods=['GET', 'POST'])
def bot():
    if request.method == 'GET':
        arizona = bot(az)
        arizona.run_botaz()
        florida = bot(fl)
        florida.run_botfl()
        return {
            "status": "retweets okay",
        }
    else:
        return {
            "tweet_status": "retweets failed"
        }

                   
        
if __name__ == "__main__":
    app.run()