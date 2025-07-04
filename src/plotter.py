import matplotlib.pyplot as plt
import numpy as np

def plot_function(f_lambdified, func_input):
    x_vals = np.linspace(-10, 10, 500)
    y_vals = f_lambdified(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=f'f(x) = {func_input}', color='teal')
    ax.axhline(0, color='gray', lw=1)
    ax.axvline(0, color='gray', lw=1)
    ax.set_title("Function Graph", fontsize=16)
    ax.grid(True)
    ax.legend()
    return fig
