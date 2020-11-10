import reader
import SteveControls

if __name__ == "__main__":
    """Sample Inputs"""
    # find a pig and five cats, kill two cows, and then walk and crouch, and finally feed a cow
    # find forty-five cows and kill ninety-nine pigs and find forty cows
    # kill three-million cats and one billion cows
    # crouch 6 and walk 5 and jump 6 and turn 2
    while True:
        commands = reader.Reader().getDict()
        print(commands)
        # read = dict(reader.Reader().getDict())
        # if not bool(read):
        #     break
        # print(read)
