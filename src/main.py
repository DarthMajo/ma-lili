#ma lili - Welcome to my world generator
from lang import toki
from world import worldGen

#MAIN======================================================================MAIN
def main():
    wg = worldGen.WorldGen(7, 7)
    print(wg.generateTemperatureMap())

if __name__ == "__main__":
    main()