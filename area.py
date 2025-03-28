import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Thiết lập dữ liệu
x = np.linspace(0, 1, 50)  # Tạo lưới tọa độ x từ 0 đến 1
y = np.linspace(0, 1, 50)  # Tạo lưới tọa độ y từ 0 đến 1
X, Y = np.meshgrid(x, y)   # Tạo lưới 2D
Z = 4 - X**2 - Y**2        # Tính giá trị z = 4 - x^2 - y^2

# Tạo figure và axes 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Vẽ bề mặt
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, edgecolor='none')

# Thêm lưới dây để dễ hình dung (tuỳ chọn)
# ax.plot_wireframe(X, Y, Z, color='black', alpha=0.2)

# Đặt nhãn cho trục
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Bề mặt z = 4 - x² - y² trên miền [0, 1] × [0, 1]')

# Đặt giới hạn cho các trục
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 4)

# Thêm thanh màu (colorbar) để biểu thị giá trị z
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

# Hiển thị biểu đồ
plt.show()