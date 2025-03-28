import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Thiết lập dữ liệu
x = np.linspace(0, 1, 50)
y = np.linspace(0, 1, 50)
X, Y = np.meshgrid(x, y)
Z = 4 - X**2 - Y**2  # Bề mặt trên

# Tạo figure và axes 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Vẽ bề mặt trên (z = 4 - x^2 - y^2)
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7, edgecolor='none')

# Vẽ mặt đáy (z = 0)
Z_bottom = np.zeros_like(X)
ax.plot_surface(X, Y, Z_bottom, color='gray', alpha=0.5)

# Vẽ các mặt bên
# Mặt bên tại x = 0 và x = 1
for x_val in [0, 1]:
    X_side = np.full_like(X, x_val)
    Z_side = 4 - X_side**2 - Y**2
    ax.plot_surface(X_side, Y, Z_side, color='yellow', alpha=0.2)

# Mặt bên tại y = 0 và y = 1
for y_val in [0, 1]:
    Y_side = np.full_like(Y, y_val)
    Z_side = 4 - X**2 - Y_side**2
    ax.plot_surface(X, Y_side, Z_side, color='yellow', alpha=0.2)

# Điền các lát cắt dọc để tạo cảm giác khối rắn
# Lát cắt theo hướng x (tại các giá trị y cố định)
for y_val in np.linspace(0, 1, 20):
    x_side = x
    y_side = np.full_like(x, y_val)
    X_side, Y_side = np.meshgrid(x_side, [y_val])
    Z_side = 4 - X_side**2 - Y_side**2
    # Tạo lưới Z từ 0 đến Z_side
    Z_vals = np.linspace(0, Z_side, 50)
    X_vals, Z_vals = np.meshgrid(x_side, np.linspace(0, 1, 50))
    Y_vals = np.full_like(X_vals, y_val)
    ax.plot_surface(X_vals, Y_vals, Z_vals * Z_side, color='yellow', alpha=0.05)

# Lát cắt theo hướng y (tại các giá trị x cố định)
for x_val in np.linspace(0, 1, 20):
    y_side = y
    x_side = np.full_like(y, x_val)
    X_side, Y_side = np.meshgrid([x_val], y_side)
    Z_side = 4 - X_side**2 - Y_side**2
    # Tạo lưới Z từ 0 đến Z_side
    Z_vals = np.linspace(0, Z_side, 50)
    Y_vals, Z_vals = np.meshgrid(y_side, np.linspace(0, 1, 50))
    X_vals = np.full_like(Y_vals, x_val)
    ax.plot_surface(X_vals, Y_vals, Z_vals * Z_side, color='blue', alpha=0.1)

# Đặt nhãn và tiêu đề
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Khối thể tích dưới bề mặt z = 4 - x² - y² trên [0, 1] × [0, 1]')

# Đặt giới hạn trục
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 4)

# Hiển thị biểu đồ
plt.show()