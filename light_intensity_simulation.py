import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def Li(x, y):
    """Hàm cường độ sáng tới Li(x,y) = 50 + 20x - 10y"""
    return 50 + 20*x - 10*y

def cos_theta(x, y):
    """Hàm cos θ(x,y) = 1/√2 * (1 + (x-y)/2)"""
    return 1/np.sqrt(2) * (1 + (x-y)/2)

def integrand(x, y):
    """Hàm tích phân: Li(x,y) * cos θ(x,y)"""
    return Li(x, y) * cos_theta(x, y)

def calculate_total_intensity():
    """Tính tổng cường độ ánh sáng phản xạ"""
    # Tích phân kép với giới hạn x ∈ [0, 2], y ∈ [0, 1]
    result, error = integrate.dblquad(
        lambda y, x: integrand(x, y),
        0, 2,  # giới hạn x
        lambda x: 0, lambda x: 1  # giới hạn y
    )
    return result, error

def visualize_intensity():
    """Hiển thị đồ thị 3D của hàm cường độ ánh sáng"""
    x = np.linspace(0, 2, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)
    Z = integrand(X, Y)

    fig = plt.figure(figsize=(15, 5))
    
    # Đồ thị 3D của hàm tích phân
    ax1 = fig.add_subplot(131, projection='3d')
    surf = ax1.plot_surface(X, Y, Z, cmap='viridis')
    ax1.set_title('Hàm tích phân Li(x,y) * cos θ(x,y)')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_zlabel('Cường độ')
    fig.colorbar(surf, ax=ax1)

    # Đồ thị contour của hàm tích phân
    ax2 = fig.add_subplot(132)
    contour = ax2.contourf(X, Y, Z, levels=20, cmap='viridis')
    ax2.set_title('Đường đồng mức của hàm tích phân')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    fig.colorbar(contour, ax=ax2)

    # Đồ thị 3D của hàm Li(x,y)
    ax3 = fig.add_subplot(133, projection='3d')
    surf3 = ax3.plot_surface(X, Y, Li(X, Y), cmap='plasma')
    ax3.set_title('Hàm cường độ sáng tới Li(x,y)')
    ax3.set_xlabel('x')
    ax3.set_ylabel('y')
    ax3.set_zlabel('Cường độ')
    fig.colorbar(surf3, ax=ax3)

    plt.tight_layout()
    plt.show()

def main():
    # Tính tổng cường độ ánh sáng
    total_intensity, error = calculate_total_intensity()
    print(f"Tổng cường độ ánh sáng phản xạ: {total_intensity:.2f} ± {error:.2e} (đơn vị ánh sáng)")
    
    # Hiển thị đồ thị
    visualize_intensity()

    # Tạo một ví dụ về phản xạ ánh sáng trên bề mặt
    x = np.linspace(0, 2, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)
    
    # Tính vector pháp tuyến dựa trên cos θ
    normal_x = np.cos(np.arccos(cos_theta(X, Y)))
    normal_y = np.sin(np.arccos(cos_theta(X, Y)))
    
    # Vẽ vector pháp tuyến
    plt.figure(figsize=(10, 5))
    plt.quiver(X[::10, ::10], Y[::10, ::10], 
               normal_x[::10, ::10], normal_y[::10, ::10],
               scale=50)
    plt.title('Vector pháp tuyến của bề mặt')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main() 