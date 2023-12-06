tweet1 = '@asac sdasda sadsdsad . dsdsd #dsddf ddfffffffff  dfdff.'
tweet2 = 'dsdsd dsdsdsdfdf fdfsdsdfsdf.'


def report_shortest(tweet1, tweet2):
    if len(tweet1) < len(tweet2):
        return 'Tweet 1'
    elif len(tweet1) == len(tweet2):
        return 'Same length'
    else:
        return 'Tweet 2'

print(report_shortest(tweet1, tweet2))
