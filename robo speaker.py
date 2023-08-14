import  os
if __name__=='__main__':
    print("welcome to robo speaker1.1:created bu bilal")
    while True:
     x=input("say what u want to hear")
     if x=="q":
        os.system("say good byefriend")
        break
    command=f"say{x}"
 os.system('command')
