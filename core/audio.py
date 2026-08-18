






# <POTBO_STAGE S0004>

try:
    pygame.mixer.init()
except pygame.error:
    pass
# </POTBO_STAGE S0004>

# <POTBO_STAGE S0010>

ana_ses = 70
muzik_sesi = 65
efekt_sesi = 70
diyalog_sesi = 80
# </POTBO_STAGE S0010>

# <POTBO_STAGE S0016>



MUSICS = os.path.join(ASSETS, "musics")



LEGACY_MUSICS = os.path.join(BASE_DIR, "musics")
# </POTBO_STAGE S0016>

# <POTBO_STAGE S0032>



MAP_AMBIENCE_SES_ADAYLARI = [

    os.path.join(MUSICS, "mapAmbience.wav"),
    os.path.join(MUSICS, "mapAmbience.ogg"),
    os.path.join(MUSICS, "mapAmbience.mp3"),

    os.path.join(MUSICS, "map_ambience.wav"),
    os.path.join(MUSICS, "map_ambience.ogg"),
    os.path.join(MUSICS, "map_ambience.mp3"),
    os.path.join(MUSICS, "map ambience.wav"),
    os.path.join(MUSICS, "map ambience.ogg"),
    os.path.join(MUSICS, "map ambience.mp3"),
    os.path.join(MUSICS, "ambience.wav"),
    os.path.join(MUSICS, "ambience.ogg"),
    os.path.join(MUSICS, "ambience.mp3"),

    os.path.join(LEGACY_MUSICS, "mapAmbience.wav"),
    os.path.join(LEGACY_MUSICS, "mapAmbience.ogg"),
    os.path.join(LEGACY_MUSICS, "mapAmbience.mp3"),

    os.path.join(ASSETS, "ambience", "mapAmbience.wav"),
    os.path.join(ASSETS, "ambience", "mapAmbience.ogg"),
    os.path.join(ASSETS, "ambience", "mapAmbience.mp3"),
    os.path.join(ASSETS, "ambience", "map_ambience.wav"),
    os.path.join(ASSETS, "ambience", "map ambience.wav"),
    os.path.join(ASSETS, "sounds", "ambience", "mapAmbience.wav"),
    os.path.join(ASSETS, "sounds", "ambience", "mapAmbience.ogg"),
    os.path.join(ASSETS, "sounds", "ambience", "mapAmbience.mp3"),
    os.path.join(ASSETS, "sounds", "mapAmbience.wav"),
    os.path.join(ASSETS, "sounds", "mapAmbience.ogg"),
    os.path.join(ASSETS, "sounds", "mapAmbience.mp3"),
]



GAMEOVER_MUSIC_ADAYLARI = [
    os.path.join(MUSICS, "gameovermusic.wav"),
    os.path.join(MUSICS, "gameovermusic.ogg"),
    os.path.join(MUSICS, "gameovermusic.mp3"),
    os.path.join(MUSICS, "gameOverMusic.wav"),
    os.path.join(MUSICS, "game_over_music.wav"),
    os.path.join(LEGACY_MUSICS, "gameovermusic.wav"),
    os.path.join(LEGACY_MUSICS, "gameovermusic.ogg"),
    os.path.join(LEGACY_MUSICS, "gameovermusic.mp3"),
    os.path.join(ASSETS, "music", "gameovermusic.wav"),
    os.path.join(ASSETS, "music", "gameovermusic.ogg"),
    os.path.join(ASSETS, "music", "gameovermusic.mp3"),
    os.path.join(BASE_DIR, "gameovermusic.wav"),
    os.path.join(BASE_DIR, "gameovermusic.ogg"),
    os.path.join(BASE_DIR, "gameovermusic.mp3"),
]
# </POTBO_STAGE S0032>

# <POTBO_STAGE S0034>
STAB_WITH_ARMOR_SES_ADAYLARI = [
    os.path.join(ASSETS, "sounds", "combat", "stabWithArmor.wav"),
    os.path.join(ASSETS, "sounds", "stabWithArmor.wav"),
    os.path.join(BASE_DIR, "stabWithArmor.wav"),
]
# </POTBO_STAGE S0034>

# <POTBO_STAGE S0040>

NPC_SES_YOLLARI = [
    os.path.join(ASSETS, "sounds", "npc", "npc_01.wav"),
    os.path.join(ASSETS, "sounds", "npc", "npc_02.wav"),
    os.path.join(ASSETS, "sounds", "npc", "npc_03.wav"),
]

OYUN_BASLANGIC_SES_ADAYLARI = [

    os.path.join(ASSETS, "ui", "game_start.wav"),
    os.path.join(ASSETS, "ui", "game_start.mp3"),
    os.path.join(ASSETS, "ui", "game_start.ogg"),

    os.path.join(ASSETS, "sounds", "ui", "game_start.wav"),
    os.path.join(ASSETS, "sounds", "ui", "game_start.mp3"),
    os.path.join(ASSETS, "sounds", "ui", "game_start.ogg"),
]
# </POTBO_STAGE S0040>

# <POTBO_STAGE S0042>


def _ses_dosyasi_anahtarlarla_bul(klasorler, anahtarlar, haric=()):
    """Exact isim yoksa kullanıcı tarafından farklı adlandırılmış sesi bulur.

    Yalnız ses uzantılarını ve verilen klasörleri tarar. Böylece map ambience gibi
    içeriklerde dosyayı illa tek bir isimle yeniden adlandırmak gerekmez.
    """
    uzantilar = {".wav", ".ogg", ".mp3"}
    anahtarlar = tuple(str(x).lower() for x in anahtarlar)
    haric = tuple(str(x).lower() for x in haric)
    adaylar = []
    for klasor in klasorler:
        if not klasor or not os.path.isdir(klasor):
            continue
        try:
            adlar = os.listdir(klasor)
        except OSError:
            continue
        for ad in adlar:
            tam = os.path.join(klasor, ad)
            if not os.path.isfile(tam):
                continue
            kok, ext = os.path.splitext(ad)
            if ext.lower() not in uzantilar:
                continue
            dusuk = kok.lower().replace("_", " ").replace("-", " ")
            if any(x in dusuk for x in haric):
                continue
            skor = sum(1 for x in anahtarlar if x in dusuk)
            if skor > 0:
                adaylar.append((skor, len(ad), tam))
    if not adaylar:
        return None
    adaylar.sort(key=lambda x: (-x[0], x[1], x[2].lower()))
    return adaylar[0][2]


OYUN_BASLANGIC_SES_YOLU = mevcut_ilk_dosya(OYUN_BASLANGIC_SES_ADAYLARI)
# </POTBO_STAGE S0042>

# <POTBO_STAGE S0045>
MAP_AMBIENCE_SES_YOLU = mevcut_ilk_dosya(MAP_AMBIENCE_SES_ADAYLARI)
if MAP_AMBIENCE_SES_YOLU is None:
    MAP_AMBIENCE_SES_YOLU = _ses_dosyasi_anahtarlarla_bul(
        [
            MUSICS,
            LEGACY_MUSICS,
            os.path.join(ASSETS, "ambience"),
            os.path.join(ASSETS, "sounds", "ambience"),
            os.path.join(ASSETS, "sounds"),
        ],
        (
            "ambience",
            "ambient",
            "nature",
            "forest",
            "field",
            "wind",
            "map",
        ),
        haric=("gameover", "game over", "goodbye", "start"),
    )
GAMEOVER_MUSIC_YOLU = mevcut_ilk_dosya(GAMEOVER_MUSIC_ADAYLARI)
if GAMEOVER_MUSIC_YOLU is None:
    GAMEOVER_MUSIC_YOLU = _ses_dosyasi_anahtarlarla_bul(
        [MUSICS, LEGACY_MUSICS, os.path.join(ASSETS, "music")],
        ("gameover", "game over", "death", "dead"),
        haric=("ambience", "ambient"),
    )
STAB_NO_ARMOR_SES_YOLU = mevcut_ilk_dosya(STAB_NO_ARMOR_SES_ADAYLARI)
STAB_WITH_ARMOR_SES_YOLU = mevcut_ilk_dosya(STAB_WITH_ARMOR_SES_ADAYLARI)

GOODBYE_SES_ADAYLARI = [
    os.path.join(ASSETS, "ui", "goodbye_talentless.wav"),
    os.path.join(ASSETS, "ui", "goodbye_talentless.mp3"),
    os.path.join(ASSETS, "ui", "goodbye_talentless.ogg"),
    os.path.join(ASSETS, "sounds", "ui", "goodbye_talentless.wav"),
    os.path.join(ASSETS, "sounds", "ui", "goodbye_talentless.mp3"),
    os.path.join(ASSETS, "sounds", "ui", "goodbye_talentless.ogg"),
]

GOODBYE_SES_YOLU = mevcut_ilk_dosya(GOODBYE_SES_ADAYLARI)

BUTTON_HOVER_SES_ADAYLARI = [
    os.path.join(ASSETS, "ui", "button_hover.wav"),
    os.path.join(ASSETS, "sounds", "ui", "button_hover.wav"),
    os.path.join(ASSETS, "sounds", "button_hover.wav"),
    os.path.join(BASE_DIR, "button_hover.wav"),
]

BUTTON_HOVER_SES_YOLU = mevcut_ilk_dosya(BUTTON_HOVER_SES_ADAYLARI)

BUTTON_HOVER1_SES_ADAYLARI = [
    os.path.join(ASSETS, "ui", "buttonHover1.wav"),
    os.path.join(ASSETS, "sounds", "ui", "buttonHover1.wav"),
    os.path.join(ASSETS, "sounds", "buttonHover1.wav"),
    os.path.join(BASE_DIR, "buttonHover1.wav"),
]
BUTTON_CLICK1_SES_ADAYLARI = [
    os.path.join(ASSETS, "ui", "buttonClick1.wav"),
    os.path.join(ASSETS, "sounds", "ui", "buttonClick1.wav"),
    os.path.join(ASSETS, "sounds", "buttonClick1.wav"),
    os.path.join(BASE_DIR, "buttonClick1.wav"),
]
# </POTBO_STAGE S0045>

# <POTBO_STAGE S0047>
BUTTON_CLICK2_SES_ADAYLARI = [
    os.path.join(ASSETS, "ui", "buttonClick2.wav"),
    os.path.join(ASSETS, "sounds", "ui", "buttonClick2.wav"),
    os.path.join(ASSETS, "sounds", "buttonClick2.wav"),
    os.path.join(BASE_DIR, "buttonClick2.wav"),
]

BUTTON_HOVER1_SES_YOLU = mevcut_ilk_dosya(BUTTON_HOVER1_SES_ADAYLARI)
BUTTON_CLICK1_SES_YOLU = mevcut_ilk_dosya(BUTTON_CLICK1_SES_ADAYLARI)
BUTTON_HOVER2_SES_YOLU = mevcut_ilk_dosya(BUTTON_HOVER2_SES_ADAYLARI)
BUTTON_CLICK2_SES_YOLU = mevcut_ilk_dosya(BUTTON_CLICK2_SES_ADAYLARI)
# </POTBO_STAGE S0047>

# <POTBO_STAGE S0049>
NO_COIN_SES_ADAYLARI = [
    os.path.join(ASSETS, "ui", "noCoinSound.wav"),
    os.path.join(ASSETS, "sounds", "ui", "noCoinSound.wav"),
    os.path.join(ASSETS, "sounds", "noCoinSound.wav"),
    os.path.join(BASE_DIR, "noCoinSound.wav"),
    os.path.join(ASSETS, "ui", "no_coin.wav"),
]
# </POTBO_STAGE S0049>

# <POTBO_STAGE S0051>
NO_COIN_SES_YOLU = mevcut_ilk_dosya(NO_COIN_SES_ADAYLARI)
# </POTBO_STAGE S0051>

# <POTBO_STAGE S0053>

CHARACTER_SELECTED_SES_ADAYLARI = [
    os.path.join(ASSETS, "ui", "characterSelected.wav"),
    os.path.join(ASSETS, "sounds", "ui", "characterSelected.wav"),
    os.path.join(ASSETS, "sounds", "characterSelected.wav"),
    os.path.join(BASE_DIR, "characterSelected.wav"),
]
CHARACTER_SELECTED_SES_YOLU = mevcut_ilk_dosya(CHARACTER_SELECTED_SES_ADAYLARI)

BUTTON_CLICK_SES_ADAYLARI = [
    os.path.join(ASSETS, "ui", "buttonClickSound.wav"),
    os.path.join(ASSETS, "sounds", "ui", "buttonClickSound.wav"),
    os.path.join(ASSETS, "sounds", "buttonClickSound.wav"),
    os.path.join(BASE_DIR, "buttonClickSound.wav"),
    os.path.join(ASSETS, "ui", "button_click.wav"),
]

NEW_ITEM_SES_ADAYLARI = [
    os.path.join(ASSETS, "ui", "newItemSound.wav"),
    os.path.join(ASSETS, "sounds", "ui", "newItemSound.wav"),
    os.path.join(ASSETS, "sounds", "newItemSound.wav"),
    os.path.join(BASE_DIR, "newItemSound.wav"),
    os.path.join(ASSETS, "ui", "new_item.wav"),
]



COIN_PICKUP_SES_ADAYLARI = [
    os.path.join(ASSETS, "ui", "coinPickup.wav"),
    os.path.join(ASSETS, "sounds", "ui", "coinPickup.wav"),
    os.path.join(ASSETS, "sounds", "coinPickup.wav"),
    os.path.join(ASSETS, "sounds", "coin_pickup.wav"),
    os.path.join(ASSETS, "sounds", "coinCollect.wav"),
    os.path.join(ASSETS, "sounds", "coin_collect.wav"),
    os.path.join(ASSETS, "sounds", "coinSound.wav"),
    os.path.join(ASSETS, "sounds", "coin.wav"),
    os.path.join(BASE_DIR, "coinPickup.wav"),
    os.path.join(BASE_DIR, "coin_pickup.wav"),
]
LIQUID_PICKUP_SES_ADAYLARI = [
    os.path.join(ASSETS, "ui", "liquidPickup.wav"),
    os.path.join(ASSETS, "sounds", "ui", "liquidPickup.wav"),
    os.path.join(ASSETS, "sounds", "liquidPickup.wav"),
    os.path.join(ASSETS, "sounds", "liquid_pickup.wav"),
    os.path.join(ASSETS, "sounds", "potionPickup.wav"),
    os.path.join(ASSETS, "sounds", "potion_pickup.wav"),
    os.path.join(ASSETS, "sounds", "liquidSound.wav"),
    os.path.join(ASSETS, "sounds", "liquid.wav"),
    os.path.join(ASSETS, "sounds", "potion.wav"),
    os.path.join(BASE_DIR, "liquidPickup.wav"),
    os.path.join(BASE_DIR, "liquid_pickup.wav"),
]

BUTTON_CLICK_SES_YOLU = mevcut_ilk_dosya(BUTTON_CLICK_SES_ADAYLARI)
NEW_ITEM_SES_YOLU = mevcut_ilk_dosya(NEW_ITEM_SES_ADAYLARI)
COIN_PICKUP_SES_YOLU = mevcut_ilk_dosya(COIN_PICKUP_SES_ADAYLARI)
LIQUID_PICKUP_SES_YOLU = mevcut_ilk_dosya(LIQUID_PICKUP_SES_ADAYLARI)
# </POTBO_STAGE S0053>

# <POTBO_STAGE S0112>
ONEMLI_ITEM_SES_ONCELIK_SURESI = 1000
# </POTBO_STAGE S0112>

# <POTBO_STAGE S0186>



ui_buton_click_baslangic = -10000
# </POTBO_STAGE S0186>

# <POTBO_STAGE S0226>


def ses_yukle(yol):
    if not pygame.mixer.get_init():
        return None

    if not os.path.exists(yol):
        return None

    try:
        return pygame.mixer.Sound(yol)
    except (pygame.error, OSError):
        return None


npc_sesleri = [ses_yukle(yol) for yol in NPC_SES_YOLLARI]

button_hover_sesi = ses_yukle(BUTTON_HOVER_SES_YOLU) if BUTTON_HOVER_SES_YOLU else None
button_click_sesi = ses_yukle(BUTTON_CLICK_SES_YOLU) if BUTTON_CLICK_SES_YOLU else None
button_hover1_sesi = (
    ses_yukle(BUTTON_HOVER1_SES_YOLU) if BUTTON_HOVER1_SES_YOLU else None
)
button_click1_sesi = (
    ses_yukle(BUTTON_CLICK1_SES_YOLU) if BUTTON_CLICK1_SES_YOLU else None
)
button_hover2_sesi = (
    ses_yukle(BUTTON_HOVER2_SES_YOLU) if BUTTON_HOVER2_SES_YOLU else None
)
button_click2_sesi = (
    ses_yukle(BUTTON_CLICK2_SES_YOLU) if BUTTON_CLICK2_SES_YOLU else None
)
# </POTBO_STAGE S0226>

# <POTBO_STAGE S0228>
no_coin_sesi = ses_yukle(NO_COIN_SES_YOLU) if NO_COIN_SES_YOLU else None
# </POTBO_STAGE S0228>

# <POTBO_STAGE S0230>
character_selected_sesi = (
    ses_yukle(CHARACTER_SELECTED_SES_YOLU) if CHARACTER_SELECTED_SES_YOLU else None
)
new_item_sesi = ses_yukle(NEW_ITEM_SES_YOLU) if NEW_ITEM_SES_YOLU else None
coin_pickup_sesi = ses_yukle(COIN_PICKUP_SES_YOLU) if COIN_PICKUP_SES_YOLU else None
liquid_pickup_sesi = (
    ses_yukle(LIQUID_PICKUP_SES_YOLU) if LIQUID_PICKUP_SES_YOLU else None
)
# </POTBO_STAGE S0230>

# <POTBO_STAGE S0233>
map_ambience_sesi = ses_yukle(MAP_AMBIENCE_SES_YOLU) if MAP_AMBIENCE_SES_YOLU else None
gameover_music_sesi = ses_yukle(GAMEOVER_MUSIC_YOLU) if GAMEOVER_MUSIC_YOLU else None



if pygame.mixer.get_init():
    if MAP_AMBIENCE_SES_YOLU is None:
        print("[AUDIO] map ambience bulunamadi.")
        print(
            "[AUDIO] Canonical yol:",
            os.path.join(MUSICS, "mapAmbience.wav"),
        )
        print(
            "[AUDIO] Dosyayi assets/musics klasorune koyabilir veya adinda ambience/nature/forest/wind gecen bir ses dosyasini ayni klasore birakabilirsin."
        )
    elif map_ambience_sesi is None:
        print(
            "[AUDIO] map ambience bulundu ama pygame yukleyemedi:",
            MAP_AMBIENCE_SES_YOLU,
        )
    else:
        debug_log(
            "[AUDIO] map ambience yuklendi:",
            MAP_AMBIENCE_SES_YOLU,
        )

    if GAMEOVER_MUSIC_YOLU is None:
        print(
            "[AUDIO] gameovermusic bulunamadi. Beklenen yol:",
            os.path.join(MUSICS, "gameovermusic.wav"),
        )
    elif gameover_music_sesi is None:
        print(
            "[AUDIO] gameovermusic bulundu ama pygame yukleyemedi:",
            GAMEOVER_MUSIC_YOLU,
        )
    else:
        debug_log(
            "[AUDIO] gameovermusic yuklendi:",
            GAMEOVER_MUSIC_YOLU,
        )
stab_no_armor_sesi = (
    ses_yukle(STAB_NO_ARMOR_SES_YOLU) if STAB_NO_ARMOR_SES_YOLU else None
)
stab_with_armor_sesi = (
    ses_yukle(STAB_WITH_ARMOR_SES_YOLU) if STAB_WITH_ARMOR_SES_YOLU else None
)
# </POTBO_STAGE S0233>

# <POTBO_STAGE S0235>


def npc_ses_seviyesini_guncelle():
    if npc_ses_kanali is None:
        return

    ses_orani = max(0.0, min(1.0, (ana_ses / 100) * (diyalog_sesi / 100)))

    npc_ses_kanali.set_volume(ses_orani)


def ui_ses_seviyesini_guncelle():
    if not pygame.mixer.get_init():
        return

    ses_orani = max(0.0, min(1.0, (ana_ses / 100) * (muzik_sesi / 100)))

    pygame.mixer.music.set_volume(ses_orani)


def goodbye_sesini_oynat():
    """
    Çıkış onayında EVET seçilince goodbye_talentless sesini oynatır.
    """

    if not pygame.mixer.get_init():
        print("UYARI: Pygame mixer başlatılamadı. Goodbye sesi çalınamadı.")
        return False

    if not GOODBYE_SES_YOLU:
        print(
            "UYARI: Goodbye ses dosyası bulunamadı. "
            "assets/sounds/ui/goodbye_talentless.wav yolunu kontrol et."
        )
        return False

    try:
        pygame.mixer.music.stop()

        pygame.mixer.music.load(GOODBYE_SES_YOLU)

        ui_ses_seviyesini_guncelle()

        pygame.mixer.music.play()

        debug_log("Goodbye sesi oynatılıyor:", GOODBYE_SES_YOLU)

        return True

    except (pygame.error, OSError) as hata:
        print("Goodbye sesi yüklenemedi:", GOODBYE_SES_YOLU)
        print("Pygame hatası:", hata)

        return False


def oyun_baslangic_sesini_oynat():
    """
    Açılış sesini WAV, MP3 veya OGG olarak oynatır.
    Dosya bulunamazsa terminale açık hata yazar.
    """

    if not pygame.mixer.get_init():
        print("UYARI: Pygame mixer başlatılamadı. Açılış sesi çalınamadı.")
        return False

    if not OYUN_BASLANGIC_SES_YOLU:
        print(
            "UYARI: Açılış ses dosyası bulunamadı. "
            "Şu klasörü kontrol et: assets/sounds/ui/"
        )
        print("Desteklenen adlar: game_start.wav, game_start.mp3, game_start.ogg")
        return False

    try:
        pygame.mixer.music.stop()

        pygame.mixer.music.load(OYUN_BASLANGIC_SES_YOLU)

        ui_ses_seviyesini_guncelle()

        pygame.mixer.music.play()

        debug_log("Açılış sesi oynatılıyor:", OYUN_BASLANGIC_SES_YOLU)

        return True

    except (pygame.error, OSError) as hata:
        print("Açılış sesi yüklenemedi:", OYUN_BASLANGIC_SES_YOLU)
        print("Pygame hatası:", hata)

        return False


def _efekt_ses_orani():
    return max(0.0, min(1.0, (ana_ses / 100) * (efekt_sesi / 100)))


def _v35_ambience_ses_orani():



    return max(0.0, min(1.0, _efekt_ses_orani() * 0.82))


def _v35_footstep_ses_orani():
    return max(0.0, min(1.0, _efekt_ses_orani() * 0.72))
# </POTBO_STAGE S0235>

# <POTBO_STAGE S0240>


def no_coin_sesi_cal():
    """Yalnız coin eksikliği yüzünden reddedilen satın almalarda çalar.

    Envanter doluluğu, yanlış fiyat veya başka bir hata ekonomik yetersizlik
    değildir; bu ses o durumlarda bilerek kullanılmaz.
    """
    if not pygame.mixer.get_init():
        return
    ses = no_coin_sesi or button_click2_sesi or button_click1_sesi
    if ses is None:
        return
    ses.set_volume(_efekt_ses_orani())
    ses.play()


def character_selected_sesi_cal():
    """Karakter seçimi kesinleştiği anda tek, özel seçim sesini çalar."""
    if character_selected_sesi is None or not pygame.mixer.get_init():
        return
    character_selected_sesi.set_volume(_efekt_ses_orani())
    character_selected_sesi.play()


def new_item_sesi_cal():
    """Yeni eşya kartından tam bir saniye önce başlayan sunum sesini çalar."""
    if new_item_sesi is None or not pygame.mixer.get_init():
        return

    new_item_sesi.set_volume(_efekt_ses_orani())
    new_item_sesi.play()
# </POTBO_STAGE S0240>

# <POTBO_STAGE S0242>


def dunya_pickup_sesi_cal(tur):
    """Yalnız E ile başarıyla alınan dünya ganimetinde doğru toplama sesini çalar."""
    if not pygame.mixer.get_init():
        return
    tur = str(tur).lower().strip()
    if tur == "coin":
        ses = coin_pickup_sesi
    elif tur in ("liquid", "potion", "drink"):
        ses = liquid_pickup_sesi
    else:
        return
    if ses is None:
        return
    ses.set_volume(_efekt_ses_orani())
    ses.play()
# </POTBO_STAGE S0242>

# <POTBO_STAGE S0244>


def secim_sesi_guncelle():
    """Aynı ekran içinde seçim değişmişse hover sesini bir kez çalar."""
    global son_secim_durumu, son_secim_imzasi

    yeni_durum = oyun_durumu
    yeni_imza = secim_imzasi_al()

    if (
        yeni_durum == son_secim_durumu
        and yeni_imza is not None
        and son_secim_imzasi is not None
        and yeni_imza != son_secim_imzasi
        and yeni_imza[0] == son_secim_imzasi[0]
    ):
        button_hover_sesi_cal()

    son_secim_durumu = yeni_durum
    son_secim_imzasi = yeni_imza
# </POTBO_STAGE S0244>

# <POTBO_STAGE S0246>


def npc_sesi_durdur():
    if npc_ses_kanali is not None:
        npc_ses_kanali.stop()


def npc_sesi_oynat(index):
    npc_sesi_durdur()

    if npc_ses_kanali is None:
        return

    if not 0 <= index < len(npc_sesleri):
        return

    ses = npc_sesleri[index]

    if ses is None:
        return

    npc_ses_seviyesini_guncelle()

    npc_ses_kanali.play(ses)
# </POTBO_STAGE S0246>

# <POTBO_STAGE S0332>


def karakter_onay_gecisini_baslat():
    """Seçili kartı kesinleştirir; özel ses + yaklaşık 2.2 saniyelik sinematik fade başlatır."""
    global karakter_onay_gecisi_aktif
    global karakter_onay_gecisi_baslangic

    if karakter_onay_gecisi_aktif:
        return False

    if not yeni_oyun_baslat(loadinge_gec=False):
        return False

    character_selected_sesi_cal()
    karakter_onay_gecisi_aktif = True
    karakter_onay_gecisi_baslangic = pygame.time.get_ticks()
    return True
# </POTBO_STAGE S0332>

# <POTBO_STAGE S0349>


def onemli_item_gosterimini_guncelle():
    """
    Temiz harita görünür olduktan sonra kısa bir stabilizasyon bekler.
    newItemSound bir saniye önce başlar; kart daha sonra açılır. Kartın
    beş saniyelik progress süresi bittiğinde otomatik kapanmaz, tuş bekler.
    """
    global onemli_item_acilis_zamani
    global onemli_item_gosterim_aktif
    global onemli_item_gosterim_hazir_zamani
    global onemli_item_gorsel_hazir_zamani

    if not onemli_item_kuyrugu:
        onemli_item_gosterim_aktif = False
        onemli_item_gosterim_hazir_zamani = 0
        onemli_item_gorsel_hazir_zamani = 0
        return

    simdi = pygame.time.get_ticks()


    if onemli_item_gosterim_aktif:
        return

    if not yeni_item_sahnesi_musait_mi():

        onemli_item_gosterim_hazir_zamani = 0
        onemli_item_gorsel_hazir_zamani = 0
        return



    if onemli_item_gorsel_hazir_zamani > 0:
        if simdi >= onemli_item_gorsel_hazir_zamani:
            onemli_item_gosterim_aktif = True
            onemli_item_gorsel_hazir_zamani = 0
            onemli_item_acilis_zamani = simdi
        return

    if onemli_item_gosterim_hazir_zamani <= 0:
        onemli_item_gosterim_hazir_zamani = simdi + ONEMLI_ITEM_SAHNE_GECIKMESI
        return

    if simdi < onemli_item_gosterim_hazir_zamani:
        return

    onemli_item_gosterim_hazir_zamani = 0
    new_item_sesi_cal()
    onemli_item_gorsel_hazir_zamani = simdi + ONEMLI_ITEM_SES_ONCELIK_SURESI
# </POTBO_STAGE S0349>

# <POTBO_STAGE S0396>


def diyalog_aksiyonlarini_isle():
    global diyalog_index
    global diyalog_secim_index
    global oyun_alt_durumu
    global diyalog_onemli_item_bekliyor

    while 0 <= diyalog_index < len(aktif_diyalog):
        dugum = aktif_diyalog[diyalog_index]

        if not isinstance(dugum, dict):
            diyalog_index += 1
            continue

        if "action" in dugum:
            diyalog_aksiyonunu_uygula(dugum.get("action"))
            diyalog_index += 1

            if diyalog_onemli_item_bekliyor:


                oyun_alt_durumu = HARITA
                return

            continue

        if "choices" in dugum:
            secenekler = dugum.get("choices")

            if not isinstance(secenekler, list) or not secenekler:
                diyalog_index += 1
                continue

            diyalog_secim_index %= len(secenekler)
            oyun_alt_durumu = DIYALOG_SECIM
        else:
            oyun_alt_durumu = DIYALOG

        return

    npc_sesi_durdur()
    oyun_alt_durumu = HARITA
# </POTBO_STAGE S0396>

# <POTBO_STAGE S0471>







def ayar_kategorileri():
    return [
        ("genel", ["language", "autosave"]),
        ("goruntu", ["fullscreen", "brightness", "fps"]),
        ("ses", ["master", "music", "effect", "dialogue"]),
        (
            "oynanis",
            [
                "interaction_prompts",
                "screen_shake",
                "damage_numbers",
            ],
        ),
        (
            "kontroller",
            [
                "bind_move_up",
                "bind_move_down",
                "bind_move_left",
                "bind_move_right",
                "bind_attack",
                "bind_block",
                "bind_dash",
                "bind_interact",
                "bind_inventory",
                "bind_quick_use",
                "bind_q_quick_use",
                "bind_save",
                "bind_pause",
                "bind_reset",
            ],
        ),
        ("erisilebilirlik", ["reduced_motion", "text_speed"]),
    ]


def ayar_kategori_adi(kategori):
    adlar = {
        "genel": bt("GENEL", "GENERAL"),
        "goruntu": bt("GÖRÜNTÜ", "DISPLAY"),
        "ses": bt("SES", "AUDIO"),
        "oynanis": bt("OYNANIŞ", "GAMEPLAY"),
        "kontroller": bt("TUŞ ATAMALARI", "KEY BINDINGS"),
        "erisilebilirlik": bt("ERİŞİLEBİLİRLİK", "ACCESSIBILITY"),
    }
    return adlar[kategori]


def ayar_aciklamasi(ayar):
    aciklamalar = {
        "language": bt(
            "Menü ve oyun metinlerinin dilini belirler.",
            "Sets the language of menus and in-game text.",
        ),
        "autosave": bt(
            "Önemli anlarda otomatik kayıt alır.",
            "Creates automatic saves at important moments.",
        ),
        "interaction_prompts": bt(
            "Yakındaki etkileşimleri tuş simgesiyle gösterir.",
            "Shows nearby interactions with a key icon.",
        ),
        "fullscreen": bt(
            "Oyunu tam ekran veya pencere modunda açar.",
            "Runs the game in fullscreen or windowed mode.",
        ),
        "brightness": bt(
            "Karanlık sahnelerin genel görünürlüğünü ayarlar.",
            "Adjusts the overall visibility of dark scenes.",
        ),
        "fps": bt(
            "Anlık kare hızını köşede gösterir.",
            "Displays the current frame rate in a corner.",
        ),
        "master": bt(
            "Tüm ses kanallarının ana seviyesini değiştirir.",
            "Changes the master level for all audio channels.",
        ),
        "music": bt(
            "Arka plan müziğinin şiddetini ayarlar.",
            "Controls the loudness of background music.",
        ),
        "effect": bt(
            "Savaş ve arayüz efektlerinin şiddetini ayarlar.",
            "Controls combat and interface effect volume.",
        ),
        "dialogue": bt(
            "Konuşma ve karakter seslerini dengeler.",
            "Balances speech and character voice playback.",
        ),
        "screen_shake": bt(
            "Darbe anlarında kameranın tepki vermesini sağlar.",
            "Allows the camera to react to heavy impacts.",
        ),
        "damage_numbers": bt(
            "Hasar ve iyileşme geri bildirimini görünür kılar.",
            "Shows damage and healing feedback values.",
        ),
        "reduced_motion": bt(
            "Kamera ve arayüz hareketlerini azaltır.",
            "Reduces camera and interface motion.",
        ),
        "text_speed": bt(
            "Diyalogların ve metin akışının hızını ayarlar.",
            "Adjusts dialogue and text-flow speed.",
        ),
        "bind_move_up": bt("Yukarı hareket.", "Move upward."),
        "bind_move_down": bt("Aşağı hareket.", "Move downward."),
        "bind_move_left": bt("Sola hareket.", "Move left."),
        "bind_move_right": bt("Sağa hareket.", "Move right."),
        "bind_attack": bt("Temel saldırı.", "Primary attack."),
        "bind_block": bt(
            "Basılı tutarak savunma yapar; stamina hızla tüketir.",
            "Hold to guard; drains stamina quickly.",
        ),
        "bind_dash": bt(
            "Hareket tuşuyla birlikte hızlı kaçış.",
            "Fast evade while held with a movement key.",
        ),
        "bind_interact": bt(
            "Dünya etkileşimi ve bağlamsal arayüz onayı.",
            "World interaction and contextual interface confirm.",
        ),
        "bind_inventory": bt(
            "Envanteri açar veya kapatır.",
            "Opens or closes the inventory.",
        ),
        "bind_quick_use": bt(
            "Seçili 1-5 öne çıkan eşyayı kullanır.",
            "Uses the selected featured item from slots 1-5.",
        ),
        "bind_q_quick_use": bt(
            "Bağımsız Q hızlı slotundaki eşyayı kullanır; büyüler yalnız buradan çalışır.",
            "Uses the independent Q quick slot; spells can only be cast from it.",
        ),
        "bind_save": bt("Manuel kayıt oluşturur.", "Creates a manual save."),
        "bind_pause": bt(
            "Oyun içi duraklatma menüsünü açar.",
            "Opens the in-game pause menu.",
        ),
        "bind_reset": bt(
            "Klavye atamalarını varsayılan düzene döndürür.",
            "Restores the default keyboard layout.",
        ),
        "back": bt(
            "Bir önceki menüye geri döner.",
            "Returns to the previous menu.",
        ),
    }
    return aciklamalar.get(ayar, "")
# </POTBO_STAGE S0471>

# <POTBO_STAGE S0477>


def ayar_sayisal_oran(ayar):
    if ayar == "master":
        return ana_ses / 100
    if ayar == "music":
        return muzik_sesi / 100
    if ayar == "effect":
        return efekt_sesi / 100
    if ayar == "dialogue":
        return diyalog_sesi / 100
    if ayar == "brightness":
        return (parlaklik - 50) / 70
    return None
# </POTBO_STAGE S0477>

# <POTBO_STAGE S0484>


def tus_atama_baslat(ayar):
    global tus_atama_bekleniyor, tus_atama_mesaji, tus_atama_mesaj_bitis
    if not ayar.startswith("bind_") or ayar == "bind_reset":
        return False
    tus_atama_bekleniyor = ayar[5:]
    tus_atama_mesaji = bt("Yeni tuşa bas.", "Press the new key.")
    tus_atama_mesaj_bitis = pygame.time.get_ticks() + 4000
    button_click_sesi_cal("menu1")
    return True
# </POTBO_STAGE S0484>

# <POTBO_STAGE S0486>


def tus_atamalari_varsayilana_don():
    global tus_atamalari, tus_atama_mesaji, tus_atama_mesaj_bitis
    tus_atamalari = dict(VARSAYILAN_TUS_ATAMALARI)
    tus_atama_mesaji = bt(
        "Varsayılan tuşlar geri yüklendi.",
        "Default keys restored.",
    )
    tus_atama_mesaj_bitis = pygame.time.get_ticks() + 1600
    ayarlari_kaydet()
    button_click_sesi_cal("menu1")
# </POTBO_STAGE S0486>

# <POTBO_STAGE S0494>






if OYUN_BASLANGIC_SES_YOLU:
    debug_log("Açılış ses dosyası bulundu:", OYUN_BASLANGIC_SES_YOLU)
else:
    print("Açılış ses dosyası bulunamadı. assets/sounds/ui klasörünü kontrol et.")

if GOODBYE_SES_YOLU:
    debug_log("Goodbye ses dosyası bulundu:", GOODBYE_SES_YOLU)
else:
    print(
        "Goodbye ses dosyası bulunamadı. "
        "assets/sounds/ui/goodbye_talentless.wav yolunu kontrol et."
    )
# </POTBO_STAGE S0494>

# <POTBO_STAGE S0577>






V33_GAMEOVER_MUSIC_STARTED = False


def _v33_gameover_music_tick(menu_alpha):
    global V33_GAMEOVER_MUSIC_STARTED
    if menu_alpha <= 0.0 or not pygame.mixer.get_init() or not GAMEOVER_MUSIC_YOLU:
        return
    try:
        if not V33_GAMEOVER_MUSIC_STARTED:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(GAMEOVER_MUSIC_YOLU)
            pygame.mixer.music.play(-1)
            V33_GAMEOVER_MUSIC_STARTED = True
        base = max(
            0.0,
            min(1.0, (ana_ses / 100.0) * (muzik_sesi / 100.0)),
        )

        gain = 0.16 + 0.84 * max(0.0, min(1.0, float(menu_alpha)))
        pygame.mixer.music.set_volume(base * gain)
    except (pygame.error, OSError):
        V33_GAMEOVER_MUSIC_STARTED = False
# </POTBO_STAGE S0577>

# <POTBO_STAGE S0579>


def _stage3_oyuncu_olum_sahnesini_sifirla():
    global V33_GAMEOVER_MUSIC_STARTED
    if V33_GAMEOVER_MUSIC_STARTED and pygame.mixer.get_init():
        try:
            pygame.mixer.music.stop()
        except pygame.error:
            pass
    V33_GAMEOVER_MUSIC_STARTED = False
    _v32_olum_reset_v33()
# </POTBO_STAGE S0579>

# <POTBO_STAGE S0606>
V34_GAMEOVER_MUSIC_MS = 10000
# </POTBO_STAGE S0606>

# <POTBO_STAGE S0608>
V34_GAMEOVER_MUSIC_STARTED_AT = 0
V34_GAMEOVER_MUSIC_FINISHED = False
# </POTBO_STAGE S0608>

# <POTBO_STAGE S0611>


def oyuncu_olum_menu_fade_orani(simdi=None):
    """V34: bu oran yalnız butonların alpha'sıdır.

    Başlık ayrı timeline'dadır. Böylece YOU ARE DEAD görünürken seçenekler
    erkenden okunmaz; gameovermusic'in 10 saniyelik penceresi bitince gelirler.
    """
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if oyuncu_olum_baslangic_ms <= 0:
        return 0.0
    bas = (
        int(oyuncu_olum_baslangic_ms) + V34_DEATH_TITLE_DELAY_MS + V34_GAMEOVER_MUSIC_MS
    )
    gecen = int(simdi) - bas
    if gecen <= 0:
        return 0.0
    return _v34_smoothstep01(gecen / max(1.0, float(V34_DEATH_BUTTON_FADE_MS)))


def _v34_gameover_music_tick(title_alpha, simdi=None):
    global V34_GAMEOVER_MUSIC_STARTED_AT, V34_GAMEOVER_MUSIC_FINISHED
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if oyuncu_olum_baslangic_ms <= 0 or V34_GAMEOVER_MUSIC_FINISHED:
        return
    if title_alpha <= 0.0:
        return

    if V34_GAMEOVER_MUSIC_STARTED_AT <= 0:
        V34_GAMEOVER_MUSIC_STARTED_AT = int(simdi)
        if pygame.mixer.get_init():
            base = max(
                0.0,
                min(
                    1.0,
                    (ana_ses / 100.0) * (muzik_sesi / 100.0),
                ),
            )
            if gameover_music_kanali is not None and gameover_music_sesi is not None:
                try:
                    gameover_music_kanali.set_volume(base, base)

                    gameover_music_kanali.play(
                        gameover_music_sesi,
                        loops=0,
                        fade_ms=220,
                    )
                except pygame.error:
                    pass
            elif GAMEOVER_MUSIC_YOLU:


                try:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(GAMEOVER_MUSIC_YOLU)
                    pygame.mixer.music.set_volume(base)
                    pygame.mixer.music.play(0, fade_ms=220)
                except (pygame.error, OSError):
                    pass


    if int(simdi) - int(V34_GAMEOVER_MUSIC_STARTED_AT) >= V34_GAMEOVER_MUSIC_MS:
        if gameover_music_kanali is not None:
            try:
                gameover_music_kanali.stop()
            except pygame.error:
                pass

        if gameover_music_sesi is None and pygame.mixer.get_init():
            try:
                pygame.mixer.music.stop()
            except pygame.error:
                pass
        V34_GAMEOVER_MUSIC_FINISHED = True
# </POTBO_STAGE S0611>

# <POTBO_STAGE S0613>


def oyuncu_olum_sahnesini_sifirla():
    global V34_GAMEOVER_MUSIC_STARTED_AT, V34_GAMEOVER_MUSIC_FINISHED
    if gameover_music_kanali is not None:
        try:
            gameover_music_kanali.stop()
        except pygame.error:
            pass
    if gameover_music_sesi is None and pygame.mixer.get_init():
        try:
            pygame.mixer.music.stop()
        except pygame.error:
            pass
    V34_GAMEOVER_MUSIC_STARTED_AT = 0
    V34_GAMEOVER_MUSIC_FINISHED = False
    _v33_olum_reset_v34()
# </POTBO_STAGE S0613>

# <POTBO_STAGE S0724>















V34_SPECIAL_AMBIENCE_DUCK = 0.48
V34_SPECIAL_AMBIENCE_RECOVERY_MS = 280
# </POTBO_STAGE S0724>

# <POTBO_STAGE S0728>

v34_audio_duck_last_active_ms = 0
# </POTBO_STAGE S0728>

# <POTBO_STAGE S0730>


def _v34_special_audio_duck_ratio(simdi):
    global v34_audio_duck_last_active_ms
    if gelistirici_x_skill_aktif_mi(simdi):
        v34_audio_duck_last_active_ms = int(simdi)
        return V34_SPECIAL_AMBIENCE_DUCK
    if v34_audio_duck_last_active_ms <= 0:
        return 1.0
    age = int(simdi) - int(v34_audio_duck_last_active_ms)
    if age >= V34_SPECIAL_AMBIENCE_RECOVERY_MS:
        return 1.0
    t = max(
        0.0,
        min(
            1.0,
            age / max(1.0, float(V34_SPECIAL_AMBIENCE_RECOVERY_MS)),
        ),
    )

    t = t * t * (3.0 - 2.0 * t)
    return V34_SPECIAL_AMBIENCE_DUCK + (1.0 - V34_SPECIAL_AMBIENCE_DUCK) * t


_v34d_map_ambience_guncelle = map_ambience_guncelle


def map_ambience_guncelle():
    _v34d_map_ambience_guncelle()
    if map_ambience_kanali is None or not map_ambience_kanali.get_busy():
        return
    simdi = pygame.time.get_ticks()
    duck = _v34_special_audio_duck_ratio(simdi)
    if duck >= 0.999:
        return
    vol = _v35_ambience_ses_orani() * duck
    try:
        map_ambience_kanali.set_volume(vol, vol)
    except pygame.error:
        pass
# </POTBO_STAGE S0730>

# <POTBO_STAGE S0749>


def oyuncu_etkilesim_yap():
    """En yakın uygun etkileşimi deterministik seçer; release build'de console spam yoktur."""
    global aktif_diyalog, oyun_alt_durumu, v34_interaction_error_count
    if oyun_alt_durumu != HARITA or oyuncu_kontrol_kilitli_mi():
        return False
    target = v34_interaction_target()
    if target is None:
        return False
    try:
        result = target["action"]()
        return True if result is None else bool(result)
    except Exception as exc:
        v34_interaction_error_count += 1
        aktif_diyalog = []
        oyun_alt_durumu = HARITA
        npc_sesi_durdur()
        debug_log(
            "Interaction error:",
            repr(exc),
            "target=",
            target.get("kind"),
        )
        return False
# </POTBO_STAGE S0749>

# <POTBO_STAGE S0867>


_v37_button_click_sesi_cal_original = button_click_sesi_cal
# </POTBO_STAGE S0867>

# <POTBO_STAGE S0869>


def button_click_sesi_cal(tur=None):
    global v37_ui_click_state
    v37_ui_click_state = oyun_durumu
    return _v37_button_click_sesi_cal_original(tur)
# </POTBO_STAGE S0869>

# <POTBO_STAGE S0873>


def v37_pause_action_schedule(index):
    button_click_sesi_cal("menu1")
    idx = int(index)
    return v37_ui_action_schedule(
        lambda idx=idx: _v37_pause_action_execute(idx), "pause"
    )
# </POTBO_STAGE S0873>

# <POTBO_STAGE S0875>


def v37_main_confirm_schedule(index):
    button_click_sesi_cal("menu1")
    idx = int(index)
    return v37_ui_action_schedule(
        lambda idx=idx: _v37_main_confirm_execute(idx),
        "main_confirm",
    )
# </POTBO_STAGE S0875>

# <POTBO_STAGE S0877>


def v37_delete_confirm_schedule(index):
    button_click_sesi_cal("menu1")
    idx = int(index)
    return v37_ui_action_schedule(
        lambda idx=idx: _v37_delete_confirm_execute(idx),
        "delete_confirm",
    )
# </POTBO_STAGE S0877>

# <POTBO_STAGE S0879>


def v37_death_action_schedule(index):
    button_click_sesi_cal("menu1")
    idx = int(index)
    return v37_ui_action_schedule(
        lambda idx=idx: _v37_death_action_execute(idx),
        "death_menu",
    )
# </POTBO_STAGE S0879>

# <POTBO_STAGE S0882>


def v37_settings_back_schedule():
    button_click_sesi_cal("menu1")
    return v37_ui_action_schedule(_v37_settings_back_execute, "settings_back")
# </POTBO_STAGE S0882>

# <POTBO_STAGE S0884>


def v37_quit_confirm_schedule(index):
    button_click_sesi_cal("menu1")
    idx = int(index)
    return v37_ui_action_schedule(
        lambda idx=idx: _v37_quit_confirm_execute(idx),
        "quit_confirm",
    )


def _v37_exit_confirm_execute(index):
    global oyun_durumu
    idx = int(index)
    if idx != 0:
        oyun_durumu = cikis_donus_durumu
        return



    ses_basladi = goodbye_sesini_oynat()
    kapanis_baslangic = pygame.time.get_ticks()
    while True:
        gecen = pygame.time.get_ticks() - kapanis_baslangic
        for kapanis_olayi in pygame.event.get():
            if kapanis_olayi.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit()
        ekran.fill(SIYAH)
        pygame.display.flip()
        saat.tick(FPS)
        if ses_basladi:
            if (not pygame.mixer.music.get_busy() and gecen > 450) or gecen >= 4500:
                break
        elif gecen >= 900:
            break
    pygame.quit()
    raise SystemExit()


def v37_exit_confirm_schedule(index):
    button_click_sesi_cal("menu1")
    idx = int(index)
    return v37_ui_action_schedule(
        lambda idx=idx: _v37_exit_confirm_execute(idx),
        "exit_confirm",
    )
# </POTBO_STAGE S0884>

# <POTBO_STAGE S0977>





def _v38_fire_explosion_init(
    self,
    x,
    y,
    simdi,
    direction=None,
    source_travel=0.0,
    source_origin=None,
    source_temperature=None,
):
    self.x = float(x)
    self.y = float(y)
    self.impact_ms = int(simdi)
    self.detonate_ms = int(simdi)
    self.explosion_start_ms = 0
    self.active = True
    self.detonated = False
    self.sound_played = False
    self.duration_ms = 650
    self.direction = pygame.Vector2(direction or (0.0, 0.0))
    self.hits = []
    self.source_travel = max(0.0, float(source_travel))
    self.source_origin = pygame.Vector2(source_origin or (x, y))
    self.source_temperature = float(source_temperature or V38_FIRE_CORE_TEMPERATURE_K)
    self.is_player_magic = True
# </POTBO_STAGE S0977>

# <POTBO_STAGE S1182>





V46_VERSION = "46.0"
# </POTBO_STAGE S1182>

# <POTBO_STAGE S1590>
V79_GAMEOVER_MUSIC_FINISHED_AT = 0

try:
    _v79_sound_length_ms = (
        int(round(gameover_music_sesi.get_length() * 1000.0))
        if gameover_music_sesi is not None
        else 0
    )
except Exception:
    _v79_sound_length_ms = 0

V79_GAMEOVER_EXPECTED_MS = (
    max(1800, min(18000, _v79_sound_length_ms)) if _v79_sound_length_ms > 0 else 10000
)
# </POTBO_STAGE S1590>

# <POTBO_STAGE S1593>


def _v79_music_is_busy():
    if not pygame.mixer.get_init():
        return False
    if gameover_music_kanali is not None and gameover_music_sesi is not None:
        try:
            return bool(gameover_music_kanali.get_busy())
        except pygame.error:
            return False
    if gameover_music_sesi is None and GAMEOVER_MUSIC_YOLU:
        try:
            return bool(pygame.mixer.music.get_busy())
        except pygame.error:
            return False
    return False


def _v34_gameover_music_tick(title_alpha, simdi=None):
    global V34_GAMEOVER_MUSIC_STARTED_AT, V34_GAMEOVER_MUSIC_FINISHED
    global V79_GAMEOVER_MUSIC_FINISHED_AT
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if oyuncu_olum_baslangic_ms <= 0:
        return
    if title_alpha <= 0.0 and V34_GAMEOVER_MUSIC_STARTED_AT <= 0:
        return

    if V34_GAMEOVER_MUSIC_STARTED_AT <= 0:
        V34_GAMEOVER_MUSIC_STARTED_AT = int(simdi)
        V34_GAMEOVER_MUSIC_FINISHED = False
        V79_GAMEOVER_MUSIC_FINISHED_AT = 0
        if pygame.mixer.get_init():
            base = max(
                0.0,
                min(
                    1.0,
                    (ana_ses / 100.0) * (muzik_sesi / 100.0),
                ),
            )
            if gameover_music_kanali is not None and gameover_music_sesi is not None:
                try:
                    gameover_music_kanali.set_volume(base, base)
                    gameover_music_kanali.play(
                        gameover_music_sesi,
                        loops=0,
                        fade_ms=650,
                    )
                except pygame.error:
                    pass
            elif GAMEOVER_MUSIC_YOLU:
                try:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(GAMEOVER_MUSIC_YOLU)
                    pygame.mixer.music.set_volume(base)
                    pygame.mixer.music.play(0, fade_ms=650)
                except (pygame.error, OSError):
                    pass

    if V34_GAMEOVER_MUSIC_FINISHED:
        return

    elapsed = int(simdi) - int(V34_GAMEOVER_MUSIC_STARTED_AT)

    natural_end = elapsed >= 900 and not _v79_music_is_busy()
    safety_end = elapsed >= int(V79_GAMEOVER_EXPECTED_MS) + 250
    if natural_end or safety_end:
        V34_GAMEOVER_MUSIC_FINISHED = True
        V79_GAMEOVER_MUSIC_FINISHED_AT = int(simdi)
        if gameover_music_kanali is not None:
            try:
                gameover_music_kanali.stop()
            except pygame.error:
                pass
        if gameover_music_sesi is None and pygame.mixer.get_init():
            try:
                pygame.mixer.music.stop()
            except pygame.error:
                pass


def oyuncu_olum_menu_fade_orani(simdi=None):
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if oyuncu_olum_baslangic_ms <= 0:
        return 0.0


    if V34_GAMEOVER_MUSIC_STARTED_AT <= 0:
        return 0.0

    if V79_GAMEOVER_MUSIC_FINISHED_AT > 0:
        start = int(V79_GAMEOVER_MUSIC_FINISHED_AT)
    elif V34_GAMEOVER_MUSIC_FINISHED:
        start = int(simdi)
    else:

        expected_end = int(V34_GAMEOVER_MUSIC_STARTED_AT) + int(
            V79_GAMEOVER_EXPECTED_MS
        )
        if int(simdi) < expected_end:
            return 0.0
        start = expected_end

    return _v79_smootherstep(
        (int(simdi) - start) / max(1.0, float(V79_DEATH_MENU_FADE_MS))
    )
# </POTBO_STAGE S1593>

# <POTBO_STAGE S1596>


def oyuncu_olum_sahnesini_sifirla():
    global V79_GAMEOVER_MUSIC_FINISHED_AT
    V79_GAMEOVER_MUSIC_FINISHED_AT = 0
    _v79_title_cache.clear()
    _v79_scene_reset_original()
# </POTBO_STAGE S1596>

# <POTBO_STAGE S1604>


def v79_diagnostics():
    return {
        "version": V79_VERSION,
        "hud_runtime_names_fixed": True,
        "ui_press_ms": V79_UI_PRESS_MS,
        "ui_action_delay_ms": V79_UI_ACTION_DELAY_MS,
        "player_walk_speed": OYUNCU_YURUYUS_HIZI,
        "dash_ms": DASH_SURESI_MS,
        "death_title_fade_ms": V79_DEATH_TITLE_FADE_MS,
        "gameover_expected_ms": V79_GAMEOVER_EXPECTED_MS,
        "death_menu_after_music": True,
        "death_palette_dither_fade": True,
    }
# </POTBO_STAGE S1604>

# <POTBO_STAGE S1868>


def v85_death_menu_draw(now):


    _v79_draw_death_title(now)
    menu_progress = oyuncu_olum_menu_fade_orani(now)
    if menu_progress <= 0.0:
        return
    menu = _v79_death_menu_content(now)
    position = (GENISLIK // 2 - menu.get_width() // 2, 400)
    _v79_dither_blit(menu, position, menu_progress)
# </POTBO_STAGE S1868>

# <POTBO_STAGE S1937>


def oyuncu_olum_durumu_guncelle():
    global oyuncu_olum_turu
    if not v86_death_state.active:
        return _v86_death_tick_original()


    saved_type = oyuncu_olum_turu
    oyuncu_olum_turu = "v86_authored"
    try:
        result = _v86_death_tick_original()
    finally:
        oyuncu_olum_turu = saved_type
    v86_death_update(pygame.time.get_ticks())
    return result
# </POTBO_STAGE S1937>

# <POTBO_STAGE S2476>


_v100_active_button_sound_base = aktif_buton_ses_turu
# </POTBO_STAGE S2476>

