import nbtlib as nbt
import base36

import chunk

class Save:
    def __init__(self, world, path = 'save'):
        self.world = world
        self.path = path

    def chunk_position_to_path(self, chunk_position):
        x, y, z = chunk_position

        chunk_path = '/'.join((self.path, 
            base36.dumps(x % 64), base36.dumps(z % 64),
            f'c.{base36.dumps(x)}.{base36.dumps(z)}.dat'))

        return chunk_path
        
    def load_chunk(self, chunk_position):
        chunk_path = self.chunk_position_to_path(chunk_position)

        try:
            chunk_blocks = nbt.load(chunk_path)['Level']['Blocks']

        except FileNotFoundError:
            return

        self.world.chunks[chunk_position] = chunk.Chunk(self.world, chunk_position)
        for x in range(chunk.CHUNK_WIDTH):
            for y in range(chunk.CHUNK_HEIGHT):
                for z in range(chunk.CHUNK_LENGTH):
                    self.world.chunks[chunk_position].blocks[x][y][z] = chunk_blocks[x * chunk.CHUNK_LENGTH * chunk.CHUNK_HEIGHT + z * chunk.CHUNK_HEIGHT + y]




    def load(self):
        for x in range(-4, 4):
            for z in range(-4, 4):
                self.load_chunk((x, 0, z))