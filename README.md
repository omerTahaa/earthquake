# Earthquake
Türkiye'de meydana gelen depremleri telegram ve e-mail üzerinden bildirir. / This software announces the earthquakes that happens in Turkey via Telegram and e-mail

# Deprem Uyarı Botu  

Bu proje, Kandilli Rasathanesi’nin yayınladığı deprem verilerini takip ederek belli büyüklükteki depremleri **Telegram** veya **E-posta** yoluyla bildirim olarak iletir.  

Amaç, 4.0 ve üzerindeki depremleri otomatik şekilde kullanıcıya haber vermektir.  

---

## Özellikler  

- Kandilli Rasathanesi’nden anlık veri çekme  
- 4.0–5.0, 5.0–6.0, 6.0–7.0 ve 7.0+ depremler için farklı uyarı mesajları  
- Bildirimleri **Telegram botu** üzerinden gönderme  
- İsteğe bağlı olarak **E-posta bildirimi** desteği  
- Tüm veriler `depremler.txt` dosyasına kaydedilir  

---

## Gereksinimler  

Projeyi çalıştırmak için şunları yüklemeniz gerekiyor:  

```bash
pip install requests pandas
```

Eğer e-posta özelliğini de kullanacaksanız:  

```bash
pip install secure-smtplib
```

Python 3.10 ve üzeri tavsiye edilir.  

---

## Telegram Bot Kurulumu  

1. Telegram’da [@BotFather](https://t.me/botfather) ile konuşarak yeni bir bot oluşturun.  
2. Size verilen **bot token**’ı alın.  
3. Kendi kullanıcı ID’nizi öğrenmek için [@userinfobot](https://t.me/userinfobot) botuna yazın.  
4. Kodun içindeki `token` ve `chat_id` kısımlarını kendi bilgilerinizle değiştirin.  

Detaylı anlatım için şu kaynak işinize yarayabilir:  
👉 [Telegram Bot Nasıl Yapılır?](https://core.telegram.org/bots/tutorial)  

---

## E-Posta Bildirim Kurulumu (Opsiyonel)  

E-posta gönderebilmek için Gmail ayarlarından **IMAP erişimini açmanız** ve **Uygulama Şifresi** oluşturmanız gerekiyor.  

- 2 adımlı doğrulamanız aktif olmalı.  
- Google hesabınızdan “Uygulama Şifreleri” kısmına girip yeni bir şifre alın.  
- Kodda `EMAIL_ADDRESS` ve `APP_PASSWORD` kısımlarını kendi bilgilerinizle değiştirin.  

Detaylı bilgi için şu makale işinize yarar:  
👉 [Gmail ile Python’dan Mail Göndermek](https://realpython.com/python-send-email/)  

---

## Kullanım  

Projeyi indirdikten sonra terminalden çalıştırabilirsiniz:  

```bash
python depremfullbot.py
```

Bot arka planda sürekli çalışarak yeni depremleri kontrol eder ve bildirim gönderir.  

---

## Katkı  

İsteyenler kodu geliştirip pull request açabilir. Daha iyi hata yakalama, loglama veya farklı platformlara bildirim eklenebilir (ör. Discord, Slack).  

---

## Not  

Bu proje sadece bilgilendirme amaçlıdır. Resmî bir uyarı sistemi yerine geçmez. Deprem güvenliği için her zaman AFAD ve Kandilli’nin resmî duyurularını takip ediniz.  


Earthquake Alert Bot
This project monitors earthquake data published by the Kandilli Observatory and sends notifications via Telegram or email for earthquakes of a certain magnitude.

The goal is to automatically notify users of earthquakes measuring 4.0 and above.

Features
Pulls real-time data from the Kandilli Observatory
Different alert messages for earthquakes of 4.0–5.0, 5.0–6.0, 6.0–7.0, and 7.0+ magnitude
Sends notifications via a Telegram bot
Optional email notification support
All data is saved to the earthquakes.txt file
Requirements
To run the project, you need to install the following:

pip install requests pandas
If you also want to use the email feature:

pip install secure-smtplib
Python 3.10 and above is recommended.

Telegram Bot Setup
Create a new bot by chatting with @BotFather on Telegram.
Get the bot token provided to you.
To find out your own user ID, write to the @userinfobot bot.
Replace the token and chat_id parts in the code with your own information.
The following resource may be useful for a detailed explanation:
👉 How to Create a Telegram Bot?

Email Notification Setup (Optional)
To send emails, you need to enable IMAP access in your Gmail settings and create an App Password.

Your 2-step verification must be active.
Go to “App Passwords” in your Google account and get a new password.
Replace the EMAIL_ADDRESS and APP_PASSWORD sections in the code with your own information.
For more details, this article may be helpful:
👉 Sending Mail from Python with Gmail

Usage
After downloading the project, you can run it from the terminal:

python depremfullbot.py
The bot runs continuously in the background, checks for new earthquakes, and sends notifications.

Contributions
Those who wish can improve the code and open a pull request. Better error handling, logging, or notifications for different platforms (e.g., Discord, Slack) can be added.

Note
This project is for informational purposes only. It does not replace an official warning system. For earthquake safety, always follow the official announcements from AFAD and Kandilli.

Translated with DeepL.com (free version)
