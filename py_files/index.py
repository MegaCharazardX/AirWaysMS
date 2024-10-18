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

def Show_pass(_widget):
    _widget.bind("<ButtonPress>", lambda event, :_widget.configure(show = ""))

#=> --------Sign Up --------------------
def on_lbl_click() :
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
    
    U_name_Entry = CTkEntry(form_frm, width = 350, placeholder_text="Username")
    U_name_Entry.place(x = 25, y = 90)
    
    pass_Entry = CTkEntry(form_frm, width = 350, placeholder_text="Password", show = "*")
    show_btn = CTkButton(pass_Entry, width = 22, height=28, text="",border_color="#565b5e",border_width=2, fg_color="transparent")
    show_btn.place(x = 328, y=0)
    pass_Entry.place(x = 25, y = 130)
    
    re_pass_Entry = CTkEntry(form_frm, width = 350, placeholder_text="Re-Password")
    show_btn = CTkButton(re_pass_Entry, width = 22, height=28, text="",border_color="#565b5e",border_width=2, fg_color="transparent", command=lambda :(Show_pass()))
    show_btn.place(x = 328, y=0)
    re_pass_Entry.place(x = 25, y = 170)
#=>3------Sign In Page --------------------------------------
global PG_Sign_in
def PG_Sign_in():
    root.title ("http:www.HADAirlineManagementSystem.com/SignIn")
    for i in Main_fame.winfo_children():
        i.destroy()
    #div_frame.destroy()
    #fligt_search_result_frm.destroy()
    
    form_frm_width = 400
    form_frm_height = 300
    form_frm = CTkFrame(Main_fame, width=form_frm_width, height=form_frm_height)
    form_frm.place(x = (m_r_width/(2))-(form_frm_width/2),
                                  y = (m_r_height/(2)-(form_frm_height/2))
                                  )
    
    def go_back():
        for i in Main_fame.winfo_children():
            i.destroy()
        #fligt_search_result_frm.destroy()
        PG_search_flight_()
        
    dummy_back_btn = CTkButton(Main_fame,text="Back", command = go_back)
    dummy_back_btn.place(x =10, y = 10)

    login_lb = CTkLabel(form_frm, text = "LOGIN :-")
    login_lb.place(x = 10, y = 10)
    
    user_Entry = CTkEntry(form_frm, width = 350, placeholder_text= "Username")
    user_Entry.place(x = 25, y = 40)
    
    password_Entry = CTkEntry(form_frm, width = 350, placeholder_text= "Password")
    password_Entry.place(x = 25, y = 70)
    
    Login_btn = CTkButton(form_frm, text= "LOGIN", width= 350, corner_radius=100)
    Login_btn.place(x = 25, y = 110)
    
    No_of_hyphen = 41
    line_lbl = CTkLabel(form_frm, text = f"{'-'*No_of_hyphen} OR {'-'*No_of_hyphen}")
    line_lbl.place(x = 25, y = 140)
    
    Dnt_hv_acc_lbl = CTkLabel(form_frm, text="Don't have an account ? ")
    Dnt_hv_acc_lbl.place(x = 75, y = 170)
    Sign_up_lbl = CTkLabel(form_frm, text="Sign Up", font = ("Arial" , 12, "italic", "underline"))
    Sign_up_lbl.place(x = 215, y = 170)
    
    
    Sign_up_lbl.bind("<Button-1>", lambda event, : on_lbl_click())
    Sign_up_lbl.bind("<Enter>", lambda event, lbl = Sign_up_lbl: lbl.configure(text_color = "#007acc"))
    Sign_up_lbl.bind("<Leave>", lambda event, lbl = Sign_up_lbl: lbl.configure(text_color = "Light Gray"))

#=>2------Show Flights details --------------------------------------

global PG_search_flight_

def PG_search_flight_():
    root.title ("http:www.HADAirlineManagementSystem.com/Search_flights")
    if div_frame.winfo_exists():
        for i in div_frame.winfo_children():
            i.destroy()
        div_frame.destroy()
    
    temp_frm_width = 900
    temp_frm_height = 550
    global fligt_search_result_frm
    fligt_search_result_frm = CTkScrollableFrame (Main_fame, width=temp_frm_width, height = temp_frm_height)
    fligt_search_result_frm.place(x = (m_r_width/(2))-(temp_frm_width/2),
                                  y = (m_r_height/(2)-(temp_frm_height/2))
                                  )

    
    def go_back():
        for i in fligt_search_result_frm.winfo_children():
            i.destroy()
        fligt_search_result_frm.destroy()
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
        PG_Sign_in()
        
    for id, label in btn_data.items() :
        
        btn = CTkButton(fligt_search_result_frm, text = label, command = lambda id=id: on_btn_click(id)).pack(pady = 10)
        btns.append(btn)
        
# =>1-----Get Flight details---------------------------------------------------------------------   

def PG_Get_Flight_Details():
    global div_frame
    temp_frm_width = 500
    temp_frm_height = 300
    div_frame = CTkFrame(Main_fame,width=temp_frm_width, height = temp_frm_height)
    div_frm_xpos = 75
    din_frm_widget_width = 350
    div_frame.place(x = ((m_r_width/2)-(temp_frm_width/2)), y = ((m_r_height/2)- (temp_frm_height/2)))
    #lbl = CTkLabel(div_frame, text= "Book A Flight :- ", font = ("Freestyle Script", 18), bg_color="transparent", text_color= glb_clr_2)\
    #   .place(x = 10, y = 10)

    def Combo_get_origin_val(origin_combo_value):
        origin_airport = origin_combo_value
        #print(origin_airport)
        #print(departure_place)
        
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
        
    mulicity_radio_btn = createRadioButton(div_frame, "Multicity", "MulticityRadio", book_a_fligt_radio_val,Func_radio_btn, div_frm_xpos+270, rd_btn_y_pos)#. place(x = 90, y = 25)

    departure_place = StringVar(value="dep_combo_other")
    departure_place.set("Departure")
    S
    #print(departure_place)
    Origin_Airport = CTkComboBox(div_frame,width=din_frm_widget_width,
                                values= [
                                    "Boston",
                                    "Chennai",
                                    "Thiruvananthapuram"
                                    ],
                                    variable= departure_place, command = Combo_get_origin_val).place (x = div_frm_xpos, y = rd_btn_y_pos+50)

    departure_place = departure_place.get()
    departure_place = Origin_Airport
    #print(departure_place)

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
    #arrival_place = Dest_Airport
    #print(arrival_place)


    passenger_Class = CTkComboBox(div_frame,width=din_frm_widget_width, values=["Passenger/Class"]).place (x = div_frm_xpos, y = rd_btn_y_pos+114)

    #Date = CT
    Search_Fligths_btn = CTkButton(div_frame, text = "Search Fligths", width = din_frm_widget_width, corner_radius=75, command=lambda :(PG_search_flight_())).place(x = div_frm_xpos, y =185)

PG_Get_Flight_Details()

#----------------------------------------------------------------------------------

#root.resizable(True,True)
root.mainloop()

