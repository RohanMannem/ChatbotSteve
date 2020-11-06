import reader

if __name__ == "__main__":
    """Sample Inputs"""
    # find a pig and five cats, kill two cows, and then walk and crouch, and finally feed a cow
    # find forty-five cows and ninety-nine pigs
    # kill three-million cats and one billion cows
    while True:
        read = dict(reader.Reader().getDict())
        if not bool(read):
            break
        print(read)
