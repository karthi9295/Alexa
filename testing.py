# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 12:38:28 2017

@author: 30216
"""
import pandas as pd
import datetime
from datetime import datetime as dt


def get_appointment():
    now = datetime.datetime.now()
    current_date = now.strftime("%d/%m/%Y")
    current_date = dt.strptime(current_date, "%d/%m/%Y")
    csv_path = pd.read_csv("C:/Users/30216/Desktop/amazon-alexa/appointment_details.csv")
    patient_info = []
    count = 0
    for i in range(0,len(csv_path['patient_name'])):
        record_date = dt.strptime(csv_path['date'][i], "%d/%m/%Y")
        if (current_date == record_date):
            patient_info.append("{}...{}...aged {}...from...{}...for ...{}".format(csv_path['patient_id'][i],csv_path['patient_name'][i],csv_path['age'][i],csv_path['address'][i],csv_path['appointment_detail'][i]))
            count += 1
    return(patient_info,count)

appointment,count = get_appointment()





