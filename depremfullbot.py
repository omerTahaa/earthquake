import requests
import pandas as pd
import time
import json
import os
import smtplib
from email.message import EmailMessage

KANDILLI_URL = "http://www.koeri.boun.edu.tr/scripts/lst0.asp"
BUYUK_DEPREM_ESIGI = 4.0
DONGU_SURESI_SN = 600

# Telegram bot
TOKEN= "[YOUR_TELEGRAM_TOKEN]"
CHAT_ID = "[YOUR_CHAT_ID]"

# Gmail bot
EMAIL_USER = "[YOUR_EMAIL_ADDRESS]"
EMAIL_PASS = "[YOUR_EMAIL_APP_PASSWORD]"
EMAIL_TO = "[RECIPIENT_EMAIL]"

SEEN_FILE = "seen_ids.json"

def load_seen_ids():
    if not os.path.exists(SEEN_FILE):
        return set()
    try:
        with open(SEEN_FILE, "r", encoding="utf-8") as f:
            return set(json.load(f))
    except Exception:
        return set()

def save_seen_ids(seen):
    try:
        with open(SEEN_FILE, "w", encoding="utf-8") as f:
            json.dump(sorted(list(seen)), f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("seen_ids kaydedilemedi:", e)

def bot_telegram(mesaj):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": mesaj}
    try:
        response = requests.post(url, data=data, timeout=10)
        print("Telegram:", response.json())
        time.sleep(1)
    except Exception as e:
        print("Telegram mesajı gönderilemedi:", e)
        time.sleep(2)

def bot_email(mesaj):
    try:
        msg = EmailMessage()
        msg["From"] = EMAIL_USER
        msg["To"] = EMAIL_TO
        msg["Subject"] = "Deprem Uyarısı"
        msg.set_content(mesaj)

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)
        print("Email gönderildi")
        time.sleep(1)
    except Exception as e:
        print("Email gönderilemedi:", e)
        time.sleep(2)

def fetch_quakes():
    resp = requests.get(KANDILLI_URL, timeout=20)
    resp.encoding = "ISO-8859-9"
    lines = resp.text.splitlines()
    records = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("----------"):
            continue
        if len(line) >= 10 and line[:10].count(".") == 2:
            parts = line.split()
            if len(parts) >= 9:
                deprem_id = f"{parts[0]}_{parts[1]}_{parts[8]}_{parts[6]}"
                records.append([
                    parts[0], parts[1], parts[2], parts[3], parts[4],
                    parts[5], parts[6], parts[7], " ".join(parts[8:10]),
                    deprem_id
                ])
    df = pd.DataFrame(records, columns=["Tarih","Saat","Enlem","Boylam","Derinlik","MD","ML","Mw","Yer","ID"])
    if not df.empty:
        df["ML"] = pd.to_numeric(df["ML"], errors="coerce")
    return df

onceki_depremler = load_seen_ids()

while True:
    try:
        df = fetch_quakes()
        if df.empty:
            print("Deprem verisi alınamadı")
        else:
            buyuk = df[df["ML"] >= BUYUK_DEPREM_ESIGI]
            yeni = buyuk[~buyuk["ID"].isin(onceki_depremler)]

            for _, row in yeni.iterrows():
                ml = row["ML"]
                if 4.0 <= ml < 5.0:
                    mesaj = f"⚠️ Deprem Uyarısı: {row['Tarih']} tarihinde, saat {row['Saat']} civarında  {row['Yer']} merkezli {ml} büyüklüğünde deprem meydana gelmiştir."
                    mesaj = mesaj.replace("İlksel ", "")
                elif 5.0 <= ml < 6.0:
                    mesaj = f"🚨 Önemli Deprem: {row['Tarih']} tarihinde, saat {row['Saat']} civarında  {row['Yer']} merkezli {ml} büyüklüğünde deprem meydana gelmiştir. Dikkatli olunuz!"
                    mesaj = mesaj.replace("İlksel ", "")
                elif 6.0 <= ml < 7.0:
                    mesaj = f"🔥 Büyük Deprem: {row['Tarih']} tarihinde, saat {row['Saat']} civarında  {row['Yer']} merkezli {ml} büyüklüğünde deprem meydana gelmiştir. Lütfen evlere girmeyiniz! Artçı depremlere karşı dikkatli olunuz!"
                    mesaj = mesaj.replace("İlksel ", "")
                elif ml >= 7.0:
                    mesaj = f"💥 Yıkıcı Deprem: {row['Tarih']} tarihinde, saat {row['Saat']} civarında  {row['Yer']} merkezli {ml} büyüklüğünde deprem meydana gelmiştir. Deprem çantanızı yanınıza alarak güvenli bölgelere intikal ediniz!"
                    mesaj = mesaj.replace("İlksel ", "")

                print(mesaj)
                bot_telegram(mesaj)
                bot_email(mesaj)
                onceki_depremler.add(row["ID"])

            save_seen_ids(onceki_depremler)
            df.drop(columns=["ID"]).to_csv("depremler.txt", sep="\t", index=False, encoding="utf-8")
            print("✅ 'depremler.txt' güncellendi!")

    except Exception as e:
        print("Hata:", e)

    print(f"⏳ {int(DONGU_SURESI_SN/60)} dakika sonra tekrar güncellenecek...")
    time.sleep(DONGU_SURESI_SN)

