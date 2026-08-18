# Path of the Bloodied One — categorized source stages
#
# This file is intentionally executed by core/bootstrap.py in original source order.
# Keeping one shared runtime namespace avoids gameplay regressions while the former
# 90k-line monolith is physically separated by responsibility. Do not import this
# file directly; edit the stage code normally and launch root main.py.

# <POTBO_STAGE S0015>

ASSETS = os.path.join(BASE_DIR, "assets")
# </POTBO_STAGE S0015>

# <POTBO_STAGE S0021>

ERKEK_SHEET_YOLU = os.path.join(ASSETS, "characters", "male_sheet.png")
# </POTBO_STAGE S0021>

# <POTBO_STAGE S0023>

ERKEK_YON_KLASORU = os.path.join(ASSETS, "characters", "male")
# </POTBO_STAGE S0023>

# <POTBO_STAGE S0027>

NPC_YOLU = os.path.join(ASSETS, "npcs", "elder.png")
# </POTBO_STAGE S0027>

# <POTBO_STAGE S0029>

AURUM_POTABILE_YOLU = os.path.join(ASSETS, "items", "aurum_potabile.png")

QUINTA_ESSENTIA_YOLU = os.path.join(ASSETS, "items", "quinta_essentia.png")

EADRIC_TASI_YOLU = os.path.join(ASSETS, "items", "eadrics_stone.png")
# </POTBO_STAGE S0029>

# <POTBO_STAGE S0036>

# Ambient rat ve Heads Thrower asset'leri. İkisi de eski sprite arşivlerinden
# geldiği için kaynakta parlak yeşil + teal preview fonu taşır; aşağıdaki loader
# çalışma anında bu iki rengi gerçek alpha=0 yapar. Rat savaş aktörü değildir.
AMBIENT_KLASORU = os.path.join(ASSETS, "ambient")
RAT_SHEET_ADAYLARI = [
    os.path.join(AMBIENT_KLASORU, "rat_spriteSheet.png"),
    os.path.join(ASSETS, "creatures", "rat_spriteSheet.png"),
    os.path.join(BASE_DIR, "rat_spriteSheet.png"),
]
# </POTBO_STAGE S0036>

# <POTBO_STAGE S0054>

KISAYOL_E_YOLU = os.path.join(ASSETS, "shortcuts", "e.png")
# </POTBO_STAGE S0054>

# <POTBO_STAGE S0058>

COIN_SEMBOL_ADAYLARI = [
    os.path.join(ASSETS, "ui", "coin.png"),
    os.path.join(ASSETS, "items", "coin.png"),
    # Kullanıcının verdiği coin.png proje kökünde de doğrudan desteklenir.
    os.path.join(BASE_DIR, "coin.png"),
    os.path.join(BASE_DIR, "coinsymbol.png"),
    os.path.join(BASE_DIR, "coinsymbol(2).png"),
]
# </POTBO_STAGE S0058>

# <POTBO_STAGE S0060>

VSCODE_LOGO_ADAYLARI = [
    os.path.join(ASSETS, "ui", "vscode_logo.png"),
    os.path.join(ASSETS, "ui", "vscode_logo.webp"),
    os.path.join(BASE_DIR, "Visual_Studio_Code_1.35_icon.svg(2).webp"),
]

COIN_SEMBOL_YOLU = mevcut_ilk_dosya(COIN_SEMBOL_ADAYLARI)
# </POTBO_STAGE S0060>

# <POTBO_STAGE S0062>
VSCODE_LOGO_YOLU = mevcut_ilk_dosya(VSCODE_LOGO_ADAYLARI)

AURUM_POTABILE_ADAYLARI = [
    AURUM_POTABILE_YOLU,
    os.path.join(ASSETS, "items", "aurum_potentia.png"),
    os.path.join(ASSETS, "items", "potentia.png"),
    os.path.join(ASSETS, "items", "potentia_potion.png"),
    os.path.join(ASSETS, "items", "potentia_iksiri.png"),
    os.path.join(BASE_DIR, "aurum_potabile.png"),
    os.path.join(BASE_DIR, "aurum_potentia.png"),
    os.path.join(BASE_DIR, "potentia.png"),
    os.path.join(BASE_DIR, "potentia_potion.png"),
]

QUINTA_ESSENTIA_ADAYLARI = [
    QUINTA_ESSENTIA_YOLU,
    os.path.join(ASSETS, "items", "essentia.png"),
    os.path.join(ASSETS, "items", "essentia_potion.png"),
    os.path.join(ASSETS, "items", "essentia_iksiri.png"),
    os.path.join(BASE_DIR, "quinta_essentia.png"),
    os.path.join(BASE_DIR, "essentia.png"),
    os.path.join(BASE_DIR, "essentia_potion.png"),
]

EADRIC_TASI_ADAYLARI = [
    EADRIC_TASI_YOLU,
    os.path.join(ASSETS, "items", "eadric_stone.png"),
    os.path.join(ASSETS, "items", "eadrics_stone.png"),
    os.path.join(ASSETS, "items", "eadric_tasi.png"),
    os.path.join(ASSETS, "items", "eadricin_tasi.png"),
    os.path.join(BASE_DIR, "eadrics_stone.png"),
    os.path.join(BASE_DIR, "eadric_stone.png"),
    os.path.join(BASE_DIR, "eadric_tasi.png"),
]

AURUM_POTABILE_YOLU = mevcut_ilk_dosya(AURUM_POTABILE_ADAYLARI) or AURUM_POTABILE_YOLU
QUINTA_ESSENTIA_YOLU = (
    mevcut_ilk_dosya(QUINTA_ESSENTIA_ADAYLARI) or QUINTA_ESSENTIA_YOLU
)
EADRIC_TASI_YOLU = mevcut_ilk_dosya(EADRIC_TASI_ADAYLARI) or EADRIC_TASI_YOLU
# </POTBO_STAGE S0062>

# <POTBO_STAGE S0067>
# Yeni düzenli yol.
BASLIK_FONT_YOLU = os.path.join(ASSETS, "fonts", "mainmenufont.ttf")
# Eski projedeki yolu da destekle.
ESKI_BASLIK_FONT_YOLU = os.path.join(ASSETS, "mainmenufont.ttf")
# </POTBO_STAGE S0067>

# <POTBO_STAGE S0071>
# =========================================================
# FONTLAR
# Sadece ana oyun başlığı özel font kullanır.
# =========================================================
if os.path.exists(BASLIK_FONT_YOLU):
    gercek_baslik_font_yolu = BASLIK_FONT_YOLU
elif os.path.exists(ESKI_BASLIK_FONT_YOLU):
    gercek_baslik_font_yolu = ESKI_BASLIK_FONT_YOLU
else:
    gercek_baslik_font_yolu = None

if gercek_baslik_font_yolu is not None:
    baslik_font = pygame.font.Font(gercek_baslik_font_yolu, 66)
else:
    baslik_font = pygame.font.SysFont("georgia", 66, bold=True)
# </POTBO_STAGE S0071>

# <POTBO_STAGE S0073>

normal_font = pygame.font.SysFont("consolas", 21, bold=True)

kucuk_font = pygame.font.SysFont("consolas", 17, bold=True)

mini_font = pygame.font.SysFont("consolas", 14, bold=True)

oyun_buyuk_font = pygame.font.SysFont("consolas", 29, bold=True)

oyun_font = pygame.font.SysFont("consolas", 21, bold=True)

oyun_kucuk_font = pygame.font.SysFont("consolas", 16, bold=True)
# </POTBO_STAGE S0073>

# <POTBO_STAGE S0075>

seviye_anim_font = pygame.font.SysFont("consolas", 52, bold=True)
# </POTBO_STAGE S0075>

# <POTBO_STAGE S0081>


def metni_satirlara_bol(metin, font, maksimum_genislik):
    kelimeler = metin.split()
    satirlar = []
    mevcut_satir = ""

    for kelime in kelimeler:
        deneme = kelime if not mevcut_satir else mevcut_satir + " " + kelime

        if font.size(deneme)[0] <= maksimum_genislik:
            mevcut_satir = deneme
        else:
            if mevcut_satir:
                satirlar.append(mevcut_satir)
            mevcut_satir = kelime

    if mevcut_satir:
        satirlar.append(mevcut_satir)

    return satirlar
# </POTBO_STAGE S0081>

# <POTBO_STAGE S0175>
sprite_olcek_onbellegi = {}
# </POTBO_STAGE S0175>

# <POTBO_STAGE S0181>
# Eadric mağaranın yol tarifini verdiğinde True olur.
magara_yolu_ogrenildi = False
# </POTBO_STAGE S0181>

# <POTBO_STAGE S0213>


def magara_yolu_bolumu():
    e = eadric_adi()

    return [
        aksiyon("magara_yolunu_ogren"),
        satir(
            e,
            bt(
                "Mağara burada değil. Yolu bırakma.",
                "The cave is not here. Do not leave the road.",
            ),
        ),
        satir(
            e,
            bt(
                "Kuzeye uzanan yolu izle. Kırık sütunları geçince, solundaki taş yarığında ağzını görürsün.",
                "Follow the road to the north. Once you pass the broken columns, you will see its mouth in the stone cleft on your left.",
            ),
        ),
        satir(
            karakter_konusmaci(),
            bt(
                "Bunu neden şimdi söylüyorsun?",
                "Why tell me this now?",
            ),
        ),
        satir(
            e,
            bt(
                "Çünkü artık yol da seni sayıyor.",
                "Because now the road is counting you as well.",
            ),
        ),
        satir(
            e,
            bt(
                "Git. Sonra istersen dönersin; görevim biter, sözlerim bitmez.",
                "Go. If you wish, come back later; my task ends, my words do not.",
            ),
        ),
    ]


def tas_secimi_bolumu():
    e = eadric_adi()

    al = [
        aksiyon("eadric_tasini_ver"),
        satir(
            e,
            bt(
                "İki kez ısınırsa ateşe at. Üç kez ısınırsa kaç.",
                "If it warms twice, cast it into the fire. If it warms "
                "three times, run.",
            ),
        ),
        satir(
            karakter_konusmaci(),
            bt("Ya bir kez ısınırsa?", "What if it warms once?"),
        ),
        satir(
            e,
            bt(
                "O zaman senden önce davranmıştır.",
                "Then it has acted before you.",
            ),
        ),
    ] + magara_yolu_bolumu()

    alma = [
        satir(
            karakter_konusmaci(),
            bt(
                "Kendi uğursuzluğunu kendin taşı.",
                "Carry your own ill omen.",
            ),
        ),
        satir(e, bt("Duydun mu?", "Did you hear that?")),
        satir(
            e,
            bt(
                "Seni sevmediğini söylüyor.",
                "It says it does not like you.",
            ),
        ),
        satir(
            karakter_konusmaci(),
            bt("Taşlar konuşmaz.", "Stones do not speak."),
        ),
        satir(
            e,
            bt(
                "İnsanlar da konuşmamalı. Yine de konuşuyorlar.",
                "Neither should people. Yet they do.",
            ),
        ),
    ] + magara_yolu_bolumu()

    return [
        satir(
            e,
            bt(
                "Bunu yanında taşı. Gece iki kez ısınırsa ateşe at. "
                "Üç kez ısınırsa kaç.",
                "Carry this. If it warms twice at night, cast it into the "
                "fire. If it warms three times, run.",
            ),
        ),
        secim(
            [
                (bt("Al.", "Take it."), al),
                (bt("Alma.", "Refuse it."), alma),
            ]
        ),
    ]


def ganimet_sonrasi_akisi():
    e = eadric_adi()

    # Eadric'in konuşması oyuncunun önceki seçimine göre değiştirilmez.
    # Bu akışın özgün giriş metni doğrudan korunur.
    giris = [
        satir(e, bt("Bir eksildi.", "One less.")),
        satir(
            karakter_konusmaci(),
            bt("Ne eksildi?", "What is one less?"),
        ),
        satir(
            e,
            bt(
                "Kayalıklardan bir şey aldın. Kayalıklar da senden aldı.",
                "You took something from the rocks. The rocks took something "
                "from you as well.",
            ),
        ),
    ]

    secenek_1 = [
        satir(
            e,
            bt(
                "Benden önce burada oturan adama.",
                "It belonged to the man who sat here before me.",
            ),
        ),
        satir(
            karakter_konusmaci(),
            bt("O da Eadric miydi?", "Was he Eadric too?"),
        ),
        satir(
            e,
            bt(
                "Bilmiyorum. Adını alınca yüzünü unuttum.",
                "I do not know. When I took his name, I forgot his face.",
            ),
        ),
    ] + magara_yolu_bolumu()

    secenek_2 = [
        satir(
            e,
            bt(
                "Ben anlatmasam da duyacaksın.",
                "You will hear it even if I do not tell you.",
            ),
        ),
        satir(karakter_konusmaci(), bt("Neyi?", "Hear what?")),
        satir(
            e,
            bt(
                "Gece taşların altında çalan çanı. İpi yoktur ama hep birisi asılır.",
                "The bell beneath the stones at night. It has no rope, yet "
                "someone is always hanged.",
            ),
        ),
    ] + magara_yolu_bolumu()

    secenek_3 = tas_secimi_bolumu()

    return giris + [
        secim(
            [
                (
                    bt(
                        "Aldığım şey kime aitti?",
                        "Who owned what I took?",
                    ),
                    secenek_1,
                ),
                (
                    bt(
                        "Uğursuz masallarını kendine sakla.",
                        "Keep your cursed tales to yourself.",
                    ),
                    secenek_2,
                ),
                (
                    bt(
                        "Bu borç nasıl ödenir?",
                        "How is this debt paid?",
                    ),
                    secenek_3,
                ),
            ]
        ),
        aksiyon("ganimet_sonrasi_tamam"),
    ]
# </POTBO_STAGE S0213>

# <POTBO_STAGE S0215>


# =========================================================
# GÖRSEL YÜKLEME
# =========================================================

# =========================================================


def resim_yukle(yol, boyut=None, alpha=True, piksel=False):
    if not os.path.exists(yol):
        return None

    try:
        resim = pygame.image.load(yol)

        if alpha:
            resim = resim.convert_alpha()
        else:
            resim = resim.convert()

        if boyut is not None:
            if piksel:
                resim = pygame.transform.scale(resim, boyut)
            else:
                resim = pygame.transform.smoothscale(resim, boyut)

        return resim

    except pygame.error:
        return None
# </POTBO_STAGE S0215>

# <POTBO_STAGE S0217>


def arka_plani_saydam_yap(resim, tolerans=24):
    """
    Görselin sol üst pikselini arka plan rengi kabul eder.
    Aynı/aşırı yakın açık renk pikselleri şeffaflaştırır.
    """

    if resim is None:
        return None

    sonuc = resim.convert_alpha().copy()

    referans = sonuc.get_at((0, 0))

    ref_r = referans.r
    ref_g = referans.g
    ref_b = referans.b

    piksel_dizisi = pygame.PixelArray(sonuc)

    try:
        for x in range(sonuc.get_width()):
            for y in range(sonuc.get_height()):
                renk = sonuc.get_at((x, y))

                fark = max(
                    abs(renk.r - ref_r),
                    abs(renk.g - ref_g),
                    abs(renk.b - ref_b),
                )

                if fark <= tolerans:
                    piksel_dizisi[x, y] = (0, 0, 0, 0)
    finally:
        del piksel_dizisi

    return sonuc
# </POTBO_STAGE S0217>

# <POTBO_STAGE S0219>


def yon_karakter_resmi_yukle(yol):
    resim = resim_yukle(yol)

    if resim is None:
        return None

    resim = arka_plani_saydam_yap(resim, 30)

    return saydam_kenarlari_kirp(resim)


def item_resmi_yukle(yol):
    """Şeffaf PNG eşya görsellerini boş kenarlarından temizleyerek yükler."""
    if not yol:
        return None

    resim = resim_yukle(yol)
    if resim is None:
        return None

    return saydam_kenarlari_kirp(resim)


def sembol_resmi_yukle(yol):
    """Kullanıcı tarafından sağlanan okul sembolünü UI için hazırlar.

    Görsel yeniden üretilmez. Sol üstteki siyah fon referans alınarak transparan
    yapılır ve boş kenarlar kırpılır. Böylece aynı PNG Q slotunda ve kartlarda
    doğrudan kullanılabilir.
    """
    if not yol:
        return None
    resim = resim_yukle(yol)
    if resim is None:
        return None
    resim = arka_plani_saydam_yap(resim, tolerans=14)
    return saydam_kenarlari_kirp(resim)


erkek_yon_resimleri = {
    ad: yon_karakter_resmi_yukle(yol) for ad, yol in ERKEK_YON_DOSYALARI.items()
}
# </POTBO_STAGE S0219>

# <POTBO_STAGE S0222>

erkek_sheet = resim_yukle(ERKEK_SHEET_YOLU)
# </POTBO_STAGE S0222>

# <POTBO_STAGE S0247>


npc_resmi_orijinal = resim_yukle(NPC_YOLU)
# </POTBO_STAGE S0247>

# <POTBO_STAGE S0251>


def _alpha_sheet_rectlerini_cikar(yol, rectler, padding=0):
    """
    Kaynak zaten gerçek alpha taşıyorsa yalnız rect keser ve opaque sınırına trim eder.

    Bu yardımcı özellikle ground-fire gibi beyaz/sarı highlight içeren efektlerde
    colorkey kullanmaz; aksi halde gerçek alevin beyaz çekirdeği yanlışlıkla fon
    sanılabilir. İşlem yalnız asset yüklenirken bir kez yapılır.
    """
    sheet = resim_yukle(yol) if yol else None
    if sheet is None:
        return []
    sheet = sheet.copy().convert_alpha()
    sonuc = []
    for x, y, w, h in rectler:
        alan = pygame.Rect(int(x), int(y), int(w), int(h)).clip(sheet.get_rect())
        if alan.width <= 0 or alan.height <= 0:
            continue
        ham = pygame.Surface(alan.size, pygame.SRCALPHA, 32).convert_alpha()
        ham.fill((0, 0, 0, 0))
        ham.blit(sheet, (0, 0), alan)
        sinir = ham.get_bounding_rect(min_alpha=1)
        if sinir.width <= 0 or sinir.height <= 0:
            continue
        if padding > 0:
            sinir = sinir.inflate(padding * 2, padding * 2).clip(ham.get_rect())
        sonuc.append(ham.subsurface(sinir).copy())
    return sonuc
# </POTBO_STAGE S0251>

# <POTBO_STAGE S0253>


def _sinir_fonlu_sheet_rectlerini_cikar(yol, rectler, fon_rengi, tolerans=6, padding=0):
    sheet = resim_yukle(yol) if yol else None
    if sheet is None:
        return []
    sheet = sheet.copy().convert_alpha()
    # Fon temizliği rect kesmeden ÖNCE bütün atlas sınırından yapılır. Böylece bir
    # alev/煙 sprite'ı kendi hücre kenarına değdiğinde yanlışlıkla fon sanılmaz.
    sheet = _sinir_baglantili_fon_temizle(sheet, fon_rengi, tolerans)
    sonuc = []
    for x, y, w, h in rectler:
        alan = pygame.Rect(int(x), int(y), int(w), int(h)).clip(sheet.get_rect())
        if alan.width <= 0 or alan.height <= 0:
            continue
        ham = pygame.Surface(alan.size, pygame.SRCALPHA, 32).convert_alpha()
        ham.fill((0, 0, 0, 0))
        ham.blit(sheet, (0, 0), alan)
        sinir = ham.get_bounding_rect(min_alpha=1)
        if sinir.width <= 0 or sinir.height <= 0:
            continue
        if padding > 0:
            sinir = sinir.inflate(padding * 2, padding * 2).clip(ham.get_rect())
        sonuc.append(ham.subsurface(sinir).copy())
    return sonuc


def _frame_listesi_dogrula(kareler, minimum, isim):
    """
    Sprite sheet revizyonlarında sessizce yanlış animation map üretmemek için
    load-time invariant. Runtime'ı durdurmaz; eksik sheet halinde fallback render
    kullanılmasına izin verir fakat geliştirici konsolunda kesin teşhis bırakır.
    """
    if len(kareler) < int(minimum):
        print(
            f"[SPRITE WARNING] {isim}: beklenen en az {minimum} frame, "
            f"bulunan {len(kareler)}."
        )
        return False
    return True
# </POTBO_STAGE S0253>

# <POTBO_STAGE S0255>

# Rat sheet iki cycle taşır. İlk cycle'daki dört küçük yön satırı 22'şer frame'dir.
# Label satırını kesmemek için y=14'ten başlanır; her hücre trim edildikten sonra
# ortak canvas'a alınır. Bu, küçük sprite'ın koşarken zıplamasını engeller.
RAT_FRAME_RECTLERI = []
# </POTBO_STAGE S0255>

# <POTBO_STAGE S0258>
rat_sheet_yolu = mevcut_ilk_dosya(RAT_SHEET_ADAYLARI)
# </POTBO_STAGE S0258>

# <POTBO_STAGE S0260>

_rat_tum_kareler = _sprite_sheet_karelerini_cikar(
    rat_sheet_yolu,
    (0, 255, 0),
    RAT_FRAME_RECTLERI,
    ozel_transparan_rgblar=((0, 128, 128),),
)
# </POTBO_STAGE S0260>

# <POTBO_STAGE S0262>

RAT_SPRITELERI = {}
for _ri, _rname in enumerate(("right", "left", "down", "up")):
    _start = _ri * 22
    RAT_SPRITELERI[_rname] = _kareleri_ortak_canvas_yap(
        _rat_tum_kareler[_start : _start + 22]
    )

# y=189'daki 28x44 şerit tam gövde yürüyüşü değil; parça/ara sprite'lar
# içerdiği için karakter dünyada sürükleniyormuş gibi görünüyordu. Locomotion artık
# 72px'lik full-body pickup satırının ilk nötr/gövde karelerinden türetilir. Pickup
# ve throw sekanslarının tamamı menzilli saldırı için korunur.
_head_fragment_canvas = _kareleri_ortak_canvas_yap(_head_idle_raw, padding=3)
# </POTBO_STAGE S0262>

# <POTBO_STAGE S0265>


def _v19_alpha_gorsel_yukle(yol):
    if not yol or not os.path.exists(yol):
        return None
    try:
        return pygame.image.load(yol).convert_alpha()
    except (pygame.error, OSError):
        return None
# </POTBO_STAGE S0265>

# <POTBO_STAGE S0275>

aurum_potabile_resmi = item_resmi_yukle(AURUM_POTABILE_YOLU)

quinta_essentia_resmi = item_resmi_yukle(QUINTA_ESSENTIA_YOLU)

eadric_tasi_resmi = item_resmi_yukle(EADRIC_TASI_YOLU)
# </POTBO_STAGE S0275>

# <POTBO_STAGE S0277>

kisayol_e_resmi = resim_yukle(KISAYOL_E_YOLU)
# </POTBO_STAGE S0277>

# <POTBO_STAGE S0281>

coin_sembol_resmi = resim_yukle(COIN_SEMBOL_YOLU) if COIN_SEMBOL_YOLU else None
# </POTBO_STAGE S0281>

# <POTBO_STAGE S0283>


vscode_logo_resmi = resim_yukle(VSCODE_LOGO_YOLU) if VSCODE_LOGO_YOLU else None
# </POTBO_STAGE S0283>

# <POTBO_STAGE S0290>

# =========================================================
# SPRITE SHEET ARKA PLAN TEMİZLEME
# =========================================================


def siyaha_yakin_pikselleri_saydam_yap(kaynak):
    if kaynak is None:
        return None

    sonuc = kaynak.copy()

    for y in range(sonuc.get_height()):
        for x in range(sonuc.get_width()):
            r, g, b, a = sonuc.get_at((x, y))

            if r < 18 and g < 18 and b < 18:
                sonuc.set_at((x, y), (0, 0, 0, 0))

    return sonuc


def kenardan_siyah_arka_plani_temizle(kaynak, esik=35):
    """
    Yalnızca görsel kenarına bağlı siyah arka plan piksellerini şeffaf yapar.
    Sprite içindeki kapalı siyah çizgiler ve gölgeler korunur.
    """
    if kaynak is None:
        return None

    sonuc = kaynak.convert_alpha()
    genislik = sonuc.get_width()
    yukseklik = sonuc.get_height()

    if genislik <= 0 or yukseklik <= 0:
        return sonuc

    ziyaret = set()
    kuyruk = deque()

    def arka_plan_mi(x, y):
        r, g, b, a = sonuc.get_at((x, y))
        return a > 0 and r <= esik and g <= esik and b <= esik

    for x in range(genislik):
        if arka_plan_mi(x, 0):
            kuyruk.append((x, 0))
        if yukseklik > 1 and arka_plan_mi(x, yukseklik - 1):
            kuyruk.append((x, yukseklik - 1))

    for y in range(yukseklik):
        if arka_plan_mi(0, y):
            kuyruk.append((0, y))
        if genislik > 1 and arka_plan_mi(genislik - 1, y):
            kuyruk.append((genislik - 1, y))

    while kuyruk:
        x, y = kuyruk.popleft()

        if (x, y) in ziyaret:
            continue

        ziyaret.add((x, y))

        if not arka_plan_mi(x, y):
            continue

        sonuc.set_at((x, y), (0, 0, 0, 0))

        if x > 0:
            kuyruk.append((x - 1, y))
        if x + 1 < genislik:
            kuyruk.append((x + 1, y))
        if y > 0:
            kuyruk.append((x, y - 1))
        if y + 1 < yukseklik:
            kuyruk.append((x, y + 1))

    return sonuc


# Common enemy sheet'leri kendi chroma-key/alpha hattında temizlenir.
# Bu bölüm yalnız eski karakter/NPC asset temizleyicileri için korunur.


def sheet_parcala(sheet, sutun_sayisi, satir_sayisi):
    if sheet is None:
        return []

    saydam_sheet = siyaha_yakin_pikselleri_saydam_yap(sheet)

    kareler = []

    sheet_genislik = saydam_sheet.get_width()

    sheet_yukseklik = saydam_sheet.get_height()

    for satir in range(satir_sayisi):
        y1 = round(satir * sheet_yukseklik / satir_sayisi)

        y2 = round((satir + 1) * sheet_yukseklik / satir_sayisi)

        for sutun in range(sutun_sayisi):
            x1 = round(sutun * sheet_genislik / sutun_sayisi)

            x2 = round((sutun + 1) * sheet_genislik / sutun_sayisi)

            hucre = saydam_sheet.subsurface(
                pygame.Rect(x1, y1, x2 - x1, y2 - y1)
            ).copy()

            hucre = saydam_kenarlari_kirp(hucre)

            kareler.append(hucre)

    return kareler
# </POTBO_STAGE S0290>

# <POTBO_STAGE S0292>


# Erkek sheet: 6 sütun × 4 satır
erkek_kareleri = sheet_parcala(erkek_sheet, 6, 4)
# </POTBO_STAGE S0292>

# <POTBO_STAGE S0300>


# =========================================================
# TEMEL ÇİZİM FONKSİYONLARI
# =========================================================


def yazi_yaz(metin, x, y, renk=BEYAZ, font=normal_font, ortala=False):
    goruntu = font.render(str(metin), True, renk)

    rect = goruntu.get_rect()

    if ortala:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)

    ekran.blit(goruntu, rect)

    return rect


def harf_aralikli_yazi_yaz(
    metin,
    x,
    y,
    renk=BEYAZ,
    font=mini_font,
    harf_araligi=2,
    ortala=True,
):
    """Başlık ve küçük-kapital metinlerde kontrollü harf aralığı kullanır."""
    metin = str(metin)
    harfler = [font.render(harf, True, renk) for harf in metin]

    toplam_genislik = sum(harf.get_width() for harf in harfler)
    toplam_genislik += max(0, len(harfler) - 1) * harf_araligi
    baslangic_x = x - toplam_genislik // 2 if ortala else x

    imlec_x = baslangic_x
    for harf in harfler:
        rect = harf.get_rect(midleft=(imlec_x, y))
        ekran.blit(harf, rect)
        imlec_x += harf.get_width() + harf_araligi

    return pygame.Rect(
        baslangic_x,
        y - font.get_height() // 2,
        toplam_genislik,
        font.get_height(),
    )
# </POTBO_STAGE S0300>

# <POTBO_STAGE S0317>


def seviye_animasyonu_ciz():
    if seviye_anim_baslangic <= 0 or seviye_anim_level <= 0:
        return
    simdi = pygame.time.get_ticks()
    gecen = simdi - seviye_anim_baslangic
    if gecen >= SEVIYE_ANIM_SURESI_MS:
        return
    p = max(0.0, min(1.0, gecen / float(SEVIYE_ANIM_SURESI_MS)))
    if p < 0.22:
        scale = 0.72 + (p / 0.22) * 0.48
    else:
        scale = 1.20 - min(1.0, (p - 0.22) / 0.38) * 0.20
    alpha = 255 if p < 0.70 else int(255 * (1.0 - (p - 0.70) / 0.30))
    metin = bt(
        f"SEVİYE {seviye_anim_level}",
        f"LEVEL {seviye_anim_level}",
    )
    base = seviye_anim_font.render(metin, True, level_rengi(seviye_anim_level))
    size = (
        max(1, int(base.get_width() * scale)),
        max(1, int(base.get_height() * scale)),
    )
    img = pygame.transform.scale(base, size)
    img.set_alpha(max(0, min(255, alpha)))
    shadow = seviye_anim_font.render(metin, True, (0, 0, 0))
    shadow = pygame.transform.scale(shadow, size)
    shadow.set_alpha(max(0, min(180, alpha)))
    merkez = (GENISLIK // 2, YUKSEKLIK // 2 - 36)
    ekran.blit(
        shadow,
        shadow.get_rect(center=(merkez[0] + 4, merkez[1] + 5)),
    )
    ekran.blit(img, img.get_rect(center=merkez))
# </POTBO_STAGE S0317>

# <POTBO_STAGE S0338>


# =========================================================
# OYUNCU SPRITE ANİMASYONU
# =========================================================


def karakter_zemin_golgesi_ciz(x, y, genislik, yukseklik, alpha=72):
    """Ayak altında küçük, yumuşak ve dikkat çekmeyen bir temas gölgesi çizer."""
    genislik = max(4, int(genislik))
    yukseklik = max(2, int(yukseklik))
    yuzey = pygame.Surface((genislik, yukseklik), pygame.SRCALPHA)
    pygame.draw.ellipse(
        yuzey,
        (0, 0, 0, max(0, min(150, int(alpha)))),
        yuzey.get_rect(),
    )
    ekran.blit(yuzey, (int(x - genislik / 2), int(y - yukseklik / 2)))


sprite_parlama_mask_onbellegi = {}


def sprite_maskeli_parlama_ciz(sprite, rect, renk, alfa):
    """Dikdörtgen halo üretmeden yalnız sprite'ın gerçek opak piksellerini renklendirir."""
    if sprite is None or rect is None or alfa <= 0:
        return
    renk = tuple(max(0, min(255, int(v))) for v in renk[:3])
    key = (id(sprite), renk)
    katman = sprite_parlama_mask_onbellegi.get(key)
    if katman is None:
        mask = pygame.mask.from_surface(sprite, 1)
        katman = mask.to_surface(
            setcolor=(*renk, 255), unsetcolor=(0, 0, 0, 0)
        ).convert_alpha()
        sprite_parlama_mask_onbellegi[key] = katman
    draw = katman.copy()
    draw.set_alpha(max(0, min(255, int(alfa))))
    ekran.blit(draw, rect, special_flags=pygame.BLEND_RGBA_ADD)
# </POTBO_STAGE S0338>

# <POTBO_STAGE S0371>


def keycap_ikonu_ciz(x, y, harf="E"):
    """Atanmış etkileşim tuşunu kompakt, keskin köşeli bir keycap içinde gösterir."""

    boyut = 30
    etiket = str(harf).upper()
    genislik = max(boyut, mini_font.size(etiket)[0] + 16)
    tus_rect = pygame.Rect(
        int(x - genislik / 2),
        int(y - boyut / 2),
        genislik,
        boyut,
    )

    pygame.draw.rect(ekran, (0, 0, 0), tus_rect.move(2, 3))
    pygame.draw.rect(ekran, (24, 20, 27), tus_rect)
    pygame.draw.rect(ekran, (198, 29, 53), tus_rect, 2)

    yazi_yaz(
        etiket,
        tus_rect.centerx,
        tus_rect.centery,
        BEYAZ,
        mini_font,
        True,
    )
# </POTBO_STAGE S0371>

# <POTBO_STAGE S0458>


def _fire_cast_sprite_yone_cevir(img, yon):
    """Stretch atlası aşağı yönlü kabul edilir ve cast yönüne döndürülür."""
    if yon == "up":
        return pygame.transform.rotate(img, 180)
    if yon == "right":
        return pygame.transform.rotate(img, 90)
    if yon == "left":
        return pygame.transform.rotate(img, -90)
    return img


def _alpha_bounds_merkez_bastir(img, merkez_x, merkez_y):
    """
    Görünen piksellerin ağırlık merkezini sabit dünya noktasına oturtur.
    Sprite sheet içindeki farklı crop/hotspot sapmaları yüzünden ateş topunun
    bir karede yukarıda, diğer karede aşağıda görünmesini bastırır.
    """
    if img is None:
        return
    bounds = img.get_bounding_rect()
    if bounds.width <= 0 or bounds.height <= 0:
        ekran.blit(
            img,
            img.get_rect(center=(int(merkez_x), int(merkez_y))),
        )
        return
    ofx = (img.get_width() * 0.5) - bounds.centerx
    ofy = (img.get_height() * 0.5) - bounds.centery
    rect = img.get_rect(
        center=(
            int(round(merkez_x + ofx)),
            int(round(merkez_y + ofy)),
        )
    )
    ekran.blit(img, rect)
# </POTBO_STAGE S0458>

# <POTBO_STAGE S0460>


def _v27_ates_pariltisi_ciz(img, merkez_x, merkez_y, simdi, guc=1.0):
    """Gerçek flame maskesinden iki katmanlı additive ışık üretir.

    Daire/halo çizmek yerine aynı alevin alpha kütlesi genişletilir. İki farklı
    sinüs fazı parlaklığı ve boyu hafifçe değiştirir; sonuç düz sprite değil,
    nefes alan ateş gibi görünür.
    """
    if img is None:
        return
    pulse = (
        1.0
        + 0.055 * math.sin(float(simdi) * 0.029)
        + 0.025 * math.sin(float(simdi) * 0.071 + 1.4)
    )
    for kat, (mul, alpha, renk) in enumerate(
        (
            (1.18, 112, (255, 52, 8)),
            (1.42, 48, (255, 18, 4)),
        )
    ):
        scale = max(1.0, mul * pulse)
        w = max(2, int(round(img.get_width() * scale)))
        h = max(2, int(round(img.get_height() * scale)))
        key = ("fire_glow_mask_v27", id(img), w, h, kat)
        glow = sprite_olcek_onbellegi.get(key)
        if glow is None:
            mask = pygame.mask.from_surface(img)
            base = mask.to_surface(
                setcolor=(renk[0], renk[1], renk[2], 255),
                unsetcolor=(0, 0, 0, 0),
            ).convert_alpha()
            glow = pygame.transform.scale(base, (w, h))
            sprite_olcek_onbellegi[key] = glow
        draw = glow.copy()
        draw.set_alpha(max(0, min(190, int(alpha * float(guc)))))
        rect = _v27_alpha_merkez_rect(draw, merkez_x, merkez_y)
        ekran.blit(draw, rect, special_flags=pygame.BLEND_RGBA_ADD)
# </POTBO_STAGE S0460>

# <POTBO_STAGE S0480>


def kontrol_atamalari_paneli_ciz(secenek_panel, secenekler):
    """Tuş atamalarını diğer ayar satırlarından bilinçli olarak ayrı bir görsel dilde çizer."""
    pygame.draw.rect(ekran, (3, 3, 6), secenek_panel)
    pygame.draw.rect(ekran, (58, 49, 58), secenek_panel, 1)
    # İnce çift ray: bu ekranı klasik gotik ayar kartlarından ayırır.
    pygame.draw.line(
        ekran,
        (128, 8, 28),
        (secenek_panel.x + 12, secenek_panel.y + 18),
        (secenek_panel.x + 12, secenek_panel.bottom - 18),
        2,
    )
    pygame.draw.line(
        ekran,
        (48, 7, 15),
        (secenek_panel.right - 12, secenek_panel.y + 18),
        (secenek_panel.right - 12, secenek_panel.bottom - 18),
        1,
    )

    yazi_yaz(
        ayar_kategori_adi("kontroller"),
        secenek_panel.x + 34,
        secenek_panel.y + 31,
        PARLAK_KIRMIZI,
        normal_font,
    )
    pygame.draw.line(
        ekran,
        (92, 14, 28),
        (secenek_panel.x + 34, secenek_panel.y + 60),
        (secenek_panel.right - 56, secenek_panel.y + 60),
        1,
    )

    gorunen_adet = 5
    baslangic = ayar_scrollunu_guncelle(len(secenekler), gorunen_adet)
    satir_y = secenek_panel.y + 82
    satir_h = 72
    satir_gap = 10
    liste_x = secenek_panel.x + 42
    liste_w = secenek_panel.width - 112

    for gorunen_index, index in enumerate(
        range(
            baslangic,
            min(len(secenekler), baslangic + gorunen_adet),
        )
    ):
        ayar = secenekler[index]
        rect = pygame.Rect(
            liste_x,
            satir_y + gorunen_index * (satir_h + satir_gap),
            liste_w,
            satir_h,
        )
        secili = ayar_odak == "secenek" and index == ayar_index
        pygame.draw.rect(ekran, (22, 7, 12) if secili else (7, 7, 10), rect)
        pygame.draw.rect(ekran, (82, 62, 72), rect, 1)
        pygame.draw.rect(
            ekran,
            PARLAK_KIRMIZI if secili else (71, 8, 19),
            (rect.x, rect.y, 5 if secili else 3, rect.height),
        )

        yazi_yaz(
            f"{index + 1:02d}",
            rect.x + 18,
            rect.y + 12,
            SARI if secili else (108, 91, 96),
            mini_font,
        )
        yazi_yaz(
            ayar_etiketi(ayar),
            rect.x + 62,
            rect.centery,
            BEYAZ if secili else ACIK_GRI,
            kucuk_font,
            False,
        )

        if ayar == "bind_reset":
            key_rect = pygame.Rect(rect.right - 190, rect.y + 17, 158, 38)
            pygame.draw.rect(
                ekran,
                (34, 6, 13) if secili else (12, 10, 14),
                key_rect,
            )
            pygame.draw.rect(
                ekran,
                PARLAK_KIRMIZI if secili else (82, 65, 74),
                key_rect,
                1,
            )
            yazi_yaz(
                bt("SIFIRLA", "RESET"),
                key_rect.centerx,
                key_rect.centery,
                BEYAZ if secili else GRI,
                mini_font,
                True,
            )
        else:
            deger = ayar_degeri(ayar)
            key_rect = pygame.Rect(rect.right - 190, rect.y + 15, 158, 42)
            bekliyor = ayar.startswith("bind_") and tus_atama_bekleniyor == ayar[5:]
            nabiz = (
                0.5 + 0.5 * math.sin(pygame.time.get_ticks() / 180.0)
                if bekliyor
                else 0.0
            )
            kenar = PARLAK_KIRMIZI if secili or bekliyor else (92, 76, 86)
            if bekliyor and nabiz > 0.45:
                kenar = (245, 205, 65)
            pygame.draw.rect(ekran, (4, 4, 7), key_rect)
            pygame.draw.rect(
                ekran,
                kenar,
                key_rect,
                2 if secili or bekliyor else 1,
            )
            yazi_yaz(
                deger,
                key_rect.centerx,
                key_rect.centery,
                SARI if secili or bekliyor else ACIK_GRI,
                mini_font,
                True,
            )

    # Dikey konum göstergesi: thumb listenin üst/orta/alt konumunu doğrudan gösterir.
    track = pygame.Rect(
        secenek_panel.right - 38,
        satir_y,
        5,
        gorunen_adet * satir_h + (gorunen_adet - 1) * satir_gap,
    )
    pygame.draw.rect(ekran, (24, 18, 23), track)
    if len(secenekler) > 0:
        thumb_h = max(
            34,
            int(track.height * min(1.0, gorunen_adet / len(secenekler))),
        )
        maksimum_baslangic = max(1, len(secenekler) - gorunen_adet)
        oran = baslangic / maksimum_baslangic if len(secenekler) > gorunen_adet else 0.0
        thumb_y = track.y + int((track.height - thumb_h) * oran)
        thumb = pygame.Rect(track.x - 2, thumb_y, 9, thumb_h)
        pygame.draw.rect(ekran, (85, 7, 20), thumb)
        pygame.draw.rect(ekran, PARLAK_KIRMIZI, thumb, 1)

    if tus_atama_mesaji and pygame.time.get_ticks() < tus_atama_mesaj_bitis:
        yazi_yaz(
            tus_atama_mesaji,
            secenek_panel.centerx,
            secenek_panel.bottom - 24,
            SARI,
            mini_font,
            True,
        )
# </POTBO_STAGE S0480>

# <POTBO_STAGE S0490>


def vscode_isareti_ciz(merkez_x, merkez_y, alfa):
    alfa = max(0, min(255, int(alfa)))

    if vscode_logo_resmi is not None:
        logo = hafif_piksellestir(vscode_logo_resmi, (205, 205), 3)
        logo.set_alpha(alfa)
        ekran.blit(
            logo,
            logo.get_rect(center=(merkez_x, merkez_y - 28)),
        )
    else:
        # Asset bulunamazsa sade bir yer tutucu göster; yeni logo çizilmez.
        pygame.draw.rect(
            ekran,
            (42, 155, 235),
            pygame.Rect(merkez_x - 82, merkez_y - 110, 164, 164),
            4,
        )

    alfa_metin_ciz(
        "VISUAL STUDIO CODE",
        merkez_x,
        merkez_y + 105,
        normal_font,
        (225, 235, 245),
        alfa,
    )
# </POTBO_STAGE S0490>

# <POTBO_STAGE S0624>
V34_SPECIAL_AFTERIMAGE_INTERVAL_MS = 34
# </POTBO_STAGE S0624>

# <POTBO_STAGE S0634>
v34_special_afterimages = deque(maxlen=24)
v34_special_last_afterimage_ms = 0
# </POTBO_STAGE S0634>

# <POTBO_STAGE S0819>
V34_SPECIAL_AFTERIMAGE_INTERVAL_MS = 26
# </POTBO_STAGE S0819>

# <POTBO_STAGE S0855>
v34_special_afterimages = deque(list(v34_special_afterimages)[-8:], maxlen=8)
# </POTBO_STAGE S0855>

# <POTBO_STAGE S0908>
v34_special_afterimages = deque(maxlen=0)
# </POTBO_STAGE S0908>

# <POTBO_STAGE S0967>


# ---------------------------------------------------------
# FIREBALL RENDER CACHES
# ---------------------------------------------------------
v38_fire_sprite_cache = {}
# </POTBO_STAGE S0967>

# <POTBO_STAGE S0971>


def _v38_oriented_fire_sprite(frame, height, direction_name, alpha=255):
    height = max(3, int(height))
    alpha = max(0, min(255, int(alpha)))
    key = (id(frame), height, str(direction_name), alpha)
    cached = v38_fire_sprite_cache.get(key)
    if cached is not None:
        return cached
    scale = height / max(1.0, float(frame.get_height()))
    img = pygame.transform.scale(
        frame,
        (max(1, int(round(frame.get_width() * scale))), height),
    )
    img = _fire_cast_sprite_yone_cevir(img, direction_name)
    if alpha < 255:
        img = img.copy()
        img.set_alpha(alpha)
    v38_fire_sprite_cache[key] = img
    _v38_cache_limit(v38_fire_sprite_cache, 240)
    return img
# </POTBO_STAGE S0971>

# <POTBO_STAGE S1066>


sprite_parlama_alpha_onbellegi = {}
# </POTBO_STAGE S1066>

# <POTBO_STAGE S1076>


V40_RAT_ASSET_RELOADED = _v40_rat_sheet_reload()


# ---------------------------------------------------------
# CHARACTER SELECT: TAM BİYOGRAFİ + ÇAKIŞMASIZ PROFİL
# ---------------------------------------------------------
v40_char_bio_font = pygame.font.SysFont("consolas", 13, bold=True)
v40_char_profile_font = pygame.font.SysFont("consolas", 12, bold=True)
# </POTBO_STAGE S1076>

# <POTBO_STAGE S1087>


class RockImpact:
    def __init__(self, x, y, simdi):
        self.x = float(x)
        self.y = float(y)
        self.started_ms = int(simdi)
        rng = random.Random(int(x * 31 + y * 17 + simdi))
        self.fragments = []
        source = V40_HEAD_ROCK_FRAGMENTS or [None] * 5
        for i in range(max(5, len(source))):
            sprite = source[i % len(source)] if source else None
            a = rng.random() * math.tau
            speed = rng.uniform(42.0, 96.0)
            self.fragments.append(
                {
                    "sprite": sprite,
                    "vx": math.cos(a) * speed,
                    "vy": math.sin(a) * speed * 0.54,
                    "vz": rng.uniform(36.0, 82.0),
                    "rot": rng.uniform(0, 360),
                    "ang": rng.uniform(-420.0, 420.0),
                    "size": rng.uniform(1.5, 3.4),
                }
            )
        self.dust = []
        for _ in range(6):
            a = rng.random() * math.tau
            speed = rng.uniform(8.0, 26.0)
            self.dust.append(
                (
                    math.cos(a) * speed,
                    math.sin(a) * speed * 0.45,
                    rng.uniform(5.0, 10.0),
                )
            )

    def alive(self, simdi):
        return int(simdi) - self.started_ms < 560

    def ciz(self, simdi):
        age_ms = max(0, int(simdi) - self.started_ms)
        t = age_ms / 1000.0
        fade = max(0.0, 1.0 - age_ms / 560.0)
        if fade <= 0.0:
            return
        sx = dunya_ekran_x(self.x)
        sy = dunya_ekran_y(self.y)
        for frag in self.fragments:
            z = max(0.0, frag["vz"] * t - 0.5 * 260.0 * t * t)
            px = sx + frag["vx"] * t * KAMERA_YAKINLASTIRMA
            py = sy + frag["vy"] * t * KAMERA_YAKINLASTIRMA - z * KAMERA_YAKINLASTIRMA
            sprite = frag["sprite"]
            if sprite is not None:
                qrot = int(round((frag["rot"] + frag["ang"] * t) / 30.0)) * 30
                h = max(
                    3,
                    int(round(sprite.get_height() * 0.76 * KAMERA_YAKINLASTIRMA)),
                )
                key = (id(sprite), h, qrot)
                img = v40_rock_fragment_cache.get(key)
                if img is None:
                    sc = h / max(1.0, float(sprite.get_height()))
                    base = pygame.transform.scale(
                        sprite,
                        (
                            max(2, int(sprite.get_width() * sc)),
                            h,
                        ),
                    )
                    img = pygame.transform.rotate(base, qrot)
                    v40_rock_fragment_cache[key] = img
                    if len(v40_rock_fragment_cache) > 80:
                        for _ in range(20):
                            if not v40_rock_fragment_cache:
                                break
                            v40_rock_fragment_cache.pop(
                                next(iter(v40_rock_fragment_cache)),
                                None,
                            )
                ekran.blit(img, img.get_rect(center=(int(px), int(py))))
            else:
                rr = max(1, int(frag["size"] * KAMERA_YAKINLASTIRMA))
                pygame.draw.circle(ekran, (96, 84, 74), (int(px), int(py)), rr)
        alpha = int(90 * fade)
        for vx, vy, size in self.dust:
            px = sx + vx * t * KAMERA_YAKINLASTIRMA
            py = sy + vy * t * KAMERA_YAKINLASTIRMA
            rr = max(2, int(size * fade * 0.34))
            if rr > 0:
                surf = pygame.Surface((rr * 2 + 4, rr * 2 + 4), pygame.SRCALPHA)
                pygame.draw.ellipse(surf, (72, 64, 56, alpha), surf.get_rect())
                ekran.blit(surf, (int(px - rr - 2), int(py - rr - 2)))
# </POTBO_STAGE S1087>

# <POTBO_STAGE S1129>

# Gerçek dünyadaki santimetre/piksel oranı oyunda fiziksel birim olarak tanımlı değil.
# Sprite gövdesi ~60-70 px olduğundan +6 px, görsel ölçekte yaklaşık 1 cm'lik küçük
# bir kılıç erişim artışı olarak kullanılır. Hitbox hâlâ yönsel ve dar kalır.
V44_SWORD_REACH_BONUS_PX = 6
# </POTBO_STAGE S1129>

# <POTBO_STAGE S1341>


def v57_bar(surface, rect, value, label, value_text=""):
    value = v57_clamp01(value)
    pygame.draw.rect(surface, (13, 10, 14), rect, border_radius=3)
    inner = rect.inflate(-2, -2)
    pygame.draw.rect(surface, (31, 25, 31), inner, border_radius=2)
    if value > 0.002:
        fill = inner.copy()
        fill.width = max(1, int(inner.width * value))
        pygame.draw.rect(surface, (83, 14, 25), fill, border_radius=2)
        if fill.width > 4:
            pygame.draw.line(
                surface,
                (222, 205, 205),
                (fill.left + 2, fill.top + 1),
                (fill.right - 2, fill.top + 1),
                1,
            )
    pygame.draw.rect(surface, (90, 79, 89), rect, width=1, border_radius=3)
    text = mini_font.render(label, True, (185, 176, 184))
    surface.blit(text, (rect.left, rect.top - 15))
    if value_text:
        val = mini_font.render(value_text, True, (222, 216, 221))
        surface.blit(val, (rect.right - val.get_width(), rect.top - 15))
# </POTBO_STAGE S1341>

# <POTBO_STAGE S1356>


def v58_draw(surface, silhouette=False):
    # Lobe arkada, iplik ve aerosol önde. Bu sıra kanın tek düz sprite gibi görünmesini önler.
    for lobe in v58_lobes:
        lobe.draw(surface, silhouette=silhouette)
    for filament in v58_filaments:
        filament.draw(surface, silhouette=silhouette)
    for mist in v58_mist:
        mist.draw(surface, silhouette=silhouette)
# </POTBO_STAGE S1356>

# <POTBO_STAGE S1382>


def v59_technique_toast_ciz():
    now = pygame.time.get_ticks()
    definition = v59_active_definition(now)
    if definition is None:
        return
    technique_id = str(v59_state.get("active_id"))
    remaining = max(0, int(v59_state.get("active_until", 0)) - now)
    total = max(1, V59_TECHNIQUE_FLASH_MS)
    t = 1.0 - remaining / total
    alpha = int(220 * (1.0 - max(0.0, (t - 0.60) / 0.40)))
    name = v59_name(technique_id)
    text = oyun_kucuk_font.render(name.upper(), True, (224, 215, 220))
    sub = mini_font.render(bt("TEKNİK", "TECHNIQUE"), True, (136, 124, 133))
    width = max(176, text.get_width() + 28)
    height = 48
    x = GENISLIK // 2 - width // 2
    y = YUKSEKLIK - 146
    layer = pygame.Surface((width, height), pygame.SRCALPHA)
    pygame.draw.rect(
        layer,
        (7, 5, 8, min(205, alpha)),
        layer.get_rect(),
        border_radius=4,
    )
    pygame.draw.rect(
        layer,
        (93, 77, 89, min(175, alpha)),
        layer.get_rect(),
        width=1,
        border_radius=4,
    )
    # Ağır UI: sol metal blok + ince koyu kırmızı progress kesiği.
    pygame.draw.rect(
        layer,
        (39, 31, 39, min(220, alpha)),
        pygame.Rect(0, 0, 9, height),
    )
    progress = max(0.0, min(1.0, remaining / total))
    pygame.draw.rect(
        layer,
        (91, 12, 23, min(220, alpha)),
        pygame.Rect(9, height - 3, int((width - 9) * progress), 3),
    )
    text.set_alpha(alpha)
    sub.set_alpha(alpha)
    layer.blit(sub, (16, 7))
    layer.blit(text, (16, 21))
    ekran.blit(layer, (x, y))
# </POTBO_STAGE S1382>

# <POTBO_STAGE S1826>


def _v85_fracture_release(self, impulse=(1.0, 0.0), power=1.0, seed=0):
    if self.released:
        return
    self.released = True
    rng = random.Random(int(seed) ^ 0x85A17)
    base = v84_safe_vector(impulse).normalize()
    width, height = self.size
    center = pygame.Vector2(width * 0.5, height * 0.5)
    for index, fragment in enumerate(self.fragments):
        v85_fragment_runtime_defaults(fragment)
        radial = fragment.centroid() - center
        if radial.length_squared() <= 1e-8:
            radial = base.rotate(rng.uniform(-110.0, 110.0))
        else:
            radial = radial.normalize()
        direction = v84_safe_vector(radial * 0.58 + base * 0.42).normalize()
        if fragment.released:
            # Already severed pieces keep their ground position; the final impact
            # adds momentum instead of snapping them back into the source sprite.
            fragment.velocity += direction * rng.uniform(150.0, 310.0) * float(power)
            fragment.vertical_velocity = max(
                fragment.vertical_velocity,
                rng.uniform(82.0, 190.0) * float(power),
            )
            fragment.angular_velocity += rng.uniform(-520.0, 520.0)
            fragment.settled = False
            continue
        v85_fragment_launch(
            fragment,
            direction,
            rng.uniform(190.0, 430.0) * float(power),
            rng.uniform(115.0, 270.0) * float(power),
            rng.uniform(-720.0, 720.0),
            delay=index * 0.006,
        )
# </POTBO_STAGE S1826>

# <POTBO_STAGE S1931>


def v86_root_draw(state, now):
    surface = state.root_surface
    if surface is None:
        return
    anchor = v86_body_anchor_screen(state)
    width, height = state.base_size
    fall_progress = 0.0
    if state.fall_started_ms > 0:
        fall_progress = v84_clamp01(
            (int(now) - int(state.fall_started_ms))
            / max(1.0, float(state.fall_duration_ms))
        )
    shadow_width = 11.0 + width * (0.19 + fall_progress * 0.31)
    v86_ground_shadow(
        (anchor.x, anchor.y + 2.0),
        shadow_width,
        2.5 + fall_progress * 2.4,
    )
    image = surface
    if abs(float(state.body_rotation)) > 0.01:
        image = pygame.transform.rotate(image, float(state.body_rotation))
    center = (
        int(round(anchor.x)),
        int(round(anchor.y - height * (0.50 - 0.36 * fall_progress))),
    )
    ekran.blit(image, image.get_rect(center=center))
    if state.burning_root:
        flame_count = 4 if fall_progress > 0.75 else 3
        for index in range(flame_count):
            offset = (index - (flame_count - 1) * 0.5) * max(5.0, width * 0.22)
            v86_flame_draw(
                (center[0] + offset, center[1] + height * 0.20),
                5.0 + (index % 2) * 1.7,
                state.seed + index * 13,
                now,
            )
# </POTBO_STAGE S1931>

# <POTBO_STAGE S1951>


V87_GROUND_FIRE_SPRITES = v87_ground_fire_frames_from_embedded()
# </POTBO_STAGE S1951>

# <POTBO_STAGE S1955>


def v86_flame_draw(center, size, seed, now):
    # This signature is used by intact burning bodies, bomb fragments and organs.
    # Quantised pulse keeps the atlas crisp and cacheable instead of resampling it
    # to a different blurry size every frame.
    pulse = ((int(now) // 78 + abs(int(seed)) * 3) % 5) - 2
    height = max(8, int(round(float(size) * 4.05)) + pulse)
    image = v87_death_fire_sprite(height, seed, 242)
    if image is None:
        return
    x = int(round(float(center[0])))
    y = int(round(float(center[1]) + (pulse & 1)))
    ekran.blit(image, image.get_rect(midbottom=(x, y)))
# </POTBO_STAGE S1955>

# <POTBO_STAGE S1963>


# A detached bite remains connected, but its boundary can inherit one-pixel
# filaments from a narrow source sprite.  Grow only candidates touching at least
# two detached pixels; this keeps asymmetry while producing a more solid piece.
_v87_bite_mask_original = v86_bite_mask
# </POTBO_STAGE S1963>

# <POTBO_STAGE S2059>

# Only grounded flame tongues are selected.  The three explosion-cloud motifs
# in the first row and every burnt-body/skeleton sprite are intentionally
# excluded; a patch therefore never morphs into an explosion or a corpse.
V89_GROUND_FIRE_RECTS = (
    (8, 34, 23, 30),
    (29, 33, 30, 42),
    (58, 38, 39, 28),
    (93, 28, 38, 35),
    (0, 64, 24, 44),
    (22, 72, 26, 47),
    (45, 69, 41, 46),
    (70, 59, 22, 32),
    (89, 61, 25, 27),
)
# </POTBO_STAGE S2059>

# <POTBO_STAGE S2065>
v89_footprint_image_cache = {}
# </POTBO_STAGE S2065>

# <POTBO_STAGE S2089>


# ---------------------------------------------------------
# CURATED GROUND FIRE + ATTACHED SMALL-FLAME DEATH SPRITES
# ---------------------------------------------------------
_v89_ground_fire_init_raw = GroundFirePatch.__init__
# </POTBO_STAGE S2089>

# <POTBO_STAGE S2103>


def v89_tight_icon(item_id, target_size):
    source = ITEM_RESIMLERI.get(item_id)
    if source is None:
        return None
    width, height = max(1, int(target_size[0])), max(1, int(target_size[1]))
    key = (str(item_id), width, height)
    cached = v89_icon_cache.get(key)
    if cached is not None:
        return cached
    try:
        bounds = source.get_bounding_rect(min_alpha=3)
    except (AttributeError, TypeError):
        bounds = source.get_rect()
    if bounds.width <= 0 or bounds.height <= 0:
        return None
    cropped = source.subsurface(bounds).copy().convert_alpha()
    scale = min(width / float(cropped.get_width()), height / float(cropped.get_height()))
    size = (
        max(1, int(round(cropped.get_width() * scale))),
        max(1, int(round(cropped.get_height() * scale))),
    )
    image = pygame.transform.scale(cropped, size).convert_alpha()
    if len(v89_icon_cache) >= 192:
        for old_key in list(v89_icon_cache)[:48]:
            v89_icon_cache.pop(old_key, None)
    v89_icon_cache[key] = image
    return image
# </POTBO_STAGE S2103>

# <POTBO_STAGE S2116>
V89_STARTUP_OK = all(
    (
        V89_STARTUP_CONTRACT["title"] == "Path of the Bloodied One",
        V89_STARTUP_CONTRACT["assets"]["ground_fire_frames"] >= 7,
        V89_STARTUP_CONTRACT["assets"]["small_fire_frames"] == 5,
        V89_STARTUP_CONTRACT["ecology"]["rat_cap"] == 3,
        V89_STARTUP_CONTRACT["blood"]["permanent"],
        not V89_STARTUP_CONTRACT["blood"]["ecology_deletes_stains"],
        not V89_STARTUP_CONTRACT["ui"]["modern_cut_corners"],
    )
)
# </POTBO_STAGE S2116>

# <POTBO_STAGE S2180>


def v90_draco_transformed(frame, height, direction):
    if frame is None:
        return None
    direction = pygame.Vector2(direction)
    if direction.length_squared() <= 1e-8:
        direction = pygame.Vector2(1.0, 0.0)
    angle = int(round(-math.degrees(math.atan2(direction.y, direction.x)) / 5.0)) * 5
    height = max(5, int(round(height)))
    ratio = frame.get_width() / max(1.0, float(frame.get_height()))
    size = (max(3, int(round(height * ratio))), height)
    key = (id(frame), size, angle)
    image = v90_draco_transform_cache.get(key)
    if image is None:
        image = pygame.transform.scale(frame, size).convert_alpha()
        if angle:
            image = pygame.transform.rotate(image, angle).convert_alpha()
        if len(v90_draco_transform_cache) >= 320:
            for old_key in list(v90_draco_transform_cache)[:80]:
                v90_draco_transform_cache.pop(old_key, None)
        v90_draco_transform_cache[key] = image
    return image


def v90_mask_tint(image, color, alpha):
    alpha_bucket = max(0, min(255, int(round(float(alpha) / 16.0)) * 16))
    key = (id(image), tuple(color[:3]), alpha_bucket)
    tinted = v90_draco_glow_cache.get(key)
    if tinted is None:
        mask = pygame.mask.from_surface(image, 8)
        tinted = mask.to_surface(
            setcolor=(*tuple(int(v) for v in color[:3]), alpha_bucket),
            unsetcolor=(0, 0, 0, 0),
        ).convert_alpha()
        if len(v90_draco_glow_cache) >= 480:
            for old_key in list(v90_draco_glow_cache)[:120]:
                v90_draco_glow_cache.pop(old_key, None)
        v90_draco_glow_cache[key] = tinted
    return tinted
# </POTBO_STAGE S2180>

# <POTBO_STAGE S2182>


def v90_draco_draw(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    state = v90_draco_state
    if state.active and V90_DRACO_FRAMES:
        age = max(0, int(now) - int(state.phase_started_ms))
        full = V90_DRACO_FRAMES[-1]
        if state.phase == "cast":
            progress = v90_clamp(age / max(1.0, float(V90_DRACO_CAST_MS)))
            index = min(
                len(V90_DRACO_FRAMES) - 1,
                int(progress * len(V90_DRACO_FRAMES)),
            )
            v90_draw_draco_sprite(
                state.position,
                V90_DRACO_FRAMES[index],
                24 + 26 * progress,
                state.direction,
                alpha=int(130 + 125 * progress),
                glow_strength=0.72,
            )
        elif state.phase == "flight":
            for trail_index, (position, frame_index, born) in enumerate(state.trail):
                trail_age = max(0, int(now) - int(born))
                alpha = max(0, int(104 * (1.0 - trail_age / 430.0)))
                if alpha <= 0:
                    continue
                v90_draw_draco_sprite(
                    position,
                    V90_DRACO_FRAMES[max(0, min(len(V90_DRACO_FRAMES) - 1, frame_index))],
                    46,
                    state.direction,
                    alpha=alpha,
                    body=False,
                    glow_strength=0.55,
                )
            index = 4 + (int(now) // 72) % max(1, len(V90_DRACO_FRAMES) - 4)
            v90_draw_draco_sprite(
                state.position,
                V90_DRACO_FRAMES[min(len(V90_DRACO_FRAMES) - 1, index)],
                50,
                state.direction,
                glow_strength=0.90,
            )
        elif state.phase == "dissipate":
            progress = v90_clamp(age / 300.0)
            v90_draw_draco_sprite(
                state.position,
                full,
                48 * (1.0 - 0.62 * progress),
                state.direction,
                alpha=int(220 * (1.0 - progress)),
                body=False,
                glow_strength=0.55,
            )
        elif state.target_valid():
            center = v90_actor_center(state.target)
            if state.phase == "bite":
                progress = v90_smoothstep(age / max(1.0, V90_DRACO_BITE_MS))
                position = center - state.direction * (34.0 * (1.0 - progress))
                v90_draw_draco_sprite(
                    position,
                    full,
                    58,
                    state.direction,
                    glow_strength=1.0,
                )
            elif state.phase == "coil":
                progress = v90_smoothstep(age / max(1.0, V90_DRACO_COIL_MS))
                for segment in range(4):
                    lag = segment * 0.15
                    local = v90_clamp(progress - lag)
                    angle = -150.0 + local * 190.0 - segment * 31.0
                    radial = 33.0 - segment * 4.2
                    offset = pygame.Vector2(radial, 0.0).rotate(angle)
                    tangent = offset.rotate(90.0)
                    v90_draw_draco_sprite(
                        center + offset,
                        full,
                        39 + (3 - segment) * 2,
                        tangent,
                        alpha=255 if segment == 0 else 142 - segment * 20,
                        body=segment == 0,
                        glow_strength=0.84,
                    )
            elif state.phase == "collapse":
                progress = v90_smoothstep(age / max(1.0, V90_DRACO_COLLAPSE_MS))
                for segment in range(3):
                    phase = progress + segment * 0.10
                    radial = max(0.0, 31.0 * (1.0 - phase))
                    angle = 45.0 + phase * 250.0 + segment * 78.0
                    offset = pygame.Vector2(radial, 0.0).rotate(angle)
                    v90_draw_draco_sprite(
                        center + offset,
                        full,
                        max(8.0, 42.0 * (1.0 - phase * 0.78)),
                        offset.rotate(90.0) if offset.length_squared() > 0.1 else state.direction,
                        alpha=max(32, int(210 * (1.0 - phase))),
                        body=False,
                        glow_strength=0.70,
                    )
            elif state.phase == "silence":
                # The deliberate half-second lacuna has only a few inward embers.
                if V89_SMALL_FIRE_FRAMES and (age // 90) % 3 == 0:
                    frame = V89_SMALL_FIRE_FRAMES[(age // 90) % len(V89_SMALL_FIRE_FRAMES)]
                    v90_draw_draco_sprite(
                        center,
                        frame,
                        8,
                        (1.0, 0.0),
                        alpha=72,
                        body=False,
                        glow_strength=0.28,
                    )
            elif state.phase == "rupture":
                v90_draw_rupture(
                    center,
                    age / max(1.0, float(V90_DRACO_RUPTURE_MS)),
                    state.seed,
                )

    for status in v90_calcinatio.values():
        if not v90_actor_alive(status.actor):
            continue
        center = v90_actor_center(status.actor)
        elapsed = max(0, int(now) - int(status.started_ms))
        if V89_SMALL_FIRE_FRAMES:
            frame = V89_SMALL_FIRE_FRAMES[(elapsed // 92 + status.seed) % len(V89_SMALL_FIRE_FRAMES)]
            for offset_x, phase in ((-8.0, 0), (7.0, 2)):
                v90_draw_draco_sprite(
                    center + pygame.Vector2(offset_x, 5.0),
                    frame,
                    11 + phase,
                    (1.0, 0.0),
                    alpha=148,
                    body=True,
                    glow_strength=0.42,
                )

    for ember in v90_embers:
        age = max(0, int(now) - int(ember.born_ms))
        fade = 1.0 - v90_clamp(age / max(1.0, float(ember.ttl_ms)))
        point = (int(dunya_ekran_x(ember.x)), int(dunya_ekran_y(ember.y)))
        length = max(1, int(round(ember.size * KAMERA_YAKINLASTIRMA)))
        color = (
            255,
            max(60, min(210, int(88 + 120 * fade))),
            8,
            int(220 * fade),
        )
        layer = pygame.Surface((length + 4, length * 3 + 4), pygame.SRCALPHA)
        pygame.draw.line(
            layer,
            color,
            (layer.get_width() // 2, layer.get_height() - 2),
            (layer.get_width() // 2, 2),
            max(1, length),
        )
        ekran.blit(layer, layer.get_rect(center=point))
# </POTBO_STAGE S2182>

# <POTBO_STAGE S2223>


def v91_oriented_small_flame(
    frame, height, direction_name, alpha=255, tint=None
):
    height = max(3, int(round(height)))
    alpha_bucket = max(16, min(255, int(round(alpha / 16.0)) * 16))
    key = (
        id(frame),
        height,
        str(direction_name),
        alpha_bucket,
        tuple(tint) if tint else None,
    )
    image = v91_small_flame_transform_cache.get(key)
    if image is not None:
        return image
    ratio = frame.get_width() / max(1.0, float(frame.get_height()))
    image = pygame.transform.scale(
        frame, (max(2, int(round(height * ratio))), height)
    )
    if direction_name == "up":
        image = pygame.transform.rotate(image, 180)
    elif direction_name == "right":
        image = pygame.transform.rotate(image, 90)
    elif direction_name == "left":
        image = pygame.transform.rotate(image, -90)
    if tint is not None:
        mask = pygame.mask.from_surface(image, 2)
        image = mask.to_surface(
            setcolor=(*tuple(tint[:3]), alpha_bucket),
            unsetcolor=(0, 0, 0, 0),
        ).convert_alpha()
    elif alpha_bucket < 255:
        image = image.copy()
        image.set_alpha(alpha_bucket)
    if len(v91_small_flame_transform_cache) >= 240:
        for old in list(v91_small_flame_transform_cache)[:60]:
            v91_small_flame_transform_cache.pop(old, None)
    v91_small_flame_transform_cache[key] = image
    return image
# </POTBO_STAGE S2223>

# <POTBO_STAGE S2226>


def v91_impact_flame_cluster(seed, progress, zoom):
    if not V89_SMALL_FIRE_FRAMES:
        return None
    bucket = max(0, min(7, int(progress * 8.0)))
    zoom_bucket = max(4, min(24, int(round(float(zoom) * 8.0))))
    key = (int(seed) % 24, bucket, zoom_bucket)
    cached = v91_impact_cluster_cache.get(key)
    if cached is not None:
        return cached
    scale = zoom_bucket / 8.0
    surface = pygame.Surface(
        (int(118 * scale), int(72 * scale)), pygame.SRCALPHA
    )
    rng = random.Random(key[0] * 1907 + bucket * 313)
    phase = math.sin(min(1.0, progress) * math.pi)
    for index in range(9):
        frame = V89_SMALL_FIRE_FRAMES[
            (bucket + index * 2) % len(V89_SMALL_FIRE_FRAMES)
        ]
        height = max(
            4, int(round((8 + rng.uniform(1, 13) * phase) * scale))
        )
        image = v91_oriented_small_flame(
            frame, height, "down", 220 - index * 8
        )
        x = int(
            surface.get_width() * 0.5 + rng.uniform(-44, 44) * scale
        )
        y = int(surface.get_height() - rng.uniform(4, 24) * scale)
        surface.blit(image, image.get_rect(midbottom=(x, y)))
    if len(v91_impact_cluster_cache) >= 96:
        for old in list(v91_impact_cluster_cache)[:24]:
            v91_impact_cluster_cache.pop(old, None)
    v91_impact_cluster_cache[key] = surface
    return surface
# </POTBO_STAGE S2226>

# <POTBO_STAGE S2229>


def v91_ground_fire_cluster(
    seed, scale_value, zoom, frame_bucket, alpha_bucket
):
    frames = V89_SMALL_FIRE_FRAMES
    if not frames:
        return None
    motif = abs(int(seed)) % 28
    scale_bucket = max(
        5, min(14, int(round(float(scale_value) * 10.0)))
    )
    zoom_bucket = max(
        4, min(24, int(round(float(zoom) * 8.0)))
    )
    alpha_bucket = max(1, min(8, int(alpha_bucket)))
    key = (
        motif,
        scale_bucket,
        zoom_bucket,
        int(frame_bucket) % len(frames),
        alpha_bucket,
    )
    cached = v91_ground_cluster_cache.get(key)
    if cached is not None:
        return cached
    factor = (scale_bucket / 10.0) * (zoom_bucket / 8.0)
    width = max(22, int(round(72 * factor)))
    height = max(14, int(round(35 * factor)))
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    rng = random.Random(motif * 1613 + scale_bucket * 101)
    count = 8
    for index in range(count):
        frame = frames[
            (frame_bucket + index * 2 + motif) % len(frames)
        ]
        flame_h = max(
            7, int(round(rng.uniform(13.0, 25.0) * factor))
        )
        image = v91_oriented_small_flame(
            frame,
            flame_h,
            "down",
            int(255 * alpha_bucket / 8.0),
        )
        x = int(
            round(
                (
                    0.10
                    + 0.80 * (index / max(1, count - 1))
                )
                * width
                + rng.uniform(-3.0, 3.0) * factor
            )
        )
        y = height - int(round(rng.uniform(0.0, 5.0) * factor))
        surface.blit(image, image.get_rect(midbottom=(x, y)))
    if len(v91_ground_cluster_cache) >= 180:
        for old in list(v91_ground_cluster_cache)[:45]:
            v91_ground_cluster_cache.pop(old, None)
    v91_ground_cluster_cache[key] = surface
    return surface
# </POTBO_STAGE S2229>

# <POTBO_STAGE S2249>


def v91_death_flame_cluster(
    seed, frame_bucket, zoom
):
    if not V89_SMALL_FIRE_FRAMES:
        return None
    zoom_bucket = max(
        4, min(20, int(round(float(zoom) * 8.0)))
    )
    key = (
        abs(int(seed)) % 16,
        int(frame_bucket)
        % len(V89_SMALL_FIRE_FRAMES),
        zoom_bucket,
    )
    cached = v91_death_flame_cache.get(key)
    if cached is not None:
        return cached
    factor = zoom_bucket / 8.0
    surface = pygame.Surface(
        (int(142 * factor), int(92 * factor)),
        pygame.SRCALPHA,
    )
    rng = random.Random(key[0] * 1187)
    # Forty authored sprite flames, composited once and drawn as one cached blit.
    for index in range(40):
        frame = V89_SMALL_FIRE_FRAMES[
            (
                frame_bucket
                + index * 3
                + key[0]
            )
            % len(V89_SMALL_FIRE_FRAMES)
        ]
        height = max(
            4,
            int(
                round(
                    rng.uniform(8.0, 21.0) * factor
                )
            ),
        )
        image = v91_oriented_small_flame(
            frame,
            height,
            "down",
            255,
            tint=V91_DEATH_BODY,
        )
        angle = rng.uniform(0.0, math.tau)
        radius = rng.uniform(4.0, 55.0) * factor
        x = int(
            surface.get_width() * 0.5
            + math.cos(angle) * radius
        )
        y = int(
            surface.get_height() * 0.68
            + math.sin(angle) * radius * 0.43
        )
        surface.blit(
            image, image.get_rect(midbottom=(x, y))
        )
    if len(v91_death_flame_cache) >= 80:
        for old in list(v91_death_flame_cache)[:20]:
            v91_death_flame_cache.pop(old, None)
    v91_death_flame_cache[key] = surface
    return surface
# </POTBO_STAGE S2249>

# <POTBO_STAGE S2319>


@dataclass
class V92ChainHead:
    image: Any
    position: pygame.Vector2
    velocity: pygame.Vector2
    z: float = 8.0
    vz: float = 44.0
    rotation: float = 0.0
    angular: float = 110.0
# </POTBO_STAGE S2319>

# <POTBO_STAGE S2352>


def _v94_normalized_crop(sheet, nx, ny, nw, nh):
    sw, sh = sheet.get_size()
    rect = pygame.Rect(
        int(round(sw * nx)),
        int(round(sh * ny)),
        max(1, int(round(sw * nw))),
        max(1, int(round(sh * nh))),
    ).clip(sheet.get_rect())
    if rect.width <= 0 or rect.height <= 0:
        return None
    return _v94_trim(sheet.subsurface(rect).copy())
# </POTBO_STAGE S2352>

# <POTBO_STAGE S2379>


def _v95_pixel_actor(frame, target_h):
    if frame is None:
        return None
    target_h = max(1, int(target_h))
    scale = target_h / max(1.0, float(frame.get_height()))
    target_w = max(1, int(round(frame.get_width() * scale)))
    # Nearest-neighbour is intentional: these are pixel sprites.
    return pygame.transform.scale(frame, (target_w, target_h))
# </POTBO_STAGE S2379>

# <POTBO_STAGE S2386>


def v90_draco_draw(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    state = v90_draco_state

    if state.active and V90_DRACO_FRAMES:
        age = max(0, int(now) - int(state.phase_started_ms))
        full = V90_DRACO_FRAMES[-1]

        if state.phase == "cast":
            p = v90_clamp(age / max(1.0, float(V90_DRACO_CAST_MS)))
            # Natural ignition: spark -> recognisable head/body -> full dragon.
            formed = v90_smoothstep(p)
            thresholds = (0.00, 0.07, 0.15, 0.25, 0.38, 0.52, 0.67, 0.82, 0.94)
            index = 0
            for i, threshold in enumerate(thresholds):
                if formed >= threshold:
                    index = min(i, len(V90_DRACO_FRAMES) - 1)
            height = 18.0 + 35.0 * (formed ** 0.82)
            v90_draw_draco_sprite(
                state.position - state.direction * (7.0 * (1.0 - formed)),
                V90_DRACO_FRAMES[index],
                height,
                state.direction,
                alpha=int(92 + 163 * formed),
                glow_strength=0.84 + 0.34 * formed,
            )
        elif state.phase == "flight":
            for trail_index, (position, _frame_index, born) in enumerate(state.trail):
                trail_age = max(0, int(now) - int(born))
                alpha = max(0, int(172 * (1.0 - trail_age / 300.0)))
                if alpha <= 0:
                    continue
                if V95_DRACO_FLIGHT_INDICES:
                    safe_index = V95_DRACO_FLIGHT_INDICES[
                        (trail_index + int(born) // 64) % len(V95_DRACO_FLIGHT_INDICES)
                    ]
                else:
                    safe_index = len(V90_DRACO_FRAMES) - 1
                v90_draw_draco_sprite(
                    position,
                    V90_DRACO_FRAMES[safe_index],
                    48,
                    state.direction,
                    alpha=alpha,
                    body=False,
                    glow_strength=1.10,
                )

            if V95_DRACO_FLIGHT_INDICES:
                core_index = V95_DRACO_FLIGHT_INDICES[
                    (int(now) // 64) % len(V95_DRACO_FLIGHT_INDICES)
                ]
            else:
                core_index = len(V90_DRACO_FRAMES) - 1
            v90_draw_draco_sprite(
                state.position,
                V90_DRACO_FRAMES[core_index],
                53,
                state.direction,
                glow_strength=1.28,
            )

        elif state.phase == "dissipate":
            p = v90_clamp(age / 300.0)
            v90_draw_draco_sprite(
                state.position,
                full,
                50 * (1.0 - 0.55 * p),
                state.direction,
                alpha=int(238 * (1.0 - p)),
                body=False,
                glow_strength=0.90,
            )

        elif state.target_valid():
            center = v90_actor_center(state.target)
            if state.phase == "bite":
                p = v90_smoothstep(age / max(1.0, V90_DRACO_BITE_MS))
                position = center - state.direction * (34.0 * (1.0 - p))
                v90_draw_draco_sprite(
                    position,
                    full,
                    60,
                    state.direction,
                    glow_strength=1.30,
                )
            elif state.phase == "coil":
                p = v90_smoothstep(age / max(1.0, V90_DRACO_COIL_MS))
                for segment in range(4):
                    local = v90_clamp(p - segment * 0.15)
                    angle = -150.0 + local * 190.0 - segment * 31.0
                    radial = 33.0 - segment * 4.2
                    offset = pygame.Vector2(radial, 0.0).rotate(angle)
                    tangent = offset.rotate(90.0)
                    v90_draw_draco_sprite(
                        center + offset,
                        full,
                        41 + (3 - segment) * 2,
                        tangent,
                        alpha=255 if segment == 0 else 166 - segment * 18,
                        body=segment == 0,
                        glow_strength=1.12,
                    )
            elif state.phase == "collapse":
                p = v90_smoothstep(age / max(1.0, V90_DRACO_COLLAPSE_MS))
                for segment in range(3):
                    phase = p + segment * 0.10
                    radial = max(0.0, 31.0 * (1.0 - phase))
                    angle = 45.0 + phase * 250.0 + segment * 78.0
                    offset = pygame.Vector2(radial, 0.0).rotate(angle)
                    v90_draw_draco_sprite(
                        center + offset,
                        full,
                        max(9.0, 44.0 * (1.0 - phase * 0.76)),
                        offset.rotate(90.0) if offset.length_squared() > 0.1 else state.direction,
                        alpha=max(38, int(230 * (1.0 - phase))),
                        body=False,
                        glow_strength=1.0,
                    )
            elif state.phase == "silence":
                if V89_SMALL_FIRE_FRAMES and (age // 90) % 3 == 0:
                    frame = V89_SMALL_FIRE_FRAMES[(age // 90) % len(V89_SMALL_FIRE_FRAMES)]
                    v90_draw_draco_sprite(
                        center,
                        frame,
                        8,
                        (1.0, 0.0),
                        alpha=80,
                        body=False,
                        glow_strength=0.35,
                    )
            elif state.phase == "rupture":
                v90_draw_rupture(
                    center,
                    age / max(1.0, float(V90_DRACO_RUPTURE_MS)),
                    state.seed,
                )

    for status in v90_calcinatio.values():
        if not v90_actor_alive(status.actor):
            continue
        center = v90_actor_center(status.actor)
        elapsed = max(0, int(now) - int(status.started_ms))
        if V89_SMALL_FIRE_FRAMES:
            frame = V89_SMALL_FIRE_FRAMES[
                (elapsed // 92 + status.seed) % len(V89_SMALL_FIRE_FRAMES)
            ]
            for offset_x, phase in ((-8.0, 0), (7.0, 2)):
                v90_draw_draco_sprite(
                    center + pygame.Vector2(offset_x, 5.0),
                    frame,
                    11 + phase,
                    (1.0, 0.0),
                    alpha=150,
                    body=True,
                    glow_strength=0.48,
                )

    # Cached ember sprite buckets avoid allocating a new alpha Surface for every
    # ember on every frame.
    for ember in v90_embers:
        age = max(0, int(now) - int(ember.born_ms))
        fade = 1.0 - v90_clamp(age / max(1.0, float(ember.ttl_ms)))
        if fade <= 0.0:
            continue
        point = (
            int(dunya_ekran_x(ember.x)),
            int(dunya_ekran_y(ember.y)),
        )
        size_bucket = max(1, min(5, int(round(ember.size * KAMERA_YAKINLASTIRMA))))
        fade_bucket = max(1, min(8, int(round(fade * 8.0))))
        key = (size_bucket, fade_bucket)
        layer = v95_ember_sprite_cache.get(key)
        if layer is None:
            alpha = int(225 * fade_bucket / 8.0)
            length = size_bucket
            layer = pygame.Surface(
                (length + 4, length * 3 + 4),
                pygame.SRCALPHA,
            ).convert_alpha()
            pygame.draw.line(
                layer,
                (255, 105 + fade_bucket * 11, 8, alpha),
                (layer.get_width() // 2, layer.get_height() - 2),
                (layer.get_width() // 2, 2),
                max(1, length),
            )
            v95_ember_sprite_cache[key] = layer
        ekran.blit(layer, layer.get_rect(center=point))
# </POTBO_STAGE S2386>

# <POTBO_STAGE S2418>
V98_MANA_ICON_ADAYLARI = (
    os.path.join(ASSETS, "ui", "mana_icon.png"),
    os.path.join(BASE_DIR, "ui", "mana_icon.png"),
)
# </POTBO_STAGE S2418>

# <POTBO_STAGE S2422>


def _v98_status_icon_scaled(source, size):
    if source is None:
        return None
    size = max(8, int(size))
    key = (id(source), size)
    cached = V98_STATUS_ICON_CACHE.get(key)
    if cached is not None:
        return cached
    scale = min(size / max(1.0, float(source.get_width())), size / max(1.0, float(source.get_height())))
    width = max(1, int(round(source.get_width() * scale)))
    height = max(1, int(round(source.get_height() * scale)))
    image = pygame.transform.smoothscale(source, (width, height)).convert_alpha()
    V98_STATUS_ICON_CACHE[key] = image
    return image
# </POTBO_STAGE S2422>

# <POTBO_STAGE S2425>


# ---------------------------------------------------------
# UNIVERSAL FIRE ATLAS
# İlk üç sprite bütün yerde yanan ateşlerin canonical animasyonudur.
# Canonical öneri: assets/effects/fire/universal_fire.png
# Verilen orijinal dosya adı da fallback olarak desteklenir.
# ---------------------------------------------------------
V98_UNIVERSAL_FIRE_ADAYLARI = (
    os.path.join(ASSETS, "effects", "fire", "universal_fire.png"),
    os.path.join(ASSETS, "effects", "fire", "fire.png"),
    os.path.join(ASSETS, "spells", "fire", "universal_fire.png"),
    os.path.join(BASE_DIR, "PlayStation - Tales of Destiny - Miscellaneous - Fire (1).png"),
    os.path.join(BASE_DIR, "PlayStation - Tales of Destiny - Miscellaneous - Fire.png"),
)
V98_UNIVERSAL_FIRE_YOLU = mevcut_ilk_dosya(V98_UNIVERSAL_FIRE_ADAYLARI)


def _v98_universal_fire_frames_load():
    if not V98_UNIVERSAL_FIRE_YOLU:
        return []
    try:
        sheet = pygame.image.load(V98_UNIVERSAL_FIRE_YOLU).convert()
    except (pygame.error, OSError):
        return []

    # 241x147 atlas. İlk üç alev 32 px hücrelerde, üst sıradadır.
    specs = (
        (0, 0, 32, 35),
        (32, 0, 32, 35),
        (64, 0, 32, 35),
    )
    bg = sheet.get_at((0, 0))[:3]
    frames = []
    for spec in specs:
        rect = pygame.Rect(spec).clip(sheet.get_rect())
        if rect.width <= 0 or rect.height <= 0:
            continue
        source = sheet.subsurface(rect).copy()
        frame = pygame.Surface(source.get_size(), pygame.SRCALPHA)
        frame.blit(source, (0, 0))
        pixels = pygame.PixelArray(frame)
        try:
            for x in range(frame.get_width()):
                for y in range(frame.get_height()):
                    c = frame.unmap_rgb(pixels[x, y])
                    if (
                        abs(int(c.r) - int(bg[0])) <= 3
                        and abs(int(c.g) - int(bg[1])) <= 3
                        and abs(int(c.b) - int(bg[2])) <= 3
                    ):
                        pixels[x, y] = (0, 0, 0, 0)
        finally:
            del pixels
        frame = _v94_trim(frame)
        if frame is not None:
            frames.append(frame)
    return frames
# </POTBO_STAGE S2425>

# <POTBO_STAGE S2428>


def _v98_fire_frame_image(frame, target_h, alpha=255):
    if frame is None:
        return None
    target_h = max(4, int(target_h))
    alpha = max(0, min(255, int(alpha)))
    alpha_bucket = max(0, min(15, int(round(alpha / 17.0))))
    key = (id(frame), target_h, alpha_bucket)
    cached = V98_FIRE_SCALE_CACHE.get(key)
    if cached is not None:
        return cached
    scale = target_h / max(1.0, float(frame.get_height()))
    target_w = max(1, int(round(frame.get_width() * scale)))
    image = pygame.transform.scale(frame, (target_w, target_h)).convert_alpha()
    image.set_alpha(alpha_bucket * 17)
    if len(V98_FIRE_SCALE_CACHE) >= 160:
        for old_key in list(V98_FIRE_SCALE_CACHE)[:40]:
            V98_FIRE_SCALE_CACHE.pop(old_key, None)
    V98_FIRE_SCALE_CACHE[key] = image
    return image
# </POTBO_STAGE S2428>

# <POTBO_STAGE S2445>


# ---------------------------------------------------------
# FIREBALL: IMPACT-ONLY FIRE FIELD
# No projectile trail. A dense fire bed is created only at detonation, with all
# flame centers kept well inside the blast presentation radius so sprite/glow
# edges do not visibly spill outside the impact zone.
# ---------------------------------------------------------
# Restore the projectile update captured before V98 added trail spawning.
FireMagicProjectile.guncelle = _v98_fire_projectile_update_raw
# </POTBO_STAGE S2445>

# <POTBO_STAGE S2481>

# ---------------------------------------------------------
# UI ICON CONTRACT
# Reinald'ın YETENEK ve GELİŞTİR sayfaları aynı gerçek ikon motorunu kullanır.
# Dosyalar hem canonical ui klasöründe hem de eski/fallback konumlarda aranır.
# ---------------------------------------------------------
def _v102_trim_alpha(image):
    if image is None:
        return None
    image = image.copy().convert_alpha()
    bounds = image.get_bounding_rect(min_alpha=2)
    if bounds.width <= 0 or bounds.height <= 0:
        return None
    return image.subsurface(bounds).copy().convert_alpha()
# </POTBO_STAGE S2481>

# <POTBO_STAGE S2488>


def _v102_upgrade_icon_draw(kind, rect, alpha=255):
    rect = pygame.Rect(rect)
    image = V102_UPGRADE_ICONS.get(kind)
    if image is None:
        image = _v102_upgrade_icon_reload(kind)

    if image is not None:
        fitted = resmi_oranli_sigdir(image, rect, 0, 0.90, True)
        if fitted is not None:
            if int(alpha) < 255:
                fitted = fitted.copy()
                fitted.set_alpha(max(0, min(255, int(alpha))))
            ekran.blit(fitted, fitted.get_rect(center=rect.center))
            return True

    fallback = _v102_upgrade_fallback(kind, min(rect.width, rect.height))
    if int(alpha) < 255:
        fallback.set_alpha(max(0, min(255, int(alpha))))
    ekran.blit(fallback, fallback.get_rect(center=rect.center))
    return False
# </POTBO_STAGE S2488>

# <POTBO_STAGE S2494>


def yazi_yaz(metin, x, y, renk=BEYAZ, font=normal_font, ortala=False):
    metin = str(metin)
    key = (id(font), metin, _v103_renk_anahtari(renk))
    goruntu = V103_TEXT_CACHE.get(key)
    if goruntu is None:
        goruntu = font.render(metin, True, renk)
        if len(V103_TEXT_CACHE) >= V103_TEXT_CACHE_LIMIT:
            # Dict insertion order gives us a cheap bounded FIFO; avoid a cache
            # clear spike by evicting only the oldest quarter.
            for eski in list(V103_TEXT_CACHE)[: V103_TEXT_CACHE_LIMIT // 4]:
                V103_TEXT_CACHE.pop(eski, None)
        V103_TEXT_CACHE[key] = goruntu

    rect = goruntu.get_rect()
    if ortala:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    ekran.blit(goruntu, rect)
    return rect
# </POTBO_STAGE S2494>

# <POTBO_STAGE S2513>


BloodMaggot.ciz = _v105_maggot_sprite_draw
# </POTBO_STAGE S2513>

# <POTBO_STAGE S2553>


def v106_corona_sprite(frame_index, size, alpha=255):
    if not V106_CORONA_FRAMES:
        return None
    src = V106_CORONA_FRAMES[int(frame_index) % len(V106_CORONA_FRAMES)]
    size = max(4, int(size))
    key = (id(src), size, int(alpha // 24) * 24)
    image = v106_corona_transform_cache.get(key)
    if image is None:
        scale = size / max(1.0, float(max(src.get_width(), src.get_height())))
        dims = (
            max(2, int(round(src.get_width() * scale))),
            max(2, int(round(src.get_height() * scale))),
        )
        image = pygame.transform.scale(src, dims).convert_alpha()
        if alpha < 255:
            image.set_alpha(max(0, min(255, int(alpha))))
        if len(v106_corona_transform_cache) >= 72:
            for old in list(v106_corona_transform_cache)[:18]:
                v106_corona_transform_cache.pop(old, None)
        v106_corona_transform_cache[key] = image
    return image
# </POTBO_STAGE S2553>

# <POTBO_STAGE S2564>


# ---------------------------------------------------------
# CORONA: faster / harsher orbit and white-hot authored silhouettes.
# No external glow surface is used: brightness is clipped to the sprite alpha,
# so the light cannot spill beyond the orb itself. Blue is intentionally removed.
# ---------------------------------------------------------
V106_CORONA_ORBIT_RADIUS = 59.0
# </POTBO_STAGE S2564>

# <POTBO_STAGE S2569>


def v108_corona_white_hot_sprite(frame_index, size, alpha=255):
    base = v106_corona_sprite(frame_index, size, alpha)
    if base is None:
        return None
    alpha_bucket = max(0, min(255, int(alpha // 16) * 16))
    key = (id(base), int(size), alpha_bucket)
    cached = V108_CORONA_BRIGHT_CACHE.get(key)
    if cached is not None:
        return cached

    # RGB_MAX whitens only RGB; original alpha silhouette stays intact.
    hot = base.copy().convert_alpha()
    hot.fill((255, 255, 255), special_flags=pygame.BLEND_RGB_MAX)
    if alpha < 255:
        hot.set_alpha(max(0, min(255, int(alpha))))

    # Internal core bloom. It is drawn onto the same sprite-sized surface, then
    # clipped by the original alpha mask, so it never grows outside the ball.
    inner = pygame.Surface(hot.get_size(), pygame.SRCALPHA).convert_alpha()
    cx, cy = hot.get_width() // 2, hot.get_height() // 2
    r_outer = max(2, int(min(hot.get_size()) * 0.31))
    r_inner = max(1, int(r_outer * 0.47))
    pygame.draw.circle(inner, (255, 255, 255, 205), (cx, cy), r_outer)
    pygame.draw.circle(inner, (255, 255, 255, 255), (cx, cy), r_inner)
    alpha_clip = pygame.mask.from_surface(base, 2).to_surface(
        setcolor=(255, 255, 255, 255),
        unsetcolor=(0, 0, 0, 0),
    ).convert_alpha()
    inner.blit(alpha_clip, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    hot.blit(inner, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)

    if len(V108_CORONA_BRIGHT_CACHE) >= 120:
        for old in list(V108_CORONA_BRIGHT_CACHE)[:30]:
            V108_CORONA_BRIGHT_CACHE.pop(old, None)
    V108_CORONA_BRIGHT_CACHE[key] = hot
    return hot
# </POTBO_STAGE S2569>

# <POTBO_STAGE S2579>

# ---------------------------------------------------------
# CORONA VISUALS
# V108'in neredeyse tamamen beyaza çeviren işlemi geri çekilir: authored sprite
# yeniden okunabilir kalır, fakat iç parlaklık ve küçük bir çevresel ışık halesi korunur.
# ---------------------------------------------------------
V109_CORONA_SPRITE_CACHE = {}
# </POTBO_STAGE S2579>

# <POTBO_STAGE S2581>


def v108_corona_white_hot_sprite(frame_index, size, alpha=255):
    base = v106_corona_sprite(frame_index, size, alpha)
    if base is None:
        return None
    alpha_bucket = max(0, min(255, int(alpha // 16) * 16))
    key = (id(base), int(size), alpha_bucket, "v109")
    cached = V109_CORONA_SPRITE_CACHE.get(key)
    if cached is not None:
        return cached

    # Authored mavi/cam dokusunu görünür bırak; yalnız tüm kanalları dengeli biçimde
    # yükselt. Önceki RGB_MAX beyazlaştırmasına göre çok daha az yıkayıcıdır.
    hot = base.copy().convert_alpha()
    hot.fill((86, 86, 86), special_flags=pygame.BLEND_RGB_ADD)

    # Beyaz merkez yalnız sprite alfa silüetinin içinde kalır.
    inner = pygame.Surface(hot.get_size(), pygame.SRCALPHA).convert_alpha()
    cx, cy = hot.get_width() // 2, hot.get_height() // 2
    r_outer = max(2, int(min(hot.get_size()) * 0.27))
    r_inner = max(1, int(r_outer * 0.44))
    pygame.draw.circle(inner, (255, 255, 255, 92), (cx, cy), r_outer)
    pygame.draw.circle(inner, (255, 255, 255, 146), (cx, cy), r_inner)
    alpha_clip = pygame.mask.from_surface(base, 2).to_surface(
        setcolor=(255, 255, 255, 255),
        unsetcolor=(0, 0, 0, 0),
    ).convert_alpha()
    inner.blit(alpha_clip, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    hot.blit(inner, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)
    if alpha < 255:
        hot.set_alpha(max(0, min(255, int(alpha))))

    if len(V109_CORONA_SPRITE_CACHE) >= 120:
        for old in list(V109_CORONA_SPRITE_CACHE)[:30]:
            V109_CORONA_SPRITE_CACHE.pop(old, None)
    V109_CORONA_SPRITE_CACHE[key] = hot
    return hot
# </POTBO_STAGE S2581>

# <POTBO_STAGE S2634>


_v111_impact_sprite_raw = v110_draw_impact_sprite
# </POTBO_STAGE S2634>

# <POTBO_STAGE S2644>


_v112_impact_raw = v110_draw_impact_sprite
# </POTBO_STAGE S2644>

# <POTBO_STAGE S2650>


# Impact sprite artık bloklu sprite yığınları kullanmaz; yalnız pürüzsüz yerel bloom.
def v110_draw_impact_sprite(center, age_ms):
    return v113_draw_strike_bloom(center, age_ms)
# </POTBO_STAGE S2650>

# <POTBO_STAGE S2659>


# Geometrik top/daire bloom kaldırıldı. Çarpma yeri yalnız düzensiz elektrik saçakları
# ve beyaz doygunlukla okunur.
def v110_draw_impact_sprite(center, age_ms):
    return None
# </POTBO_STAGE S2659>

