import numpy as np
from PIL import Image as Img


class Image:

    def __init__(self, path):
        self.path = './' + path
        self.data = self._decode()

    def _decode(self):
        img = Img.open(self.path)
        return np.asarray(img)

    def save(self, path):
        Img.fromarray(self.data).save('./' + path)
