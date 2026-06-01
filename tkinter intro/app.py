import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Tk Example")
root.configure(background="yellow")
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("1000x1000+100+100")

# Create two labels
tk.Label(root, text="Nothing will work unless you do.").pack()
tk.Label(root, text="- Maya Angelou").pack()

image = tk.Image(file="pionel_pessi.png")
label = tk.Label(root, image=image)



print(f"hello i smell")
label.pack()

root.mainloop()     