#https://en.wikipedia.org/wiki/Biome#/media/File:Lifezones_Pengo.svg
import math

class World:
    def __init__(self, x, y):
        """Constructor for the World class.

        Parameters:
            x (int): The width of the world in kilometers
            y (int): The height of the world in kilometers
        """
        self.x = x
        self.y = y

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

    def __generateRainfallMap(self):
        pass

    def generateTemperatureMap(self):
        """Private method for generating temperature on the planet.
        
        Returns:
            A 2-D array of doubles representing temperature (Celcius).
        """
        #This uses the sin function to make a mirror image of temperature from north to south poles
        tempMap = [[(self.TEMPERATURE_EQUATOR - self.TEMPERATURE_POLAR) * math.sin(((0.5 / int(self.y / 2)) * i) * math.pi) + self.TEMPERATURE_POLAR] * self.y for i in range(self.x)]
        return tempMap
