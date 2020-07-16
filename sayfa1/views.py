from django.shortcuts import render
from django.http import HttpResponse
from evds import evdsAPI
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


def home(request):
    evds = evdsAPI('RwIRmdu6Gq')
    data=evds.get_data(['TP.KKHARTUT.KT1'], startdate="01-01-2015", enddate="01-01-2020")
    date=data['Tarih'].values.tolist()
    deger=data['TP_KKHARTUT_KT1'].values.tolist()

    data=evds.get_data(['TP.KKHARTUT.KT1'], startdate="01-01-2015", enddate="01-01-2020")
    data = data[(data['YEARWEEK']>='2015-1')&(data['YEARWEEK']<='2015-52')]
    df2015=data['TP_KKHARTUT_KT1'].sum(axis = 0, skipna = True).tolist()

    data1=evds.get_data(['TP.KKHARTUT.KT1'], startdate="01-01-2015", enddate="01-01-2020")
    data1 = data1[(data1['YEARWEEK']>='2016-1')&(data1['YEARWEEK']<='2016-52')]
    df2016=data1['TP_KKHARTUT_KT1'].sum(axis = 0, skipna = True).tolist()

    data2=evds.get_data(['TP.KKHARTUT.KT1'], startdate="01-01-2015", enddate="01-01-2020")
    data2 = data2[(data2['YEARWEEK']>='2017-1')&(data2['YEARWEEK']<='2017-52')]
    df2017=data2['TP_KKHARTUT_KT1'].sum(axis = 0, skipna = True).tolist()

    data3=evds.get_data(['TP.KKHARTUT.KT1'], startdate="01-01-2015", enddate="01-01-2020")
    data3 = data3[(data3['YEARWEEK']>='2018-1')&(data3['YEARWEEK']<='2018-52')]
    df2018=data3['TP_KKHARTUT_KT1'].sum(axis = 0, skipna = True).tolist() 

    data4=evds.get_data(['TP.KKHARTUT.KT1'], startdate="01-01-2015", enddate="01-01-2020")
    data4 = data4[(data4['YEARWEEK']>='2019-1')&(data4['YEARWEEK']<='2019-52')]
    df2019=data4['TP_KKHARTUT_KT1'].sum(axis = 0, skipna = True).tolist()

    context={'date':date,'deger':deger,'df':df2015,'df1':df2016,'df2':df2017,'df3':df2018,'df4':df2019}

    return render(request,'index.html',context)

