import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

# Thiết lập dữ liệu
x = np.linspace(0, 1, 50)
y = np.linspace(0, 1, 50)
X, Y = np.meshgrid(x, y)
Z = 4 - X**2 - Y**2

# Tạo figure và axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Vẽ bề mặt
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Hàm khởi tạo animation
def init():
    return surf,

# Hàm cập nhật animation: mô phỏng quá trình tích phân
def animate(i):
    ax.clear()
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    # Vẽ các lát cắt dọc theo x
    x_slice = np.linspace(0, i/50, 50)
    X_slice, Y_slice = np.meshgrid(x_slice, y)
    Z_slice = 4 - X_slice**2 - Y_slice**2
    ax.plot_surface(X_slice, Y_slice, Z_slice, color='red', alpha=0.5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Tích phân hai lớp: Quét diện tích bề mặt z = 4 - x² - y²')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 4)
    return surf,

# Tạo animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=50, interval=100, blit=False)

ani.save('double_integral_1.gif', writer='pillow', fps=15)


# Hàm khởi tạo animation
# def init2():
#     # Vẽ toàn bộ bề mặt trên (z = 4 - x^2 - y^2)
#     ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7, edgecolor='none')
#     # Vẽ mặt đáy (z = 0)
#     Z_bottom = np.zeros_like(X)
#     ax.plot_surface(X, Y, Z_bottom, color='gray', alpha=0.5)
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Z')
#     ax.set_title('Tích phân hai lớp: Quét khối thể tích z = 4 - x² - y²')
#     ax.set_xlim(0, 1)
#     ax.set_ylim(0, 1)
#     ax.set_zlim(0, 4)
#     return ax,

# # Hàm cập nhật animation: quét từng lát cắt của khối thể tích
# def animate2(i):
#     ax.clear()
    
#     # Vẽ toàn bộ bề mặt trên (z = 4 - x^2 - y^2)
#     ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7, edgecolor='none')
    
#     # Vẽ mặt đáy (z = 0)
#     Z_bottom = np.zeros_like(X)
#     ax.plot_surface(X, Y, Z_bottom, color='gray', alpha=0.5)
    
#     # Quét khối thể tích theo x
#     x_slice = np.linspace(0, i/50, 50)  # Quét từ x = 0 đến x = i/50
#     X_slice, Y_slice = np.meshgrid(x_slice, y)
#     Z_slice = 4 - X_slice**2 - Y_slice**2
    
#     # Vẽ bề mặt trên của lát cắt
#     ax.plot_surface(X_slice, Y_slice, Z_slice, color='red', alpha=0.5)
    
#     # Vẽ mặt đáy của lát cắt
#     Z_bottom_slice = np.zeros_like(X_slice)
#     ax.plot_surface(X_slice, Y_slice, Z_bottom_slice, color='gray', alpha=0.5)
    
#     # Vẽ các mặt bên của lát cắt
#     # Mặt bên tại x = i/50 (mặt quét)
#     x_val = i/50
#     y_side = y
#     x_side = np.full_like(y, x_val)
#     X_side, Y_side = np.meshgrid([x_val], y_side)
#     Z_side = 4 - X_side**2 - Y_side**2
#     Z_vals = np.linspace(0, Z_side, 50)
#     Y_vals, Z_vals = np.meshgrid(y_side, np.linspace(0, 1, 50))
#     X_vals = np.full_like(Y_vals, x_val)
#     ax.plot_surface(X_vals, Y_vals, Z_vals * Z_side, color='blue', alpha=0.3)
    
#     # Mặt bên tại y = 0 và y = 1 cho lát cắt
#     for y_val in [0, 1]:
#         x_side = x_slice
#         y_side = np.full_like(x_slice, y_val)
#         X_side, Y_side = np.meshgrid(x_side, [y_val])
#         Z_side = 4 - X_side**2 - Y_side**2
#         Z_vals = np.linspace(0, Z_side, 50)
#         X_vals, Z_vals = np.meshgrid(x_side, np.linspace(0, 1, 50))
#         Y_vals = np.full_like(X_vals, y_val)
#         ax.plot_surface(X_vals, Y_vals, Z_vals * Z_side, color='blue', alpha=0.3)
    
#     # Đặt lại nhãn và giới hạn
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Z')
#     ax.set_title('Tích phân hai lớp: Quét khối thể tích z = 4 - x² - y²')
#     ax.set_xlim(0, 1)
#     ax.set_ylim(0, 1)
#     ax.set_zlim(0, 4)
#     return ax,

# # Tạo animation
# ani2 = animation.FuncAnimation(fig, animate2, init_func=init2, frames=50, interval=100, blit=False)

# ani2.save('double_integral_2.gif', writer='pillow', fps=15)
