def is_mentioned(tweet, username):
    tweet = tweet.split()
    for separately in tweet:
        if separately[0] == '@':
            if separately[1: (len(username)+1)] == username:
                return True
    else:
        return False
