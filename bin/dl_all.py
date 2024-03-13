import requests
import time
import os


base_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir ))
kt_file = os.path.join(base_dir,"tmp","kennitolur.txt")
output_dir = os.path.join(base_dir,"tmp","results")


kts = open(kt_file).read()
kts = kts.strip()
kts = kts.split("\n")



def dl_info(kt):

    url = "https://her.reykjavik.is/?q={KT}&o=name&pnr="

    url = url.replace("{KT}",kt)


    file_name = os.path.join(output_dir,kt + ".html")

    try:
        response = requests.request("GET",url,timeout=3) 
        data = response.text

        f = open(file_name,"w")
        f.write(data)
        f.close()
    except requests.exceptions.Timeout:
        print("\n TIMEOUT: " + kt + "\n")



tc = len(kts)

offset = 0
pcount = 0
cprint = 50
c = offset + 1


for kt in kts[offset:]:


    c += 1
    pcount += 1

    if pcount == cprint: 
        print()
        print( str(c) + "/" + str(tc))
        pcount = 0
    else:
        print(".",end="",flush=True)
        

    dl_info(kt)
    time.sleep(1)
    


