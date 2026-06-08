import streamlit as st
import numpy as np

st.set_page_config(page_title="Tic Tac Toe", page_icon="🎮")

# Initialize board
if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)

if "current" not in st.session_state:
    st.session_state.current = 1

if "winner" not in st.session_state:
    st.session_state.winner = None


def check_winner(board):

    # Rows and Columns
    if 3 in np.sum(board, axis=1) or 3 in np.sum(board, axis=0):
        return "X"

    if -3 in np.sum(board, axis=1) or -3 in np.sum(board, axis=0):
        return "O"

    # Diagonals
    if np.trace(board) == 3 or np.trace(np.fliplr(board)) == 3:
        return "X"

    if np.trace(board) == -3 or np.trace(np.fliplr(board)) == -3:
        return "O"

    # Draw
    if not 0 in board:
        return "DRAW"

    return None


def make_move(row, col):

    if st.session_state.board[row, col] != 0:
        return

    st.session_state.board[row, col] = st.session_state.current

    result = check_winner(st.session_state.board)

    if result:
        st.session_state.winner = result
    else:
        st.session_state.current *= -1


st.title("🎮 Tic Tac Toe")

player = "X" if st.session_state.current == 1 else "O"

if st.session_state.winner is None:
    st.subheader(f"Current Player: {player}")

symbols = {
    0: " ",
    1: "❌",
    -1: "⭕"
}

for r in range(3):

    cols = st.columns(3)

    for c in range(3):

        with cols[c]:

            if st.button(
                symbols[st.session_state.board[r, c]],
                key=f"{r}{c}",
                use_container_width=True
            ):
                if st.session_state.winner is None:
                    make_move(r, c)

if st.session_state.winner:

    if st.session_state.winner == "DRAW":
        st.warning("🤝 Match Draw!")
    else:
        st.success(f"🎉 Player {st.session_state.winner} Wins!")

if st.button("🔄 Restart Game"):

    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.winner = None

    st.rerun()