import subprocess
import smtplib
import os
import sys
# KU

# def install(package):
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# # List of required packages
# required_packages = ["customtkinter", 
#                      "matplotlib", 
#                      "pillow",
#                      "pymysql",
#                      "colorama",
#                      "tkcalendar"
#                     ]

# # Install missing packages
# for package in required_packages:
#     try:
#         __import__(package)
#         print(f"{package} Succesfully installed.")
#     except ImportError:
#         install(package)

from customtkinter import *
from PIL import Image
from subprocess import call
import Global_Config as GC
import pymysql
from tkcalendar import Calendar
import tkinter as tk 
from Usable_screen import ScreenGeometry as SG
from tkcalendar import Calendar
from datetime import datetime
from tkinter import Toplevel
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

con = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd  = "*password*11",
    database = "airwaysms2_0"
                    )

cur = con.cursor()
#---------GLOBAL VARIABLES --------
global prev_page, _isSignedIn, User, is_flight_details_obtained
_isSignedIn = False
is_flight_details_obtained = False
User = ""
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

def errorLabeling(_Master, _text : str, _font = ("Bradley Hand ITC" , 18, "italic", "bold"), _textcolor = "red", _x = 10, _y = 10, _cooldowntime = 3000):
    error_label = CTkLabel(_Master, text = _text, font = _font, text_color = _textcolor)
    error_label.place(x = _x, y = _y)
    def refresh():
        error_label.destroy()
    error_label.after(_cooldowntime, refresh)
#------------------------------------------------------

Main_fame = CTkFrame(root, width = m_r_width, height= m_r_height-24, border_width=2, border_color= "#007acc", fg_color="transparent")
Main_fame.place(x = 0, y = 0)

global PG_Payment
def PG_Payment():
    root.title ("http:www.HADAirlineManagementSystem.com/Payment")
    for i in Main_fame.winfo_children():
        i.destroy()
    
    form_frm_width = 400
    form_frm_height = 210
    form_frm = CTkFrame(Main_fame, width=form_frm_width, height=form_frm_height)
    form_frm.place(x = (m_r_width/(2))-(form_frm_width/2), y = (m_r_height/(2)-(form_frm_height/2)))
    
    def go_back():
        global _isSignedIn
        if _isSignedIn == True :
            for i in Main_fame.winfo_children():
                i.destroy()
            Main_frm_Authentication_Btns()
            PG_search_flight_()
        else : 
            for i in Main_fame.winfo_children():
                i.destroy()
            Main_frm_Authentication_Btns()
            PG_Get_Flight_Details()
            
    dummy_back_btn = CTkButton(Main_fame, text="Back", command = go_back)
    dummy_back_btn.place(x =10, y = 10)
    
    Payment_Method_label = CTkLabel(form_frm, text= "Select Payment Method")
    Payment_Method_label.place(x = 25, y = 10)
    
    CBF_width = 290
    CBF_height = 28
    Centre_btn_frame = CTkFrame(form_frm, height=CBF_height, width= CBF_width, fg_color= "transparent") 
    Centre_btn_frame.place(x = (form_frm_width/(2))-(CBF_width/2),
                                  y = (form_frm_height/(2)-(CBF_height/2)) )
    
    def on_UPI_btn_click():
        root.title ("http:www.HADAirlineManagementSystem.com/Payment/UPI")
        for i in form_frm.winfo_children():
            i.destroy()
        
        Temp_Entry_Width = 350
    
        UPI_Method_label = CTkLabel(form_frm, text= "UPI -")
        UPI_Method_label.place(x = 25, y = 10)
        
        UPI_Number_Entry = CTkEntry(form_frm, placeholder_text= "UPI Number",width= Temp_Entry_Width)
        UPI_Number_Entry.place(x =25, y = 50)
        
        Amount_Entry = CTkEntry(form_frm, placeholder_text= "Amount",width= Temp_Entry_Width)
        Amount_Entry.place(x =25, y = 90)
        
        def _on_UPI_pay_btn_click():
            UPI_Number = UPI_Number_Entry.get()
            Amount = Amount_Entry.get()
            print(User)
            
            if UPI_Number == "" or Amount == "":
                errorLabeling(form_frm, "Feilds Can Not Be Empty", _x = 90, _y = 170)
            
            elif UPI_Number.isdigit() == False or Amount.isdigit() == False:
                is_flight_details_obtained
            else:
                tempqry = "SELECT COUNT(*) FROM payment"
                cur.execute(tempqry)
                p_id = int(cur.fetchone())[0] + 1
                tempqry = "SELECT UID FROM user_details WHERE U_name = {%s}"
                cur.execute(tempqry, User)
                Uid = cur.fetchone()
                tempqry = "INSERT PID, P_UID, AMOUNT, P_STATUS, P_UPI_NUM INTO payment VALUES (%s,%s,%s,%s,%s)"
                cur.execute(tempqry, (int(p_id), int(Uid), int(Amount), 400, int(UPI_Number)))
                errorLabeling(form_frm, "Payment Sucessful", _textcolor = "green", _x = 90, _y = 170)
                
        Pay_btn = CTkButton(form_frm, width= Temp_Entry_Width, text = "Pay", corner_radius= 100, command= _on_UPI_pay_btn_click)
        Pay_btn.place(x = 25, y = 130)
        
    UPI_btn = CTkButton(Centre_btn_frame, text = "UPI", command= on_UPI_btn_click)
    UPI_btn.place(x = 0, y = 0)
    
    NetBanking_btn = CTkButton(Centre_btn_frame, text = "Net Banking")
    NetBanking_btn.place(x = 150, y = 0)
    
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
        
    def NullCheck():
        global DOB_selected_date, cal
        F_name = F_name_Entry.get()
        L_name = L_name_Entry.get()
        U_name = U_name_Entry.get()
        _Gender = Gender.get()
        if "cal" in globals():
            dob = cal.get_date()
            dob_dt = datetime.strptime(dob, "%Y-%m-%d")
            today = datetime.today()
            Age = today.year - dob_dt.year
            if (today.month, today.day) > (dob_dt.month, dob_dt.day):
                Age +=1
        else :
            dob = ""
        Gmail = gmail_Entry.get()
        _pass = pass_Entry.get()
        _re_pass = re_pass_Entry.get()
        phonenumber = phonnumber_Entry.get()
        print(F_name,L_name,U_name,dob,Gmail,_pass,_re_pass,phonenumber)
        print(_Gender)
        
        tmp_qry =f"SELECT U_name FROM user_details WHERE U_name= '{U_name}'"
        cur.execute(tmp_qry)
        row = cur.fetchone()
        if F_name == "" or L_name == "" or U_name == "" or dob == "" or  Gmail == "" or _pass == "" or _re_pass == "" or phonenumber == "" or _Gender == "other" :
            errorLabeling(form_frm, "Feilds Cannot Be Null", _x = 110, _y = 410)

        if _pass != _re_pass:
            errorLabeling(form_frm, "Passwords Don't Match", _x = 110, _y = 410)
            
        elif row :
            errorLabeling(form_frm, "Username Already Exist", _x = 110, _y = 410)
        
        else:
            cur.execute("SELECT Count(*) FROM user_details")
            ans = cur.fetchone()  # ans will be a tuple, e.g., (5,)

            # Extract the count value from the tuple and add 1
            new_uid = ans[0] + 1

            # Insert the new record with the new UID
            tmp_qry = """
                INSERT INTO user_details (UID, UF_name, UL_name, U_name, U_Gmail, U_phno, U_password, U_dob, U_gender, U_AGE)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(tmp_qry, (new_uid, F_name, L_name, U_name, Gmail, phonenumber, _pass, dob, _Gender, Age))

            cur.execute("SELECT Count(*) FROM user_details")
            ans2 = cur.fetchone()

            con.commit()
            if ans2 > ans :
                errorLabeling(form_frm, "Succesfully Added", _textcolor = "green", _x = 110, _y = 410)
                def _fun():
                    global _isSignedIn, User
                    _isSignedIn = True
                    User = U_name
                    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!--------------------------------------------
                    PG_Get_Flight_Details()
                errorLabeling(form_frm, "Succesfully Added", _textcolor = "green", _x = 110, _y = 410)
                fun_lbl = CTkLabel(form_frm)
                fun_lbl.after(4000, _fun)    
            else:
                errorLabeling(form_frm, "Error Occured While Inserting Try Restarting", _x = 5, _y = 410)
               
    dummy_back_btn = CTkButton(Main_fame,text="Back", command = go_back)
    dummy_back_btn.place(x =10, y = 10)
    
    F_name_Entry = CTkEntry(form_frm, width = 350, placeholder_text="First Name")
    F_name_Entry.place(x = 25, y = 10)
    
    L_name_Entry = CTkEntry(form_frm, width = 350, placeholder_text="Last Name")
    L_name_Entry.place(x = 25, y = 50)
    
    def Func_radio_btn():
        global _Gender
        _Gender = Gender.get()
        print(_Gender)
    global Gender
    Gender = StringVar(value = "other")
    print(Gender.get())
    
    rd_btn_y_pos = 90
    
    male_radio_btn = createRadioButton(form_frm, "Male","M",Gender,Func_radio_btn,25, rd_btn_y_pos)#. place(x = 10, y = 25)
        
    female_radio_btn = createRadioButton(form_frm,"Female", "F", Gender,Func_radio_btn, 25+130, rd_btn_y_pos)#. place(x = 50, y = 25)
        
    other_radio_btn = createRadioButton(form_frm,"Other", "O", Gender,Func_radio_btn, 25+130 + 130, rd_btn_y_pos)
    global cal
    
    def DOB_open_date_picker():
        
        top = CTkToplevel(form_frm)
        top.title("Select a Date")
        top.attributes("-topmost", True)
        global cal
        cal = Calendar(top, selectmode='day', date_pattern = "yyyy-mm-dd")
        cal.pack(pady=10)
        def select_date():
            global DOB_selected_date
            DOB_selected_date = cal.get_date()
            DOB_Date_label.configure(text=f"Selected Date : {DOB_selected_date}")
            top.destroy()
            
        select_button = CTkButton(top, text="Select Date", command=select_date)
        select_button.pack(pady=10)

    DOB_Date_Btn = CTkButton(form_frm, text="Date Of Birth", command=DOB_open_date_picker, corner_radius=100)
    DOB_Date_Btn.place(x=25, y =rd_btn_y_pos+40)

    DOB_Date_label = CTkLabel(form_frm, text= "Select Date")
    DOB_Date_label.place(x = 25+170, y = 90+40)
    
    U_name_Entry = CTkEntry(form_frm, width = 350, placeholder_text="Username")
    U_name_Entry.place(x = 25, y = 130+40)
    
    
    gmail_Entry = CTkEntry(form_frm, width = 350, placeholder_text="Gmail")
    gmail_Entry.place(x = 25, y = 170+40)
    
    
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
    pass_Entry.place(x = 25, y = 170+80)
    
    re_pass_Entry = CTkEntry(form_frm, width = 350, placeholder_text="Re-Password", show = "*")
    re_show_btn = CTkButton(re_pass_Entry, width = 22, height=28, text="Show",border_color="#565b5e",border_width=2, fg_color="transparent", command=Re_Show_pass)
    re_show_btn.place(x = 304, y=0)
    re_pass_Entry.place(x = 25, y = 210+80)
    
    phonnumber_Entry = CTkEntry(form_frm, 350, placeholder_text="Phone Number")
    phonnumber_Entry.place(x = 25, y =250+80)
    
    Create_acc_btn = CTkButton(form_frm, width = 350, text="Create Account", corner_radius=100, command = NullCheck)
    Create_acc_btn.place(x = 25, y = 290+80)
    
    tempxpos = 100
    tempypos = 410
    Dnt_hv_acc_lbl = CTkLabel(form_frm, text="Already have an account ? ")
    Dnt_hv_acc_lbl.place(x = tempxpos, y = tempypos)
    Sign_up_lbl = CTkLabel(form_frm, text="Sign In", font = ("Arial" , 12, "italic", "underline"))
    Sign_up_lbl.place(x = tempxpos + 150, y = tempypos)
#=>3------Sign In Page --------------------------------------
global PG_Sign_in
def PG_Sign_in():
    root.title ("http:www.HADAirlineManagementSystem.com/Sign_In")
    for i in Main_fame.winfo_children():
        i.destroy()
    
    form_frm_width = 400
    form_frm_height = 340
    form_frm = CTkFrame(Main_fame, width=form_frm_width, height=form_frm_height)
    form_frm.place(x = (m_r_width/(2))-(form_frm_width/2),
                                  y = (m_r_height/(2)-(form_frm_height/2))
                                  )
    
    def go_back():
        global _isSignedIn
        if _isSignedIn == True :
            for i in Main_fame.winfo_children():
                i.destroy()
            #fligt_search_result_frm.destroy()
            Main_frm_Authentication_Btns()
            PG_search_flight_()
        else : 
            for i in Main_fame.winfo_children():
                i.destroy()
            #fligt_search_result_frm.destroy()
            Main_frm_Authentication_Btns()
            PG_Get_Flight_Details()
            
    dummy_back_btn = CTkButton(Main_fame,text="Back", command = go_back)
    dummy_back_btn.place(x =10, y = 10)

    login_lb = CTkLabel(form_frm, text = "LOGIN")
    login_lb.place(x = 10, y = 10)
    
    def Login_authentication(_username, _pass):
        global _isSignedIn, User
        _username=  _username.get() #"vs_hari_dhejus"
        _pass = _pass.get() #"Charazard101"
        if (_username == "" or _pass == "" ) :
            errorLabeling(form_frm, "Feilds Cannot Be Empty", _x = 90, _y = 150)
        else:
            temp_qry = f"SELECT U_name, U_Gmail, U_password FROM user_details WHERE U_name = '{_username}' or U_Gmail = '{_username}' and U_password = '{_pass}'"
            cur.execute(temp_qry)
            qry_result = cur.fetchone()
            print(qry_result)
            
            if qry_result == None :
                errorLabeling(form_frm, "Username Or Password Is Incorrect", _x = 50, _y = 150)
                
            else: 
                User = qry_result[0]
                print(User)
                _isSignedIn = True
                if is_flight_details_obtained == True : 
                    PG_Payment()
                else:
                    PG_Get_Flight_Details()
    
    user_Entry = CTkEntry(form_frm, width = 350, placeholder_text= "Username/Gmail")
    user_Entry.place(x = 25, y = 40)
    
    def Show_pass():
        
        if pass_Entry.cget('show') == '*':
            pass_Entry.configure(show='')  # Show the password
            show_btn.configure(text=" Hide ")
        else:
            pass_Entry.configure(show='*')  # Hide the password
            show_btn.configure(text="Show")
            
    pass_Entry = CTkEntry(form_frm, width = 350, placeholder_text="Password", show = "*")
    show_btn = CTkButton(pass_Entry, width = 22, height=28, text="Show",border_color="#565b5e",border_width=2, fg_color="transparent", command=Show_pass)
    show_btn.place(x = 304, y=0)
    pass_Entry.place(x = 25, y = 80)
    
    Login_btn = CTkButton(form_frm, text= "LOGIN", width= 350, corner_radius=100, command=lambda :(Login_authentication(user_Entry, pass_Entry)))
    Login_btn.place(x = 25, y = 120)
    
    No_of_hyphen = 41
    line_lbl = CTkLabel(form_frm, text = f"{'-'*No_of_hyphen} OR {'-'*No_of_hyphen}")
    line_lbl.place(x = 25, y = 170)
    
    def loginWithGoogle():
        temp_TL = CTkToplevel(root)
        temp_TL.title("http:www.HADAirlineManagementSystem.com/Error?loginWithGoogle")
        temp_TL.attributes("-topmost", True)
        temp_TL.geometry("400x300")
        errorLabeling(temp_TL, _text="""
We are Extremly Sorry for the Inconvenience: 
We at HAD are currently working to 
bring in that feature.""",_textcolor = "#007acc", _cooldowntime = None)
    
    Login_btn2 = CTkButton(form_frm, text= "LOGIN with Google", width= 350, corner_radius=100, command=loginWithGoogle)
    Login_btn2.place(x = 25, y = 220)
    
    tempxpos = 100
    tempypos = 270
    Dnt_hv_acc_lbl = CTkLabel(form_frm, text="Don't have an account ? ")
    Dnt_hv_acc_lbl.place(x = tempxpos, y = tempypos)
    Sign_up_lbl = CTkLabel(form_frm, text="Sign Up", font = ("Arial" , 12, "italic", "underline"))
    Sign_up_lbl.place(x = tempxpos + 140, y = tempypos)
    
    
    Sign_up_lbl.bind("<Button-1>", lambda event, : PG_Sign_Up())
    Sign_up_lbl.bind("<Enter>", lambda event, lbl = Sign_up_lbl: lbl.configure(text_color = "#007acc"))
    Sign_up_lbl.bind("<Leave>", lambda event, lbl = Sign_up_lbl: lbl.configure(text_color = "Light Gray"))
# =>2------Show Flights details --------------------------------------
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

    PG_Heading = CTkLabel(fligt_search_result_frm, text = "AVAILABLE FLIGHTS")
    PG_Heading.pack(padx = 25, pady = 10, anchor = "w")
    def go_back():
        for i in Main_fame.winfo_children():
            i.destroy()
        Main_frm_Authentication_Btns()
        PG_Get_Flight_Details()
        
    dummy_back_btn = CTkButton(Main_fame,text="Back", command = go_back)
    dummy_back_btn.place(x =10, y = 10)
    
    btns = []
    
    global radio_val, dest_airport, origin_airport
    temp_qry = "SELECT F_Departure, F_Ariaval, F_Airline, F_price FROM flight WHERE F_Departure = '" + origin_airport+ "' AND F_Ariaval = '" + dest_airport+ "';"
    cur.execute(temp_qry)
    result = cur.fetchall()
    btn_data= {}
    key = 1
    for i in result :
        btn_data[key] = f"{i[0]} -----> {i[1]} : {i[2]} : {i[3]}"
        print(i)
        key += 1
    print(btn_data)    

    def on_btn_click(index):
        print(f"{index} clicked. ")
        if _isSignedIn == True:
            print("Signed In")
            PG_Payment()
            pass#----------------------------------------------------------------------------------------------------------------
        else :
            PG_Sign_in()
        
    for id, label in btn_data.items() :
        
        btn = CTkButton(fligt_search_result_frm, text = label,bg_color="transparent", command = lambda id=id: on_btn_click(id)).pack(pady = 10, padx = 10, anchor = "w")
        btns.append(btn)
# =>1-----Get Flight details---------------------------------------------------------------------   
def PG_Get_Flight_Details():
    global div_frame, _isSignedIn, User    
    for i in Main_fame.winfo_children():
        i.destroy()
        
    prev_page = 1
    print(prev_page)
    temp_frm_width = 500
    temp_frm_height = 320
    div_frame = CTkFrame(Main_fame,width=temp_frm_width, height = temp_frm_height)
    div_frm_xpos = 75
    din_frm_widget_width = 350
    div_frame.place(x = (m_r_width/(2))-(temp_frm_width/2),
                                  y = (m_r_height/(2)-(temp_frm_height/2)))

    def Func_radio_btn():
        global radio_val
        radio_val = book_a_fligt_radio_val.get()
        if radio_val == "ReturnRadio":
            Dest_Date_Btn.configure(state = tk.NORMAL)
        else:
            Dest_Date_Btn.configure(state = tk.DISABLED)
        print(radio_val)

    global book_a_fligt_radio_val
    book_a_fligt_radio_val = StringVar(value = "other")
    rd_btn_y_pos = 20
    return_radio_btn = createRadioButton(div_frame,"Return","ReturnRadio",book_a_fligt_radio_val,Func_radio_btn,div_frm_xpos, rd_btn_y_pos)#. place(x = 10, y = 25)
        
    one_way_radio_btn = createRadioButton(div_frame,"One Way", "OnewayRadio", book_a_fligt_radio_val,Func_radio_btn, div_frm_xpos+130, rd_btn_y_pos)#. place(x = 50, y = 25)
        
    #mulicity_radio_btn = createRadioButton(div_frame, "Multicity", "MulticityRadio", book_a_fligt_radio_val,Func_radio_btn, div_frm_xpos+270, rd_btn_y_pos)#. place(x = 90, y = 25)

    def Combo_get_origin_val(origin_combo_value):
        global origin_airport
        origin_airport = origin_combo_value
        print(origin_airport)
        
    departure_place = StringVar(value="dep_combo_other")
    departure_place.set("Departure")
    
    Origin_Airport = CTkComboBox(div_frame,width=din_frm_widget_width,
                                values= [
                                    "Boston",
                                    "Chennai",
                                    "Thiruvananthapuram"
                                    ],
                                    variable= departure_place, command = Combo_get_origin_val)
    Origin_Airport.place (x = div_frm_xpos, y = rd_btn_y_pos+50)

    def Combo_get_dest_val(dest_combo_value):
        global dest_airport
        dest_airport = dest_combo_value
        print(dest_airport)

    global arrival_place 
    arrival_place = StringVar(value="des_combo_other")
    arrival_place.set("Destination")
    Dest_Airport = CTkComboBox(div_frame,width=din_frm_widget_width, 
                            values=[
                                    "Boston",
                                    "Chennai",
                                    "Thiruvananthapuram"
                                ],
                            variable= arrival_place, command= Combo_get_dest_val)
    Dest_Airport.place (x = div_frm_xpos, y = rd_btn_y_pos+82)

    arrival_place = arrival_place.get()

    passenger_Class = CTkComboBox(div_frame,width=din_frm_widget_width, values=["Passenger/Class"])
    passenger_Class.place (x = div_frm_xpos, y = rd_btn_y_pos+114)

    def Dept_open_date_picker():
        
        top = CTkToplevel(root)
        top.title("Select a Date")
        top.attributes("-topmost", True)
        cal = Calendar(top, selectmode='day', date_pattern = "yyyy-mm-dd")
        cal.pack(pady=10)
        def select_date():
            global Dept_selected_date
            Dept_selected_date = cal.get_date()
            Dept_date_label.configure(text=f"Selected Date : {Dept_selected_date}")
            top.destroy()
            
        select_button = CTkButton(top, text="Select Date", command=select_date)
        select_button.pack(pady=10)

    Dept_Date_Btn = CTkButton(div_frame, text="Departure Date", command=Dept_open_date_picker, corner_radius=100)
    Dept_Date_Btn.place(x=div_frm_xpos, y =rd_btn_y_pos+154)

    Dept_date_label = CTkLabel(div_frame, text= "Select Date")
    Dept_date_label.place(x = div_frm_xpos+170, y = rd_btn_y_pos+154)
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def Dest_open_date_picker():
        
        top = CTkToplevel(root)
        top.title("Select a Date")
        top.attributes("-topmost", True)
        cal = Calendar(top, selectmode='day', date_pattern = "yyyy-mm-dd")
        cal.pack(pady=10)
        def select_date():
            global Dest_selected_date
            Dest_selected_date = cal.get_date()
            Dest_date_label.configure(text=f"Selected Date : {Dest_selected_date}")
            top.destroy()
            
        select_button = CTkButton(top, text="Select Date", command=select_date)
        select_button.pack(pady=10)

    
    Dest_Date_Btn = CTkButton(div_frame, text="Arrival Date", command=Dest_open_date_picker, corner_radius=100, state=tk.DISABLED)
    Dest_Date_Btn.place(x=div_frm_xpos, y =rd_btn_y_pos+190)

    Dest_date_label = CTkLabel(div_frame, text= "Select Date")
    Dest_date_label.place(x = div_frm_xpos+170, y = rd_btn_y_pos+190)
    
    def Null_Check():
        error_name = ""
        try :
            global radio_val, dest_airport, origin_airport
            print(radio_val)
            #___--------------______________________---------------------------------------
            origin_airport = "CHENNAI"
            dest_airport = "Thiruvananthapuram"
            Dept_selected_date = "2024-11-22"
            radio_val = "OnewayRadio"
            print(dest_airport)
            print(origin_airport)
            print(Dept_selected_date)
            if radio_val == "ReturnRadio" :
                print(Dest_selected_date)
            
            if dest_airport not in globals() or origin_airport not in globals() or radio_val not in globals():
                pass
            
        except NameError :
            error_name = "NameError"
            error_label = CTkLabel(div_frame, text = "Feilds Cannot Be Empty", font = ("Bradley Hand ITC" , 18, "italic", "bold"), text_color = "red")
            error_label.place(x = 140, y = 280)
            def refresh():
                error_label.destroy()
            error_label.after(3000, refresh)
            
        finally:
            if error_name != "NameError":
                global is_flight_details_obtained
                is_flight_details_obtained = True
                PG_search_flight_()
                
    Search_Fligths_btn = CTkButton(div_frame, text = "Search Fligths", width = din_frm_widget_width, corner_radius=75, command=lambda :(Null_Check()))
    Search_Fligths_btn.place(x = div_frm_xpos, y =245)
    Main_frm_Authentication_Btns()
# =>-----MAIN FRAME---------------------------------------------------------------------
global Main_frm_Authentication_Btns
def Main_frm_Authentication_Btns():
    if _isSignedIn == True:
        errorLabeling(Main_fame, f"{User}", _textcolor = "#007acc", _x = m_r_width-200, _y= 10,_cooldowntime = None)
    else:
        temp_xpos = m_r_width-300
        Sign_in_btn = CTkButton(Main_fame, text = "Sign In", command= PG_Sign_in)
        Sign_in_btn.place(x = temp_xpos, y = 10)

        Sign_up_btn = CTkButton(Main_fame, text = "Sign Up", fg_color="transparent", border_color= "grey", border_width=2, command=PG_Sign_Up)
        Sign_up_btn.place(x = temp_xpos+150, y = 10)

Main_frm_Authentication_Btns()
# PG_Payment()
PG_Get_Flight_Details()

#----------------------------------------------------------------------------------

#root.resizable(True,True)
root.mainloop()
cur.close()
con.commit()
