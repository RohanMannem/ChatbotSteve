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

    def kill(self, animal):
        total = 0
        for a in self.getSteve()[1]:
            if a['name'].lower() == animal:
                total += 1
        if total <= 0:
            return
        while True:
            self.findAnimal(animal)
            self.agent.sendCommand('setPitch 50')
            time.sleep(0.1)
            self.agent.sendCommand("attack 1")
            time.sleep(0.1)
            self.agent.sendCommand('setPitch 0')
            self.agent.sendCommand("attack 0")
            time.sleep(0.1)
            tempTotal = 0
            for a in self.getSteve()[1]:
                if a['name'].lower() == animal:
                    tempTotal+= 1
            if tempTotal != total:
                break
        self.agent.sendCommand('setPitch 0')


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

    def findAnimal(self, animal, num=1):
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
                self.agent.sendCommand('hotbar.9 1')
                self.agent.sendCommand('hotbar.9 0')
                self.agent.sendCommand('setPitch 15')
                self.agent.sendCommand('use 1')
                self.agent.sendCommand('use 0')
                time.sleep(2)

            if self.attempts >= 10:
                self.attempts = 0
                break

            if steve["y"] == 228:
                self.attempts = 0
                break
            else:
                self.attempts += 1
                self.ride()

    def feed(self, animal, num):
        for i in range(num):
            self.findAnimal(animal)
            if animal == "pig":
                self.agent.sendCommand("hotbar.5 1")
                self.agent.sendCommand("hotbar.5 0")
                self.agent.sendCommand('setPitch 30')
            elif animal == "cow" or animal == "sheep":
                self.agent.sendCommand("hotbar.4 1")
                self.agent.sendCommand("hotbar.4 0")
                self.agent.sendCommand('setPitch 15')
            elif animal =="horse":
                self.agent.sendCommand("hotbar.8 1")
                self.agent.sendCommand("hotbar.8 0")
                self.agent.sendCommand('use 1')
                self.agent.sendCommand('use 0')
                return
            elif animal == "chicken":
                self.agent.sendCommand("hotbar.6 1")
                self.agent.sendCommand("hotbar.6 0")
                self.agent.sendCommand('setPitch 45')
            time.sleep(1)
            self.agent.sendCommand('use 1')
            self.agent.sendCommand('use 0')
            time.sleep(1)
            self.agent.sendCommand('setPitch 0')
            self.agent.sendCommand("hotbar.0 1")
            self.agent.sendCommand("hotbar.0 0")
        self.agent.sendCommand("hotbar.0 1")
        self.agent.sendCommand("hotbar.0 0")


