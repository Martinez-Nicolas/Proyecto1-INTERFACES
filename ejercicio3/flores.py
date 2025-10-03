import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def separar_planos_colores_y_convertir_gris(ruta_imagen):
    """
    Función que separa los planos de colores de una imagen y la convierte a escala de grises
    
    Parámetros:
    ruta_imagen (str): Ruta del archivo de imagen
    """
    try:
        # Cargar la imagen
        imagen = cv2.imread(ruta_imagen)
        if imagen is None:
            raise ValueError(f"No se pudo cargar la imagen desde {ruta_imagen}")
        
        # Convertir de BGR a RGB para mostrar correctamente con matplotlib
        imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        
        print(f"Imagen cargada: {ruta_imagen}")
        print(f"Dimensiones: {imagen_rgb.shape}")
        
        # Separar los planos de colores (canales RGB)
        plano_rojo = imagen_rgb[:, :, 0]    # Canal Rojo
        plano_verde = imagen_rgb[:, :, 1]   # Canal Verde  
        plano_azul = imagen_rgb[:, :, 2]    # Canal Azul
        
        # Convertir la imagen a escala de grises
        imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        
        # Crear visualización con matplotlib
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        fig.suptitle('Separación de Planos de Colores y Conversión a Escala de Grises', 
                     fontsize=16, fontweight='bold')
        
        # Imagen original
        axes[0, 0].imshow(imagen_rgb)
        axes[0, 0].set_title('Imagen Original (RGB)')
        axes[0, 0].axis('off')
        
        # Plano Rojo
        axes[0, 1].imshow(plano_rojo, cmap='Reds')
        axes[0, 1].set_title('Plano Rojo')
        axes[0, 1].axis('off')
        
        # Plano Verde
        axes[0, 2].imshow(plano_verde, cmap='Greens')
        axes[0, 2].set_title('Plano Verde')
        axes[0, 2].axis('off')
        
        # Plano Azul
        axes[1, 0].imshow(plano_azul, cmap='Blues')
        axes[1, 0].set_title('Plano Azul')
        axes[1, 0].axis('off')
        
        # Imagen en escala de grises
        axes[1, 1].imshow(imagen_gris, cmap='gray')
        axes[1, 1].set_title('Imagen en Escala de Grises')
        axes[1, 1].axis('off')
        
        # Comparación RGB vs Escala de Grises
        axes[1, 2].imshow(np.hstack((imagen_rgb, cv2.cvtColor(imagen_gris, cv2.COLOR_GRAY2RGB))))
        axes[1, 2].set_title('Comparación: Original vs Escala de Grises')
        axes[1, 2].axis('off')
        
        # Ajustar el layout
        plt.tight_layout()
        plt.show()
        
        # Mostrar estadísticas de cada canal
        print("\n=== Estadísticas de los Planos de Colores ===")
        print(f"Plano Rojo - Min: {np.min(plano_rojo)}, Max: {np.max(plano_rojo)}, Media: {np.mean(plano_rojo):.2f}")
        print(f"Plano Verde - Min: {np.min(plano_verde)}, Max: {np.max(plano_verde)}, Media: {np.mean(plano_verde):.2f}")
        print(f"Plano Azul - Min: {np.min(plano_azul)}, Max: {np.max(plano_azul)}, Media: {np.mean(plano_azul):.2f}")
        print(f"Escala de Grises - Min: {np.min(imagen_gris)}, Max: {np.max(imagen_gris)}, Media: {np.mean(imagen_gris):.2f}")
        
        # Crear una segunda figura con los planos de colores individuales más detallados
        crear_visualizacion_detallada(imagen_rgb, plano_rojo, plano_verde, plano_azul, imagen_gris)
        
        return {
            'imagen_original': imagen_rgb,
            'plano_rojo': plano_rojo,
            'plano_verde': plano_verde,
            'plano_azul': plano_azul,
            'imagen_gris': imagen_gris
        }
        
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")
        return None

def crear_visualizacion_detallada(imagen_rgb, plano_rojo, plano_verde, plano_azul, imagen_gris):
    """
    Crea una visualización más detallada de cada plano de color
    """
    # Crear imágenes con solo un canal activo
    solo_rojo = np.zeros_like(imagen_rgb)
    solo_rojo[:, :, 0] = plano_rojo
    
    solo_verde = np.zeros_like(imagen_rgb)
    solo_verde[:, :, 1] = plano_verde
    
    solo_azul = np.zeros_like(imagen_rgb)
    solo_azul[:, :, 2] = plano_azul
    
    # Crear segunda figura
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Visualización Detallada de Cada Canal de Color', 
                 fontsize=16, fontweight='bold')
    
    # Imagen original
    axes[0, 0].imshow(imagen_rgb)
    axes[0, 0].set_title('Imagen Original')
    axes[0, 0].axis('off')
    
    # Solo canal rojo activo
    axes[0, 1].imshow(solo_rojo)
    axes[0, 1].set_title('Solo Canal Rojo Activo')
    axes[0, 1].axis('off')
    
    # Solo canal verde activo
    axes[0, 2].imshow(solo_verde)
    axes[0, 2].set_title('Solo Canal Verde Activo')
    axes[0, 2].axis('off')
    
    # Solo canal azul activo
    axes[1, 0].imshow(solo_azul)
    axes[1, 0].set_title('Solo Canal Azul Activo')
    axes[1, 0].axis('off')
    
    # Imagen en escala de grises
    axes[1, 1].imshow(imagen_gris, cmap='gray')
    axes[1, 1].set_title('Escala de Grises')
    axes[1, 1].axis('off')
    
    # Histograma de la imagen en escala de grises
    axes[1, 2].hist(imagen_gris.flatten(), bins=256, color='gray', alpha=0.7)
    axes[1, 2].set_title('Histograma Escala de Grises')
    axes[1, 2].set_xlabel('Intensidad')
    axes[1, 2].set_ylabel('Frecuencia')
    axes[1, 2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def crear_histogramas_canales(plano_rojo, plano_verde, plano_azul, imagen_gris):
    """
    Crea histogramas para cada canal de color y la escala de grises
    """
    plt.figure(figsize=(12, 8))
    
    # Histograma combinado
    plt.subplot(2, 2, 1)
    plt.hist(plano_rojo.flatten(), bins=256, color='red', alpha=0.5, label='Rojo')
    plt.hist(plano_verde.flatten(), bins=256, color='green', alpha=0.5, label='Verde')
    plt.hist(plano_azul.flatten(), bins=256, color='blue', alpha=0.5, label='Azul')
    plt.title('Histograma Combinado RGB')
    plt.xlabel('Intensidad')
    plt.ylabel('Frecuencia')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Histograma canal rojo
    plt.subplot(2, 2, 2)
    plt.hist(plano_rojo.flatten(), bins=256, color='red', alpha=0.7)
    plt.title('Histograma Canal Rojo')
    plt.xlabel('Intensidad')
    plt.ylabel('Frecuencia')
    plt.grid(True, alpha=0.3)
    
    # Histograma canal verde
    plt.subplot(2, 2, 3)
    plt.hist(plano_verde.flatten(), bins=256, color='green', alpha=0.7)
    plt.title('Histograma Canal Verde')
    plt.xlabel('Intensidad')
    plt.ylabel('Frecuencia')
    plt.grid(True, alpha=0.3)
    
    # Histograma canal azul
    plt.subplot(2, 2, 4)
    plt.hist(plano_azul.flatten(), bins=256, color='blue', alpha=0.7)
    plt.title('Histograma Canal Azul')
    plt.xlabel('Intensidad')
    plt.ylabel('Frecuencia')
    plt.grid(True, alpha=0.3)
    
    plt.suptitle('Histogramas de Cada Canal de Color', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    
    # Histograma de escala de grises por separado
    plt.figure(figsize=(8, 6))
    plt.hist(imagen_gris.flatten(), bins=256, color='gray', alpha=0.7)
    plt.title('Histograma de la Imagen en Escala de Grises', fontsize=14, fontweight='bold')
    plt.xlabel('Intensidad')
    plt.ylabel('Frecuencia')
    plt.grid(True, alpha=0.3)
    plt.show()

def main():
    """
    Función principal que ejecuta el procesamiento de la imagen
    """
    # Ruta de la imagen de flores
    ruta_imagen = os.path.join(os.path.dirname(__file__), "flores.png")
    
    # Verificar si existe la imagen
    if os.path.exists(ruta_imagen):
        print("Iniciando procesamiento de la imagen de flores...")
        print("Separando planos de colores y convirtiendo a escala de grises...")
        
        resultado = separar_planos_colores_y_convertir_gris(ruta_imagen)
        
        if resultado:
            # Crear histogramas adicionales
            crear_histogramas_canales(
                resultado['plano_rojo'], 
                resultado['plano_verde'], 
                resultado['plano_azul'], 
                resultado['imagen_gris']
            )
            
            print("\n¡Procesamiento completado exitosamente!")
            print("Se han generado las siguientes visualizaciones:")
            print("1. Separación de planos de colores")
            print("2. Conversión a escala de grises")
            print("3. Visualización detallada de cada canal")
            print("4. Histogramas de todos los canales")
        
    else:
        print(f"No se encontró la imagen flores.png en {os.path.dirname(__file__)}")
        print("Archivos disponibles en el directorio:")
        directorio = os.path.dirname(__file__)
        for archivo in os.listdir(directorio):
            if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                print(f"  - {archivo}")

if __name__ == "__main__":
    main()
