# Script para colorear la imagen sea.jpg en azul
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Leer la imagen en escala de grises
img_gray = cv2.imread('./ejercicio7/sea.jpg', cv2.IMREAD_GRAYSCALE)
if img_gray is None:
	raise FileNotFoundError('No se encontró el archivo sea.jpg')


# Crear una imagen en color (azul claro/celeste)
# Sumar un valor al canal azul y dar un leve tinte verde para aclarar
img_color = np.zeros((img_gray.shape[0], img_gray.shape[1], 3), dtype=np.uint8)
azul_claro = cv2.add(img_gray, 100)  # Suma 100 para aclarar (máx 255)
img_color[:, :, 0] = azul_claro      # Canal azul
img_color[:, :, 1] = (img_gray * 0.3).astype(np.uint8)  # Un poco de verde para celeste
img_color[:, :, 2] = 0               # Canal rojo

# Guardar la imagen coloreada
cv2.imwrite('./ejercicio7/sea_colorized.jpg', img_color)

# Mostrar ambas imágenes
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.title('Original en Gris')
plt.imshow(img_gray, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title('Coloreada Azul')
plt.imshow(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.tight_layout()
plt.show()
