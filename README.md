# Documentação do Projeto: Jogo da Vida de Conway

## Descrição do Projeto

Este projeto implementa o **Jogo da Vida de Conway**, um autômato celular desenvolvido por John Horton Conway. O jogo consiste em uma grade bidimensional de células que podem estar vivas ou mortas. A evolução do estado da grade ocorre em gerações discretas, seguindo regras simples baseadas no número de vizinhos vivos de cada célula. Este projeto é uma implementação simples, destinada a fins de teste e aprendizado.

### Objetivos do Projeto

- Demonstrar a implementação do Jogo da Vida de Conway utilizando **NumPy** para manipulação de arrays.
- Aprender sobre autômatos celulares e suas regras básicas de evolução.
- Explorar a biblioteca **Matplotlib** para visualização de dados e animações.

## Estrutura do Código

O código está dividido em várias seções principais:

### 1. Importação de Bibliotecas

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
```

- **NumPy**: Usada para manipulação eficiente de arrays, permitindo criar e modificar a grade do jogo.
- **Matplotlib**: Usada para visualização dos dados em uma animação gráfica.

### 2. Configurações Iniciais

```python
grid_size = 50
generations = 100
```

- **grid_size**: Define o tamanho da grade (número de células na vertical e horizontal).
- **generations**: Define o número total de gerações a serem exibidas na animação.

### 3. Inicialização da Grade

```python
grid = np.random.choice([0, 1], size=(grid_size, grid_size), p=[0.8, 0.2])
```

- Uma grade inicial é criada com células aleatórias, onde `0` representa uma célula morta e `1` representa uma célula viva. A probabilidade de uma célula estar viva é de 20%.

### 4. Função de Atualização

```python
def update(frameNum, img, grid):
    ...
```

- Esta função é chamada a cada geração para atualizar o estado da grade.
- Uma cópia da grade atual é criada (`new_grid`), e para cada célula, o número de vizinhos vivos é contado.
- As regras do Jogo da Vida são aplicadas:
  - Uma célula viva morre se tiver menos de 2 ou mais de 3 vizinhos vivos.
  - Uma célula morta se torna viva se tiver exatamente 3 vizinhos vivos.
- A imagem é atualizada com o novo estado da grade.

### 5. Configuração da Animação

```python
fig, ax = plt.subplots(figsize=(8, 8))
img = ax.imshow(grid, interpolation='nearest', cmap='inferno', aspect='equal')
```

- A visualização da grade é configurada utilizando Matplotlib.
- O tamanho da figura é ajustado para 8x8, e um colormap interessante (`'inferno'`) é utilizado para uma visualização melhorada.

### 6. Execução da Animação

```python
ani = animation.FuncAnimation(fig, update, fargs=(img, grid), frames=generations, interval=100)
plt.show()
```

- A animação é gerada utilizando a função `FuncAnimation`, que chama a função de atualização a cada intervalo definido.
- O resultado é exibido em uma janela gráfica.

## Potencial da Biblioteca NumPy

**NumPy** é uma biblioteca fundamental para computação científica em Python. Suas principais características e potenciais incluem:

- **Manipulação de Arrays**: NumPy fornece suporte para arrays multidimensionais de forma eficiente, permitindo operações rápidas em grandes conjuntos de dados.
- **Operações Matemáticas**: Oferece uma vasta gama de funções matemáticas que podem ser aplicadas em arrays, como álgebra linear, estatísticas e transformações.
- **Desempenho**: NumPy é otimizada para desempenho, permitindo que operações em arrays sejam realizadas em paralelo, o que é particularmente útil em cálculos científicos e análises de dados.
- **Integração com Outras Bibliotecas**: NumPy serve como base para muitas outras bibliotecas populares em ciência de dados e aprendizado de máquina, como Pandas, SciPy e TensorFlow.

## Conclusão

Este projeto de Jogo da Vida de Conway foi uma implementação simples para testar e aprender sobre conceitos de autômatos celulares, manipulação de arrays e visualização gráfica utilizando NumPy e Matplotlib. A experiência adquirida através deste projeto pode ser aplicada a desenvolvimentos mais complexos em computação científica e visualização de dados.
