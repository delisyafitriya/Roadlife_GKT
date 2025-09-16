import matplotlib.pyplot as plt
import numpy as np

def draw_stickman():
    fig, ax = plt.subplots()

    # 1. Kepala (lingkaran)
    head_center = (0, 180)  # Pusat kepala
    head_radius = 60        # Radius kepala
    head = plt.Circle(head_center, head_radius, color='black', fill=True)
    ax.add_patch(head)

    # 2. Tubuh (garis lurus ke bawah)
    body_x = [0, 0]
    body_y = [120, -60]
    ax.plot(body_x, body_y, color='black', linewidth=15)

    # 3. Tangan (dua garis miring)
    # Tangan kiri
    left_arm_x = [0, -100]
    left_arm_y = [100, 40]
    ax.plot(left_arm_x, left_arm_y, color='black', linewidth=15)

    # Tangan kanan
    right_arm_x = [0, 100]
    right_arm_y = [100, 40]
    ax.plot(right_arm_x, right_arm_y, color='black', linewidth=15)

    # 4. Kaki (dua garis miring ke bawah)
    # Kaki kiri
    left_leg_x = [0, -80]
    left_leg_y = [-60, -200]
    ax.plot(left_leg_x, left_leg_y, color='black', linewidth=15)

    # Kaki kanan
    right_leg_x = [0, 80]
    right_leg_y = [-60, -200]
    ax.plot(right_leg_x, right_leg_y, color='black', linewidth=15)

    # Set properti plot
    ax.set_xlim(-360, 360)
    ax.set_ylim(-360, 360)
    ax.set_aspect('equal')  # Skala sama
    plt.axhline(0, color='gray', linestyle='--')  # Garis horizontal pusat
    plt.axvline(0, color='gray', linestyle='--')  # Garis vertikal pusat
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.title("Stickman Coordinate System")

    plt.show()

# Jalankan fungsi untuk menggambar stickman
draw_stickman()