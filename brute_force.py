
import time
import zipfile
folderPath = input("path to the file")
zipf = zipfile.ZipFile(folderPath)

if not zipf:
    print("folder is not password protected")

else:
    startTime = time.time()
    result = 0
    c = 0

characters = ['0','1','2','3','4','5','6','7','8','9',
                 'a','b','c','d','e','f','g','h','i','j','l','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','p','Q','R','S','T','U','V','W','X','Y','Z',
                 '!','@','#','$','%','=',':','?','.','/','|','~','>','*','(',')','<','}','{','^','[',']',' ','+','-','_','&',';','"','?','`',"'",'\\']


print("Brute force started..")

if(result == 0):
    print("checking for four character password")

    for i in characters:
        for j in characters:
            for k in characters:
                for l in characters:
                    guess = str(i) + str(j) + str(k) + str(l)
                    password = guess.encode("utf-8").strip()
                    c= c + 1
                    try:
                        with zipfile.ZipFile(folderPath,"r") as zf:
                            zf.extractall(pwd = password)
                            print("success,the password is : " + guess)
                            endtime = time.time()
                            result = 1
                            break
                    except:
                        pass
                if result == 1:
                    break
            if result == 1:
                break
        if result ==1:
            break

if (result == 0):
    print("sorry pasword not found")

else:
    duration = endtime - startTime
    print('Congratulations!!! Password found after trying '+str(c)+' combinations in '+str(duration)+' seconds')



    



            


