

Strings are immutable means ka inko change nhi kia ja sakta insa sa new bani ja sakti ha jasa ma apko neacha bana ka dakta ho

a="!!!Masroor!!!"
print(a.lower())# is ma sara string lower case ma chala jaya ga 

print(a.upper())#is ma sare string upper case ma chali jaya gi


# Ab yaha bat ati ha strip ke strip means ignore karta ha ya nhi

print(a.rstrip("!"))# rstrip means right side pa jo ham na ignore karwana ha ignore karwa sakta han 
#   leading ko strip nhi karta  tailing ko strip karta ha 
# leading left side and tailing rigth side


REPLACE 

yaha pa kuch is tarha ha ka replace karna pa jo name ya koi bi string ma jo word ham na replace karna ha wo enter karna ha 
us name ka jo word jatna marzi bar aya sabb bar change ho jaya ga agr 10 bar aya ha to 10 bar moezz aya ga

a="Masroor "
print(a)

print(a.replace("Masroor","Moez"))


 Split 

a='Masroor Moez  Abdullaha'# split ka ya hota ha agr ham na space ma koi words likha han string ma to unko braces ya kisi ma bi lakhna ha likh sakta han 
print(a.split(" "))



Capatilize

iska use ya hota ha ka ham na ik sentence likh dia to us ma sara words jaldi jaldi ma chota likh dia to unka first word capital 
likhana ho to ya use karta ha 

bolgheading="intriduction to python"
print(bolgheading.capitalize())



Center method

center method jo ha wo spaces dal data ha jatna ke string ha usko include kar ka baki jo bacha gi spaces dal data

a="Masroor"
print(len(a))
print(len(a.center(50)))



count method

ya count karta ha ka string ma jo word ap dakhna chaho wo katni bar use hoya ha 


a="masroor masroor masroor"
print(a.count("masroor"))



 endswitch

endswitch is lia use hota ha ka ham na ya dakhana hota ha ka koi bi string  ha wo jo ham check kar raha han wo wahi pa end ho rahi ha 

a="Masroor ali !"
print(a.endswith("!")) # yaha pa ho rahi end string ! to ya true da ga warna false



Find method

a="My name is masroor ali"
print(a.find("is"))#yaha pa first occurence ma muja is ka index da da ga find kar ka 

find method ma agr ham na jo chez find ke ha agr wo nhi milti to foran return -1 ho ga


index method

a="my name is masroor ali"
print(a.index("ish"))
ya similar ha find ka is ma farak ya ha ka agr wo word na mila to error aya ga 
ya tab use kara ga jab ham pura sure ho ga ka ya mila ga 



isalnum 

is ma jo marzi use karo true he aya ga number charactrer wagra

a="MYNAMEismasroor007"
print(a.isalnum())


isalpha

agr string ma A to Z,ya a to z , 0 to 9 ho gi sare string tab true 

a="MYNAMEismasroor007"
print(a.isalpha())




islower

agr string ma sara lower case hoya to ya true da ga

a="masroor"
print(a.islower())


isprintable

yaha pa \n ka use ho jo print karna pa nazar nhi ati to ya false da ga 

a="intriduction to pyhton\n"
print(a.isprintable())



isspace 

agr string ma space hoye to true warna false

a="   "
print(a.isspace())


istitle

istitle ka use is tarha ha ka ham na blog wagra banana ha to us ma title upper ma ha to thek warna false

a="Introduction To Python"
print(a.istitle())


startwith


a="introduction to python"
print(a.startswith("introduction"))


swapcase 

lower character ko upper or upper ko lower ma convert kar data ha



title 

ya title ma bana ka lia use hota ha 

a="introduction to python this is my first lecture"

print(a.title())

