from malmo import MalmoPython
import time

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

    def jump(self):
        self.agent.sendCommand("jump 1")
        time.sleep(0.5)
        self.agent.sendCommand("jump 0")

    def walk(self, times = 10):
        for i in range(times):
            self.agent.sendCommand("move 1")
            time.sleep(0.1)
        self.agent.sendCommand("move 0")