import matplotlib.pyplot as plt
from PIL import Image
import tkinter.filedialog as fd

import numpy

path = fd.askopenfilename()
imgFile = Image.open(path).convert('L')
imgFile = imgFile.resize((8, 8), Image.Resampling.LANCZOS)
data = numpy.asarray(imgFile, dtype=float)
data = 16 - numpy.floor(17 * data / 256)
data = imgFile
print(data)
plt.imshow(data, cmap='Grays')
plt.show()