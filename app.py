import streamlit as st
import numpy as np
from solver import solve_sudoku
from generator import generate_sudoku
from utils import parse_upload_file, print_board, display_sudoku_grid

def display_board(board, title='Sudoku Board'):
    st.markdown(f'### {title}')
    for row in board:
        st.write(' '.join(str(cell) if cell !=0 else '.' for cell in row))
st.set_page_config(page_title='Sudoku Solver', layout='centered')
st.title('Sudoku solver and generator')

# --- Sidebar ---
option = st.sidebar.radio('Choose Action',('Upload & Solve','Generate Puzzle'))

# --- Upload & Solve ---

if option == 'Upload & Solve':
    uploaded_file = st.file_uploader('Upload Sudoku File', type=['txt','csv'])
    
    if uploaded_file:
        try:
            board = parse_upload_file(uploaded_file)
            st.success('Puzzle loaded successfully!')
            display_sudoku_grid(board, 'Input Puzzle')
            
            if st.button('Solve Puzzle'):
                if solve_sudoku(board):
                    display_sudoku_grid(board, 'Solved Puzzle')
                else:
                    st.error('No solution found.')
        except Exception as e:
            st.error(f'Error parsing file: {e}')

# --- Generate ---
elif option == 'Generate Puzzle':
    difficulty = st.selectbox('Select difficulty', ['easy','medium','hard'])
    
    if st.button('Generate Puzzle'):
        puzzle, solution = generate_sudoku(difficulty)
        st.session_state["generated_puzzle"] = puzzle
        st.session_state["generated_solution"] = solution
        if 'generated_puzzle' in st.session_state:
            display_sudoku_grid(st.session_state["generated_puzzle"], f" {difficulty.title()} Puzzle")
