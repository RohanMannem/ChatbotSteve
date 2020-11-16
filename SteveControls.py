try:
    from malmo import MalmoPython
except:
    import MalmoPython

import time
import json
import math

class SteveControls:

    def __init__(self, agent_host):
        self.agent = agent_host
        self.attempts = 0

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
            AnimalPosition = observation["Find"]
            #print(observation)
        return [observation, AnimalPosition]

    def findWater(self):
        steve = self.getSteve()[0]
        
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
                self.walk(math.ceil(abs(diffX)))
            else:
                self.agent.sendCommand("setYaw -90")
                self.walk(math.ceil(abs(diffX)))
        else:
            if diffZ < 0:
                self.agent.sendCommand("setYaw 180")
                self.walk(math.ceil(abs(diffZ)))
            else:
                self.agent.sendCommand("setYaw 0")
                self.walk(math.ceil(abs(diffZ)))

    def findAnimal(self, animal):
        while True:
            entitiesInfor = self.getSteve()[1]
            steve = entitiesInfor[0]

            diffX = 0
            diffZ = 0

            for a in entitiesInfor:
                if a['name'].lower() == animal:
                    diffX = a['x'] - steve['x']
                    diffZ = a['z'] - steve['z']

            moveDis = math.floor(math.sqrt(abs(diffX)**2 + abs(diffZ)**2))
            Yaw = -180 * math.atan2(diffX, diffZ) / math.pi

            self.agent.sendCommand("setYaw {}".format(Yaw))
            self.walk(moveDis)

            if moveDis <= 1:
                break

    def fish(self, times = 1):
        timer = time.time()
        for i in range(times):
            self.findWater()

            self.agent.sendCommand('hotbar.3 1')
            self.agent.sendCommand('hotbar.3 0')

            self.agent.sendCommand('setPitch 15')

            self.agent.sendCommand('use 1')
            self.agent.sendCommand('use 0')

            while True:
                now = time.time()

                if timer - now > 30:
                    break

                currSteve = self.getSteve()
                animalPosition = currSteve[1]

                for animalDict in animalPosition:
                    print(animalDict) # Look for the one with name = unknown

                time.sleep(1)

            self.agent.sendCommand('use 1')
            self.agent.sendCommand('use 0')

    def ride(self):        
        while True:
            self.findAnimal("horse")
            steve = self.getSteve()
            steve = steve[1]
            
            for entity in steve:
                if entity["name"] == "SteveWhisperer":
                    steve = entity

            if steve["y"] != 228:
                self.agent.sendCommand('hotbar.8 1')
                self.agent.sendCommand('hotbar.8 0')
                self.agent.sendCommand('setPitch 15')
                self.agent.sendCommand('use 1')
                self.agent.sendCommand('use 0')
                time.sleep(2)

            if self.attempts >= 10:
                break

            if steve["y"] == 228:
                break
            else:
                self.attempts += 1
                self.ride()