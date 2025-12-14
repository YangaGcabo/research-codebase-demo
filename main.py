import numpy as np

def experiment():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    return x, y

x, y = experiment()
print("Experiment completed. Sample output:")
print(y[:5])
