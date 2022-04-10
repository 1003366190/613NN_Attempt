from huffman import huffman
import random

img = [random.randint(0,255) for i in range(400)]
total_bits = int(huffman(img))


print('total: ', total_bits)
