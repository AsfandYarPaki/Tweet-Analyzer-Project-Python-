tweet1 = '@asac sdasda sadsdsadhhhhhhhhhhhhhhhhhhhhh hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj. dsdsd #dsddf ddfffffffff  dfdff.'


def format_reply_to(username, replytweet):
    ready_reply_tweet = ''
    if username[0] != '@':
        username = '@' + username
    ready_reply_tweet = username + ' ' + replytweet
    if len(ready_reply_tweet) <= 140:
        return ready_reply_tweet
    else:
        return str((len(ready_reply_tweet)-140))+ ' ' + 'characters too long'

print(format_reply_to('asfand' ,tweet1))
