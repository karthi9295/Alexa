import sys
sys.path.append("C:\\Python27\\Lib\\site-packages")
from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode
import pandas as pd
import datetime
from datetime import datetime as dt

app = Flask(__name__)
ask = Ask(app, "/personal_assistant")

def load_file():
    csv_path = pd.read_csv("C:/Users/30216/Desktop/amazon-alexa/appointment_details.csv")
    return csv_path

def get_appointment_today():
    csv_path  = load_file()
    now = datetime.datetime.now()
    current_date = now.strftime("%d/%m/%Y")
    current_date = dt.strptime(current_date, "%d/%m/%Y")
    patient_info_current = []
    count = 0
    for i in range(0,len(csv_path['patient_name'])):
        record_date = dt.strptime(csv_path['date'][i], "%d/%m/%Y")
        if (current_date == record_date):
            count += 1
            patient_info_current.append("{}...patient name  {}...aged {}...from...{}...for ...{}".format(count,csv_path['patient_name'][i],csv_path['age'][i],csv_path['address'][i],csv_path['appointment_detail'][i]))
    return patient_info_current,count

def get_appointment_previous():
    csv_path  = load_file()
    now = datetime.datetime.now()
    current_date = now.strftime("%d/%m/%Y")
    current_date = dt.strptime(current_date, "%d/%m/%Y")
    patient_info_previous = []
    count = 0
    for i in range(0,len(csv_path['patient_name'])):
        record_date = dt.strptime(csv_path['date'][i], "%d/%m/%Y")
        if (current_date > record_date):
            count += 1
            patient_info_previous.append("{}...patient name  {}...aged {}...from...{}...for...{}".format(count,csv_path['patient_name'][i],csv_path['age'][i],csv_path['address'][i],csv_path['appointment_detail'][i]))
    return patient_info_previous,count

def get_appointment_future():
    csv_path  = load_file()
    now = datetime.datetime.now()
    current_date = now.strftime("%d/%m/%Y")
    current_date = dt.strptime(current_date, "%d/%m/%Y")
    patient_info_future = []
    count = 0
    for i in range(0,len(csv_path['patient_name'])):
        record_date = dt.strptime(csv_path['date'][i], "%d/%m/%Y")
        if (current_date < record_date):
            count += 1
            patient_info_future.append("{}...patient name  {}...aged {}...from...{}...for...{}".format(count,csv_path['patient_name'][i],csv_path['age'][i],csv_path['address'][i],csv_path['appointment_detail'][i]))
    return patient_info_future,count


@app.route('/')
def homepage():
    return "hi there, how ya doing ?"

@ask.launch
def start_skill():
    welcome_message = 'Hello there, how would I help you ?'
    return question(welcome_message)

@ask.intent("YesIntent")
def share_appointment_today():
    appointments, count = get_appointment_today()
    if (count == 1):
        appointment_msg = 'You have {} appointment for today ... The appointment is {}'.format(count,appointments)
    if (count > 1):
        appointment_msg = 'You have {} appointments for today ... The appointments are {}'.format(count,appointments)
    if (count == 0):
        appointment_msg = 'You dont have any appointments today'
    return statement(appointment_msg)

@ask.intent("PreviousIntent")
def share_appointment_previous():
    appointments, count = get_appointment_previous()
    if (count == 1):
        appointment_msg = 'You had {} previous appointment ... The appointment is {}'.format(count,appointments)
    if (count > 1):
        appointment_msg = 'You had {} previous appointments ... The appointments are {}'.format(count,appointments)
    if (count == 0):
        appointment_msg = 'You dont have any previous appointments'
    return statement(appointment_msg)

@ask.intent("FutureIntent")
def share_appointment_future():
    appointments, count = get_appointment_future()
    if (count == 1):
        appointment_msg = 'You are having {} future appointment ... The appointment is {}'.format(count,appointments)
    if (count > 1):
        appointment_msg = 'You are having {} future appointments ... The appointments are {}'.format(count,appointments)
    if (count == 0):
        appointment_msg = 'You dont have any previous appointments'
    return statement(appointment_msg)

@ask.intent("NoIntent")
def no_intent():
    bye_text='Its ok...bye'
    return statement(bye_text)

if __name__=='__main__':
    
    app.run(debug=True)
