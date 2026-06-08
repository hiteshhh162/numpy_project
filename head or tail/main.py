import streamlit as st
import numpy as np

st.title("🪙 Coin Toss Game")
st.write("Choose Head or Tail and test your luck!")

choices = np.array(["head", "tail"])

player_choice = st.radio(
    "Select your choice:",
    ["head", "tail"]
)

if st.button("Toss Coin"):
    computer_choice = np.random.choice(choices)

    st.subheader(f"Coin Result: {computer_choice.upper()}")

    if computer_choice == player_choice:
        st.success(f"🎉 You Win! Your choice was {player_choice.upper()}")
    else:
        st.error(f"😢 Computer Wins! Your choice was {player_choice.upper()}")