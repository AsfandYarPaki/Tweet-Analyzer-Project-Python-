str = '@abcd abcdefghijkl. as #dcdvf. sdnnsd sdsffg kjhk.'

def is_mentioned(tweet, username):
    tweet = tweet.split()
    for separately in tweet:
        if separately[0] == '@':
            if separately[1:] == username:
                return True
    else:
        return False


print(is_mentioned(str, 'abcd'))
