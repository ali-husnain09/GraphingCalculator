import streamlit as st
from sympy import symbols, sympify
from src.plotter import plot_function
from src.analyzer import get_derivative, latexify, lambdify_expr


def main():
    
    # Set page configuration
    # st.set_page_config(
    #     page_title="Function Plotter",
    #     page_icon="📈",
    # )
    
    # Load custom CSS
    with open("assets/custom.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    x = symbols('x')
    st.title("📈 Function Plotter")

    st.markdown("Enter any valid mathematical expression like `x**2`, `sin(x)`, `exp(x)`")

    col1, col2 = st.columns([2, 1])
    with col1:
        user_input = st.text_input("✏️ Your Function f(x)", "x**2")

    if user_input:
        try:
            expr = sympify(user_input)
            f_lambdified = lambdify_expr(expr)

            fig = plot_function(f_lambdified, user_input)
            st.markdown("### 📊 Graph of f(x)")
            st.pyplot(fig)

            with col2:
                derivative = get_derivative(expr)
                st.markdown("### 🧮 Derivative")
                st.latex(f"f'(x) = {latexify(derivative)}")

        except Exception as e:
            st.error("⚠️ Invalid function. Try something like `x**2`, `sin(x)`, or `1/x`.")


if __name__ == "__main__":
    main()
