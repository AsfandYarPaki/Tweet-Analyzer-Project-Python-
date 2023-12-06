def is_mentioned(tweet, username):
    """  Return True if and only if the tweet mentions that username
    preceded by @. Note: if a tweet contains @dancing, then we would
    consider username dan to be mentioned.

    >>>is_mentioned('I am Asfand Yar and I am doing @programming right now', 'program')
    True
    >>>is_mentioned('I am Asfand Yar and I am doing programming right now', 'Asfand')
    False
    """

    
    tweet = tweet.split()
    for separately in tweet:
        if separately[0] == '@':
            if separately[1: (len(username)+1)] == username:
                return True
    else:
        return False

print(is_mentioned("This tweet has @dancing in it", "dan"))
