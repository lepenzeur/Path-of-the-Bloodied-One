






# <POTBO_STAGE S0028>

MERCHANT_MEDOLI_YOLU = os.path.join(ASSETS, "npcs", "merchant_medoli.png")

MERCHANT_VERI_YOLU = os.path.join(BASE_DIR, "data", "merchant_medoli.json")
# </POTBO_STAGE S0028>

# <POTBO_STAGE S0046>

BUTTON_HOVER2_SES_ADAYLARI = [
    os.path.join(ASSETS, "ui", "buttonHover2.wav"),
    os.path.join(ASSETS, "sounds", "ui", "buttonHover2.wav"),
    os.path.join(ASSETS, "sounds", "buttonHover2.wav"),
    os.path.join(BASE_DIR, "buttonHover2.wav"),
]
# </POTBO_STAGE S0046>

# <POTBO_STAGE S0048>









MERCHANT_BUY_SES_ADAYLARI = [
    os.path.join(ASSETS, "ui", "buySound.wav"),
    os.path.join(ASSETS, "sounds", "ui", "buySound.wav"),
    os.path.join(ASSETS, "sounds", "buySound.wav"),
    os.path.join(BASE_DIR, "buySound.wav"),
    os.path.join(ASSETS, "ui", "merchantBuy.wav"),
    os.path.join(ASSETS, "sounds", "ui", "merchantBuy.wav"),
    os.path.join(ASSETS, "sounds", "merchantBuy.wav"),
    os.path.join(ASSETS, "ui", "merchant_buy.wav"),
    os.path.join(BASE_DIR, "merchantBuy.wav"),
]
MERCHANT_SELL_SES_ADAYLARI = [
    os.path.join(ASSETS, "ui", "sellSound.wav"),
    os.path.join(ASSETS, "sounds", "ui", "sellSound.wav"),
    os.path.join(ASSETS, "sounds", "sellSound.wav"),
    os.path.join(BASE_DIR, "sellSound.wav"),
    os.path.join(ASSETS, "ui", "merchantSell.wav"),
    os.path.join(ASSETS, "sounds", "ui", "merchantSell.wav"),
    os.path.join(ASSETS, "sounds", "merchantSell.wav"),
    os.path.join(ASSETS, "ui", "merchant_sell.wav"),
    os.path.join(BASE_DIR, "merchantSell.wav"),
]
# </POTBO_STAGE S0048>

# <POTBO_STAGE S0050>


MERCHANT_BUY_SELL_SES_ADAYLARI = [
    os.path.join(ASSETS, "ui", "merchantBuySell.wav"),
    os.path.join(ASSETS, "sounds", "ui", "merchantBuySell.wav"),
    os.path.join(ASSETS, "sounds", "merchantBuySell.wav"),
    os.path.join(ASSETS, "ui", "merchant_buy_sell.wav"),
    os.path.join(BASE_DIR, "merchantBuySell.wav"),
]
MERCHANT_BUY_SES_YOLU = mevcut_ilk_dosya(MERCHANT_BUY_SES_ADAYLARI)
MERCHANT_SELL_SES_YOLU = mevcut_ilk_dosya(MERCHANT_SELL_SES_ADAYLARI)
# </POTBO_STAGE S0050>

# <POTBO_STAGE S0052>
MERCHANT_BUY_SELL_SES_YOLU = mevcut_ilk_dosya(MERCHANT_BUY_SELL_SES_ADAYLARI)
# </POTBO_STAGE S0052>

# <POTBO_STAGE S0076>



METINLER = {
    "TR": {
        "continue": "DEVAM ET",
        "new_game": "YENİ OYUN",
        "load_game": "OYUN YÜKLE",
        "settings": "AYARLAR",
        "credits": "EMEĞİ GEÇENLER",
        "quit": "ÇIKIŞ",
        "restart": "YENİDEN BAŞLAT",
        "main_menu": "ANA MENÜ",
        "game_over_title": "GEBERDIN",
        "merchant_title": "TÜCCAR",
        "exit_confirm": "EMİN MİSİN?",
        "exit_yes": "EVET, BEN BU OYUNU OYNAYABİLECEK KADAR BECERİKLİ BİR İNSAN DEĞİLİM",
        "exit_no": "HAYIR, BEN VAZGEÇMEDİM",
        "save_name_title": "KAYIT ADI",
        "save_name_help": "Kayıt adını yaz ve ENTER tuşuna bas",
        "save_name_empty": "Kayıt adı boş bırakılamaz.",
        "pause_title": "OYUN DURAKLATILDI",
        "resume_game": "OYUNA DEVAM ET",
        "return_main_menu": "ANA MENÜYE DÖN",
        "pause_settings": "AYARLAR",
        "pause_quit": "ÇIKIŞ",
        "pause_exit_confirm": "OYUNDAN ÇIKMAK İSTEDİĞİNE EMİN MİSİN?",
        "main_menu_confirm": "ANA MENÜYE DÖNMEK İSTEDİĞİNE EMİN MİSİN?",
        "yes": "EVET",
        "no": "HAYIR",
        "delete_save_confirm": "BU KAYDI SİLMEK İSTEDİĞİNE EMİN MİSİN?",
        "delete_help": "DELETE: Kaydı sil",
        "subtitle": "KANLA YAZILMIŞ BİR YOL",
        "menu_help": "W/S veya yön tuşları: Seç    ENTER/SPACE/E: Onayla",
        "no_continue": "Devam edilecek kayıt bulunamadı.",
        "create_title": "KARAKTER SEÇ",
        "character_name": "KARAKTER ADI",
        "character": "KARAKTER",
        "male": "ERKEK",
        "female": "KADIN",
        "remaining_bonus": "KALAN BONUS PUANI",
        "strength": "GÜÇ",
        "health": "CAN",
        "mana": "MANA",
        "strength_desc": "Her puan saldırı hasarını +2 artırır.",
        "health_desc": "Her puan maksimum canı +10 artırır.",
        "mana_desc": "Her puan maksimum manayı +5 artırır.",
        "start_game": "OYUNU BAŞLAT",
        "create_help": "Yukarı/Aşağı: Seç    Sol/Sağ: Değiştir    ENTER/SPACE/E: Onayla",
        "name_empty": "Karakter adı boş bırakılamaz.",
        "points_remaining": "10 bonus puanın tamamını dağıtmalısın.",
        "loading": "YÜKLENİYOR",
        "loading_complete": "YÜKLEME TAMAMLANDI",
        "press_key": "DEVAM ETMEK İÇİN HERHANGİ BİR TUŞA BASIN",
        "hint": "İPUCU",
        "controls": "TUŞ KOMBİNASYONLARI",
        "move_key": "WASD / YÖN TUŞLARI",
        "move_desc": "Karakteri hareket ettirir",
        "attack_key": "J",
        "attack_desc": "Kılıç saldırısı yapar",
        "interact_key": "E",
        "interact_desc": "Karakter ve nesnelerle etkileşim",
        "save_key": "F5",
        "save_desc": "Oyunu kaydeder",
        "menu_key": "ESC",
        "menu_desc": "Duraklatma menüsünü açar",
        "settings_title": "AYARLAR",
        "language": "DİL",
        "master_sound": "ANA SES",
        "effect_sound": "EFEKT SESİ",
        "fullscreen": "TAM EKRAN",
        "show_fps": "FPS GÖSTER",
        "back_option": "GERİ",
        "on": "AÇIK",
        "off": "KAPALI",
        "settings_help": "Yön tuşları: Seç/Değiştir    ENTER/SPACE: Onayla    ESC: Geri",
        "load_title": "OYUN YÜKLE",
        "no_save": "KAYIT BULUNAMADI",
        "load_help": "Yön tuşları: Seç    ENTER/SPACE: Yükle    ESC: Geri",
        "credits_title": "EMEĞİ GEÇENLER",
        "game_design": "Oyun Tasarımı",
        "programming": "Programlama",
        "visual_design": "Görsel Tasarım",
        "team": "AGRAPHON STUDIOS",
        "made_with": "Agraphon Studios tarafından Python ve Pygame ile geliştirildi.",
        "thanks": "Oynadığınız için teşekkürler.",
        "level": "SEVİYE",
        "damage": "HASAR",
        "talk": "Konuşmak için E",
        "dialogue_next": "Devam etmek için ENTER / SPACE",
        "game_menu": "WASD: Hareket   J: Saldırı   K: Savunma   E: Etkileşim   F5: Kaydet   ESC: Menü",
        "saved": "Oyun kaydedildi.",
        "asset_missing": "Görsel dosyası bulunamadı",
    },
    "EN": {
        "continue": "CONTINUE",
        "new_game": "NEW GAME",
        "load_game": "LOAD GAME",
        "settings": "SETTINGS",
        "credits": "CREDITS",
        "quit": "QUIT",
        "restart": "RESTART",
        "main_menu": "MAIN MENU",
        "game_over_title": "YOU ARE DEAD",
        "merchant_title": "MERCHANT",
        "exit_confirm": "ARE YOU SURE?",
        "exit_yes": "YES, I AM NOT SKILLED ENOUGH TO PLAY THIS GAME",
        "exit_no": "NO, I HAVE NOT GIVEN UP",
        "save_name_title": "SAVE NAME",
        "save_name_help": "Enter a save name and press ENTER",
        "save_name_empty": "Save name cannot be empty.",
        "pause_title": "GAME PAUSED",
        "resume_game": "RESUME GAME",
        "return_main_menu": "RETURN TO MAIN MENU",
        "pause_settings": "SETTINGS",
        "pause_quit": "QUIT",
        "pause_exit_confirm": "ARE YOU SURE YOU WANT TO EXIT THE GAME?",
        "main_menu_confirm": "ARE YOU SURE YOU WANT TO RETURN TO THE MAIN MENU?",
        "yes": "YES",
        "no": "NO",
        "delete_save_confirm": "ARE YOU SURE YOU WANT TO DELETE THIS SAVE?",
        "delete_help": "DELETE: Remove save",
        "subtitle": "A PATH WRITTEN IN BLOOD",
        "menu_help": "W/S or Arrow Keys: Select    ENTER/SPACE/E: Confirm",
        "no_continue": "No save file was found.",
        "create_title": "CHARACTER SELECT",
        "character_name": "CHARACTER NAME",
        "character": "CHARACTER",
        "male": "MALE",
        "female": "FEMALE",
        "remaining_bonus": "REMAINING BONUS POINTS",
        "strength": "STRENGTH",
        "health": "HEALTH",
        "mana": "MANA",
        "strength_desc": "Each point increases attack damage by +2.",
        "health_desc": "Each point increases maximum health by +10.",
        "mana_desc": "Each point increases maximum mana by +5.",
        "start_game": "START GAME",
        "create_help": "Up/Down: Select    Left/Right: Change    ENTER/SPACE/E: Confirm",
        "name_empty": "Character name cannot be empty.",
        "points_remaining": "You must distribute all 10 bonus points.",
        "loading": "LOADING",
        "loading_complete": "LOADING COMPLETE",
        "press_key": "PRESS ANY KEY TO CONTINUE",
        "hint": "HINT",
        "controls": "KEY COMBINATIONS",
        "move_key": "WASD / ARROW KEYS",
        "move_desc": "Move the character",
        "attack_key": "J",
        "attack_desc": "Perform a sword attack",
        "interact_key": "E",
        "interact_desc": "Interact with characters and objects",
        "save_key": "F5",
        "save_desc": "Save the game",
        "menu_key": "ESC",
        "menu_desc": "Open the pause menu",
        "settings_title": "SETTINGS",
        "language": "LANGUAGE",
        "master_sound": "MASTER VOLUME",
        "effect_sound": "SFX VOLUME",
        "fullscreen": "FULLSCREEN",
        "show_fps": "SHOW FPS",
        "back_option": "BACK",
        "on": "ON",
        "off": "OFF",
        "settings_help": "Arrow keys: Select/Change    ENTER/SPACE: Confirm    ESC: Back",
        "load_title": "LOAD GAME",
        "no_save": "NO SAVE FILE FOUND",
        "load_help": "Arrow keys: Select    ENTER/SPACE: Load    ESC: Back",
        "credits_title": "CREDITS",
        "game_design": "Game Design",
        "programming": "Programming",
        "visual_design": "Visual Design",
        "team": "AGRAPHON STUDIOS",
        "made_with": "Developed by Agraphon Studios with Python and Pygame.",
        "thanks": "Thank you for playing.",
        "level": "LEVEL",
        "damage": "DAMAGE",
        "talk": "Press E to talk",
        "dialogue_next": "Press ENTER / SPACE to continue",
        "game_menu": "WASD: Move   J: Attack   K: Block   E: Interact   F5: Save   ESC: Menu",
        "saved": "Game saved.",
        "asset_missing": "Image file was not found",
    },
}
# </POTBO_STAGE S0076>

# <POTBO_STAGE S0093>
MERCHANT = "merchant"
# </POTBO_STAGE S0093>

# <POTBO_STAGE S0167>









def varsayilan_dunya_durumu():
    return {
        "version": 2,
        "elapsed_ms": 0,
        "distance_travelled": 0.0,
        "tension": 0.0,
        "threat": 0.0,
        "items_acquired": 0,
        "items_used": 0,
        "items_dropped": 0,
        "merchant_buys": 0,
        "merchant_sells": 0,
        "combat_hits_given": 0,
        "combat_hits_taken": 0,
        "saves": 0,
        "event_seq": 0,
    }
# </POTBO_STAGE S0167>

# <POTBO_STAGE S0196>


merchant_sayfa = "menu"
merchant_menu_index = 0
merchant_index = 0
merchant_mesaji = ""
merchant_mesaj_zamani = 0
merchant_acilis_zamani = 0
merchant_kapanis_zamani = 0
merchant_kapanis_isteniyor = False
MERCHANT_ACILIS_FADE_SURESI = 520
merchant_yukseltmeler = {"weapon": 1, "armor": 1, "focus": 1}
merchant_gorulen_urunler = set()
merchant_buy_sayfasi_goruldu = False
# </POTBO_STAGE S0196>

# <POTBO_STAGE S0199>

merchant_modal = None
merchant_onay_index = 1
merchant_bekleyen_islem = None
merchant_fiyat_girdisi = ""
merchant_geri_alim_listesi = []
# </POTBO_STAGE S0199>

# <POTBO_STAGE S0201>

MERCHANT_HARF_ARALIGI = 24
merchant_diyalog_kuyrugu = []
merchant_diyalog_index = 0
merchant_yazi_baslangici = 0
merchant_yazi_tamamlandi = False
# </POTBO_STAGE S0201>

# <POTBO_STAGE S0227>
merchant_buy_sesi = ses_yukle(MERCHANT_BUY_SES_YOLU) if MERCHANT_BUY_SES_YOLU else None
merchant_sell_sesi = (
    ses_yukle(MERCHANT_SELL_SES_YOLU) if MERCHANT_SELL_SES_YOLU else None
)
# </POTBO_STAGE S0227>

# <POTBO_STAGE S0229>
merchant_buy_sell_sesi = (
    ses_yukle(MERCHANT_BUY_SELL_SES_YOLU) if MERCHANT_BUY_SELL_SES_YOLU else None
)
# </POTBO_STAGE S0229>

# <POTBO_STAGE S0236>


def map_ambience_guncelle():
    """Harita doğa sesini tek dedicated channel üzerinde kesintisiz loop eder.

    Pause/envanter/merchant dünya sahnesinin modal uzantıları olduğu için ambience
    kesilmez; ölüm, loading ve ana menüde kapanır. Game-over müziğiyle üst üste binmez.
    """
    if map_ambience_kanali is None or map_ambience_sesi is None:
        return
    dunya_acik = oyun_durumu in (
        OYUN,
        ENVANTER,
        MERCHANT,
        DURAKLATMA,
        OYUNDAN_CIKIS_ONAY,
        ANA_MENU_ONAY,
    )


    if oyun_durumu == CIKIS_ONAY and cikis_donus_durumu in (
        DURAKLATMA,
        OYUN,
    ):
        dunya_acik = True
    aktif = bool(dunya_acik and oyuncu_hp > 0)
    if aktif:
        vol = _v35_ambience_ses_orani()


        map_ambience_kanali.set_volume(vol, vol)
        if not map_ambience_kanali.get_busy():
            map_ambience_kanali.play(map_ambience_sesi, loops=-1, fade_ms=650)
    elif map_ambience_kanali.get_busy():
        map_ambience_kanali.fadeout(220)
# </POTBO_STAGE S0236>

# <POTBO_STAGE S0239>


def aktif_buton_ses_turu():
    """Ekrana göre buton ses ailesini seçer; slot ve seçimler bu sisteme girmez."""
    if oyun_durumu == OYUN and oyuncu_hp <= 0:
        return "menu1"
    if oyun_durumu in (
        ANA_MENU,
        DURAKLATMA,
        KARAKTER_OLUSTUR,
        AYARLAR,
        CIKIS_ONAY,
        ANA_MENU_ONAY,
        OYUNDAN_CIKIS_ONAY,
    ):
        return "menu1"
    if oyun_durumu == MERCHANT:
        return "merchant2"

    return "menu1"


def button_hover_sesi_cal(tur=None):
    """Yalnızca gerçek buton odağı değiştiğinde doğru ses ailesini çalar."""
    if not pygame.mixer.get_init():
        return

    tur = tur or aktif_buton_ses_turu()
    ses = {
        "menu1": button_hover1_sesi,
        "merchant2": button_hover2_sesi,
    }.get(tur, button_hover1_sesi)


    if ses is None and tur == "merchant2":
        ses = button_hover1_sesi
    if ses is None:
        return

    ses.set_volume(_efekt_ses_orani())
    ses.play()


def button_click_sesi_cal(tur=None):
    """Gerçek bir UI butonu onaylandığında ses + kısa click animasyonu üretir."""
    global ui_buton_click_baslangic
    ui_buton_click_baslangic = pygame.time.get_ticks()

    if not pygame.mixer.get_init():
        return

    tur = tur or aktif_buton_ses_turu()
    ses = {
        "menu1": button_click1_sesi,
        "merchant2": button_click2_sesi,
    }.get(tur, button_click1_sesi)

    if ses is None and tur == "merchant2":
        ses = button_click1_sesi
    if ses is None:
        return

    ses.set_volume(_efekt_ses_orani())
    ses.play()


def merchant_islem_sesi_cal(islem_turu):
    """Başarılı ekonomik işlemin tek ve deterministik ses olayı.

    ``buy`` yalnız para oyuncudan çıktığında, ``sell`` yalnız para oyuncuya
    girdiğinde çağrılır. Eadric gibi Merchant ekranı dışında satış yapan NPC'ler
    de aynı kontratı kullanır. Böylece ekonomi sistemi büyüdükçe ses davranışı
    ekranlara dağılmaz.
    """
    if not pygame.mixer.get_init():
        return

    tur = str(islem_turu).lower().strip()
    if tur == "buy":
        ses = merchant_buy_sesi
    elif tur == "sell":
        ses = merchant_sell_sesi
    else:
        return



    ses = ses or merchant_buy_sell_sesi or button_click2_sesi or button_click1_sesi
    if ses is None:
        return
    ses.set_volume(_efekt_ses_orani())
    ses.play()
# </POTBO_STAGE S0239>

# <POTBO_STAGE S0243>


def secim_imzasi_al():
    """Hover sesi için yalnızca gerçek buton odaklarını izler; seçimler ve slotlar sessizdir."""
    if oyun_durumu == ANA_MENU:
        return ("menu_button", menu_index)
    if oyun_durumu == DURAKLATMA:
        return ("pause_button", duraklatma_index)
    if oyun_durumu == OYUN and oyuncu_hp <= 0 and oyuncu_olum_menu_hazir_mi():
        return ("death_button", oyuncu_olum_menu_index)
    if oyun_durumu == CIKIS_ONAY:
        return ("exit_button", cikis_index)
    if oyun_durumu == ANA_MENU_ONAY:
        return ("main_confirm_button", ana_menu_onay_index)
    if oyun_durumu == OYUNDAN_CIKIS_ONAY:
        return ("quit_confirm_button", oyundan_cikis_onay_index)
    if oyun_durumu == KAYIT_SIL_ONAY:
        return ("delete_confirm_button", kayit_sil_onay_index)
    if oyun_durumu == AYARLAR:
        if tus_atama_bekleniyor is not None:
            return None
        if ayar_odak == "kategori":
            return ("settings_category", ayar_kategori_index)
        return (
            "settings_option",
            ayar_kategori_index,
            ayar_index,
        )
    if oyun_durumu == MERCHANT:
        if merchant_modal == "confirm":
            return (
                "merchant_confirm_button",
                merchant_onay_index,
            )
        if merchant_modal is None and merchant_sayfa == "menu":
            return ("merchant_menu_button", merchant_menu_index)

        if merchant_modal is None and merchant_sayfa in (
            "sell",
            "buy",
        ):
            liste = merchant_aktif_liste()
            if liste:
                return (
                    "merchant_list",
                    merchant_sayfa,
                    merchant_index % len(liste),
                )
    return None
# </POTBO_STAGE S0243>

# <POTBO_STAGE S0248>

merchant_resmi_orijinal = resim_yukle(MERCHANT_MEDOLI_YOLU)
# </POTBO_STAGE S0248>

# <POTBO_STAGE S0274>

try:
    with open(MERCHANT_VERI_YOLU, "r", encoding="utf-8") as dosya:
        MERCHANT_VERI = json.load(dosya)
except (OSError, ValueError, TypeError):
    MERCHANT_VERI = {
        "name": "Merchant Hanus",
        "x": 1380,
        "y": 330,
        "interaction_radius_x": 72,
        "interaction_radius_y": 58,
        "sell_ratio": 0.5,
        "stock": [
            {"id": "aurum_potabile", "price": 200},
            {"id": "quinta_essentia", "price": 500},
        ],
        "upgrades": [],
    }

merchant_x = float(MERCHANT_VERI.get("x", 1380))
merchant_y = float(MERCHANT_VERI.get("y", 330))
# </POTBO_STAGE S0274>

# <POTBO_STAGE S0289>

if merchant_resmi_orijinal is not None:

    merchant_orijinal_w = max(1, merchant_resmi_orijinal.get_width())
    merchant_orijinal_h = max(1, merchant_resmi_orijinal.get_height())

    merchant_maksimum_w = 84
    merchant_maksimum_h = 76

    merchant_olcek = min(
        merchant_maksimum_w / merchant_orijinal_w,
        merchant_maksimum_h / merchant_orijinal_h,
    )

    merchant_cizim_w = max(1, int(round(merchant_orijinal_w * merchant_olcek)))
    merchant_cizim_h = max(1, int(round(merchant_orijinal_h * merchant_olcek)))

    merchant_resmi = pygame.transform.scale(
        merchant_resmi_orijinal,
        (merchant_cizim_w, merchant_cizim_h),
    )
else:
    merchant_resmi = None
# </POTBO_STAGE S0289>

# <POTBO_STAGE S0310>


def dunya_olayi_kaydet(olay_turu, **veri):
    """Küçük, sınırlı bir olay günlüğü ve sayaç katmanı; dışarı veri göndermez."""
    global dunya_son_combat_zamani

    dunya_durumu["event_seq"] = int(dunya_durumu.get("event_seq", 0)) + 1
    kayit = {
        "seq": dunya_durumu["event_seq"],
        "type": str(olay_turu),
        "world_ms": int(dunya_durumu.get("elapsed_ms", 0)),
        "x": round(float(oyuncu_x), 2),
        "y": round(float(oyuncu_y), 2),
    }
    for anahtar, deger in veri.items():
        if isinstance(deger, (str, int, float, bool)) or deger is None:
            kayit[str(anahtar)] = deger
        else:
            kayit[str(anahtar)] = str(deger)
    dunya_olay_gunlugu.append(kayit)

    sayac_esleme = {
        "item_acquired": "items_acquired",
        "item_used": "items_used",
        "item_dropped": "items_dropped",
        "merchant_buy": "merchant_buys",
        "merchant_sell": "merchant_sells",
        "hit_given": "combat_hits_given",
        "hit_taken": "combat_hits_taken",
        "save": "saves",
    }
    sayac = sayac_esleme.get(str(olay_turu))
    if sayac:
        miktar = veri.get("count", 1)
        try:
            miktar = max(1, int(miktar))
        except (TypeError, ValueError):
            miktar = 1
        dunya_durumu[sayac] = int(dunya_durumu.get(sayac, 0)) + miktar

    if olay_turu in (
        "attack",
        "hit_given",
        "hit_taken",
        "enemy_attack",
    ):
        dunya_son_combat_zamani = pygame.time.get_ticks()
# </POTBO_STAGE S0310>

# <POTBO_STAGE S0373>


def merchant_carpisma_rect():
    """
    Tüccarın görünen gövdesini kapsayan fiziksel engel.
    Oyuncu içinden geçemez; collision'ın hemen dışında E ile konuşabilir.
    """
    return pygame.Rect(
        int(round(merchant_x)) - 22,
        int(round(merchant_y)) - 57,
        44,
        59,
    )
# </POTBO_STAGE S0373>

# <POTBO_STAGE S0382>


def hareket_gecerli_mi(yeni_x, yeni_y):
    def konum_engelsiz_mi(test_x, test_y):
        if not (
            14 <= test_x <= HARITA_GENISLIK - 14
            and 16 <= test_y <= HARITA_YUKSEKLIK - 10
        ):
            return False

        oyuncu_rect = oyuncu_carpisma_rect(test_x, test_y)

        if oyuncu_rect.colliderect(npc_carpisma_rect()):
            return False

        if oyuncu_rect.colliderect(merchant_carpisma_rect()):
            return False

        for dusman in common_enemies:
            if getattr(dusman, "active", False) and oyuncu_rect.colliderect(
                common_enemy_carpisma_rect(dusman)
            ):
                return False

        if (
            tarkard_actor is not None
            and getattr(tarkard_actor, "active", False)
            and oyuncu_rect.colliderect(common_enemy_carpisma_rect(tarkard_actor))
        ):
            return False

        if (
            torrmund_actor is not None
            and getattr(torrmund_actor, "active", False)
            and oyuncu_rect.colliderect(common_enemy_carpisma_rect(torrmund_actor))
        ):
            return False

        for nokta_x, nokta_y in oyuncu_ayak_noktalari(test_x, test_y):
            if harita_pikseli_engel_mi(nokta_x, nokta_y):
                return False

        return True



    fark_x = yeni_x - oyuncu_x
    fark_y = yeni_y - oyuncu_y
    mesafe = max(abs(fark_x), abs(fark_y))
    adim_sayisi = max(1, int(math.ceil(mesafe / 2.0)))

    for adim in range(1, adim_sayisi + 1):
        oran = adim / adim_sayisi
        test_x = oyuncu_x + fark_x * oran
        test_y = oyuncu_y + fark_y * oran

        if not konum_engelsiz_mi(test_x, test_y):
            return False

    return True
# </POTBO_STAGE S0382>

# <POTBO_STAGE S0386>


def envanter_aksiyonlari(item_index, kaynak="grid"):
    if not isinstance(item_index, int) or not 0 <= item_index < len(envanter_itemleri):
        return []
    item = envanter_itemleri[item_index]
    if not isinstance(item, dict):
        return []

    sonuc = []
    buyu = item_buyu_mu(item)
    q_uygun = item_q_hizli_kullanima_uygun_mu(item)



    if not buyu and item.get("id") in (
        "health_potion",
        "aurum_potabile",
        "quinta_essentia",
        "eadric_stone",
    ):
        sonuc.append(("use", bt("KULLAN", "USE")))
    if q_uygun:
        q_bagli = q_hizli_item_index == item_index
        sonuc.append(
            (
                "bind_q",
                bt(
                    "Q HIZLI SLOTUNDAN ÇIKAR" if q_bagli else "Q HIZLI SLOTUNA ATA",
                    "REMOVE FROM Q QUICK SLOT" if q_bagli else "BIND TO Q QUICK SLOT",
                ),
            )
        )

    if not merchant_gorev_itemi_mi(item) and not buyu:
        sonuc.append(("drop", bt("AT", "DROP")))

    if not buyu:
        if kaynak == "featured":
            sonuc.append(
                (
                    "unfeature",
                    bt(
                        "ÖNE ÇIKANLARDAN ÇIKAR",
                        "REMOVE FROM FEATURED",
                    ),
                )
            )
        else:
            sonuc.append(
                (
                    "feature",
                    bt(
                        "ÖNE ÇIKANLARA ATA",
                        "ASSIGN TO FEATURED",
                    ),
                )
            )

    sonuc.append(("move", bt("TAŞI / YER DEĞİŞTİR", "MOVE / SWAP")))
    return sonuc
# </POTBO_STAGE S0386>

# <POTBO_STAGE S0393>



MERCHANT_KAPANIS_SURESI = 1000
MERCHANT_STOK_FIYATLARI = {
    "aurum_potabile": 160,
    "quinta_essentia": 240,
    "fire_magic": FIRE_MAGIC_EADRIC_FIYATI,
}
MERCHANT_SATIS_REFERANSI = {
    "aurum_potabile": 64,
    "quinta_essentia": 96,
    "fire_magic": FIRE_MAGIC_SATIS_FIYATI,
}
MERCHANT_MAKSIMUM_TEKLIF = {
    "aurum_potabile": 64,
    "quinta_essentia": 96,
    "fire_magic": FIRE_MAGIC_SATIS_FIYATI,
}
MERCHANT_GERI_ALIM_FIYATI = {
    "aurum_potabile": 70,
    "quinta_essentia": 100,
    "fire_magic": FIRE_MAGIC_GERI_ALIM_FIYATI,
}


def merchant_yakin_mi():
    return abs(oyuncu_x - merchant_x) < 66 and abs(oyuncu_y - merchant_y) < 62


def merchant_item_olustur(item_id):
    if item_id == "health_potion":
        return None
    if item_id == "aurum_potabile":
        return aurum_potabile_olustur()
    if item_id == "quinta_essentia":
        return quinta_essentia_olustur()
    if item_id == "fire_magic":
        return fire_magic_olustur()
    return None


def merchant_gorev_itemi_mi(item):
    if not isinstance(item, dict):
        return False
    kategori = str(item.get("category", "")).upper()
    tur = str(item.get("type", "")).upper()
    return bool(
        item.get("quest_item", False)
        or item.get("id") == "eadric_stone"
        or kategori in ("GÖREV EŞYASI", "QUEST ITEM")
        or tur in ("GÖREV EŞYASI", "QUEST ITEM")
    )


def merchant_envanter_satiliklari():
    return [
        (i, item)
        for i, item in enumerate(envanter_itemleri)
        if isinstance(item, dict) and not merchant_gorev_itemi_mi(item)
    ]


def merchant_stok_urun_idleri():
    return {
        str(kayit.get("id"))
        for kayit in MERCHANT_VERI.get("stock", [])
        if isinstance(kayit, dict)
        and kayit.get("id")
        and kayit.get("id") not in ("fire_magic", "health_potion")
    }


def merchant_yeni_urun_idleri():
    return merchant_stok_urun_idleri() - merchant_gorulen_urunler


def merchant_yeni_urun_var_mi():
    return bool(merchant_yeni_urun_idleri())


def merchant_yeni_urunleri_goruldu_isaretle():
    global merchant_gorulen_urunler
    merchant_gorulen_urunler.update(merchant_stok_urun_idleri())


def merchant_buy_listesi():
    sonuc = []
    for kayit in MERCHANT_VERI.get("stock", []):
        if isinstance(kayit, dict):
            if kayit.get("id") == "health_potion":
                continue
            if kayit.get("id") == "fire_magic":


                continue
            kopya = dict(kayit)
            kopya["source"] = "stock"
            kopya["price"] = MERCHANT_STOK_FIYATLARI.get(kopya.get("id"), 1)
            sonuc.append(kopya)
    for i, kayit in enumerate(merchant_geri_alim_listesi):
        if isinstance(kayit, dict):
            if kayit.get("id") == "health_potion":
                continue
            kopya = dict(kayit)
            kopya["source"] = "buyback"
            kopya["buyback_index"] = i
            sonuc.append(kopya)
    return sonuc


def merchant_aktif_liste():
    if merchant_sayfa == "sell":
        return merchant_envanter_satiliklari()
    if merchant_sayfa == "buy":
        return merchant_buy_listesi()
    return []


def merchant_diyalog_yaz(metin, devam=None):
    """Merchant konuşmasını sıraya alır ve harf harf gösterir."""
    global merchant_mesaji, merchant_mesaj_zamani
    global merchant_diyalog_kuyrugu, merchant_diyalog_index
    global merchant_yazi_baslangici, merchant_yazi_tamamlandi

    satirlar = [str(metin)]
    if devam:
        if isinstance(devam, (list, tuple)):
            satirlar.extend(str(x) for x in devam if str(x))
        else:
            satirlar.append(str(devam))

    merchant_diyalog_kuyrugu = satirlar
    merchant_diyalog_index = 0
    merchant_mesaji = satirlar[0] if satirlar else ""
    merchant_mesaj_zamani = pygame.time.get_ticks()
    merchant_yazi_baslangici = merchant_mesaj_zamani
    merchant_yazi_tamamlandi = False


def merchant_diyalog_gorunen_metin():
    global merchant_yazi_tamamlandi
    metin = merchant_mesaji or ""
    if merchant_yazi_tamamlandi:
        return metin
    gecen = max(0, pygame.time.get_ticks() - merchant_yazi_baslangici)
    adet = min(len(metin), 1 + gecen // MERCHANT_HARF_ARALIGI)
    if adet >= len(metin):
        merchant_yazi_tamamlandi = True
    return metin[:adet]


def merchant_diyalog_tamamla():
    global merchant_yazi_tamamlandi
    merchant_yazi_tamamlandi = True


def merchant_diyalog_sonraki():
    global merchant_diyalog_index, merchant_mesaji
    global merchant_yazi_baslangici, merchant_yazi_tamamlandi
    if not merchant_yazi_tamamlandi:
        merchant_diyalog_tamamla()
        return
    if merchant_diyalog_index + 1 < len(merchant_diyalog_kuyrugu):
        merchant_diyalog_index += 1
        merchant_mesaji = merchant_diyalog_kuyrugu[merchant_diyalog_index]
        merchant_yazi_baslangici = pygame.time.get_ticks()
        merchant_yazi_tamamlandi = False


def merchant_ac():
    global oyun_durumu, merchant_sayfa, merchant_menu_index, merchant_index
    global merchant_acilis_zamani, merchant_kapanis_zamani, merchant_kapanis_isteniyor
    global merchant_modal, merchant_bekleyen_islem, merchant_buy_sayfasi_goruldu
    merchant_sayfa = "menu"
    merchant_menu_index = 0
    merchant_index = 0
    merchant_acilis_zamani = pygame.time.get_ticks()
    merchant_kapanis_zamani = 0
    merchant_kapanis_isteniyor = False
    merchant_buy_sayfasi_goruldu = False
    merchant_modal = None
    merchant_bekleyen_islem = None
    merchant_diyalog_yaz(
        bt(
            "Hoş geldin. Ben Hanus; mallara bakabilirsin.",
            "Welcome. I am Hanus; you may inspect the wares.",
        )
    )
    aktif_gorevler.setdefault("merchant_medoli_met", {"status": "completed"})
    dunya_olayi_kaydet("merchant_open")
    oyun_durumu = MERCHANT


def merchant_kapat():
    global merchant_kapanis_zamani, merchant_kapanis_isteniyor
    if merchant_kapanis_isteniyor or merchant_kapanis_zamani:
        return
    if merchant_buy_sayfasi_goruldu:
        merchant_yeni_urunleri_goruldu_isaretle()
    merchant_diyalog_yaz(
        bt(
            "Yolun açık olsun. Altının değil, seçimin seni yaşatsın.",
            "Safe travels. May your choices, not your gold, keep you alive.",
        )
    )

    merchant_kapanis_isteniyor = True
    merchant_kapanis_zamani = 0


def merchant_guncelle():
    global \
        oyun_durumu, \
        merchant_kapanis_zamani, \
        merchant_mesaji, \
        merchant_kapanis_isteniyor
    if not merchant_kapanis_isteniyor:
        return

    son_satir = merchant_diyalog_index + 1 >= len(merchant_diyalog_kuyrugu)
    if not merchant_yazi_tamamlandi or not son_satir:
        return

    simdi = pygame.time.get_ticks()
    if merchant_kapanis_zamani <= 0:
        merchant_kapanis_zamani = simdi
        return

    if simdi - merchant_kapanis_zamani >= MERCHANT_KAPANIS_SURESI:
        merchant_kapanis_zamani = 0
        merchant_kapanis_isteniyor = False
        merchant_mesaji = ""
        dunya_olayi_kaydet("merchant_close")
        oyun_durumu = OYUN


def merchant_menu_secimini_ac():
    global merchant_sayfa, merchant_index, merchant_buy_sayfasi_goruldu
    if merchant_menu_index == 0:
        merchant_sayfa = "sell"
        merchant_index = 0
        merchant_diyalog_yaz(
            bt(
                "Elindekini göster. Kusurunu da, değerini de saklama.",
                "Show me what you carry. Hide neither its flaws nor its worth.",
            )
        )
    elif merchant_menu_index == 1:
        merchant_sayfa = "buy"
        merchant_index = 0
        merchant_buy_sayfasi_goruldu = True
        merchant_diyalog_yaz(
            bt(
                "Raflarımda yalnız işe yarayan şeyler durur.",
                "Only useful things earn a place on my shelves.",
            )
        )
    else:
        merchant_kapat()


def merchant_alt_menu_geri():
    global merchant_sayfa, merchant_menu_index, merchant_index, merchant_modal
    if merchant_sayfa == "buy":
        merchant_yeni_urunleri_goruldu_isaretle()
    merchant_sayfa = "menu"
    merchant_menu_index = 0
    merchant_index = 0
    merchant_modal = None
    merchant_diyalog_yaz(
        bt(
            "Terazi hâlâ dengede. Başka bir işin var mı?",
            "The scales remain balanced. Do you have other business?",
        )
    )


def merchant_satis_fiyati_girisi_baslat():
    global \
        merchant_modal, \
        merchant_fiyat_girdisi, \
        merchant_bekleyen_islem, \
        merchant_onay_index
    satiliklar = merchant_envanter_satiliklari()
    if not satiliklar:
        merchant_diyalog_yaz(
            bt(
                "Satabileceğin eşya yok.",
                "You have nothing I can buy.",
            )
        )
        return
    slot_index, item = satiliklar[merchant_index % len(satiliklar)]
    item_id = item.get("id")
    if merchant_gorev_itemi_mi(item):
        merchant_diyalog_yaz(
            bt(
                "Görev eşyaları satılamaz.",
                "Quest items cannot be sold.",
            )
        )
        return
    kabul_siniri = MERCHANT_MAKSIMUM_TEKLIF.get(
        item_id, MERCHANT_SATIS_REFERANSI.get(item_id, 1)
    )
    merchant_bekleyen_islem = {
        "type": "sell",
        "slot": slot_index,
        "item_id": item_id,
    }
    if item_id == "fire_magic":

        merchant_bekleyen_islem["price"] = FIRE_MAGIC_SATIS_FIYATI
        merchant_onay_index = 1
        merchant_modal = "confirm"
        return
    merchant_fiyat_girdisi = str(kabul_siniri)
    merchant_modal = "price"


def merchant_satin_alma_onayi_baslat():
    global merchant_modal, merchant_bekleyen_islem, merchant_onay_index
    liste = merchant_buy_listesi()
    if not liste:
        merchant_diyalog_yaz(bt("Raflarım boş.", "My shelves are empty."))
        return
    kayit = liste[merchant_index % len(liste)]
    merchant_bekleyen_islem = {
        "type": "buy",
        "record": dict(kayit),
    }
    merchant_onay_index = 1
    merchant_modal = "confirm"


def merchant_satis_onayi_baslat():
    global merchant_modal, merchant_onay_index
    try:
        fiyat = int(merchant_fiyat_girdisi)
    except ValueError:
        fiyat = 0
    item_id = (merchant_bekleyen_islem or {}).get("item_id")
    kabul_siniri = MERCHANT_MAKSIMUM_TEKLIF.get(
        item_id, MERCHANT_SATIS_REFERANSI.get(item_id, 1)
    )
    if fiyat > kabul_siniri:
        merchant_diyalog_yaz(
            bt(
                f"Bu eşya için {kabul_siniri} coinden fazlasını vermem.",
                f"I will not pay more than {kabul_siniri} coins for this item.",
            )
        )
        return
    merchant_bekleyen_islem["price"] = fiyat
    merchant_onay_index = 1
    merchant_modal = "confirm"


def merchant_islemi_uygula():
    global oyuncu_altin, merchant_modal, merchant_bekleyen_islem, merchant_index
    islem = merchant_bekleyen_islem or {}
    if islem.get("type") == "sell":
        slot = islem.get("slot")
        if not isinstance(slot, int) or not 0 <= slot < len(envanter_itemleri):
            merchant_modal = None
            return
        item = envanter_itemleri[slot]
        if not isinstance(item, dict) or merchant_gorev_itemi_mi(item):
            merchant_diyalog_yaz(
                bt(
                    "Bu eşya artık satılamıyor.",
                    "That item can no longer be sold.",
                )
            )
            merchant_modal = None
            return
        fiyat = int(islem.get("price", 0))
        item_id = item.get("id")
        oyuncu_altin += fiyat
        geri_item = dict(item)
        geri_item["quantity"] = 1
        merchant_geri_alim_listesi.append(
            {
                "id": item_id,
                "item": geri_item,
                "price": MERCHANT_GERI_ALIM_FIYATI.get(item_id, max(1, fiyat)),
                "name": item.get("name", ""),
            }
        )
        envanterden_bir_azalt(slot)
        merchant_islem_sesi_cal("sell")
        dunya_olayi_kaydet(
            "merchant_sell",
            item_id=str(item_id or ""),
            price=fiyat,
            count=1,
        )
        merchant_diyalog_yaz(
            bt(
                f"{item.get('name', 'Eşya')} için {fiyat} coin. Anlaştık.",
                f"{fiyat} coins for {item.get('name', 'Item')}. Agreed.",
            )
        )
        merchant_index = min(
            merchant_index,
            max(0, len(merchant_envanter_satiliklari()) - 1),
        )
    elif islem.get("type") == "buy":
        kayit = islem.get("record", {})
        fiyat = int(kayit.get("price", 1))
        if oyuncu_altin < fiyat:
            no_coin_sesi_cal()
            merchant_diyalog_yaz(
                bt(
                    "Yeterli coinin yok.",
                    "You do not have enough coins.",
                )
            )
            merchant_modal = None
            return
        if kayit.get("source") == "buyback" and isinstance(kayit.get("item"), dict):
            item = dict(kayit["item"])
        else:
            item = merchant_item_olustur(kayit.get("id"))
        if not isinstance(item, dict) or not envantere_item_ekle(
            item, kazanimi_goster=True
        ):
            merchant_diyalog_yaz(
                bt(
                    "Envanterinde yer yok.",
                    "Your inventory has no room.",
                )
            )
            merchant_modal = None
            return
        oyuncu_altin -= fiyat
        merchant_islem_sesi_cal("buy")
        dunya_olayi_kaydet(
            "merchant_buy",
            item_id=str(item.get("id", "")),
            price=fiyat,
            count=1,
        )
        if kayit.get("source") == "buyback":
            idx = kayit.get("buyback_index")
            if isinstance(idx, int) and 0 <= idx < len(merchant_geri_alim_listesi):
                merchant_geri_alim_listesi.pop(idx)
        merchant_diyalog_yaz(
            bt(
                f"{item.get('name', 'Eşya')} artık senin.",
                f"{item.get('name', 'Item')} is yours.",
            )
        )
        item_alindi_bildirimi(item.get("name", bt("Eşya", "Item")), 1)
        merchant_index = min(
            merchant_index,
            max(0, len(merchant_buy_listesi()) - 1),
        )
    merchant_modal = None
    merchant_bekleyen_islem = None


def merchant_onayla():
    if merchant_sayfa == "menu":
        merchant_menu_secimini_ac()
    elif merchant_sayfa == "sell":
        merchant_satis_fiyati_girisi_baslat()
    elif merchant_sayfa == "buy":
        merchant_satin_alma_onayi_baslat()


def merchant_sprite_ciz():
    if merchant_resmi is not None:
        rect = merchant_resmi.get_rect(
            midbottom=(
                dunya_ekran_x(merchant_x),
                dunya_ekran_y(merchant_y),
            )
        )
        ekran.blit(merchant_resmi, rect)


def merchant_panel_ciz(rect, kenar=GRI, kalinlik=1, dolgu=(7, 6, 10)):
    pygame.draw.rect(ekran, dolgu, rect)
    pygame.draw.rect(ekran, kenar, rect, kalinlik)


def merchant_coin_ciz(x, y, boyut=22):
    if coin_sembol_resmi is not None:
        coin = hafif_piksellestir(coin_sembol_resmi, (boyut, boyut), 2)
        ekran.blit(coin, (int(x), int(y)))
        return
    pygame.draw.circle(
        ekran,
        SARI,
        (int(x + boyut / 2), int(y + boyut / 2)),
        boyut // 2,
    )


def merchant_fiyat_ciz(rect, miktar, saga_yasla=False, yazi_rengi=ACIK_GRI):
    boyut = min(22, rect.height - 6)
    metin = str(miktar)
    toplam = boyut + 7 + kucuk_font.size(metin)[0]
    x = rect.right - toplam if saga_yasla else rect.x
    merchant_coin_ciz(x, rect.centery - boyut // 2, boyut)
    yazi_yaz(
        metin,
        x + boyut + 7,
        rect.centery,
        yazi_rengi,
        kucuk_font,
        False,
    )


def merchant_diyalog_kutusu_ciz(panel):
    kutu = pygame.Rect(panel.x + 24, panel.bottom - 190, panel.width - 48, 154)
    merchant_panel_ciz(kutu, KOYU_KIRMIZI, 2)
    yazi_yaz(
        "MEDOLI",
        kutu.x + 20,
        kutu.y + 28,
        PARLAK_KIRMIZI,
        normal_font,
        False,
    )
    satirlar = metni_satirlara_bol(
        merchant_diyalog_gorunen_metin() or "...",
        oyun_kucuk_font,
        kutu.width - 40,
    )
    for i, sat in enumerate(satirlar[:4]):
        yazi_yaz(
            sat,
            kutu.x + 20,
            kutu.y + 64 + i * 22,
            ACIK_GRI,
            oyun_kucuk_font,
            False,
        )


def merchant_karakter_ciz(rect):
    merchant_panel_ciz(rect, KOYU_KIRMIZI, 1)
    if merchant_resmi_orijinal is not None:
        hedef = rect.inflate(-24, -24)
        cizilecek = resmi_oranli_sigdir(merchant_resmi_orijinal, hedef, 0, 1.0, True)
        if cizilecek is not None:
            ekran.blit(
                cizilecek,
                cizilecek.get_rect(center=hedef.center),
            )


def merchant_menu_butonu_ciz(rect, metin, secili, rozet=None):
    cizim_rect = buton_click_anim_rect(rect, secili)
    merchant_panel_ciz(
        cizim_rect,
        PARLAK_KIRMIZI if secili else KOYU_KIRMIZI,
        2 if secili else 1,
        (49, 8, 14) if secili else (10, 8, 12),
    )
    yazi_yaz(
        metin,
        cizim_rect.centerx,
        cizim_rect.centery,
        BEYAZ if secili else ACIK_GRI,
        menu_font,
        True,
    )
    if rozet:
        rozet_rect = pygame.Rect(cizim_rect.right - 62, cizim_rect.y + 7, 50, 18)
        pygame.draw.rect(ekran, PARLAK_KIRMIZI, rozet_rect)
        yazi_yaz(
            str(rozet),
            rozet_rect.centerx,
            rozet_rect.centery,
            BEYAZ,
            mini_font,
            True,
        )


def merchant_ana_menu_ciz(panel):
    ust = panel.y + 74
    alt = panel.bottom - 208
    sol = pygame.Rect(panel.x + 24, ust, 360, alt - ust)
    sag = pygame.Rect(
        sol.right + 22,
        ust,
        panel.right - sol.right - 46,
        alt - ust,
    )
    merchant_karakter_ciz(sol)
    secenekler = [
        bt("SAT", "SELL"),
        bt("AL", "BUY"),
        bt("ÇIKIŞ", "EXIT"),
    ]
    for i, metin in enumerate(secenekler):
        r = pygame.Rect(sag.x + 60, sag.y + 55 + i * 86, sag.width - 120, 62)
        rozet = bt("YENİ", "NEW") if i == 1 and merchant_yeni_urun_var_mi() else None
        merchant_menu_butonu_ciz(r, metin, i == merchant_menu_index, rozet)


def merchant_liste_satiri_ciz(rect, item, fiyat, secili, yeni=False):
    merchant_panel_ciz(
        rect,
        PARLAK_KIRMIZI if secili else (60, 45, 52),
        2 if secili else 1,
        (44, 17, 20) if secili else (10, 8, 12),
    )
    merchant_fiyat_ciz(
        pygame.Rect(rect.x + 12, rect.y + 12, 85, rect.height - 24),
        fiyat,
        False,
        BEYAZ,
    )
    yazi_yaz(
        item.get("name", ""),
        rect.x + 115,
        rect.centery,
        BEYAZ,
        oyun_kucuk_font,
        False,
    )
    if yeni:
        rozet = pygame.Rect(rect.right - 106, rect.y + 6, 48, 18)
        pygame.draw.rect(ekran, PARLAK_KIRMIZI, rozet)
        yazi_yaz(
            bt("YENİ", "NEW"),
            rozet.centerx,
            rozet.centery,
            BEYAZ,
            mini_font,
            True,
        )
    item_ikonu_ciz(
        item.get("id"),
        pygame.Rect(rect.right - 48, rect.y + 7, 40, 40),
        cerceve=False,
    )
    adet = item_adedi(item)
    if adet > 1:
        yazi_yaz(
            f"x{adet}",
            rect.right - 56,
            rect.bottom - 10,
            ACIK_GRI,
            mini_font,
            True,
        )


def merchant_item_bilgi_ciz(rect, item, fiyat):
    merchant_panel_ciz(rect, KOYU_KIRMIZI, 1)
    yazi_yaz(
        item.get("name", bt("Eşya", "Item")),
        rect.x + 22,
        rect.y + 30,
        PARLAK_KIRMIZI,
        normal_font,
        False,
    )
    _kat = str(item.get("category", item.get("type", "")))
    _okul = str(item.get("spell_school", ""))
    if _okul:
        _kat = f"{_kat} · {_okul}"
    _kat_rect = yazi_yaz(_kat, rect.x + 22, rect.y + 60, GRI, mini_font, False)
    if _okul:
        spell_okulu_sembol_ciz(
            _okul,
            pygame.Rect(
                _kat_rect.right + 7,
                _kat_rect.centery - 9,
                18,
                18,
            ),
        )
    ikon = pygame.Rect(rect.x + 22, rect.y + 92, 92, 92)
    item_ikonu_ciz(item.get("id"), ikon, cerceve=True)
    for i, sat in enumerate(
        metni_satirlara_bol(
            item.get("description", ""),
            oyun_kucuk_font,
            rect.width - 156,
        )[:8]
    ):
        yazi_yaz(
            sat,
            ikon.right + 18,
            rect.y + 98 + i * 21,
            ACIK_GRI,
            oyun_kucuk_font,
            False,
        )
    deger = pygame.Rect(rect.x + 22, rect.bottom - 64, rect.width - 44, 44)
    merchant_panel_ciz(deger, KOYU_KIRMIZI, 1, (17, 9, 12))
    yazi_yaz(
        bt("NET DEĞER", "NET VALUE"),
        deger.x + 14,
        deger.centery,
        PARLAK_KIRMIZI,
        kucuk_font,
        False,
    )
    merchant_fiyat_ciz(
        pygame.Rect(deger.right - 105, deger.y + 8, 90, 28),
        fiyat,
        True,
        BEYAZ,
    )


def merchant_alt_sayfa_ciz(panel):
    ust = panel.y + 74
    alt = panel.bottom - 208
    portre = pygame.Rect(panel.x + 24, ust, 250, alt - ust)
    liste_rect = pygame.Rect(portre.right + 18, ust, 390, alt - ust)
    bilgi = pygame.Rect(
        liste_rect.right + 18,
        ust,
        panel.right - liste_rect.right - 42,
        alt - ust,
    )
    merchant_karakter_ciz(portre)
    merchant_panel_ciz(liste_rect, KOYU_KIRMIZI, 1)
    yazi_yaz(
        bt("SAT", "SELL") if merchant_sayfa == "sell" else bt("AL", "BUY"),
        liste_rect.centerx,
        liste_rect.y + 28,
        PARLAK_KIRMIZI,
        normal_font,
        True,
    )
    liste = merchant_aktif_liste()
    if not liste:
        yazi_yaz(
            bt("Liste boş.", "The list is empty."),
            liste_rect.centerx,
            liste_rect.centery,
            GRI,
            kucuk_font,
            True,
        )
        merchant_panel_ciz(bilgi, KOYU_KIRMIZI, 1)
        return
    secim = merchant_index % len(liste)
    bas = max(0, min(secim - 2, max(0, len(liste) - 6)))
    for satir_no, kayit in enumerate(liste[bas : bas + 6]):
        idx = bas + satir_no
        if merchant_sayfa == "sell":
            _, item = kayit
            fiyat = MERCHANT_SATIS_REFERANSI.get(item.get("id"), 1)
        else:
            if kayit.get("source") == "buyback" and isinstance(kayit.get("item"), dict):
                item = kayit["item"]
            else:
                item = merchant_item_olustur(kayit.get("id")) or {
                    "id": kayit.get("id"),
                    "name": "",
                }
            fiyat = int(kayit.get("price", 1))
        yeni = (
            merchant_sayfa == "buy"
            and isinstance(kayit, dict)
            and kayit.get("source") == "stock"
            and str(kayit.get("id")) in merchant_yeni_urun_idleri()
        )
        merchant_liste_satiri_ciz(
            pygame.Rect(
                liste_rect.x + 12,
                liste_rect.y + 54 + satir_no * 58,
                liste_rect.width - 24,
                50,
            ),
            item,
            fiyat,
            idx == secim,
            yeni,
        )
    kayit = liste[secim]
    if merchant_sayfa == "sell":
        _, item = kayit
        fiyat = MERCHANT_SATIS_REFERANSI.get(item.get("id"), 1)
    else:
        item = (
            kayit.get("item")
            if kayit.get("source") == "buyback"
            else merchant_item_olustur(kayit.get("id"))
        )
        item = item if isinstance(item, dict) else {"name": "", "id": kayit.get("id")}
        fiyat = int(kayit.get("price", 1))
    merchant_item_bilgi_ciz(bilgi, item, fiyat)
    if merchant_sayfa == "buy" and any(
        k.get("source") == "buyback" for k in liste if isinstance(k, dict)
    ):
        yazi_yaz(
            bt("SATTIKLARIN", "WHAT YOU SOLD"),
            liste_rect.x + 14,
            liste_rect.bottom - 14,
            GRI,
            mini_font,
            False,
        )


def merchant_modal_ciz(panel):
    if merchant_modal is None:
        return
    koyu_kaplama(165)
    kutu = pygame.Rect(panel.centerx - 260, panel.centery - 105, 520, 210)
    merchant_panel_ciz(kutu, PARLAK_KIRMIZI, 2, (8, 6, 10))
    if merchant_modal == "price":
        yazi_yaz(
            bt("SATIŞ FİYATINI GİR", "ENTER SELLING PRICE"),
            kutu.centerx,
            kutu.y + 38,
            PARLAK_KIRMIZI,
            normal_font,
            True,
        )
        giris = pygame.Rect(kutu.x + 110, kutu.y + 78, 300, 52)
        merchant_panel_ciz(giris, KOYU_KIRMIZI, 2, (15, 9, 12))
        yazi_yaz(
            merchant_fiyat_girdisi or "0",
            giris.centerx,
            giris.centery,
            BEYAZ,
            menu_font,
            True,
        )
        yazi_yaz(
            bt(
                "Rakamları yaz, ENTER ile devam et.",
                "Type digits, then press ENTER.",
            ),
            kutu.centerx,
            kutu.bottom - 34,
            GRI,
            mini_font,
            True,
        )
    else:
        yazi_yaz(
            bt("EMİN MİSİN?", "ARE YOU SURE?"),
            kutu.centerx,
            kutu.y + 42,
            PARLAK_KIRMIZI,
            normal_font,
            True,
        )
        secenekler = [bt("EVET", "YES"), bt("HAYIR", "NO")]
        for i, metin in enumerate(secenekler):
            r = pygame.Rect(kutu.x + 65 + i * 210, kutu.y + 92, 180, 54)
            merchant_menu_butonu_ciz(r, metin, merchant_onay_index == i)


def merchant_ekrani_ciz():
    merchant_guncelle()




    if oyun_durumu != MERCHANT:
        oyun_ekrani_ciz()
        return

    oyun_ekrani_ciz()
    gecen = max(0, pygame.time.get_ticks() - merchant_acilis_zamani)
    oran = max(
        0.0,
        min(1.0, gecen / max(1, MERCHANT_ACILIS_FADE_SURESI)),
    )
    oran = oran * oran * (3.0 - 2.0 * oran)
    merchant_taban = ekran.copy() if oran < 1.0 else None
    koyu_kaplama(205)
    panel = pygame.Rect(32, 24, GENISLIK - 64, YUKSEKLIK - 48)
    merchant_panel_ciz(panel, KOYU_KIRMIZI, 3)
    pygame.draw.rect(ekran, PARLAK_KIRMIZI, panel.inflate(-10, -10), 1)
    yazi_yaz(
        t("merchant_title"),
        panel.x + 28,
        panel.y + 31,
        PARLAK_KIRMIZI,
        menu_baslik_font,
        False,
    )
    altin = pygame.Rect(panel.right - 150, panel.y + 16, 118, 42)
    merchant_panel_ciz(altin, KOYU_KIRMIZI, 1, (12, 8, 11))
    merchant_fiyat_ciz(
        pygame.Rect(altin.x + 14, altin.y + 7, altin.width - 28, 28),
        oyuncu_altin,
        False,
        BEYAZ,
    )
    if merchant_sayfa == "menu":
        merchant_ana_menu_ciz(panel)
    else:
        merchant_alt_sayfa_ciz(panel)
    merchant_diyalog_kutusu_ciz(panel)
    merchant_modal_ciz(panel)



    if merchant_taban is not None:
        merchant_taban.set_alpha(int(round(255 * (1.0 - oran))))
        ekran.blit(merchant_taban, (0, 0))
# </POTBO_STAGE S0393>

# <POTBO_STAGE S0403>


def oyuncu_etkilesim_yap():
    global aktif_diyalog, oyun_alt_durumu

    if oyun_alt_durumu != HARITA:
        return

    npc_yakin = eadric_yakin_mi()

    ganimet_yakin = (
        npc_intro_tamamlandi
        and not ganimet_alindi
        and abs(oyuncu_x - ganimet_x) < 40
        and abs(oyuncu_y - ganimet_y) < 36
    )

    try:
        if torrmund_yakin_mi():
            torrmund_konusmasini_baslat()
        elif tarkard_yakin_mi():
            tarkard_konusmasini_baslat()
        elif merchant_yakin_mi():
            merchant_ac()
        elif ganimet_yakin:
            ganimeti_al()
        elif npc_yakin:
            npc_konusmasini_baslat()
    except Exception as hata:
        aktif_diyalog = []
        oyun_alt_durumu = HARITA
        npc_sesi_durdur()
        print("Interaction error:", repr(hata))
# </POTBO_STAGE S0403>

# <POTBO_STAGE S0432>


def dunya_ince_los_acik_mi(baslangic, bitis, adim=5.0, npc_bloklar=True):
    """İki world noktası arasında ince projectile/vision koridoru.

    Enemy navigation footprint'ini taşımadığı için menzilli saldırıda gereksiz
    false-negative üretmez; ancak gerçek solid map pikselleri ve istenirse NPC /
    merchant gövdeleri hâlâ hattı keser. Endpoint'ler bilinçli olarak atlanır.
    """
    bas = pygame.Vector2(baslangic)
    son = pygame.Vector2(bitis)
    fark = son - bas
    mesafe = fark.length()
    if mesafe <= 1.0:
        return True
    sayi = max(2, int(math.ceil(mesafe / max(3.5, float(adim)))))
    for i in range(1, sayi):
        p = bas.lerp(son, i / sayi)
        if harita_pikseli_engel_mi(p.x, p.y):
            return False
    if npc_bloklar:
        a = (int(round(bas.x)), int(round(bas.y)))
        b = (int(round(son.x)), int(round(son.y)))
        for blocker in (
            npc_carpisma_rect(),
            merchant_carpisma_rect(),
        ):
            r = blocker.inflate(-4, -4)
            if r.width > 0 and r.height > 0 and r.clipline(a, b):
                if not r.collidepoint(a) and not r.collidepoint(b):
                    return False
    return True
# </POTBO_STAGE S0432>

# <POTBO_STAGE S0438>


def common_enemy_statik_konum_gecerli_mi(tur, x, y, navigation=False):
    """
    Enemy body footprint için kesin statik dünya testi.

    navigation=True iken birkaç piksel ek güvenlik payı kullanılır. Bu pay gerçek
    collision gövdesini büyütmez; yalnız path planner'ın duvarı yalayan rota
    seçmesini azaltır.
    """
    _common_enemy_nav_cache_dogrula()
    cfg = COMMON_ENEMY_CONFIG[tur]
    margin = int(cfg.get("nav_margin", 0)) if navigation else 0
    yarim = int(cfg["body_half_width"]) + margin
    yuk = int(cfg["body_height"]) + margin

    if not (
        24 + yarim <= x <= HARITA_GENISLIK - 24 - yarim
        and 28 + yuk <= y <= HARITA_YUKSEKLIK - 18
    ):
        return False

    rect = pygame.Rect(
        int(round(x)) - yarim,
        int(round(y)) - yuk,
        yarim * 2,
        yuk,
    )

    if rect.colliderect(npc_carpisma_rect().inflate(margin * 2, margin * 2)):
        return False
    if rect.colliderect(merchant_carpisma_rect().inflate(margin * 2, margin * 2)):
        return False

    for bbox, polygon in _common_enemy_collision_bbox_cache:
        if rect.colliderect(bbox) and _rect_polygon_cakisiyor_mu(rect, polygon):
            return False
    return True
# </POTBO_STAGE S0438>

# <POTBO_STAGE S0448>


def common_enemy_sistemi_sifirla():
    global common_enemies
    global tarkard_actor
    global torrmund_actor
    global common_enemy_son_guncelleme
    global common_enemy_onceki_oyuncu_konumu
    global common_enemy_oyuncu_hizi
    global common_enemy_oyuncu_ivmesi
    global common_enemy_onceki_oyuncu_hizi

    gecici_dunya_aktorlerini_sifirla()
    common_enemies = []
    for index, tur in enumerate(COMMON_ENEMY_TURLERI):
        x, y = common_enemy_guvenli_spawn_bul(tur, common_enemies)
        common_enemies.append(common_enemy_olustur(f"{tur}_{index + 1}", tur, x, y))



    tx, ty = common_enemy_guvenli_spawn_bul("tarkard", common_enemies)
    tarkard_actor = TarkardEnemy("tarkard_unique", tx, ty)



    torr_blockers = list(common_enemies) + [tarkard_actor]
    sx, sy = common_enemy_guvenli_spawn_bul("torrmund", torr_blockers)
    torrmund_actor = SirTorrmundEnemy("torrmund_unique", sx, sy)

    common_enemy_son_guncelleme = pygame.time.get_ticks()
    common_enemy_onceki_oyuncu_konumu = (oyuncu_x, oyuncu_y)
    common_enemy_oyuncu_hizi = pygame.Vector2(0.0, 0.0)
    common_enemy_onceki_oyuncu_hizi = pygame.Vector2(0.0, 0.0)
    common_enemy_oyuncu_ivmesi = pygame.Vector2(0.0, 0.0)
# </POTBO_STAGE S0448>

# <POTBO_STAGE S0453>


def _magic_hedefleri():
    """
    Aktif combat aktörlerini döndürür. NPC/merchant burada yoktur; büyü onlarla
    hikâye etkileşimini bozmaz. Pasif common enemy patlamayla vurulursa kendi
    `hasar_al()` kontratı üzerinden doğal biçimde aggro olur.
    """
    hedefler = [
        d
        for d in common_enemies
        if getattr(d, "active", False) and getattr(d, "hp", 0) > 0
    ]
    if (
        tarkard_actor is not None
        and getattr(tarkard_actor, "active", False)
        and getattr(tarkard_actor, "hp", 0) > 0
    ):
        hedefler.append(tarkard_actor)
    if (
        torrmund_actor is not None
        and getattr(torrmund_actor, "active", False)
        and getattr(torrmund_actor, "hp", 0) > 0
    ):
        hedefler.append(torrmund_actor)
    return hedefler
# </POTBO_STAGE S0453>

# <POTBO_STAGE S0463>


def _stage1_dunya_aktorlerini_derinlige_gore_ciz():

    kan_lekelerini_ciz()


    for kurt in blood_maggots:
        if kurt.active:
            kurt.ciz()


    for p in blood_particles:
        if p.zemin_katmani_mi():
            p.ciz()

    fire_magic_alt_katman_ciz()

    komutlar = [
        (float(npc_y), 0, npc_ciz),
        (float(merchant_y), 1, merchant_sprite_ciz),
        (float(oyuncu_y), 2, oyuncu_sprite_ciz),
    ]



    if "blacksmith_y" in globals() and "blacksmith_world_ciz" in globals():
        komutlar.append((float(blacksmith_y), 2, blacksmith_world_ciz))

    for index, dusman in enumerate(common_enemies):
        if dusman.active and dusman.hp > 0:
            komutlar.append((float(dusman.y), 10 + index, dusman.ciz_govde))

    if tarkard_actor is not None and tarkard_actor.active and tarkard_actor.hp > 0:
        komutlar.append(
            (
                float(tarkard_actor.y),
                30,
                tarkard_actor.ciz_govde,
            )
        )
    if torrmund_actor is not None and torrmund_actor.active and torrmund_actor.hp > 0:
        komutlar.append(
            (
                float(torrmund_actor.y),
                31,
                torrmund_actor.ciz_govde,
            )
        )





    marj = 100.0 / max(0.01, KAMERA_YAKINLASTIRMA)
    gx0 = float(kamera_x) - marj
    gy0 = float(kamera_y) - marj
    gx1 = float(kamera_x) + GENISLIK / max(0.01, KAMERA_YAKINLASTIRMA) + marj
    gy1 = float(kamera_y) + YUKSEKLIK / max(0.01, KAMERA_YAKINLASTIRMA) + marj
    gorunen_gore = [g for g in gore_chunks if gx0 <= g.x <= gx1 and gy0 <= g.y <= gy1]
    if len(gorunen_gore) > V37_MAX_VISIBLE_GORE:
        gorunen_gore = gorunen_gore[-V37_MAX_VISIBLE_GORE:]
    for index, parca in enumerate(gorunen_gore):
        komutlar.append((float(parca.y), 34 + index, parca.ciz))



    for index, rat in enumerate(ambient_rats):
        if rat.active:
            komutlar.append((float(rat.y), 40 + index, rat.ciz))
    for index, projectile in enumerate(enemy_projectiles):
        if projectile.active:
            komutlar.append(
                (
                    float(projectile.y),
                    60 + index,
                    projectile.ciz,
                )
            )




    for index, patch in enumerate(player_magic_ground_fires):
        if patch.active:
            komutlar.append((float(patch.y), 65 + index, patch.ciz))

    for index, projectile in enumerate(player_magic_projectiles):
        if projectile.active:
            komutlar.append(
                (
                    float(projectile.y),
                    90 + index,
                    projectile.ciz,
                )
            )
    for index, explosion in enumerate(player_magic_explosions):
        if explosion.active:
            komutlar.append((float(explosion.y), 110 + index, explosion.ciz))

    for _, _, cizim in sorted(komutlar, key=lambda kayit: (kayit[0], kayit[1])):
        cizim()



    for p in blood_particles:
        if p.active and not p.zemin_katmani_mi():
            p.ciz()


    _simdi_fx = pygame.time.get_ticks()
    for _fx in enemy_rock_impacts:
        _fx.ciz(_simdi_fx)


    for dusman in common_enemies:
        dusman.ciz_ui()
        dusman.ciz_debug_nav()
    if tarkard_actor is not None and tarkard_actor.active:
        tarkard_actor.ciz_ui()
        tarkard_actor.ciz_debug_nav()
    if torrmund_actor is not None and torrmund_actor.active:
        torrmund_actor.ciz_ui()
        torrmund_actor.ciz_debug_nav()
# </POTBO_STAGE S0463>

# <POTBO_STAGE S0495>



for ses_adi, ses_yolu in (
    ("buttonHover1.wav", BUTTON_HOVER1_SES_YOLU),
    ("buttonClick1.wav", BUTTON_CLICK1_SES_YOLU),
    ("buttonHover2.wav", BUTTON_HOVER2_SES_YOLU),
    ("buttonClick2.wav", BUTTON_CLICK2_SES_YOLU),
    ("buySound.wav", MERCHANT_BUY_SES_YOLU),
    ("sellSound.wav", MERCHANT_SELL_SES_YOLU),
    ("noCoinSound.wav", NO_COIN_SES_YOLU),
    (
        "merchantBuySell.wav (legacy fallback)",
        MERCHANT_BUY_SELL_SES_YOLU,
    ),
    ("characterSelected.wav", CHARACTER_SELECTED_SES_YOLU),
    ("newItemSound.wav", NEW_ITEM_SES_YOLU),
    ("fireMagicCharge.wav", FIRE_MAGIC_CHARGE_SES_YOLU),
    ("fireMagicWhoosh.wav", FIRE_MAGIC_WHOOSH_SES_YOLU),
    ("fireMagicExplosion.wav", FIRE_MAGIC_EXPLOSION_SES_YOLU),
):
    if ses_yolu:
        debug_log(f"{ses_adi} bulundu:", ses_yolu)
    elif ses_adi == "noCoinSound.wav":
        debug_log("noCoinSound.wav henüz yok; eklendiğinde otomatik kullanılacak.")
    elif "legacy fallback" in ses_adi:

        pass
    else:
        print(f"{ses_adi} bulunamadı. ilgili assets/sounds klasörünü kontrol et.")
# </POTBO_STAGE S0495>

# <POTBO_STAGE S0599>





def dunya_aktorlerini_derinlige_gore_ciz():


    kan_lekelerini_ciz()
    for p in blood_particles:
        if p.active:
            p.ciz()
    for kurt in blood_maggots:
        if kurt.active:
            kurt.ciz()

    fire_magic_alt_katman_ciz()
    komutlar = [
        (float(npc_y), 0, npc_ciz),
        (float(merchant_y), 1, merchant_sprite_ciz),
        (float(oyuncu_y), 2, oyuncu_sprite_ciz),
    ]
    for index, dusman in enumerate(common_enemies):
        if dusman.active and dusman.hp > 0:
            komutlar.append((float(dusman.y), 10 + index, dusman.ciz_govde))
    if tarkard_actor is not None and tarkard_actor.active and tarkard_actor.hp > 0:
        komutlar.append(
            (
                float(tarkard_actor.y),
                30,
                tarkard_actor.ciz_govde,
            )
        )
    if torrmund_actor is not None and torrmund_actor.active and torrmund_actor.hp > 0:
        komutlar.append(
            (
                float(torrmund_actor.y),
                31,
                torrmund_actor.ciz_govde,
            )
        )

    marj = 100.0 / max(0.01, KAMERA_YAKINLASTIRMA)
    gx0 = float(kamera_x) - marj
    gy0 = float(kamera_y) - marj
    gx1 = float(kamera_x) + GENISLIK / max(0.01, KAMERA_YAKINLASTIRMA) + marj
    gy1 = float(kamera_y) + YUKSEKLIK / max(0.01, KAMERA_YAKINLASTIRMA) + marj
    gorunen_gore = [g for g in gore_chunks if gx0 <= g.x <= gx1 and gy0 <= g.y <= gy1]
    for index, parca in enumerate(gorunen_gore):
        komutlar.append((float(parca.y), 34 + index, parca.ciz))
    for index, rat in enumerate(ambient_rats):
        if rat.active:
            komutlar.append((float(rat.y), 40 + index, rat.ciz))
    for index, projectile in enumerate(enemy_projectiles):
        if projectile.active:
            komutlar.append(
                (
                    float(projectile.y),
                    60 + index,
                    projectile.ciz,
                )
            )
    for index, patch in enumerate(player_magic_ground_fires):
        if patch.active:
            komutlar.append((float(patch.y), 65 + index, patch.ciz))
    for index, projectile in enumerate(player_magic_projectiles):
        if projectile.active:
            komutlar.append(
                (
                    float(projectile.y),
                    90 + index,
                    projectile.ciz,
                )
            )
    for index, explosion in enumerate(player_magic_explosions):
        if explosion.active:
            komutlar.append((float(explosion.y), 110 + index, explosion.ciz))

    for _, _, cizim in sorted(komutlar, key=lambda kayit: (kayit[0], kayit[1])):
        cizim()

    _simdi_fx = pygame.time.get_ticks()
    for _fx in enemy_rock_impacts:
        _fx.ciz(_simdi_fx)

    for dusman in common_enemies:
        dusman.ciz_ui()
        dusman.ciz_debug_nav()
    if tarkard_actor is not None and tarkard_actor.active:
        tarkard_actor.ciz_ui()
        tarkard_actor.ciz_debug_nav()
    if torrmund_actor is not None and torrmund_actor.active:
        torrmund_actor.ciz_ui()
        torrmund_actor.ciz_debug_nav()
# </POTBO_STAGE S0599>

# <POTBO_STAGE S0644>


def _v34_static_blockers():
    """Scripted movement sırasında geçilemeyecek sabit dünya aktörleri."""
    return (npc_carpisma_rect(), merchant_carpisma_rect())
# </POTBO_STAGE S0644>

# <POTBO_STAGE S0646>


def _v34_static_position_valid(x, y, allow_static_escape=False, baseline=None):
    """Map + NPC/merchant açısından oyuncu pozisyonunu değerlendirir."""
    if not _v34_player_bounds_ok(x, y):
        return False

    test_rect = oyuncu_carpisma_rect(x, y)
    baseline_rect = None
    baseline_map = 0
    if baseline is not None:
        bx, by = baseline
        baseline_rect = oyuncu_carpisma_rect(bx, by)
        baseline_map = _v34_player_map_block_count(bx, by)

    for blocker in _v34_static_blockers():
        test_area = _v34_rect_overlap_alani(test_rect, blocker)
        if test_area <= 0:
            continue
        if not allow_static_escape or baseline_rect is None:
            return False
        old_area = _v34_rect_overlap_alani(baseline_rect, blocker)
        if old_area <= 0 or test_area > old_area:
            return False

    blocked = _v34_player_map_block_count(x, y)
    if blocked > 0:
        if not allow_static_escape or baseline is None:
            return False


        if baseline_map <= 0 or blocked > baseline_map:
            return False
    return True
# </POTBO_STAGE S0646>

# <POTBO_STAGE S0658>


def _v34_special_scripted_position_apply(desired, previous=None):
    """Special body motion'u static collision'a karşı sub-step çözer.

    Dynamic enemies bilerek blocker değildir. Karakter hedefin bedeninden geçebilir;
    map, NPC ve merchant içinden geçemez. Geçerli olmayan frame'de son geçerli
    noktada kalır ve bir sonraki frame aynı fazın daha ileri örneği tekrar denenir.
    """
    global oyuncu_x, oyuncu_y
    desired = pygame.Vector2(desired)
    current = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    delta = desired - current
    length = delta.length()
    if length <= 0.001:
        return current
    n = max(1, int(math.ceil(length / V34_SCRIPT_STEP)))
    last = current.copy()
    for i in range(1, n + 1):
        p = current.lerp(desired, i / n)
        if _v34_static_position_valid(p.x, p.y):
            last = p
            continue


        x_try = pygame.Vector2(p.x, last.y)
        y_try = pygame.Vector2(last.x, p.y)
        x_ok = _v34_static_position_valid(x_try.x, x_try.y)
        y_ok = _v34_static_position_valid(y_try.x, y_try.y)
        if x_ok and not y_ok:
            last = x_try
        elif y_ok and not x_ok:
            last = y_try
        elif x_ok and y_ok:
            last = x_try if abs(delta.x) >= abs(delta.y) else y_try
        else:
            break
    oyuncu_x = float(last.x)
    oyuncu_y = float(last.y)
    return last
# </POTBO_STAGE S0658>

# <POTBO_STAGE S1119>


def _v43_base_world_renderer():
    """V37 compositor'ın kullandığı base world render; yalnız map zoom yolu değişir."""
    kamerayi_guncelle()

    if oyuncu_hp <= 0 and oyuncu_olum_baslangic_ms > 0:
        oyuncu_olum_sahnesi_ciz()
        return

    _v43_map_draw()

    dunya_aktorlerini_derinlige_gore_ciz()
    _v34_dash_trail_ciz()
    combat_impact_fx_ciz()
    gelistirici_x_skill_efekt_ciz()
    fire_magic_screen_flash_ciz()
    genel_vinyet_ciz()
    seviye_animasyonu_ciz()
    oyuncu_paneli_ciz()
    one_cikan_item_paneli_ciz()
    gelistirici_test_paneli_ciz()
    oyuncu_bayginlik_ui_ciz()
    oyuncu_kesik_efekti_ciz()
    oyuncu_olum_ui_ciz()

    if etkilesim_ipuclari and oyun_alt_durumu == HARITA and eadric_yakin_mi():
        keycap_ikonu_ciz(
            dunya_ekran_x(npc_x),
            dunya_ekran_y(npc_y) - 66,
            tus_gorunen_adi("interact"),
        )
    if etkilesim_ipuclari and oyun_alt_durumu == HARITA and merchant_yakin_mi():
        keycap_ikonu_ciz(
            dunya_ekran_x(merchant_x),
            dunya_ekran_y(merchant_y) - 70,
            tus_gorunen_adi("interact"),
        )
    if etkilesim_ipuclari and oyun_alt_durumu == HARITA and tarkard_yakin_mi():
        keycap_ikonu_ciz(
            dunya_ekran_x(tarkard_actor.x),
            dunya_ekran_y(tarkard_actor.y) - 92,
            tus_gorunen_adi("interact"),
        )
    if etkilesim_ipuclari and oyun_alt_durumu == HARITA and torrmund_yakin_mi():
        keycap_ikonu_ciz(
            dunya_ekran_x(torrmund_actor.x),
            dunya_ekran_y(torrmund_actor.y) - 96,
            tus_gorunen_adi("interact"),
        )

    ganimet_uzerinde = (
        oyun_alt_durumu == HARITA
        and npc_intro_tamamlandi
        and not ganimet_alindi
        and abs(oyuncu_x - ganimet_x) < 40
        and abs(oyuncu_y - ganimet_y) < 36
    )
    if etkilesim_ipuclari and ganimet_uzerinde:
        keycap_ikonu_ciz(
            dunya_ekran_x(ganimet_x),
            dunya_ekran_y(ganimet_y) - 38,
            tus_gorunen_adi("interact"),
        )

    if oyun_alt_durumu in (DIYALOG, DIYALOG_SECIM):
        diyalog_ciz()

    kayit_animasyonu_ciz()
    if fps_goster:
        yazi_yaz(
            f"FPS: {int(saat.get_fps())}",
            1170,
            660,
            SARI,
            mini_font,
        )
    if yeni_item_sahnesi_musait_mi() and not onemli_item_kuyrugu:
        bildirim_ciz()
    if onemli_item_penceresi_acik_mi():
        onemli_item_penceresi_ciz()
# </POTBO_STAGE S1119>

# <POTBO_STAGE S2130>
V90_DRACO_MERCHANT_PRICE = 1850
# </POTBO_STAGE S2130>

# <POTBO_STAGE S2137>




MERCHANT_STOK_FIYATLARI["draco_calcinans"] = V90_DRACO_MERCHANT_PRICE
MERCHANT_SATIS_REFERANSI["draco_calcinans"] = V90_DRACO_SELL_PRICE
MERCHANT_MAKSIMUM_TEKLIF["draco_calcinans"] = V90_DRACO_SELL_PRICE
MERCHANT_GERI_ALIM_FIYATI["draco_calcinans"] = V90_DRACO_BUYBACK_PRICE
if not any(
    isinstance(record, dict) and record.get("id") == "draco_calcinans"
    for record in MERCHANT_VERI.setdefault("stock", [])
):
    MERCHANT_VERI["stock"].append(
        {"id": "draco_calcinans", "price": V90_DRACO_MERCHANT_PRICE}
    )

_v90_merchant_item_raw = merchant_item_olustur


def merchant_item_olustur(item_id):
    if item_id == "draco_calcinans":
        return draco_calcinans_olustur()
    return _v90_merchant_item_raw(item_id)


_v90_merchant_buy_list_raw = merchant_buy_listesi


def merchant_buy_listesi():
    result = _v90_merchant_buy_list_raw()
    owns_draco = any(
        isinstance(item, dict) and item.get("id") == "draco_calcinans"
        for item in envanter_itemleri
    )
    has_buyback = any(
        isinstance(record, dict) and record.get("id") == "draco_calcinans"
        for record in merchant_geri_alim_listesi
    )
    if owns_draco or has_buyback:
        result = [
            record
            for record in result
            if not (
                isinstance(record, dict)
                and record.get("id") == "draco_calcinans"
                and record.get("source") == "stock"
            )
        ]
    return result
# </POTBO_STAGE S2137>

# <POTBO_STAGE S2241>



V90_DRACO_MERCHANT_PRICE = 2300
MERCHANT_STOK_FIYATLARI["draco_calcinans"] = 2300
for _v91_stock in MERCHANT_VERI.setdefault("stock", []):
    if (
        isinstance(_v91_stock, dict)
        and _v91_stock.get("id") == "draco_calcinans"
    ):
        _v91_stock["price"] = 2300
# </POTBO_STAGE S2241>

# <POTBO_STAGE S2253>





def v91_diagnostics():
    stock_prices = [
        int(record.get("price", -1))
        for record in MERCHANT_VERI.get("stock", [])
        if (
            isinstance(record, dict)
            and record.get("id") == "draco_calcinans"
        )
    ]
    return {
        "version": V91_VERSION,
        "hud": {
            "layout_preserved": True,
            "minimap_added": False,
            "pixel_black_white_red_style": True,
            "tight_icons": True,
        },
        "sphaera": {
            "cast_frames": len(
                FIRE_MAGIC_CAST_SPRITELERI
            ),
            "explosion_frames": len(
                FIRE_MAGIC_EXPLOSION_SPRITELERI
            ),
            "ground_source": os.path.basename(
                V89_SMALL_FIRE_PATH
            ),
            "flames_per_patch": 8,
            "geometry_glow": False,
            "screen_flash": False,
            "ground_patch_cap": V38_MAX_GROUND_FIRES,
        },
        "draco": {
            "long_frames": len(V91_DRACO_LONG_FRAMES),
            "merchant_price": MERCHANT_STOK_FIYATLARI.get(
                "draco_calcinans"
            ),
            "stock_prices": stock_prices,
            "stronger_rupture": True,
            "distance_forms": True,
        },
        "blood": {
            "transient_cap": V89_BLOOD_TRANSIENT_LIMIT,
            "burst_cap": V89_BLOOD_BURST_LIMIT,
            "arterial_cap": V89_BLOOD_ARTERIAL_BURST_LIMIT,
            "permanent_decal_audit_cap": V49_DECAL_HARD_LIMIT,
            "footprint_samples_source_color": True,
            "fresh_tracks_longer_than_dry": True,
            "injury_drops_dark_and_small": True,
            "stats": dict(v91_blood_stats),
        },
        "death": {
            "palette": (
                V91_DEATH_BLACK,
                V91_DEATH_BODY,
                V91_DEATH_BLOOD,
            ),
            "flames_per_cluster": 40,
            "small_flame_sprite": os.path.basename(
                V89_SMALL_FIRE_PATH
            ),
        },
        "test_controls": {
            "toggle": '"',
            "ctrl_1": "Sphaera Exothermica",
            "ctrl_2": "Draco Calcinans",
            "ctrl_i_gold": 1000,
            "starts_hidden": not v91_test_panel_visible,
        },
        "performance": {
            "visible_gore_cap": V37_MAX_VISIBLE_GORE,
            "ground_fire_cluster_one_blit": True,
            "death_flames_one_cached_blit": True,
            "path_budget": COMMON_ENEMY_PATH_BUDGET_PER_FRAME,
            "developer_overlay_hidden_by_default": True,
        },
    }
# </POTBO_STAGE S2253>

# <POTBO_STAGE S2255>
V91_STARTUP_OK = all(
    (
        V91_STARTUP_CONTRACT["hud"][
            "layout_preserved"
        ],
        not V91_STARTUP_CONTRACT["hud"][
            "minimap_added"
        ],
        V91_STARTUP_CONTRACT["sphaera"][
            "cast_frames"
        ]
        >= 6,
        V91_STARTUP_CONTRACT["sphaera"][
            "explosion_frames"
        ]
        >= 8,
        V91_STARTUP_CONTRACT["sphaera"][
            "ground_source"
        ]
        == "ambient_small_flame_cycle.png",
        V91_STARTUP_CONTRACT["draco"][
            "long_frames"
        ]
        >= 5,
        V91_STARTUP_CONTRACT["draco"][
            "merchant_price"
        ]
        == 2300,
        all(
            price == 2300
            for price in V91_STARTUP_CONTRACT["draco"][
                "stock_prices"
            ]
        ),
        V91_STARTUP_CONTRACT["blood"][
            "transient_cap"
        ]
        <= 128,
        V91_STARTUP_CONTRACT["death"][
            "flames_per_cluster"
        ]
        >= 36,
    )
)
# </POTBO_STAGE S2255>

# <POTBO_STAGE S2259>













V92_VERSION = "92.0"
BLACKSMITH = "blacksmith"







MERCHANT_SHARED_YOLU = os.path.join(ASSETS, "npcs", "merchant", "merchant.png")
BLACKSMITH_YOLU = os.path.join(ASSETS, "npcs", "blacksmith", "blacksmith.png")
# </POTBO_STAGE S2259>

# <POTBO_STAGE S2262>


def _v92_merchant_frames_load():
    sheet = _v92_load_alpha(MERCHANT_SHARED_YOLU)
    if sheet is None:
        return []


    specs = (
        (8, 0, 45, 55),
        (53, 0, 45, 55),
        (98, 0, 45, 55),
        (21, 55, 58, 58),
        (80, 55, 58, 58),
    )
    out = []
    for spec in specs:
        area = pygame.Rect(spec).clip(sheet.get_rect())
        if area.width <= 0 or area.height <= 0:
            continue
        frame = _v92_trim(sheet.subsurface(area).copy())
        if frame is not None and frame.get_width() >= 8 and frame.get_height() >= 12:
            out.append(frame)
    return out


v92_merchant_frames = _v92_merchant_frames_load()
if v92_merchant_frames:
    merchant_resmi_orijinal = v92_merchant_frames[-2]
    merchant_resmi = resmi_oranli_sigdir(
        merchant_resmi_orijinal,
        pygame.Rect(0, 0, 72, 78),
        0,
        1.0,
        True,
    )
# </POTBO_STAGE S2262>

# <POTBO_STAGE S2269>


def oyuncu_seviye_kazanclarini_uygula(eski_level, yeni_level):
    global oyuncu_guc, oyuncu_hasari, oyuncu_max_stamina, oyuncu_stamina
    global oyuncu_max_hp, oyuncu_hp
    _v92_level_gain_raw(eski_level, yeni_level)
    if int(yeni_level) <= int(eski_level):
        return
    for lv in range(int(eski_level) + 1, int(yeni_level) + 1):
        curve = v92_level_curve(lv)

        v92_level_stats["strength"] += curve["strength"]
        v92_level_stats["speed"] += curve["speed"]
        v92_level_stats["endurance"] += curve["endurance"]
        oyuncu_guc += 1 if lv % 4 == 0 else 0
        oyuncu_hasari += 1 if lv % 5 == 0 else 0
        stamina_gain = 0.9 + curve["endurance"] * 0.55
        hp_gain = 1 + (1 if lv % 4 == 0 else 0)
        oyuncu_max_stamina += stamina_gain
        oyuncu_stamina = min(oyuncu_max_stamina, oyuncu_stamina + stamina_gain)
        oyuncu_max_hp += hp_gain
        oyuncu_hp = min(oyuncu_max_hp, oyuncu_hp + hp_gain)
    v92_resource_balance_refresh()
    v92_merchant_restock_for_level(int(yeni_level))
# </POTBO_STAGE S2269>

# <POTBO_STAGE S2275>






V90_DRACO_MERCHANT_PRICE = 3000
# </POTBO_STAGE S2275>

# <POTBO_STAGE S2278>
MERCHANT_STOK_FIYATLARI["draco_calcinans"] = 3000
MERCHANT_SATIS_REFERANSI["draco_calcinans"] = V90_DRACO_SELL_PRICE
MERCHANT_MAKSIMUM_TEKLIF["draco_calcinans"] = V90_DRACO_SELL_PRICE
MERCHANT_GERI_ALIM_FIYATI["draco_calcinans"] = V90_DRACO_BUYBACK_PRICE
MERCHANT_STOK_FIYATLARI["fire_magic"] = 3100
MERCHANT_SATIS_REFERANSI["fire_magic"] = max(900, FIRE_MAGIC_SATIS_FIYATI)
MERCHANT_MAKSIMUM_TEKLIF["fire_magic"] = MERCHANT_SATIS_REFERANSI["fire_magic"]
MERCHANT_GERI_ALIM_FIYATI["fire_magic"] = max(1120, FIRE_MAGIC_GERI_ALIM_FIYATI)
# </POTBO_STAGE S2278>

# <POTBO_STAGE S2297>





V92_MERCHANT_LEVEL_UNLOCKS = {
    "aurum_potabile": 1,
    "quinta_essentia": 2,
    "fire_magic": 4,
    "draco_calcinans": 6,
}
V92_MERCHANT_BASE_STOCK = {
    "aurum_potabile": 2,
    "quinta_essentia": 2,
    "fire_magic": 1,
    "draco_calcinans": 1,
}
V92_MERCHANT_MAX_STOCK = {
    "aurum_potabile": 8,
    "quinta_essentia": 7,
    "fire_magic": 1,
    "draco_calcinans": 1,
}
V92_MERCHANT_PRICES = {
    "aurum_potabile": 160,
    "quinta_essentia": 240,
    "fire_magic": 3100,
    "draco_calcinans": 3000,
}
for _id, _price in V92_MERCHANT_PRICES.items():
    MERCHANT_STOK_FIYATLARI[_id] = _price




V92_MERCHANT_HAGGLE_PATHS = (
    {"tr": "Kusurları tek tek göster.", "en": "List every defect.", "lev": 1.30, "risk": 0.24},
    {"tr": "Peşin ödeme teklif et.", "en": "Offer immediate payment.", "lev": 0.95, "risk": 0.10},
    {"tr": "Birden fazla alacağını söyle.", "en": "Promise a larger order.", "lev": 1.15, "risk": 0.18},
    {"tr": "Başka tüccarın fiyatını ima et.", "en": "Hint at a rival's price.", "lev": 1.25, "risk": 0.34},
    {"tr": "Sessiz kal ve fiyatı onun bozmasını bekle.", "en": "Stay silent and let him break first.", "lev": 1.05, "risk": 0.22},
    {"tr": "Eski müşteriliğini hatırlat.", "en": "Invoke your customer history.", "lev": 0.90, "risk": 0.08},
    {"tr": "Ürünün rafta kaldığını söyle.", "en": "Call out shelf age.", "lev": 1.12, "risk": 0.28},
    {"tr": "Yol masrafını bahane et.", "en": "Use travel costs as leverage.", "lev": 0.72, "risk": 0.19},
    {"tr": "Coinleri masaya sayarak koy.", "en": "Count the coins on the table.", "lev": 1.00, "risk": 0.12},
    {"tr": "Ürünü geri bırakıp çıkacakmış gibi yap.", "en": "Set it down and feign departure.", "lev": 1.42, "risk": 0.43},
    {"tr": "Kalite garantisi iste.", "en": "Demand a quality guarantee.", "lev": 0.88, "risk": 0.14},
    {"tr": "Yuvarlak rakama çek.", "en": "Push for a round number.", "lev": 0.78, "risk": 0.10},
    {"tr": "Nakit akışını sorgula.", "en": "Question his cash flow.", "lev": 1.18, "risk": 0.38},
    {"tr": "Ürünün mevsim dışı olduğunu söyle.", "en": "Call the item out of season.", "lev": 0.92, "risk": 0.20},
    {"tr": "Hızlı anlaşma karşılığı indirim iste.", "en": "Trade speed for a discount.", "lev": 1.08, "risk": 0.13},
    {"tr": "Fiyat yerine değeri tartış.", "en": "Argue value instead of price.", "lev": 1.22, "risk": 0.24},
    {"tr": "Eksik bilgi verdiğini ima et.", "en": "Suggest he omitted information.", "lev": 1.35, "risk": 0.49},
    {"tr": "Bir sonraki alışverişi bağla.", "en": "Bundle a future purchase.", "lev": 0.98, "risk": 0.12},
    {"tr": "Kayıp riskini ona bırak.", "en": "Make him carry the walk-away risk.", "lev": 1.28, "risk": 0.33},
    {"tr": "Teklifini bir kez söyle, tekrar etme.", "en": "State one offer and never repeat it.", "lev": 1.16, "risk": 0.27},
)
assert len(V92_MERCHANT_HAGGLE_PATHS) == 20
# </POTBO_STAGE S2297>

# <POTBO_STAGE S2299>

v92_merchant_stock = {}
v92_merchant_last_restock_level = 0
v92_merchant_haggle_choices = []
v92_merchant_haggle_index = 0
v92_merchant_haggle_round = 0
v92_merchant_haggle_score = 0.0
v92_merchant_haggle_seed = 0
v92_merchant_haggle_mode = "buy"
v92_merchant_quantity_input = "1"
v92_merchant_selected_quantity = 1
v92_merchant_fake_quote = None
v92_merchant_reputation = 0.0


def v92_merchant_stock_init(level=None):
    global v92_merchant_last_restock_level
    if level is None:
        level = oyuncu_level
    if not v92_merchant_stock:
        for item_id, unlock in V92_MERCHANT_LEVEL_UNLOCKS.items():
            v92_merchant_stock[item_id] = {
                "remaining": V92_MERCHANT_BASE_STOCK[item_id] if int(level) >= unlock else 0,
                "unlocked": int(level) >= unlock,
            }
    v92_merchant_last_restock_level = max(v92_merchant_last_restock_level, int(level))


def v92_merchant_restock_for_level(level):
    global v92_merchant_last_restock_level
    v92_merchant_stock_init(level)
    old_level = int(v92_merchant_last_restock_level)
    level = int(level)
    if level <= old_level:
        return
    rng = random.Random((level * 9176) ^ 0x4D3D0)
    arrivals = []
    for lv in range(old_level + 1, level + 1):

        for item_id, unlock in V92_MERCHANT_LEVEL_UNLOCKS.items():
            record = v92_merchant_stock[item_id]
            if not record.get("unlocked") and lv >= unlock:
                record["unlocked"] = True
                record["remaining"] = V92_MERCHANT_BASE_STOCK[item_id]
                arrivals.append(item_id)

        pool = [
            item_id
            for item_id in ("aurum_potabile", "quinta_essentia")
            if v92_merchant_stock[item_id].get("unlocked")
        ]
        rng.shuffle(pool)
        for item_id in pool[: rng.choice((1, 2))]:
            rec = v92_merchant_stock[item_id]
            gain = rng.choice((1, 1, 2))
            rec["remaining"] = min(
                V92_MERCHANT_MAX_STOCK[item_id], int(rec.get("remaining", 0)) + gain
            )
            arrivals.append(item_id)
    v92_merchant_last_restock_level = level
    if arrivals and oyun_durumu == OYUN:
        bildirim_goster(
            bt("Hanus'nin stoğu seviye ile yenilendi.", "Hanus's stock changed with your level."),
            V91_UI_GOLD,
        )


v92_merchant_stock_init(oyuncu_level)


def merchant_stok_urun_idleri():
    v92_merchant_stock_init()
    return {
        item_id
        for item_id, record in v92_merchant_stock.items()
        if record.get("unlocked")
    }


def merchant_buy_listesi():
    v92_merchant_stock_init()
    out = []
    order = ("aurum_potabile", "quinta_essentia", "fire_magic", "draco_calcinans")
    for item_id in order:
        rec = v92_merchant_stock.get(item_id, {})
        if not rec.get("unlocked"):
            continue
        out.append(
            {
                "id": item_id,
                "source": "stock",
                "price": int(V92_MERCHANT_PRICES[item_id]),
                "remaining": max(0, int(rec.get("remaining", 0))),
                "sold": int(rec.get("remaining", 0)) <= 0,
            }
        )
    for i, record in enumerate(merchant_geri_alim_listesi):
        if not isinstance(record, dict):
            continue
        copy = dict(record)
        copy["source"] = "buyback"
        copy["buyback_index"] = i
        copy["remaining"] = max(1, int(item_adedi(copy.get("item", {}))))
        copy["sold"] = False
        out.append(copy)
    return out


def merchant_item_olustur(item_id):
    if item_id == "aurum_potabile":
        return aurum_potabile_olustur()
    if item_id == "quinta_essentia":
        return quinta_essentia_olustur()
    if item_id == "fire_magic":
        return fire_magic_olustur()
    if item_id == "draco_calcinans":
        return draco_calcinans_olustur()
    return None


def v92_merchant_current_record():
    records = merchant_buy_listesi() if merchant_sayfa == "buy" else merchant_envanter_satiliklari()
    if not records:
        return None
    return records[merchant_index % len(records)]


def v92_merchant_begin_quantity():
    global merchant_modal, merchant_bekleyen_islem
    global v92_merchant_quantity_input, v92_merchant_selected_quantity
    record = v92_merchant_current_record()
    if not isinstance(record, dict):
        return False
    if record.get("sold"):
        merchant_diyalog_yaz(bt("Satıldı. Bir sonraki seviye stoğu değiştirebilir.", "Sold. A later level may change the stock."))
        return True
    available = max(1, int(record.get("remaining", 1)))
    item_id = record.get("id")
    if item_id in ("fire_magic", "draco_calcinans"):
        available = 1
    v92_merchant_quantity_input = "1"
    v92_merchant_selected_quantity = 1
    merchant_bekleyen_islem = {"type": "buy", "record": dict(record), "quantity": 1}
    merchant_modal = "quantity"
    merchant_diyalog_yaz(
        bt(
            f"Kaç adet? Stokta {available}. Miktarı burada yaz.",
            f"How many? {available} in stock. Type the quantity here.",
        )
    )
    return True


def v92_merchant_confirm_quantity():
    global merchant_modal, merchant_bekleyen_islem, v92_merchant_selected_quantity
    record = (merchant_bekleyen_islem or {}).get("record", {})
    available = max(1, int(record.get("remaining", 1)))
    try:
        qty = int(v92_merchant_quantity_input or "1")
    except ValueError:
        qty = 1
    qty = max(1, min(available, qty))
    if record.get("id") in ("fire_magic", "draco_calcinans"):
        qty = 1
    v92_merchant_selected_quantity = qty
    merchant_bekleyen_islem["quantity"] = qty
    merchant_bekleyen_islem["unit_price"] = int(record.get("price", 1))
    merchant_bekleyen_islem["price"] = int(record.get("price", 1)) * qty
    merchant_modal = "confirm"
    merchant_diyalog_yaz(
        bt(
            f"{qty} adet için toplam {merchant_bekleyen_islem['price']} coin. E ile onayla, F ile pazarlık et.",
            f"{merchant_bekleyen_islem['price']} coins for {qty}. Press E to accept or F to haggle.",
        )
    )


def v92_haggle_choices(seed, round_index, pool):
    rng = random.Random(int(seed) ^ (int(round_index) * 0x9E3779B1))
    indices = list(range(len(pool)))
    rng.shuffle(indices)
    return [pool[i] for i in indices[:3]]


def v92_merchant_haggle_begin():
    global merchant_modal, merchant_bekleyen_islem
    global v92_merchant_haggle_choices, v92_merchant_haggle_index
    global v92_merchant_haggle_round, v92_merchant_haggle_score
    global v92_merchant_haggle_seed, v92_merchant_haggle_mode, v92_merchant_fake_quote
    if merchant_sayfa == "buy":
        record = v92_merchant_current_record()
        if not isinstance(record, dict) or record.get("sold"):
            return False
        if not merchant_bekleyen_islem or merchant_bekleyen_islem.get("type") != "buy":
            merchant_bekleyen_islem = {
                "type": "buy",
                "record": dict(record),
                "quantity": 1,
                "unit_price": int(record.get("price", 1)),
                "price": int(record.get("price", 1)),
            }
        v92_merchant_haggle_mode = "buy"
    else:
        sale = v92_merchant_current_record()
        if not isinstance(sale, tuple) or len(sale) != 2:
            return False
        slot, item = sale
        base = int(MERCHANT_SATIS_REFERANSI.get(item.get("id"), 1))
        merchant_bekleyen_islem = {
            "type": "sell",
            "slot": slot,
            "item_id": item.get("id"),
            "quantity": 1,
            "unit_price": base,
            "price": base,
        }
        v92_merchant_haggle_mode = "sell"
    v92_merchant_haggle_round = 0
    v92_merchant_haggle_score = 0.0
    v92_merchant_haggle_index = 0
    v92_merchant_haggle_seed = (
        pygame.time.get_ticks() ^ int(oyuncu_level * 733) ^ int(oyuncu_altin * 3)
    )
    v92_merchant_fake_quote = None
    v92_merchant_haggle_choices = v92_haggle_choices(
        v92_merchant_haggle_seed, 0, V92_MERCHANT_HAGGLE_PATHS
    )
    merchant_modal = "haggle"
    merchant_diyalog_yaz(
        bt("Peki. Fiyatı konuşalım. Bir yaklaşım seç.", "Fine. Let us discuss the price. Choose an approach.")
    )
    return True


def v92_merchant_haggle_choose():
    global v92_merchant_haggle_round, v92_merchant_haggle_score
    global v92_merchant_haggle_choices, v92_merchant_haggle_index
    global merchant_modal, v92_merchant_fake_quote, v92_merchant_reputation
    if not v92_merchant_haggle_choices:
        return
    tactic = v92_merchant_haggle_choices[v92_merchant_haggle_index % len(v92_merchant_haggle_choices)]
    rng = random.Random(v92_merchant_haggle_seed ^ (v92_merchant_haggle_round * 7717) ^ int(tactic["lev"] * 1000))
    roll = rng.random()
    risk = float(tactic["risk"])
    leverage = float(tactic["lev"])
    success = roll > risk * (0.74 + max(0.0, -v92_merchant_reputation) * 0.08)
    delta = leverage * (1.0 if success else -0.75 - risk * 0.45)
    v92_merchant_haggle_score += delta
    if success:
        v92_merchant_reputation = min(3.0, v92_merchant_reputation + 0.05)
    else:
        v92_merchant_reputation = max(-3.0, v92_merchant_reputation - 0.08)

    counter_pool = V92_MEDOLI_COUNTERS_TR if dil == "TR" else V92_MEDOLI_COUNTERS_EN
    counter = rng.choice(counter_pool)


    if rng.random() < 0.20 + risk * 0.16:
        v92_merchant_fake_quote = True
        counter += bt(" Teklifinin altına küçük bir rakam karalıyor; fazla hızlı davranıyor.", " He scribbles a smaller number under the offer, a little too quickly.")
    v92_merchant_haggle_round += 1
    if v92_merchant_haggle_round >= 3:
        v92_merchant_haggle_finalize(counter)
        return
    v92_merchant_haggle_choices = v92_haggle_choices(
        v92_merchant_haggle_seed, v92_merchant_haggle_round, V92_MERCHANT_HAGGLE_PATHS
    )
    v92_merchant_haggle_index = 0
    merchant_diyalog_yaz(counter, bt("Bir kez daha bastırabilirsin.", "You can press once more."))


def v92_merchant_haggle_finalize(counter_text=""):
    global merchant_modal, merchant_onay_index
    txn = merchant_bekleyen_islem or {}
    base_unit = max(1, int(txn.get("unit_price", txn.get("price", 1))))
    quantity = max(1, int(txn.get("quantity", 1)))


    if v92_merchant_haggle_mode == "buy":
        discount = max(-0.08, min(0.24, v92_merchant_haggle_score * 0.037))
        if v92_merchant_fake_quote:
            discount -= 0.035
        final_unit = max(1, int(round(base_unit * (1.0 - discount))))
    else:
        premium = max(-0.12, min(0.34, v92_merchant_haggle_score * 0.045))
        if v92_merchant_fake_quote:
            premium -= 0.045
        final_unit = max(1, int(round(base_unit * (1.0 + premium))))
    txn["unit_price"] = final_unit
    txn["price"] = final_unit * quantity
    txn["haggle_score"] = round(v92_merchant_haggle_score, 3)
    merchant_onay_index = 1
    merchant_modal = "confirm"
    text = bt(
        f"Son yazdığı rakam: {txn['price']} coin. Hanus'nin ilk söylediğiyle aynı olmayabilir.",
        f"Final written figure: {txn['price']} coins. It may not match what Hanus first said.",
    )
    merchant_diyalog_yaz(counter_text or text, text)


def merchant_islemi_uygula():
    global oyuncu_altin, merchant_modal, merchant_bekleyen_islem, merchant_index
    txn = merchant_bekleyen_islem or {}
    if txn.get("type") == "buy":
        record = txn.get("record", {})
        qty = max(1, int(txn.get("quantity", 1)))
        total = max(1, int(txn.get("price", int(record.get("price", 1)) * qty)))
        if oyuncu_altin < total:
            no_coin_sesi_cal()
            merchant_diyalog_yaz(bt("Coinlerin bu rakama yetmiyor.", "Your coins do not reach that figure."))
            merchant_modal = None
            return
        if record.get("source") == "stock":
            stock = v92_merchant_stock.get(record.get("id"), {})
            if int(stock.get("remaining", 0)) < qty:
                merchant_diyalog_yaz(bt("O kadar kalmadı.", "That many are no longer available."))
                merchant_modal = None
                return
            item = merchant_item_olustur(record.get("id"))
        else:
            item = dict(record.get("item", {}))
            qty = 1
        if not isinstance(item, dict):
            merchant_modal = None
            return
        item["quantity"] = qty
        if not envantere_item_ekle(item, kazanimi_goster=True):
            merchant_diyalog_yaz(bt("Envanterinde yeterli yer yok.", "Your inventory lacks enough space."))
            merchant_modal = None
            return
        oyuncu_altin -= total
        merchant_islem_sesi_cal("buy")
        if record.get("source") == "stock":
            stock = v92_merchant_stock[record.get("id")]
            stock["remaining"] = max(0, int(stock.get("remaining", 0)) - qty)
        else:
            idx = record.get("buyback_index")
            if isinstance(idx, int) and 0 <= idx < len(merchant_geri_alim_listesi):
                merchant_geri_alim_listesi.pop(idx)
        dunya_olayi_kaydet("merchant_buy", item_id=str(item.get("id", "")), price=total, count=qty)
        merchant_diyalog_yaz(
            bt(f"{qty} adet için {total} coin. İş bitti.", f"{total} coins for {qty}. Done.")
        )
        item_alindi_bildirimi(item.get("name", bt("Eşya", "Item")), qty)
    elif txn.get("type") == "sell":
        slot = txn.get("slot")
        if not isinstance(slot, int) or not 0 <= slot < len(envanter_itemleri):
            merchant_modal = None
            return
        item = envanter_itemleri[slot]
        if not isinstance(item, dict) or merchant_gorev_itemi_mi(item):
            merchant_modal = None
            return
        price = max(0, int(txn.get("price", MERCHANT_SATIS_REFERANSI.get(item.get("id"), 1))))
        oyuncu_altin += price
        back = dict(item)
        back["quantity"] = 1
        merchant_geri_alim_listesi.append(
            {
                "id": item.get("id"),
                "item": back,
                "price": MERCHANT_GERI_ALIM_FIYATI.get(item.get("id"), max(1, price)),
                "name": item.get("name", ""),
            }
        )
        envanterden_bir_azalt(slot)
        merchant_islem_sesi_cal("sell")
        dunya_olayi_kaydet("merchant_sell", item_id=str(item.get("id", "")), price=price, count=1)
        merchant_diyalog_yaz(bt(f"{price} coin. Bu kez anlaştık.", f"{price} coins. This time we agree."))
    merchant_modal = None
    merchant_bekleyen_islem = None
    merchant_index = max(0, merchant_index)


def merchant_liste_satiri_ciz(rect, item, fiyat, secili, yeni=False, sold=False, remaining=None):
    rect = pygame.Rect(rect)
    base = (34, 8, 13) if secili and not sold else (10, 8, 11)
    edge = V91_UI_RED_HOT if secili and not sold else V91_UI_GREY if sold else V91_UI_RED
    merchant_panel_ciz(rect, edge, 2 if secili and not sold else 1, base)
    text_color = (82, 78, 78) if sold else V91_UI_WHITE
    price_color = (70, 66, 66) if sold else V91_UI_GOLD
    merchant_fiyat_ciz(pygame.Rect(rect.x + 10, rect.y + 12, 86, rect.height - 24), fiyat, False, price_color)
    yazi_yaz(item.get("name", ""), rect.x + 112, rect.centery, text_color, oyun_kucuk_font)
    if yeni and not sold:
        yazi_yaz(bt("YENİ", "NEW"), rect.right - 104, rect.y + 8, V91_UI_RED_HOT, mini_font)
    if sold:
        yazi_yaz(bt("SATILDI", "SOLD"), rect.right - 83, rect.centery, (92, 82, 82), mini_font, True)
    elif remaining is not None:
        yazi_yaz(f"x{remaining}", rect.right - 72, rect.bottom - 12, V91_UI_GREY, mini_font, True)
    item_ikonu_ciz(item.get("id"), pygame.Rect(rect.right - 46, rect.y + 7, 38, 38), False)


def merchant_alt_sayfa_ciz(panel):
    ust = panel.y + 74
    alt = panel.bottom - 208
    portrait = pygame.Rect(panel.x + 24, ust, 250, alt - ust)
    list_rect = pygame.Rect(portrait.right + 18, ust, 390, alt - ust)
    info = pygame.Rect(list_rect.right + 18, ust, panel.right - list_rect.right - 42, alt - ust)
    merchant_karakter_ciz(portrait)
    merchant_panel_ciz(list_rect, V91_UI_RED, 1)
    yazi_yaz(bt("SAT", "SELL") if merchant_sayfa == "sell" else bt("AL", "BUY"), list_rect.centerx, list_rect.y + 28, V91_UI_RED_HOT, normal_font, True)
    records = merchant_aktif_liste()
    if not records:
        yazi_yaz(bt("Liste boş.", "The list is empty."), list_rect.centerx, list_rect.centery, V91_UI_GREY, kucuk_font, True)
        merchant_panel_ciz(info, V91_UI_RED, 1)
        return
    selection = merchant_index % len(records)
    start = max(0, min(selection - 2, max(0, len(records) - 6)))
    for row_no, record in enumerate(records[start : start + 6]):
        idx = start + row_no
        sold = False
        remaining = None
        if merchant_sayfa == "sell":
            _, item = record
            price = int(MERCHANT_SATIS_REFERANSI.get(item.get("id"), 1))
        else:
            if record.get("source") == "buyback" and isinstance(record.get("item"), dict):
                item = record["item"]
            else:
                item = merchant_item_olustur(record.get("id")) or {"id": record.get("id"), "name": ""}
            price = int(record.get("price", 1))
            sold = bool(record.get("sold"))
            remaining = int(record.get("remaining", 0))
        new = merchant_sayfa == "buy" and record.get("source") == "stock" and str(record.get("id")) in merchant_yeni_urun_idleri()
        merchant_liste_satiri_ciz(
            pygame.Rect(list_rect.x + 12, list_rect.y + 54 + row_no * 58, list_rect.width - 24, 50),
            item,
            price,
            idx == selection,
            new,
            sold,
            remaining,
        )
    record = records[selection]
    if merchant_sayfa == "sell":
        _, item = record
        price = int(MERCHANT_SATIS_REFERANSI.get(item.get("id"), 1))
    else:
        item = record.get("item") if record.get("source") == "buyback" else merchant_item_olustur(record.get("id"))
        item = item if isinstance(item, dict) else {"name": "", "id": record.get("id")}
        price = int(record.get("price", 1))
    merchant_item_bilgi_ciz(info, item, price)
    yazi_yaz(
        bt("E: SEÇ / MİKTAR     F: PAZARLIK", "E: SELECT / QUANTITY     F: HAGGLE"),
        list_rect.centerx,
        list_rect.bottom - 18,
        V91_UI_GREY,
        mini_font,
        True,
    )


def merchant_karakter_ciz(rect):
    merchant_panel_ciz(rect, V91_UI_RED, 1)
    frame = None
    if v92_merchant_frames:
        frame = v92_merchant_frames[-2 + ((pygame.time.get_ticks() // 520) % 2)]
    elif merchant_resmi_orijinal is not None:
        frame = merchant_resmi_orijinal
    if frame is not None:
        target = rect.inflate(-34, -26)
        image = resmi_oranli_sigdir(frame, target, 0, 1.0, True)
        if image is not None:
            ekran.blit(image, image.get_rect(center=target.center))


def merchant_sprite_ciz():
    frame = None
    if v92_merchant_frames:
        frame = v92_merchant_frames[(pygame.time.get_ticks() // 330) % min(3, len(v92_merchant_frames))]
    elif merchant_resmi is not None:
        frame = merchant_resmi
    if frame is None:
        return
    target_h = 70
    scale = target_h / max(1.0, float(frame.get_height()))
    image = pygame.transform.scale(frame, (max(1, int(round(frame.get_width() * scale))), target_h))
    ekran.blit(image, image.get_rect(midbottom=(int(dunya_ekran_x(merchant_x)), int(dunya_ekran_y(merchant_y)))))


def merchant_diyalog_kutusu_ciz(panel):
    box = pygame.Rect(panel.x + 24, panel.bottom - 190, panel.width - 48, 154)
    merchant_panel_ciz(box, V91_UI_RED, 2)
    yazi_yaz("MEDOLI", box.x + 20, box.y + 25, V91_UI_RED_HOT, normal_font)
    if merchant_modal == "quantity":
        record = (merchant_bekleyen_islem or {}).get("record", {})
        available = max(1, int(record.get("remaining", 1)))
        yazi_yaz(bt("MİKTAR", "QUANTITY"), box.x + 20, box.y + 58, V91_UI_GREY, mini_font)
        field = pygame.Rect(box.x + 118, box.y + 49, 128, 35)
        merchant_panel_ciz(field, V91_UI_WHITE, 1, V91_UI_BLACK)
        yazi_yaz(v92_merchant_quantity_input or "0", field.centerx, field.centery, V91_UI_WHITE, normal_font, True)
        yazi_yaz(bt(f"Stok: {available} · ENTER/E: onay · F: pazarlık", f"Stock: {available} · ENTER/E: confirm · F: haggle"), box.x + 20, box.y + 101, ACIK_GRI, mini_font)
        return
    if merchant_modal == "haggle":
        yazi_yaz(bt(f"PAZARLIK {v92_merchant_haggle_round + 1}/3", f"HAGGLE {v92_merchant_haggle_round + 1}/3"), box.x + 20, box.y + 57, V91_UI_GOLD, mini_font)
        for i, tactic in enumerate(v92_merchant_haggle_choices):
            selected = i == v92_merchant_haggle_index
            text = tactic["tr" if dil == "TR" else "en"]
            yazi_yaz(("> " if selected else "  ") + text, box.x + 20, box.y + 80 + i * 21, V91_UI_WHITE if selected else V91_UI_GREY, mini_font)
        return
    lines = metni_satirlara_bol(merchant_diyalog_gorunen_metin() or "...", oyun_kucuk_font, box.width - 40)
    for i, line in enumerate(lines[:4]):
        yazi_yaz(line, box.x + 20, box.y + 58 + i * 21, ACIK_GRI, oyun_kucuk_font)


def merchant_modal_ciz(panel):


    if merchant_modal != "confirm":
        return
    txn = merchant_bekleyen_islem or {}
    total = int(txn.get("price", 0))
    box = pygame.Rect(panel.right - 342, panel.bottom - 184, 288, 62)
    merchant_panel_ciz(box, V91_UI_RED_HOT, 2, V91_UI_BLACK)
    yazi_yaz(bt(f"E: ONAYLA  ·  {total} coin", f"E: ACCEPT  ·  {total} coin"), box.centerx, box.centery, V91_UI_WHITE, mini_font, True)


def v92_merchant_handle_event(olay):
    global merchant_index, merchant_menu_index, merchant_modal, merchant_bekleyen_islem
    global v92_merchant_quantity_input, v92_merchant_haggle_index
    merchant_fade_bitti = pygame.time.get_ticks() - merchant_acilis_zamani >= MERCHANT_ACILIS_FADE_SURESI
    if olay.type != pygame.KEYDOWN or not merchant_fade_bitti or merchant_kapanis_isteniyor or merchant_kapanis_zamani:
        return
    if merchant_modal == "quantity":
        if olay.key == pygame.K_ESCAPE:
            merchant_modal = None
            merchant_bekleyen_islem = None
        elif olay.key == pygame.K_BACKSPACE:
            v92_merchant_quantity_input = v92_merchant_quantity_input[:-1]
        elif olay.key == pygame.K_f:
            v92_merchant_haggle_begin()
        elif olay.key in (pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_e):
            v92_merchant_confirm_quantity()
        elif olay.unicode.isdigit() and len(v92_merchant_quantity_input) < 2:
            v92_merchant_quantity_input += olay.unicode
        return
    if merchant_modal == "haggle":
        if olay.key == pygame.K_ESCAPE:
            merchant_modal = None
        elif olay.key in ui_yukari_tuslari():
            v92_merchant_haggle_index = (v92_merchant_haggle_index - 1) % max(1, len(v92_merchant_haggle_choices))
        elif olay.key in ui_asagi_tuslari():
            v92_merchant_haggle_index = (v92_merchant_haggle_index + 1) % max(1, len(v92_merchant_haggle_choices))
        elif olay.key in (pygame.K_e, pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE):
            v92_merchant_haggle_choose()
        return
    if merchant_modal == "confirm":
        if olay.key == pygame.K_ESCAPE:
            merchant_modal = None
            merchant_bekleyen_islem = None
        elif olay.key == pygame.K_f:
            v92_merchant_haggle_begin()
        elif olay.key in (pygame.K_e, pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE):
            merchant_islemi_uygula()
        return
    if merchant_modal is None and olay.key in ONAY_TUSLARI and not merchant_yazi_tamamlandi:
        merchant_diyalog_tamamla()
        return
    if olay.key == pygame.K_ESCAPE:
        if merchant_sayfa == "menu":
            merchant_kapat()
        else:
            merchant_alt_menu_geri()
    elif olay.key in ui_yukari_tuslari():
        if merchant_sayfa == "menu":
            merchant_menu_index = (merchant_menu_index - 1) % 3
        else:
            records = merchant_aktif_liste()
            if records:
                merchant_index = (merchant_index - 1) % len(records)
    elif olay.key in ui_asagi_tuslari():
        if merchant_sayfa == "menu":
            merchant_menu_index = (merchant_menu_index + 1) % 3
        else:
            records = merchant_aktif_liste()
            if records:
                merchant_index = (merchant_index + 1) % len(records)
    elif merchant_sayfa == "menu" and olay.key in (pygame.K_e, pygame.K_RETURN, pygame.K_SPACE):
        merchant_menu_secimini_ac()
    elif merchant_sayfa == "buy" and olay.key == pygame.K_e:
        v92_merchant_begin_quantity()
    elif merchant_sayfa in ("buy", "sell") and olay.key == pygame.K_f:
        v92_merchant_haggle_begin()
    elif merchant_sayfa == "sell" and olay.key == pygame.K_e:

        sale = v92_merchant_current_record()
        if isinstance(sale, tuple) and len(sale) == 2:
            slot, item = sale
            base = int(MERCHANT_SATIS_REFERANSI.get(item.get("id"), 1))
            merchant_bekleyen_islem = {"type": "sell", "slot": slot, "item_id": item.get("id"), "quantity": 1, "unit_price": base, "price": base}
            merchant_modal = "confirm"
            merchant_diyalog_yaz(bt(f"Teklifim {base} coin. E ile kabul et, F ile pazarlık yap.", f"My offer is {base} coins. E accepts; F haggles."))





blacksmith_x = float(MERCHANT_VERI.get("blacksmith_x", merchant_x + 248.0))
blacksmith_y = float(MERCHANT_VERI.get("blacksmith_y", merchant_y + 28.0))
blacksmith_resmi_orijinal = _v92_load_alpha(BLACKSMITH_YOLU)
if blacksmith_resmi_orijinal is not None:

    converted = blacksmith_resmi_orijinal.copy()
    for px in range(converted.get_width()):
        for py in range(converted.get_height()):
            c = converted.get_at((px, py))
            if c.g > 130 and c.g > c.r * 1.30 and c.g > c.b * 1.25:
                converted.set_at((px, py), (0, 0, 0, 0))
    blacksmith_resmi_orijinal = _v92_trim(converted)

blacksmith_menu_index = 0
blacksmith_sayfa = "menu"
blacksmith_index = 0
blacksmith_modal = None
blacksmith_mesaji = ""
blacksmith_fiyat = 0
blacksmith_pending = None
blacksmith_weight_index = 1
blacksmith_haggle_choices = []
blacksmith_haggle_index = 0
blacksmith_haggle_round = 0
blacksmith_haggle_score = 0.0
blacksmith_seed = 0
v92_blacksmith_upgrades = {"weapon": 0, "armor": 0, "endurance": 0}
# </POTBO_STAGE S2299>

# <POTBO_STAGE S2301>

V92_BLACKSMITH_HAGGLE_PATHS = (
    {"tr": "Malzemeyi kendin getir.", "en": "Provide your own material.", "lev": 1.20, "risk": 0.12},
    {"tr": "İşçilik süresini kısaltmayı teklif et.", "en": "Offer a shorter workmanship window.", "lev": 0.86, "risk": 0.16},
    {"tr": "Çeliğin kusurunu göster.", "en": "Point out a flaw in the steel.", "lev": 1.16, "risk": 0.22},
    {"tr": "Bir sonraki geliştirmeyi de ona vereceğini söyle.", "en": "Promise the next upgrade too.", "lev": 1.05, "risk": 0.10},
    {"tr": "Eski zırh parçasını takasa bırak.", "en": "Trade in an old armor piece.", "lev": 1.24, "risk": 0.18},
    {"tr": "Yalnız gerekli perçinleri değiştirmesini iste.", "en": "Ask him to replace only necessary rivets.", "lev": 0.92, "risk": 0.08},
    {"tr": "Ustalık ücretini malzemeden ayır.", "en": "Separate labor from material cost.", "lev": 1.34, "risk": 0.25},
    {"tr": "Acil olmadığını söyle.", "en": "Tell him the job is not urgent.", "lev": 1.08, "risk": 0.09},
    {"tr": "Aynı işi başka demircinin yapacağını ima et.", "en": "Hint another smith can do it.", "lev": 1.28, "risk": 0.36},
    {"tr": "Ölçü hatasının riskini paylaşmasını iste.", "en": "Ask him to share fitting risk.", "lev": 1.02, "risk": 0.20},
    {"tr": "İşin bir bölümünü kendin sök.", "en": "Disassemble part of it yourself.", "lev": 1.12, "risk": 0.11},
    {"tr": "Peşin yarısını teklif et.", "en": "Offer half up front.", "lev": 0.94, "risk": 0.07},
    {"tr": "Ağırlık toleransını genişlet.", "en": "Relax the weight tolerance.", "lev": 0.88, "risk": 0.08},
    {"tr": "Süsleme istemediğini belirt.", "en": "Decline decorative work.", "lev": 0.98, "risk": 0.05},
    {"tr": "Kenar sertliğini tek bölgede iste.", "en": "Request edge hardening only where needed.", "lev": 1.10, "risk": 0.12},
    {"tr": "Hurda değerini hesaba kat.", "en": "Credit the scrap value.", "lev": 1.26, "risk": 0.18},
    {"tr": "Saat hesabını sorgula.", "en": "Challenge his labor-hour estimate.", "lev": 1.31, "risk": 0.31},
    {"tr": "Teslimde test etmeyi şart koş.", "en": "Require a test on delivery.", "lev": 0.82, "risk": 0.14},
    {"tr": "Kusurlu çıkarsa ücretsiz düzeltme iste.", "en": "Ask for free correction if flawed.", "lev": 0.90, "risk": 0.19},
    {"tr": "Tek rakam söyle ve sus.", "en": "Name one figure and go silent.", "lev": 1.22, "risk": 0.27},
)
assert len(V92_BLACKSMITH_HAGGLE_PATHS) == 20


def blacksmith_yakin_mi():
    return abs(float(oyuncu_x) - blacksmith_x) < 74 and abs(float(oyuncu_y) - blacksmith_y) < 68


def v92_blacksmith_actor_surface():
    if blacksmith_resmi_orijinal is not None:
        return blacksmith_resmi_orijinal

    surf = pygame.Surface((42, 68), pygame.SRCALPHA)
    pygame.draw.circle(surf, (78, 72, 73, 255), (21, 12), 9)
    pygame.draw.polygon(surf, (53, 49, 51, 255), [(10, 22), (32, 22), (38, 60), (4, 60)])
    pygame.draw.rect(surf, (112, 83, 48, 255), (6, 30, 30, 5))
    pygame.draw.rect(surf, (92, 89, 92, 255), (30, 17, 8, 26))
    return surf


def blacksmith_world_ciz():
    frame = v92_blacksmith_actor_surface()
    if frame is None:
        return
    h = 74
    scale = h / max(1.0, float(frame.get_height()))
    image = pygame.transform.scale(frame, (max(1, int(round(frame.get_width() * scale))), h))
    ekran.blit(image, image.get_rect(midbottom=(int(dunya_ekran_x(blacksmith_x)), int(dunya_ekran_y(blacksmith_y)))))
# </POTBO_STAGE S2301>

# <POTBO_STAGE S2304>


def blacksmith_ac():
    global oyun_durumu, blacksmith_sayfa, blacksmith_menu_index, blacksmith_index
    global blacksmith_modal, blacksmith_mesaji
    blacksmith_sayfa = "menu"
    blacksmith_menu_index = 0
    blacksmith_index = 0
    blacksmith_modal = None
    blacksmith_mesaji = bt("Çeliği konuşacaksan konuş. Üç iş yaparım: öğretirim, geliştiririm, gönderirim.", "If it is steel, speak. I do three things: teach, improve, and send you away.")
    oyun_durumu = BLACKSMITH
    return True


def blacksmith_kapat():
    global oyun_durumu, blacksmith_modal
    blacksmith_modal = None
    oyun_durumu = OYUN
# </POTBO_STAGE S2304>

# <POTBO_STAGE S2306>


def _v34_interaction_candidates():
    candidates = list(_v92_interaction_candidates_raw())
    player = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    point = pygame.Vector2(blacksmith_x, blacksmith_y)
    distance = player.distance_to(point)
    if distance <= 96.0:
        candidates.append(
            _v34_interaction_candidate(
                "blacksmith", None, blacksmith_x, blacksmith_y, distance, blacksmith_ac
            )
        )
    candidates.sort(key=lambda c: c["score"])
    return candidates
# </POTBO_STAGE S2306>

# <POTBO_STAGE S2310>


def v92_blacksmith_upgrade_cost(kind):
    level = int(v92_blacksmith_upgrades.get(kind, 0))
    base = {"weapon": 210, "armor": 190, "endurance": 175}.get(kind, 180)
    return int(round(base * (1.0 + level * 0.48 + level * level * 0.055)))


def v92_blacksmith_upgrade_apply(kind, price):
    global oyuncu_altin, oyuncu_hasari, oyuncu_max_stamina, oyuncu_stamina
    global oyuncu_max_hp, oyuncu_hp, v92_armor_rating
    if oyuncu_altin < price:
        no_coin_sesi_cal()
        return False
    oyuncu_altin -= int(price)
    tier = int(v92_blacksmith_upgrades.get(kind, 0)) + 1
    v92_blacksmith_upgrades[kind] = tier
    if kind == "weapon":
        oyuncu_hasari += 2 + tier // 3
    elif kind == "armor":
        v92_armor_rating = min(0.30, v92_armor_rating + 0.032 + min(0.012, tier * 0.0015))
    else:
        gain = 4.5 + min(3.0, tier * 0.35)
        oyuncu_max_stamina += gain
        oyuncu_stamina = min(oyuncu_max_stamina, oyuncu_stamina + gain)
        oyuncu_max_hp += 2
        oyuncu_hp = min(oyuncu_max_hp, oyuncu_hp + 2)
    merchant_islem_sesi_cal("buy")
    return True


def v92_blacksmith_haggle_begin(kind):
    global blacksmith_modal, blacksmith_haggle_choices, blacksmith_haggle_index
    global blacksmith_haggle_round, blacksmith_haggle_score, blacksmith_seed
    global blacksmith_pending, blacksmith_fiyat, blacksmith_mesaji
    blacksmith_pending = {"type": "upgrade", "kind": kind}
    blacksmith_fiyat = v92_blacksmith_upgrade_cost(kind)
    blacksmith_haggle_round = 0
    blacksmith_haggle_score = 0.0
    blacksmith_haggle_index = 0
    blacksmith_seed = pygame.time.get_ticks() ^ (oyuncu_level * 811) ^ (blacksmith_fiyat * 7)
    blacksmith_haggle_choices = v92_haggle_choices(blacksmith_seed, 0, V92_BLACKSMITH_HAGGLE_PATHS)
    blacksmith_modal = "haggle"
    blacksmith_mesaji = bt("İşçilik fiyatını düşürmek istiyorsan nedenini düzgün seç.", "If you want labor cheaper, choose your reason carefully.")


def v92_blacksmith_haggle_choose():
    global blacksmith_haggle_round, blacksmith_haggle_score, blacksmith_haggle_index
    global blacksmith_haggle_choices, blacksmith_modal, blacksmith_fiyat, blacksmith_mesaji
    tactic = blacksmith_haggle_choices[blacksmith_haggle_index % len(blacksmith_haggle_choices)]
    rng = random.Random(blacksmith_seed ^ (blacksmith_haggle_round * 4909) ^ int(tactic["lev"] * 1000))
    success = rng.random() > float(tactic["risk"])
    blacksmith_haggle_score += float(tactic["lev"]) * (1.0 if success else -0.70)
    blacksmith_haggle_round += 1
    if blacksmith_haggle_round >= 3:
        discount = max(-0.05, min(0.22, blacksmith_haggle_score * 0.036))
        blacksmith_fiyat = max(1, int(round(v92_blacksmith_upgrade_cost(blacksmith_pending["kind"]) * (1.0 - discount))))
        blacksmith_modal = "confirm"
        blacksmith_mesaji = bt(f"İşçilik ve malzeme: {blacksmith_fiyat} coin. Son rakam.", f"Labor and material: {blacksmith_fiyat} coins. Final figure.")
        return
    blacksmith_haggle_choices = v92_haggle_choices(blacksmith_seed, blacksmith_haggle_round, V92_BLACKSMITH_HAGGLE_PATHS)
    blacksmith_haggle_index = 0
    blacksmith_mesaji = bt("Demirci çenesini sıkar. Bir argüman daha dinleyecek.", "The smith tightens his jaw. He will hear one more argument.")


def v92_blacksmith_train(skill_id):
    global oyuncu_altin, gelistirici_x_skill_aktif, blacksmith_mesaji
    cost = 67
    if int(v92_training.get(skill_id, 0)) >= 5:
        name = "Decussatio Rubra" if skill_id == "decussatio_rubra" else "Catena Decollationis"
        blacksmith_mesaji = bt(
            f"{name} zaten kas hafızana yerleşti. Bunun için daha fazla saat satmam.",
            f"{name} is already in your muscle memory. I will not sell you more hours for it.",
        )
        return
    if oyuncu_altin < cost:
        no_coin_sesi_cal()
        blacksmith_mesaji = bt("67 altının yoksa bir saatim de yok.", "No 67 gold, no hour of mine.")
        return
    oyuncu_altin -= cost
    v92_training[skill_id] = min(5, int(v92_training.get(skill_id, 0)) + 1)
    merchant_islem_sesi_cal("buy")
    if skill_id == "decussatio_rubra" and v92_training[skill_id] >= 5:
        gelistirici_x_skill_aktif = True
    name = "Decussatio Rubra" if skill_id == "decussatio_rubra" else "Catena Decollationis"
    blacksmith_mesaji = bt(
        f"{name}: {v92_training[skill_id]}/5 saat. Her saat 67 altın.",
        f"{name}: {v92_training[skill_id]}/5 hours. Each hour costs 67 gold.",
    )


def blacksmith_ekrani_ciz():
    oyun_ekrani_ciz()
    koyu_kaplama(210)
    panel = pygame.Rect(60, 40, GENISLIK - 120, YUKSEKLIK - 80)
    v89_medieval_panel(panel, V91_UI_RED, 252)
    yazi_yaz("BLACKSMITH", panel.x + 28, panel.y + 28, V91_UI_WHITE, menu_baslik_font)
    yazi_yaz(str(oyuncu_altin), panel.right - 48, panel.y + 31, V91_UI_GOLD, normal_font, False)
    if blacksmith_sayfa == "menu":
        options = (bt("YETENEK", "SKILL"), bt("GELİŞTİR", "UPGRADE"), bt("ÇIKIŞ", "EXIT"))
        for i, text in enumerate(options):
            rect = pygame.Rect(panel.centerx - 230, panel.y + 145 + i * 96, 460, 70)
            merchant_menu_butonu_ciz(rect, text, blacksmith_menu_index == i)
    elif blacksmith_sayfa == "upgrade":
        left = pygame.Rect(panel.x + 28, panel.y + 92, 260, 360)
        right = pygame.Rect(panel.right - 288, panel.y + 92, 260, 360)
        center = pygame.Rect(left.right + 22, panel.y + 92, right.x - left.right - 44, 360)
        merchant_panel_ciz(left, V91_UI_RED, 1)
        merchant_panel_ciz(right, V91_UI_RED, 1)
        merchant_panel_ciz(center, V91_UI_RED, 1)
        smith = v92_blacksmith_actor_surface()
        if smith is not None:
            image = resmi_oranli_sigdir(smith, left.inflate(-35, -35), 0, 1.0, True)
            if image is not None:
                ekran.blit(image, image.get_rect(center=left.center))
        player = v84_player_silhouette()
        if player is not None:
            ekran.blit(player, player.get_rect(center=right.center))
        rows = (
            ("weapon", bt("SİLAH GÜCÜ", "WEAPON POWER")),
            ("armor", bt("ZIRH DAYANIKLILIĞI", "ARMOR DURABILITY")),
            ("endurance", bt("DAYANIKLILIK", "ENDURANCE")),
        )
        for i, (kind, label) in enumerate(rows):
            row = pygame.Rect(center.x + 16, center.y + 38 + i * 88, center.width - 32, 68)
            merchant_menu_butonu_ciz(row, label, blacksmith_index == i)
            yazi_yaz(f"{v92_blacksmith_upgrade_cost(kind)} coin", row.centerx, row.bottom - 14, V91_UI_GOLD, mini_font, True)
        yazi_yaz(bt("E: seç · F: pazarlık", "E: select · F: haggle"), center.centerx, center.bottom - 28, V91_UI_GREY, mini_font, True)
    else:
        rows = (
            ("decussatio_rubra", "Decussatio Rubra", bt("J basılı tut · R", "Hold J · R")),
            ("catena_decollationis", "Catena Decollationis", bt("J basılı tut · Dash", "Hold J · Dash")),
        )
        for i, (skill, name, key) in enumerate(rows):
            rect = pygame.Rect(panel.x + 110, panel.y + 140 + i * 150, panel.width - 220, 112)
            merchant_panel_ciz(rect, V91_UI_RED_HOT if blacksmith_index == i else V91_UI_GREY, 2 if blacksmith_index == i else 1)
            yazi_yaz(name, rect.x + 22, rect.y + 20, V91_UI_WHITE, normal_font)
            yazi_yaz(key, rect.x + 22, rect.y + 54, V91_UI_GREY, mini_font)
            progress = int(v92_training.get(skill, 0))
            status = bt("ÖĞRENİLDİ", "LEARNED") if progress >= 5 else f"{progress}/5 · 67 coin/saat"
            yazi_yaz(status, rect.right - 22, rect.y + 24, V91_UI_GOLD, mini_font, False)
        yazi_yaz(bt("E: 1 saat eğitim", "E: train 1 hour"), panel.centerx, panel.bottom - 142, V91_UI_GREY, mini_font, True)

    dialogue = pygame.Rect(panel.x + 28, panel.bottom - 114, panel.width - 56, 80)
    merchant_panel_ciz(dialogue, V91_UI_RED, 1)
    if blacksmith_modal == "haggle":
        for i, tactic in enumerate(blacksmith_haggle_choices):
            text = tactic["tr" if dil == "TR" else "en"]
            yazi_yaz(("> " if i == blacksmith_haggle_index else "  ") + text, dialogue.x + 18, dialogue.y + 10 + i * 21, V91_UI_WHITE if i == blacksmith_haggle_index else V91_UI_GREY, mini_font)
    elif blacksmith_modal == "weight":
        choices = (bt("HAFİFLET", "LIGHTEN"), bt("DENGELİ", "BALANCED"), bt("AĞIRLAŞTIR", "HEAVIER"))
        yazi_yaz(bt("Zırhın ağırlığını nasıl ayarlayayım?", "How should I tune the armor weight?"), dialogue.x + 18, dialogue.y + 10, V91_UI_WHITE, mini_font)
        yazi_yaz("   ".join((">" if i == blacksmith_weight_index else " ") + x for i, x in enumerate(choices)), dialogue.x + 18, dialogue.y + 42, V91_UI_GOLD, mini_font)
    else:
        lines = metni_satirlara_bol(blacksmith_mesaji or "...", mini_font, dialogue.width - 36)
        for i, line in enumerate(lines[:3]):
            yazi_yaz(line, dialogue.x + 18, dialogue.y + 12 + i * 21, ACIK_GRI, mini_font)


def v92_blacksmith_handle_event(olay):
    global blacksmith_menu_index, blacksmith_index, blacksmith_sayfa, blacksmith_modal
    global blacksmith_haggle_index, blacksmith_weight_index, blacksmith_pending
    global blacksmith_fiyat, v92_armor_weight, blacksmith_mesaji
    if olay.type != pygame.KEYDOWN:
        return
    if blacksmith_modal == "haggle":
        if olay.key == pygame.K_ESCAPE:
            blacksmith_modal = None
        elif olay.key in ui_yukari_tuslari():
            blacksmith_haggle_index = (blacksmith_haggle_index - 1) % 3
        elif olay.key in ui_asagi_tuslari():
            blacksmith_haggle_index = (blacksmith_haggle_index + 1) % 3
        elif olay.key in (pygame.K_e, pygame.K_RETURN, pygame.K_SPACE):
            v92_blacksmith_haggle_choose()
        return
    if blacksmith_modal == "weight":
        if olay.key in ui_sol_tuslari() + ui_yukari_tuslari():
            blacksmith_weight_index = (blacksmith_weight_index - 1) % 3
        elif olay.key in ui_sag_tuslari() + ui_asagi_tuslari():
            blacksmith_weight_index = (blacksmith_weight_index + 1) % 3
        elif olay.key in (pygame.K_e, pygame.K_RETURN, pygame.K_SPACE):
            v92_armor_weight = ("light", "balanced", "heavy")[blacksmith_weight_index]
            if blacksmith_pending and v92_blacksmith_upgrade_apply("armor", blacksmith_fiyat):
                blacksmith_mesaji = bt("Ayarlandı. Ağırlık koruma ve hız arasında gerçek bir takastır.", "Adjusted. Weight is a real trade between protection and speed.")
            blacksmith_modal = None
            blacksmith_pending = None
        elif olay.key == pygame.K_ESCAPE:
            blacksmith_modal = None
        return
    if blacksmith_modal == "confirm":
        if olay.key == pygame.K_ESCAPE:
            blacksmith_modal = None
        elif olay.key == pygame.K_f and blacksmith_pending:
            v92_blacksmith_haggle_begin(blacksmith_pending["kind"])
        elif olay.key in (pygame.K_e, pygame.K_RETURN, pygame.K_SPACE):
            kind = (blacksmith_pending or {}).get("kind")
            if kind == "armor":
                blacksmith_weight_index = ("light", "balanced", "heavy").index(v92_armor_weight)
                blacksmith_modal = "weight"
                blacksmith_mesaji = bt("Önce ağırlık profilini seç.", "Choose the armor weight profile first.")
            elif kind and v92_blacksmith_upgrade_apply(kind, blacksmith_fiyat):
                blacksmith_mesaji = bt("İş bitti.", "The work is done.")
                blacksmith_modal = None
                blacksmith_pending = None
        return

    if olay.key == pygame.K_ESCAPE:
        if blacksmith_sayfa == "menu":
            blacksmith_kapat()
        else:
            blacksmith_sayfa = "menu"
            blacksmith_index = 0
        return
    if blacksmith_sayfa == "menu":
        if olay.key in ui_yukari_tuslari():
            blacksmith_menu_index = (blacksmith_menu_index - 1) % 3
        elif olay.key in ui_asagi_tuslari():
            blacksmith_menu_index = (blacksmith_menu_index + 1) % 3
        elif olay.key in (pygame.K_e, pygame.K_RETURN, pygame.K_SPACE):
            if blacksmith_menu_index == 0:
                blacksmith_sayfa = "skills"
                blacksmith_index = 0
                blacksmith_mesaji = bt("Beş saat tekrar etmeden kas hafızası oluşmaz.", "Muscle memory does not appear before five hours of repetition.")
            elif blacksmith_menu_index == 1:
                blacksmith_sayfa = "upgrade"
                blacksmith_index = 0
                blacksmith_mesaji = bt("Ne güçlendireceğini seç.", "Choose what you want strengthened.")
            else:
                blacksmith_kapat()
        return
    if blacksmith_sayfa == "upgrade":
        kinds = ("weapon", "armor", "endurance")
        if olay.key in ui_yukari_tuslari():
            blacksmith_index = (blacksmith_index - 1) % 3
        elif olay.key in ui_asagi_tuslari():
            blacksmith_index = (blacksmith_index + 1) % 3
        elif olay.key == pygame.K_f:
            v92_blacksmith_haggle_begin(kinds[blacksmith_index])
        elif olay.key in (pygame.K_e, pygame.K_RETURN, pygame.K_SPACE):
            kind = kinds[blacksmith_index]
            blacksmith_pending = {"type": "upgrade", "kind": kind}
            blacksmith_fiyat = v92_blacksmith_upgrade_cost(kind)
            blacksmith_modal = "confirm"
            blacksmith_mesaji = bt(f"{blacksmith_fiyat} coin. F pazarlık, E kabul.", f"{blacksmith_fiyat} coins. F haggles; E accepts.")
        return
    if blacksmith_sayfa == "skills":
        skills = ("decussatio_rubra", "catena_decollationis")
        if olay.key in ui_yukari_tuslari():
            blacksmith_index = (blacksmith_index - 1) % 2
        elif olay.key in ui_asagi_tuslari():
            blacksmith_index = (blacksmith_index + 1) % 2
        elif olay.key in (pygame.K_e, pygame.K_RETURN, pygame.K_SPACE):
            v92_blacksmith_train(skills[blacksmith_index])
# </POTBO_STAGE S2310>

# <POTBO_STAGE S2333>





_v92_ambience_raw = map_ambience_guncelle


def map_ambience_guncelle():
    if oyun_durumu == BLACKSMITH:
        if map_ambience_kanali is None or map_ambience_sesi is None or oyuncu_hp <= 0:
            return
        vol = _v35_ambience_ses_orani()
        map_ambience_kanali.set_volume(vol, vol)
        if not map_ambience_kanali.get_busy():
            map_ambience_kanali.play(map_ambience_sesi, loops=-1)
        return
    return _v92_ambience_raw()
# </POTBO_STAGE S2333>

# <POTBO_STAGE S2335>


def v92_save_payload():
    return {
        "version": V92_VERSION,
        "level_stats": {k: round(float(v), 6) for k, v in v92_level_stats.items()},
        "merchant_stock": {
            k: {"remaining": int(v.get("remaining", 0)), "unlocked": bool(v.get("unlocked", False))}
            for k, v in v92_merchant_stock.items()
        },
        "merchant_restock_level": int(v92_merchant_last_restock_level),
        "merchant_reputation": round(float(v92_merchant_reputation), 4),
        "blacksmith_upgrades": {k: int(v) for k, v in v92_blacksmith_upgrades.items()},
        "armor_weight": str(v92_armor_weight),
        "armor_rating": round(float(v92_armor_rating), 6),
        "training": {k: int(v) for k, v in v92_training.items()},
    }


def v92_restore_payload(payload):
    global v92_merchant_last_restock_level, v92_merchant_reputation
    global v92_armor_weight, v92_armor_rating, gelistirici_x_skill_aktif
    if not isinstance(payload, dict):
        v92_merchant_stock_init(oyuncu_level)
        return
    levels = payload.get("level_stats", {})
    for key in v92_level_stats:
        try:
            v92_level_stats[key] = max(0.0, float(levels.get(key, v92_level_stats[key])))
        except (TypeError, ValueError):
            pass
    stock = payload.get("merchant_stock", {})
    if isinstance(stock, dict):
        v92_merchant_stock.clear()
        for item_id in V92_MERCHANT_LEVEL_UNLOCKS:
            row = stock.get(item_id, {}) if isinstance(stock.get(item_id, {}), dict) else {}
            v92_merchant_stock[item_id] = {
                "remaining": max(0, int(row.get("remaining", 0))),
                "unlocked": bool(row.get("unlocked", oyuncu_level >= V92_MERCHANT_LEVEL_UNLOCKS[item_id])),
            }
    try:
        v92_merchant_last_restock_level = int(payload.get("merchant_restock_level", oyuncu_level))
        v92_merchant_reputation = float(payload.get("merchant_reputation", 0.0))
    except (TypeError, ValueError):
        pass
    upgrades = payload.get("blacksmith_upgrades", {})
    if isinstance(upgrades, dict):
        for key in v92_blacksmith_upgrades:
            v92_blacksmith_upgrades[key] = max(0, int(upgrades.get(key, 0)))
    v92_armor_weight = str(payload.get("armor_weight", "balanced"))
    if v92_armor_weight not in ("light", "balanced", "heavy"):
        v92_armor_weight = "balanced"
    try:
        v92_armor_rating = max(0.0, min(0.30, float(payload.get("armor_rating", 0.0))))
    except (TypeError, ValueError):
        v92_armor_rating = 0.0
    training = payload.get("training", {})
    if isinstance(training, dict):
        for key in v92_training:
            v92_training[key] = max(0, min(5, int(training.get(key, 0))))
    gelistirici_x_skill_aktif = v92_training.get("decussatio_rubra", 0) >= 5
    v92_resource_balance_refresh()
    v92_merchant_restock_for_level(oyuncu_level)
# </POTBO_STAGE S2335>

# <POTBO_STAGE S2338>


def yeni_oyun_baslat(loadinge_gec=True):
    global v92_merchant_last_restock_level, v92_merchant_reputation
    global v92_armor_weight, v92_armor_rating, gelistirici_x_skill_aktif
    result = _v92_new_game_raw(loadinge_gec)
    if not result:
        return result
    for key in v92_level_stats:
        v92_level_stats[key] = 0.0
    v92_merchant_stock.clear()
    v92_merchant_last_restock_level = 0
    v92_merchant_reputation = 0.0
    for key in v92_blacksmith_upgrades:
        v92_blacksmith_upgrades[key] = 0
    for key in v92_training:
        v92_training[key] = 0
    v92_armor_weight = "balanced"
    v92_armor_rating = 0.0
    gelistirici_x_skill_aktif = False
    v92_chain_state.reset()
    v92_merchant_stock_init(oyuncu_level)
    v92_resource_balance_refresh()
    return result
# </POTBO_STAGE S2338>

# <POTBO_STAGE S2350>





def _v94_load_alpha(path):
    if not path or not os.path.isfile(path):
        return None
    try:
        return pygame.image.load(path).convert_alpha()
    except pygame.error:
        return None
# </POTBO_STAGE S2350>

# <POTBO_STAGE S2354>


def _v94_merchant_idle_load():
    sheet = _v94_load_alpha(MERCHANT_SHARED_YOLU)
    if sheet is None:
        return None


    frames = [
        _v94_normalized_crop(sheet, 21 / 168.0, 55 / 113.0, 58 / 168.0, 58 / 113.0),
        _v94_normalized_crop(sheet, 80 / 168.0, 55 / 113.0, 58 / 168.0, 58 / 113.0),
    ]
    return _v94_best([frame for frame in frames if frame is not None])
# </POTBO_STAGE S2354>

# <POTBO_STAGE S2356>


def _v94_blacksmith_idle_load():
    sheet = _v94_load_alpha(BLACKSMITH_YOLU)
    if sheet is None:
        return None
    mask = pygame.mask.from_surface(sheet, 8)
    sw, sh = sheet.get_size()

    y_start = int(sh * 0.70)
    row_counts = []
    for y in range(y_start, sh):
        count = 0
        for x in range(sw):
            count += mask.get_at((x, y))
        row_counts.append(count)
    row_bands = _v94_projection_bands(row_counts, max(7, int(sw * 0.07)), 9)
    if not row_bands:
        return _v94_normalized_crop(sheet, 0.0, 0.82, 1.0, 0.18)


    row_bands = row_bands[-4:]
    frames = []
    for local_y0, local_y1 in row_bands:
        ry0 = y_start + local_y0
        ry1 = y_start + local_y1
        col_counts = []
        for x in range(sw):
            count = 0
            for y in range(ry0, ry1):
                count += mask.get_at((x, y))
            col_counts.append(count)
        col_bands = _v94_projection_bands(col_counts, max(4, int((ry1 - ry0) * 0.11)), 7)
        for cx0, cx1 in col_bands:
            rect = pygame.Rect(cx0 - 4, ry0 - 4, (cx1 - cx0) + 8, (ry1 - ry0) + 8).clip(sheet.get_rect())
            if rect.width > 0 and rect.height > 0:
                frames.append(sheet.subsurface(rect).copy().convert_alpha())
    return _v94_best(frames)


def _v94_blacksmith_fallback():
    surf = pygame.Surface((42, 68), pygame.SRCALPHA)
    pygame.draw.circle(surf, (78, 72, 73, 255), (21, 12), 9)
    pygame.draw.polygon(surf, (53, 49, 51, 255), [(10, 22), (32, 22), (38, 60), (4, 60)])
    pygame.draw.rect(surf, (112, 83, 48, 255), (6, 30, 30, 5))
    pygame.draw.rect(surf, (92, 89, 92, 255), (30, 17, 8, 26))
    return surf


v94_merchant_idle = _v94_merchant_idle_load()
v94_blacksmith_idle = _v94_blacksmith_idle_load()
if v94_merchant_idle is not None:
    merchant_resmi_orijinal = v94_merchant_idle
    merchant_resmi = resmi_oranli_sigdir(v94_merchant_idle, pygame.Rect(0, 0, 72, 78), 0, 1.0, True)


def merchant_karakter_ciz(rect):
    merchant_panel_ciz(rect, V91_UI_RED, 1)
    frame = v94_merchant_idle or merchant_resmi_orijinal
    if frame is not None:
        image = resmi_oranli_sigdir(frame, rect.inflate(-34, -26), 0, 1.0, True)
        if image is not None:
            ekran.blit(image, image.get_rect(center=rect.center))


def merchant_sprite_ciz():
    frame = v94_merchant_idle or merchant_resmi
    if frame is None:
        return
    target_h = 70
    scale = target_h / max(1.0, float(frame.get_height()))
    image = pygame.transform.scale(frame, (max(1, int(round(frame.get_width() * scale))), target_h))
    ekran.blit(image, image.get_rect(midbottom=(int(dunya_ekran_x(merchant_x)), int(dunya_ekran_y(merchant_y)))))


def v92_blacksmith_actor_surface():
    if v94_blacksmith_idle is not None:
        return v94_blacksmith_idle
    if blacksmith_resmi_orijinal is not None:
        return blacksmith_resmi_orijinal
    return _v94_blacksmith_fallback()
# </POTBO_STAGE S2356>

# <POTBO_STAGE S2359>






def _v94_blacksmith_icon(rect, symbol, selected=False):
    merchant_panel_ciz(rect, V91_UI_RED_HOT if selected else V91_UI_GREY, 2 if selected else 1)
    yazi_yaz(symbol, rect.centerx, rect.centery, V91_UI_GOLD if selected else V91_UI_WHITE, normal_font, True)


def _v94_blacksmith_rows():
    if blacksmith_sayfa == "skills":
        return (
            ("decussatio_rubra", "X", "Decussatio Rubra", bt("J basılı tut · R", "Hold J · R")),
            ("catena_decollationis", "-", "Catena Decollationis", bt("J basılı tut · Dash", "Hold J · Dash")),
        )
    return (
        ("weapon", "W", bt("SİLAH GÜCÜ", "WEAPON POWER"), bt("Hasar", "Damage")),
        ("armor", "A", bt("ZIRH DAYANIKLILIĞI", "ARMOR DURABILITY"), bt("Koruma / ağırlık", "Protection / weight")),
        ("endurance", "E", bt("DAYANIKLILIK", "ENDURANCE"), bt("Stamina toleransı", "Stamina tolerance")),
    )


def blacksmith_ekrani_ciz():
    oyun_ekrani_ciz()
    koyu_kaplama(210)
    panel = pygame.Rect(60, 40, GENISLIK - 120, YUKSEKLIK - 80)
    v89_medieval_panel(panel, V91_UI_RED, 252)
    yazi_yaz("BLACKSMITH", panel.x + 28, panel.y + 28, V91_UI_WHITE, menu_baslik_font)
    yazi_yaz(str(oyuncu_altin), panel.right - 48, panel.y + 31, V91_UI_GOLD, normal_font, False)

    if blacksmith_sayfa == "menu":
        options = (bt("YETENEK", "SKILL"), bt("GELİŞTİR", "UPGRADE"), bt("ÇIKIŞ", "EXIT"))
        for i, text_value in enumerate(options):
            merchant_menu_butonu_ciz(pygame.Rect(panel.centerx - 230, panel.y + 145 + i * 96, 460, 70), text_value, blacksmith_menu_index == i)
    else:
        left = pygame.Rect(panel.x + 26, panel.y + 92, 226, 340)
        center = pygame.Rect(left.right + 18, panel.y + 92, 438, 340)
        right = pygame.Rect(center.right + 18, panel.y + 92, panel.right - center.right - 44, 340)
        for rect in (left, center, right):
            merchant_panel_ciz(rect, V91_UI_RED, 1)
        smith = v92_blacksmith_actor_surface()
        if smith is not None:
            image = resmi_oranli_sigdir(smith, left.inflate(-28, -44), 0, 1.0, True)
            if image is not None:
                ekran.blit(image, image.get_rect(center=left.center))
        yazi_yaz(bt("DEMİRCİ", "SMITH"), left.centerx, left.y + 19, V91_UI_RED_HOT, mini_font, True)

        rows = _v94_blacksmith_rows()
        selection = max(0, min(len(rows) - 1, int(blacksmith_index)))
        row_h = 88 if blacksmith_sayfa == "skills" else 78
        for i, (kind, symbol, name, meta) in enumerate(rows):
            row = pygame.Rect(center.x + 12, center.y + 18 + i * (row_h + 10), center.width - 24, row_h)
            selected = i == selection
            merchant_panel_ciz(row, V91_UI_RED_HOT if selected else V91_UI_GREY, 2 if selected else 1)
            icon = pygame.Rect(row.x + 10, row.y + 10, 54, row.height - 20)
            _v94_blacksmith_icon(icon, symbol, selected)
            yazi_yaz(name, icon.right + 13, row.y + 15, V91_UI_WHITE, normal_font)
            yazi_yaz(meta, icon.right + 13, row.y + 45, V91_UI_GREY, mini_font)
            if blacksmith_sayfa == "skills":
                progress = int(v92_training.get(kind, 0))
                value = bt("ÖĞRENİLDİ", "LEARNED") if progress >= 5 else f"{progress}/5 · 67"
            else:
                value = f"{v92_blacksmith_upgrade_cost(kind)} coin"
            yazi_yaz(value, row.right - 12, row.y + 16, V91_UI_GOLD, mini_font, False)

        if blacksmith_sayfa == "upgrade":

            player = v84_player_silhouette()
            if player is not None:
                image = resmi_oranli_sigdir(player, right.inflate(-34, -44), 0, 1.0, True)
                if image is not None:
                    ekran.blit(image, image.get_rect(center=(right.centerx, right.centery + 12)))
            yazi_yaz(bt("SEN", "YOU"), right.centerx, right.y + 19, V91_UI_WHITE, mini_font, True)
            selected_kind = rows[selection][0]
            tier = int(v92_blacksmith_upgrades.get(selected_kind, 0))
            yazi_yaz(bt(f"Kademe {tier}", f"Tier {tier}"), right.centerx, right.bottom - 45, V91_UI_GOLD, mini_font, True)
        else:
            selected_kind, symbol, name, meta = rows[selection]
            _v94_blacksmith_icon(pygame.Rect(right.centerx - 38, right.y + 25, 76, 76), symbol, True)
            progress = int(v92_training.get(selected_kind, 0))
            yazi_yaz(name, right.centerx, right.y + 122, V91_UI_WHITE, normal_font, True)
            yazi_yaz(meta, right.centerx, right.y + 155, V91_UI_GREY, mini_font, True)
            yazi_yaz(bt(f"Eğitim: {progress}/5", f"Training: {progress}/5"), right.centerx, right.y + 193, V91_UI_GOLD, mini_font, True)
            detail = bt(
                "5 eğitimden sonra açılır. Öldürücü koşul oluşursa infaza dönüşebilir." if selected_kind == "decussatio_rubra" else "En az iki hedefi zincirler. Tüm hedefler ölecekse siyah/kırmızı infaz sahnesine geçer.",
                "Unlocks after 5 trainings. It can become an execution when lethal." if selected_kind == "decussatio_rubra" else "Chains at least two targets. If all will die, it enters the black/red execution scene.",
            )
            wrapped = metni_satirlara_bol(detail, mini_font, right.width - 30)
            for i, segment in enumerate(wrapped[:5]):
                yazi_yaz(segment, right.x + 15, right.y + 225 + i * 19, ACIK_GRI, mini_font)

        yazi_yaz(bt("E: seç/eğit · F: pazarlık · ESC: geri", "E: select/train · F: haggle · ESC: back"), center.centerx, center.bottom - 18, V91_UI_GREY, mini_font, True)

    dialogue = pygame.Rect(panel.x + 28, panel.bottom - 114, panel.width - 56, 80)
    merchant_panel_ciz(dialogue, V91_UI_RED, 1)
    if blacksmith_modal == "haggle":
        for i, tactic in enumerate(blacksmith_haggle_choices):
            value = tactic["tr" if dil == "TR" else "en"]
            yazi_yaz(("> " if i == blacksmith_haggle_index else "  ") + value, dialogue.x + 18, dialogue.y + 10 + i * 21, V91_UI_WHITE if i == blacksmith_haggle_index else V91_UI_GREY, mini_font)
    elif blacksmith_modal == "weight":
        choices = (bt("HAFİFLET", "LIGHTEN"), bt("DENGELİ", "BALANCED"), bt("AĞIRLAŞTIR", "HEAVIER"))
        yazi_yaz(bt("Zırhın ağırlığını nasıl ayarlayayım?", "How should I tune the armor weight?"), dialogue.x + 18, dialogue.y + 10, V91_UI_WHITE, mini_font)
        yazi_yaz("   ".join((">" if i == blacksmith_weight_index else " ") + item for i, item in enumerate(choices)), dialogue.x + 18, dialogue.y + 42, V91_UI_GOLD, mini_font)
    else:
        wrapped = metni_satirlara_bol(blacksmith_mesaji or "...", mini_font, dialogue.width - 36)
        for i, segment in enumerate(wrapped[:3]):
            yazi_yaz(segment, dialogue.x + 18, dialogue.y + 12 + i * 21, ACIK_GRI, mini_font)
# </POTBO_STAGE S2359>

# <POTBO_STAGE S2371>










V95_VERSION = "95.0"
# </POTBO_STAGE S2371>

# <POTBO_STAGE S2378>







V95_MERCHANT_IDLE_FRAME_MS = 420


def _v95_merchant_idle_frames_load():
    sheet = _v94_load_alpha(MERCHANT_SHARED_YOLU)
    if sheet is None:
        return []

    ref_w, ref_h = 168, 113
    idle_rects = (
        (0, 58, 34, 55),
        (34, 58, 34, 55),
    )

    frames = []
    for x, y, w, h in idle_rects:
        frame = _v94_normalized_crop(
            sheet,
            float(x) / float(ref_w),
            float(y) / float(ref_h),
            float(w) / float(ref_w),
            float(h) / float(ref_h),
        )
        frame = _v92_trim(frame)
        if frame is not None:
            frames.append(frame)

    return frames


v95_merchant_idle_frames = _v95_merchant_idle_frames_load()
v95_merchant_idle = (
    v95_merchant_idle_frames[0] if v95_merchant_idle_frames else None
)


def _v95_merchant_current_idle():
    if not v95_merchant_idle_frames:
        return v95_merchant_idle or v94_merchant_idle or merchant_resmi_orijinal

    index = (
        pygame.time.get_ticks() // V95_MERCHANT_IDLE_FRAME_MS
    ) % len(v95_merchant_idle_frames)
    return v95_merchant_idle_frames[index]




v95_blacksmith_idle = _v95_idle_crop(
    BLACKSMITH_YOLU,
    (322, 1775),
    (3, 287, 36, 54),
)

if v95_merchant_idle is not None:
    merchant_resmi_orijinal = v95_merchant_idle
    merchant_resmi = resmi_oranli_sigdir(
        v95_merchant_idle,
        pygame.Rect(0, 0, 66, 74),
        0,
        1.0,
        True,
    )


def v92_blacksmith_actor_surface():
    if v95_blacksmith_idle is not None:
        return v95_blacksmith_idle
    if v94_blacksmith_idle is not None:
        return v94_blacksmith_idle
    if blacksmith_resmi_orijinal is not None:
        return blacksmith_resmi_orijinal
    return _v94_blacksmith_fallback()
# </POTBO_STAGE S2378>

# <POTBO_STAGE S2380>


def merchant_sprite_ciz():


    frame = _v95_merchant_current_idle()
    image = _v95_pixel_actor(frame, 68)
    if image is None:
        return

    ekran.blit(
        image,
        image.get_rect(
            midbottom=(
                int(round(dunya_ekran_x(merchant_x))),
                int(round(dunya_ekran_y(merchant_y))),
            )
        ),
    )


def blacksmith_world_ciz():
    frame = v92_blacksmith_actor_surface()
    image = _v95_pixel_actor(frame, 72)
    if image is None:
        return
    ekran.blit(
        image,
        image.get_rect(
            midbottom=(
                int(round(dunya_ekran_x(blacksmith_x))),
                int(round(dunya_ekran_y(blacksmith_y))),
            )
        ),
    )


def _v95_vendor_portrait(rect, frame, title=None):
    merchant_panel_ciz(rect, V91_UI_RED, 1)
    if title:
        yazi_yaz(title, rect.centerx, rect.y + 20, V91_UI_RED_HOT, mini_font, True)
    if frame is None:
        return
    target = rect.inflate(-34, -42)
    image = resmi_oranli_sigdir(frame, target, 0, 1.0, True)
    if image is not None:

        target_center = (target.centerx, target.centery + 8)
        ekran.blit(image, image.get_rect(center=target_center))


def merchant_karakter_ciz(rect):

    _v95_vendor_portrait(
        pygame.Rect(rect),
        _v95_merchant_current_idle(),
        None,
    )





def _v95_vendor_main_geometry(panel):
    top = panel.y + 74
    bottom = panel.bottom - 208
    portrait = pygame.Rect(panel.x + 24, top, 360, bottom - top)
    options = pygame.Rect(
        portrait.right + 22,
        top,
        panel.right - portrait.right - 46,
        bottom - top,
    )
    return portrait, options


def _v95_vendor_sub_geometry(panel):
    top = panel.y + 74
    bottom = panel.bottom - 208
    portrait = pygame.Rect(panel.x + 24, top, 250, bottom - top)
    listing = pygame.Rect(portrait.right + 18, top, 390, bottom - top)
    info = pygame.Rect(
        listing.right + 18,
        top,
        panel.right - listing.right - 42,
        bottom - top,
    )
    return portrait, listing, info


def _v95_vendor_main_menu(panel, frame, options, selected, new_badge_index=None):
    portrait, option_rect = _v95_vendor_main_geometry(panel)
    _v95_vendor_portrait(portrait, frame)
    for i, label in enumerate(options):
        button = pygame.Rect(
            option_rect.x + 60,
            option_rect.y + 55 + i * 86,
            option_rect.width - 120,
            62,
        )
        badge = bt("YENİ", "NEW") if new_badge_index == i else None
        merchant_menu_butonu_ciz(button, label, i == selected, badge)


def merchant_ana_menu_ciz(panel):
    _v95_vendor_main_menu(
        panel,
        v95_merchant_idle or v94_merchant_idle or merchant_resmi_orijinal,
        (bt("SAT", "SELL"), bt("AL", "BUY"), bt("ÇIKIŞ", "EXIT")),
        merchant_menu_index,
        1 if merchant_yeni_urun_var_mi() else None,
    )




def merchant_alt_sayfa_ciz(panel):
    portrait, list_rect, info = _v95_vendor_sub_geometry(panel)
    _v95_vendor_portrait(
        portrait,
        v95_merchant_idle or v94_merchant_idle or merchant_resmi_orijinal,
    )
    merchant_panel_ciz(list_rect, V91_UI_RED, 1)
    yazi_yaz(
        bt("SAT", "SELL") if merchant_sayfa == "sell" else bt("AL", "BUY"),
        list_rect.centerx,
        list_rect.y + 28,
        V91_UI_RED_HOT,
        normal_font,
        True,
    )
    records = merchant_aktif_liste()
    if not records:
        yazi_yaz(
            bt("Liste boş.", "The list is empty."),
            list_rect.centerx,
            list_rect.centery,
            V91_UI_GREY,
            kucuk_font,
            True,
        )
        merchant_panel_ciz(info, V91_UI_RED, 1)
        return

    selection = merchant_index % len(records)
    start = max(0, min(selection - 2, max(0, len(records) - 6)))
    for row_no, record in enumerate(records[start : start + 6]):
        idx = start + row_no
        sold = False
        remaining = None
        if merchant_sayfa == "sell":
            _, item = record
            price = int(MERCHANT_SATIS_REFERANSI.get(item.get("id"), 1))
        else:
            if record.get("source") == "buyback" and isinstance(record.get("item"), dict):
                item = record["item"]
            else:
                item = merchant_item_olustur(record.get("id")) or {
                    "id": record.get("id"),
                    "name": "",
                }
            price = int(record.get("price", 1))
            sold = bool(record.get("sold"))
            remaining = int(record.get("remaining", 0))

        new = (
            merchant_sayfa == "buy"
            and isinstance(record, dict)
            and record.get("source") == "stock"
            and str(record.get("id")) in merchant_yeni_urun_idleri()
        )
        merchant_liste_satiri_ciz(
            pygame.Rect(
                list_rect.x + 12,
                list_rect.y + 54 + row_no * 58,
                list_rect.width - 24,
                50,
            ),
            item,
            price,
            idx == selection,
            new,
            sold,
            remaining,
        )

    record = records[selection]
    if merchant_sayfa == "sell":
        _, item = record
        price = int(MERCHANT_SATIS_REFERANSI.get(item.get("id"), 1))
    else:
        item = (
            record.get("item")
            if record.get("source") == "buyback"
            else merchant_item_olustur(record.get("id"))
        )
        item = item if isinstance(item, dict) else {
            "name": "",
            "id": record.get("id"),
        }
        price = int(record.get("price", 1))
    merchant_item_bilgi_ciz(info, item, price)


def merchant_diyalog_kutusu_ciz(panel):
    box = pygame.Rect(panel.x + 24, panel.bottom - 190, panel.width - 48, 154)
    merchant_panel_ciz(box, V91_UI_RED, 2)
    yazi_yaz("MEDOLI", box.x + 20, box.y + 25, V91_UI_RED_HOT, normal_font)

    if merchant_modal == "quantity":
        record = (merchant_bekleyen_islem or {}).get("record", {})
        available = max(0, int(record.get("remaining", 0)))
        yazi_yaz(bt("MİKTAR", "QUANTITY"), box.x + 20, box.y + 59, V91_UI_GREY, mini_font)
        field = pygame.Rect(box.x + 118, box.y + 49, 128, 35)
        merchant_panel_ciz(field, V91_UI_WHITE, 1, V91_UI_BLACK)
        yazi_yaz(
            v92_merchant_quantity_input or "0",
            field.centerx,
            field.centery,
            V91_UI_WHITE,
            normal_font,
            True,
        )
        yazi_yaz(
            bt(f"Stok: {available}", f"Stock: {available}"),
            box.x + 20,
            box.y + 105,
            ACIK_GRI,
            mini_font,
        )
        return

    if merchant_modal == "haggle":
        yazi_yaz(
            bt(
                f"PAZARLIK {v92_merchant_haggle_round + 1}/3",
                f"HAGGLE {v92_merchant_haggle_round + 1}/3",
            ),
            box.x + 20,
            box.y + 57,
            V91_UI_GOLD,
            mini_font,
        )
        for i, tactic in enumerate(v92_merchant_haggle_choices):
            selected = i == v92_merchant_haggle_index
            value = tactic["tr" if dil == "TR" else "en"]
            yazi_yaz(
                ("> " if selected else "  ") + value,
                box.x + 20,
                box.y + 80 + i * 21,
                V91_UI_WHITE if selected else V91_UI_GREY,
                mini_font,
            )
        return

    if merchant_modal == "confirm":
        txn = merchant_bekleyen_islem or {}
        total = int(txn.get("price", 0))
        yazi_yaz(
            bt("ANLAŞMA BEDELİ", "AGREED TOTAL"),
            box.x + 20,
            box.y + 61,
            V91_UI_GREY,
            mini_font,
        )
        merchant_fiyat_ciz(
            pygame.Rect(box.x + 20, box.y + 78, 180, 34),
            total,
            False,
            V91_UI_GOLD,
        )
        return

    lines = metni_satirlara_bol(
        merchant_diyalog_gorunen_metin() or "...",
        oyun_kucuk_font,
        box.width - 40,
    )
    for i, line in enumerate(lines[:4]):
        yazi_yaz(
            line,
            box.x + 20,
            box.y + 58 + i * 21,
            ACIK_GRI,
            oyun_kucuk_font,
        )


def merchant_modal_ciz(panel):

    return None





def _v95_blacksmith_rows():
    if blacksmith_sayfa == "skills":
        return (
            {
                "id": "decussatio_rubra",
                "icon": "X",
                "name": "Decussatio Rubra",
                "description": bt(
                    "Üç kesili yakın menzil özel hareketi. Ölüm kesinleşirse infaza dönüşür.",
                    "A close-range three-cut special. It becomes an execution when death is certain.",
                ),
                "shortcut": bt("J basılı tut + R", "Hold J + R"),
                "price": 67,
            },
            {
                "id": "catena_decollationis",
                "icon": "—",
                "name": "Catena Decollationis",
                "description": bt(
                    "Bir çizgi veya zigzag üzerindeki yakın hedefleri art arda biçer.",
                    "Cuts through nearby targets in sequence along a line or zigzag.",
                ),
                "shortcut": bt("J basılı tut + Dash", "Hold J + Dash"),
                "price": 67,
            },
        )
    return (
        {
            "id": "weapon",
            "icon": "W",
            "name": bt("SİLAH GÜCÜ", "WEAPON POWER"),
            "description": bt(
                "Silahın gerçek vuruş gücünü kontrollü biçimde artırır.",
                "Raises the weapon's actual strike power in controlled increments.",
            ),
            "price": v92_blacksmith_upgrade_cost("weapon"),
        },
        {
            "id": "armor",
            "icon": "A",
            "name": bt("ZIRH DAYANIKLILIĞI", "ARMOR DURABILITY"),
            "description": bt(
                "Zırh korumasını geliştirir; işlem sonunda ağırlık profili seçilir.",
                "Improves armor protection; a weight profile is chosen after the work.",
            ),
            "price": v92_blacksmith_upgrade_cost("armor"),
        },
        {
            "id": "endurance",
            "icon": "E",
            "name": bt("DAYANIKLILIK", "ENDURANCE"),
            "description": bt(
                "Uzun dövüşlerde stamina toleransını artırır.",
                "Improves stamina tolerance in prolonged combat.",
            ),
            "price": v92_blacksmith_upgrade_cost("endurance"),
        },
    )


def _v95_blacksmith_list_row(rect, row_data, selected):
    rect = pygame.Rect(rect)
    merchant_panel_ciz(
        rect,
        V91_UI_RED_HOT if selected else V91_UI_RED,
        2 if selected else 1,
        (34, 8, 13) if selected else (10, 8, 11),
    )
    icon = pygame.Rect(rect.x + 10, rect.y + 8, 42, rect.height - 16)
    merchant_panel_ciz(icon, V91_UI_RED_HOT if selected else V91_UI_GREY, 1)
    yazi_yaz(
        row_data["icon"],
        icon.centerx,
        icon.centery,
        V91_UI_GOLD if selected else V91_UI_WHITE,
        normal_font,
        True,
    )
    yazi_yaz(
        row_data["name"],
        icon.right + 12,
        rect.y + 14,
        V91_UI_WHITE,
        oyun_kucuk_font,
    )
    if blacksmith_sayfa == "skills":
        progress = int(v92_training.get(row_data["id"], 0))
        status = (
            bt("ÖĞRENİLDİ", "LEARNED")
            if progress >= 5
            else bt(f"Eğitim {progress}/5", f"Training {progress}/5")
        )
        yazi_yaz(status, rect.right - 12, rect.y + 12, V91_UI_GOLD, mini_font, False)
        if progress < 5:
            merchant_fiyat_ciz(
                pygame.Rect(rect.right - 98, rect.bottom - 31, 86, 24),
                row_data["price"],
                True,
                V91_UI_GOLD,
            )
    else:
        merchant_fiyat_ciz(
            pygame.Rect(rect.right - 118, rect.y + 9, 106, 28),
            row_data["price"],
            True,
            V91_UI_GOLD,
        )


def _v95_blacksmith_info(rect, row_data):
    merchant_panel_ciz(rect, V91_UI_RED, 1)
    icon = pygame.Rect(rect.centerx - 40, rect.y + 24, 80, 80)
    merchant_panel_ciz(icon, V91_UI_RED_HOT, 2)
    yazi_yaz(
        row_data["icon"],
        icon.centerx,
        icon.centery,
        V91_UI_GOLD,
        normal_font,
        True,
    )
    yazi_yaz(
        row_data["name"],
        rect.centerx,
        icon.bottom + 26,
        V91_UI_WHITE,
        normal_font,
        True,
    )
    desc = metni_satirlara_bol(
        row_data["description"],
        mini_font,
        rect.width - 34,
    )
    y = icon.bottom + 62
    for line in desc[:5]:
        yazi_yaz(line, rect.x + 17, y, ACIK_GRI, mini_font)
        y += 20

    if blacksmith_sayfa == "skills":
        progress = int(v92_training.get(row_data["id"], 0))
        yazi_yaz(
            bt(f"Eğitim: {progress}/5", f"Training: {progress}/5"),
            rect.x + 17,
            rect.bottom - 84,
            V91_UI_GOLD,
            mini_font,
        )

        yazi_yaz(
            row_data["shortcut"],
            rect.x + 17,
            rect.bottom - 52,
            V91_UI_RED_HOT,
            mini_font,
        )
        if progress < 5:
            merchant_fiyat_ciz(
                pygame.Rect(rect.right - 122, rect.bottom - 64, 104, 28),
                row_data["price"],
                True,
                V91_UI_GOLD,
            )
    else:
        tier = int(v92_blacksmith_upgrades.get(row_data["id"], 0))
        yazi_yaz(
            bt(f"Kademe: {tier}", f"Tier: {tier}"),
            rect.x + 17,
            rect.bottom - 84,
            V91_UI_GREY,
            mini_font,
        )
        merchant_fiyat_ciz(
            pygame.Rect(rect.x + 17, rect.bottom - 66, 118, 30),
            row_data["price"],
            False,
            V91_UI_GOLD,
        )


def _v95_blacksmith_dialogue(panel):
    box = pygame.Rect(panel.x + 24, panel.bottom - 190, panel.width - 48, 154)
    merchant_panel_ciz(box, V91_UI_RED, 2)
    yazi_yaz(bt("DEMİRCİ", "BLACKSMITH"), box.x + 20, box.y + 25, V91_UI_RED_HOT, normal_font)

    if blacksmith_modal == "haggle":
        yazi_yaz(
            bt(
                f"PAZARLIK {blacksmith_haggle_round + 1}/3",
                f"HAGGLE {blacksmith_haggle_round + 1}/3",
            ),
            box.x + 20,
            box.y + 55,
            V91_UI_GOLD,
            mini_font,
        )
        for i, tactic in enumerate(blacksmith_haggle_choices):
            selected = i == blacksmith_haggle_index
            value = tactic["tr" if dil == "TR" else "en"]
            yazi_yaz(
                ("> " if selected else "  ") + value,
                box.x + 20,
                box.y + 78 + i * 21,
                V91_UI_WHITE if selected else V91_UI_GREY,
                mini_font,
            )
        return

    if blacksmith_modal == "weight":
        choices = (
            bt("HAFİFLET", "LIGHTEN"),
            bt("DENGELİ", "BALANCED"),
            bt("AĞIRLAŞTIR", "HEAVIER"),
        )
        yazi_yaz(
            bt("Zırhın ağırlık profilini seç.", "Choose the armor weight profile."),
            box.x + 20,
            box.y + 61,
            V91_UI_WHITE,
            mini_font,
        )
        yazi_yaz(
            "   ".join(
                (">" if i == blacksmith_weight_index else " ") + choice
                for i, choice in enumerate(choices)
            ),
            box.x + 20,
            box.y + 96,
            V91_UI_GOLD,
            mini_font,
        )
        return

    if blacksmith_modal == "confirm":
        yazi_yaz(
            bt("İŞÇİLİK BEDELİ", "WORK TOTAL"),
            box.x + 20,
            box.y + 61,
            V91_UI_GREY,
            mini_font,
        )
        merchant_fiyat_ciz(
            pygame.Rect(box.x + 20, box.y + 78, 190, 34),
            blacksmith_fiyat,
            False,
            V91_UI_GOLD,
        )
        return


    msg = str(blacksmith_mesaji or "...")
    for fragment in (
        " F pazarlık, E kabul.",
        " F haggles; E accepts.",
        "E: seç · F: pazarlık",
        "E: select · F: haggle",
        "E: 1 saat eğitim",
        "E: train 1 hour",
    ):
        msg = msg.replace(fragment, "")
    lines = metni_satirlara_bol(msg, oyun_kucuk_font, box.width - 40)
    for i, line in enumerate(lines[:4]):
        yazi_yaz(line, box.x + 20, box.y + 58 + i * 21, ACIK_GRI, oyun_kucuk_font)


def blacksmith_ekrani_ciz():
    oyun_ekrani_ciz()
    koyu_kaplama(205)
    panel = pygame.Rect(32, 24, GENISLIK - 64, YUKSEKLIK - 48)
    merchant_panel_ciz(panel, KOYU_KIRMIZI, 3)
    pygame.draw.rect(ekran, PARLAK_KIRMIZI, panel.inflate(-10, -10), 1)

    yazi_yaz(
        bt("DEMİRCİ", "BLACKSMITH"),
        panel.x + 28,
        panel.y + 31,
        PARLAK_KIRMIZI,
        menu_baslik_font,
    )
    gold = pygame.Rect(panel.right - 150, panel.y + 16, 118, 42)
    merchant_panel_ciz(gold, KOYU_KIRMIZI, 1, (12, 8, 11))
    merchant_fiyat_ciz(
        pygame.Rect(gold.x + 14, gold.y + 7, gold.width - 28, 28),
        oyuncu_altin,
        False,
        BEYAZ,
    )

    smith_frame = v92_blacksmith_actor_surface()
    if blacksmith_sayfa == "menu":
        _v95_vendor_main_menu(
            panel,
            smith_frame,
            (
                bt("YETENEK", "SKILL"),
                bt("GELİŞTİR", "UPGRADE"),
                bt("ÇIKIŞ", "EXIT"),
            ),
            blacksmith_menu_index,
        )
    else:
        portrait, list_rect, info = _v95_vendor_sub_geometry(panel)
        _v95_vendor_portrait(portrait, smith_frame)
        merchant_panel_ciz(list_rect, V91_UI_RED, 1)
        yazi_yaz(
            bt("YETENEK", "SKILL")
            if blacksmith_sayfa == "skills"
            else bt("GELİŞTİR", "UPGRADE"),
            list_rect.centerx,
            list_rect.y + 28,
            V91_UI_RED_HOT,
            normal_font,
            True,
        )
        rows = _v95_blacksmith_rows()
        selection = max(0, min(len(rows) - 1, int(blacksmith_index)))
        row_h = 72
        for row_no, row_data in enumerate(rows):
            row = pygame.Rect(
                list_rect.x + 12,
                list_rect.y + 58 + row_no * (row_h + 10),
                list_rect.width - 24,
                row_h,
            )
            _v95_blacksmith_list_row(row, row_data, row_no == selection)
        _v95_blacksmith_info(info, rows[selection])

    _v95_blacksmith_dialogue(panel)
# </POTBO_STAGE S2380>

# <POTBO_STAGE S2394>













V96_VERSION = "96.0"


v96_ikna_xp = 0
# </POTBO_STAGE S2394>

# <POTBO_STAGE S2396>


def v96_ikna_sansi(tactic, vendor="hanus"):
    risk = max(0.0, min(1.0, float(tactic.get("risk", 0.20))))
    mastery = v96_ikna_ustaligi()
    level_bonus = min(0.12, max(0, int(oyuncu_level) - 1) * 0.006)
    mastery_bonus = (mastery - 1) * 0.026
    reputation_bonus = 0.0
    if vendor == "hanus":
        reputation_bonus = max(-0.06, min(0.06, float(v92_merchant_reputation) * 0.018))
    vendor_penalty = 0.055 if vendor == "hanus" else 0.0
    chance = 0.61 + level_bonus + mastery_bonus + reputation_bonus - risk * 0.58 - vendor_penalty
    return max(0.18, min(0.90, chance))



V92_MERCHANT_HAGGLE_PATHS = (
    {"tr": "Şu kusurlara bak. Bu mal o fiyat etmez.", "en": "Look at those flaws. This is not worth that price.", "lev": 1.30, "risk": 0.24},
    {"tr": "Coini şimdi veririm; peşin fiyatını söyle.", "en": "I pay now. Give me the cash price.", "lev": 0.95, "risk": 0.10},
    {"tr": "İyi fiyat verirsen birden fazla alırım.", "en": "Give me a fair price and I will take more than one.", "lev": 1.15, "risk": 0.18},
    {"tr": "Aynısını başka yerde daha ucuza gördüm.", "en": "I saw the same thing cheaper elsewhere.", "lev": 1.25, "risk": 0.34},
    {"tr": "Ben teklifimi söyledim. Şimdi sen düşün.", "en": "I made my offer. Now you think about it.", "lev": 1.05, "risk": 0.22},
    {"tr": "Kaç kez alışveriş yaptık; bana yabancı fiyatı çekme.", "en": "We have traded before. Do not quote me a stranger's price.", "lev": 0.90, "risk": 0.08},
    {"tr": "Bu rafta epeydir duruyor. Fiyatını indir.", "en": "That has been sitting there a while. Lower the price.", "lev": 1.12, "risk": 0.28},
    {"tr": "Buraya gelmek bile masraf. Biraz yaklaş.", "en": "Getting here costs me enough. Come down a little.", "lev": 0.72, "risk": 0.19},
    {"tr": "Coin burada. Rakamı makul tut, hemen bitsin.", "en": "The coin is here. Keep it reasonable and we finish now.", "lev": 1.00, "risk": 0.12},
    {"tr": "Olmazsa bırakırım. Bu mala mecbur değilim.", "en": "If not, I walk. I do not need this item.", "lev": 1.42, "risk": 0.43},
    {"tr": "Bu fiyata garanti de verirsin.", "en": "At that price you give me a guarantee too.", "lev": 0.88, "risk": 0.14},
    {"tr": "Yuvarlak bir rakam söyle; ikimiz de uğraşmayalım.", "en": "Give me a round number and save us both the trouble.", "lev": 0.78, "risk": 0.10},
    {"tr": "Bu kadar nakdi rafta bekletmek senin de işine gelmez.", "en": "You do not want that much money sitting on a shelf either.", "lev": 1.18, "risk": 0.38},
    {"tr": "Bunun zamanı geçmiş. Bugünün fiyatını söyle.", "en": "Its season is gone. Give me today's price.", "lev": 0.92, "risk": 0.20},
    {"tr": "Şimdi anlaşalım; hızlı satışın indirimi olsun.", "en": "Deal now. Give me the quick-sale discount.", "lev": 1.08, "risk": 0.13},
    {"tr": "Fiyat değil değer konuşalım. Bu rakamı hak etmiyor.", "en": "Let us talk value, not price. It does not justify that number.", "lev": 1.22, "risk": 0.24},
    {"tr": "Benden bir şey saklıyorsun. Açık konuş.", "en": "You are hiding something from me. Speak plainly.", "lev": 1.35, "risk": 0.49},
    {"tr": "Bunu düzgün verirsen sonraki alışveriş de sende.", "en": "Treat me fairly and the next purchase is yours too.", "lev": 0.98, "risk": 0.12},
    {"tr": "Ben çıkarsam satış kaçar. Riski sen al.", "en": "If I leave, the sale leaves too. You carry that risk.", "lev": 1.28, "risk": 0.33},
    {"tr": "Teklifim bu. İkinci kez söylemeyeceğim.", "en": "That is my offer. I will not say it twice.", "lev": 1.16, "risk": 0.27},
)

V92_BLACKSMITH_HAGGLE_PATHS = (
    {"tr": "Malzemeyi ben getiririm; işçilikten düş.", "en": "I bring the material. Take it off the labor price.", "lev": 1.20, "risk": 0.12},
    {"tr": "Acele etmiyorum. Süreyi uzat, fiyatı indir.", "en": "I am not in a hurry. Take longer and lower the price.", "lev": 1.08, "risk": 0.09},
    {"tr": "Bu çeliğin kusuru var. Tam fiyat isteme.", "en": "This steel has a flaw. Do not ask full price.", "lev": 1.16, "risk": 0.22},
    {"tr": "Sonraki işi de sana getiririm; bugünü biraz kır.", "en": "I will bring the next job too. Cut today's price a little.", "lev": 1.05, "risk": 0.10},
    {"tr": "Eski parçayı sende bırakırım; hurdasını fiyattan düş.", "en": "Keep the old part and deduct its scrap value.", "lev": 1.24, "risk": 0.18},
    {"tr": "Sadece gereken perçinleri değiştir. Fazlasını istemiyorum.", "en": "Replace only what is needed. I do not want extra work.", "lev": 0.92, "risk": 0.08},
    {"tr": "Malzeme ile ustalığı ayrı hesapla.", "en": "Price the material and workmanship separately.", "lev": 1.34, "risk": 0.25},
    {"tr": "Bu işi başka demirci de yapar. Beni burada tutacak fiyatı söyle.", "en": "Another smith can do this. Give me a reason to stay here.", "lev": 1.28, "risk": 0.36},
    {"tr": "Sökümü ben yaparım; o saati benden alma.", "en": "I will do the disassembly. Do not charge me for that hour.", "lev": 1.12, "risk": 0.11},
    {"tr": "Yarısını peşin veririm. Karşılığında fiyatı indir.", "en": "I pay half up front. Lower the price in return.", "lev": 0.94, "risk": 0.07},
    {"tr": "Süs istemiyorum. Sadece işini yap.", "en": "I want no decoration. Just do the work.", "lev": 0.98, "risk": 0.05},
    {"tr": "Tek rakamım bu, Reinald. Kabul edersen başla.", "en": "That is my one number, Reinald. Take it and start.", "lev": 1.22, "risk": 0.27},
)
# </POTBO_STAGE S2396>

# <POTBO_STAGE S2398>



_v96_merchant_ac_original = merchant_ac


def merchant_ac():
    result = _v96_merchant_ac_original()
    merchant_diyalog_yaz(
        bt(
            "Ben Hanus. Malı görürsün, fiyatı benden duyarsın. İkisini birbirine karıştırma.",
            "I am Hanus. You see the goods; you hear the price from me. Do not confuse the two.",
        )
    )
    return result


_v96_blacksmith_ac_original = blacksmith_ac


def blacksmith_ac():
    result = _v96_blacksmith_ac_original()
    global blacksmith_mesaji
    blacksmith_mesaji = bt(
        "Ben Reinald. Çeliğin varsa konuş; işim temizdir, fiyatım da açık.",
        "I am Reinald. If it is steel, speak; my work is clean and my price is plain.",
    )
    return result


def v92_merchant_haggle_begin():
    global merchant_modal, merchant_bekleyen_islem
    global v92_merchant_haggle_choices, v92_merchant_haggle_index
    global v92_merchant_haggle_round, v92_merchant_haggle_score
    global v92_merchant_haggle_seed, v92_merchant_haggle_mode, v92_merchant_fake_quote
    global v96_son_ikna_basarili, v96_hanus_hile_yakalandi

    if merchant_sayfa == "buy":
        record = v92_merchant_current_record()
        if not isinstance(record, dict) or record.get("sold"):
            return False
        if not merchant_bekleyen_islem or merchant_bekleyen_islem.get("type") != "buy":
            merchant_bekleyen_islem = {
                "type": "buy",
                "record": dict(record),
                "quantity": 1,
                "unit_price": int(record.get("price", 1)),
                "price": int(record.get("price", 1)),
            }
        v92_merchant_haggle_mode = "buy"
    else:
        sale = v92_merchant_current_record()
        if not isinstance(sale, tuple) or len(sale) != 2:
            return False
        slot, item = sale
        base = int(MERCHANT_SATIS_REFERANSI.get(item.get("id"), 1))
        merchant_bekleyen_islem = {
            "type": "sell",
            "slot": slot,
            "item_id": item.get("id"),
            "quantity": 1,
            "unit_price": base,
            "price": base,
        }
        v92_merchant_haggle_mode = "sell"

    v92_merchant_haggle_round = 0
    v92_merchant_haggle_score = 0.0
    v92_merchant_haggle_index = 0
    v92_merchant_haggle_seed = pygame.time.get_ticks() ^ int(oyuncu_level * 733) ^ int(oyuncu_altin * 3)
    v92_merchant_fake_quote = False
    v96_son_ikna_basarili = None
    v96_hanus_hile_yakalandi = False
    v92_merchant_haggle_choices = v92_haggle_choices(v92_merchant_haggle_seed, 0, V92_MERCHANT_HAGGLE_PATHS)
    merchant_modal = "haggle"
    merchant_diyalog_yaz(
        bt(
            "Pazarlık istiyorsun demek. Üç cümlen var; beni ikna edersen fiyat oynar.",
            "So you want to bargain. You get three lines; convince me and the price moves.",
        )
    )
    return True


def v92_merchant_haggle_choose():
    global v92_merchant_haggle_round, v92_merchant_haggle_score
    global v92_merchant_haggle_choices, v92_merchant_haggle_index
    global merchant_modal, v92_merchant_fake_quote, v92_merchant_reputation
    global v96_ikna_xp, v96_son_ikna_sansi, v96_son_ikna_basarili
    global v96_hanus_hile_yakalandi, v96_hanus_hile_sayisi

    if not v92_merchant_haggle_choices:
        return

    tactic = v92_merchant_haggle_choices[v92_merchant_haggle_index % len(v92_merchant_haggle_choices)]
    rng = random.Random(v92_merchant_haggle_seed ^ (v92_merchant_haggle_round * 7717) ^ int(tactic["lev"] * 1000))
    chance = v96_ikna_sansi(tactic, "hanus")
    success = rng.random() < chance
    v96_son_ikna_sansi = chance
    v96_son_ikna_basarili = success

    risk = float(tactic.get("risk", 0.20))
    leverage = float(tactic.get("lev", 1.0))
    v92_merchant_haggle_score += leverage * (1.0 if success else -0.72 - risk * 0.35)
    if success:
        v96_ikna_xp += 1
        v92_merchant_reputation = min(3.0, v92_merchant_reputation + 0.06)
    else:
        v92_merchant_reputation = max(-3.0, v92_merchant_reputation - 0.07)


    cheat_chance = min(0.52, 0.17 + risk * 0.38 + max(0.0, -v92_merchant_reputation) * 0.025)
    tried_cheat = rng.random() < cheat_chance
    caught = False
    if tried_cheat:
        v96_hanus_hile_sayisi += 1
        detect_chance = min(0.86, 0.24 + v96_ikna_ustaligi() * 0.045 + (0.13 if success else 0.0))
        caught = rng.random() < detect_chance
        if caught:
            v96_hanus_hile_yakalandi = True
            v92_merchant_fake_quote = False
            v92_merchant_haggle_score += 0.42
            counter = bt(
                "Gözün iyiymiş. Evet, ikinci rakamı fark ettin. Tamam; o numara bu tur işlemedi.",
                "Sharp eyes. Yes, you caught the second number. Fine; that trick did not work this round.",
            )
        else:
            v92_merchant_fake_quote = True
            counter = bt(
                "Tamam, sana özel bir rakam yazıyorum. Kağıttaki küçük düzeltmeye takılma.",
                "Fine, I am writing you a special number. Do not worry about the little correction on the paper.",
            )
    else:
        if dil == "TR":
            counter = rng.choice(V96_HANUS_BASARI_TR if success else V96_HANUS_BASARISIZ_TR)
        else:
            counter = rng.choice(V96_HANUS_BASARI_EN if success else V96_HANUS_BASARISIZ_EN)

    v92_merchant_haggle_round += 1
    if v92_merchant_haggle_round >= 3:
        v92_merchant_haggle_finalize(counter)
        return

    v92_merchant_haggle_choices = v92_haggle_choices(
        v92_merchant_haggle_seed,
        v92_merchant_haggle_round,
        V92_MERCHANT_HAGGLE_PATHS,
    )
    v92_merchant_haggle_index = 0
    merchant_diyalog_yaz(counter)


def v92_merchant_haggle_finalize(counter_text=""):
    global merchant_modal, merchant_onay_index
    txn = merchant_bekleyen_islem or {}
    base_unit = max(1, int(txn.get("unit_price", txn.get("price", 1))))
    quantity = max(1, int(txn.get("quantity", 1)))

    if v92_merchant_haggle_mode == "buy":
        discount = max(-0.08, min(0.24, v92_merchant_haggle_score * 0.037))
        if v92_merchant_fake_quote:
            discount -= 0.045
        final_unit = max(1, int(round(base_unit * (1.0 - discount))))
    else:
        premium = max(-0.12, min(0.34, v92_merchant_haggle_score * 0.045))
        if v92_merchant_fake_quote:
            premium -= 0.055
        final_unit = max(1, int(round(base_unit * (1.0 + premium))))

    txn["unit_price"] = final_unit
    txn["price"] = final_unit * quantity
    txn["haggle_score"] = round(v92_merchant_haggle_score, 3)
    merchant_onay_index = 1
    merchant_modal = "confirm"

    if v92_merchant_fake_quote:
        final_line = bt(
            f"Az önceki rakam taslaktı. Kağıtta {txn['price']} coin yazıyor; anlaşma buysa el sıkışırız.",
            f"The earlier number was a draft. The paper says {txn['price']} coins; if that is the deal, we shake on it.",
        )
    else:
        final_line = bt(
            f"Son rakam {txn['price']} coin. Bundan sonrası evet ya da hayır.",
            f"Final number: {txn['price']} coins. From here it is yes or no.",
        )
    merchant_diyalog_yaz(counter_text or final_line, final_line)


def v92_blacksmith_haggle_begin(kind):
    global blacksmith_modal, blacksmith_haggle_choices, blacksmith_haggle_index
    global blacksmith_haggle_round, blacksmith_haggle_score, blacksmith_seed
    global blacksmith_pending, blacksmith_fiyat, blacksmith_mesaji
    global v96_son_ikna_basarili

    blacksmith_pending = {"type": "upgrade", "kind": kind}
    blacksmith_fiyat = v92_blacksmith_upgrade_cost(kind)
    blacksmith_haggle_round = 0
    blacksmith_haggle_score = 0.0
    blacksmith_haggle_index = 0
    blacksmith_seed = pygame.time.get_ticks() ^ (oyuncu_level * 811) ^ (blacksmith_fiyat * 7)
    blacksmith_haggle_choices = v92_haggle_choices(blacksmith_seed, 0, V92_BLACKSMITH_HAGGLE_PATHS)
    blacksmith_modal = "haggle"
    v96_son_ikna_basarili = None
    blacksmith_mesaji = bt(
        "Peki. Fiyatı konuşalım. Bana gerçekten masrafı düşüren bir sebep söyle.",
        "Fine. Let us talk price. Give me a reason that actually lowers the cost.",
    )


def v92_blacksmith_haggle_choose():
    global blacksmith_haggle_round, blacksmith_haggle_score, blacksmith_haggle_index
    global blacksmith_haggle_choices, blacksmith_modal, blacksmith_fiyat, blacksmith_mesaji
    global v96_ikna_xp, v96_son_ikna_sansi, v96_son_ikna_basarili

    if not blacksmith_haggle_choices:
        return
    tactic = blacksmith_haggle_choices[blacksmith_haggle_index % len(blacksmith_haggle_choices)]
    rng = random.Random(blacksmith_seed ^ (blacksmith_haggle_round * 4909) ^ int(tactic["lev"] * 1000))
    chance = v96_ikna_sansi(tactic, "reinald")
    success = rng.random() < chance
    v96_son_ikna_sansi = chance
    v96_son_ikna_basarili = success
    blacksmith_haggle_score += float(tactic["lev"]) * (1.0 if success else -0.70)
    if success:
        v96_ikna_xp += 1

    if dil == "TR":
        response = rng.choice(V96_REINALD_BASARI_TR if success else V96_REINALD_BASARISIZ_TR)
    else:
        response = rng.choice(V96_REINALD_BASARI_EN if success else V96_REINALD_BASARISIZ_EN)

    blacksmith_haggle_round += 1
    if blacksmith_haggle_round >= 3:
        discount = max(-0.05, min(0.22, blacksmith_haggle_score * 0.036))
        blacksmith_fiyat = max(
            1,
            int(round(v92_blacksmith_upgrade_cost(blacksmith_pending["kind"]) * (1.0 - discount))),
        )
        blacksmith_modal = "confirm"
        blacksmith_mesaji = bt(
            f"{response} Son rakamım {blacksmith_fiyat} coin.",
            f"{response} My final number is {blacksmith_fiyat} coins.",
        )
        return

    blacksmith_haggle_choices = v92_haggle_choices(
        blacksmith_seed,
        blacksmith_haggle_round,
        V92_BLACKSMITH_HAGGLE_PATHS,
    )
    blacksmith_haggle_index = 0
    blacksmith_mesaji = response





def _v96_vendor_shell(name, role):
    panel = pygame.Rect(32, 24, GENISLIK - 64, YUKSEKLIK - 48)
    merchant_panel_ciz(panel, KOYU_KIRMIZI, 3)
    pygame.draw.rect(ekran, PARLAK_KIRMIZI, panel.inflate(-10, -10), 1)

    title_rect = yazi_yaz(name, panel.x + 28, panel.y + 31, PARLAK_KIRMIZI, menu_baslik_font)
    role_x = min(panel.right - 330, title_rect.right + 16)
    yazi_yaz(role, role_x, panel.y + 42, V91_UI_GREY, mini_font)

    gold = pygame.Rect(panel.right - 150, panel.y + 16, 118, 42)
    merchant_panel_ciz(gold, KOYU_KIRMIZI, 1, (12, 8, 11))
    merchant_fiyat_ciz(
        pygame.Rect(gold.x + 14, gold.y + 7, gold.width - 28, 28),
        oyuncu_altin,
        False,
        BEYAZ,
    )
    return panel


def merchant_diyalog_kutusu_ciz(panel):
    box = pygame.Rect(panel.x + 24, panel.bottom - 190, panel.width - 48, 154)
    merchant_panel_ciz(box, V91_UI_RED, 2)
    yazi_yaz("HANUS", box.x + 20, box.y + 25, V91_UI_RED_HOT, normal_font)

    if merchant_modal == "quantity":
        record = (merchant_bekleyen_islem or {}).get("record", {})
        available = max(0, int(record.get("remaining", 0)))
        yazi_yaz(bt("MİKTAR", "QUANTITY"), box.x + 20, box.y + 59, V91_UI_GREY, mini_font)
        field = pygame.Rect(box.x + 118, box.y + 49, 128, 35)
        merchant_panel_ciz(field, V91_UI_WHITE, 1, V91_UI_BLACK)
        yazi_yaz(v92_merchant_quantity_input or "0", field.centerx, field.centery, V91_UI_WHITE, normal_font, True)
        yazi_yaz(bt(f"Stok: {available}", f"Stock: {available}"), box.x + 20, box.y + 105, ACIK_GRI, mini_font)
        return

    if merchant_modal == "haggle":
        yazi_yaz(
            bt(f"PAZARLIK {v92_merchant_haggle_round + 1}/3", f"HAGGLE {v92_merchant_haggle_round + 1}/3"),
            box.x + 20,
            box.y + 55,
            V91_UI_GOLD,
            mini_font,
        )
        selected_tactic = None
        if v92_merchant_haggle_choices:
            selected_tactic = v92_merchant_haggle_choices[v92_merchant_haggle_index % len(v92_merchant_haggle_choices)]
        chance = v96_ikna_sansi(selected_tactic or {}, "hanus")
        yazi_yaz(
            bt(f"İKNA %{int(round(chance * 100))} · USTALIK {v96_ikna_ustaligi()}", f"PERSUADE {int(round(chance * 100))}% · SKILL {v96_ikna_ustaligi()}"),
            box.right - 20,
            box.y + 55,
            V91_UI_GOLD,
            mini_font,
            False,
        )
        for i, tactic in enumerate(v92_merchant_haggle_choices):
            selected = i == v92_merchant_haggle_index
            value = tactic["tr" if dil == "TR" else "en"]
            yazi_yaz(("> " if selected else "  ") + value, box.x + 20, box.y + 78 + i * 21, V91_UI_WHITE if selected else V91_UI_GREY, mini_font)
        return

    if merchant_modal == "confirm":
        txn = merchant_bekleyen_islem or {}
        total = int(txn.get("price", 0))
        msg = merchant_diyalog_gorunen_metin() or bt("Bu rakam son.", "That number is final.")
        lines = metni_satirlara_bol(msg, oyun_kucuk_font, box.width - 270)
        for i, line in enumerate(lines[:3]):
            yazi_yaz(line, box.x + 20, box.y + 58 + i * 21, ACIK_GRI, oyun_kucuk_font)
        merchant_fiyat_ciz(pygame.Rect(box.right - 220, box.y + 68, 190, 38), total, True, V91_UI_GOLD)
        return

    lines = metni_satirlara_bol(merchant_diyalog_gorunen_metin() or "...", oyun_kucuk_font, box.width - 40)
    for i, line in enumerate(lines[:4]):
        yazi_yaz(line, box.x + 20, box.y + 58 + i * 21, ACIK_GRI, oyun_kucuk_font)


def _v95_blacksmith_dialogue(panel):
    box = pygame.Rect(panel.x + 24, panel.bottom - 190, panel.width - 48, 154)
    merchant_panel_ciz(box, V91_UI_RED, 2)
    yazi_yaz("REINALD", box.x + 20, box.y + 25, V91_UI_RED_HOT, normal_font)

    if blacksmith_modal == "haggle":
        yazi_yaz(
            bt(f"PAZARLIK {blacksmith_haggle_round + 1}/3", f"HAGGLE {blacksmith_haggle_round + 1}/3"),
            box.x + 20,
            box.y + 55,
            V91_UI_GOLD,
            mini_font,
        )
        selected_tactic = None
        if blacksmith_haggle_choices:
            selected_tactic = blacksmith_haggle_choices[blacksmith_haggle_index % len(blacksmith_haggle_choices)]
        chance = v96_ikna_sansi(selected_tactic or {}, "reinald")
        yazi_yaz(
            bt(f"İKNA %{int(round(chance * 100))} · USTALIK {v96_ikna_ustaligi()}", f"PERSUADE {int(round(chance * 100))}% · SKILL {v96_ikna_ustaligi()}"),
            box.right - 20,
            box.y + 55,
            V91_UI_GOLD,
            mini_font,
            False,
        )
        for i, tactic in enumerate(blacksmith_haggle_choices):
            selected = i == blacksmith_haggle_index
            value = tactic["tr" if dil == "TR" else "en"]
            yazi_yaz(("> " if selected else "  ") + value, box.x + 20, box.y + 78 + i * 21, V91_UI_WHITE if selected else V91_UI_GREY, mini_font)
        return

    if blacksmith_modal == "weight":
        choices = (bt("HAFİFLET", "LIGHTEN"), bt("DENGELİ", "BALANCED"), bt("AĞIRLAŞTIR", "HEAVIER"))
        yazi_yaz(bt("Zırhın ağırlığını nasıl ayarlayayım?", "How should I set the armor weight?"), box.x + 20, box.y + 61, V91_UI_WHITE, mini_font)
        yazi_yaz("   ".join((">" if i == blacksmith_weight_index else " ") + choice for i, choice in enumerate(choices)), box.x + 20, box.y + 96, V91_UI_GOLD, mini_font)
        return

    if blacksmith_modal == "confirm":
        msg = str(blacksmith_mesaji or bt("Bu benim son rakamım.", "That is my final number."))
        lines = metni_satirlara_bol(msg, oyun_kucuk_font, box.width - 270)
        for i, line in enumerate(lines[:3]):
            yazi_yaz(line, box.x + 20, box.y + 58 + i * 21, ACIK_GRI, oyun_kucuk_font)
        merchant_fiyat_ciz(pygame.Rect(box.right - 220, box.y + 68, 190, 38), blacksmith_fiyat, True, V91_UI_GOLD)
        return

    msg = str(blacksmith_mesaji or "...")

    for fragment in (
        " F pazarlık, E kabul.", " F haggles; E accepts.",
        "E: seç · F: pazarlık", "E: select · F: haggle",
        "E: 1 saat eğitim", "E: train 1 hour",
    ):
        msg = msg.replace(fragment, "")
    lines = metni_satirlara_bol(msg, oyun_kucuk_font, box.width - 40)
    for i, line in enumerate(lines[:4]):
        yazi_yaz(line, box.x + 20, box.y + 58 + i * 21, ACIK_GRI, oyun_kucuk_font)


def merchant_ekrani_ciz():
    merchant_guncelle()
    if oyun_durumu != MERCHANT:
        oyun_ekrani_ciz()
        return

    oyun_ekrani_ciz()
    gecen = max(0, pygame.time.get_ticks() - merchant_acilis_zamani)
    oran = max(0.0, min(1.0, gecen / max(1, MERCHANT_ACILIS_FADE_SURESI)))
    oran = oran * oran * (3.0 - 2.0 * oran)
    merchant_taban = ekran.copy() if oran < 1.0 else None

    koyu_kaplama(205)
    panel = _v96_vendor_shell("HANUS", bt("TÜCCAR", "MERCHANT"))
    if merchant_sayfa == "menu":
        merchant_ana_menu_ciz(panel)
    else:
        merchant_alt_sayfa_ciz(panel)
    merchant_diyalog_kutusu_ciz(panel)
    merchant_modal_ciz(panel)

    if merchant_taban is not None:
        merchant_taban.set_alpha(int(round(255 * (1.0 - oran))))
        ekran.blit(merchant_taban, (0, 0))


def blacksmith_ekrani_ciz():
    oyun_ekrani_ciz()
    koyu_kaplama(205)
    panel = _v96_vendor_shell("REINALD", bt("DEMİRCİ", "BLACKSMITH"))

    smith_frame = v92_blacksmith_actor_surface()
    if blacksmith_sayfa == "menu":
        _v95_vendor_main_menu(
            panel,
            smith_frame,
            (bt("YETENEK", "SKILL"), bt("GELİŞTİR", "UPGRADE"), bt("ÇIKIŞ", "EXIT")),
            blacksmith_menu_index,
        )
    else:
        portrait, list_rect, info = _v95_vendor_sub_geometry(panel)
        _v95_vendor_portrait(portrait, smith_frame)
        merchant_panel_ciz(list_rect, V91_UI_RED, 1)
        yazi_yaz(
            bt("YETENEK", "SKILL") if blacksmith_sayfa == "skills" else bt("GELİŞTİR", "UPGRADE"),
            list_rect.centerx,
            list_rect.y + 28,
            V91_UI_RED_HOT,
            normal_font,
            True,
        )
        rows = _v95_blacksmith_rows()
        selection = max(0, min(len(rows) - 1, int(blacksmith_index)))
        row_h = 72
        for row_no, row_data in enumerate(rows):
            row = pygame.Rect(list_rect.x + 12, list_rect.y + 58 + row_no * (row_h + 10), list_rect.width - 24, row_h)
            _v95_blacksmith_list_row(row, row_data, row_no == selection)
        _v95_blacksmith_info(info, rows[selection])

    _v95_blacksmith_dialogue(panel)
# </POTBO_STAGE S2398>

# <POTBO_STAGE S2400>















V97_VERSION = "97.0"
# </POTBO_STAGE S2400>

# <POTBO_STAGE S2402>





def _v97_vendor_shell(role):
    panel = pygame.Rect(32, 24, GENISLIK - 64, YUKSEKLIK - 48)
    merchant_panel_ciz(panel, KOYU_KIRMIZI, 3)
    pygame.draw.rect(ekran, PARLAK_KIRMIZI, panel.inflate(-10, -10), 1)



    yazi_yaz(
        role,
        panel.x + 28,
        panel.y + 31,
        PARLAK_KIRMIZI,
        menu_baslik_font,
    )

    gold = pygame.Rect(panel.right - 150, panel.y + 16, 118, 42)
    merchant_panel_ciz(gold, KOYU_KIRMIZI, 1, (12, 8, 11))
    merchant_fiyat_ciz(
        pygame.Rect(gold.x + 14, gold.y + 7, gold.width - 28, 28),
        oyuncu_altin,
        False,
        BEYAZ,
    )
    return panel


def _v97_vendor_main(panel, frame, options, selected, new_badge_index=None):
    """Exact same main-menu geometry for every vendor."""
    portrait, option_rect = _v95_vendor_main_geometry(panel)
    _v95_vendor_portrait(portrait, frame)

    for i, label in enumerate(options):
        button = pygame.Rect(
            option_rect.x + 60,
            option_rect.y + 55 + i * 86,
            option_rect.width - 120,
            62,
        )
        badge = bt("YENİ", "NEW") if new_badge_index == i else None
        merchant_menu_butonu_ciz(button, label, i == selected, badge)


def _v97_vendor_sub_geometry(panel):

    return _v95_vendor_sub_geometry(panel)





def _v97_hanus_main(panel):
    _v97_vendor_main(
        panel,
        _v95_merchant_current_idle(),
        (bt("SAT", "SELL"), bt("AL", "BUY"), bt("ÇIKIŞ", "EXIT")),
        merchant_menu_index,
        1 if merchant_yeni_urun_var_mi() else None,
    )


def _v97_hanus_subpage(panel):


    portrait, list_rect, info = _v97_vendor_sub_geometry(panel)
    _v95_vendor_portrait(portrait, _v95_merchant_current_idle())
    merchant_panel_ciz(list_rect, V91_UI_RED, 1)

    yazi_yaz(
        bt("SAT", "SELL") if merchant_sayfa == "sell" else bt("AL", "BUY"),
        list_rect.centerx,
        list_rect.y + 28,
        V91_UI_RED_HOT,
        normal_font,
        True,
    )

    records = merchant_aktif_liste()
    if not records:
        yazi_yaz(
            bt("Liste boş.", "The list is empty."),
            list_rect.centerx,
            list_rect.centery,
            V91_UI_GREY,
            kucuk_font,
            True,
        )
        merchant_panel_ciz(info, V91_UI_RED, 1)
        return

    selection = merchant_index % len(records)
    start = max(0, min(selection - 2, max(0, len(records) - 6)))

    for row_no, record in enumerate(records[start : start + 6]):
        idx = start + row_no
        sold = False
        remaining = None

        if merchant_sayfa == "sell":
            _, item = record
            price = int(MERCHANT_SATIS_REFERANSI.get(item.get("id"), 1))
        else:
            if record.get("source") == "buyback" and isinstance(record.get("item"), dict):
                item = record["item"]
            else:
                item = merchant_item_olustur(record.get("id")) or {
                    "id": record.get("id"),
                    "name": "",
                }
            price = int(record.get("price", 1))
            sold = bool(record.get("sold"))
            remaining = int(record.get("remaining", 0))

        new_item = (
            merchant_sayfa == "buy"
            and isinstance(record, dict)
            and record.get("source") == "stock"
            and str(record.get("id")) in merchant_yeni_urun_idleri()
        )

        merchant_liste_satiri_ciz(
            pygame.Rect(
                list_rect.x + 12,
                list_rect.y + 54 + row_no * 58,
                list_rect.width - 24,
                50,
            ),
            item,
            price,
            idx == selection,
            new_item,
            sold,
            remaining,
        )

    record = records[selection]
    if merchant_sayfa == "sell":
        _, item = record
        price = int(MERCHANT_SATIS_REFERANSI.get(item.get("id"), 1))
    else:
        item = (
            record.get("item")
            if record.get("source") == "buyback"
            else merchant_item_olustur(record.get("id"))
        )
        item = item if isinstance(item, dict) else {
            "name": "",
            "id": record.get("id"),
        }
        price = int(record.get("price", 1))

    merchant_item_bilgi_ciz(info, item, price)





def _v97_reinald_row(rect, row_data, selected):
    """Merchant row grammar: price left, name center, compact icon right."""
    rect = pygame.Rect(rect)
    base = (34, 8, 13) if selected else (10, 8, 11)
    edge = V91_UI_RED_HOT if selected else V91_UI_RED
    merchant_panel_ciz(rect, edge, 2 if selected else 1, base)

    progress = int(v92_training.get(row_data["id"], 0)) if blacksmith_sayfa == "skills" else 0
    learned = blacksmith_sayfa == "skills" and progress >= 5

    if learned:
        yazi_yaz(
            bt("ÖĞRENİLDİ", "LEARNED"),
            rect.x + 14,
            rect.centery,
            V91_UI_GOLD,
            mini_font,
        )
    else:
        merchant_fiyat_ciz(
            pygame.Rect(rect.x + 10, rect.y + 12, 86, rect.height - 24),
            int(row_data.get("price", 0)),
            False,
            V91_UI_GOLD,
        )

    yazi_yaz(
        row_data.get("name", ""),
        rect.x + 112,
        rect.centery,
        V91_UI_WHITE,
        oyun_kucuk_font,
    )

    if blacksmith_sayfa == "skills" and not learned:
        yazi_yaz(
            f"{progress}/5",
            rect.right - 76,
            rect.bottom - 12,
            V91_UI_GREY,
            mini_font,
            True,
        )

    icon = pygame.Rect(rect.right - 46, rect.y + 7, 38, 38)
    merchant_panel_ciz(icon, V91_UI_RED_HOT if selected else V91_UI_GREY, 1)
    yazi_yaz(
        str(row_data.get("icon", "")),
        icon.centerx,
        icon.centery,
        V91_UI_GOLD if selected else V91_UI_WHITE,
        mini_font,
        True,
    )


def _v97_reinald_info(rect, row_data):
    """Merchant item-info grammar, but the payload is an upgrade/skill."""
    rect = pygame.Rect(rect)
    merchant_panel_ciz(rect, KOYU_KIRMIZI, 1)

    yazi_yaz(
        row_data.get("name", ""),
        rect.x + 22,
        rect.y + 30,
        PARLAK_KIRMIZI,
        normal_font,
    )
    category = bt("YETENEK", "SKILL") if blacksmith_sayfa == "skills" else bt("GELİŞTİRME", "UPGRADE")
    yazi_yaz(category, rect.x + 22, rect.y + 60, GRI, mini_font)

    icon = pygame.Rect(rect.x + 22, rect.y + 92, 92, 92)
    merchant_panel_ciz(icon, V91_UI_RED_HOT, 2)
    yazi_yaz(
        str(row_data.get("icon", "")),
        icon.centerx,
        icon.centery,
        V91_UI_GOLD,
        oyun_buyuk_font,
        True,
    )

    desc_lines = metni_satirlara_bol(
        str(row_data.get("description", "")),
        oyun_kucuk_font,
        rect.width - 156,
    )
    for i, line in enumerate(desc_lines[:8]):
        yazi_yaz(
            line,
            icon.right + 18,
            rect.y + 98 + i * 21,
            ACIK_GRI,
            oyun_kucuk_font,
        )

    value = pygame.Rect(rect.x + 22, rect.bottom - 64, rect.width - 44, 44)
    merchant_panel_ciz(value, KOYU_KIRMIZI, 1, (17, 9, 12))

    if blacksmith_sayfa == "skills":
        progress = int(v92_training.get(row_data["id"], 0))
        left_text = bt(f"EĞİTİM {progress}/5", f"TRAINING {progress}/5")
        yazi_yaz(left_text, value.x + 14, value.centery, PARLAK_KIRMIZI, kucuk_font)
        if progress < 5:
            merchant_fiyat_ciz(
                pygame.Rect(value.right - 105, value.y + 8, 90, 28),
                int(row_data.get("price", 0)),
                True,
                BEYAZ,
            )
    else:
        tier = int(v92_blacksmith_upgrades.get(row_data["id"], 0))
        yazi_yaz(
            bt(f"KADEME {tier}", f"TIER {tier}"),
            value.x + 14,
            value.centery,
            PARLAK_KIRMIZI,
            kucuk_font,
        )
        merchant_fiyat_ciz(
            pygame.Rect(value.right - 105, value.y + 8, 90, 28),
            int(row_data.get("price", 0)),
            True,
            BEYAZ,
        )


def _v97_reinald_main(panel):
    _v97_vendor_main(
        panel,
        v92_blacksmith_actor_surface(),
        (bt("YETENEK", "SKILL"), bt("GELİŞTİR", "UPGRADE"), bt("ÇIKIŞ", "EXIT")),
        blacksmith_menu_index,
    )


def _v97_reinald_subpage(panel):
    portrait, list_rect, info = _v97_vendor_sub_geometry(panel)
    _v95_vendor_portrait(portrait, v92_blacksmith_actor_surface())
    merchant_panel_ciz(list_rect, V91_UI_RED, 1)

    yazi_yaz(
        bt("YETENEK", "SKILL") if blacksmith_sayfa == "skills" else bt("GELİŞTİR", "UPGRADE"),
        list_rect.centerx,
        list_rect.y + 28,
        V91_UI_RED_HOT,
        normal_font,
        True,
    )

    rows = list(_v95_blacksmith_rows())
    if not rows:
        yazi_yaz(
            bt("Liste boş.", "The list is empty."),
            list_rect.centerx,
            list_rect.centery,
            V91_UI_GREY,
            kucuk_font,
            True,
        )
        merchant_panel_ciz(info, V91_UI_RED, 1)
        return

    selection = max(0, min(len(rows) - 1, int(blacksmith_index)))
    start = max(0, min(selection - 2, max(0, len(rows) - 6)))
    for row_no, row_data in enumerate(rows[start : start + 6]):
        idx = start + row_no
        _v97_reinald_row(
            pygame.Rect(
                list_rect.x + 12,
                list_rect.y + 54 + row_no * 58,
                list_rect.width - 24,
                50,
            ),
            row_data,
            idx == selection,
        )

    _v97_reinald_info(info, rows[selection])
# </POTBO_STAGE S2402>

# <POTBO_STAGE S2404>


def merchant_diyalog_kutusu_ciz(panel):
    box = _v97_dialogue_box(panel)
    merchant_panel_ciz(box, V91_UI_RED, 2)
    yazi_yaz(V97_HANUS_NAME, box.x + 20, box.y + 25, V91_UI_RED_HOT, normal_font)

    if merchant_modal == "quantity":
        record = (merchant_bekleyen_islem or {}).get("record", {})
        available = max(0, int(record.get("remaining", 0)))
        yazi_yaz(bt("MİKTAR", "QUANTITY"), box.x + 20, box.y + 59, V91_UI_GREY, mini_font)
        field = pygame.Rect(box.x + 118, box.y + 49, 128, 35)
        merchant_panel_ciz(field, V91_UI_WHITE, 1, V91_UI_BLACK)
        yazi_yaz(v92_merchant_quantity_input or "0", field.centerx, field.centery, V91_UI_WHITE, normal_font, True)
        yazi_yaz(bt(f"Stok: {available}", f"Stock: {available}"), box.x + 20, box.y + 105, ACIK_GRI, mini_font)
        return

    if merchant_modal == "haggle":
        yazi_yaz(
            bt(f"PAZARLIK {v92_merchant_haggle_round + 1}/3", f"HAGGLE {v92_merchant_haggle_round + 1}/3"),
            box.x + 20,
            box.y + 55,
            V91_UI_GOLD,
            mini_font,
        )
        selected_tactic = None
        if v92_merchant_haggle_choices:
            selected_tactic = v92_merchant_haggle_choices[v92_merchant_haggle_index % len(v92_merchant_haggle_choices)]
        chance = v96_ikna_sansi(selected_tactic or {}, "hanus")
        yazi_yaz(
            bt(
                f"İKNA %{int(round(chance * 100))} · USTALIK {v96_ikna_ustaligi()}",
                f"PERSUADE {int(round(chance * 100))}% · SKILL {v96_ikna_ustaligi()}",
            ),
            box.right - 20,
            box.y + 55,
            V91_UI_GOLD,
            mini_font,
            False,
        )
        for i, tactic in enumerate(v92_merchant_haggle_choices):
            selected = i == v92_merchant_haggle_index
            value = tactic["tr" if dil == "TR" else "en"]
            yazi_yaz(("> " if selected else "  ") + value, box.x + 20, box.y + 78 + i * 21, V91_UI_WHITE if selected else V91_UI_GREY, mini_font)
        return

    if merchant_modal == "confirm":
        txn = merchant_bekleyen_islem or {}
        total = int(txn.get("price", 0))
        msg = merchant_diyalog_gorunen_metin() or bt("Bu rakam son.", "That number is final.")
        lines = metni_satirlara_bol(msg, oyun_kucuk_font, box.width - 270)
        for i, line in enumerate(lines[:3]):
            yazi_yaz(line, box.x + 20, box.y + 58 + i * 21, ACIK_GRI, oyun_kucuk_font)
        merchant_fiyat_ciz(pygame.Rect(box.right - 220, box.y + 68, 190, 38), total, True, V91_UI_GOLD)
        return

    lines = metni_satirlara_bol(merchant_diyalog_gorunen_metin() or "...", oyun_kucuk_font, box.width - 40)
    for i, line in enumerate(lines[:4]):
        yazi_yaz(line, box.x + 20, box.y + 58 + i * 21, ACIK_GRI, oyun_kucuk_font)


def _v95_blacksmith_dialogue(panel):
    box = _v97_dialogue_box(panel)
    merchant_panel_ciz(box, V91_UI_RED, 2)
    yazi_yaz(V97_REINALD_NAME, box.x + 20, box.y + 25, V91_UI_RED_HOT, normal_font)

    if blacksmith_modal == "haggle":
        yazi_yaz(
            bt(f"PAZARLIK {blacksmith_haggle_round + 1}/3", f"HAGGLE {blacksmith_haggle_round + 1}/3"),
            box.x + 20,
            box.y + 55,
            V91_UI_GOLD,
            mini_font,
        )
        selected_tactic = None
        if blacksmith_haggle_choices:
            selected_tactic = blacksmith_haggle_choices[blacksmith_haggle_index % len(blacksmith_haggle_choices)]
        chance = v96_ikna_sansi(selected_tactic or {}, "reinald")
        yazi_yaz(
            bt(
                f"İKNA %{int(round(chance * 100))} · USTALIK {v96_ikna_ustaligi()}",
                f"PERSUADE {int(round(chance * 100))}% · SKILL {v96_ikna_ustaligi()}",
            ),
            box.right - 20,
            box.y + 55,
            V91_UI_GOLD,
            mini_font,
            False,
        )
        for i, tactic in enumerate(blacksmith_haggle_choices):
            selected = i == blacksmith_haggle_index
            value = tactic["tr" if dil == "TR" else "en"]
            yazi_yaz(("> " if selected else "  ") + value, box.x + 20, box.y + 78 + i * 21, V91_UI_WHITE if selected else V91_UI_GREY, mini_font)
        return

    if blacksmith_modal == "weight":
        choices = (bt("HAFİFLET", "LIGHTEN"), bt("DENGELİ", "BALANCED"), bt("AĞIRLAŞTIR", "HEAVIER"))
        yazi_yaz(bt("Zırhın ağırlığını nasıl ayarlayayım?", "How should I set the armor weight?"), box.x + 20, box.y + 61, V91_UI_WHITE, mini_font)
        yazi_yaz("   ".join((">" if i == blacksmith_weight_index else " ") + choice for i, choice in enumerate(choices)), box.x + 20, box.y + 96, V91_UI_GOLD, mini_font)
        return

    if blacksmith_modal == "confirm":
        msg = str(blacksmith_mesaji or bt("Bu benim son rakamım.", "That is my final number."))
        lines = metni_satirlara_bol(msg, oyun_kucuk_font, box.width - 270)
        for i, line in enumerate(lines[:3]):
            yazi_yaz(line, box.x + 20, box.y + 58 + i * 21, ACIK_GRI, oyun_kucuk_font)
        merchant_fiyat_ciz(pygame.Rect(box.right - 220, box.y + 68, 190, 38), blacksmith_fiyat, True, V91_UI_GOLD)
        return

    msg = str(blacksmith_mesaji or "...")
    lines = metni_satirlara_bol(msg, oyun_kucuk_font, box.width - 40)
    for i, line in enumerate(lines[:4]):
        yazi_yaz(line, box.x + 20, box.y + 58 + i * 21, ACIK_GRI, oyun_kucuk_font)





def merchant_ekrani_ciz():
    merchant_guncelle()
    if oyun_durumu != MERCHANT:
        oyun_ekrani_ciz()
        return

    oyun_ekrani_ciz()
    gecen = max(0, pygame.time.get_ticks() - merchant_acilis_zamani)
    oran = max(0.0, min(1.0, gecen / max(1, MERCHANT_ACILIS_FADE_SURESI)))
    oran = oran * oran * (3.0 - 2.0 * oran)
    merchant_taban = ekran.copy() if oran < 1.0 else None

    koyu_kaplama(205)
    panel = _v97_vendor_shell(bt("TÜCCAR", "MERCHANT"))
    if merchant_sayfa == "menu":
        _v97_hanus_main(panel)
    else:
        _v97_hanus_subpage(panel)
    merchant_diyalog_kutusu_ciz(panel)
    merchant_modal_ciz(panel)

    if merchant_taban is not None:
        merchant_taban.set_alpha(int(round(255 * (1.0 - oran))))
        ekran.blit(merchant_taban, (0, 0))


def blacksmith_ekrani_ciz():
    oyun_ekrani_ciz()
    koyu_kaplama(205)
    panel = _v97_vendor_shell(bt("DEMİRCİ", "BLACKSMITH"))

    if blacksmith_sayfa == "menu":
        _v97_reinald_main(panel)
    else:
        _v97_reinald_subpage(panel)

    _v95_blacksmith_dialogue(panel)





def _v97_vendor_carpisma_rect(x, y, width=42, height=22):
    return pygame.Rect(
        int(round(float(x))) - int(width // 2),
        int(round(float(y))) - int(height),
        int(width),
        int(height),
    )


def merchant_carpisma_rect():

    return _v97_vendor_carpisma_rect(merchant_x, merchant_y, 40, 21)


def blacksmith_carpisma_rect():
    return _v97_vendor_carpisma_rect(blacksmith_x, blacksmith_y, 42, 22)


def _v97_vendor_yakin_mi(rect, x_pad=48, y_pad=42):
    player_rect = oyuncu_carpisma_rect(oyuncu_x, oyuncu_y)
    return player_rect.colliderect(rect.inflate(int(x_pad * 2), int(y_pad * 2)))


def merchant_yakin_mi():
    return _v97_vendor_yakin_mi(merchant_carpisma_rect(), 46, 40)


def blacksmith_yakin_mi():
    return _v97_vendor_yakin_mi(blacksmith_carpisma_rect(), 48, 42)


def _v34_static_blockers():

    return (
        npc_carpisma_rect(),
        merchant_carpisma_rect(),
        blacksmith_carpisma_rect(),
    )
# </POTBO_STAGE S2404>

# <POTBO_STAGE S2406>


def common_enemy_statik_konum_gecerli_mi(tur, x, y, navigation=False):
    if not _v97_common_enemy_static_raw(tur, x, y, navigation=navigation):
        return False
    cfg = COMMON_ENEMY_CONFIG[tur]
    margin = int(cfg.get("nav_margin", 0)) if navigation else 0
    half = int(cfg["body_half_width"]) + margin
    height = int(cfg["body_height"]) + margin
    rect = pygame.Rect(
        int(round(x)) - half,
        int(round(y)) - height,
        half * 2,
        height,
    )
    return not rect.colliderect(blacksmith_carpisma_rect().inflate(margin * 2, margin * 2))
# </POTBO_STAGE S2406>

# <POTBO_STAGE S2408>


def _common_enemy_hizli_statik_gecerli_mi(tur, x, y):
    if not _v97_common_enemy_fast_raw(tur, x, y):
        return False
    cfg = COMMON_ENEMY_CONFIG[tur]
    half = int(cfg["body_half_width"])
    height = int(cfg["body_height"])
    rect = pygame.Rect(int(round(x)) - half, int(round(y)) - height, half * 2, height)
    return not rect.colliderect(blacksmith_carpisma_rect())



def _v97_segment_blocked_by_rect(a, b, blocker):
    a = (int(round(float(a[0]))), int(round(float(a[1]))))
    b = (int(round(float(b[0]))), int(round(float(b[1]))))
    rect = blocker.inflate(-4, -4)
    if rect.width <= 0 or rect.height <= 0:
        rect = blocker
    if not rect.clipline(a, b):
        return False
    return not rect.collidepoint(a) and not rect.collidepoint(b)
# </POTBO_STAGE S2408>

# <POTBO_STAGE S2410>


def common_enemy_saldiri_los_acik_mi(dusman, adim=4.5):
    if not _v97_melee_los_raw(dusman, adim=adim):
        return False
    if dusman is None:
        return False
    start = (float(dusman.x), float(dusman.y) - 7.0)
    end = (float(oyuncu_x), float(oyuncu_y) - 7.0)
    return not _v97_segment_blocked_by_rect(start, end, blacksmith_carpisma_rect())
# </POTBO_STAGE S2410>

# <POTBO_STAGE S2412>


def dunya_ince_los_acik_mi(baslangic, bitis, adim=5.0, npc_bloklar=True):
    if not _v97_thin_los_raw(baslangic, bitis, adim=adim, npc_bloklar=npc_bloklar):
        return False
    if npc_bloklar and _v97_segment_blocked_by_rect(baslangic, bitis, blacksmith_carpisma_rect()):
        return False
    return True
# </POTBO_STAGE S2412>

# <POTBO_STAGE S2415>


def oyun_ekrani_ciz():
    result = _v97_game_draw_raw()

    if (
        etkilesim_ipuclari
        and oyun_durumu == OYUN
        and oyun_alt_durumu == HARITA
        and oyuncu_hp > 0
        and blacksmith_yakin_mi()
    ):
        target = v34_interaction_target()
        if target is not None and target.get("kind") == "blacksmith":
            keycap_ikonu_ciz(
                dunya_ekran_x(blacksmith_x),
                dunya_ekran_y(blacksmith_y) - 82,
                tus_gorunen_adi("interact"),
            )

    return result
# </POTBO_STAGE S2415>

# <POTBO_STAGE S2424>







V98_BLACKSMITH_ADAYLARI = (
    os.path.join(ASSETS, "npcs", "blacksmith", "blacksmith.png"),
    os.path.join(ASSETS, "npcs", "blacksmith", "blacksmith(1).png"),
    os.path.join(BASE_DIR, "blacksmith.png"),
    os.path.join(BASE_DIR, "blacksmith(1).png"),
)
V98_BLACKSMITH_YOLU = mevcut_ilk_dosya(V98_BLACKSMITH_ADAYLARI)
V98_BLACKSMITH_IDLE = (
    _v95_idle_crop(
        V98_BLACKSMITH_YOLU,
        (322, 1775),
        (6, 294, 28, 40),
    )
    if V98_BLACKSMITH_YOLU
    else None
)

if V98_BLACKSMITH_IDLE is not None:
    blacksmith_resmi_orijinal = V98_BLACKSMITH_IDLE
    v94_blacksmith_idle = V98_BLACKSMITH_IDLE
    v95_blacksmith_idle = V98_BLACKSMITH_IDLE


def v92_blacksmith_actor_surface():
    if V98_BLACKSMITH_IDLE is not None:
        return V98_BLACKSMITH_IDLE
    if v95_blacksmith_idle is not None:
        return v95_blacksmith_idle
    if v94_blacksmith_idle is not None:
        return v94_blacksmith_idle
    if blacksmith_resmi_orijinal is not None:
        return blacksmith_resmi_orijinal
    return _v94_blacksmith_fallback()


def blacksmith_world_ciz():
    frame = v92_blacksmith_actor_surface()
    image = _v95_pixel_actor(frame, 72)
    if image is None:
        return
    ekran.blit(
        image,
        image.get_rect(
            midbottom=(
                int(round(dunya_ekran_x(blacksmith_x))),
                int(round(dunya_ekran_y(blacksmith_y))),
            )
        ),
    )
# </POTBO_STAGE S2424>

# <POTBO_STAGE S2433>







def dunya_aktorlerini_derinlige_gore_ciz():
    kan_lekelerini_ciz()
    for p in blood_particles:
        if p.active:
            p.ciz()
    for kurt in blood_maggots:
        if kurt.active:
            kurt.ciz()

    fire_magic_alt_katman_ciz()

    now = pygame.time.get_ticks()
    if v98_projectile_trail_fires:
        v98_projectile_trail_fires[:] = [
            flame for flame in v98_projectile_trail_fires if flame.aktif_mi(now)
        ]

    komutlar = [
        (float(npc_y), 0, npc_ciz),
        (float(merchant_y), 1, merchant_sprite_ciz),
        (float(blacksmith_y), 2, blacksmith_world_ciz),
        (float(oyuncu_y), 3, oyuncu_sprite_ciz),
    ]

    for index, dusman in enumerate(common_enemies):
        if dusman.active and dusman.hp > 0:
            komutlar.append((float(dusman.y), 10 + index, dusman.ciz_govde))

    if tarkard_actor is not None and tarkard_actor.active and tarkard_actor.hp > 0:
        komutlar.append((float(tarkard_actor.y), 30, tarkard_actor.ciz_govde))
    if torrmund_actor is not None and torrmund_actor.active and torrmund_actor.hp > 0:
        komutlar.append((float(torrmund_actor.y), 31, torrmund_actor.ciz_govde))

    marj = 100.0 / max(0.01, KAMERA_YAKINLASTIRMA)
    gx0 = float(kamera_x) - marj
    gy0 = float(kamera_y) - marj
    gx1 = float(kamera_x) + GENISLIK / max(0.01, KAMERA_YAKINLASTIRMA) + marj
    gy1 = float(kamera_y) + YUKSEKLIK / max(0.01, KAMERA_YAKINLASTIRMA) + marj
    gorunen_gore = [g for g in gore_chunks if gx0 <= g.x <= gx1 and gy0 <= g.y <= gy1]
    for index, parca in enumerate(gorunen_gore):
        komutlar.append((float(parca.y), 34 + index, parca.ciz))

    for index, rat in enumerate(ambient_rats):
        if rat.active:
            komutlar.append((float(rat.y), 40 + index, rat.ciz))

    for index, projectile in enumerate(enemy_projectiles):
        if projectile.active:
            komutlar.append((float(projectile.y), 60 + index, projectile.ciz))

    for index, flame in enumerate(v98_projectile_trail_fires):
        komutlar.append((float(flame.y), 63 + index, flame.ciz))

    for index, patch in enumerate(player_magic_ground_fires):
        if patch.active:
            komutlar.append((float(patch.y), 65 + index, patch.ciz))

    for index, projectile in enumerate(player_magic_projectiles):
        if projectile.active:
            komutlar.append((float(projectile.y), 90 + index, projectile.ciz))

    for index, explosion in enumerate(player_magic_explosions):
        if explosion.active:
            komutlar.append((float(explosion.y), 110 + index, explosion.ciz))

    for _, _, cizim in sorted(komutlar, key=lambda kayit: (kayit[0], kayit[1])):
        cizim()

    _simdi_fx = pygame.time.get_ticks()
    for _fx in enemy_rock_impacts:
        _fx.ciz(_simdi_fx)

    for dusman in common_enemies:
        dusman.ciz_ui()
        dusman.ciz_debug_nav()
    if tarkard_actor is not None and tarkard_actor.active:
        tarkard_actor.ciz_ui()
        tarkard_actor.ciz_debug_nav()
    if torrmund_actor is not None and torrmund_actor.active:
        torrmund_actor.ciz_ui()
        torrmund_actor.ciz_debug_nav()


    if "v90_draco_draw" in globals():
        v90_draco_draw(pygame.time.get_ticks())
# </POTBO_STAGE S2433>

# <POTBO_STAGE S2459>







def _v95_blacksmith_rows():
    if blacksmith_sayfa == "skills":
        return (
            {
                "id": "decussatio_rubra",
                "icon": "X",
                "name": V100_SKILL_META["decussatio_rubra"]["name"],
                "description": V100_SKILL_META["decussatio_rubra"]["description"],
                "shortcut": V100_SKILL_META["decussatio_rubra"]["shortcut"],
                "price": 67,
            },
            {
                "id": "catena_decollationis",
                "icon": "C",
                "name": V100_SKILL_META["catena_decollationis"]["name"],
                "description": V100_SKILL_META["catena_decollationis"]["description"],
                "shortcut": V100_SKILL_META["catena_decollationis"]["shortcut"],
                "price": 67,
            },
        )
    return (
        {
            "id": "weapon",
            "icon": "W",
            "name": bt("SİLAH GÜCÜ", "WEAPON POWER"),
            "description": bt(
                "Silahın gerçek vuruş gücünü kontrollü biçimde artırır.",
                "Raises the weapon's actual strike power in controlled increments.",
            ),
            "price": v92_blacksmith_upgrade_cost("weapon"),
        },
        {
            "id": "armor",
            "icon": "A",
            "name": bt("ZIRH DAYANIKLILIĞI", "ARMOR DURABILITY"),
            "description": bt(
                "Zırh korumasını geliştirir; işlem sonunda ağırlık profili seçilir.",
                "Improves armor protection; a weight profile is chosen after the work.",
            ),
            "price": v92_blacksmith_upgrade_cost("armor"),
        },
        {
            "id": "endurance",
            "icon": "E",
            "name": bt("DAYANIKLILIK", "ENDURANCE"),
            "description": bt(
                "Uzun dövüşlerde stamina toleransını artırır.",
                "Improves stamina tolerance in prolonged combat.",
            ),
            "price": v92_blacksmith_upgrade_cost("endurance"),
        },
    )
# </POTBO_STAGE S2459>

# <POTBO_STAGE S2461>


def _v95_blacksmith_list_row(rect, row_data, selected):
    rect = pygame.Rect(rect)
    merchant_panel_ciz(
        rect,
        V91_UI_RED_HOT if selected else V91_UI_RED,
        2 if selected else 1,
        (34, 8, 13) if selected else (10, 8, 11),
    )
    icon = pygame.Rect(rect.x + 10, rect.y + 8, 48, rect.height - 16)
    merchant_panel_ciz(icon, V91_UI_RED_HOT if selected else V91_UI_GREY, 1)
    if blacksmith_sayfa == "skills":
        v100_skill_icon_draw(row_data["id"], icon.inflate(-6, -6), 255 if selected else 210)
    else:
        yazi_yaz(
            row_data["icon"],
            icon.centerx,
            icon.centery,
            V91_UI_GOLD if selected else V91_UI_WHITE,
            normal_font,
            True,
        )

    text_x = icon.right + 12
    reserve_right = 132 if blacksmith_sayfa == "skills" else 124
    _v100_draw_row_name(row_data["name"], text_x, rect.y + 13, rect.right - reserve_right - text_x)

    if blacksmith_sayfa == "skills":
        progress = int(v92_training.get(row_data["id"], 0))
        status = bt("ÖĞRENİLDİ", "LEARNED") if progress >= 5 else bt(
            f"Eğitim {progress}/5", f"Training {progress}/5"
        )
        yazi_yaz(status, rect.right - 12, rect.y + 12, V91_UI_GOLD, mini_font, False)
        if progress < 5:
            merchant_fiyat_ciz(
                pygame.Rect(rect.right - 100, rect.bottom - 31, 88, 24),
                row_data["price"],
                True,
                V91_UI_GOLD,
            )
    else:
        merchant_fiyat_ciz(
            pygame.Rect(rect.right - 118, rect.y + 20, 106, 28),
            row_data["price"],
            True,
            V91_UI_GOLD,
        )


def _v95_blacksmith_info(rect, row_data):
    rect = pygame.Rect(rect)
    merchant_panel_ciz(rect, V91_UI_RED, 1)
    icon = pygame.Rect(rect.centerx - 40, rect.y + 22, 80, 80)
    merchant_panel_ciz(icon, V91_UI_RED_HOT, 2)
    if blacksmith_sayfa == "skills":
        v100_skill_icon_draw(row_data["id"], icon.inflate(-8, -8))
    else:
        yazi_yaz(row_data["icon"], icon.centerx, icon.centery, V91_UI_GOLD, normal_font, True)

    title_font = normal_font if normal_font.size(str(row_data["name"]))[0] <= rect.width - 30 else mini_font
    yazi_yaz(row_data["name"], rect.centerx, icon.bottom + 25, V91_UI_WHITE, title_font, True)

    desc = metni_satirlara_bol(row_data["description"], mini_font, rect.width - 34)
    y = icon.bottom + 59
    max_desc_lines = 8 if blacksmith_sayfa == "skills" else 6
    for line in desc[:max_desc_lines]:
        if y > rect.bottom - 112:
            break
        yazi_yaz(line, rect.x + 17, y, ACIK_GRI, mini_font)
        y += 19

    if blacksmith_sayfa == "skills":
        progress = int(v92_training.get(row_data["id"], 0))
        yazi_yaz(
            bt(f"Eğitim: {progress}/5", f"Training: {progress}/5"),
            rect.x + 17,
            rect.bottom - 82,
            V91_UI_GOLD,
            mini_font,
        )

        yazi_yaz(
            bt(f"Kullanım: {row_data['shortcut']}", f"Use: {row_data['shortcut']}"),
            rect.x + 17,
            rect.bottom - 51,
            V91_UI_RED_HOT,
            mini_font,
        )
        if progress < 5:
            merchant_fiyat_ciz(
                pygame.Rect(rect.right - 122, rect.bottom - 65, 104, 28),
                row_data["price"],
                True,
                V91_UI_GOLD,
            )
    else:
        tier = int(v92_blacksmith_upgrades.get(row_data["id"], 0))
        yazi_yaz(
            bt(f"Kademe: {tier}", f"Tier: {tier}"),
            rect.x + 17,
            rect.bottom - 82,
            V91_UI_GREY,
            mini_font,
        )
        merchant_fiyat_ciz(
            pygame.Rect(rect.x + 17, rect.bottom - 65, 118, 30),
            row_data["price"],
            False,
            V91_UI_GOLD,
        )
# </POTBO_STAGE S2461>

# <POTBO_STAGE S2473>








@dataclass
class V100NegotiationState:
    active: bool = False
    vendor: str = ""
    phase: str = "player"
    round_index: int = 0
    max_rounds: int = 4
    selected: int = 0
    choices: list = field(default_factory=list)
    npc_line: str = ""
    score: float = 0.0
    trust: float = 0.0
    patience: int = 5
    seed: int = 0
    base_total: int = 0
    cheat_pending: bool = False
    cheat_uncaught: int = 0
    finished: bool = False

    def reset(self):
        self.active = False
        self.vendor = ""
        self.phase = "player"
        self.round_index = 0
        self.max_rounds = 4
        self.selected = 0
        self.choices = []
        self.npc_line = ""
        self.score = 0.0
        self.trust = 0.0
        self.patience = 5
        self.seed = 0
        self.base_total = 0
        self.cheat_pending = False
        self.cheat_uncaught = 0
        self.finished = False
# </POTBO_STAGE S2473>

# <POTBO_STAGE S2475>


def v100_negotiation_choices(vendor, round_index):
    state = v100_negotiation
    pool = list(V100_HANUS_LINES if vendor == "hanus" else V100_REINALD_LINES)
    rng = random.Random(state.seed ^ (round_index * 7919) ^ (state.cheat_uncaught * 331))
    rng.shuffle(pool)
    choices = pool[:3]
    if vendor == "hanus" and state.cheat_pending:
        catch = {
            "tr": "Hayır, az önce başka bir rakam söyledin. Sayıyı değiştirme, Hanus.",
            "en": "No. You quoted a different number a moment ago. Do not change it, Hanus.",
            "lev": 1.45,
            "risk": 0.08,
            "tone": "catch",
            "catch": True,
        }


        detect = min(0.92, 0.42 + v96_ikna_ustaligi() * 0.055)
        if rng.random() < detect:
            choices[-1] = catch
    return choices


def v100_negotiation_begin(vendor):
    state = v100_negotiation
    state.reset()
    state.active = True
    state.vendor = str(vendor)
    state.phase = "player"
    state.round_index = 0
    state.max_rounds = 4
    state.selected = 0
    state.patience = 4 if vendor == "hanus" else 5
    state.seed = pygame.time.get_ticks() ^ (oyuncu_level * 1237) ^ (oyuncu_altin * 17)
    if vendor == "hanus":
        txn = merchant_bekleyen_islem or {}
        state.base_total = max(1, int(txn.get("price", txn.get("unit_price", 1))))
        state.npc_line = bt(
            "Peki. Rakamı konuşalım; ama lafı dolandırırsan fiyat değil sabrım düşer.",
            "Fine. We can discuss the number; waste my time and my patience drops before the price does.",
        )
    else:
        state.base_total = max(1, int(blacksmith_fiyat or 1))
        state.npc_line = bt(
            "Fiyatı konuşuruz. Masrafı gerçekten azaltan bir gerekçen varsa dinlerim.",
            "We can discuss the price. If you have a reason that truly lowers the cost, I will hear it.",
        )
    state.choices = v100_negotiation_choices(vendor, 0)


def v100_negotiation_success_chance(choice):
    state = v100_negotiation
    mastery = float(v96_ikna_ustaligi())
    leverage = float(choice.get("lev", 1.0))
    risk = float(choice.get("risk", 0.2))
    base = 0.38 + mastery * 0.035 + (leverage - 1.0) * 0.32 - risk * 0.22
    base += state.trust * 0.035
    if state.vendor == "hanus":
        base -= 0.035
    else:
        base += 0.035
    return max(0.12, min(0.88, base))


def v100_negotiation_npc_reply(choice, success, caught=False):
    vendor = v100_negotiation.vendor
    tone = str(choice.get("tone", "reason"))
    if vendor == "hanus":
        if caught:
            return bt(
                "İyi. Gözün rakamda kalmış. Bu kez kâğıdı değiştirmiyorum; devam et.",
                "Good. You kept your eye on the number. I will not alter the paper this time; continue.",
            )
        if success:
            replies = (
                bt("Bu cümle para eder. Biraz aşağı inebilirim.", "That line is worth coin. I can come down a little."),
                bt("Peki, orada hakkın var. Rakamı biraz oynatırım.", "Fine, you have a point there. I will move the number a little."),
                bt("Tamam. O gerekçe masaya konur; ama daha bitmedi.", "All right. That argument belongs on the table, but we are not done."),
            )
        else:
            replies = (
                bt("Hayır. O cümle benim cebimden para çıkarmıyor.", "No. That line does not take coin out of my pocket."),
                bt("Güzel deneme. Fiyat hâlâ aynı tarafta duruyor.", "Nice try. The price is still standing where it was."),
                bt("Beni ikna etmedin. Başka bir şey söyle.", "You did not convince me. Say something else."),
            )
    else:
        if success:
            replies = (
                bt("Mantıklı. O kalemi hesaptan biraz düşebilirim.", "Reasonable. I can trim that part of the estimate."),
                bt("Haklısın. O şart işçilik hesabını değiştirir.", "You are right. That condition changes the labor estimate."),
                bt("Bunu kabul ederim. Rakamı yeniden hesaplarım.", "I can accept that. I will recalculate the number."),
            )
        else:
            replies = (
                bt("Hayır. O şart işi ucuzlatmıyor; yalnız riski artırıyor.", "No. That condition does not make the job cheaper; it only adds risk."),
                bt("O gerekçeyle fiyatı düşürürsem işten çalmam gerekir. Yapmam.", "If I lower the price for that reason, I would have to cut corners. I will not."),
                bt("Bana masrafı azaltan bir sebep söyle; pazarlık ancak öyle yürür.", "Give me a reason that reduces the cost; that is how bargaining moves."),
            )
    rng = random.Random(v100_negotiation.seed ^ (v100_negotiation.round_index * 6151) ^ len(tone))
    return rng.choice(replies)


def v100_negotiation_choose():
    global v96_ikna_xp, v92_merchant_reputation
    state = v100_negotiation
    if not state.active or state.phase != "player" or not state.choices:
        return False
    choice = state.choices[state.selected % len(state.choices)]
    rng = random.Random(state.seed ^ (state.round_index * 104729) ^ int(float(choice.get("lev", 1.0)) * 1000))
    caught = bool(choice.get("catch", False) and state.cheat_pending)
    if caught:
        success = True
        state.cheat_pending = False
        state.cheat_uncaught = max(0, state.cheat_uncaught - 1)
        state.score += 1.25
        state.trust += 0.22
    else:
        chance = v100_negotiation_success_chance(choice)
        success = rng.random() < chance
        leverage = float(choice.get("lev", 1.0))
        risk = float(choice.get("risk", 0.2))
        state.score += leverage * (1.0 if success else -(0.58 + risk * 0.55))
        state.trust += 0.18 if success else -0.13
        state.patience -= 1 + (1 if (not success and risk >= 0.30) else 0)
        if success:
            v96_ikna_xp += 1
            if state.vendor == "hanus":
                v92_merchant_reputation = min(3.0, float(v92_merchant_reputation) + 0.05)
        elif state.vendor == "hanus":
            v92_merchant_reputation = max(-3.0, float(v92_merchant_reputation) - 0.05)



    if state.vendor == "hanus" and not caught and state.round_index < state.max_rounds - 1:
        cheat_chance = min(0.46, 0.19 + max(0.0, -state.trust) * 0.04)
        if rng.random() < cheat_chance:
            state.cheat_pending = True
            state.cheat_uncaught += 1
            state.score -= 0.24
            state.npc_line = bt(
                "Bir dakika. Az önce söylediğim rakam buydu zaten. Kâğıtta da öyle yazıyor.",
                "Hold on. That was the number I quoted already. It is right there on the paper.",
            )
        else:
            state.npc_line = v100_negotiation_npc_reply(choice, success, False)
    else:
        state.npc_line = v100_negotiation_npc_reply(choice, success, caught)

    state.phase = "npc"
    return True


def v100_negotiation_finalize():
    state = v100_negotiation
    if not state.active:
        return
    score = float(state.score) + float(state.trust) * 0.22
    if state.vendor == "hanus":
        txn = merchant_bekleyen_islem or {}
        quantity = max(1, int(txn.get("quantity", 1)))
        base_unit = max(1, int(txn.get("unit_price", max(1, state.base_total // quantity))))
        if str(txn.get("type", "buy")) == "sell":
            premium = max(-0.12, min(0.34, score * 0.040 - state.cheat_uncaught * 0.045))
            final_unit = max(1, int(round(base_unit * (1.0 + premium))))
        else:
            discount = max(-0.08, min(0.28, score * 0.036 - state.cheat_uncaught * 0.050))
            final_unit = max(1, int(round(base_unit * (1.0 - discount))))
        txn["unit_price"] = final_unit
        txn["price"] = final_unit * quantity
        txn["haggle_score"] = round(score, 3)
        globals()["merchant_modal"] = "confirm"
        merchant_diyalog_yaz(
            bt(
                f"Son rakam {txn['price']} coin. Şimdi anlaşırız ya da mal burada kalır.",
                f"Final number: {txn['price']} coins. Now we make the deal or the goods stay here.",
            )
        )
    else:
        base = max(1, int(state.base_total))
        discount = max(-0.05, min(0.24, score * 0.034))
        globals()["blacksmith_fiyat"] = max(1, int(round(base * (1.0 - discount))))
        globals()["blacksmith_modal"] = "confirm"
        globals()["blacksmith_mesaji"] = bt(
            f"Hesabı kapattım: {blacksmith_fiyat} coin. Bu rakamla işi temiz yaparım.",
            f"I have closed the estimate: {blacksmith_fiyat} coins. At that number I can do the work properly.",
        )
    state.finished = True
    state.active = False


def v100_negotiation_advance():
    state = v100_negotiation
    if not state.active:
        return False
    if state.phase == "player":
        return v100_negotiation_choose()


    if state.phase == "npc":
        if state.round_index + 1 >= state.max_rounds or state.patience <= 0:
            v100_negotiation_finalize()
            return True
        state.round_index += 1
        state.phase = "player"
        state.selected = 0
        state.choices = v100_negotiation_choices(state.vendor, state.round_index)
        return True
    return False


_v100_merchant_haggle_begin_base = v92_merchant_haggle_begin
_v100_blacksmith_haggle_begin_base = v92_blacksmith_haggle_begin


def v92_merchant_haggle_begin():
    result = _v100_merchant_haggle_begin_base()
    if result is False:
        return False
    v100_negotiation_begin("hanus")
    return True


def v92_blacksmith_haggle_begin(kind):
    _v100_blacksmith_haggle_begin_base(kind)
    v100_negotiation_begin("reinald")
    return True


def v100_negotiation_draw(box, vendor):
    state = v100_negotiation
    if not state.active or state.vendor != vendor:
        return False
    speaker = "HANUS" if vendor == "hanus" else "REINALD"
    yazi_yaz(speaker, box.x + 20, box.y + 25, V91_UI_RED_HOT, normal_font)
    yazi_yaz(
        bt(
            f"PAZARLIK {state.round_index + 1}/{state.max_rounds}",
            f"HAGGLE {state.round_index + 1}/{state.max_rounds}",
        ),
        box.right - 20,
        box.y + 26,
        V91_UI_GOLD,
        mini_font,
        False,
    )

    if state.phase == "npc":
        lines = metni_satirlara_bol(state.npc_line, oyun_kucuk_font, box.width - 40)
        y = box.y + 60
        for line in lines[:4]:
            yazi_yaz(line, box.x + 20, y, ACIK_GRI, oyun_kucuk_font)
            y += 22
        return True



    context = metni_satirlara_bol(state.npc_line, mini_font, box.width - 40)
    if context:
        yazi_yaz(context[0], box.x + 20, box.y + 53, V91_UI_GREY, mini_font)
    y = box.y + 78
    for index, choice in enumerate(state.choices[:3]):
        selected = index == state.selected
        text = choice["tr" if dil == "TR" else "en"]
        prefix = "> " if selected else "  "

        font = mini_font
        if font.size(prefix + text)[0] > box.width - 42:
            text = text[: max(24, int(len(text) * (box.width - 42) / max(1, font.size(prefix + text)[0])) - 2)] + "…"
        yazi_yaz(prefix + text, box.x + 20, y, V91_UI_WHITE if selected else V91_UI_GREY, font)
        y += 22
    return True


_v100_merchant_dialogue_base = merchant_diyalog_kutusu_ciz
_v100_blacksmith_dialogue_base = _v95_blacksmith_dialogue


def merchant_diyalog_kutusu_ciz(panel):
    if merchant_modal == "haggle" and v100_negotiation.active and v100_negotiation.vendor == "hanus":
        box = _v97_dialogue_box(panel)
        merchant_panel_ciz(box, V91_UI_RED, 2)
        v100_negotiation_draw(box, "hanus")
        return
    return _v100_merchant_dialogue_base(panel)


def _v95_blacksmith_dialogue(panel):
    if blacksmith_modal == "haggle" and v100_negotiation.active and v100_negotiation.vendor == "reinald":
        box = _v97_dialogue_box(panel)
        merchant_panel_ciz(box, V91_UI_RED, 2)
        v100_negotiation_draw(box, "reinald")
        return
    return _v100_blacksmith_dialogue_base(panel)





blacksmith_acilis_zamani = 0
_v100_blacksmith_ac_base = blacksmith_ac


def blacksmith_ac():
    global blacksmith_acilis_zamani
    result = _v100_blacksmith_ac_base()
    blacksmith_acilis_zamani = pygame.time.get_ticks()
    return result
# </POTBO_STAGE S2475>

# <POTBO_STAGE S2477>


def aktif_buton_ses_turu():
    if oyun_durumu == BLACKSMITH:
        return "merchant2"
    return _v100_active_button_sound_base()
# </POTBO_STAGE S2477>

# <POTBO_STAGE S2479>


def secim_imzasi_al():
    if oyun_durumu == BLACKSMITH:
        if blacksmith_modal == "haggle" and v100_negotiation.active:
            return (
                "blacksmith_haggle",
                v100_negotiation.phase,
                v100_negotiation.round_index,
                v100_negotiation.selected,
            )
        if blacksmith_modal == "confirm":
            return ("blacksmith_confirm", str((blacksmith_pending or {}).get("kind", "")))
        if blacksmith_sayfa == "menu":
            return ("blacksmith_menu_button", int(blacksmith_menu_index))
        return ("blacksmith_list", str(blacksmith_sayfa), int(blacksmith_index))
    return _v100_selection_signature_base()


_v100_merchant_event_base = v92_merchant_handle_event
_v100_blacksmith_event_base = v92_blacksmith_handle_event


def v92_merchant_handle_event(olay):
    global merchant_modal
    if merchant_modal == "haggle" and v100_negotiation.active and v100_negotiation.vendor == "hanus":
        if olay.type != pygame.KEYDOWN:
            return
        if olay.key == pygame.K_ESCAPE:
            v100_negotiation.reset()
            merchant_modal = None
            return
        if v100_negotiation.phase == "player":
            if olay.key in ui_yukari_tuslari():
                v100_negotiation.selected = (v100_negotiation.selected - 1) % max(1, len(v100_negotiation.choices))
                return
            if olay.key in ui_asagi_tuslari():
                v100_negotiation.selected = (v100_negotiation.selected + 1) % max(1, len(v100_negotiation.choices))
                return
        if olay.key in (pygame.K_e, pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE):
            button_click_sesi_cal("merchant2")
            v100_negotiation_advance()
        return
    return _v100_merchant_event_base(olay)


def v92_blacksmith_handle_event(olay):
    global blacksmith_modal
    if olay.type == pygame.KEYDOWN:

        if pygame.time.get_ticks() - int(blacksmith_acilis_zamani) < MERCHANT_ACILIS_FADE_SURESI:
            return
        if blacksmith_modal == "haggle" and v100_negotiation.active and v100_negotiation.vendor == "reinald":
            if olay.key == pygame.K_ESCAPE:
                v100_negotiation.reset()
                blacksmith_modal = None
                return
            if v100_negotiation.phase == "player":
                if olay.key in ui_yukari_tuslari():
                    v100_negotiation.selected = (v100_negotiation.selected - 1) % max(1, len(v100_negotiation.choices))
                    return
                if olay.key in ui_asagi_tuslari():
                    v100_negotiation.selected = (v100_negotiation.selected + 1) % max(1, len(v100_negotiation.choices))
                    return
            if olay.key in (pygame.K_e, pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE):
                button_click_sesi_cal("merchant2")
                v100_negotiation_advance()
            return



        if blacksmith_modal is None:
            if blacksmith_sayfa == "menu" and olay.key in (pygame.K_e, pygame.K_RETURN, pygame.K_SPACE):
                button_click_sesi_cal("merchant2")
            elif blacksmith_sayfa == "upgrade" and olay.key in (pygame.K_e, pygame.K_f):
                button_click_sesi_cal("merchant2")
        elif blacksmith_modal == "haggle" and olay.key in (pygame.K_e, pygame.K_RETURN, pygame.K_SPACE):
            button_click_sesi_cal("merchant2")
    return _v100_blacksmith_event_base(olay)


def blacksmith_ekrani_ciz():
    oyun_ekrani_ciz()
    elapsed = max(0, pygame.time.get_ticks() - int(blacksmith_acilis_zamani))
    ratio = max(0.0, min(1.0, elapsed / max(1, MERCHANT_ACILIS_FADE_SURESI)))
    ratio = ratio * ratio * (3.0 - 2.0 * ratio)
    base = ekran.copy() if ratio < 1.0 else None

    koyu_kaplama(205)
    panel = _v97_vendor_shell(bt("DEMİRCİ", "BLACKSMITH"))
    if blacksmith_sayfa == "menu":
        _v97_reinald_main(panel)
    else:
        _v97_reinald_subpage(panel)
    _v95_blacksmith_dialogue(panel)

    if base is not None:
        base.set_alpha(int(round(255 * (1.0 - ratio))))
        ekran.blit(base, (0, 0))
# </POTBO_STAGE S2479>

# <POTBO_STAGE S2489>


def _v102_reinald_payload_icon_draw(row_data, rect, selected=True):
    """Yetenek ve geliştirme kartlarının tek ikon giriş noktası."""
    if blacksmith_sayfa == "skills":
        return v100_skill_icon_draw(
            row_data.get("id", ""),
            pygame.Rect(rect),
            255 if selected else 210,
        )
    return _v102_upgrade_icon_draw(
        row_data.get("id", ""),
        pygame.Rect(rect),
        255 if selected else 210,
    )






def _v97_reinald_row(rect, row_data, selected):
    """Hanus ile aynı satır grameri; sağ tarafta gerçek skill/upgrade ikonu."""
    rect = pygame.Rect(rect)
    base = (34, 8, 13) if selected else (10, 8, 11)
    edge = V91_UI_RED_HOT if selected else V91_UI_RED
    merchant_panel_ciz(rect, edge, 2 if selected else 1, base)

    progress = int(v92_training.get(row_data["id"], 0)) if blacksmith_sayfa == "skills" else 0
    learned = blacksmith_sayfa == "skills" and progress >= 5

    if learned:
        yazi_yaz(
            bt("ÖĞRENİLDİ", "LEARNED"),
            rect.x + 14,
            rect.centery,
            V91_UI_GOLD,
            mini_font,
        )
    else:
        merchant_fiyat_ciz(
            pygame.Rect(rect.x + 10, rect.y + 12, 86, rect.height - 24),
            int(row_data.get("price", 0)),
            False,
            V91_UI_GOLD,
        )

    name_x = rect.x + 112
    icon = pygame.Rect(rect.right - 48, rect.y + 6, 40, 40)

    name_max_w = max(40, icon.x - 12 - name_x)
    _v100_draw_row_name(row_data.get("name", ""), name_x, rect.y + 13, name_max_w)

    if blacksmith_sayfa == "skills" and not learned:
        progress_text = f"{progress}/5"
        progress_right = icon.x - 10
        progress_x = progress_right - mini_font.size(progress_text)[0]
        progress_y = rect.bottom - mini_font.get_height() - 6
        yazi_yaz(
            progress_text,
            progress_x,
            progress_y,
            V91_UI_GOLD if selected else V91_UI_WHITE,
            mini_font,
        )

    merchant_panel_ciz(icon, V91_UI_RED_HOT if selected else V91_UI_GREY, 1)
    _v102_reinald_payload_icon_draw(
        row_data,
        icon.inflate(-6, -6),
        selected,
    )


def _v97_reinald_info(rect, row_data):
    """Sağ bilgi kartında da satırla aynı gerçek ikon kullanılır."""
    rect = pygame.Rect(rect)
    merchant_panel_ciz(rect, KOYU_KIRMIZI, 1)

    yazi_yaz(
        row_data.get("name", ""),
        rect.x + 22,
        rect.y + 30,
        PARLAK_KIRMIZI,
        normal_font,
    )
    category = bt("YETENEK", "SKILL") if blacksmith_sayfa == "skills" else bt("GELİŞTİRME", "UPGRADE")
    yazi_yaz(category, rect.x + 22, rect.y + 60, GRI, mini_font)

    icon = pygame.Rect(rect.x + 22, rect.y + 92, 92, 92)
    merchant_panel_ciz(icon, V91_UI_RED_HOT, 2)
    _v102_reinald_payload_icon_draw(row_data, icon.inflate(-10, -10), True)

    desc_lines = metni_satirlara_bol(
        str(row_data.get("description", "")),
        oyun_kucuk_font,
        rect.width - 156,
    )
    for i, line in enumerate(desc_lines[:8]):
        yazi_yaz(
            line,
            icon.right + 18,
            rect.y + 98 + i * 21,
            ACIK_GRI,
            oyun_kucuk_font,
        )

    value = pygame.Rect(rect.x + 22, rect.bottom - 64, rect.width - 44, 44)
    merchant_panel_ciz(value, KOYU_KIRMIZI, 1, (17, 9, 12))

    if blacksmith_sayfa == "skills":
        progress = int(v92_training.get(row_data["id"], 0))
        left_text = bt(f"EĞİTİM {progress}/5", f"TRAINING {progress}/5")
        yazi_yaz(left_text, value.x + 14, value.centery, PARLAK_KIRMIZI, kucuk_font)
        if progress < 5:
            merchant_fiyat_ciz(
                pygame.Rect(value.right - 105, value.y + 8, 90, 28),
                int(row_data.get("price", 0)),
                True,
                BEYAZ,
            )
    else:
        tier = int(v92_blacksmith_upgrades.get(row_data["id"], 0))
        yazi_yaz(
            bt(f"KADEME {tier}", f"TIER {tier}"),
            value.x + 14,
            value.centery,
            PARLAK_KIRMIZI,
            kucuk_font,
        )
        merchant_fiyat_ciz(
            pygame.Rect(value.right - 105, value.y + 8, 90, 28),
            int(row_data.get("price", 0)),
            True,
            BEYAZ,
        )
# </POTBO_STAGE S2489>

# <POTBO_STAGE S2525>






_v106_blacksmith_cost_previous = v92_blacksmith_upgrade_cost
_v106_blacksmith_apply_previous = v92_blacksmith_upgrade_apply
_v106_blacksmith_haggle_previous = v92_blacksmith_haggle_begin
# </POTBO_STAGE S2525>

# <POTBO_STAGE S2527>

# Silah geliştirmesi mevcut tek-seferlik x2 dövümü korur; artık saldırı ritmini de hızlandırır.
V116_WEAPON_ATTACK_SPEED_BONUS = 0.12
V116_ARMOR_PRICE_MULTIPLIERS = {"light": 0.86, "balanced": 1.00, "heavy": 1.28}
V116_ARMOR_LABELS = {
    "light": ("HAFİFLET", "LIGHTEN"),
    "balanced": ("DENGELİ", "BALANCED"),
    "heavy": ("GÜÇLENDİR", "REINFORCE"),
}
blacksmith_armor_after_weight = "confirm"


def v116_weapon_attack_speed_multiplier():
    return 1.0 + (V116_WEAPON_ATTACK_SPEED_BONUS if int(v92_blacksmith_upgrades.get("weapon", 0)) >= 1 else 0.0)


def v116_weapon_preview():
    done = int(v92_blacksmith_upgrades.get("weapon", 0)) >= 1
    current_damage = max(1, int(round(float(oyuncu_hasari))))
    next_damage = current_damage if done else max(1, int(round(float(current_damage) * 2.0)))
    current_speed = int(round(v116_weapon_attack_speed_multiplier() * 100.0))
    next_speed = current_speed if done else int(round((1.0 + V116_WEAPON_ATTACK_SPEED_BONUS) * 100.0))
    return current_damage, next_damage, current_speed, next_speed, done


def v116_armor_speed_multiplier(profile):
    if str(profile) == "light":
        return 1.035
    if str(profile) == "heavy":
        return 0.955
    return 1.0


def v116_armor_effective_protection(base_rating, profile):
    protection = max(0.0, min(0.32, float(base_rating)))
    if str(profile) == "light":
        protection *= 0.88
    elif str(profile) == "heavy":
        protection = min(0.38, protection + 0.055)
    return protection


def v116_armor_projected_rating(profile):
    current = max(0.0, min(0.30, float(v92_armor_rating)))
    tier = int(v92_blacksmith_upgrades.get("armor", 0)) + 1
    profile = str(profile)
    if profile == "light":
        # Levha/perçin sökümü: daha hızlı, fakat koruma bilinçli biçimde düşer.
        return max(0.0, current - (0.012 + min(0.008, tier * 0.001)))
    if profile == "heavy":
        # Ek plaka ve daha sert bağlama: en güçlü koruma, en yüksek bedel ve hız cezası.
        return min(0.30, current + 0.050 + min(0.016, tier * 0.002))
    return min(0.30, current + 0.032 + min(0.012, tier * 0.0015))


def v116_active_armor_profile():
    if blacksmith_modal == "weight":
        return ("light", "balanced", "heavy")[int(blacksmith_weight_index) % 3]
    pending = blacksmith_pending if isinstance(blacksmith_pending, dict) else {}
    profile = str(pending.get("armor_profile", "balanced"))
    return profile if profile in V116_ARMOR_PRICE_MULTIPLIERS else "balanced"


def v116_armor_plan_cost(profile):
    # Önceki kademe bazlı maliyet korunur; profil yalnız işçilik/malzeme katsayısıdır.
    base = max(1, int(_v106_blacksmith_cost_previous("armor")))
    return max(1, int(round(base * V116_ARMOR_PRICE_MULTIPLIERS[str(profile)])))


def v116_armor_preview(profile=None):
    profile = str(profile or v116_active_armor_profile())
    if profile not in V116_ARMOR_PRICE_MULTIPLIERS:
        profile = "balanced"
    current_protection = v116_armor_effective_protection(v92_armor_rating, v92_armor_weight)
    projected_rating = v116_armor_projected_rating(profile)
    next_protection = v116_armor_effective_protection(projected_rating, profile)
    current_speed = int(round(v116_armor_speed_multiplier(v92_armor_weight) * 100.0))
    next_speed = int(round(v116_armor_speed_multiplier(profile) * 100.0))
    return current_protection, next_protection, current_speed, next_speed, projected_rating


def v116_endurance_preview():
    tier = int(v92_blacksmith_upgrades.get("endurance", 0)) + 1
    stamina_gain = 4.5 + min(3.0, tier * 0.35)
    current_hp = max(1, int(round(float(oyuncu_max_hp))))
    next_hp = current_hp + 2
    current_stamina = float(oyuncu_max_stamina)
    next_stamina = current_stamina + stamina_gain
    return current_hp, next_hp, current_stamina, next_stamina


_v106_blacksmith_cost_previous = v92_blacksmith_upgrade_cost
_v106_blacksmith_apply_previous = v92_blacksmith_upgrade_apply
_v106_blacksmith_haggle_previous = v92_blacksmith_haggle_begin


def v92_blacksmith_upgrade_cost(kind):
    kind = str(kind)
    if kind == "weapon":
        return v106_double_power_cost()
    if kind == "armor":
        profile = v116_active_armor_profile()
        return v116_armor_plan_cost(profile)
    return _v106_blacksmith_cost_previous(kind)


def v92_blacksmith_upgrade_apply(kind, price):
    global oyuncu_altin, oyuncu_guc, oyuncu_hasari, blacksmith_mesaji
    global v92_armor_rating, v92_armor_weight
    kind = str(kind)

    if kind == "weapon":
        if int(v92_blacksmith_upgrades.get("weapon", 0)) >= 1:
            blacksmith_mesaji = bt(
                "Silah dövümü zaten tamamlandı.",
                "The weapon forging is already complete.",
            )
            return False
        if int(oyuncu_altin) < int(price):
            no_coin_sesi_cal()
            return False
        oyuncu_altin -= int(price)
        oyuncu_guc = max(1, int(round(float(oyuncu_guc) * 2.0)))
        oyuncu_hasari = max(1, int(round(float(oyuncu_hasari) * 2.0)))
        v92_blacksmith_upgrades["weapon"] = 1
        merchant_islem_sesi_cal("buy")
        blacksmith_mesaji = bt(
            "Silah dövümü tamam. Vuruş gücü iki katına çıktı; saldırı ritmi de hızlandı.",
            "Weapon forging complete. Strike power doubled and the attack rhythm is faster.",
        )
        dunya_olayi_kaydet("blacksmith_weapon_upgrade", level=int(oyuncu_level), price=int(price))
        return True

    if kind == "armor":
        if int(oyuncu_altin) < int(price):
            no_coin_sesi_cal()
            return False
        pending = blacksmith_pending if isinstance(blacksmith_pending, dict) else {}
        profile = str(pending.get("armor_profile", v116_active_armor_profile()))
        if profile not in V116_ARMOR_PRICE_MULTIPLIERS:
            profile = "balanced"
        projected = v116_armor_projected_rating(profile)
        oyuncu_altin -= int(price)
        v92_blacksmith_upgrades["armor"] = int(v92_blacksmith_upgrades.get("armor", 0)) + 1
        v92_armor_rating = projected
        v92_armor_weight = profile
        merchant_islem_sesi_cal("buy")
        if profile == "light":
            blacksmith_mesaji = bt(
                "Zırh hafifletildi. Hız kazandın; hasar engelleme düştü.",
                "Armor lightened. You gained speed, but damage blocking decreased.",
            )
        elif profile == "heavy":
            blacksmith_mesaji = bt(
                "Zırh güçlendirildi. Daha çok hasar engeller; hareketin ağırlaştı.",
                "Armor reinforced. It blocks more damage, but movement is slower.",
            )
        else:
            blacksmith_mesaji = bt(
                "Zırh dengeli biçimde geliştirildi.",
                "Armor improved with a balanced profile.",
            )
        dunya_olayi_kaydet(
            "blacksmith_armor_upgrade",
            level=int(oyuncu_level),
            price=int(price),
            profile=profile,
            rating=round(float(v92_armor_rating), 5),
        )
        return True

    return _v106_blacksmith_apply_previous(kind, price)


def v92_blacksmith_haggle_begin(kind):
    global blacksmith_fiyat
    kind = str(kind)
    if kind == "weapon" and int(v92_blacksmith_upgrades.get("weapon", 0)) >= 1:
        globals()["blacksmith_mesaji"] = bt(
            "Silah dövümü zaten tamamlandı.",
            "The weapon forging is already complete.",
        )
        return False

    armor_profile = None
    if kind == "armor":
        pending = blacksmith_pending if isinstance(blacksmith_pending, dict) else {}
        armor_profile = str(pending.get("armor_profile", v116_active_armor_profile()))
        if armor_profile not in V116_ARMOR_PRICE_MULTIPLIERS:
            armor_profile = "balanced"

    result = _v106_blacksmith_haggle_previous(kind)
    if result is False:
        return False

    if kind == "armor":
        # v100 pazarlık katmanı pending'i yeniden kurduğu için profil kararını geri bağla.
        if isinstance(blacksmith_pending, dict):
            blacksmith_pending["armor_profile"] = armor_profile
        blacksmith_fiyat = v116_armor_plan_cost(armor_profile)
        if "v100_negotiation" in globals() and getattr(v100_negotiation, "active", False):
            v100_negotiation.base_total = int(blacksmith_fiyat)
    return True


_v106_blacksmith_rows_previous = _v95_blacksmith_rows


def _v95_blacksmith_rows():
    rows = [dict(row) for row in _v106_blacksmith_rows_previous()]
    if blacksmith_sayfa != "upgrade":
        return tuple(rows)
    for row in rows:
        kind = str(row.get("id", ""))
        if kind == "weapon":
            done = int(v92_blacksmith_upgrades.get("weapon", 0)) >= 1
            row["name"] = bt("SİLAH", "WEAPON")
            row["description"] = bt(
                "Reinald silahın kuvvet aktarımını yeniden döver: vuruş gücü ikiye katlanır ve saldırı ritmi hızlanır.",
                "Reinald reforges the weapon's power transfer: strike power doubles and attack rhythm becomes faster.",
            )
            row["price"] = 0 if done else v106_double_power_cost()
        elif kind == "armor":
            row["name"] = bt("ZIRH", "ARMOR")
            row["description"] = bt(
                "Zırhı hafifletebilir, dengeli geliştirebilir veya daha ağır biçimde güçlendirebilirsin. Koruma, hız ve fiyat birlikte değişir.",
                "Armor can be lightened, balanced, or heavily reinforced. Protection, speed, and price change together.",
            )
            row["price"] = v92_blacksmith_upgrade_cost("armor")
        elif kind == "endurance":
            row["name"] = bt("BEDEN", "BODY")
            row["description"] = bt(
                "Bedensel dayanımı geliştirir; azami can ve stamina birlikte yükselir.",
                "Improves physical endurance; maximum health and stamina rise together.",
            )
            row["price"] = v92_blacksmith_upgrade_cost("endurance")
    return tuple(rows)


def _v116_right_text(metin, right, y, renk=V91_UI_GOLD, font=mini_font):
    metin = str(metin)
    width = font.size(metin)[0]
    return yazi_yaz(metin, int(right) - int(width), y, renk, font)


_v116_reinald_info_previous = _v97_reinald_info


def _v97_reinald_info(rect, row_data):
    if blacksmith_sayfa != "upgrade":
        return _v116_reinald_info_previous(rect, row_data)

    rect = pygame.Rect(rect)
    merchant_panel_ciz(rect, KOYU_KIRMIZI, 1)
    yazi_yaz(row_data.get("name", ""), rect.x + 22, rect.y + 30, PARLAK_KIRMIZI, normal_font)
    yazi_yaz(bt("GELİŞTİRME", "UPGRADE"), rect.x + 22, rect.y + 60, GRI, mini_font)

    icon = pygame.Rect(rect.x + 22, rect.y + 88, 88, 88)
    merchant_panel_ciz(icon, V91_UI_RED_HOT, 2)
    _v102_reinald_payload_icon_draw(row_data, icon.inflate(-10, -10), True)

    desc_lines = metni_satirlara_bol(str(row_data.get("description", "")), oyun_kucuk_font, rect.width - 150)
    for i, line in enumerate(desc_lines[:5]):
        yazi_yaz(line, icon.right + 16, rect.y + 94 + i * 20, ACIK_GRI, oyun_kucuk_font)

    kind = str(row_data.get("id", ""))
    stats_y = max(icon.bottom + 18, rect.y + 202)
    if kind == "weapon":
        cur_dmg, next_dmg, cur_speed, next_speed, done = v116_weapon_preview()
        yazi_yaz(bt("VURUŞ GÜCÜ", "STRIKE POWER"), rect.x + 22, stats_y, V91_UI_GREY, mini_font)
        _v116_right_text(f"{cur_dmg}  >  {next_dmg}", rect.right - 22, stats_y)
        stats_y += 24
        yazi_yaz(bt("SALDIRI HIZI", "ATTACK SPEED"), rect.x + 22, stats_y, V91_UI_GREY, mini_font)
        _v116_right_text(f"%{cur_speed}  >  %{next_speed}", rect.right - 22, stats_y)
        if done:
            stats_y += 23
            yazi_yaz(bt("TAMAMLANDI", "COMPLETE"), rect.x + 22, stats_y, V91_UI_RED_HOT, mini_font)
    elif kind == "armor":
        profile = v116_active_armor_profile()
        cur_prot, next_prot, cur_speed, next_speed, _ = v116_armor_preview(profile)
        yazi_yaz(bt("HASAR ENGELLEME", "DAMAGE BLOCK"), rect.x + 22, stats_y, V91_UI_GREY, mini_font)
        _v116_right_text(f"%{cur_prot * 100.0:.1f}  >  %{next_prot * 100.0:.1f}", rect.right - 22, stats_y)
        stats_y += 24
        yazi_yaz(bt("HAREKET HIZI", "MOVE SPEED"), rect.x + 22, stats_y, V91_UI_GREY, mini_font)
        _v116_right_text(f"%{cur_speed}  >  %{next_speed}", rect.right - 22, stats_y)
        stats_y += 22
        label = V116_ARMOR_LABELS[profile][0 if dil == "TR" else 1]
        yazi_yaz(bt("PLAN", "PLAN") + f": {label}", rect.x + 22, stats_y, V91_UI_RED_HOT, mini_font)
    elif kind == "endurance":
        cur_hp, next_hp, cur_sta, next_sta = v116_endurance_preview()
        yazi_yaz(bt("CAN", "HEALTH"), rect.x + 22, stats_y, V91_UI_GREY, mini_font)
        _v116_right_text(f"{cur_hp}  >  {next_hp}", rect.right - 22, stats_y)
        stats_y += 24
        yazi_yaz("STAMINA", rect.x + 22, stats_y, V91_UI_GREY, mini_font)
        _v116_right_text(f"{cur_sta:.1f}  >  {next_sta:.1f}", rect.right - 22, stats_y)

    value = pygame.Rect(rect.x + 22, rect.bottom - 58, rect.width - 44, 38)
    merchant_panel_ciz(value, KOYU_KIRMIZI, 1, (17, 9, 12))
    tier = int(v92_blacksmith_upgrades.get(kind, 0))
    yazi_yaz(bt(f"KADEME {tier}", f"TIER {tier}"), value.x + 12, value.centery, PARLAK_KIRMIZI, mini_font)
    price = int(row_data.get("price", 0))
    if not (kind == "weapon" and int(v92_blacksmith_upgrades.get("weapon", 0)) >= 1):
        merchant_fiyat_ciz(pygame.Rect(value.right - 105, value.y + 5, 90, 28), price, True, BEYAZ)


_v116_blacksmith_dialogue_previous = _v95_blacksmith_dialogue


def _v95_blacksmith_dialogue(panel):
    if blacksmith_modal != "weight":
        return _v116_blacksmith_dialogue_previous(panel)

    box = _v97_dialogue_box(panel)
    merchant_panel_ciz(box, V91_UI_RED, 2)
    yazi_yaz(V97_REINALD_NAME, box.x + 20, box.y + 24, V91_UI_RED_HOT, normal_font)
    yazi_yaz(bt("Zırhı nasıl döveyim?", "How should I forge the armor?"), box.x + 20, box.y + 51, V91_UI_WHITE, mini_font)

    profiles = ("light", "balanced", "heavy")
    choice_texts = []
    for i, profile in enumerate(profiles):
        label = V116_ARMOR_LABELS[profile][0 if dil == "TR" else 1]
        choice_texts.append((">" if i == int(blacksmith_weight_index) else " ") + label)
    yazi_yaz("   ".join(choice_texts), box.x + 20, box.y + 76, V91_UI_GOLD, mini_font)

    profile = profiles[int(blacksmith_weight_index) % 3]
    cur_prot, next_prot, cur_speed, next_speed, _ = v116_armor_preview(profile)
    yazi_yaz(
        bt("Hasar engelleme", "Damage block") + f": %{cur_prot * 100.0:.1f} > %{next_prot * 100.0:.1f}",
        box.x + 20,
        box.y + 103,
        ACIK_GRI,
        mini_font,
    )
    yazi_yaz(
        bt("Hız", "Speed") + f": %{cur_speed} > %{next_speed}",
        box.x + 20,
        box.y + 126,
        ACIK_GRI,
        mini_font,
    )
    merchant_fiyat_ciz(
        pygame.Rect(box.right - 205, box.y + 93, 175, 36),
        v116_armor_plan_cost(profile),
        True,
        V91_UI_GOLD,
    )


_v106_blacksmith_event_previous = v92_blacksmith_handle_event


def v92_blacksmith_handle_event(olay):
    global blacksmith_mesaji, blacksmith_modal, blacksmith_pending, blacksmith_fiyat
    global blacksmith_weight_index, blacksmith_armor_after_weight, v92_armor_weight

    if olay.type != pygame.KEYDOWN:
        return _v106_blacksmith_event_previous(olay)

    # Silah tek seferlik dövüm olarak kalır.
    if (
        blacksmith_modal is None
        and blacksmith_sayfa == "upgrade"
        and int(blacksmith_index) == 0
        and int(v92_blacksmith_upgrades.get("weapon", 0)) >= 1
        and olay.key in (pygame.K_e, pygame.K_f, pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE)
    ):
        blacksmith_mesaji = bt("Silah dövümü zaten tamamlandı.", "The weapon forging is already complete.")
        return

    # Zırhta önce fiziksel plan seçilir; E normal teklif, F pazarlık akışıdır.
    if blacksmith_modal is None and blacksmith_sayfa == "upgrade" and int(blacksmith_index) == 1:
        if olay.key in (pygame.K_e, pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE, pygame.K_f):
            blacksmith_pending = {"type": "upgrade", "kind": "armor"}
            blacksmith_weight_index = ("light", "balanced", "heavy").index(v92_armor_weight)
            blacksmith_armor_after_weight = "haggle" if olay.key == pygame.K_f else "confirm"
            blacksmith_modal = "weight"
            blacksmith_mesaji = bt(
                "Hafifletirsem koruma düşer; güçlendirirsem koruma ve fiyat artar ama hız düşer.",
                "Lightening reduces protection; reinforcement raises protection and price but slows you down.",
            )
            return

    if blacksmith_modal == "weight":
        if olay.key == pygame.K_ESCAPE:
            blacksmith_modal = None
            blacksmith_pending = None
            return
        if olay.key in ui_sol_tuslari() + ui_yukari_tuslari():
            blacksmith_weight_index = (int(blacksmith_weight_index) - 1) % 3
            return
        if olay.key in ui_sag_tuslari() + ui_asagi_tuslari():
            blacksmith_weight_index = (int(blacksmith_weight_index) + 1) % 3
            return
        if olay.key in (pygame.K_e, pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE):
            profile = ("light", "balanced", "heavy")[int(blacksmith_weight_index) % 3]
            if not isinstance(blacksmith_pending, dict):
                blacksmith_pending = {"type": "upgrade", "kind": "armor"}
            blacksmith_pending["armor_profile"] = profile
            blacksmith_fiyat = v116_armor_plan_cost(profile)
            if blacksmith_armor_after_weight == "haggle":
                v92_blacksmith_haggle_begin("armor")
            else:
                blacksmith_modal = "confirm"
                blacksmith_mesaji = bt(
                    f"{V116_ARMOR_LABELS[profile][0]} işi {blacksmith_fiyat} coin. F ile pazarlık, E ile kabul.",
                    f"{V116_ARMOR_LABELS[profile][1]} work is {blacksmith_fiyat} coins. F haggles; E accepts.",
                )
            return

    # Önce seçilmiş zırh planı varsa confirm ekranı tekrar weight menüsüne dönmez.
    if blacksmith_modal == "confirm" and isinstance(blacksmith_pending, dict) and blacksmith_pending.get("kind") == "armor":
        if olay.key == pygame.K_ESCAPE:
            blacksmith_modal = None
            blacksmith_pending = None
            return
        if olay.key == pygame.K_f:
            v92_blacksmith_haggle_begin("armor")
            return
        if olay.key in (pygame.K_e, pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE):
            if v92_blacksmith_upgrade_apply("armor", blacksmith_fiyat):
                blacksmith_modal = None
                blacksmith_pending = None
            return

    return _v106_blacksmith_event_previous(olay)
# </POTBO_STAGE S2527>

