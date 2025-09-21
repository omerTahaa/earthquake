# earthquake
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
