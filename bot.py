import requests
import shutil
import os
import json
url="https://tools.zone-xsec.com/api/nulis.php?q="
logo="""
╲╲╲╲╲┏━━━┓╱╱╱╱╱
╲┏━━━┻━━━┻━━━┓╱         Bot Nulis
╲┃╭━╮┏━━━┓╭━╮┃╱   =====================
╱┃┃╳┃┣◯-◯┫┃╳┃┃╲
╱┃╰━╯┣━━━┫╰━╯┃╲   Author : Tegar Sabila
╱┃┈▊▊▊▊┈▂▃▅▇┈┃╲   Versi  : 0.01
╱┗━━━━━━━━━━━┛╲
"""

def biasa():
    tulis=input("masukan tulisan: ")
    req=requests.get(url+tulis)
    jeson=json.loads(req.text)
    link=jeson['image']
    image_url= link
    nama_file = image_url.split("/")[-1]
    r = requests.get(image_url, stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(nama_file,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            print('Berhasil, nama file:',nama_file)
    else:
        print('Terjadi Kesalahan')

def file():
    tulis=input("nama file: ")
    try:
        file=open(tulis, "r").read()
    except IOError:
        print("file tidak ada")
    ubah=file.replace(" ", "%20")
    cek=ubah.replace("\n", "%0A")
    req=requests.get(url+cek)
    jeson=json.loads(req.text)
    link=jeson['image']
    image_url= link
    nama_file = image_url.split("/")[-1]
    r = requests.get(image_url, stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(nama_file,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            print('Berhasil, nama file:',nama_file)
    else:
        print('Terjadi Kesalahan')

if __name__=="__main__":
    os.system("clear")
    print(logo)
    print("1. Tulis Biasa")
    print("2. Tulis Lewat File")
    print("0. Kembali")
    pil=input("Metode => ")
    if pil == "1":
        biasa()
    elif pil == "2":
        file()
    else:
        print(pil, "tidak ada")