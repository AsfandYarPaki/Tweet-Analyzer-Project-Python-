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
    >>>format_reply_to('Asfand', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    '163 characters too long'
    """
    ready_reply_tweet = ''
    if username[0] != '@':
        username = '@' + username
    ready_reply_tweet = username + ' ' + replytweet
    if len(ready_reply_tweet) <= 140:
        return ready_reply_tweet
    else:
        return str((len(ready_reply_tweet)-140))+ ' ' + 'characters too long'
