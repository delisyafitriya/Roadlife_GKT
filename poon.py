import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menggambar segitiga (daun) terbalik
def draw_inverted_triangle(center_x, center_y, width, height, color='green'):
    half_width = width / 2
    x_coords = [center_x, center_x - half_width, center_x + half_width, center_x]  # X koordinat
    y_coords = [center_y, center_y + height, center_y + height, center_y]  # Y koordinat dibalik
    plt.fill(x_coords, y_coords, color=color)

# Fungsi untuk menggambar persegi (batang)
def draw_rectangle(bottom_left_x, bottom_left_y, width, height, color='brown'):
    x_coords = [bottom_left_x, bottom_left_x + width, bottom_left_x + width, bottom_left_x, bottom_left_x]
    y_coords = [bottom_left_y, bottom_left_y, bottom_left_y + height, bottom_left_y + height, bottom_left_y]
    plt.fill(x_coords, y_coords, color=color)

# Ukuran kanvas
plt.figure(figsize=(7.2, 7.2))  # Sesuai kanvas 720x720

# Koordinat untuk batang (persegi) dan daun (segitiga terbalik)
# Batang pohon
draw_rectangle(-30, 50, 60, 120, color='brown')  # Persegi batang di tengah bawah

# Daun pohon (Segitiga terbalik bertumpuk dengan jarak lebih rapat)
draw_inverted_triangle(0, -30, 180, 100, color='green')  # Segitiga daun pertama
draw_inverted_triangle(0, -90, 150, 100, color='green')  # Segitiga daun kedua (lebih rapat)
draw_inverted_triangle(0, -150, 120, 100, color='green')  # Segitiga daun ketiga (lebih rapat)

# Tambahkan detail kanvas
plt.xlim(-360, 360)  # Batas sumbu X
plt.ylim(360, -360)  # Batas sumbu Y (dibalik agar sesuai koordinat)
plt.gca().set_aspect('equal', adjustable='box')  # Proporsi grid sama
plt.title("Pohon dengan Segitiga Terbalik Rapat (Daun) dan Persegi (Batang)")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Garis sumbu untuk referensi
plt.axhline(0, color='gray', linestyle='--')  # Garis horizontal
plt.axvline(0, color='gray', linestyle='--')  # Garis vertikal

# Tampilkan plot
plt.show()
