import matplotlib.pyplot as plt

caracteres = ["123", "134", "111", "222", "333", "444", "445", "567", "122", "445", "555", "343"]
tiempos = [92.3, 93.4, 91.1, 102.4, 113.6, 124.9, 125.0, 137.4, 92.2, 125.0, 136.2, 114.6]

plt.figure(figsize=(10,6))
plt.bar(range(len(caracteres)), tiempos, color="skyblue")
plt.title("Tiempo de fuerza bruta según la contraseña")
plt.xlabel("Contraseña")
plt.ylabel("Tiempo (s)")
plt.tight_layout()
plt.show()
