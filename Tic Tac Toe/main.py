import tkinter as tk
from tkinter import messagebox

# Check for a winner
def check_winner(): 
    for i in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
        if buttons[i[0]]["text"] == buttons[i[1]]["text"] == buttons[i[2]]["text"] != "":
            buttons[i[0]].config(bg="green")
            buttons[i[1]].config(bg="green")
            buttons[i[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"player {buttons[i[0]]['text']} wins!")
            root.quit()

    # Check for a tie
    if buttons[0]["text"] != "" and buttons[1]["text"] != "" and buttons[2]["text"] != "" and buttons[3]["text"] != "" and buttons[4]["text"] != "" and buttons[5]["text"] != "" and buttons[6]["text"] != "" and buttons[7]["text"] != "" and buttons[8]["text"] != "":
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        root.quit()

# Handle button click event
def button_click(index):
    if buttons[index]["text"] == "" and not check_winner():
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()

# Toggle between players
def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player: {current_player}'s Turn")

# Initialize the main application window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create buttons for the Tic-Tac-Toe grid
buttons = [tk.Button(root, text="", font=('normal', 30), width=5, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)

# Initialize the current player to "X"
current_player = "X" 
winner = False

label = tk.Label(root, text=f"Player: {current_player}'s Turn", font=('normal', 20)) 
label.grid(row=3, column=0, columnspan=3) 

root.mainloop()
