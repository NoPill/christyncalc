import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
from pint import UnitRegistry

# Setup unit registry
ureg = UnitRegistry()

st.set_page_config(page_title="ChristynCalc", page_icon="🦄")
st.title("🦄 ChristynCalc™ – Your Math Bestie 💅📚")
st.success("👋 Hey bestie, drop your math drama below and I’ll fix it. No judgment 💖")

st.divider()

# --- Solver ---
st.header("🧮 Solve an Equation")
eq_input = st.text_input("Type an equation (e.g., 2*x + 3 = 7):", key="eq")

if st.button("Solve Equation"):
    try:
        x = sp.Symbol('x')
        left, right = eq_input.split("=")
        solution = sp.solve(sp.sympify(left) - sp.sympify(right), x)
        st.success(f"Solution: x = {solution[0]}")
    except Exception as e:
        st.error(f"Could not solve equation: {e}")

st.divider()

# --- Graph Plotter ---
st.header("📈 Plot a Graph")
func_input = st.text_input("Type a function (e.g., x**2 - 4):", key="graph")

if st.button("Plot Graph"):
    try:
        x = sp.Symbol('x')
        func = sp.sympify(func_input)
        f = sp.lambdify(x, func, modules=['numpy'])
        import numpy as np
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f(x_vals)

        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals)
        ax.axhline(0, color='black', lw=0.5)
        ax.axvline(0, color='black', lw=0.5)
        ax.set_title(f"y = {func_input}")
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Could not plot graph: {e}")

st.divider()

# --- Unit Converter ---
st.header("🔁 Convert Units")
unit_input = st.text_input("Type conversion (e.g., 5 kilometers to meters):", key="unit")

if st.button("Convert"):
    try:
        amount, from_unit, _, to_unit = unit_input.split()
        quantity = float(amount) * ureg(from_unit)
        result = quantity.to(to_unit)
        st.success(f"{unit_input} = {result}")
    except Exception as e:
        st.error(f"Could not convert units: {e}")
