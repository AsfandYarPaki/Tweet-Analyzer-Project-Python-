def is_reply(tweet):
    """  Return True if and only if this tweet is a reply.

    >>>is_reply('@Asfand How many hours do you work ?')
    True
    >>>is_reply('How many hours do you work?')
    False
    """
    
    tweet = tweet.split()
    for separate in tweet:
        if separate[0] == '@':
            return True
    else:
        return False

