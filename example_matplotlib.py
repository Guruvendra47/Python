# Minimal matplotlib example for visualization
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [n**2 for n in x]

plt.figure()
plt.plot(x, y, marker='o')
plt.title("Simple Quadratic Plot")
plt.xlabel("x")
plt.ylabel("y = x^2")
plt.tight_layout()
plt.savefig("artifacts/quadratic_plot.png")
print("Saved: artifacts/quadratic_plot.png")
