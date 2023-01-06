#ma lili - Welcome to my world generator
from lang import toki
from world import worldGen

#MAIN======================================================================MAIN
def main():
    wg = worldGen.WorldGen(7, 7)
    world = worldGen.World(7, 7, wg.GenerateWorld())
    world.Display()

if __name__ == "__main__":
    main()