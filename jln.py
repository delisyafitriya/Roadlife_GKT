import numpy as np
import matplotlib.pyplot as plt

# Koordinat jalan (trapezoid)
x_coords = np.array([-15, -180, 180, 15])  # Koordinat x: puncak dan dasar jalan
y_coords = np.array([-360, 360, 360, -360])  # Koordinat y: atas dan bawah

# Plot jalan menggunakan matplotlib
plt.figure(figsize=(6, 6))
plt.plot(x_coords, y_coords, color='black')  # Garis jalan
plt.fill(x_coords, y_coords, color='black')  # Isi warna jalan

# Tambahkan detail kanvas
plt.xlim(-360, 360)  # Batas sumbu X
plt.ylim(360, -360)  # Batas sumbu Y (dibalik agar sesuai koordinat)
plt.gca().set_aspect('equal', adjustable='box')  # Proporsi grid sama
plt.title("Visualisasi Jalan")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Menampilkan garis sumbu tengah untuk referensi
plt.axhline(0, color='gray', linestyle='--')  # Garis horizontal (Y=0)
plt.axvline(0, color='gray', linestyle='--')  # Garis vertikal (X=0)

# Tampilkan plot
plt.show()
