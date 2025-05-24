import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from matplotlib.animation import FuncAnimation
# Miền quét
x_range = (-2, 2)
y_range = (-2, 2)
num_points = 50
x = np.linspace(x_range[0], x_range[1], num_points)
y = np.linspace(y_range[0], y_range[1], num_points)
X, Y = np.meshgrid(x, y)
Z = 4 - X**2 - Y**2

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Hàm khởi tạo animation
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
def init():
    return surf,

def animate(i):
    ax.clear()
    # Vẽ toàn bộ bề mặt
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    # Vẽ lát cắt dọc theo x
    x_slice = np.linspace(x_range[0], x_range[0] + (x_range[1] - x_range[0]) * i / num_points, num_points)
    X_slice, Y_slice = np.meshgrid(x_slice, y)
    Z_slice = 4 - X_slice**2 - Y_slice**2
    ax.plot_surface(X_slice, Y_slice, Z_slice, color='red', alpha=0.5)
    # # Vẽ mặt đáy
    # Z_bottom = np.zeros_like(X_slice)
    # ax.plot_surface(X_slice, Y_slice, Z_bottom, color='gray', alpha=0.3)
    # Vẽ mặt bên tại x = x_slice.max()
    x_val = x_slice.max()
    y_side = y
    x_side = np.full_like(y, x_val)
    X_side, Y_side = np.meshgrid([x_val], y_side)
    Z_side = 4 - X_side**2 - Y_side**2
    Z_vals = np.linspace(0, 1, 50)
    if Z_side.shape[1] > 0:
        for j in range(Z_side.shape[1]):
            ax.plot([x_val]*50, [y_side[j]]*50, Z_vals*Z_side[0, j], color='blue', alpha=0.3)
    # Đặt lại nhãn và giới hạn
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Tích phân hai lớp: Quét diện tích bề mặt z = 4 - x² - y²')
    ax.set_xlim(x_range)
    ax.set_ylim(y_range)
    ax.set_zlim(-4, 4)
    return surf,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=num_points, interval=40, blit=False)

# Lưu animation ra file GIF
ani.save('surface_scan_animation.gif', writer='pillow', fps=20)

plt.show() 
