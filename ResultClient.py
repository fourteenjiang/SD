import socket
import xlsxwriter
import xlrd
from fuzzylogic.classes import Domain, Set, Rule
from fuzzylogic.classes import Domain
from fuzzylogic.functions import bounded_sigmoid
import matplotlib.pyplot as plt
from fuzzylogic.functions import R, S
from fuzzylogic.functions import (sigmoid, gauss, trapezoid,
                                  triangular_sigmoid, rectangular)

import serial


ser = serial.Serial(port="COM3", baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE, timeout=5)  # 开启com3口，波特率9600，超时5
ser.flushInput()  # 清空缓冲区
HOST = '192.168.125.1'
PORT = 1023
from fuzzylogic.classes import Domain, Set, Rule
from fuzzylogic.classes import Domain
from fuzzylogic.functions import bounded_sigmoid
import matplotlib.pyplot as plt
from fuzzylogic.functions import R, S
from fuzzylogic.functions import (sigmoid, gauss, trapezoid,
                             triangular_sigmoid, rectangular)


def fuzzy_logic(x1, x2,x3):
    A = Domain("angle",45,55, res=0.02)
    D = Domain("Difference", -0.1, 2, res=0.02)
    density = Domain("density", 0, 5, res=0.02)
    Sa = Domain("shaking", 0.1, 8,res=0.02)
    P = Domain('particle size', 0, 5, res=0.02)
    D1= Domain("Differenceforsmallspoon", 0, 0.1, res=0.0002)
    D1.vs=S(0.005,0.01)
    D1.s=trapezoid (0.005, 0.01, 0.015, 0.02, c_m=1)
    D1.m = trapezoid( 0.015, 0.02,0.03,0.035, c_m=1)
    D1.l= trapezoid ( 0.03, 0.035, 0.05,0.055, c_m=1)
    D1.vl=R(0.05,0.055)
    # D1.vs.plot()
    # D1.s.plot()
    # D1.m.plot()
    # D1.l.plot()
    # D1.vl.plot()
    # plt.text(0.001, 0.9, 'VS')
    # plt.text(0.011, 0.9, 'S')
    # plt.text(0.025, 0.9, 'M')
    # plt.text(0.04, 0.9, 'L')
    # plt.text(0.08, 0.9, 'VL')
    # plt.xlabel("Difference (g) ")
    # plt.ylabel("Membership value")
    # plt.show()

    A.vs = S(45.5,46)
    A.s = trapezoid(45.5,46,46.5,47, c_m=1)
    A.m = trapezoid(46.5,47,48,48.5, c_m=1)
    A.l = trapezoid(48,48.5,49.5,50, c_m=1)
    A.vl = R(49.5,50)
    # A.vs.plot()
    # A.s.plot()
    # A.m.plot()
    # A.l.plot()
    # A.vl.plot()
    # plt.text(45.12, 0.9, 'VS')
    # plt.text(46.1, 0.9, 'S')
    # plt.text(47.5, 0.9, 'M')
    # plt.text(48.9, 0.9, 'L')
    # plt.text(52.4, 0.9, 'VL')
    # plt.xlabel("Tilt angle ")
    # plt.ylabel("Membership value")
    # plt.show()



    D.small = S(0.2, 0.4)
    D.large = R(0.6, 0.8)
    D.medium = trapezoid(0.2, 0.4, 0.6, 0.8, c_m=1)

    # D.small.plot()
    # D.medium.plot()
    # D.large.plot()
    # plt.xlim(0,1)
    # plt.text(0.1, 0.9, 'S')
    # plt.text(0.5, 0.9, 'M')
    # plt.text(0.89, 0.9, 'L')
    # plt.xlabel("Difference (g) ")
    # plt.ylabel("Membership value")
    # plt.show()

    density.small = S(1.0, 2.5)
    density.large = R(4, 4.5)
    density.medium = trapezoid(2, 2.8, 3.6, 4.2, c_m=1)
    # density.small.plot()
    # density.medium.plot()
    # density.large.plot()
    # plt.text(0.5, 0.9, 'S')
    # plt.text(3.17, 0.9, 'M')
    # plt.text(4.7, 0.9, 'L')
    # plt.xlabel("Density (g/cm3) ")
    # plt.ylabel("Membership value")
    # plt.show()
    Sa.small = S(1,3)
    Sa.large = R(4,6)
    #Sa.medium = trapezoid(1, 2, 4, 8, c_m=1)
    Sa.medium = trapezoid(1,3,4,6, c_m=1)
    # Sa.small.plot()
    # Sa.medium.plot()
    # Sa.large.plot()
    # plt.text(0.5, 0.9, 'S')
    # plt.text(3.45, 0.9, 'M')
    # plt.text(7.26, 0.9, 'L')
    # plt.xlabel("Robot shaking times ")
    # plt.ylabel("Membership value")
    # plt.show()
    P.small = S(1.5, 3)
    P.large = R(1.5, 3)
    # P.small.plot()
    # P.large.plot()
    # plt.text(0.1, 0.9, 'S')
    # plt.text(5, 0.9, 'L')
    # plt.xlabel("Particle size ")
    # plt.ylabel("Membership value")
    # plt.show()


    # R1 = Rule({(D.small, density.medium, P.small): Sa.small})
    # R2 = Rule({(D.small, density.small, P.small): Sa.small})
    # R3 = Rule({(D.small, density.large, P.small): Sa.small})
    # R4 = Rule({(D.medium, density.small, P.small): Sa.large})
    # R5 = Rule({(D.medium, density.medium, P.small): Sa.medium})
    # R6 = Rule({(D.medium, density.large, P.small): Sa.medium})
    # R7 = Rule({(D.large, density.small, P.small): Sa.large})
    # R8 = Rule({(D.large, density.medium, P.small): Sa.large})
    # R9 = Rule({(D.large, density.large, P.small): Sa.large})
    # R10 = Rule({(D.small, density.medium, P.large): Sa.small})
    # R11 = Rule({(D.small, density.small, P.large): Sa.small})
    # R12 = Rule({(D.small, density.large, P.large): Sa.small})
    # R13 = Rule({(D.medium, density.small, P.large): Sa.medium})
    # R14 = Rule({(D.medium, density.medium, P.large): Sa.medium})
    # R15 = Rule({(D.medium, density.large, P.large): Sa.small})
    # R16 = Rule({(D.large, density.small, P.large): Sa.large})
    # R17 = Rule({(D.large, density.medium, P.large): Sa.large})
    # R18 = Rule({(D.large, density.large, P.large): Sa.large})
    R1 = Rule({(D.small, P.small): Sa.small})
    R2 = Rule({(D.small, P.large): Sa.small})
    R3 = Rule({(D.medium, P.small): Sa.large})
    R4 = Rule({(D.medium, P.large): Sa.medium})
    R5 = Rule({(D.large, P.small): Sa.large})
    R6 = Rule({(D.large, P.large): Sa.large})

    A1 = Rule({(D1.vs, P.small): A.s})
    A2 = Rule({(D1.vs, P.large): A.vs})
    A3 = Rule({(D1.s, P.small): A.s})
    A4 = Rule({(D1.s, P.large): A.s})
    A5 = Rule({(D1.m, P.small): A.l})
    A6 = Rule({(D1.m,  P.large): A.m})
    A7 = Rule({(D1.l,  P.small): A.vl})
    A8 = Rule({(D1.l,  P.large): A.l})
    A9 = Rule({(D1.vl, P.small): A.vl})
    A10 = Rule({(D1.vl, P.large): A.l})




    # rules_shaking = sum([R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18])
    rules_shaking = sum([R1, R2, R3, R4, R5, R6])
    rules_angle = sum([A1, A2, A3, A4, A5, A6, A7, A8, A9, A10])

    X = {D: x1, P:x3}
    X1= {D1: x1, P: x3}
    y = rules_shaking(X)
    y1= rules_angle(X1)
    return [y,y1]
    print(y,y1)


def calculate_shaking(target_w,d,v,p,weight):#target weight,density

                w=float(weight)
                D =target_w - float(w)+v
                M= fuzzy_logic(D,d,p)
                return M
def getw(switch=True):

 while switch:

        count = ser.inWaiting()
        if count != 0:
            recv = ser.read(size=32).decode("ASCII")  # 读出串口数据，数据采用ASCII编码
            if recv==None:
                w=None


            elif recv.find('?') != -1:
                w = None # the weight on data no stable

            else:
                weight = recv.splitlines()
                w1 = [x for x in weight if weight.count(x) > 1]

                if w1:
                    w = w1[0]
                    w=float(w)


                else:
                    w = None #unvalid num

        else: w=None




        if w!=None:
            switch=False
            return w
        else:
            switch=True


def main():

    loc = ("C:\\Users\\fourteen\\Desktop\\500mg.xls")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    row = 1#1
    col = 1 #1
    density=2.11
    vial_weight=9.7
    particle_size=3

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.connect((HOST, PORT))
        soc.settimeout(30) #15
          # 获取串口缓冲区数据


        yumi_done = False
        while not yumi_done:
            recv_msg = soc.recv(10240)
            recv_string=recv_msg.decode()
            if (recv_string == 'new_target'):
                print("new_target")
                if (row in range(sheet.nrows-1)):
                  row = row + 1
                else:
                  if (col in  range(sheet.ncols-1)):
                       row = row + 2- sheet.nrows
                       col = col + 1
                  else:
                        yumi_done = True
                target_weight = sheet.cell_value(row, col)
                print(target_weight,type(target_weight))
                W = getw()
                y=calculate_shaking(target_weight,density,vial_weight,particle_size,W)
                y0=y[0] #shaking
                y1=y[1]#angle
                if y0==None or W==None or y1==None:
                    y0=1000
                    y1=1000
                    W=100
                target_weight_2=target_weight






                #string_weight = str(target_weight)
                #compount_msg = "s1," + string_weight # "s1,0.25"
                send_string=''+(str(target_weight))+' '+str(y0)+' '+str(W)+' '+str(y1)+' '+'#'
                soc.send(send_string.encode())
               # print(send_string)
            elif  ( 'executing' in recv_string ):
                W = getw()
                y= calculate_shaking(target_weight_2, density,vial_weight,particle_size,W)

                y0=y[0] #shaking
                y1=y[1]#angle
                if y0==None or W==None or y1==None:
                    y0=1000
                    y1=1000
                    W=100
                send_string2 = '' + '0' + ' ' + str(y0) + ' ' + str(W) + ' ' +str(y1)+' '+ '#'
                soc.send(send_string2.encode())
                #print(send_string2)
            elif (recv_msg!=0):
                vial_weight= float(recv_string)



if __name__ == '__main__':
    main()