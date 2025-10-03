import matplotlib.pyplot as plt

caracteres = ["GB%", "MJ2", "C$2", "v1!", "126", "$67", "gVb", "2mV", "&cG", "/#2", "/%B", "/!2"]
tiempos = [0.03, 0.01, 0.01, 0.05, 0.02, 0.04, 0.05, 0.05, 0.03, 0.06, 0.06, 0.06]

plt.figure(figsize=(10,6))
plt.bar(range(len(caracteres)), tiempos, color="skyblue")
plt.title("Tiempo de fuerza bruta según la contraseña")
plt.xlabel("Contraseña")
plt.ylabel("Tiempo (s)")
plt.tight_layout()
plt.show()