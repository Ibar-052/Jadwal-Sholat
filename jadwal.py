import os
try:
   import requests
except ImportError:
   os.system('pip install requests')
   
def keluar():
    cod = input("ingin melanjutkan [y/t] -> ")
    if cod == 't' or cod == 'T':
       os.system("clear")
       exit()
    else:
        if cod == 'y' or cod == 'Y':
           os.system("clear")
           print(banner)
           menu()

banner = """
─╔╗╔══╗╔══╗╔╦═╦╗╔══╗╔╗─╔══╗╔╗╔╗╔═╗╔╗─╔══╗╔══╗
─║║║╔╗║╚╗╗║║║║║║║╔╗║║║─║══╣║╚╝║║║║║║─║╔╗║╚╗╔╝
╔╣║║╠╣║╔╩╝║║║║║║║╠╣║║╚╗╠══║║╔╗║║║║║╚╗║╠╣║─║║─
╚═╝╚╝╚╝╚══╝╚═╩═╝╚╝╚╝╚═╝╚══╝╚╝╚╝╚═╝╚═╝╚╝╚╝─╚╝─
}------------{Author : Ibar052}-------------{
}-------------{Code : Python3}--------------{
}-------{Team : 407 Authentic Exploit}------{
"""
os.system("clear")
print(banner)

def menu():   
    asw = input("Masukkan Nama Kota : ")
    req = requests.get('https://time.siswadi.com/pray/'+asw)
    print("{=================================}")
    print("[1]. Subuh           ->",req.json()["data"]["Fajr"])
    print("[2]. Sunrise         ->",req.json()["data"]["Sunrise"])
    print("[3]. Zuhur           ->",req.json()["data"]["Dhuhr"])
    print("[4]. Asar            ->",req.json()["data"]["Asr"])
    print("[5]. Sunset          ->",req.json()["data"]["Sunset"])
    print("[6]. Maghrib         ->",req.json()["data"]["Maghrib"])
    print("[7]. Isya            ->",req.json()["data"]["Isha"])
    print("[8]. Sepertiga Malam ->",req.json()["data"]["SepertigaMalam"])
    print("[9]. Tengah Malam    ->",req.json()["data"]["TengahMalam"])
    print("[10].Duapertiga Malam->",req.json()["data"]["DuapertigaMalam"])
    print("{=================================}")
    keluar()
    
if __name__ == "__main__":
       menu()