# Script para mostrar el histograma de una imagen a color
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Cambia el nombre de la imagen si es necesario
img = cv2.imread('./ejercicio6/fig_00.jpg')
if img is None:
	raise FileNotFoundError('No se encontró la imagen fig_00.jpg')

# Mostrar la imagen
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Imagen original')
plt.axis('off')

# Calcular y graficar el histograma de cada canal y encontrar la tonalidad más repetida
plt.subplot(1,2,2)
colores = ('b','g','r')
max_tonos = []
for i, color in enumerate(colores):
	hist = cv2.calcHist([img],[i],None,[256],[0,256])
	plt.plot(hist, color=color)
	tono_max = np.argmax(hist)
	max_tonos.append(tono_max)
plt.title('Histograma RGB')
plt.xlabel('Valores Pixeles')
plt.ylabel('Cantidad')
plt.xlim([0,256])
plt.tight_layout()
plt.show()

print(f"Tonalidad más repetida en R: {max_tonos[2]}")
print(f"Tonalidad más repetida en G: {max_tonos[1]}")
print(f"Tonalidad más repetida en B: {max_tonos[0]}")

# Convertir la imagen a escala de grises y mostrar su histograma
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.imshow(img_gray, cmap='gray')
plt.title('Imagen en Gris')
plt.axis('off')

plt.subplot(1,2,2)
hist_gray = cv2.calcHist([img_gray],[0],None,[256],[0,256])
plt.plot(hist_gray, color='k')
plt.title('Histograma Gris')
plt.xlabel('Valor Pixel')
plt.ylabel('Cantidad')
plt.xlim([0,256])
plt.tight_layout()
plt.show()

tono_max_gray = np.argmax(hist_gray)
print(f"Tonalidad más repetida en la imagen gris: {tono_max_gray}")

print("\nConclusiones:")
print("- El histograma RGB muestra la distribución de intensidades para cada canal de color.")
print("- El histograma en escala de grises resume la información de todos los canales en una sola curva.")
print("- La tonalidad más repetida indica el valor de pixel dominante en cada plano, lo que puede asociarse a la iluminación o color predominante de la imagen.")
