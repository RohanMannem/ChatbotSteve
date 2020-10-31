from __future__ import print_function
from builtins import range
from malmo import MalmoPython
import os
import sys
import time

if sys.version_info[0] == 2:
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately
else:
    import functools
    print = functools.partial(print, flush=True)

missionXML='''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
            <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            
              <About>
                <Summary>Chat with Chatbot Steve</Summary>
              </About>
              
              <ServerSection>
                <ServerInitialConditions>
                  <Time>
                    <StartTime>6000</StartTime>
                    <AllowPassageOfTime>false</AllowPassageOfTime>
                  </Time>
                  <Weather>clear</Weather>
                  <AllowSpawning>true</AllowSpawning>
                </ServerInitialConditions>
                <ServerHandlers>
                  <FlatWorldGenerator generatorString="3;7,220*1,5*3,2;3;,biome_1"/>
                  <DrawingDecorator>
                    <DrawEntity x="0"  y="227" z="8" type="Pig"/>
                    <DrawEntity x="3"  y="227" z="8" type="Cow"/>
                    <DrawEntity x="-3"  y="227" z="8" type="Chicken"/>
                    <DrawEntity x="6"  y="227" z="8" type="Sheep"/>

                    <DrawCuboid x1="-10" y1="227" z1="-10" x2="10" y2="227" z2="-10" type="fence"/>
                    <DrawCuboid x1="-10" y1="227" z1="-10" x2="-10" y2="227" z2="10" type="fence"/>
                    <DrawCuboid x1="10" y1="227" z1="10" x2="10" y2="227" z2="-10" type="fence"/>

                    <DrawCuboid x1="-9" y1="226" z1="10" x2="9" y2="226" z2="10" type="water"/>
                    <DrawCuboid x1="9" y1="226" z1="10" x2="9" y2="226" z2="20" type="water"/>
                    <DrawCuboid x1="9" y1="226" z1="20" x2="-9" y2="226" z2="20" type="water"/>
                    <DrawCuboid x1="-9" y1="226" z1="20" x2="-9" y2="226" z2="10" type="water"/>

                    <DrawBlock x="-5"  y="226" z="0" type="lava" />
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
                    <InventoryItem slot="3" type="bone" quantity="64"/>
                    <InventoryItem slot="4" type="wheat" quantity="64"/>
                    <InventoryItem slot="5" type="apple" quantity="64"/>
                    <InventoryItem slot="6" type="saddle" quantity="64"/>
                </Inventory>
                </AgentStart>
                <AgentHandlers>
                  <ObservationFromFullStats/>
                  <ContinuousMovementCommands turnSpeedDegs="180"/>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''

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
        agent_host.startMission( my_mission, my_mission_record )
        break
    except RuntimeError as e:
        if retry == max_retries - 1:
            print("Error starting mission:",e)
            exit(1)
        else:
            time.sleep(2)

# Loop until mission starts:
print("Waiting for the mission to start ", end=' ')
world_state = agent_host.getWorldState()
while not world_state.has_mission_begun:
    print(".", end="")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print("Error:",error.text)

print()
print("Mission running ", end=' ')

# Loop until mission ends:
while world_state.is_mission_running:
    #agent_host.sendCommand("turn 1")
    print(".", end="")
    time.sleep(2)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print("Error:",error.text)

print()
print("Mission ended")
# Mission has ended.
