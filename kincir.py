import pygame
import math

# Inisialisasi pygame
pygame.init()

# Dimensi kanvas
WIDTH, HEIGHT = 720, 720
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 50  # Radius kincir kecil
HANDLE_LENGTH = 50  # Panjang pegangan pendek

# Warna
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 223, 0)

# Buat layar
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kincir Kecil dengan Pegangan")

# Fungsi menggambar baling-baling kincir
def draw_kincir(center, radius, angle):
    num_blades = 4  # Jumlah baling-baling
    blade_angle = 360 / num_blades

    for i in range(num_blades):
        current_angle = math.radians(angle + i * blade_angle)
        x = center[0] + radius * math.cos(current_angle)
        y = center[1] + radius * math.sin(current_angle)
        pygame.draw.polygon(screen, YELLOW, [
            center,
            (x, y),
            (
                center[0] + (radius / 2) * math.cos(current_angle + math.pi / 8),
                center[1] + (radius / 2) * math.sin(current_angle + math.pi / 8),
            ),
        ])

# Fungsi menggambar pegangan
def draw_handle(center, length):
    handle_end = (center[0], center[1] + length)
    pygame.draw.line(screen, WHITE, center, handle_end, 3)
    pygame.draw.circle(screen, WHITE, handle_end, 5)

# Loop utama
running = True
clock = pygame.time.Clock()
angle = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gambar latar belakang
    screen.fill(BLACK)

    # Gambar kincir
    draw_kincir(CENTER, RADIUS, angle)

    # Gambar pegangan
    draw_handle(CENTER, HANDLE_LENGTH)

    # Update layar
    pygame.display.flip()

    # Update sudut rotasi
    angle += 2
    if angle >= 360:
        angle -= 360

    clock.tick(60)

pygame.quit()
