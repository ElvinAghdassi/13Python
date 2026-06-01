import tkinter as tk

root = tk.Tk()
root.title("Tk Example")
root.geometry("1000x1000+100+100")



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        description_button = tk.Button(root, text="Description", command=self.description)
        description_button.pack()

        area_button = tk.Button(root, text="Area", command=self.area_calc)
        area_button.pack()
        pass

    def description(self):
        print(f"Rectangle with a width of {self.width} and a height of {self.height}")
        return self.width, self.height
    
    def area_calc(self):
        area = self.width * self.height
        print(f"Your Rectange has an area of {area} units^2")
        return area
        
    def perimeter_calc(self):
        perimeter = 2*self.width + 2*self.height
        print(f"Your Rectange has a perimeter of {perimeter}")
        return perimeter
    

if __name__ == "__main__":
    myRec = Rectangle(10, 10)
    root.mainloop()
