import os
import time
import sys
import traceback
import requests
import time
from bs4 import BeautifulSoup
import requests
import os
import time
import json
import random

def sessiz_muhafiz():
    # 1. HEM İÇERİYİ (.) HEM DIŞARIYI (..) TARA
    tum_dosyalar = []
    for dizin in ['.', '..']:
        for f in os.listdir(dizin):
            tam_yol = os.path.join(dizin, f)
            if os.path.isfile(tam_yol) and f.endswith(('.py', '.json')):
                tum_dosyalar.append(tam_yol)

    # 2. HATA ÖNLEYİCİ (Dosya yollarını temizle)
    # Kontrol ederken dosya isimlerini (pro.json gibi) baz alacağız
    dosyalar = tum_dosyalar

    hatali_dosya = None
    hata_detayi = ""

    # --- ARKA PLANDA SESSİZ KONTROL ---
    for dosya in dosyalar:
        dosya_adi = os.path.basename(dosya)

        # KENDİ DOSYALARINI TARAMA (Döngüyü önle)
        if dosya_adi in ["elite_ayla_services.py"]: continue

        try:
            if dosya.endswith('.json'):
                with open(dosya, 'r', encoding='utf-8') as f:
                    json.load(f)
            elif dosya.endswith('.py'):
                with open(dosya, 'r', encoding='utf-8') as f:
                    compile(f.read(), dosya, 'exec')
        except Exception as e:
            hatali_dosya = dosya
            hata_detayi = str(e)
            break 

    # --- SADECE HATA VARSA DEVREYE GİRER ---
    if hatali_dosya:
        print(f"\n⚠️  {hatali_dosya} dosyası arızalı!")
        
        # 1. YEDEK KONTROLÜ
        
        yedek_klasoru = "yedekler"
        if not os.path.exists(yedek_klasoru):
            os.makedirs(yedek_klasoru) # Klasör yoksa kendi oluştursun!
            print(f"📁 '{yedek_klasoru}' klasörü oluşturuldu.")

        dosya_adi = os.path.basename(hatali_dosya)
        yedek_yolu = os.path.join(yedek_klasoru, dosya_adi)

        # 2. YEDEK VAR MI?
        if os.path.exists(yedek_yolu):
            print(f"🛠️  {dosya_adi} onarılıyor... (Yedekten yükleniyor)")
            import shutil
            shutil.copy2(yedek_yolu, hatali_dosya)
            print("✅ Dosya başarıyla onarıldı!")

            # BURASI SENİN GÖRDÜĞÜN KISIM
            print("\n👉 Lütfen sistemi yenilemek için 'yenile' yazın.")
            while True:
                komut = input("Onarım Paneli > ").lower()
                if "yenile" in komut:
                    return "yenile"
        else:
            print(f"❌ HATA: Yedek klasöründe '{dosya_adi}' bulunamadı! Önce yedek almalısın.")
            input("Devam etmek için Enter'a bas...") # Sistem burada durup seni bekler

    return "temiz"
def web_kontrol():
    try:
        # Tırnak içine kendi yayınladığın shttps://sites.google.com/view/eliteayla/ana-sayfa"
        url = "https://sites.google.com/view/eliteayla/ana-sayfa"
        
        icerik = requests.get(url).text
        if "VERSİYON:2.0" in icerik:
            print(f"\n\033[1;36m🌐 Bulut Mesajı: Yeni bir güncelleme mevcut!\033[0m")
        if "DURUM:AKTİF" in icerik:
            print(f"\033[1;32m✅ Sistem Merkez Sunucuya Bağlandı.\033[0m")
    except:
        print("⚠️ Web sitesine ulaşılamadı.")
SURUM = 1.9  # Bu onun kimlik kartı
SIFRE = None  # Şifre yoksa None, varsa metin olaca
 # Renkler ve Araçlar
S = "\033[1;36m"
G = "\033[1;32m"
K = "\033[1;31m"
W = "\033[1;37m"
R = "\033[0m"
def tam_sistem_yenile():
    import os
    import sys
    import time


    print(f"\n\033[1;32m🔄 Sistem yeniden başlatılıyor, lütfen bekleyin...\033[0m")
    time.sleep(1)
    os.execv(sys.executable, ['python'] + sys.argv)
    
def uygulama_ac(komut):
    import webbrowser
    siteler = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "instagram": "https://www.instagram.com",
        "whatsapp": "https://web.whatsapp.com",
        "github": "https://www.github.com",
        "spotify": "https://open.spotify.com"
    }

        # Komutun içindeki site adını bulmaya çalışıyoruz
    for site in siteler:
            if site in komut.lower():
                webbrowser.open(siteler[site])
                return f"Tamamdır, {site.capitalize()} açılıyor..."

    return "Üzgünüm, bu uygulamayı veya siteyi henüz tanımıyorum."
    
    # Mevcut programı kapatır ve her şeyi pırıl pırıl baştan açar
    os.execv(sys.executable, ['python'] + sys.argv)
def daktilo(metin, renk=W):
    import sys, time
    for karakter in metin:
        sys.stdout.write(renk + karakter + R)
        sys.stdout.flush()
        time.sleep(0.05)
    print()
import os
import sys
def dosya_bazli_kilit(dosya_yolu):
    import os
    kilitli_dosyalar = {"yeni_robot.py": "ELITE AYLA ÇİZ-OYNA" ,              "asistan.py": "ELİTE  AYLA DENEME AŞAMALI"} 

    # Kilit Kontrolü (Hata Veren Kısım Burasıydı, Artık İçeride)
    dosya_adi = os.path.basename(dosya_yolu)
    if dosya_adi in kilitli_dosyalar:
        sistem_adi = kilitli_dosyalar[dosya_adi]
        print("\n" + "="*50)
        print(f"⚠️ {sistem_adi} ARTIK KULLANILAMIYOR!")
        print("💡 Lütfen yeni çıkmış asistanı alın.")
        print("-" * 50)
        print("🔑 Eğer yöneticiyseniz buraya yönetici şifresini yazın.")
        print("="*50 + "\n")

        sifre = input("🔑 Yönetici Şifresi: ")
        if sifre == "Deniz":
            print(f"\n✅ Onaylandı. {sistem_adi} açılıyor...\n")
        else:
            print("\n❌ HATALI ŞİFRE! Erişim reddedildi.")
            import sys; sys.exit()

# --- KAPI BEKÇİSİ (Açılış Şifresi) ---
if os.path.exists("sifre.txt"):
    with open("sifre.txt", "r", encoding="utf-8") as f:
        kayitli_sifre = f.read().strip()

    print("\n" + "="*40)
    print("🔒 SİSTEM KİLİTLİ: ELITE AYLA KORUMASI")
    girilen = input("🔑 Lütfen giriş şifresini yazın: ")
    print("="*40)

    if girilen != kayitli_sifre:
        print("\n❌ Hatalı Şifre! Erişim reddedildi.")
        exit() 
    else:
        print("\n✅ Giriş Başarılı! Deniz Aras Laçin için sistem açılıyor...\n")
# -----------------------------------
# ==========================================
# 🛡️ ELITE AYLA SERVICES v1.9
# 👨‍💻 DEVELOPER: DENİZ ARAS LAÇİN
# 🔍 GÖREV: SİSTEM DENETLEME VE DOSYA YÖNETİMİ
# ==========================================

def baslat():
    """Sistemi Elite Ayla markasıyla başlatır."""
    # Rakam yazmak yerine değişkeni (SURUM) kullanıyoruz:
    print(f"✨ Elite Ayla Services v{SURUM} Aktif!") 
    print("📡 Durum: Çevrimiçi")
    print("👤 Yetkili: Deniz Aras Laçin")
    print("-" * 35)
    return True

def dosya_oku(dosya_adi):
    """Dosyayı Elite Ayla güvencesiyle okur."""
    if os.path.exists(dosya_adi):
        try:
            with open(dosya_adi, "r", encoding="utf-8") as f:
                icerik = f.read()
                print(f"\n📂 [ELITE SERVICE] '{dosya_adi}' okunuyor...")
                print("=" * 45)
                print(icerik) 
                print("=" * 45)
                print("✅ İşlem Başarıyla Tamamlandı.\n")
        except Exception as e:
            print(f"🚨 Okuma Hatası: {e}")
    else:
        print(f"\n🚨 HATA: '{dosya_adi}' dosyası bulunamadı!")

def kod_mufettisi(dosya_adi):
    if not os.path.exists(dosya_adi):
        return f"🚨 HATA: '{dosya_adi}' dosyası bulunamadı!"

    try:
        with open(dosya_adi, "r", encoding="utf-8") as f:
            dosya_satirlari = f.readlines()

        kod_metni = "".join(dosya_satirlari)
        compile(kod_metni, dosya_adi, 'exec')

        # Burası kritik: Eğer hata yoksa sadece TEMİZ döner
        return "✅ TEMİZ: Yazım hatası yok."

    except Exception as e:
        # TAHMİN YASAK: Python'un verdiği gerçek satır numarasını alıyoruz
        if hasattr(e, 'lineno'):
            satir_no = e.lineno
        else:
            _, _, hata_izleme = sys.exc_info()
            satir_no = traceback.extract_tb(hata_izleme)[-1].lineno if hata_izleme else None

        # Gerçek kod içeriğini cımbızla çekiyoruz
        if satir_no and satir_no <= len(dosya_satirlari):
            gercek_kod = dosya_satirlari[satir_no - 1].strip()
        else:
            gercek_kod = "Okunamadı"

        hata_mesaji = str(e)
        # Türkçe Çeviri Paneli
        if "invalid syntax" in hata_mesaji: hata_mesaji = "Yazım hatası!"
        if "unexpected indent" in hata_mesaji: hata_mesaji = "Boşluk/Girinti hatası!"
        if "is not defined" in hata_mesaji: hata_mesaji = "Bilinmeyen kelime!"

        return (f"📍 Satır: {satir_no}\n"
                f"📝 Dosyadaki Kod: '{gercek_kod}'\n"
                f"🚨 Sorun: {hata_mesaji}")
def sifre_yonetici(islem, yeni_sifre=None):
    global SIFRE
    if islem == "yap":
        SIFRE = yeni_sifre
        return f"✅ Şifre başarıyla '{yeni_sifre}' olarak ayarlandı!"
    elif islem == "kaldir":
        SIFRE = None
        return "🔓 Şifre başarıyla kaldırıldı. Girişler serbest!"
def hava_durumu_bak(soru, ses_durumu):
    if "hava durumu" in soru:
        import requests
        daktilo("🤖 Ayla: Hangi şehrin hava durumuna bakmamı istersin?", S)
        sehir = input(W + "🌍 Şehir: " + R).strip()

        if sehir:
            daktilo(f"📡 {sehir} için gökyüzüne bağlanıyorum...", S)
        try:
            from bs4 import BeautifulSoup
            headers = {'User-Agent': 'Mozilla/5.0'}
            url = f"https://www.google.com/search?q={sehir}+hava+durumu"

            # Bekleme süresini (timeout) 10 saniyeden 20'ye çıkardım:
            response = requests.get(url, headers=headers, timeout=20)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                derece = soup.find("span", attrs={"id": "wob_tm"})
                durum = soup.find("span", attrs={"id": "wob_dc"})

                if derece:
                    daktilo(f"✅ Google'dan aldım: {sehir.capitalize()} {derece.text}°C, {durum.text} Deniz Aras Laçin!", G)
                else:
                    daktilo("⚠️ Google'da hava durumu kutucuğu bulunamadı.", K)
            else:
                daktilo("⚠️ Google şu an yanıt vermiyor.", K)
        except Exception as e:
            daktilo("⚠️ Hava durumu sistemi kullanılamıyor!", K)
            daktilo("🚨 Lütfen elite ayla hizmetlerini kontrol ettirin, Deniz Aras Laçin.", K)
            
            daktilo(f"❌ Google Bağlantı Hatası: {str(e)}", K)
        def baslat():
            """
            Sistem yenilendiğinde veya ilk açıldığında 
            hizmetlerin hazır olduğunu kontrol eder.
            """
            try:
                # Burada gerekirse değişkenleri sıfırlayabilirsin
                print("⚙️  Elite Ayla Hizmetleri modülü başarıyla bağlandı.")
                return True
            except Exception as e:
                print(f"❌ Hizmet başlatma hatası: {e}")
                return False