import cv2
import numpy as np
import matplotlib.pyplot as plt

def procesar_figura_1c(ruta_imagen):
    imagen
    imagen = cv2.imread(ruta_imagen)
    if imagen is None:
        raise ValueError(f"No se pudo cargar la imagen desde {ruta_imagen}")
    
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    hsv
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    
    azul_bajo
    azul_bajo = np.array([100, 50, 50])
    azul_alto = np.array([130, 255, 255])
    
    mascara_azul
    mascara_azul = cv2.inRange(hsv, azul_bajo, azul_alto)
    
    momentos
    momentos = cv2.moments(mascara_azul)
    
    if momentos["m00"] == 0:
        print("Error: No se detectó la figura azul o área es cero")
        return None
    
    cx
    cx = momentos["m10"] / momentos["m00"]
    cy = momentos["m01"] / momentos["m00"]
    
    print(f"Centroide de la figura azul: ({cx:.2f}, {cy:.2f})")
    print(f"Área (m00): {momentos['m00']}")
    
    momentos_centrales_norm
    momentos_centrales_norm = calcular_momentos_centrales_normalizados(mascara_azul, cx, cy)
    
    hu_moments
    hu_moments = calcular_hu_moments(momentos_centrales_norm)
    
    print(f"\n=== MOMENTOS DE HU ===")
    print(f"H1: {hu_moments['H1']:.8f}")
    print(f"H2: {hu_moments['H2']:.8f}")
    print(f"H3: {hu_moments['H3']:.8f}")
    
    hu_opencv
    hu_opencv = cv2.HuMoments(momentos).flatten()
    print(f"\n=== VERIFICACIÓN CON OPENCV ===")
    print(f"H1 (OpenCV): {hu_opencv[0]:.8f}")
    print(f"H2 (OpenCV): {hu_opencv[1]:.8f}")
    print(f"H3 (OpenCV): {hu_opencv[2]:.8f}")
    
    plt.figure(figsize=(15, 5))
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
    plt.title('Imagen Original')
    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.imshow(mascara_azul, cmap='gray')
    plt.title('Máscara de la Figura Azul')
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
        'hu_moments': hu_moments,
        'hu_opencv': hu_opencv[:3],
        'centroide': (cx, cy),
        'area': momentos["m00"],
        'momentos_centrales_norm': momentos_centrales_norm
    }

def calcular_momentos_centrales_normalizados(mascara, cx, cy):
    altura, ancho = mascara.shape
    area = np.sum(mascara > 0)
    
    momentos_centrales
    momentos_centrales = {}
    
    ordenes
    ordenes = [(1,1), (2,0), (0,2), (3,0), (1,2), (2,1), (0,3)]
    
    for p, q in ordenes:
        mu_pq = 0.0
        for y in range(altura):
            for x in range(ancho):
                if mascara[y, x] > 0:
                    mu_pq += ((x - cx) ** p) * ((y - cy) ** q)
        
        gamma
        gamma = (p + q) / 2 + 1
        eta_pq = mu_pq / (area ** gamma)
        momentos_centrales[f"eta{p}{q}"] = eta_pq
        
        print(f"μ({p},{q}): {mu_pq:.6f}")
        print(f"η({p},{q}): {eta_pq:.8f}")
    
    return momentos_centrales

def calcular_hu_moments(eta):
    H1
    H1 = eta["eta20"] + eta["eta02"]
    
    H2
    H2 = (eta["eta20"] - eta["eta02"])**2 + 4 * (eta["eta11"])**2
    
    H3
    H3 = (eta["eta30"] - 3*eta["eta12"])**2 + (3*eta["eta21"] - eta["eta03"])**2
    
    return {
        'H1': H1,
        'H2': H2,
        'H3': H3
    }

if __name__ == "__main__":
    import os
    ruta = os.path.join(os.path.dirname(__file__), "c.png")
    resultado = procesar_figura_1c(ruta)
    if resultado:
        print("\n=== RESULTADOS FIGURA 1C ===")
        print(f"Momento de Hu H1: {resultado['hu_moments']['H1']:.8f}")
        print(f"Momento de Hu H2: {resultado['hu_moments']['H2']:.8f}")
        print(f"Momento de Hu H3: {resultado['hu_moments']['H3']:.8f}")
        print(f"Área: {resultado['area']:.0f} píxeles")