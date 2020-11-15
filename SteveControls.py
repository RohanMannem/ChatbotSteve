try:
    from malmo import MalmoPython
except:
    import MalmoPython

import time
import json

class SteveControls:

    def __init__(self, agent_host):
        self.agent = agent_host

    def crouch(self, crouching):
        if crouching:
            print("stand")
            time.sleep(0.5)
            self.agent.sendCommand("crouch 0")
        else:
            print("crouch")
            time.sleep(0.5)
            self.agent.sendCommand("crouch 1")

    def jump(self, times = 1):
        for i in range(times):
            self.agent.sendCommand("jump 1")
            time.sleep(0.58)
        self.agent.sendCommand("jump 0")            

    def walk(self, times = 10):
        for i in range(times):
            self.agent.sendCommand("move 1")
            time.sleep(0.2)
            self.agent.sendCommand("move 0")

    def turn(self, times = 1):
        for i in range(times):
            self.agent.sendCommand("turn 1")
            time.sleep(0.5)
            self.agent.sendCommand("turn 0")

    def attack(self, times = 1):
        for i in range(times):
            self.agent.sendCommand("attack 1")
            time.sleep(0.55)
        self.agent.sendCommand("attack 0")

    def getSteve(self):
        lastWorldState = self.agent.peekWorldState()
        if lastWorldState.number_of_observations_since_last_state > 0:
            observation = json.loads(lastWorldState.observations[-1].text)
            print(observation)
        return observation

    def findWater(self):
        steve = self.getSteve()
        
        if steve["XPos"] < 0:
            waterX = -17
        else:
            waterX = 17

        if steve["ZPos"] < 0:
            waterZ = -17
        else:
            waterZ = 17

        diffX = waterX - steve["XPos"]
        diffZ = waterZ - steve["ZPos"]

        if abs(diffX) < abs(diffZ):
            if diffX < 0:
                self.agent.sendCommand("setYaw 90")
                self.walk(int(abs(diffX)))
            else:
                self.agent.sendCommand("setYaw -90")
                self.walk(int(abs(diffX)))
        else:
            if diffZ < 0:
                self.agent.sendCommand("setYaw 180")
                self.walk(int(abs(diffZ)))
            else:
                self.agent.sendCommand("setYaw 0")
                self.walk(int(abs(diffZ)))

    def findAnimal(self):
        count = 0
        self.agent.sendCommand('setPitch 30')
        while True:
            steve = self.getSteve()
            
            if "LineOfSight" in steve:
                break
            if "Entities" in steve:
                break

            count += 1

            if count > 100:
                break

        print(steve)
