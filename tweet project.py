
def is_valid_tweet(tweet):
    """Return True if and only if the potential
    tweet is no less than 1 and no more than 140 characters long

    >>>is_valid_tweet('I am Asfand Yar and I am doing programming right now')
    True
    >>>is_valid_tweet('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    False
    """

    return True if len(tweet) >= 1 and len(tweet) <= 140 else False




def contains_hash_symbol(tweet):
    """ Return True if and only if the tweet contains a hash symbol.

    >>>contains_hash_symbol('I am Asfand Yar and I am doing #programming right now')
    True
    >>>contains_hash_symbol('I am Asfand Yar and I am doing programming right now')
    False
    """
    
    for i in tweet:
        if i == '#':
            return True
    else:
        return False




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

def report_shortest(tweet1, tweet2):
    """ Return ’Tweet 1’ if the ﬁrst tweet is shorter than the
    second, ’Tweet 2’ if the second tweet is shorter than the
    ﬁrst, and ’Same length’ if the tweets have the same length.

    >>>report_shortest('I am Asfand Yar.', 'I am doing programming')
    'Tweet 1'
    >>>report_shortest('I am doing programming', 'I am Asfand Yar.')
    'Tweet 2'
    >>>report_shortest('I am Asfand Yar.', 'I am very tired.')
    'Same length'
    """
    
    if len(tweet1) < len(tweet2):
        return 'Tweet 1'
    elif len(tweet1) == len(tweet2):
        return 'Same length'
    else:
        return 'Tweet 2'
    
        
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

def format_reply_to(username, replytweet):
    """  Return username followed by replytweet if the reply tweet is
    at most 140 characters long. Otherwise, return a string that indicates
    how many extra characters there are in the invalid
    reply tweet. For example, ifthereplytweetwas143characters
    long, the string ’3 characters too long’ would be returned.
    The "too long" return string must be a single string that
    contains the number of extra characters followed by the string
    ’ characters too long’

    >>>format_reply_to('Asfand', 'How many hours do you work ?')
    '@Asfand How many hours do you work ?'
    >>>format_reply_to('Asfand', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    '23 characters too long'
    """
    ready_reply_tweet = ''
    if username[0] != '@':
        username = '@' + username
    ready_reply_tweet = username + ' ' + replytweet
    if len(ready_reply_tweet) <= 140:
        return ready_reply_tweet
    else:
        return str((len(ready_reply_tweet)-140))+ ' ' + 'characters too long'

        
