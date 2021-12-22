#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 15:00:38 2018

@author: peterspencer-smith
"""
import numpy as np
import matplotlib.pyplot as plt

MyInput = '0'
while MyInput != 'q':
    MyInput = input('In this exercise Felix Baumgartner’s supersonic freefall is modeled, under various conditions, \
using variations of the Euler method, which solves the differential equation describing the motion of an object in free fall. \
\n\nPlease enter one of the following choices, "a" where the Euler method is used to solve the differential \
equation, "b" where an analytical solution to the problem described in part a), \
is compared with the Euler method, "c" where a a modified version of the Euler method is coded and the results \
compared to those presented in part a), "d" where finally, air density is introduced as a function of position, or "q" to quit: ')
    print('User has entered the choice: ',MyInput)

    if MyInput == 'a':
        
        input_h= input('Please enter a value for h, the time inteval in seconds (a floating point number of around 0.1): ')
        h=float(input_h)

#Part a, The Euler method:
#establish the constants and initial conditions..    
        t=0
        y=1000
        v=0
        
        c=1
        A=0.7
        p=1
        g=9.8
        k=(c*p*A)/2
        m=75
#Create empty lists to populate via the while loop..             
        v_values = []
        y_values = []
        t_values = []
      
        while (y>0):
            y=y+(h*v)
            v=v-h*(g+(k/m)*np.abs(v)*v)
            t=t+h
#Populate the lists...
            y_values.append(y)
            t_values.append(t)
            v_values.append(v)
#Plot the lists...
        print('')
        print('Graphs showing the Euler method soloution')
        print('')
        plt.plot(t_values,y_values)
        plt.title('Plot of position for the Euler method')
        plt.ylabel('Y-axis position (m)')
        plt.xlabel('Time (s)')
        plt.show()
        print('Plot of velocity')
        plt.plot(t_values,v_values)
        plt.title('Plot of Velocity for the Euler method')
        plt.ylabel('Velocity of falling object (m/s)')
        plt.xlabel('Time (s)')        
        plt.show()
        
#Part b, The analytical soloution:
    elif MyInput == 'b':

        t_1=np.arange(0,25.1,0.1)
        y_0=1000
#The analytical soloution coded mathematically...
        y_1=y_0-(m/(2*k))*(np.log((np.cosh(np.sqrt((k*g)/m)*t_1))**2))
        v_1=-np.sqrt((m*g)/k)*np.tanh(np.sqrt((k*g)/m)*t_1)
        
        print('')
        print('Graphs showing the analytical soloution')
        print('')
        plt.plot(t_1,y_1)
        plt.title('Plot of position for the analytical method')
        plt.ylabel('Y-axis position (m)')
        plt.xlabel('Time (s)')        
        plt.show()
        plt.plot(t_1,v_1)
        plt.title('Plot of Velocity for the analytical method')
        plt.ylabel('Velocity of falling object (m/s)')
        plt.xlabel('Time (s)')                
        plt.show()
        
#Part c, the modified Euler method: 
#This section is the same as section a, with the while loop modified..
    elif MyInput == 'c':
      
        t=0
        y1=1000
        v1=0
        v=0
        y=1000
        
        c=1
        A=0.7
        p=1
        
        g=9.8
        k=(c*p*A)/2
        m=75
        
        input_h= input('Please enter a value for h, the time inteval in seconds (a floating point number of around 0.1): ')
        h=float(input_h)
        
        v_values = []
        y_values = []
        t_values = []
        
        while (y>0):
#The modified  part of the loop..         
            y1=y+((h/2)*v1)
            v1=v-(h/2)*(g-(k/m)*v1**2)
            t1=t+h/2
            
            y=y+(h*v1)
            v=v-h*(g-(k/m)*v1**2)
            t=t+h
            
            y_values.append(y)
            t_values.append(t)
            v_values.append(v)
        
        print('')
        print('Graphs showing the modified Euler method soloution')
        print('')
        plt.plot(t_values,y_values)
        plt.title('Plot of position for the modified Euler method')
        plt.ylabel('Y-axis position (m)')
        plt.xlabel('Time (s)')
        plt.show()
        plt.plot(t_values,v_values)
        plt.title('Plot of Velocity for the modified Euler method')
        plt.ylabel('Velocity of falling object (m/s)')
        plt.xlabel('Time (s)')        
        plt.show()
 
    elif MyInput == 'd':
        t=0
        v=0
        c=1
        A=0.7
        p0=1.2   
        g=9.8
        m=75
        y1=7640
        v1=0
        
        h=0.1
        
        #Sets the initial height of the jump..
        y=7640
        
        v_values = []
        y_values = []
        t_values = []
        
        while (y>0):
        
        #Setting air density as a function of position..       
            p=p0*np.exp(-y/7640)
            k=(c*p*A)/2
        
            y1=y+((h/2)*v1)
            v1=v-(h/2)*(g-(k/m)*v1**2)
            t1=t+h/2
        
        
            v=v-h*(g+(k/m)*np.abs(v)*v)
            y=y+(h*v)
            t=t+h
            
            y_values.append(y)
            t_values.append(t)
            v_values.append(v)
        
        print('')
        print('Graphs showing the modified Euler method soloution, using air density as a function of position')
        print('')
        plt.plot(t_values,y_values)
        plt.title('Plot of position for the modified Euler method with air density a function of position')
        plt.ylabel('Height above sea level (m)')
        plt.xlabel('Time (s)')
        plt.show()
        plt.plot(t_values,v_values)
        plt.title('Plot of Velocity for the Euler method with air density a function of position')
        plt.ylabel('Velocity of falling object (m/s)')
        plt.xlabel('Time (s)')        
        plt.show()
      
    elif MyInput != 'q':
        print('Sorry, this is not a recognised choice')
        
print('Farewell.')













