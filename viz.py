#!/usr/bin/env python
'''
Quick script to vizulize points from DCC program.
The program reads in a textfile whose fomat is x-cord\n y-cord\n z-cord then repeats
Author: Jake Chanenson / 25 July 2019
'''
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def main():
    print "*********************************************"
    print "************DRONE PATH VISUALIZER************"
    print "*********************************************\n"
    progLen = input("Please enter how many paths you want to render: ")

    x =[]
    y =[]
    z =[]

    for i in range(progLen):
        print "\n \n****************Path Viz {0}*****************".format(i+1)
        #Setting up the figures
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        #Clear lists for next figure
        del x[:]
        del y[:]
        del z[:]

        readCoords(x, y, z)

        #set the axis dim
        print "\nPlease type '0' if you want the axis set automatically,"
        print "type '1' to set the upperbounds manually, or type '2' to set both bounds"
        dimFlag = int(input("\nType your selction here: "))
        if dimFlag == 1:
            xH = float(input("Please input a float upperbound for the x-axis: "))
            yH = float(input("Please input a float upperbound for the y-axis: "))
            zH = float(input("Please input a float upperbound for the z-axis: "))

            ax.set(xlim=(0,xH), ylim=(0,yH))
            ax.set_zlim(0,zH)

        elif dimFlag == 2:
            xL = float(input("Please input a float lowerbound for the x-axis: "))
            yL = float(input("Please input a float lowerbound for the y-axis: "))
            zL = float(input("Please input a float lowerbound for the z-axis: "))
            print "---------------------------------------------------"
            xH = float(input("Please input a float upperbound for the x-axis: "))
            yH = float(input("Please input a float upperbound for the y-axis: "))
            zH = float(input("Please input a float upperbound for the z-axis: "))

            ax.set(xlim=(xL,xH), ylim=(yL,yH))
            ax.set_zlim(zL,zH)
        #create the plots and plot the points
        figTitle = raw_input('Please input the figure title: ')
        fig.suptitle(figTitle, fontsize=16)
        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis')
        ax.plot(x, y, z)

        plt.show()

def readCoords(x, y, z):
    """
    This function gets the file name and reads in the cords from the file and
    put the x coords in the x list, y coords in the y list, and z coords in the
    z list. 
    """
    #pNum = input("Please enter participant number: ")
    pGest = raw_input("Please enter the file name: ")
    #filename = '/home/jake/Desktop/participant00'+str(pNum)+'/'+pGest+'.txt'
    filename = '/home/jake/Desktop/participant007/'+pGest+'.txt'

    try:
        with open(filename, 'r') as f:
            cntr = 1
            for line in f:
                num = float(line)
                if cntr == 1:
                    x.append(num)
                    cntr+=1
                elif cntr == 2:
                    y.append(num)
                    cntr+=1
                elif cntr == 3:
                    absNum = abs(num)
                    z.append(absNum)
                    cntr = 1
    except IOError: #If the input file was not found
        print("File not found. Please input the filename w/out the extension.\nPlease try again.")
        print "recursion!"
        readCoords(x, y, z)

if __name__ == "__main__":
    main()
