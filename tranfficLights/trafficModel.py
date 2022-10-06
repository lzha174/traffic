import collections

from simPyExtentionSkillSet import *
red= 0
green = 1
trafficInterval = 6
# at intersection, there are 4 traffic lights to make a configuration
# for cars travelling from left, it should look at the lightForLeft and so on so fourth

traffic_config =  collections.namedtuple('traffic', 'lightForLeftStraight lightForLeftTurnRight'
                                                    ' lightForRightStraight lightForRightTurnRight lightForUpStraight lightForUpTurnRigt'
                                                    ' lightForBottomStraight lightForBottomTurnRight')
configLeftRightStraight = traffic_config(lightForLeftStraight=green, lightForLeftTurnRight=red, lightForRightStraight=green, lightForRightTurnRight=red,
                                         lightForUpStraight=red, lightForUpTurnRigt=red, lightForBottomStraight=red, lightForBottomTurnRight=red)

configLeftTurnRight = traffic_config(lightForLeftStraight=red, lightForLeftTurnRight=green, lightForRightStraight=red, lightForRightTurnRight=red,
                         lightForUpStraight=red, lightForUpTurnRigt=red, lightForBottomStraight=red, lightForBottomTurnRight=red)

configUpTurnRight = traffic_config(lightForLeftStraight=red, lightForLeftTurnRight=red, lightForRightStraight=red, lightForRightTurnRight=red,
                         lightForUpStraight=red, lightForUpTurnRigt=green, lightForBottomStraight=red, lightForBottomTurnRight=red)

configUpBottomStraight= traffic_config(lightForLeftStraight=red, lightForLeftTurnRight=red, lightForRightStraight=red, lightForRightTurnRight=red,
                                       lightForUpStraight=green, lightForUpTurnRigt=red, lightForBottomStraight=green, lightForBottomTurnRight=red)


configBottomTurnRight = traffic_config(lightForLeftStraight=red, lightForLeftTurnRight=red, lightForRightStraight=red, lightForRightTurnRight=red,
                         lightForUpStraight=red, lightForUpTurnRigt=red, lightForBottomStraight=red, lightForBottomTurnRight=green)




configRightTurnRight = traffic_config(lightForLeftStraight=red, lightForLeftTurnRight=red, lightForRightStraight=red, lightForRightTurnRight=green,
                         lightForUpStraight=red, lightForUpTurnRigt=red, lightForBottomStraight=red, lightForBottomTurnRight=red)

configRightToLeft = traffic_config(lightForLeftStraight=red, lightForLeftTurnRight=red, lightForRightStraight=green, lightForRightTurnRight=red,
                         lightForUpStraight=red, lightForUpTurnRigt=red, lightForBottomStraight=red, lightForBottomTurnRight=red)


trafficConfigs = [configLeftRightStraight, configLeftTurnRight, configUpTurnRight,
                  configBottomTurnRight, configRightTurnRight, configUpBottomStraight]
# two trafffic modes alternative every 10 mins


# define a 26x18 grid, index from 0,0 to 11,11
# traffic light is at 12,8 -> 15,11
turnLeft = 'turnLeft'
straight = 'straight'
turnRight = 'turnRight'
startLeft = 'startLeft'
startRight = 'startRight'
startUp = 'startUp'
startDown = 'startDown'

startLeftPosition = [12,0]
startRightPosition = [15,17]
startUpPosition = [0,11]
startDownPosition = [25,8]

leftToTopStopPosition = [12,7]
leftToRigthStopPostion = [12,7]
leftToBottomStopPostion = [13,7]
leftToBottomTurnPosition = [13,10]
leftToTopTurnPosition = [12,8]

rightToLeftStopPosition = [15,12]


rightToBottomStopPosition = [15,12]
rightToBottomTurnPosition = [15,11]
rightToUpStopPostion = [14,12]
rightToUpTurnPosition = [14,9]

upToLeftStopPosition = [11, 10]
upToLeftTurnPosition = [14,10]


upToRightStopPosition = [11,11]
upToRightTurnPosition = [12,11]


bottomToTopStopPosition = [16,8]
bottomToRightStopPosition = [16,9]
bottomToRightTurnPosition = [13,9]
bottomToLeftStopPosition = bottomToTopStopPosition
bottomToLeftTurnPosition = [15,8]

leftToTopEnd = [0,8]
leftToBottomEnd = [25,10]
upToLeftEnd = [14,0]
upToRightEnd = [12,17]
upToBottomEnd = [25,11]
bottomToRightEnd = [13,17]
rightToUpEnd = [0,9]
lefttoRightEnd = [12,17]
bottomToTopEnd = [0,8]
bottomToLeftEnd = [15,0]
righttoLeftEnd = [15,0]
upToRightEnd = [12,17]
rightToBottomEnd = [25,11]

trafficHistory = []

#startLocation left, right, up or bottom
class Car():
    def __init__(self, id, startLocation, startPostion, trafficLightTurn):
        self.id = id
        self.startLocation = startLocation
        self.startPostion = startPostion
        self.trafficLightTurn = trafficLightTurn
        self.currentPosition= startPostion
        self.changedLaneForRightTurn = False
        self.turnedRight = False
        self.turnedLeft = False
        self.history = []
        self.trafficHistory = []

    def add_traffic(self, t = 0, traffic: traffic_config = None):
        self.trafficHistory.append([t,traffic])
    def next_position(self):
        if self.trafficLightTurn == turnLeft:
            current = self.currentPosition
            if self.startLocation == startLeft:
                if current == leftToTopTurnPosition and not self.turnedLeft:
                    self.turnedLeft = True
                    new = [current[0] - 1, current[1]]
                elif current[1] < leftToTopTurnPosition[1]:
                    new = [current[0] , current[1] + 1]
                elif self.turnedLeft:
                    new = [current[0] - 1, current[1]]
            if self.startLocation == startUp:
                if current == upToRightTurnPosition and not self.turnedLeft:
                    self.turnedLeft = True
                    new = [current[0] , current[1] + 1]
                elif current[0] < upToRightTurnPosition[0]:
                    new = [current[0] +1 , current[1]]
                elif self.turnedLeft:
                    new = [current[0], current[1] + 1]
            if self.startLocation == startDown:
                if current == bottomToLeftTurnPosition and not self.turnedLeft:
                    self.turnedLeft = True
                    new = [current[0] , current[1] - 1]
                elif current[0] > bottomToLeftTurnPosition[0]:
                    new = [current[0] -1 , current[1]]
                elif self.turnedLeft:
                    new = [current[0], current[1] -1]
            if self.startLocation == startRight:
                if current == rightToBottomTurnPosition and not self.turnedLeft:
                    self.turnedLeft = True
                    new = [current[0] + 1 , current[1]]
                elif current[1] > rightToBottomTurnPosition[1]:
                    new = [current[0]  , current[1]-1]
                elif self.turnedLeft:
                    new = [current[0] +1 , current[1]]
        if self.trafficLightTurn == straight:
            if self.startLocation == startLeft:
                current = self.currentPosition
                new = [current[0], current[1] + 1]
                #self.currentPosition = new
            if self.startLocation == startRight:
                current = self.currentPosition
                new = [current[0], current[1] - 1]
                #self.currentPosition = new
            if self.startLocation == startUp:
                current = self.currentPosition
                new = [current[0] + 1, current[1]]
                #self.currentPosition = new
            if self.startLocation == startDown:
                current = self.currentPosition
                new = [current[0] -1, current[1]]
                #self.currentPosition = new

        if self.trafficLightTurn == turnRight:
            if not self.changedLaneForRightTurn:
                # has not move dto the turn lane, try to as early as possible
                if self.startLocation == startLeft:
                    current = self.currentPosition
                    new = [current[0] + 1, current[1]]
                    #self.currentPosition = new

                if self.startLocation == startRight:

                    current = self.currentPosition
                    new = [current[0] - 1, current[1]]
                    #self.currentPosition = new
                if self.startLocation == startUp:
                    current = self.currentPosition
                    new = [current[0] , current[1] - 1]
                    #self.currentPosition = new
                if self.startLocation == startDown:
                    current = self.currentPosition
                    new = [current[0], current[1] + 1]
                    #self.currentPosition = new
                self.changedLaneForRightTurn = True
            else:
                # lane already changed
                # keep going straight if not passed traffic light
                if self.startLocation == startLeft:

                    current = self.currentPosition
                    if current[1] < leftToBottomStopPostion[1]:
                        new = [current[0], current[1] + 1]
                        #self.currentPosition = new
                    # betwen stop position and turn position, keep going
                    if current[1] >= leftToBottomStopPostion[1] and current[1]< leftToBottomTurnPosition[1]:
                        new = [current[0], current[1] + 1]
                        #self.currentPosition = new
                    # not turn to bottom
                    if  current == leftToBottomTurnPosition and not self.turnedRight:
                        self.turnedRight = True
                        new = [current[0] + 1, current[1] ]
                        #self.currentPosition = new
                    # turned already, keep going
                    if current[1] == leftToBottomTurnPosition[1] and self.turnedRight:
                        new = [current[0] + 1, current[1] ]
                        #self.currentPosition = new

                if self.startLocation == startRight:

                    current = self.currentPosition
                    # not at traffic yet, keep going
                    if current[1] > rightToUpStopPostion[1]:
                        new = [current[0], current[1] - 1]
                        #self.currentPosition = new
                    # at traffic, not not reaching turn position
                    if current[1] <= rightToUpStopPostion[1] and current[1]> rightToUpTurnPosition[1]:
                        new = [current[0], current[1] - 1]
                        #self.currentPosition = new
                    # now turn to up
                    if  current == rightToUpTurnPosition and not self.turnedRight:
                        self.turnedRight = True
                        new = [current[0] -1, current[1] ]
                        #self.currentPosition = new
                    # turned already, keep going
                    if current[1] == rightToUpTurnPosition[1] and self.turnedRight:
                        new = [current[0] - 1, current[1] ]
                        #self.currentPosition = new

                if self.startLocation == startUp:

                    current = self.currentPosition
                    # not at traffic yet, keep going
                    if current[0] < upToLeftStopPosition[0]:
                        new = [current[0] + 1, current[1]]
                        #self.currentPosition = new
                    # at traffic, not not reaching turn position
                    if current[0] >= upToLeftStopPosition[0] and current[1]< upToLeftTurnPosition[0]:
                        new = [current[0] + 1, current[1] ]
                        #self.currentPosition = new
                    # now turn to left road
                    if  current == upToLeftTurnPosition and not self.turnedRight:
                        self.turnedRight = True
                        new = [current[0] , current[1] - 1 ]
                        #self.currentPosition = new
                    # turned already, keep going
                    if current[0] == upToLeftTurnPosition[0] and self.turnedRight:
                        new = [current[0] , current[1] -1 ]
                        #self.currentPosition = new

                if self.startLocation == startDown:

                    current = self.currentPosition
                    # not at traffic yet, keep going
                    if current[0] > bottomToRightStopPosition[0]:
                        new = [current[0] - 1, current[1]]
                        #self.currentPosition = new
                    # at traffic, not not reaching turn position
                    if current[0] <= bottomToRightStopPosition[0] and current[0]> bottomToRightTurnPosition[0]:
                        new = [current[0] - 1, current[1] ]
                        #self.currentPosition = new
                    # now turn to right road
                    if  current == bottomToRightTurnPosition and not self.turnedRight:
                        self.turnedRight = True
                        new = [current[0] , current[1] + 1 ]
                        #self.currentPosition = new
                    # turned already, keep going
                    if current[0] == bottomToRightTurnPosition[0] and self.turnedRight:
                        new = [current[0] , current[1] +1 ]
                        #self.currentPosition = new
        return new
    
    def update_possition(self, p=[], t = 0):
        self.currentPosition = p
        self.history.append([self.id, self.startLocation,
                             self.trafficLightTurn, self.currentPosition[0], self.currentPosition[1], \
                            t])


    def getHistory(self):
        # expand history to ever time step
        newHistory = []
        for idx,value in enumerate(self.history):
            newValue = copy.deepcopy(value)
            currentTime = newValue[-1]
            for trafficIdx in range(len(self.trafficHistory) - 1):
                if self.trafficHistory[trafficIdx][0] <= currentTime and self.trafficHistory[trafficIdx + 1][0] > currentTime:
                    traffic = self.trafficHistory[trafficIdx][1]
                    break
            list1 = ([traffic.lightForLeftStraight, traffic.lightForLeftTurnRight, \
                                        traffic.lightForRightStraight, traffic.lightForRightTurnRight, \
                                        traffic.lightForUpStraight, traffic.lightForUpTurnRigt, \
                                        traffic.lightForBottomStraight, traffic.lightForBottomTurnRight])

            newValue.extend(list1)

            newHistory.append(newValue)
            #newHistory.append(value)
            if idx < len(self.history) - 2:
                if self.history[idx+1][-1] - self.history[idx][-1] > 1:
                    for i in range(self.history[idx+1][-1] - self.history[idx][-1] -1):
                        newValue = value[:-1]
                        newValue.append(value[-1]+i + 1)
                        # need the currect traffic information
                        currentTime = newValue[-1]
                        for idx in range(len(self.trafficHistory)-1):
                            if self.trafficHistory[idx][0] <= currentTime and self.trafficHistory[idx+1][0] > currentTime:
                                traffic = self.trafficHistory[idx][1]
                                break
                        newValue.extend([ traffic.lightForLeftStraight, traffic.lightForLeftTurnRight,\
                             traffic.lightForRightStraight, traffic.lightForRightTurnRight,\
                            traffic.lightForUpStraight, traffic.lightForUpTurnRigt,\
                             traffic.lightForBottomStraight, traffic.lightForBottomTurnRight])
                        newHistory.append(newValue)


        historyLog = pandas.DataFrame(newHistory, columns=['id',f'startLocation_{self.id}',f'traffic_{self.id}', f'x_{self.id}',
                                                             f'y_{self.id}',f'time_{self.id}', 'lightForLeftStraight',
                                                           'lightForLeftTurnRight', 'lightForRightStraight',
                                                           'lightForRightTurnRight',
                                         'lightForUpStraight', 'lightForUpTurnRigt', 'lightForBottomStraight',
                                                           'lightForBottomTurnRight'])

        return historyLog
class TrafficSimulation:
    # top left position and vertial and horizontal distance to the boundary
    trafficLightsRect = [12,8]
    trafficCells = []
    for i in range(4):
        for j in range(4):
            trafficCells.append([trafficLightsRect[0]+i, trafficLightsRect[1]+j])

    def __init__(self):


        self.currentTraffic: traffic_config = trafficConfigs[0]
        self.env = simpy.Environment()

        self.leftToBottomSingal: simpy.Event = simpy.Event(self.env)
        self.leftRightSignal: simpy.Event = simpy.Event(self.env)

        self.upToLeftSignal: simpy.Event = simpy.Event(self.env)
        # stright stinal is used for straight and turn left
        self.upBottomStraightSignal: simpy.Event = simpy.Event(self.env)

        self.bottomToRightSignal:simpy.Event = simpy.Event(self.env)


        self.rightToUpSignal:simpy.Event = simpy.Event(self.env)


        self.res = {}
        # define resoruce for the horizontal locations
        xPositions = [i for i in range(12,16)]
        yPositions = [i for i in range(0,18)]
        for x in xPositions:
            for y in yPositions:
                tag = f'{x}_{y}'
                current_stage_workers = WorkerCollection(tag)
                capacity = 1
                for i in range(capacity):
                    current_stage_workers.add(Worker(i, 0, 23, tag))
                self.res[(x,y)] = MyPriorityResource(self.env,current_stage_workers, tag)
        # now define vertical positions make sure no redef:
        xVerPositions = [i for i in range(0,26)]
        yVerPositions = [i for i in range(8, 12)]

        for x in xVerPositions:
            for y in yVerPositions:
                tag = f'{x}_{y}'
                if (x,y) in self.res:
                    continue
                current_stage_workers = WorkerCollection(tag)
                capacity = 1
                for i in range(capacity):
                    current_stage_workers.add(Worker(i, 0, 23, tag))
                self.res[(x, y)] = MyPriorityResource(self.env, current_stage_workers, tag)

    def load_cars(self,cars):
        self.cars = cars

    
    def runSim(self):
        runUntil = 500
        self.env.process(self.trafficLightsSim())
        start = 5
        for i in range(len(self.cars)):
            self.cars[i].update_possition(self.cars[i].currentPosition, start)
            self.env.process(self.carRun(i, startTime = start))
            start += 4
        self.env.run(until=runUntil)
    
    def carRun(self, idx, startTime =  0):
        yield self.env.timeout(startTime)
        car: Car = self.cars[idx]

        reachEnd = False
        oldReq = None
        oldKey = None
        while not reachEnd:

            nextPosition = car.next_position()
            if car.startLocation == startLeft and car.trafficLightTurn== turnLeft:
                if self.currentTraffic != configLeftRightStraight:
                    if car.currentPosition == leftToTopStopPosition:
                        # cant move forward unless in up to right turn config
                        yield self.leftRightSignal
                        print(f'I can go from left to top at {self.env.now}')
            if car.startLocation == startLeft and car.trafficLightTurn== straight:
                if self.currentTraffic != configLeftRightStraight:
                    if car.currentPosition == leftToRigthStopPostion:
                        # cant move forward unless in up to right turn config
                        yield self.leftRightSignal
                        print(f'I can go from left to right at {self.env.now}')
            if car.startLocation == startUp and car.trafficLightTurn== turnRight:
                if self.currentTraffic != configUpTurnRight:
                    if car.currentPosition == upToLeftStopPosition:
                        # cant move forward unless in up to right turn config
                        yield self.upToLeftSignal
                        print(f'I can turn to left from top at {self.env.now}')
            if car.startLocation == startUp and car.trafficLightTurn== straight:
                if self.currentTraffic != configUpBottomStraight:
                    if car.currentPosition == upToRightStopPosition:
                        # cant move forward unless in up to right turn config
                        yield self.upBottomStraightSignal
                        print(f'I can go to bottom from top at {self.env.now}')
            if car.startLocation == startUp and car.trafficLightTurn== turnLeft:
                if self.currentTraffic != configUpBottomStraight:
                    if car.currentPosition == upToLeftStopPosition:
                        # cant move forward unless in up to right turn config
                        yield self.upBottomStraightSignal
                        print(f'I can turn to right from top at {self.env.now}')
            if car.startLocation == startLeft and car.trafficLightTurn== turnRight:
                if self.currentTraffic != configLeftTurnRight:
                    if car.currentPosition == leftToBottomStopPostion:
                        # cant move forward unless in up to right turn config
                        yield self.leftToBottomSingal
                        print(f'I can turn to bottom from left at {self.env.now}')
            if car.startLocation == startDown and car.trafficLightTurn== turnRight:
                if self.currentTraffic != configBottomTurnRight:
                    if car.currentPosition == bottomToRightStopPosition:
                        # cant move forward unless in up to right turn config
                        yield self.bottomToRightSignal
                        print(f'I can turn to right from bottom at {self.env.now}')
            if car.startLocation == startDown and car.trafficLightTurn== straight:
                if self.currentTraffic != configUpBottomStraight:
                    if car.currentPosition == bottomToTopStopPosition:
                        # cant move forward unless in up to right turn config
                        yield self.upBottomStraightSignal
                        print(f'I can turn to right from bottom at {self.env.now}')
            if car.startLocation == startDown and car.trafficLightTurn== turnLeft:
                if self.currentTraffic != configUpBottomStraight:
                    if car.currentPosition == bottomToLeftStopPosition:
                        # cant move forward unless in up to right turn config
                        yield self.upBottomStraightSignal
                        print(f'I can turn to left from bottom at {self.env.now}')
            if car.startLocation == startRight and car.trafficLightTurn== turnRight:
                if self.currentTraffic != configRightTurnRight:
                    if car.currentPosition == rightToUpStopPostion:
                        # cant move forward unless in up to right turn config
                        yield self.rightToUpSignal
                        print(f'I can turn to up from right at {self.env.now}')
            if car.startLocation == startRight and car.trafficLightTurn== straight:
                if self.currentTraffic != configLeftRightStraight:
                    if car.currentPosition == rightToLeftStopPosition:
                        # cant move forward unless in up to right turn config
                        yield self.leftRightSignal
                        print(f'I can go to left from right at {self.env.now}')
            if car.startLocation == startRight and car.trafficLightTurn== turnLeft:
                if self.currentTraffic != configLeftRightStraight:
                    if car.currentPosition == rightToBottomStopPosition:
                        # cant move forward unless in up to right turn config
                        yield self.leftRightSignal
                        print(f'I can go to bottom from right at {self.env.now}')
            # at 13,6 request 13,7, got it, move to 13,7 after 1 min, but should not release 13,7 yet
            newReq = self.res[(nextPosition[0], nextPosition[1])].request(priority=0, event=NewJobEvent(job_id=idx))
            yield newReq
            # oldReq points to the request at the current posistion before moving to the next posisiton, when we are ready to move
            # to next position, we can release the current position
            if oldReq is not None:
                self.res[oldKey].release(oldReq)
            yield self.env.timeout(1)

            # when resource is acquired at this time, wait 1 timestep and move to the next position, then release the current res
            # then at the new posistion, request the next next position
            #print(f'car {idx} get next free slot at {self.env.now} at {nextPosition}')


            car.update_possition(nextPosition, self.env.now)
            oldReq = newReq
            oldKey = (nextPosition[0], nextPosition[1])

            print(f' car {idx} reach at {self.env.now} at {car.currentPosition}')
            # if this car cannot move forward it should release the current position
            reachEnd = self.checkReachEnd(car, reachEnd)
        # at the boundary, we dont occupy the last posisiton so all cars will get to the end
        self.res[(nextPosition[0], nextPosition[1])].release(newReq)

    def checkReachEnd(self, car, reachEnd):
        if car.startLocation == startLeft and car.trafficLightTurn == straight:
            if car.currentPosition == lefttoRightEnd:
                reachEnd = True
        if car.startLocation == startLeft and car.trafficLightTurn == turnLeft:
            if car.currentPosition == leftToTopEnd:
                reachEnd = True
        if car.startLocation == startLeft and car.trafficLightTurn == turnRight:
            if car.currentPosition == leftToBottomEnd:
                reachEnd = True
        if car.startLocation == startUp and car.trafficLightTurn == turnRight:
            if car.currentPosition == upToLeftEnd:
                reachEnd = True
        if car.startLocation == startUp and car.trafficLightTurn == turnLeft:
            if car.currentPosition == upToRightEnd:
                reachEnd = True
        if car.startLocation == startUp and car.trafficLightTurn == straight:
            if car.currentPosition == upToBottomEnd:
                reachEnd = True
        if car.startLocation == startDown and car.trafficLightTurn == turnRight:
            if car.currentPosition == bottomToRightEnd:
                reachEnd = True
        if car.startLocation == startDown and car.trafficLightTurn == straight:
            if car.currentPosition == bottomToTopEnd:
                reachEnd = True
        if car.startLocation == startDown and car.trafficLightTurn == turnLeft:
            if car.currentPosition == bottomToLeftEnd:
                reachEnd = True
        if car.startLocation == startRight and car.trafficLightTurn == turnRight:
            if car.currentPosition == rightToUpEnd:
                reachEnd = True
        if car.startLocation == startRight and car.trafficLightTurn == straight:
            if car.currentPosition == righttoLeftEnd:
                reachEnd = True
        if car.startLocation == startRight and car.trafficLightTurn == turnLeft:
            if car.currentPosition == rightToBottomEnd:
                reachEnd = True
        return reachEnd

    def trafficLightsSim(self):
        while True:
            for trafficLight in trafficConfigs:
                self.currentTraffic = trafficLight
                trafficHistory.append([self.env.now,trafficLight.lightForLeftStraight, trafficLight.lightForLeftTurnRight, \
                                        trafficLight.lightForRightStraight, trafficLight.lightForRightTurnRight, \
                                        trafficLight.lightForUpStraight, trafficLight.lightForUpTurnRigt, \
                                        trafficLight.lightForBottomStraight, trafficLight.lightForBottomTurnRight])
                for car in self.cars:
                    car.add_traffic(self.env.now, trafficLight)
                #e.g., left stright traffic, cells at intersection need some break events
                if trafficLight == configLeftRightStraight:
                    print(f' traffic light start operating of {trafficLight} at {self.env.now}')
                    self.leftRightSignal.succeed()
                    self.leftRightSignal = simpy.Event(self.env)
                    # x = 14,15 y = 8 to 11 are blocked
                    # block turn right from left
                    xSet = [13]
                    ySet = [8,9,10]
                    blockPs = []
                    leftTurnRightBlock = self.env.process(self.createBlockProcess(blockPs, trafficLight, xSet, ySet))
                    # block turn right from right
                    xSet = [14]
                    ySet = [11,10,9]
                    blockPs = []
                    rightTurnRightBlock = self.env.process(self.createBlockProcess(blockPs, trafficLight, xSet, ySet))
                    all = [leftTurnRightBlock, rightTurnRightBlock]
                    yield self.env.all_of(all)
                    print(f' traffic light finish operating of {trafficLight} at {self.env.now}')

                if trafficLight == configLeftTurnRight:
                    print(f' traffic light start operating of {trafficLight} at {self.env.now}')
                    self.leftToBottomSingal.succeed()
                    self.leftToBottomSingal: simpy.Event = simpy.Event(self.env)
                    xSet = [12]
                    ySet = [8,9,10,11]
                    blockPs = []
                    r = self.env.process(self.createBlockProcess(blockPs, trafficLight, xSet, ySet))
                    yield r
                    print(f' traffic light finish operating of {trafficLight} at {self.env.now}')
                if trafficLight == configUpTurnRight:
                    print(f' traffic light start operating of {trafficLight} at {self.env.now}')
                    self.upToLeftSignal.succeed()
                    self.upToLeftSignal: simpy.Event = simpy.Event(self.env)
                    xSet = [12,13,14,15]
                    ySet = [11]
                    blockPs = []
                    r = self.env.process(self.createBlockProcess(blockPs, trafficLight, xSet, ySet))
                    yield r
                    print(f' traffic light finish operating of {trafficLight} at {self.env.now}')
                if trafficLight == configUpBottomStraight:
                    print(f' traffic light start operating of {trafficLight} at {self.env.now}')
                    self.upBottomStraightSignal.succeed()
                    self.upBottomStraightSignal: simpy.Event = simpy.Event(self.env)
                    xSet = [12,13,14,15]
                    ySet = [10]
                    blockPs = []
                    upTurnRightBlock = self.env.process(self.createBlockProcess(blockPs, trafficLight, xSet, ySet))

                    xSet = [12,13,14,15]
                    ySet = [9]
                    blockPs = []
                    bottomTurnRightBlocks = self.env.process(self.createBlockProcess(blockPs, trafficLight, xSet, ySet))
                    all = [upTurnRightBlock, bottomTurnRightBlocks]
                    yield self.env.all_of(all)
                    print(f' traffic light finish operating of {trafficLight} at {self.env.now}')
                if trafficLight == configBottomTurnRight:
                    print(f' traffic light start operating of {trafficLight} at {self.env.now}')
                    self.bottomToRightSignal.succeed()
                    self.bottomToRightSignal: simpy.Event = simpy.Event(self.env)
                    xSet = [12,13,14,15]
                    ySet = [8]
                    blockPs = []
                    r = self.env.process(self.createBlockProcess(blockPs, trafficLight, xSet, ySet))
                    yield r
                    print(f' traffic light finish operating of {trafficLight} at {self.env.now}')

                if trafficLight == configRightTurnRight:
                    print(f' traffic light start operating of {trafficLight} at {self.env.now}')
                    self.rightToUpSignal.succeed()
                    self.rightToUpSignal: simpy.Event = simpy.Event(self.env)
                    xSet = [15]
                    ySet = [11,10,9,8]
                    blockPs = []
                    r = self.env.process(self.createBlockProcess(blockPs, trafficLight, xSet, ySet))
                    yield r
                    print(f' traffic light finish operating of {trafficLight} at {self.env.now}')

    def createBlockProcess(self, blockPs, trafficLight, xSet, ySet):
        for x in xSet:
            for y in ySet:
                key = (x, y)
                blockP = self.env.process(self.blockTrafficLight(key))
                blockPs.append(blockP)

        yield self.env.all_of(blockPs)


    def blockTrafficLight(self, key):
        with self.res[key].request(priority=-4, event=BreakEvent(worker_id=0)) as req:
            yield req
            yield self.env.timeout(trafficInterval)


car0 = Car(id=0, startLocation=startLeft, startPostion=startLeftPosition, trafficLightTurn=turnLeft)



car1 = Car(id=1, startLocation=startLeft, startPostion=startLeftPosition, trafficLightTurn=straight)

car2 = Car(id=2, startLocation=startUp, startPostion=startUpPosition, trafficLightTurn=turnRight)
print('up turn right', car2.startPostion)


car3 = Car(id=3, startLocation=startDown, startPostion=startDownPosition, trafficLightTurn=turnLeft)


mapping = {startUp: startUpPosition, startDown: startDownPosition, startLeft: startLeftPosition, startRight: startRightPosition}
cars = []
for i in range(40):
    x = random.choices([startUp, startDown, startLeft, startRight], [1,1,1,1], k=1)[0]
    y = random.choices([straight, turnLeft, turnRight], [1,1,1], k =1)[0]
    car = Car(id=i, startLocation=x, startPostion=mapping[x], trafficLightTurn=y)
    cars.append(car)
#cars = [car3]
trafficSim =  TrafficSimulation()
trafficSim.load_cars(cars=cars)
trafficSim.runSim()

for i in range(len(cars)):
    cars[i].getHistory().to_csv(f'{i}_history.csv',index=False)


trafficHistoryByTimeStep = []
for v in trafficHistory:
    newTime = v[0]
    for l in range(trafficInterval):
        newV = [newTime]
        newV.extend(v[1:])
        newTime+=1
        trafficHistoryByTimeStep.append(newV)
print(trafficHistoryByTimeStep)
trafficHistoryByTimeStepLog = pandas.DataFrame(trafficHistoryByTimeStep,
                              columns=['time', 'lightForLeftStraight',
                                       'lightForLeftTurnRight', 'lightForRightStraight',
                                       'lightForRightTurnRight',
                                       'lightForUpStraight', 'lightForUpTurnRigt', 'lightForBottomStraight',
                                       'lightForBottomTurnRight'])
trafficHistoryByTimeStepLog.to_csv('traffic.csv', index=False)