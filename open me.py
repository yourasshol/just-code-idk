import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello World Animation")
root.geometry("400x300")
root.configure(bg="white")

# Create the label
label = tk.Label(root, text="Hello, World!", font=("Arial", 24), bg="white")
label.place(x=120, y=100)

# Animation variables
y = 100
direction = 1

def animate():
    global y, direction
    y += direction * 2
    if y > 200 or y < 50:
        direction *= -1
    label.place(x=120, y=y)
    root.after(20, animate)

# Start animation
animate()

# Run the app
root.mainloop()
