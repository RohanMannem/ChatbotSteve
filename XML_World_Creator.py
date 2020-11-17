from __future__ import print_function
from builtins import range
import os
import sys
import time
import random
import SteveControls
import reader
try:
    from malmo import MalmoPython
except:
    import MalmoPython


if sys.version_info[0] == 2:
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately
else:
    import functools
    print = functools.partial(print, flush=True)

# HYPERPARAMETERS
flowerChance = 0.01
SIZE = 24
waterGap = SIZE/5
crouching = False

flowerXML = ""
for x in range (-SIZE + 4, SIZE - 3):
  for z in range (-SIZE + 4, SIZE - 3):
    plant = random.uniform(0, 1)
    if plant <= flowerChance:
      type = random.randint(0, 1)
      if type <= 0.5:
        flowerXML += "<DrawBlock x='{}' y='{}' z='{}' type='red_flower'/>".format(x, 227, z)
      else:
        flowerXML += "<DrawBlock x='{}' y='{}' z='{}' type='yellow_flower'/>".format(x, 227, z)

floorLightsXML = ""
for x in range (-SIZE, SIZE):
  for z in range (-SIZE, SIZE):
    if x % 4 == 0 and z % 4 == 0 and x != 0 and z != 0 and (x == z or x == -z):
      floorLightsXML += "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='glowstone'/>".format(x, 226, z, (-1 * x), 226, z)
      floorLightsXML += "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='glowstone'/>".format((-1 * x), 226, z, (-1 * x), 226, (-1 * z))
      floorLightsXML += "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='glowstone'/>".format((-1 * x), 226, (-1 * z), x, 226, (-1 * z))
      floorLightsXML += "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='glowstone'/>".format(x, 226, (-1 * z), x, 226, z)
floorLightsXML += "<DrawBlock x='{}' y='{}' z='{}' type='glowstone'/>".format(0, 226, 0)

waterXML = ""
for x in range (-SIZE, SIZE):
  for z in range (-SIZE, SIZE):
    if (-SIZE + waterGap < x < -SIZE or SIZE - waterGap < x < SIZE) and ((-SIZE + waterGap < z < -SIZE or SIZE - waterGap < z < SIZE)) and (x == z or x == -z):
      waterXML += "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='water'/>".format(x, 220, z, (-1 * x), 226, z)
      waterXML += "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='water'/>".format((-1 * x), 220, z, (-1 * x), 226, (-1 * z))
      waterXML += "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='water'/>".format((-1 * x), 220, (-1 * z), x, 226, (-1 * z))
      waterXML += "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='water'/>".format(x, 220, (-1 * z), x, 226, z)

torchXML = ""
for x in range (-SIZE + 1, SIZE):
  if x % 2 == 0:
    torchXML += "<DrawBlock x='{}' y='{}' z='{}' type='torch'/>".format(x, 233, SIZE)
    torchXML += "<DrawBlock x='{}' y='{}' z='{}' type='torch'/>".format(x, 233, -SIZE)
for z in range (-SIZE + 1, SIZE):
  if z % 2 == 0:
    torchXML += "<DrawBlock x='{}' y='{}' z='{}' type='torch'/>".format(SIZE, 233, z)
    torchXML += "<DrawBlock x='{}' y='{}' z='{}' type='torch'/>".format(-SIZE, 233, z)

missionXML='''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
            <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            
              <About>
                <Summary>Chat with Chatbot Steve</Summary>
              </About>
              
              <ServerSection>
                <ServerInitialConditions>
                  <Time>
                    <StartTime>18000</StartTime>
                  </Time>
                  <Weather>clear</Weather>
                  <AllowSpawning>true</AllowSpawning>
                </ServerInitialConditions>
                <ServerHandlers>
                  <FlatWorldGenerator generatorString="3;7,220*1,5*3,2;3;,biome_1" forceReset="true"/>
                  <DrawingDecorator>''' + \
                    "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='brick_block'/>".format(-SIZE, 227, -SIZE, SIZE, 233, -SIZE) + \
                    "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='brick_block'/>".format(-SIZE, 227, -SIZE, -SIZE, 233, SIZE) + \
                    "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='brick_block'/>".format(SIZE, 227, SIZE, SIZE, 233, -SIZE) + \
                    "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='brick_block'/>".format(SIZE, 227, SIZE, -SIZE, 233, SIZE) + \
                    "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='glass'/>".format(-SIZE, 228, -SIZE, SIZE, 228, -SIZE) + \
                    "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='glass'/>".format(-SIZE, 228, -SIZE, -SIZE, 228, SIZE) + \
                    "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='glass'/>".format(SIZE, 228, SIZE, SIZE, 228, -SIZE) + \
                    "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='glass'/>".format(SIZE, 228, SIZE, -SIZE, 228, SIZE) + \
                    "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='iron_block'/>".format(-SIZE, 230, -SIZE, SIZE, 230, -SIZE) + \
                    "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='iron_block'/>".format(-SIZE, 230, -SIZE, -SIZE, 230, SIZE) + \
                    "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='iron_block'/>".format(SIZE, 230, SIZE, SIZE, 230, -SIZE) + \
                    "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='iron_block'/>".format(SIZE, 230, SIZE, -SIZE, 230, SIZE) + \
                    "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='glass'/>".format(-SIZE, 232, -SIZE, SIZE, 232, -SIZE) + \
                    "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='glass'/>".format(-SIZE, 232, -SIZE, -SIZE, 232, SIZE) + \
                    "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='glass'/>".format(SIZE, 232, SIZE, SIZE, 232, -SIZE) + \
                    "<DrawCuboid x1='{}' y1='{}' z1='{}' x2='{}' y2='{}' z2='{}' type='glass'/>".format(SIZE, 232, SIZE, -SIZE, 232, SIZE) + \
                    floorLightsXML + \
                    flowerXML + \
                    waterXML + \
                    torchXML + \
                    '''<DrawEntity x="0" y="227" z="8" type="Pig"/>
                    <DrawEntity x="5" y="227" z="8" type="Cow"/>
                    <DrawEntity x="-5" y="227" z="8" type="Chicken"/>
                    <DrawEntity x="10" y="227" z="8" type="Sheep"/>
                    <DrawEntity x="-10" y="227" z="8" type="Horse" />
                  </DrawingDecorator>
                  <ServerQuitFromTimeUp timeLimitMs="1000000"/>
                  <ServerQuitWhenAnyAgentFinishes/>
                </ServerHandlers>
              </ServerSection>
              
              <AgentSection mode="Survival">
                <Name>SteveWhisperer</Name>
                <AgentStart>
                  <Placement x="0" y="227" z="0" yaw="0"/>
                  <Inventory>
                    <InventoryItem slot="0" type="diamond_sword"/>
                    <InventoryItem slot="1" type="diamond_pickaxe"/>
                    <InventoryItem slot="2" type="fishing_rod"/>
                    <InventoryItem slot="3" type="wheat" quantity="64"/>
                    <InventoryItem slot="4" type="carrot" quantity="64"/>
                    <InventoryItem slot="5" type="melon_seeds" quantity="64"/>
                    <InventoryItem slot="6" type="saddle" quantity="64"/>
                    <InventoryItem slot="7" type="apple" quantity="64"/>
                </Inventory>
                </AgentStart>
                <AgentHandlers>
                  <ObservationFromFullStats/>
                  <ObservationFromNearbyEntities>''' + \
                    "<Range name='Find' xrange='{}'  yrange='{}'  zrange='{}' />".format(SIZE, 2, SIZE) + \
                  '''</ObservationFromNearbyEntities>
                  <AbsoluteMovementCommands/>
                  <ContinuousMovementCommands turnSpeedDegs="180"/>
                  <InventoryCommands/>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''

# the extra port for Zhaodong, just leave it there please. :-)
client_pool = MalmoPython.ClientPool()
client_pool.add(MalmoPython.ClientInfo("127.0.0.1", 10001))

# Create default Malmo objects:

agent_host = MalmoPython.AgentHost()
try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print('ERROR:',e)
    print(agent_host.getUsage())
    exit(1)
if agent_host.receivedArgument("help"):
    print(agent_host.getUsage())
    exit(0)

my_mission = MalmoPython.MissionSpec(missionXML, True)
my_mission_record = MalmoPython.MissionRecordSpec()

# Attempt to start a mission:
max_retries = 3
for retry in range(max_retries):
    try:
        # extra port for Zhaodong, Plz do not change. :)
        # agent_host.startMission(my_mission, client_pool, my_mission_record, 0, "")
        agent_host.startMission( my_mission, my_mission_record )
        break
    except RuntimeError as e:
        if retry == max_retries - 1:
            print("Error starting mission:",e)
            exit(1)
        else:
            time.sleep(2)

# Loop until mission starts:
world_state = agent_host.getWorldState()
while not world_state.has_mission_begun:
    print(".", end="")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print("Error:", error.text)

print("Mission running ")

# Loop until mission ends:
while world_state.is_mission_running:
    time.sleep(1)

    commands = reader.Reader().getDict()
    steve = SteveControls.SteveControls(agent_host)
    print("commands:", commands)
    animalList = ["pig", "cow", "sheep", "chicken", "horse"]
    for command, entity in commands.items():
        if entity == [1]:
          nums = 1
        else:
          nums = entity

        if command == "crouch":
            steve.crouch(crouching)
            crouching = not crouching
        elif command == "jump":
            steve.jump(nums)
        elif command == "walk":
            steve.walk(nums)
        elif command == "turn":
            steve.turn(nums)
        elif command == "attack":
            steve.attack(nums)
        elif command == "find":
          if entity[0][0] == "steve":
            steve.getSteve()
          elif entity[0][0] == "water":
            steve.findWater()
          elif entity[0][0] in animalList:
            steve.findAnimal(entity[0][0])
        elif command == "catch":
          if entity[0][0] == "fish":
            steve.fish()
        elif command == "ride":
          if entity[0][0] == "horse":
            steve.ride()
          else:
            print("You can't ride that animal!")
        elif command == "feed":
          if entity[0][0] in animalList:
            steve.feed(entity[0][0])


    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print("Error:", error.text)

print()
print("Mission ended")
# Mission has ended.

