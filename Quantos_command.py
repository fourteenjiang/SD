import serial
import threading
import time
import logging
import sys
switch= True
wait_command= True
wait_command1= True
wait_command2= True

ser = serial.Serial(port="COM4", baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
             stopbits=serial.STOPBITS_ONE, timeout=5,)

ser.flushInput()  # 清空缓冲
num=0


def stopdosing():
    global switch, wait_command, wait_command2,wait_command1
    ser.write(("QRA 61 4"+ '\n').encode("utf-8"))
    wait_command=False
    wait_command1 = False
    wait_command2 = False
    switch = False

def startdosing():
    global wait_command,time1,time2
    ser.write(("QRA 61 1" + '\n').encode("utf-8"))
    time.sleep(2)
    time1 = time.time()
    while wait_command:

        r = ser.readline().decode()
        read_string = r.strip()
        print(num, read_string)
        if read_string == 'QRA 61 1 I 13':
            print(str(num) + 'dispensing finish but sampler blocking')
            stopdosing()

        elif read_string == None:
            time.sleep(0.2)


        elif read_string == 'QRA 61 1 I 10':
            print(str(num) + 'dispensing finish but head not allow')
            stopdosing()

        elif read_string == 'QRA 61 1 I 11':
            print(str(num) + 'dispensing finish but head limit reach')
            stopdosing()
        elif read_string == 'QRA 61 1 A':
            wait_command = False
        elif read_string == 'QRA 61 1 B':
            wait_command = True
        elif read_string in ['QRA 61 1 I 0', 'QRA 61 1 I 1', 'QRA 61 1 I 2', 'QRA 61 1 I 3', 'QRA 61 1 I 4', 'QRA 61 1 I 5', 'QRA 61 1 I 6', 'QRA 61 1 I 7', 'QRA 61 1 I 8', 'QRA 61 1 I 9', 'QRA 61 1 I 12','QRA 61 1 I 13']:

            print(str(num) + 'dispensing finish but error code' + read_string)
            stopdosing()
    time2=time.time()

def getsmapledata():
    global wait_command1, switch,time1,time2
    ser.write(("QRD 2 4 12"+ '\n').encode('utf-8'))
    while wait_command1:
        r= ser.readline().decode()
        read_string=r.strip()
        print(num, read_string)
        if read_string == 'QRD 2 4 12 B':
            time.sleep(1)
        elif read_string==None:
            time.sleep(0.2)
        elif read_string == 'QRD 2 4 12 A':
            wait_command1=False

        elif read_string == 'QRD 2 4 L':
            print(str(num) + 'dispensing finish but can not get result from Quatos')
            wait_command1 = False
            switch=False
        elif read_string == 'QRD 2 4 12 I 2' or read_string == 'QRD 2 4 12 I 3'or read_string == 'QRD 2 4 12 I 5'or read_string == 'QRD 2 4 12 I 8':
            wait_command1 = False
            switch = False
            print('error on get the result')

        else :
            #print(ser.readline(),type(ser.readline().decode()),'lines',ser.readlines(),type(ser.readlines))
            s=''

            while s!='QRD 2 4 12 A':
                s=ser.readline().decode().strip()
                print(s)
                if 'Content Unit' in s:
                  text_file = open("LiOH.H2O.txt", "a")
                  text_file.writelines('successful times' + str(num)+s+'time'+str(time2-time1)+'\n')
                  text_file.close()

            print('good')

            wait_command1 = False
def moveheadpos(pos):
    global switch, wait_command2
    ser.write(("QRA 60 8 "+str(pos)+'\n').encode("utf-8"))
    print('move_head')

    while wait_command2:
        time.sleep(0.2)
        r = ser.readline().decode()
        read_string = r.strip()
        print(num,read_string)
        if read_string == 'QRA 60 8 B':
            time.sleep(0.2)
        elif read_string == None:
            time.sleep(0.2)

        elif read_string == 'QRA 60 8 A':
            wait_command2 = False

        elif read_string == 'QRA 60 8 L':
            print(str(pos) + 'dispensing finish but can not get go to head pos')
            wait_command2 = False
            switch = False
        elif read_string in ['QRA 60 8 I 1', 'QRA 60 8 I 2', 'QRA 60 8 I 3', 'QRA 60 8 I 4', 'QRA 60 8 I 5',
                             'QRA 60 8 I 8', 'QRA 60 8 I 13']:
            wait_command2 = False
            switch = False
            print(str(pos) + 'dispensing finish but can not get go to head pos')




while switch:
    wait_command = True
    wait_command1 = True
    wait_command2 = True
    num=num+1

    if num>31:
        num=num%30+1

    if num>30:
        switch=False
    moveheadpos(num)
    startdosing()
    getsmapledata()
    print(num)

stopdosing()




