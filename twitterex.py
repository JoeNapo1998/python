import tweepy

access_token ='821280964626227200-ler6QHV422W27WnhY9flTAKp9ujMGzT'
access_token_secret ='G6pWDt7fUn47faODDZRT1rf9yykFPcs172xqAYOoCNFcz'
consumer_key ='ZOFBXvFBKSl2p4BcoVtqyVwve'
consumer_secret ='NXFBKgfB2Qhyxdwgxoxo72QEvizW8rG0OhfLtfby4yBKNKnqi5'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


Onoma_Proto = raw_input("Insert first Account")
follower_protou = api.followers_ids(Onoma_Proto)

Onoma_Deutero = raw_input("Insert second Account")
follower_deuterou = api.followers_ids(Onoma_Deutero);

Koinoi_Followers = set(follower_protou).intersection(follower_deuterou)

for x in Koinoi_Followers:
    print api.get_user(x).name.encode('utf8')
