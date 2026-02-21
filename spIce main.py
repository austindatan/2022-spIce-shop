import tkinter as tk
from tkinter import LEFT, RIGHT, VERTICAL, Y, ttk, messagebox, NO, simpledialog
from PIL import Image, ImageTk
import mysql.connector
from tkinter.ttk import Treeview

root = tk.Tk()
root.title("S P I C E")
root.geometry("1220x620")
root.resizable(False, False)

mydb = mysql.connector.connect(
    user="root",
    host="127.0.0.1",
    password="austinreverie",
    database="spice")
db = mydb.cursor(buffered=True)

canvas_frame = tk.Canvas(root, bg='#FFEDBF', highlightthickness=0, width=850, height=620)
canvas_frame.pack(side=LEFT, expand=False)

scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=canvas_frame.yview)
scrollbar.pack(side=RIGHT, fill=Y)

def update_scrollregion():
    second_frame.update_idletasks()
    canvas_frame.configure(scrollregion=canvas_frame.bbox("all"))
canvas_frame.configure(yscrollcommand=scrollbar.set)
canvas_frame.bind('<Configure>', lambda e: update_scrollregion())

second_frame = tk.Frame(canvas_frame, bg='#FFEDBF')
canvas_frame.create_window((0, 0), window=second_frame, anchor="nw")
second_frame.lower()

non_scrollable_frame = tk.Frame(root, bg='#79E4DF', width=200)
non_scrollable_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

ss_icecream = Image.open("assets/ice_cream.png")
ss_icecream_resize = ss_icecream.resize((850, 480))
ss_icecream_convert = ImageTk.PhotoImage(ss_icecream_resize)
ss_donuts = Image.open("assets/donuts.png")
ss_donuts_resize = ss_donuts.resize((850, 480))
ss_donuts_convert = ImageTk.PhotoImage(ss_donuts_resize)
ss_fried_chicken = Image.open("assets/pride.png")
ss_fried_chicken_resize = ss_fried_chicken.resize((850, 480))
ss_fried_chicken_convert = ImageTk.PhotoImage(ss_fried_chicken_resize)

slideshow_assets = tk.Label(second_frame,borderwidth=0, highlightthickness=0)
home_screen_line = tk.Label(second_frame,borderwidth=0, highlightthickness=0, width=850, height=3, bg='#FCB7BA')
slideshow_assets.pack()
slideshow_timer = 1

username_entry = tk.Entry(non_scrollable_frame)
username = username_entry.get()

def no_user():
    username = username_entry.get()
    if username == "":
        messagebox.showwarning("Warning!", "Login first to continue")

def check_user_checkout():
    username = username_entry.get()
    if username == "":
        messagebox.showwarning("Warning!", "Login first to continue")
    else:
        checkout_function()

barlow_font = 'Barlow'
checkout_button = tk.Button(second_frame, text="Checkout", bg='#FCB7BA', command=lambda: check_user_checkout(),fg='#000000', font=(barlow_font,12), highlightthickness=0, borderwidth=0)
checkout_button.place(x=740, y=32)

def slideshow_function():
    global slideshow_timer
    if slideshow_timer == 4:
        slideshow_timer = 1
    if slideshow_timer == 1:
        slideshow_assets.config(image=ss_icecream_convert)
        home_screen_line.configure(bg='#FCB7BA')
        checkout_button.configure(bg='#FCB7BA', fg='#000000')
        update_scrollregion()
    elif slideshow_timer == 2:
        slideshow_assets.config(image=ss_donuts_convert)
        home_screen_line.configure(bg='#F8F8FF')
        checkout_button.configure(bg='#F8F8FF', fg='#5E376D')
        update_scrollregion()
    elif slideshow_timer == 3:
        slideshow_assets.config(image=ss_fried_chicken_convert)
        home_screen_line.configure(bg='white')
        checkout_button.configure(bg='white', fg='black')
    slideshow_assets.place(x=0, y=0)
    home_screen_line.place(x=0,y=25)
    slideshow_timer = slideshow_timer + 1
    second_frame.after(2000, slideshow_function)

intro_assets = Image.open('assets/intro.png')
intro_assets_resize = intro_assets.resize((353, 620))
intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
intro_assets_assets = tk.Label(non_scrollable_frame, borderwidth=0, highlightthickness=0)
intro_assets_assets.pack()
intro_assets_assets.config(image=intro_assets_convert)
intro_assets_assets.place(x=0, y=0)

def side_window():
    global signup_button_window, login_button_window, intro_assets_label
    global username_entry, email_entry, password_entry, signup_submit_button, return_window_button
    global login_submit_button

    signup_button_window = tk.Button(non_scrollable_frame, font=(barlow_font, 10), command=signup_window, text="Signup", bg='#F6B3C2', highlightthickness=0, borderwidth=0, width=28)
    signup_button_window.place(x=76, y=357)

    login_button_window = tk.Button(non_scrollable_frame, font=(barlow_font, 10), command=login_window,text="Login", bg='#F6B3C2', highlightthickness=0, borderwidth=0, width=28)
    login_button_window.place(x=77, y=426)

    intro_assets_label = tk.Label(non_scrollable_frame, borderwidth=0, highlightthickness=0)
    intro_assets_label.place(x=0, y=0)

def signup_window():
    global username_entry, email_entry, password_entry, signup_submit_button, return_window_button

    signup_button_window.place_configure(x=1000,y=1000)
    login_button_window.place_configure(x=1000,y=1000)

    intro_assets = Image.open('assets/signup.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Signup Window")

    signup_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 11), command=signup_function, text='Signup', bg='#F6B3C2', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    signup_submit_button.place(x=223, y=547)

    return_image = Image.open('assets/return.png')
    return_image_resize = return_image.resize((75, 25))
    return_image_convert = ImageTk.PhotoImage(return_image_resize)
    non_scrollable_frame.image = return_image_convert
    return_window_button = tk.Button(non_scrollable_frame, font=(barlow_font, 11), command=return_window, image=return_image_convert, bg='#F6B3C2', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    return_window_button.place(x=50, y=30)

    username_entry = tk.Entry(non_scrollable_frame, font=(barlow_font, 11), bg='#FCB7BA', width=28, highlightthickness=0, borderwidth=0)
    username_entry.place(x=66, y=358)
    email_entry = tk.Entry(non_scrollable_frame, font=(barlow_font, 11), bg='#FCB7BA', width=28, highlightthickness=0, borderwidth=0)
    email_entry.place(x=65, y=426)
    password_entry = tk.Entry(non_scrollable_frame, font=(barlow_font, 11), bg='#FCB7BA', width=28, highlightthickness=0, borderwidth=0)
    password_entry.place(x=65, y=493)

def signup_function():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if (username == "" or email == "" or password == ""):
        messagebox.showwarning('WARNING', 'Insert Information, All Fields are Required')

    db.execute(f"SELECT * from account_info WHERE username='{username}'")
    if db.fetchall():
        messagebox.showwarning('WARNING', 'User Already Exists!')

    else:
        insert_query = "INSERT INTO account_info (`username`, `email`, `password`) VALUES (%s,%s,%s)"
        vals = (username, email, password)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showwarning('SUCCESFUL', 'Book Added, Please Exit the System and Restart it.')

        intro_assets = Image.open('assets/homescreen.png')
        intro_assets_resize = intro_assets.resize((353, 620))
        intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
        intro_assets_label.config(image=intro_assets_convert)
        intro_assets_label.image = intro_assets_convert
        print("Homescreen Window through Sign Up")

        if username_entry.winfo_exists():
            if 'username_entry' in globals() and username_entry.winfo_exists():
                username_entry.place_forget()
            if 'password_entry' in globals() and password_entry.winfo_exists():
                password_entry.place_forget()
            if 'return_window_button' in globals() and return_window_button.winfo_exists():
                return_window_button.place_forget()
            if 'signup_submit_button' in globals() and signup_submit_button.winfo_exists():
                signup_submit_button.place_forget()
            if 'email_entry' in globals() and email_entry.winfo_exists():
                email_entry.place_forget()
            if 'login_submit_button' in globals() and login_submit_button.winfo_exists():
                login_submit_button.place_forget()
def return_window():
    global signup_button_window, login_button_window, intro_assets_label
    signup_button_window.place_configure(x=76, y=357)
    login_button_window.place_configure(x=77, y=426)
    signup_button_window.lift()
    login_button_window.lift()
    if username_entry.winfo_exists():
        if 'username_entry' in globals() and username_entry.winfo_exists():
            username_entry.place_forget()
        if 'password_entry' in globals() and password_entry.winfo_exists():
            password_entry.place_forget()
        if 'return_window_button' in globals() and return_window_button.winfo_exists():
            return_window_button.place_forget()
        if 'signup_submit_button' in globals() and signup_submit_button.winfo_exists():
            signup_submit_button.place_forget()
        if 'email_entry' in globals() and email_entry.winfo_exists():
            email_entry.place_forget()
        if 'login_submit_button' in globals() and login_submit_button.winfo_exists():
            login_submit_button.place_forget()

    intro_assets = Image.open('assets/intro.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Returned Window")

def login_window():
    global username_entry, password_entry, login_submit_button, return_window_button

    signup_button_window.place_configure(x=1000, y=1000)
    login_button_window.place_configure(x=1000, y=1000)

    intro_assets = Image.open('assets/login.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Login Window")

    login_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 11), command=login_function, text='Login', bg='#F6B3C2', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    login_submit_button.place(x=225, y=547)

    username_entry = tk.Entry(non_scrollable_frame, font=(barlow_font, 11), bg='#FCB7BA', width=28, highlightthickness=0, borderwidth=0)
    username_entry.place(x=65, y=426)
    password_entry = tk.Entry(non_scrollable_frame, font=(barlow_font, 11), bg='#FCB7BA', width=28, highlightthickness=0, borderwidth=0)
    password_entry.place(x=65, y=493)

    return_image = Image.open('assets/return.png')
    return_image_resize = return_image.resize((75, 25))
    return_image_convert = ImageTk.PhotoImage(return_image_resize)
    non_scrollable_frame.image = return_image_convert  # Keep reference to the image
    return_window_button = tk.Button(non_scrollable_frame, font=(barlow_font, 11), command=return_window, image=return_image_convert, bg='#F6B3C2', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    return_window_button.place(x=50, y=30)

def login_function():
    username = username_entry.get()
    password = password_entry.get()

    select_query = 'SELECT * FROM `account_info` WHERE `username` = %s and password = %s'
    vals = (username, password)
    db.execute(select_query, vals)
    user = db.fetchone()
    if user is not None:
        messagebox.showwarning('Logged In Successfully','Logged In Successfully, Please wait as we prepare your Adventures!')

        global intro_assets_convert
        intro_assets = Image.open('assets/homescreen.png')
        intro_assets_resize = intro_assets.resize((353, 620))
        intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
        intro_assets_label.config(image=intro_assets_convert)
        intro_assets_label.image = intro_assets_convert
        print("Homescreen Window through Login")

        if username_entry.winfo_exists():
            if 'username_entry' in globals() and username_entry.winfo_exists():
                username_entry.place_forget()
            if 'password_entry' in globals() and password_entry.winfo_exists():
                password_entry.place_forget()
            if 'return_window_button' in globals() and return_window_button.winfo_exists():
                return_window_button.place_forget()
            if 'signup_submit_button' in globals() and signup_submit_button.winfo_exists():
                signup_submit_button.place_forget()
            if 'email_entry' in globals() and email_entry.winfo_exists():
                email_entry.place_forget()
            if 'login_submit_button' in globals() and login_submit_button.winfo_exists():
                login_submit_button.place_forget()
    else:
        messagebox.showwarning('Login Failed', 'Invalid username or password.')

spice_cart_wrapper = tk.LabelFrame(non_scrollable_frame)

def hide_interface():
    if spice_cart_wrapper.winfo_exists():
        if 'spice_cart_wrapper' in globals() and spice_cart_wrapper.winfo_exists():
            spice_cart_wrapper.place_forget()
        if 'checkout_assets_assets' in globals() and checkout_assets_assets.winfo_exists():
            checkout_assets_assets.place_forget()
        if 'cancel_item_button' in globals() and cancel_item_button.winfo_exists():
            cancel_item_button.place_forget()
        if 'checkout_item_button' in globals() and checkout_item_button.winfo_exists():
            checkout_item_button.place_forget()
        if 'price_label' in globals() and price_label.winfo_exists():
            price_label.place_forget()
    else:
        pass

def dogd():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/1 Dozen Original Glazed Donuts.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    intro_assets_label.lift()
    print("1 Dozen Original Glazed Donuts")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: product_button_function(), text='Add to Basket',
                                    bg='#FEBE16', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def product_button_function():
        username = username_entry.get()
        product_name = '1 Dozen Original Glazed Donuts'
        price = 449

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def acc():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/5 Assortment Candy Cubes.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("5 Assortment Candy Cubes")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: product_button_function(), text='Add to Basket', bg='#0684B8', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def product_button_function():
        username = username_entry.get()
        product_name = '5 Assortment Candy Cubes'
        price = 225

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def pcmb():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/12 Pack Mixed Cookie Box.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("12 Pack Mixed Cookie Box")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: product_button_function(), text='Add to Basket', bg='#FEBE16', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def product_button_function():
        username = username_entry.get()
        product_name = '12 Pack Mixed Cookie Box'
        price = 675

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def apcl():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/2024 Pride Cookie Limiteds.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("2024 Pride Cookie Limiteds")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: product_button_function(), text='Add to Basket', bg='#79E4DF', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def product_button_function():
        username = username_entry.get()
        product_name = '2024 Pride Cookie Limiteds'
        price = 115

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def awb():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/All Weather Beauty.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("All Weather Beauty")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: product_button_function(), text='Add to Basket', fg='white', bg='617E59', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def product_button_function():
        username = username_entry.get()
        product_name = 'All Weather Beauty'
        price = 235

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def af():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Auguste  Fisheries.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Auguste Fisheries")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: product_button_function(), text='Add to Basket', bg='#FF66C4', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def product_button_function():
        username = username_entry.get()
        product_name = 'Auguste Fisheries'
        price = 145

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def bcs():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Banana Cream Soda.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Banana Cream Soda")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: product_button_function(), text='Add to Basket', bg='#F2726C', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def product_button_function():
        username = username_entry.get()
        product_name = 'Banana Cream Soda'
        price = 85

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def bpcs():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/BARBIE Peaches & Cream Soda.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("BARBIE Peaches & Cream Soda")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: product_button_function(), text='Add to Basket', fg='white', bg='#DD628E', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def product_button_function():
        username = username_entry.get()
        product_name = 'BARBIE Peaches & Cream Soda'
        price = 85

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def bmc():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Blueberry Muffin Cookie.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Blueberry Muffin Cookie")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: product_button_function(), text='Add to Basket', bg='#FF66C4', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def product_button_function():
        username = username_entry.get()
        product_name = 'Blueberry Muffin Cookie'
        price = 85

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def bcso():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Bridesmaid Cake SPICE Originals.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Bridesmaid Cake SPICE Originals")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: product_button_function(), text='Add to Basket', bg='#0684B8', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def product_button_function():
        username = username_entry.get()
        product_name = 'Bridesmaid Cake SPICE Originals'
        price = 1175

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def bpcc():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Bridesmaid Party Candy Cubes.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Bridesmaid Party Candy Cubes")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: product_button_function(), text='Add to Basket', bg='#79E4DF', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def product_button_function():
        username = username_entry.get()
        product_name = 'Bridesmaid Party Candy Cubes'
        price = 315

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def bbso():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Brioche Box SPICE Originals.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Brioche Box SPICE Originals")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: product_button_function(), text='Add to Basket', bg='#0684B8', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def product_button_function():
        username = username_entry.get()
        product_name = 'Brioche Box SPICE Originals'
        price = 515

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def bbso1():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Brunch Box SPICE Originals.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Brunch Box SPICE Originals")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: product_button_function(), text='Add to Basket', bg='#79E4DF', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def product_button_function():
        username = username_entry.get()
        product_name = 'Brunch Box SPICE Originals'
        price = 515

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def bgcb():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Bucket Glazed Cake Bites.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Bucket Glazed Cake Bites")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: product_button_function(), text='Add to Basket', bg='#0684B8', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def product_button_function():
        username = username_entry.get()
        product_name = 'Bucket Glazed Cake Bites'
        price = 339

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def cfso():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Cake Framboise SPICE Originals.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Cake Framboise SPICE Originals")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: af_button_function(), text='Add to Basket', bg='#FFDE59', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def af_button_function():
        username = username_entry.get()
        product_name = 'Cake Framboise SPICE Originals'
        price = 675

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def ciebso():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Cake-it-Easy Box SPICE Originals.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Cake-it-Easy Box SPICE Originals")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: bcs_button_function(), text='Add to Basket', bg='#F2726C', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def bcs_button_function():
        username = username_entry.get()
        product_name = 'Cake-it-Easy Box SPICE Originals'
        price = 515

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def clpcb():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/California Love Pretzel Chocolate Bar.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("California Love Pretzel Chocolate Bar")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: clpcb_button_function(), text='Add to Basket', bg='#FEBE16', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def clpcb_button_function():
        username = username_entry.get()
        product_name = 'California Love Pretzel Chocolate Bar'
        price = 115

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def ccso():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Cake Confetti SPICE Originals.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Cake Confetti SPICE Originals")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: clpcb_button_function(), text='Add to Basket', bg='#DD628E', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def clpcb_button_function():
        username = username_entry.get()
        product_name = 'Cake Confetti SPICE Originals'
        price = 675

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def cscb():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Campfire S’mores Chocolate Bar.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Campfire S’mores Chocolate Bar")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: cscb_button_function(), text='Add to Basket', bg='#DD628E', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def cscb_button_function():
        username = username_entry.get()
        product_name = 'Campfire S’mores Chocolate Bar'
        price = 115

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def cbb():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Candy  Bento Box.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Candy Bento Box")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: cbbo_button_function(), text='Add to Basket', bg='#F2726C', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def cbbo_button_function():
        username = username_entry.get()
        product_name = 'Candy Bento Box'
        price = 745

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def ccmbt():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Caramel Choco Boba Milk Tea.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Caramel Choco Boba Milk Tea")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: ccmbt_button_function(), text='Add to Basket', fg='white', bg='2E5C98', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def ccmbt_button_function():
        username = username_entry.get()
        product_name = 'Caramel Choco Boba Milk Tea'
        price = 80

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def cbgcb():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Cereal Bowl Gourmet Chocolate Bar.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Cereal Bowl Gourmet Chocolate Bar")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: cbgcb_button_function(), text='Add to Basket', bg='#0684B8', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def cbgcb_button_function():
        username = username_entry.get()
        product_name = 'Cereal Bowl Gourmet Chocolate Bar'
        price = 115

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def clpp():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Chai Lovers Petite Pyramid.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Chai Lovers Petite Pyramid")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: clpp_button_function(), text='Add to Basket', fg='white', bg='#617E59', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def clpp_button_function():
        username = username_entry.get()
        product_name = 'Chai Lovers Petite Pyramid'
        price = 535

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def cbbmt():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Champagne Bears.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Champagne Bears")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: cbbmt_button_function(), text='Add to Basket', bg='#FF66C4', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def cbbmt_button_function():
        username = username_entry.get()
        product_name = 'Champagne Bears'
        price = 875

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def cboa():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Cherry Bakewell Oak Boosts.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Cherry Bakewell Oak Boosts")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: cboa_button_function(), text='Add to Basket', fg='white', bg='#617E59', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def cboa_button_function():
        username = username_entry.get()
        product_name = 'Cherry Bakewell Oak Boosts'
        price = 155

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def cvs():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Cherry Vanilla Soda.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Cherry Vanilla Soda")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: cvs_button_function(), text='Add to Basket', bg='#0684B8', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def cvs_button_function():
        username = username_entry.get()
        product_name = 'Cherry Vanilla Soda'
        price = 85

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def cov():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Chobani  Oatmilk Vanilla.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Chobani Oatmilk Vanilla")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: cov_button_function(), text='Add to Basket', bg='#FF66C4', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def cov_button_function():
        username = username_entry.get()
        product_name = 'Chobani Oatmilk Vanilla'
        price = 315

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def cccc():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Chobani Creations Cherry Cheesecake.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Chobani Creations Cherry Cheesecake")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: cccc_button_function(), text='Add to Basket', bg='#0684B8', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def cccc_button_function():
        username = username_entry.get()
        product_name = 'Chobani Creations Cherry Cheesecake'
        price = 435

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def cfss():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Chobani Flip S\'more S\'mores.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Chobani Flip S'more S'mores")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: cfss_button_function(), text='Add to Basket', bg='#FFDE59', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def cfss_button_function():
        username = username_entry.get()
        product_name = "Chobani Flip S'more S'mores"
        price = 125

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def cob():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Chobani Oatmilk Barista Original.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Chobani Oatmilk Barista Original")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: cob_button_function(), text='Add to Basket', bg='#FFDE59', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def cob_button_function():
        username = username_entry.get()
        product_name = 'Chobani Oatmilk Barista Original'
        price = 315

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def coec():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Chobani Oatmilk Extra Creamy.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Chobani Oatmilk Extra Creamy")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: coec_button_function(), text='Add to Basket', bg='#DD628E', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def coec_button_function():
        username = username_entry.get()
        product_name = 'Chobani Oatmilk Extra Creamy'
        price = 315

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def cozso():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Chobani Oatmilk Zero Sugar Original.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Chobani Oatmilk Zero Sugar Original")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: cozso_button_function(), text='Add to Basket', bg='#F2726C', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def cozso_button_function():
        username = username_entry.get()
        product_name = 'Chobani Oatmilk Zero Sugar Original'
        price = 265

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def ccso1():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Chocolate Caramel SPICE Originals.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Chocolate Caramel SPICE Originals")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: ccso_button_function(), text='Add to Basket', bg='#FEBE16', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def ccso_button_function():
        username = username_entry.get()
        product_name = 'Chocolate Caramel SPICE Originals'
        price = 675

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def ctdb():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Chocolate Truffle Donut Bites.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Chocolate Truffle Donut Bites")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: ctdb_button_function(), text='Add to Basket', bg='#FFDE59', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def ctdb_button_function():
        username = username_entry.get()
        product_name = 'Chocolate Truffle Donut Bites'
        price = 475

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def cpsso():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Complimentary Pairs SPICE Originals.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Complimentary Pairs SPICE Originals")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: cpsso_button_function(), text='Add to Basket', bg='#FEBE16', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def cpsso_button_function():
        username = username_entry.get()
        product_name = 'Complimentary Pairs SPICE Originals'
        price = 515

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def oddb():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Orange Dreamsicle Donut Bites.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Orange Dreamsicle Donut Bites")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: oddb_button_function(), text='Add to Basket', bg='#79E4DF', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def oddb_button_function():
        username = username_entry.get()
        product_name = 'Orange Dreamsicle Donut Bites'
        price = 475

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def pbdb():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Party Bites! Donut Bites.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Party Bites! Donut Bites")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: pbdb_button_function(), text='Add to Basket', bg='#F2726C', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def pbdb_button_function():
        username = username_entry.get()
        product_name = 'Party Bites! Donut Bites'
        price = 475

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def pbsso():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/PARTY Box SPICE Originals.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("PARTY Box SPICE Originals")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: pbsso_button_function(), text='Add to Basket', bg='#DD628E', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def pbsso_button_function():
        username = username_entry.get()
        product_name = 'PARTY Box SPICE Originals'
        price = 515

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def cas():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Crisp Apple Soda.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Crisp Apple Soda")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: cas_button_function(), text='Add to Basket', bg='#FEBE16', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def cas_button_function():
        username = username_entry.get()
        product_name = 'Crisp Apple Soda'
        price = 85

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def diod():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Disney INSIDE OUT 2 Donut Box.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Disney INSIDE OUT 2 Donut Box")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: diod_button_function(), text='Add to Basket', bg='#F2726C', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def diod_button_function():
        username = username_entry.get()
        product_name = 'Disney INSIDE OUT 2 Donut Box'
        price = 485

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def dnsc():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Dragon Noodles & Sausage Combo.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Dragon Noodles & Sausage Combo")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: dnsc_button_function(), text='Add to Basket', bg='#DD628E', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def dnsc_button_function():
        username = username_entry.get()
        product_name = 'Dragon Noodles & Sausage Combo'
        price = 235

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def ent():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Evoker Nier Tea Set.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Evoker Nier Tea Set")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: ent_button_function(), text='Add to Basket', bg='#F2726C', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def ent_button_function():
        username = username_entry.get()
        product_name = 'Evoker Nier Tea Set'
        price = 125

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def ffo():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/FFFries Off, Tempura Plate.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("FFFries Off, Tempura Plate")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: ffo_button_function(), text='Add to Basket', bg='#0684B8', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def ffo_button_function():
        username = username_entry.get()
        product_name = 'FFFries Off, Tempura Plate'
        price = 119

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def fsp():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Fiendarce Steak Platter.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Fiendarce Steak Platter")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: fsp_button_function(), text='Add to Basket', bg='#FEBE16', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def fsp_button_function():
        username = username_entry.get()
        product_name = 'Fiendarce Steak Platter'
        price = 145

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def gvt():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Garlic  Vegetables Tsukemen.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Garlic Vegetables Tsukemen")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: gvt_button_function(), text='Add to Basket', bg='#FF66C4', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def gvt_button_function():
        username = username_entry.get()
        product_name = 'Garlic Vegetables Tsukemen'
        price = 165

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def gbcc():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Granola, Blueberry  & Chia Cookie.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Granola, Blueberry & Chia Cookie")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: gbcc_button_function(), text='Add to Basket', bg='#FFDE59', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def gbcc_button_function():
        username = username_entry.get()
        product_name = 'Granola, Blueberry & Chia Cookie'
        price = 85

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def hrptb():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Herbal Retreat Pyramid Tea Box.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Herbal Retreat Pyramid Tea Box")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: hrptb_button_function(), text='Add to Basket', bg='#FF66C4', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def hrptb_button_function():
        username = username_entry.get()
        product_name = 'Herbal Retreat Pyramid Tea Box'
        price = 635

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def hclc():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Hollywood x sugarfina Candy Cove.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Hollywood x Laduree Candy Cove")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: hclc_button_function(), text='Add to Basket', bg='#FF66C4', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def hclc_button_function():
        username = username_entry.get()
        product_name = 'Hollywood x Laduree Candy Cove'
        price = 675

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def hpa():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Hot Pot Assortments Platter.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Hot Pot Assortments Platter")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: hpa_button_function(), text='Add to Basket', fg='white', bg='#FF5757', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def hpa_button_function():
        username = username_entry.get()
        product_name = 'Hot Pot Assortments Platter'
        price = 85

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def lxblbm():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Laduree x Bridgerton Macaron Box.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Laduree x Bridgerton Macaron Box")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: lxblbm_button_function(), text='Add to Basket', fg='white', bg='#617E59', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def lxblbm_button_function():
        username = username_entry.get()
        product_name = 'Laduree x Bridgerton Macaron Box'
        price = 475

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def lcb():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Lavender Chocolate Bar.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Lavender Chocolate Bar")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: lcb_button_function(), text='Add to Basket', bg='#FFDE59', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def lcb_button_function():
        username = username_entry.get()
        product_name = 'Lavender Chocolate Bar'
        price = 115

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def lhssp():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Le Haut Special Steak Plate.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Le Haut Special Steak Plate")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: lhssp_button_function(), text='Add to Basket', bg='#79E4DF', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def lhssp_button_function():
        username = username_entry.get()
        product_name = 'Le Haut Special Steak Plate'
        price = 435

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def lpdb():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Lemon Poppy Donut Bites.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Lemon Poppy Donut Bites")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: lpdb_button_function(), text='Add to Basket', fg='white',bg='#617E59', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def lpdb_button_function():
        username = username_entry.get()
        product_name = 'Lemon Poppy Donut Bites'
        price = 475

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def lcgb():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Luxury Candy  Cubes Gift Box.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Luxury Candy Cubes Gift Box")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: lcgb_button_function(), text='Add to Basket', bg='#DD628E', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def lcgb_button_function():
        username = username_entry.get()
        product_name = 'Luxury Candy Cubes Gift Box'
        price = 515

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def lgcm():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Luxury Gourmet Chocolate Mix.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Luxury Gourmet Chocolate Mix")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: lgcm_button_function(), text='Add to Basket', bg='#79E4DF', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def lgcm_button_function():
        username = username_entry.get()
        product_name = 'Luxury Gourmet Chocolate Mix'
        price = 815

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def mpso():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Macaron Pyramid SPICE Originals.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Macaron Pyramid SPICE Originals")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: mpso_button_function(), text='Add to Basket', bg='#F2726C', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def mpso_button_function():
        username = username_entry.get()
        product_name = 'Macaron Pyramid SPICE Originals'
        price = 1175

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def mgdbmc():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Maple Drizzle  & Chopped-Bacon.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Maple Drizzle  & Chopped-Bacon")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: mgdbmc_button_function(), text='Add to Basket', bg='#FFDE59', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def mgdbmc_button_function():
        username = username_entry.get()
        product_name = 'Maple Drizzle  & Chopped-Bacon'
        price = 145

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def nmsfast():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Nyan Milk Set for a Special Time.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Nyan Milk Set for a Special Time")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: nmsfast_button_function(), text='Add to Basket', bg='#FFDE59', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def nmsfast_button_function():
        username = username_entry.get()
        product_name = 'Nyan Milk Set for a Special Time'
        price = 55

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def pmcc():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Peppermint Mocha  Coffee Creamer.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Peppermint Mocha Coffee Creamer")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: pmcc_button_function(), text='Add to Basket', fg='white', bg='#617E59', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def pmcc_button_function():
        username = username_entry.get()
        product_name = 'Peppermint Mocha Coffee Creamer'
        price = 385

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def ppalm():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Perfect  Puddling a la Moode.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Perfect Puddling a la Moode")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: ppalm_button_function(), text='Add to Basket', bg='#FF66C4', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def ppalm_button_function():
        username = username_entry.get()
        product_name = 'Perfect Puddling a la Moode'
        price = 235

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def rvcso():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Red Velvet Cake SPICE Originals.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Red Velvet Cake SPICE Originals")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: rvcso_button_function(), text='Add to Basket', fg='white', bg='#617E59', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def rvcso_button_function():
        username = username_entry.get()
        product_name = 'Red Velvet Cake SPICE Originals'
        price = 675

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def rmpyp():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Ruby Mini  Petite Pyramid.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Ruby Mini Petite Pyramid")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: rmpyp_button_function(), text='Add to Basket', bg='#79E4DF', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def rmpyp_button_function():
        username = username_entry.get()
        product_name = 'Ruby Mini Petite Pyramid'
        price = 435

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def sgc():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Sauteed  Grudge Chunks.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Sauteed Grudge Chunks")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: sgc_button_function(), text='Add to Basket', bg='#0684B8', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def sgc_button_function():
        username = username_entry.get()
        product_name = 'Sauteed Grudge Chunks'
        price = 325

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def sscb():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Strawberry Shortcake Chocolate Bar.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Strawberry Shortcake Chocolate Bar")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: sscb_button_function(), text='Add to Basket', fg="white", bg='#617E59', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def sscb_button_function():
        username = username_entry.get()
        product_name = 'Strawberry Shortcake Chocolate Bar'
        price = 115

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def ssfcmm():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Stunning Strategem Flurry Cocktail Mix.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Stunning Strategem Flurry Cocktail Mix")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: ssfcmm_button_function(), text='Add to Basket', fg='white', bg='#0684B8', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def ssfcmm_button_function():
        username = username_entry.get()
        product_name = 'Stunning Strategem Flurry Cocktail Mix'
        price = 55

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def sff():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Summer  Festival Fish.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Summer Festival Fish")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: sff_button_function(), text='Add to Basket', fg='white', bg='#D16D49', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def sff_button_function():
        username = username_entry.get()
        product_name = 'Summer Festival Fish'
        price = 85

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def sppf():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Sutera’s Pot-au-Feu.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Sutera’s Pot-au-Feu")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: sppf_button_function(), text='Add to Basket',fg='white', bg='#617E59', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def sppf_button_function():
        username = username_entry.get()
        product_name = 'Sutera’s Pot-au-Feu'
        price = 115

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def tcjpp():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Tea Chest Jubilee Petite Pyramid.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Tea Chest Jubilee Petite Pyramid")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: tcjpp_button_function(), text='Add to Basket', bg='#FFDE59', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def tcjpp_button_function():
        username = username_entry.get()
        product_name = 'Tea Chest Jubilee Petite Pyramid'
        price = 635

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def ssdb():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Strawberry Shortcake Donut Bites.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Strawberry Shortcake Donut Bites")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: ssdb_button_function(), text='Add to Basket', bg='#0684B8', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def ssdb_button_function():
        username = username_entry.get()
        product_name = 'Strawberry Shortcake Donut Bites'
        price = 475

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def tcwc():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Toasted Coconut & White Cookie Bites.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Toasted Coconut & White Cookie Bites")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: tcwc_button_function(), text='Add to Basket', fg='white',bg='#617E59', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def tcwc_button_function():
        username = username_entry.get()
        product_name = 'Toasted Coconut & White Cookie Bites'
        price = 55

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def ts():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Traditional Shortbread.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Traditional Shortbread")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: ts_button_function(), text='Add to Basket', bg='#FF66C4', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def ts_button_function():
        username = username_entry.get()
        product_name = 'Traditional Shortbread'
        price = 105

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def tmpc():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Tropical Mango  & Passionfruit Cookie.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Tropical Mango & Passionfruit Cookie")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: tmpc_button_function(), text='Add to Basket', bg='#79E4DF', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def tmpc_button_function():
        username = username_entry.get()
        product_name = 'Tropical Mango & Passionfruit Cookie'
        price = 85

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def vvcb():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Vacation Vibes Candy Cubes.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Vacation Vibes Candy Cubes")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: vvcb_button_function(), text='Add to Basket', bg='#FEBE16', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def vvcb_button_function():
        username = username_entry.get()
        product_name = 'Vacation Vibes Candy Cubes'
        price = 315

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def vgmcpj():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Vegan Gluten Maple & Pecan Cookie Jar.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Vegan Gluten Maple & Pecan Cookie Jar")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: vgmcpj_button_function(), text='Add to Basket', bg='#DD628E', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def vgmcpj_button_function():
        username = username_entry.get()
        product_name = 'Vegan Gluten Maple & Pecan Cookie Jar'
        price = 675

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def vlt():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Victorious Legend Tonkotsu Ramen.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Victorious Legend Tonkotsu Ramen")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: vlt_button_function(), text='Add to Basket', fg='white', bg='#2E333A', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def vlt_button_function():
        username = username_entry.get()
        product_name = 'Victorious Legend Tonkotsu Ramen'
        price = 155

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def wssmy():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Way of the Strong  Special Mixed Yakisoba.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Way of the Strong Special Mixed Yakisoba")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: wssmy_button_function(), text='Add to Basket', fg='white', bg='#802F2E', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def wssmy_button_function():
        username = username_entry.get()
        product_name = 'Way of the Strong Special Mixed Yakisoba'
        price = 145

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def zsgymb():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Zero Sugar Greek Yogurt Mixed Berry.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Zero Sugar Greek Yogurt Mixed Berry")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: zsgymb_button_function(), text='Add to Basket', bg='#F2726C', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def zsgymb_button_function():
        username = username_entry.get()
        product_name = 'Zero Sugar Greek Yogurt Mixed Berry'
        price = 345

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def zsgys():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Zero Sugar Greek Yogurt Strawberry.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Zero Sugar Greek Yogurt Strawberry")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: zsgys_button_function(), text='Add to Basket', bg='#FEBE16', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def zsgys_button_function():
        username = username_entry.get()
        product_name = 'Zero Sugar Greek Yogurt Strawberry'
        price = 155

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

def mgdb():
    hide_interface()
    intro_assets = Image.open('assets/products/prices/Maple Glazed Donut Bites.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Maple Glazed Donut Bites")

    product_submit_button = tk.Button(non_scrollable_frame, font=(barlow_font, 14), command=lambda: zsgys_button_function(), text='Add to Basket', bg='#FF66C4', highlightthickness=0, borderwidth=0, padx=0, pady=0)
    product_submit_button.place(x=181, y=568)

    def zsgys_button_function():
        username = username_entry.get()
        product_name = 'Maple Glazed Donut Bites'
        price = 475

        insert_query = "INSERT INTO cart_info (`username`, `product_name`, `price`) VALUES (%s,%s,%s)"
        vals = (username, product_name, price)
        db.execute(insert_query, vals)
        mydb.commit()
        messagebox.showinfo('SUCCESSFUL!', f'1 {product_name} added to cart!')

books = [
    {"title": "1dogd", "genre": "Cookies & Donuts", "image": "assets/products/1 Dozen Original Glazed Donuts.png", "command": lambda: dogd()},
    {"title": "5acc", "genre": "Candies & Cakes", "image": "assets/products/5 Assortment Candy Cubes.png", "command": lambda: acc()},
    {"title": "12pmcb", "genre": "Cookies & Donuts", "image": "assets/products/12 Pack Mixed Cookie Box.png", "command": lambda: pcmb()},
    {"title": "2024pcl", "genre": "Limiteds", "image": "assets/products/2024 Pride Cookie Limiteds.png", "command": lambda: apcl()},
    {"title": "awb", "genre": "Meal & Lunch Sets", "image": "assets/products/All Weather Beauty.png", "command": lambda: awb()},
    {"title": "af", "genre": "Meal & Lunch Sets", "image": "assets/products/Auguste  Fisheries.png", "command": lambda: af()},
    {"title": "bcs", "genre": "Tea & Beverages", "image": "assets/products/Banana Cream Soda.png", "command": lambda: bcs()},
    {"title": "bpcs", "genre": "Tea & Beverages", "image": "assets/products/BARBIE Peaches & Cream Soda.png", "command": lambda: bpcs()},
    {"title": "bmc", "genre": "Cookies & Donuts", "image": "assets/products/Blueberry Muffin Cookie.png","command": lambda: bmc()},
    {"title": "bcso", "genre": "Candies & Cakes", "image": "assets/products/Bridesmaid Cake SPICE Originals.png","command": lambda: bcso()},

    {"title": "1dogd", "genre": "Candies & Cakes", "image": "assets/products/Bridesmaid Party Candy Cubes.png","command": lambda: bpcc()},
    {"title": "5acc", "genre": "Limiteds", "image": "assets/products/Brioche Box SPICE Originals.png","command": lambda: bbso()},
    {"title": "12pmcb", "genre": "Cookies & Donuts", "image": "assets/products/Brunch Box SPICE Originals.png","command": lambda: bbso1()},
    {"title": "2024pcl", "genre": "Cookies & Donuts", "image": "assets/products/Bucket Glazed Cake Bites.png","command": lambda: bgcb()},
    {"title": "awb", "genre": "Candies & Cakes", "image": "assets/products/Cake Confetti SPICE Originals.png","command": lambda: ccso()},
    {"title": "af", "genre": "Candies & Cakes", "image": "assets/products/Cake Framboise SPICE Originals.png","command": lambda: cfso()},
    {"title": "bcs", "genre": "Cookies & Donuts", "image": "assets/products/Cake-it-Easy Box SPICE Originals.png","command": lambda: ciebso()},
    {"title": "bpcs", "genre": "Pastries & Chocolate","image": "assets/products/California Love Pretzel Chocolate Bar.png","command": lambda: clpcb()},
    {"title": "bmc", "genre": "Pastries & Chocolate", "image": "assets/products/Campfire S’mores Chocolate Bar.png","command": lambda: cscb()},
    {"title": "bcso", "genre": "Candies & Cakes", "image": "assets/products/Candy  Bento Box.png","command": lambda: cbb()},

    {"title": "1dogd", "genre": "Tea & Beverages", "image": "assets/products/Caramel Choco Boba Milk Tea.png", "command": lambda: ccmbt()},
    {"title": "5acc", "genre": "Pastries & Chocolate", "image": "assets/products/Cereal Bowl Gourmet Chocolate Bar.png", "command": lambda: cbgcb()},
    {"title": "12pmcb", "genre": "Tea & Beverages", "image": "assets/products/Chai Lovers Petite Pyramid.png", "command": lambda: clpp()},
    {"title": "2024pcl", "genre": "Candies & Cakes", "image": "assets/products/Champagne Bears.png", "command": lambda: cbbmt()},
    {"title": "awb", "genre": "Cookies & Donuts", "image": "assets/products/Cherry Bakewell Oak Boosts.png","command": lambda: cboa()},
    {"title": "af", "genre": "Tea & Beverages", "image": "assets/products/Cherry Vanilla Soda.png", "command": lambda: cvs()},
    {"title": "bcs", "genre": "Tea & Beverages", "image": "assets/products/Chobani  Oatmilk Vanilla.png", "command": lambda: cov()},
    {"title": "bpcs", "genre": "Candies & Cakes", "image": "assets/products/Chobani Creations Cherry Cheesecake.png", "command": lambda: cccc()},
    {"title": "bmc", "genre": "Candies & Cakes", "image": "assets/products/Chobani Flip S'more S'mores.png", "command": lambda: cfss()},
    {"title": "bcso", "genre": "Tea & Beverages", "image": "assets/products/Chobani Oatmilk Barista Original.png", "command": lambda: cob()},

    {"title": "1dogd", "genre": "Tea & Beverages", "image": "assets/products/Chobani Oatmilk Extra Creamy.png", "command": lambda: coec()},
    {"title": "5acc", "genre": "Tea & Beverages", "image": "assets/products/Chobani Oatmilk Zero Sugar Original.png", "command": lambda: cozso()},
    {"title": "12pmcb", "genre": "Cookies & Donuts", "image": "assets/products/Chocolate Caramel SPICE Originals.png", "command": lambda: ccso1()},
    {"title": "2024pcl", "genre": "Cookies & Donuts", "image": "assets/products/Chocolate Truffle Donut Bites.png", "command": lambda: ctdb()},
    {"title": "awb", "genre": "Cookies & Donuts", "image": "assets/products/Complimentary Pairs SPICE Originals.png", "command": lambda: cpsso()},
    {"title": "bcs", "genre": "Cookies & Donuts", "image": "assets/products/Orange Dreamsicle Donut Bites.png", "command": lambda: oddb()},
    {"title": "bpcs", "genre": "Cookies & Donuts", "image": "assets/products/Party Bites! Donut Bites.png", "command": lambda: pbdb()},
    {"title": "bmc", "genre": "Cookies & Donuts", "image": "assets/products/PARTY Box SPICE Originals.png", "command": lambda: pbsso()},
    {"title": "bcso", "genre": "Tea & Beverages", "image": "assets/products/Crisp Apple Soda.png", "command": lambda: cas()},

    {"title": "1dogd", "genre": "Limiteds", "image": "assets/products/Disney INSIDE OUT 2 Donut Box.png", "command": lambda: diod()},
    {"title": "5acc", "genre": "Meal & Lunch Sets", "image": "assets/products/Dragon Noodles & Sausage Combo.png", "command": lambda: dnsc()},
    {"title": "12pmcb", "genre": "Meal & Lunch Sets", "image": "assets/products/Evoker Nier Tea Set.png", "command": lambda: ent()},
    {"title": "2024pcl", "genre": "Meal & Lunch Sets", "image": "assets/products/FFFries Off, Tempura Plate.png", "command": lambda: ffo()},
    {"title": "awb", "genre": "Meal & Lunch Sets", "image": "assets/products/Fiendarce Steak Platter.png", "command": lambda: fsp()},
    {"title": "af", "genre": "Meal & Lunch Sets", "image": "assets/products/Garlic Vegetables  Tsukemen.png", "command": lambda: gvt()},
    {"title": "bcs", "genre": "Cookies & Donuts", "image": "assets/products/Granola, Blueberry  & Chia Cookie.png", "command": lambda: gbcc()},
    {"title": "bpcs", "genre": "Tea & Beverages", "image": "assets/products/Herbal Retreat Pyramid Tea Box.png", "command": lambda: hrptb()},
    {"title": "bmc", "genre": "Limiteds", "image": "assets/products/Hollywood x Laduree Candy Cove.png", "command": lambda: hclc()},
    {"title": "bcso", "genre": "Meal & Lunch Sets", "image": "assets/products/Hot Pot Assortments Platter.png", "command": lambda: hpa()},

    {"title": "1dogd", "genre": "Limiteds", "image": "assets/products/Laduree x Bridgerton Macaron Box.png", "command": lambda: lxblbm()},
    {"title": "5acc", "genre": "Pastries & Chocolate", "image": "assets/products/Lavender Chocolate Bar.png", "command": lambda: lcb()},
    {"title": "12pmcb", "genre": "Meal & Lunch Sets", "image": "assets/products/Le Haut Special Steak Plate.png", "command": lambda: lhssp()},
    {"title": "2024pcl", "genre": "Cookies & Donuts", "image": "assets/products/Lemon Poppy Donut Bites.png", "command": lambda: lpdb()},
    {"title": "awb", "genre": "Candies & Cakes", "image": "assets/products/Luxury Candy  Cubes Gift Box.png", "command": lambda: lcgb()},
    {"title": "af", "genre": "Pastries & Chocolate", "image": "assets/products/Luxury Gourmet Chocolate Mix.png", "command": lambda: lgcm()},
    {"title": "bcs", "genre": "Limiteds", "image": "assets/products/Macaron Pyramid SPICE Originals.png", "command": lambda: mpso()},
    {"title": "bpcs", "genre": "Meal & Lunch Sets", "image": "assets/products/Maple Drizzle  & Chopped-Bacon.png", "command": lambda: mgdbmc()},
    {"title": "bmc", "genre": "Cookies & Donuts", "image": "assets/products/Maple Glazed Donut BitesMuffin Cookie.png", "command": lambda: mgdb()},
    {"title": "bcso", "genre": "Cookies & Donuts", "image": "assets/products/Nyan Milk Set for a Special Time.png", "command": lambda: nmsfast()},

    {"title": "1dogd", "genre": "Tea & Beverages", "image": "assets/products/Peppermint Mocha  Coffee Creamer.png", "command": lambda: pmcc()},
    {"title": "5acc", "genre": "Pastries & Chocolate", "image": "assets/products/Perfect Puddling a la Moode.png", "command": lambda: ppalm()},
    {"title": "12pmcb", "genre": "Candies & Cakes", "image": "assets/products/Red Velvet Cake SPICE Originals.png", "command": lambda: rvcso()},
    {"title": "2024pcl", "genre": "Tea & Beverages", "image": "assets/products/Ruby Mini  Petite Pyramid.png", "command": lambda: rmpyp()},
    {"title": "awb", "genre": "Meal & Lunch Sets", "image": "assets/products/Sauteed  Grudge Chunks.png", "command": lambda: sgc()},
    {"title": "af", "genre": "Pastries & Chocolate", "image": "assets/products/Strawberry Shortcake Chocolate Bar.png", "command": lambda: sscb()},
    {"title": "bcs", "genre": "Tea & Beverages", "image": "assets/products/Stunning Strategem Flurry Cocktail Mix.png", "command": lambda: ssfcmm()},
    {"title": "bpcs", "genre": "Meal & Lunch Sets", "image": "assets/products/Summer  Festival Fish.png", "command": lambda: sff()},
    {"title": "bmc", "genre": "Meal & Lunch Sets", "image": "assets/products/Sutera’s Pot-au-Feu.png", "command": lambda: sppf()},
    {"title": "bcso", "genre": "Tea & Beverages", "image": "assets/products/Tea Chest Jubilee Petite Pyramid.png", "command": lambda: tcjpp()},

    {"title": "1dogd", "genre": "Cookies & Donuts", "image": "assets/products/Strawberry Shortcake Donut Bites.png", "command": lambda: ssdb()},
    {"title": "5acc", "genre": "Cookies & Donuts", "image": "assets/products/Toasted Coconut & White Cookie Bites.png", "command": lambda: tcwc()},
    {"title": "12pmcb", "genre": "Limiteds", "image": "assets/products/Traditional Shortbread.png", "command": lambda: ts()},
    {"title": "2024pcl", "genre": "Cookies & Donuts", "image": "assets/products/Tropical Mango  & Passionfruit Cookie.png", "command": lambda: tmpc()},
    {"title": "awb", "genre": "Candies & Cakes", "image": "assets/products/Vacation Vibes Candy Cubes.png", "command": lambda: vvcb()},
    {"title": "af", "genre": "Cookies & Donuts", "image": "assets/products/Vegan Gluten Maple & Pecan Cookie Jar.png", "command": lambda: vgmcpj()},
    {"title": "bcs", "genre": "Meal & Lunch Sets", "image": "assets/products/Victorious Legend Tonkotsu Ramen.png", "command": lambda: vlt()},
    {"title": "bpcs", "genre": "Meal & Lunch Sets", "image": "assets/products/Way of the Strong  Special Mixed Yakisoba.png", "command": lambda: wssmy()},
    {"title": "bmc", "genre": "Pastries & Chocolate", "image": "assets/products/Zero Sugar Greek Yogurt Mixed Berry.png", "command": lambda: zsgymb()},
    {"title": "bcso", "genre": "Pastries & Chocolate", "image": "assets/products/Zero Sugar Greek Yogurt Strawberry.png", "command": lambda: zsgys()}

]

class BookDisplay(tk.LabelFrame):
    def __init__(self, second_frame, books, width=None, height=None, bg="#FFEDBF", borderwidth=0, highlightthickness=0):
        super().__init__(second_frame, padx=1, pady=1, width=width, height=height, bg=bg, borderwidth=borderwidth, highlightthickness=highlightthickness, relief=tk.RAISED)
        self.books = books
        self.display_frame = tk.Frame(self, bg=bg)
        self.display_frame.pack(pady=1)

        self.create_widgets()
        self.show_all_books()

    def create_widgets(self):
        genres = set(book["genre"] for book in self.books)
        genre_frame = tk.Frame(self, bg="#FFEDBF")
        genre_frame.place(x=20, y=30)

        for genre in genres:
            button = tk.Button(genre_frame, text=genre, command=lambda g=genre: self.filter_books(g), bg='#FFEDBF', fg='#000000', font=(barlow_font,10), highlightthickness=0, borderwidth=0)
            button.pack(side=tk.LEFT, padx=10, pady=(0,10))

        show_all_button = tk.Button(genre_frame, text="Show All", command=self.show_all_books, bg='#FFEDBF', fg='#000000', font=(barlow_font,10), highlightthickness=0, borderwidth=0)
        show_all_button.pack(side=tk.LEFT, padx=5, pady=(0,10))

        for i in range(4):
            self.display_frame.grid_columnconfigure(i, weight=1)

    def filter_books(self, genre):
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        row, col = 0, 0
        for book in self.books:
            if book["genre"] == genre:
                self.display_book(book, row, col)
                col += 1
                if col == 4:
                    col = 0
                    row += 1

        update_scrollregion()

    def show_all_books(self):
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        row, col = 0, 0
        for book in self.books:
            self.display_book(book, row, col)
            col += 1
            if col == 4:
                col = 0
                row += 1

        update_scrollregion()

    def display_book(self, book, row, col):
        frame = tk.Frame(self.display_frame, padx=1, pady=10, bg="#FFEDBF", bd=1, highlightthickness=0,
                         relief=tk.RAISED, borderwidth=1, width=200, height=220)
        frame.grid(row=row, column=col)
        frame.grid_propagate(False)

        image = Image.open(book["image"])
        image = image.resize((200, 200), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        pady_value = 60 if row < 1 else 0

        button_image = tk.Button(frame, image=photo, borderwidth=0, highlightthickness=0)
        button_image.image = photo
        button_image.pack(side=tk.LEFT, padx=1, pady=(pady_value, 20))
        button_image.configure(command=lambda: self.check_user(book["command"]))

        frame.configure(borderwidth=0, relief=tk.FLAT)

        self.display_frame.grid_rowconfigure(row, weight=1)
        self.display_frame.grid_columnconfigure(col, weight=1)

    def check_user(self, command):
        username = username_entry.get()
        if username == "":
            no_user()
        else:
            command()

book_display = BookDisplay(second_frame, books, width=300, height=600, bg="#FFEDBF", borderwidth=0, highlightthickness=0)
book_display.pack(fill=tk.NONE, expand=True,pady=(400, 0), padx=1)

def checkout_function():
    global spice_cart_wrapper
    global checkout_assets_assets
    global cancel_item_button
    global checkout_item_button
    global price_label

    username = username_entry.get()
    intro_assets = Image.open('assets/checkout.png')
    intro_assets_resize = intro_assets.resize((353, 620))
    intro_assets_convert = ImageTk.PhotoImage(intro_assets_resize)
    intro_assets_label.config(image=intro_assets_convert)
    intro_assets_label.image = intro_assets_convert
    print("Checkout")

    checkout_assets = Image.open('assets/checkout_preview.png')
    checkout_assets_resize = checkout_assets.resize((320,320))
    checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
    checkout_assets_assets = tk.Label(non_scrollable_frame, borderwidth=0, highlightthickness=0)
    checkout_assets_assets.pack()
    checkout_assets_assets.config(image=checkout_assets_convert)
    checkout_assets_assets.place(x=20, y=20)
    checkout_assets_assets.image = checkout_assets_convert

    spice_cart_wrapper = tk.LabelFrame(non_scrollable_frame, bg="#FEFFBC")
    spice_cart_wrapper.place(x=30, y=350)

    def clicker(e):
        getrows()

    global spice_cart_cart
    spice_cart_cart = Treeview(spice_cart_wrapper, columns=(1, 2, 3,4), show="headings", height=6)
    spice_cart_cart.grid(row=0, column=0, sticky="nsew")
    spice_cart_cart.bind("<Double-1>", clicker)
    spice_cart_cart.heading(1, text="Order ID")
    spice_cart_cart.column(1, minwidth=0, width=0, stretch=NO, anchor=tk.CENTER)
    spice_cart_cart.heading(2, text="User Name")
    spice_cart_cart.column(2, minwidth=0, width=0, stretch=NO, anchor=tk.CENTER)
    spice_cart_cart.heading(3, text="Product Name")
    spice_cart_cart.column(3, minwidth=0, width=290, stretch=NO, anchor=tk.CENTER)
    spice_cart_cart.heading(4, text="Price")
    spice_cart_cart.column(4, minwidth=0, width=0, stretch=NO, anchor=tk.CENTER)

    cart_id = tk.StringVar()
    message_cart_id = tk.Entry(non_scrollable_frame, textvariable=cart_id, font=('verdana', 12), bg="#F7EEE5", state="readonly")
    message_cart_id.place(x=85, y=1000)

    product_name = tk.StringVar()
    message_product_name = tk.Entry(non_scrollable_frame, textvariable=product_name, font=('verdana', 12), bg="#F7EEE5", state="readonly")
    message_product_name.place(x=305, y=1000)

    select_query = 'SELECT * FROM `cart_info` WHERE `username` = %s'
    vals = (username,)
    db.execute(select_query, vals)
    rows = db.fetchall()

    if not rows:
        pass
    else:
        def update(rows):
            spice_cart_cart.delete(*spice_cart_cart.get_children())
            for row in rows:
                spice_cart_cart.insert('', 'end', values=(row[0], row[1],row[2], row[3]))

        def add_prices(rows):
            total_price = sum(float(row[3]) for row in rows)
            return total_price

        total_price = add_prices(rows)
        print(total_price)

        price_label = tk.Label(non_scrollable_frame, text=f'{total_price:.0f}', bg='#79E4DF', fg='#000000', font=(barlow_font, 25))
        price_label.place(x=50, y=560)

        query = f"SELECT cart_id, username, product_name, price FROM cart_info WHERE username = %s"
        db.execute(query, vals)
        rows = db.fetchall()
        update(rows)

        def delete_cart():
            cart_idS = cart_id.get()
            if cart_idS == '':
                tk.messagebox.showwarning("WARNING", "No items to cancel!")
            else:
                if tk.messagebox.askyesno("CONFIRM CANCEL", "Are you sure you want to cancel your book order?"):
                    query = f"DELETE FROM cart_info WHERE cart_id = %s"
                    db.execute(query, (cart_idS,))
                    mydb.commit()
                    query = f"SELECT cart_id, username, product_name, price FROM cart_info WHERE username = %s"
                    db.execute(query, vals)
                    rows = db.fetchall()
                    update(rows)

                    message_cart_id.configure(state="normal", bg="#F7EEE5")
                    message_product_name.configure(state="normal", bg="#F7EEE5")

                    message_cart_id.delete(0, tk.END)
                    message_product_name.delete(0, tk.END)

                    message_cart_id.configure(state="readonly", readonlybackground="#F7EEE5")
                    message_product_name.configure(state="readonly", readonlybackground="#F7EEE5")
                    tk.messagebox.showinfo('Successful!', 'Book Order was Cancelled')

                    global checkout_assets_convert
                    checkout_assets = Image.open('assets/checkout_preview.png')
                    checkout_assets_resize = checkout_assets.resize((320, 320))
                    checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                    checkout_assets_assets.config(image=checkout_assets_convert)
                    checkout_assets_assets.image = checkout_assets_convert

                    total_price = add_prices(rows)
                    price_label.configure(text=f'{total_price:.0f}')
                    print(total_price)
                else:
                    return True

        def checkout_cart():
            total_price = add_prices(rows)
            amount = simpledialog.askstring("NOTICE", "Enter your amount: ")
            if not amount:
                messagebox.showwarning("ERROR", "The entry should not be empty!")
            else:
                try:
                    check_number = float(amount)
                    print(check_number)
                    if check_number < float(total_price):
                        messagebox.showwarning("ERROR", "The entry should not be lower than the required amount!")
                    else:
                        global final_total
                        final_checked = check_number - float(total_price)
                        final_total = f"{final_checked:.0f}"
                        print(final_total)
                        price_label.configure(text=final_total)
                        global change
                        change = final_total
                        username = username_entry.get()
                        transfer_to_order_info(username, final_total)
                except ValueError:
                    messagebox.showwarning("ERROR", "The entry should contain numerical numbers!")

        def transfer_to_order_info(username, change):
            try:
                select_query = 'SELECT cart_id, username, product_name, price FROM cart_info WHERE username = %s'
                vals = (username,)
                db.execute(select_query, vals)
                rows = db.fetchall()

                insert_query = ('INSERT INTO ordered_info (cart_id, username, product_name, price, `change`) '
                                'VALUES (%s, %s, %s, %s, %s) '
                                'ON DUPLICATE KEY UPDATE '
                                'username = VALUES(username), '
                                'product_name = VALUES(product_name), '
                                'price = VALUES(price), '
                                '`change` = VALUES(`change`)')

                for row in rows:
                    db.execute(insert_query, (*row, change))

                delete_query = 'DELETE FROM cart_info WHERE username = %s'
                db.execute(delete_query, vals)

                mydb.commit()
                messagebox.showinfo("Successful!", "Items successfully ordered!")

                query = f"SELECT cart_id, username, product_name, price FROM cart_info WHERE username = %s"
                db.execute(query, vals)
                rows = db.fetchall()
                update(rows)

                checkout_assets = Image.open('assets/checkout_preview.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            except Exception as e:
                print("Error during data transfer:", e)
                mydb.rollback()

        cancel_item_button = tk.Button(non_scrollable_frame, text="Delete Item", command=delete_cart,bg='#FFEDBF', fg='#000000', font=(barlow_font, 12), borderwidth=0, highlightthickness=0)
        cancel_item_button.place(x=40, y=505)

        checkout_item_button = tk.Button(non_scrollable_frame, text="Checkout Item", command=checkout_cart, bg='#79E4DF', fg='#000000', font=(barlow_font, 14), borderwidth=0, highlightthickness=0)
        checkout_item_button.place(x=181, y=568)

    def getrows():
        message_cart_id.delete(0, tk.END)
        message_product_name.delete(0, tk.END)

        selected_row = spice_cart_cart.focus()
        if selected_row:
            message_cart_id.configure(state="normal", bg="#F7EEE5")
            message_product_name.configure(state="normal", bg="#F7EEE5")
            values = spice_cart_cart.item(selected_row, 'values')

            message_cart_id.delete(0, tk.END)
            message_product_name.delete(0, tk.END)

            message_cart_id.configure(state="normal", bg="#F7EEE5")
            message_product_name.configure(state="normal", bg="#F7EEE5")
            values = spice_cart_cart.item(selected_row, 'values')

            message_cart_id.insert(0, values[0])
            message_product_name.insert(0, values[2])

            message_cart_id.configure(state="readonly", readonlybackground="#F7EEE5")
            message_product_name.configure(state="readonly", readonlybackground="#F7EEE5")

            global checkout_assets_convert
            product_name = message_product_name.get()
            if product_name == "1 Dozen Original Glazed Donuts":
                checkout_assets = Image.open('assets/products/1 Dozen Original Glazed Donuts.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "5 Assortment Candy Cubes":
                checkout_assets = Image.open('assets/products/5 Assortment Candy Cubes.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "12 Pack Mixed Cookie Box":
                checkout_assets = Image.open('assets/products/12 Pack Mixed Cookie Box.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "2024 Pride Cookie Limiteds":
                checkout_assets = Image.open('assets/products/2024 Pride Cookie Limiteds.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "All Weather Beauty":
                checkout_assets = Image.open('assets/products/All Weather Beauty.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Auguste Fisheries":
                checkout_assets = Image.open('assets/products/Auguste  Fisheries.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Banana Cream Soda":
                checkout_assets = Image.open('assets/products/Banana Cream Soda.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "BARBIE Peaches & Cream Soda":
                checkout_assets = Image.open('assets/products/BARBIE Peaches & Cream Soda.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Blueberry Muffin Cookie":
                checkout_assets = Image.open('assets/products/Blueberry Muffin Cookie.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Bridesmaid Cake SPICE Originals":
                checkout_assets = Image.open('assets/products/Bridesmaid Cake SPICE Originals.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Bridesmaid Party Candy Cubes":
                checkout_assets = Image.open('assets/products/Bridesmaid Party Candy Cubes.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Brioche Box SPICE Originals":
                checkout_assets = Image.open('assets/products/Brioche Box SPICE Originals.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Brunch Box SPICE Originals":
                checkout_assets = Image.open('assets/products/Brunch Box SPICE Originals.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Bucket Glazed Cake Bites":
                checkout_assets = Image.open('assets/products/Bucket Glazed Cake Bites.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Cake Confetti SPICE Originals":
                checkout_assets = Image.open('assets/products/Cake Confetti SPICE Originals.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Cake Framboise SPICE Originals":
                checkout_assets = Image.open('assets/products/Cake Framboise SPICE Originals.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Cake-it-Easy Box SPICE Originals":
                checkout_assets = Image.open('assets/products/Cake-it-Easy Box SPICE Originals.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "California Love Pretzel Chocolate Bar":
                checkout_assets = Image.open('assets/products/California Love Pretzel Chocolate Bar.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Campfire S’mores Chocolate Bar":
                checkout_assets = Image.open('assets/products/Campfire S’mores Chocolate Bar.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Candy Bento Box":
                checkout_assets = Image.open('assets/products/Candy  Bento Box.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Caramel Choco Boba Milk Tea":
                checkout_assets = Image.open('assets/products/Caramel Choco Boba Milk Tea.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Cereal Bowl Gourmet Chocolate Bar":
                checkout_assets = Image.open('assets/products/Cereal Bowl Gourmet Chocolate Bar.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Chai Lovers Petite Pyramid":
                checkout_assets = Image.open('assets/products/Chai Lovers Petite Pyramid.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Champagne Bears":
                checkout_assets = Image.open('assets/products/Champagne Bears.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Cherry Bakewell Oak Boosts":
                checkout_assets = Image.open('assets/products/Cherry Bakewell Oak Boosts.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Cherry Vanilla Soda":
                checkout_assets = Image.open('assets/products/Cherry Vanilla Soda.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Chobani Oatmilk Vanilla":
                checkout_assets = Image.open('assets/products/Chobani  Oatmilk Vanilla.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Chobani Creations Cherry Cheesecake":
                checkout_assets = Image.open('assets/products/Chobani Creations Cherry Cheesecake.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Chobani Flip S'more S'mores":
                checkout_assets = Image.open("assets/products/Chobani Flip S'more S'mores.png")
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Chobani Oatmilk Barista Original":
                checkout_assets = Image.open('assets/products/Chobani Oatmilk Barista Original.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Chobani Oatmilk Extra Creamy":
                checkout_assets = Image.open('assets/products/Chobani Oatmilk Extra Creamy.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Chobani Oatmilk Zero Sugar Original":
                checkout_assets = Image.open('assets/products/Chobani Oatmilk Zero Sugar Original.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Chocolate Caramel SPICE Originals":
                checkout_assets = Image.open('assets/products/Chocolate Caramel SPICE Originals.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Chocolate Truffle Donut Bites":
                checkout_assets = Image.open('assets/products/Chocolate Truffle Donut Bites.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Complimentary Pairs SPICE Originals":
                checkout_assets = Image.open('assets/products/Complimentary Pairs SPICE Originals.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Crisp Apple Soda":
                checkout_assets = Image.open('assets/products/Crisp Apple Soda.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Disney INSIDE OUT 2 Donut Box":
                checkout_assets = Image.open('assets/products/Disney INSIDE OUT 2 Donut Box.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Dragon Noodles & Sausage Combo":
                checkout_assets = Image.open('assets/products/Dragon Noodles & Sausage Combo.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Evoker Nier Tea Set":
                checkout_assets = Image.open('assets/products/Evoker Nier Tea Set.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "FFFries Off, Tempura Plate":
                checkout_assets = Image.open('assets/products/FFFries Off, Tempura Plate.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Fiendarce Steak Platter":
                checkout_assets = Image.open('assets/products/Fiendarce Steak Platter.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Garlic Vegetables Tsukemen":
                checkout_assets = Image.open('assets/products/Garlic Vegetables  Tsukemen.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Granola, Blueberry & Chia Cookie":
                checkout_assets = Image.open('assets/products/Granola, Blueberry  & Chia Cookie.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Herbal Retreat Pyramid Tea Box":
                checkout_assets = Image.open('assets/products/Herbal Retreat Pyramid Tea Box.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Hollywood x Laduree Candy Cove":
                checkout_assets = Image.open('assets/products/Hollywood x Laduree Candy Cove.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Hot Pot Assortments Platter":
                checkout_assets = Image.open('assets/products/Hot Pot Assortments Platter.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Laduree x Bridgerton Macaron Box":
                checkout_assets = Image.open('assets/products/Laduree x Bridgerton Macaron Box.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Lavender Chocolate Bar":
                checkout_assets = Image.open('assets/products/Lavender Chocolate Bar.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Le Haut Special Steak Plate":
                checkout_assets = Image.open('assets/products/Le Haut Special Steak Plate.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Lemon Poppy Donut Bites":
                checkout_assets = Image.open('assets/products/Lemon Poppy Donut Bites.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Luxury Candy Cubes Gift Box":
                checkout_assets = Image.open('assets/products/Luxury Candy  Cubes Gift Box.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Luxury Gourmet Chocolate Mix":
                checkout_assets = Image.open('assets/products/Luxury Gourmet Chocolate Mix.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Macaron Pyramid SPICE Originals":
                checkout_assets = Image.open('assets/products/Macaron Pyramid SPICE Originals.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Maple Drizzle & Chopped-Bacon":
                checkout_assets = Image.open('assets/products/Maple Drizzle  & Chopped-Bacon.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Maple Glazed Donut BitesMuffin Cookie":
                checkout_assets = Image.open('assets/products/Maple Glazed Donut BitesMuffin Cookie.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Nyan Milk Set for a Special Time":
                checkout_assets = Image.open('assets/products/Nyan Milk Set for a Special Time.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Orange Dreamsicle Donut Bites":
                checkout_assets = Image.open('assets/products/Orange Dreamsicle Donut Bites.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Party Bites! Donut Bites":
                checkout_assets = Image.open('assets/products/Party Bites! Donut Bites.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "PARTY Box SPICE Originals":
                checkout_assets = Image.open('assets/products/PARTY Box SPICE Originals.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Peppermint Mocha Coffee Creamer":
                checkout_assets = Image.open('assets/products/Peppermint Mocha  Coffee Creamer.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Perfect Puddling a la Moode":
                checkout_assets = Image.open('assets/products/Perfect Puddling a la Moode.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Red Velvet Cake SPICE Originals":
                checkout_assets = Image.open('assets/products/Red Velvet Cake SPICE Originals.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Ruby Mini Petite Pyramid":
                checkout_assets = Image.open('assets/products/Ruby Mini  Petite Pyramid.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Sauteed Grudge Chunks":
                checkout_assets = Image.open('assets/products/Sauteed  Grudge Chunks.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Strawberry Shortcake Chocolate Bar":
                checkout_assets = Image.open('assets/products/Strawberry Shortcake Chocolate Bar.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Strawberry Shortcake Donut Bites":
                checkout_assets = Image.open('assets/products/Strawberry Shortcake Donut Bites.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Stunning Strategem Flurry Cocktail Mix":
                checkout_assets = Image.open('assets/products/Stunning Strategem Flurry Cocktail Mix.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Summer Festival Fish":
                checkout_assets = Image.open('assets/products/Summer  Festival Fish.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Sutera’s Pot-au-Feu":
                checkout_assets = Image.open('assets/products/Sutera’s Pot-au-Feu.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Tea Chest Jubilee Petite Pyramid":
                checkout_assets = Image.open('assets/products/Tea Chest Jubilee Petite Pyramid.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Toasted Coconut & White Cookie Bites":
                checkout_assets = Image.open('assets/products/Toasted Coconut & White Cookie Bites.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Traditional Shortbread":
                checkout_assets = Image.open('assets/products/Traditional Shortbread.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Tropical Mango & Passionfruit Cookie":
                checkout_assets = Image.open('assets/products/Tropical Mango  & Passionfruit Cookie.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Vacation Vibes Candy Cubes":
                checkout_assets = Image.open('assets/products/Vacation Vibes Candy Cubes.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Vegan Gluten Maple & Pecan Cookie Jar":
                checkout_assets = Image.open('assets/products/Vegan Gluten Maple & Pecan Cookie Jar.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Victorious Legend Tonkotsu Ramen":
                checkout_assets = Image.open('assets/products/Victorious Legend Tonkotsu Ramen.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Way of the Strong Special Mixed Yakisoba":
                checkout_assets = Image.open('assets/products/Way of the Strong  Special Mixed Yakisoba.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Zero Sugar Greek Yogurt Mixed Berry":
                checkout_assets = Image.open('assets/products/Zero Sugar Greek Yogurt Mixed Berry.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

            elif product_name == "Zero Sugar Greek Yogurt Strawberry":
                checkout_assets = Image.open('assets/products/Zero Sugar Greek Yogurt Strawberry.png')
                checkout_assets_resize = checkout_assets.resize((320, 320))
                checkout_assets_convert = ImageTk.PhotoImage(checkout_assets_resize)
                checkout_assets_assets.config(image=checkout_assets_convert)
                checkout_assets_assets.image = checkout_assets_convert

homescreen_assets = tk.Label(second_frame, borderwidth=0, highlightthickness=0)
homescreen_pic = Image.open('assets/robin.png')
homescreen_pic_resize = homescreen_pic.resize((850, 1))
homescreen_pic_convert = ImageTk.PhotoImage(homescreen_pic_resize)
homescreen_assets.homescreen_pic_convert = homescreen_pic_convert
homescreen_assets.config(image=homescreen_pic_convert)
homescreen_assets.pack(pady=(1, 0))

side_window()
slideshow_function()
root.mainloop()
