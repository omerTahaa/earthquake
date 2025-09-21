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


# Earthquake Alert Bot  

This project monitors earthquake data published by Kandilli Observatory and sends alerts via **Telegram** or **Email** when an earthquake above a certain magnitude occurs.  

The goal is to automatically notify users about earthquakes with magnitude 4.0 and above.  

---

## Features  

- Fetches live earthquake data from Kandilli Observatory  
- Different alert messages for magnitudes: 4.0–5.0, 5.0–6.0, 6.0–7.0, and 7.0+  
- Sends notifications through a **Telegram bot**  
- Optional support for **Email alerts**  
- Saves all earthquake data into a `depremler.txt` file  

---

## Requirements  

You need to install the following dependencies:  

```bash
pip install requests pandas
```

If you want to enable email alerts as well:  

```bash
pip install secure-smtplib
```

Python 3.10 or later is recommended.  

---

## Telegram Bot Setup  

1. Talk to [@BotFather](https://t.me/botfather) on Telegram and create a new bot.  
2. Copy the **bot token** provided to you.  
3. Get your own user ID by messaging [@userinfobot](https://t.me/userinfobot).  
4. Replace the `token` and `chat_id` values in the code with your own.  

For more details, check the official tutorial:  
👉 [How to Create a Telegram Bot](https://core.telegram.org/bots/tutorial)  

---

## Email Notification Setup (Optional)  

To enable email alerts, you need to enable **IMAP access** in Gmail and create an **App Password**.  

- Two-factor authentication must be enabled.  
- Go to your Google account, generate an "App Password," and copy it.  
- Replace the `EMAIL_ADDRESS` and `APP_PASSWORD` values in the code with your own.  

For more details, this guide might help:  
👉 [Sending Email with Python and Gmail](https://realpython.com/python-send-email/)  

---

## Usage  

After downloading the project, you can run it from your terminal:  

```bash
python depremfullbot.py
```

The bot will continuously run in the background, monitoring for new earthquakes and sending alerts.  

---

## Contribution  

Feel free to contribute by improving the code or creating pull requests. Possible improvements include better error handling, logging, or adding support for other platforms (e.g., Discord, Slack).  

---

## Disclaimer  

This project is for **informational purposes only**. It is not an official warning system. For official earthquake safety and warnings, always follow AFAD and Kandilli Observatory announcements.  
