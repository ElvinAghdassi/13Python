import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests


class User:
    def __init__(self, weight, weight_goal):
        self.weight = weight
        self.weight_goal = weight_goal


class Calorie_API:
    BASE_URL = "https://api.calorieninjas.com/v1/nutrition?query="
    API_KEY = "/Lb0Y6CjWcapKYvOn9GC4w==qKmmqwGZhSpxfe6n"

    def calorie_program_calculator(self, weight, weight_goal):
        maintenance = weight * 33
        if weight_goal < weight:
            goal = maintenance - 500
        elif weight_goal > weight:
            goal = maintenance + 300
        else:
            goal = maintenance
        return max(int(goal), 1200)

    def fetch_nutrition(self, query):
        response = requests.get(
            self.BASE_URL + query,
            headers={"X-Api-Key": self.API_KEY},
            timeout=8,
        )
        if response.status_code == requests.codes.ok:
            return response.json().get("items", [])
        else:
            raise ConnectionError(
                f"API error {response.status_code}: {response.text}"
            )


class Calorie_Tracker_App:
    def __init__(self, root):
        self.root = root
        self.root.title("Calorie Tracker")
        self.root.geometry("800x800+800+200")
        self.root.maxsize(800, 800)
        self.root.minsize(800, 800)

        self.calorie_goal_var = tk.IntVar(value=0)
        self.calories_consumed_var = tk.DoubleVar(value=0.0)
        self.calorie_api = Calorie_API()

        self.create_title()
        self.create_frames()
        self.create_widgets()

    # ------------------------------------------------------------------ #
    #  Helpers                                                             #
    # ------------------------------------------------------------------ #

    def make_window(self, title):
        """Create a standard 800x800 Toplevel."""
        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry("800x800+800+200")
        win.maxsize(800, 800)
        win.minsize(800, 800)
        return win

    def add_return_button(self, parent, window):
        """Add a 'Return to Menu' button that closes the given window."""
        tk.Button(
            parent,
            text="Return to Menu",
            font=("Arial", 13),
            width=20,
            command=window.destroy,
        ).pack(pady=(20, 10))

    # ------------------------------------------------------------------ #
    #  Main menu                                                           #
    # ------------------------------------------------------------------ #

    def create_title(self):
        tk.Label(self.root, text="Calorie Tracker", font=("Arial", 22)).pack(pady=(20, 5))
        tk.Label(self.root, text="Welcome", font=("Arial", 16)).pack(pady=(0, 20))

    def create_frames(self):
        self.input_frame = tk.Frame(self.root, padx=20, pady=10)
        self.display_frame = tk.Frame(self.root, padx=20, pady=10)
        self.button_frame = tk.Frame(self.root, padx=20, pady=10)
        self.input_frame.pack(fill="x")
        self.display_frame.pack(fill="x")
        self.button_frame.pack(fill="x")

    def create_widgets(self):
        for text, cmd in [
            ("Set Calorie Program", self.open_calorie_program),
            ("View Daily Progress", self.open_calorie_progress),
            ("Enter Calories", self.open_enter_calories),
        ]:
            tk.Button(
                self.button_frame,
                text=text,
                font=("Arial", 16),
                height=3,
                width=30,
                command=cmd,
            ).pack(pady=5)

    # ------------------------------------------------------------------ #
    #  Set Calorie Program                                                 #
    # ------------------------------------------------------------------ #

    def open_calorie_program(self):
        program = self.make_window("Calorie Program")

        tk.Label(program, text="Set Calorie Program", font=("Arial", 22)).pack(pady=(20, 5))

        tk.Label(program, text="Enter your current weight (kg):", font=("Arial", 16)).pack(pady=(20, 5))
        self.weight_entry = tk.Entry(program, font=("Arial", 16))
        self.weight_entry.pack(pady=(0, 20))

        tk.Label(program, text="Enter your goal weight (kg):", font=("Arial", 16)).pack(pady=(0, 5))
        self.weight_goal_entry = tk.Entry(program, font=("Arial", 16))
        self.weight_goal_entry.pack(pady=(0, 30))

        self.program_result_label = tk.Label(program, text="", font=("Arial", 15), fg="#2a7d4f")
        self.program_result_label.pack(pady=(0, 10))

        tk.Button(
            program,
            text="Calculate & Save",
            font=("Arial", 16),
            height=3,
            width=30,
            command=lambda: self.calorie_program_validator(program),
        ).pack(pady=(0, 10))

        self.add_return_button(program, program)

    def calorie_program_validator(self, window):
        weight_str = self.weight_entry.get().strip()
        goal_str = self.weight_goal_entry.get().strip()
        try:
            weight = float(weight_str)
            weight_goal = float(goal_str)
            if weight <= 0 or weight_goal <= 0:
                messagebox.showwarning("Warning", "Please enter a positive weight. Try again!")
                return
            goal_kcal = self.calorie_api.calorie_program_calculator(weight, weight_goal)
            self.calorie_goal_var.set(goal_kcal)
            direction = (
                "cutting" if weight_goal < weight
                else "bulking" if weight_goal > weight
                else "maintenance"
            )
            messagebox.showinfo(
                "Calorie Goal Set",
                f"Daily calorie goal set to {goal_kcal} kcal\n({direction} programme)"
            )
            window.destroy()   # close and return to menu after saving
        except ValueError:
            messagebox.showwarning("Warning", "Please enter numeric weights. Try again!")

    # ------------------------------------------------------------------ #
    #  View Daily Progress                                                 #
    # ------------------------------------------------------------------ #

    def open_calorie_progress(self):
        progress = self.make_window("Daily Progress")

        tk.Label(progress, text="Daily Calorie Progress", font=("Arial", 22)).pack(pady=(20, 5))

        content = tk.Frame(progress)
        content.pack(pady=20)

        tk.Label(content, text="Calorie Goal", font=("Arial", 18)).grid(row=0, column=0, padx=60)
        tk.Label(content, text="Calories Consumed", font=("Arial", 18)).grid(row=0, column=1, padx=60)

        tk.Label(
            content,
            text=f"{self.calorie_goal_var.get()} kcal",
            font=("Arial", 16),
        ).grid(row=1, column=0, pady=(10, 30))

        tk.Label(
            content,
            text=f"{self.calories_consumed_var.get():.0f} kcal",
            font=("Arial", 16),
        ).grid(row=1, column=1, pady=(10, 30))

        try:
            goal = self.calorie_goal_var.get()
            consumed = self.calories_consumed_var.get()
            percent = (consumed / goal * 100) if goal > 0 else 0
        except Exception:
            percent = 0

        progressbar = ttk.Progressbar(progress, orient="horizontal", length=600, mode="determinate")
        progressbar.pack(pady=(10, 5))
        progressbar["value"] = min(max(percent, 0), 100)

        if percent >= 100:
            colour, status = "#c0392b", "Goal reached!"
        elif percent >= 75:
            colour, status = "#e67e22", f"{percent:.1f}% of goal"
        else:
            colour, status = "#27ae60", f"{percent:.1f}% of goal"

        tk.Label(progress, text=status, font=("Arial", 14), fg=colour).pack()

        if goal == 0:
            tk.Label(
                progress,
                text="Set your calorie goal first via 'Set Calorie Program'.",
                font=("Arial", 12),
                fg="grey",
            ).pack(pady=(10, 0))

        self.add_return_button(progress, progress)

    # ------------------------------------------------------------------ #
    #  Enter Calories                                                      #
    # ------------------------------------------------------------------ #

    def open_enter_calories(self):
        window = self.make_window("Enter Calories")

        tk.Label(window, text="Enter Calories", font=("Arial", 22)).pack(pady=(20, 5))

        tk.Label(window, text="Describe what you ate:", font=("Arial", 16)).pack(pady=(20, 5))
        self.food_entry = tk.Entry(window, font=("Arial", 16), width=35)
        self.food_entry.pack(pady=(0, 10))

        self.calories_result_label = tk.Label(window, text="", font=("Arial", 14), fg="#2a7d4f")
        self.calories_result_label.pack(pady=(5, 5))

        tk.Button(
            window,
            text="Add Calories",
            font=("Arial", 16),
            height=3,
            width=30,
            command=self.submit_calories,
        ).pack(pady=(10, 5))

        self.add_return_button(window, window)

    def submit_calories(self):
        query = self.food_entry.get().strip()
        if not query:
            messagebox.showwarning("Warning", "Please describe what you ate.")
            return
        try:
            items = self.calorie_api.fetch_nutrition(query)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return
        if not items:
            messagebox.showwarning("Warning", "No results found. Try a different description.")
            return

        total_kcal = sum(item.get("calories", 0) for item in items)
        self.calories_consumed_var.set(self.calories_consumed_var.get() + total_kcal)
        self.calories_result_label.config(
            text=f"+{total_kcal:.0f} kcal added  |  Today's total: {self.calories_consumed_var.get():.0f} kcal"
        )
        self.food_entry.delete(0, tk.END)

    def update_display(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = Calorie_Tracker_App(root)
    root.mainloop()