import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import time
from datetime import datetime, date
from random import randint
import streamlit as st
from writing_data import end_writing, intro_writing

example_values = st.checkbox("Example Values")
if example_values:
    filename = "newticket"
    ticket_number = "999"

    booking_num = "9999"
    date_number = "30.05.2023"
    booking_agent = "Booking guy"
    booking_phone = "080000000"
    booking_email = "bookingguy@travelagent"
    booking_logo = "images/logo.jpg"
    booking_address = "booking address"
    booking_company = "Company"
    booking_gds = "AAABBB"

    passenger_last = "Last name"
    passenger_first = "first name"
    passenger_title = "MR"
    passenger_full_name = passenger_last + ' / ' + passenger_first + ' ' + passenger_title

    passenger_ff = "ff number"
    passenger_country = "nationality"
    passenger_country_web = "govwebsite.gov"

    year = 2020
    month = 10
    day = 13
    hours = 15
    minutes = 31
    seconds = 0

    flight_date = datetime(year, month, day, hours, minutes, seconds)
    flight_date_text = flight_date.strftime('%a %d %b %Y')
    flight_time_text = flight_date.strftime('%H%M')
    flight_airline = "EMIRATES"
    flight_code = "EK000"
    flight_departing = "NEW YORK"
    flight_arriving_city = "PARIS"
    flight_arriving_country = "FRANCE"
    flight_arriving_time = "2315"
    flight_class = "Y - Economy Class"
    flight_reference = "5R78U4"
    flight_ticket = str(randint(a=100, b=999)) + " " + str(randint(a=1000000000, b=9999000000))
    flight_aircraft = "BOEING 737"
    flight_seats = "1"
    flight_bag_check = "1 pcs - Baggage allowance listed not inclusive of any frequent flyer benefits"
    flight_bag_add = "No Extra Baggage has been purchased. Refer to Agent if Extra Baggage is required."
    flight_stops = "0"
    flight_time = "8 hrs 20 mins"

filename = st.text_input('Filename', "newticket")
ticket_number = st.text_input('Ticket_Number', "999")

booking_num = st.text_input('Booking_Num', "9999")
date_number = st.text_input('Date_Number', "30.05.2023")
booking_agent = st.text_input('Booking_Agent', "Booking guy")
booking_phone = st.text_input('Booking_Phone', "080000000")
booking_email = st.text_input('Booking_Email', "bookingguy@travelagent")
booking_logo = st.text_input('Booking_Logo', "images/logo.jpg")
booking_address = st.text_input('Booking_Address', "booking address")
booking_company = st.text_input('Booking_Company', "Company")
booking_gds = st.text_input('Booking_Gds', "AAABBB")

passenger_last = st.text_input('Passenger_Last', "Last name")
passenger_first = st.text_input('Passenger_First', "first name")
passenger_title = st.text_input('Passenger_Title', "MR")
passenger_full_name = passenger_last + ' / ' + passenger_first + ' ' + passenger_title

passenger_ff = st.text_input('Passenger_Ff', "ff number")
passenger_country = st.text_input('Passenger_Country', "nationality")
passenger_country_web = st.text_input('Passenger_Country_Web', "govwebsite.gov")

year = st.number_input('Year', 2020)
month = st.number_input('Month', 10)
day = st.number_input('Day', 13)
hours = st.number_input('Hours', 15)
minutes = st.number_input('Minutes', 31)
seconds = st.number_input('Seconds', 0)

flight_date = datetime(year, month, day, hours, minutes, seconds)
flight_date_text = flight_date.strftime('%a %d %b %Y')
flight_time_text = flight_date.strftime('%H%M')
flight_airline = st.text_input('Flight_Airline', "EMIRATES")
flight_code = st.text_input('Flight_Code', "EK000")
flight_departing = st.text_input('Flight_Departing', "NEW YORK")
flight_arriving_city = st.text_input('Flight_Arriving_City', "PARIS")
flight_arriving_country = st.text_input('Flight_Arriving_Country', "FRANCE")
flight_arriving_time = st.text_input('Flight_Arriving_Time', "2315")
flight_class = st.text_input('Flight_Class', "Y - Economy Class")
flight_reference = st.text_input('Flight_Reference', "5R78U4")
flight_ticket = st.text_input('Flight_Ticket', str(randint(a=100, b=999)) + " " + str(randint(a=1000000000, b=9999000000)))
flight_aircraft = st.text_input('Flight_Aircraft', "BOEING 737")
flight_seats = st.text_input('Flight_Seats', "1")
flight_bag_check = st.text_input('Flight_Bag_Check', "1 pcs - Baggage allowance listed not inclusive of any frequent flyer benefits")
flight_bag_add = st.text_input('Flight_Bag_Add', "No Extra Baggage has been purchased. Refer to Agent if Extra Baggage is required.")
flight_stops = st.text_input('Flight_Stops', "0")
flight_time = st.text_input('Flight_Time', "8 hrs 20 mins")



col_width = 40
line_break = 5
passenger_column1 = 80
passenger_column2 = 60
passenger_column3 = 40
ticket_column = 35
col_width_t = 50
line_height = 5


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_fill_color(r=200)
pdf.set_auto_page_break(auto=False, margin=0)
pdf.add_page()
pdf.set_font(family="Arial", style="B", size=10)
pdf.cell(w=col_width, h=12, txt="Invoice num: ", align="L")
pdf.set_font('')
pdf.cell(w=col_width, h=12, txt=ticket_number, align="L")
pdf.image(booking_logo, w=0, h=12, x=150)
pdf.set_x(x=150)
pdf.cell(w=col_width, h=12, txt=booking_address, align="L")
pdf.ln(line_break)
pdf.set_y(y=15)
pdf.set_font('', 'B')
pdf.cell(w=col_width, h=12, txt="Date: ", align="L")
pdf.set_font('')
pdf.cell(w=col_width, h=12, txt=date_number, align="L")
pdf.ln(line_break)
pdf.set_font('', 'B')
pdf.cell(w=col_width, h=12, txt="Consultant: ", align="L")
pdf.set_font('')
pdf.cell(w=col_width, h=12, txt=booking_agent, align="L")
pdf.set_font('', 'B')
pdf.ln(line_break)
pdf.cell(w=col_width, h=12, txt="Phone: ", align="L")
pdf.set_font('')
pdf.cell(w=col_width, h=12, txt=booking_phone, align="L")
pdf.set_font('', 'B')
pdf.ln(line_break)
pdf.cell(w=col_width, h=12, txt="Email: ", align="L")
pdf.set_font('')
pdf.cell(w=col_width, h=12, txt=booking_email, align="L")
pdf.set_font('', 'B')
pdf.ln(line_break)
pdf.cell(w=col_width, h=12, txt="GDS Reference: ", align="L")
pdf.set_font('')
pdf.cell(w=col_width, h=12, txt=booking_gds, align="L")
pdf.set_font('', 'B', 18)
pdf.ln(line_break)
pdf.ln(line_break)
pdf.ln(line_break)
pdf.cell(w=col_width, h=12, txt="Passenger ", align="L")
pdf.ln(10)
pdf.set_font('', 'B', 10)
pdf.cell(w=passenger_column1, h=12, txt=passenger_last + ' / ' + passenger_first + ' ' + passenger_title, align="C", fill=True)
pdf.cell(w=60, h=12, txt="FF " + passenger_ff, align="C", fill=True)
pdf.cell(w=40, h=12, txt="", align="C", fill=True)
pdf.ln(line_break)
pdf.ln(line_break)
pdf.ln(line_break)
pdf.set_font('')

pdf.multi_cell(w=0, h=5, txt=intro_writing, align="L")
pdf.set_font('', 'B', 18)
pdf.ln(line_break)
pdf.ln(line_break)
pdf.cell(w=col_width, h=12, txt="Your Itinerary", align="L")
pdf.ln(10)
ticket_1_x = pdf.get_x()
ticket_1_y = pdf.get_y()
pdf.cell(w=0, h=75, txt="", align="C", fill=True)
pdf.set_font('', 'B', 10)
pdf.set_x(ticket_1_x)
pdf.set_y(ticket_1_y)
pdf.cell(w=passenger_column1, h=5, txt=flight_date_text + " at " + flight_time_text, align="C")
pdf.cell(w=passenger_column2, h=5, txt=flight_airline + " (" + flight_code + ")", align="L")
pdf.ln(line_break)
pdf.set_x(ticket_column)
pdf.set_font('')
pdf.cell(w=col_width_t, h=line_height, txt="Departing: ", align="L")
pdf.cell(w=col_width, h=line_height, txt=flight_departing + " at " + flight_time_text, align="L")
pdf.ln(line_break)
pdf.set_x(ticket_column)
pdf.cell(w=col_width_t, h=line_height, txt="Arriving: ", align="L")
pdf.cell(w=col_width, h=line_height, txt=flight_arriving_city + ", " + flight_arriving_country + " at " + flight_arriving_time, align="L")
pdf.ln(line_break)
pdf.set_x(ticket_column)
pdf.cell(w=col_width_t, h=line_height, txt="Class of Service: ", align="L")
pdf.cell(w=col_width, h=line_height, txt=flight_class, align="L")
pdf.ln(line_break)
pdf.set_x(ticket_column)
pdf.cell(w=col_width_t, h=line_height, txt="Flight Status: ", align="L")
pdf.cell(w=col_width, h=line_height, txt="Confirmed [HK]", align="L")
pdf.ln(line_break)
pdf.set_x(ticket_column)
pdf.cell(w=col_width_t, h=line_height, txt="Airline Reference: ", align="L")
pdf.cell(w=col_width, h=line_height, txt=flight_reference, align="L")
pdf.ln(line_break)
pdf.set_x(ticket_column)
pdf.multi_cell(w=col_width_t, h=5, txt="Ticket Number" + " (" + passenger_full_name + "): ", align="L")
pdf.set_x(ticket_column+col_width_t)
pdf.set_y(pdf.get_y()-5)
pdf.set_x(ticket_column+col_width_t)
pdf.cell(w=col_width_t, h=line_height, txt=flight_ticket, align="L")
pdf.ln(line_break)
pdf.set_x(ticket_column)
pdf.cell(w=col_width_t, h=line_height, txt="Aircraft: ", align="L")
pdf.cell(w=col_width, h=line_height, txt=flight_aircraft, align="L")
pdf.ln(line_break)
pdf.set_x(ticket_column)
pdf.cell(w=col_width_t, h=line_height, txt="Number of Seats: ", align="L")
pdf.cell(w=col_width, h=line_height, txt=flight_seats, align="L")
pdf.ln(line_break)
pdf.set_x(ticket_column)
pdf.cell(w=col_width_t, h=line_height, txt="Include Checked Baggage: ", align="L")
pdf.cell(w=col_width, h=line_height, txt=flight_bag_check, align="L")
pdf.ln(line_break)
pdf.set_x(ticket_column)
pdf.cell(w=col_width_t, h=line_height, txt="Additional Purchased Baggage: ", align="L")
pdf.cell(w=col_width, h=line_height, txt=flight_bag_add, align="L")
pdf.ln(line_break)
pdf.set_x(ticket_column)
pdf.cell(w=col_width_t, h=line_height, txt="Number of Stops: ", align="L")
pdf.cell(w=col_width, h=line_height, txt=flight_stops, align="L")
pdf.ln(line_break)
pdf.set_x(ticket_column)
pdf.cell(w=col_width_t, h=line_height, txt="Flight Time: ", align="L")
pdf.cell(w=col_width, h=line_height, txt=flight_time, align="L")
pdf.ln(line_break)
pdf.ln(10)

pdf.set_font(family="Arial", style="", size=8)
pdf.set_auto_page_break(auto=1)
pdf.write(h=5, txt=end_writing)

new_filename = filename + flight_ticket[:3] + ".pdf"

generate_ticket = st.checkbox("Generate ticket")
if generate_ticket:
    pdf.output(f"tickets\\{new_filename}")
with open(f"tickets\\{new_filename}", "rb") as file:
    btn = st.download_button(label='Download example ticket', data=file, file_name=new_filename)
