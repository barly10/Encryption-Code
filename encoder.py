import os

def char_to_num(char):
    ver=0
    for cah in char:
        ver=ord(cah)
    return ver

def num_to_char(num):
    char=""
    char=chr(num)
    return char

def encrypt(text,key):
    encoded=""
    rerun=0
    for letter in text:
        if rerun==0:
            encoded+=str(char_to_num(letter)+char_to_num(key[rerun%len(key)]))
        else:
            encoded+=" "+str(char_to_num(letter)+char_to_num(key[rerun%len(key)]))
        rerun+=1
    return(encoded)

def decrypt(text,key):
    text_numbs=text.split(" ")
    decoded=""
    rerun=0
    for number in text_numbs:
        decoded+=num_to_char(int(number)-char_to_num(key[rerun%len(key)]))
        rerun+=1
    return(decoded)

def decrypt_data():
    global data, data_code
    read_data()
    password=input("Please input Password:")
    data=eval(decrypt(data_code,password))
    if password==data[1][0]:
        menu()
    else:
        print("Failed")
    
    
def read_data():
    global data_code
    f = open("data.txt", "r")
    data_code=f.readline()
    f.close()
    
def encrypt_data_save():
    global data
    read_txt()
    f= open("data.txt","w+")
    os.remove("txt.txt")
    f.write(encrypt(str(data),data[1][0]))
    f.close()

def read_txt():
    global data
    f = open("txt.txt", "r")
    data[0]=[]
    for line in f:
        data[0].append(line)
    f.close()
    
def write_txt():
    f= open("txt.txt","w+")
    for line in data[0]:
        f.write(line)
    f.close()

def edit_txt():
    write_txt()
    os.startfile("txt.txt")

def view():
    f= open("txt.txt","w+")
    for line in data[0]:
        f.write(line)
    f.close()
    os.startfile("txt.txt")

def menu():
    global recur
    input_1=eval(input("[1]  Edit/View\n[2]  Save & Encrypt\n[3]  Exit\n"))
    if input_1==1:
        edit_txt()
    if input_1==2:
        encrypt_data_save()
    else:
        recur=False
    
#encrypt('[[65,39],["Key of Chiron"]]',"Key of Chiron")

data_code=[]
data=[]

decrypt_data()

recur=True

while(recur==True):
    menu()
while(recur==True):
    menu()
while(recur==True):
    menu()
while(recur==True):
    menu()
while(recur==True):
    menu()
while(recur==True):
    menu()
while(recur==True):
    menu()
