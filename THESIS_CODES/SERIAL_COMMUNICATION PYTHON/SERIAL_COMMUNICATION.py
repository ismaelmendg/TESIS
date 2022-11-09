import serial

def sendID(Trigg):

    global TEMP
    TEMP = str(Trigg)

def SERIAL():
    arduino_port = ("COM7")
    baud = 115200 #arduino uno runs at 9600 baud
    print("Nombre del archivo")
    archivo = input()
    fileName= archivo + ".csv" #name of the CSV file generated

    ser = serial.Serial(arduino_port, baud)
    print("Connected to Arduino port:" + arduino_port)
    # file = open(fileName, "a")
    print("Created file")

    #display the data to the terminal
    getData=str(ser.readline())
    data=getData[0:][:-2]
    print(data)

    #add the data to the file
    file = open(fileName, "a") #append the data to the file
    file.write(data + "\\n") #write data with a newline

    #close out the file
    file.close()

    samples = 10 #how many samples to collect
    print_labels = False
    line = 0 #start at 0 because our header is 0 (not real data)
    while line <= samples:
        # incoming = ser.read(9999)
        # if len(incoming) > 0:
        if print_labels:
            if line==0:
                print("Printing Column Headers")
            else:
                print("Line " + str(line) + ": writing...")

        getData=str(ser.readline())
        sendID(',14')
        x = 0
        data=getData[2:][:-6] + TEMP
        print(data)

        file = open(fileName, "a")
        file.write(data + "\n") #write data with a newline
        # file.write( Trigg + "\n")
        line = line+1

    print("Data collection complete!")
    file.close()

if __name__ == '__main__':
    SERIAL()