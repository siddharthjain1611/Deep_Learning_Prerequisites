# Image is just a matrix of numbers
# each value is the intensity of that pixel at that position in the image

import pandas as pd
import matplotlib.pyplot as plt

# load the data

df = pd.read_csv('train.csv')

# check the shape of the frame to know what size is it

print(df.shape) # 42000 samples in 785 columns

# turn it into a matrix

M = df.as_matrix()

# now we select zero row and all the columns except 0, cause it's not pixel

im = M[0,1:]

# now we will reshape it

im = im.reshape(28, 28)

# now let's see the image

plt.imshow(im)
# plt.imshow(im, cmap = 'grey') - too se it's in black & white
plt.show()
