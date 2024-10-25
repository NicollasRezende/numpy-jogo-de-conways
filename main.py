import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configurações
grid_size = 50
generations = 100

# Inicialização da grade
grid = np.random.choice([0, 1], size=(grid_size, grid_size), p=[0.8, 0.2])

def update(frameNum, img, grid):
    # Cópia da grade atual
    new_grid = grid.copy()
    
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            # Contar vizinhos vivos
            total = (grid[i, (j-1)%grid.shape[1]] + grid[i, (j+1)%grid.shape[1]] +
                     grid[(i-1)%grid.shape[0], j] + grid[(i+1)%grid.shape[0], j] +
                     grid[(i-1)%grid.shape[0], (j-1)%grid.shape[1]] + grid[(i-1)%grid.shape[0], (j+1)%grid.shape[1]] +
                     grid[(i+1)%grid.shape[0], (j-1)%grid.shape[1]] + grid[(i+1)%grid.shape[0], (j+1)%grid.shape[1]])
            
            # Aplicar as regras
            if grid[i, j] == 1 and (total < 2 or total > 3):
                new_grid[i, j] = 0  # Morte
            elif grid[i, j] == 0 and total == 3:
                new_grid[i, j] = 1  # Reprodução
                
    img.set_array(new_grid)
    grid[:] = new_grid[:]
    return img,

fig, ax = plt.subplots(figsize=(8, 8))
img = ax.imshow(grid, interpolation='nearest', cmap='inferno', aspect='equal')

# Configurações do gráfico
ax.set_title("Jogo da Vida de Conway", fontsize=16)
ax.set_xticks([])
ax.set_yticks([])
# Animação
ani = animation.FuncAnimation(fig, update, fargs=(img, grid), frames=generations, interval=100)

plt.show()
