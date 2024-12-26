import tkinter as tk
from tkinter import ttk, messagebox
from controller import stockmanager

# Initialize database connection
host = "localhost"
user = "root"
password = ""
database = "stocks"
stock_obj = stockmanager(host, user, password, database)

class StockManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Management System")
        self.root.geometry("900x700")
        self.root.configure(bg="#f4f4f4")

        # Create title label
        title = tk.Label(self.root, text="Stock Management System", font=("Arial", 24, "bold"), bg="#004d99", fg="white")
        title.pack(side=tk.TOP, fill=tk.X)

        # Frames for inputs and buttons
        input_frame = tk.Frame(self.root, bd=4, relief=tk.RIDGE, bg="#e6f2ff")
        input_frame.place(x=10, y=70, width=400, height=250)

        table_frame = tk.Frame(self.root, bd=4, relief=tk.RIDGE, bg="#e6f2ff")
        table_frame.place(x=420, y=70, width=460, height=580)

        button_frame = tk.Frame(self.root, bd=4, relief=tk.RIDGE, bg="#e6f2ff")
        button_frame.place(x=10, y=330, width=400, height=150)

        # Input fields
        self.name_var = tk.StringVar()
        self.qty_var = tk.StringVar()
        self.price_var = tk.StringVar()

        tk.Label(input_frame, text="Product Name:", font=("Arial", 14), bg="#e6f2ff").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(input_frame, textvariable=self.name_var, font=("Arial", 14), width=20).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(input_frame, text="Quantity:", font=("Arial", 14), bg="#e6f2ff").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(input_frame, textvariable=self.qty_var, font=("Arial", 14), width=20).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(input_frame, text="Price:", font=("Arial", 14), bg="#e6f2ff").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(input_frame, textvariable=self.price_var, font=("Arial", 14), width=20).grid(row=2, column=1, padx=10, pady=10)

        # Buttons
        tk.Button(button_frame, text="Add", command=self.add_stock, font=("Arial", 14), bg="#009933", fg="white", width=10).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(button_frame, text="Update", command=self.update_stock, font=("Arial", 14), bg="#0066cc", fg="white", width=10).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(button_frame, text="Delete", command=self.delete_stock, font=("Arial", 14), bg="#cc0000", fg="white", width=10).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(button_frame, text="Retrieve", command=self.retrieve_stock, font=("Arial", 14), bg="#ff9900", fg="white", width=10).grid(row=1, column=1, padx=10, pady=10)

        # Table to display stocks
        self.stock_table = ttk.Treeview(table_frame, columns=("Name", "Quantity", "Price"), show="headings")
        self.stock_table.heading("Name", text="Name")
        self.stock_table.heading("Quantity", text="Quantity")
        self.stock_table.heading("Price", text="Price")
        self.stock_table.column("Name", width=150)
        self.stock_table.column("Quantity", width=100)
        self.stock_table.column("Price", width=100)
        self.stock_table.pack(fill=tk.BOTH, expand=1)

        # Add scrollbar to the table
        scroll_y = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.stock_table.yview)
        self.stock_table.configure(yscrollcommand=scroll_y.set)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        # Bind row selection to an event
        self.stock_table.bind("<ButtonRelease-1>", self.fill_input_fields)

    def add_stock(self):
        name = self.name_var.get()
        qty = self.qty_var.get()
        price = self.price_var.get()

        if not name or not qty or not price:
            messagebox.showerror("Input Error", "All fields are required")
            return

        try:
            stock_obj.add(name, qty, price)
            messagebox.showinfo("Success", "Stock added successfully")
            self.clear_fields()
            self.retrieve_stock()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_stock(self):
        name = self.name_var.get()
        qty = self.qty_var.get()
        price = self.price_var.get()

        if not name or not qty or not price:
            messagebox.showerror("Input Error", "All fields are required")
            return

        try:
            stock_obj.update(name, qty, price)
            messagebox.showinfo("Success", "Stock updated successfully")
            self.clear_fields()
            self.retrieve_stock()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_stock(self):
        name = self.name_var.get()

        if not name:
            messagebox.showerror("Input Error", "Name field is required")
            return

        try:
            stock_obj.delete(name)
            messagebox.showinfo("Success", "Stock deleted successfully")
            self.clear_fields()
            self.retrieve_stock()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def retrieve_stock(self):
        try:
            self.stock_table.delete(*self.stock_table.get_children())
            result = stock_obj.retrive_data()
            for row in result:
                self.stock_table.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def fill_input_fields(self, event):
        try:
            selected_item = self.stock_table.selection()[0]  # Get selected row ID
            values = self.stock_table.item(selected_item, "values")  # Get row values
            self.name_var.set(values[0])  # Set Name
            self.qty_var.set(values[1])  # Set Quantity
            self.price_var.set(values[2])  # Set Price
        except IndexError:
            pass

    def clear_fields(self):
        self.name_var.set("")
        self.qty_var.set("")
        self.price_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = StockManagementApp(root)
    root.mainloop()
