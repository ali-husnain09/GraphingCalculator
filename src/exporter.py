from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import sympy as sp

def export_pdf(expr, derivative, image_path, output_pdf):
    with PdfPages(output_pdf) as pdf:
        # Page 1: Function and Derivative
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.axis('off')
        text = "Function: f(x) = " + sp.pretty(expr, use_unicode=True) + "\n\n"
        text += "Derivative: f'(x) = " + sp.pretty(derivative, use_unicode=True)
        ax.text(0.05, 0.95, text, transform=ax.transAxes, fontsize=12, va='top', family='monospace')
        pdf.savefig(fig)
        plt.close(fig)

        # Page 2: Graph image
        fig_img = plt.figure(figsize=(8, 5))
        img = plt.imread(image_path)
        plt.imshow(img)
        plt.axis('off')
        pdf.savefig(fig_img)
        plt.close(fig_img)
        print(f"PDF exported successfully to {output_pdf}")