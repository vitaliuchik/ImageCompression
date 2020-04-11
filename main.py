from src.image import Image
import sys


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Argument error')

    img = Image(sys.argv[1])
    size = len(img.data) // 2
    img.data = img.data[:size, :size]
    img.save('img/penguin128.png')
