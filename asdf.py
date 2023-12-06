tweet1 = '@asac sdasda sadsdsad . dsdsd #dsddf ddfffffffff  dfdff.'


def is_reply(tweet):
    tweet = tweet.split()
    for separate in tweet:
        if separate[0] == '@':
            return True
    else:
        return False

print(is_reply(tweet1))
    
