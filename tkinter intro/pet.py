import tkinter as tk

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 100
        self.mood = "Okay"
        
        self.status_label = tk.Label(root, text=f"Welcome! This is {self.name}", bg="white", wraplength=180)
        self.hunger_label = tk.Label(root, text=f"Hunger : {self.hunger}")
        self.energy_label = tk.Label(root, text=f"Energy : {self.energy}")
        self.mood_label = tk.Label(root, text=f"{self.name} is {self.mood}")
        self.status_label.pack(pady=10)
        self.hunger_label.pack()
        self.energy_label.pack()
        self.mood_label.pack()

    def update_status(self, message):
        self.status_label.config(text=message)
        self.hunger_label.config(text=f"Hunger : {self.hunger}")
        self.energy_label.config(text=f"Energy : {self.energy}")
        self.mood_label.config(text=f"{self.name} is {self.mood}")

    def feed_pet(self):
        if self.hunger < 100:
            self.hunger += 10
            if self.hunger > 100: self.hunger = 100
            self.update_status(f"{self.name} now has a hunger of {self.hunger}.")
        else:
            self.update_status(f"{self.name} is not hungry, try again later")
        
        self.pet_mood()

    def play_pet(self):
        min_limit = 0
        if self.energy < 20:
            self.update_status(f"{self.name} is too tired to play right now.")
        elif self.hunger < 20:
            self.update_status(f"{self.name} is too hungry to play right now.")
        else:
            self.energy -= 20
            self.hunger -= 20
            if self.energy < min_limit: self.energy = min_limit
            if self.hunger < min_limit: self.hunger = min_limit
            self.update_status(f"{self.name} played!\nEnergy: {self.energy} | Hunger: {self.hunger}")
        self.pet_mood()

    def rest_pet(self):
        max_limit = 100
        if self.energy < 100:
            self.energy += 40
            if self.energy > max_limit: self.energy = max_limit
            self.update_status(f"{self.name} is rested. Energy: {self.energy}")
            
        else:
            self.update_status(f"{self.name} is already rested")
        self.pet_mood()

    def pet_mood(self):
        if self.hunger >= 80 and self.energy >= 80:
            self.mood = "Happy"
        elif self.hunger <= 30:
            self.mood = "Hungry"
        elif self.energy <= 30:
            self.mood = "Tired"
        else:
            self.mood = "Okay"
        self.mood_label.config(text=f"{self.name} is {self.mood}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pet")
    root.configure(background="white")
    root.geometry("250x300+100+100")

    myPet = Pet("Xavier")

    tk.Button(root, text="Feed Pet", width=15, command=myPet.feed_pet).pack(pady=5)
    tk.Button(root, text="Play with Pet", width=15, command=myPet.play_pet).pack(pady=5)
    tk.Button(root, text="Rest Pet", width=15, command=myPet.rest_pet).pack(pady=5)

    root.mainloop()