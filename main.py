import matplotlib.pyplot as plt
import numpy as np

#Random 1D Images 
image_data = np.random.random((10, 10))

def on_mouse_move(event):
    if event.inaxes:  # Check your mouse position
        x, y = int(event.xdata), int(event.ydata) 
        # Get pixel value in your image
        pixel_value = image_data[y, x]
        print(f'Tọa độ: ({x}, {y}), Giá trị điểm ảnh: {pixel_value}')

# Show
fig, ax = plt.subplots()
ax.imshow(image_data, cmap='gray')

# Conect with on_mouse_move
fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)

plt.show()
