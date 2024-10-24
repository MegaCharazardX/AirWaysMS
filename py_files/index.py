from customtkinter import *
from PIL import Image
import os 
from subprocess import call
import Global_Config as GC
import pymysql
import tkinter as tk 
from Usable_screen import ScreenGeometry as SG
from colorama import Fore

m_r_width, m_r_height = SG().GetUsableScreenSize()[0], SG().GetUsableScreenSize()[1]

root = CTk()
#root.attributes("-fullscreen", True)
root.title("http:www.HADAirlineManagementSystem.com/")
set_appearance_mode("Dark")
GC.centreScreen(root,root, m_r_width, m_r_height)
root.state("zoomed")
root.minsize(m_r_width, m_r_height)
root.geometry(f"{m_r_width}x{m_r_height}")

#---------GLOBAL VARIABLES --------
_isSignedIn = False
global prev_page
prev_page = 0
glb_clr_1 = "blue"
glb_clr_2 = "green"
glb_clr_3 = "yellow"
global  PG_Get_Flight_Details
#--------------------- GLOBAL FUNCTIONS ---------------------------------

def createRadioButton (_frame ,_text : str , _value, _variable, _command,  _xpos : int, _ypos  : int):
    tmpRdBtn = CTkRadioButton(_frame, text = _text , value = _value, variable = _variable,width = 75, command = lambda :(_command()) )
    tmpRdBtn.place(x =_xpos, y = _ypos)
    return tmpRdBtn

#------------------------------------------------------
Main_fame = CTkFrame(root, width = m_r_width, height= m_r_height-24, border_width=2, border_color= glb_clr_1, fg_color="transparent")
Main_fame.place(x = 0, y = 0)
#=> --------Sign Up --------------------
global PG_Sign_Up
def PG_Sign_Up() :
    #print("Hi")
    root.title ("http:www.HADAirlineManagementSystem.com/SignUp")
    for i in Main_fame.winfo_children():
        i.destroy()
    #div_frame.destroy()
    #fligt_search_result_frm.destroy()
    
    form_frm_width = 400
    form_frm_height = 600
    form_frm = CTkFrame(Main_fame, width=form_frm_width, height=form_frm_height)
    form_frm.place(x = (m_r_width/(2))-(form_frm_width/2),
                                  y = (m_r_height/(2)-(form_frm_height/2))
                                  )
    
    def go_back():
        for i in Main_fame.winfo_children():
            i.destroy()
        #fligt_search_result_frm.destroy()
        PG_Sign_in()
        
    
    dummy_back_btn = CTkButton(Main_fame,text="Back", command = go_back)
    dummy_back_btn.place(x =10, y = 10)
    
    F_name_Entry = CTkEntry(form_frm, width = 350, placeholder_text="First Name")
    F_name_Entry.place(x = 25, y = 10)
    
    L_name_Entry = CTkEntry(form_frm, width = 350, placeholder_text="Last Name")
    L_name_Entry.place(x = 25, y = 50)
    
    def Func_radio_btn():
        print(Gender.get())

    Gender = StringVar(value = "other")
    print(Gender.get())
    
    rd_btn_y_pos = 90
    
    male_radio_btn = createRadioButton(form_frm, "Male","Male",Gender,Func_radio_btn,25, rd_btn_y_pos)#. place(x = 10, y = 25)
        
    female_radio_btn = createRadioButton(form_frm,"Female", "Female", Gender,Func_radio_btn, 25+130, rd_btn_y_pos)#. place(x = 50, y = 25)
        
    female_radio_btn = createRadioButton(form_frm,"Other", "Other", Gender,Func_radio_btn, 25+130 + 130, rd_btn_y_pos)
    
    
    U_name_Entry = CTkEntry(form_frm, width = 350, placeholder_text="Username")
    U_name_Entry.place(x = 25, y = 130)
    
    
    gmail_Entry = CTkEntry(form_frm, width = 350, placeholder_text="Gmail")
    gmail_Entry.place(x = 25, y = 130+40)
    
    
    def Show_pass():
        if pass_Entry.cget('show') == '*':
            pass_Entry.configure(show='')  # Show the password
            show_btn.configure(text=" Hide ")
        else:
            pass_Entry.configure(show='*')  # Hide the password
            show_btn.configure(text="Show")
            
    def Re_Show_pass():
        if re_pass_Entry.cget('show') == '*':
            re_pass_Entry.configure(show='')  # Show the password
            re_show_btn.configure(text=" Hide ")
        else:
            re_pass_Entry.configure(show='*')  # Hide the password
            re_show_btn.configure(text="Show")
    
    pass_Entry = CTkEntry(form_frm, width = 350, placeholder_text="Password", show = "*")
    show_btn = CTkButton(pass_Entry, width = 22, height=28, text="Show",border_color="#565b5e",border_width=2, fg_color="transparent", command=Show_pass)
    show_btn.place(x = 304, y=0)
    pass_Entry.place(x = 25, y = 170+40)
    
    re_pass_Entry = CTkEntry(form_frm, width = 350, placeholder_text="Re-Password")
    re_show_btn = CTkButton(re_pass_Entry, width = 22, height=28, text="Show",border_color="#565b5e",border_width=2, fg_color="transparent", command=Re_Show_pass)
    re_show_btn.place(x = 304, y=0)
    re_pass_Entry.place(x = 25, y = 210+40)
    
    phonnumber_Entry = CTkEntry(form_frm, 350, placeholder_text="Phone Number")
    phonnumber_Entry.place(x = 25, y =250+40)
    
    dob_Widget = CTk
    
    Create_acc_btn = CTkButton(form_frm, width = 350, text="Create Account", corner_radius=100)
    Create_acc_btn.place(x = 25, y = 290+40)
    
#=>3------Sign In Page --------------------------------------
global PG_Sign_in
def PG_Sign_in():
    root.title ("http:www.HADAirlineManagementSystem.com/SignIn")
    for i in Main_fame.winfo_children():
        i.destroy()
    #div_frame.destroy()
    #fligt_search_result_frm.destroy()
    
    form_frm_width = 400
    form_frm_height = 340
    form_frm = CTkFrame(Main_fame, width=form_frm_width, height=form_frm_height)
    form_frm.place(x = (m_r_width/(2))-(form_frm_width/2),
                                  y = (m_r_height/(2)-(form_frm_height/2))
                                  )
    
    def go_back():
        for i in Main_fame.winfo_children():
            i.destroy()
        #fligt_search_result_frm.destroy()
        Main_frm_Authentication_Btns()
        PG_search_flight_()
        
    dummy_back_btn = CTkButton(Main_fame,text="Back", command = go_back)
    dummy_back_btn.place(x =10, y = 10)

    login_lb = CTkLabel(form_frm, text = "LOGIN")
    login_lb.place(x = 10, y = 10)
    
    user_Entry = CTkEntry(form_frm, width = 350, placeholder_text= "Username")
    user_Entry.place(x = 25, y = 40)
    
    password_Entry = CTkEntry(form_frm, width = 350, placeholder_text= "Password")
    password_Entry.place(x = 25, y = 80)
    
    def Login_authentication():
        _isSignedIn = True
        print("Signed In")
        if prev_page ==1:
            PG_Get_Flight_Details()
        elif prev_page == 2:
            PG_search_flight_()
    
    Login_btn = CTkButton(form_frm, text= "LOGIN", width= 350, corner_radius=100, command=Login_authentication)
    Login_btn.place(x = 25, y = 120)
    
    No_of_hyphen = 41
    line_lbl = CTkLabel(form_frm, text = f"{'-'*No_of_hyphen} OR {'-'*No_of_hyphen}")
    line_lbl.place(x = 25, y = 150)
    
    Gmail_Entry = CTkEntry(form_frm, width = 350, placeholder_text= "Gmail")
    Gmail_Entry.place(x = 25, y = 180)
    
    password_Entry2 = CTkEntry(form_frm, width = 350, placeholder_text= "Password")
    password_Entry2.place(x = 25, y =220)
    
    Login_btn2 = CTkButton(form_frm, text= "LOGIN", width= 350, corner_radius=100, command=Login_authentication)
    Login_btn2.place(x = 25, y = 260)
    

    tempxpos = 100
    Dnt_hv_acc_lbl = CTkLabel(form_frm, text="Don't have an account ? ")
    Dnt_hv_acc_lbl.place(x = tempxpos, y = 300)
    Sign_up_lbl = CTkLabel(form_frm, text="Sign Up", font = ("Arial" , 12, "italic", "underline"))
    Sign_up_lbl.place(x = tempxpos + 140, y = 300)
    
    
    Sign_up_lbl.bind("<Button-1>", lambda event, : PG_Sign_Up())
    Sign_up_lbl.bind("<Enter>", lambda event, lbl = Sign_up_lbl: lbl.configure(text_color = "#007acc"))
    Sign_up_lbl.bind("<Leave>", lambda event, lbl = Sign_up_lbl: lbl.configure(text_color = "Light Gray"))

#=>2------Show Flights details --------------------------------------

global PG_search_flight_
def PG_search_flight_():
    prev_page = 2
    print(prev_page)
    root.title ("http:www.HADAirlineManagementSystem.com/Search_flights")
    if div_frame.winfo_exists():
        for i in div_frame.winfo_children():
            i.destroy()
        div_frame.destroy()
    
    temp_frm_width = 900
    temp_frm_height = 550
    global fligt_search_result_frm
    fligt_search_result_frm = CTkScrollableFrame (Main_fame, width=temp_frm_width, height = temp_frm_height, scrollbar_button_color= None)
    fligt_search_result_frm.place(x = (m_r_width/(2))-(temp_frm_width/2),
                                  y = (m_r_height/(2)-(temp_frm_height/2))
                                  )

    
    def go_back():
        for i in Main_fame.winfo_children():
            i.destroy()
        #fligt_search_result_frm.destroy()
        Main_frm_Authentication_Btns()
        PG_Get_Flight_Details()
        
    dummy_back_btn = CTkButton(Main_fame,text="Back", command = go_back)
    dummy_back_btn.place(x =10, y = 10)
    
    btns = []

    btn_data= {
        1:"F1",
        2:"F2",
        3:"F3",
        4:"F4",
        5:"F5"
    }

    def on_btn_click(index):
        print(f"{index} clicked. ")
        if _isSignedIn == True:
            print("Signed In")
            pass#----------------------------------------------------------------------------------------------------------------
        else :
            PG_Sign_in()
        
    for id, label in btn_data.items() :
        
        btn = CTkButton(fligt_search_result_frm, text = label, command = lambda id=id: on_btn_click(id)).pack(pady = 10)
        btns.append(btn)
        
# =>1-----Get Flight details---------------------------------------------------------------------   

def PG_Get_Flight_Details():
    global div_frame    
    for i in Main_fame.winfo_children():
        i.destroy()
        
    prev_page = 1
    print(prev_page)
    temp_frm_width = 500
    temp_frm_height = 300
    div_frame = CTkFrame(Main_fame,width=temp_frm_width, height = temp_frm_height)
    div_frm_xpos = 75
    din_frm_widget_width = 350
    div_frame.place(x = ((m_r_width/2)-(temp_frm_width/2)), y = ((m_r_height/2)- (temp_frm_height/2)))
    
    def Combo_get_origin_val(origin_combo_value):
        origin_airport = origin_combo_value
        
    def Combo_get_dest_val(dest_combo_value):
        dest_airport = dest_combo_value
        #print(dest_airport)


    def Func_radio_btn():
        print(book_a_fligt_radio_val.get())

    book_a_fligt_radio_val = StringVar(value = "other")
    print(book_a_fligt_radio_val.get())
    rd_btn_y_pos = 20
    return_radio_btn = createRadioButton(div_frame,"Return","ReturnRadio",book_a_fligt_radio_val,Func_radio_btn,div_frm_xpos, rd_btn_y_pos)#. place(x = 10, y = 25)
        
    one_way_radio_btn = createRadioButton(div_frame,"One Way", "OnewayRadio", book_a_fligt_radio_val,Func_radio_btn, div_frm_xpos+130, rd_btn_y_pos)#. place(x = 50, y = 25)
        
    #mulicity_radio_btn = createRadioButton(div_frame, "Multicity", "MulticityRadio", book_a_fligt_radio_val,Func_radio_btn, div_frm_xpos+270, rd_btn_y_pos)#. place(x = 90, y = 25)

    departure_place = StringVar(value="dep_combo_other")
    departure_place.set("Departure")

    Origin_Airport = CTkComboBox(div_frame,width=din_frm_widget_width,
                                values= [
                                    "Boston",
                                    "Chennai",
                                    "Thiruvananthapuram"
                                    ],
                                    variable= departure_place, command = Combo_get_origin_val).place (x = div_frm_xpos, y = rd_btn_y_pos+50)

    departure_place = Origin_Airport

    arrival_place = StringVar(value="des_combo_other")
    Dest_Airport = CTkComboBox(div_frame,width=din_frm_widget_width, 
                            values=[
                                    "Boston",
                                    "Chennai",
                                    "Thiruvananthapuram"
                                ],
                            variable= arrival_place, command= Combo_get_dest_val).place (x = div_frm_xpos, y = rd_btn_y_pos+79)

    arrival_place.set("Destination")
    arrival_place = arrival_place.get()


    passenger_Class = CTkComboBox(div_frame,width=din_frm_widget_width, values=["Passenger/Class"]).place (x = div_frm_xpos, y = rd_btn_y_pos+114)

    def Null_Check():
        arrival_place = arrival_place.get()
        departure_place = departure_place.get()
        radio_val = book_a_fligt_radio_val.get()
        if arrival_place  or departure_place or radio_val == "other":
            error_label = CTkLabel(div_frame, text = "Feilds Cannot Be Empty", font = ("Bradley Hand ITC" , 15, "italic", "bold"), text_color = "red")
            error_label.place(x = 75, y = 170)
            def refresh():
                error_label.destroy()
            error_label.after(3000, refresh)
        
    #Date = CT
    Search_Fligths_btn = CTkButton(div_frame, text = "Search Fligths", width = din_frm_widget_width, corner_radius=75, command=lambda :(Null_Check())).place(x = div_frm_xpos, y =185)
    Main_frm_Authentication_Btns()
    
global Main_frm_Authentication_Btns
def Main_frm_Authentication_Btns():
        
    temp_xpos = 300
    Sign_in_btn = CTkButton(Main_fame, text = "Sign In", command= PG_Sign_in)
    Sign_in_btn.place(x = temp_xpos, y = 10)

    Sign_up_btn = CTkButton(Main_fame, text = "Sign Up", fg_color="transparent", border_color= "grey", border_width=2, command=PG_Sign_Up)
    Sign_up_btn.place(x = temp_xpos+150, y = 10)

Main_frm_Authentication_Btns()

PG_Get_Flight_Details()

#----------------------------------------------------------------------------------

#root.resizable(True,True)
root.mainloop()

