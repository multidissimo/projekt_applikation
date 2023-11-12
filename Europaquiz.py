from matplotlib import pyplot as plt
from matplotlib import image as mpimg
 
plt.title("Hauptstädtequiz")
 
image = mpimg.imread("EuropaleereKarte.png")
plt.imshow(image)

ax = plt.gca()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
