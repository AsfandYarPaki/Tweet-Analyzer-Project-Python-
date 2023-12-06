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

