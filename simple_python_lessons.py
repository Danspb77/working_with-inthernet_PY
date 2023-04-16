"------------------------------------Browse and parsing--------------------"
from urllib import request, parse
posturl = "https://www.google.com/search?"

"our query zapros"
value = {
    "q": "ANDESA Soft"
}

"create dictionary for header"
header={}

"add header"
header["User-Agent"]="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.5.708 Yowser/2.5 Safari/537.36"

try:
    "query for google"
    mydata = parse.urlencode(value)
    print("zdjsfvnjvz",mydata)

    posturl = posturl + mydata

    "send url and headers together"
    req = request.Request(posturl,headers=header)

    "open page on request"
    answer = request.urlopen(req)
    answer = answer.readlines()
    for line in answer:
        print(line)

except Exception:
    print("Errro occured")
    "print current exception"
    print(sys.exc_info()[1])



"-------------------------------------------DOWNLOAD--------------------------"

from urllib import request
import sys,os

"address of image in Internet"
urladdress="http://adv400.tripod.com/kartinka.jpg"

'way for saving'
myfile="D:\\programming\\mykartin.jpg"
os.remove("mykartin.jpg")

try:
    print("try to download")
    "try to izvlech"
    request.urlretrieve(urladdress,myfile)

except Exception:
    print("stop")
    exit()
print("saved succesfully")



"-----------------------------------INTERNET----------------------------"

from urllib import request, parse
import sys

myurl = "https://www.astahov.net"

"send request to the server"
otvet = request.urlopen(myurl)
print(otvet)

# ans1 = otvet.readline()
#
# print(ans1)

"read the answer from the server"
ans2 = otvet.readlines()
for lines in ans2:
    print(lines)

