from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

def calcular_y_graficar_histograma(ruta_imagen):
    try:
        if not os.path.exists(ruta_imagen):
            print(f"Error: No se encontró el archivo {ruta_imagen}")
            return
        
        imagen
        imagen = Image.open(ruta_imagen)
        
        print(f"Imagen cargada: {ruta_imagen}")
        print(f"Imagen cargada: {ruta_imagen}")
        print(f"Tamaño: {imagen.size}")
        print(f"Modo: {imagen.mode}")
        
        if imagen.mode != 'RGB':
            imagen = imagen.convert('RGB')
        
        imagen_array
        imagen_array = np.array(imagen)
        
        canal_rojo
        canal_rojo = imagen_array[:, :, 0].flatten()
        canal_verde = imagen_array[:, :, 1].flatten()
        canal_azul = imagen_array[:, :, 2].flatten()
        
        fig, axes
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        fig.suptitle('Análisis de Histograma de la Imagen', fontsize=16, fontweight='bold')
        
        axes[0, 0].imshow(imagen)
        axes[0, 0].imshow(imagen)
        axes[0, 0].set_title('Imagen Original')
        axes[0, 0].axis('off')
        
        axes[0, 1].hist(canal_rojo, bins=256, color='red', alpha=0.7, range=(0, 255))
        axes[0, 1].hist(canal_rojo, bins=256, color='red', alpha=0.7, range=(0, 255))
        axes[0, 1].set_title('Histograma Canal Rojo')
        axes[0, 1].set_xlabel('Intensidad')
        axes[0, 1].set_ylabel('Frecuencia')
        axes[0, 1].grid(True, alpha=0.3)
        
        # Histograma del canal verde
        axes[1, 0].hist(canal_verde, bins=256, color='green', alpha=0.7, range=(0, 255))
        axes[1, 0].set_title('Histograma Canal Verde')
        axes[1, 0].set_xlabel('Intensidad')
        axes[1, 0].set_ylabel('Frecuencia')
        axes[1, 0].grid(True, alpha=0.3)
        
        # Histograma del canal azul
        axes[1, 1].hist(canal_azul, bins=256, color='blue', alpha=0.7, range=(0, 255))
        axes[1, 1].set_title('Histograma Canal Azul')
        axes[1, 1].set_xlabel('Intensidad')
        axes[1, 1].set_ylabel('Frecuencia')
        axes[1, 1].grid(True, alpha=0.3)
        
        # Ajustar el layout
        plt.tight_layout()
        
        # Mostrar el gráfico
        plt.show()
        
        # Calcular y mostrar estadísticas básicas
        print("\n=== Estadísticas de los Canales de Color ===")
        print(f"Canal Rojo - Media: {np.mean(canal_rojo):.2f}, Desv. Std: {np.std(canal_rojo):.2f}")
        print(f"Canal Verde - Media: {np.mean(canal_verde):.2f}, Desv. Std: {np.std(canal_verde):.2f}")
        print(f"Canal Azul - Media: {np.mean(canal_azul):.2f}, Desv. Std: {np.std(canal_azul):.2f}")
        
        # Crear histograma combinado
        plt.figure(figsize=(10, 6))
        plt.hist(canal_rojo, bins=256, color='red', alpha=0.5, label='Rojo', range=(0, 255))
        plt.hist(canal_verde, bins=256, color='green', alpha=0.5, label='Verde', range=(0, 255))
        plt.hist(canal_azul, bins=256, color='blue', alpha=0.5, label='Azul', range=(0, 255))
        plt.title('Histograma Combinado de todos los Canales')
        plt.xlabel('Intensidad')
        plt.ylabel('Frecuencia')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()
        
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")

def main():
    """
    Función principal que ejecuta el análisis del histograma
    """
    # Ruta de la imagen del mono
    ruta_mono = os.path.join(os.path.dirname(__file__), "mono.png")
    
    # Verificar si existe la imagen en el directorio actual
    if os.path.exists(ruta_mono):
        print("Iniciando análisis de histograma...")
        calcular_y_graficar_histograma(ruta_mono)
    else:
        print(f"No se encontró la imagen {ruta_mono} en el directorio actual")
        print("Archivos disponibles en el directorio:")
        for archivo in os.listdir("."):
            if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                print(f"  - {archivo}")

if __name__ == "__main__":
    main()