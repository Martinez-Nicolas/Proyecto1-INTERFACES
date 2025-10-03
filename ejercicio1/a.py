import cv2
import numpy as np
import matplotlib.pyplot as plt

def procesar_figura_1a(ruta_imagen):
    imagen
    imagen = cv2.imread(ruta_imagen)
    if imagen is None:
        raise ValueError(f"No se pudo cargar la imagen desde {ruta_imagen}")
    
    gris
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    hsv
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    
    rojo_bajo1
    rojo_bajo1 = np.array([0, 50, 50])
    rojo_alto1 = np.array([10, 255, 255])
    rojo_bajo2 = np.array([170, 50, 50])
    rojo_alto2 = np.array([180, 255, 255])
    
    mascara1
    mascara1 = cv2.inRange(hsv, rojo_bajo1, rojo_alto1)
    mascara2 = cv2.inRange(hsv, rojo_bajo2, rojo_alto2)
    mascara_roja = cv2.bitwise_or(mascara1, mascara2)
    
    area
    area = cv2.countNonZero(mascara_roja)
    print(f"Área de la figura: {area} píxeles")
    
    momentos
    momentos = cv2.moments(mascara_roja)
    
    if momentos["m00"] != 0:
        cx
        cx = int(momentos["m10"] / momentos["m00"])
        cy = int(momentos["m01"] / momentos["m00"])
        
        print(f"Centroide mediante momentos: ({cx}, {cy})")
        print(f"Momento m00 (área): {momentos['m00']}")
        print(f"Momento m10: {momentos['m10']}")
        print(f"Momento m01: {momentos['m01']}")
    else:
        cx, cy = 0, 0
        print("No se pudo calcular el centroide - área cero")
    
    imagen_resultado
    imagen_resultado = imagen.copy()
    
    tamaño_cruz
    tamaño_cruz = 10
    color_cruz = (0, 255, 255)
    grosor = 2
    
    cv2.line(imagen_resultado, (cx - tamaño_cruz, cy), (cx + tamaño_cruz, cy), color_cruz, grosor)
    cv2.line(imagen_resultado, (cx, cy - tamaño_cruz), (cx, cy + tamaño_cruz), color_cruz, grosor)
    cv2.line(imagen_resultado, (cx, cy - tamaño_cruz), (cx, cy + tamaño_cruz), color_cruz, grosor)
    
    plt.figure(figsize=(15, 5))
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
    plt.title('Imagen Original')
    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.imshow(mascara_roja, cmap='gray')
    plt.title('Máscara de la Figura Roja')
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(imagen_resultado, cv2.COLOR_BGR2RGB))
    plt.title(f'Centroide marcado: ({cx}, {cy})')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    return {
        'area': area,
        'centroide': (cx, cy),
        'momentos': momentos
    }

if __name__ == "__main__":
    import os
    ruta = os.path.join(os.path.dirname(__file__), "a.png")
    resultado = procesar_figura_1a(ruta)
    print("\n=== RESULTADOS FIGURA 1A ===")
    print(f"Área: {resultado['area']} píxeles")
    print(f"Centroide: {resultado['centroide']}")