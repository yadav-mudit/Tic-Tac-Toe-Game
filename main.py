import customtkinter as ctk

p1="X"
p2="O"

chance=p1

list=["-","-","-","-","-","-","-","-","-"]

root = ctk.CTk()

root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(720,480)

root.title("Tic Tac Toe")


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def freeze_all():
    button1.configure(state=ctk.DISABLED)
    button2.configure(state=ctk.DISABLED)
    button3.configure(state=ctk.DISABLED)
    button4.configure(state=ctk.DISABLED)
    button5.configure(state=ctk.DISABLED)
    button6.configure(state=ctk.DISABLED)
    button7.configure(state=ctk.DISABLED)
    button8.configure(state=ctk.DISABLED)
    button9.configure(state=ctk.DISABLED)

def check_condition():
    global list
    countt=0
    winner=0
    
    if list[0]==p1 and list[1]==p1 and list[2]==p1:
        winner_label_p1.place(x=310,y=420)
        freeze_all()
        winner=winner+1

    if list[0]==p2 and list[1]==p2 and list[2]==p2:
        winner_label_p2.place(x=310,y=420)
        freeze_all()
        winner=winner+1

    if list[0]==p1 and list[4]==p1 and list[8]==p1:
        winner_label_p1.place(x=310,y=420)
        freeze_all()
        winner=winner+1

    if list[0]==p2 and list[4]==p2 and list[8]==p2:
        winner_label_p2.place(x=310,y=420)
        freeze_all()
        winner=winner+1
    
    if list[0]==p1 and list[3]==p1 and list[6]==p1:
        winner_label_p1.place(x=310,y=420)
        freeze_all()
        winner=winner+1

    if list[0]==p2 and list[3]==p2 and list[6]==p2:
        winner_label_p2.place(x=310,y=420)
        freeze_all()
        winner=winner+1
    
    if list[1]==p1 and list[4]==p1 and list[7]==p1:
        winner_label_p1.place(x=310,y=420)
        freeze_all()
        winner=winner+1

    if list[1]==p2 and list[4]==p2 and list[7]==p2:
        winner_label_p2.place(x=310,y=420)
        freeze_all()
        winner=winner+1
    
    if list[2]==p1 and list[5]==p1 and list[8]==p1:
        winner_label_p1.place(x=310,y=420)
        freeze_all()
        winner=winner+1

    if list[2]==p2 and list[5]==p2 and list[8]==p2:
        winner_label_p2.place(x=310,y=420)
        freeze_all()
        winner=winner+1

    if list[2]==p1 and list[4]==p1 and list[6]==p1:
        winner_label_p1.place(x=310,y=420)
        freeze_all()
        winner=winner+1

    if list[2]==p2 and list[4]==p2 and list[6]==p2:
        winner_label_p2.place(x=310,y=420)
        freeze_all()
        winner=winner+1

    if list[3]==p1 and list[4]==p1 and list[5]==p1:
        winner_label_p1.place(x=310,y=420)
        freeze_all()
        winner=winner+1

    if list[3]==p2 and list[4]==p2 and list[5]==p2:
        winner_label_p2.place(x=310,y=420)
        freeze_all()
        winner=winner+1

    if list[6]==p1 and list[7]==p1 and list[8]==p1:
        winner_label_p1.place(x=310,y=420)
        freeze_all()
        winner=winner+1

    if list[6]==p2 and list[7]==p2 and list[8]==p2:
        winner_label_p2.place(x=310,y=420)
        freeze_all()
        winner=winner+1
    for i in list:
        if i=="-":
            countt=countt+1
    if countt==0 and winner==0:
            winner_label_draw.place(x=330,y=420)

    

def on_press1():
    
    global chance
    global list   
    button1.configure(text_color="black",text=chance,font=my_font,state=ctk.DISABLED)
    if chance==p1:
       button1.configure(fg_color="light blue")
       list[0]=chance
       chance=p2

    else:
        button1.configure(fg_color="light green")
        list[0]=chance
        chance=p1 
    check_condition()


def on_press2():
    
    global chance
    global list
    button2.configure(text=chance,font=my_font,text_color="black",state=ctk.DISABLED)
    if chance==p1:
       button2.configure(fg_color="light blue")
       list[1]=chance
       chance=p2
    else:
        button2.configure(fg_color="light green")
        list[1]=chance
        chance=p1 
    check_condition()

def on_press3():
    
    global chance
    global list
    button3.configure(text=chance,font=my_font,text_color="black",state=ctk.DISABLED)
    if chance==p1:
       button3.configure(fg_color="light blue")
       list[2]=chance
       chance=p2
    else:
        button3.configure(fg_color="light green")
        list[2]=chance
        chance=p1 
    check_condition()

def on_press4():
    
    global chance
    global list
    button4.configure(text=chance,font=my_font,text_color="black",state=ctk.DISABLED)
    if chance==p1:
       button4.configure(fg_color="light blue")
       list[3]=chance
       chance=p2
    else:
        button4.configure(fg_color="light green")
        list[3]=chance
        chance=p1 
    check_condition()

def on_press5():
    
    global chance
    global list
    button5.configure(text=chance,font=my_font,text_color="black",state=ctk.DISABLED)
    if chance==p1:
       button5.configure(fg_color="light blue")
       list[4]=chance
       chance=p2
    else:
        button5.configure(fg_color="light green")
        list[4]=chance
        chance=p1 
    check_condition()

def on_press6():
    
    global chance
    global list
    button6.configure(text=chance,font=my_font,text_color="black",state=ctk.DISABLED)
    if chance==p1:
       button6.configure(fg_color="light blue")
       list[5]=chance
       chance=p2
    else:
        button6.configure(fg_color="light green")
        list[5]=chance
        chance=p1 
    check_condition()

def on_press7():
    
    global chance
    global list
    button7.configure(text=chance,font=my_font,text_color="black",state=ctk.DISABLED)
    if chance==p1:
       button7.configure(fg_color="light blue")
       list[6]=chance
       chance=p2
    else:
        button7.configure(fg_color="light green")
        list[6]=chance
        chance=p1 
    check_condition()

def on_press8():
    
    global chance
    global list
    button8.configure(text=chance,font=my_font,text_color="black",state=ctk.DISABLED)
    if chance==p1:
       button8.configure(fg_color="light blue")
       list[7]=chance
       chance=p2
    else:
        button8.configure(fg_color="light green")
        list[7]=chance
        chance=p1 
    check_condition()

def on_press9():
    
    global chance
    global list
    button9.configure(text=chance,font=my_font,text_color="black",state=ctk.DISABLED)
    if chance==p1:
       button9.configure(fg_color="light blue")
       list[8]=chance
       chance=p2
    else:
        button9.configure(fg_color="light green")
        list[8]=chance
        chance=p1 
    check_condition()


main_frame = ctk.CTkFrame(root)
main_frame.pack(expand=True,fill=ctk.BOTH,padx=10,pady=10)

my_font = ctk.CTkFont(family="Comic Sans", size=34, weight="bold")

label = ctk.CTkLabel(main_frame,text="TIC TAC TOE")
label.place(x=310,y=30)

frame1= ctk.CTkFrame(main_frame,height = 100,width=100)
frame1.place(x=180,y=70)
button1 = ctk.CTkButton(frame1,text_color="black",text="",command=on_press1,height=100,width=100,fg_color="#808080")
button1.pack()

frame2= ctk.CTkFrame(main_frame,height = 100,width=100)
frame2.place(x=300,y=70)
button2 = ctk.CTkButton(frame2,text_color="black",text="",command=on_press2,height=100,width=100,fg_color="#808080")
button2.pack()

frame3= ctk.CTkFrame(main_frame,height = 100,width=100)
frame3.place(x=420,y=70)
button3 = ctk.CTkButton(frame3,text_color="black",text="",command=on_press3,height=100,width=100,fg_color="#808080")
button3.pack()

frame4= ctk.CTkFrame(main_frame,height = 100,width=100)
frame4.place(x=180,y=190)
button4 = ctk.CTkButton(frame4,text_color="black",text="",command=on_press4,height=100,width=100,fg_color="#808080")
button4.pack()

frame5= ctk.CTkFrame(main_frame,height = 100,width=100)
frame5.place(x=300,y=190)
button5 = ctk.CTkButton(frame5,text_color="black",text="",command=on_press5,height=100,width=100,fg_color="#808080")
button5.pack()

frame6= ctk.CTkFrame(main_frame,height = 100,width=100)
frame6.place(x=420,y=190)
button6 = ctk.CTkButton(frame6,text_color="black",text="",command=on_press6,height=100,width=100,fg_color="#808080")
button6.pack()

frame7= ctk.CTkFrame(main_frame,height = 100,width=100)
frame7.place(x=180,y=310)
button7 = ctk.CTkButton(frame7,text_color="black",text="",command=on_press7,height=100,width=100,fg_color="#808080")
button7.pack()

frame8= ctk.CTkFrame(main_frame,height = 100,width=100)
frame8.place(x=300,y=310)
button8 = ctk.CTkButton(frame8,text_color="black",text="",command=on_press8,height=100,width=100,fg_color="#808080")
button8.pack()

frame9= ctk.CTkFrame(main_frame,height = 100,width=100)
frame9.place(x=420,y=310)
button9 = ctk.CTkButton(frame9,text_color="black",text="",command=on_press9,height=100,width=100,fg_color="#808080")
button9.pack()

winner_label_p1 = ctk.CTkLabel(main_frame,text="WINNER IS P1!!",fg_color="light blue",text_color="black")
winner_label_p2 = ctk.CTkLabel(main_frame,text="WINNER IS P2!!",fg_color="light green",text_color="black")
winner_label_draw = ctk.CTkLabel(main_frame,text="DRAW!!",fg_color="white",text_color="black")

root.mainloop()
