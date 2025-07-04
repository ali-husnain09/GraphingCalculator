import streamlit as st
from sympy import symbols, sympify
from src.plotter import plot_function
from src.analyzer import get_derivative, latexify, lambdify_expr


def main():
        # Load custom CSS
    with open("assets/custom.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    x = symbols('x')
    st.title("📈 Graphing Calculator with Derivative Viewer")

    user_input = st.text_input("Enter a function of x:", "x**2")

    try:
        expr = sympify(user_input)
        f_lambdified = lambdify_expr(expr)
        fig = plot_function(f_lambdified, user_input)
        st.pyplot(fig)

        st.subheader("🧮 Derivative")
        derivative = get_derivative(expr)
        st.latex(f"f'(x) = {latexify(derivative)}")

    except Exception as e:
        st.error(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
