from tkinter import*
window = Tk()
window.geometry("400x400")
window.title("Login")
window.config(background="pink")
# creating labels

username = Label(window,text="Username",bg="green")
username.place(x=100,y=100)

user_name_input=Entry(window,width=40)
user_name_input.place(x=190,y=100)

password = Label(window,text="Pssword",bg="green")
password.place(x=100,y=200)

user_password = Entry(window,width=40)
user_password.place(x=190,y=200)

# bd is border
button = Button(window,text="Submit",bd=5,bg="orange")
button.place(x=100,y=300)







window.mainloop()