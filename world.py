import noise
import random


class World:
    def __init__(self, name, x_dimension, y_dimension, octaves):
        self.name = name
        self.x_dimension = x_dimension
        self.y_dimension = y_dimension
        self.octaves = octaves
        self.seed = random.uniform(-10000, 10000)

    def create_world(self):
        world_file = self.name + ".txt"
        freq = self.octaves*120
        file = open(world_file, "w")

        for i in range(self.y_dimension):
            let_array = []
            for j in range(self.x_dimension):
                height = int(noise.snoise3(i/freq, j/freq, self.seed, self.octaves) * 1000)
                if height < 200:
                    let_array.append('.')
                elif height < 320:
                    let_array.append('#')
                else: 
                    let_array.append('S')
            line = ''.join(map(str,let_array)) + '\n'
            file.write(line)
        file.close()

if __name__=="__main__":
    multi = World("the_multi", 500, 500, 4)
    multi.create_world()

