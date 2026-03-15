import sys
import os
import json
import time
from datetime import datetime
from gtts import gTTS
import importlib.util
import sys
import os

# --- 1. EN ÜSTTE MUHAFIZ KONTROLÜ ---
# Hizmetlerin yolu
klasor_adi = "elite_aylahizmetleri.py"
sys.path.append(os.path.join(os.getcwd(), klasor_adi))

try:
    import elite_ayla_services as services
    # Burası hata bulursa zaten o print'leri ekrana basacak
    if services.sessiz_muhafiz() == "yenile":
        os.system(f"python {os.path.basename(__file__)}")
        sys.exit()
except Exception as e:
    # Hizmetler bile yüklenemediyse burası çalışır
    print(f"Hizmetler bulunamadı veya arızalı: {e}")
    sys.exit()

# --- 2. HİZMETLER SAĞLAMSA GERİSİ ÇALIŞIR ---
# Şimdi buraya pro.json'ı okuyan kodlarını yazabilirsin

# --------------------------------
# 1. ÖNCE KİLİT EKRANI
hizmet_yolu = os.path.join(os.getcwd(), "elite_aylahizmetleri.py")
if hizmet_yolu not in sys.path:
    sys.path.append(hizmet_yolu)

try:
    import elite_ayla_services as services
    services.dosya_bazli_kilit(__file__)
except Exception as e:
    print(f"Hata: {e}")


# --- SİSTEM YENİLEME MOTORU ---
def tam_sistem_yenile():
    try:
        # Yenilenecek dosyaların listesi
        dosyalar = ['elite_ayla_services', 'beta']

        for dosya in dosyalar:
            if dosya in sys.modules:
                importlib.reload(sys.modules[dosya])

        return True, "✅ Tüm dosyalar ve hizmetler başarıyla yenilendi."
    except Exception as e:
        return False, f"❌ Yenileme sırasında hata: {e}"


MAIN_SURUM = 1.9

if os.path.exists("sifre.txt"):
    with open("sifre.txt", "r", encoding="utf-8") as f:
        kayitli_sifre = f.read().strip()

    print("\n" + "=" * 30)
    print("🔒 SİSTEM KİLİTLİ")
    girilen = input("🔑 Lütfen giriş şifresini yazın: ")
    print("=" * 30)

    if girilen != kayitli_sifre:
        print("\n❌ Hatalı Şifre! Erişim engellendi.")
        exit()
    else:
        print("\n✅ Giriş Başarılı! Ayla hazırlanıyor...\n")
# -----------------------------------
hizmet_aktif = False
services = None

# Dosyanın tam yolunu gösteriyoruz
dosya_yolu = "elite_aylahizmetleri.py/elite_ayla_services.py"

try:
    # Python'a diyoruz ki: "Bu dosyayı sanki ilk defa görüyormuş gibi baştan oku"
    spec = importlib.util.spec_from_file_location("elite_ayla_services",
                                                  dosya_yolu)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # HATA VARSA TAM BURADA PATLAR!
    services = module

    # --- 🛡️ ÖZEL SÜRÜM BEKÇİSİ ---
    if MAIN_SURUM < services.SURUM:
        # Durum 1: main.py eski
        print("\n[!] ELITE AYLA BAŞLATILAMIYOR...")
        print("👉 Lütfen Elite Ayla hizmetlerini  güncelleyin!\n")
        exit()

    elif services.SURUM < MAIN_SURUM:
        # Durum 2: Hizmetler dosyası eski
        print("\n[!] ELITE AYLA BAŞLATILAMIYOR...")
        print("👉 Lütfen Elite Ayla'yı güncelleyin!\n")
        exit()
    # ----------------------------

    hizmet_aktif = services.baslat()
except Exception as e:
    # Eğer elite_ayla_services.py içinde 1 tane bile parantez eksikse burası çalışır
    print("\n" + "!" * 60)
    print("🚨 GÜVENLİK İHLALİ: Elite Ayla Services KODU ARIZALANDI!")
    print("🛠️  Sistem Deniz Aras Laçin tarafından tamir edilmeyi bekliyor.")
    print(f"🔍 Hata Detayı: {e}")
    print("!" * 60 + "\n")
    hizmet_aktif = False

# --- KLAVYE HATASI ENGEL --- (Senin 8. satırdaki kodun buradan devam edecek)
os.system("")
# --- KLAVYE HATASI ENGEL ---
os.system("")
if sys.platform == "win32":
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), 128)


# ===============================
# PAKET KONTROL
# ===============================
def paket_kur():
    try:
        import requests
        return requests
    except:
        os.system("pip install requests")
        import requests
        return requests


requests = paket_kur()

# ===============================
# AYARLAR
# ===============================
G = "\033[92m"
B = "\033[94m"
S = "\033[93m"
K = "\033[91m"
W = "\033[97m"
R = "\033[0m"

DEV = "Deniz Aras Laçin"
USER_F = "user.json"
KOMUT_F = "komutlar.json"

dusunme_modu = "kısa"
ses_durumu = True


# ===============================
# YAZI EFEKTİ
# ===============================
def daktilo(metin, renk=R):
    if dusunme_modu == "uzun":
        time.sleep(0.6)
    for h in metin:
        sys.stdout.write(renk + h)
        sys.stdout.flush()
        time.sleep(0.03)
    print(R)


def sesli_konus(metin):
    try:
        tts = gTTS(text=metin, lang='tr')
        tts.save("cevap.mp3")
        # Replit'te sesi tarayıcıya iletmek için en güvenli komut budur:
        os.system("play -q cevap.mp3 > /dev/null 2>&1 &"
                  )  # Sonuna eklenen & 'arka planda çal' demektir
    except:
        pass


# ===============================
# JSON YARDIMCI
# ===============================
def yukle(dosya, varsayilan):
    if os.path.exists(dosya):
        try:
            with open(dosya, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return varsayilan
    return varsayilan


def kaydet(dosya, veri):
    with open(dosya, "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=2)


# ===============================
# DEMO TABLO
# ===============================
def tabloya_kaydet(email, pw):
    print(K + ">>> [DEMO] Dış veri gönderimi kapalı." + R)
    return True


# ===============================
# ANA SİSTEM
# ===============================
def baslat():
    global dusunme_modu, ses_durumu
    uykuda = False

    if os.path.exists(USER_F):
        try:
            with open(USER_F, "r", encoding="utf-8") as f:
                veri = json.load(f)
                if "isim" not in veri:
                    os.remove(USER_F)
        except:
            os.remove(USER_F)

    if not os.path.exists(USER_F):
        print(S + "📝 --- SİSTEM KAYIT (DEMO) ---" + R)
        ad = input("👤 Kullanıcı Adı: ").strip()
        tabloya_kaydet(ad, "demo")
        kaydet(USER_F, {"isim": ad})
        print(G + "✅ Kayıt tamamlandı." + R)

    user = yukle(USER_F, {"isim": DEV})
    with open(KOMUT_F, "r", encoding="utf-8") as f:
        komutlar = json.load(f)

    print(W + "=" * 50 + R)
    daktilo("🚀 ELITE AYLA BAŞLATILIYOR...", S)
    print(S + "🔎 Komutlar kontrol ediliyor..." + R)
    print(S + f"📊 {len(komutlar)} komut yüklendi." + R)
    print(G + "✅ Sistem çevrimiçi!" + R)
    # ===============================
    #    ⚠️ SİSTEM BİLDİRİM RAPORU ⚠️
    # ===============================
    print(K + "=" * 50 + R)
    daktilo("🚨 KRİTİK SİSTEM UYARISI...", K)

    print(G + "✅ saat ölçüm bilimi: AKTİF" + R)
    print(G + "✅ Ses Sistemi: AKTİF" + R)
    print(G + "✅ Güncelleme takip istemi: AKTİF" + R)
    print(S + "ℹ️  Sistemler sorunsuz çalışıyor." + R)

    print(B + "\n🚀 v1.9 GÜNCELLEME NOTLARI:" + R)
    print(W + "  » yeniden başlat özelliği geldi." + R)
    print(W + "  » Ses sistemi (Beta) eklendi." + R)
    print(W + "  » Kritik sistem hataları düzeltildi." + R)
    print(W + "  » uygulama açma eklendi." + R)
    print(W + "  » Elite Ayla Hizmetleri başarıyla eklendi." + R)
    print(W + "  » Not sistemi eklendi." + R)
    print(W + "=" * 50 + R)
    while True:
        isim = user.get("isim", DEV)
        soru = input(f"\n{G}👤 {isim}:{R} ").lower().strip()

        if not  soru:
            continue
        if "sistemi yenile" in soru or "dosyaları tazele" in soru:
            import elite_ayla_services as services
            services.tam_sistem_yenile()
            continue

        # --- DİĞER KOMUTLARIN (ŞİFRE, OKU VB.) ---
        if "şifre yap" in soru:
            yeni = input("🛠️ Nasıl bir şifre olsun?: ")
            print(services.sifre_yonetici("yap", yeni))
            continue

        if "şifre kaldır" in soru:
            print(services.sifre_yonetici("kaldir"))
            continue

        if "oku" in soru:
            dosya_adi = soru.replace("oku ", "").strip()

            if not os.path.exists(dosya_adi):
                print(
                    K +
                    f"❓ HATA: '{dosya_adi}' adında bir dosya sistemde bulunamadı!"
                    + R)
            elif hizmet_aktif and services:
                services.dosya_oku(dosya_adi)
            else:
                print( 
                    K +
                    "🚨 HATA: Elite Services arızalı olduğu için dosyalar okunamıyor!"
                    + R)
                print(
                    S +
                    "🛠️  Lütfen önce servisleri Deniz Aras Laçin'e tamir ettirin."
                    + R)
            continue
        if "aç" in soru:
            import elite_ayla_services as services
            mesaj = services.uygulama_ac(soru)
            print(f"{G}{mesaj}{R}")
            continue
        # --- 2. İNCELEME KOMUTU ---
        if "incele" in soru:
            hedef_dosya = soru.replace("incele ", "").strip()

            if not os.path.exists(hedef_dosya):
                print(
                    K +
                    f"❓ HATA: İncelemek istediğiniz '{hedef_dosya}' dosyası mevcut değil!"
                    + R)
            elif hizmet_aktif and services:
                daktilo(
                    f"🧐 {hedef_dosya} dosyası Deniz Aras Laçin için inceleniyor...",
                    B)
                rapor = services.kod_mufettisi(hedef_dosya)

                if "✅ TEMİZ" in rapor:
                    print(
                        G +
                        f" ✨ Müjde! {hedef_dosya} tertemiz, hata bulunamadı." +
                        R)
                else:
                    print(K + "\n" + "!" * 55)
                    print(f" ⚠️  ARIZA TESPİT EDİLDİ!")
                    print(f" 📂 Dosya: {hedef_dosya}")
                    print(f" {rapor}")
                    print("!" * 55 + "\n" + R)
                continue

            print(
                K +
                "🚨 HATA: Elite Services arızalı olduğu için inceleme yapılamıyor!"
                + R)
            continue
        if "sesi kapat" in soru:
            ses_durumu = False
            daktilo("🤖 Ayla: Sesimi kapattım. 🤐", S)
            continue
        # --- NOT YAPMA SİSTEMİ ---
        if soru == "not yap":
            daktilo("🤖 Ayla: Notun başlığı ne olsun?", S)
            baslik = input(W + "📝 Başlık: " + R).strip()

            daktilo("🤖 Ayla: Not içeriğini yazar mısın?", S)
            icerik = input(W + "✍️ İçerik: " + R).strip()

            # Notları yükle, yeni notu ekle ve geri kaydet
            notlar = yukle("notlar.json", {})
            notlar[baslik] = icerik
            kaydet("notlar.json", notlar)

            daktilo(
                f"✅ '{baslik}' başlıklı notun notlar.json dosyasına başarıyla kaydedildi.",
                G)
            continue

        # --- NOT OKUMA SİSTEMİ ---
        if soru == "not oku":
            daktilo("🤖 Ayla: Hangi başlıklı notu okumamı istersin?", S)
            baslik = input(W + "🔍 Başlık Ara: " + R).strip()

            notlar = yukle("notlar.json", {})

            if baslik in notlar:
                # Tek satırda, doğru tırnaklarla yazıyoruz
                cevap = f"{baslik} başlıklı notun içeriği: {notlar[baslik]}"
                daktilo("🤖 Ayla: " + cevap, G)
                if ses_durumu:
                    sesli_konus(cevap)
            else:
                daktilo(
                    f"❌ Üzgünüm Deniz Aras Laçin, '{baslik}' adında bir not bulamadım.",
                    K)
            continue
        if "sesi aç" in soru:
            ses_durumu = True
            daktilo("🤖 Ayla: Sesimi açtım! 🔊", G)
            continue

        if not soru:
            continue

        if soru == "uyku modu":
            uykuda = True
            daktilo("😴 Ayla uyku modunda. 'uyandır' yaz.", S)
            continue

        if uykuda:
            if soru == "uyandır":
                uykuda = False
                daktilo("☀️ Ayla uyandı.", G)
            else:
                daktilo("💤 Uyku modundayım...", S)
            continue

        if soru == "uzun düşün":
            dusunme_modu = "uzun"
            daktilo("🤔 Uzun düşünme aktif.", B)
            continue

        if soru == "kısa düşün":
            dusunme_modu = "kısa"
            daktilo("⚡ Kısa düşünme aktif.", B)
            continue

        if soru == "saat kaç":
            daktilo("🕒 " + datetime.now().strftime("%H:%M:%S"), G)
            continue

        if soru == "tarih ne":
            daktilo("📅 " + datetime.now().strftime("%d.%m.%Y"), G)
            continue
        if soru.startswith("adım") or soru == "adımı değiştir":
            daktilo("🤖 Ayla: Sana nasıl hitap edeyim?", S)
            yeni_ad = input(W + "Yeni Adınız: " + R).strip()
            if yeni_ad:
                user["isim"] = yeni_ad
                kaydet(USER_F, user)
                daktilo(f"✅ Tamamdır {yeni_ad}!", G)
            continue
        if soru in ["çıkış", "cikis", "exit", "kapat"]:
            kaydet(USER_F, user)
            daktilo("👋 Görüşürüz!", K)
            break

        if soru in komutlar:
            cevap = komutlar[soru]
            if ses_durumu:
                sesli_konus(cevap)
            daktilo("🤖 Ayla: " + cevap, W)
            continue

        try:
            raise Exception("GeminiKaldirildi")
        except Exception:
            # Gemini hata verirse veya öğretme modu tetiklenirse burası çalışır
            daktilo(
                "🤖 Ayla: Bunu henüz öğrenemedim. Bana bunu öğretir misin? 🤖",
                W)
            yeni = input(W + "Öğretmek için yazın (veya 'hayır' deyin): " +
                         R).strip().lower()

            if yeni == "hayır" or yeni == "iptal":
                print(K + "❌ İptal edildi." + R)
                daktilo("🤖 Ayla: Peki o zaman, başka bir şey yapalım.", W)
            else:
                # Burası yazdığın şeyi komutlar.json dosyasına kaydeder
                komutlar[soru] = yeni
                with open(KOMUT_F, "w", encoding="utf-8") as f:
                    json.dump(komutlar, f, ensure_ascii=False, indent=4)
                print(G + "✅ Kaydedildi!" + R)
                daktilo(f"🤖 Ayla: Teşekkürler, bunu öğrendim: {yeni}", G)


if __name__ == "__main__":
    # Önce hizmetler dosyasındaki dedektifi çalıştırıyoruz
    from elite_ayla_services import web_kontrol

    print("🔎 Web Sitesi Dedektifi (Elite Ayla) kontrol ediliyor...")
    web_kontrol() # Sitedeki VERSİYON:2.0 yazısını kontrol eder

    # Sonra senin asistanını başlatıyoruz
    baslat()
