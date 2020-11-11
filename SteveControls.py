try:
    from malmo import MalmoPython
except:
    import MalmoPython

import time

class SteveControls:

    def __init__(self, agent_host):
        self.agent = agent_host

    def crouch(self, crouching, times = 1):
        if crouching:
            for i in range(times):
                print("crouch")
                time.sleep(0.5)
                self.agent.sendCommand("crouch 0")
                time.sleep(0.5)
                self.agent.sendCommand("crouch 1")
            self.agent.sendCommand("crouch 0")
        else:
            for i in range(times):
                print("stand")
                time.sleep(0.5)
                self.agent.sendCommand("crouch 1")
                time.sleep(0.5)
                self.agent.sendCommand("crouch 0")

    def jump(self, times = 1):
        for i in range(times):
            self.agent.sendCommand("jump 1")
            time.sleep(0.58)
        self.agent.sendCommand("jump 0")            

    def walk(self, times = 10):
        self.agent.sendCommand("move 1")
        for i in range(times):
            time.sleep(0.2)
        self.agent.sendCommand("move 0")

    def turn(self, times = 1):
        self.agent.sendCommand("turn 1")
        for i in range(times):
            time.sleep(0.4875)
        self.agent.sendCommand("turn 0")

    def attack(self, times = 1):
        for i in range(times):
            self.agent.sendCommand("attack 1")
            time.sleep(0.55)
        self.agent.sendCommand("attack 0")

