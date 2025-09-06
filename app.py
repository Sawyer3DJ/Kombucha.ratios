import streamlit as st

# Title
st.title("🍵 Kombucha Ratio Calculator")

st.write("Enter your desired batch size, and this app will calculate the ratios for starter tea, sugar, and water.")

# User input: finished amount in mL
batch_size = st.number_input("Finished amount (mL)", min_value=500, max_value=20000, step=100, value=4000)

# Ratios
starter_ratio = 0.10   # 10% starter tea
sugar_per_3785ml = 200 # grams per gallon (3785 ml)
sugar_ratio = sugar_per_3785ml / 3785

# Calculations
starter_amount = batch_size * starter_ratio
sweet_tea = batch_size - starter_amount
sugar_amount = batch_size * sugar_ratio
water_amount = sweet_tea  # sugar dissolves in water

# Output results
st.subheader("Your Recipe")
st.write(f"**Starter tea:** {starter_amount:.0f} mL")
st.write(f"**Sugar:** {sugar_amount:.0f} g")
st.write(f"**Water (before sugar):** {water_amount:.0f} mL")

st.success("Now you can brew your kombucha with the right ratios! 🍹")
