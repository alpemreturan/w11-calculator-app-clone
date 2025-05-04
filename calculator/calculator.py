#Making Windows 11 Standard calculator with CustomTkinter in Python **credits: github.com/alpemreturan
import customtkinter
from tkinter import *
from math import sqrt
import os
import sys

WIDTH = 500
HEIGHT = 700

op_color = "#333333"
digits_color = "#454545"

if hasattr(sys, "_MEIPASS"):
    icon_path = os.path.join(sys._MEIPASS, "icon.ico")
else:
    icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.title("Calculator")
        self.iconbitmap((icon_path))

        self.entry = customtkinter.CTkEntry(self,
        width=200, 
        height=40, 
        font=("Roboto", 50), 
        corner_radius=7, 
        placeholder_text="0", 
        text_color="white", 
        fg_color=digits_color, 
        border_width=5, 
        border_color=op_color
        )

        self.entry.grid(row=0, column=0, columnspan= 5, padx=10, pady=10, sticky="nsew")
        self.entry.configure(validate="key", validatecommand=(self.register(self.validate_input), "%P"))

        for i in range(8): 
            self.grid_rowconfigure(i, weight=1)
        for j in range(5):  
            self.grid_columnconfigure(j, weight=1)

        self.button_0 = customtkinter.CTkButton(self, 
        text="0",
        font=("Roboto", 35), 
        fg_color=digits_color, 
        hover_color=op_color, 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=lambda: self.button_click("0"),
        )
        self.button_0.grid(row=7, column=1, padx=3, pady=3, sticky="nsew")

        self.button_1 = customtkinter.CTkButton(self, 
        text="1",
        font=("Roboto", 35), 
        fg_color=digits_color, 
        hover_color=op_color, 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=lambda: self.button_click("1"),
        )
        self.button_1.grid(row=6, column=0, padx=3, pady=3, sticky="nsew")

        self.button_2 = customtkinter.CTkButton(self, 
        text="2",
        font=("Roboto", 35), 
        fg_color=digits_color, 
        hover_color=op_color, 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=lambda: self.button_click("2"),
        )
        self.button_2.grid(row=6, column=1, padx=3, pady=3, sticky="nsew")

        self.button_3 = customtkinter.CTkButton(self, 
        text="3",
        font=("Roboto", 35), 
        fg_color=digits_color, 
        hover_color=op_color, 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=lambda: self.button_click("3"),
        )
        self.button_3.grid(row=6, column=2, padx=3, pady=3, sticky="nsew")

        self.button_4= customtkinter.CTkButton(self, 
        text="4",
        font=("Roboto", 35), 
        fg_color=digits_color, 
        hover_color=op_color, 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=lambda: self.button_click("4"),
        )
        self.button_4.grid(row=5, column=0, padx=3, pady=3, sticky="nsew")

        self.button_5= customtkinter.CTkButton(self, 
        text="5",
        font=("Roboto", 35), 
        fg_color=digits_color, 
        hover_color=op_color, 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=lambda: self.button_click("5"),
        )
        self.button_5.grid(row=5, column=1, padx=3, pady=3, sticky="nsew")

        self.button_6= customtkinter.CTkButton(self, 
        text="6",
        font=("Roboto", 35), 
        fg_color=digits_color, 
        hover_color=op_color, 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=lambda: self.button_click("6"),
        )
        self.button_6.grid(row=5, column=2, padx=3, pady=3, sticky="nsew")

        self.button_7= customtkinter.CTkButton(self, 
        text="7",
        font=("Roboto", 35), 
        fg_color=digits_color, 
        hover_color=op_color, 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=lambda: self.button_click("7"),
        )
        self.button_7.grid(row=4, column=0, padx=3, pady=3, sticky="nsew")

        self.button_8= customtkinter.CTkButton(self, 
        text="8",
        font=("Roboto", 35), 
        fg_color=digits_color, 
        hover_color=op_color, 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=lambda: self.button_click("8"),
        )
        self.button_8.grid(row=4, column=1, padx=3, pady=3, sticky="nsew")

        self.button_9= customtkinter.CTkButton(self, 
        text="9",
        font=("Roboto", 35), 
        fg_color=digits_color, 
        hover_color=op_color, 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=lambda: self.button_click("9"),
        )
        self.button_9.grid(row=4, column=2, padx=3, pady=3, sticky="nsew")

        self.button_brackets = customtkinter.CTkButton(self, 
        text="( )",
        font=("Roboto", 35), 
        fg_color=digits_color, 
        hover_color=op_color, 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=self.button_click_brackets
        )
        self.button_brackets.grid(row=7, column=0, padx=3, pady=3, sticky="nsew")

        self.button_decimal = customtkinter.CTkButton(self, 
        text=".",
        font=("Roboto", 35), 
        fg_color=digits_color, 
        hover_color=op_color, 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=lambda: self.button_click(".")
        )
        self.button_decimal.grid(row=7, column=2, padx=3, pady=3, sticky="nsew")

        self.button_equal = customtkinter.CTkButton(self, 
        text="=",
        font=("Roboto", 35), 
        fg_color="#00A2E8", 
        hover_color="#008DC9", 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=self.button_click_equal
        )
        self.button_equal.grid(row=7, column=3, columnspan = 2, padx=3, pady=3, sticky="nsew")

        self.button_addition = customtkinter.CTkButton(self, 
        text="+",
        font=("Roboto", 35), 
        fg_color="yellow", 
        hover_color="#DBDB00", 
        text_color="gray", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=lambda: self.button_click("+")
        )
        self.button_addition.grid(row=6, column=3, columnspan = 2, padx=3, pady=3, sticky="nsew")

        self.button_subtraction = customtkinter.CTkButton(self, 
        text="—",
        font=("Roboto", 35), 
        fg_color="red", 
        hover_color="#AD1E1E", 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=lambda: self.button_click("-")
        )
        self.button_subtraction.grid(row=5, column=3, columnspan = 2, padx=3, pady=3, sticky="nsew")

        self.button_multiplication = customtkinter.CTkButton(self, 
        text="×",
        font=("Roboto", 35), 
        fg_color="green", 
        hover_color="#007000", 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=lambda: self.button_click("×")
        )
        self.button_multiplication.grid(row=4, column=3, columnspan = 2, padx=3, pady=3, sticky="nsew")

        self.button_dividing = customtkinter.CTkButton(self, 
        text="÷",
        font=("Roboto", 35), 
        fg_color="#8D00E6", 
        hover_color="purple", 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=lambda: self.button_click("÷")
        )
        self.button_dividing.grid(row=3, column=3, columnspan = 2, padx=3, pady=3, sticky="nsew")

        self.button_squareroot = customtkinter.CTkButton(self, 
        text="√",
        font=("Roboto", 35), 
        fg_color=op_color, 
        hover_color=digits_color, 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=self.button_click_squareroot
        )
        self.button_squareroot.grid(row=3, column=2, padx=3, pady=3, sticky="nsew")

        self.button_exponentiaton = customtkinter.CTkButton(self, 
        text="xʸ",
        font=("Roboto", 35), 
        fg_color=op_color, 
        hover_color=digits_color, 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=lambda: self.button_click("^")
        )
        self.button_exponentiaton.grid(row=3, column=1, padx=3, pady=3, sticky="nsew")

        self.button_percent = customtkinter.CTkButton(self, 
        text="%",
        font=("Roboto", 35), 
        fg_color=op_color, 
        hover_color=digits_color, 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=lambda: self.button_click("%")
        )
        self.button_percent.grid(row=3, column=0, padx=3, pady=3, sticky="nsew")

        self.button_reset = customtkinter.CTkButton(self, 
        text="C",
        font=("Roboto", 35), 
        fg_color=op_color, 
        hover_color=digits_color, 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=self.button_click_reset
        )
        self.button_reset.grid(row=2, column=0, padx=3, pady=3, sticky="nsew")

        self.button_clear = customtkinter.CTkButton(self, 
        text="␡",
        font=("Roboto", 35), 
        fg_color=op_color, 
        hover_color=digits_color, 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=self.button_click_clear
        )
        self.button_clear.grid(row=2, column=3, columnspan=2, padx=3, pady=3, sticky="nsew")

        self.button_theme = customtkinter.CTkButton(self, 
        text="🔦",
        font=("Roboto", 35), 
        fg_color=op_color, 
        hover_color=digits_color, 
        text_color="white", 
        width=40, 
        height=25, 
        corner_radius=7, 
        command=self.button_click_theme
        )
        self.button_theme.grid(row=2, column=1, columnspan=2, padx=3, pady=3, sticky="nsew")

    def validate_input(self, new_value):
        allowed_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "×", "÷", "%", "(", ")", "√", "^", "/", "."]
        for char in new_value: 
            if char not in allowed_characters:  
                return False
        return True  
    
    def button_click(self, symbol):
        cursor_position = self.entry.index("insert")
        self.entry.insert(cursor_position, symbol)

    def button_click_brackets(self):
        current_text = self.entry.get()
        open_count = current_text.count("(")
        close_count = current_text.count(")")

        cursor_position = self.entry.index("insert")

        if open_count > close_count:
            self.entry.insert(cursor_position, ")")
        else:
            self.entry.insert(cursor_position, "(")

    def button_click_squareroot(self):
        cursor_position = self.entry.index("insert")
        self.entry.insert(cursor_position, "√()")
        self.entry.icursor(cursor_position + 2) 

    def button_click_equal(self):
        try:
            current_data = self.entry.get()
            current_data = current_data.replace("×", "*").replace("÷", "/").replace("%", "/100*").replace("√", "sqrt").replace("^", "**")
            result = eval(current_data)

            self.entry.delete(0, "end")
            self.entry.insert("end", str(result))          
        except:
            self.entry.delete(0, "end")

    def button_click_clear(self):
        cursor_position = self.entry.index("insert")
        self.entry.delete(cursor_position - 1, cursor_position)

    def button_click_reset(self):
        self.entry.delete(0, END)

    def button_click_theme(self):
        if not hasattr(self, "current_theme"):
            self.current_theme = "dark"

        if self.current_theme == "dark":
            customtkinter.set_appearance_mode("light")
            self.current_theme = "light"
        else:
            customtkinter.set_appearance_mode("dark")
            self.current_theme = "dark"

app = App()
app.mainloop()