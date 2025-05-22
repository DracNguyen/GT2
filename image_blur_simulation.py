import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def Li(x, y):
    """Hàm cường độ sáng Li(x,y)"""
    return 50 + 20*x - 10*y

def cos_theta(x, y):
    """Hàm cos θ(x,y)"""
    return 1/np.sqrt(2) * (1 + (x-y)/2)

def intensity_function(x, y):
    """Hàm cường độ I(x,y) = 100 + 30sin(πx)cos(πy)"""
    return 100 + 30 * np.sin(np.pi * x) * np.cos(np.pi * y)

def calculate_average_intensity():
    """Tính giá trị trung bình của cường độ sáng"""
    # Tích phân kép của hàm cường độ
    result, error = integrate.dblquad(
        lambda y, x: intensity_function(x, y),
        0, 1,  # giới hạn x
        lambda x: 0, lambda x: 1  # giới hạn y
    )
    return result

def visualize_intensity():
    """Hiển thị đồ thị 3D của hàm cường độ"""
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)
    Z = intensity_function(X, Y)

    fig = plt.figure(figsize=(12, 5))
    
    # Đồ thị 3D
    ax1 = fig.add_subplot(121, projection='3d')
    surf = ax1.plot_surface(X, Y, Z, cmap='viridis')
    ax1.set_title('Hàm cường độ I(x,y)')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_zlabel('I(x,y)')
    fig.colorbar(surf, ax=ax1)

    # Đồ thị contour
    ax2 = fig.add_subplot(122)
    contour = ax2.contourf(X, Y, Z, levels=20, cmap='viridis')
    ax2.set_title('Đường đồng mức của I(x,y)')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    fig.colorbar(contour, ax=ax2)

    plt.tight_layout()
    plt.show()

def main():
    # Tính giá trị trung bình
    avg_intensity = calculate_average_intensity()
    print(f"Giá trị trung bình của cường độ sáng: {avg_intensity:.2f}")
    
    # Hiển thị đồ thị
    visualize_intensity()

    # Tạo một ảnh mẫu và áp dụng làm mờ
    # Tạo ảnh nhiễu
    noisy_image = np.random.normal(100, 20, (100, 100))
    
    # Áp dụng bộ lọc trung bình (làm mờ)
    kernel_size = 5
    blurred_image = np.zeros_like(noisy_image)
    for i in range(kernel_size//2, noisy_image.shape[0]-kernel_size//2):
        for j in range(kernel_size//2, noisy_image.shape[1]-kernel_size//2):
            blurred_image[i,j] = np.mean(noisy_image[i-kernel_size//2:i+kernel_size//2+1,
                                                    j-kernel_size//2:j+kernel_size//2+1])

    # Hiển thị ảnh gốc và ảnh đã làm mờ
    plt.figure(figsize=(12, 5))
    plt.subplot(121)
    plt.imshow(noisy_image, cmap='gray')
    plt.title('Ảnh nhiễu')
    plt.colorbar()

    plt.subplot(122)
    plt.imshow(blurred_image, cmap='gray')
    plt.title('Ảnh sau khi làm mờ')
    plt.colorbar()
    plt.show()

if __name__ == "__main__":
    main() 