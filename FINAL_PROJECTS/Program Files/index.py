import subprocess
import smtplib
import os
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

required_packages = ["customtkinter", 
                     "matplotlib", 
                     "pillow",
                     "pymysql",
                     "colorama",
                     "tkcalendar"
                    ]

for package in required_packages:
    try:
        __import__(package)
        print(f"{package} Succesfully installed.")
    except ImportError:
        install(package)

# Created Modules 
import Ticket_Code_Gen as TCG
from Usable_screen import ScreenGeometry as SG
from flights import major_airports
import Global_Config as GC
from Crypter import crypt

# Global Modules

from customtkinter import *
import pymysql
from tkcalendar import Calendar
import tkinter as tk 
from pathlib import Path
from tkcalendar import Calendar
from datetime import datetime
from tkinter import filedialog

m_r_width, m_r_height = SG().GetUsableScreenSize()[0], SG().GetUsableScreenSize()[1]

root = CTk()
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
                    )

cur = con.cursor()
#---------GLOBAL VARIABLES --------
_isSignedIn = True 
is_flight_details_obtained = False
User = "vs_hari_dhejus" #vs_hari_dhejus
isAdmin = True ###########
prev_page = 0
glb_clr_1 = "blue"
glb_clr_2 = "green"
BASE_DIR = Path(__file__).resolve().parent.parent
glb_clr_3 = "yellow"
destroy_after = None

global  PG_Get_Flight_Details

def DB_INIT_():
    try :
        cur.execute("CREATE DATABASE IF NOT EXISTS `airwaysms2_0` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;")
              
        cur.execute("""CREATE TABLE IF NOT EXISTS `user_details` (
                        `UID` int NOT NULL AUTO_INCREMENT,
                        `UF_name` varchar(100) DEFAULT NULL,
                        `UL_name` varchar(100) DEFAULT NULL,
                        `U_name` varchar(100) NOT NULL,
                        `U_Gmail` varchar(100) NOT NULL,
                        `U_phno` varchar(12) DEFAULT NULL,
                        `U_password` varchar(100) NOT NULL,
                        `U_dob` date DEFAULT NULL,
                        `U_AGE` int DEFAULT NULL,
                        `U_gender` varchar(5) DEFAULT NULL,
                        `U_isActive` tinyint DEFAULT '1',
                        PRIMARY KEY (`UID`),
                        UNIQUE KEY `U_name_UNIQUE` (`U_name`)
                        ) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;""")
        
        cur.execute("""CREATE TABLE `flights` (
                        `F_ID` int NOT NULL AUTO_INCREMENT,
                        `F_Departure` varchar(100) DEFAULT NULL,
                        `F_Arrival` varchar(100) DEFAULT NULL,
                        `F_Airline` varchar(45) NOT NULL,
                        `F_price` int DEFAULT NULL,
                        PRIMARY KEY (`F_ID`)
                        ) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
                    """)
        
        cur.execute("""CREATE TABLE IF NOT EXISTS `booking` (
                        `BID` varchar(100) NOT NULL,
                        `BU_NAME` varchar(100) DEFAULT NULL,
                        `B_FLIGHT` int DEFAULT NULL,
                        `IS_ACTIVE` int DEFAULT NULL,
                        PRIMARY KEY (`BID`),
                        KEY `B_FORIEGN_KEY_idx` (`B_FLIGHT`),
                        CONSTRAINT `B_FORIEGN_KEY` FOREIGN KEY (`B_FLIGHT`) REFERENCES `flights` (`F_ID`)
                        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;""")
        
        cur.execute("""CREATE TABLE `payment` (
                        `PID` int NOT NULL AUTO_INCREMENT,
                        `P_UID` int DEFAULT NULL,
                        `AMOUNT` int DEFAULT NULL,
                        `P_STATUS` int DEFAULT NULL,
                        `P_ACC_NUM` int DEFAULT NULL,
                        `P_UPI_NUM` int DEFAULT NULL,
                        `P_METHOD` varchar(45) DEFAULT NULL,
                        PRIMARY KEY (`PID`),
                        KEY `P_UID_idx` (`P_UID`),
                        CONSTRAINT `P_UID` FOREIGN KEY (`P_UID`) REFERENCES `user_details` (`UID`)
                        ) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
                        """)
        
    except Exception as e:
        pass
        
    finally :
        print("Sucessfully Initialized Database.")
        cur.execute("USE airwaysms2_0 ;")
DB_INIT_()
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

global booking
def booking ():
    Ticket_Code = TCG.Gen_Code()
    cur.execute("SELECT * FROM flights WHERE F_ID ='%s'", Flight_ID)
    cur.execute("SELECT COUNT(*) FROM booking")
    F_id = cur.fetchone()[0] 
    global User
    cur.execute("INSERT INTO booking (BID, BU_NAME, B_FLIGHT) VALUES (%s, %s, %s)", (Ticket_Code, User, Flight_ID))
    con.commit()
    file_path = filedialog.asksaveasfilename(defaultextension = ".txt", 
                                             filetypes=[("Text Files", "*.txt"),
                                              ("All Files", "*.*")
                                              ],
                                             initialfile= "SELECT WHERE TO SAVE THE TICKET.txt")
    temp_qry = f"SELECT F_Departure, F_Arrival, F_Airline, F_price FROM flights WHERE flights.F_ID = %s ;"
    cur.execute(temp_qry, (Flight_ID,))
    result = cur.fetchone()
    if file_path:
        with open(file_path, "w")as f:
            f.write(f"Ticket Id : {Ticket_Code}, User : {User}, Departure : {result[0]}, Arrival : {result[1]}\
Airline : {result[2]}, Price : {result[3]}")
            
    errorLabeling(form_frm, "Sucessfully Booked", _textcolor = "green", _x = 120, _y = 170)
    
global PG_Payment
def PG_Payment():
    root.title ("http:www.HADAirlineManagementSystem.com/Payment")
    for i in Main_fame.winfo_children():
        i.destroy()
    
    form_frm_width = 400
    form_frm_height = 210
    global form_frm
    form_frm = CTkFrame(Main_fame, width=form_frm_width, height=form_frm_height)
    form_frm.place(x = (m_r_width/(2))-(form_frm_width/2), y = (m_r_height/(2)-(form_frm_height/2)))
    
    def go_back():
        PG_search_flight_()
            
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
    
        def go_back():
            PG_Payment()
                
        dummy_back_btn = CTkButton(Main_fame, text="Back", command = go_back)
        dummy_back_btn.place(x =10, y = 10)
        Temp_Entry_Width = 350
    
        UPI_Method_label = CTkLabel(form_frm, text= "UPI -")
        UPI_Method_label.place(x = 25, y = 10)
        
        UPI_Number_Entry = CTkEntry(form_frm, placeholder_text= "UPI Number",width= Temp_Entry_Width)
        UPI_Number_Entry.place(x =25, y = 50)
        
        cur.execute(f"SELECT F_Price FROM flights WHERE F_ID = '{Flight_ID}'")
        Amount = str(cur.fetchone()[0])
        
        Amount_LBL = CTkLabel(form_frm,text= f"Amount : {Amount}",width= Temp_Entry_Width)
        Amount_LBL.place(x =25, y = 90)
        
        def _on_UPI_pay_btn_click():
            UPI_Number = UPI_Number_Entry.get()
            cur.execute(f"SELECT F_Price FROM flights WHERE F_ID = '{Flight_ID}'")
            Amount = str(cur.fetchone()[0])
            
            if UPI_Number == "" or Amount == "":
                errorLabeling(form_frm, "Feilds Can Not Be Empty", _x = 90, _y = 170)
            
            elif UPI_Number.isdigit() == False or Amount.isdigit() == False:
                is_flight_details_obtained
            else:
                Amount = int(Amount)
                UPI_Number = int(UPI_Number)
                tempqry = "SELECT COUNT(*) FROM payment"
                cur.execute(tempqry)
                p_id = int(cur.fetchone()[0])+1
                global User
                tempqry = f"SELECT UID FROM user_details WHERE U_name = '{User}'"
                cur.execute(tempqry)
                Uid = int(cur.fetchone()[0])
                tempqry = "INSERT INTO payment (PID, AMOUNT, P_STATUS, P_UPI_NUM, P_METHOD) VALUES (%s, %s, %s, %s, %s)"
                cur.execute(tempqry, (p_id,Amount,400,UPI_Number, "UPI"))
                errorLabeling(form_frm, "Payment Sucessful", _textcolor = "green", _x = 110, _y = 170)
                def delayed_lbl():
                    errorLabeling(form_frm, "Booking Ticket ...", _textcolor = "green", _x = 1100, _y = 170)
                    def delayed():
                        booking()
                        PG_Get_Flight_Details()
                    root.after(3000, delayed)
                con.commit()
                root.after(3000, delayed_lbl)
                
        Pay_btn = CTkButton(form_frm, width= Temp_Entry_Width, text = "Pay", corner_radius= 100, command= _on_UPI_pay_btn_click)
        Pay_btn.place(x = 25, y = 130)
        
    UPI_btn = CTkButton(Centre_btn_frame, text = "UPI", command= on_UPI_btn_click)
    UPI_btn.place(x = 0, y = 0)
    
    def on_NET_btn_click():
        root.title ("http:www.HADAirlineManagementSystem.com/Payment/UPI")
        for i in form_frm.winfo_children():
            i.destroy()
    
        def go_back():
            PG_Payment()
                
        dummy_back_btn = CTkButton(Main_fame, text="Back", command = go_back)
        dummy_back_btn.place(x =10, y = 10)
        
        Temp_Entry_Width = 350
    
        NETB_Method_label = CTkLabel(form_frm, text= "NET BANKING -")
        NETB_Method_label.place(x = 25, y = 10)
        
        NETB_Number_Entry = CTkEntry(form_frm, placeholder_text= "Account Number",width= Temp_Entry_Width)
        NETB_Number_Entry.place(x =25, y = 50)
        
        cur.execute(f"SELECT F_Price FROM flights WHERE F_ID = '{Flight_ID}'")
        Amount = str(cur.fetchone()[0])
        
        Amount_LBL = CTkLabel(form_frm,text= f"Amount : {Amount}",width= Temp_Entry_Width)
        Amount_LBL.place(x =25, y = 90)
        
        def _on_NETB_pay_btn_click():
            ACC_Number = NETB_Number_Entry.get()
            cur.execute(f"SELECT F_Price FROM flights WHERE F_ID = '{Flight_ID}'")
            Amount = str(cur.fetchone()[0]) 
            
            if ACC_Number == "" or Amount == "":
                errorLabeling(form_frm, "Feilds Can Not Be Empty", _x = 90, _y = 170)
            
            elif ACC_Number.isdigit() == False or Amount.isdigit() == False:
                is_flight_details_obtained
            else:
                Amount = int(Amount)
                ACC_Number = int(ACC_Number)
                tempqry = "SELECT COUNT(*) FROM payment"
                cur.execute(tempqry)
                p_id = int(cur.fetchone()[0])+1
                global User
                tempqry = f"SELECT UID FROM user_details WHERE U_name = '{User}'"
                cur.execute(tempqry)
                Uid = int(cur.fetchone()[0])
                tempqry = "INSERT INTO payment (PID, AMOUNT, P_STATUS, P_UPI_NUM, P_METHOD) VALUES (%s, %s, %s, %s, %s)"
                cur.execute(tempqry, (p_id,Amount,400,ACC_Number, "NET"))
                con.commit()
                errorLabeling(form_frm, "Payment Sucessful", _textcolor = "green", _x = 110, _y = 170)
                def delayed_lbl():
                    errorLabeling(form_frm, "Booking Ticket ...", _textcolor = "green", _x = 1100, _y = 170)
                    def delayed():
                        booking()
                        PG_Get_Flight_Details()
                    root.after(3000, delayed)
                con.commit()
                root.after(3000, delayed_lbl)
                
        Pay_btn = CTkButton(form_frm, width= Temp_Entry_Width, text = "Pay", corner_radius= 100, command= _on_NETB_pay_btn_click)
        Pay_btn.place(x = 25, y = 130)
        
    NetBanking_btn = CTkButton(Centre_btn_frame, text = "Net Banking", command= on_NET_btn_click)
    NetBanking_btn.place(x = 150, y = 0)
    Main_frm_Authentication_Btns()
    
#=> --------Sign Up --------------------
global PG_Sign_Up
def PG_Sign_Up() :
    root.title ("http:www.HADAirlineManagementSystem.com/SignUp")
    for i in Main_fame.winfo_children():
        i.destroy()
    
    form_frm_width = 400
    form_frm_height = 600
    form_frm = CTkFrame(Main_fame, width=form_frm_width, height=form_frm_height)
    form_frm.place(x = (m_r_width/(2))-(form_frm_width/2),
                                  y = (m_r_height/(2)-(form_frm_height/2))
                                  )
    
    def go_back():
        for i in Main_fame.winfo_children():
            i.destroy()
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
        _pass = crypt(pass_Entry.get()).encrypt()
        _re_pass = crypt(re_pass_Entry.get()).encrypt()
        phonenumber = phonnumber_Entry.get()
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
            ans = cur.fetchone() 

            new_uid = ans[0] + 1
            
            tmp_qry = """
                INSERT INTO user_details (UID, UF_name, UL_name, U_name, U_Gmail, U_phno, U_password, U_dob, U_gender, U_AGE)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(tmp_qry, (new_uid, F_name, L_name, U_name, Gmail, phonenumber, _pass, dob, _Gender, Age))
            con.commit()

            cur.execute("SELECT Count(*) FROM user_details")
            ans2 = cur.fetchone()

            con.commit()
            if ans2 > ans :
                errorLabeling(form_frm, "Succesfully Added", _textcolor = "green", _x = 110, _y = 410)
                def _fun():
                    global _isSignedIn, User
                    _isSignedIn = True
                    User = U_name
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
    global Gender
    Gender = StringVar(value = "other")
    
    rd_btn_y_pos = 90
    
    male_radio_btn = createRadioButton(form_frm, "Male","M",Gender,Func_radio_btn,25, rd_btn_y_pos)
        
    female_radio_btn = createRadioButton(form_frm,"Female", "F", Gender,Func_radio_btn, 25+130, rd_btn_y_pos)
        
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
            pass_Entry.configure(show='')
            show_btn.configure(text=" Hide ")
        else:
            pass_Entry.configure(show='*') 
            show_btn.configure(text="Show")
            
    def Re_Show_pass():
        if re_pass_Entry.cget('show') == '*':
            re_pass_Entry.configure(show='') 
            re_show_btn.configure(text=" Hide ")
        else:
            re_pass_Entry.configure(show='*') 
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
            Main_frm_Authentication_Btns()
            PG_search_flight_()
        else : 
            for i in Main_fame.winfo_children():
                i.destroy()
            Main_frm_Authentication_Btns()
            PG_Get_Flight_Details()
            
    dummy_back_btn = CTkButton(Main_fame,text="Back", command = go_back)
    dummy_back_btn.place(x =10, y = 10)

    login_lb = CTkLabel(form_frm, text = "LOGIN")
    login_lb.place(x = 10, y = 10)
    
    def Login_authentication(_username, _pass):
        global _isSignedIn, User
        _isSignedIn = True
        _username=  _username.get()
        _pass = crypt(_pass.get()).encrypt()
        if (_username == "" or _pass == "" ) :
            errorLabeling(form_frm, "Feilds Cannot Be Empty", _x = 90, _y = 150)
        else:
            temp_qry = f"SELECT U_name, U_Gmail, U_password, U_isAdmin FROM user_details WHERE U_name = '{_username}' or U_Gmail = '{_username}' and U_password = '{_pass}'"
            cur.execute(temp_qry)
            qry_result = cur.fetchone()
            
            if qry_result == None :
                errorLabeling(form_frm, "Username Or Password Is Incorrect", _x = 50, _y = 150)
                
            else: 
                global User, isAdmin
                User = qry_result[0]
                _isSignedIn = True
                isAdmin = qry_result[-1]
                if is_flight_details_obtained == True : 
                    PG_Payment()
                else:
                    PG_Get_Flight_Details()
    
    user_Entry = CTkEntry(form_frm, width = 350, placeholder_text= "Username/Gmail")
    user_Entry.place(x = 25, y = 40)
    
    def Show_pass():
        
        if pass_Entry.cget('show') == '*':
            pass_Entry.configure(show='') 
            show_btn.configure(text=" Hide ")
        else:
            pass_Entry.configure(show='*')
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
    temp_qry = "SELECT F_Departure, F_Arrival, F_Airline, F_price, F_ID FROM flights WHERE F_Departure = '" + origin_airport+ "' AND F_Arrival = '" + dest_airport+ "';"
    cur.execute(temp_qry)
    result = cur.fetchall()
    btn_data= {}
    FLIGHT_ID_dict = {}
    key = 1
    for i in result :
        btn_data[key] = f"{i[0]} -----> {i[1]} : {i[2]} : {i[3]}"
        FLIGHT_ID_dict[key] = i[4]
        key += 1

    def on_btn_click(index):
        global Flight_ID
        Flight_ID = FLIGHT_ID_dict[index]
        if _isSignedIn == True:
            PG_Payment()
        else :
            PG_Sign_in()
            pass
    for id, label in btn_data.items() :
        
        btn = CTkButton(fligt_search_result_frm, text = label,bg_color="transparent", command = lambda idx=id: on_btn_click(idx)).pack(pady = 10, padx = 10, anchor = "w")
        btns.append(btn)
    con.commit()
    Main_frm_Authentication_Btns()    
    
# =>1-----Get Flight details---------------------------------------------------------------------   
def PG_Get_Flight_Details():
    global div_frame, _isSignedIn, User    
    for i in Main_fame.winfo_children():
        i.destroy()
                
    prev_page = 1
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

    global book_a_fligt_radio_val
    book_a_fligt_radio_val = StringVar(value = "other")
    rd_btn_y_pos = 20
    return_radio_btn = createRadioButton(div_frame,"Return","ReturnRadio",book_a_fligt_radio_val,Func_radio_btn,div_frm_xpos, rd_btn_y_pos)
        
    one_way_radio_btn = createRadioButton(div_frame,"One Way", "OnewayRadio", book_a_fligt_radio_val,Func_radio_btn, div_frm_xpos+130, rd_btn_y_pos)
        
    

    def Combo_get_origin_val(origin_combo_value):
        global origin_airport
        origin_airport = origin_combo_value
        
    departure_place = StringVar(value="dep_combo_other")
    departure_place.set("Departure")
    
    Origin_Airport = CTkComboBox(div_frame,width=din_frm_widget_width,
                                values=major_airports,
                                    variable= departure_place, command = Combo_get_origin_val)
    Origin_Airport.place (x = div_frm_xpos, y = rd_btn_y_pos+50)

    def Combo_get_dest_val(dest_combo_value):
        global dest_airport
        dest_airport = dest_combo_value

    global arrival_place 
    arrival_place = StringVar(value="des_combo_other")
    arrival_place.set("Destination")
    Dest_Airport = CTkComboBox(div_frame,width=din_frm_widget_width, 
                            values=major_airports,variable= arrival_place, command= Combo_get_dest_val)
    
    Dest_Airport.place (x = div_frm_xpos, y = rd_btn_y_pos+82)

    arrival_place = arrival_place.get()

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
    Dept_Date_Btn.place(x=div_frm_xpos, y =rd_btn_y_pos+114)

    Dept_date_label = CTkLabel(div_frame, text= "Select Date")
    Dept_date_label.place(x = div_frm_xpos+170, y = rd_btn_y_pos+114)
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
    Dest_Date_Btn.place(x=div_frm_xpos, y =rd_btn_y_pos+147)

    Dest_date_label = CTkLabel(div_frame, text= "Select Date")
    Dest_date_label.place(x = div_frm_xpos+170, y = rd_btn_y_pos+147)
    
    def Null_Check():
        error_name = ""
        try :
            global radio_val, dest_airport, origin_airport
            radio_val
            dest_airport
            origin_airport
            Dept_selected_date
            if radio_val == "ReturnRadio" :
                Dest_selected_date
            
            if dest_airport not in globals() or origin_airport not in globals() or radio_val not in globals():
                pass
            
        except NameError :
            error_name = "NameError"
            error_label = CTkLabel(div_frame, text = "Feilds Cannot Be Empty", font = ("Bradley Hand ITC" , 18, "italic", "bold"), text_color = "red")
            error_label.place(x = 140, y = 238)
            def refresh():
                error_label.destroy()
            error_label.after(3000, refresh)
            
        finally:
            if error_name != "NameError":
                global is_flight_details_obtained
                is_flight_details_obtained = True
                PG_search_flight_()
                
    Search_Fligths_btn = CTkButton(div_frame, text = "Search Fligths", width = din_frm_widget_width, corner_radius=75, command=lambda :(Null_Check()))
    Search_Fligths_btn.place(x = div_frm_xpos, y =rd_btn_y_pos + 180)
    con.commit()
    Main_frm_Authentication_Btns()
    
# =>-----MAIN FRAME---------------------------------------------------------------------
global Main_frm_Authentication_Btns
def Main_frm_Authentication_Btns():
    if _isSignedIn == True:
        global User
        User_Label = CTkLabel(Main_fame, text = f"{User}", text_color= "#007acc", font= ("Bradley Hand ITC" , 18, "italic", "bold"), width = 20)
        User_Label.place(x = m_r_width-200, y= 10)
        User_Label.update_idletasks()
        lbl_width = User_Label.winfo_width()
        User_Label.place(x = (m_r_width/(1.2))-(lbl_width/2),y = 10)
           
        def on_select(option):
            global _isSignedIn, User , isAdmin   
            
            if option ==  "Cancel Flights":
                Setting_btn.set("Settings")
                tmp_root = CTkToplevel(root)
                tmp_root_width , tmp_root_height = 400, 300
                tmp_root.geometry(f"{tmp_root_width}x{tmp_root_height}")
                tmp_root.attributes("-topmost", True)
                
                temp_frame = CTkFrame(tmp_root, width= tmp_root_width, height = tmp_root_height, border_color= "#007acc", border_width= 2)
                temp_frame.pack()
                
                Flight_ID_entry = CTkEntry(temp_frame, placeholder_text= "Ticket ID",width= 350)              
                Flight_ID_entry.place(x = (tmp_root_width/(2))-(350/2),
                                  y = (tmp_root_height/(2)-(28/2))-38)
            
                def Cancel_tickets():
                    Flight_id = Flight_ID_entry.get()
                    
                    cur.execute("SELECT BID, BU_NAME FROM booking WHERE BID = %s AND IS_ACTIVE = 1", Flight_id)
                    row = cur.fetchone()
                    global User
                    if row and row[1] == User :
                        cur.execute("UPDATE booking SET IS_ACTIVE = 0 WHERE BID = %s AND IS_ACTIVE = 1", Flight_id)
                        lbl = CTkLabel(temp_frame, text ="Successfully Canceled", text_color="green", font = ("Bradley Hand ITC", 18, "italic", "bold")) #errorLabeling(temp_frame, "Successfully Canceled", _textcolor = "green", _x = 110, _y = (tmp_root_height/(2)-(28/2)+38) )                            
                        lbl.place(x = 110, y = (tmp_root_height/(2)-(28/2)+38))
                        def w8():
                            tmp_root.destroy()
                            con.commit()
                        lbl.after(3000,w8)
                    else:
                        errorLabeling(temp_frame, "Flight ID is Incorect", _x = 110, _y = (tmp_root_height/(2)-(28/2)+38))   
            
                Cancel_btn = CTkButton(temp_frame, text="Cancel Flight", width = 350 , corner_radius= 100, command= Cancel_tickets)
                Cancel_btn.place(x = (tmp_root_width/(2))-(350/2),
                                  y = (tmp_root_height/(2)-(28/2)))
            
            if option == "Booking History" :
                Setting_btn.set("Settings")
                tmp_root = CTkToplevel(root)
                tmp_root_width , tmp_root_height = 900, 300
                tmp_root.geometry(f"{tmp_root_width}x{tmp_root_height}")
                tmp_root.attributes("-topmost", True)
                tmp_root.resizable(False, False)
                
                temp_frame = CTkScrollableFrame(tmp_root, width= tmp_root_width, height = tmp_root_height, border_color= "#007acc", border_width= 2)
                temp_frame.pack()
                global User
                cur.execute("SELECT BU_NAME, BID, F_Departure, F_Arrival, F_Airline, F_price FROM  booking B, flights F WHERE B.BU_NAME = %s AND B.B_FLIGHT = F.F_ID AND B.IS_ACTIVE = 1", User)
                row = cur.fetchall()
                for i in row :
                    CTkLabel(temp_frame, text = i).pack(padx = 20, pady = 5, anchor = "w")
                    
            if option == "Edit Account" :
                Setting_btn.set("Settings")
                tmp_root = CTkToplevel(root)
                tmp_root_width , tmp_root_height = 400, 600
                tmp_root.geometry(f"{tmp_root_width}x{tmp_root_height}")
                tmp_root.attributes("-topmost", True)
                tmp_root.resizable(False, False)
                
                form_frm_width = 400
                form_frm_height = 600
                form_frm = CTkFrame(tmp_root, width=form_frm_width, height=form_frm_height)
                form_frm.place(x = 0, y = 0)
                
                def go_back():
                    for i in Main_fame.winfo_children():
                        i.destroy()
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
                        global Age
                        Age = today.year - dob_dt.year
                        if (today.month, today.day) > (dob_dt.month, dob_dt.day):
                            Age +=1
                    else :
                        dob = ""
                    Gmail = gmail_Entry.get()
                    _pass = crypt(pass_Entry.get()).encrypt()
                    _re_pass = crypt(re_pass_Entry.get()).encrypt()
                    phonenumber = phonnumber_Entry.get()
                                        
                    if _pass != _re_pass:
                        errorLabeling(form_frm, "Passwords Don't Match", _x = 110, _y = 410)
                        
                    if F_name != "" :
                        cur.execute("UPDATE user_details set UF_name = %s", F_name)
                        
                    if L_name != "" :
                        cur.execute("UPDATE user_details set UL_name = %s", L_name)
                        
                    if U_name != "" :
                        cur.execute("UPDATE user_details set U_name = %s", U_name)
                        
                    if _Gender != "other"  :
                        cur.execute("UPDATE user_details set U_gender = %s", _Gender)
                        
                    if phonenumber != "" :
                        cur.execute("UPDATE user_details set U_phno = %s", phonenumber)
                        
                    if _pass != "" :
                        cur.execute("UPDATE user_details set U_password = %s", _pass)
                        
                    if Gmail != "" :
                        cur.execute("UPDATE user_details set U_Gmail = %s", Gmail)
                        
                    if dob != "" :
                        cur.execute("UPDATE user_details set U_dob = %s", dob)
                        cur.execute("UPDATE user_details set U_AGE = %s", Age)
                        
                    if F_name == "" and L_name == "" and U_name == "" and dob == "" and  Gmail == "" and _pass == "" and _re_pass == "" and phonenumber == "" and _Gender == "other" :
                        errorLabeling(form_frm, "Feilds Cannot Be Null", _x = 110, _y = 410)

                    else :
                        lbl = CTkLabel(form_frm, text= "Succesfully Updated", text_color= "green", font=("Bradley Hand ITC" , 18, "italic", "bold"))
                        lbl.place(x = 110, y = 410)
                        # errorLabeling(form_frm, "Succesfully Updated", _textcolor = "green", _x = 110, _y = 410)
                        def w8():
                            tmp_root.destroy()
                        lbl.after(3000, w8)
                    con.commit() 
                    
                cur.execute("SELECT UF_name, UL_name, U_name, U_Gmail, U_phno, U_password, U_dob, U_gender, U_AGE FROM user_details WHERE U_name = %s", User)
                result = cur.fetchone()
                
                F_name_Entry = CTkEntry(form_frm, width = 350, placeholder_text=result[0])
                F_name_Entry.place(x = 25, y = 10)
                
                L_name_Entry = CTkEntry(form_frm, width = 350, placeholder_text=result[1])
                L_name_Entry.place(x = 25, y = 50)
                
                def Func_radio_btn():
                    global _Gender
                    _Gender = Gender.get()
                    
                global Gender
                Gender = StringVar(value = "other")
                
                rd_btn_y_pos = 90
                
                male_radio_btn = createRadioButton(form_frm, "Male","M",Gender,Func_radio_btn,25, rd_btn_y_pos)
                    
                female_radio_btn = createRadioButton(form_frm,"Female", "F", Gender,Func_radio_btn, 25+130, rd_btn_y_pos)
                    
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
                
                U_name_Entry = CTkEntry(form_frm, width = 350, placeholder_text=result[2])
                U_name_Entry.place(x = 25, y = 130+40)
                
                
                gmail_Entry = CTkEntry(form_frm, width = 350, placeholder_text=result[3])
                gmail_Entry.place(x = 25, y = 170+40)
                
                
                def Show_pass():
                    if pass_Entry.cget('show') == '*':
                        pass_Entry.configure(show='')
                        show_btn.configure(text=" Hide ")
                    else:
                        pass_Entry.configure(show='*') 
                        show_btn.configure(text="Show")
                        
                def Re_Show_pass():
                    if re_pass_Entry.cget('show') == '*':
                        re_pass_Entry.configure(show='')
                        re_show_btn.configure(text=" Hide ")
                    else:
                        re_pass_Entry.configure(show='*')  
                        re_show_btn.configure(text="Show")
                
                pass_Entry = CTkEntry(form_frm, width = 350, placeholder_text="Password", show = "*")
                show_btn = CTkButton(pass_Entry, width = 22, height=28, text="Show",border_color="#565b5e",border_width=2, fg_color="transparent", command=Show_pass)
                show_btn.place(x = 304, y=0)
                pass_Entry.place(x = 25, y = 170+80)
                
                re_pass_Entry = CTkEntry(form_frm, width = 350, placeholder_text="Re-Password", show = "*")
                re_show_btn = CTkButton(re_pass_Entry, width = 22, height=28, text="Show",border_color="#565b5e",border_width=2, fg_color="transparent", command=Re_Show_pass)
                re_show_btn.place(x = 304, y=0)
                re_pass_Entry.place(x = 25, y = 210+80)
                
                phonnumber_Entry = CTkEntry(form_frm, 350, placeholder_text=result[4])
                phonnumber_Entry.place(x = 25, y =250+80)
                
                Create_acc_btn = CTkButton(form_frm, width = 350, text="Alter Account", corner_radius=100, command = NullCheck)
                Create_acc_btn.place(x = 25, y = 290+80)
                
                temp_frame2 = CTkFrame(form_frm, width = 100, height= 200, border_color= "light Grey", border_width= 2,fg_color= "transparent")
                lbl = CTkLabel(temp_frame2, text="Enter The Feilds That You Want to Change",fg_color= "transparent")
                lbl.pack()
                def onhover(event):
                    temp_frame2.place(x = 25, y =410+40)
                
                info_Btn = CTkButton(form_frm, text = "i", width= 10, height = 5, corner_radius= 100, hover= "on_hover")
                info_Btn.place(x = 25, y = 370+40)
                info_Btn.bind("<Enter>", onhover)
                info_Btn.bind("<Leave>", lambda event : temp_frame2.place_forget())
                
            if  option == "Logout":
                _isSignedIn = False
                User =  ""
                isAdmin = False
                PG_Get_Flight_Details()
                
            if  option == "Adiministrate":
                temp_TL = CTkToplevel(root)
                temp_TL.title("http:www.HADAirlineManagementSystem.com/Admin")
                temp_TL.attributes("-topmost", True)
                temp_TL.geometry("400x300")
                
                def addAdmin():
                    temp_TL.destroy()
                    temp_TL2 = CTkToplevel(root)
                    temp_TL2.title("http:www.HADAirlineManagementSystem.com/Admin")
                    temp_TL2.attributes("-topmost", True)
                    temp_TL2.geometry("400x300")
                    
                    def add():
                        user = user_Entry.get()
                        cur.execute("UPDATE user_details SET U_isAdmin = 1 WHERE U_name = %s", user)
                        con.commit()
                        if cur.execute("SELECT U_isAdmin from user_details WHERE U_name = %s", user)==1:
                            label = CTkLabel(temp_TL2, text= "Successfully Updated", font= ("Bradley Hand ITC" , 18, "italic", "bold"), text_color= "green")
                            label.place(x = 110, y = 178)
                            def dest():
                                label.destroy()
                                temp_TL2.destroy()
                            label.after(3000, dest)
                        else:
                            label = CTkLabel(temp_TL2, text= "Username Not Found Or Server Down ", font= ("Bradley Hand ITC" , 18, "italic", "bold"), text_color= "red")
                            label.place(x = 45, y = 178)
                            def dest():
                                label.destroy()
                            label.after(3000, dest)
                        
                             
                    
                    user_Entry = CTkEntry(temp_TL2, placeholder_text= "UserName To Change As Admin", width=240)                    
                    user_Entry.place(x = 80, y = 100)
                    
                    user_Entry_btn = CTkButton(temp_TL2, text= " Change", command=add)                    
                    user_Entry_btn.place(x = 130, y = 138)
                
                def delAdmin():
                    temp_TL.destroy()
                    temp_TL2 = CTkToplevel(root)
                    temp_TL2.title("http:www.HADAirlineManagementSystem.com/Admin")
                    temp_TL2.attributes("-topmost", True)
                    temp_TL2.geometry("400x300")
                    
                    def _del():
                        user = user_Entry.get()
                        cur.execute("UPDATE user_details SET U_isActive = 0 WHERE U_name = %s", user)
                        con.commit()
                        if cur.execute("SELECT U_isActive from user_details WHERE U_name = %s", user)==0:
                            label = CTkLabel(temp_TL2, text= "Username Not Found Or Server Down ", font= ("Bradley Hand ITC" , 18, "italic", "bold"), text_color= "red")
                            label.place(x = 45, y = 178)
                            def dest():
                                label.destroy()
                            label.after(3000, dest)
                        
                        else:
                            label = CTkLabel(temp_TL2, text= "Successfully Deleted", font= ("Bradley Hand ITC" , 18, "italic", "bold"), text_color= "green")
                            label.place(x = 110, y = 178)
                            def dest():
                                label.destroy()
                                temp_TL2.destroy()
                            label.after(3000, dest)
                             
                    
                    user_Entry = CTkEntry(temp_TL2, placeholder_text= "UserName To Delete From Admin", width=240)                    
                    user_Entry.place(x = 80, y = 100)
                    
                    user_Entry_btn = CTkButton(temp_TL2, text= " Change", command=_del)                    
                    user_Entry_btn.place(x = 130, y = 138)
                
                def addFlights():
                    temp_TL.destroy()
                    temp_TL2 = CTkToplevel(root)
                    temp_TL2.title("http:www.HADAirlineManagementSystem.com/Admin")
                    temp_TL2.attributes("-topmost", True)
                    temp_TL2.geometry("400x300")
                    
                    def add():
                        dept = Dept_Entry.get()
                        arr = Arr_Entry.get()
                        Air = Air_Entry.get()
                        price = price_Entry.get()
                        cur.execute("SELECT COUNT(*) FROM flights")
                        tempCount = cur.fetchone()[0]
                        if dept ==""or arr ==""or Air ==""or price =="":
                            errorLabeling(temp_TL2, "Fields Cannot Be Empty", _x = 30, _y = 190+35)
                        elif not price.isdigit():
                           errorLabeling(temp_TL2, "Check The Price", _x = 30, _y = 190+35)
                        else:
                            cur.execute("INSERT INTO flights(F_Departure,F_Arrival,F_Airline, F_price ) VALUES (%s, %s,%s,%s)", (dept, arr, Air, int(price)))
                            con.commit()
                        cur.execute("SELECT COUNT(*) FROM flights")
                        check_Count = cur.fetchone()[0]
                        if check_Count ==tempCount+1:
                            label = CTkLabel(temp_TL2, text= "Successfully Added", font= ("Bradley Hand ITC" , 18, "italic", "bold"), text_color= "green")
                            label.place(x = 110, y = 190+35)
                            def dest():
                                label.destroy()
                                temp_TL2.destroy()
                            label.after(3000, dest)
                        
                        else:
                            label = CTkLabel(temp_TL2, text= " Error Occured While Inserting ", font= ("Bradley Hand ITC" , 18, "italic", "bold"), text_color= "red")
                            label.place(x = 45, y = 190+35)
                            def dest():
                                label.destroy()
                            label.after(3000, dest)
                             
                    tempy = 50
                    Dept_Entry = CTkEntry(temp_TL2, placeholder_text= "Depature Place", width=240)                    
                    Dept_Entry.place(x = 80, y = tempy)
                    
                    Arr_Entry = CTkEntry(temp_TL2, placeholder_text= "Arrival Place", width=240)                    
                    Arr_Entry.place(x = 80, y = tempy+35)
                    
                    Air_Entry = CTkEntry(temp_TL2, placeholder_text= "Airline Name", width=240)                    
                    Air_Entry.place(x = 80, y = tempy+35+35)
                    
                    price_Entry = CTkEntry(temp_TL2, placeholder_text= "Price", width=240)                    
                    price_Entry.place(x = 80, y = tempy+35+35+35)
                    
                    add_Flight_btn = CTkButton(temp_TL2, text="Add", command=add)
                    add_Flight_btn.place(x = 125, y = tempy+35+35+35+35)
                
                def delflights():
                    temp_TL.destroy()
                    temp_TL2 = CTkToplevel(root)
                    temp_TL2.title("http:www.HADAirlineManagementSystem.com/Admin")
                    temp_TL2.attributes("-topmost", True)
                    temp_TL2.geometry("760x300")
                    
                    def _del():
                        flightId = FlightIDEntry.get()
                        if flightId =="":
                            errorLabeling(temp_TL2, "Feild Empty", _x = 345, _y = 1)
                        elif flightId.isalpha():
                            errorLabeling(temp_TL2, "Invalid ID", _x = 346, _y = 1)
                        else:
                            cur.execute("SELECT F_ID FROM flights WHERE F_IsActive = 1")    
                            result = cur.fetchall()
                            if (int(flightId),) not in result:
                                errorLabeling(temp_TL2, "ID Not Found", _x = 344, _y = 1)
                            else:
                                cur.execute("UPDATE flights SET F_IsActive = 0 WHERE F_ID = %s", flightId)
                                #errorLabeling(temp_TL2, "Deleted", _x = 347, _y = 1)
                                con.commit()
                                label = CTkLabel(temp_TL2, text= "Successfully Deleted", font= ("Bradley Hand ITC" , 18, "italic", "bold"), text_color= "green")
                                label.place(x = 336, y = 1)
                                def dest():
                                    label.destroy()
                                    temp_TL2.destroy()
                                label.after(3000, dest)
                                
                                
                    tempx, tempy = 10, 30
                    FlightIDEntry = CTkEntry(temp_TL2, placeholder_text="Flight ID")
                    FlightIDEntry.place(x = tempx+240, y = tempy)
                    
                    mod_btn = CTkButton(temp_TL2, text="Modify", command=_del)
                    mod_btn.place(x = tempx+390, y = tempy)
                    
                    sckrlble_frame = CTkScrollableFrame(temp_TL2, width = 720, height=220)
                    sckrlble_frame.place(x = tempx, y = tempy+35)
                    cur.execute("SELECT * FROM Flights WHERE F_IsActive = 1")
                    result = cur.fetchall()
                    for i in result:
                        lbl = CTkLabel(sckrlble_frame, text=f"{i[0]}  {i[1]}  {i[2]}  {i[3]}  {i[4]}", text_color= "Light Gray")
                        lbl.pack(padx = 50,pady = 10, anchor = "w")
                       
                def ModFlights():
                    temp_TL.destroy()
                    temp_TL2 = CTkToplevel(root)
                    temp_TL2.title("http:www.HADAirlineManagementSystem.com/Admin")
                    temp_TL2.attributes("-topmost", True)
                    temp_TL2.geometry("760x300")
                    
                    def mod():
                        flightId = FlightIDEntry.get()
                        if flightId =="":
                            errorLabeling(temp_TL2, "Feild Empty", _x = 345, _y = 1)
                        elif flightId.isalpha():
                            errorLabeling(temp_TL2, "Invalid ID", _x = 346, _y = 1)
                        else:
                            cur.execute("SELECT F_ID FROM flights WHERE F_IsActive = 1")    
                            result = cur.fetchall()
                            if (int(flightId),) not in result:
                                errorLabeling(temp_TL2, "ID Not Found", _x = 344, _y = 1)
                            else:
                                temp_TL2.destroy()    
                                temp_TL3 = CTkToplevel(root)
                                temp_TL3.title("http:www.HADAirlineManagementSystem.com/Admin")
                                temp_TL3.attributes("-topmost", True)
                                temp_TL3.geometry("400x300")
                                
                                tempx, tempy = 10 , 30
                                cur.execute("SELECT * FROM flights WHERE F_ID = %s", flightId)
                                result = cur.fetchone()
                                
                                def Check():
                                    Dept = Dept_Entry.get()
                                    Arr = Arr_Entry.get()
                                    Air = Air_Entry.get()
                                    price = price_Entry.get()
                        
                                    if Dept != "":   
                                        cur.execute("UPDATE flights SET F_Departure = %s WHERE F_ID =%s", Dept) 
                        
                                    if Arr != "":   
                                        cur.execute("UPDATE flights SET F_Arrival = %s WHERE F_ID =%s", Arr) 
                        
                                    if Air != "":   
                                        cur.execute("UPDATE flights SET F_Airline = %s WHERE F_ID =%s", Air) 
                        
                                    if price != "":   
                                        cur.execute("UPDATE flights SET F_price = %s WHERE F_ID =%s", price) 
                                    
                                    con.commit()      
                                    label = CTkLabel(temp_TL3, text= "Successfully Updated", font= ("Bradley Hand ITC" , 18, "italic", "bold"), text_color= "green")
                                    label.place(x = 336, y = 1)
                                    def dest():
                                        label.destroy()
                                        temp_TL3.destroy()
                                    label.after(3000, dest)   
                                             
                                Dept_Entry = CTkEntry(temp_TL3, placeholder_text=result[1],width = 240)
                                Dept_Entry.pack(pady = 5)
                                Arr_Entry = CTkEntry(temp_TL3, placeholder_text=result[2],width = 240)
                                Arr_Entry.pack(pady = 5)
                                Air_Entry = CTkEntry(temp_TL3, placeholder_text=result[3],width = 240)
                                Air_Entry.pack(pady = 5)
                                price_Entry = CTkEntry(temp_TL3, placeholder_text=result[4],width = 240)
                                price_Entry.pack(pady = 5)
                                Upd_BTN = CTkButton(temp_TL3, text="Update",width = 240, command=Check)
                                Upd_BTN.pack(pady = 5)
                    
                    tempx, tempy = 10, 30
                    FlightIDEntry = CTkEntry(temp_TL2, placeholder_text="Flight ID")
                    FlightIDEntry.place(x = tempx+240, y = tempy)
                    
                    mod_btn = CTkButton(temp_TL2, text="Modify", command=mod)
                    mod_btn.place(x = tempx+390, y = tempy)
                    
                    sckrlble_frame = CTkScrollableFrame(temp_TL2, width = 720, height=220)
                    sckrlble_frame.place(x = tempx, y = tempy+35)
                    cur.execute("SELECT * FROM Flights WHERE F_IsActive = 1")
                    result = cur.fetchall()
                    for i in result:
                        lbl = CTkLabel(sckrlble_frame, text=f"{i[0]}  {i[1]}  {i[2]}  {i[3]}  {i[4]}", text_color= "Light Gray")
                        lbl.pack(padx = 50,pady = 10, anchor = "w")
                        
                tempx = 55
                tempy = 150
                Add_Admin_btn = CTkButton(temp_TL, text="Add Admin", command=addAdmin)
                Add_Admin_btn.place(x = tempx, y = tempy-30)
                
                Add_Flight_btn = CTkButton(temp_TL, text="Add Flights", command=addFlights)
                Add_Flight_btn.place(x = tempx+150, y = tempy-30)
                    
                Rem_Flight_btn = CTkButton(temp_TL, text="Delete Flights", command= delflights)
                Rem_Flight_btn.place(x = tempx+150, y = tempy+10)
                    
                Rem_Admin_btn = CTkButton(temp_TL, text="Delete Admin", command=delAdmin)
                Rem_Admin_btn.place(x = tempx, y = tempy+10)
                    
                Mod_Flight_btn = CTkButton(temp_TL, text="Modify Flights", command= ModFlights)
                Mod_Flight_btn.place(x = 130, y = tempy+50)
                
                
                    
  ######################## ADMINISTRATE    
        if isAdmin==1:           
            option = ["Cancel Flights", "Booking History", "Edit Account","Adiministrate", "Logout"]
        else:
            option = ["Cancel Flights", "Booking History", "Edit Account", "Logout"]
        Setting_btn = CTkOptionMenu(Main_fame,  values= option, command= on_select)
        Setting_btn.place(x = ((m_r_width/(1.2))-(lbl_width/2)) +lbl_width+ 10, y = 10)
        Setting_btn.set("Settings")
    else:
        temp_xpos = m_r_width-300
        Sign_in_btn = CTkButton(Main_fame, text = "Sign In", command= PG_Sign_in)
        Sign_in_btn.place(x = temp_xpos, y = 10)

        Sign_up_btn = CTkButton(Main_fame, text = "Sign Up", fg_color="transparent", border_color= "grey", border_width=2, command=PG_Sign_Up)
        Sign_up_btn.place(x = temp_xpos+150, y = 10)

Main_frm_Authentication_Btns()

PG_Get_Flight_Details()

#----------------------------------------------------------------------------------

root.mainloop()
cur.close()
con.commit()
