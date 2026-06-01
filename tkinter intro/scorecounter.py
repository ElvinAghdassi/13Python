import tkinter as tk

root = tk.Tk()
root.title("Tk Example")
root.configure(background="white")
root.geometry("200x200+100+100")

score = 0

def score_up():
    global score
    print("Score increased by +1")
    score += 1
    score_label.config(text=score)


    
def score_down():
    global score
    print("Score decreased by -1")
    score -= 1
    score_label.config(text=score)


point_up = tk.Button(root, text="+", command=score_up)
point_up.pack()

point_down = tk.Button(root, text="-", command=score_down)
point_down.pack()

score_label = tk.Label(root, text=score)
score_label.pack()

root.mainloop()