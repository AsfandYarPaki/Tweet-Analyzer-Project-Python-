str = 'abcdefghijkl. as #dcdvf. sdsd sdsffg kjhk.'

def hasher(str):
    for i in str:
        if i == '@' or i == '#':
            return 'valid password'

print(hasher(str))
