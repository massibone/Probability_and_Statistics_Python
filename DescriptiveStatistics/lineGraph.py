import matplotlib.pyplot as plt

stipendio_iniziale = [27, 28, 29, 30, 31, 32, 34, 36, 37, 40]
frequenza = [4, 1, 3, 5, 8, 10, 5, 2, 3, 1]

plt.bar(stipendio_iniziale, frequenza)
plt.xlabel('Stipendio Iniziale')
plt.ylabel('Frequenza')
plt.title('Grafico a Bastoncini degli Stipendi Iniziali')

plt.show()
