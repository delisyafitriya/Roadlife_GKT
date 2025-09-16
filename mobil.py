import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menggambar segitiga
def draw_triangle(ax, points, color='black'):
    triangle = plt.Polygon(points, closed=True, color=color)
    ax.add_patch(triangle)

# Fungsi untuk menggambar persegi panjang
def draw_rectangle(ax, x, y, width, height, color='black'):
    rectangle = plt.Rectangle((x, y), width, height, color=color)
    ax.add_patch(rectangle)

# Setup kanvas
fig, ax = plt.subplots()
ax.set_xlim(-360, 360)
ax.set_ylim(-360, 360)
ax.set_aspect('equal')  # Aspek rasio sama

# 1. Atap Mobil (dibalik sumbu Y)
draw_rectangle(ax, -180, 100, 360, 110, color='black')

# 2. Kaca Depan Mobil (kotak putih)
# Kaca depan sedikit lebih rendah dari atap mobil
draw_rectangle(ax, -150, 100, 300, 80, color='white') 

# 2. Badan Mobil (dibalik sumbu Y)
draw_rectangle(ax, -200, -100, 400, 200, color='black')

# 3. Lampu Kiri (ditempatkan di luar grid, sebelah kiri)
draw_rectangle(ax, -180, -50, 50, 40, color='white')  # Lampu kiri di luar grid

# 4. Lampu Kanan (ditempatkan di luar grid, sebelah kanan)
draw_rectangle(ax, 130, -50, 50, 40, color='white')  # Lampu kanan di luar grid

# 5. Roda Kiri (Persegi Panjang)
draw_rectangle(ax, -180, -150, 60, 50, color='black')

# 6. Roda Kanan (Persegi Panjang)
draw_rectangle(ax, 120, -150, 60, 50, color='black')

# 7. Gril Depan (Persegi Panjang Kecil)
draw_rectangle(ax, -50, -80, 100, 30, color='white')

#8. Spion Kiri (Persegi Panjang Kecil)
draw_rectangle(ax, -230, 50, 30, 30, color='black')  # X: -230, Y: 50

# 9. Spion Kanan (Persegi Panjang Kecil)
draw_rectangle(ax, 200, 50, 30, 30, color='black')  # X: 200, Y: 50


# Tambahkan grid dan tampilkan hasil
ax.grid(True)
plt.axhline(0, color='gray', linestyle='--')  # Garis horizontal tengah
plt.axvline(0, color='gray', linestyle='--')  # Garis vertikal tengah
plt.title("Gambar Mobil ")
plt.show()
