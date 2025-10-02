import cv2
import numpy as np
import matplotlib.pyplot as plt

def procesar_figura_1a(ruta_imagen):
    """
    Procesa la Figura 1a y calcula:
    a. Su Área (Ver 2.17)
    b. Su Centroide (Ver 2.14). Señalícelo con una cruz sobre la imagen.
    c. Su Centroide mediante sus Momentos (Ver 2.18 y 2.19)
    """
    
    # Cargar la imagen
    imagen = cv2.imread(ruta_imagen)
    if imagen is None:
        raise ValueError(f"No se pudo cargar la imagen desde {ruta_imagen}")
    
    # Convertir a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Crear máscara binaria para la figura roja
    # Convertir BGR a HSV para mejor detección de color rojo
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    
    # Definir rango para color rojo en HSV
    rojo_bajo1 = np.array([0, 50, 50])
    rojo_alto1 = np.array([10, 255, 255])
    rojo_bajo2 = np.array([170, 50, 50])
    rojo_alto2 = np.array([180, 255, 255])
    
    # Crear máscaras para ambos rangos de rojo
    mascara1 = cv2.inRange(hsv, rojo_bajo1, rojo_alto1)
    mascara2 = cv2.inRange(hsv, rojo_bajo2, rojo_alto2)
    mascara_roja = cv2.bitwise_or(mascara1, mascara2)
    
    # a) Calcular el área (Ver 2.17)
    area = cv2.countNonZero(mascara_roja)
    print(f"Área de la figura: {area} píxeles")
    
    # b) y c) Calcular centroide usando momentos (Ver 2.14, 2.18, 2.19)
    momentos = cv2.moments(mascara_roja)
    
    if momentos["m00"] != 0:
        # Centroide usando momentos (Ver 2.18 y 2.19)
        cx = int(momentos["m10"] / momentos["m00"])
        cy = int(momentos["m01"] / momentos["m00"])
        
        print(f"Centroide mediante momentos: ({cx}, {cy})")
        print(f"Momento m00 (área): {momentos['m00']}")
        print(f"Momento m10: {momentos['m10']}")
        print(f"Momento m01: {momentos['m01']}")
    else:
        cx, cy = 0, 0
        print("No se pudo calcular el centroide - área cero")
    
    # Visualización con cruz en el centroide
    imagen_resultado = imagen.copy()
    
    # Dibujar cruz en el centroide
    tamaño_cruz = 10
    color_cruz = (0, 255, 255)  # Amarillo en BGR
    grosor = 2
    
    # Línea horizontal
    cv2.line(imagen_resultado, (cx - tamaño_cruz, cy), (cx + tamaño_cruz, cy), color_cruz, grosor)
    # Línea vertical
    cv2.line(imagen_resultado, (cx, cy - tamaño_cruz), (cx, cy + tamaño_cruz), color_cruz, grosor)
    
    # Mostrar resultados
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
    # Ejecutar con la imagen a.png
    ruta = "a.png"
    resultado = procesar_figura_1a(ruta)
    print("\n=== RESULTADOS FIGURA 1A ===")
    print(f"Área: {resultado['area']} píxeles")
    print(f"Centroide: {resultado['centroide']}")