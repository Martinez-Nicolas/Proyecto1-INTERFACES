import cv2
import numpy as np
import matplotlib.pyplot as plt

def procesar_figura_1b(ruta_imagen):
    imagen
    imagen = cv2.imread(ruta_imagen)
    if imagen is None:
        raise ValueError(f"No se pudo cargar la imagen desde {ruta_imagen}")
    
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    hsv
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    
    verde_bajo
    verde_bajo = np.array([40, 50, 50])
    verde_alto = np.array([80, 255, 255])
    
    mascara_verde
    mascara_verde = cv2.inRange(hsv, verde_bajo, verde_alto)
    
    momentos
    momentos = cv2.moments(mascara_verde)
    
    if momentos["m00"] == 0:
        print("Error: No se detectó la figura verde o área es cero")
        return None
    
    cx
    cx = momentos["m10"] / momentos["m00"]
    cy = momentos["m01"] / momentos["m00"]
    
    print(f"Centroide de la figura verde: ({cx:.2f}, {cy:.2f})")
    print(f"Área (m00): {momentos['m00']}")
    
    momento_orden_21
    momento_orden_21 = calcular_momento_orden(mascara_verde, p=2, q=1)
    print(f"Momento de Orden m(2,1): {momento_orden_21}")
    
    momento_central_21
    momento_central_21 = calcular_momento_central(mascara_verde, cx, cy, p=2, q=1)
    print(f"Momento Central μ(2,1): {momento_central_21}")
    
    gamma
    gamma = (2 + 1) / 2 + 1
    momento_normalizado_21 = momento_central_21 / (momentos["m00"] ** gamma)
    print(f"Momento Central Normalizado η(2,1): {momento_normalizado_21}")
    
    plt.figure(figsize=(15, 5))
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
    plt.title('Imagen Original')
    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.imshow(mascara_verde, cmap='gray')
    plt.title('Máscara de la Figura Verde')
    plt.axis('off')
    
    imagen_resultado
    imagen_resultado = imagen.copy()
    cx_int, cy_int = int(cx), int(cy)
    tamaño_cruz = 10
    color_cruz = (0, 255, 255)
    grosor = 2
    
    cv2.line(imagen_resultado, (cx_int - tamaño_cruz, cy_int), (cx_int + tamaño_cruz, cy_int), color_cruz, grosor)
    cv2.line(imagen_resultado, (cx_int, cy_int - tamaño_cruz), (cx_int, cy_int + tamaño_cruz), color_cruz, grosor)
    
    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(imagen_resultado, cv2.COLOR_BGR2RGB))
    plt.title(f'Centroide: ({cx:.1f}, {cy:.1f})')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    return {
        'momento_orden_21': momento_orden_21,
        'momento_central_21': momento_central_21,
        'momento_normalizado_21': momento_normalizado_21,
        'centroide': (cx, cy),
        'area': momentos["m00"]
    }

def calcular_momento_orden(mascara, p, q):
    momento = 0.0
    altura, ancho = mascara.shape
    
    for y in range(altura):
        for x in range(ancho):
            if mascara[y, x] > 0:
                momento += (x ** p) * (y ** q)
    
    return momento

def calcular_momento_central(mascara, cx, cy, p, q):
    momento = 0.0
    altura, ancho = mascara.shape
    
    for y in range(altura):
        for x in range(ancho):
            if mascara[y, x] > 0:
                momento += ((x - cx) ** p) * ((y - cy) ** q)
    
    return momento

if __name__ == "__main__":
    import os
    ruta = os.path.join(os.path.dirname(__file__), "b.png")
    resultado = procesar_figura_1b(ruta)
    if resultado:
        print("\n=== RESULTADOS FIGURA 1B ===")
        print(f"Momento de Orden m(2,1): {resultado['momento_orden_21']:.6f}")
        print(f"Momento Central μ(2,1): {resultado['momento_central_21']:.6f}")
        print(f"Momento Central Normalizado η(2,1): {resultado['momento_normalizado_21']:.6f}")
        print(f"Área: {resultado['area']:.0f} píxeles")