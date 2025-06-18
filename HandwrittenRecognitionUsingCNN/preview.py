import dataset_loading as dl
import matplotlib.pyplot as plt

# Preview of one image using matplotlib
idx = int('007') # Taking an example
img = dl.X_Axis.loc[idx].values.reshape(28, 28)
print(dl.Y_Axis[idx])
plt.imshow(img, cmap='gray')  # It will specify grayscale for better display
plt.show()