# Path of the Bloodied One — categorized source stages
#
# This file is intentionally executed by core/bootstrap.py in original source order.
# Keeping one shared runtime namespace avoids gameplay regressions while the former
# 90k-line monolith is physically separated by responsibility. Do not import this
# file directly; edit the stage code normally and launch root main.py.

# <POTBO_STAGE S0005>

# =========================================================
# TEMEL AYARLAR
# =========================================================

GENISLIK = 1280
# </POTBO_STAGE S0005>

# <POTBO_STAGE S0008>

# UI çizgileri ve ölçeklemelerinde hafif piksel estetiği.
PIKSEL_UI = True
# </POTBO_STAGE S0008>

# <POTBO_STAGE S0019>

ERKEK_LOADING_YOLU = os.path.join(ASSETS, "backgrounds", "loading_male.png")
# </POTBO_STAGE S0019>

# <POTBO_STAGE S0039>

# Ölüm ekranındaki game-over başlığı için özel font. Dosya yoksa
# oyun güvenli biçimde sistem fontuna düşer; font dosyası paketle paylaşılmaz.
GAMEOVER_FONT_YOLU = os.path.join(ASSETS, "fonts", "gameoverfont.ttf")
# </POTBO_STAGE S0039>

# <POTBO_STAGE S0055>

LOADING_BAR_YOLU = os.path.join(ASSETS, "ui", "loading_bar.png")
# </POTBO_STAGE S0055>

# <POTBO_STAGE S0072>

menu_baslik_font = pygame.font.SysFont("georgia", 38, bold=True)

menu_font = pygame.font.SysFont("consolas", 27, bold=True)
# </POTBO_STAGE S0072>

# <POTBO_STAGE S0074>

if os.path.exists(GAMEOVER_FONT_YOLU):
    gameover_font = pygame.font.Font(GAMEOVER_FONT_YOLU, 82)
    gameover_secim_font = pygame.font.Font(GAMEOVER_FONT_YOLU, 31)
else:
    gameover_font = pygame.font.SysFont("georgia", 82, bold=True)
    gameover_secim_font = pygame.font.SysFont("consolas", 28, bold=True)
# </POTBO_STAGE S0074>

# <POTBO_STAGE S0082>


# =========================================================
# OYUN DURUMLARI
# =========================================================
ANA_MENU = "ana_menu"
# </POTBO_STAGE S0082>

# <POTBO_STAGE S0084>
AYARLAR = "ayarlar"
# </POTBO_STAGE S0084>

# <POTBO_STAGE S0086>
CREDITS = "credits"
# </POTBO_STAGE S0086>

# <POTBO_STAGE S0090>
ANA_MENU_ONAY = "ana_menu_onay"
# </POTBO_STAGE S0090>

# <POTBO_STAGE S0092>
ENVANTER = "envanter"
# </POTBO_STAGE S0092>

# <POTBO_STAGE S0096>
DIYALOG = "diyalog"
DIYALOG_SECIM = "diyalog_secim"

oyun_durumu = ANA_MENU
# </POTBO_STAGE S0096>

# <POTBO_STAGE S0098>
# =========================================================
# MENÜ / OYUN DEĞİŞKENLERİ
# =========================================================
menu_index = 0
# </POTBO_STAGE S0098>

# <POTBO_STAGE S0101>
# MAIN MENU onayı pause veya ölüm ekranından gelebilir; NO/ESC kaynağa döner.
ana_menu_onay_donus_durumu = DURAKLATMA

menu_mesaji = ""
# </POTBO_STAGE S0101>

# <POTBO_STAGE S0103>
ana_menu_onay_index = 1
ayarlar_donus_durumu = ANA_MENU
# </POTBO_STAGE S0103>

# <POTBO_STAGE S0107>
envanter_secili_slot = 0
envanter_imlec = 0
# </POTBO_STAGE S0107>

# <POTBO_STAGE S0109>
envanter_itemleri = [None] * 30
# 1-5 öne çıkanlardan bağımsız altıncı bağlamsal hızlı slot. Varsayılan tuş Q'dur.
# Slot item'in envanter indeksini izler; taşıma/satış/tüketim sırasında referans
# otomatik güncellenir veya temizlenir. Büyüler yalnızca bu slot üzerinden cast edilir.
q_hizli_item_index = None

envanter_aksiyon_acik = False
envanter_aksiyon_index = 0
envanter_aksiyon_item_index = None
# Aksiyon menüsünün 30'lu ana gridten mi yoksa öne çıkan slotlardan mı
# açıldığını belirtir. Böylece aynı pencere bağlama göre doğru eylemleri sunar.
envanter_aksiyon_kaynagi = "grid"
# Envanter içindeki eşyalar taşınıp başka slotlarla yer değiştirebilir.
envanter_tasima_kaynagi = None
# </POTBO_STAGE S0109>

# <POTBO_STAGE S0114>

cikis_donus_durumu = ANA_MENU
# </POTBO_STAGE S0114>

# <POTBO_STAGE S0118>

loading_baslangic = 0
# Önceki 13 saniyelik süre kısaltıldı.
loading_suresi = 4500

loading_ipucu = ""
loading_tamamlandi = False
# </POTBO_STAGE S0118>

# <POTBO_STAGE S0150>
oyuncu_olum_menu_index = 0
# </POTBO_STAGE S0150>

# <POTBO_STAGE S0154>
# lethal darbeyi yapan aktör ölüm tablosunda tek başına korunur. Diğer bütün
# karakterler görünmezken katil kırmızı silhouette olarak kalır; uid kaydı isim
# çakışmalarında dahi doğru aktörü bulmamızı sağlar.
oyuncu_olum_katil_uid = ""
# </POTBO_STAGE S0154>

# <POTBO_STAGE S0161>
OLU_MENU_GECIKME_MS = 4000
OLU_MENU_FADE_IN_MS = 760
# </POTBO_STAGE S0161>

# <POTBO_STAGE S0179>

diyalog_index = 0
aktif_diyalog = []
diyalog_secim_index = 0
# Bazı hikâye eşyaları diyalog akışını geçici olarak New Item sunumuna bırakır.
# Sunum kapandıktan sonra aynı diyalog düğümünden devam edilir.
diyalog_onemli_item_bekliyor = False
# </POTBO_STAGE S0179>

# <POTBO_STAGE S0183>
# Oyuncunun ilk diyalog seçimleri sonraki konuşmalarda hatırlanır.
eadric_tutumu = "neutral"
# </POTBO_STAGE S0183>

# <POTBO_STAGE S0187>
UI_BUTON_CLICK_SURE_MS = 140
# ENTER ve SPACE arayüz onayının sabit omurgasıdır. Oynanış tuşları
# AYARLAR > TUŞ ATAMALARI içinden değiştirilebilir. Etkileşim için atanan
# tuş, gerçek butonlarda ve envanterde bağlamsal onay tuşu olarak da çalışır.
ONAY_TUSLARI = (
    pygame.K_RETURN,
    pygame.K_KP_ENTER,
    pygame.K_SPACE,
)
# </POTBO_STAGE S0187>

# <POTBO_STAGE S0192>


def buton_onay_tuslari():
    return ONAY_TUSLARI + (tus_atamasi("interact"),)


def envanter_onay_tuslari():
    return ONAY_TUSLARI + (tus_atamasi("interact"),)
# </POTBO_STAGE S0192>

# <POTBO_STAGE S0194>


def ui_yon_tuslari(eylem, ok_tusu):
    """Menüler oynanış yön atamasını izler; boştaki yön oku erişilebilir fallback olur."""
    ana = tus_atamasi(eylem)
    sonuc = [ana]
    # Ok başka bir oynanış eylemine atanmışsa iki farklı işi aynı anda yapmasın.
    kullanan = next(
        (ad for ad, kod in tus_atamalari.items() if kod == ok_tusu),
        None,
    )
    if kullanan is None or kullanan == eylem:
        sonuc.append(ok_tusu)
    return tuple(dict.fromkeys(sonuc))


def ui_yukari_tuslari():
    return ui_yon_tuslari("move_up", pygame.K_UP)


def ui_asagi_tuslari():
    return ui_yon_tuslari("move_down", pygame.K_DOWN)


def ui_sol_tuslari():
    return ui_yon_tuslari("move_left", pygame.K_LEFT)


def ui_sag_tuslari():
    return ui_yon_tuslari("move_right", pygame.K_RIGHT)
# </POTBO_STAGE S0194>

# <POTBO_STAGE S0200>
# Harf harf diyalog sistemi.
DIYALOG_HARF_ARALIGI = 28
diyalog_yazi_baslangici = 0
diyalog_tamamlandi = False
# </POTBO_STAGE S0200>

# <POTBO_STAGE S0202>

DIYALOGLAR = {"TR": [], "EN": []}

DIYALOG_KONUSMACILARI = {"TR": [], "EN": []}
# </POTBO_STAGE S0202>

# <POTBO_STAGE S0205>


def eadric_adi():
    """Diyalog çizilirken çözülecek dinamik konuşmacı işareti."""
    return EADRIC_DINAMIK_KONUSMACI
# </POTBO_STAGE S0205>

# <POTBO_STAGE S0220>

erkek_loading_arka_plan = resim_yukle(ERKEK_LOADING_YOLU, (GENISLIK, YUKSEKLIK), False)
# </POTBO_STAGE S0220>

# <POTBO_STAGE S0278>

loading_bar_resmi_orijinal = resim_yukle(LOADING_BAR_YOLU)
# </POTBO_STAGE S0278>

# <POTBO_STAGE S0286>

# =========================================================
# LOADING BAR GÖRSELİNİ HAZIRLAMA
# =========================================================


def loading_bar_arka_planini_saydam_yap(kaynak):
    """
    PNG içinde gerçek şeffaflık yerine dama desenli açık gri/beyaz
    arka plan varsa bunu saydamlaştırır.
    """

    if kaynak is None:
        return None

    sonuc = kaynak.copy().convert_alpha()

    for y in range(sonuc.get_height()):
        for x in range(sonuc.get_width()):
            r, g, b, a = sonuc.get_at((x, y))

            acik_arka_plan = (
                r > 218 and g > 218 and b > 218 and max(r, g, b) - min(r, g, b) < 18
            )

            if acik_arka_plan:
                sonuc.set_at((x, y), (0, 0, 0, 0))

    return sonuc


def loading_bar_dolumunu_temizle(kaynak):
    """
    Görselin iç kanalındaki hazır kırmızı dolumu temizler.
    Kenarlardaki kırmızı süsler ve orta kristal korunur.
    Dinamik dolum daha sonra kodla çizilir.
    """

    if kaynak is None:
        return None

    sonuc = kaynak.copy().convert_alpha()

    genislik = sonuc.get_width()
    yukseklik = sonuc.get_height()

    merkez_x = genislik // 2
    merkez_y = yukseklik // 2

    kanal_sol = int(genislik * 0.10)
    kanal_sag = int(genislik * 0.90)
    kanal_ust = int(yukseklik * 0.44)
    kanal_alt = int(yukseklik * 0.56)

    kristal_yaricap = int(genislik * 0.045)

    for y in range(kanal_ust, kanal_alt):
        for x in range(kanal_sol, kanal_sag):
            if abs(x - merkez_x) < kristal_yaricap:
                continue

            r, g, b, a = sonuc.get_at((x, y))

            parlak_kirmizi = r > 110 and r > g * 1.6 and r > b * 1.25

            if parlak_kirmizi:
                sonuc.set_at((x, y), (5, 3, 6, a))

    return sonuc


def loading_bar_hazirla(kaynak):
    if kaynak is None:
        return None

    sonuc = loading_bar_arka_planini_saydam_yap(kaynak)
    sonuc = loading_bar_dolumunu_temizle(sonuc)

    return sonuc


loading_bar_resmi = loading_bar_hazirla(loading_bar_resmi_orijinal)
# </POTBO_STAGE S0286>

# <POTBO_STAGE S0303>


def genel_vinyet_ciz():
    """Sabit gotik vinyet; arka plan dünya gerilimi kenarlara çok hafifçe yansır."""
    yuzey = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    gerilim = 0.0
    try:
        gerilim = max(
            0.0,
            min(1.0, float(dunya_durumu.get("tension", 0.0))),
        )
    except (TypeError, ValueError, NameError):
        gerilim = 0.0

    katman = 52 + int(round(gerilim * 14))

    for i in range(katman):
        oran = 1.0 - i / max(1, katman)
        alpha = int((3.1 + gerilim * 1.8) * oran * oran)
        pygame.draw.rect(
            yuzey,
            (0, 0, 0, alpha),
            (i, i, GENISLIK - i * 2, YUKSEKLIK - i * 2),
            1,
        )

    # Tehdit yükseldiğinde yalnız kenarlarda, HUD okunurluğunu bozmayan
    # düşük alfa kan tonu oluşur. Nabız deterministik olarak zamana bağlıdır.
    if gerilim > 0.08:
        nabiz = 0.72 + 0.28 * (0.5 + 0.5 * math.sin(pygame.time.get_ticks() / 310.0))
        alfa = int(15 * gerilim * nabiz)
        kenar = 22
        pygame.draw.rect(yuzey, (110, 0, 18, alfa), (0, 0, GENISLIK, kenar))
        pygame.draw.rect(
            yuzey,
            (110, 0, 18, alfa),
            (0, YUKSEKLIK - kenar, GENISLIK, kenar),
        )
        pygame.draw.rect(yuzey, (110, 0, 18, alfa), (0, 0, kenar, YUKSEKLIK))
        pygame.draw.rect(
            yuzey,
            (110, 0, 18, alfa),
            (GENISLIK - kenar, 0, kenar, YUKSEKLIK),
        )

    ekran.blit(yuzey, (0, 0))


def loading_alt_vinyet_ciz():
    """Karakterlerin alt bölümünü siyaha eriten tam genişlikte gölge."""
    baslangic_y = 360
    yukseklik = YUKSEKLIK - baslangic_y
    yuzey = pygame.Surface((GENISLIK, yukseklik), pygame.SRCALPHA)

    for y in range(yukseklik):
        oran = y / max(1, yukseklik - 1)
        # Üstte görünmez, altta tamamen siyah. Yumuşak ama kararlı geçiş.
        alpha = int(255 * (oran**1.75))
        pygame.draw.line(yuzey, (0, 0, 0, alpha), (0, y), (GENISLIK, y))

    ekran.blit(yuzey, (0, baslangic_y))
# </POTBO_STAGE S0303>

# <POTBO_STAGE S0306>


ayarlari_yukle()
# </POTBO_STAGE S0306>

# <POTBO_STAGE S0322>


def menu_rect(index):
    return pygame.Rect(GENISLIK // 2 - 120, 356 + index * 47, 240, 34)


def buton_click_anim_rect(rect, secili=True):
    """Seçili UI plakasına 155 ms'lik press -> rebound mikro animasyonu uygular."""
    if not secili:
        return rect.copy()
    gecen = pygame.time.get_ticks() - ui_buton_click_baslangic
    if gecen < 0 or gecen >= UI_BUTON_CLICK_SURE_MS:
        return rect.copy()

    p = max(0.0, min(1.0, gecen / float(UI_BUTON_CLICK_SURE_MS)))
    if p < 0.36:
        q = p / 0.36
        scale = 1.0 - 0.085 * math.sin(q * math.pi * 0.5)
    else:
        q = (p - 0.36) / 0.64
        # Hafif overshoot; son karede tam 1.0'a yerleşir.
        scale = 0.915 + 0.085 * q + 0.030 * math.sin(q * math.pi)

    w = max(1, int(round(rect.width * scale)))
    h = max(1, int(round(rect.height * scale)))
    return pygame.Rect(0, 0, w, h).move(rect.centerx - w // 2, rect.centery - h // 2)


def menu_susleme_ciz(rect, secili):
    """
    Görseldeki gotik metal menü plakasını kodla oluşturur.
    Arka plan resminin içinde hazır menü yazısı bulunmaz.
    """

    # Gölge
    golge = rect.move(5, 6)

    pygame.draw.rect(ekran, (0, 0, 0), golge, border_radius=0)

    # Ana plaka
    # Seçili olmayan butonlar küçük ve sade kalır.
    # Seçili olan buton hafif büyütülür ve kalınlaştırılır.
    cizim_rect = rect.inflate(32, 14) if secili else rect
    cizim_rect = buton_click_anim_rect(cizim_rect, secili)

    # Seçilmeyenler yalnızca hafifçe arkada kalır.
    # Seçili buton belirgin biçimde büyür.
    taban_renk = (78, 6, 16) if secili else (8, 7, 9)

    pygame.draw.rect(ekran, taban_renk, cizim_rect, border_radius=0)

    # Seçili butonda iç kırmızı parıltı
    if secili:
        ic = cizim_rect.inflate(-10, -8)

        pygame.draw.rect(ekran, (105, 4, 13), ic, border_radius=0)

        pygame.draw.line(
            ekran,
            (210, 40, 55),
            (ic.left + 8, ic.top + 2),
            (ic.right - 8, ic.top + 2),
            2,
        )

        pygame.draw.line(
            ekran,
            (65, 0, 5),
            (ic.left + 8, ic.bottom - 2),
            (ic.right - 8, ic.bottom - 2),
            2,
        )

    # Dış metal kenarlıklar
    dis_renk = (245, 72, 92) if secili else (54, 47, 49)

    pygame.draw.rect(
        ekran,
        dis_renk,
        cizim_rect,
        5 if secili else 1,
        border_radius=0,
    )

    pygame.draw.line(
        ekran,
        (28, 22, 23),
        (cizim_rect.left + 14, cizim_rect.top + 5),
        (cizim_rect.right - 14, cizim_rect.top + 5),
        1,
    )

    pygame.draw.line(
        ekran,
        (28, 22, 23),
        (cizim_rect.left + 14, cizim_rect.bottom - 5),
        (cizim_rect.right - 14, cizim_rect.bottom - 5),
        1,
    )

    # Sol ve sağ sivri uzantılar
    sol_uc = [
        (cizim_rect.left - 22, cizim_rect.centery),
        (cizim_rect.left, cizim_rect.top + 7),
        (cizim_rect.left + 13, cizim_rect.centery),
        (cizim_rect.left, cizim_rect.bottom - 7),
    ]

    sag_uc = [
        (cizim_rect.right + 22, cizim_rect.centery),
        (cizim_rect.right, cizim_rect.top + 7),
        (cizim_rect.right - 13, cizim_rect.centery),
        (cizim_rect.right, cizim_rect.bottom - 7),
    ]

    pygame.draw.polygon(ekran, (24, 18, 20), sol_uc)

    pygame.draw.polygon(ekran, (24, 18, 20), sag_uc)

    pygame.draw.lines(ekran, dis_renk, True, sol_uc, 2)

    pygame.draw.lines(ekran, dis_renk, True, sag_uc, 2)


def ana_menu_ciz():
    global menu_index

    ekran.fill(SIYAH)

    # Düz siyah zemin üzerinde yalnızca başlık, menü ve hafif bir merkez
    # parlaması kullanılır; herhangi bir arka plan görseli çizilmez.
    merkez_parlama = pygame.Surface((520, YUKSEKLIK), pygame.SRCALPHA)
    for genislik, alfa in ((520, 22), (410, 18), (300, 14)):
        pygame.draw.ellipse(
            merkez_parlama,
            (95, 0, 18, alfa),
            ((520 - genislik) // 2, 40, genislik, 620),
        )

    ekran.blit(merkez_parlama, (GENISLIK // 2 - 260, 0))

    yazi_yaz(
        "PATH OF THE",
        GENISLIK // 2 + 4,
        92,
        (40, 0, 5),
        baslik_font,
        True,
    )
    yazi_yaz("PATH OF THE", GENISLIK // 2, 87, BEYAZ, baslik_font, True)
    yazi_yaz(
        "BLOODIED ONE",
        GENISLIK // 2 + 4,
        163,
        (40, 0, 5),
        baslik_font,
        True,
    )
    yazi_yaz(
        "BLOODIED ONE",
        GENISLIK // 2,
        158,
        PARLAK_KIRMIZI,
        baslik_font,
        True,
    )

    yazi_yaz(
        t("subtitle"),
        GENISLIK // 2,
        226,
        ACIK_GRI,
        kucuk_font,
        True,
    )

    for index, secenek in enumerate(menu_secenekleri()):
        rect = menu_rect(index)
        secili = index == menu_index

        menu_susleme_ciz(rect, secili)

        yazi_yaz(
            secenek,
            rect.centerx,
            rect.centery,
            BEYAZ if secili else (155, 145, 150),
            menu_font if secili else normal_font,
            True,
        )

    if menu_mesaji:
        yazi_yaz(
            menu_mesaji,
            GENISLIK // 2,
            688,
            PARLAK_KIRMIZI,
            kucuk_font,
            True,
        )
# </POTBO_STAGE S0322>

# <POTBO_STAGE S0326>


# =========================================================
# ÇIKIŞ ONAY EKRANI
# =========================================================


def cikis_onay_ciz():
    # QUIT ölüm ekranından geldiyse ana menüye ışınlanmayız. Aynı ARE YOU SURE?
    # paneli doğrudan siyah-kırmızı ölüm tablosunun üzerinde açılır. Ana menüden
    # gelen normal quit davranışı ise eski görünümünü korur.
    if cikis_donus_durumu == OYUN and oyuncu_hp <= 0:
        # Death QUIT: ölüm ekranı aynen arkada kalır.
        oyuncu_olum_sahnesi_ciz()
    elif cikis_donus_durumu == DURAKLATMA:
        # Pause QUIT: ana menüyü asla araya sokma; onay panelini mevcut pause
        # ekranının doğrudan üstüne bindir.
        duraklatma_menusu_ciz()
    else:
        ana_menu_ciz()

    panel = pygame.Rect(GENISLIK // 2 - 360, 245, 720, 265)

    panel_yuzeyi = pygame.Surface(panel.size, pygame.SRCALPHA)
    panel_yuzeyi.fill((5, 4, 8, 238))
    ekran.blit(panel_yuzeyi, panel.topleft)

    pygame.draw.rect(ekran, PARLAK_KIRMIZI, panel, 2, border_radius=0)

    yazi_yaz(
        t("exit_confirm"),
        panel.centerx,
        panel.y + 42,
        PARLAK_KIRMIZI,
        menu_baslik_font,
        True,
    )

    secenekler = [t("exit_yes"), t("exit_no")]

    for index, secenek in enumerate(secenekler):
        rect = pygame.Rect(
            panel.x + 42,
            panel.y + 92 + index * 72,
            panel.width - 84,
            50,
        )
        secili = index == cikis_index
        rect = buton_click_anim_rect(rect, secili)

        pygame.draw.rect(
            ekran,
            (58, 4, 15) if secili else (8, 7, 11),
            rect,
            border_radius=0,
        )
        pygame.draw.rect(
            ekran,
            PARLAK_KIRMIZI if secili else (82, 72, 80),
            rect,
            2 if secili else 1,
            border_radius=0,
        )
        yazi_yaz(
            secenek,
            rect.centerx,
            rect.centery,
            BEYAZ if secili else ACIK_GRI,
            mini_font,
            True,
        )
# </POTBO_STAGE S0326>

# <POTBO_STAGE S0333>


def karakter_onay_gecisini_guncelle():
    global karakter_onay_gecisi_aktif

    if not karakter_onay_gecisi_aktif:
        return

    if (
        pygame.time.get_ticks() - karakter_onay_gecisi_baslangic
        >= KARAKTER_ONAY_GECIS_SURESI
    ):
        karakter_onay_gecisi_aktif = False
        loading_baslat()
# </POTBO_STAGE S0333>

# <POTBO_STAGE S0342>


# =========================================================
# HUD / ENVANTER YARDIMCILARI
# =========================================================


def item_kisa_adi(index):
    return str(item_aciklamasi(index).get("name", ""))
# </POTBO_STAGE S0342>

# <POTBO_STAGE S0351>


def onemli_item_penceresini_ilerlet():
    global onemli_item_gosterim_aktif
    global onemli_item_gosterim_hazir_zamani
    global onemli_item_gorsel_hazir_zamani
    global diyalog_onemli_item_bekliyor
    global oyun_alt_durumu

    if not onemli_item_penceresi_acik_mi():
        return

    onemli_item_kuyrugu.pop(0)
    onemli_item_gosterim_aktif = False
    onemli_item_gosterim_hazir_zamani = 0
    onemli_item_gorsel_hazir_zamani = 0

    # Eadric'in Taşı gibi diyalog içi kazanımlarda sunum, konuşmanın gerçek bir
    # parçasıdır: kart kapanınca bir sonraki replik yeni baştan harf harf akar.
    if diyalog_onemli_item_bekliyor and not onemli_item_kuyrugu:
        diyalog_onemli_item_bekliyor = False
        oyun_alt_durumu = DIYALOG
        diyalog_yazisini_sifirla()
        diyalog_aksiyonlarini_isle()
# </POTBO_STAGE S0351>

# <POTBO_STAGE S0354>


def envantere_item_ekle(item, kazanimi_goster=True):
    """Aynı eşya kimliğini slot başına en fazla 10 adet olacak şekilde stackler."""
    if not isinstance(item, dict):
        return False
    yeni = dict(item)
    yeni_id = yeni.get("id")
    try:
        kalan = max(1, int(yeni.get("quantity", 1)))
    except (TypeError, ValueError):
        kalan = 1

    # Önce mevcut stackleri 10'a tamamla.
    for mevcut in envanter_itemleri:
        if kalan <= 0:
            break
        if isinstance(mevcut, dict) and mevcut.get("id") == yeni_id:
            adet = item_adedi(mevcut)
            eklenebilir = min(10 - adet, kalan)
            if eklenebilir > 0:
                mevcut["quantity"] = adet + eklenebilir
                kalan -= eklenebilir

    # Kalan miktarı yeni slotlara dağıt.
    for index in range(30):
        if kalan <= 0:
            break
        if envanter_itemleri[index] is None:
            kopya = dict(yeni)
            kopya["quantity"] = min(10, kalan)
            envanter_itemleri[index] = kopya
            kalan -= kopya["quantity"]

    basarili = kalan == 0
    if basarili:
        dunya_olayi_kaydet(
            "item_acquired",
            item_id=str(yeni_id or ""),
            count=max(1, int(yeni.get("quantity", 1))),
        )
        if kazanimi_goster:
            # Kart hemen açılmaz; temiz oyun sahnesi görünür olduğunda sunulur.
            onemli_item_kazanimi_ekle(yeni)
    return basarili
# </POTBO_STAGE S0354>

# <POTBO_STAGE S0357>


def envantere_test_itemi_ekle():
    if envantere_item_ekle(can_iksiri_olustur(), kazanimi_goster=False):
        item_alindi_bildirimi(bt("Can İksiri", "Health Potion"), 1)
    else:
        bildirim_goster(bt("Envanter dolu.", "Inventory is full."))
# </POTBO_STAGE S0357>

# <POTBO_STAGE S0363>


def q_hizli_slot_normalize_et():
    global q_hizli_item_index
    if not isinstance(q_hizli_item_index, int):
        q_hizli_item_index = None
        return
    if not 0 <= q_hizli_item_index < len(envanter_itemleri):
        q_hizli_item_index = None
        return
    item = envanter_itemleri[q_hizli_item_index]
    if not item_q_hizli_kullanima_uygun_mu(item):
        q_hizli_item_index = None


def itemi_q_hizli_slota_ata(item_index):
    global q_hizli_item_index
    if not isinstance(item_index, int) or not 0 <= item_index < len(envanter_itemleri):
        return False
    item = envanter_itemleri[item_index]
    if not item_q_hizli_kullanima_uygun_mu(item):
        bildirim_goster(
            bt(
                "Bu eşya Q hızlı kullanımına atanamaz.",
                "This item cannot be bound to Q quick-use.",
            )
        )
        return False
    q_hizli_item_index = item_index
    bildirim_goster(
        bt(
            f"{item.get('name', 'Eşya')} Q hızlı slotuna atandı.",
            f"{item.get('name', 'Item')} bound to the Q quick slot.",
        )
    )
    dunya_olayi_kaydet("q_quick_bind", item_id=str(item.get("id", "")))
    return True
# </POTBO_STAGE S0363>

# <POTBO_STAGE S0366>


def secili_itemi_kullan(item_index):
    global oyuncu_hp
    global oyuncu_mana

    if not isinstance(item_index, int) or not 0 <= item_index < 30:
        return

    item = envanter_itemleri[item_index]

    if not isinstance(item, dict):
        return

    item_id = item.get("id")

    if item_buyu_mu(item):
        bildirim_goster(
            bt(
                "Büyüler yalnız Q hızlı slotundan kullanılabilir.",
                "Spells can only be cast from the Q quick slot.",
            )
        )
        return

    if item_id in ("health_potion", "aurum_potabile"):
        if oyuncu_hp >= oyuncu_max_hp:
            bildirim_goster(bt("Can zaten dolu.", "Health is already full."))
            return

        oyuncu_hp = min(oyuncu_max_hp, oyuncu_hp + int(item.get("heal", 30)))

        envanterden_bir_azalt(item_index)
        dunya_olayi_kaydet("item_used", item_id=str(item_id), count=1)

        # Can veren her içecek aynı kısa kırmızı-beyaz "içildi" geri bildirimini
        # kullanır; health_potion artık sessiz/görselsiz tüketilmez.
        oyuncu_parlama_baslat("potion")

        if item_id == "aurum_potabile":
            bildirim_goster(
                bt(
                    "Aurum Potabile kullanıldı.",
                    "Aurum Potabile used.",
                )
            )
        else:
            bildirim_goster(
                bt(
                    "Can iksiri kullanıldı.",
                    "Health potion used.",
                )
            )

    elif item_id == "quinta_essentia":
        if oyuncu_mana >= oyuncu_max_mana:
            bildirim_goster(bt("Mana zaten dolu.", "Mana is already full."))
            return

        oyuncu_mana = min(
            oyuncu_max_mana,
            oyuncu_mana + int(item.get("mana", 40)),
        )

        envanterden_bir_azalt(item_index)
        dunya_olayi_kaydet("item_used", item_id=str(item_id), count=1)
        oyuncu_parlama_baslat("potion")
        bildirim_goster(
            bt(
                "Quinta Essentia kullanıldı.",
                "Quinta Essentia used.",
            )
        )

    elif item_id == "eadric_stone":
        bildirim_goster(
            bt(
                "Taş sessiz. Şimdilik.",
                "The stone is silent. For now.",
            )
        )


def secili_itemi_at(item_index):
    if not isinstance(item_index, int) or not 0 <= item_index < 30:
        return

    item = envanter_itemleri[item_index]

    if not isinstance(item, dict):
        return

    if item.get("id") == "eadric_stone":
        bildirim_goster(
            bt(
                "Görev eşyaları atılamaz.",
                "Quest items cannot be dropped.",
            )
        )
        return
    if item_buyu_mu(item):
        bildirim_goster(
            bt(
                "Büyü atılamaz. İstersen Hanus'ye satabilirsin.",
                "A spell cannot be dropped. You may sell it to Hanus instead.",
            )
        )
        return

    envanterden_bir_azalt(item_index)
    dunya_olayi_kaydet("item_dropped", item_id=str(item.get("id", "")), count=1)

    bildirim_goster(bt("Eşya atıldı.", "Item dropped."))
# </POTBO_STAGE S0366>

# <POTBO_STAGE S0368>


def envanter_tasimayi_baslat(item_index):
    global envanter_tasima_kaynagi

    if not isinstance(item_index, int):
        return
    if not 0 <= item_index < len(envanter_itemleri):
        return
    if envanter_itemleri[item_index] is None:
        return

    envanter_tasima_kaynagi = item_index
# </POTBO_STAGE S0368>

# <POTBO_STAGE S0370>


def envanter_aksiyon_menusunu_ac(item_index, kaynak):
    global envanter_aksiyon_acik
    global envanter_aksiyon_index
    global envanter_aksiyon_item_index
    global envanter_aksiyon_kaynagi

    if not isinstance(item_index, int):
        return False
    if not 0 <= item_index < len(envanter_itemleri):
        return False
    if not isinstance(envanter_itemleri[item_index], dict):
        return False

    envanter_aksiyon_acik = True
    envanter_aksiyon_index = 0
    envanter_aksiyon_item_index = item_index
    envanter_aksiyon_kaynagi = "featured" if kaynak == "featured" else "grid"
    return True


def item_ikonu_ciz(item_id, rect, cerceve=True):
    """Envanter ve kazanım kartlarında aynı piksel ikon dilini kullanır."""
    if cerceve:
        pygame.draw.rect(ekran, (5, 4, 8), rect)
        pygame.draw.rect(ekran, (92, 76, 88), rect, 2)

    ikon = ITEM_RESIMLERI.get(item_id)
    if ikon is None:
        return False

    hedef = pygame.Rect(0, 0, max(1, rect.width - 18), max(1, rect.height - 18))
    cizilecek = resmi_oranli_sigdir(ikon, hedef, 0, 1.0, True)
    if cizilecek is None:
        return False

    ekran.blit(cizilecek, cizilecek.get_rect(center=rect.center))
    return True
# </POTBO_STAGE S0370>

# <POTBO_STAGE S0375>


def hud_sol_rect():
    return pygame.Rect(18, 14, 500, 168)


def hud_sag_rect():
    # Sağ panel sol panelle aynı yükseklikte kalır; ancak ekranın ortasında
    # anlamsız geniş bir boşluk bırakmaz. İki panel arasında yalnızca ince
    # bir görsel nefes payı vardır ve sağ panel sağ dış marja kadar uzanır.
    sol = hud_sol_rect()
    panel_araligi = 20
    x = sol.right + panel_araligi
    return pygame.Rect(x, sol.y, max(1, GENISLIK - 18 - x), sol.height)
# </POTBO_STAGE S0375>

# <POTBO_STAGE S0383>


def slot_ciz(
    rect,
    secili=False,
    numara=None,
    item_index=None,
    tasima_kaynagi=False,
):
    pygame.draw.rect(ekran, (8, 7, 11), rect, border_radius=0)

    cerceve_rengi = (
        SARI if tasima_kaynagi else PARLAK_KIRMIZI if secili else (86, 72, 82)
    )
    cerceve_kalinligi = 3 if (secili or tasima_kaynagi) else 1

    pygame.draw.rect(
        ekran,
        cerceve_rengi,
        rect,
        cerceve_kalinligi,
        border_radius=0,
    )

    if numara is not None:
        yazi_yaz(str(numara), rect.x + 8, rect.y + 6, SARI, mini_font)

    if item_index is not None and 0 <= item_index < 30:
        item = envanter_itemleri[item_index]

        if item is not None:
            ikon = ITEM_RESIMLERI.get(item.get("id"))

            if ikon is not None:
                ikon_alani = pygame.Rect(0, 0, rect.width - 14, rect.height - 14)
                cizilecek_ikon = resmi_oranli_sigdir(ikon, ikon_alani, 0, 1.0, True)
                if cizilecek_ikon is not None:
                    ekran.blit(
                        cizilecek_ikon,
                        cizilecek_ikon.get_rect(center=rect.center),
                    )
            else:
                ad = item_kisa_adi(item_index)
                yazi_yaz(
                    ad[:9],
                    rect.centerx,
                    rect.centery + 5,
                    BEYAZ,
                    mini_font,
                    True,
                )

            adet = item_adedi(item)
            if adet > 1:
                adet_kutu = pygame.Rect(rect.right - 29, rect.bottom - 25, 24, 20)
                pygame.draw.rect(ekran, (5, 4, 7), adet_kutu)
                pygame.draw.rect(ekran, KOYU_KIRMIZI, adet_kutu, 1)
                yazi_yaz(
                    f"x{adet}",
                    adet_kutu.centerx,
                    adet_kutu.centery,
                    BEYAZ,
                    mini_font,
                    True,
                )
# </POTBO_STAGE S0383>

# <POTBO_STAGE S0387>


def envanter_aksiyon_menusu_ciz(panel, item_index, kaynak="grid"):
    aksiyonlar = envanter_aksiyonlari(item_index, kaynak)
    if not aksiyonlar:
        return

    satir_h = 44
    menu_h = 100 + len(aksiyonlar) * satir_h
    menu_rect = pygame.Rect(
        panel.centerx - 250,
        panel.centery - menu_h // 2,
        500,
        menu_h,
    )

    pygame.draw.rect(ekran, (5, 4, 8), menu_rect)
    pygame.draw.rect(ekran, PARLAK_KIRMIZI, menu_rect, 3)

    item = item_aciklamasi(item_index)
    yazi_yaz(
        item["name"],
        menu_rect.centerx,
        menu_rect.y + 32,
        BEYAZ,
        normal_font,
        True,
    )

    if q_hizli_item_index == item_index:
        yazi_yaz(
            bt("Q'YA BAĞLI", "BOUND TO Q"),
            menu_rect.centerx,
            menu_rect.y + 57,
            (255, 142, 48),
            mini_font,
            True,
        )

    bas_y = menu_rect.y + 76
    for index, (_, etiket) in enumerate(aksiyonlar):
        rect = pygame.Rect(
            menu_rect.x + 42,
            bas_y + index * satir_h,
            menu_rect.width - 84,
            36,
        )
        secili = index == (envanter_aksiyon_index % len(aksiyonlar))
        pygame.draw.rect(ekran, (65, 4, 14) if secili else (13, 11, 15), rect)
        pygame.draw.rect(
            ekran,
            PARLAK_KIRMIZI if secili else GRI,
            rect,
            2 if secili else 1,
        )
        yazi_yaz(
            etiket,
            rect.centerx,
            rect.centery,
            BEYAZ if secili else ACIK_GRI,
            kucuk_font,
            True,
        )
# </POTBO_STAGE S0387>

# <POTBO_STAGE S0389>


def envanter_ciz():
    # Oyun dünyası yalnızca donmuş bir arka plan olarak çizilir. Envanter
    # açıkken oyun, HUD ve öne çıkan hızlı kullanım girdileri çalışmaz.
    oyun_ekrani_ciz()
    koyu_kaplama(220)

    panel = pygame.Rect(80, 52, 1120, 625)

    gotik_panel(panel, PARLAK_KIRMIZI, 245)

    yazi_yaz(
        ("ENVANTER" if dil == "TR" else "INVENTORY"),
        panel.centerx,
        panel.y + 34,
        PARLAK_KIRMIZI,
        menu_baslik_font,
        True,
    )

    # 30 slot: 6 sütun x 5 satır
    grid_x = panel.x + 42
    grid_y = panel.y + 82
    slot = 66
    gap = 10

    for index in range(30):
        row = index // 6
        col = index % 6

        rect = pygame.Rect(
            grid_x + col * (slot + gap),
            grid_y + row * (slot + gap),
            slot,
            slot,
        )

        slot_ciz(
            rect,
            secili=(index == envanter_imlec),
            item_index=index,
            tasima_kaynagi=(index == envanter_tasima_kaynagi),
        )

    # Sağ item bilgi bölümü
    bilgi_panel = pygame.Rect(panel.x + 550, panel.y + 82, 520, 470)

    # Öne çıkan 1-5 ve bağımsız Q büyü slotu tek satırda görünür. Altı kutu,
    # ana envanterin altı sütunuyla birebir hizalanır; böylece Q artık envanter
    # açıkken görünmez bir sistem değildir.
    grid_toplam_genislik = 6 * slot + 5 * gap
    one_cikan_slot_w = slot
    one_cikan_gap = gap
    one_cikan_h = 52
    one_cikan_y = bilgi_panel.bottom - one_cikan_h

    yazi_yaz(
        bt("ÖNE ÇIKAN SLOTLAR + Q", "FEATURED SLOTS + Q"),
        grid_x,
        one_cikan_y - 23,
        PARLAK_KIRMIZI,
        kucuk_font,
    )

    for i in range(5):
        rect = pygame.Rect(
            grid_x + i * (one_cikan_slot_w + one_cikan_gap),
            one_cikan_y,
            one_cikan_slot_w,
            one_cikan_h,
        )

        slot_ciz(
            rect,
            secili=(i == envanter_secili_slot),
            numara=i + 1,
            item_index=one_cikan_slotlar[i],
            tasima_kaynagi=(i == one_cikan_tasima_kaynagi),
        )

    # Altıncı kutu Q slotudur. 1-5 seçiminin parçası değildir; büyü atama eylemi
    # yine mevcut "Q slotuna ata" menüsünden yapılır. Burada gerçek bağlı item,
    # sonsuzluk ve okul sembolü görünür.
    q_hizli_slot_normalize_et()
    q_rect = pygame.Rect(
        grid_x + 5 * (one_cikan_slot_w + one_cikan_gap),
        one_cikan_y,
        one_cikan_slot_w,
        one_cikan_h,
    )
    q_item = q_hizli_item_index
    q_debug_spell = bool(gelistirici_sonsuz_ates)
    q_is_magic = q_debug_spell or (
        isinstance(q_item, int)
        and 0 <= q_item < len(envanter_itemleri)
        and item_buyu_mu(envanter_itemleri[q_item])
    )
    pygame.draw.rect(ekran, (15, 8, 8) if q_is_magic else (9, 8, 12), q_rect)
    pygame.draw.rect(
        ekran,
        (210, 78, 28) if q_is_magic else (110, 83, 92),
        q_rect,
        2,
    )
    yazi_yaz(
        "Q",
        q_rect.x + 9,
        q_rect.y + 9,
        (255, 177, 70) if q_is_magic else SARI,
        mini_font,
        True,
    )

    if q_debug_spell:
        item_ikonu_ciz("fire_magic", q_rect.inflate(-16, -8), False)
        spell_okulu_sembol_ciz(
            "IGNIS",
            pygame.Rect(q_rect.right - 21, q_rect.bottom - 21, 17, 17),
        )
        yazi_yaz(
            "∞",
            q_rect.centerx,
            q_rect.y + 10,
            (255, 238, 178),
            mini_font,
            True,
        )
    elif isinstance(q_item, int) and 0 <= q_item < len(envanter_itemleri):
        q_veri = envanter_itemleri[q_item]
        if isinstance(q_veri, dict):
            item_ikonu_ciz(q_veri.get("id"), q_rect.inflate(-16, -8), False)
            if q_veri.get("spell_school"):
                spell_okulu_sembol_ciz(
                    q_veri.get("spell_school"),
                    pygame.Rect(
                        q_rect.right - 21,
                        q_rect.bottom - 21,
                        17,
                        17,
                    ),
                )
            if q_veri.get("infinite", False):
                yazi_yaz(
                    "∞",
                    q_rect.centerx,
                    q_rect.y + 10,
                    (255, 238, 178),
                    mini_font,
                    True,
                )

    # Envanterde de cooldown okunabilsin; Q kutusunu aşağıdan yukarı koyulaştırır.
    if q_is_magic and not q_debug_spell:
        kalan = max(
            0,
            FIRE_MAGIC_COOLDOWN_MS
            - (pygame.time.get_ticks() - fire_magic_son_kullanim),
        )
        if kalan > 0:
            oran = max(0.0, min(1.0, kalan / FIRE_MAGIC_COOLDOWN_MS))
            kap_h = int(round((q_rect.height - 4) * oran))
            kap = pygame.Surface((q_rect.width - 4, kap_h), pygame.SRCALPHA)
            kap.fill((0, 0, 0, 128))
            ekran.blit(kap, (q_rect.x + 2, q_rect.y + 2))

    pygame.draw.rect(ekran, (7, 6, 10), bilgi_panel, border_radius=0)

    pygame.draw.rect(ekran, (92, 76, 88), bilgi_panel, 2, border_radius=0)

    bilgi = item_aciklamasi(envanter_imlec)

    item_verisi = (
        envanter_itemleri[envanter_imlec]
        if 0 <= envanter_imlec < len(envanter_itemleri)
        else None
    )

    ikon_rect = pygame.Rect(bilgi_panel.right - 146, bilgi_panel.y + 22, 116, 116)

    if isinstance(item_verisi, dict):
        item_ikonu_ciz(item_verisi.get("id"), ikon_rect, True)

    yazi_yaz(
        bilgi["name"],
        bilgi_panel.x + 28,
        bilgi_panel.y + 30,
        BEYAZ,
        normal_font,
    )

    kategori = str(bilgi.get("category", bilgi.get("type", "")))
    okul = str(bilgi.get("spell_school", ""))
    if okul:
        kategori += "  ·  " + okul
    kategori_rect = yazi_yaz(
        kategori,
        bilgi_panel.x + 28,
        bilgi_panel.y + 70,
        SARI,
        kucuk_font,
    )
    if okul:
        spell_okulu_sembol_ciz(
            okul,
            pygame.Rect(
                kategori_rect.right + 8,
                kategori_rect.centery - 10,
                20,
                20,
            ),
        )

    pygame.draw.line(
        ekran,
        (72, 58, 68),
        (bilgi_panel.x + 28, bilgi_panel.y + 156),
        (bilgi_panel.right - 28, bilgi_panel.y + 156),
        1,
    )

    aciklama_satirlari = metni_satirlara_bol(
        bilgi["description"], mini_font, bilgi_panel.width - 56
    )

    y = bilgi_panel.y + 178

    for satir in aciklama_satirlari:
        yazi_yaz(satir, bilgi_panel.x + 28, y, ACIK_GRI, mini_font)

        y += 22

    if envanter_aksiyon_acik and envanter_aksiyon_item_index is not None:
        envanter_aksiyon_menusu_ciz(
            panel,
            envanter_aksiyon_item_index,
            envanter_aksiyon_kaynagi,
        )

    if one_cikan_atama_item_index is not None:
        one_cikan_atama_penceresi_ciz(panel)
# </POTBO_STAGE S0389>

# <POTBO_STAGE S0392>


def oyuncu_paneli_ciz():
    sol_panel = hud_sol_rect()
    gotik_panel(sol_panel, PARLAK_KIRMIZI, 230)

    ad_rect = yazi_yaz(
        secili_karakter_adi(),
        sol_panel.x + 24,
        sol_panel.y + 14,
        BEYAZ,
        oyun_font,
    )
    seviye_rect = yazi_yaz(
        f"{t('level')}: {oyuncu_level}",
        ad_rect.right + 16,
        sol_panel.y + 14,
        level_rengi(oyuncu_level),
        oyun_font,
    )

    coin_x = min(sol_panel.right - 78, seviye_rect.right + 20)
    if coin_sembol_resmi is not None:
        coin_ikon = hafif_piksellestir(coin_sembol_resmi, (22, 22), 2)
        ekran.blit(coin_ikon, (coin_x, sol_panel.y + 13))
        yazi_yaz(
            str(oyuncu_altin),
            coin_x + 29,
            sol_panel.y + 14,
            SARI,
            oyun_font,
        )

    bar_x = sol_panel.x + 24
    bar_w = sol_panel.width - 48
    hp_oran = hp_gorunen / max(1.0, float(oyuncu_max_hp))
    mana_oran = mana_gorunen / max(1.0, float(oyuncu_max_mana))
    stamina_oran = stamina_gorunen / max(1.0, oyuncu_max_stamina)
    tier = min(5, oyuncu_level // 10)

    # sıralaması değişmez: CAN -> STAMINA -> MANA. Üçlü blok header'dan
    # daha aşağı taşındı ve bıçak barları daha ince/keskin oranlara çekildi.
    gotik_bicak_bari_ciz(
        pygame.Rect(bar_x, sol_panel.y + 70, bar_w, 22),
        hp_oran,
        (126, 5, 25),
        (24, 3, 8),
        (224, 44, 58),
        "",
        False,
        True,
        tier,
    )

    sade_stamina_bari_ciz(
        pygame.Rect(bar_x + 8, sol_panel.y + 96, bar_w - 30, 6),
        stamina_oran,
        pygame.time.get_ticks() < stamina_uyari_bitis,
    )

    gotik_bicak_bari_ciz(
        pygame.Rect(bar_x, sol_panel.y + 110, bar_w, 20),
        mana_oran,
        (43, 121, 205),
        (3, 8, 19),
        (135, 207, 255),
        "",
        pygame.time.get_ticks() < mana_uyari_bitis,
        True,
        tier,
    )
# </POTBO_STAGE S0392>

# <POTBO_STAGE S0394>


# =========================================================
# DİYALOG
# =========================================================


def diyalog_yazisini_sifirla():
    global diyalog_yazi_baslangici, diyalog_tamamlandi
    diyalog_yazi_baslangici = pygame.time.get_ticks()
    diyalog_tamamlandi = False


def diyalog_gorunen_metin(metin):
    global diyalog_tamamlandi
    metin = str(metin)
    if diyalog_tamamlandi:
        return metin
    gecen = max(0, pygame.time.get_ticks() - diyalog_yazi_baslangici)
    adet = min(len(metin), 1 + gecen // DIYALOG_HARF_ARALIGI)
    if adet >= len(metin):
        diyalog_tamamlandi = True
    return metin[:adet]


def diyalog_yazisini_tamamla():
    global diyalog_tamamlandi
    diyalog_tamamlandi = True


def diyalog_baslat(akis):
    global aktif_diyalog
    global diyalog_index
    global diyalog_secim_index
    global oyun_alt_durumu
    global diyalog_onemli_item_bekliyor

    if not isinstance(akis, (list, tuple)):
        aktif_diyalog = []
        oyun_alt_durumu = HARITA
        return False

    aktif_diyalog = [dugum for dugum in akis if isinstance(dugum, dict)]

    if not aktif_diyalog:
        oyun_alt_durumu = HARITA
        return False

    diyalog_index = 0
    diyalog_secim_index = 0
    diyalog_onemli_item_bekliyor = False
    diyalog_yazisini_sifirla()
    oyun_alt_durumu = DIYALOG

    diyalog_aksiyonlarini_isle()
    return oyun_alt_durumu in (DIYALOG, DIYALOG_SECIM)
# </POTBO_STAGE S0394>

# <POTBO_STAGE S0397>


def diyalog_ilerlet():
    global diyalog_index

    if not aktif_diyalog:
        return

    diyalog_index += 1
    diyalog_yazisini_sifirla()
    diyalog_aksiyonlarini_isle()


def diyalog_secimini_onayla():
    global aktif_diyalog
    global diyalog_index

    if not (0 <= diyalog_index < len(aktif_diyalog)):
        diyalog_aksiyonlarini_isle()
        return

    dugum = aktif_diyalog[diyalog_index]
    secenekler = dugum.get("choices", [])

    if not secenekler:
        diyalog_index += 1
        diyalog_aksiyonlarini_isle()
        return

    secim_index = diyalog_secim_index % len(secenekler)
    secim_dugumu = secenekler[secim_index]

    if not (isinstance(secim_dugumu, (list, tuple)) and len(secim_dugumu) == 2):
        diyalog_index += 1
        diyalog_aksiyonlarini_isle()
        return

    eklenecek_akis = secim_dugumu[1]

    if not isinstance(eklenecek_akis, (list, tuple)):
        eklenecek_akis = []

    aktif_diyalog = (
        aktif_diyalog[:diyalog_index]
        + [dugum for dugum in eklenecek_akis if isinstance(dugum, dict)]
        + aktif_diyalog[diyalog_index + 1 :]
    )

    diyalog_aksiyonlarini_isle()


def aktif_diyalog_secim_sayisi():
    if not (0 <= diyalog_index < len(aktif_diyalog)):
        return 0

    dugum = aktif_diyalog[diyalog_index]

    if not isinstance(dugum, dict):
        return 0

    secenekler = dugum.get("choices", [])

    if not isinstance(secenekler, list):
        return 0

    return len(secenekler)
# </POTBO_STAGE S0397>

# <POTBO_STAGE S0402>


def npc_konusmasini_baslat():
    if not npc_intro_tamamlandi:
        akis = ilk_konusma_akisi()
    elif ganimet_alindi and not ganimet_sonrasi_konusma_yapildi:
        akis = ganimet_sonrasi_akisi()
    elif magara_yolu_ogrenildi:
        akis = rastgele_eadric_akisi()
    else:
        akis = [
            satir(
                eadric_adi(),
                bt(
                    "Kayalıkların ardındakiler hâlâ sahiplerini bekliyor.",
                    "What lies beyond the rocks still waits for its owners.",
                ),
            )
        ]

    return diyalog_baslat(akis)
# </POTBO_STAGE S0402>

# <POTBO_STAGE S0404>


def diyalog_ciz():
    if not (aktif_diyalog and 0 <= diyalog_index < len(aktif_diyalog)):
        return

    dugum = aktif_diyalog[diyalog_index]

    if not isinstance(dugum, dict):
        return

    rect = pygame.Rect(70, 472, 1140, 188)

    pygame.draw.rect(ekran, (3, 3, 6), rect)
    pygame.draw.rect(ekran, BEYAZ, rect, 4)

    if "choices" in dugum:
        secenekler = dugum.get("choices", [])

        yazi_yaz(
            bt("SEÇİM", "CHOICE"),
            rect.x + 35,
            rect.y + 24,
            PARLAK_KIRMIZI,
            oyun_font,
        )

        for index, secim_dugumu in enumerate(secenekler[:3]):
            if not (isinstance(secim_dugumu, (list, tuple)) and secim_dugumu):
                continue

            secenek_metni = str(secim_dugumu[0])
            secili = index == diyalog_secim_index

            yazi_yaz(
                ("▶ " if secili else "  ") + secenek_metni,
                rect.x + 48,
                rect.y + 67 + index * 35,
                BEYAZ if secili else GRI,
                oyun_kucuk_font,
            )

        return

    konusmaci = konusmaci_gorunen_adi(dugum.get("speaker", ""))
    metin = diyalog_gorunen_metin(dugum.get("text", ""))

    yazi_yaz(
        konusmaci,
        rect.x + 35,
        rect.y + 22,
        PARLAK_KIRMIZI,
        oyun_font,
    )

    satirlar = metni_satirlara_bol(metin, oyun_kucuk_font, rect.width - 70)

    y = rect.y + 62
    for metin_satiri in satirlar[:4]:
        yazi_yaz(metin_satiri, rect.x + 35, y, BEYAZ, oyun_kucuk_font)
        y += 28
# </POTBO_STAGE S0404>

# <POTBO_STAGE S0466>


# =========================================================
# OYUN İÇİ DURAKLATMA MENÜSÜ
# =========================================================


def duraklatma_secenekleri():
    return [
        t("resume_game"),
        t("return_main_menu"),
        t("pause_settings"),
        t("pause_quit"),
    ]
# </POTBO_STAGE S0466>

# <POTBO_STAGE S0469>


def _stage1_ana_menu_onay_ciz():
    standart_onay_penceresi_ciz(t("main_menu_confirm"), ana_menu_onay_index, "oyun")


ana_menu_onay_ciz = _stage1_ana_menu_onay_ciz
# </POTBO_STAGE S0469>

# <POTBO_STAGE S0472>


def pause_ayar_secenekleri():
    return [
        "master",
        "effect",
        "dialogue",
        "brightness",
        "interaction_prompts",
        "screen_shake",
        "fps",
        "back",
    ]
# </POTBO_STAGE S0472>

# <POTBO_STAGE S0478>


def ayar_satiri_ciz(rect, ayar, secili):
    rect = buton_click_anim_rect(rect, secili)
    pygame.draw.rect(
        ekran,
        (56, 4, 15) if secili else (8, 7, 11),
        rect,
        border_radius=0,
    )
    pygame.draw.rect(
        ekran,
        PARLAK_KIRMIZI if secili else (72, 64, 72),
        rect,
        2 if secili else 1,
        border_radius=0,
    )

    baslik_rengi = BEYAZ if secili else ACIK_GRI
    # Açıklama, başlığın ikincil tipografik katmanıdır.
    alt_renk = (162, 155, 168) if secili else (104, 98, 110)

    yazi_yaz(
        ayar_etiketi(ayar),
        rect.x + 18,
        rect.y + 14,
        baslik_rengi,
        kucuk_font,
    )

    deger = ayar_degeri(ayar)
    if deger:
        deger_genisligi = kucuk_font.size(deger)[0]
        yazi_yaz(
            deger,
            rect.right - 18 - deger_genisligi,
            rect.y + 14,
            SARI if secili else ACIK_GRI,
            kucuk_font,
        )

    aciklama = ayar_aciklamasi(ayar)
    if aciklama:
        yazi_yaz(
            aciklama,
            rect.x + 18,
            rect.y + 38,
            alt_renk,
            mini_font,
        )

    oran = ayar_sayisal_oran(ayar)
    if oran is not None:
        bar = pygame.Rect(rect.x + 18, rect.bottom - 11, rect.width - 36, 4)
        pygame.draw.rect(ekran, (25, 19, 24), bar)
        pygame.draw.rect(
            ekran,
            (156, 13, 35),
            (
                bar.x,
                bar.y,
                int(bar.width * max(0.0, min(1.0, oran))),
                bar.height,
            ),
        )


def ayarlar_arka_plani_ciz():
    if ayarlar_donus_durumu == DURAKLATMA:
        oyun_ekrani_ciz()
        koyu_kaplama(192)
    else:
        varsayilan_gotik_arka_plan()

    # Ayrı ekran hissi veren hafif piksel örgüsü.
    doku = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    for x in range(0, GENISLIK, 32):
        pygame.draw.line(doku, (120, 0, 24, 10), (x, 0), (x, YUKSEKLIK), 1)
    for y in range(0, YUKSEKLIK, 32):
        pygame.draw.line(doku, (120, 0, 24, 8), (0, y), (GENISLIK, y), 1)
    ekran.blit(doku, (0, 0))
    koyu_kaplama(120)
# </POTBO_STAGE S0478>

# <POTBO_STAGE S0482>


def pause_ayarlar_ciz():
    oyun_ekrani_ciz()
    koyu_kaplama(200)

    panel = pygame.Rect(GENISLIK // 2 - 405, 20, 810, 680)
    gotik_panel(panel, PARLAK_KIRMIZI, 248)

    yazi_yaz(
        bt("OYUN AYARLARI", "IN-GAME SETTINGS"),
        panel.centerx,
        panel.y + 38,
        PARLAK_KIRMIZI,
        menu_baslik_font,
        True,
    )

    for index, ayar in enumerate(pause_ayar_secenekleri()):
        rect = pygame.Rect(
            panel.x + 58,
            panel.y + 72 + index * 76,
            panel.width - 116,
            64,
        )
        ayar_satiri_ciz(rect, ayar, index == ayar_index)


def ayarlar_ciz():
    # Ana menüden ve pause içinden aynı ayarlar ekranı kullanılır; böylece
    # ses davranışı, tuş atamaları ve kategori yapısı iki yerde ayrışmaz.
    tam_ayarlar_ciz()
# </POTBO_STAGE S0482>

# <POTBO_STAGE S0492>


def menu_onizleme_yuzeyi_olustur():
    """
    Ana menüye geçiş sırasında kullanılacak tam ekran görüntüyü hazırlar.
    """

    onceki_ekran = ekran.copy()

    ana_menu_ciz()

    menu_yuzeyi = ekran.copy()

    ekran.blit(onceki_ekran, (0, 0))

    return menu_yuzeyi
# </POTBO_STAGE S0492>

# <POTBO_STAGE S0497>


def hud_uyari_baslat(tur):
    global stamina_uyari_bitis, mana_uyari_bitis
    bitis = pygame.time.get_ticks() + 430
    if tur == "stamina":
        stamina_uyari_bitis = bitis
    elif tur == "mana":
        mana_uyari_bitis = bitis
# </POTBO_STAGE S0497>

# <POTBO_STAGE S0510>


def _stage1_oyuncu_olum_menu_fade_orani(simdi=None):
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if oyuncu_olum_baslangic_ms <= 0:
        return 0.0
    gecen = int(simdi) - int(oyuncu_olum_baslangic_ms) - OLU_MENU_GECIKME_MS
    if gecen <= 0:
        return 0.0
    p = max(
        0.0,
        min(1.0, gecen / max(1.0, float(OLU_MENU_FADE_IN_MS))),
    )
    # smoothstep: düz lineer fade yerine ağır başlayan, yumuşak biten sinematik geçiş.
    return p * p * (3.0 - 2.0 * p)


oyuncu_olum_menu_fade_orani = _stage1_oyuncu_olum_menu_fade_orani


def oyuncu_olum_menu_hazir_mi():
    if oyuncu_olum_cikis_baslangic_ms > 0:
        return False
    return oyuncu_olum_menu_fade_orani() >= 0.985
# </POTBO_STAGE S0510>

# <POTBO_STAGE S0529>


_oyuncu_olum_menu_layer_ciz = _stage1__oyuncu_olum_menu_layer_ciz
# </POTBO_STAGE S0529>

# <POTBO_STAGE S0535>


def oyuncu_olum_ui_ciz():
    if oyuncu_hp > 0:
        return
    katman = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    katman.fill((10, 0, 3, 74))
    ekran.blit(katman, (0, 0))
    yazi_yaz(
        t("game_over_title"),
        GENISLIK // 2,
        YUKSEKLIK - 112,
        PARLAK_KIRMIZI,
        oyun_buyuk_font,
        True,
    )
    if oyuncu_son_infaz_kaynagi:
        yazi_yaz(
            oyuncu_son_infaz_kaynagi,
            GENISLIK // 2,
            YUKSEKLIK - 78,
            ACIK_GRI,
            mini_font,
            True,
        )
# </POTBO_STAGE S0535>

# <POTBO_STAGE S0537>


def oyuncu_bayginlik_ui_ciz():
    simdi = pygame.time.get_ticks()
    if oyuncu_hp <= 0 or simdi >= oyuncu_baygin_bitis:
        return
    kalan = max(0.0, (oyuncu_baygin_bitis - simdi) / 1000.0)
    kaplama = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    kaplama.fill((24, 0, 4, 36))
    ekran.blit(kaplama, (0, 0))
    yazi_yaz(
        bt("BAYGIN", "STUNNED"),
        GENISLIK // 2,
        YUKSEKLIK - 92,
        PARLAK_KIRMIZI,
        normal_font,
        True,
    )
    yazi_yaz(
        f"{kalan:.1f}s",
        GENISLIK // 2,
        YUKSEKLIK - 63,
        ACIK_GRI,
        mini_font,
        True,
    )
# </POTBO_STAGE S0537>

# <POTBO_STAGE S0549>


def oyuncu_dash_yap(dx, dy):
    """Dash'i başlatır; fizik hareketi sonraki framelere ease-out olarak yayılır."""
    global oyuncu_yonu, son_dash_zamani, oyuncu_stamina, stamina_son_harcama
    global dash_aktif_baslangic, dash_aktif_bitis, dash_aktif_yonu, dash_aktif_son_ease
    simdi = pygame.time.get_ticks()
    if (
        oyuncu_kontrol_kilitli_mi(simdi)
        or oyuncu_saldiriyor
        or oyuncu_dash_aktif_mi(simdi)
    ):
        return False
    if simdi - son_dash_zamani < DASH_BEKLEME_SURESI:
        return False
    if oyuncu_stamina < DASH_STAMINA_MALIYETI:
        hud_uyari_baslat("stamina")
        return False
    yon = pygame.Vector2(float(dx), float(dy))
    if yon.length_squared() <= 1e-6:
        return False
    yon = yon.normalize()
    if abs(yon.x) > abs(yon.y):
        oyuncu_yonu = "right" if yon.x > 0 else "left"
    else:
        oyuncu_yonu = "down" if yon.y > 0 else "up"
    oyuncu_stamina = max(0.0, oyuncu_stamina - DASH_STAMINA_MALIYETI)
    stamina_son_harcama = simdi
    son_dash_zamani = simdi

    dash_aktif_baslangic = simdi
    dash_aktif_bitis = simdi + DASH_SURESI_MS
    dash_aktif_yonu = yon
    dash_aktif_son_ease = 0.0
    return True
# </POTBO_STAGE S0549>

# <POTBO_STAGE S0607>
V34_DEATH_BUTTON_FADE_MS = 1600
# </POTBO_STAGE S0607>

# <POTBO_STAGE S0617>


# Death MAIN MENU confirmation keeps the death tableau as its background.
_v33_ana_menu_onay_ciz_v34 = ana_menu_onay_ciz
# </POTBO_STAGE S0617>

# <POTBO_STAGE S0620>

# =========================================================
# V34 PROFESSIONAL POLISH / COLLISION SAFETY / SPECIAL MOVE DIRECTOR
# =========================================================
# Bu katman mevcut sistemleri söküp yeniden yazmak yerine runtime kontratlarını
# güçlendirir. Özellikle üç problem çözülür:
#   1) dynamic-body overlap yüzünden oyuncunun "içeride kilitlenmesi",
#   2) scripted special move'un collision polygonlarının içine gömülmesi,
#   3) üç-vuruşlu tekniğin hedef erken öldüğünde görsel/işitsel olarak yarıda kalması.
# Aynı katman dash izi, special-move kamera kompozisyonu, hit crescendo, güvenli
# depenetration ve küçük HUD geri bildirimleri ekler. Save formatı değişmez.

V34_POLISH_VERSION = 34
# </POTBO_STAGE S0620>

# <POTBO_STAGE S0638>
v34_special_last_target_uid = ""
# </POTBO_STAGE S0638>

# <POTBO_STAGE S0712>


def _v34_combo_ui_ciz():
    simdi = pygame.time.get_ticks()
    if v34_combo_count < 2 or simdi >= v34_combo_fade_until:
        return
    if simdi <= v34_combo_window_until:
        alpha = 235
        scale_bump = 1.0
    else:
        fade = max(
            0.0,
            min(
                1.0,
                (v34_combo_fade_until - simdi) / V34_COMBO_FADE_MS,
            ),
        )
        alpha = int(235 * fade)
        scale_bump = 1.0

    kill_flash = simdi < v34_combo_kill_flash_until
    x = GENISLIK - 150
    y = 214
    label = bt(f"{v34_combo_count} VURUŞ", f"{v34_combo_count} HIT")
    detail = bt(
        f"{v34_combo_damage} toplam hasar",
        f"{v34_combo_damage} total damage",
    )
    text = normal_font.render(
        label,
        True,
        (245, 236, 239) if not kill_flash else (255, 226, 126),
    )
    sub = mini_font.render(detail, True, (190, 182, 188))
    text.set_alpha(alpha)
    sub.set_alpha(int(alpha * 0.80))
    box_w = max(text.get_width(), sub.get_width()) + 24
    box_h = text.get_height() + sub.get_height() + 14
    box = pygame.Rect(0, 0, box_w, box_h)
    box.midtop = (x, y)
    bg = pygame.Surface((box.width, box.height), pygame.SRCALPHA)
    bg.fill((7, 5, 9, int(128 * (alpha / 235.0))))
    pygame.draw.rect(
        bg,
        (118, 16, 36, int(145 * (alpha / 235.0))),
        bg.get_rect(),
        1,
    )
    ekran.blit(bg, box.topleft)
    tr = text.get_rect(midtop=(box.centerx, box.top + 5))
    sr = sub.get_rect(midtop=(box.centerx, tr.bottom + 2))
    ekran.blit(text, tr)
    ekran.blit(sub, sr)
# </POTBO_STAGE S0712>

# <POTBO_STAGE S0719>


def oyun_ekrani_ciz():
    _v34c_oyun_ekrani_ciz()
    if oyuncu_hp <= 0:
        return
    _v34_damage_feedback_ciz()
    _v34_combo_ui_ciz()
    _v34_special_recovery_control_hint_ciz()
# </POTBO_STAGE S0719>

# <POTBO_STAGE S0770>
v34f_special_target_anchor_uid = ""
# </POTBO_STAGE S0770>

# <POTBO_STAGE S0774>


def _v34f_actor_uid(actor):
    if actor is None:
        return "none"
    explicit = getattr(actor, "uid", None)
    if explicit not in (None, ""):
        return str(explicit)
    kind = getattr(actor, "tur", actor.__class__.__name__)
    return f"{kind}:{id(actor)}"
# </POTBO_STAGE S0774>

# <POTBO_STAGE S0781>


# ---------------------------------------------------------
# TRANSIENT STATE HYGIENE
# ---------------------------------------------------------
def _v34f_reset_transient_combat_state(after_load=False):
    """Save'e ait olmayan kısa ömürlü state'leri tek merkezden temizler."""
    global v34_attack_buffer_until, v34_dash_buffer_until, v34_dash_buffer_direction
    global v34f_post_special_recovery_until, v34f_special_target_anchor
    global v34f_special_target_anchor_uid, v34f_special_started_seen
    global v34f_special_was_active, dash_tus_kilitli
    global oyuncu_hareket_hiz_vektoru, oyuncu_zorlanmis_hiz

    v34_attack_buffer_until = 0
    v34_dash_buffer_until = 0
    v34_dash_buffer_direction.update(0.0, 0.0)
    oyuncu_hareket_hiz_vektoru.update(0.0, 0.0)
    oyuncu_zorlanmis_hiz.update(0.0, 0.0)
    v34f_special_target_anchor = None
    v34f_special_target_anchor_uid = ""
    v34f_special_started_seen = False
    v34f_special_was_active = False
    v34f_post_special_recovery_until = 0
    if after_load:
        try:
            gelistirici_x_skill_sifirla(True)
        except Exception:
            pass
        dash_tus_kilitli = False
# </POTBO_STAGE S0781>

# <POTBO_STAGE S0784>


# ---------------------------------------------------------
# SPECIAL TARGET COMMITMENT
# ---------------------------------------------------------
def _v34f_special_capture_target_anchor():
    global v34f_special_target_anchor, v34f_special_target_anchor_uid
    target = gelistirici_x_skill_hedef
    if target is None:
        v34f_special_target_anchor = None
        v34f_special_target_anchor_uid = ""
        return False
    if v34_special_locked_center is not None:
        center = pygame.Vector2(v34_special_locked_center)
    else:
        center = pygame.Vector2(float(target.x), float(target.y))
    v34f_special_target_anchor = center.copy()
    v34f_special_target_anchor_uid = _v34f_actor_uid(target)
    return True
# </POTBO_STAGE S0784>

# <POTBO_STAGE S0790>


def _v34f_special_finished(simdi):
    global v34f_special_finished_ms, v34f_special_last_exit
    global v34f_post_special_recovery_until, dash_tus_kilitli
    global v34f_special_target_anchor, v34f_special_target_anchor_uid

    v34f_special_finished_ms = int(simdi)
    v34f_special_last_exit = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    v34f_post_special_recovery_until = int(simdi) + max(
        90, int(V34_SPECIAL_RECOVERY_GRACE_MS)
    )
    _v34f_add_landing_mark(
        v34f_special_last_exit,
        v34f_special_last_final_direction,
        simdi,
    )
    # Special çıkışında static/dynamic depenetration son kez çalışır.
    try:
        _v34_player_depenetrate(False)
    except Exception as exc:
        _v34f_report_issue(
            "special_exit_depenetrate_failed",
            exc,
            False,
            "warning",
        )
    # Shift fiziksel olarak basılı değilse dash latch'i serbest bırak. Basılıysa KEYUP
    # mevcut input sistemi tarafından güvenli biçimde çözülür.
    try:
        keys = pygame.key.get_pressed()
        dash_pressed = bool(keys[tus_atamasi("dash")])
    except Exception:
        dash_pressed = False
    if not dash_pressed:
        dash_tus_kilitli = False
    v34f_special_target_anchor = None
    v34f_special_target_anchor_uid = ""
# </POTBO_STAGE S0790>

# <POTBO_STAGE S0831>


# ---------------------------------------------------------
# KESIK IVMESI / SEVERANCE FLOW
# ---------------------------------------------------------
# Başarılı fiziksel melee temasları küçük bir hareket ritmi biriktirir. Flow hasar
# artırmaz. Normal dash stamina maliyetini ve input hissini hafifçe iyileştirir; kısa
# süre saldırmadan kalınca kendiliğinden söner. Böylece sistem oyuncuya yeni bir HUD
# ezberi dayatmadan agresif, kontrollü oyunu ödüllendirir.
V35_FLOW_MAX = 3.0
# </POTBO_STAGE S0831>

# <POTBO_STAGE S0863>


def _v35_flow_hud_ciz():
    """V36: flow HUD tam ekran alpha surface ayırmaz."""
    if (
        oyun_durumu != OYUN
        or oyun_alt_durumu != HARITA
        or oyuncu_hp <= 0
        or v35_combat_flow <= 0.01
    ):
        return
    simdi = pygame.time.get_ticks()
    pulse = 1.0
    if simdi < v35_flow_pulse_until:
        pulse = 1.0 + 0.18 * ((v35_flow_pulse_until - simdi) / 160.0)
    surf = pygame.Surface((70, 32), pygame.SRCALPHA)
    full = int(v35_combat_flow)
    frac = max(0.0, min(1.0, v35_combat_flow - full))
    for i in range(3):
        alpha = 38
        if i < full:
            alpha = int(155 * pulse)
        elif i == full and frac > 0:
            alpha = int(38 + 110 * frac)
        a = pygame.Vector2(6 + i * 18, 25)
        b = pygame.Vector2(17 + i * 18, 7)
        pygame.draw.line(surf, (126, 8, 24, min(180, alpha)), a, b, 5)
        pygame.draw.line(
            surf,
            (248, 230, 234, min(230, int(alpha * 1.18))),
            a,
            b,
            1,
        )
    ekran.blit(surf, (GENISLIK - 96, YUKSEKLIK - 62))
# </POTBO_STAGE S0863>

# <POTBO_STAGE S0866>

# ---------------------------------------------------------
# UI TIMING COORDINATOR
# ---------------------------------------------------------
V37_UI_ACTION_DELAY_MS = 150
V37_UI_INPUT_GUARD_MS = 165
v37_ui_pending_action = None
v37_ui_pending_due = 0
v37_ui_pending_label = ""
v37_ui_last_action_ms = -10000
v37_ui_click_state = None
# </POTBO_STAGE S0866>

# <POTBO_STAGE S0868>
_v37_buton_click_anim_rect_original = buton_click_anim_rect
# </POTBO_STAGE S0868>

# <POTBO_STAGE S0870>


def buton_click_anim_rect(rect, secili=True):
    # Global click timestamp başka bir ekrana sızıp yanlış butonu oynatmasın.
    if v37_ui_click_state is not None and oyun_durumu != v37_ui_click_state:
        return rect.copy()
    return _v37_buton_click_anim_rect_original(rect, secili)


def v37_ui_action_pending():
    return v37_ui_pending_action is not None


def v37_ui_action_schedule(action, label="ui", delay_ms=V37_UI_ACTION_DELAY_MS):
    """Bir UI aksiyonunu click animasyonu görünür olduktan sonra tek kez uygular."""
    global v37_ui_pending_action, v37_ui_pending_due, v37_ui_pending_label
    if action is None or v37_ui_pending_action is not None:
        return False
    now = pygame.time.get_ticks()
    v37_ui_pending_action = action
    v37_ui_pending_due = now + max(1, int(delay_ms))
    v37_ui_pending_label = str(label)
    return True


def v37_ui_transition_tick():
    """Pending UI action'ı render edilmiş en az birkaç frame sonrasında commit eder."""
    global v37_ui_pending_action, v37_ui_pending_due, v37_ui_pending_label
    global v37_ui_last_action_ms
    if v37_ui_pending_action is None:
        return False
    now = pygame.time.get_ticks()
    if now < v37_ui_pending_due:
        return False
    action = v37_ui_pending_action
    label = v37_ui_pending_label
    v37_ui_pending_action = None
    v37_ui_pending_due = 0
    v37_ui_pending_label = ""
    try:
        action()
        v37_ui_last_action_ms = now
        return True
    except SystemExit:
        raise
    except Exception as exc:
        debug_log("V37 deferred UI action failed:", label, repr(exc))
        return False
# </POTBO_STAGE S0870>

# <POTBO_STAGE S0872>


def tus_girdisi_kabul(olay):
    # Pending click/action sırasında ikinci KEYDOWN state makinesine giremez.
    if olay.type == pygame.KEYDOWN and v37_ui_action_pending():
        return False
    return _v37_tus_girdisi_kabul_original(olay)


_v37_menu_secimini_calistir_original = menu_secimini_calistir


def menu_secimini_calistir():
    # Event handler click sesini/animasyonunu zaten başlatır; state bir sonraki
    # 150ms boyunca aynı ekranda kalır ve basma animasyonu gerçekten görünür.
    return v37_ui_action_schedule(
        _v37_menu_secimini_calistir_original,
        "main_menu",
    )


def _v37_pause_action_execute(index):
    global oyun_durumu, ana_menu_onay_index, ana_menu_onay_donus_durumu
    global ayarlar_donus_durumu, ayar_kategori_index, ayar_index, ayar_odak
    global cikis_index, cikis_donus_durumu
    idx = int(index)
    if idx == 0:
        oyun_durumu = OYUN
    elif idx == 1:
        ana_menu_onay_index = 1
        ana_menu_onay_donus_durumu = DURAKLATMA
        oyun_durumu = ANA_MENU_ONAY
    elif idx == 2:
        ayarlar_donus_durumu = DURAKLATMA
        ayar_kategori_index = 0
        ayar_index = 0
        ayar_odak = "kategori"
        oyun_durumu = AYARLAR
    elif idx == 3:
        cikis_index = 1
        cikis_donus_durumu = DURAKLATMA
        oyun_durumu = CIKIS_ONAY
# </POTBO_STAGE S0872>

# <POTBO_STAGE S0878>


def _v37_death_action_execute(index):
    global ana_menu_onay_index, ana_menu_onay_donus_durumu
    global cikis_index, cikis_donus_durumu, oyun_durumu
    global oyuncu_olum_cikis_baslangic_ms, oyuncu_olum_cikis_hedefi
    idx = int(index)
    if idx == 0:
        oyuncu_olum_cikis_baslat("restart")
    elif idx == 1:
        oyuncu_olum_cikis_baslat("load")
    elif idx == 2:
        ana_menu_onay_index = 1
        ana_menu_onay_donus_durumu = OYUN
        oyun_durumu = ANA_MENU_ONAY
    else:
        oyuncu_olum_cikis_baslangic_ms = 0
        oyuncu_olum_cikis_hedefi = None
        cikis_index = 1
        cikis_donus_durumu = OYUN
        oyun_durumu = CIKIS_ONAY
# </POTBO_STAGE S0878>

# <POTBO_STAGE S0881>


def _v37_settings_back_execute():
    global oyun_durumu
    ayarlari_kaydet()
    oyun_durumu = ayarlar_donus_durumu
# </POTBO_STAGE S0881>

# <POTBO_STAGE S0885>


# Click'i daha görünür yapan tek, ucuz highlight. Ana/pause menu zaten aynı
# menu_susleme_ciz() dilini paylaştığı için state-specific efekt gerekmez.
_v37_menu_susleme_ciz_original = menu_susleme_ciz


def menu_susleme_ciz(rect, secili):
    _v37_menu_susleme_ciz_original(rect, secili)
    if not secili or (
        v37_ui_click_state is not None and oyun_durumu != v37_ui_click_state
    ):
        return
    elapsed = pygame.time.get_ticks() - ui_buton_click_baslangic
    if 0 <= elapsed < UI_BUTON_CLICK_SURE_MS:
        p = elapsed / max(1.0, float(UI_BUTON_CLICK_SURE_MS))
        alpha = int(235 * (1.0 - p) ** 1.35)
        rr = buton_click_anim_rect(rect.inflate(32, 14), True)
        # Display surface üzerinde alpha kanalının etkisi sürücüye bağlı olabileceği
        # için renk yoğunluğu da fade eder; ek Surface tahsisi yapılmaz.
        c = max(80, min(255, alpha))
        pygame.draw.rect(ekran, (c, c, c), rr, 1)
# </POTBO_STAGE S0885>

# <POTBO_STAGE S0889>


def ayarlar_arka_plani_ciz():
    if ayarlar_donus_durumu == DURAKLATMA:
        oyun_ekrani_ciz()
        koyu_kaplama(192)
    else:
        varsayilan_gotik_arka_plan()
    ekran.blit(v37_settings_grid, (0, 0))
    koyu_kaplama(120)
# </POTBO_STAGE S0889>

# <POTBO_STAGE S0994>


def gelistirici_x_skill_r_baslat(simdi=None):
    """R arm olduğunda hazırlık rezervini geri ver; gerçek maliyet hit anlarında gelir."""
    global oyuncu_stamina, stamina_son_harcama
    global v38_special_arm_refund_active, v38_special_stamina_start
    global v38_special_stamina_paid_mask, v38_special_stamina_spent
    if simdi is None:
        simdi = pygame.time.get_ticks()
    effective_available = min(
        float(oyuncu_max_stamina),
        float(oyuncu_stamina) + V38_SPECIAL_PREP_REFUND,
    )
    if effective_available + 1e-6 < V38_SPECIAL_TOTAL_STAMINA:
        hud_uyari_baslat("stamina")
        bildirim_goster(
            bt(
                f"Özel hareket için {int(V38_SPECIAL_TOTAL_STAMINA)} stamina gerekiyor.",
                f"{int(V38_SPECIAL_TOTAL_STAMINA)} stamina required for the special move.",
            ),
            GRI,
        )
        return False
    ok = _v38_special_r_arm_original(simdi)
    if not ok:
        return False
    if not v38_special_arm_refund_active:
        oyuncu_stamina = min(
            float(oyuncu_max_stamina),
            float(oyuncu_stamina) + V38_SPECIAL_PREP_REFUND,
        )
        v38_special_arm_refund_active = True
    v38_special_stamina_start = float(oyuncu_stamina)
    v38_special_stamina_paid_mask = 0
    v38_special_stamina_spent = 0.0
    # Regen timer bu noktadan itibaren special'ın ilk gerçek hitini bekler.
    stamina_son_harcama = int(simdi)
    return True
# </POTBO_STAGE S0994>

# <POTBO_STAGE S1028>


# ---------------------------------------------------------
# COMPACT BALANCE SNAPSHOT
# ---------------------------------------------------------
def v38_balance_snapshot():
    """Tek çağrıda tuning için gerekli bütün özet; oyun HUD'ına otomatik basılmaz."""
    bounds = v38_tuning_bounds_validate()
    invariants = v38_cross_system_invariants()
    equation_validation = v38_equation_catalog_validate()
    return {
        "version": V38_VERSION,
        "startup_ok": bool(V38_STARTUP_OK),
        "bounds_ok": all(x.get("ok", False) for x in bounds.values()),
        "invariants_ok": all(invariants.values()),
        "equations_ok": bool(equation_validation.get("all_required"))
        and bool(equation_validation.get("no_empty_equations")),
        "fire": v38_runtime_balance_summary(),
        "projectile": v38_projectile_equation_samples(),
        "contact": v38_contact_profile(),
        "contact_contract": v38_contact_contract(),
        "special": v38_special_stamina_contract(),
        "quality": v38_fire_quality_profile(),
        "bounds": bounds,
        "invariants": invariants,
    }
# </POTBO_STAGE S1028>

# <POTBO_STAGE S1031>


def gelistirici_x_skill_r_baslat(simdi=None):
    global oyuncu_stamina, v38_special_arm_refund_active
    if simdi is None:
        simdi = pygame.time.get_ticks()
    ok = _v38_special_r_arm_stage1(simdi)
    if not ok:
        return False
    if float(oyuncu_stamina) + 1e-6 >= V38_SPECIAL_TOTAL_STAMINA:
        return True

    # Stage1 refund yaptıysa tam tersini uygula ve arm bayrağını söndür.
    if v38_special_arm_refund_active:
        oyuncu_stamina = max(0.0, float(oyuncu_stamina) - V38_SPECIAL_PREP_REFUND)
        v38_special_arm_refund_active = False
    global gelistirici_x_skill_r_basildi
    gelistirici_x_skill_r_basildi = False
    hud_uyari_baslat("stamina")
    bildirim_goster(
        bt(
            f"Özel hareket için {int(V38_SPECIAL_TOTAL_STAMINA)} stamina gerekiyor.",
            f"{int(V38_SPECIAL_TOTAL_STAMINA)} stamina required for the special move.",
        ),
        GRI,
    )
    return False
# </POTBO_STAGE S1031>

# <POTBO_STAGE S1043>
UI_BUTON_CLICK_SURE_MS = 170
# </POTBO_STAGE S1043>

# <POTBO_STAGE S1065>


def diyalog_secimini_onayla():
    global aktif_diyalog
    global diyalog_index

    if not (0 <= diyalog_index < len(aktif_diyalog)):
        diyalog_yazisini_sifirla()
        diyalog_aksiyonlarini_isle()
        return

    dugum = aktif_diyalog[diyalog_index]
    secenekler = dugum.get("choices", [])

    if not secenekler:
        diyalog_index += 1
        diyalog_yazisini_sifirla()
        diyalog_aksiyonlarini_isle()
        return

    secim_index = diyalog_secim_index % len(secenekler)
    secim_dugumu = secenekler[secim_index]

    if not (isinstance(secim_dugumu, (list, tuple)) and len(secim_dugumu) == 2):
        diyalog_index += 1
        diyalog_yazisini_sifirla()
        diyalog_aksiyonlarini_isle()
        return

    eklenecek_akis = secim_dugumu[1]
    if not isinstance(eklenecek_akis, (list, tuple)):
        eklenecek_akis = []

    aktif_diyalog = (
        aktif_diyalog[:diyalog_index]
        + [dugum for dugum in eklenecek_akis if isinstance(dugum, dict)]
        + aktif_diyalog[diyalog_index + 1 :]
    )
    diyalog_yazisini_sifirla()
    diyalog_aksiyonlarini_isle()
# </POTBO_STAGE S1065>

# <POTBO_STAGE S1092>


# Menülerde E artık hiçbir zaman genel onay değildir. E yalnız dünya/diyalog bağlamıdır.
def buton_onay_tuslari():
    return ONAY_TUSLARI


def envanter_onay_tuslari():
    return ONAY_TUSLARI


def diyalog_onay_tuslari():
    return ONAY_TUSLARI + (tus_atamasi("interact"),)


# Metin sözleşmesi: eski açıklamalar E'yi bağlamsal UI confirm gibi tanımlamasın.
METINLER["TR"]["interact_desc"] = "Konuşur, alır, açar; diyalog içinde devam eder"
METINLER["EN"]["interact_desc"] = "Talk, pick up, open; continue dialogue"
METINLER["TR"]["dialogue_next"] = "E / ENTER / SPACE: Devam"
METINLER["EN"]["dialogue_next"] = "E / ENTER / SPACE: Continue"
METINLER["TR"]["game_menu"] = (
    "WASD Hareket  J Saldırı/Hold  K Savunma  SHIFT Dash  E Etkileşim  F Öne Çıkan  Q Hızlı  TAB Envanter"
)
METINLER["EN"]["game_menu"] = (
    "WASD Move  J Attack/Hold  K Block  SHIFT Dash  E Interact  F Featured  Q Quick  TAB Inventory"
)
# </POTBO_STAGE S1092>

# <POTBO_STAGE S1106>

v42_recent_loading_hints = deque(maxlen=5)
# </POTBO_STAGE S1106>

# <POTBO_STAGE S1166>
v45_combo_last_target_uid = None
# </POTBO_STAGE S1166>

# <POTBO_STAGE S1173>


def v45_combo_reset():
    global v45_combo_count, v45_combo_last_hit_ms, v45_combo_last_target_uid
    v45_combo_count = 0
    v45_combo_last_hit_ms = -10000
    v45_combo_last_target_uid = None


def v45_combo_stage(now, target_uid=None):
    global v45_combo_count, v45_combo_last_hit_ms, v45_combo_last_target_uid
    same_target = target_uid is not None and target_uid == v45_combo_last_target_uid
    delta = int(now) - int(v45_combo_last_hit_ms)
    if (
        v45_skill_unlocked("tempo_chain")
        and delta <= V45_COMBO_WINDOW_MS
        and (same_target or v45_combo_last_target_uid is None)
    ):
        v45_combo_count = min(V45_COMBO_MAX, max(1, v45_combo_count + 1))
    else:
        v45_combo_count = 1
    v45_combo_last_hit_ms = int(now)
    v45_combo_last_target_uid = target_uid
    if v45_combo_count > 1:
        v45_skill_flash("tempo_chain")
    return v45_combo_count
# </POTBO_STAGE S1173>

# <POTBO_STAGE S1184>
V46_UI_SPRING_K = 32.0
V46_UI_SPRING_D = 9.6
V46_UI_HEAVY_SHADOW = 10
V46_UI_CORNER = 9
V46_UI_PLATE_ALPHA = 214
V46_UI_TEST_PANEL_WIDTH = 350
V46_UI_TEST_LINE_H = 18
V46_UI_PANEL_SMOOTH = 0.18
v46_ui_test_height_current = 0.0
v46_ui_panel_open = 0.0
# </POTBO_STAGE S1184>

# <POTBO_STAGE S1189>


def v46_heavy_plate(rect, active=True, alpha=V46_UI_PLATE_ALPHA):
    shadow = pygame.Surface((rect.width + 18, rect.height + 18), pygame.SRCALPHA)
    pygame.draw.rect(
        shadow,
        (0, 0, 0, 116),
        pygame.Rect(9, 9, rect.width, rect.height),
        border_radius=V46_UI_CORNER,
    )
    ekran.blit(shadow, (rect.x - 9, rect.y - 9))
    surf = pygame.Surface(rect.size, pygame.SRCALPHA)
    surf.fill((7, 6, 9, int(alpha)))
    pygame.draw.rect(
        surf,
        (62, 42, 48, 225),
        surf.get_rect(),
        2,
        border_radius=V46_UI_CORNER,
    )
    if active:
        pygame.draw.line(
            surf,
            (126, 14, 29, 236),
            (10, 6),
            (surf.get_width() - 11, 6),
            2,
        )
        pygame.draw.line(
            surf,
            (49, 35, 40, 220),
            (12, surf.get_height() - 7),
            (surf.get_width() - 13, surf.get_height() - 7),
            1,
        )
    ekran.blit(surf, rect)
# </POTBO_STAGE S1189>

# <POTBO_STAGE S1191>


def gelistirici_test_paneli_ciz():
    global v46_ui_test_height_current
    if oyun_durumu != OYUN or not GELISTIRICI_MODU:
        return
    rows = v46_test_rows()
    target_h = 37 + V46_UI_TEST_LINE_H * len(rows) + 12
    if v46_ui_test_height_current <= 1.0:
        v46_ui_test_height_current = float(target_h)
    else:
        v46_ui_test_height_current += (
            target_h - v46_ui_test_height_current
        ) * V46_UI_PANEL_SMOOTH
    h = int(round(v46_ui_test_height_current))
    rect = pygame.Rect(
        GENISLIK - V46_UI_TEST_PANEL_WIDTH - 14,
        YUKSEKLIK - h - 14,
        V46_UI_TEST_PANEL_WIDTH,
        h,
    )
    v46_heavy_plate(rect, active=True, alpha=206)
    yazi_yaz(
        bt("GELİŞTİRİCİ / TEST", "DEVELOPER / TEST"),
        rect.x + 12,
        rect.y + 13,
        ACIK_GRI,
        mini_font,
    )
    pygame.draw.line(
        ekran,
        (112, 23, 34),
        (rect.x + 10, rect.y + 31),
        (rect.right - 10, rect.y + 31),
        1,
    )
    yy = rect.y + 39
    for key_text, action_text in rows:
        yazi_yaz(key_text, rect.x + 12, yy, SARI, mini_font)
        yazi_yaz(action_text, rect.x + 120, yy, GRI, mini_font)
        yy += V46_UI_TEST_LINE_H
# </POTBO_STAGE S1191>

# <POTBO_STAGE S1209>


_v48_character_create_original = karakter_olusturma_ciz


def karakter_olusturma_ciz():
    v48_character_motion_update()
    _v48_character_create_original()
    # Waveform tail sırasında ekranın tamamına çok hafif ağır vignette; fade'in yerine değil,
    # seçimin gövdesini güçlendiren bir katman. 60 FPS'te alpha değişimi smoothstep'tir.
    if karakter_onay_gecisi_aktif:
        elapsed = pygame.time.get_ticks() - int(karakter_onay_gecisi_baslangic)
        env = v46_envelope_value(elapsed)
        if env > 0.02:
            shade = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
            alpha = int(18 + 34 * env)
            shade.fill((12, 0, 3, alpha))
            ekran.blit(
                shade,
                (0, 0),
                special_flags=pygame.BLEND_RGBA_SUB,
            )
# </POTBO_STAGE S1209>

# <POTBO_STAGE S1218>


def v50_ui_contract_check():
    rows = v46_test_rows()
    keys = tuple(row[0].replace(" ", "") for row in rows)
    return {
        "character_transition_ms": KARAKTER_ONAY_GECIS_SURESI,
        "sample_envelope_ms": V46_CHARACTER_SAMPLE_MS,
        "envelope_peak": max(v for _ms, v in V46_CHARACTER_ENVELOPE),
        "test_keys": keys,
        "all_required_visible": all(key in keys for key in V50_REQUIRED_TEST_KEYS),
        "panel_width": V46_UI_TEST_PANEL_WIDTH,
    }
# </POTBO_STAGE S1218>

# <POTBO_STAGE S1342>


def v57_combat_rhythm_hud_ciz():
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA or oyuncu_hp <= 0:
        return
    now = pygame.time.get_ticks()
    if (
        now - int(v57_state.get("last_contact_ms", -10000)) > 2600
        and not v57_attack_active()
    ):
        return
    panel = pygame.Rect(22, YUKSEKLIK - 118, 206, 82)
    layer = pygame.Surface(panel.size, pygame.SRCALPHA)
    pygame.draw.rect(
        layer,
        (8, 6, 10, 198),
        layer.get_rect(),
        border_radius=5,
    )
    pygame.draw.rect(
        layer,
        (91, 74, 87, 150),
        layer.get_rect(),
        width=1,
        border_radius=5,
    )
    ekran.blit(layer, panel.topleft)
    title = mini_font.render(bt("KESİŞ RİTMİ", "EDGE RHYTHM"), True, (214, 207, 213))
    ekran.blit(title, (panel.left + 8, panel.top + 7))
    v57_bar(
        ekran,
        pygame.Rect(panel.left + 8, panel.top + 34, 92, 7),
        v57_state.get("flow", 0.0),
        bt("AKIŞ", "FLOW"),
    )
    v57_bar(
        ekran,
        pygame.Rect(panel.left + 108, panel.top + 34, 90, 7),
        v57_state.get("fatigue", 0.0),
        bt("YÜK", "LOAD"),
    )
    precision = v57_clamp01(v57_state.get("precision", 0.0))
    ptxt = mini_font.render(
        bt("TEMAS", "CONTACT") + f" {int(precision * 100):02d}%",
        True,
        (176, 166, 175),
    )
    ekran.blit(ptxt, (panel.left + 8, panel.top + 56))
    result = str(v57_state.get("last_result", "idle"))
    result_map = {
        "clean_hit": bt("TEMİZ", "CLEAN"),
        "kill": bt("SON", "FINAL"),
        "whiff": bt("BOŞ", "WHIFF"),
        "contact": bt("TEMAS", "CONTACT"),
        "committed": bt("YAY", "ARC"),
        "idle": "",
    }
    rt = mini_font.render(
        result_map.get(result, result.upper()),
        True,
        (151, 139, 149),
    )
    ekran.blit(rt, (panel.right - rt.get_width() - 8, panel.top + 56))
# </POTBO_STAGE S1342>

# <POTBO_STAGE S1344>


def oyun_ekrani_ciz():
    result = _v57_game_draw_original()
    v57_combat_rhythm_hud_ciz()
    return result
# </POTBO_STAGE S1344>

# <POTBO_STAGE S1387>


_v60_character_screen_original = karakter_olusturma_ciz


def karakter_olusturma_ciz():
    result = _v60_character_screen_original()
    v60_confirm_vignette_ciz()
    return result
# </POTBO_STAGE S1387>

# <POTBO_STAGE S1401>


def v61_diagnostics():
    return {
        "version": V61_VERSION,
        "active_reactions": len(v61_reactions),
        "last_uid": str(v61_last.get("uid", "")),
        "last_kind": str(v61_last.get("kind", "none")),
        "last_depth": round(float(v61_last.get("depth", 0.0)), 4),
        "last_impulse": round(float(v61_last.get("impulse", 0.0)), 4),
        "last_poise_extra": round(float(v61_last.get("poise_extra", 0.0)), 3),
        "last_stun_extra_ms": int(v61_last.get("stun_extra_ms", 0)),
        "last_zone": str(v61_last.get("zone", "")),
        "last_armor": round(float(v61_last.get("armor", 0.0)), 3),
    }
# </POTBO_STAGE S1401>

# <POTBO_STAGE S1415>


# =========================================================
# END V63
# =========================================================


# =========================================================
# V64 - HEAVY HUD FRAME / INERTIAL RESOURCE READOUT
# =========================================================
V64_VERSION = "64.0"
V64_HUD_SPRING_K = 26.0
V64_HUD_SPRING_D = 10.5
V64_HUD_MAX_DROP = 3.2
V64_HUD_IMPACT_HOLD_MS = 180
V64_HUD_SPECULAR_ALPHA = 58
v64_hud_state = {
    "offset": 0.0,
    "velocity": 0.0,
    "last_hp": float(oyuncu_hp),
    "impact_until": 0,
    "impact_strength": 0.0,
    "last_update_ms": pygame.time.get_ticks(),
}


def v64_hud_update(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    previous = int(v64_hud_state.get("last_update_ms", now))
    dt = max(
        1.0 / 240.0,
        min(
            0.05,
            (int(now) - previous) / 1000.0 if now > previous else 1.0 / FPS,
        ),
    )
    v64_hud_state["last_update_ms"] = int(now)
    hp_now = float(oyuncu_hp)
    hp_before = float(v64_hud_state.get("last_hp", hp_now))
    if hp_now < hp_before:
        loss_ratio = (hp_before - hp_now) / max(1.0, float(oyuncu_max_hp))
        v64_hud_state["impact_strength"] = min(1.0, 0.28 + loss_ratio * 3.8)
        v64_hud_state["impact_until"] = int(now) + V64_HUD_IMPACT_HOLD_MS
        v64_hud_state["velocity"] += min(18.0, 5.0 + loss_ratio * 48.0)
    v64_hud_state["last_hp"] = hp_now
    target = 0.0
    if int(now) < int(v64_hud_state.get("impact_until", 0)):
        target = V64_HUD_MAX_DROP * float(v64_hud_state.get("impact_strength", 0.0))
    accel = (target - float(v64_hud_state["offset"])) * V64_HUD_SPRING_K
    accel -= float(v64_hud_state["velocity"]) * V64_HUD_SPRING_D
    v64_hud_state["velocity"] += accel * dt
    v64_hud_state["offset"] += float(v64_hud_state["velocity"]) * dt
    v64_hud_state["offset"] = v44_clamp(
        v64_hud_state["offset"], -1.4, V64_HUD_MAX_DROP + 1.5
    )


def v64_hud_frame_ciz():
    if oyun_durumu != OYUN:
        return
    v64_hud_update()
    base = hud_sol_rect()
    offset_y = int(round(v64_hud_state.get("offset", 0.0)))
    rect = base.move(0, offset_y).inflate(8, 8)
    layer = pygame.Surface(rect.size, pygame.SRCALPHA)
    pygame.draw.rect(
        layer,
        (0, 0, 0, 112),
        layer.get_rect(),
        3,
        border_radius=7,
    )
    pygame.draw.rect(
        layer,
        (72, 63, 69, 128),
        layer.get_rect().inflate(-4, -4),
        1,
        border_radius=6,
    )
    inner = layer.get_rect().inflate(-9, -9)
    pygame.draw.line(
        layer,
        (92, 12, 24, 146),
        (inner.left + 10, inner.top),
        (inner.right - 10, inner.top),
        2,
    )
    # Köşe plakaları UI'yi "ağır" gösterir fakat animasyon yalnız birkaç piksel oynar.
    corner = 12
    corner_color = (48, 42, 47, 188)
    for x, y in (
        (2, 2),
        (layer.get_width() - corner - 2, 2),
        (2, layer.get_height() - corner - 2),
        (
            layer.get_width() - corner - 2,
            layer.get_height() - corner - 2,
        ),
    ):
        pygame.draw.rect(
            layer,
            corner_color,
            pygame.Rect(x, y, corner, corner),
            border_radius=2,
        )
        pygame.draw.circle(
            layer,
            (105, 96, 102, 150),
            (x + corner // 2, y + corner // 2),
            2,
        )
    # Üst kenarda tek, çok zayıf beyaz yansıma. Kan highlight diliyle aynı materyal ailesi.
    pygame.draw.line(
        layer,
        (238, 232, 234, V64_HUD_SPECULAR_ALPHA),
        (26, 4),
        (min(layer.get_width() - 28, 116), 4),
        1,
    )
    ekran.blit(layer, rect.topleft)
# </POTBO_STAGE S1415>

# <POTBO_STAGE S1417>


def oyuncu_paneli_ciz():
    result = _v64_player_panel_original()
    v64_hud_frame_ciz()
    return result


def v64_reset():
    v64_hud_state["offset"] = 0.0
    v64_hud_state["velocity"] = 0.0
    v64_hud_state["last_hp"] = float(oyuncu_hp)
    v64_hud_state["impact_until"] = 0
    v64_hud_state["impact_strength"] = 0.0
    v64_hud_state["last_update_ms"] = pygame.time.get_ticks()


def v64_diagnostics():
    return {
        "version": V64_VERSION,
        "offset": round(float(v64_hud_state.get("offset", 0.0)), 3),
        "velocity": round(float(v64_hud_state.get("velocity", 0.0)), 3),
        "impact_strength": round(float(v64_hud_state.get("impact_strength", 0.0)), 3),
    }
# </POTBO_STAGE S1417>

# <POTBO_STAGE S1439>
V68_UID_VARIANCE = 7
# </POTBO_STAGE S1439>

# <POTBO_STAGE S1442>


def v68_uid_bias():
    ctx = v44_context_current() or {}
    if not isinstance(ctx, dict):
        return 0
    uid = str(ctx.get("target_uid", ctx.get("uid", ctx.get("target", ""))))
    if not uid:
        return 0
    checksum = sum((idx + 1) * ord(ch) for idx, ch in enumerate(uid))
    return int(checksum % (V68_UID_VARIANCE * 2 + 1)) - V68_UID_VARIANCE


def v68_apply_signature(color, key):
    global v68_last_signature, v68_last_tone
    signature = V68_SIGNATURES.get(key, V68_SIGNATURES["default"])
    uid_bias = v68_uid_bias()
    r, g, b = [int(x) for x in color]
    r = int(round((r + float(signature["red"]) + uid_bias) * float(signature["sat"])))
    g = int(round(g + float(signature["green"]) + max(0, -uid_bias) * 0.06))
    b = int(round(b + float(signature["blue"]) + max(0, uid_bias) * 0.08))
    tone = (
        max(18, min(V68_MAX_CHANNEL, r)),
        max(0, min(18, g)),
        max(2, min(31, b)),
    )
    v68_last_signature = key
    v68_last_tone = tone
    return tone
# </POTBO_STAGE S1442>

# <POTBO_STAGE S1521>


# ---------------------------------------------------------
# HIT / ATTACK HUD KAPALI
# ---------------------------------------------------------
# Normal combo 'N VURUŞ / N HIT' paneli.
def _v34_combo_ui_ciz():
    return
# </POTBO_STAGE S1521>

# <POTBO_STAGE S1523>


# Sol alttaki EDGE RHYTHM / KESİŞ RİTMİ saldırı paneli.
def v57_combat_rhythm_hud_ciz():
    return


# ---------------------------------------------------------
# BUTON CLICK: UÇ SÜSLERİN İÇİNE ÇİZGİ SIZDIRMAZ
# ---------------------------------------------------------
V76_BUTTON_CLICK_MS = 170


def buton_click_anim_rect(rect, secili=True):
    """Daha kısa mesafeli press + rebound; metali ezmek yerine fiziksel basış hissi verir."""
    rect = pygame.Rect(rect)
    if not secili:
        return rect.copy()
    if v37_ui_click_state is not None and oyun_durumu != v37_ui_click_state:
        return rect.copy()
    elapsed = pygame.time.get_ticks() - ui_buton_click_baslangic
    if elapsed < 0 or elapsed >= V76_BUTTON_CLICK_MS:
        return rect.copy()

    p = max(0.0, min(1.0, elapsed / float(V76_BUTTON_CLICK_MS)))
    if p < 0.38:
        q = p / 0.38
        # İlk 65 ms: küçük bir inward press + 1px aşağı hareket.
        scale = 1.0 - 0.055 * (1.0 - math.cos(q * math.pi * 0.5))
        y_shift = int(round(2.0 * q))
    else:
        q = (p - 0.38) / 0.62
        # Geri sekme 1.0 çevresinde çok küçük overshoot yapıp sakinleşir.
        scale = 0.945 + 0.055 * q + 0.012 * math.sin(q * math.pi)
        y_shift = int(round(2.0 * (1.0 - q)))

    w = max(1, int(round(rect.width * scale)))
    h = max(1, int(round(rect.height * scale)))
    out = pygame.Rect(0, 0, w, h)
    out.center = (rect.centerx, rect.centery + y_shift)
    return out


# V37'nin tam dikdörtgen click-outline'ı sivri uçların içinde görünüyordu. Ana buton
# çizimini koruyoruz; yalnız click parlamasını merkez plakanın yatay metal çizgilerine
# kısıtlıyoruz. Dikey outline yok, dolayısıyla uç poligonların içine çizgi giremez.
def menu_susleme_ciz(rect, secili):
    _v37_menu_susleme_ciz_original(rect, secili)
    if not secili or (
        v37_ui_click_state is not None and oyun_durumu != v37_ui_click_state
    ):
        return
    elapsed = pygame.time.get_ticks() - ui_buton_click_baslangic
    if not (0 <= elapsed < V76_BUTTON_CLICK_MS):
        return

    p = elapsed / float(V76_BUTTON_CLICK_MS)
    strength = max(0.0, (1.0 - p) ** 1.45)
    rr = buton_click_anim_rect(pygame.Rect(rect).inflate(32, 14), True)
    inset = max(24, min(42, rr.width // 7))
    if rr.width <= inset * 2 + 8:
        return
    c = int(105 + 105 * strength)
    top_y = rr.top + 5
    bottom_y = rr.bottom - 6
    pygame.draw.line(
        ekran,
        (c, 56, 68),
        (rr.left + inset, top_y),
        (rr.right - inset, top_y),
        1,
    )
    if strength > 0.28:
        c2 = int(48 + 42 * strength)
        pygame.draw.line(
            ekran,
            (c2, 18, 25),
            (rr.left + inset + 5, bottom_y),
            (rr.right - inset - 5, bottom_y),
            1,
        )
# </POTBO_STAGE S1523>

# <POTBO_STAGE S1530>


# Ölümde eski wrapper zincirinin HUD/debug/telemetry katmanlarını tamamen atla.
_v76_game_draw_original = oyun_ekrani_ciz
# </POTBO_STAGE S1530>

# <POTBO_STAGE S1547>


def _v77_death_button(rect, selected):
    base = rect.inflate(32, 14) if selected else rect.copy()
    base = buton_click_anim_rect(base, selected)
    pygame.draw.rect(ekran, V77_DEATH_BLACK, base)
    pygame.draw.rect(ekran, V77_DEATH_BODY, base, 4 if selected else 1)

    # Orijinal iki sivri uç korunur; dolgu siyah, yalnız kontur açık kırmızıdır.
    left_tip = [
        (base.left - 22, base.centery),
        (base.left, base.top + 7),
        (base.left + 13, base.centery),
        (base.left, base.bottom - 7),
    ]
    right_tip = [
        (base.right + 22, base.centery),
        (base.right, base.top + 7),
        (base.right - 13, base.centery),
        (base.right, base.bottom - 7),
    ]
    pygame.draw.polygon(ekran, V77_DEATH_BLACK, left_tip)
    pygame.draw.polygon(ekran, V77_DEATH_BLACK, right_tip)
    pygame.draw.lines(
        ekran,
        V77_DEATH_BODY,
        True,
        left_tip,
        2 if selected else 1,
    )
    pygame.draw.lines(
        ekran,
        V77_DEATH_BODY,
        True,
        right_tip,
        2 if selected else 1,
    )

    if selected:
        inner = base.inflate(-12, -9)
        if inner.width > 20 and inner.height > 5:
            pygame.draw.line(
                ekran,
                V77_DEATH_BODY,
                (inner.left + 10, inner.top + 1),
                (inner.right - 10, inner.top + 1),
                1,
            )
# </POTBO_STAGE S1547>

# <POTBO_STAGE S1550>


# Death -> MAIN MENU onayı da aynı üç renk dışına çıkmasın.
_v77_main_menu_confirm_original = ana_menu_onay_ciz


def ana_menu_onay_ciz():
    if not (ana_menu_onay_donus_durumu == OYUN and oyuncu_hp <= 0):
        return _v77_main_menu_confirm_original()

    oyuncu_olum_sahnesi_ciz()
    panel = pygame.Rect(GENISLIK // 2 - 350, 200, 700, 320)
    pygame.draw.rect(ekran, V77_DEATH_BLACK, panel)
    pygame.draw.rect(ekran, V77_DEATH_BODY, panel, 2)
    label = normal_font.render(t("main_menu_confirm"), False, V77_DEATH_BODY)
    ekran.blit(
        label,
        label.get_rect(center=(panel.centerx, panel.y + 58)),
    )
    pygame.draw.line(
        ekran,
        V77_DEATH_BODY,
        (panel.x + 75, panel.y + 98),
        (panel.right - 75, panel.y + 98),
        1,
    )
    for index, option in enumerate((t("yes"), t("no"))):
        rect = pygame.Rect(
            panel.x + 115,
            panel.y + 122 + index * 70,
            panel.width - 230,
            50,
        )
        selected = index == ana_menu_onay_index
        _v77_death_button(rect, selected)
        font = menu_font if selected else normal_font
        surf = font.render(option, False, V77_DEATH_BODY)
        ekran.blit(surf, surf.get_rect(center=rect.center))
# </POTBO_STAGE S1550>

# <POTBO_STAGE S1553>
V78_UI_FILL = (4, 3, 6)
V78_UI_LINE = (121, 34, 46)
V78_UI_LINE_SOFT = (88, 70, 79)
V78_UI_GLOW = (180, 52, 67)
V78_UI_TEXT_SOFT = (184, 176, 182)
# </POTBO_STAGE S1553>

# <POTBO_STAGE S1555>


def v78_panel_draw(rect, accent=PARLAK_KIRMIZI, alpha=236, title_band=True):
    surf = pygame.Surface(rect.size, pygame.SRCALPHA)
    surf.fill((*V78_UI_FILL, int(alpha)))
    outer = surf.get_rect()
    pygame.draw.rect(surf, (*accent, min(255, alpha + 12)), outer, 2)
    inner = outer.inflate(-10, -10)
    if inner.width > 8 and inner.height > 8:
        pygame.draw.rect(surf, (*V78_UI_LINE_SOFT, 170), inner, 1)
    if title_band and rect.height >= 48:
        pygame.draw.line(
            surf,
            (*accent, 210),
            (16, 12),
            (outer.width - 16, 12),
            2,
        )
        pygame.draw.line(
            surf,
            (*V78_UI_LINE_SOFT, 160),
            (16, outer.height - 13),
            (outer.width - 16, outer.height - 13),
            1,
        )
    corners = [
        pygame.Rect(2, 2, 12, 12),
        pygame.Rect(outer.width - 14, 2, 12, 12),
        pygame.Rect(2, outer.height - 14, 12, 12),
        pygame.Rect(outer.width - 14, outer.height - 14, 12, 12),
    ]
    for c in corners:
        pygame.draw.rect(surf, (22, 18, 24, 235), c)
        pygame.draw.rect(surf, (*accent, 165), c, 1)
    ekran.blit(surf, rect)
# </POTBO_STAGE S1555>

# <POTBO_STAGE S1557>


def slot_ciz(
    rect,
    secili=False,
    numara=None,
    item_index=None,
    tasima_kaynagi=False,
):
    _v78_slot_surface(rect, PARLAK_KIRMIZI, secili, tasima_kaynagi, False)
    if numara is not None:
        yazi_yaz(str(numara), rect.x + 8, rect.y + 6, SARI, mini_font)

    if item_index is not None and 0 <= item_index < len(envanter_itemleri):
        item = envanter_itemleri[item_index]
        if item is not None:
            ikon = (
                ITEM_RESIMLERI.get(item.get("id")) if isinstance(item, dict) else None
            )
            if ikon is not None:
                ikon_alani = pygame.Rect(0, 0, rect.width - 14, rect.height - 14)
                cizilecek_ikon = resmi_oranli_sigdir(ikon, ikon_alani, 0, 1.0, True)
                if cizilecek_ikon is not None:
                    ekran.blit(
                        cizilecek_ikon,
                        cizilecek_ikon.get_rect(center=rect.center),
                    )
            else:
                ad = item_kisa_adi(item_index)
                yazi_yaz(
                    ad[:9],
                    rect.centerx,
                    rect.centery + 5,
                    BEYAZ,
                    mini_font,
                    True,
                )
            adet = item_adedi(item)
            if adet > 1:
                adet_kutu = pygame.Rect(rect.right - 29, rect.bottom - 24, 24, 18)
                pygame.draw.rect(ekran, (6, 5, 8), adet_kutu)
                pygame.draw.rect(ekran, KOYU_KIRMIZI, adet_kutu, 1)
                yazi_yaz(
                    f"x{adet}",
                    adet_kutu.centerx,
                    adet_kutu.centery,
                    BEYAZ,
                    mini_font,
                    True,
                )
# </POTBO_STAGE S1557>

# <POTBO_STAGE S1572>


def _v78_death_button(rect, selected):
    base = buton_click_anim_rect(
        rect.inflate(28, 14) if selected else rect.copy(),
        selected,
    )
    pygame.draw.rect(ekran, V77_DEATH_BLACK, base)
    pygame.draw.rect(ekran, V77_DEATH_BODY, base, 2 if selected else 1)
    left_tip = [
        (base.left - 18, base.centery),
        (base.left, base.top + 7),
        (base.left + 10, base.centery),
        (base.left, base.bottom - 7),
    ]
    right_tip = [
        (base.right + 18, base.centery),
        (base.right, base.top + 7),
        (base.right - 10, base.centery),
        (base.right, base.bottom - 7),
    ]
    pygame.draw.polygon(ekran, V77_DEATH_BLACK, left_tip)
    pygame.draw.polygon(ekran, V77_DEATH_BLACK, right_tip)
    pygame.draw.lines(
        ekran,
        V77_DEATH_BODY,
        True,
        left_tip,
        2 if selected else 1,
    )
    pygame.draw.lines(
        ekran,
        V77_DEATH_BODY,
        True,
        right_tip,
        2 if selected else 1,
    )
    if selected:
        inner = base.inflate(-12, -10)
        pygame.draw.line(
            ekran,
            V77_DEATH_BODY,
            (inner.left + 8, inner.top + 1),
            (inner.right - 8, inner.top + 1),
            1,
        )
# </POTBO_STAGE S1572>

# <POTBO_STAGE S1574>


def ana_menu_onay_ciz():
    if not (ana_menu_onay_donus_durumu == OYUN and oyuncu_hp <= 0):
        return _v77_main_menu_confirm_original()
    oyuncu_olum_sahnesi_ciz()
    panel = pygame.Rect(GENISLIK // 2 - 350, 208, 700, 300)
    pygame.draw.rect(ekran, V77_DEATH_BLACK, panel)
    pygame.draw.rect(ekran, V77_DEATH_BODY, panel, 2)
    label = normal_font.render(t("main_menu_confirm"), False, V77_DEATH_BODY)
    ekran.blit(
        label,
        label.get_rect(center=(panel.centerx, panel.y + 54)),
    )
    pygame.draw.line(
        ekran,
        V77_DEATH_BODY,
        (panel.x + 78, panel.y + 94),
        (panel.right - 78, panel.y + 94),
        1,
    )
    for index, option in enumerate((t("yes"), t("no"))):
        rect = pygame.Rect(
            panel.x + 120,
            panel.y + 122 + index * 70,
            panel.width - 240,
            42,
        )
        selected = index == ana_menu_onay_index
        _v78_death_button(rect, selected)
        surf = (menu_font if selected else normal_font).render(
            option, False, V77_DEATH_BODY
        )
        ekran.blit(surf, surf.get_rect(center=rect.center))
# </POTBO_STAGE S1574>

# <POTBO_STAGE S1578>

# ---------------------------------------------------------
# 1) V78 HUD runtime düzeltmesi + daha sade/keskin kaynak barları
# ---------------------------------------------------------
V79_UI_PRESS_MS = 235
V79_UI_ACTION_DELAY_MS = 218
V79_UI_PRESS_DEPTH = 0.038
# </POTBO_STAGE S1578>

# <POTBO_STAGE S1580>


def oyuncu_paneli_ciz():
    panel = hud_sol_rect()
    gotik_panel(panel, PARLAK_KIRMIZI, 238)

    # V78'de olmayan coin_gorseli_getir/altin/max isimleri kullanılmıştı.
    # Burada oyunun mevcut ve kanonik değişkenleri kullanılır.
    ad = secili_karakter_adi()
    ad_rect = yazi_yaz(ad, panel.x + 22, panel.y + 17, BEYAZ, oyun_font)
    level_rect = yazi_yaz(
        f"{t('level')}: {oyuncu_level}",
        ad_rect.right + 16,
        panel.y + 17,
        level_rengi(oyuncu_level),
        oyun_font,
    )
    coin_x = min(panel.right - 84, level_rect.right + 20)
    if _v79_coin_draw(coin_x, panel.y + 16, 22):
        yazi_yaz(
            str(oyuncu_altin),
            coin_x + 29,
            panel.y + 17,
            SARI,
            oyun_font,
        )
    else:
        yazi_yaz(
            str(oyuncu_altin),
            coin_x,
            panel.y + 17,
            SARI,
            oyun_font,
        )

    hp_ratio = float(hp_gorunen) / max(1.0, float(oyuncu_max_hp))
    mana_ratio = float(mana_gorunen) / max(1.0, float(oyuncu_max_mana))
    stamina_ratio = float(stamina_gorunen) / max(1.0, float(oyuncu_max_stamina))
    hp_real = float(oyuncu_hp) / max(1.0, float(oyuncu_max_hp))

    x = panel.x + 24
    w = panel.width - 48
    hp_rect = pygame.Rect(x, panel.y + 70, w, 24)
    stamina_rect = pygame.Rect(x + 8, panel.y + 102, w - 16, 7)
    mana_rect = pygame.Rect(x, panel.y + 118, w, 21)

    _v79_sharp_bar(
        hp_rect,
        hp_real,
        (157, 3, 29),
        (31, 3, 9),
        (122, 103, 110),
        shown_ratio=hp_ratio,
    )
    _v79_sharp_bar(
        stamina_rect,
        stamina_ratio,
        (221, 195, 42),
        (38, 34, 8),
        (103, 96, 57),
        warning=pygame.time.get_ticks() < stamina_uyari_bitis,
    )
    _v79_sharp_bar(
        mana_rect,
        mana_ratio,
        (45, 117, 205),
        (7, 20, 38),
        (91, 116, 151),
        warning=pygame.time.get_ticks() < mana_uyari_bitis,
    )


# Ana/pause/death butonlarının basışı daha ağırdır; state değişimi animasyonu kesmez.
def buton_click_anim_rect(rect, secili=True):
    rect = pygame.Rect(rect)
    if not secili:
        return rect.copy()
    if v37_ui_click_state is not None and oyun_durumu != v37_ui_click_state:
        return rect.copy()
    elapsed = pygame.time.get_ticks() - ui_buton_click_baslangic
    if elapsed < 0 or elapsed >= V79_UI_PRESS_MS:
        return rect.copy()

    p = _v79_clamp01(elapsed / float(V79_UI_PRESS_MS))
    if p < 0.44:
        q = _v79_smootherstep(p / 0.44)
        scale = 1.0 - V79_UI_PRESS_DEPTH * q
        y_shift = 2.0 * q
    else:
        q = _v79_smootherstep((p - 0.44) / 0.56)
        # Çok küçük overshoot; ağır metal plaka yerine oturur.
        scale = (
            (1.0 - V79_UI_PRESS_DEPTH)
            + V79_UI_PRESS_DEPTH * q
            + math.sin(q * math.pi) * 0.006
        )
        y_shift = 2.0 * (1.0 - q)

    w = max(1, int(round(rect.width * scale)))
    h = max(1, int(round(rect.height * scale)))
    out = pygame.Rect(0, 0, w, h)
    out.center = (
        rect.centerx,
        int(round(rect.centery + y_shift)),
    )
    return out


def v37_ui_action_schedule(action, label="ui", delay_ms=None):
    global v37_ui_pending_action, v37_ui_pending_due, v37_ui_pending_label
    if action is None or v37_ui_pending_action is not None:
        return False
    if delay_ms is None:
        delay_ms = V79_UI_ACTION_DELAY_MS
    now = pygame.time.get_ticks()
    v37_ui_pending_action = action
    v37_ui_pending_due = now + max(1, int(delay_ms))
    v37_ui_pending_label = str(label)
    return True
# </POTBO_STAGE S1580>

# <POTBO_STAGE S1588>
V79_DEATH_MENU_FADE_MS = 1450
# </POTBO_STAGE S1588>

# <POTBO_STAGE S1594>


def oyuncu_olum_menu_hazir_mi():
    if oyuncu_olum_cikis_baslangic_ms > 0:
        return False
    return oyuncu_olum_menu_fade_orani() >= 0.985
# </POTBO_STAGE S1594>

# <POTBO_STAGE S1597>


def _v79_title_surface(text):
    key = str(text)
    surf = _v79_title_cache.get(key)
    if surf is None:
        surf = gameover_font.render(key, False, V77_DEATH_BODY).convert_alpha()
        _v79_title_cache[key] = surf
    return surf
# </POTBO_STAGE S1597>

# <POTBO_STAGE S1600>


def _v77_death_menu_draw(now):
    _v79_draw_death_title(now)
    menu_p = oyuncu_olum_menu_fade_orani(now)
    if menu_p <= 0.0:
        return
    menu = _v79_death_menu_content(now)
    pos = (GENISLIK // 2 - menu.get_width() // 2, 400)
    _v79_dither_blit(menu, pos, menu_p)
# </POTBO_STAGE S1600>

# <POTBO_STAGE S1606>


# =========================================================
# END V79
# =========================================================


# =========================================================
# V80 - SELECT PACE / SYMMETRIC HUD / DYNAMIC DEATH BLOOD
# =========================================================
V80_VERSION = "80.0"
# </POTBO_STAGE S1606>

# <POTBO_STAGE S1608>


def oyuncu_paneli_ciz():
    panel = hud_sol_rect()
    gotik_panel(panel, PARLAK_KIRMIZI, 238)

    ad = secili_karakter_adi()
    ad_rect = yazi_yaz(ad, panel.x + 22, panel.y + 17, BEYAZ, oyun_font)
    level_rect = yazi_yaz(
        f"{t('level')}: {oyuncu_level}",
        ad_rect.right + 16,
        panel.y + 17,
        level_rengi(oyuncu_level),
        oyun_font,
    )
    coin_x = min(panel.right - 84, level_rect.right + 20)
    if _v79_coin_draw(coin_x, panel.y + 16, 22):
        yazi_yaz(
            str(oyuncu_altin),
            coin_x + 29,
            panel.y + 17,
            SARI,
            oyun_font,
        )
    else:
        yazi_yaz(
            str(oyuncu_altin),
            coin_x,
            panel.y + 17,
            SARI,
            oyun_font,
        )

    hp_ratio = float(hp_gorunen) / max(1.0, float(oyuncu_max_hp))
    mana_ratio = float(mana_gorunen) / max(1.0, float(oyuncu_max_mana))
    stamina_ratio = float(stamina_gorunen) / max(1.0, float(oyuncu_max_stamina))
    hp_real = float(oyuncu_hp) / max(1.0, float(oyuncu_max_hp))

    x = panel.x + 24
    w = panel.width - 48
    hp_rect = pygame.Rect(x, panel.y + 70, w, 24)
    stamina_rect = pygame.Rect(x, panel.y + 101, w, 8)
    mana_rect = pygame.Rect(x, panel.y + 118, w, 21)

    _v79_sharp_bar(
        hp_rect,
        hp_real,
        (121, 2, 18),
        (24, 2, 7),
        (108, 88, 96),
        shown_ratio=hp_ratio,
    )
    _v79_sharp_bar(
        stamina_rect,
        stamina_ratio,
        (219, 193, 46),
        (36, 33, 8),
        (103, 96, 57),
        warning=pygame.time.get_ticks() < stamina_uyari_bitis,
    )
    _v79_sharp_bar(
        mana_rect,
        mana_ratio,
        (36, 186, 188),
        (6, 28, 31),
        (83, 140, 146),
        warning=pygame.time.get_ticks() < mana_uyari_bitis,
    )
# </POTBO_STAGE S1608>

# <POTBO_STAGE S1618>


def v80_diagnostics():
    return {
        "version": V80_VERSION,
        "character_select_ms": KARAKTER_ONAY_GECIS_SURESI,
        "hud_symmetric_bars": True,
        "hud_hp_darkened": True,
        "hud_mana_turquoise": True,
        "death_dynamic_emitters": len(v80_death_fx.get("emitters", [])),
        "death_dynamic_pools": len(v80_death_fx.get("pools", [])),
    }
# </POTBO_STAGE S1618>

# <POTBO_STAGE S1635>


# =========================================================
# END V81
# =========================================================


# =========================================================
# V81 - BRUTAL DEATH TABLEAU / TOPMOST HUD / HARD-EDGED BARS
# =========================================================
V81_VERSION = "81.0"
V81_HUD_ACCENT = (214, 38, 56)
V81_HUD_PANEL_ACCENT = V81_HUD_ACCENT
V81_HUD_BORDER = (112, 88, 97)
V81_HUD_DARK = (8, 7, 10)
V81_HUD_METAL = (34, 28, 33)
# </POTBO_STAGE S1635>

# <POTBO_STAGE S1640>


def _v81_draw_rivets(rect, color):
    points = [
        (rect.left + 9, rect.top + 8),
        (rect.right - 10, rect.top + 8),
        (rect.left + 9, rect.bottom - 9),
        (rect.right - 10, rect.bottom - 9),
    ]
    for pt in points:
        pygame.draw.circle(ekran, color, pt, 2)
        pygame.draw.circle(ekran, V81_HUD_DARK, pt, 1)


def _v81_bar_frame(rect, accent, dark_back):
    rect = pygame.Rect(rect)
    shell = rect.inflate(8, 8)
    pygame.draw.rect(ekran, (2, 2, 3), shell)
    pygame.draw.rect(ekran, V81_HUD_METAL, shell.inflate(-2, -2))
    pygame.draw.rect(ekran, accent, shell, 2)
    pygame.draw.rect(ekran, V81_HUD_BORDER, shell.inflate(-4, -4), 1)
    _v81_draw_rivets(shell, accent)
    pygame.draw.rect(ekran, dark_back, rect)
    pygame.draw.line(
        ekran,
        (145, 125, 132),
        (shell.left + 14, shell.top + 4),
        (shell.right - 14, shell.top + 4),
        1,
    )
    return shell
# </POTBO_STAGE S1640>

# <POTBO_STAGE S1643>


def _v81_feature_slot_draw(
    rect,
    key_text,
    item_index=None,
    selected=False,
    magic=False,
    dragging=False,
):
    rect = pygame.Rect(rect)
    accent = (
        SARI
        if dragging
        else (
            V81_SLOT_MAGIC if magic else (V81_HUD_ACCENT if selected else V81_SLOT_IDLE)
        )
    )
    bg = (16, 10, 12) if magic else (10, 9, 13)
    inner_bg = (28, 16, 18) if magic else (20, 17, 22)
    pygame.draw.rect(ekran, (2, 2, 3), rect.inflate(4, 4))
    pygame.draw.rect(ekran, bg, rect)
    pygame.draw.rect(ekran, accent, rect, 2 if (selected or dragging) else 1)
    inner = rect.inflate(-8, -8)
    if inner.width > 0 and inner.height > 0:
        pygame.draw.rect(ekran, inner_bg, inner)
        pygame.draw.rect(ekran, V81_HUD_BORDER, inner, 1)
    if selected:
        pygame.draw.line(
            ekran,
            accent,
            (rect.left + 8, rect.top + 5),
            (rect.right - 8, rect.top + 5),
            1,
        )
        pygame.draw.line(
            ekran,
            accent,
            (rect.left + 8, rect.bottom - 6),
            (rect.right - 8, rect.bottom - 6),
            1,
        )
    yazi_yaz(
        str(key_text),
        rect.x + 9,
        rect.y + 6,
        (255, 187, 84) if magic else SARI,
        mini_font,
    )

    if item_index is not None and 0 <= item_index < len(envanter_itemleri):
        item = envanter_itemleri[item_index]
        if isinstance(item, dict):
            ikon = ITEM_RESIMLERI.get(item.get("id"))
            if ikon is not None:
                ikon_alani = pygame.Rect(0, 0, rect.width - 14, rect.height - 14)
                cizilecek_ikon = resmi_oranli_sigdir(ikon, ikon_alani, 0, 1.0, True)
                if cizilecek_ikon is not None:
                    ekran.blit(
                        cizilecek_ikon,
                        cizilecek_ikon.get_rect(center=rect.center),
                    )
            else:
                ad = item_kisa_adi(item_index)
                yazi_yaz(
                    ad[:9],
                    rect.centerx,
                    rect.centery + 5,
                    BEYAZ,
                    mini_font,
                    True,
                )
            adet = item_adedi(item)
            if adet > 1:
                adet_kutu = pygame.Rect(rect.right - 29, rect.bottom - 24, 24, 18)
                pygame.draw.rect(ekran, (6, 5, 8), adet_kutu)
                pygame.draw.rect(ekran, KOYU_KIRMIZI, adet_kutu, 1)
                yazi_yaz(
                    f"x{adet}",
                    adet_kutu.centerx,
                    adet_kutu.centery,
                    BEYAZ,
                    mini_font,
                    True,
                )


def oyuncu_paneli_ciz():
    panel = hud_sol_rect()
    gotik_panel(panel, V81_HUD_PANEL_ACCENT, 242)

    ad = secili_karakter_adi()
    ad_rect = yazi_yaz(ad, panel.x + 22, panel.y + 17, BEYAZ, oyun_font)
    level_rect = yazi_yaz(
        f"{t('level')}: {oyuncu_level}",
        ad_rect.right + 16,
        panel.y + 17,
        level_rengi(oyuncu_level),
        oyun_font,
    )
    coin_x = min(panel.right - 84, level_rect.right + 20)
    if _v79_coin_draw(coin_x, panel.y + 16, 22):
        yazi_yaz(
            str(oyuncu_altin),
            coin_x + 29,
            panel.y + 17,
            SARI,
            oyun_font,
        )
    else:
        yazi_yaz(
            str(oyuncu_altin),
            coin_x,
            panel.y + 17,
            SARI,
            oyun_font,
        )

    hp_ratio = float(hp_gorunen) / max(1.0, float(oyuncu_max_hp))
    mana_ratio = float(mana_gorunen) / max(1.0, float(oyuncu_max_mana))
    stamina_ratio = float(stamina_gorunen) / max(1.0, float(oyuncu_max_stamina))
    hp_real = float(oyuncu_hp) / max(1.0, float(oyuncu_max_hp))

    x = panel.x + 26
    w = panel.width - 52
    hp_rect = pygame.Rect(x, panel.y + 68, w, 22)
    stamina_rect = pygame.Rect(x + 12, panel.y + 101, w - 24, V81_STAMINA_HEIGHT)
    mana_rect = pygame.Rect(x, panel.y + 114, w, 18)

    yazi_yaz(
        "HP",
        hp_rect.x - 2,
        hp_rect.y - 17,
        (181, 116, 123),
        mini_font,
    )
    yazi_yaz(
        "ST",
        stamina_rect.x - 2,
        stamina_rect.y - 14,
        (170, 159, 88),
        mini_font,
    )
    yazi_yaz(
        "MN",
        mana_rect.x - 2,
        mana_rect.y - 16,
        (96, 178, 181),
        mini_font,
    )

    _v81_jagged_bar(
        hp_rect,
        hp_real,
        (131, 4, 20),
        (21, 3, 8),
        (109, 88, 95),
        shown_ratio=hp_ratio,
        warning=False,
        chunk_px=19,
        coarse=True,
    )
    _v81_stamina_bar(
        stamina_rect,
        stamina_ratio,
        (219, 193, 46),
        (34, 31, 8),
        (103, 96, 57),
        warning=pygame.time.get_ticks() < stamina_uyari_bitis,
    )
    _v81_jagged_bar(
        mana_rect,
        mana_ratio,
        (30, 170, 174),
        (5, 24, 26),
        (83, 139, 144),
        shown_ratio=mana_ratio,
        warning=pygame.time.get_ticks() < mana_uyari_bitis,
        chunk_px=16,
        coarse=True,
    )
# </POTBO_STAGE S1643>

# <POTBO_STAGE S1653>


def v81_diagnostics():
    return {
        "version": V81_VERSION,
        "hud_topmost_redraw": True,
        "hud_hard_bars": True,
        "stamina_thinner": V81_STAMINA_HEIGHT,
        "death_more_brutal": True,
        "death_emitters": len(v80_death_fx.get("emitters", []))
        if isinstance(v80_death_fx, dict)
        else 0,
    }
# </POTBO_STAGE S1653>

# <POTBO_STAGE S1655>


# =========================================================
# END V81
# =========================================================

# =========================================================
# V82 - FLUID DEATH / GOTHIC HUD / DISTINCT MELEE CONTACT
# =========================================================
V82_VERSION = "82.0"
# </POTBO_STAGE S1655>

# <POTBO_STAGE S1658>

V82_UI_ACCENT = (205, 31, 49)
V82_UI_EDGE = (111, 91, 99)
V82_UI_DARK = (7, 6, 9)
V82_UI_IRON = (31, 25, 30)
# </POTBO_STAGE S1658>

# <POTBO_STAGE S1661>


def _v82_gothic_shell(rect, accent, back, cut=6):
    rect = pygame.Rect(rect)
    c = max(2, min(int(cut), rect.height // 2 - 1, rect.width // 5))
    pts = [
        (rect.left + c, rect.top),
        (rect.right - c, rect.top),
        (rect.right, rect.top + c),
        (rect.right, rect.bottom - c),
        (rect.right - c, rect.bottom),
        (rect.left + c, rect.bottom),
        (rect.left, rect.bottom - c),
        (rect.left, rect.top + c),
    ]
    pygame.draw.polygon(ekran, (2, 2, 3), pts)
    inner = rect.inflate(-4, -4)
    if inner.width > 4 and inner.height > 4:
        ci = max(1, c - 2)
        ipts = [
            (inner.left + ci, inner.top),
            (inner.right - ci, inner.top),
            (inner.right, inner.top + ci),
            (inner.right, inner.bottom - ci),
            (inner.right - ci, inner.bottom),
            (inner.left + ci, inner.bottom),
            (inner.left, inner.bottom - ci),
            (inner.left, inner.top + ci),
        ]
        pygame.draw.polygon(ekran, V82_UI_IRON, ipts)
        pygame.draw.lines(ekran, V82_UI_EDGE, True, ipts, 1)
    pygame.draw.lines(ekran, accent, True, pts, 1)
    return rect.inflate(-6, -6)
# </POTBO_STAGE S1661>

# <POTBO_STAGE S1665>


def _v82_feature_slot(rect, key_text, item_index=None, selected=False, magic=False):
    rect = pygame.Rect(rect)
    outer = rect.inflate(4, 4)
    pygame.draw.polygon(ekran, (2, 2, 3), _v82_slot_polygon(outer, 6))
    pygame.draw.polygon(ekran, (11, 9, 13), _v82_slot_polygon(rect, 5))
    accent = V82_UI_ACCENT if selected else V82_UI_EDGE
    pygame.draw.lines(
        ekran,
        accent,
        True,
        _v82_slot_polygon(rect, 5),
        2 if selected else 1,
    )
    inner = rect.inflate(-9, -9)
    pygame.draw.rect(ekran, (20, 16, 21), inner)
    pygame.draw.rect(ekran, (55, 45, 52), inner, 1)
    if selected:
        pygame.draw.line(
            ekran,
            V82_UI_ACCENT,
            (rect.left + 10, rect.top + 5),
            (rect.right - 10, rect.top + 5),
            1,
        )
    if magic:
        # Q slotu panelin rengini bozmaz; büyü kimliği yalnız küçük turuncu rune/işaretle okunur.
        pygame.draw.line(
            ekran,
            (211, 106, 36),
            (rect.right - 17, rect.top + 7),
            (rect.right - 7, rect.top + 17),
            2,
        )
    yazi_yaz(str(key_text), rect.x + 9, rect.y + 6, SARI, mini_font)

    if item_index is not None and 0 <= item_index < len(envanter_itemleri):
        item = envanter_itemleri[item_index]
        if isinstance(item, dict):
            ikon = ITEM_RESIMLERI.get(item.get("id"))
            if ikon is not None:
                alan = pygame.Rect(0, 0, rect.width - 15, rect.height - 15)
                draw = resmi_oranli_sigdir(ikon, alan, 0, 1.0, True)
                if draw is not None:
                    ekran.blit(draw, draw.get_rect(center=rect.center))
            else:
                yazi_yaz(
                    item_kisa_adi(item_index)[:9],
                    rect.centerx,
                    rect.centery + 5,
                    BEYAZ,
                    mini_font,
                    True,
                )
            adet = item_adedi(item)
            if adet > 1:
                badge = pygame.Rect(rect.right - 29, rect.bottom - 24, 24, 18)
                pygame.draw.rect(ekran, V82_UI_DARK, badge)
                pygame.draw.rect(ekran, KOYU_KIRMIZI, badge, 1)
                yazi_yaz(
                    f"x{adet}",
                    badge.centerx,
                    badge.centery,
                    BEYAZ,
                    mini_font,
                    True,
                )


def oyuncu_paneli_ciz():
    panel = hud_sol_rect()
    gotik_panel(panel, V82_UI_ACCENT, 244)

    ad = secili_karakter_adi()
    ad_rect = yazi_yaz(ad, panel.x + 22, panel.y + 17, BEYAZ, oyun_font)
    level_rect = yazi_yaz(
        f"{t('level')}: {oyuncu_level}",
        ad_rect.right + 16,
        panel.y + 17,
        level_rengi(oyuncu_level),
        oyun_font,
    )
    coin_x = min(panel.right - 84, level_rect.right + 20)
    if _v79_coin_draw(coin_x, panel.y + 16, 22):
        yazi_yaz(
            str(oyuncu_altin),
            coin_x + 29,
            panel.y + 17,
            SARI,
            oyun_font,
        )
    else:
        yazi_yaz(
            str(oyuncu_altin),
            coin_x,
            panel.y + 17,
            SARI,
            oyun_font,
        )

    hp_ratio = float(hp_gorunen) / max(1.0, float(oyuncu_max_hp))
    mana_ratio = float(mana_gorunen) / max(1.0, float(oyuncu_max_mana))
    stamina_ratio = float(stamina_gorunen) / max(1.0, float(oyuncu_max_stamina))
    hp_real = float(oyuncu_hp) / max(1.0, float(oyuncu_max_hp))

    x = panel.x + 27
    w = panel.width - 54
    hp_rect = pygame.Rect(x, panel.y + 70, w, 23)
    stamina_rect = pygame.Rect(x + 14, panel.y + 106, w - 28, V82_STAMINA_H)
    mana_rect = pygame.Rect(x, panel.y + 121, w, 19)

    _v82_gothic_bar(
        hp_rect,
        hp_real,
        (128, 3, 20),
        (22, 3, 8),
        (111, 88, 96),
        shown_ratio=hp_ratio,
    )
    _v82_stamina_bar(
        stamina_rect,
        stamina_ratio,
        pygame.time.get_ticks() < stamina_uyari_bitis,
    )
    _v82_gothic_bar(
        mana_rect,
        mana_ratio,
        (28, 166, 171),
        (5, 24, 27),
        (79, 136, 142),
        shown_ratio=mana_ratio,
        warning=pygame.time.get_ticks() < mana_uyari_bitis,
    )
# </POTBO_STAGE S1665>

# <POTBO_STAGE S1672>


def _v82_death_menu_draw(now):
    title_p = oyuncu_olum_baslik_fade_orani(now)
    menu_p = oyuncu_olum_menu_fade_orani(now)

    if title_p > 0.02:
        title = gameover_font.render(t("game_over_title"), False, V77_DEATH_BODY)
        title_rect = title.get_rect(center=(GENISLIK // 2, 136))
        ekran.blit(title, title_rect)
        # Başlığın iki yanında gotik yatay kollar; merkez boş bırakılır, okunurluk artar.
        y = title_rect.bottom + 18
        left_end = title_rect.left - 26
        right_start = title_rect.right + 26
        pygame.draw.line(
            ekran,
            V77_DEATH_BODY,
            (GENISLIK // 2 - 340, y),
            (left_end, y),
            1,
        )
        pygame.draw.line(
            ekran,
            V77_DEATH_BODY,
            (right_start, y),
            (GENISLIK // 2 + 340, y),
            1,
        )
        pygame.draw.polygon(
            ekran,
            V77_DEATH_BODY,
            [
                (left_end - 9, y),
                (left_end, y - 4),
                (left_end, y + 4),
            ],
        )
        pygame.draw.polygon(
            ekran,
            V77_DEATH_BODY,
            [
                (right_start + 9, y),
                (right_start, y - 4),
                (right_start, y + 4),
            ],
        )
        # Az sayıda sabit başlık damlası: 'kanlı' fakat menüyü kapatmıyor.
        for i, dx in enumerate((-282, -168, 193, 276)):
            phase = ((now // 30 + i * 17) % 46) / 46.0
            if phase < 0.72:
                yy = y + 3 + int((phase / 0.72) ** 1.7 * 13)
                pygame.draw.line(
                    ekran,
                    V77_DEATH_BLOOD,
                    (GENISLIK // 2 + dx, y),
                    (GENISLIK // 2 + dx, yy),
                    1,
                )

    if menu_p > 0.02:
        options = [
            t("restart"),
            t("load_game"),
            t("main_menu"),
            t("quit"),
        ]
        # Menü bölgesine temiz siyah nefes alanı. Kan/ceset görsel şölen olarak arkada kalır,
        # seçim hiyerarşisi asla kaybolmaz.
        panel = pygame.Rect(GENISLIK // 2 - 235, 390, 470, 260)
        pygame.draw.rect(ekran, V77_DEATH_BLACK, panel)
        pygame.draw.line(
            ekran,
            V77_DEATH_BODY,
            (panel.left + 34, panel.top),
            (panel.right - 34, panel.top),
            1,
        )
        pygame.draw.line(
            ekran,
            V77_DEATH_BLOOD,
            (panel.left + 72, panel.bottom),
            (panel.right - 72, panel.bottom),
            1,
        )
        for i, text in enumerate(options):
            rect = pygame.Rect(GENISLIK // 2 - 170, 410 + i * 56, 340, 34)
            selected = i == oyuncu_olum_menu_index
            _v77_death_button(rect, selected)
            font = menu_font if selected else normal_font
            surf = font.render(text, False, V77_DEATH_BODY)
            ekran.blit(surf, surf.get_rect(center=rect.center))


_v77_death_menu_draw = _v82_death_menu_draw
# </POTBO_STAGE S1672>

# <POTBO_STAGE S1683>


# =========================================================
# END V82
# =========================================================

# =========================================================
# V83 - DEATH TABLEAU REFOCUS / SHARP GOTHIC HUD / LIGHTER STAMINA
# =========================================================
V83_VERSION = "83.0"
# </POTBO_STAGE S1683>

# <POTBO_STAGE S1686>

V83_UI_ACCENT = (189, 26, 43)
V83_UI_EDGE = (96, 79, 87)
V83_UI_DARK = (7, 6, 9)
V83_UI_FILL = (14, 11, 15)
# </POTBO_STAGE S1686>

# <POTBO_STAGE S1689>


def _v83_panel(rect, accent=V83_UI_ACCENT, alpha=244):
    rect = pygame.Rect(rect)
    surf = pygame.Surface(rect.size, pygame.SRCALPHA)
    outer = [(x - rect.x, y - rect.y) for x, y in _v83_poly(rect, 10)]
    pygame.draw.polygon(surf, (3, 3, 4, alpha), outer)
    inner_rect = pygame.Rect(4, 4, rect.width - 8, rect.height - 8)
    inner = [(x - rect.x, y - rect.y) for x, y in _v83_poly(rect.inflate(-8, -8), 8)]
    pygame.draw.polygon(surf, (12, 10, 14, min(255, alpha)), inner)
    pygame.draw.lines(surf, (*accent, 220), True, outer, 1)
    pygame.draw.lines(surf, (*V83_UI_EDGE, 190), True, inner, 1)
    if rect.width > 80:
        pygame.draw.line(
            surf,
            (116, 98, 105, 120),
            (18, 8),
            (rect.width - 18, 8),
            1,
        )
        pygame.draw.line(
            surf,
            (44, 34, 38, 140),
            (18, rect.height - 9),
            (rect.width - 18, rect.height - 9),
            1,
        )
    ekran.blit(surf, rect)


# --- HUD -----------------------------------------------------------------
def _v83_bar_shell(rect, accent):
    shell = pygame.Rect(rect).inflate(8, 6)
    pygame.draw.polygon(ekran, (2, 2, 3), _v83_poly(shell, 7))
    pygame.draw.polygon(ekran, (15, 11, 16), _v83_poly(shell.inflate(-3, -3), 5))
    pygame.draw.lines(ekran, accent, True, _v83_poly(shell, 7), 1)
    pygame.draw.lines(
        ekran,
        V83_UI_EDGE,
        True,
        _v83_poly(shell.inflate(-3, -3), 5),
        1,
    )
# </POTBO_STAGE S1689>

# <POTBO_STAGE S1692>


def _v83_slot(rect, key_text, item_index=None, selected=False, magic=False):
    rect = pygame.Rect(rect)
    outer = rect.inflate(3, 3)
    pygame.draw.polygon(ekran, (2, 2, 3), _v83_poly(outer, 6))
    pygame.draw.polygon(ekran, (10, 9, 13), _v83_poly(rect, 5))
    accent = V83_UI_ACCENT if selected else V83_UI_EDGE
    pygame.draw.lines(ekran, accent, True, _v83_poly(rect, 5), 1)
    inner = rect.inflate(-8, -8)
    if inner.width > 0 and inner.height > 0:
        pygame.draw.rect(ekran, (18, 14, 19), inner)
        pygame.draw.rect(ekran, (49, 39, 45), inner, 1)
    if selected:
        pygame.draw.line(
            ekran,
            V83_UI_ACCENT,
            (rect.left + 9, rect.top + 5),
            (rect.right - 9, rect.top + 5),
            1,
        )
    if magic:
        pygame.draw.line(
            ekran,
            (204, 109, 34),
            (rect.right - 16, rect.top + 8),
            (rect.right - 8, rect.top + 16),
            2,
        )
    yazi_yaz(str(key_text), rect.x + 8, rect.y + 6, SARI, mini_font)
    if item_index is not None and 0 <= item_index < len(envanter_itemleri):
        item = envanter_itemleri[item_index]
        if isinstance(item, dict):
            ikon = ITEM_RESIMLERI.get(item.get("id"))
            if ikon is not None:
                alan = pygame.Rect(0, 0, rect.width - 15, rect.height - 15)
                draw = resmi_oranli_sigdir(ikon, alan, 0, 1.0, True)
                if draw is not None:
                    ekran.blit(draw, draw.get_rect(center=rect.center))
            else:
                yazi_yaz(
                    item_kisa_adi(item_index)[:9],
                    rect.centerx,
                    rect.centery + 5,
                    BEYAZ,
                    mini_font,
                    True,
                )
            adet = item_adedi(item)
            if adet > 1:
                badge = pygame.Rect(rect.right - 29, rect.bottom - 24, 24, 18)
                pygame.draw.rect(ekran, V83_UI_DARK, badge)
                pygame.draw.rect(ekran, KOYU_KIRMIZI, badge, 1)
                yazi_yaz(
                    f"x{adet}",
                    badge.centerx,
                    badge.centery,
                    BEYAZ,
                    mini_font,
                    True,
                )


def oyuncu_paneli_ciz():
    panel = hud_sol_rect()
    _v83_panel(panel, V83_UI_ACCENT, 244)

    ad = secili_karakter_adi()
    ad_rect = yazi_yaz(ad, panel.x + 22, panel.y + 17, BEYAZ, oyun_font)
    level_rect = yazi_yaz(
        f"{t('level')}: {oyuncu_level}",
        ad_rect.right + 16,
        panel.y + 17,
        level_rengi(oyuncu_level),
        oyun_font,
    )
    coin_x = min(panel.right - 84, level_rect.right + 20)
    if _v79_coin_draw(coin_x, panel.y + 16, 22):
        yazi_yaz(
            str(oyuncu_altin),
            coin_x + 29,
            panel.y + 17,
            SARI,
            oyun_font,
        )
    else:
        yazi_yaz(
            str(oyuncu_altin),
            coin_x,
            panel.y + 17,
            SARI,
            oyun_font,
        )

    hp_ratio = float(hp_gorunen) / max(1.0, float(oyuncu_max_hp))
    mana_ratio = float(mana_gorunen) / max(1.0, float(oyuncu_max_mana))
    stamina_ratio = float(stamina_gorunen) / max(1.0, float(oyuncu_max_stamina))
    hp_real = float(oyuncu_hp) / max(1.0, float(oyuncu_max_hp))

    x = panel.x + 28
    w = panel.width - 56
    hp_rect = pygame.Rect(x, panel.y + 70, w, 18)
    stamina_rect = pygame.Rect(x + 12, panel.y + 100, w - 24, V83_STAMINA_H)
    mana_rect = pygame.Rect(x, panel.y + 112, w, 16)

    yazi_yaz(
        "HP",
        hp_rect.x,
        hp_rect.y - 15,
        (165, 114, 121),
        mini_font,
    )
    yazi_yaz(
        "ST",
        stamina_rect.x,
        stamina_rect.y - 13,
        (170, 159, 89),
        mini_font,
    )
    yazi_yaz(
        "MN",
        mana_rect.x,
        mana_rect.y - 14,
        (94, 170, 171),
        mini_font,
    )

    _v83_bar(
        hp_rect,
        hp_real,
        (132, 5, 21),
        (20, 4, 8),
        (108, 85, 92),
        shown_ratio=hp_ratio,
        marks=6,
    )
    _v83_stamina_bar(
        stamina_rect,
        stamina_ratio,
        warning=pygame.time.get_ticks() < stamina_uyari_bitis,
    )
    _v83_bar(
        mana_rect,
        mana_ratio,
        (28, 160, 164),
        (5, 22, 24),
        (82, 132, 136),
        shown_ratio=mana_ratio,
        warning=pygame.time.get_ticks() < mana_uyari_bitis,
        marks=6,
    )
# </POTBO_STAGE S1692>

# <POTBO_STAGE S1705>


_v77_death_menu_draw = _v83_death_menu_draw
# </POTBO_STAGE S1705>

# <POTBO_STAGE S1707>


# HUD yine en üstte kalsın; dünya katmanları artık buna sızamaz.
_v83_game_draw_original = oyun_ekrani_ciz
# </POTBO_STAGE S1707>

# <POTBO_STAGE S1709>


def v83_diagnostics():
    return {
        "version": V83_VERSION,
        "death_title_side_lines_removed": True,
        "killer_ground_removed": True,
        "hud_sharper_gothic": True,
        "stamina_cost": SALDIRI_STAMINA_MALIYETI,
        "attack_cd_ms": saldiri_bekleme_suresi,
    }
# </POTBO_STAGE S1709>

# <POTBO_STAGE S1715>
V84_UI_EDGE = (111, 91, 97)
V84_UI_DARK = (8, 6, 9)
# </POTBO_STAGE S1715>

# <POTBO_STAGE S1726>


def v84_actor_uid(actor):
    if actor is None:
        return ""
    explicit = getattr(actor, "uid", None)
    if explicit not in (None, ""):
        return str(explicit)
    return f"{getattr(actor, 'tur', actor.__class__.__name__)}:{id(actor)}"
# </POTBO_STAGE S1726>

# <POTBO_STAGE S1737>


@dataclass
class V84RiposteState:
    target: Any = None
    target_uid: str = ""
    armed_at_ms: int = 0
    expires_at_ms: int = 0
    committed: bool = False
    consumed: bool = False
    attack_id: int = 0
    quality: float = 0.0
    armor_breach: str = ""

    def clear(self):
        self.target = None
        self.target_uid = ""
        self.armed_at_ms = 0
        self.expires_at_ms = 0
        self.committed = False
        self.consumed = False
        self.attack_id = 0
        self.quality = 0.0
        self.armor_breach = ""


@dataclass
class V84ExecutionState:
    active: bool = False
    target: Any = None
    target_uid: str = ""
    source: str = ""
    seed: int = 0
    elapsed_ms: float = 0.0
    last_tick_ms: int = 0
    next_beat_index: int = 0
    target_was_active: bool = False
    target_saved_state: dict = field(default_factory=dict)
    player_start: pygame.Vector2 = field(
        default_factory=lambda: pygame.Vector2(0.0, 0.0)
    )
    player_hp_at_start: int = 0
    fracture: Any = None
    slashes: list = field(default_factory=list)
    choreography_points: list = field(default_factory=list)
    final_applied: bool = False
    interrupted: bool = False
    interrupt_reason: str = ""
    cuts_landed: int = 0

    def reset(self):
        self.active = False
        self.target = None
        self.target_uid = ""
        self.source = ""
        self.seed = 0
        self.elapsed_ms = 0.0
        self.last_tick_ms = 0
        self.next_beat_index = 0
        self.target_was_active = False
        self.target_saved_state = {}
        self.player_start = pygame.Vector2(0.0, 0.0)
        self.player_hp_at_start = 0
        self.fracture = None
        self.slashes = []
        self.choreography_points = []
        self.final_applied = False
        self.interrupted = False
        self.interrupt_reason = ""
        self.cuts_landed = 0
# </POTBO_STAGE S1737>

# <POTBO_STAGE S1739>
v84_guard_last_target_uid = ""
# </POTBO_STAGE S1739>

# <POTBO_STAGE S1751>


def v84_mark_poise_break(actor, now, duration_ms):
    if actor is None:
        return
    uid = v84_actor_uid(actor)
    until = int(now) + max(1, int(duration_ms))
    v84_poise_break_windows[uid] = max(
        int(v84_poise_break_windows.get(uid, 0)),
        until,
    )
    setattr(actor, "v84_poise_broken_until", until)
    setattr(
        actor,
        "stagger_until",
        max(
            int(getattr(actor, "stagger_until", 0)),
            until,
        ),
    )
    setattr(
        actor,
        "hit_stun_until",
        max(
            int(getattr(actor, "hit_stun_until", 0)),
            until,
        ),
    )
    setattr(
        actor,
        "recovery_until",
        max(
            int(getattr(actor, "recovery_until", 0)),
            until,
        ),
    )
# </POTBO_STAGE S1751>

# <POTBO_STAGE S1753>


def v84_actor_poise_broken(actor, now=None):
    if actor is None:
        return False
    if now is None:
        now = pygame.time.get_ticks()
    uid = v84_actor_uid(actor)
    until = max(
        int(v84_poise_break_windows.get(uid, 0)),
        int(getattr(actor, "v84_poise_broken_until", 0)),
    )
    return int(now) <= until
# </POTBO_STAGE S1753>

# <POTBO_STAGE S1755>


def v84_refresh_execution_window(actor, now=None):
    if actor is None:
        return False
    if now is None:
        now = pygame.time.get_ticks()
    uid = v84_actor_uid(actor)
    if v84_execution_naturally_eligible(actor, now):
        v84_execution_windows[uid] = int(now) + 820
        setattr(actor, "v84_execution_window_until", int(now) + 820)
        return True
    return int(v84_execution_windows.get(uid, 0)) >= int(now)


def v84_riposte_active(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    state = v84_riposte_state
    if state.target is None:
        return False
    if state.consumed:
        return False
    if int(now) > int(state.expires_at_ms):
        return False
    if not v84_actor_alive(state.target):
        return False
    if v84_actor_uid(state.target) != state.target_uid:
        return False
    return v84_actor_distance(state.target) <= V84_RIPOSTE_TARGET_GRACE_PX


def v84_riposte_arm(actor, quality, now=None):
    if now is None:
        now = pygame.time.get_ticks()
    profile = V84_RIPOSTE_PROFILES.get(
        str(getattr(actor, "tur", "")),
        {
            "armor": "unknown",
        },
    )
    v84_riposte_state.target = actor
    v84_riposte_state.target_uid = v84_actor_uid(actor)
    v84_riposte_state.armed_at_ms = int(now)
    v84_riposte_state.expires_at_ms = int(now) + V84_RIPOSTE_WINDOW_MS
    v84_riposte_state.committed = False
    v84_riposte_state.consumed = False
    v84_riposte_state.attack_id = 0
    v84_riposte_state.quality = float(quality)
    v84_riposte_state.armor_breach = str(profile.get("armor", "unknown"))
# </POTBO_STAGE S1755>

# <POTBO_STAGE S1757>


def v84_perfect_guard_apply(
    source_type,
    source_x,
    source_y,
    attacker,
    now=None,
):
    global oyuncu_stamina
    global savunma_son_temasi
    global v84_guard_last_contact_ms
    global v84_guard_last_quality
    global v84_guard_last_target_uid
    global v84_perfect_guard_total
    if now is None:
        now = pygame.time.get_ticks()
    quality = v84_guard_quality(now)
    class_name = _savunma_sinifi(source_type)
    opening_ms = int(V84_GUARD_OPENING_MS[class_name])
    maximum = v84_actor_poise_max(attacker)
    poise_fraction = float(V84_GUARD_POISE_FRACTIONS[class_name])
    poise_damage = maximum * poise_fraction * (0.86 + 0.14 * quality)

    # Holding K for the current render tick may have consumed a fraction of a
    # stamina point.  This small compensation makes the contact itself net-zero
    # without turning a held guard into stamina generation.
    oyuncu_stamina = min(
        float(oyuncu_max_stamina),
        float(oyuncu_stamina) + min(0.42, SAVUNMA_TUTMA_STAMINA_SANIYE / FPS),
    )
    savunma_son_temasi = int(now)
    v84_guard_last_contact_ms = int(now)
    v84_guard_last_quality = float(quality)
    v84_guard_last_target_uid = v84_actor_uid(attacker)
    v84_perfect_guard_total += 1

    attacker.attacking = False
    attacker.attack_connected = True
    attacker.attack_damage_applied = True
    attacker.recovery_until = max(
        int(getattr(attacker, "recovery_until", 0)),
        int(now) + opening_ms,
    )
    attacker.hit_stun_until = max(
        int(getattr(attacker, "hit_stun_until", 0)),
        int(now) + opening_ms,
    )
    if hasattr(attacker, "dash_kind"):
        attacker.dash_kind = None
    if hasattr(attacker, "dash_until"):
        attacker.dash_until = 0
    attacker.vx = float(getattr(attacker, "vx", 0.0)) * -0.24
    attacker.vy = float(getattr(attacker, "vy", 0.0)) * -0.24

    broken = v84_apply_poise_damage(
        attacker,
        poise_damage,
        now,
        opening_ms,
    )
    if not broken:
        # A perfect guard always creates a short punish opening, but only a true
        # poise break satisfies the natural execution condition.
        attacker.stagger_until = max(
            int(getattr(attacker, "stagger_until", 0)),
            int(now) + min(opening_ms, 420),
        )
    v84_riposte_arm(attacker, quality, now)
    v84_refresh_execution_window(attacker, now)
    v84_perfect_guard_feedback(
        attacker,
        source_x,
        source_y,
        class_name,
        quality,
        now,
    )
    dunya_olayi_kaydet(
        "perfect_guard",
        enemy=str(getattr(attacker, "tur", source_type)),
        quality=round(float(quality), 3),
        poise_break=bool(broken),
    )
    return True
# </POTBO_STAGE S1757>

# <POTBO_STAGE S1762>


def v84_riposte_matches(actor, source):
    if not v84_riposte_state.committed:
        return False
    if v84_riposte_state.consumed:
        return False
    if actor is not v84_riposte_state.target:
        return False
    if v84_actor_uid(actor) != v84_riposte_state.target_uid:
        return False
    if int(saldiri_baslangic) != int(v84_riposte_state.attack_id):
        return False
    return _v44_is_player_melee_source(source)
# </POTBO_STAGE S1762>

# <POTBO_STAGE S1777>


def v84_execution_update(now=None):
    global oyuncu_x
    global oyuncu_y
    global oyuncu_yonu
    global v84_execution_last_end_ms
    state = v84_execution_state
    if not state.active:
        return
    if now is None:
        now = pygame.time.get_ticks()
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA:
        state.last_tick_ms = int(now)
        return
    if oyuncu_hp <= 0:
        v84_execution_interrupt("player_death")
        return
    if state.target is None:
        state.reset()
        return
    if v84_actor_uid(state.target) != state.target_uid:
        v84_execution_interrupt("target_identity")
        return

    delta_ms = max(
        0.0,
        min(50.0, float(int(now) - int(state.last_tick_ms))),
    )
    state.last_tick_ms = int(now)
    state.elapsed_ms += delta_ms
    if state.fracture is not None:
        state.fracture.update(delta_ms / 1000.0)
    v84_execution_trace_prune(now)

    player_position = v84_execution_player_position(state.elapsed_ms)
    oyuncu_x = float(player_position.x)
    oyuncu_y = float(player_position.y)
    to_target = pygame.Vector2(
        float(state.target.x) - oyuncu_x,
        float(state.target.y) - oyuncu_y,
    )
    oyuncu_yonu = v84_direction_name(to_target)

    while (
        state.next_beat_index < len(V84_EXECUTION_BEAT_TIMES)
        and state.elapsed_ms >= V84_EXECUTION_BEAT_TIMES[state.next_beat_index]
    ):
        v84_execution_apply_cut(
            state.next_beat_index,
            now,
        )
        state.next_beat_index += 1

    end_time = V84_EXECUTION_BEAT_TIMES[-1] + V84_EXECUTION_END_LINGER_MS
    if state.final_applied and state.elapsed_ms >= end_time:
        v84_execution_last_end_ms = int(now)
        state.reset()
# </POTBO_STAGE S1777>

# <POTBO_STAGE S1782>


@dataclass
class V84Wound:
    actor: Any
    actor_uid: str
    body_zone: str
    direction: pygame.Vector2
    pressure: float
    created_ms: int
    expires_ms: int
    next_emit_ms: int
    profile: str
    source: str
    ruptures: int = 0
    emitted: int = 0

    def alive(self, now):
        return (
            self.actor is not None
            and v84_actor_alive(self.actor)
            and int(now) <= int(self.expires_ms)
            and float(self.pressure) > 0.015
        )
# </POTBO_STAGE S1782>

# <POTBO_STAGE S1785>


def v84_wound_register(
    actor,
    damage,
    profile,
    direction,
    source="melee",
    now=None,
):
    if actor is None or int(getattr(actor, "hp", 0)) <= 0:
        return None
    if now is None:
        now = pygame.time.get_ticks()
    profile_name = str(profile or "slash")
    if profile_name in ("burn", "fire", "medium_blunt"):
        return None
    uid = v84_actor_uid(actor)
    key = (
        uid,
        v84_wound_zone(actor, int(now) + int(damage)),
    )
    pressure_add = v84_clamp(
        float(damage) / max(1.0, float(getattr(actor, "max_hp", 1))) * 4.8,
        0.08,
        0.58,
    )
    if "heavy" in profile_name:
        pressure_add *= 1.28
    existing = v84_wounds.get(key)
    safe_direction = v84_safe_vector(direction).normalize()
    if existing is None:
        existing = V84Wound(
            actor=actor,
            actor_uid=uid,
            body_zone=key[1],
            direction=safe_direction,
            pressure=v84_clamp(pressure_add, 0.05, 1.0),
            created_ms=int(now),
            expires_ms=int(now) + 11800,
            next_emit_ms=int(now) + random.randint(260, 480),
            profile=profile_name,
            source=str(source),
        )
        v84_wounds[key] = existing
    else:
        existing.actor = actor
        existing.direction = v84_safe_vector(
            existing.direction * 0.58 + safe_direction * 0.42
        ).normalize()
        existing.pressure = v84_clamp(
            existing.pressure + pressure_add,
            0.0,
            1.0,
        )
        existing.expires_ms = max(
            int(existing.expires_ms),
            int(now) + 8200,
        )
        existing.profile = profile_name
        existing.source = str(source)
    if len(v84_wounds) > V84_WOUND_MAX:
        oldest = min(
            v84_wounds,
            key=lambda wound_key: v84_wounds[wound_key].created_ms,
        )
        if oldest != key:
            v84_wounds.pop(oldest, None)
    return existing


def v84_wounds_for_actor(actor):
    uid = v84_actor_uid(actor)
    return [wound for wound in v84_wounds.values() if wound.actor_uid == uid]
# </POTBO_STAGE S1785>

# <POTBO_STAGE S1790>


def v84_transient_reset(restore_execution_target=True):
    global v84_guard_pressed_ms
    global v84_guard_press_serial
    global v84_guard_last_contact_ms
    global v84_guard_last_quality
    global v84_guard_last_target_uid
    global v84_guard_flash_until
    global v84_guard_flash_started_ms
    global v84_guard_label_until
    global v84_combat_last_tick_ms
    if (
        restore_execution_target
        and v84_execution_state.active
        and not v84_execution_state.final_applied
    ):
        v84_execution_restore_target_after_interrupt(pygame.time.get_ticks())
    v84_execution_state.reset()
    v84_riposte_state.clear()
    v84_guard_pressed_ms = -10000
    v84_guard_press_serial = 0
    v84_guard_last_contact_ms = -10000
    v84_guard_last_quality = 0.0
    v84_guard_last_target_uid = ""
    v84_guard_flash_until = 0
    v84_guard_flash_started_ms = 0
    v84_guard_label_until = 0
    v84_poise_break_windows.clear()
    v84_execution_windows.clear()
    v84_wounds.clear()
    v84_combat_last_tick_ms = pygame.time.get_ticks()
    try:
        v51_riposte_clear()
    except NameError:
        pass
# </POTBO_STAGE S1790>

# <POTBO_STAGE S1812>


def v84_combat_prompt_draw():
    if oyuncu_hp <= 0 or v84_execution_state.active:
        return
    now = pygame.time.get_ticks()
    target = v84_riposte_state.target
    if v84_riposte_active(now) and not v84_riposte_state.committed:
        center_x = int(dunya_ekran_x(oyuncu_x))
        center_y = int(dunya_ekran_y(oyuncu_y) - 82)
        width = 154
        plate = pygame.Rect(
            center_x - width // 2,
            center_y - 14,
            width,
            28,
        )
        points = (
            (plate.left + 8, plate.top),
            (plate.right - 14, plate.top),
            (plate.right, plate.centery),
            (plate.right - 14, plate.bottom),
            (plate.left + 8, plate.bottom),
            (plate.left, plate.centery),
        )
        pygame.draw.polygon(ekran, V84_UI_DARK, points)
        pygame.draw.lines(ekran, V84_BODY, True, points, 1)
        yazi_yaz(
            bt("J  RIPOSTE", "J  RIPOSTE"),
            plate.centerx,
            plate.centery,
            V84_BODY_HOT,
            mini_font,
            True,
        )

    eligible = [
        actor
        for actor in v84_hostile_actors(include_suspended=False)
        if v84_execution_naturally_eligible(actor, now)
    ]
    if eligible:
        actor = min(eligible, key=v84_actor_distance)
        center_x = int(dunya_ekran_x(actor.x))
        top = int(dunya_ekran_y(actor.y) - 96)
        text = bt("CTRL+Y  İNFAZ", "CTRL+Y  EXECUTE")
        rect = yazi_yaz(
            text,
            center_x,
            top,
            V84_BODY_HOT,
            mini_font,
            True,
        )
        pygame.draw.line(
            ekran,
            V84_BLOOD,
            (rect.left - 12, rect.bottom + 3),
            (rect.right + 12, rect.bottom + 3),
            2,
        )


def v84_combat_ui_draw():
    v84_guard_flash_draw()
    v84_combat_prompt_draw()
# </POTBO_STAGE S1812>

# <POTBO_STAGE S1816>


def v84_integrity_tick(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    state = v84_execution_state
    if state.active:
        if state.target is None:
            state.reset()
        elif state.target_uid != v84_actor_uid(state.target):
            v84_execution_interrupt("target_identity")
        elif not state.final_applied:
            # Rendering suspension is an invariant, not an optional animation flag.
            state.target.active = False
            state.target.attacking = False
            state.target.vx = 0.0
            state.target.vy = 0.0
    if (
        v84_riposte_state.target is not None
        and not v84_riposte_state.committed
        and int(now) > int(v84_riposte_state.expires_at_ms)
    ):
        v84_riposte_state.clear()
    return True
# </POTBO_STAGE S1816>

# <POTBO_STAGE S1821>


def v84_diagnostics():
    execution = v84_execution_state
    riposte = v84_riposte_state
    return {
        "version": V84_VERSION,
        "timing": v84_timing_contract(),
        "palette": v84_palette_contract(),
        "fracture": v84_fracture_contract(),
        "runtime": {
            "perfect_guards": int(v84_perfect_guard_total),
            "normal_guards": int(v84_normal_guard_total),
            "ripostes": int(v84_riposte_total),
            "executions_started": int(v84_execution_total),
            "executions_finished": int(v84_execution_finishes),
            "executions_interrupted": int(v84_execution_interruptions),
            "execution_active": bool(execution.active),
            "execution_target": str(execution.target_uid),
            "execution_cuts": int(execution.cuts_landed),
            "riposte_active": bool(v84_riposte_active()),
            "riposte_target": str(riposte.target_uid),
            "wounds": len(v84_wounds),
        },
    }
# </POTBO_STAGE S1821>

# <POTBO_STAGE S1834>


def v84_execution_update(now=None):
    global oyuncu_x, oyuncu_y, oyuncu_yonu, v84_execution_last_end_ms
    state = v84_execution_state
    if not state.active:
        return
    if now is None:
        now = pygame.time.get_ticks()
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA:
        state.last_tick_ms = int(now)
        return
    if oyuncu_hp <= 0:
        v84_execution_interrupt("player_death")
        return
    if state.target is None:
        state.reset()
        return
    if v84_actor_uid(state.target) != state.target_uid:
        v84_execution_interrupt("target_identity")
        return

    delta_ms = max(
        0.0,
        min(50.0, float(int(now) - int(state.last_tick_ms))),
    )
    state.last_tick_ms = int(now)
    state.elapsed_ms += delta_ms
    if state.fracture is not None:
        state.fracture.update(delta_ms / 1000.0)
    v84_execution_trace_prune(now)

    desired = v84_execution_player_position(state.elapsed_ms)
    previous = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    try:
        actual = _v34_special_scripted_position_apply(desired, previous=previous)
    except (NameError, TypeError, ValueError):
        actual = pygame.Vector2(desired)
        oyuncu_x, oyuncu_y = float(actual.x), float(actual.y)
    movement = pygame.Vector2(actual) - previous
    if movement.length_squared() > 0.04:
        oyuncu_yonu = v84_direction_name(movement)
    elif state.target is not None and state.motion_phase not in (
        "retreat",
        "aftermath",
    ):
        oyuncu_yonu = v84_direction_name(
            pygame.Vector2(
                state.target.x - oyuncu_x,
                state.target.y - oyuncu_y,
            )
        )
    v85_execution_record_motion(state, now, actual)
    state.last_player_position = pygame.Vector2(actual)

    oyuncu_hareket_hiz_vektoru.update(0.0, 0.0)
    oyuncu_zorlanmis_hiz.update(0.0, 0.0)

    while (
        state.next_beat_index < len(V84_EXECUTION_BEAT_TIMES)
        and state.elapsed_ms >= V84_EXECUTION_BEAT_TIMES[state.next_beat_index]
    ):
        v84_execution_apply_cut(state.next_beat_index, now)
        state.next_beat_index += 1

    if state.final_applied and state.elapsed_ms >= V85_EXECUTION_TOTAL_MS:
        v84_execution_last_end_ms = int(now)
        try:
            _v34_player_depenetrate(False)
        except (NameError, TypeError, ValueError):
            pass
        state.reset()
# </POTBO_STAGE S1834>

# <POTBO_STAGE S1845>


@dataclass
class V85MortalWoundState:
    active: bool = False
    finalized: bool = False
    started_ms: int = 0
    killer: Any = None
    killer_uid: str = ""
    source_x: float = 0.0
    source_y: float = 0.0
    profile: str = "slash"
    source_name: str = ""
    damage: int = 1
    artery_zone: str = "neck"
    attack_restarted: bool = False

    def reset(self):
        self.active = False
        self.finalized = False
        self.started_ms = 0
        self.killer = None
        self.killer_uid = ""
        self.source_x = 0.0
        self.source_y = 0.0
        self.profile = "slash"
        self.source_name = ""
        self.damage = 1
        self.artery_zone = "neck"
        self.attack_restarted = False
# </POTBO_STAGE S1845>

# <POTBO_STAGE S1847>


def v85_direct_killer(source_x, source_y, source_name):
    name = str(source_name or "").strip().lower()
    point = pygame.Vector2(float(source_x), float(source_y))
    candidates = []
    for actor in v84_hostile_actors(include_suspended=False):
        actor_name = str(getattr(actor, "name", "")).strip().lower()
        actor_uid = str(getattr(actor, "uid", "")).strip().lower()
        actor_type = str(getattr(actor, "tur", "")).strip().lower()
        distance = pygame.Vector2(float(actor.x), float(actor.y)).distance_to(point)
        exact = bool(name and name in (actor_name, actor_uid, actor_type))
        partial = bool(
            name and any(token and token in name for token in (actor_name, actor_type))
        )
        score = distance - (260.0 if exact else 120.0 if partial else 0.0)
        candidates.append((score, distance, actor))
    if not candidates:
        return None
    candidates.sort(key=lambda row: row[0])
    score, distance, actor = candidates[0]
    if distance > 190.0 and score > 80.0:
        return None
    return actor
# </POTBO_STAGE S1847>

# <POTBO_STAGE S1849>


def v85_mortal_wound_start(
    killer,
    source_x,
    source_y,
    profile,
    damage,
    source_name,
):
    global oyuncu_savunuyor
    state = v85_mortal_wound_state
    state.reset()
    state.active = True
    state.started_ms = pygame.time.get_ticks()
    state.killer = killer
    state.killer_uid = v84_actor_uid(killer)
    state.source_x = float(source_x)
    state.source_y = float(source_y)
    state.profile = str(profile or "slash")
    state.source_name = str(source_name or "")
    state.damage = max(1, int(damage))
    state.artery_zone = v85_artery_zone_for(profile, killer)
    oyuncu_saldiri_durumunu_sifirla()
    oyuncu_savunuyor = False
    oyuncu_hareket_hiz_vektoru.update(0.0, 0.0)
    oyuncu_zorlanmis_hiz.update(0.0, 0.0)
    dunya_olayi_kaydet(
        "mortal_followthrough_start",
        enemy=str(getattr(killer, "tur", "enemy")),
        profile=state.profile,
    )
    return True
# </POTBO_STAGE S1849>

# <POTBO_STAGE S1874>


@dataclass
class V85HoldCrossState:
    active: bool = False
    attack_id: int = 0
    target: Any = None
    target_uid: str = ""
    hit_ms: int = 0
    start: pygame.Vector2 = field(default_factory=lambda: pygame.Vector2(0.0, 0.0))
    exit: pygame.Vector2 = field(default_factory=lambda: pygame.Vector2(0.0, 0.0))
    direction: pygame.Vector2 = field(default_factory=lambda: pygame.Vector2(1.0, 0.0))
    hit_registered: bool = False

    def reset(self, attack_id=0):
        self.active = False
        self.attack_id = int(attack_id)
        self.target = None
        self.target_uid = ""
        self.hit_ms = 0
        self.start = pygame.Vector2(0.0, 0.0)
        self.exit = pygame.Vector2(0.0, 0.0)
        self.direction = pygame.Vector2(1.0, 0.0)
        self.hit_registered = False
# </POTBO_STAGE S1874>

# <POTBO_STAGE S1882>


# ---------------------------------------------------------
# SHARP HUD / SLOT GEOMETRY
# ---------------------------------------------------------
V85_HUD_PANEL_FILL = (7, 6, 9)
V85_HUD_PANEL_INNER = (14, 11, 15)
V85_HUD_EDGE = (96, 77, 86)
V85_HUD_EDGE_LIGHT = (139, 111, 120)
V85_HUD_SELECTED = (181, 8, 29)
# </POTBO_STAGE S1882>

# <POTBO_STAGE S1884>


def v85_hud_panel_draw(rect, accent=V85_HUD_SELECTED):
    rect = pygame.Rect(rect)
    layer = pygame.Surface(rect.size, pygame.SRCALPHA)
    local_outer = v85_cut_rect_points(layer.get_rect(), 11)
    local_inner = v85_cut_rect_points(layer.get_rect().inflate(-5, -5), 7)
    pygame.draw.polygon(layer, (*V85_HUD_PANEL_FILL, 244), local_outer)
    pygame.draw.lines(layer, (*accent, 255), True, local_outer, 2)
    pygame.draw.lines(layer, (*V85_HUD_EDGE, 230), True, local_inner, 1)
    pygame.draw.line(
        layer,
        (*V85_HUD_EDGE_LIGHT, 190),
        (24, 10),
        (layer.get_width() - 24, 10),
        1,
    )
    pygame.draw.line(
        layer,
        (76, 7, 20, 230),
        (12, 3),
        (layer.get_width() - 12, 3),
        2,
    )
    ekran.blit(layer, rect.topleft)


def v85_resource_bar(
    rect,
    ratio,
    fill_color,
    back_color,
    edge_color,
    trail_ratio=None,
    warning=False,
    marks=5,
):
    rect = pygame.Rect(rect)
    ratio = v84_clamp01(ratio)
    trail_ratio = ratio if trail_ratio is None else v84_clamp01(trail_ratio)
    outer = rect.inflate(8, 6)
    pygame.draw.polygon(ekran, (2, 2, 3), v85_cut_rect_points(outer, 3))
    pygame.draw.lines(
        ekran,
        V85_HUD_SELECTED if warning else edge_color,
        True,
        v85_cut_rect_points(outer, 3),
        1,
    )
    pygame.draw.rect(ekran, back_color, rect)
    if trail_ratio > ratio + 0.001:
        trail_width = int(round(rect.width * trail_ratio))
        if trail_width > 0:
            pygame.draw.rect(
                ekran,
                (68, 27, 35),
                pygame.Rect(rect.x, rect.y, trail_width, rect.height),
            )
    fill_width = int(round(rect.width * ratio))
    if fill_width > 0:
        fill_rect = pygame.Rect(rect.x, rect.y, fill_width, rect.height)
        pygame.draw.rect(ekran, fill_color, fill_rect)
        pygame.draw.line(
            ekran,
            tuple(min(255, channel + 28) for channel in fill_color),
            (fill_rect.left, fill_rect.top),
            (fill_rect.right - 1, fill_rect.top),
            1,
        )
        if fill_rect.height >= 4:
            pygame.draw.line(
                ekran,
                tuple(max(0, channel - 24) for channel in fill_color),
                (fill_rect.left, fill_rect.bottom - 1),
                (fill_rect.right - 1, fill_rect.bottom - 1),
                1,
            )
    if marks > 1:
        for index in range(1, marks):
            x = rect.left + int(round(rect.width * index / float(marks)))
            pygame.draw.line(
                ekran,
                (18, 15, 20),
                (x, rect.top),
                (x, rect.bottom - 1),
                1,
            )
    pygame.draw.rect(ekran, edge_color, rect, 1)


def v85_stamina_bar(rect, ratio, warning=False):
    rect = pygame.Rect(rect)
    ratio = v84_clamp01(ratio)
    pygame.draw.rect(ekran, (24, 21, 7), rect)
    width = int(round(rect.width * ratio))
    if width > 0:
        pygame.draw.rect(
            ekran,
            (224, 196, 46),
            pygame.Rect(rect.x, rect.y, width, rect.height),
        )
    edge = V85_HUD_SELECTED if warning else (108, 99, 52)
    pygame.draw.line(
        ekran,
        edge,
        (rect.left, rect.top - 1),
        (rect.right, rect.top - 1),
        1,
    )
    pygame.draw.line(
        ekran,
        edge,
        (rect.left, rect.bottom),
        (rect.right, rect.bottom),
        1,
    )


def v85_slot_shell(rect, selected=False, transfer=False, magic=False):
    rect = pygame.Rect(rect)
    outer = rect.inflate(4, 4)
    accent = SARI if transfer else V85_HUD_SELECTED if selected else V85_HUD_EDGE
    pygame.draw.polygon(ekran, (2, 2, 3), v85_cut_rect_points(outer, 4))
    pygame.draw.polygon(
        ekran,
        (13, 9, 11) if magic else (10, 9, 12),
        v85_cut_rect_points(rect, 3),
    )
    pygame.draw.lines(
        ekran,
        accent,
        True,
        v85_cut_rect_points(rect, 3),
        2 if selected or transfer else 1,
    )
    inner = rect.inflate(-9, -9)
    if inner.width > 0 and inner.height > 0:
        pygame.draw.rect(ekran, (18, 14, 18), inner)
        pygame.draw.rect(ekran, (52, 41, 47), inner, 1)
    if selected:
        pygame.draw.line(
            ekran,
            V85_HUD_SELECTED,
            (rect.left + 8, rect.top + 5),
            (rect.right - 8, rect.top + 5),
            2,
        )
    if magic:
        pygame.draw.line(
            ekran,
            (207, 106, 32),
            (rect.right - 16, rect.top + 7),
            (rect.right - 7, rect.top + 16),
            2,
        )


def v85_slot_contents(rect, key_text=None, item_index=None):
    rect = pygame.Rect(rect)
    if key_text is not None:
        yazi_yaz(
            str(key_text),
            rect.x + 8,
            rect.y + 6,
            SARI,
            mini_font,
        )
    if item_index is None or not isinstance(item_index, int):
        return
    if not 0 <= item_index < len(envanter_itemleri):
        return
    item = envanter_itemleri[item_index]
    if not isinstance(item, dict):
        return
    icon = ITEM_RESIMLERI.get(item.get("id"))
    if icon is not None:
        area = pygame.Rect(0, 0, rect.width - 15, rect.height - 15)
        draw = resmi_oranli_sigdir(icon, area, 0, 1.0, True)
        if draw is not None:
            ekran.blit(draw, draw.get_rect(center=rect.center))
    else:
        yazi_yaz(
            item_kisa_adi(item_index)[:9],
            rect.centerx,
            rect.centery + 5,
            BEYAZ,
            mini_font,
            True,
        )
    count = item_adedi(item)
    if count > 1:
        badge = pygame.Rect(rect.right - 29, rect.bottom - 24, 24, 18)
        pygame.draw.rect(ekran, V85_HUD_PANEL_FILL, badge)
        pygame.draw.rect(ekran, KOYU_KIRMIZI, badge, 1)
        yazi_yaz(
            f"x{count}",
            badge.centerx,
            badge.centery,
            BEYAZ,
            mini_font,
            True,
        )
# </POTBO_STAGE S1884>

# <POTBO_STAGE S1886>


def oyuncu_paneli_ciz():
    panel = hud_sol_rect()
    v85_hud_panel_draw(panel, V85_HUD_SELECTED)
    name_rect = yazi_yaz(
        secili_karakter_adi(),
        panel.x + 22,
        panel.y + 17,
        BEYAZ,
        oyun_font,
    )
    level_rect = yazi_yaz(
        f"{t('level')}: {oyuncu_level}",
        name_rect.right + 16,
        panel.y + 17,
        level_rengi(oyuncu_level),
        oyun_font,
    )
    coin_x = min(panel.right - 84, level_rect.right + 20)
    if _v79_coin_draw(coin_x, panel.y + 16, 22):
        coin_x += 29
    yazi_yaz(str(oyuncu_altin), coin_x, panel.y + 17, SARI, oyun_font)

    displayed_hp = 0.0 if v85_mortal_wound_state.active else float(oyuncu_hp)
    hp_ratio = displayed_hp / max(1.0, float(oyuncu_max_hp))
    hp_trail = (0.0 if v85_mortal_wound_state.active else float(hp_gorunen)) / max(
        1.0, float(oyuncu_max_hp)
    )
    stamina_ratio = float(stamina_gorunen) / max(1.0, float(oyuncu_max_stamina))
    mana_ratio = float(mana_gorunen) / max(1.0, float(oyuncu_max_mana))
    x = panel.x + 27
    width = panel.width - 54
    hp_rect = pygame.Rect(x, panel.y + 72, width, 19)
    stamina_rect = pygame.Rect(x + 13, panel.y + 105, width - 26, 4)
    mana_rect = pygame.Rect(x, panel.y + 127, width, 18)

    yazi_yaz("HP", x, panel.y + 55, (174, 111, 121), mini_font)
    yazi_yaz("ST", x + 13, panel.y + 92, (178, 164, 85), mini_font)
    yazi_yaz("MN", x, panel.y + 111, (84, 169, 174), mini_font)
    v85_resource_bar(
        hp_rect,
        hp_ratio,
        (137, 4, 22),
        (20, 3, 8),
        (111, 86, 94),
        trail_ratio=hp_trail,
        marks=6,
    )
    v85_stamina_bar(
        stamina_rect,
        stamina_ratio,
        warning=pygame.time.get_ticks() < stamina_uyari_bitis,
    )
    v85_resource_bar(
        mana_rect,
        mana_ratio,
        (29, 159, 165),
        (4, 21, 24),
        (78, 133, 138),
        trail_ratio=mana_ratio,
        warning=pygame.time.get_ticks() < mana_uyari_bitis,
        marks=6,
    )
# </POTBO_STAGE S1886>

# <POTBO_STAGE S1889>


def v85_diagnostics():
    timing = v84_timing_contract()
    return {
        "version": V85_VERSION,
        "execution": timing,
        "hold_cross": {
            "active": bool(v85_hold_cross_state.active),
            "one_contact": True,
            "duration_ms": V85_HOLD_CROSS_MS,
        },
        "death": {
            "variant": str(v84_death_state.variant),
            "ground_plane_fragments": True,
            "v74_persistent_blood": True,
            "mortal_followthrough": bool(v85_mortal_wound_state.active),
            "title_delay_ms": V79_DEATH_TITLE_DELAY_MS,
            "title_fade_ms": V79_DEATH_TITLE_FADE_MS,
            "menu_fade_ms": V79_DEATH_MENU_FADE_MS,
        },
        "hud": {
            "rounded_geometry": False,
            "sharp_slots": True,
            "sharp_resource_bars": True,
        },
    }
# </POTBO_STAGE S1889>

# <POTBO_STAGE S1891>
V85_STARTUP_OK = all(
    (
        V85_STARTUP_CONTRACT["execution"]["strict_guard_in_range"],
        V85_STARTUP_CONTRACT["execution"]["standard_guard_in_range"],
        V85_STARTUP_CONTRACT["execution"]["three_readable_openers"],
        V85_STARTUP_CONTRACT["execution"]["ten_hit_burst"],
        V85_STARTUP_CONTRACT["execution"]["burst_is_ultrafast"],
        V85_STARTUP_CONTRACT["execution"]["retreat_ms"] == 2300,
        V85_STARTUP_CONTRACT["death"]["title_delay_ms"] == 2500,
        V85_STARTUP_CONTRACT["death"]["title_fade_ms"] == 2700,
        V85_STARTUP_CONTRACT["death"]["menu_fade_ms"] == 1450,
    )
)
# </POTBO_STAGE S1891>

# <POTBO_STAGE S1910>


@dataclass
class V86DeathState:
    active: bool = False
    started_ms: int = 0
    last_tick_ms: int = 0
    seed: int = 0
    killer: Any = None
    killer_uid: str = ""
    killer_type: str = ""
    profile: str = "slash"
    source_name: str = ""
    source_position: pygame.Vector2 = field(
        default_factory=lambda: pygame.Vector2(0.0, 0.0)
    )
    damage: int = 1
    intensity: float = 1.0
    one_shot: bool = True
    death_kind: str = "generic"
    phase: str = "palette"
    approach_target: pygame.Vector2 = field(
        default_factory=lambda: pygame.Vector2(0.0, 0.0)
    )
    ready_ms: int = 0
    attack_ms: int = 0
    events: set = field(default_factory=set)
    body_anchor: pygame.Vector2 = field(
        default_factory=lambda: pygame.Vector2(0.0, 0.0)
    )
    body_offset: pygame.Vector2 = field(
        default_factory=lambda: pygame.Vector2(0.0, 0.0)
    )
    body_push: pygame.Vector2 = field(default_factory=lambda: pygame.Vector2(0.0, 0.0))
    body_rotation: float = 0.0
    fall_started_ms: int = 0
    fall_duration_ms: int = 430
    fall_target_rotation: float = 90.0
    base_size: tuple = (1, 1)
    original_pixels: int = 0
    remaining_mask: Any = None
    root_surface: Any = None
    pieces: list = field(default_factory=list)
    debris: list = field(default_factory=list)
    rocks: list = field(default_factory=list)
    burning_root: bool = False
    shockwave: bool = False
    head_destroyed: bool = False
    fully_fragmented: bool = False

    def reset(self):
        self.active = False
        self.started_ms = 0
        self.last_tick_ms = 0
        self.seed = 0
        self.killer = None
        self.killer_uid = ""
        self.killer_type = ""
        self.profile = "slash"
        self.source_name = ""
        self.source_position = pygame.Vector2(0.0, 0.0)
        self.damage = 1
        self.intensity = 1.0
        self.one_shot = True
        self.death_kind = "generic"
        self.phase = "palette"
        self.approach_target = pygame.Vector2(0.0, 0.0)
        self.ready_ms = 0
        self.attack_ms = 0
        self.events = set()
        self.body_anchor = pygame.Vector2(0.0, 0.0)
        self.body_offset = pygame.Vector2(0.0, 0.0)
        self.body_push = pygame.Vector2(0.0, 0.0)
        self.body_rotation = 0.0
        self.fall_started_ms = 0
        self.fall_duration_ms = 430
        self.fall_target_rotation = 90.0
        self.base_size = (1, 1)
        self.original_pixels = 0
        self.remaining_mask = None
        self.root_surface = None
        self.pieces = []
        self.debris = []
        self.rocks = []
        self.burning_root = False
        self.shockwave = False
        self.head_destroyed = False
        self.fully_fragmented = False
# </POTBO_STAGE S1910>

# <POTBO_STAGE S1917>


def v86_history_record(killer, damage, now):
    if killer is None:
        return
    uid = v84_actor_uid(killer)
    previous = v86_player_hit_history.get(uid)
    count = 1
    if previous and int(now) - int(previous.get("last_ms", 0)) <= V86_DEATH_HISTORY_MS:
        count = int(previous.get("count", 0)) + 1
    v86_player_hit_history[uid] = {
        "last_ms": int(now),
        "count": count,
        "damage": max(0, int(damage)),
    }


def v86_was_one_shot(killer, now):
    if killer is None:
        return True
    previous = v86_player_hit_history.get(v84_actor_uid(killer))
    if not previous:
        return True
    return not (
        int(now) - int(previous.get("last_ms", 0)) <= V86_DEATH_HISTORY_MS
        and int(previous.get("count", 0)) >= 1
    )
# </POTBO_STAGE S1917>

# <POTBO_STAGE S1943>
V86_STARTUP_OK = all(
    (
        V86_STARTUP_CONTRACT["execution"]["execution_beats_monotonic"],
        V86_STARTUP_CONTRACT["execution"]["three_slow_fast_slow_openers"],
        V86_STARTUP_CONTRACT["execution"]["asymmetric_x_burst_count"] == 18,
        V86_STARTUP_CONTRACT["execution"]["burst_is_ultrafast"],
        V86_STARTUP_CONTRACT["execution"]["retreat_ms"] == 2300,
        not V86_STARTUP_CONTRACT["execution"]["progress_bar"],
        V86_STARTUP_CONTRACT["death"]["fracture_seams"] is False,
        V86_STARTUP_CONTRACT["death"]["title_delay_ms"] == 2500,
        V86_STARTUP_CONTRACT["death"]["title_fade_ms"] == 2700,
        V86_STARTUP_CONTRACT["death"]["menu_fade_ms"] == 1450,
    )
)
# </POTBO_STAGE S1943>

# <POTBO_STAGE S1993>


# ---------------------------------------------------------
# Immutable damage provenance and atomic lethal ownership
# ---------------------------------------------------------


@dataclass(frozen=True)
class V88DamageProvenance:
    event_id: int
    created_ms: int
    actor: Any = field(default=None, compare=False, repr=False)
    attacker_uid: str = ""
    attacker_type: str = ""
    attacker_name: str = ""
    source_kind: str = "unknown"
    source_uid: str = ""
    source_position: tuple = (0.0, 0.0)
    attack_started_ms: int = 0
    attack_variant: str = ""
    direction: str = ""


@dataclass(frozen=True)
class V88LethalEvent:
    event_id: int
    provenance_id: int
    created_ms: int
    actor: Any = field(default=None, compare=False, repr=False)
    attacker_uid: str = ""
    attacker_type: str = ""
    attacker_name: str = ""
    source_kind: str = "unknown"
    source_uid: str = ""
    source_name: str = ""
    source_position: tuple = (0.0, 0.0)
    profile: str = "slash"
    damage: int = 0
    hp_after: int = 0
    attack_started_ms: int = 0
    attack_variant: str = ""
    direction: str = ""
    impact_already_landed: bool = True
# </POTBO_STAGE S1993>

# <POTBO_STAGE S1999>


def v88_actor_by_uid(uid, include_inactive=True):
    wanted = str(uid or "")
    if not wanted:
        return None
    for actor in v88_actor_pool(include_inactive=include_inactive):
        if str(getattr(actor, "uid", "")) == wanted:
            return actor
    return None
# </POTBO_STAGE S1999>

# <POTBO_STAGE S2003>


def v88_make_damage_source(
    actor,
    source_kind,
    source_object=None,
    position=None,
):
    now = pygame.time.get_ticks()
    actor_uid = str(getattr(actor, "uid", "")) if actor is not None else ""
    actor_type = str(getattr(actor, "tur", "")) if actor is not None else ""
    actor_name = str(getattr(actor, "name", "")) if actor is not None else ""
    source_uid = str(
        getattr(
            source_object,
            "owner_uid",
            getattr(source_object, "uid", actor_uid),
        )
    )
    if position is None:
        point = pygame.Vector2(
            float(getattr(source_object, "x", getattr(actor, "x", oyuncu_x))),
            float(getattr(source_object, "y", getattr(actor, "y", oyuncu_y))),
        )
    else:
        point = pygame.Vector2(position)
    return V88DamageProvenance(
        event_id=v88_next_damage_serial(),
        created_ms=int(now),
        actor=actor,
        attacker_uid=actor_uid,
        attacker_type=actor_type,
        attacker_name=actor_name,
        source_kind=str(source_kind or "unknown"),
        source_uid=source_uid,
        source_position=(float(point.x), float(point.y)),
        attack_started_ms=int(getattr(actor, "attack_started_ms", now)),
        attack_variant=str(getattr(actor, "attack_variant", "")),
        direction=str(
            getattr(actor, "direction", getattr(actor, "visual_direction", ""))
        ),
    )
# </POTBO_STAGE S2003>

# <POTBO_STAGE S2005>


def v85_direct_killer(source_x, source_y, source_name):
    """The killer is the damage author.  Distance is intentionally irrelevant."""
    event = v88_lethal_event
    if v88_lethal_event_matches_call(event, source_x, source_y, source_name):
        return event.actor
    provenance = v88_current_damage_source()
    if provenance is not None:
        if provenance.actor is not None:
            return provenance.actor
        return v88_unique_exact_actor(
            source_name,
            source_uid=provenance.source_uid,
        )
    return v88_unique_exact_actor(source_name)


def v88_build_lethal_event(
    source_x,
    source_y,
    profile,
    damage,
    source_name,
):
    provenance = v88_current_damage_source()
    actor = provenance.actor if provenance is not None else None
    source_uid = provenance.source_uid if provenance is not None else ""
    if actor is None:
        actor = v88_unique_exact_actor(source_name, source_uid=source_uid)
    actor_uid = str(getattr(actor, "uid", "")) if actor is not None else ""
    actor_type = (
        str(getattr(actor, "tur", ""))
        if actor is not None
        else v88_source_type_hint(source_name)
    )
    actor_name = str(getattr(actor, "name", "")) if actor is not None else ""
    return V88LethalEvent(
        event_id=v88_next_damage_serial(),
        provenance_id=int(provenance.event_id) if provenance is not None else 0,
        created_ms=int(pygame.time.get_ticks()),
        actor=actor,
        attacker_uid=actor_uid,
        attacker_type=actor_type,
        attacker_name=actor_name,
        source_kind=(provenance.source_kind if provenance is not None else "unscoped"),
        source_uid=source_uid,
        source_name=str(source_name or ""),
        source_position=(float(source_x), float(source_y)),
        profile=str(profile or "slash"),
        damage=max(0, int(damage)),
        hp_after=int(oyuncu_hp),
        attack_started_ms=(
            int(provenance.attack_started_ms) if provenance is not None else 0
        ),
        attack_variant=(
            str(provenance.attack_variant) if provenance is not None else ""
        ),
        direction=str(provenance.direction) if provenance is not None else "",
        impact_already_landed=True,
    )


def v88_record_damage_for_diagnostics(
    source_x,
    source_y,
    profile,
    damage,
    source_name,
):
    provenance = v88_current_damage_source()
    v88_recent_damage_events.append(
        {
            "time_ms": int(pygame.time.get_ticks()),
            "source": str(source_name or ""),
            "profile": str(profile or ""),
            "damage": max(0, int(damage)),
            "hp_after": int(oyuncu_hp),
            "position": (float(source_x), float(source_y)),
            "provenance_id": int(provenance.event_id) if provenance is not None else 0,
            "attacker_uid": provenance.attacker_uid if provenance is not None else "",
            "attacker_type": provenance.attacker_type
            if provenance is not None
            else v88_source_type_hint(source_name),
            "source_kind": provenance.source_kind
            if provenance is not None
            else "unscoped",
        }
    )
    if len(v88_recent_damage_events) > 48:
        del v88_recent_damage_events[:-48]
# </POTBO_STAGE S2005>

# <POTBO_STAGE S2010>


def _v88_rock_init(self, *args, **kwargs):
    _v88_rock_init_original(self, *args, **kwargs)
    self.v88_owner_ref = v88_actor_by_uid(self.owner_uid, include_inactive=True)
# </POTBO_STAGE S2010>

# <POTBO_STAGE S2012>


def _v88_rock_impact(self, simdi):
    owner = getattr(self, "v88_owner_ref", None)
    if owner is None:
        owner = v88_actor_by_uid(self.owner_uid, include_inactive=True)
    provenance = v88_make_damage_source(
        owner,
        "projectile",
        self,
        position=(self.x, self.y),
    )
    result = v88_call_with_damage_source(
        provenance,
        _v88_rock_impact_original,
        self,
        simdi,
    )
    v88_enforce_death_physics_ownership()
    return result
# </POTBO_STAGE S2012>

# <POTBO_STAGE S2020>


# ---------------------------------------------------------
# Impact-linked transitions: no replayed lethal heavy hit
# ---------------------------------------------------------


def v88_linked_lethal_event_for_scene(killer, source_name):
    event = v88_lethal_event
    if event is None:
        return None
    if killer is not None and event.actor is killer:
        return event
    if str(event.attacker_uid) and str(event.attacker_uid) == str(
        getattr(killer, "uid", "")
    ):
        return event
    if v88_name_key(event.source_name) == v88_name_key(source_name):
        return event
    return None
# </POTBO_STAGE S2020>

# <POTBO_STAGE S2100>


# ---------------------------------------------------------
# MEDIEVAL HUD / INVENTORY: IRON, OAK, RIVETS; NO MODERN CUTS
# ---------------------------------------------------------
V89_UI_IRON = (37, 31, 29)
V89_UI_IRON_DARK = (12, 10, 10)
V89_UI_OAK = (59, 39, 25)
V89_UI_OAK_LIGHT = (103, 69, 38)
V89_UI_BRASS = (154, 112, 55)
V89_UI_BLOOD = (145, 7, 24)
V89_UI_PARCHMENT = (206, 181, 126)
# </POTBO_STAGE S2100>

# <POTBO_STAGE S2102>


def hud_sol_rect():
    return pygame.Rect(18, 14, 436, 142)


def hud_sag_rect():
    return pygame.Rect(GENISLIK - 18 - 516, 14, 516, 142)


def v89_medieval_panel(rect, accent=V89_UI_BLOOD, alpha=244):
    rect = pygame.Rect(rect)
    shadow = rect.move(4, 5)
    pygame.draw.rect(ekran, (0, 0, 0), shadow)
    layer = pygame.Surface(rect.size, pygame.SRCALPHA)
    layer.fill((*V89_UI_IRON_DARK, max(0, min(255, int(alpha)))))
    pygame.draw.rect(layer, (*V89_UI_OAK, alpha), layer.get_rect().inflate(-6, -6))
    # Quiet vertical grain: deterministic, low-contrast, and explicitly material.
    for x in range(11, rect.width - 10, 23):
        pygame.draw.line(
            layer,
            (*V89_UI_OAK_LIGHT, 42),
            (x, 8),
            (x - 3, rect.height - 9),
            1,
        )
    pygame.draw.rect(layer, (*V89_UI_IRON, 255), layer.get_rect(), 4)
    pygame.draw.rect(layer, (*V89_UI_BRASS, 220), layer.get_rect().inflate(-5, -5), 1)
    pygame.draw.line(
        layer,
        (*accent, 255),
        (12, 8),
        (rect.width - 13, 8),
        2,
    )
    for point in (
        (9, 9),
        (rect.width - 10, 9),
        (9, rect.height - 10),
        (rect.width - 10, rect.height - 10),
    ):
        pygame.draw.circle(layer, (27, 23, 22, 255), point, 4)
        pygame.draw.circle(layer, (133, 113, 84, 255), point, 4, 1)
        pygame.draw.circle(layer, (196, 163, 105, 220), (point[0] - 1, point[1] - 1), 1)
    ekran.blit(layer, rect.topleft)


def v85_hud_panel_draw(rect, accent=V89_UI_BLOOD):
    v89_medieval_panel(rect, accent=accent)
# </POTBO_STAGE S2102>

# <POTBO_STAGE S2104>


def item_ikonu_ciz(item_id, rect, cerceve=True):
    rect = pygame.Rect(rect)
    if cerceve:
        pygame.draw.rect(ekran, V89_UI_IRON_DARK, rect)
        pygame.draw.rect(ekran, V89_UI_BRASS, rect, 2)
        pygame.draw.rect(ekran, V89_UI_OAK_LIGHT, rect.inflate(-6, -6), 1)
    inset = 7 if cerceve else 2
    area = rect.inflate(-inset * 2, -inset * 2)
    image = v89_tight_icon(item_id, area.size)
    if image is None:
        return False
    ekran.blit(image, image.get_rect(center=area.center))
    return True


def v85_slot_shell(rect, selected=False, transfer=False, magic=False):
    rect = pygame.Rect(rect)
    outer = rect.inflate(4, 4)
    pygame.draw.rect(ekran, (3, 2, 2), outer)
    pygame.draw.rect(ekran, V89_UI_IRON, rect)
    pygame.draw.rect(ekran, V89_UI_OAK, rect.inflate(-4, -4))
    inner = rect.inflate(-10, -10)
    pygame.draw.rect(ekran, (10, 8, 8), inner)
    pygame.draw.rect(ekran, (74, 54, 37), inner, 1)
    edge = V89_UI_BRASS if transfer else V89_UI_BLOOD if selected else (96, 82, 65)
    pygame.draw.rect(ekran, edge, rect, 3 if (selected or transfer) else 1)
    if selected:
        pygame.draw.rect(ekran, (218, 28, 43), rect.inflate(-4, -4), 1)
    if magic:
        pygame.draw.line(
            ekran,
            (218, 126, 42),
            (rect.right - 15, rect.top + 5),
            (rect.right - 5, rect.top + 15),
            2,
        )
        pygame.draw.line(
            ekran,
            (218, 126, 42),
            (rect.left + 5, rect.bottom - 15),
            (rect.left + 15, rect.bottom - 5),
            2,
        )
    for point in (
        (rect.left + 4, rect.top + 4),
        (rect.right - 5, rect.bottom - 5),
    ):
        pygame.draw.circle(ekran, (155, 126, 82), point, 1)


def v85_slot_contents(rect, key_text=None, item_index=None):
    rect = pygame.Rect(rect)
    item = None
    if isinstance(item_index, int) and 0 <= item_index < len(envanter_itemleri):
        candidate = envanter_itemleri[item_index]
        if isinstance(candidate, dict):
            item = candidate
    if item is not None:
        icon_area = rect.inflate(-8, -8)
        image = v89_tight_icon(item.get("id"), icon_area.size)
        if image is not None:
            ekran.blit(image, image.get_rect(center=icon_area.center))
        else:
            yazi_yaz(
                item_kisa_adi(item_index)[:8],
                rect.centerx,
                rect.centery,
                BEYAZ,
                mini_font,
                True,
            )
        count = item_adedi(item)
        if count > 1:
            badge = pygame.Rect(rect.right - 28, rect.bottom - 21, 24, 17)
            pygame.draw.rect(ekran, (18, 11, 8), badge)
            pygame.draw.rect(ekran, V89_UI_BRASS, badge, 1)
            yazi_yaz(f"x{count}", badge.centerx, badge.centery, BEYAZ, mini_font, True)
    if key_text is not None:
        label = str(key_text)
        label_width = max(18, mini_font.size(label)[0] + 8)
        tag = pygame.Rect(rect.x + 4, rect.y + 4, label_width, 17)
        pygame.draw.rect(ekran, (43, 28, 18), tag)
        pygame.draw.rect(ekran, V89_UI_PARCHMENT, tag, 1)
        yazi_yaz(label, tag.centerx, tag.centery, V89_UI_PARCHMENT, mini_font, True)
# </POTBO_STAGE S2104>

# <POTBO_STAGE S2106>


def v89_medieval_bar(rect, ratio, fill, label, trail=None, warning=False):
    rect = pygame.Rect(rect)
    ratio = v89_clamp01(ratio)
    trail = ratio if trail is None else v89_clamp01(trail)
    pygame.draw.rect(ekran, (3, 2, 2), rect.inflate(4, 4))
    pygame.draw.rect(ekran, (26, 18, 14), rect)
    if trail > ratio + 0.002:
        width = int(round(rect.width * trail))
        pygame.draw.rect(
            ekran,
            (71, 38, 34),
            pygame.Rect(rect.x, rect.y, width, rect.height),
        )
    width = int(round(rect.width * ratio))
    if width > 0:
        fill_rect = pygame.Rect(rect.x, rect.y, width, rect.height)
        pygame.draw.rect(ekran, fill, fill_rect)
        pygame.draw.line(
            ekran,
            tuple(min(255, value + 34) for value in fill),
            fill_rect.topleft,
            (fill_rect.right - 1, fill_rect.top),
            1,
        )
    border = (214, 53, 48) if warning else V89_UI_BRASS
    pygame.draw.rect(ekran, border, rect, 1)
    label_y = rect.y + max(0, (rect.height - mini_font.get_height()) // 2)
    yazi_yaz(label, rect.x + 5, label_y, (231, 213, 170), mini_font, False)


def oyuncu_paneli_ciz():
    panel = hud_sol_rect()
    v89_medieval_panel(panel, V89_UI_BLOOD)
    name = yazi_yaz(
        secili_karakter_adi(),
        panel.x + 20,
        panel.y + 16,
        (238, 226, 196),
        oyun_font,
    )
    yazi_yaz(
        f"{t('level')} {oyuncu_level}",
        min(panel.right - 180, name.right + 14),
        panel.y + 17,
        level_rengi(oyuncu_level),
        mini_font,
    )
    coin_x = panel.right - 72
    if _v79_coin_draw(coin_x, panel.y + 15, 20):
        coin_x += 25
    yazi_yaz(str(oyuncu_altin), coin_x, panel.y + 17, SARI, mini_font)

    displayed_hp = 0.0 if v85_mortal_wound_state.active else float(oyuncu_hp)
    hp_ratio = displayed_hp / max(1.0, float(oyuncu_max_hp))
    hp_trail = (0.0 if v85_mortal_wound_state.active else float(hp_gorunen)) / max(
        1.0, float(oyuncu_max_hp)
    )
    stamina_ratio = float(stamina_gorunen) / max(1.0, float(oyuncu_max_stamina))
    mana_ratio = float(mana_gorunen) / max(1.0, float(oyuncu_max_mana))
    x = panel.x + 22
    width = panel.width - 44
    v89_medieval_bar(
        pygame.Rect(x, panel.y + 56, width, 18),
        hp_ratio,
        (133, 6, 24),
        bt("CAN", "HEALTH"),
        trail=hp_trail,
    )
    v89_medieval_bar(
        pygame.Rect(x, panel.y + 84, width, 12),
        stamina_ratio,
        (183, 145, 42),
        bt("GÜÇ", "STAMINA"),
        warning=pygame.time.get_ticks() < stamina_uyari_bitis,
    )
    v89_medieval_bar(
        pygame.Rect(x, panel.y + 106, width, 16),
        mana_ratio,
        (30, 125, 139),
        bt("MANA", "MANA"),
        warning=pygame.time.get_ticks() < mana_uyari_bitis,
    )
# </POTBO_STAGE S2106>

# <POTBO_STAGE S2109>


def v89_inventory_action_menu(panel, item_index, source="grid"):
    actions = envanter_aksiyonlari(item_index, source)
    if not actions:
        return
    width = 400
    line_height = 42
    height = 72 + line_height * len(actions)
    rect = pygame.Rect(panel.centerx - width // 2, panel.centery - height // 2, width, height)
    v89_medieval_panel(rect, V89_UI_BLOOD, 252)
    yazi_yaz(
        bt("EŞYA EYLEMİ", "ITEM ACTION"),
        rect.centerx,
        rect.y + 27,
        V89_UI_PARCHMENT,
        normal_font,
        True,
    )
    for index, (_key, label) in enumerate(actions):
        row = pygame.Rect(rect.x + 30, rect.y + 54 + index * line_height, rect.width - 60, 34)
        selected = index == envanter_aksiyon_index % len(actions)
        pygame.draw.rect(ekran, (66, 34, 24) if selected else (28, 20, 16), row)
        pygame.draw.rect(ekran, V89_UI_BLOOD if selected else V89_UI_BRASS, row, 2 if selected else 1)
        yazi_yaz(label, row.centerx, row.centery, BEYAZ, kucuk_font, True)


def envanter_aksiyon_menusu_ciz(panel, item_index, kaynak="grid"):
    v89_inventory_action_menu(panel, item_index, kaynak)
# </POTBO_STAGE S2109>

# <POTBO_STAGE S2111>


def envanter_ciz():
    oyun_ekrani_ciz()
    koyu_kaplama(218)
    panel = pygame.Rect(62, 42, 1156, 636)
    v89_medieval_panel(panel, V89_UI_BLOOD, 252)
    yazi_yaz(
        bt("KARAKTER ENVANTERİ", "CHARACTER INVENTORY"),
        panel.centerx,
        panel.y + 32,
        V89_UI_PARCHMENT,
        menu_baslik_font,
        True,
    )

    grid_x = panel.x + 30
    grid_y = panel.y + 84
    slot_size = 68
    gap = 8
    for index in range(30):
        row, column = divmod(index, 6)
        rect = pygame.Rect(
            grid_x + column * (slot_size + gap),
            grid_y + row * (slot_size + gap),
            slot_size,
            slot_size,
        )
        slot_ciz(
            rect,
            secili=index == envanter_imlec,
            item_index=index,
            tasima_kaynagi=index == envanter_tasima_kaynagi,
        )

    info = pygame.Rect(panel.x + 518, panel.y + 82, 604, 456)
    pygame.draw.rect(ekran, (24, 17, 13), info)
    pygame.draw.rect(ekran, V89_UI_BRASS, info, 2)
    pygame.draw.rect(ekran, (78, 50, 30), info.inflate(-8, -8), 1)
    details = item_aciklamasi(envanter_imlec)
    item = (
        envanter_itemleri[envanter_imlec]
        if 0 <= envanter_imlec < len(envanter_itemleri)
        else None
    )
    icon_rect = pygame.Rect(info.right - 146, info.y + 24, 112, 112)
    if isinstance(item, dict):
        item_ikonu_ciz(item.get("id"), icon_rect, True)
    yazi_yaz(details.get("name", ""), info.x + 26, info.y + 28, BEYAZ, normal_font)
    category = str(details.get("category", details.get("type", "")))
    school = str(details.get("spell_school", ""))
    if school:
        category = f"{category} · {school}"
    yazi_yaz(category, info.x + 26, info.y + 67, V89_UI_PARCHMENT, kucuk_font)
    pygame.draw.line(
        ekran,
        V89_UI_BRASS,
        (info.x + 24, info.y + 151),
        (info.right - 24, info.y + 151),
        1,
    )
    description = metni_satirlara_bol(
        str(details.get("description", "")),
        mini_font,
        info.width - 52,
    )
    y = info.y + 176
    for line in description[:11]:
        yazi_yaz(line, info.x + 26, y, ACIK_GRI, mini_font)
        y += 22

    belt_y = panel.bottom - 84
    yazi_yaz(
        bt("KEMER  1–5  /  BÜYÜ  Q", "BELT  1–5  /  SPELL  Q"),
        grid_x,
        belt_y - 24,
        V89_UI_PARCHMENT,
        mini_font,
    )
    belt_slot = 58
    belt_gap = 11
    for index in range(5):
        rect = pygame.Rect(
            grid_x + index * (belt_slot + belt_gap),
            belt_y,
            belt_slot,
            belt_slot,
        )
        v85_slot_shell(
            rect,
            selected=index == envanter_secili_slot,
            transfer=index == one_cikan_tasima_kaynagi,
        )
        v85_slot_contents(rect, index + 1, one_cikan_slotlar[index])
    q_rect = pygame.Rect(
        grid_x + 5 * (belt_slot + belt_gap) + 12,
        belt_y,
        belt_slot,
        belt_slot,
    )
    v89_q_slot_draw(q_rect)

    if envanter_aksiyon_acik and envanter_aksiyon_item_index is not None:
        envanter_aksiyon_menusu_ciz(
            panel,
            envanter_aksiyon_item_index,
            envanter_aksiyon_kaynagi,
        )
    if one_cikan_atama_item_index is not None:
        one_cikan_atama_penceresi_ciz(panel)
# </POTBO_STAGE S2111>

# <POTBO_STAGE S2210>


# =========================================================
# END V90
# =========================================================


# =========================================================
# V91 - PIXEL HUD / COMPACT BLOOD / AUTHORED IGNIS VFX
# =========================================================

V91_VERSION = "91.0"
# </POTBO_STAGE S2210>

# <POTBO_STAGE S2212>

# The HUD reference is used only as a material/style vocabulary. Existing
# information, panels, slot count and layout stay untouched; no minimap or new
# screen region is introduced.
V91_UI_BLACK = (0, 0, 0)
V91_UI_INK = (9, 7, 9)
V91_UI_WHITE = (231, 232, 220)
V91_UI_GREY = (116, 112, 108)
V91_UI_RED = (151, 5, 27)
V91_UI_RED_HOT = (232, 28, 48)
V91_UI_GOLD = (226, 184, 66)
V91_UI_MANA = (42, 142, 187)
# </POTBO_STAGE S2212>

# <POTBO_STAGE S2214>

# Keep inherited call sites coherent with the new pixel palette.
V89_UI_IRON = V91_UI_GREY
V89_UI_IRON_DARK = V91_UI_BLACK
V89_UI_OAK = V91_UI_INK
V89_UI_OAK_LIGHT = (42, 35, 39)
V89_UI_BRASS = V91_UI_WHITE
V89_UI_BLOOD = V91_UI_RED
V89_UI_PARCHMENT = V91_UI_WHITE


def v91_pixel_corner_marks(surface, rect, accent):
    rect = pygame.Rect(rect)
    white = (*V91_UI_WHITE, 255)
    red = (*tuple(accent[:3]), 255)
    for x, y, sx, sy in (
        (rect.left + 3, rect.top + 3, 1, 1),
        (rect.right - 4, rect.top + 3, -1, 1),
        (rect.left + 3, rect.bottom - 4, 1, -1),
        (rect.right - 4, rect.bottom - 4, -1, -1),
    ):
        pygame.draw.line(surface, white, (x, y), (x + sx * 3, y), 1)
        pygame.draw.line(surface, white, (x, y), (x, y + sy * 3), 1)
        pygame.draw.rect(surface, red, (x + sx * 4 - 1, y + sy * 4 - 1, 2, 2))


def v89_medieval_panel(rect, accent=V91_UI_RED, alpha=248):
    """Sharp 8-bit plate inspired by the reference, preserving every rect."""
    rect = pygame.Rect(rect)
    layer = pygame.Surface(rect.size, pygame.SRCALPHA)
    opacity = max(0, min(255, int(alpha)))
    layer.fill((*V91_UI_BLACK, opacity))
    local = layer.get_rect()
    pygame.draw.rect(layer, (*V91_UI_WHITE, 255), local, 2)
    pygame.draw.rect(layer, (*tuple(accent[:3]), 255), local.inflate(-6, -6), 2)
    pygame.draw.line(
        layer,
        (*V91_UI_GREY, 255),
        (8, local.bottom - 5),
        (local.right - 9, local.bottom - 5),
        1,
    )
    v91_pixel_corner_marks(layer, local, accent)
    ekran.blit(layer, rect.topleft)


def v85_hud_panel_draw(rect, accent=V91_UI_RED):
    v89_medieval_panel(rect, accent=accent)


def v85_slot_shell(rect, selected=False, transfer=False, magic=False):
    rect = pygame.Rect(rect)
    outer = rect.inflate(4, 4)
    pygame.draw.rect(ekran, V91_UI_BLACK, outer)
    pygame.draw.rect(ekran, V91_UI_WHITE, rect, 2)
    pygame.draw.rect(ekran, V91_UI_BLACK, rect.inflate(-4, -4))
    pygame.draw.rect(ekran, (55, 45, 51), rect.inflate(-8, -8), 1)
    edge = V91_UI_GOLD if transfer else V91_UI_RED_HOT if selected else V91_UI_RED
    pygame.draw.rect(ekran, edge, rect.inflate(-3, -3), 2 if (selected or transfer) else 1)
    if magic:
        pygame.draw.rect(ekran, V91_UI_GOLD, (rect.right - 7, rect.top + 4, 3, 3))
        pygame.draw.rect(ekran, V91_UI_GOLD, (rect.left + 4, rect.bottom - 7, 3, 3))
    for point in ((rect.left + 3, rect.top + 3), (rect.right - 5, rect.bottom - 5)):
        pygame.draw.rect(ekran, V91_UI_WHITE, (*point, 2, 2))


def v85_slot_contents(rect, key_text=None, item_index=None):
    rect = pygame.Rect(rect)
    item = None
    if isinstance(item_index, int) and 0 <= item_index < len(envanter_itemleri):
        candidate = envanter_itemleri[item_index]
        if isinstance(candidate, dict):
            item = candidate
    if item is not None:
        # Tight alpha crop plus three pixels of breathing room makes every item
        # fit the authored slot instead of floating in a large modern inset.
        icon_area = rect.inflate(-6, -6)
        image = v89_tight_icon(item.get("id"), icon_area.size)
        if image is not None:
            ekran.blit(image, image.get_rect(center=icon_area.center))
        else:
            fallback = item_kisa_adi(item_index)[:5]
            yazi_yaz(
                fallback,
                rect.centerx,
                rect.centery,
                V91_UI_WHITE,
                mini_font,
                True,
            )
        count = item_adedi(item)
        if count > 1:
            badge = pygame.Rect(rect.right - 27, rect.bottom - 20, 23, 16)
            pygame.draw.rect(ekran, V91_UI_BLACK, badge)
            pygame.draw.rect(ekran, V91_UI_WHITE, badge, 1)
            yazi_yaz(
                f"x{count}", badge.centerx, badge.centery, V91_UI_WHITE, mini_font, True
            )
    if key_text is not None:
        label = str(key_text)
        width = max(18, mini_font.size(label)[0] + 8)
        tag = pygame.Rect(rect.x + 4, rect.y + 4, width, 17)
        pygame.draw.rect(ekran, V91_UI_BLACK, tag)
        pygame.draw.rect(ekran, V91_UI_WHITE, tag, 1)
        pygame.draw.line(ekran, V91_UI_RED, tag.bottomleft, tag.bottomright, 1)
        yazi_yaz(label, tag.centerx, tag.centery, V91_UI_WHITE, mini_font, True)


def item_ikonu_ciz(item_id, rect, cerceve=True):
    rect = pygame.Rect(rect)
    if cerceve:
        pygame.draw.rect(ekran, V91_UI_BLACK, rect)
        pygame.draw.rect(ekran, V91_UI_WHITE, rect, 2)
        pygame.draw.rect(ekran, V91_UI_RED, rect.inflate(-5, -5), 1)
    area = rect.inflate(-6 if cerceve else -2, -6 if cerceve else -2)
    image = v89_tight_icon(item_id, area.size)
    if image is None:
        return False
    ekran.blit(image, image.get_rect(center=area.center))
    return True


def v89_medieval_bar(rect, ratio, fill, label, trail=None, warning=False):
    """Reference-style discrete pixels instead of smooth modern fill bars."""
    rect = pygame.Rect(rect)
    ratio = v89_clamp01(ratio)
    trail = ratio if trail is None else v89_clamp01(trail)
    pygame.draw.rect(ekran, V91_UI_BLACK, rect.inflate(4, 4))
    pygame.draw.rect(ekran, V91_UI_WHITE if not warning else V91_UI_RED_HOT, rect, 1)
    label_w = min(58, max(42, mini_font.size(str(label))[0] + 9))
    yazi_yaz(
        str(label),
        rect.x + 4,
        rect.y + max(0, (rect.height - mini_font.get_height()) // 2),
        V91_UI_WHITE,
        mini_font,
        False,
    )
    area = pygame.Rect(
        rect.x + label_w,
        rect.y + 3,
        max(1, rect.width - label_w - 4),
        max(2, rect.height - 6),
    )
    count = max(6, min(18, area.width // 13))
    gap = 2
    seg_w = max(2, (area.width - gap * (count - 1)) // count)
    used_w = seg_w * count + gap * (count - 1)
    area.x += max(0, (area.width - used_w) // 2)
    trail_count = int(round(trail * count))
    fill_count = int(round(ratio * count))
    for index in range(count):
        segment = pygame.Rect(
            area.x + index * (seg_w + gap), area.y, seg_w, area.height
        )
        pygame.draw.rect(ekran, (31, 26, 30), segment)
        if index < trail_count:
            pygame.draw.rect(ekran, (79, 52, 55), segment.inflate(-1, -1))
        if index < fill_count:
            pygame.draw.rect(ekran, fill, segment.inflate(-1, -1))
        pygame.draw.rect(ekran, V91_UI_GREY, segment, 1)
# </POTBO_STAGE S2214>

# <POTBO_STAGE S2218>


def v91_find_inventory_item(item_id):
    for index, item in enumerate(envanter_itemleri):
        if isinstance(item, dict) and item.get("id") == item_id:
            return index
    return None
# </POTBO_STAGE S2218>

# <POTBO_STAGE S2263>


# ---------------------------------------------------------
# HUD: status + quick inventory become one continuous top band.
# ---------------------------------------------------------
def hud_sol_rect():
    return pygame.Rect(12, 10, 494, 150)


def hud_sag_rect():
    sol = hud_sol_rect()
    return pygame.Rect(sol.right, sol.y, GENISLIK - 12 - sol.right, sol.height)


def _v92_top_hud_outer_rect():
    left = hud_sol_rect()
    right = hud_sag_rect()
    return left.union(right)


def oyuncu_paneli_ciz():
    if oyuncu_hp <= 0:
        return
    outer = _v92_top_hud_outer_rect()
    left = hud_sol_rect()
    v89_medieval_panel(outer, V91_UI_RED, 250)
    pygame.draw.line(
        ekran,
        V91_UI_RED,
        (left.right, outer.y + 9),
        (left.right, outer.bottom - 9),
        2,
    )

    name_rect = yazi_yaz(
        secili_karakter_adi(),
        left.x + 18,
        left.y + 13,
        V91_UI_WHITE,
        oyun_font,
    )
    yazi_yaz(
        f"{t('level')} {oyuncu_level}",
        min(left.right - 150, name_rect.right + 12),
        left.y + 15,
        level_rengi(oyuncu_level),
        mini_font,
    )
    coin_x = left.right - 88
    if _v79_coin_draw(coin_x, left.y + 13, 19):
        coin_x += 23
    yazi_yaz(str(oyuncu_altin), coin_x, left.y + 15, V91_UI_GOLD, mini_font)

    displayed_hp = 0.0 if v85_mortal_wound_state.active else float(oyuncu_hp)
    hp_ratio = displayed_hp / max(1.0, float(oyuncu_max_hp))
    hp_trail = (0.0 if v85_mortal_wound_state.active else float(hp_gorunen)) / max(
        1.0, float(oyuncu_max_hp)
    )
    stamina_ratio = float(stamina_gorunen) / max(1.0, float(oyuncu_max_stamina))
    mana_ratio = float(mana_gorunen) / max(1.0, float(oyuncu_max_mana))
    x = left.x + 18
    width = left.width - 36
    v89_medieval_bar(
        pygame.Rect(x, left.y + 50, width, 17),
        hp_ratio,
        (126, 5, 23),
        bt("CAN", "HEALTH"),
        trail=hp_trail,
    )
    v89_medieval_bar(
        pygame.Rect(x, left.y + 79, width, 12),
        stamina_ratio,
        (184, 149, 47),
        bt("DAYANIKLILIK", "STAMINA"),
        warning=pygame.time.get_ticks() < stamina_uyari_bitis,
    )
    v89_medieval_bar(
        pygame.Rect(x, left.y + 103, width, 15),
        mana_ratio,
        (28, 120, 154),
        "MANA",
        warning=pygame.time.get_ticks() < mana_uyari_bitis,
    )
    severity = v90_injury_severity()
    if severity >= 0.22:
        label = (
            bt("KRİTİK · KANAMA", "CRITICAL · BLEEDING")
            if v90_hp_ratio() <= 0.20
            else bt("AĞIR YARALI", "SEVERELY WOUNDED")
            if severity >= 0.52
            else bt("YARALI", "WOUNDED")
        )
        color = V91_UI_RED_HOT if severity >= 0.52 else V91_UI_GOLD
        yazi_yaz(label, left.right - 18, left.bottom - 19, color, mini_font, False)
# </POTBO_STAGE S2263>

# <POTBO_STAGE S2265>


# ---------------------------------------------------------
# Inventory: two equal visual halves and a centered belt.
# ---------------------------------------------------------
def envanter_ciz():
    oyun_ekrani_ciz()
    koyu_kaplama(220)
    panel = pygame.Rect(48, 36, GENISLIK - 96, YUKSEKLIK - 72)
    v89_medieval_panel(panel, V91_UI_RED, 252)
    yazi_yaz(
        bt("KARAKTER ENVANTERİ", "CHARACTER INVENTORY"),
        panel.centerx,
        panel.y + 29,
        V91_UI_WHITE,
        menu_baslik_font,
        True,
    )
    content_top = panel.y + 74
    content_bottom = panel.bottom - 112
    center_gap = 24
    half_w = (panel.width - 72 - center_gap) // 2
    left = pygame.Rect(panel.x + 30, content_top, half_w, content_bottom - content_top)
    right = pygame.Rect(left.right + center_gap, content_top, half_w, content_bottom - content_top)
    pygame.draw.rect(ekran, V91_UI_BLACK, left)
    pygame.draw.rect(ekran, V91_UI_GREY, left, 1)
    pygame.draw.rect(ekran, V91_UI_BLACK, right)
    pygame.draw.rect(ekran, V91_UI_GREY, right, 1)

    slot_size = 66
    gap = 8
    grid_w = slot_size * 6 + gap * 5
    grid_h = slot_size * 5 + gap * 4
    grid_x = left.centerx - grid_w // 2
    grid_y = left.centery - grid_h // 2
    for index in range(30):
        row, column = divmod(index, 6)
        rect = pygame.Rect(
            grid_x + column * (slot_size + gap),
            grid_y + row * (slot_size + gap),
            slot_size,
            slot_size,
        )
        slot_ciz(
            rect,
            secili=index == envanter_imlec,
            item_index=index,
            tasima_kaynagi=index == envanter_tasima_kaynagi,
        )

    details = item_aciklamasi(envanter_imlec)
    item = (
        envanter_itemleri[envanter_imlec]
        if 0 <= envanter_imlec < len(envanter_itemleri)
        else None
    )
    icon = pygame.Rect(right.centerx - 58, right.y + 22, 116, 116)
    if isinstance(item, dict):
        item_ikonu_ciz(item.get("id"), icon, True)
    yazi_yaz(
        details.get("name", ""),
        right.centerx,
        icon.bottom + 24,
        V91_UI_WHITE,
        normal_font,
        True,
    )
    category = str(details.get("category", details.get("type", "")))
    school = str(details.get("spell_school", ""))
    if school:
        category = f"{category} · {school}"
    yazi_yaz(category, right.centerx, icon.bottom + 53, V91_UI_GREY, mini_font, True)
    pygame.draw.line(
        ekran,
        V91_UI_RED,
        (right.x + 26, icon.bottom + 78),
        (right.right - 26, icon.bottom + 78),
        1,
    )
    lines = metni_satirlara_bol(
        str(details.get("description", "")), mini_font, right.width - 62
    )
    y = icon.bottom + 101
    for line in lines[:9]:
        yazi_yaz(line, right.x + 31, y, ACIK_GRI, mini_font)
        y += 21

    belt_slot = 58
    belt_gap = 13
    separator = 24
    belt_total = belt_slot * 6 + belt_gap * 4 + separator
    belt_x = panel.centerx - belt_total // 2
    belt_y = panel.bottom - 80
    for index in range(5):
        rect = pygame.Rect(
            belt_x + index * (belt_slot + belt_gap), belt_y, belt_slot, belt_slot
        )
        v85_slot_shell(
            rect,
            selected=index == envanter_secili_slot,
            transfer=index == one_cikan_tasima_kaynagi,
        )
        v85_slot_contents(rect, index + 1, one_cikan_slotlar[index])
    q_rect = pygame.Rect(
        belt_x + belt_slot * 5 + belt_gap * 4 + separator,
        belt_y,
        belt_slot,
        belt_slot,
    )
    v89_q_slot_draw(q_rect)

    if envanter_aksiyon_acik and envanter_aksiyon_item_index is not None:
        envanter_aksiyon_menusu_ciz(
            panel,
            envanter_aksiyon_item_index,
            envanter_aksiyon_kaynagi,
        )
    if one_cikan_atama_item_index is not None:
        one_cikan_atama_penceresi_ciz(panel)
# </POTBO_STAGE S2265>

# <POTBO_STAGE S2341>

# UI timing: a click should read physically, but never feel like a lock.
V37_UI_ACTION_DELAY_MS = 92
V37_UI_INPUT_GUARD_MS = 105
# </POTBO_STAGE S2341>

# <POTBO_STAGE S2343>
UI_BUTON_CLICK_SURE_MS = 105


def v37_ui_action_schedule(action, label="ui", delay_ms=None):
    """V94 responsive menu scheduling; one click, one short readable press."""
    global v37_ui_pending_action, v37_ui_pending_due, v37_ui_pending_label
    if action is None or v37_ui_pending_action is not None:
        return False
    now = pygame.time.get_ticks()
    delay = V37_UI_ACTION_DELAY_MS if delay_ms is None else max(1, int(delay_ms))
    v37_ui_pending_action = action
    v37_ui_pending_due = int(now) + int(delay)
    v37_ui_pending_label = str(label)
    return True
# </POTBO_STAGE S2343>

# <POTBO_STAGE S2346>


# ---------------------------------------------------------
# Main menu: cache the static glow instead of allocating a 520x720 alpha surface
# every frame.
# ---------------------------------------------------------
v94_menu_glow = pygame.Surface((520, YUKSEKLIK), pygame.SRCALPHA).convert_alpha()
v94_menu_glow.fill((0, 0, 0, 0))
for _width, _alpha in ((520, 22), (410, 18), (300, 14)):
    pygame.draw.ellipse(
        v94_menu_glow,
        (95, 0, 18, _alpha),
        ((520 - _width) // 2, 40, _width, 620),
    )


def ana_menu_ciz():
    ekran.fill(SIYAH)
    ekran.blit(v94_menu_glow, (GENISLIK // 2 - 260, 0))
    yazi_yaz("PATH OF THE", GENISLIK // 2 + 4, 92, (40, 0, 5), baslik_font, True)
    yazi_yaz("PATH OF THE", GENISLIK // 2, 87, BEYAZ, baslik_font, True)
    yazi_yaz("BLOODIED ONE", GENISLIK // 2 + 4, 163, (40, 0, 5), baslik_font, True)
    yazi_yaz("BLOODIED ONE", GENISLIK // 2, 158, PARLAK_KIRMIZI, baslik_font, True)
    yazi_yaz(t("subtitle"), GENISLIK // 2, 226, ACIK_GRI, kucuk_font, True)
    for index, secenek in enumerate(menu_secenekleri()):
        rect = menu_rect(index)
        secili = index == menu_index
        menu_susleme_ciz(rect, secili)
        yazi_yaz(
            secenek,
            rect.centerx,
            rect.centery,
            BEYAZ if secili else (155, 145, 150),
            menu_font if secili else normal_font,
            True,
        )
    if menu_mesaji:
        yazi_yaz(menu_mesaji, GENISLIK // 2, 688, PARLAK_KIRMIZI, kucuk_font, True)
# </POTBO_STAGE S2346>

# <POTBO_STAGE S2358>


# ---------------------------------------------------------
# Compact status symbols. PNG icons can replace these later without changing bar
# geometry.
# ---------------------------------------------------------
def oyuncu_paneli_ciz():
    if oyuncu_hp <= 0:
        return
    outer = _v92_top_hud_outer_rect()
    left = hud_sol_rect()
    v89_medieval_panel(outer, V91_UI_RED, 250)
    pygame.draw.line(ekran, V91_UI_RED, (left.right, outer.y + 9), (left.right, outer.bottom - 9), 2)
    name_rect = yazi_yaz(secili_karakter_adi(), left.x + 18, left.y + 13, V91_UI_WHITE, oyun_font)
    yazi_yaz(bt(f"Sv {oyuncu_level}", f"Lv {oyuncu_level}"), min(left.right - 150, name_rect.right + 12), left.y + 15, level_rengi(oyuncu_level), mini_font)
    coin_x = left.right - 88
    if _v79_coin_draw(coin_x, left.y + 13, 19):
        coin_x += 23
    yazi_yaz(str(oyuncu_altin), coin_x, left.y + 15, V91_UI_GOLD, mini_font)
    displayed_hp = 0.0 if v85_mortal_wound_state.active else float(oyuncu_hp)
    hp_ratio = displayed_hp / max(1.0, float(oyuncu_max_hp))
    hp_trail = (0.0 if v85_mortal_wound_state.active else float(hp_gorunen)) / max(1.0, float(oyuncu_max_hp))
    stamina_ratio = float(stamina_gorunen) / max(1.0, float(oyuncu_max_stamina))
    mana_ratio = float(mana_gorunen) / max(1.0, float(oyuncu_max_mana))
    x = left.x + 18
    width = left.width - 36
    v89_medieval_bar(pygame.Rect(x, left.y + 50, width, 17), hp_ratio, (126, 5, 23), "♥", trail=hp_trail)
    v89_medieval_bar(pygame.Rect(x, left.y + 79, width, 12), stamina_ratio, (184, 149, 47), "◈", warning=pygame.time.get_ticks() < stamina_uyari_bitis)
    v89_medieval_bar(pygame.Rect(x, left.y + 103, width, 15), mana_ratio, (28, 120, 154), "✦", warning=pygame.time.get_ticks() < mana_uyari_bitis)
    severity = v90_injury_severity()
    if severity >= 0.22:
        label = bt("KRİTİK · KANAMA", "CRITICAL · BLEEDING") if v90_hp_ratio() <= 0.20 else bt("AĞIR YARALI", "SEVERELY WOUNDED") if severity >= 0.52 else bt("YARALI", "WOUNDED")
        yazi_yaz(label, left.right - 18, left.bottom - 19, V91_UI_RED_HOT if severity >= 0.52 else V91_UI_GOLD, mini_font, False)
# </POTBO_STAGE S2358>

# <POTBO_STAGE S2368>


def oyuncu_olum_sahnesi_ciz():
    _v94_death_scene_previous()
    if not v86_death_state.active or oyuncu_olum_baslangic_ms <= 0:
        return
    now = pygame.time.get_ticks()
    if oyuncu_olum_cikis_orani(now) >= 0.52:
        return
    v85_death_menu_draw(now)
# </POTBO_STAGE S2368>

# <POTBO_STAGE S2373>

# Restore the deliberate original UI rhythm. Performance work must never alter
# menu/interaction timing.
V37_UI_ACTION_DELAY_MS = 150
V37_UI_INPUT_GUARD_MS = 165
# </POTBO_STAGE S2373>

# <POTBO_STAGE S2375>
UI_BUTON_CLICK_SURE_MS = 140
# </POTBO_STAGE S2375>

# <POTBO_STAGE S2403>


# ---------------------------------------------------------
# Dialogue strips: names live here, not in the top header.
# ---------------------------------------------------------
def _v97_dialogue_box(panel):
    return pygame.Rect(panel.x + 24, panel.bottom - 190, panel.width - 48, 154)
# </POTBO_STAGE S2403>

# <POTBO_STAGE S2416>


# =========================================================
# END V97
# =========================================================


# =========================================================
# V98 - STATUS ICONS / REINALD WORLD INTEGRATION /
# UNIVERSAL GROUND FIRE + FIREBALL TRAIL
# =========================================================
# Bu katman dosyanın en sonunda tanımlanır; böylece önceki HUD/world/fire
# override'larının tamamından sonra canonical davranış olur.

V98_VERSION = "98.0"
# </POTBO_STAGE S2416>

# <POTBO_STAGE S2423>


def _v98_status_bar(rect, ratio, fill, trail=None, warning=False):
    """V91 segment dilini korur fakat barın içinde yazı/sembol bırakmaz."""
    rect = pygame.Rect(rect)
    ratio = v89_clamp01(ratio)
    trail = ratio if trail is None else v89_clamp01(trail)

    pygame.draw.rect(ekran, V91_UI_BLACK, rect.inflate(4, 4))
    pygame.draw.rect(
        ekran,
        V91_UI_RED_HOT if warning else V91_UI_WHITE,
        rect,
        1,
    )

    area = pygame.Rect(
        rect.x + 4,
        rect.y + 3,
        max(1, rect.width - 8),
        max(2, rect.height - 6),
    )
    count = max(8, min(20, area.width // 13))
    gap = 2
    seg_w = max(2, (area.width - gap * (count - 1)) // count)
    used_w = seg_w * count + gap * (count - 1)
    area.x += max(0, (area.width - used_w) // 2)

    trail_count = int(round(trail * count))
    fill_count = int(round(ratio * count))
    for index in range(count):
        segment = pygame.Rect(
            area.x + index * (seg_w + gap),
            area.y,
            seg_w,
            area.height,
        )
        pygame.draw.rect(ekran, (31, 26, 30), segment)
        if index < trail_count:
            pygame.draw.rect(ekran, (79, 52, 55), segment.inflate(-1, -1))
        if index < fill_count:
            pygame.draw.rect(ekran, fill, segment.inflate(-1, -1))
        pygame.draw.rect(ekran, V91_UI_GREY, segment, 1)


def _v98_status_row(panel, y, height, ratio, fill, icon, trail=None, warning=False):
    icon_size = 18 if height >= 16 else 16
    icon_box = pygame.Rect(panel.x + 17, y - 2, 22, max(20, height + 4))
    image = _v98_status_icon_scaled(icon, icon_size)
    if image is not None:
        ekran.blit(image, image.get_rect(center=icon_box.center))
    else:
        # Asset eksikse bar geometrisi bozulmaz; yalnız sade bir işaret kullanılır.
        pygame.draw.rect(ekran, V91_UI_GREY, icon_box.inflate(-8, -8), 1)

    bar_x = icon_box.right + 5
    bar = pygame.Rect(
        bar_x,
        y,
        max(40, panel.right - 18 - bar_x),
        height,
    )
    _v98_status_bar(bar, ratio, fill, trail=trail, warning=warning)
    return bar


def oyuncu_paneli_ciz():
    if oyuncu_hp <= 0:
        return

    outer = _v92_top_hud_outer_rect()
    left = hud_sol_rect()
    v89_medieval_panel(outer, V91_UI_RED, 250)
    pygame.draw.line(
        ekran,
        V91_UI_RED,
        (left.right, outer.y + 9),
        (left.right, outer.bottom - 9),
        2,
    )

    name_rect = yazi_yaz(
        secili_karakter_adi(),
        left.x + 18,
        left.y + 13,
        V91_UI_WHITE,
        oyun_font,
    )
    yazi_yaz(
        f"{t('level')} {oyuncu_level}",
        min(left.right - 150, name_rect.right + 12),
        left.y + 15,
        level_rengi(oyuncu_level),
        mini_font,
    )

    coin_x = left.right - 88
    if _v79_coin_draw(coin_x, left.y + 13, 19):
        coin_x += 23
    yazi_yaz(str(oyuncu_altin), coin_x, left.y + 15, V91_UI_GOLD, mini_font)

    displayed_hp = 0.0 if v85_mortal_wound_state.active else float(oyuncu_hp)
    hp_ratio = displayed_hp / max(1.0, float(oyuncu_max_hp))
    hp_trail = (
        0.0 if v85_mortal_wound_state.active else float(hp_gorunen)
    ) / max(1.0, float(oyuncu_max_hp))
    stamina_ratio = float(stamina_gorunen) / max(1.0, float(oyuncu_max_stamina))
    mana_ratio = float(mana_gorunen) / max(1.0, float(oyuncu_max_mana))
    now = pygame.time.get_ticks()

    hp_bar = _v98_status_row(
        left,
        left.y + 50,
        17,
        hp_ratio,
        (126, 5, 23),
        V98_HEALTH_ICON,
        trail=hp_trail,
    )
    stamina_bar = _v98_status_row(
        left,
        left.y + 79,
        12,
        stamina_ratio,
        (184, 149, 47),
        V98_STAMINA_ICON,
        warning=now < stamina_uyari_bitis,
    )
    _v98_status_row(
        left,
        left.y + 103,
        15,
        mana_ratio,
        (28, 120, 154),
        V98_MANA_ICON,
        warning=now < mana_uyari_bitis,
    )

    # Injury sistemi stamina'nın erişilebilir kapasitesini bar üzerinde korur.
    if "v90_injury" in globals():
        effective = max(0.0, min(1.0, float(v90_injury.effective_stamina_ratio)))
        cap_x = stamina_bar.x + int(round(stamina_bar.width * effective))
        pygame.draw.line(
            ekran,
            V91_UI_BLACK,
            (cap_x, stamina_bar.y - 2),
            (cap_x, stamina_bar.bottom + 2),
            4,
        )
        pygame.draw.line(
            ekran,
            V91_UI_WHITE,
            (cap_x, stamina_bar.y - 2),
            (cap_x, stamina_bar.bottom + 2),
            1,
        )

    severity = v90_injury_severity()
    if severity >= 0.22:
        label = (
            bt("KRİTİK · KANAMA", "CRITICAL · BLEEDING")
            if v90_hp_ratio() <= 0.20
            else bt("AĞIR YARALI", "SEVERELY WOUNDED")
            if severity >= 0.52
            else bt("YARALI", "WOUNDED")
        )
        yazi_yaz(
            label,
            left.right - 18,
            left.bottom - 19,
            V91_UI_RED_HOT if severity >= 0.52 else V91_UI_GOLD,
            mini_font,
            False,
        )
# </POTBO_STAGE S2423>

# <POTBO_STAGE S2437>

V99_COMMON_HINTS_EN = [
    "E is only for world interaction: talking to NPCs, picking up objects and advancing dialogue. Use ENTER or SPACE to confirm menus.",
    "Keys 1-5 select the featured inventory slot; F uses the selected slot. Q is a separate quick item or spell slot.",
    "Spells can only be cast from the Q quick slot. Check which spell is assigned before entering a fight.",
    "Save with F5 while you are safe. Saving after a difficult fight, purchase or major upgrade prevents unnecessary progress loss.",
    "Stamina is not only for attacks; dashing, guarding and heavy techniques use the same resource. Emptying the bar removes your escape options.",
    "Injuries reduce usable stamina capacity and recovery. The capacity marker on the stamina bar shows your current effective limit.",
    "When health becomes critical, slow your attack rhythm. Severe wounds directly weaken movement, stamina economy and combat tempo.",
    "Guard with K. Guarding close to the incoming hit is more economical than holding block continuously and leaves a better counter window.",
    "A normal dash needs SHIFT plus a movement direction. Time it to leave an attack line rather than using it only to gain distance.",
    "When an enemy shows an attack startup, do not immediately trade into it. Reading the startup and stepping aside is often safer than blocking.",
    "Do not throw long attack chains into armored targets. One clean contact is worth more than several swings into empty space.",
    "Berserkers can close distance with short dashes. Move diagonally instead of retreating in a straight line.",
    "Do not run straight at ranged enemies. Small direction changes make it harder for projectiles to lead you.",
    "In a crowd, prioritize the nearest attack-ready threat instead of automatically chasing the lowest-health target. Space is a resource.",
    "Sphaera Exothermica is strongest near the center of the blast. Use the outer area to create space and the core when you need a decisive hit.",
    "The fire left at a Sphaera Exothermica impact can hurt you too. Do not place the blast on your own escape route.",
    "Draco Calcinans focuses on one target, catches and coils around it, then applies intense heat. Use it to pressure an important target, not for crowd control.",
    "Pressing Q repeatedly does not restore mana. Reposition and return to melee or defense while waiting for your spell economy to recover.",
    "Do not assume Hanus's first number is honest. Persuasion can lower prices, and Hanus may try to turn the agreement back in his favor.",
    "Reinald does not sell ordinary items; he teaches techniques and applies permanent upgrades. Spend gold on the resource that actually limits you.",
    "Decussatio Rubra unlocks after five training sessions with Reinald. Hold J and use R to prepare the technique.",
    "Catena Decollationis unlocks after five training sessions. With at least two chainable targets ahead, hold J and press SHIFT; no movement key is required.",
    "Do not release J too quickly when using Catena. The combination becomes available after the heavy-attack charge threshold.",
    "Catena searches in the direction you are facing. If it does not start, face the target first, then use J + SHIFT.",
    "Choose your direction before committing to a heavy attack. Once the release begins, the move cannot make a sharp last-second turn.",
    "Knocking enemies into fire is useful, but the same fire can damage you. Re-read the ground immediately after an explosion.",
    "Bloody areas can influence the behavior of small creatures over time. Returning to an old battlefield may reveal a changed local ecology.",
    "Open the inventory with TAB. Arrange your 1-5 and Q slots before entering danger instead of searching for items during combat.",
    "Guarding, dashing and magic all belong to the same combat economy. A combination that empties every resource can leave you defenseless afterward.",
    "An enemy can remain dangerous until its action fully resolves. Watch body motion as well as HP before assuming the threat is over.",
]
# </POTBO_STAGE S2437>

# <POTBO_STAGE S2454>
V101_UI_PATCH_VERSION = "101.0"
# </POTBO_STAGE S2454>

# <POTBO_STAGE S2456>


def _v101_skill_icon_reload(skill_id):
    """İkon oyun açılırken bulunmadıysa çalışma anında tekrar ara.

    Böylece aynı ikon yüzeyi hem envanter skill belt'inde hem de Reinald'ın
    YETENEK ekranında kullanılır. Dosya sonradan doğru klasöre eklense bile
    UI harf placeholder'ına düşmez.
    """
    meta = V100_SKILL_META.get(skill_id, {})
    image = _v100_skill_image_load(meta.get("paths", ()))
    if image is not None:
        V100_SKILL_ICONS[skill_id] = image
    return image
# </POTBO_STAGE S2456>

# <POTBO_STAGE S2458>


def v100_skill_icon_draw(skill_id, rect, alpha=255):
    rect = pygame.Rect(rect)
    image = V100_SKILL_ICONS.get(skill_id)
    if image is None:
        image = _v101_skill_icon_reload(skill_id)

    if image is not None:
        fitted = resmi_oranli_sigdir(image, rect, 0, 0.90, True)
        if fitted is not None:
            if alpha < 255:
                fitted = fitted.copy()
                fitted.set_alpha(max(0, min(255, int(alpha))))
            ekran.blit(fitted, fitted.get_rect(center=rect.center))
            return True

    # Harf placeholder kullanma; Reinald ve envanter aynı grafik fallback'i görür.
    fallback = _v101_skill_fallback_surface(skill_id, min(rect.width, rect.height))
    if alpha < 255:
        fallback.set_alpha(max(0, min(255, int(alpha))))
    ekran.blit(fallback, fallback.get_rect(center=rect.center))
    return False
# </POTBO_STAGE S2458>

# <POTBO_STAGE S2460>


def _v100_draw_row_name(text, x, y, max_width):
    font = oyun_kucuk_font
    if font.size(str(text))[0] > max_width:
        font = mini_font
    yazi_yaz(str(text), x, y, V91_UI_WHITE, font)
# </POTBO_STAGE S2460>

# <POTBO_STAGE S2463>


def envanter_ciz():
    oyun_ekrani_ciz()
    koyu_kaplama(220)
    panel = pygame.Rect(48, 36, GENISLIK - 96, YUKSEKLIK - 72)
    v89_medieval_panel(panel, V91_UI_RED, 252)
    yazi_yaz(
        bt("KARAKTER ENVANTERİ", "CHARACTER INVENTORY"),
        panel.centerx,
        panel.y + 29,
        V91_UI_WHITE,
        menu_baslik_font,
        True,
    )
    content_top = panel.y + 74
    content_bottom = panel.bottom - 112
    center_gap = 24
    half_w = (panel.width - 72 - center_gap) // 2
    left = pygame.Rect(panel.x + 30, content_top, half_w, content_bottom - content_top)
    right = pygame.Rect(left.right + center_gap, content_top, half_w, content_bottom - content_top)
    pygame.draw.rect(ekran, V91_UI_BLACK, left)
    pygame.draw.rect(ekran, V91_UI_GREY, left, 1)
    pygame.draw.rect(ekran, V91_UI_BLACK, right)
    pygame.draw.rect(ekran, V91_UI_GREY, right, 1)

    slot_size = 66
    gap = 8
    grid_w = slot_size * 6 + gap * 5
    grid_h = slot_size * 5 + gap * 4
    grid_x = left.centerx - grid_w // 2
    grid_y = left.centery - grid_h // 2
    for index in range(30):
        row, column = divmod(index, 6)
        rect = pygame.Rect(
            grid_x + column * (slot_size + gap),
            grid_y + row * (slot_size + gap),
            slot_size,
            slot_size,
        )
        slot_ciz(
            rect,
            secili=index == envanter_imlec,
            item_index=index,
            tasima_kaynagi=index == envanter_tasima_kaynagi,
        )

    details = item_aciklamasi(envanter_imlec)
    item = envanter_itemleri[envanter_imlec] if 0 <= envanter_imlec < len(envanter_itemleri) else None
    icon = pygame.Rect(right.centerx - 58, right.y + 22, 116, 116)
    if isinstance(item, dict):
        item_ikonu_ciz(item.get("id"), icon, True)
    yazi_yaz(details.get("name", ""), right.centerx, icon.bottom + 24, V91_UI_WHITE, normal_font, True)
    category = str(details.get("category", details.get("type", "")))
    school = str(details.get("spell_school", ""))
    if school:
        category = f"{category} · {school}"
    yazi_yaz(category, right.centerx, icon.bottom + 53, V91_UI_GREY, mini_font, True)
    pygame.draw.line(
        ekran,
        V91_UI_RED,
        (right.x + 26, icon.bottom + 78),
        (right.right - 26, icon.bottom + 78),
        1,
    )
    lines = metni_satirlara_bol(str(details.get("description", "")), mini_font, right.width - 62)
    y = icon.bottom + 101
    for line in lines[:9]:
        yazi_yaz(line, right.x + 31, y, ACIK_GRI, mini_font)
        y += 21

    # Alt kemer slotları üstteki 30 envanter slotuyla aynı ölçekte tutulur.
    # Tasarım değişmez; yalnız 58 px'lik küçük sürüm yerine 66 px kullanılır ve
    # bütün 1-5 + Q / skill grubu panel merkezine simetrik yayılır.
    belt_slot = slot_size  # 66 px: 30'lu grid ile birebir aynı slot boyutu
    item_gap = gap         # 8 px: üst grid ile aynı ritim
    item_separator = 22
    item_group_w = belt_slot * 6 + item_gap * 4 + item_separator
    skill_gap = gap
    skill_group_w = belt_slot * 5 + skill_gap * 4
    group_gap = 38
    total_w = item_group_w + group_gap + skill_group_w
    belt_x = panel.centerx - total_w // 2
    belt_y = panel.bottom - belt_slot - 18

    for index in range(5):
        rect = pygame.Rect(
            belt_x + index * (belt_slot + item_gap),
            belt_y,
            belt_slot,
            belt_slot,
        )
        v85_slot_shell(
            rect,
            selected=index == envanter_secili_slot,
            transfer=index == one_cikan_tasima_kaynagi,
        )
        v85_slot_contents(rect, index + 1, one_cikan_slotlar[index])

    q_rect = pygame.Rect(
        belt_x + belt_slot * 5 + item_gap * 4 + item_separator,
        belt_y,
        belt_slot,
        belt_slot,
    )
    v89_q_slot_draw(q_rect)

    divider_x = belt_x + item_group_w + group_gap // 2
    pygame.draw.line(
        ekran,
        V91_UI_GREY,
        (divider_x, belt_y - 4),
        (divider_x, belt_y + belt_slot + 4),
        1,
    )
    v100_skill_belt_draw(belt_x + item_group_w + group_gap, belt_y, belt_slot, skill_gap)

    if envanter_aksiyon_acik and envanter_aksiyon_item_index is not None:
        envanter_aksiyon_menusu_ciz(panel, envanter_aksiyon_item_index, envanter_aksiyon_kaynagi)
    if one_cikan_atama_item_index is not None:
        one_cikan_atama_penceresi_ciz(panel)
# </POTBO_STAGE S2463>

# <POTBO_STAGE S2483>


# Skill ikonları için ui/skills zorunlu değildir. Kullanıcı PNG'yi doğrudan
# assets/ui içine koyarsa da aynı ikon hem Reinald'da hem envanter skill belt'inde görünür.
V102_SKILL_PATH_EXTRAS = {
    "decussatio_rubra": (
        os.path.join(ASSETS, "ui", "decussatio_rubra.png"),
        os.path.join(ASSETS, "ui", "skills", "decussatio_rubra.png"),
        os.path.join(ASSETS, "skills", "decussatio_rubra.png"),
        os.path.join(BASE_DIR, "decussatio_rubra.png"),
    ),
    "catena_decollationis": (
        os.path.join(ASSETS, "ui", "catena_decollationis.png"),
        os.path.join(ASSETS, "ui", "skills", "catena_decollationis.png"),
        os.path.join(ASSETS, "skills", "catena_decollationis.png"),
        os.path.join(BASE_DIR, "catena_decollationis.png"),
    ),
}
# </POTBO_STAGE S2483>

# <POTBO_STAGE S2490>


# ---------------------------------------------------------
# INVENTORY BELT FINAL ALIGNMENT
# 1-5 + Q tam olarak sol 6x5 grid'in kolonlarına oturur.
# Skill belt sağ bilgi kutusunun tam merkezindedir.
# İki dikey ayraç üstteki iki ana kutunun iç kenarlarıyla birebir hizalıdır.
# ---------------------------------------------------------
def envanter_ciz():
    oyun_ekrani_ciz()
    koyu_kaplama(220)
    panel = pygame.Rect(48, 36, GENISLIK - 96, YUKSEKLIK - 72)
    v89_medieval_panel(panel, V91_UI_RED, 252)
    yazi_yaz(
        bt("KARAKTER ENVANTERİ", "CHARACTER INVENTORY"),
        panel.centerx,
        panel.y + 29,
        V91_UI_WHITE,
        menu_baslik_font,
        True,
    )

    content_top = panel.y + 74
    content_bottom = panel.bottom - 112
    center_gap = 24
    half_w = (panel.width - 72 - center_gap) // 2
    left = pygame.Rect(panel.x + 30, content_top, half_w, content_bottom - content_top)
    right = pygame.Rect(left.right + center_gap, content_top, half_w, content_bottom - content_top)

    pygame.draw.rect(ekran, V91_UI_BLACK, left)
    pygame.draw.rect(ekran, V91_UI_GREY, left, 1)
    pygame.draw.rect(ekran, V91_UI_BLACK, right)
    pygame.draw.rect(ekran, V91_UI_GREY, right, 1)

    slot_size = 66
    gap = 8
    grid_w = slot_size * 6 + gap * 5
    grid_h = slot_size * 5 + gap * 4
    grid_x = left.centerx - grid_w // 2
    grid_y = left.centery - grid_h // 2

    for index in range(30):
        row, column = divmod(index, 6)
        rect = pygame.Rect(
            grid_x + column * (slot_size + gap),
            grid_y + row * (slot_size + gap),
            slot_size,
            slot_size,
        )
        slot_ciz(
            rect,
            secili=index == envanter_imlec,
            item_index=index,
            tasima_kaynagi=index == envanter_tasima_kaynagi,
        )

    details = item_aciklamasi(envanter_imlec)
    item = envanter_itemleri[envanter_imlec] if 0 <= envanter_imlec < len(envanter_itemleri) else None
    icon = pygame.Rect(right.centerx - 58, right.y + 22, 116, 116)
    if isinstance(item, dict):
        item_ikonu_ciz(item.get("id"), icon, True)

    yazi_yaz(details.get("name", ""), right.centerx, icon.bottom + 24, V91_UI_WHITE, normal_font, True)
    category = str(details.get("category", details.get("type", "")))
    school = str(details.get("spell_school", ""))
    if school:
        category = f"{category} · {school}"
    yazi_yaz(category, right.centerx, icon.bottom + 53, V91_UI_GREY, mini_font, True)

    pygame.draw.line(
        ekran,
        V91_UI_RED,
        (right.x + 26, icon.bottom + 78),
        (right.right - 26, icon.bottom + 78),
        1,
    )

    lines = metni_satirlara_bol(str(details.get("description", "")), mini_font, right.width - 62)
    y = icon.bottom + 101
    for line in lines[:9]:
        yazi_yaz(line, right.x + 31, y, ACIK_GRI, mini_font)
        y += 21

    # Alt slotlar üst grid ile aynı boyut ve aynı yatay kolon ritmini kullanır.
    belt_slot = slot_size
    belt_gap = gap
    belt_y = panel.bottom - belt_slot - 18

    # SOL: 1-5 ve Q, üstteki 6 kolonun TAM ALTINA oturur.
    quick_x = grid_x
    for index in range(5):
        rect = pygame.Rect(
            quick_x + index * (belt_slot + belt_gap),
            belt_y,
            belt_slot,
            belt_slot,
        )
        v85_slot_shell(
            rect,
            selected=index == envanter_secili_slot,
            transfer=index == one_cikan_tasima_kaynagi,
        )
        v85_slot_contents(rect, index + 1, one_cikan_slotlar[index])

    q_rect = pygame.Rect(
        quick_x + 5 * (belt_slot + belt_gap),
        belt_y,
        belt_slot,
        belt_slot,
    )
    v89_q_slot_draw(q_rect)

    # SAĞ: 5 pasif skill slotu sağ bilgi kutusunun tam merkezine yerleşir.
    skill_group_w = belt_slot * 5 + belt_gap * 4
    skill_x = right.centerx - skill_group_w // 2
    v100_skill_belt_draw(skill_x, belt_y, belt_slot, belt_gap)

    # Tek merkez çizgisi yerine iki çizgi: yukarıdaki sol/sağ kutuların iç
    # sınırlarıyla tam aynı x koordinatlarında. Böylece alt kemer iki panele bağlanır.
    divider_top = left.bottom + 7
    divider_bottom = panel.bottom - 10
    for divider_x in (left.right, right.x):
        pygame.draw.line(
            ekran,
            V91_UI_GREY,
            (divider_x, divider_top),
            (divider_x, divider_bottom),
            1,
        )

    if envanter_aksiyon_acik and envanter_aksiyon_item_index is not None:
        envanter_aksiyon_menusu_ciz(panel, envanter_aksiyon_item_index, envanter_aksiyon_kaynagi)
    if one_cikan_atama_item_index is not None:
        one_cikan_atama_penceresi_ciz(panel)
# </POTBO_STAGE S2490>

# <POTBO_STAGE S2492>

# ---------------------------------------------------------
# Text render cache
# font.render() is surprisingly expensive when dozens of static HUD/menu labels
# are rebuilt at 60 Hz. Dynamic values still work; the cache is bounded.
# ---------------------------------------------------------
V103_TEXT_CACHE = {}
# </POTBO_STAGE S2492>

# <POTBO_STAGE S2496>


# ---------------------------------------------------------
# Medieval HUD panel cache
# The top HUD used to allocate/redraw the same alpha plate every frame.
# ---------------------------------------------------------
V103_PANEL_CACHE = {}


def v89_medieval_panel(rect, accent=V91_UI_RED, alpha=248):
    rect = pygame.Rect(rect)
    accent_rgb = tuple(int(v) for v in accent[:3])
    opacity = max(0, min(255, int(alpha)))
    key = (rect.width, rect.height, accent_rgb, opacity)
    layer = V103_PANEL_CACHE.get(key)
    if layer is None:
        layer = pygame.Surface(rect.size, pygame.SRCALPHA).convert_alpha()
        layer.fill((*V91_UI_BLACK, opacity))
        local = layer.get_rect()
        pygame.draw.rect(layer, (*V91_UI_WHITE, 255), local, 2)
        pygame.draw.rect(layer, (*accent_rgb, 255), local.inflate(-6, -6), 2)
        pygame.draw.line(
            layer,
            (*V91_UI_GREY, 255),
            (8, local.bottom - 5),
            (local.right - 9, local.bottom - 5),
            1,
        )
        v91_pixel_corner_marks(layer, local, accent_rgb)
        if len(V103_PANEL_CACHE) >= 32:
            V103_PANEL_CACHE.clear()
        V103_PANEL_CACHE[key] = layer
    ekran.blit(layer, rect.topleft)
# </POTBO_STAGE S2496>

# <POTBO_STAGE S2503>

# ---------------------------------------------------------
# CTRL+3: Corona Aetherica -> inventory + Q test slot
# ---------------------------------------------------------
def v105_find_inventory_item(item_id):
    for index, item in enumerate(envanter_itemleri):
        if isinstance(item, dict) and item.get("id") == item_id:
            return index
    return None
# </POTBO_STAGE S2503>

# <POTBO_STAGE S2517>

# ---------------------------------------------------------
# PLAYER CONDITION
# Normal HUD never prints condition text. CTRL+I is the diagnostic readout.
# Wounded characters drip compact sprite blood from the body; critical condition
# keeps the same drip and adds a restrained red screen wash.
# ---------------------------------------------------------
def v106_player_condition():
    if oyuncu_hp <= 0:
        return "critical"
    hp_ratio = max(0.0, min(1.0, float(oyuncu_hp) / max(1.0, float(oyuncu_max_hp))))
    severity = float(v90_injury_severity()) if "v90_injury_severity" in globals() else 1.0 - hp_ratio
    if hp_ratio <= 0.25 or severity >= 0.62:
        return "critical"
    if hp_ratio <= 0.70 or severity >= 0.20:
        return "wounded"
    return "healthy"
# </POTBO_STAGE S2517>

# <POTBO_STAGE S2523>


# Final HUD definition: identical compact V98 bars, but condition words are never
# shown during normal play. CTRL+I owns the textual diagnosis.
def oyuncu_paneli_ciz():
    if oyuncu_hp <= 0:
        return

    outer = _v92_top_hud_outer_rect()
    left = hud_sol_rect()
    v89_medieval_panel(outer, V91_UI_RED, 250)
    pygame.draw.line(
        ekran,
        V91_UI_RED,
        (left.right, outer.y + 9),
        (left.right, outer.bottom - 9),
        2,
    )

    name_rect = yazi_yaz(
        secili_karakter_adi(),
        left.x + 18,
        left.y + 13,
        V91_UI_WHITE,
        oyun_font,
    )
    yazi_yaz(
        f"{t('level')} {oyuncu_level}",
        min(left.right - 150, name_rect.right + 12),
        left.y + 15,
        level_rengi(oyuncu_level),
        mini_font,
    )

    coin_x = left.right - 88
    if _v79_coin_draw(coin_x, left.y + 13, 19):
        coin_x += 23
    yazi_yaz(str(oyuncu_altin), coin_x, left.y + 15, V91_UI_GOLD, mini_font)

    displayed_hp = 0.0 if v85_mortal_wound_state.active else float(oyuncu_hp)
    hp_ratio = displayed_hp / max(1.0, float(oyuncu_max_hp))
    hp_trail = (
        0.0 if v85_mortal_wound_state.active else float(hp_gorunen)
    ) / max(1.0, float(oyuncu_max_hp))
    stamina_ratio = float(stamina_gorunen) / max(1.0, float(oyuncu_max_stamina))
    mana_ratio = float(mana_gorunen) / max(1.0, float(oyuncu_max_mana))
    now = pygame.time.get_ticks()

    _v98_status_row(
        left,
        left.y + 50,
        17,
        hp_ratio,
        (126, 5, 23),
        V98_HEALTH_ICON,
        trail=hp_trail,
    )
    stamina_bar = _v98_status_row(
        left,
        left.y + 79,
        12,
        stamina_ratio,
        (184, 149, 47),
        V98_STAMINA_ICON,
        warning=now < stamina_uyari_bitis,
    )
    _v98_status_row(
        left,
        left.y + 103,
        15,
        mana_ratio,
        (28, 120, 154),
        V98_MANA_ICON,
        warning=now < mana_uyari_bitis,
    )

    if "v90_injury" in globals():
        effective = max(0.0, min(1.0, float(v90_injury.effective_stamina_ratio)))
        cap_x = stamina_bar.x + int(round(stamina_bar.width * effective))
        pygame.draw.line(
            ekran,
            V91_UI_BLACK,
            (cap_x, stamina_bar.y - 2),
            (cap_x, stamina_bar.bottom + 2),
            4,
        )
        pygame.draw.line(
            ekran,
            V91_UI_WHITE,
            (cap_x, stamina_bar.y - 2),
            (cap_x, stamina_bar.bottom + 2),
            1,
        )


# CTRL+I replaces the old coin diagnostic. No normal HUD text is emitted.
_v106_dev_input_previous = gelistirici_test_girdisi_uygula


def gelistirici_test_girdisi_uygula(olay):
    if (
        GELISTIRICI_MODU
        and olay.type == pygame.KEYDOWN
        and bool(olay.mod & pygame.KMOD_CTRL)
        and olay.key == pygame.K_i
    ):
        condition = v106_player_condition()
        color = {
            "healthy": (92, 205, 111),
            "wounded": V91_UI_GOLD,
            "critical": V91_UI_RED_HOT,
        }[condition]
        bildirim_goster(
            bt(
                f"DURUM: {v106_player_condition_label()}",
                f"CONDITION: {v106_player_condition_label()}",
            ),
            color,
        )
        return True
    return _v106_dev_input_previous(olay)
# </POTBO_STAGE S2523>

# <POTBO_STAGE S2529>


def v106_has_eadric_stone():
    return any(
        isinstance(item, dict) and item.get("id") == "eadric_stone"
        for item in envanter_itemleri
    )
# </POTBO_STAGE S2529>

# <POTBO_STAGE S2552>


def v106_corona_update(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA or oyuncu_hp <= 0:
        return

    if v106_corona.active:
        if int(now) >= int(v106_corona.expires_ms):
            v106_corona_scatter_remaining(now)
        else:
            player = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
            for actor in _v35_physical_targets():
                center = v90_actor_center(actor)
                delta = center - player
                distance = delta.length()
                if distance > V106_CORONA_ORBIT_RADIUS + 24.0 or distance < 20.0:
                    continue
                uid = v84_actor_uid(actor) or str(id(actor))
                if int(now) < int(v106_corona.contact_next.get(uid, 0)):
                    continue
                direction = delta.normalize() if delta.length_squared() > 1e-8 else pygame.Vector2(1.0, 0.0)
                v106_corona_apply_hit(actor, center, direction, projectile=False)
                v106_corona.contact_next[uid] = int(now) + V106_CORONA_CONTACT_COOLDOWN_MS

    for projectile in list(v106_corona.projectiles):
        if not projectile.active:
            continue
        dt = max(0.0, min(0.05, (int(now) - int(projectile.last_ms)) / 1000.0))
        projectile.last_ms = int(now)
        if int(now) - int(projectile.born_ms) >= V106_CORONA_PROJECTILE_LIFE_MS:
            projectile.active = False
            continue
        projectile.x += projectile.direction.x * V106_CORONA_PROJECTILE_SPEED * dt
        projectile.y += projectile.direction.y * V106_CORONA_PROJECTILE_SPEED * dt
        if not projectile.trail or pygame.Vector2(projectile.x, projectile.y).distance_to(projectile.trail[-1]) >= 11.0:
            projectile.trail.append((float(projectile.x), float(projectile.y)))
        if harita_pikseli_engel_mi(projectile.x, projectile.y):
            projectile.active = False
            v106_corona.impacts.append(V106CoronaImpact(projectile.x, projectile.y, int(now)))
            continue
        pos = pygame.Vector2(projectile.x, projectile.y)
        for actor in _v35_physical_targets():
            center = v90_actor_center(actor)
            if pos.distance_to(center) > 25.0:
                continue
            v106_corona_apply_hit(actor, pos, projectile.direction, projectile=True)
            projectile.active = False
            v106_corona.impacts.append(V106CoronaImpact(center.x, center.y, int(now)))
            break

    v106_corona.projectiles[:] = [p for p in v106_corona.projectiles if p.active]
    v106_corona.impacts[:] = [
        impact for impact in v106_corona.impacts if int(now) - int(impact.born_ms) <= 260
    ]
# </POTBO_STAGE S2552>

# <POTBO_STAGE S2574>


def _v108_ui_noop(*args, **kwargs):
    return None
# </POTBO_STAGE S2574>

# <POTBO_STAGE S2590>


def v106_corona_update(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA or oyuncu_hp <= 0:
        return

    # Yörünge temas bölgesi aynı kalır: yaklaşan düşmanları vurur/geri iter.
    if v106_corona.active:
        if int(now) >= int(v106_corona.expires_ms):
            v106_corona_scatter_remaining(now)
        else:
            player = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
            for actor in _v35_physical_targets():
                if not v109_corona_target_valid(actor):
                    continue
                center = v90_actor_center(actor)
                delta = center - player
                distance = delta.length()
                if distance > V106_CORONA_ORBIT_RADIUS + 24.0 or distance < 20.0:
                    continue
                uid = v84_actor_uid(actor) or str(id(actor))
                if int(now) < int(v106_corona.contact_next.get(uid, 0)):
                    continue
                direction = (
                    delta.normalize()
                    if delta.length_squared() > 1e-8
                    else pygame.Vector2(1.0, 0.0)
                )
                v106_corona_apply_hit(actor, center, direction, projectile=False)
                v106_corona.contact_next[uid] = int(now) + V106_CORONA_CONTACT_COOLDOWN_MS

    for projectile in list(v106_corona.projectiles):
        if not projectile.active:
            continue
        dt = max(0.0, min(0.05, (int(now) - int(projectile.last_ms)) / 1000.0))
        projectile.last_ms = int(now)
        if dt <= 0.0:
            continue

        v109_corona_steer(projectile, dt)
        previous = pygame.Vector2(float(projectile.x), float(projectile.y))
        proposed = previous + pygame.Vector2(projectile.direction) * V106_CORONA_PROJECTILE_SPEED * dt

        wall_hit = v109_corona_first_wall(previous, proposed)
        travel_end = pygame.Vector2(wall_hit[1]) if wall_hit is not None else proposed

        # Yüksek hızda bir aktörün iki frame arasından atlanmaması için segment collision.
        first_actor = None
        first_t = 2.0
        first_point = None
        for actor in _v35_physical_targets():
            if not v109_corona_target_valid(actor):
                continue
            t_hit, point, distance = v109_segment_closest(
                previous,
                travel_end,
                v90_actor_center(actor),
            )
            if distance <= V109_CORONA_DIRECT_HIT_RADIUS and t_hit < first_t:
                first_actor = actor
                first_t = t_hit
                first_point = point

        if first_actor is not None:
            projectile.x = float(first_point.x)
            projectile.y = float(first_point.y)
            v106_corona_apply_hit(
                first_actor,
                first_point,
                pygame.Vector2(projectile.direction),
                projectile=True,
            )
            projectile.active = False
            impact_center = v90_actor_center(first_actor)
            v106_corona.impacts.append(
                V106CoronaImpact(impact_center.x, impact_center.y, int(now))
            )
            continue

        if wall_hit is not None:
            projectile.x = float(travel_end.x)
            projectile.y = float(travel_end.y)
            projectile.active = False
            v106_corona.impacts.append(
                V106CoronaImpact(projectile.x, projectile.y, int(now))
            )
            continue

        projectile.x = float(proposed.x)
        projectile.y = float(proposed.y)

        # Oyuncuya göre menzil sınırı yoktur; yalnız gerçek dünya sınırından çıkınca temizlenir.
        if (
            projectile.x < -V109_CORONA_WORLD_MARGIN
            or projectile.y < -V109_CORONA_WORLD_MARGIN
            or projectile.x > HARITA_GENISLIK + V109_CORONA_WORLD_MARGIN
            or projectile.y > HARITA_YUKSEKLIK + V109_CORONA_WORLD_MARGIN
        ):
            projectile.active = False
            continue

        pos = pygame.Vector2(projectile.x, projectile.y)
        if not projectile.trail or pos.distance_to(projectile.trail[-1]) >= 11.0:
            projectile.trail.append((float(projectile.x), float(projectile.y)))

        # Hasarsız itici alan: top değmeden de yakın hedefi dışarı doğru iter.
        v109_corona_repulsion(projectile, dt)

    v106_corona.projectiles[:] = [p for p in v106_corona.projectiles if p.active]
    v106_corona.impacts[:] = [
        impact
        for impact in v106_corona.impacts
        if int(now) - int(impact.born_ms) <= 260
    ]


# ---------------------------------------------------------
# DEATH UI
# Ölüm sahnesinin üst başlığı zaten _v83_death_menu_draw tarafından çiziliyor.
# Eski oyuncu_olum_ui_ciz alt kısımda ikinci GEBERDİN + katil adını ekliyordu;
# final UI compositor bu fonksiyonu yeniden çağırdığı için duplicate görünüyordu.
# ---------------------------------------------------------
def oyuncu_olum_ui_ciz():
    return None


# ---------------------------------------------------------
# CONSUMABLE FLASH QUEUE
# Envanter modalında kullanılan iksirler efekt sürelerini harcamaz. Envanter kapanınca
# 430ms'lik mevcut sprite-parlama dili tek tek, çakışmadan oynatılır.
# ---------------------------------------------------------
V109_CONSUMABLE_FLASH_QUEUE = deque()
# </POTBO_STAGE S2590>

# <POTBO_STAGE S2594>


# ---------------------------------------------------------
# EADRIC STONE MANA
# Mana doğal olarak yenilenmez. Eadric'in taşı varken HUD'daki altı mana karesinden
# tam bir kareyi her 5 saniyede doldurur: tick başına max_mana / 6.
# ---------------------------------------------------------
V109_EADRIC_TICK_MS = 5000
# </POTBO_STAGE S2594>

# <POTBO_STAGE S2598>


def stamina_guncelle():
    global oyuncu_mana, mana_gorunen, v109_eadric_next_tick_ms

    # Parent V106 doğal mana regenini zaten kapatıyor ama Eadric için continuous rate
    # ekliyor. Bu çağrıda taşı geçici olarak görünmez yapıp yalnız stamina/HUD pipeline'ını al.
    g = globals()
    saved_has_stone = g.get("v106_has_eadric_stone")
    g["v106_has_eadric_stone"] = lambda: False
    try:
        result = _v109_stamina_update_raw()
    finally:
        if saved_has_stone is not None:
            g["v106_has_eadric_stone"] = saved_has_stone
        else:
            g.pop("v106_has_eadric_stone", None)

    now = pygame.time.get_ticks()
    active = (
        oyun_durumu == OYUN
        and oyun_alt_durumu == HARITA
        and oyuncu_hp > 0
        and bool(_v109_has_eadric_stone_raw())
        and float(oyuncu_mana) < float(oyuncu_max_mana)
    )
    if not active:
        v109_eadric_next_tick_ms = int(now) + V109_EADRIC_TICK_MS
        return result

    if int(now) >= int(v109_eadric_next_tick_ms):
        elapsed_ticks = 1 + max(
            0,
            (int(now) - int(v109_eadric_next_tick_ms)) // V109_EADRIC_TICK_MS,
        )
        # Çok uzun bir frame hitch'inde tek karede sınırsız catch-up yapma.
        elapsed_ticks = min(3, int(elapsed_ticks))
        per_tick = float(oyuncu_max_mana) / V109_EADRIC_BAR_SQUARES
        oyuncu_mana = min(
            float(oyuncu_max_mana),
            float(oyuncu_mana) + per_tick * elapsed_ticks,
        )
        v109_eadric_next_tick_ms += V109_EADRIC_TICK_MS * elapsed_ticks
        # Görsel bar bir anda teleport etmesin; mevcut smooth display sonraki karelerde yaklaşır.
        mana_gorunen = min(float(oyuncu_max_mana), float(mana_gorunen))
    return result
# </POTBO_STAGE S2598>

# <POTBO_STAGE S2606>


def v110_find_inventory_item(item_id):
    for index, item in enumerate(envanter_itemleri):
        if isinstance(item, dict) and item.get("id") == item_id:
            return index
    return None
# </POTBO_STAGE S2606>

