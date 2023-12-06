str = 'abcdefghijkl. as dcdvf. sdsd sdsffg kjhk.'


def contains_hash_symbol(tweet):
    for i in tweet:
        if i == '#':
            return True
    else:
        return False
print(contains_hash_symbol(str))
