from tkinter import*
from tkinter import messagebox 
arun=Tk()
arun.title("FLAMES !    Just For Fun!!!=====<>:)")
arun.iconbitmap(r'C:\Users\PK\Downloads\npp.7.bin.x64\code (1).ico')
#arun.tk.call('wm', 'iconphoto', arun._w, PhotoImage(file='code1.ico'))
'''
arun.overrideredirect(True)
# make a frame for the title bar
title_bar = Frame(arun, bg='#2e2e2e', relief='raised', bd=2,highlightthickness=0)

# put a close button on the title bar
close_button = Button(title_bar, text='X', command=arun.destroy,bg="#2e2e2e",padx=2,pady=2,activebackground='red',bd=0,font="bold",fg='white',highlightthickness=0)


# a canvas for the main area of the window
window = Canvas(arun, bg='#2e2e2e',highlightthickness=0)

# pack the widgets
title_bar.pack(expand=1, fill=X)
close_button.pack(side=RIGHT)
window.pack(expand=1, fill=BOTH)
xwin=None
ywin=None
# bind title bar motion to the move window function

def move_window(event):
    arun.geometry('+{0}+{1}'.format(event.x_arun, event.y_arun))
def change_on_hovering(event):
    global close_button
    close_button['bg']='red'
def return_to_normalstate(event):
    global close_button
    close_button['bg']='#2e2e2e'


title_bar.bind('<B1-Motion>', move_window)
close_button.bind('<Enter>',change_on_hovering)
close_button.bind('<Leave>',return_to_normalstate)
'''

ScreenWidth=arun.winfo_screenwidth()
ScreenHeight=arun.winfo_screenheight()

Awidth=750
Aheight=350
Ax=(ScreenWidth/2)-(Awidth/2)
Ay=(ScreenHeight/2)-(Aheight/2)
arun.configure(width=1000,height=350,background="#BADA55")
arun.geometry("%dx%d+%d+%d" % (Awidth,Aheight,Ax,Ay))
#arun.geometry("%dx%d+%d+%d" % (600,350,660,365))


def Re():
	e1.delete(0,END)
	e2.delete(0,END)
	#b2=Button(arun,text="Proceed",width=15,bg="#5AC18E",font="Calibri 15 bold").grid(row=3,column=1,padx=2)
	l4.grid_forget()
	e3.grid_forget()
	
	return
def pro():

	
	Your_Name=e1.get()
	Your_Partner_Name=e2.get()
	if Your_Name=="" or Your_Partner_Name=="" :
		messagebox.showinfo("Information","Please Enter the Names")
		return
	li1=[]
	li2=[]
	for letter in Your_Name.lower():
		li1.append(letter)
	for letter in Your_Partner_Name.lower():
		li2.append(letter)

	li3=[]
	li4=[]
	for i in li1:
		if i in li2:
			li2.remove(i)
			li3.append(i)
	for i in li3:
		li1.remove(i)

	li4=li1+li2
	
	x=len(li4)#5
	if x==0:
		messagebox.showinfo("Information","all letters are striked ,so not able to next move ,sorry!!")
		return
	start_pos=0
	li5=['f','l','a','m','e','s']

	if x> len(li5):
		x=x-len(li5)
	while len(li5)!=1:
		y=start_pos+x
		while y> len(li5):
			y-=len(li5)
		li5.remove(li5[y-1])
		start_pos=y-1
		x=len(li4)
		
	l4.grid(row=4,column=0,padx=5)
	
	e3.grid(row=5,column=0,columnspan=2,pady=20)
	e3.delete(0,END)
	if li5[0]=="f":
		e3.insert(0,(Your_Name+'  and  '+Your_Partner_Name +"  are  friends"))
	if li5[0]=="l":
		e3.insert(0,(Your_Name+ '  and  '+Your_Partner_Name +"  are  lovers"))
	if li5[0]=="a":
		e3.insert(0,(Your_Name+ '  and  '+Your_Partner_Name +"  are  Affection"))
	if li5[0]=="m":
		e3.insert(0,(Your_Name+ '  and  '+Your_Partner_Name +"  get  Marriage"))
	if li5[0]=="e":
		e3.insert(0,(Your_Name+ '  and  '+Your_Partner_Name +"  are  Enemies"))
	if li5[0]=="s":
		e3.insert(0,(Your_Name+ '  and  '+Your_Partner_Name +"  are  Siblings"))

	return
l1=Label(arun,text="WELCOME",bg="#BADA55",font="calibri 25 bold italic")

l2=Label(arun,text="Enter Your Name                :",width=25,anchor=W,font="calibri 15")

l3=Label(arun,text="Enter Your Partnar Name   :",width=25,anchor=W,font="calibri 15")
l4=Label(arun,text="Result   :",width=25,anchor=W,font="calibri 15")

l1.grid(row=0,column=0,columnspan=3)
l2.grid(row=1,column=0,padx=5)
l3.grid(row=2,column=0,padx=5)

e1=Entry(arun,width=40,font="calibri 15")
e2=Entry(arun,width=40,font="calibri 15")
e3=Entry(arun,width=40,font="calibri 15")
e1.grid(row=1,column=1,columnspan=3,pady=20,padx=5)
e2.grid(row=2,column=1,columnspan=3,pady=20,padx=5)

b1=Button(arun,text="Proceed",width=15,bg="#5AC18E",font="Calibri 15 bold",command=pro).grid(row=3,column=1,padx=2)
b2=Button(arun,text="Reset",width=15,bg="#5AC18E",font="Calibri 15 bold ",command=Re).grid(row=3,column=2,padx=2)
arun.mainloop()



'''
#flames
Your_Name=input("Enter Your Name")
Your_Partner_Name=input("Enter Your partner Name")

li1=[]
li2=[]
for letter in Your_Name.lower():
	li1.append(letter)
for letter in Your_Partner_Name.lower():
	li2.append(letter)

li3=[]
li4=[]
for i in li1:
	if i in li2:
		li2.remove(i)
		li3.append(i)
for i in li3:
	li1.remove(i)

li4=li1+li2

x=len(li4)#5
start_pos=0
li5=['f','l','a','m','e','s']

if x> len(li5):
	x=x-len(li5)
while len(li5)!=1:
	y=start_pos+x
	while y> len(li5):
		y-=len(li5)
	li5.remove(li5[y-1])
	start_pos=y-1
	x=len(li4)
	
if li5[0]=="f":
	print(Your_Name, "and ",Your_Partner_Name ," are friends")
if li5[0]=="l":
	print(Your_Name, "and ",Your_Partner_Name ," are lovers")
if li5[0]=="a":
	print(Your_Name, "and ",Your_Partner_Name ," are Affection")
if li5[0]=="m":
	print(Your_Name, "and ",Your_Partner_Name ," get Marriage")
if li5[0]=="e":
	print(Your_Name, "and ",Your_Partner_Name ," are Enemies")
if li5[0]=="s":
	print(Your_Name, "and ",Your_Partner_Name ," are Siblings")
'''