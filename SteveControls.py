from malmo import MalmoPython

class SteveControls:

    def __init__(self, agent_host):
        self.agent = agent_host

    def crouch(self, crouching):
        if crouching:
            print("crouch")
            self.agent.sendCommand("crouch 0")
        else:
            print("stand")
            self.agent.sendCommand("crouch 1")