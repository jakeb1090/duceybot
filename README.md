## Twitter Sentiment Aggregator

### Using Tweepy collect unbiased tweets about Arizona's governor. 

### Criteria used to filter tweets within Tweepy API:
<br>*300mi radius set around Phoenix Geocode
<br>*Tweets contains links and images
<br>*Tweets containing a username == target
<br>*Api results returned as json and stored in SQL Database

<p>

Note: bot does not stream tweets. 
Aggregator is used in conjunction with the Invictify webapp to trigger webhooks and set intervals (4 hours). 
<br>Webhook can also be triggered manually, for this usecase, webhook is located at i29sunset@herokuapps.com 


