from tkinter import messagebox
import tkinter as tk


class PizzaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pizza Order App")
        self.geometry("400x400")

        self.style_var = tk.StringVar()
        self.style_var.set(1)
        self.sauce_var = tk.StringVar()
        self.sauce_var.set(1)
        self.toppings_vars = []
        
        self.toppings_costs = {
            "Pepperoni": 1.5,
            "Mushrooms": 1.0,
            "Olives": 0.75,
            "Onions": 0.5,
            "Mozzarella": 0.5,
            "Chicken": 1.5,
            "Bacon" : 1.0,
        }
        
        self.total_cost_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Choose Pizza Style:").pack(anchor=tk.W)
        self.create_style_radiobutton("American 7.0$")
        self.create_style_radiobutton("Italian 7.0$")

        tk.Label(self, text="Choose Sauce:").pack(anchor=tk.W)
        self.create_sauce_radiobutton("Tomato")
        self.create_sauce_radiobutton("Garlic")

        tk.Label(self, text="Choose Toppings (4):").pack(anchor=tk.W)
        self.create_topping_checkbox("Pepperoni 1.5$")
        self.create_topping_checkbox("Mushrooms 1.0$")
        self.create_topping_checkbox("Olives 0.75$")
        self.create_topping_checkbox("Onions 0.5$")
        self.create_topping_checkbox("Mozzarella 0.5$")
        self.create_topping_checkbox("Chicken 1.5$")
        self.create_topping_checkbox("Bacon 1.0$")

        tk.Button(self, text="Confirm Order", command=self.show_order).pack()

    def create_style_radiobutton(self, text):
        tk.Radiobutton(self, text=text, variable=self.style_var, value=text).pack(
            anchor=tk.W
        )

    def create_sauce_radiobutton(self, text):
        tk.Radiobutton(self, text=text, variable=self.sauce_var, value=text).pack(
            anchor=tk.W
        )

    def create_topping_checkbox(self, text):
        var = tk.IntVar()
        checkbox = tk.Checkbutton(self, text=text, variable=var)
        checkbox.pack(anchor=tk.W)
        self.toppings_vars.append(var)
        print("Toppings Vars:", self.toppings_vars)
        print("Toppings Length:", len(self.toppings_vars))

    def show_order(self):
        style = self.style_var.get()
        sauce = self.sauce_var.get()
        toppings = [
            var.get() for var in self.toppings_vars
        ]

        print("Toppings:", toppings)

        selected_toppings = [
            topping
            for topping, selected in zip(
                [
                    "Pepperoni",
                    "Mushrooms",
                    "Olives",
                    "Onions",
                    "Mozzarella",
                    "Chicken",
                    "Bacon",
                ],
                toppings,
            )
            if selected
        ]

        print("Selected Toppings:", selected_toppings)
        print("Selected Toppings Length:", len(selected_toppings))

        if not style or not sauce or len(selected_toppings) != 4:
            messagebox.showwarning("Incomplete Order", "Please select all options.")
        else:
            base_cost = 7.0
            topping_costs = [self.toppings_costs[topping] for topping in selected_toppings]
            total_cost = base_cost + sum(topping_costs)
            order_summary = f"Your Pizza Order:\nStyle: {style}\nSauce: {sauce}\nToppings: {', '.join(selected_toppings)} \nTotal Cost: {total_cost}$"
            messagebox.showinfo("Order Confirmation", order_summary)


if __name__ == "__main__":
    app = PizzaApp()
    app.mainloop()
