import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def cargar_imagenes():
    rutas = {
        'fig_00': os.path.join(os.path.dirname(__file__), "fig_00.jpg"),
        'pla_01': os.path.join(os.path.dirname(__file__), "pla_01.jpg"),
        'pla_02': os.path.join(os.path.dirname(__file__), "pla_02.jpg"),
        'pla_03': os.path.join(os.path.dirname(__file__), "pla_03.jpg"),
        'pla_04': os.path.join(os.path.dirname(__file__), "pla_04.jpg"),
        'fig_01': os.path.join(os.path.dirname(__file__), "fig_01.jpg"),
        'fig_02': os.path.join(os.path.dirname(__file__), "fig_02.jpg"),
        'fig_03': os.path.join(os.path.dirname(__file__), "fig_03.jpg"),
        'fig_04': os.path.join(os.path.dirname(__file__), "fig_04.jpg")
    }
    
    imagenes = {}
    for nombre, ruta in rutas.items():
        img = cv2.imread(ruta)
        if img is not None:
            imagenes[nombre] = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    return imagenes

def crear_mascara_circular(tamaño, centro, radio):
    mascara = np.zeros(tamaño[:2], dtype=np.uint8)
    cv2.circle(mascara, centro, radio, 255, -1)
    return mascara

def crear_mascara_rectangular(tamaño, esquina1, esquina2):
    mascara = np.zeros(tamaño[:2], dtype=np.uint8)
    cv2.rectangle(mascara, esquina1, esquina2, 255, -1)
    return mascara

def crear_mascara_pentagonal(tamaño, centro, radio):
    mascara = np.zeros(tamaño[:2], dtype=np.uint8)
    puntos = []
    for i in range(5):
        angulo = 2 * np.pi * i / 5 - np.pi/2
        x = int(centro[0] + radio * np.cos(angulo))
        y = int(centro[1] + radio * np.sin(angulo))
        puntos.append([x, y])
    
    puntos = np.array(puntos, dtype=np.int32)
    cv2.fillPoly(mascara, [puntos], 255)
    return mascara

def crear_mascara_corazon(tamaño, centro, escala):
    mascara = np.zeros(tamaño[:2], dtype=np.uint8)
    puntos = []
    
    for t in np.linspace(0, 2*np.pi, 1000):
        x = 16 * np.sin(t)**3
        y = -(13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t))
        
        x_pixel = int(centro[0] + x * escala)
        y_pixel = int(centro[1] + y * escala)
        
        if 0 <= x_pixel < tamaño[1] and 0 <= y_pixel < tamaño[0]:
            puntos.append([x_pixel, y_pixel])
    
    if puntos:
        puntos = np.array(puntos, dtype=np.int32)
        cv2.fillPoly(mascara, [puntos], 255)
    
    return mascara

def aplicar_efecto_mascara(imagen_fondo, imagen_frente, mascara):
    mascara_3d = cv2.merge([mascara, mascara, mascara])
    mascara_norm = mascara_3d.astype(np.float32) / 255.0
    
    resultado = imagen_fondo.astype(np.float32) * (1 - mascara_norm) + imagen_frente.astype(np.float32) * mascara_norm
    return resultado.astype(np.uint8)

def procesar_efectos():
    imagenes = cargar_imagenes()
    
    if len(imagenes) < 9:
        print("Faltan algunas imágenes")
        return
    
    efectos = []
    
    cara_mujer = imagenes['fig_00']
    
    altura, ancho = imagenes['fig_01'].shape[:2]
    cara_redimensionada = cv2.resize(cara_mujer, (ancho, altura))
    centro = (ancho // 2, altura // 2)
    
    mascara_circular = crear_mascara_circular(imagenes['fig_01'].shape, centro, min(ancho, altura) // 4)
    efecto1 = aplicar_efecto_mascara(imagenes['fig_01'], cara_redimensionada, mascara_circular)
    efectos.append(('Efecto Circular', efecto1))
    
    altura, ancho = imagenes['fig_02'].shape[:2]
    cara_redimensionada = cv2.resize(cara_mujer, (ancho, altura))
    esquina1 = (ancho // 4, altura // 4)
    esquina2 = (3 * ancho // 4, 3 * altura // 4)
    mascara_rectangular = crear_mascara_rectangular(imagenes['fig_02'].shape, esquina1, esquina2)
    efecto2 = aplicar_efecto_mascara(imagenes['fig_02'], cara_redimensionada, mascara_rectangular)
    efectos.append(('Efecto Rectangular', efecto2))
    
    altura, ancho = imagenes['fig_03'].shape[:2]
    cara_redimensionada = cv2.resize(cara_mujer, (ancho, altura))
    centro = (ancho // 2, altura // 2)
    mascara_pentagonal = crear_mascara_pentagonal(imagenes['fig_03'].shape, centro, min(ancho, altura) // 4)
    efecto3 = aplicar_efecto_mascara(imagenes['fig_03'], cara_redimensionada, mascara_pentagonal)
    efectos.append(('Efecto Pentagonal', efecto3))
    
    altura, ancho = imagenes['fig_04'].shape[:2]
    cara_redimensionada = cv2.resize(cara_mujer, (ancho, altura))
    centro = (ancho // 2, altura // 2)
    escala = min(ancho, altura) // 35
    mascara_corazon = crear_mascara_corazon(imagenes['fig_04'].shape, centro, escala)
    efecto4 = aplicar_efecto_mascara(imagenes['fig_04'], cara_redimensionada, mascara_corazon)
    efectos.append(('Efecto Corazón', efecto4))
    
    return efectos, imagenes

def mostrar_resultados():
    efectos, imagenes = procesar_efectos()
    
    fig, axes = plt.subplots(3, 5, figsize=(20, 12))
    fig.suptitle('Efectos de Composición con Máscaras Geométricas', fontsize=16, fontweight='bold')
    
    originales = ['fig_01', 'fig_02', 'fig_03', 'fig_04']
    plantillas = ['pla_01', 'pla_02', 'pla_03', 'pla_04']
    
    for i in range(4):
        axes[0, i].imshow(imagenes[originales[i]])
        axes[0, i].set_title(f'Original {i+1}')
        axes[0, i].axis('off')
        
        axes[1, i].imshow(efectos[i][1])
        axes[1, i].set_title(efectos[i][0])
        axes[1, i].axis('off')
        
        axes[2, i].imshow(imagenes[plantillas[i]])
        axes[2, i].set_title(f'Plantilla {i+1}')
        axes[2, i].axis('off')
    
    axes[2, 4].imshow(imagenes['fig_00'])
    axes[2, 4].set_title('fig_00.jpg')
    axes[2, 4].axis('off')
    
    axes[0, 4].axis('off')
    axes[1, 4].axis('off')
    
    plt.tight_layout()
    plt.show()

def mostrar_mascaras():
    imagenes = cargar_imagenes()
    
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    fig.suptitle('Máscaras Geométricas Utilizadas', fontsize=14, fontweight='bold')
    
    altura, ancho = imagenes['fig_01'].shape[:2]
    centro = (ancho // 2, altura // 2)
    
    mascara_circular = crear_mascara_circular(imagenes['fig_01'].shape, centro, min(ancho, altura) // 4)
    axes[0].imshow(mascara_circular, cmap='gray')
    axes[0].set_title('Máscara Circular')
    axes[0].axis('off')
    
    altura, ancho = imagenes['fig_02'].shape[:2]
    esquina1 = (ancho // 4, altura // 4)
    esquina2 = (3 * ancho // 4, 3 * altura // 4)
    mascara_rectangular = crear_mascara_rectangular(imagenes['fig_02'].shape, esquina1, esquina2)
    axes[1].imshow(mascara_rectangular, cmap='gray')
    axes[1].set_title('Máscara Rectangular')
    axes[1].axis('off')
    
    altura, ancho = imagenes['fig_03'].shape[:2]
    centro = (ancho // 2, altura // 2)
    mascara_pentagonal = crear_mascara_pentagonal(imagenes['fig_03'].shape, centro, min(ancho, altura) // 4)
    axes[2].imshow(mascara_pentagonal, cmap='gray')
    axes[2].set_title('Máscara Pentagonal')
    axes[2].axis('off')
    
    altura, ancho = imagenes['fig_04'].shape[:2]
    centro = (ancho // 2, altura // 2)
    escala = min(ancho, altura) // 35
    mascara_corazon = crear_mascara_corazon(imagenes['fig_04'].shape, centro, escala)
    axes[3].imshow(mascara_corazon, cmap='gray')
    axes[3].set_title('Máscara Corazón')
    axes[3].axis('off')
    
    plt.tight_layout()
    plt.show()

def main():
    print("Procesando efectos de composición...")
    mostrar_resultados()
    print("Procesamiento completado.")

if __name__ == "__main__":
    main()
