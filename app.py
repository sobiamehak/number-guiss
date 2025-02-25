
import streamlit as st
import random

# Set the range for the number
lower_bound = 0
upper_bound = 20

# Set up session state for tracking game status
if 'number' not in st.session_state:
    st.session_state.number = random.randint(lower_bound, upper_bound)
    st.session_state.guesses = 0
    st.session_state.game_over = False

# Display Title with Emojis and Styling
st.markdown("<h1 style='text-align: center; background-color: black; border-radius: 5px; color: #32cd32;'>🎉 Number Guessing Game 🎉</h1>", unsafe_allow_html=True)

# Instructions with Emojis
st.write("### 🧐 Try to guess the number between:")
st.write(f"**{lower_bound}** and **{upper_bound}**! 🤔")

# Add some style to the instruction and game layout
st.markdown("""
    <style>
    .stButton button {
        background-color: black;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
    }
    .stButton button:hover {
        
    }
    </style>
""", unsafe_allow_html=True)

# Get user input (guess)
if not st.session_state.game_over:
    guess = st.number_input("📝 Enter your guess:", min_value=lower_bound, max_value=upper_bound, step=1)

    if st.button("🎯 Guess"):
        # Increase the guess count
        st.session_state.guesses += 1

        if guess < st.session_state.number:
            st.write("🔻 **Your guess is too low!** Try a higher number.")
        elif guess > st.session_state.number:
            st.write("🔺 **Your guess is too high!** Try a lower number.")
        else:
            st.session_state.game_over = True
            st.write(f"🎉 **Congratulations!** You guessed the correct number {st.session_state.number} in {st.session_state.guesses} attempts! 🎊")

else:
    # If game is over, prompt to restart
    st.write("💥 **Game Over!** 💥")
    restart = st.button("🔄 Play Again")
    if restart:
        # Reset the game
        st.session_state.number = random.randint(lower_bound, upper_bound)
        st.session_state.guesses = 0
        st.session_state.game_over = False
        st.experimental_rerun()
