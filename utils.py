import numpy as np

def parse_upload_file(file):
    content = file.read().decode('utf-8').strip()
    lines = content.split('\n')
    board = []
    for line in lines:
        row = [int(x) if x.isdigit() else 0 for x in line.strip().split()]
        board.append(row)
    return np.array(board)

def print_board(board):
    for i in range(9):
        if i%3 == 0 and i != 0:
            print('-'*21)
        for j in range(9):
            if j%3 ==0 and j != 0:
                print('|', end=' ')
            print(board[i][j] if board[i][j] != 0 else '.', end=' ')
        print()
import streamlit as st


def display_sudoku_grid(board, title="Sudoku Grid"):
    st.markdown(f"### {title}")

    grid_html = """
    <style>
    .sudoku-table {
        border-collapse: collapse;
        margin: auto;
    }
    .sudoku-cell {
        width: 40px;
        height: 40px;
        text-align: center;
        vertical-align: middle;
        font-size: 20px;
        border: 1px solid #ccc;
    }
    </style>
    <table class="sudoku-table">
    """

    for i in range(9):
        grid_html += "<tr>"
        for j in range(9):
            value = board[i][j]
            display_value = str(value) if value != 0 else "&nbsp;"
            
            style = "border: 1px solid #ccc;"

            # Add bold borders for 3x3 boxes
            if i % 3 == 0:
                style += "border-top: 3px solid white;"
            if j % 3 == 0:
                style += "border-left: 3px solid white;"
            if i == 8:
                style += "border-bottom: 3px solid white;"
            if j == 8:
                style += "border-right: 3px solid white;"

            grid_html += f'<td class="sudoku-cell" style="{style}">{display_value}</td>'
        grid_html += "</tr>"

    grid_html += "</table>"

    st.markdown(grid_html, unsafe_allow_html=True)
