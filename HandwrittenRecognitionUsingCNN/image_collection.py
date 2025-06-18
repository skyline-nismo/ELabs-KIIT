import pyscreenshot as imagegrab
import time

# Screen Capture
images_folder = "captured_images/9/" # Run it by 10 times by changing the number from 0 to 9
for i in range(0,100):
    time.sleep(4.5)
    image = imagegrab.grab(bbox=(100, 300, 950, 1000)) # x1, y1, x2, y2
    print("Saved Image number", i)
    image.save(images_folder + str(i) + '.png')
    print("Clear the screen and then redraw")
    