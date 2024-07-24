import tkinter as tk

def show_frame(frame):
    frame.tkraise()

root = tk.Tk()
root.geometry("400x300")

container = tk.Frame(root)
container.pack(fill="both", expand=True)

frame1 = tk.Frame(container, bg="red")
frame2 = tk.Frame(container, bg="blue")
frame3 = tk.Frame(container, bg="green")

label1 = tk.Label(frame1, text="Frame 1")
button1 = tk.Button(frame1, text="Show Frame 2", command=lambda: show_frame(frame2))

label2 = tk.Label(frame2, text="Frame 2")
button2 = tk.Button(frame2, text="Show Frame 3", command=lambda: show_frame(frame3))

label3 = tk.Label(frame3, text="Frame 3")
button3 = tk.Button(frame3, text="Show Frame 1", command=lambda: show_frame(frame1))

label1.pack()
button1.pack()
label2.pack()
button2.pack()
label3.pack()
button3.pack()

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky="nsew")

# Configure rows and columns to expand with the window
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

show_frame(frame1)

root.mainloop()
