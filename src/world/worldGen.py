#Contains the world and the generator for the world
import math
import random

class World:
    def __init__(self, x, y, tilemap):
        """Constructor for the World class.

        Parameters:
            x (int): The width of the world in kilometers
            y (int): The height of the world in kilometers
            tileMap (list[list[WorldTile]]): The world itself
        """
        self.x = x
        self.y = y
        self.tilemap = tilemap

    def Display(self):
        stringBuilder = ""
        for y in range(0, self.y):
            for x in range(0, self.x):
                stringBuilder += self.tilemap[x][y].GetChar()
            stringBuilder += "\n"
        print(stringBuilder)

class WorldTile:
    def __init__(self, elevation, rainfall, temperature):
        """Constructor for the WorldTile class.
        
        Parameters:
            elevation (int): The elevation of this tile in meters.
            rainfall (int): The avg. rainfall of this tile in mm.
            temperature (double): The avg. temperature of this tile (in C).
        """
        self.elevation = elevation
        self.rainfall = rainfall
        self.temperature = temperature

    def GetChar(self):
        """Returns a character of how we can visually see this tile.
        
        Returns:
            A char
        """
        if(self.elevation <= 0):
            return '~'
        elif(self.elevation >= 2500):
            return '^'
        elif(self.elevation < 2500 and self.elevation > 1666):
            return '\''
        elif(self.elevation <= 1666 and self.elevation > 834):
            return ','
        else:
            return '.'

class WorldGen:
    def __init__(self, x, y):
        """Constructor for the WorldGen class.

        Parameters:
            x (int): The width of the world in kilometers
            y (int): The height of the world in kilometers
        """
        self.x = x
        self.y = y
        self.TEMPERATURE_POLAR = -20.0
        self.TEMPERATURE_EQUATOR = 32.0

    def GenerateWorld(self):
        """It's generating time!!!
        
        Returns:
            The world that ma lili sits on
        """
        #Generate the parameters of the world
        eleMap = self.generateElevationMap()
        rainMap = self.generateRainfallMap()
        tempMap = self.generateTemperatureMap()

        #Turn data arrays into tiles
        world = [[WorldTile] * self.y for _ in range(self.x)]
        for y in range(0, self.y):
            for x in range(0, self.x):
                world[x][y] = WorldTile(eleMap[x][y], rainMap[x][y], tempMap[x][y])
        return world


    def generateElevationMap(self):
        """Private method for generating elevation on the planet.
        
        Returns:
            A 2-D array of ints representing altitude in meters above sea level.
        """
        #TODO: This should be improved in the future
        eleMap = [[0] * self.y for _ in range(self.x)]
        for y in range(0, self.y):
            for x in range(0, self.x):
                eleMap[x][y] = random.randint(-10971, 8849)
        return eleMap

    def generateRainfallMap(self):
        """Private method for generating rainfall on the planet.
        
        Returns:
            A 2-D array of ints representing millimeters of rainfall.
        """
        #TODO: This should be improved in the future
        rainMap = [[0] * self.y for _ in range(self.x)]
        for y in range(0, self.y):
            for x in range(0, self.x):
                rainMap[x][y] = random.randint(0, 16000)
        return rainMap

    def generateTemperatureMap(self):
        """Private method for generating temperature on the planet.
        
        Returns:
            A 2-D array of doubles representing temperature (Celcius).
        """
        #This uses the sin function to make a mirror image of temperature from north to south poles
        tempMap = [[(self.TEMPERATURE_EQUATOR - self.TEMPERATURE_POLAR) * math.sin(((0.5 / int(self.y / 2)) * i) * math.pi) + self.TEMPERATURE_POLAR] * self.y for i in range(self.x)]
        return tempMap

#NOTES====================================================================NOTES
#https://en.wikipedia.org/wiki/Biome#/media/File:Lifezones_Pengo.svg