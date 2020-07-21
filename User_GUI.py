import os
from tkinter import *
import warnings
import matplotlib.pyplot as plt
import matplotlib.cbook
import pandas as pd
from tkinter import messagebox
import Data_Loading


# Generating Donut Graph to classify Domestic and Public violence in requested region
def donut_chart():
    df = Data_Loading.df
    print("Generating Donut Graph")
    s = df[['domestic']]  # get a series from data frame
    violence = pd.DataFrame(s.groupby('domestic').size().sort_values(ascending=True).rename('counts'))
    data = violence.get_values()
    print(data[0], "were Domestic crimes and ", data[1], "were Public crimes")
    names = 'Domestic', 'Public',
    # Create a circle for the center of the plot
    my_circle = plt.Circle((0, 0), 0.7, color='white')
    plt.pie(data, labels=names, colors=['skyblue', 'lightsalmon'])
    plt.title("Crime Statistics ")
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    plt.show()
    warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)


# Generating Horizontal Bar Graph to rank major crimes in requested region
def hor_bargraph():
    df = Data_Loading.df
    print("-" * 50)
    print("Generating Horizontal Bar Graph")
    s = df[['primary_type']]  # get a series from data frame
    crime_count = pd.DataFrame(s.groupby('primary_type').size().sort_values(ascending=True).rename('counts'))
    data = crime_count.iloc[-10:-5]  # retrieving select rows by loc method
    print(data[::-1])
    data.plot(kind='barh', color='darkcyan')
    plt.xlabel('Counts')
    plt.ylabel('Crime Categories')
    plt.title("Crime Statistics ")
    plt.subplots_adjust(left=0.33, right=0.89)
    print("-" * 50)
    plt.show()


# Generating Pie Chart to view Arrest and Non-Arrest ratio in requested region
def pie_chart():
    df = Data_Loading.df
    print("-" * 50)
    print("Generating Pie chart")
    s = df[['arrest']]  # get a series from data frame
    arrest = pd.DataFrame(s.groupby('arrest').size().sort_values(ascending=True).rename('counts'))
    print(arrest.values[0], " were Arrested  and ", arrest.values[1], " weren't arrested")
    plt.figure(figsize=(5, 5))
    labels = ["Arrest", "Non-Arrest"]
    values = [arrest.values[0], arrest.values[1]]
    explode = [0, 0.05]
    colors = ["y", "c"]
    plt.pie(values, labels=labels, autopct="%.1f%%", explode=explode, colors=colors)
    plt.title("Crime Statistics ")
    plt.show()
    print("-" * 50)
    warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)


# Generating Vertical Bar Graph to generate rate of requested crime in requested region
def ver_bargraph():
    df = Data_Loading.df
    datalist = {}
    print("-" * 50)
    print("Generating Bar Graph")
    print("Count \t", "Crime")
    if var1.get():
        is_Burglary = df[df.primary_type == 'BURGLARY']
        count_Burglary = is_Burglary.shape[0]
        print(count_Burglary, "\tBURGLARY")
        datalist1 = {'Burglary': count_Burglary}
        datalist.update(datalist1)

    if var2.get():
        is_Weapons = df[df.primary_type == 'WEAPONS VIOLATION']
        count_Weapons = is_Weapons.shape[0]
        print(count_Weapons, "\tWeapons Violation")
        datalist2 = {'Weapons': count_Weapons}
        datalist.update(datalist2)

    if var3.get():
        is_Robbery = df[df.primary_type == 'ROBBERY']
        count_Robbery = is_Robbery.shape[0]
        print(count_Robbery, "\tRobbery")
        datalist3 = {'Robbery': count_Robbery}
        datalist.update(datalist3)

    if var4.get():
        is_SO = df[df.primary_type == 'SEX OFFENSE']
        count_SO = is_SO.shape[0]
        print(count_SO, "\tSex Offense")
        datalist4 = {'Sex Offence': count_SO}
        datalist.update(datalist4)

    width = 0.5 / 1
    plt.bar(range(len(datalist)), datalist.values(), width, align='center', color='lightcoral')
    plt.ylabel('Counts')
    plt.xlabel('Crime Categories')
    plt.title("Crime Statistics ")
    plt.xticks(range(len(datalist)), datalist.keys())
    print("-" * 50)
    plt.show()


# A function to generate Crime Report and validate user input before generating report
def crime_report():
    global latitude
    global longitude
    print("Latitude :", lat_var.get(), "and Longitude : ", lon_var.get())
    try:
        latitude = float(lat_var.get())
        longitude = float(lon_var.get())
        if latitude < 41.00 or latitude > 42.00:
            print("Please enter Latitude range for chicago")
            messagebox.showinfo(message="Please enter Latitude range for chicago!!! Eg : 41.808000")
        elif longitude < -88.00 or longitude > -87.00:
            print("Please enter Longitude range for chicago")
            messagebox.showinfo(message="Please enter Longitude range for chicago!!! Eg:, -87.111000")
        else:
            print("Selected Option : ", tkvar.get())
            if tkvar.get() == 'Violence Classification':
                donut_chart()
            elif tkvar.get() == 'Major Crimes':
                hor_bargraph()
            elif tkvar.get() == 'Arrest Ratio':
                pie_chart()
            if var1.get() or var2.get() or var3.get() or var4.get():
                print("-" * 50)
                ver_bargraph()
                print("-" * 50)
    except ValueError:
        print("Please enter valid value in Latitude & Longitude.Eg : 41.808000, -87.111000")
        messagebox.showinfo(message="Please enter valid value in Latitude & Longitude. \n Eg : 41.808000, -87.111000")


# A function to accept user input using GUI before generating report
def buildFrame():
    global lat_var, lon_var, select, tkvar, var1, var2, var3, var4
    main_screen.destroy()
    root = Tk()
    frame1 = Frame(root)
    root.geometry("300x400")
    root.title("Crime Data Analysis")
    # Add a grid
    frame1.grid(column=0, row=0, sticky=(N, W, E, S))
    frame1.columnconfigure(0, weight=1)
    frame1.rowconfigure(0, weight=1)
    frame1.pack(pady=10, padx=10)
    tkvar = StringVar(root)

    # Dictionary with options
    choices = {'Major Crimes', 'Violence Classification', 'Arrest Ratio'}
    tkvar.set('Major Crimes')  # set the default option

    popupMenu = OptionMenu(frame1, tkvar, *choices)
    Label(frame1, text="Choose the graph").grid(row=2, column=0)
    popupMenu.grid(row=2, column=1, sticky= W)

    # on change dropdown value
    lat_var = StringVar()
    lon_var = StringVar()

    Label(frame1, text="Latitude ").grid(row=0, column=0, sticky=W)
    latitude = Entry(frame1, textvariable=lat_var, highlightcolor="green", highlightthickness=1)
    latitude.grid(row=0, column=1, sticky=E)

    Label(frame1, text="Longitude ").grid(row=1, column=0, sticky=W)
    longitude = Entry(frame1, textvariable=lon_var, highlightcolor="green", highlightthickness=1)
    longitude.grid(row=1, column=1, sticky=E)

    Label(frame1, text="Select Crimes").grid(row=4, sticky=W)
    var1 = IntVar()
    Checkbutton(frame1, text="Burglary", onvalue=1, offvalue=0, variable=var1).grid(row=5, sticky=W)
    var2 = IntVar()
    Checkbutton(frame1, text="Weapons Violation", onvalue=1, offvalue=0, variable=var2).grid(row=6, sticky=W)
    var3 = IntVar()
    Checkbutton(frame1, text="Robbery", onvalue=1, offvalue=0, variable=var3).grid(row=7, sticky=W)
    var4 = IntVar()
    Checkbutton(frame1, text="Sex Offense", onvalue=1, offvalue=0, variable=var4).grid(row=8, sticky=W)

    print("-"*50)
    frame1 = Frame(root)  # add a row of buttons
    frame1.pack()
    Button(frame1, text="Generate Crime Report", command=crime_report).pack()
    print("-"*50)

    frame1 = Frame(root)  # add a row of buttons
    frame1.pack()
    Button(frame1, text="Exit", command=exit_app).pack()

    return root


# To exit GUI
def exit_app():
    from tkinter import messagebox
    if messagebox.askokcancel(message="Are you sure tou want to Quit .?!") == 1:
        print("*"*50, "Thank you for using our application", "*"*50)
        os._exit(1)


# To verify user before accessing Crime Analysis APP
def login_verification():
    if username_verify.get() == "" or password_verify.get() == "":
        print("Please enter User name and password")
        messagebox.showinfo(message="Please enter User name and password!!!")
    elif username_verify.get() == "admin" and password_verify.get() == "admin":
        print("Successfully Logged In.....")
        messagebox.showinfo(message="Successfully Logged in!!!")
        buildFrame()
    else:
        print("Invalid Log In.....")
        messagebox.showinfo(message="Invalid Log in! Please verify User name and password!")


# Function to display GUI for user authentication
def login():
    global username_verify
    global password_verify

    main_screen = Tk()  # create a GUI window
    main_screen.config(highlightcolor="black", highlightthickness=2)
    main_screen.geometry("300x250")  # set the configuration of GUI window
    main_screen.title("Account Login")

    frame1 = Frame(main_screen)
    frame1.pack()

    Label(frame1, text="Please enter details below to login").pack()
    Label(frame1, text="").pack()

    username_verify = StringVar()
    password_verify = StringVar()

    Label(frame1, text="Username * ").pack()
    username_login_entry = Entry(frame1, textvariable=username_verify, highlightcolor="green", highlightthickness=1)
    username_login_entry.pack()
    Label(frame1, text="").pack()

    Label(frame1, text="Password * ").pack()
    password__login_entry = Entry(frame1, textvariable=password_verify, show='*', highlightcolor="green", highlightthickness=1)
    password__login_entry.pack()
    Label(frame1, text="").pack()

    Button(frame1, text="Login", width=10, height=1, command=login_verification).pack()
    return main_screen


# start the GUI
main_screen = login()
main_screen.mainloop()
