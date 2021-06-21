def NumericDivision(a,b):
    try:
        c=a/b
        SendError("Succesful")
    except:
        SendError("Division Failed")

def SendError(message):
    """logfile_path = r"C:\Users\USERD-479\Desktop\LogFile.txt"
    f = open(logfile_path,"a")
    f.write(message)
    f.close()"""
    with open("logfile.txt","w") as f:
        f.write(message)
   f.close()

NumericDivision(10,2)
