from PIL import Image
import PIL.ImageOps   
from io import BytesIO
import numpy as np
import pandas as pd

def invert(image):
    imagee = PIL.ImageOps.invert(image)
    colourPixels = image.convert("RGB")
    colourArray = np.array(colourPixels.getdata()).reshape(image.size + (3,))
    indicesArray = np.moveaxis(np.indices(image.size), 0, 2)
    allArray = np.dstack((indicesArray, colourArray)).reshape((-1, 5))
    df_result = pd.DataFrame(allArray, columns=["y", "x", "red","green","blue"])
    return imagee,df_result