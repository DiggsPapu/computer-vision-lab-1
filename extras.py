import matplotlib.pyplot as plt

def mostrar_imagenes(titulos, imagenes):
    """
    Muestra una lista de imágenes con sus títulos en una sola fila.

    Parámetros:
    - titulos: Lista de títulos para cada imagen.
    - imagenes: Lista de imágenes a mostrar.

    """
    num_imagenes = len(imagenes)
    
    # Crear una figura con subgráficos
    fig, axes = plt.subplots(1, num_imagenes, figsize=(5 * num_imagenes, 5))

    # Si hay solo una imagen, convertir axes en lista para evitar errores
    if num_imagenes == 1:
        axes = [axes]

    # Recorrer listas de imágenes y títulos
    for ax, img, titulo in zip(axes, imagenes, titulos):
        ax.imshow(img, cmap='gray')
        ax.set_title(titulo)
        ax.axis('off')  # Ocultar ejes

    plt.tight_layout()
    plt.show()



def mostrar_graficas(datos, titulos):
    """
    Muestra varias gráficas en una sola fila.

    Parámetros:
    - datos: Lista de tuplas (x, y), donde x e y son listas de coordenadas.
    - titulos: Lista de títulos para cada gráfica.

    """
    num_graficas = len(datos)

    # Crear una figura con subgráficos en una fila
    fig, axes = plt.subplots(1, num_graficas, figsize=(5 * num_graficas, 4))

    # Si solo hay una gráfica, convertir axes en lista para evitar errores
    if num_graficas == 1:
        axes = [axes]

    # Recorrer cada conjunto de datos y título
    for ax, (x, y), titulo in zip(axes, datos, titulos):
        ax.plot(x, y, 'b-')  # Graficar con líneas y marcadores
        ax.set_title(titulo)
        ax.grid(True)  # Agregar rejilla para mejor visualización

    plt.tight_layout()
    plt.show()

     
