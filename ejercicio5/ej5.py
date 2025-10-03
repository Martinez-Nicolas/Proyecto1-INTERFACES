import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carga la imagen (reemplaza el nombre si usas otro archivo)
img = cv2.imread('./ejercicio5/fig_05.jpg')  # Cambia por el nombre de tu archivo

# OpenCV carga en BGR, así que convertimos a RGB para visualización correcta
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Separar los canales
R = img_rgb[:,:,0]
G = img_rgb[:,:,1]
B = img_rgb[:,:,2]

# Calcular área ocupada (pixeles distintos de cero en cada canal)
area_R = np.count_nonzero(R)
area_G = np.count_nonzero(G)
area_B = np.count_nonzero(B)

# Crear imágenes con fondo negro para cada canal
R_img = np.zeros_like(img_rgb)
R_img[:,:,0] = R
G_img = np.zeros_like(img_rgb)
G_img[:,:,1] = G
B_img = np.zeros_like(img_rgb)
B_img[:,:,2] = B

# Visualizar los planos
fig, axs = plt.subplots(1, 4, figsize=(15,5))
axs[0].imshow(img_rgb)
axs[0].set_title('Imagen Original')
axs[1].imshow(R_img)
axs[1].set_title(f'Plano R\nÁrea: {area_R} px')
axs[2].imshow(G_img)
axs[2].set_title(f'Plano G\nÁrea: {area_G} px')
axs[3].imshow(B_img)
axs[3].set_title(f'Plano B\nÁrea: {area_B} px')

for ax in axs:
    ax.axis('off')
plt.tight_layout()
plt.show()