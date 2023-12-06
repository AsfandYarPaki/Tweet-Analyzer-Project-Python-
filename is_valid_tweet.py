str = 'abcdefghijkl. as #dcdvf. sdnnsd sdsffg kjhk.'

def is_valid_tweet(tweet):
    return True if len(tweet)>=1 and len(tweet)<=140 else False
print(is_valid_tweet('abcdefghijkl. as #dcdvf. sdnnsd sdsffg kjhk.'))

def contains_hash_symbol(tweet):
    for i in tweet:
        for s in i:
            if i=='#':
                return True 
            else:
                return False
print(contains_hash_symbol(str))
