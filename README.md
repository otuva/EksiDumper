# EksiDumper

TR - Verilen kullaniciya ait entryleri csv dosyasina dump edin, arsivleyin. Data-set olusturmak ya da yedek almak icin ideal.

EN - Dump, archive all entries to a csv file for given username. Ideal for creating data-sets or backups.

---

     ______ _        _ _____                                  
    |  ____| |      (_)  __ \                                 
    | |__  | | _____ _| |  | |_   _ _ __ ___  _ __   ___ _ __ 
    |  __| | |/ / __| | |  | | | | | '_ ` _ \| '_ \ / _ \ '__|
    | |____|   <\__ \ | |__| | |_| | | | | | | |_) |  __/ |   
    |______|_|\_\___/_|_____/ \__,_|_| |_| |_| .__/ \___|_|   
                                             | |              
                                             |_|              

---

[Turkce](https://github.com/otuva/EksiDumper#tr)

[English](https://github.com/otuva/EksiDumper#en)

---

# TR

- [x] Verilen kullanicinin tum entrylerini aktarabilir.
- [ ] Verilen basliktaki tum entryleri aktarabilir.

### Kullanimi

0- Ana klasore gelin.

1- Gereklilikleri yukleyin. Size bagli olarak `pip` yerine `pip3` yazmak zorunda olabilirsiniz.

    pip install -r requirements.txt

2- Komut satirindan scripti, ilk argumani kullanici adi olacak sekilde baslatin. Eger kullanici adi birden cok kelimeden olusuyorsa bosluk yerine `-` karakteri kullanin.

    python3 main.py <KULLANICIADI>
    python3 main.py foo
ya da

    python3 main.py <COK-KELIMELI-KULLANICI-ADI> 
    python3 main.py foo-bar

3- Scriptin bitmesini bekleyin. Dosyalar `dumps` klasoru altinda olacaktir.


Bilgisayariniza ve internetinize bagli olmakla birlikte, script yaklasik olarak 120 entry/dakika hizinda calisir.

Ornek ciktilar icin [dumps klasorune](https://github.com/otuva/EksiDumper/tree/main/dumps) ya da [resimlere](https://github.com/otuva/EksiDumper#imgs) bakabilirsiniz.

### Katkida bulunmak icin

1- Repo'yu forklayin.

2- Gelistirin.

3- Pull request olusturun.

---

# EN

- [x] Can dump entries for a given user
- [ ] Can dump entries for a given topic

### Usage

0- Navigate to base folder.

1- Install requirements. Note that you might need to use `pip3` instead of `pip`

    pip -r requirements.txt

2- Start main script from command line. With the username as the first argument. If username contains multiple words, use `-` instead of space.

    python3 main.py <USERNAME>
    python3 main.py foo
or

    python3 main.py <USER-NAME-WITH-WORDS> 
    python3 main.py foo-bar

3- Wait for script to finish. The files will be under `dumps` directory.


Depending on your computer and network, the script usually takes about 120 entries/minute.

For example outputs, you can check [dumps directory](https://github.com/otuva/EksiDumper/tree/main/dumps) or [images](https://github.com/otuva/EksiDumper#imgs).


### Contributing

1- Fork the repository.

2- Develop.

3- Create a pull request.

---


## IMGs

![1](https://github.com/otuva/EksiDumper/blob/main/img/1.png)

![2](https://github.com/otuva/EksiDumper/blob/main/img/2.png)

![3](https://github.com/otuva/EksiDumper/blob/main/img/3.png)
