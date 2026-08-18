# Path of the Bloodied One — categorized source stages
#
# This file is intentionally executed by core/bootstrap.py in original source order.
# Keeping one shared runtime namespace avoids gameplay regressions while the former
# 90k-line monolith is physically separated by responsibility. Do not import this
# file directly; edit the stage code normally and launch root main.py.

# <POTBO_STAGE S0022>

# Adefonsus'un yeni birleşik sprite sheet'i. Bu asset varsa eski dört-yön
# PNG sisteminin yerine locomotion / normal attack / hold attack dizileri kullanılır.
# Dosya yoksa mevcut karakter sistemi otomatik fallback olarak çalışmaya devam eder.
ADEFONSUS_SHEET_ADAYLARI = [
    os.path.join(ASSETS, "characters", "adefonsus_spriteSheet.png"),
    os.path.join(ASSETS, "characters", "adefonsus_spritesheet.png"),
    os.path.join(BASE_DIR, "adefonsus_spriteSheet.png"),
]
# </POTBO_STAGE S0022>

# <POTBO_STAGE S0031>

# =========================================================
# LOCOMOTION / AMBIENCE / MELEE IMPACT SESLERİ
# =========================================================
# Adefonsus'un sample'ı tam 1 saniyedir ve kendi içinde iki ayak vuruşu taşır.
# Sample yeniden tetiklenmez; yürürken dedicated channel üzerinde loop edilir.
ADEFONSUS_FOOTSTEP_SES_ADAYLARI = [
    os.path.join(ASSETS, "sounds", "adefonsusFootsteps.wav"),
    os.path.join(ASSETS, "sounds", "characters", "adefonsusFootsteps.wav"),
    os.path.join(BASE_DIR, "adefonsusFootsteps.wav"),
]
# </POTBO_STAGE S0031>

# <POTBO_STAGE S0044>

# Bu yollar mevcut_ilk_dosya() tanımlandıktan sonra çözülür.
ADEFONSUS_FOOTSTEP_SES_YOLU = mevcut_ilk_dosya(ADEFONSUS_FOOTSTEP_SES_ADAYLARI)
# </POTBO_STAGE S0044>

# <POTBO_STAGE S0056>

ADEFONSUS_PORTRE_YOLU = os.path.join(ASSETS, "portraits", "adefonsus.png")
# </POTBO_STAGE S0056>

# <POTBO_STAGE S0063>

ADEFONSUS_KART_ADAYLARI = [
    os.path.join(ASSETS, "portraits", "adefonsus_card.jpeg"),
    os.path.join(ASSETS, "portraits", "adefonsus_card.jpg"),
    os.path.join(BASE_DIR, "1.jpeg"),
    ADEFONSUS_PORTRE_YOLU,
]
# </POTBO_STAGE S0063>

# <POTBO_STAGE S0065>

ADEFONSUS_KART_YOLU = mevcut_ilk_dosya(ADEFONSUS_KART_ADAYLARI)
# </POTBO_STAGE S0065>

# <POTBO_STAGE S0080>
# =========================================================
# KARAKTER ÖZGEÇMİŞLERİ
# =========================================================
KARAKTER_OZGECMISLERI = {
    "TR": {
        "male": {
            "title": "KİRLİ ŞÖVALYE",
            "name": "Adefonsus",
            "bio": (
                "Batı sınırındaki yoksul bir soylu ailede doğan Adefonsus, çocukluğundan "
                "itibaren ailesinin konumunu kurtarmak için kullanıldı; sevgi yerine itaat, "
                "şefkat yerine dayanıklılık öğrendi. Şövalye olduğunda iç savaş boyunca köy "
                "baskınlarına ve katliamlara katıldı. Ardında bıraktığı yakılmış köyler nedeniyle "
                "halk ona Kirli Şövalye adını verdi. Savaştan sonra rütbesi alındı fakat bildikleri "
                "yüzünden yargılanmadı. Şimdi suçlarını emirlere yükleyerek yaşayan, Agamon'un "
                "inkâr edilebilir işlerini yapan lekeli bir şövalyedir."
            ),
            "style": "Oyun tarzı: Güçlü saldırı, yüksek dayanıklılık, ağır hareket",
        },
        "female": {
            "title": "ADSIZ KILIÇ",
            "name": "Preciosa",
            "bio": (
                "Güneyde köle olarak doğan Preciosa'nın gerçek adı ve ailesi bilinmez; çocukluğu "
                "boyunca ağır şiddete maruz kaldı ve hayatta kalmak için duygularını bedeninden "
                "ayırmayı öğrendi. Saray ahırlarında çalışırken gizlice binicilik ve silah eğitimi "
                "aldı. Özgürlüğünü kazansa da şövalye kabul edilmedi; kazandığı zaferler erkek "
                "komutanların adına yazıldı. Bu yüzden askerler arasında Adsız Kılıç olarak anılır: "
                "Her savaşta bulunan, fakat hiçbir kayıtta adı geçmeyen kadın."
            ),
            "style": "Oyun tarzı: Hızlı saldırı, yüksek mana, kritik hasar",
        },
    },
    "EN": {
        "male": {
            "title": "THE TAINTED KNIGHT",
            "name": "Adefonsus",
            "bio": (
                "Born into an impoverished noble family on the western frontier, Adefonsus was "
                "used from childhood to restore his family's position. He learned obedience instead "
                "of love and endurance instead of compassion. As a knight, he took part in village "
                "raids and massacres throughout the civil war. The people named him the Tainted "
                "Knight for the burned villages left behind. His rank was stripped after the war, "
                "yet he was never tried because of what he knew. Now he survives by blaming orders "
                "for his crimes and carrying out Agamon's deniable work."
            ),
            "style": "Play style: Heavy attacks, high endurance, slower movement",
        },
        "female": {
            "title": "THE NAMELESS BLADE",
            "name": "Preciosa",
            "bio": (
                "Born into slavery in the south, Preciosa's real name and family are unknown. "
                "She endured severe violence throughout childhood and learned to separate her "
                "emotions from her body in order to survive. While working in the palace stables, "
                "she secretly trained in riding and weapons. Even after gaining her freedom, she "
                "was denied knighthood, and her victories were credited to male commanders. Soldiers "
                "therefore call her the Nameless Blade: a woman present in every battle, yet absent "
                "from every record."
            ),
            "style": "Play style: Fast attacks, high mana, critical damage",
        },
    },
}
# </POTBO_STAGE S0080>

# <POTBO_STAGE S0135>

# CTRL+U yalnız bu geçici özel hareket prototipini açıp kapatır; kendi başına
# hiçbir aksiyon üretmez ve normal dash'i değiştirmez. Prototip yalnız Adefonsus
# hold-to-attack charge durumundayken R'ye basılıp R bırakıldığında tetiklenir.
# Tetiklenince input yaklaşık 2.3 saniye kilitlenir: önce hedefe doğru düz bir giriş
# dash'i, ardından ekran geometrisinde alttan üste '/' kesişi ve üstten alta '\\'
# kesişi oynar. Karakter bu iki diyagonali gerçekten kat eder; çizgiler yalnız FX değildir.
gelistirici_x_skill_aktif = False
# </POTBO_STAGE S0135>

# <POTBO_STAGE S0171>
# — Adefonsus yönsel saldırı / charge-release state machine.
# Yeni sheet üç bağımsız yön grubudur; satırın tamamı hiçbir zaman tek animasyon
# olarak oynatılmaz. J kısa basılırsa normal vuruş, tutulursa charge, bırakılırsa
# yön kilitli ağır dash-slash oluşur. Charge sırasında karakter yerinde kalır ve
# yön tuşları yalnız nişan yönünü değiştirebilir; böylece ağır vuruş telegraph'ı
# okunabilir fakat oyuncunun kontrol hissi korunur.
oyuncu_saldiri_modu = "normal"  # normal | press | charge | hold_release
# </POTBO_STAGE S0171>

# <POTBO_STAGE S0173>
ADEFO_HOLD_ESIK_MS = 180
ADEFO_NORMAL_SURE_MS = 365
ADEFO_HOLD_RELEASE_SURE_MS = 310
ADEFO_HOLD_EK_STAMINA = 14
ADEFO_HOLD_HASAR_CARPANI = 2.50
ADEFO_NORMAL_HASAR_CARPANI = 1.0
ADEFO_HOLD_CHARGE_FRAME_MS = 125
ADEFO_HOLD_FLASH_MS = 92
ADEFO_HOLD_DASH_SURE_MS = 205
ADEFO_HOLD_DASH_MESAFESI = 158.0
ADEFO_HOLD_DASH_ADIMI = 4.0
ADEFO_HOLD_MAX_CHARGE_MS = 3200
ADEFO_HOLD_GECIS_YAPILDI = False
adefo_saldiri_tusu_baslangic_ms = 0
adefo_hold_charge_baslangic_ms = 0
adefo_hold_dash_baslangic_ms = 0
adefo_hold_dash_bitis = 0
adefo_hold_dash_son_guncelleme = 0
adefo_hold_dash_son_ease = 0.0
adefo_hold_dash_yonu = pygame.Vector2(0.0, 0.0)
adefo_hold_charge_yonu = "down"
# </POTBO_STAGE S0173>

# <POTBO_STAGE S0210>


def karakter_tanisma_bolumu():
    e = eadric_adi()

    if karakter_cinsiyet == "male":
        return [
            satir(
                e,
                bt(
                    "Seni tanıyorum. Atın yok ama mahmuzlarının sesi hâlâ "
                    "geliyor. Kirli bir şövalye…",
                    "I know you. Your horse is gone, yet I still hear your "
                    "spurs. A tainted knight…",
                ),
            ),
            satir(
                "ADEFONSUS",
                bt(
                    "Beni nereden tanıyorsun?",
                    "Where do you know me from?",
                ),
            ),
            satir(
                e,
                bt(
                    "Yanmış bir köyden. Hangisi olduğunu sorma. Siz çok "
                    "yaktınız, ben çok kaçtım.",
                    "From a burned village. Do not ask which one. You burned "
                    "many; I fled from many.",
                ),
            ),
        ]

    return [
        satir(
            e,
            bt(
                "Seni tanımıyorum. Güzel. Tanıdığım kadınların çoğu öldü.",
                "I do not know you. Good. Most women I knew are dead.",
            ),
        ),
        satir("PRECIOSA", "…"),
        satir(
            e,
            bt(
                "Sessizlik bazen isimden daha güvenlidir.",
                "Silence is sometimes safer than a name.",
            ),
        ),
    ]
# </POTBO_STAGE S0210>

# <POTBO_STAGE S0223>

adefonsus_sheet_yolu = mevcut_ilk_dosya(ADEFONSUS_SHEET_ADAYLARI)
adefonsus_sheet = resim_yukle(adefonsus_sheet_yolu) if adefonsus_sheet_yolu else None
# </POTBO_STAGE S0223>

# <POTBO_STAGE S0232>
adefonsus_footstep_sesi = (
    ses_yukle(ADEFONSUS_FOOTSTEP_SES_YOLU) if ADEFONSUS_FOOTSTEP_SES_YOLU else None
)
# </POTBO_STAGE S0232>

# <POTBO_STAGE S0234>

if pygame.mixer.get_init():
    # Sound.play() otomatik kanal seçerken ambience/footstep kanallarını çalmasın.
    # Pygame'de Channel(n) almak tek başına kanalı rezerve etmez; yoğun combat SFX
    # ambience kanalını ele geçirip sesi görünürde "yok" edebiliyordu.
    try:
        pygame.mixer.set_num_channels(max(16, pygame.mixer.get_num_channels()))
        # 0-4 arası otomatik Sound.play() tarafından alınmaz.
        # 1 NPC, 2 ambience, 3 footstep, 4 game-over music.
        pygame.mixer.set_reserved(5)
    except pygame.error:
        pass

    npc_ses_kanali = pygame.mixer.Channel(1)
    map_ambience_kanali = pygame.mixer.Channel(2)
    adefonsus_footstep_kanali = pygame.mixer.Channel(3)
    gameover_music_kanali = pygame.mixer.Channel(4)
else:
    npc_ses_kanali = None
    map_ambience_kanali = None
    adefonsus_footstep_kanali = None
    gameover_music_kanali = None
# </POTBO_STAGE S0234>

# <POTBO_STAGE S0237>


def adefonsus_footstep_guncelle():
    """1 saniyelik/two-step Adefonsus sample'ını yürüyüş boyunca fazını bozmadan loop eder."""
    if adefonsus_footstep_kanali is None or adefonsus_footstep_sesi is None:
        return
    simdi = pygame.time.get_ticks()
    hiz = (
        oyuncu_hareket_hiz_vektoru.length()
        if isinstance(oyuncu_hareket_hiz_vektoru, pygame.Vector2)
        else 0.0
    )
    aktif = bool(
        karakter_cinsiyet == "male"
        and oyun_durumu == OYUN
        and oyun_alt_durumu == HARITA
        and oyuncu_hp > 0
        and oyuncu_hareket_ediyor
        and hiz >= OYUNCU_YURUYUS_HIZI * 0.16
        and not oyun_sinematik_kilitli_mi()
        and not oyuncu_dash_aktif_mi(simdi)
    )
    if aktif:
        # Yavaş attack-strafe sırasında ses geriye çekilir; sample hızı değiştirilmez.
        hiz_orani = max(0.30, min(1.0, hiz / max(1.0, OYUNCU_YURUYUS_HIZI)))
        adefonsus_footstep_kanali.set_volume(
            _v35_footstep_ses_orani() * (0.58 + 0.42 * hiz_orani)
        )
        if not adefonsus_footstep_kanali.get_busy():
            adefonsus_footstep_kanali.play(
                adefonsus_footstep_sesi, loops=-1, fade_ms=35
            )
    elif adefonsus_footstep_kanali.get_busy():
        adefonsus_footstep_kanali.fadeout(70)
# </POTBO_STAGE S0237>

# <POTBO_STAGE S0279>

adefonsus_portre = resim_yukle(ADEFONSUS_PORTRE_YOLU)
# </POTBO_STAGE S0279>

# <POTBO_STAGE S0284>

adefonsus_kart_portre = (
    resim_yukle(ADEFONSUS_KART_YOLU) if ADEFONSUS_KART_YOLU else adefonsus_portre
)
# </POTBO_STAGE S0284>

# <POTBO_STAGE S0291>


# =========================================================
# ADEFONSUS — YÖNSEL SPRITE SHEET / CHARGE -> DASH SLASH
# =========================================================
# Kullanıcının tarif ettiği gerçek semantik düzen:
# ÜST SATIR — locomotion, üçerli yön grupları
# 0..2 : aşağı = idle, sol ayak, sağ ayak
# 3..5 : sol = idle, sol ayak, sağ ayak (sağ için runtime flip)
# 6..8 : yukarı = idle, sol ayak, sağ ayak
# ORTA SATIR — normal saldırı, ikişerli yön grupları
# 0..1 : aşağı
# 2..3 : sol (sağ için runtime flip)
# 4..5 : yukarı
# Kredi kutusu sprite değildir ve bilerek hiç çıkarılmaz.
# ALT SATIR — hold-to-attack, üçerli yön grupları
# [0,1] charge telegraph, [2] release slash
# ilk üç aşağı, orta üç sol/sağ, son üç yukarı.
# Bütün gruplar kendi canvas'ında normalize edilir. Farklı yönlerin birlikte
# normalize edilmemesi, geniş slash frame'inin idle sprite'ı yanlış merkezlemesini
# ve yürüme sırasında karakterin yatay "zıplamasını" engeller.
ADEFONSUS_LOCOMOTION_RECTLERI = [
    (11, 16, 58, 56),
    (76, 16, 56, 56),
    (139, 12, 51, 57),
    (205, 17, 47, 55),
    (261, 18, 41, 52),
    (311, 17, 55, 53),
    (387, 17, 58, 53),
    (454, 18, 51, 52),
    (515, 18, 49, 52),
]

ADEFONSUS_NORMAL_ATTACK_RECTLERI = [
    (11, 80, 42, 64),
    (61, 98, 70, 60),
    (145, 89, 46, 53),
    (201, 97, 58, 63),
    (273, 105, 37, 46),
    (319, 91, 52, 57),
]

ADEFONSUS_HOLD_ATTACK_RECTLERI = [
    (9, 170, 60, 67),
    (77, 170, 61, 67),
    (147, 188, 91, 50),
    (256, 172, 50, 66),
    (316, 171, 50, 65),
    (375, 178, 51, 60),
    (447, 172, 57, 65),
    (508, 175, 56, 65),
    (570, 187, 83, 51),
]

ADEFONSUS_FRAME_RECTLERI = (
    ADEFONSUS_LOCOMOTION_RECTLERI
    + ADEFONSUS_NORMAL_ATTACK_RECTLERI
    + ADEFONSUS_HOLD_ATTACK_RECTLERI
)


def _adefonsus_sheet_karelerini_cikar(sheet, rectler):
    """Yalnız gerçek sprite rectlerini çıkar ve magenta preview fonunu alpha yap.

    Bu fonksiyon kredi kutusunu hiç görmez. Kaynak zırhın bordo/mor tonlarına
    dokunmamak için chroma anahtarı yalnız yüksek R+B / çok düşük G ailesidir.
    """
    if sheet is None:
        return []
    kaynak = sheet.convert_alpha()
    sonuc = []
    for x, y, w, h in rectler:
        if x < 0 or y < 0 or x + w > kaynak.get_width() or y + h > kaynak.get_height():
            sonuc.append(None)
            continue
        kare = kaynak.subsurface(pygame.Rect(x, y, w, h)).copy().convert_alpha()
        px = pygame.PixelArray(kare)
        try:
            for py in range(kare.get_height()):
                for px_x in range(kare.get_width()):
                    renk = kare.unmap_rgb(px[px_x, py])
                    if renk.a == 0 or (
                        renk.r >= 238 and renk.g <= 14 and renk.b >= 238
                    ):
                        px[px_x, py] = (0, 0, 0, 0)
        finally:
            del px
        sinir = kare.get_bounding_rect(min_alpha=1)
        sonuc.append(
            kare.subsurface(sinir).copy()
            if sinir.width > 0 and sinir.height > 0
            else None
        )
    return sonuc


def _adefo_grubu(kareler, bas, adet, padding=4):
    sec = [k for k in kareler[bas : bas + adet] if k is not None]
    return _kareleri_ortak_canvas_yap(sec, padding=padding) if sec else []


_adefo_loco_raw = _adefonsus_sheet_karelerini_cikar(
    adefonsus_sheet, ADEFONSUS_LOCOMOTION_RECTLERI
)
_adefo_normal_raw = _adefonsus_sheet_karelerini_cikar(
    adefonsus_sheet, ADEFONSUS_NORMAL_ATTACK_RECTLERI
)
_adefo_hold_raw = _adefonsus_sheet_karelerini_cikar(
    adefonsus_sheet, ADEFONSUS_HOLD_ATTACK_RECTLERI
)

# Kaynak side grubu SOLA bakar. Sağ yön yalnız render-time horizontal flip'tir.
_adefo_loco_down = _adefo_grubu(_adefo_loco_raw, 0, 3, 4)
_adefo_loco_left = _adefo_grubu(_adefo_loco_raw, 3, 3, 4)
_adefo_loco_up = _adefo_grubu(_adefo_loco_raw, 6, 3, 4)
_adefo_atk_down = _adefo_grubu(_adefo_normal_raw, 0, 2, 5)
_adefo_atk_left = _adefo_grubu(_adefo_normal_raw, 2, 2, 5)
_adefo_atk_up = _adefo_grubu(_adefo_normal_raw, 4, 2, 5)
_adefo_hold_down = _adefo_grubu(_adefo_hold_raw, 0, 3, 6)
_adefo_hold_left = _adefo_grubu(_adefo_hold_raw, 3, 3, 6)
_adefo_hold_up = _adefo_grubu(_adefo_hold_raw, 6, 3, 6)


def _adefo_yon_kaynagi(y=None):
    yon = oyuncu_yonu if y is None else str(y)
    if yon == "up":
        return "up"
    if yon in ("left", "right"):
        return "left"
    return "down"


ADEFONSUS_SPRITELERI = {
    "down": {
        "idle": _adefo_loco_down[:1],
        "walk": (
            _adefo_loco_down[:1]
            + _adefo_loco_down[1:2]
            + _adefo_loco_down[:1]
            + _adefo_loco_down[2:3]
        ),
        "attack": _adefo_atk_down,
        "hold": _adefo_hold_down,
    },
    "left": {
        "idle": _adefo_loco_left[:1],
        "walk": (
            _adefo_loco_left[:1]
            + _adefo_loco_left[1:2]
            + _adefo_loco_left[:1]
            + _adefo_loco_left[2:3]
        ),
        "attack": _adefo_atk_left,
        "hold": _adefo_hold_left,
    },
    "up": {
        "idle": _adefo_loco_up[:1],
        "walk": (
            _adefo_loco_up[:1]
            + _adefo_loco_up[1:2]
            + _adefo_loco_up[:1]
            + _adefo_loco_up[2:3]
        ),
        "attack": _adefo_atk_up,
        "hold": _adefo_hold_up,
    },
}

ADEFONSUS_YENI_SHEET_AKTIF = all(
    ADEFONSUS_SPRITELERI[y][a]
    for y in ("down", "left", "up")
    for a in ("idle", "walk", "attack", "hold")
)


def adefonsus_yon_animasyon_kareleri(animasyon_adi, yon=None):
    """Yeni sheet'ten yalnız istenen yön grubunu döndürür.

    hold_charge: ilk iki frame; hold_release: üçüncü frame. Bu ayrım renderer'ın
    alt sıranın dokuz karesini veya üçlü grubun tamamını istemeden oynatmasını
    yapısal olarak imkânsız kılar.
    """
    kaynak_yon = _adefo_yon_kaynagi(yon)
    veri = ADEFONSUS_SPRITELERI.get(kaynak_yon, ADEFONSUS_SPRITELERI["down"])
    if animasyon_adi == "hold_charge":
        return veri.get("hold", [])[:2]
    if animasyon_adi == "hold_release":
        hold = veri.get("hold", [])
        return hold[2:3] if len(hold) >= 3 else hold[-1:]
    return veri.get(animasyon_adi, [])


def adefonsus_render_flip_gerekli_mi(yon=None):
    # Sheet'in side frame'leri sola bakıyor; yalnız sağ yön için flip gerekir.
    return (
        ADEFONSUS_YENI_SHEET_AKTIF and (oyuncu_yonu if yon is None else yon) == "right"
    )
# </POTBO_STAGE S0291>

# <POTBO_STAGE S0298>


def aktif_animasyon_kareleri(animasyon_adi):
    """
    Erkek karakterde yön bazlı ayrı PNG'ler kullanılır.
    Kadın karakter mevcut sprite sheet sistemiyle çalışmaya devam eder.
    """

    if karakter_cinsiyet == "male":
        if ADEFONSUS_YENI_SHEET_AKTIF:
            yeni = temiz_kareler(
                adefonsus_yon_animasyon_kareleri(animasyon_adi, oyuncu_yonu)
            )
            if yeni:
                return yeni
            if animasyon_adi in ("hold_charge", "hold_release"):
                yeni = temiz_kareler(
                    adefonsus_yon_animasyon_kareleri("attack", oyuncu_yonu)
                )
                if yeni:
                    return yeni

        yon_verisi = ERKEK_YON_ANIMASYONLARI.get(
            oyuncu_yonu, ERKEK_YON_ANIMASYONLARI["down"]
        )

        fallback_adi = (
            "attack"
            if animasyon_adi in ("hold_charge", "hold_release")
            else animasyon_adi
        )
        kareler = temiz_kareler(yon_verisi.get(fallback_adi, []))

        if kareler:
            return kareler

        # Dosyalardan biri eksikse eski sheet'e düş.
        return erkek_animasyonlari.get(fallback_adi, [])

    return kadin_animasyonlari.get(animasyon_adi, [])
# </POTBO_STAGE S0298>

# <POTBO_STAGE S0328>


def karakter_karti_ciz(rect, cinsiyet, secili, onay_animasyonu=False):
    pygame.draw.rect(ekran, (3, 3, 5), rect, border_radius=0)

    portre = adefonsus_kart_portre if cinsiyet == "male" else preciosa_kart_portre

    doldurulmus = resmi_oranli_doldur(portre, rect)

    if doldurulmus is not None:
        portre_rect = doldurulmus.get_rect(center=rect.center)

        eski_clip = ekran.get_clip()
        ekran.set_clip(rect)
        ekran.blit(doldurulmus, portre_rect)

        # Alt bölümdeki metnin okunabilmesi için katmanlı gölge.
        for yukseklik, alfa in (
            (170, 145),
            (125, 185),
            (84, 220),
        ):
            golge = pygame.Surface((rect.width, yukseklik), pygame.SRCALPHA)
            golge.fill((0, 0, 0, alfa))
            ekran.blit(golge, (rect.x, rect.bottom - yukseklik))

        ekran.set_clip(eski_clip)
    else:
        yazi_yaz(
            t("asset_missing"),
            rect.centerx,
            rect.centery,
            GRI,
            mini_font,
            True,
        )

    bilgi = KARAKTER_OZGECMISLERI[dil][cinsiyet]

    yazi_yaz(
        bilgi["name"],
        rect.centerx,
        rect.bottom - 92,
        BEYAZ,
        normal_font,
        True,
    )
    yazi_yaz(
        bilgi["title"],
        rect.centerx,
        rect.bottom - 58,
        PARLAK_KIRMIZI if secili else ACIK_GRI,
        kucuk_font,
        True,
    )
    yazi_yaz(
        t("male") if cinsiyet == "male" else t("female"),
        rect.centerx,
        rect.bottom - 27,
        SARI if secili else GRI,
        mini_font,
        True,
    )

    kenar_kalinligi = 4 if secili else 1
    if onay_animasyonu:
        gecen = max(
            0,
            pygame.time.get_ticks() - karakter_onay_gecisi_baslangic,
        )
        oran = min(1.0, gecen / max(1, KARAKTER_ONAY_GECIS_SURESI))
        nabiz = math.sin(min(1.0, oran * 1.65) * math.pi)
        kenar_kalinligi = 5 + int(round(3 * max(0.0, nabiz)))
        genisleme = 5 + int(round(7 * max(0.0, nabiz)))
        pygame.draw.rect(
            ekran,
            (255, 68, 92),
            rect.inflate(genisleme * 2, genisleme * 2),
            2,
            border_radius=0,
        )

    pygame.draw.rect(
        ekran,
        PARLAK_KIRMIZI if secili else (80, 72, 82),
        rect,
        kenar_kalinligi,
        border_radius=0,
    )
# </POTBO_STAGE S0328>

# <POTBO_STAGE S0336>


def loading_ekrani_ciz():
    global loading_tamamlandi

    ekran.fill(SIYAH)

    simdi = pygame.time.get_ticks()
    gecen = simdi - loading_baslangic
    oran = min(1.0, gecen / max(1, loading_suresi))

    if oran >= 1.0:
        loading_tamamlandi = True

    # Progress bar ve ipucu panelleri aynı dış sınırlara hizalanır.
    # Referanstaki ince, yatay ve uçları sivrilen loading çizgisi.
    # Asset yerine kodla çizilir; mevcut kırmızı dolum ve orta sembol korunur.
    dekor_y = 530
    kanal_w = 1120
    kanal_h = 10
    kanal_x = (GENISLIK - kanal_w) // 2
    kanal_y = dekor_y + 92

    # Seçilen karakter tek başına gösterilir. Karakter görseli kesilmez;
    # yalnızca alt bölümdeki vinyetle siyaha erir. Bu sürümde karakterler
    # hafifçe büyütüldü ve konumları istenen yöne göre ince ayarlandı.
    karakter_gorseli = (
        adefonsus_portre if karakter_cinsiyet == "male" else preciosa_portre
    )

    if karakter_cinsiyet == "male":
        karakter_alani = pygame.Rect(520, 0, 680, 580)
        karakter_olcegi = 1.94
        karakter_merkez = (
            karakter_alani.centerx - 68,
            karakter_alani.bottom + 352,
        )
    else:
        karakter_alani = pygame.Rect(36, 0, 680, 580)
        karakter_olcegi = 1.94
        karakter_merkez = (
            karakter_alani.centerx + 22,
            karakter_alani.bottom + 386,
        )

    karakter_cizimi = resmi_oranli_sigdir(
        karakter_gorseli,
        karakter_alani,
        0,
        karakter_olcegi,
        True,
    )

    if karakter_cizimi is not None:
        karakter_rect = karakter_cizimi.get_rect(midbottom=karakter_merkez)
        ekran.blit(karakter_cizimi, karakter_rect)

    loading_alt_vinyet_ciz()

    # Sol panelin sol kenarı ve sağ panelin sağ kenarı progress barın
    # iki dış ucuyla tam hizalıdır.
    hint_panel_w = 470
    hint_panel = (
        pygame.Rect(kanal_x, 100, hint_panel_w, 405)
        if karakter_cinsiyet == "male"
        else pygame.Rect(
            kanal_x + kanal_w - hint_panel_w,
            100,
            hint_panel_w,
            405,
        )
    )

    gotik_panel(hint_panel, KAN_KIRMIZISI, 218)

    yazi_yaz(
        t("hint"),
        hint_panel.centerx,
        hint_panel.y + 42,
        PARLAK_KIRMIZI,
        menu_baslik_font,
        True,
    )

    pygame.draw.line(
        ekran,
        (105, 75, 82),
        (hint_panel.x + 35, hint_panel.y + 78),
        (hint_panel.right - 35, hint_panel.y + 78),
        1,
    )

    ipucu_satirlari = metni_satirlara_bol(
        loading_ipucu, kucuk_font, hint_panel.width - 70
    )

    ipucu_y = hint_panel.y + 112
    for satir_metni in ipucu_satirlari[:8]:
        yazi_yaz(
            satir_metni,
            hint_panel.x + 35,
            ipucu_y,
            BEYAZ,
            kucuk_font,
        )
        ipucu_y += 29

    merkez_x = GENISLIK // 2
    merkez_y = kanal_y + kanal_h // 2

    # İki ray da merkez sembolünün tam arkasına kadar uzanır. Sembol en son
    # çizildiği için raylar ve kırmızı dolum görsel olarak ona bağlı görünür.
    sol_ic = merkez_x
    sag_ic = merkez_x
    sol_dis = kanal_x
    sag_dis = kanal_x + kanal_w

    # Dış ray: ikinci referanstaki gibi ince, gri ve sivri uçlu.
    ray_arka = (8, 7, 10)
    ray_kenar = (92, 88, 96)
    ray_vurgu = (154, 150, 158)

    sol_ray = [
        (sol_dis, merkez_y),
        (sol_dis + 15, kanal_y),
        (sol_ic, kanal_y),
        (sol_ic, kanal_y + kanal_h),
        (sol_dis + 15, kanal_y + kanal_h),
    ]
    sag_ray = [
        (sag_dis, merkez_y),
        (sag_dis - 15, kanal_y),
        (sag_ic, kanal_y),
        (sag_ic, kanal_y + kanal_h),
        (sag_dis - 15, kanal_y + kanal_h),
    ]

    pygame.draw.polygon(ekran, ray_arka, sol_ray)
    pygame.draw.polygon(ekran, ray_arka, sag_ray)
    pygame.draw.lines(ekran, ray_kenar, True, sol_ray, 1)
    pygame.draw.lines(ekran, ray_kenar, True, sag_ray, 1)
    pygame.draw.line(
        ekran,
        ray_vurgu,
        (sol_dis + 15, kanal_y + 2),
        (sol_ic, kanal_y + 2),
        1,
    )
    pygame.draw.line(
        ekran,
        ray_vurgu,
        (sag_ic, kanal_y + 2),
        (sag_dis - 15, kanal_y + 2),
        1,
    )

    # Dolum merkezden iki yana eşzamanlı büyür; mevcut kan kırmızısı korunur.
    kullanilabilir_yari = max(1, sol_ic - sol_dis)
    dolum_yari = int(kullanilabilir_yari * oran)
    dolum_rengi = (142, 12, 31)
    dolum_vurgusu = (176, 29, 48)

    if dolum_yari > 0:
        sol_ucluk = max(sol_dis, sol_ic - dolum_yari)
        sag_ucluk = min(sag_dis, sag_ic + dolum_yari)
        ic_ust = kanal_y + 2
        ic_alt = kanal_y + kanal_h - 2

        sol_dolum = [
            (sol_ucluk, merkez_y),
            (min(sol_ic, sol_ucluk + 9), ic_ust),
            (sol_ic, ic_ust),
            (sol_ic, ic_alt),
            (min(sol_ic, sol_ucluk + 9), ic_alt),
        ]
        sag_dolum = [
            (sag_ucluk, merkez_y),
            (max(sag_ic, sag_ucluk - 9), ic_ust),
            (sag_ic, ic_ust),
            (sag_ic, ic_alt),
            (max(sag_ic, sag_ucluk - 9), ic_alt),
        ]

        pygame.draw.polygon(ekran, dolum_rengi, sol_dolum)
        pygame.draw.polygon(ekran, dolum_rengi, sag_dolum)
        pygame.draw.line(
            ekran,
            dolum_vurgusu,
            (min(sol_ic, sol_ucluk + 9), ic_ust),
            (sol_ic, ic_ust),
            1,
        )
        pygame.draw.line(
            ekran,
            dolum_vurgusu,
            (sag_ic, ic_ust),
            (max(sag_ic, sag_ucluk - 9), ic_ust),
            1,
        )

    # Mevcut orta sembol aynen korunur.
    pygame.draw.polygon(
        ekran,
        (22, 15, 25),
        [
            (merkez_x - 20, merkez_y),
            (merkez_x, merkez_y - 23),
            (merkez_x + 20, merkez_y),
            (merkez_x, merkez_y + 23),
        ],
    )
    pygame.draw.polygon(
        ekran,
        (238, 20, 72),
        [
            (merkez_x - 12, merkez_y),
            (merkez_x, merkez_y - 14),
            (merkez_x + 12, merkez_y),
            (merkez_x, merkez_y + 14),
        ],
        3,
    )
    pygame.draw.circle(ekran, (255, 90, 145), (merkez_x, merkez_y), 4)

    # İstenen tasarım gereği yüzde metni gösterilmez.
    if loading_tamamlandi:
        if pygame.time.get_ticks() // 500 % 2 == 0:
            yazi_yaz(
                t("press_key"),
                GENISLIK // 2,
                704,
                SARI,
                mini_font,
                True,
            )
# </POTBO_STAGE S0336>

# <POTBO_STAGE S0340>


def oyuncu_sprite_ciz():
    global animasyon_index
    global animasyon_zamani

    oyuncu_ekran_x = dunya_ekran_x(oyuncu_x)
    oyuncu_ekran_y = dunya_ekran_y(oyuncu_y)
    # midbottom sprite anchor ile aynı x ekseni ve ayağın hemen altı. Eski -1 y
    # offset'i karakteri gölgeden kopuk gösteriyordu.
    karakter_zemin_golgesi_ciz(
        oyuncu_ekran_x,
        oyuncu_ekran_y - 3,
        34 * KAMERA_YAKINLASTIRMA,
        7 * KAMERA_YAKINLASTIRMA,
        68,
    )

    yeni_adefo = karakter_cinsiyet == "male" and ADEFONSUS_YENI_SHEET_AKTIF
    if oyuncu_savunuyor:
        # Savunma sprite'ı yok: Adefonsus'un hold-to-attack idle/charge pozu kullanılır.
        animasyon_adi = "hold_charge" if yeni_adefo else "idle"
    elif gelistirici_x_skill_aktif_mi():
        # Special move sırasında karakter gerçekten hareket eder; walk animasyonu yerine
        # hold-release commitment pozu korunur ki iki dash kesişi tek bir teknik gibi okunsun.
        animasyon_adi = "hold_release" if yeni_adefo else "attack"
    elif oyuncu_saldiriyor:
        if yeni_adefo and oyuncu_saldiri_modu in (
            "press",
            "charge",
        ):
            animasyon_adi = "hold_charge"
        elif yeni_adefo and oyuncu_saldiri_modu == "hold_release":
            animasyon_adi = "hold_release"
        else:
            animasyon_adi = "attack"
    elif oyuncu_hareket_ediyor:
        animasyon_adi = "walk"
    else:
        animasyon_adi = "idle"

    kareler = aktif_animasyon_kareleri(animasyon_adi)
    if not kareler:
        pygame.draw.circle(
            ekran,
            PARLAK_KIRMIZI,
            (oyuncu_ekran_x, oyuncu_ekran_y),
            int(round(15 * KAMERA_YAKINLASTIRMA)),
        )
        return

    simdi = pygame.time.get_ticks()

    if yeni_adefo and animasyon_adi == "hold_charge":
        # Savunmada kullanıcının istediği "hold-to-attack idle" pozu sabittir;
        # saldırı charge'ındaki pulse animasyonu savunmaya sızmaz.
        if oyuncu_savunuyor:
            animasyon_index = 0
        # Basışın ilk kısa bölümünde birinci charge frame okunur. Eşik geçilince
        # ilk iki sprite arasında kontrollü pulse vardır; üçüncü sprite release'e
        # kadar hiçbir koşulda gösterilmez.
        elif oyuncu_saldiri_modu == "press" or len(kareler) == 1:
            animasyon_index = 0
        else:
            gecen = max(0, simdi - adefo_hold_charge_baslangic_ms)
            animasyon_index = int(gecen // ADEFO_HOLD_CHARGE_FRAME_MS) % min(
                2, len(kareler)
            )

    elif yeni_adefo and animasyon_adi == "hold_release":
        # Alt gruptaki üçüncü sprite release/dash boyunca sabit commitment pozu.
        animasyon_index = 0

    elif animasyon_adi == "attack":
        gecen = max(0, simdi - saldiri_baslangic)
        ilerleme = min(
            0.999999,
            gecen / max(1, oyuncu_aktif_saldiri_suresi_ms()),
        )
        animasyon_index = min(len(kareler) - 1, int(ilerleme * len(kareler)))

    else:
        if animasyon_adi == "walk":
            # Animasyon ritmi gerçek hızla bağlanır; hızlanırken ayaklar hızlanır,
            # yavaşlarken frame akışı da ağırlaşır. Bu, zeminde kayma hissini azaltır.
            hiz_orani = min(
                1.0,
                oyuncu_hareket_hiz_vektoru.length() / max(1.0, OYUNCU_YURUYUS_HIZI),
            )
            taban = 92 if yeni_adefo else 140
            gecikme = int(round(taban + (1.0 - hiz_orani) * 48))
        else:
            gecikme = 240

        if simdi - animasyon_zamani >= gecikme:
            animasyon_zamani = simdi
            animasyon_index = (animasyon_index + 1) % len(kareler)

    kare = kareler[animasyon_index % len(kareler)]

    if karakter_cinsiyet == "male":
        if yeni_adefo:
            if animasyon_adi == "hold_release":
                taban_yukseklik = 73
            elif animasyon_adi == "hold_charge":
                taban_yukseklik = 70
            elif animasyon_adi == "attack":
                taban_yukseklik = 72
            else:
                taban_yukseklik = 64
        else:
            taban_yukseklik = (
                70 if animasyon_adi in ("attack", "hold_charge", "hold_release") else 60
            )
    else:
        taban_yukseklik = 68 if animasyon_adi == "attack" else 58

    hedef_yukseklik = int(round(taban_yukseklik * KAMERA_YAKINLASTIRMA))
    # Tek idle karesi bile tamamen donuk görünmesin: yalnız 1 px'lik, ayak anchor'ını
    # bozmayan yavaş gövde nefesi. Geometrik aura yoktur.
    if animasyon_adi == "idle" and not oyuncu_saldiriyor:
        nefes = 0.5 + 0.5 * math.sin(simdi * 0.0026)
        if nefes > 0.58:
            hedef_yukseklik += 1

    # Source side grubu SOLA bakar. Yalnız oyuncu sağa baktığında flip edilir.
    adefo_flip = bool(yeni_adefo and adefonsus_render_flip_gerekli_mi(oyuncu_yonu))
    onbellek_anahtari = (
        id(kare),
        hedef_yukseklik,
        "adefo_right_flip" if adefo_flip else "normal",
    )

    olcekli_kare = sprite_olcek_onbellegi.get(onbellek_anahtari)
    if olcekli_kare is None:
        oran = hedef_yukseklik / max(1, kare.get_height())
        hedef_genislik = max(1, int(round(kare.get_width() * oran)))
        olcekli_kare = pygame.transform.scale(kare, (hedef_genislik, hedef_yukseklik))
        if adefo_flip:
            olcekli_kare = pygame.transform.flip(olcekli_kare, True, False)
        sprite_olcek_onbellegi[onbellek_anahtari] = olcekli_kare

    rect = olcekli_kare.get_rect(midbottom=(oyuncu_ekran_x, oyuncu_ekran_y))
    ekran.blit(olcekli_kare, rect)

    # Charge'ın "yanıp sönme" geri bildirimi sprite dışına taşan aura değil, doğrudan
    # alfa maskesi üzerinde kısa beyaz pulse'tır. Böylece pixel-art dili korunur.
    if yeni_adefo and oyuncu_saldiriyor and oyuncu_saldiri_modu == "charge":
        charge_gecen = max(0, simdi - adefo_hold_charge_baslangic_ms)
        faz = (charge_gecen // ADEFO_HOLD_FLASH_MS) % 2
        if faz == 0:
            sprite_maskeli_parlama_ciz(olcekli_kare, rect, (238, 238, 238), 96)

    oyuncu_sprite_parlamasi_ciz(olcekli_kare, rect)
    fire_magic_burn_overlay_oyuncu_ciz(olcekli_kare, rect)
# </POTBO_STAGE S0340>

# <POTBO_STAGE S0344>


def secili_karakter_adi():
    return "Adefonsus" if karakter_cinsiyet == "male" else "Preciosa"
# </POTBO_STAGE S0344>

# <POTBO_STAGE S0399>


def torrmund_konusma_akisi():
    """Sir Torrmund'un nezaket ile infaz tehdidi arasında kalan disiplinli diyaloğu."""
    konusmaci = "SIR TORRMUND"
    isim = secili_karakter_adi()
    lakap = karakter_lakabi()
    kimlik_cevabi = (
        bt("Ben Adefonsus.", "I am Adefonsus.")
        if karakter_cinsiyet == "male"
        else "Preciosa."
    )
    lakap_cevabi = (
        bt(
            "Halk taktı o lakabı bana.",
            "The people gave me that name.",
        )
        if karakter_cinsiyet == "male"
        else bt(
            "Yalnız Preciosa'yı tercih ederim.",
            "I prefer only Preciosa.",
        )
    )

    if torrmund_konusuldu:
        return [
            satir(
                konusmaci,
                bt(
                    "Sözümü unutma. Bu orman insanın ardından bakar.",
                    "Forget not my warning. This forest watches a man after he passes.",
                ),
            )
        ]

    tavsiye = [
        satir(
            konusmaci,
            bt(
                "Seni tutmayayım. Yolun açık olsun. Fakat bir öğüdümü al.",
                "I shall not keep you. Good road to you. But take one counsel from me.",
            ),
        ),
        satir(
            konusmaci,
            bt(
                "Bu orman sizi izler, sizi işitir. Burada aklın tartamayacağı şeyler olur. "
                "Adımını ve sözünü ölç. İyi yolculuklar.",
                "This forest watches you and hears you. Things pass here that the mind cannot weigh. "
                "Measure your step and your word. Good journey.",
            ),
        ),
        satir(karakter_konusmaci(), "..."),
        aksiyon("torrmund_konusma_tamam"),
    ]

    return [
        satir(
            konusmaci,
            bt(
                "Ben Monthiem şövalyesi, Wessir'li Sir Torrmund'um. Adınız nedir?",
                "I am Sir Torrmund of Wessir, knight of Monthiem. What is your name?",
            ),
        ),
        secim(
            [
                (
                    bt(
                        "Çekil yolumdan, demir adam.",
                        "Stand aside, iron man.",
                    ),
                    [
                        satir(
                            konusmaci,
                            bt(
                                "Krallığın şövalyesine böyle dil uzatırsın ha? Bu ağız cezasını "
                                "kılıçtan alır. Seni burada infaz edeceğim.",
                                "You loose that tongue upon a knight of the realm? Then let your mouth "
                                "take its answer from steel. I shall execute you here.",
                            ),
                        ),
                        aksiyon("torrmund_savas_baslat"),
                    ],
                ),
                (
                    kimlik_cevabi,
                    [
                        satir(konusmaci, f"{isim}?"),
                        satir(
                            konusmaci,
                            bt(
                                f"{lakap}. Daha evvel adını işittim.",
                                f"{lakap}. I have heard your name before.",
                            ),
                        ),
                        secim(
                            [
                                (
                                    lakap_cevabi,
                                    [
                                        satir(
                                            konusmaci,
                                            bt(
                                                f"Lakabını sen seçseydin bir kıymeti olmazdı. Lakap insanın "
                                                f"peşinden gelir ve sonunda onu bulur. Bunu kabullenmelisin, {lakap}.",
                                                f"Had you chosen the name yourself, it would mean little. A title follows a person "
                                                f"and in time finds them. You should accept that, {lakap}.",
                                            ),
                                        )
                                    ]
                                    + tavsiye,
                                ),
                                ("...", list(tavsiye)),
                            ]
                        ),
                    ],
                ),
            ]
        ),
    ]
# </POTBO_STAGE S0399>

# <POTBO_STAGE S0416>


def _stage1__v30_olum_koreografi_guncelle(simdi):
    """Ceset yere oturduktan sonra katile özgü post-mortem saldırıları tetikler."""
    global oyuncu_olum_ikiye_bolundu
    if oyuncu_olum_baslangic_ms <= 0 or oyuncu_olum_turu not in (
        "blood",
        "blast_inner",
    ):
        return
    alt = str(oyuncu_olum_alt_turu or "")
    if not alt:
        return
    gecen = int(simdi) - int(oyuncu_olum_baslangic_ms)
    katil = _v24_olum_katil_actor_bul()
    if katil is not None:
        base = pygame.Vector2(oyuncu_x - float(katil.x), oyuncu_y - float(katil.y))
    else:
        base = _adefo_yon_vektoru(oyuncu_yonu)
    if base.length_squared() <= 1e-6:
        base = pygame.Vector2(1.0, 0.0)
    base = base.normalize()

    def vur(key, zaman, blood_n, gore_n, power, yoff=-9.0, puddle=0):
        if gecen < zaman or key in oyuncu_olum_koreografi_vuruslari:
            return False
        oyuncu_olum_koreografi_vuruslari.add(key)
        kan_parcacigi_patlat(
            oyuncu_x,
            oyuncu_y + yoff,
            blood_n,
            power,
            yon=base,
            arterial=power > 1.42,
        )
        _v30_kucuk_gore_jet(
            oyuncu_x,
            oyuncu_y + yoff,
            gore_n,
            base,
            max(0.72, power * 0.70),
            True,
        )
        for _ in range(max(0, int(puddle))):
            kan_lekesi_ekle(
                oyuncu_x + random.uniform(-11.0, 11.0),
                oyuncu_y + random.uniform(-6.0, 8.0),
                random.uniform(0.52, 1.10) * min(1.25, power),
            )
        kamera_hit_sarsintisi_baslat(3.5 + power * 2.7, int(82 + power * 48))
        return True

    # 340 ms düşüş tamamlanır. İlk post-mortem temas 470 ms'de başlar; yani
    # katil ceset havadayken havayı dövmez.
    if alt == "crawler":
        zamanlar = (470, 635, 800, 965, 1130, 1295)
        for i, zaman in enumerate(zamanlar):
            vur(
                f"crawler_{i}",
                zaman,
                random.randint(18, 26),
                random.randint(2, 3),
                1.02 + i * 0.025,
                -9.0,
                1 if i in (2, 5) else 0,
            )
    elif alt == "berserker":
        zamanlar = (470, 660, 850, 1040, 1230, 1420)
        for i, zaman in enumerate(zamanlar):
            vur(
                f"bers_{i}",
                zaman,
                random.randint(25, 36),
                random.randint(3, 4),
                1.22 + i * 0.035,
                -13.0,
                1,
            )
    elif alt == "headshot":
        vur(
            "head_residual",
            470,
            random.randint(12, 18),
            random.randint(2, 3),
            0.92,
            -24.0,
            1,
        )
    elif alt == "tarkard_crush":
        # Tek whirl/crush hareketi yeter; fakat boss ağırlığı nedeniyle gore normal
        # düşmanlardan açık biçimde yüksektir.
        vur(
            "tarkard_whirl",
            520,
            random.randint(62, 78),
            random.randint(24, 32),
            1.78,
            -8.0,
            4,
        )
    elif alt == "torrmund_decap_cleave":
        if vur(
            "torrmund_second",
            1420,
            random.randint(72, 96),
            random.randint(18, 24),
            1.96,
            -8.0,
            4,
        ):
            oyuncu_olum_ikiye_bolundu = True
# </POTBO_STAGE S0416>

# <POTBO_STAGE S0424>


def oyuncu_saldiri_durumunu_sifirla():
    """Save/load, ölüm, stun ve sahne geçişlerinde transient saldırı state'ini temizle.

    Charge/dash state'i özellikle sıfırlanır. Aksi halde diyalog/pause sırasında
    kaçırılan KEYUP, oyuna dönüldüğünde Adefonsus'u sonsuz charge'da bırakabilirdi.
    """
    global oyuncu_saldiriyor, oyuncu_saldiri_modu, oyuncu_saldiri_sure_ms
    global ADEFO_HOLD_GECIS_YAPILDI, animasyon_index, saldiri_baslangic
    global adefo_saldiri_tusu_baslangic_ms, adefo_hold_charge_baslangic_ms
    global adefo_hold_dash_baslangic_ms, adefo_hold_dash_bitis
    global adefo_hold_dash_son_guncelleme, adefo_hold_dash_son_ease
    global adefo_hold_dash_yonu, adefo_hold_charge_yonu

    oyuncu_saldiriyor = False
    oyuncu_saldiri_modu = "normal"
    oyuncu_saldiri_sure_ms = ADEFO_NORMAL_SURE_MS
    ADEFO_HOLD_GECIS_YAPILDI = False
    animasyon_index = 0
    saldiri_baslangic = 0
    adefo_saldiri_tusu_baslangic_ms = 0
    adefo_hold_charge_baslangic_ms = 0
    adefo_hold_dash_baslangic_ms = 0
    adefo_hold_dash_bitis = 0
    adefo_hold_dash_son_guncelleme = 0
    adefo_hold_dash_son_ease = 0.0
    adefo_hold_dash_yonu = pygame.Vector2(0.0, 0.0)
    adefo_hold_charge_yonu = oyuncu_yonu


def oyuncu_aktif_saldiri_suresi_ms():
    if not oyuncu_saldiriyor:
        return ADEFO_NORMAL_SURE_MS if karakter_cinsiyet == "male" else saldiri_suresi
    if karakter_cinsiyet == "male" and ADEFONSUS_YENI_SHEET_AKTIF:
        if oyuncu_saldiri_modu in ("press", "charge"):
            # Bu fazlar KEYUP ile biter; genel duration timeout bunları kesmemeli.
            return 10**9
        if oyuncu_saldiri_modu == "hold_release":
            return ADEFO_HOLD_RELEASE_SURE_MS
    return max(1, int(oyuncu_saldiri_sure_ms))
# </POTBO_STAGE S0424>

# <POTBO_STAGE S0426>


def _adefo_yon_vektoru(yon=None):
    yon = oyuncu_yonu if yon is None else str(yon)
    if yon == "left":
        return pygame.Vector2(-1.0, 0.0)
    if yon == "right":
        return pygame.Vector2(1.0, 0.0)
    if yon == "up":
        return pygame.Vector2(0.0, -1.0)
    return pygame.Vector2(0.0, 1.0)


def adefonsus_saldiri_baslat(simdi=None):
    """Yeni sheet aktifken J basışını normal/hold kararının başlangıcına al.

    Stamina temel maliyeti basışta rezerve edilir. Böylece tuşa basılı tutup daha
    sonra hit almadan vazgeçerek stamina sistemini bedavaya kilitlemek mümkün olmaz.
    Quick tap KEYUP'ta normal saldırıya commit olur; hold eşiği geçilirse alt satırın
    charge frame'leri devreye girer.
    """
    global oyuncu_saldiriyor, oyuncu_saldiri_modu, oyuncu_saldiri_sure_ms
    global oyuncu_stamina, stamina_son_harcama, saldiri_baslangic, son_saldiri_zamani
    global animasyon_index, ADEFO_HOLD_GECIS_YAPILDI
    global adefo_saldiri_tusu_baslangic_ms, adefo_hold_charge_baslangic_ms
    global adefo_hold_charge_yonu

    if simdi is None:
        simdi = pygame.time.get_ticks()
    if oyuncu_saldiriyor or oyuncu_savunuyor or oyuncu_kontrol_kilitli_mi(simdi):
        return False
    if simdi - son_saldiri_zamani < saldiri_bekleme_suresi:
        return False
    if oyuncu_stamina < SALDIRI_STAMINA_MALIYETI:
        hud_uyari_baslat("stamina")
        return False

    oyuncu_stamina = max(0.0, oyuncu_stamina - SALDIRI_STAMINA_MALIYETI)
    stamina_son_harcama = simdi
    oyuncu_saldiriyor = True
    oyuncu_saldiri_modu = "press"
    oyuncu_saldiri_sure_ms = 10**9
    ADEFO_HOLD_GECIS_YAPILDI = False
    adefo_saldiri_tusu_baslangic_ms = simdi
    adefo_hold_charge_baslangic_ms = 0
    adefo_hold_charge_yonu = oyuncu_yonu
    saldiri_baslangic = simdi
    son_saldiri_zamani = simdi
    animasyon_index = 0
    dunya_olayi_kaydet("attack_prepare", mode="adefonsus_press")
    return True


def _adefo_normal_saldiriyi_commit_et(simdi):
    global oyuncu_saldiri_modu, oyuncu_saldiri_sure_ms
    global saldiri_baslangic, son_saldiri_zamani, animasyon_index
    global ADEFO_HOLD_GECIS_YAPILDI
    oyuncu_saldiri_modu = "normal"
    oyuncu_saldiri_sure_ms = ADEFO_NORMAL_SURE_MS
    ADEFO_HOLD_GECIS_YAPILDI = True
    saldiri_baslangic = int(simdi)
    son_saldiri_zamani = int(simdi)
    animasyon_index = 0
    dunya_olayi_kaydet("attack", mode="normal")


def _adefo_hold_charge_baslat(simdi):
    global oyuncu_saldiri_modu, oyuncu_saldiri_sure_ms
    global oyuncu_stamina, stamina_son_harcama, ADEFO_HOLD_GECIS_YAPILDI
    global adefo_hold_charge_baslangic_ms, adefo_hold_charge_yonu, animasyon_index

    if oyuncu_stamina < ADEFO_HOLD_EK_STAMINA:
        # Hold'a yetecek stamina yoksa basış bozulmaz; bırakınca normal vuruş gelir.
        ADEFO_HOLD_GECIS_YAPILDI = True
        hud_uyari_baslat("stamina")
        return False

    oyuncu_stamina = max(0.0, oyuncu_stamina - ADEFO_HOLD_EK_STAMINA)
    stamina_son_harcama = simdi
    oyuncu_saldiri_modu = "charge"
    oyuncu_saldiri_sure_ms = 10**9
    ADEFO_HOLD_GECIS_YAPILDI = True
    adefo_hold_charge_baslangic_ms = int(simdi)
    adefo_hold_charge_yonu = oyuncu_yonu
    animasyon_index = 0
    dunya_olayi_kaydet("attack_charge", mode="hold")
    return True


def _adefo_hold_release_baslat(simdi):
    global oyuncu_saldiri_modu, oyuncu_saldiri_sure_ms, saldiri_baslangic
    global son_saldiri_zamani, animasyon_index, oyuncu_yonu
    global adefo_hold_dash_baslangic_ms, adefo_hold_dash_bitis
    global adefo_hold_dash_son_guncelleme, adefo_hold_dash_son_ease
    global adefo_hold_dash_yonu

    oyuncu_saldiri_modu = "hold_release"
    oyuncu_saldiri_sure_ms = ADEFO_HOLD_RELEASE_SURE_MS
    saldiri_baslangic = int(simdi)
    son_saldiri_zamani = int(simdi)
    oyuncu_yonu = adefo_hold_charge_yonu
    adefo_hold_dash_yonu = _adefo_yon_vektoru(oyuncu_yonu)
    adefo_hold_dash_baslangic_ms = int(simdi)
    adefo_hold_dash_bitis = int(simdi) + ADEFO_HOLD_DASH_SURE_MS
    adefo_hold_dash_son_guncelleme = int(simdi)
    adefo_hold_dash_son_ease = 0.0
    animasyon_index = 0
    dunya_olayi_kaydet("attack", mode="hold_release")


def adefonsus_saldiri_tusu_birakildi(simdi=None):
    """KEYUP veya missed-KEYUP recovery için tek release noktası."""
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if (
        not oyuncu_saldiriyor
        or karakter_cinsiyet != "male"
        or not ADEFONSUS_YENI_SHEET_AKTIF
    ):
        return False
    if oyuncu_saldiri_modu == "press":
        # KEYUP iki render tick'i arasına düşebilir. Süre eşiği geçmişse state
        # updater'ı henüz charge'a çevirmemiş olsa bile hold niyetini kaybetmeyiz.
        gecen = int(simdi) - int(adefo_saldiri_tusu_baslangic_ms)
        if gecen >= ADEFO_HOLD_ESIK_MS and _adefo_hold_charge_baslat(simdi):
            _adefo_hold_release_baslat(simdi)
        else:
            _adefo_normal_saldiriyi_commit_et(simdi)
        return True
    if oyuncu_saldiri_modu == "charge":
        _adefo_hold_release_baslat(simdi)
        return True
    return False


def adefonsus_charge_yon_guncelle():
    """Charge sırasında yürütmeden dört yön nişanı verir.

    Son basılan/baskın eksen mantığı normal locomotion ile aynı kalır. Bu yalnızca
    facing'i değiştirir; oyuncu_x/y değiştirilmez.
    """
    global oyuncu_yonu, adefo_hold_charge_yonu
    if (
        karakter_cinsiyet != "male"
        or not ADEFONSUS_YENI_SHEET_AKTIF
        or not oyuncu_saldiriyor
        or oyuncu_saldiri_modu not in ("press", "charge")
    ):
        return
    try:
        tuslar = pygame.key.get_pressed()
    except pygame.error:
        return

    dx = int(bool(tuslar[tus_atamasi("move_right")])) - int(
        bool(tuslar[tus_atamasi("move_left")])
    )
    dy = int(bool(tuslar[tus_atamasi("move_down")])) - int(
        bool(tuslar[tus_atamasi("move_up")])
    )
    if dx == 0 and dy == 0:
        return
    if abs(dy) > abs(dx):
        oyuncu_yonu = "down" if dy > 0 else "up"
    elif dx != 0:
        oyuncu_yonu = "right" if dx > 0 else "left"
    adefo_hold_charge_yonu = oyuncu_yonu


def oyuncu_saldiri_gecislerini_guncelle(simdi=None):
    """Adefonsus press -> charge -> release zincirini frame güvenli günceller.

    Pygame pencere odağı kaybederken KEYUP kaçırılabildiği için fiziksel tuş durumu
    da doğrulanır. Bu, sonsuz charge ve saldırı input-lock bug'ını önler.
    """
    global stamina_son_harcama
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if not oyuncu_saldiriyor:
        return
    if karakter_cinsiyet != "male" or not ADEFONSUS_YENI_SHEET_AKTIF:
        return

    adefonsus_charge_yon_guncelle()
    if oyuncu_saldiri_modu in ("press", "charge"):
        stamina_son_harcama = int(simdi)

    if oyuncu_saldiri_modu == "press":
        gecen = int(simdi) - int(adefo_saldiri_tusu_baslangic_ms)
        if not oyuncu_saldiri_tusu_basili_mi():
            _adefo_normal_saldiriyi_commit_et(simdi)
            return
        if gecen >= ADEFO_HOLD_ESIK_MS and not ADEFO_HOLD_GECIS_YAPILDI:
            _adefo_hold_charge_baslat(simdi)
            return

    elif oyuncu_saldiri_modu == "charge":
        if not oyuncu_saldiri_tusu_basili_mi():
            _adefo_hold_release_baslat(simdi)
            return
        # Charge hasarı süreyle ölçeklenmez; 2.5x sabittir. Süre yalnız görsel pulse
        # için clamp edilir, böylece oyuncu sonsuza kadar tutarak one-shot üretemez.
        if adefo_hold_charge_baslangic_ms:
            _ = min(
                ADEFO_HOLD_MAX_CHARGE_MS,
                int(simdi) - int(adefo_hold_charge_baslangic_ms),
            )


def adefonsus_hold_dash_guncelle(simdi=None):
    """Release slash'ın collision-safe, ease-out fizik hareketi.

    Dash teleport değildir: toplam mesafe frame delta ile parçalara bölünür ve her
    alt adım mevcut oyuncu collision sisteminden geçer. Enemy body de blocker olduğu
    için Adefonsus hedefin içinden geçmez; tam temas noktasında keser.
    """
    global oyuncu_x, oyuncu_y
    global adefo_hold_dash_son_guncelleme, adefo_hold_dash_son_ease

    if simdi is None:
        simdi = pygame.time.get_ticks()
    if (
        not oyuncu_saldiriyor
        or oyuncu_saldiri_modu != "hold_release"
        or adefo_hold_dash_baslangic_ms <= 0
        or int(simdi) >= adefo_hold_dash_bitis
    ):
        return False

    sure = max(1.0, float(ADEFO_HOLD_DASH_SURE_MS))
    p = max(
        0.0,
        min(
            1.0,
            (int(simdi) - adefo_hold_dash_baslangic_ms) / sure,
        ),
    )
    # sin ease-out: ilk anda güçlü kopuş, son bölümde akıcı frenleme.
    ease = math.sin(p * math.pi * 0.5)
    delta_ease = max(0.0, ease - float(adefo_hold_dash_son_ease))
    adefo_hold_dash_son_ease = ease
    adefo_hold_dash_son_guncelleme = int(simdi)
    mesafe = ADEFO_HOLD_DASH_MESAFESI * delta_ease
    if mesafe <= 0.0001 or adefo_hold_dash_yonu.length_squared() <= 1e-6:
        return False

    kalan = mesafe
    hareket_oldu = False
    yon = adefo_hold_dash_yonu.normalize()
    while kalan > 0.0001:
        adim = min(ADEFO_HOLD_DASH_ADIMI, kalan)
        yeni_x = max(
            35.0,
            min(HARITA_GENISLIK - 35.0, oyuncu_x + yon.x * adim),
        )
        yeni_y = max(
            35.0,
            min(HARITA_YUKSEKLIK - 25.0, oyuncu_y + yon.y * adim),
        )
        if not hareket_gecerli_mi(yeni_x, yeni_y):
            # Duvar/enemy temasında kalan dash iptal edilir; sonraki framelerde
            # aynı collision'a tekrar tekrar basıp jitter üretmesin.
            adefo_hold_dash_son_ease = 1.0
            break
        oyuncu_x, oyuncu_y = yeni_x, yeni_y
        kalan -= adim
        hareket_oldu = True
    return hareket_oldu


def oyuncu_saldiri_vurus_penceresi_aktif_mi(simdi=None):
    """Telegraph -> active -> recovery ayrımı; charge tek başına asla hasar vermez."""
    if not oyuncu_saldiriyor:
        return False
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if karakter_cinsiyet == "male" and ADEFONSUS_YENI_SHEET_AKTIF:
        if oyuncu_saldiri_modu in ("press", "charge"):
            return False
        sure = max(1.0, float(oyuncu_aktif_saldiri_suresi_ms()))
        ilerleme = (simdi - saldiri_baslangic) / sure
        if oyuncu_saldiri_modu == "hold_release":
            return 0.04 <= ilerleme <= 0.70
        return 0.28 <= ilerleme <= 0.72
    sure = max(1.0, float(oyuncu_aktif_saldiri_suresi_ms()))
    ilerleme = (simdi - saldiri_baslangic) / sure
    return 0.255 <= ilerleme <= 0.595


def oyuncu_saldiri_hasar_miktari():
    carpan = 1.0
    if karakter_cinsiyet == "male" and oyuncu_saldiri_modu == "hold_release":
        carpan = ADEFO_HOLD_HASAR_CARPANI
    elif karakter_cinsiyet == "male":
        carpan = ADEFO_NORMAL_HASAR_CARPANI
    return max(1, int(round(float(oyuncu_hasari) * carpan)))


def oyuncu_saldiri_vurus_rect():
    """Yönsel yakın dövüş hitbox'ı; charge/pending fazında boş döner.

    Heavy release'ın hitbox'ı dash ile birlikte hareket eder. Menzil dash'in kendisi
    tarafından üretilir; burada ayrıca dev bir görünmez rect verilip uzaktan vurma
    yaratılmaz.
    """
    if (
        karakter_cinsiyet == "male"
        and ADEFONSUS_YENI_SHEET_AKTIF
        and oyuncu_saldiri_modu in ("press", "charge")
    ):
        return pygame.Rect(int(round(oyuncu_x)), int(round(oyuncu_y)), 1, 1)

    merkez_x = int(round(oyuncu_x))
    merkez_y = int(round(oyuncu_y - 18))
    heavy = karakter_cinsiyet == "male" and oyuncu_saldiri_modu == "hold_release"
    ileri = 88 if heavy else 62
    yan = 58 if heavy else 48

    if oyuncu_yonu == "left":
        return pygame.Rect(
            merkez_x - ileri,
            merkez_y - yan // 2,
            ileri + 4,
            yan,
        )
    if oyuncu_yonu == "right":
        return pygame.Rect(merkez_x - 4, merkez_y - yan // 2, ileri + 4, yan)
    if oyuncu_yonu == "up":
        return pygame.Rect(
            merkez_x - yan // 2,
            merkez_y - ileri,
            yan,
            ileri + 4,
        )
    return pygame.Rect(merkez_x - yan // 2, merkez_y - 4, yan, ileri + 4)
# </POTBO_STAGE S0426>

# <POTBO_STAGE S0506>


def _savunma_kaynagi_onden_mi(kaynak_x, kaynak_y):
    to_source = pygame.Vector2(float(kaynak_x) - oyuncu_x, float(kaynak_y) - oyuncu_y)
    if to_source.length_squared() <= 1e-6:
        return True
    face = _adefo_yon_vektoru(oyuncu_yonu)
    return face.dot(to_source.normalize()) >= -0.10


def oyuncu_savunma_darbe_karsila(kaynak_turu, kaynak_x, kaynak_y, attacker=None):
    global oyuncu_stamina, stamina_son_harcama
    global oyuncu_savunuyor, savunma_zincir_vurus, savunma_son_temasi
    simdi = pygame.time.get_ticks()
    if oyuncu_hp <= 0 or not oyuncu_savunuyor:
        return False
    if not _savunma_kaynagi_onden_mi(kaynak_x, kaynak_y):
        return False
    sinif = _savunma_sinifi(kaynak_turu)
    limit = int(SAVUNMA_ZINCIR_LIMITI[sinif])
    if savunma_zincir_vurus >= limit:
        return False
    maliyet = float(SAVUNMA_STAMINA_MALIYETI[sinif])
    if oyuncu_stamina < maliyet:
        oyuncu_stamina = 0.0
        oyuncu_savunuyor = False
        hud_uyari_baslat("stamina")
        return False

    oyuncu_stamina = max(0.0, oyuncu_stamina - maliyet)
    stamina_son_harcama = simdi
    savunma_zincir_vurus += 1
    savunma_son_temasi = simdi

    incoming = pygame.Vector2(oyuncu_x - float(kaynak_x), oyuncu_y - float(kaynak_y))
    if incoming.length_squared() <= 1e-6:
        incoming = _adefo_yon_vektoru(oyuncu_yonu)

    if sinif == "heavy":
        # Ağır silah: tek sert kesişim ve saldırıyı gerçekten durdurma.
        combat_impact_spawn(
            oyuncu_x,
            oyuncu_y - 12,
            "slash_heavy",
            1.75,
            incoming,
        )
        kamera_hit_sarsintisi_baslat(6.5, 150)
        durdurma = 540
    else:
        # Hafif/orta savunmada tek kesik yerine üç ayrı çarpışma izi.
        for aci in (-22.0, 0.0, 22.0):
            combat_impact_spawn(
                oyuncu_x,
                oyuncu_y - 12,
                "slash",
                1.05,
                incoming.rotate(aci),
            )
        kamera_hit_sarsintisi_baslat(3.8 if sinif == "medium" else 2.5, 115)
        durdurma = 310 if sinif == "medium" else 220

    if attacker is not None:
        try:
            attacker.attacking = False
            attacker.attack_connected = True
            attacker.attack_damage_applied = True
            attacker.recovery_until = max(
                int(getattr(attacker, "recovery_until", 0)),
                simdi + durdurma,
            )
            attacker.hit_stun_until = max(
                int(getattr(attacker, "hit_stun_until", 0)),
                simdi + durdurma // 2,
            )
            attacker.vx *= -0.18
            attacker.vy *= -0.18
        except Exception:
            pass
    return True
# </POTBO_STAGE S0506>

# <POTBO_STAGE S0533>


def oyuncu_agir_darbe_uygula(kaynak_x, kaynak_y, kaynak_adi="Tarkard"):
    """
    Tarkard'ın tek ağır vuruş kontratı:
      - oyuncu maksimum canının %75'i kadar hasar,
      - stamina doğrudan 0,
      - 2.0 saniye kontrol kaybı,
      - collision-aware fiziksel savrulma.

    Hasar max HP üzerinden hesaplanır; stat yatırımı saldırıyı anlamsızlaştırmaz.
    Düşük candaki oyuncu ölebilir. Ağır darbe aynı active frame'de iki kez uygulanamaz.
    """
    global oyuncu_hp, oyuncu_stamina, stamina_son_harcama
    global oyuncu_baygin_bitis, oyuncu_zorlanmis_hiz, oyuncu_zorlanmis_bitis
    global oyuncu_zorlanmis_son_guncelleme, oyuncu_agir_darbe_bagisiklik_bitis
    global oyuncu_saldiriyor, animasyon_index, son_dash_zamani, dash_tus_kilitli
    global oyuncu_saldiri_modu, oyuncu_saldiri_sure_ms, ADEFO_HOLD_GECIS_YAPILDI

    simdi = pygame.time.get_ticks()
    if simdi < oyuncu_agir_darbe_bagisiklik_bitis or oyuncu_hp <= 0:
        return 0

    hasar = max(1, int(math.ceil(float(oyuncu_max_hp) * 0.75)))
    oyuncu_hp = max(0, int(oyuncu_hp) - hasar)
    oyuncu_kanli_hasar_kaydi(kaynak_x, kaynak_y, "heavy_blunt", hasar, kaynak_adi)
    oyuncu_stamina = 0.0
    oyuncu_baygin_bitis = simdi + 2000
    oyuncu_agir_darbe_bagisiklik_bitis = simdi + 420
    stamina_son_harcama = oyuncu_baygin_bitis

    # Aktif saldırı/charge/release commitment tek merkezden kesilir; gelecekte
    # yeni transient alan eklendiğinde heavy-hit reset kodunun geride kalmaması sağlanır.
    oyuncu_saldiri_durumunu_sifirla()
    son_dash_zamani = simdi
    dash_tus_kilitli = True

    itme = pygame.Vector2(oyuncu_x - float(kaynak_x), oyuncu_y - float(kaynak_y))
    if itme.length_squared() <= 1e-6:
        itme = pygame.Vector2(1.0, 0.15)
    itme = itme.normalize()
    oyuncu_zorlanmis_hiz = itme * 720.0
    oyuncu_zorlanmis_bitis = simdi + 470
    oyuncu_zorlanmis_son_guncelleme = simdi

    combat_impact_spawn(
        oyuncu_x,
        oyuncu_y - 12,
        "shock_heavy",
        2.2,
        pygame.Vector2(oyuncu_x - kaynak_x, oyuncu_y - kaynak_y),
    )
    kamera_hit_sarsintisi_baslat(10.5, 320)
    dunya_olayi_kaydet("hit_taken", damage=hasar, count=1, enemy="tarkard")
    bildirim_goster(
        bt(
            f"{kaynak_adi} seni yere serdi: -{hasar} can, stamina 0.",
            f"{kaynak_adi} knocked you down: -{hasar} HP, stamina 0.",
        ),
        PARLAK_KIRMIZI,
    )
    return hasar


def oyuncu_infaz_darbesi_uygula(
    kaynak_x,
    kaynak_y,
    kaynak_adi="Sir Torrmund",
    saldiri_yonu="right",
):
    """Sir Torrmund'un ölümcül kesme kontratı.

    Knockback yoktur: darbe karakteri fiziksel olarak savurmak yerine bulunduğu
    yerde keser. Tek saldırı active window'unda yalnız bir kez uygulanır; HP 0'a
    iner, stamina boşalır, aktif saldırı/dash iptal edilir ve keskin ekran izi doğar.
    """
    global oyuncu_hp, oyuncu_stamina, stamina_son_harcama
    global oyuncu_baygin_bitis, oyuncu_saldiriyor, animasyon_index
    global oyuncu_saldiri_modu, oyuncu_saldiri_sure_ms, ADEFO_HOLD_GECIS_YAPILDI
    global son_dash_zamani, dash_tus_kilitli
    global \
        oyuncu_kesik_efekti_bitis, \
        oyuncu_kesik_efekti_acisi, \
        oyuncu_son_infaz_kaynagi
    global oyuncu_agir_darbe_bagisiklik_bitis

    simdi = pygame.time.get_ticks()
    if oyuncu_hp <= 0 or simdi < oyuncu_agir_darbe_bagisiklik_bitis:
        return 0

    hasar = max(1, int(oyuncu_hp))
    oyuncu_hp = 0
    oyuncu_kanli_hasar_kaydi(kaynak_x, kaynak_y, "heavy_slash", hasar, kaynak_adi)
    oyuncu_stamina = 0.0
    stamina_son_harcama = simdi + 999999
    oyuncu_baygin_bitis = max(oyuncu_baygin_bitis, simdi + 900)
    oyuncu_agir_darbe_bagisiklik_bitis = simdi + 900
    oyuncu_saldiri_durumunu_sifirla()
    son_dash_zamani = simdi
    dash_tus_kilitli = True

    # Yatay facing'e göre çapraz kesik yönü; hareket/knockback yoktur.
    oyuncu_kesik_efekti_acisi = -18.0 if saldiri_yonu in ("right", "down") else 18.0
    oyuncu_kesik_efekti_bitis = simdi + 520
    oyuncu_son_infaz_kaynagi = str(kaynak_adi)

    combat_impact_spawn(
        oyuncu_x,
        oyuncu_y - 12,
        "slash_heavy",
        2.0,
        _common_enemy_yon_vektoru(saldiri_yonu),
    )
    kamera_hit_sarsintisi_baslat(7.0, 145)
    dunya_olayi_kaydet(
        "hit_taken",
        damage=hasar,
        count=1,
        enemy="sir_torrmund",
        lethal=True,
    )
    bildirim_goster(
        bt(
            f"{kaynak_adi} tek darbede seni kesti.",
            f"{kaynak_adi} cut you down in a single blow.",
        ),
        PARLAK_KIRMIZI,
    )
    return hasar
# </POTBO_STAGE S0533>

# <POTBO_STAGE S0541>


def gelistirici_x_skill_r_baslat(simdi=None):
    """Ctrl+U açıkken yalnız gerçek hold-charge içinde R kombinasyonunu arm eder."""
    global gelistirici_x_skill_r_basildi
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if not gelistirici_x_skill_aktif or gelistirici_x_skill_aktif_mi(simdi):
        return False
    if (
        karakter_cinsiyet != "male"
        or not ADEFONSUS_YENI_SHEET_AKTIF
        or not oyuncu_saldiriyor
    ):
        return False

    # KEYDOWN tam eşik framine denk geldiyse charge updater'ını beklemeden hold'u kur.
    if oyuncu_saldiri_modu == "press":
        gecen = int(simdi) - int(adefo_saldiri_tusu_baslangic_ms)
        if gecen < ADEFO_HOLD_ESIK_MS or not _adefo_hold_charge_baslat(simdi):
            return False
    if oyuncu_saldiri_modu != "charge":
        return False

    gelistirici_x_skill_r_basildi = True
    return True
# </POTBO_STAGE S0541>

# <POTBO_STAGE S0544>


def _gelistirici_x_skill_yol_kur(hedef, baslangic):
    """Düz giriş + sabit '/' ve '\\' diyagonallerini kurar.

    Slash-1 kesin olarak alttan üste gider: bottom-left -> top-right (/).
    Slash-2 kesin olarak üstten alta gider: top-left -> bottom-right (\\).
    Böylece hedefe geliş yönü değişse bile special move'un imzası ekranda sabit kalır.
    """
    merkez = pygame.Vector2(float(hedef.x), float(hedef.y))
    bas = pygame.Vector2(baslangic)
    yaklasim = merkez - bas
    if yaklasim.length_squared() <= 1e-6:
        yaklasim = _adefo_yon_vektoru(adefo_hold_charge_yonu)
    if yaklasim.length_squared() <= 1e-6:
        yaklasim = pygame.Vector2(1.0, 0.0)
    yaklasim = yaklasim.normalize()

    # HIT-1: düz giriş hedefte durmaz; karakter hedef merkezinin içinden gerçekten
    # geçip yaklaşık 72 px ötesine çıkar. İlk temas böylece gerçek beden hareketidir.
    entry = merkez + yaklasim * 72.0
    entry.x = max(35.0, min(HARITA_GENISLIK - 35.0, entry.x))
    entry.y = max(35.0, min(HARITA_YUKSEKLIK - 25.0, entry.y))

    r = GELISTIRICI_X_SKILL_YARI_CAP
    h = r * 0.78
    slash1_start = _gelistirici_x_skill_nokta(hedef, -r, +h)  # alt-sol
    slash1_end = _gelistirici_x_skill_nokta(hedef, +r, -h)  # üst-sağ
    slash2_start = _gelistirici_x_skill_nokta(hedef, -r, -h)  # üst-sol
    slash2_end = _gelistirici_x_skill_nokta(hedef, +r, +h)  # alt-sağ
    return [
        bas,
        entry,
        slash1_start,
        slash1_end,
        slash2_start,
        slash2_end,
    ]


def gelistirici_x_skill_r_birak(simdi=None):
    """Armed R bırakılınca hold charge'ı üç fiziksel vuruşlu special move'a çevirir."""
    global gelistirici_x_skill_r_basildi, gelistirici_x_skill_baslangic_ms
    global gelistirici_x_skill_bitis_ms, gelistirici_x_skill_hedef
    global \
        gelistirici_x_skill_yol, \
        gelistirici_x_skill_vurus_maskesi, \
        gelistirici_x_skill_iz_bitis
    global oyuncu_hareket_hiz_vektoru, oyuncu_zorlanmis_hiz, oyuncu_zorlanmis_bitis
    global dash_aktif_bitis, dash_aktif_yonu, dash_aktif_son_ease, dash_tus_kilitli
    global oyuncu_savunuyor

    if simdi is None:
        simdi = pygame.time.get_ticks()
    if not gelistirici_x_skill_r_basildi:
        return False
    gelistirici_x_skill_r_basildi = False
    if not gelistirici_x_skill_aktif or oyuncu_saldiri_modu != "charge":
        return False

    yon = _adefo_yon_vektoru(adefo_hold_charge_yonu)
    hedef = _gelistirici_x_skill_hedef_sec(yon)
    if hedef is None:
        bildirim_goster(
            bt(
                "Özel hareket için menzilde hedef yok.",
                "No target in range for the special move.",
            ),
            GRI,
        )
        return False

    baslangic = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    gelistirici_x_skill_hedef = hedef
    gelistirici_x_skill_yol = _gelistirici_x_skill_yol_kur(hedef, baslangic)
    gelistirici_x_skill_baslangic_ms = int(simdi)
    gelistirici_x_skill_bitis_ms = int(simdi) + GELISTIRICI_X_SKILL_SURE_MS
    gelistirici_x_skill_vurus_maskesi = 0
    gelistirici_x_skill_iz_bitis = int(simdi) + GELISTIRICI_X_SKILL_SURE_MS + 230

    # Charge saldırısını burada tüket: J daha sonra bırakılsa bile normal hold-release
    # üretilmez. Special move kendi hareket state'iyle karakteri sürer.
    oyuncu_saldiri_durumunu_sifirla()

    # Special move başlarken diğer bütün hareket kanalları kesilir. Önceki yürüyüş
    # ivmesi, dash veya knockback momentumu authored üç-vuruş rotasını bozamaz.
    oyuncu_hareket_hiz_vektoru.update(0.0, 0.0)
    oyuncu_zorlanmis_hiz.update(0.0, 0.0)
    oyuncu_zorlanmis_bitis = 0
    dash_aktif_bitis = 0
    dash_aktif_yonu = pygame.Vector2(0.0, 0.0)
    dash_aktif_son_ease = 0.0
    dash_tus_kilitli = True
    oyuncu_savunuyor = False

    # Hedef teknik boyunca kısa bir commitment stun'ında kalır; böylece karakterin
    # gerçek dash rotası ile hit anları birbirinden kopmaz. Süre bitince AI devam eder.
    try:
        hedef.hit_stun_until = max(
            int(getattr(hedef, "hit_stun_until", 0)),
            gelistirici_x_skill_bitis_ms,
        )
        hedef.recovery_until = max(
            int(getattr(hedef, "recovery_until", 0)),
            gelistirici_x_skill_bitis_ms,
        )
        hedef.attacking = False
        hedef.vx = 0.0
        hedef.vy = 0.0
    except Exception:
        pass

    kamera_hit_sarsintisi_baslat(3.0, 90)
    dunya_olayi_kaydet(
        "developer_x_special_move",
        trigger="hold+r",
        target=str(getattr(hedef, "tur", "enemy")),
        hits=3,
    )
    return True
# </POTBO_STAGE S0544>

# <POTBO_STAGE S0554>


# =========================================================
# DEATH CONTACT + RAGGED DISMEMBERMENT + TRUE BURN DEATH
# =========================================================
# geometrisini / parçalanma sunumunu değiştirir. Yeni sprite gerekmez; Adefonsus'un
# mevcut idle silüeti runtime alpha maskeleriyle tırtıklı parçalara ayrılır.

V32_OLUM_KATIL_READY_MS = 0
# </POTBO_STAGE S0554>

# <POTBO_STAGE S0564>


def _stage2__v30_olum_koreografi_guncelle(simdi):
    """V32: önce fiziksel temas, sonra post-mortem saldırı."""
    global oyuncu_olum_ikiye_bolundu
    if oyuncu_olum_baslangic_ms <= 0 or oyuncu_olum_turu not in (
        "blood",
        "blast_inner",
    ):
        return
    alt = str(oyuncu_olum_alt_turu or "")
    if not alt:
        return

    ready = _v32_katil_temasa_yaklastir(simdi)
    if ready <= 0:
        return
    gecen = max(0, int(simdi) - int(ready))
    katil = _v24_olum_katil_actor_bul()
    if katil is not None:
        base = pygame.Vector2(oyuncu_x - float(katil.x), oyuncu_y - float(katil.y))
    else:
        base = _adefo_yon_vektoru(oyuncu_yonu)
    if base.length_squared() <= 1e-6:
        base = pygame.Vector2(1.0, 0.0)
    base = base.normalize()

    def vur(key, zaman, blood_n, gore_n, power, yoff=-9.0, puddle=0):
        if gecen < zaman or key in oyuncu_olum_koreografi_vuruslari:
            return False
        oyuncu_olum_koreografi_vuruslari.add(key)
        kan_parcacigi_patlat(
            oyuncu_x,
            oyuncu_y + yoff,
            blood_n,
            power,
            yon=base,
            arterial=power > 1.42,
        )
        _v30_kucuk_gore_jet(
            oyuncu_x,
            oyuncu_y + yoff,
            gore_n,
            base,
            max(0.72, power * 0.70),
            True,
        )
        for _ in range(max(0, int(puddle))):
            kan_lekesi_ekle(
                oyuncu_x + random.uniform(-11.0, 11.0),
                oyuncu_y + random.uniform(-6.0, 8.0),
                random.uniform(0.52, 1.10) * min(1.25, power),
            )
        kamera_hit_sarsintisi_baslat(3.5 + power * 2.7, int(82 + power * 48))
        return True

    if alt == "crawler":
        # Ceset yerleşmiş ve crawler gerçek temas menzilindedir. Altı darbe birbirine
        # yakın gelir; her biri yeni bir küçük tırtıklı kopma ve organ jeti üretir.
        zamanlar = (70, 205, 340, 475, 610, 745)
        for i, zaman in enumerate(zamanlar):
            vur(
                f"crawler_{i}",
                zaman,
                random.randint(20, 29),
                random.randint(3, 5),
                1.04 + i * 0.028,
                -9.0,
                1 if i in (2, 5) else 0,
            )
    elif alt == "berserker":
        zamanlar = (80, 235, 390, 545, 700, 855)
        for i, zaman in enumerate(zamanlar):
            vur(
                f"bers_{i}",
                zaman,
                random.randint(29, 42),
                random.randint(4, 6),
                1.26 + i * 0.038,
                -13.0,
                1,
            )
    elif alt == "headshot":
        vur(
            "head_residual",
            120,
            random.randint(12, 18),
            random.randint(2, 3),
            0.92,
            -24.0,
            1,
        )
    elif alt == "tarkard_crush":
        # Tek hareket. Temas + ceset yerleşmesi garanti edilmeden whirl başlamaz.
        vur(
            "tarkard_whirl",
            110,
            random.randint(66, 84),
            random.randint(26, 34),
            1.82,
            -8.0,
            4,
        )
    elif alt == "torrmund_decap_cleave":
        if vur(
            "torrmund_second",
            1060,
            random.randint(72, 96),
            random.randint(18, 24),
            1.96,
            -8.0,
            4,
        ):
            oyuncu_olum_ikiye_bolundu = True
# </POTBO_STAGE S0564>

# <POTBO_STAGE S0590>


# Post-mortem: yalnız Crawler/Berserker altı gerçek temas. Tarkard burada yoktur.
def _v30_olum_koreografi_guncelle(simdi):
    global oyuncu_olum_ikiye_bolundu
    if oyuncu_olum_baslangic_ms <= 0 or oyuncu_olum_turu not in (
        "blood",
        "blast_inner",
    ):
        return
    alt = str(oyuncu_olum_alt_turu or "")
    if not alt or alt == "tarkard_crush":
        return

    # Crawler/Berserker ancak cesede yürüyüp el/silah teması kurduktan sonra başlar.
    # Torrmund'un decap->cleave istisnası aynı ready kontratını kullanır.
    ready = _v32_katil_temasa_yaklastir(simdi)
    if ready <= 0:
        return
    gecen = max(0, int(simdi) - int(ready))
    katil = _v24_olum_katil_actor_bul()
    if katil is not None:
        base = pygame.Vector2(oyuncu_x - float(katil.x), oyuncu_y - float(katil.y))
    else:
        base = _adefo_yon_vektoru(oyuncu_yonu)
    if base.length_squared() <= 1e-6:
        base = pygame.Vector2(1.0, 0.0)
    base = base.normalize()

    def vur(key, zaman, blood_n, gore_n, power, yoff=-9.0, puddle=0):
        if gecen < zaman or key in oyuncu_olum_koreografi_vuruslari:
            return False
        oyuncu_olum_koreografi_vuruslari.add(key)
        kan_parcacigi_patlat(
            oyuncu_x,
            oyuncu_y + yoff,
            blood_n,
            power,
            yon=base,
            arterial=power > 1.36,
        )
        _v30_kucuk_gore_jet(
            oyuncu_x,
            oyuncu_y + yoff,
            gore_n,
            base,
            max(0.78, power * 0.74),
            True,
        )
        for _ in range(max(0, int(puddle))):
            kan_lekesi_ekle(
                oyuncu_x + random.uniform(-12.0, 12.0),
                oyuncu_y + random.uniform(-7.0, 9.0),
                random.uniform(0.50, 1.12) * min(1.25, power),
            )
        kamera_hit_sarsintisi_baslat(3.8 + power * 2.9, int(88 + power * 52))
        return True

    if alt == "crawler":
        zamanlar = (70, 205, 340, 475, 610, 745)
        for i, zaman in enumerate(zamanlar):
            vur(
                f"crawler_{i}",
                zaman,
                random.randint(24, 34),
                random.randint(4, 7),
                1.06 + i * 0.03,
                -9.0,
                1 if i in (1, 3, 5) else 0,
            )
    elif alt == "berserker":
        zamanlar = (80, 235, 390, 545, 700, 855)
        for i, zaman in enumerate(zamanlar):
            vur(
                f"bers_{i}",
                zaman,
                random.randint(34, 48),
                random.randint(5, 8),
                1.30 + i * 0.04,
                -13.0,
                1,
            )
    elif alt == "headshot":
        # Head Thrower ekstra post-hit yapmaz; yalnız kırılmış baştan residual akış.
        vur(
            "head_residual",
            120,
            random.randint(16, 24),
            random.randint(3, 5),
            0.96,
            -24.0,
            1,
        )
    elif alt == "torrmund_decap_cleave":
        # İstisna: ilk darbe sadece kafayı uçurduysa bazen ikinci, farklı heavy cleave.
        # Bisect senaryosunda bu branch hiç yoktur.
        if vur(
            "torrmund_second",
            1060,
            random.randint(82, 108),
            random.randint(22, 30),
            2.02,
            -8.0,
            4,
        ):
            oyuncu_olum_ikiye_bolundu = True
# </POTBO_STAGE S0590>

# <POTBO_STAGE S0656>


# ---------------------------------------------------------
# SPECIAL MOVE PATH PLANNING
# ---------------------------------------------------------
def _v34_special_candidate_path(hedef, baslangic, radius):
    center = pygame.Vector2(float(hedef.x), float(hedef.y))
    start = pygame.Vector2(baslangic)
    approach = center - start
    if approach.length_squared() <= 1e-6:
        approach = _adefo_yon_vektoru(adefo_hold_charge_yonu)
    if approach.length_squared() <= 1e-6:
        approach = pygame.Vector2(1.0, 0.0)
    approach = approach.normalize()

    entry = center + approach * min(V34_SPECIAL_ENTRY_OVERSHOOT, radius * 0.68)
    h = radius * 0.78
    p1 = center + pygame.Vector2(-radius, +h)
    p2 = center + pygame.Vector2(+radius, -h)
    p3 = center + pygame.Vector2(-radius, -h)
    p4 = center + pygame.Vector2(+radius, +h)
    return [start, entry, p1, p2, p3, p4]
# </POTBO_STAGE S0656>

# <POTBO_STAGE S0661>


def gelistirici_x_skill_r_birak(simdi=None):
    """V34 special start: preflight, hard input lock, target commitment ve safe path."""
    global gelistirici_x_skill_r_basildi, gelistirici_x_skill_baslangic_ms
    global gelistirici_x_skill_bitis_ms, gelistirici_x_skill_hedef
    global \
        gelistirici_x_skill_yol, \
        gelistirici_x_skill_vurus_maskesi, \
        gelistirici_x_skill_iz_bitis
    global oyuncu_hareket_hiz_vektoru, oyuncu_zorlanmis_hiz, oyuncu_zorlanmis_bitis
    global dash_aktif_bitis, dash_aktif_yonu, dash_aktif_son_ease, dash_tus_kilitli
    global oyuncu_savunuyor, v34_special_effect_center, v34_special_last_pos
    global \
        v34_special_move_serial, \
        v34_special_exit_safe_pos, \
        v34_special_last_target_uid
    global v34_special_recovery_grace_until

    if simdi is None:
        simdi = pygame.time.get_ticks()
    simdi = int(simdi)
    if not gelistirici_x_skill_r_basildi:
        return False
    gelistirici_x_skill_r_basildi = False
    if not gelistirici_x_skill_aktif or oyuncu_saldiri_modu != "charge":
        return False

    yon = _adefo_yon_vektoru(adefo_hold_charge_yonu)
    hedef = _gelistirici_x_skill_hedef_sec(yon)
    if hedef is None:
        bildirim_goster(
            bt(
                "Özel hareket için menzilde hedef yok.",
                "No target in range for the special move.",
            ),
            GRI,
        )
        return False

    start = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    path = _gelistirici_x_skill_yol_kur(hedef, start)
    if len(path) < 6:
        bildirim_goster(
            bt(
                "Özel hareket yolu kurulamadı.",
                "Special move path could not be built.",
            ),
            GRI,
        )
        return False

    # Path fallback static olarak tamamen temiz değilse special'ı duvar içine sokmak
    # yerine kontrollü biçimde reddet. Oyuncunun input'u normal charge'da kalır.
    if not v34_special_path_valid:
        bildirim_goster(
            bt(
                "Bu alanda özel hareket için yeterli boşluk yok.",
                "Not enough clear space for the special move here.",
            ),
            GRI,
        )
        return False

    gelistirici_x_skill_hedef = hedef
    gelistirici_x_skill_yol = path
    gelistirici_x_skill_baslangic_ms = simdi
    gelistirici_x_skill_bitis_ms = simdi + GELISTIRICI_X_SKILL_SURE_MS
    gelistirici_x_skill_vurus_maskesi = 0
    gelistirici_x_skill_iz_bitis = gelistirici_x_skill_bitis_ms + 300
    v34_special_effect_center = pygame.Vector2(float(hedef.x), float(hedef.y))
    v34_special_last_pos = start.copy()
    v34_special_exit_safe_pos = None
    v34_special_recovery_grace_until = (
        gelistirici_x_skill_bitis_ms + V34_SPECIAL_RECOVERY_GRACE_MS
    )
    v34_special_move_serial += 1
    v34_special_last_target_uid = str(
        getattr(hedef, "uid", getattr(hedef, "tur", "enemy"))
    )
    v34_special_trail.clear()
    v34_special_afterimages.clear()
    _v34_special_register_trail(simdi, start, "entry")

    oyuncu_saldiri_durumunu_sifirla()
    oyuncu_hareket_hiz_vektoru.update(0.0, 0.0)
    oyuncu_zorlanmis_hiz.update(0.0, 0.0)
    oyuncu_zorlanmis_bitis = 0
    dash_aktif_bitis = 0
    dash_aktif_yonu = pygame.Vector2(0.0, 0.0)
    dash_aktif_son_ease = 0.0
    dash_tus_kilitli = True
    oyuncu_savunuyor = False

    try:
        lock_until = gelistirici_x_skill_bitis_ms + V34_SPECIAL_TARGET_LOCK_EXTRA_MS
        hedef.hit_stun_until = max(int(getattr(hedef, "hit_stun_until", 0)), lock_until)
        hedef.recovery_until = max(int(getattr(hedef, "recovery_until", 0)), lock_until)
        hedef.attacking = False
        hedef.vx = 0.0
        hedef.vy = 0.0
    except Exception:
        pass

    # Başlangıç feedback'i vuruş gibi ağır değildir; yalnız teknik commit edildiğini söyler.
    kamera_hit_sarsintisi_baslat(2.2, 82)
    dunya_olayi_kaydet(
        "developer_x_special_move",
        trigger="hold+r",
        target=str(getattr(hedef, "tur", "enemy")),
        hits=3,
        radius=float(v34_special_effect_radius),
        collision_safe=True,
        serial=v34_special_move_serial,
    )
    return True
# </POTBO_STAGE S0661>

# <POTBO_STAGE S0671>


def _v34_special_ready_prompt_ciz():
    """Ctrl+U test açıkken charge sırasında yalnız R-release bilgisini gösterir."""
    if not GELISTIRICI_MODU or not gelistirici_x_skill_aktif:
        return
    if gelistirici_x_skill_aktif_mi():
        return
    if karakter_cinsiyet != "male" or oyuncu_saldiri_modu != "charge":
        return
    yon = _adefo_yon_vektoru(adefo_hold_charge_yonu)
    hedef = _gelistirici_x_skill_hedef_sec(yon)
    if hedef is None:
        return
    x = dunya_ekran_x(oyuncu_x)
    y = dunya_ekran_y(oyuncu_y) - 78
    label = bt("R: ÖZEL HAREKET", "R: SPECIAL MOVE")
    surf = mini_font.render(label, True, (242, 236, 240))
    pad_x, pad_y = 10, 5
    rect = surf.get_rect(center=(x, y))
    box = rect.inflate(pad_x * 2, pad_y * 2)
    overlay = pygame.Surface((box.width, box.height), pygame.SRCALPHA)
    overlay.fill((8, 5, 9, 186))
    ekran.blit(overlay, box.topleft)
    pygame.draw.rect(ekran, (118, 18, 38), box, 1)
    ekran.blit(surf, rect)
# </POTBO_STAGE S0671>

# <POTBO_STAGE S0691>


# ---------------------------------------------------------
# INPUT BUFFERING
# ---------------------------------------------------------
_v34a_adefonsus_saldiri_baslat = adefonsus_saldiri_baslat


def adefonsus_saldiri_baslat(simdi=None):
    """Recovery sonuna yakın J basışını kaybetmek yerine kısa buffer'a alır."""
    global v34_attack_buffer_until, v34_input_buffer_attack_count
    if simdi is None:
        simdi = pygame.time.get_ticks()
    simdi = int(simdi)

    if gelistirici_x_skill_aktif_mi(simdi) or oyuncu_hp <= 0:
        return False

    if oyuncu_saldiriyor:
        # Press/charge sırasında yeni buffer üretme; bu hold input'unu double-tap'e
        # çevirebilir. Yalnız committed normal/heavy recovery penceresinde buffer.
        if oyuncu_saldiri_modu in ("normal", "hold_release"):
            v34_attack_buffer_until = max(
                v34_attack_buffer_until,
                simdi + V34_ATTACK_BUFFER_MS,
            )
            v34_input_buffer_attack_count += 1
        return False

    ok = _v34a_adefonsus_saldiri_baslat(simdi)
    if ok:
        v34_attack_buffer_until = 0
    return ok
# </POTBO_STAGE S0691>

# <POTBO_STAGE S0693>


def v34_input_buffer_guncelle():
    """Buffered attack/dash'i yalnız karakter gerçekten tekrar serbest olduğunda tüketir."""
    global v34_attack_buffer_until, v34_dash_buffer_until, v34_dash_buffer_direction
    simdi = pygame.time.get_ticks()
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA or oyuncu_hp <= 0:
        return
    if oyun_sinematik_kilitli_mi() or oyuncu_kontrol_kilitli_mi(simdi):
        return

    if v34_attack_buffer_until and simdi > v34_attack_buffer_until:
        v34_attack_buffer_until = 0
    if v34_dash_buffer_until and simdi > v34_dash_buffer_until:
        v34_dash_buffer_until = 0
        v34_dash_buffer_direction.update(0.0, 0.0)

    # Attack önce gelir; aynı frame'de hem attack hem dash buffer varsa en eski niyet
    # olarak saldırı commitment'ı korunur. Dash bir sonraki frame'e kalabilir.
    if (
        v34_attack_buffer_until > simdi
        and not oyuncu_saldiriyor
        and not oyuncu_savunuyor
    ):
        if _v34a_adefonsus_saldiri_baslat(simdi):
            v34_attack_buffer_until = 0
            return

    if (
        v34_dash_buffer_until > simdi
        and not oyuncu_saldiriyor
        and not oyuncu_savunuyor
        and not oyuncu_dash_aktif_mi(simdi)
        and v34_dash_buffer_direction.length_squared() > 1e-6
    ):
        d = v34_dash_buffer_direction.normalize()
        if _v34a_oyuncu_dash_yap(d.x, d.y):
            v34_dash_buffer_until = 0
            v34_dash_buffer_direction.update(0.0, 0.0)
# </POTBO_STAGE S0693>

# <POTBO_STAGE S0731>


_v34d_adefonsus_footstep_guncelle = adefonsus_footstep_guncelle


def adefonsus_footstep_guncelle():
    simdi = pygame.time.get_ticks()
    if gelistirici_x_skill_aktif_mi(simdi):
        if (
            adefonsus_footstep_kanali is not None
            and adefonsus_footstep_kanali.get_busy()
        ):
            try:
                adefonsus_footstep_kanali.fadeout(35)
            except pygame.error:
                pass
        return
    _v34d_adefonsus_footstep_guncelle()


def _v34_special_target_preview_target():
    global v34_special_target_preview_cache, v34_special_target_preview_cache_ms
    simdi = pygame.time.get_ticks()
    if simdi - v34_special_target_preview_cache_ms < 55:
        target = v34_special_target_preview_cache
        if (
            target is not None
            and getattr(target, "active", False)
            and int(getattr(target, "hp", 0)) > 0
        ):
            return target
    v34_special_target_preview_cache_ms = simdi
    v34_special_target_preview_cache = None
    if not GELISTIRICI_MODU or not gelistirici_x_skill_aktif:
        return None
    if karakter_cinsiyet != "male" or oyuncu_saldiri_modu != "charge":
        return None
    direction = _adefo_yon_vektoru(adefo_hold_charge_yonu)
    target = _gelistirici_x_skill_hedef_sec(direction)
    v34_special_target_preview_cache = target
    return target
# </POTBO_STAGE S0731>

# <POTBO_STAGE S0813>


# =========================================================
# END V34F
# =========================================================


# =========================================================
# V35 COMBAT IDENTITY / CONTACT INTEGRITY / KINETIC POLISH
# =========================================================
# V35'in amacı hasarı görünmez dikdörtgenlerle büyütmek değil, ekranda görülen beden
# hareketi ile mekanik sonucu aynı hizaya getirmektir. Normal melee daha dürüst yakın
# temas ister; dash ve Adefonsus hold-release ise menzili gerçek world hareketinden
# kazanır. Special move üç fiziksel hit kontratını korur fakat daha kısa, daha sert ve
# daha okunaklı bir ritme çekilir. Yeni "Kesik İvmesi" katmanı başarılı yakın dövüş
# temaslarını hareket akışına bağlar; doğrudan hasar çarpanı vermez, bu yüzden temel
# dengeyi sessizce bozmaz.

V35_VERSION = 35
# </POTBO_STAGE S0813>

# <POTBO_STAGE S0815>

# Heavy hold-release artık görünmez uzun hitbox yerine karakterin bedenini daha uzağa
# taşır. Böylece menzil artışı görsel ve fiziksel olarak aynı şeydir.
ADEFO_HOLD_DASH_MESAFESI = 206.0
ADEFO_HOLD_DASH_SURE_MS = 214
# </POTBO_STAGE S0815>

# <POTBO_STAGE S0824>


def oyuncu_saldiri_vurus_rect():
    """V35: normal melee yakın, heavy ise fiziksel lunge ile menzil kazanır.

    Bu rect yalnız broad-phase'tir. Normal saldırıda eski 62/48 kutusu birkaç sprite
    genişliğinde uzaktan temas hissi üretebiliyordu. Heavy release'ın gerçek menzili
    ADEFO_HOLD_DASH_MESAFESI ile geldiği için onun rect'ini de gereksiz büyütmüyoruz.
    """
    if (
        karakter_cinsiyet == "male"
        and ADEFONSUS_YENI_SHEET_AKTIF
        and oyuncu_saldiri_modu in ("press", "charge")
    ):
        return pygame.Rect(int(round(oyuncu_x)), int(round(oyuncu_y)), 1, 1)

    cx = int(round(oyuncu_x))
    cy = int(round(oyuncu_y - 18))
    heavy = karakter_cinsiyet == "male" and oyuncu_saldiri_modu == "hold_release"
    ileri = V35_PLAYER_HEAVY_REACH if heavy else V35_PLAYER_NORMAL_REACH
    yan = V35_PLAYER_HEAVY_WIDTH if heavy else V35_PLAYER_NORMAL_WIDTH
    geri = 3

    if oyuncu_yonu == "left":
        return pygame.Rect(cx - ileri, cy - yan // 2, ileri + geri, yan)
    if oyuncu_yonu == "right":
        return pygame.Rect(cx - geri, cy - yan // 2, ileri + geri, yan)
    if oyuncu_yonu == "up":
        return pygame.Rect(cx - yan // 2, cy - ileri, yan, ileri + geri)
    return pygame.Rect(cx - yan // 2, cy - geri, yan, ileri + geri)
# </POTBO_STAGE S0824>

# <POTBO_STAGE S0830>


_v35_hold_release_original = _adefo_hold_release_baslat


def _adefo_hold_release_baslat(simdi):
    global adefo_hold_dash_yonu, oyuncu_yonu, v35_hold_dash_distance_scale
    _v35_hold_release_original(simdi)
    if oyuncu_saldiri_modu != "hold_release":
        return
    corrected = _v35_heavy_assist_direction(adefo_hold_dash_yonu)
    adefo_hold_dash_yonu = corrected
    if abs(corrected.x) >= abs(corrected.y):
        oyuncu_yonu = "right" if corrected.x >= 0 else "left"
    else:
        oyuncu_yonu = "down" if corrected.y >= 0 else "up"
    # Flow heavy menzilini çok küçük oranda destekler; asıl menzil artışı taban
    # sabitindedir. Bu bonus hasarı değil hareket zincirini ödüllendirir.
    v35_hold_dash_distance_scale = 1.0 + min(0.09, v35_combat_flow * 0.03)


# Hold movement'ın orijinal state-machine'ini koruyup yalnız frame'de uygulanacak
# toplam mesafeyi flow ölçeğiyle çarpmak için V35 sürümü.
def adefonsus_hold_dash_guncelle(simdi=None):
    global oyuncu_x, oyuncu_y
    global adefo_hold_dash_son_guncelleme, adefo_hold_dash_son_ease
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if (
        not oyuncu_saldiriyor
        or oyuncu_saldiri_modu != "hold_release"
        or adefo_hold_dash_baslangic_ms <= 0
        or int(simdi) >= adefo_hold_dash_bitis
    ):
        return False

    duration = max(1.0, float(ADEFO_HOLD_DASH_SURE_MS))
    p = max(
        0.0,
        min(
            1.0,
            (int(simdi) - adefo_hold_dash_baslangic_ms) / duration,
        ),
    )
    # Daha keskin quintic ease-out: heavy ilk 1/3'te gerçek bir lunge gibi kopar.
    ease = 1.0 - (1.0 - p) ** 5
    delta_ease = max(0.0, ease - float(adefo_hold_dash_son_ease))
    adefo_hold_dash_son_ease = ease
    adefo_hold_dash_son_guncelleme = int(simdi)
    distance = (
        ADEFO_HOLD_DASH_MESAFESI * float(v35_hold_dash_distance_scale) * delta_ease
    )
    if distance <= 0.0001 or adefo_hold_dash_yonu.length_squared() <= 1e-6:
        return False

    remaining = distance
    moved = False
    direction = adefo_hold_dash_yonu.normalize()
    while remaining > 0.0001:
        step = min(ADEFO_HOLD_DASH_ADIMI, remaining)
        nx = max(
            35.0,
            min(
                HARITA_GENISLIK - 35.0,
                oyuncu_x + direction.x * step,
            ),
        )
        ny = max(
            35.0,
            min(
                HARITA_YUKSEKLIK - 25.0,
                oyuncu_y + direction.y * step,
            ),
        )
        progressed = False
        if hareket_gecerli_mi(nx, oyuncu_y):
            oyuncu_x = nx
            progressed = True
        if hareket_gecerli_mi(oyuncu_x, ny):
            oyuncu_y = ny
            progressed = True
        if not progressed:
            adefo_hold_dash_son_ease = 1.0
            break
        moved = True
        remaining -= step
    return moved
# </POTBO_STAGE S0830>

# <POTBO_STAGE S0843>


def kamerayi_guncelle():
    global kamera_x, kamera_y, v35_camera_lead
    _v35_camera_original()
    simdi = pygame.time.get_ticks()
    target = pygame.Vector2(0.0, 0.0)
    if gelistirici_x_skill_aktif_mi(simdi):
        d = _v35_special_motion_direction(simdi)
        if d.length_squared() > 1e-6:
            target = d.normalize() * V35_CAMERA_SPECIAL_LEAD
    elif (
        oyuncu_saldiriyor
        and oyuncu_saldiri_modu == "hold_release"
        and adefo_hold_dash_yonu.length_squared() > 1e-6
    ):
        target = adefo_hold_dash_yonu.normalize() * V35_CAMERA_HEAVY_LEAD
    elif oyuncu_dash_aktif_mi(simdi) and dash_aktif_yonu.length_squared() > 1e-6:
        target = dash_aktif_yonu.normalize() * V35_CAMERA_DASH_LEAD

    # Exponential-like smoothing; bir frame'de snap üretmez.
    v35_camera_lead += (target - v35_camera_lead) * 0.22
    kamera_x += v35_camera_lead.x
    kamera_y += v35_camera_lead.y
    visible_w = GENISLIK / KAMERA_YAKINLASTIRMA
    visible_h = YUKSEKLIK / KAMERA_YAKINLASTIRMA
    kamera_x = max(
        0.0,
        min(max(0.0, HARITA_GENISLIK - visible_w), kamera_x),
    )
    kamera_y = max(
        0.0,
        min(max(0.0, HARITA_YUKSEKLIK - visible_h), kamera_y),
    )
# </POTBO_STAGE S0843>

# <POTBO_STAGE S0850>


def v35_diagnostics():
    """Geliştirici konsolundan çağrılabilir; normal oyuncuya UI spam üretmez."""
    base = v34f_diagnostics()
    base["v35"] = {
        "version": V35_VERSION,
        "dash_distance": float(DASH_MESAFESI),
        "hold_distance": float(ADEFO_HOLD_DASH_MESAFESI),
        "special_ms": int(GELISTIRICI_X_SKILL_SURE_MS),
        "special_radius": float(GELISTIRICI_X_SKILL_YARI_CAP),
        "flow": round(float(v35_combat_flow), 3),
        "flow_best": round(float(v35_flow_best), 3),
        "melee_hits": int(v35_flow_hits),
        "player_normal_reach": int(V35_PLAYER_NORMAL_REACH),
        "player_heavy_reach": int(V35_PLAYER_HEAVY_REACH),
    }
    return base
# </POTBO_STAGE S0850>

# <POTBO_STAGE S0852>
V35_STARTUP_OK = (
    GELISTIRICI_X_SKILL_SURE_MS >= 900
    and V35_PLAYER_NORMAL_REACH < V35_PLAYER_HEAVY_REACH
    and ADEFO_HOLD_DASH_MESAFESI > DASH_MESAFESI
    and len(GELISTIRICI_X_SKILL_HASAR_CARPANLARI) == 3
    and bool(V35_SPECIAL_PHASE_OK)
)
# </POTBO_STAGE S0852>

# <POTBO_STAGE S0983>


def oyuncu_saldiri_vurus_rect():
    """V38 broad-phase: kısa ve yönsel.

    Heavy menzil ADEFO_HOLD_DASH_MESAFESI ile beden hareketinden gelir; bu rect yalnız
    o an karakterin önündeki gerçek blade/body temasını kabul eder.
    """
    if (
        karakter_cinsiyet == "male"
        and ADEFONSUS_YENI_SHEET_AKTIF
        and oyuncu_saldiri_modu in ("press", "charge")
    ):
        return pygame.Rect(int(round(oyuncu_x)), int(round(oyuncu_y)), 1, 1)
    nr, nw, hr, hw = _v38_player_reach_values()
    heavy = karakter_cinsiyet == "male" and oyuncu_saldiri_modu == "hold_release"
    reach = hr if heavy else nr
    width = hw if heavy else nw
    cx = int(round(oyuncu_x))
    cy = int(round(oyuncu_y - 18))
    back = 2
    if oyuncu_yonu == "left":
        return pygame.Rect(cx - reach, cy - width // 2, reach + back, width)
    if oyuncu_yonu == "right":
        return pygame.Rect(cx - back, cy - width // 2, reach + back, width)
    if oyuncu_yonu == "up":
        return pygame.Rect(cx - width // 2, cy - reach, width, reach + back)
    return pygame.Rect(cx - width // 2, cy - back, width, reach + back)
# </POTBO_STAGE S0983>

# <POTBO_STAGE S0989>
V38_SPECIAL_PREP_REFUND = float(SALDIRI_STAMINA_MALIYETI + ADEFO_HOLD_EK_STAMINA)
# </POTBO_STAGE S0989>

# <POTBO_STAGE S1044>

# Normal saldırılar ve hold-release daha seri; temas kutuları ise biraz daha kısa.
ADEFO_NORMAL_SURE_MS = 315
# </POTBO_STAGE S1044>

# <POTBO_STAGE S1046>
ADEFO_HOLD_FLASH_MS = 128
ADEFO_HOLD_DASH_SURE_MS = 178
ADEFO_HOLD_DASH_ADIMI = 6.0
# </POTBO_STAGE S1046>

# <POTBO_STAGE S1059>


def oyuncu_saldiri_hasar_miktari():
    carpan = 1.0
    if karakter_cinsiyet == "male" and oyuncu_saldiri_modu == "hold_release":
        carpan = ADEFO_HOLD_HASAR_CARPANI
    elif karakter_cinsiyet == "male":
        carpan = ADEFO_NORMAL_HASAR_CARPANI

    sig = v39_character_signature()
    stamina_ratio = v39_clamp01(oyuncu_stamina / max(1.0, float(oyuncu_max_stamina)))
    hp_ratio = v39_clamp01(oyuncu_hp / max(1.0, float(oyuncu_max_hp)))
    wound = 1.0 - hp_ratio
    scalar = 1.0 + sig["power"] * 0.018
    if karakter_cinsiyet == "male":
        scalar += min(0.14, wound * 0.18)
        scalar += 0.03 * (1.0 - stamina_ratio)
        if oyuncu_saldiri_modu == "hold_release":
            scalar += sig["poise"] * 0.006
    else:
        scalar += 0.05 * stamina_ratio + sig["edge"] * 0.010
        if oyuncu_saldiri_modu == "normal":
            scalar += 0.035
    return max(1, int(round(float(oyuncu_hasari) * carpan * scalar)))
# </POTBO_STAGE S1059>

# <POTBO_STAGE S1068>


def adefonsus_hold_dash_guncelle(simdi=None):
    """Daha akıcı, daha kısa ve daha ucuz hold-release dash."""
    global oyuncu_x, oyuncu_y
    global adefo_hold_dash_son_guncelleme, adefo_hold_dash_son_ease

    if simdi is None:
        simdi = pygame.time.get_ticks()
    if (
        not oyuncu_saldiriyor
        or oyuncu_saldiri_modu != "hold_release"
        or adefo_hold_dash_baslangic_ms <= 0
        or int(simdi) >= adefo_hold_dash_bitis
    ):
        return False

    sure = max(1.0, float(ADEFO_HOLD_DASH_SURE_MS))
    p = max(
        0.0,
        min(
            1.0,
            (int(simdi) - adefo_hold_dash_baslangic_ms) / sure,
        ),
    )
    ease = p * p * (3.0 - 2.0 * p)
    delta_ease = max(0.0, ease - float(adefo_hold_dash_son_ease))
    adefo_hold_dash_son_ease = ease
    adefo_hold_dash_son_guncelleme = int(simdi)
    mesafe = ADEFO_HOLD_DASH_MESAFESI * delta_ease
    if mesafe <= 0.0001 or adefo_hold_dash_yonu.length_squared() <= 1e-6:
        return False

    kalan = mesafe
    hareket_oldu = False
    yon = adefo_hold_dash_yonu.normalize()
    while kalan > 0.0001:
        adim = min(ADEFO_HOLD_DASH_ADIMI, kalan)
        yeni_x = max(
            35.0,
            min(HARITA_GENISLIK - 35.0, oyuncu_x + yon.x * adim),
        )
        yeni_y = max(
            35.0,
            min(HARITA_YUKSEKLIK - 25.0, oyuncu_y + yon.y * adim),
        )
        if not hareket_gecerli_mi(yeni_x, yeni_y):
            adefo_hold_dash_son_ease = 1.0
            break
        oyuncu_x, oyuncu_y = yeni_x, yeni_y
        kalan -= adim
        hareket_oldu = True
    return hareket_oldu
# </POTBO_STAGE S1068>

# <POTBO_STAGE S1091>

# Tek bir kontrol dili:
# - ENTER / SPACE = yalnız gerçek UI onayı.
# - E = dünya etkileşimi + diyalog ilerletme/cevap seçimi.
# - 1..5 = öne çıkan slot seçimi.
# - F = seçili öne çıkan slotu kullan / envanterde featured bağlamı.
# - Q = bağımsız quick slot; büyüler de burada.
# - TAB = envanter.
# - J = saldırı; Adefonsus'ta hold aynı tuşun ağır saldırı niyetidir.
# - SHIFT = dash, K = block, ESC = pause/back.
# Special move normal kontrol şemasının parçası değildir; Ctrl+U açık geliştirici
# testinde hold-J -> R bas/bırak kombinasyonu olarak izole kalır.
V41_CONTROL_DOCTRINE = {
    "ui_confirm": ("ENTER", "SPACE"),
    "world_interact": "E",
    "featured_select": "1-5",
    "featured_use": "F",
    "quick_slot": "Q",
    "inventory": "TAB",
    "attack": "J",
    "block": "K",
    "dash": "L SHIFT",
    "pause": "ESC",
    "special_test": "CTRL+U unlock; hold J, press/release R",
}
# </POTBO_STAGE S1091>

# <POTBO_STAGE S1094>


def ayar_aciklamasi(ayar):
    if ayar == "bind_interact":
        return bt(
            "Yalnız dünya etkileşimi: konuş, al, aç ve diyalogda devam et. Menülerde onay değildir.",
            "World interaction only: talk, pick up, open and continue dialogue. It does not confirm menus.",
        )
    if ayar == "bind_quick_use":
        return bt(
            "1-5 ile seçilen öne çıkan slotu kullanır. F bu sistemin tek kullanım tuşudur.",
            "Uses the featured slot selected with 1-5. F is the single use key for this system.",
        )
    if ayar == "bind_q_quick_use":
        return bt(
            "Bağımsız hızlı slotu kullanır. İksir veya büyü atanabilir; büyüler yalnız bu slot üzerinden çalışır.",
            "Uses the independent quick slot. It can hold an item or spell; spells cast only from this slot.",
        )
    if ayar == "bind_attack":
        return bt(
            "J kısa basış temel saldırı; Adefonsus'ta basılı tutmak ağır saldırıyı hazırlar.",
            "Tap J for a basic attack; with Adefonsus, holding it prepares the heavy attack.",
        )
    if ayar == "bind_dash":
        return bt(
            "Hareket yönünde kısa, fiziksel dash. Special move'un tetikleyicisi değildir.",
            "A short physical dash in the movement direction. It does not trigger the special move.",
        )
    return _v41_ayar_aciklamasi_original(ayar)
# </POTBO_STAGE S1094>

# <POTBO_STAGE S1140>


def v44_attack_speed_estimate(mode=None):
    """Kılıcın görünür yay hızını yaklaşık px/s olarak tahmin eder.

    Bu fizik motoru blade tip velocity çözmüyor; animasyon süresi, attack modu ve
    special timeline bilindiği için kan morfolojisi için yeterli bir kinematik proxy
    üretiyoruz. Hız yalnız kan şekli/temas karakteri içindir, doğrudan hasar değildir.
    """
    if mode is None:
        mode = str(oyuncu_saldiri_modu or "normal")
    mode = str(mode)
    if gelistirici_x_skill_aktif_mi():
        return 920.0
    if mode == "hold_release":
        held = max(
            0,
            int(v44_last_player_swing_release_ms) - int(v44_last_player_swing_start_ms),
        )
        charge = v44_clamp01((held - 180.0) / 850.0)
        return 650.0 + 210.0 * charge
    if mode in ("press", "charge"):
        return 260.0
    # Preciosa ve klasik normal saldırı daha seri; Adefonsus normal biraz ağır.
    if karakter_cinsiyet == "female":
        return 590.0
    return 500.0
# </POTBO_STAGE S1140>

# <POTBO_STAGE S1153>


# Saldırı start/release zamanları kan morfolojisinin gerçek input temposunu görür.
_v44_adefo_attack_start_original = adefonsus_saldiri_baslat


def adefonsus_saldiri_baslat(simdi=None):
    global v44_last_player_swing_start_ms, v44_last_player_attack_mode
    if simdi is None:
        simdi = pygame.time.get_ticks()
    ok = _v44_adefo_attack_start_original(simdi)
    if ok:
        v44_last_player_swing_start_ms = int(simdi)
        v44_last_player_attack_mode = str(oyuncu_saldiri_modu)
    return ok


_v44_adefo_attack_release_original = adefonsus_saldiri_tusu_birakildi


def adefonsus_saldiri_tusu_birakildi(simdi=None):
    global v44_last_player_swing_release_ms, v44_last_player_attack_mode
    if simdi is None:
        simdi = pygame.time.get_ticks()
    v44_last_player_swing_release_ms = int(simdi)
    ok = _v44_adefo_attack_release_original(simdi)
    v44_last_player_attack_mode = str(oyuncu_saldiri_modu)
    return ok
# </POTBO_STAGE S1153>

# <POTBO_STAGE S1583>

ADEFO_NORMAL_SURE_MS = 286
# </POTBO_STAGE S1583>

# <POTBO_STAGE S1585>
ADEFO_HOLD_DASH_SURE_MS = 154
ADEFO_HOLD_DASH_ADIMI = 4.25
# </POTBO_STAGE S1585>

# <POTBO_STAGE S1611>


def _v80_player_basis():
    f = _adefo_yon_vektoru(oyuncu_yonu)
    if f.length_squared() <= 1e-6:
        f = pygame.Vector2(1.0, 0.0)
    f = f.normalize()
    side = pygame.Vector2(f.y, -f.x)
    return f, side
# </POTBO_STAGE S1611>

# <POTBO_STAGE S1620>


def _v81_impact_direction():
    killer = _v24_olum_katil_actor_bul()
    if killer is not None:
        d = pygame.Vector2(
            float(oyuncu_x) - float(getattr(killer, "x", oyuncu_x)),
            float(oyuncu_y) - float(getattr(killer, "y", oyuncu_y)),
        )
        if d.length_squared() > 1e-6:
            return d.normalize()
    d = _adefo_yon_vektoru(oyuncu_yonu)
    if d.length_squared() <= 1e-6:
        d = pygame.Vector2(1.0, 0.0)
    return d.normalize()


def _v81_body_basis():
    forward = _adefo_yon_vektoru(oyuncu_yonu)
    if forward.length_squared() <= 1e-6:
        forward = pygame.Vector2(1.0, 0.0)
    forward = forward.normalize()
    side = pygame.Vector2(forward.y, -forward.x)
    return forward, side
# </POTBO_STAGE S1620>

# <POTBO_STAGE S1656>

# Combat pace: animation daha hızlı, fakat cooldown animasyondan uzun kalır.
# Böylece input daha çevik hissedilirken J spam ritmi oyunu makine tüfeğine çevirmez.
ADEFO_NORMAL_SURE_MS = 252
# </POTBO_STAGE S1656>

# <POTBO_STAGE S1675>


def _v82_spawn_hit_fx(enemy, kind, depth, damage):
    now = pygame.time.get_ticks()
    d = pygame.Vector2(
        float(getattr(enemy, "x", oyuncu_x)) - float(oyuncu_x),
        float(getattr(enemy, "y", oyuncu_y)) - float(oyuncu_y),
    )
    if d.length_squared() <= 1e-7:
        d = _adefo_yon_vektoru(oyuncu_yonu)
    if d.length_squared() <= 1e-7:
        d = pygame.Vector2(1.0, 0.0)
    d = d.normalize()
    life = {
        "glance": 88,
        "clean": 112,
        "deep": 132,
        "armor": 128,
        "heavy": 146,
        "lethal": 176,
    }.get(kind, 110)
    v82_hit_fx.append(
        {
            "x": float(getattr(enemy, "x", oyuncu_x)),
            "y": float(getattr(enemy, "y", oyuncu_y)) - 14.0,
            "start": now,
            "life": life,
            "kind": str(kind),
            "depth": float(depth),
            "damage": max(1, int(damage)),
            "angle": math.degrees(math.atan2(d.y, d.x)),
            "seed": (
                now * 17
                + sum(
                    ord(c)
                    for c in str(
                        getattr(
                            enemy,
                            "uid",
                            getattr(enemy, "tur", "enemy"),
                        )
                    )
                )
            )
            & 0x7FFFFFFF,
        }
    )
    if len(v82_hit_fx) > V82_HIT_FX_MAX:
        del v82_hit_fx[:-V82_HIT_FX_MAX]
# </POTBO_STAGE S1675>

# <POTBO_STAGE S1681>


def v82_diagnostics():
    return {
        "version": V82_VERSION,
        "attack_ms": int(ADEFO_NORMAL_SURE_MS),
        "attack_cooldown_ms": int(saldiri_bekleme_suresi),
        "stamina_cost": int(SALDIRI_STAMINA_MALIYETI),
        "stamina_regen": float(STAMINA_YENILENME_HIZI),
        "stamina_bar_px": int(V82_STAMINA_H),
        "fluid_death_uses_v81_droplets": True,
        "active_hit_fx": len(v82_hit_fx),
        "hud_last_pass": True,
    }
# </POTBO_STAGE S1681>

# <POTBO_STAGE S1684>

# Oynanış biraz daha çevik: daha hızlı temas, daha hafif stamina yükü,
# fakat halen kontrolsüz spam ritmine düşmez.
ADEFO_NORMAL_SURE_MS = 236
# </POTBO_STAGE S1684>

# <POTBO_STAGE S1700>


def _v83_death_continuous_artery():
    if str(oyuncu_olum_turu) != "blood":
        return
    age = max(
        0,
        pygame.time.get_ticks() - int(oyuncu_olum_baslangic_ms or 0),
    )
    if age > 2200:
        return
    strength = max(0.18, 1.0 - age / 2200.0)
    origin = pygame.Vector2(float(oyuncu_x), float(oyuncu_y) - 11.0)
    base = _adefo_yon_vektoru(oyuncu_yonu)
    if base.length_squared() <= 1e-6:
        base = pygame.Vector2(1.0, 0.0)
    base = base.normalize()
    branches = [(-16.0, 1.00), (9.0, 0.88), (33.0, 0.64)]
    now = pygame.time.get_ticks()
    for idx, (ang, mul) in enumerate(branches):
        pulse = 0.72 + 0.28 * math.sin((now / 90.0) + idx * 1.37)
        length = (18.0 + 28.0 * strength * mul) * pulse
        d = base.rotate(ang)
        prev = origin
        for step in range(1, 6):
            s = step / 5.0
            pos = (
                origin
                + d * (length * s)
                + pygame.Vector2(0.0, 10.0 + 8.0 * s * strength)
            )
            _v80_draw_world_line(
                prev,
                pos,
                V77_DEATH_BLOOD,
                2 if step <= 2 and strength > 0.45 else 1,
            )
            if step >= 3:
                _v80_draw_world_circle(pos, 1 if step < 5 else 2, V77_DEATH_BLOOD)
            prev = pos
# </POTBO_STAGE S1700>

# <POTBO_STAGE S1733>


def v84_player_silhouette():
    animation = "attack"
    if karakter_cinsiyet == "male" and ADEFONSUS_YENI_SHEET_AKTIF:
        animation = "hold_release"
    frames = aktif_animasyon_kareleri(animation)
    if not frames:
        base = _v30_oyuncu_base_siluet()
        return base
    beat = max(0, int(v84_execution_state.next_beat_index))
    frame = frames[min(len(frames) - 1, beat % len(frames))]
    base_height = 73 if karakter_cinsiyet == "male" else 68
    height = max(1, int(round(base_height * KAMERA_YAKINLASTIRMA)))
    scale = height / max(1.0, float(frame.get_height()))
    image = pygame.transform.scale(
        frame,
        (
            max(1, int(round(frame.get_width() * scale))),
            height,
        ),
    )
    if karakter_cinsiyet == "male" and ADEFONSUS_YENI_SHEET_AKTIF:
        if adefonsus_render_flip_gerekli_mi(oyuncu_yonu):
            image = pygame.transform.flip(image, True, False)
    mask = pygame.mask.from_surface(image, 1)
    return mask.to_surface(
        setcolor=(*V84_BODY, 255),
        unsetcolor=(0, 0, 0, 0),
    ).convert_alpha()
# </POTBO_STAGE S1733>

# <POTBO_STAGE S1746>


def v84_source_in_front(source_x, source_y):
    source = pygame.Vector2(
        float(source_x) - float(oyuncu_x),
        float(source_y) - float(oyuncu_y),
    )
    if source.length_squared() <= 1e-8:
        return True
    facing = v84_safe_vector(_adefo_yon_vektoru(oyuncu_yonu)).normalize()
    return facing.dot(source.normalize()) >= v84_perfect_guard_front_dot()
# </POTBO_STAGE S1746>

# <POTBO_STAGE S1756>


def v84_perfect_guard_feedback(
    actor,
    source_x,
    source_y,
    class_name,
    quality,
    now,
):
    global v84_guard_flash_until
    global v84_guard_flash_started_ms
    global v84_guard_label_until
    incoming = pygame.Vector2(
        float(oyuncu_x) - float(source_x),
        float(oyuncu_y) - float(source_y),
    )
    incoming = v84_safe_vector(
        incoming,
        _adefo_yon_vektoru(oyuncu_yonu),
    ).normalize()
    power = 1.55 + float(quality) * (0.72 if class_name == "heavy" else 0.52)
    combat_impact_spawn(
        oyuncu_x,
        oyuncu_y - 13.0,
        "slash_heavy" if class_name == "heavy" else "slash",
        power,
        incoming,
    )
    for angle in (-13.0, 13.0):
        combat_impact_spawn(
            oyuncu_x,
            oyuncu_y - 13.0,
            "slash",
            power * 0.58,
            incoming.rotate(angle),
        )
    kamera_hit_sarsintisi_baslat(
        4.4 + 2.0 * float(quality),
        112 + int(42 * float(quality)),
    )
    v84_guard_flash_started_ms = int(now)
    v84_guard_flash_until = int(now) + 126
    v84_guard_label_until = int(now) + 620
    setattr(actor, "hit_flash_until", int(now) + 170)
# </POTBO_STAGE S1756>

# <POTBO_STAGE S1760>


def v84_riposte_commit(now=None):
    global oyuncu_saldiriyor
    global oyuncu_savunuyor
    global oyuncu_saldiri_modu
    global oyuncu_saldiri_sure_ms
    global oyuncu_stamina
    global stamina_son_harcama
    global saldiri_baslangic
    global son_saldiri_zamani
    global animasyon_index
    global ADEFO_HOLD_GECIS_YAPILDI
    global v84_riposte_total
    if now is None:
        now = pygame.time.get_ticks()
    if not v84_riposte_active(now):
        return False
    if oyuncu_saldiriyor or v84_execution_state.active:
        return False
    cost = max(
        1.0,
        float(SALDIRI_STAMINA_MALIYETI) * V84_RIPOSTE_STAMINA_SCALE,
    )
    if float(oyuncu_stamina) < cost:
        hud_uyari_baslat("stamina")
        return True
    oyuncu_stamina = max(0.0, float(oyuncu_stamina) - cost)
    stamina_son_harcama = int(now)
    oyuncu_savunuyor = False
    oyuncu_saldiriyor = True
    oyuncu_saldiri_modu = "normal"
    oyuncu_saldiri_sure_ms = V84_RIPOSTE_ATTACK_MS
    ADEFO_HOLD_GECIS_YAPILDI = True
    saldiri_baslangic = int(now)
    son_saldiri_zamani = int(now)
    animasyon_index = 0
    v84_face_actor(v84_riposte_state.target)
    v84_riposte_state.committed = True
    v84_riposte_state.attack_id = int(saldiri_baslangic)
    v84_riposte_total += 1
    dunya_olayi_kaydet(
        "riposte_commit",
        enemy=str(getattr(v84_riposte_state.target, "tur", "enemy")),
        armor=v84_riposte_state.armor_breach,
    )
    return True
# </POTBO_STAGE S1760>

# <POTBO_STAGE S1764>


def v84_execution_target_select(override=True):
    facing = v84_safe_vector(_adefo_yon_vektoru(oyuncu_yonu)).normalize()
    maximum = V84_EXECUTION_OVERRIDE_RANGE if override else V84_EXECUTION_NATURAL_RANGE
    candidates = [
        actor
        for actor in v84_hostile_actors(include_suspended=False)
        if v84_actor_distance(actor) <= maximum
        and (override or v84_execution_naturally_eligible(actor))
    ]
    if not candidates:
        return None
    return min(
        candidates,
        key=lambda actor: v84_execution_target_score(
            actor,
            facing,
            override,
        ),
    )
# </POTBO_STAGE S1764>

# <POTBO_STAGE S1801>


def v84_death_prepare(
    source_x,
    source_y,
    profile,
    source_name="",
):
    state = v84_death_state
    if state.built:
        return
    now = pygame.time.get_ticks()
    state.built = True
    state.seed = (
        int(oyuncu_olum_koreografi_seed or 0)
        ^ int(oyuncu_olum_patlama_seed or 0)
        ^ int(now)
        ^ int(abs(float(source_x) * 79.0))
        ^ int(abs(float(source_y) * 131.0))
    ) & 0x7FFFFFFF
    state.profile = str(profile or "slash")
    state.source = str(source_name or "")
    state.source_position = pygame.Vector2(
        float(source_x),
        float(source_y),
    )
    state.created_ms = int(now)
    state.last_tick_ms = int(now)
    state.cut_count = v84_death_cut_count(
        state.profile,
        oyuncu_olum_turu,
    )
    away = pygame.Vector2(
        float(oyuncu_x) - float(source_x),
        float(oyuncu_y) - float(source_y),
    )
    state.direction = v84_safe_vector(
        away,
        _adefo_yon_vektoru(oyuncu_yonu),
    ).normalize()
    if str(oyuncu_olum_turu) == "fire":
        return
    surface = _v30_oyuncu_base_siluet()
    state.fracture = V84FractureField(
        surface,
        max_fragments=32,
    )
    rng = random.Random(state.seed)
    angle_families = (
        (-28.0, 34.0, -51.0, 12.0, 61.0, -8.0, 43.0, -66.0),
        (32.0, -23.0, 55.0, -47.0, 8.0, 68.0, -12.0, 41.0),
        (-16.0, 49.0, -42.0, 25.0, -62.0, 7.0, 57.0, -31.0),
    )
    family = angle_families[state.seed % len(angle_families)]
    for index in range(state.cut_count):
        angle = family[index % len(family)] + rng.uniform(-7.0, 7.0)
        offset = rng.uniform(-0.24, 0.24)
        if index < 2:
            offset *= 0.45
        state.fracture.cut(
            angle,
            offset_ratio=offset,
            gap_px=0.9 + index * 0.14,
        )
    power = 1.34 if str(oyuncu_olum_turu) == "blast_core" else 1.05
    if state.profile == "heavy_slash":
        power = max(power, 1.18)
    state.fracture.release(
        impulse=state.direction,
        power=power,
        seed=state.seed,
    )
# </POTBO_STAGE S1801>

# <POTBO_STAGE S1829>


def v84_execution_choreography(target, seed):
    rng = random.Random(int(seed) ^ 0x85EC7)
    center = pygame.Vector2(float(target.x), float(target.y))
    start = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    approach = center - start
    if approach.length_squared() <= 1e-8:
        approach = _adefo_yon_vektoru(oyuncu_yonu)
    approach = v84_safe_vector(approach).normalize()
    side = approach.rotate(90.0)

    # Dash 1 crosses on a straight line.  Dash 2 is diagonal; Dash 3 is the
    # mirrored diagonal.  Endpoints sit beyond the target, not in front of it.
    dash1 = center + approach * 76.0
    dash2 = center - approach * 61.0 + side * 67.0
    dash3 = center + approach * 57.0 - side * 71.0
    points = [
        start,
        v85_execution_safe_point(dash1, center),
        v85_execution_safe_point(dash2, center),
        v85_execution_safe_point(dash3, center),
    ]

    radial = points[-1] - center
    radial = v84_safe_vector(radial, side).normalize()
    for index in range(10):
        turn = 180.0 + V85_EXECUTION_BURST_ANGLES[index] * 0.34
        turn += rng.uniform(-5.0, 5.0)
        radial = radial.rotate(turn).normalize()
        radius = rng.uniform(70.0, 91.0)
        points.append(v85_execution_safe_point(center + radial * radius, center))

    target_facing = _common_enemy_yon_vektoru(str(getattr(target, "direction", "left")))
    target_facing = v84_safe_vector(target_facing, approach).normalize()
    behind = v85_execution_safe_point(center - target_facing * 62.0, center)
    retreat = v85_execution_safe_point(center - target_facing * 154.0, center)
    final_exit = v85_execution_safe_point(center + target_facing * 102.0, center)
    points.extend((behind, retreat, final_exit))
    return points
# </POTBO_STAGE S1829>

# <POTBO_STAGE S1851>


def v85_mortal_final_hit(now):
    global oyuncu_hp, hp_gorunen, v85_forcing_final_hit
    state = v85_mortal_wound_state
    if not state.active or state.finalized:
        return False
    state.finalized = True
    direction = pygame.Vector2(
        float(oyuncu_x) - state.source_x,
        float(oyuncu_y) - state.source_y,
    )
    direction = v84_safe_vector(direction, _adefo_yon_vektoru(oyuncu_yonu)).normalize()
    oyuncu_hp = 0
    hp_gorunen = 0.0
    v85_forcing_final_hit = True
    try:
        _v85_player_damage_original(
            state.source_x,
            state.source_y,
            state.profile,
            state.damage,
            state.source_name,
        )
    finally:
        v85_forcing_final_hit = False
        oyuncu_hp = 0

    kan_parcacigi_patlat(
        float(oyuncu_x),
        float(oyuncu_y) - (22.0 if state.artery_zone == "neck" else 12.0),
        random.randint(34, 52),
        random.uniform(1.34, 1.72),
        yon=direction,
        arterial=True,
    )
    if "v73_ground_splatter" in globals():
        v73_ground_splatter(
            float(oyuncu_x),
            float(oyuncu_y) + 1.0,
            direction,
            random.randint(18, 28),
            scale_range=(0.18, 0.56),
            distance_range=(3.0, 42.0),
            cone_deg=126.0,
            backscatter=0.30,
            source="mortal_followthrough",
        )
    combat_impact_spawn(
        float(oyuncu_x),
        float(oyuncu_y) - 13.0,
        "slash_heavy",
        2.35,
        direction,
    )
    kamera_hit_sarsintisi_baslat(13.5, 310)
    dunya_olayi_kaydet(
        "mortal_followthrough_hit",
        enemy=str(getattr(state.killer, "tur", "enemy")),
        profile=state.profile,
    )
    state.active = False
    return True
# </POTBO_STAGE S1851>

# <POTBO_STAGE S1861>


def v84_death_prepare(source_x, source_y, profile, source_name=""):
    state = v84_death_state
    if state.built:
        return
    now = pygame.time.get_ticks()
    state.reset()
    state.built = True
    state.seed = (
        int(oyuncu_olum_koreografi_seed or 0)
        ^ int(oyuncu_olum_patlama_seed or 0)
        ^ int(now)
        ^ int(abs(float(source_x) * 79.0))
        ^ int(abs(float(source_y) * 131.0))
    ) & 0x7FFFFFFF
    state.profile = str(profile or "slash")
    state.source = str(source_name or "")
    state.source_position = pygame.Vector2(float(source_x), float(source_y))
    state.created_ms = int(now)
    state.last_tick_ms = int(now)
    state.direction = v84_safe_vector(
        pygame.Vector2(
            float(oyuncu_x) - float(source_x),
            float(oyuncu_y) - float(source_y),
        ),
        _adefo_yon_vektoru(oyuncu_yonu),
    ).normalize()
    state.rotation_sign = -1.0 if state.direction.x >= 0.0 else 1.0
    state.artery_zone = v85_mortal_wound_state.artery_zone or v85_artery_zone_for(
        profile
    )
    state.variant = v85_death_variant(
        state.profile,
        oyuncu_olum_turu,
        oyuncu_olum_alt_turu,
        state.seed,
    )
    state.ground_flows = v85_ground_flow_build(
        (oyuncu_x, oyuncu_y + 1.0),
        state.direction,
        state.seed,
        15 if state.variant in ("shatter", "torso") else 11,
    )

    if state.variant not in ("minor", "fire"):
        state.fracture = V84FractureField(_v30_oyuncu_base_siluet(), max_fragments=28)
        rng = random.Random(state.seed ^ 0xC0785)
        if state.variant == "decap":
            state.fracture.cut(
                rng.uniform(-5.0, 5.0),
                offset_ratio=-0.31,
                gap_px=1.2,
            )
        elif state.variant == "bisect":
            state.fracture.cut(
                rng.uniform(-28.0, 28.0),
                offset_ratio=rng.uniform(-0.035, 0.035),
                gap_px=1.5,
            )
        elif state.variant == "torso":
            for index, angle in enumerate(
                (
                    rng.uniform(-12.0, 12.0),
                    rng.choice((-52.0, 52.0)),
                )
            ):
                state.fracture.cut(
                    angle,
                    offset_ratio=rng.uniform(-0.14, 0.14),
                    gap_px=1.2 + index * 0.2,
                )
        elif state.variant == "shatter":
            for index in range(rng.randint(6, 9)):
                state.fracture.cut(
                    rng.uniform(-72.0, 72.0),
                    offset_ratio=rng.uniform(-0.20, 0.20),
                    gap_px=1.0 + index * 0.12,
                )
        state.cut_count = max(0, len(state.fracture.fragments) - 1)

    v85_death_tissue_spawn(state)
    if state.variant != "fire" and "v73_ground_splatter" in globals():
        count = (
            34
            if state.variant == "shatter"
            else 25
            if state.variant in ("torso", "bisect")
            else 17
        )
        v73_ground_splatter(
            float(oyuncu_x),
            float(oyuncu_y) + 1.0,
            state.direction,
            count,
            scale_range=(
                0.17,
                0.62 if state.variant != "minor" else 0.44,
            ),
            distance_range=(
                2.0,
                52.0 if state.variant != "minor" else 34.0,
            ),
            cone_deg=142.0,
            backscatter=0.34,
            source="player_death_ground",
        )
# </POTBO_STAGE S1861>

# <POTBO_STAGE S1876>


def v85_hold_cross_begin(target, now):
    global adefo_hold_dash_bitis, oyuncu_saldiri_sure_ms
    state = v85_hold_cross_state
    direction = pygame.Vector2(adefo_hold_dash_yonu)
    if direction.length_squared() <= 1e-8:
        direction = pygame.Vector2(
            float(target.x) - oyuncu_x,
            float(target.y) - oyuncu_y,
        )
    direction = v84_safe_vector(direction, _adefo_yon_vektoru(oyuncu_yonu)).normalize()
    target_position = pygame.Vector2(float(target.x), float(target.y))
    desired = target_position + direction * V85_HOLD_EXIT_CLEARANCE
    desired = v85_execution_safe_point(desired, target_position)
    state.active = True
    state.attack_id = int(saldiri_baslangic)
    state.target = target
    state.target_uid = v84_actor_uid(target)
    state.hit_ms = int(now)
    state.start = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    state.exit = pygame.Vector2(desired)
    state.direction = direction
    state.hit_registered = True
    adefo_hold_dash_bitis = max(
        int(adefo_hold_dash_bitis),
        int(now) + V85_HOLD_CROSS_MS + 24,
    )
    oyuncu_saldiri_sure_ms = max(
        int(oyuncu_saldiri_sure_ms),
        int(now) - int(saldiri_baslangic) + V85_HOLD_CROSS_MS + 36,
    )
    return True
# </POTBO_STAGE S1876>

# <POTBO_STAGE S1878>


_v85_hold_release_original = _adefo_hold_release_baslat


def _adefo_hold_release_baslat(simdi):
    result = _v85_hold_release_original(simdi)
    if oyuncu_saldiri_modu == "hold_release":
        v85_hold_cross_state.reset(int(saldiri_baslangic))
    return result
# </POTBO_STAGE S1878>

# <POTBO_STAGE S1880>


_v85_hold_dash_original = adefonsus_hold_dash_guncelle


def adefonsus_hold_dash_guncelle(simdi=None):
    moved = _v85_hold_dash_original(simdi)
    crossed = v85_hold_cross_update(simdi)
    return bool(moved or crossed)
# </POTBO_STAGE S1880>

# <POTBO_STAGE S1893>


def v84_execution_choreography(target, seed):
    rng = random.Random(int(seed) ^ 0x86EC7)
    center = pygame.Vector2(float(target.x), float(target.y))
    start = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    approach = center - start
    if approach.length_squared() <= 1e-8:
        approach = _adefo_yon_vektoru(oyuncu_yonu)
    approach = v84_safe_vector(approach).normalize()
    side = approach.rotate(90.0)

    # Each pair is a slow staging point followed by the far side of a very fast
    # crossing.  The second and third crossings are opposing diagonals.
    stage_1 = center - approach * 73.0
    exit_1 = center + approach * 81.0
    stage_2 = center + approach * 46.0 - side * 70.0
    exit_2 = center - approach * 48.0 + side * 73.0
    stage_3 = center - approach * 45.0 - side * 75.0
    exit_3 = center + approach * 51.0 + side * 76.0
    points = [
        start,
        v85_execution_safe_point(stage_1, center),
        v85_execution_safe_point(exit_1, center),
        v85_execution_safe_point(stage_2, center),
        v85_execution_safe_point(exit_2, center),
        v85_execution_safe_point(stage_3, center),
        v85_execution_safe_point(exit_3, center),
    ]

    radial = v84_safe_vector(points[-1] - center, side).normalize()
    for index in range(V86_EXECUTION_BURST_COUNT):
        authored = V86_EXECUTION_BURST_ANGLES[index]
        turn = 180.0 + authored * 0.38 + rng.uniform(-6.0, 6.0)
        radial = radial.rotate(turn).normalize()
        radius = rng.uniform(69.0, 94.0)
        # Deliberate radius asymmetry prevents the path from collapsing into a
        # circular orbit or one repeated screen-space line.
        if index % 4 == 1:
            radius *= 0.86
        elif index % 5 == 3:
            radius *= 1.08
        points.append(v85_execution_safe_point(center + radial * radius, center))

    target_facing = _common_enemy_yon_vektoru(str(getattr(target, "direction", "left")))
    target_facing = v84_safe_vector(target_facing, approach).normalize()
    behind = v85_execution_safe_point(center - target_facing * 63.0, center)
    retreat = v85_execution_safe_point(center - target_facing * 155.0, center)
    final_exit = v85_execution_safe_point(center + target_facing * 104.0, center)
    points.extend((behind, retreat, final_exit))
    return points
# </POTBO_STAGE S1893>

# <POTBO_STAGE S1914>


def v86_killer_front_target(killer):
    player = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    facing = v84_safe_vector(_adefo_yon_vektoru(oyuncu_yonu)).normalize()
    distance_by_type = {
        "crawler": 50.0,
        "berserker": 61.0,
        "headsthrower": 128.0,
        "tarkard": 72.0,
        "torrmund": 81.0,
    }
    enemy_type = str(getattr(killer, "tur", ""))
    desired_distance = distance_by_type.get(enemy_type, 60.0)
    current = pygame.Vector2(float(killer.x), float(killer.y))
    delta = current - player
    already_front = (
        delta.length_squared() > 1e-8
        and delta.normalize().dot(facing) >= 0.62
        and abs(delta.length() - desired_distance) <= 34.0
    )
    if already_front:
        return current
    desired = player + facing * desired_distance
    for offset in (0.0, 18.0, -18.0, 34.0, -34.0, 58.0, -58.0):
        candidate = player + facing.rotate(offset) * desired_distance
        try:
            valid = common_enemy_statik_konum_gecerli_mi(
                enemy_type, candidate.x, candidate.y, navigation=True
            )
        except (NameError, TypeError, ValueError):
            valid = True
        if valid:
            return candidate
    return v85_execution_safe_point(desired, player)
# </POTBO_STAGE S1914>

# <POTBO_STAGE S1922>


# =========================================================
# END V86 DEATH DATA / ROUTING
# =========================================================


def v86_impact_direction(state, rotate=0.0):
    source = (
        pygame.Vector2(float(state.killer.x), float(state.killer.y))
        if state.killer is not None
        else pygame.Vector2(state.source_position)
    )
    direction = v84_safe_vector(
        state.body_anchor - source,
        _adefo_yon_vektoru(oyuncu_yonu),
    ).normalize()
    return direction.rotate(float(rotate))
# </POTBO_STAGE S1922>

# <POTBO_STAGE S1969>


def kan_parcacigi_patlat(x, y, adet, guc=1.0, yon=None, arterial=False):
    context = dict(v44_context_current() or {})
    before = len(blood_particles)
    result = _v87_blood_emit_original(x, y, adet, guc, yon=yon, arterial=arterial)
    lethal_enemy = bool(context.get("lethal", False)) and str(
        context.get("target", "")
    ).lower() not in {"", "player", "adefonsus", "preciosa"}
    if not lethal_enemy:
        return result
    created = list(blood_particles[before:])
    for particle in created:
        if hasattr(particle, "v"):
            particle.v *= random.uniform(0.54, 0.68)
        if hasattr(particle, "vz"):
            particle.vz *= random.uniform(0.78, 0.88)
        if hasattr(particle, "gravity"):
            particle.gravity *= random.uniform(1.06, 1.14)
        particle.v87_enemy_death = True
    v87_persistent_blood_stats["enemy_death_particles_shortened"] += len(created)
    return result
# </POTBO_STAGE S1969>

# <POTBO_STAGE S1985>

V88_ASSET_SELECTED = {
    "particles": [],
    "decals": [],
    "gore": {},
    "gore_atlas": "",
    "extra_gore_atlas": "",
    "adefonsus_sheet": "",
}
# </POTBO_STAGE S1985>

# <POTBO_STAGE S1990>


def v88_adefonsus_candidates():
    return (
        os.path.join(ASSETS, "characters", "adefonsus_spriteSheet(3).png"),
        os.path.join(ASSETS, "characters", "adefonsus_spriteSheet.png"),
        os.path.join(ASSETS, "characters", "adefonsus_spritesheet.png"),
        os.path.join(BASE_DIR, "adefonsus_spriteSheet(3).png"),
        os.path.join(BASE_DIR, "adefonsus_spriteSheet.png"),
        os.path.join(V88_REVIEW_ROOT, "adefonsus_spriteSheet(3).png"),
    )


def v88_reload_adefonsus_sheet():
    """Rebuild all directional groups from the supplied magenta-keyed sheet."""
    global adefonsus_sheet, ADEFONSUS_SPRITELERI
    global ADEFONSUS_YENI_SHEET_AKTIF
    global _adefo_loco_raw, _adefo_normal_raw, _adefo_hold_raw
    global _adefo_loco_down, _adefo_loco_left, _adefo_loco_up
    global _adefo_atk_down, _adefo_atk_left, _adefo_atk_up
    global _adefo_hold_down, _adefo_hold_left, _adefo_hold_up

    path, sheet = v88_load_alpha_asset(v88_adefonsus_candidates())
    if sheet is None:
        return False

    loco_raw = _adefonsus_sheet_karelerini_cikar(sheet, ADEFONSUS_LOCOMOTION_RECTLERI)
    normal_raw = _adefonsus_sheet_karelerini_cikar(
        sheet, ADEFONSUS_NORMAL_ATTACK_RECTLERI
    )
    hold_raw = _adefonsus_sheet_karelerini_cikar(sheet, ADEFONSUS_HOLD_ATTACK_RECTLERI)

    loco_down = _adefo_grubu(loco_raw, 0, 3, 4)
    loco_left = _adefo_grubu(loco_raw, 3, 3, 4)
    loco_up = _adefo_grubu(loco_raw, 6, 3, 4)
    attack_down = _adefo_grubu(normal_raw, 0, 2, 5)
    attack_left = _adefo_grubu(normal_raw, 2, 2, 5)
    attack_up = _adefo_grubu(normal_raw, 4, 2, 5)
    hold_down = _adefo_grubu(hold_raw, 0, 3, 6)
    hold_left = _adefo_grubu(hold_raw, 3, 3, 6)
    hold_up = _adefo_grubu(hold_raw, 6, 3, 6)

    candidate = {
        "down": {
            "idle": loco_down[:1],
            "walk": (loco_down[:1] + loco_down[1:2] + loco_down[:1] + loco_down[2:3]),
            "attack": attack_down,
            "hold": hold_down,
        },
        "left": {
            "idle": loco_left[:1],
            "walk": (loco_left[:1] + loco_left[1:2] + loco_left[:1] + loco_left[2:3]),
            "attack": attack_left,
            "hold": hold_left,
        },
        "up": {
            "idle": loco_up[:1],
            "walk": (loco_up[:1] + loco_up[1:2] + loco_up[:1] + loco_up[2:3]),
            "attack": attack_up,
            "hold": hold_up,
        },
    }
    complete = all(
        candidate[direction][animation]
        for direction in ("down", "left", "up")
        for animation in ("idle", "walk", "attack", "hold")
    )
    if not complete:
        return False

    adefonsus_sheet = sheet
    _adefo_loco_raw = loco_raw
    _adefo_normal_raw = normal_raw
    _adefo_hold_raw = hold_raw
    _adefo_loco_down = loco_down
    _adefo_loco_left = loco_left
    _adefo_loco_up = loco_up
    _adefo_atk_down = attack_down
    _adefo_atk_left = attack_left
    _adefo_atk_up = attack_up
    _adefo_hold_down = hold_down
    _adefo_hold_left = hold_left
    _adefo_hold_up = hold_up
    ADEFONSUS_SPRITELERI = candidate
    ADEFONSUS_YENI_SHEET_AKTIF = True
    V88_ASSET_SELECTED["adefonsus_sheet"] = path
    sprite_olcek_onbellegi.clear()
    return True
# </POTBO_STAGE S1990>

# <POTBO_STAGE S1992>
v88_reload_adefonsus_sheet()
# </POTBO_STAGE S1992>

# <POTBO_STAGE S2051>


def v88_asset_diagnostics():
    direct_gore = set(V88_ASSET_SELECTED.get("gore", {}))
    required_gore = {"foot", "intestine", "leg", "liver", "ribcage"}
    return {
        "particle_sprites": len(BLOOD_PARTICLE_SPRITELERI),
        "decal_sprites": len(BLOOD_DECAL_SPRITELERI),
        "direct_gore_loaded": sorted(direct_gore),
        "direct_gore_complete": required_gore.issubset(GORE_SPRITELERI),
        "atlas_gore_loaded": bool(V88_ASSET_SELECTED["gore_atlas"]),
        "extra_gore_loaded": bool(V88_ASSET_SELECTED["extra_gore_atlas"]),
        "adefonsus_sheet_loaded": bool(V88_ASSET_SELECTED["adefonsus_sheet"]),
        "adefonsus_directional_complete": bool(ADEFONSUS_YENI_SHEET_AKTIF),
        "canonical_particle_folder": V88_PARTICLE_ROOT,
        "canonical_decal_folder": V88_DECAL_ROOT,
        "canonical_gore_folder": V88_GORE_ROOT,
    }
# </POTBO_STAGE S2051>

# <POTBO_STAGE S2055>
V88_STARTUP_OK = all(
    (
        V88_STARTUP_CONTRACT["assets"]["particle_sprites"] >= 6,
        V88_STARTUP_CONTRACT["assets"]["decal_sprites"] >= 2,
        V88_STARTUP_CONTRACT["assets"]["direct_gore_complete"],
        V88_STARTUP_CONTRACT["assets"]["adefonsus_directional_complete"],
        not V88_STARTUP_CONTRACT["attribution"]["nearest_enemy_fallback"],
        V88_STARTUP_CONTRACT["death"]["max_hits_per_update"] == 1,
        V88_STARTUP_CONTRACT["death"]["crawler_hit_step_ms"] >= 400,
        V88_STARTUP_CONTRACT["death"]["berserker_hit_step_ms"] >= 580,
        V88_STARTUP_CONTRACT["blood"]["single_drop_pool_spawn"] is False,
        V88_STARTUP_CONTRACT["blood"]["persistent_v74_commit"],
        V88_STARTUP_CONTRACT["death"]["title_delay_ms"] == 2500,
        V88_STARTUP_CONTRACT["death"]["title_fade_ms"] == 2700,
        V88_STARTUP_CONTRACT["death"]["menu_fade_ms"] == 1450,
    )
)
# </POTBO_STAGE S2055>

# <POTBO_STAGE S2114>


def v89_diagnostics():
    return {
        "version": V89_VERSION,
        "title": V89_GAME_TITLE,
        "assets": {
            "ground_fire_frames": len(V89_GROUND_FIRE_FRAMES),
            "small_fire_frames": len(V89_SMALL_FIRE_FRAMES),
            "rat_directions": sum(bool(frames) for frames in RAT_SPRITELERI.values()),
            "worm_frames": len(BLOOD_WORM_SPRITELERI),
            "adefonsus_sheet": bool(ADEFONSUS_YENI_SHEET_AKTIF),
        },
        "blood": {
            "permanent": True,
            "ecology_deletes_stains": False,
            "fire_chars_without_deleting": True,
            "tile_world_size": V89_BLOOD_TILE_WORLD,
            "tile_cache_entries": len(v89_blood_tile_cache),
            "transient_limit": V89_BLOOD_TRANSIENT_LIMIT,
            "decal_count": len(blood_decals),
            "footprint_count": sum(len(items) for items in v89_footprint_grid.values()),
            "active_rivulets": len(v89_rivulets),
        },
        "ecology": {
            "rat_cap": AMBIENT_RAT_MAX,
            "maggot_cap": V89_MAGGOT_MAX,
            "rats_eat_blood": False,
            "rats_eat_maggots_and_organs": True,
            "maggots_feed_and_reproduce": True,
            "fire_is_ecological_hazard": True,
        },
        "ui": {
            "style": "medieval_iron_oak",
            "modern_cut_corners": False,
            "tight_alpha_cropped_icons": True,
            "status_rect": tuple(hud_sol_rect()),
            "belt_rect": tuple(hud_sag_rect()),
        },
        "runtime_stats": dict(v89_stats),
    }
# </POTBO_STAGE S2114>

# <POTBO_STAGE S2140>
V90_BASE_HOLD_COST = float(ADEFO_HOLD_EK_STAMINA)
# </POTBO_STAGE S2140>

# <POTBO_STAGE S2153>


def v90_injury_update(now, dt):
    global oyuncu_stamina
    global saldiri_bekleme_suresi, SALDIRI_STAMINA_MALIYETI
    global ADEFO_HOLD_EK_STAMINA, SAVUNMA_TUTMA_STAMINA_SANIYE
    current_hp = float(oyuncu_hp)
    if current_hp > v90_injury.last_hp + 0.01:
        v90_injury_relieve(current_hp - v90_injury.last_hp)
    v90_injury.last_hp = current_hp
    if int(now) - int(v90_injury.last_damage_ms) > 2200:
        v90_injury.shock = max(0.0, v90_injury.shock - dt * 0.026)
    if not oyuncu_saldiriyor and not oyuncu_savunuyor:
        v90_injury.exertion = max(0.0, v90_injury.exertion - dt * 0.050)
    else:
        v90_injury.exertion = v90_clamp(v90_injury.exertion + dt * 0.018)
    v90_injury_recalculate()
    effective_max = float(oyuncu_max_stamina) * v90_injury.effective_stamina_ratio
    oyuncu_stamina = min(float(oyuncu_stamina), effective_max)
    saldiri_bekleme_suresi = int(
        round(V90_BASE_ATTACK_COOLDOWN * v90_injury.attack_time_multiplier)
    )
    SALDIRI_STAMINA_MALIYETI = max(
        1,
        int(
            round(
                V90_BASE_ATTACK_COST
                * (1.0 + v90_injury_severity() * 0.24 + v90_injury.exertion * 0.14)
            )
        ),
    )
    ADEFO_HOLD_EK_STAMINA = max(
        1,
        int(
            round(
                V90_BASE_HOLD_COST
                * (1.0 + v90_injury_severity() * 0.20)
            )
        ),
    )
    SAVUNMA_TUTMA_STAMINA_SANIYE = (
        V90_BASE_GUARD_DRAIN
        * (1.0 + v90_injury_severity() * 0.32 + v90_injury.shock * 0.12)
    )
    v90_critical_bleed(now)
# </POTBO_STAGE S2153>

# <POTBO_STAGE S2157>


_v90_adefonsus_attack_raw = adefonsus_saldiri_baslat


def adefonsus_saldiri_baslat(simdi=None):
    result = _v90_adefonsus_attack_raw(simdi)
    if result:
        v90_injury.exertion = v90_clamp(
            v90_injury.exertion + 0.075 + 0.045 * v90_injury_severity()
        )
    return result
# </POTBO_STAGE S2157>

# <POTBO_STAGE S2176>


class V90DracoState:
    def __init__(self):
        self.reset()

    def reset(self):
        self.active = False
        self.phase = "idle"
        self.phase_started_ms = 0
        self.cast_started_ms = 0
        self.last_tick_ms = 0
        self.position = pygame.Vector2()
        self.direction = pygame.Vector2(1.0, 0.0)
        self.travelled = 0.0
        self.target = None
        self.target_uid = ""
        self.trail = deque(maxlen=10)
        self.last_trail_ms = 0
        self.next_scorch_ms = 0
        self.damage_applied = False
        self.seed = 0

    def begin(self, now):
        self.reset()
        self.active = True
        self.phase = "cast"
        self.phase_started_ms = int(now)
        self.cast_started_ms = int(now)
        self.last_tick_ms = int(now)
        self.direction = _adefo_yon_vektoru(oyuncu_yonu)
        if self.direction.length_squared() <= 1e-8:
            self.direction = pygame.Vector2(1.0, 0.0)
        self.direction = self.direction.normalize()
        self.position = (
            pygame.Vector2(float(oyuncu_x), float(oyuncu_y) - 23.0)
            + self.direction * 34.0
        )
        self.seed = int(now) ^ int(oyuncu_x * 59) ^ int(oyuncu_y * 83)
        self.next_scorch_ms = int(now)

    def phase_set(self, phase, now):
        self.phase = str(phase)
        self.phase_started_ms = int(now)

    def bind_target(self, actor, now):
        self.target = actor
        self.target_uid = v84_actor_uid(actor)
        self.position = v90_actor_center(actor)
        self.phase_set("bite", now)
        self.trail.clear()
        for attr in ("hit_stun_until", "recovery_until", "stagger_until"):
            if hasattr(actor, attr):
                setattr(
                    actor,
                    attr,
                    max(int(getattr(actor, attr, 0)), int(now) + 1280),
                )
        if hasattr(actor, "attacking"):
            actor.attacking = False
        v90_spawn_embers(self.position, 7, self.seed, self.direction * 20.0)
        v90_draco_stats["hits"] += 1

    def target_valid(self):
        return v90_actor_alive(self.target) and (
            not self.target_uid or v84_actor_uid(self.target) == self.target_uid
        )

    def apply_rupture(self, now):
        if self.damage_applied or not self.target_valid():
            return
        self.damage_applied = True
        target = self.target
        center = v90_actor_center(target)
        source = V90MagicSource(oyuncu_x, oyuncu_y, "draco_calcinans")
        damage = max(
            62,
            int(round(72 + float(oyuncu_guc) * 2.1 + float(oyuncu_level) * 1.4)),
        )
        target.hasar_al(damage, source)
        v90_draco_stats["ruptures"] += 1
        v90_spawn_embers(center, 18, self.seed ^ int(now), pygame.Vector2(0.0, -18.0))
        if v90_actor_alive(target):
            uid = v84_actor_uid(target)
            v90_calcinatio[uid] = V90CalcinatioStatus(
                target,
                uid,
                int(now),
                int(now) + V90_CALCINATIO_DURATION_MS,
                int(now) + V90_CALCINATIO_TICK_MS,
                int(now) + V90_CALCINATIO_PHYSICAL_TRIGGER_MS,
                v90_actor_center(target),
                int(now) + 90,
                self.seed ^ int(now),
            )
            for attr in ("hit_stun_until", "recovery_until"):
                if hasattr(target, attr):
                    setattr(
                        target,
                        attr,
                        max(int(getattr(target, attr, 0)), int(now) + 420),
                    )

    def update(self, now):
        if not self.active:
            self.last_tick_ms = int(now)
            return
        dt = max(0.0, min(0.05, (int(now) - int(self.last_tick_ms)) / 1000.0))
        self.last_tick_ms = int(now)
        age = int(now) - int(self.phase_started_ms)

        if self.phase == "cast":
            self.position = (
                pygame.Vector2(float(oyuncu_x), float(oyuncu_y) - 23.0)
                + self.direction * 34.0
            )
            if age >= V90_DRACO_CAST_MS:
                self.phase_set("flight", now)
                self.last_trail_ms = int(now)
            return

        if self.phase == "flight":
            previous = pygame.Vector2(self.position)
            step = self.direction * (V90_DRACO_SPEED * dt)
            self.position += step
            self.travelled += step.length()
            if int(now) - int(self.last_trail_ms) >= 42:
                frame_index = 4 + (int(now) // 72) % max(1, len(V90_DRACO_FRAMES) - 4)
                self.trail.append(
                    (
                        pygame.Vector2(self.position),
                        min(len(V90_DRACO_FRAMES) - 1, frame_index),
                        int(now),
                    )
                )
                self.last_trail_ms = int(now)
                v90_spawn_embers(
                    self.position - self.direction * 20.0,
                    1,
                    self.seed ^ int(now),
                    -self.direction * 8.0,
                )
            if int(now) >= int(self.next_scorch_ms):
                self.next_scorch_ms = int(now) + 180
                v90_spawn_ash(self.position, now, self.seed ^ int(now))
                v89_fire_affect_world(
                    self.position.x,
                    self.position.y + 17.0,
                    18.0,
                    now,
                )
            target = v90_segment_target(previous, self.position)
            if target is not None:
                self.bind_target(target, now)
                return
            if self.travelled >= V90_DRACO_MAX_TRAVEL:
                self.phase_set("dissipate", now)
                v90_spawn_embers(self.position, 10, self.seed ^ 0xD15A)
                v90_draco_stats["misses"] += 1
            return

        if self.phase == "dissipate":
            if age >= 300:
                self.reset()
            return

        if not self.target_valid():
            self.phase_set("dissipate", now)
            return
        self.position = v90_actor_center(self.target)
        for attr in ("hit_stun_until", "recovery_until"):
            if hasattr(self.target, attr) and self.phase in ("bite", "coil", "collapse"):
                setattr(
                    self.target,
                    attr,
                    max(int(getattr(self.target, attr, 0)), int(now) + 160),
                )

        if self.phase == "bite" and age >= V90_DRACO_BITE_MS:
            self.phase_set("coil", now)
        elif self.phase == "coil" and age >= V90_DRACO_COIL_MS:
            self.phase_set("collapse", now)
        elif self.phase == "collapse" and age >= V90_DRACO_COLLAPSE_MS:
            self.phase_set("silence", now)
        elif self.phase == "silence" and age >= V90_DRACO_SILENCE_MS:
            self.phase_set("rupture", now)
            self.apply_rupture(now)
        elif self.phase == "rupture" and age >= V90_DRACO_RUPTURE_MS:
            self.reset()
# </POTBO_STAGE S2176>

# <POTBO_STAGE S2272>


# ---------------------------------------------------------
# Consistent resource economy. Natural/normal spells are expensive; developer
# casts are handled separately and never touch this curve.
# ---------------------------------------------------------
def v92_resource_balance_refresh():
    global FIRE_MAGIC_MANA_MALIYETI, V38_FIRE_CAST_STAMINA_COST
    global V90_DRACO_MANA_COST, V90_DRACO_STAMINA_COST
    global SALDIRI_STAMINA_MALIYETI, DASH_STAMINA_MALIYETI, ADEFO_HOLD_EK_STAMINA
    global V90_BASE_ATTACK_COST, V90_BASE_DASH_COST, V90_BASE_HOLD_COST
    global V90_BASE_GUARD_DRAIN, SAVUNMA_TUTMA_STAMINA_SANIYE
    global V38_SPECIAL_STAMINA_PER_HIT, V38_SPECIAL_TOTAL_STAMINA
    global V38_SPECIAL_PREP_REFUND
    mana_pool = max(1.0, float(oyuncu_max_mana))
    stamina_pool = max(1.0, float(oyuncu_max_stamina))
    p = (max(1, int(oyuncu_level)) - 1) / max(1.0, float(MAKSIMUM_LEVEL - 1))

    # Natural magic stays deliberately expensive. Increasing max mana creates
    # additional casts only gradually instead of trivialising the economy.
    FIRE_MAGIC_MANA_MALIYETI = max(50, int(round(mana_pool * (0.43 - 0.035 * p))))
    V90_DRACO_MANA_COST = max(68, int(round(mana_pool * (0.53 - 0.040 * p))))
    V38_FIRE_CAST_STAMINA_COST = max(9.0, stamina_pool * (0.090 - 0.006 * p))
    V90_DRACO_STAMINA_COST = max(12.0, stamina_pool * (0.125 - 0.012 * p))

    # These V90 baseline values are the canonical inputs used by the injury
    # system every frame. Updating only the live aliases would be overwritten.
    V90_BASE_ATTACK_COST = max(15.0, stamina_pool * (0.175 - 0.018 * p))
    V90_BASE_DASH_COST = max(28.0, stamina_pool * (0.315 - 0.025 * p))
    V90_BASE_HOLD_COST = max(10.0, stamina_pool * (0.115 - 0.010 * p))
    V90_BASE_GUARD_DRAIN = max(6.0, stamina_pool * (0.070 - 0.006 * p))
    SALDIRI_STAMINA_MALIYETI = V90_BASE_ATTACK_COST
    DASH_STAMINA_MALIYETI = V90_BASE_DASH_COST
    ADEFO_HOLD_EK_STAMINA = V90_BASE_HOLD_COST
    SAVUNMA_TUTMA_STAMINA_SANIYE = V90_BASE_GUARD_DRAIN
    V38_SPECIAL_STAMINA_PER_HIT = max(15.0, stamina_pool * (0.170 - 0.012 * p))
    V38_SPECIAL_TOTAL_STAMINA = V38_SPECIAL_STAMINA_PER_HIT * 3.0
    V38_SPECIAL_PREP_REFUND = V90_BASE_ATTACK_COST + V90_BASE_HOLD_COST
# </POTBO_STAGE S2272>

# <POTBO_STAGE S2292>


def v92_spawn_passive_headsthrowers():
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA:
        return True
    direction = pygame.Vector2(_adefo_yon_vektoru(oyuncu_yonu))
    if direction.length_squared() <= 1e-8:
        direction = pygame.Vector2(1.0, 0.0)
    direction = direction.normalize()
    side = direction.rotate(90.0)
    spawned = 0
    for index in range(5):
        distance = 82.0 + index * 72.0
        point = pygame.Vector2(float(oyuncu_x), float(oyuncu_y)) + direction * distance
        point += side * ((-1 if index % 2 else 1) * (5.0 + index * 1.8))
        point.x = max(42.0, min(HARITA_GENISLIK - 42.0, point.x))
        point.y = max(48.0, min(HARITA_YUKSEKLIK - 34.0, point.y))
        uid = f"v92_passive_head_{pygame.time.get_ticks()}_{index}_{random.randint(10,9999)}"
        try:
            actor = CommonEnemy(uid, "headsthrower", point.x, point.y)
        except Exception:
            continue
        actor.v92_passive = True
        actor.aggro = False
        actor.attacking = False
        common_enemies.append(actor)
        spawned += 1
    bildirim_goster(
        bt(f"{spawned} pasif Heads Thrower yerleştirildi.", f"Placed {spawned} passive Heads Throwers."),
        V91_UI_GREY,
    )
    return True
# </POTBO_STAGE S2292>

# <POTBO_STAGE S2314>


def gelistirici_x_skill_r_birak(simdi=None):
    global gelistirici_x_skill_r_basildi
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if v92_training.get("decussatio_rubra", 0) >= 5 and gelistirici_x_skill_r_basildi:
        direction = pygame.Vector2(_adefo_yon_vektoru(oyuncu_yonu))
        if direction.length_squared() <= 1e-8:
            direction = pygame.Vector2(1.0, 0.0)
        target = _gelistirici_x_skill_hedef_sec(direction.normalize())
        if target is not None and v84_actor_distance(target) <= V92_X_SPECIAL_MAX_RANGE:
            expected = float(oyuncu_saldiri_hasar_miktari()) * sum(GELISTIRICI_X_SKILL_HASAR_CARPANLARI)
            target_hp = max(0, int(getattr(target, "hp", 0)))
            target_max_hp = max(target_hp, int(getattr(target, "max_hp", target_hp or 1)))
            critical = target_hp / max(1.0, float(target_max_hp)) <= 0.28
            if critical and target_hp <= int(expected * 0.96):
                global oyuncu_saldiriyor, oyuncu_savunuyor
                gelistirici_x_skill_r_basildi = False
                gelistirici_x_skill_sifirla(False)
                # Execution director rejects ordinary combat locks. The learned
                # special owns this transition, so clear only the player's local
                # attack/guard latch; enemy and world locks remain authoritative.
                oyuncu_saldiriyor = False
                oyuncu_savunuyor = False
                if v84_execution_start(target=target, override=True, source="decussatio_rubra_lethal"):
                    return True
    return _v92_x_release_raw(simdi)
# </POTBO_STAGE S2314>

# <POTBO_STAGE S2323>


def v92_chain_start(dx, dy):
    global oyuncu_savunuyor, oyuncu_saldiriyor, oyuncu_stamina, stamina_son_harcama
    if v92_training.get("catena_decollationis", 0) < 5 or v92_chain_state.active:
        return False
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA or oyuncu_hp <= 0:
        return False
    direction = pygame.Vector2(dx, dy)
    if direction.length_squared() <= 1e-8:
        direction = pygame.Vector2(_adefo_yon_vektoru(oyuncu_yonu))
    if direction.length_squared() <= 1e-8:
        return False
    direction = direction.normalize()
    targets = v92_chain_targets(direction)
    if not targets:
        return False
    cost = max(24.0, float(DASH_STAMINA_MALIYETI) * 0.82 + len(targets) * 4.0)
    if float(oyuncu_stamina) < cost:
        hud_uyari_baslat("stamina")
        return True
    oyuncu_stamina = max(0.0, float(oyuncu_stamina) - cost)
    stamina_son_harcama = pygame.time.get_ticks()
    damage = max(1, int(round(oyuncu_saldiri_hasar_miktari() * V92_CHAIN_HIT_SCALE)))
    lethal_all = all(int(getattr(actor, "hp", 0)) <= damage for actor in targets)
    state = v92_chain_state
    state.reset()
    state.active = True
    state.execution = bool(lethal_all)
    state.started_ms = pygame.time.get_ticks()
    state.last_ms = state.started_ms
    state.targets = list(targets)
    state.damage = damage
    state.start_player = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    state.points = [state.start_player]
    state.silhouettes = []
    for actor in targets:
        center = v90_actor_center(actor)
        # Attack crosses the body then exits slightly behind it.
        state.points.append(center - direction * 12.0)
        state.points.append(center + direction * 30.0)
        try:
            silhouette = v84_actor_silhouette(actor)
        except Exception:
            silhouette = None
        state.silhouettes.append((actor, silhouette, center))
    state.final_player = state.points[-1] + direction * 20.0
    state.points.append(state.final_player)
    state.duration_ms = V92_CHAIN_EXECUTION_MS if lethal_all else max(360, len(targets) * V92_CHAIN_NORMAL_MS_PER_LINK + 180)
    oyuncu_savunuyor = False
    oyuncu_saldiriyor = False
    for actor in targets:
        if hasattr(actor, "attacking"):
            actor.attacking = False
        for attr in ("hit_stun_until", "stagger_until", "recovery_until"):
            if hasattr(actor, attr):
                setattr(actor, attr, state.started_ms + state.duration_ms + 300)
    dunya_olayi_kaydet("special_chain_start", targets=len(targets), lethal=bool(lethal_all))
    return True
# </POTBO_STAGE S2323>

# <POTBO_STAGE S2325>


def v92_chain_spawn_head(actor, silhouette, center, index):
    if silhouette is None:
        return
    h = max(4, int(round(silhouette.get_height() * 0.31)))
    crop = silhouette.subsurface(pygame.Rect(0, 0, silhouette.get_width(), h)).copy().convert_alpha()
    rng = random.Random(v92_chain_state.started_ms ^ (index * 1999) ^ int(center.x * 11))
    velocity = pygame.Vector2(rng.uniform(-28.0, 28.0), rng.uniform(-18.0, 18.0))
    velocity += pygame.Vector2(_adefo_yon_vektoru(oyuncu_yonu)).rotate(rng.uniform(-34.0, 34.0)) * rng.uniform(25.0, 58.0)
    v92_chain_state.heads.append(
        V92ChainHead(crop, pygame.Vector2(center), velocity, 7.0, rng.uniform(38.0, 68.0), rng.uniform(0.0, 360.0), rng.uniform(-140.0, 140.0))
    )


def v92_chain_hit_target(index, now):
    state = v92_chain_state
    bit = 1 << index
    if state.hit_mask & bit or index >= len(state.targets):
        return
    state.hit_mask |= bit
    actor = state.targets[index]
    if not v90_actor_alive(actor):
        return
    center = v90_actor_center(actor)
    silhouette = state.silhouettes[index][1] if index < len(state.silhouettes) else None
    actor.hasar_al(state.damage, "player")
    direction = pygame.Vector2(float(actor.x) - float(oyuncu_x), float(actor.y) - float(oyuncu_y))
    direction = v84_safe_vector(direction, _adefo_yon_vektoru(oyuncu_yonu)).normalize()
    kan_parcacigi_patlat(center.x, center.y, 22 if state.execution else 14, 1.16, yon=direction, arterial=state.execution)
    combat_impact_spawn(center.x, center.y - 8.0, "slash_heavy", 1.8, direction)
    if state.execution:
        v92_chain_spawn_head(actor, silhouette, center, index)
    kamera_hit_sarsintisi_baslat(6.0 if az_hareket else 9.0, 110)
# </POTBO_STAGE S2325>

# <POTBO_STAGE S2362>


def _v94_hold_ready(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    if not oyuncu_saldiriyor or karakter_cinsiyet != "male" or not ADEFONSUS_YENI_SHEET_AKTIF:
        return False
    if oyuncu_saldiri_modu == "charge":
        return True
    if oyuncu_saldiri_modu == "press" and adefo_saldiri_tusu_baslangic_ms > 0:
        return int(now) - int(adefo_saldiri_tusu_baslangic_ms) >= int(ADEFO_HOLD_ESIK_MS)
    return False
# </POTBO_STAGE S2362>

# <POTBO_STAGE S2365>


def v92_chain_start(dx, dy):
    global v94_chain_next_ready_ms
    now = pygame.time.get_ticks()
    if v92_training.get("catena_decollationis", 0) < 5:
        return False
    if not _v94_hold_ready(now) or now < int(v94_chain_next_ready_ms):
        return False
    direction = pygame.Vector2(dx, dy)
    if direction.length_squared() <= 1e-8:
        direction = pygame.Vector2(_adefo_yon_vektoru(oyuncu_yonu))
    if direction.length_squared() <= 1e-8:
        return False
    targets = v92_chain_targets(direction.normalize())
    if len(targets) < 2:
        return False
    started = bool(_v94_chain_start_previous(dx, dy))
    if started and v92_chain_state.active:
        v94_chain_next_ready_ms = int(now) + V94_CHAIN_RECOVERY_MS
    return started
# </POTBO_STAGE S2365>

# <POTBO_STAGE S2436>

V99_ADEFONSUS_HINTS_TR = [
    "Adefonsus'ta J'ye kısa basmak normal saldırı, basılı tutmak ağır saldırı hazırlığıdır. İki girdi aynı tuşu paylaşır; süreyi bilinçli kullan.",
    "Adefonsus'un ağır saldırısı hedefin içinden geçerek arkasına çıkabilir. Hamleyi duvara veya kalabalığın merkezine doğru başlatmak kaçış alanını daraltır.",
    "Adefonsus yüksek baskıyı sever ancak stamina'sız kaldığında avantajını kaybeder. Ağır saldırıdan sonra en az bir savunma veya dash payı bırak.",
    "Decussatio Rubra ve Catena Decollationis normal saldırı değildir. İkisi de Reinald'da tam eğitim ister ve J hold durumundan tetiklenir.",
    "Catena yalnızca birbirine bağlanabilecek en az iki uygun hedef bulunduğunda başlar. Hedefler aynı çizgide veya yakın bir zincirdeyse teknik onları sırayla keser.",
    "Adefonsus ile dar koridorlarda düz baskı güçlüdür; açık alanda ise saldırıdan önce hedefe dönmek ve çıkış yönünü seçmek daha önemlidir.",
]
# </POTBO_STAGE S2436>

# <POTBO_STAGE S2439>

IPUCLARI = {
    "TR": V99_COMMON_HINTS_TR + V99_ADEFONSUS_HINTS_TR,
    "EN": V99_COMMON_HINTS_EN + [
        "With Adefonsus, tapping J performs a normal attack while holding J prepares a heavy attack. The same key serves both actions, so control the timing deliberately.",
        "Adefonsus's heavy release can pass through a target and leave him behind it. Do not commit toward a wall or the center of a crowd unless the exit is safe.",
        "Adefonsus thrives on pressure but loses that advantage when stamina is empty. Leave enough resource for at least one guard or dash after a heavy attack.",
        "Decussatio Rubra and Catena Decollationis are not ordinary attacks. Both require full training with Reinald and start from a held-J state.",
        "Catena starts only when at least two valid targets can be chained. If they share a line or a close chain, the technique cuts through them in sequence.",
        "Adefonsus is strong in narrow lanes. In open ground, facing the target and choosing an exit line before attacking matters more than raw pressure.",
    ],
}
# </POTBO_STAGE S2439>

# <POTBO_STAGE S2441>


# ---------------------------------------------------------
# CATENA DECOLLATIONIS INPUT FIX
# - at least two valid, chainable targets are required;
# - holding J + SHIFT is buffered until the heavy-charge threshold;
# - no movement key is required: facing direction is used as fallback;
# - ordinary dash is not allowed to consume the combo while a valid target exists.
# ---------------------------------------------------------
def v92_chain_start(dx, dy):
    global v94_chain_next_ready_ms
    now = pygame.time.get_ticks()
    if v92_training.get("catena_decollationis", 0) < 5:
        return False
    if not _v94_hold_ready(now) or now < int(v94_chain_next_ready_ms):
        return False

    direction = pygame.Vector2(dx, dy)
    if direction.length_squared() <= 1e-8:
        direction = pygame.Vector2(_adefo_yon_vektoru(oyuncu_yonu))
    if direction.length_squared() <= 1e-8:
        return False
    direction = direction.normalize()

    # A single target gives the technique a useful minimum case; multiple targets
    # still form the authored chain / zig-zag path.
    if not v92_chain_targets(direction):
        return False

    started = bool(_v94_chain_start_previous(direction.x, direction.y))
    if started and v92_chain_state.active:
        v94_chain_next_ready_ms = int(now) + V94_CHAIN_RECOVERY_MS
    return started


def _v99_catena_direction_from_keys(keys):
    direction = pygame.Vector2(
        int(bool(keys[tus_atamasi("move_right")]))
        - int(bool(keys[tus_atamasi("move_left")])),
        int(bool(keys[tus_atamasi("move_down")]))
        - int(bool(keys[tus_atamasi("move_up")])),
    )
    if direction.length_squared() > 1.0:
        direction = direction.normalize()
    if direction.length_squared() <= 1e-8:
        direction = pygame.Vector2(_adefo_yon_vektoru(oyuncu_yonu))
    return direction
# </POTBO_STAGE S2441>

# <POTBO_STAGE S2444>


def oyuncu_serbest_hareket_guncelle():
    global dash_tus_kilitli, v99_catena_combo_latched

    if (
        oyun_durumu != OYUN
        or oyun_alt_durumu != HARITA
        or oyuncu_hp <= 0
        or karakter_cinsiyet != "male"
        or not ADEFONSUS_YENI_SHEET_AKTIF
        or v92_training.get("catena_decollationis", 0) < 5
    ):
        v99_catena_combo_latched = False
        return _v99_free_move_raw()

    keys = pygame.key.get_pressed()
    dash_held = bool(keys[tus_atamasi("dash")])
    attack_held = bool(keys[tus_atamasi("attack")])

    if not dash_held or not attack_held:
        v99_catena_combo_latched = False
        return _v99_free_move_raw()

    direction = _v99_catena_direction_from_keys(keys)
    targets = v92_chain_targets(direction) if direction.length_squared() > 1e-8 else []

    # No valid target: preserve ordinary dash behavior instead of eating the input.
    if not targets:
        return _v99_free_move_raw()

    now = pygame.time.get_ticks()
    if not v99_catena_combo_latched and _v94_hold_ready(now):
        if v92_chain_start(direction.x, direction.y):
            v99_catena_combo_latched = True
            dash_tus_kilitli = True
            return True

    # A target exists and the combo is being held, but J has not reached the
    # charge threshold yet. Block the ordinary dash for this frame so SHIFT stays
    # buffered instead of consuming the combination too early.
    dash_tus_kilitli = True
    result = _v99_free_move_raw()
    if dash_held and attack_held and not v92_chain_state.active:
        dash_tus_kilitli = True
    return result
# </POTBO_STAGE S2444>

# <POTBO_STAGE S2464>


# ---------------------------------------------------------
# DECUSSATIO RUBRA: lethal prediction alone decides whether the red/black
# many-cut execution director is entered. Non-lethal use remains the authored
# three-cut special and never enters the execution tableau.
# ---------------------------------------------------------
def gelistirici_x_skill_r_birak(simdi=None):
    global gelistirici_x_skill_r_basildi, oyuncu_saldiriyor, oyuncu_savunuyor
    if simdi is None:
        simdi = pygame.time.get_ticks()

    if v92_training.get("decussatio_rubra", 0) >= 5 and gelistirici_x_skill_r_basildi:
        direction = pygame.Vector2(_adefo_yon_vektoru(oyuncu_yonu))
        if direction.length_squared() <= 1e-8:
            direction = pygame.Vector2(1.0, 0.0)
        target = _gelistirici_x_skill_hedef_sec(direction.normalize())
        if target is not None and v84_actor_distance(target) <= V92_X_SPECIAL_MAX_RANGE:
            expected = max(
                1,
                int(round(float(oyuncu_saldiri_hasar_miktari()) * sum(GELISTIRICI_X_SKILL_HASAR_CARPANLARI))),
            )
            target_hp = max(0, int(getattr(target, "hp", 0)))
            if 0 < target_hp <= expected:
                gelistirici_x_skill_r_basildi = False
                gelistirici_x_skill_sifirla(False)
                oyuncu_saldiriyor = False
                oyuncu_savunuyor = False
                if v84_execution_start(
                    target=target,
                    override=True,
                    source="decussatio_rubra_lethal",
                ):
                    return True

    # The inherited X move applies its normal three physical cuts and damage.
    return _v92_x_release_raw(simdi)
# </POTBO_STAGE S2464>

# <POTBO_STAGE S2467>


def v92_chain_start(dx, dy):
    global v94_chain_next_ready_ms
    now = pygame.time.get_ticks()
    if v92_training.get("catena_decollationis", 0) < 5:
        return False
    if not _v94_hold_ready(now) or now < int(v94_chain_next_ready_ms):
        return False

    direction = pygame.Vector2(dx, dy)
    if direction.length_squared() <= 1e-8:
        direction = pygame.Vector2(_adefo_yon_vektoru(oyuncu_yonu))
    if direction.length_squared() <= 1e-8:
        return False
    direction = direction.normalize()

    targets = v92_chain_targets(direction)
    if len(targets) < V100_CATENA_MIN_TARGETS:
        return False

    started = bool(_v94_chain_start_previous(direction.x, direction.y))
    if started and v92_chain_state.active:
        # Re-evaluate the duration after the inherited constructor because V94
        # may have been authored with a shorter execution constant.
        if v92_chain_state.execution:
            v92_chain_state.duration_ms = V92_CHAIN_EXECUTION_MS
        v94_chain_next_ready_ms = int(now) + V94_CHAIN_RECOVERY_MS
    return started


# Replace V99's one-target buffer with the final multi-target contract.
def oyuncu_serbest_hareket_guncelle():
    global dash_tus_kilitli, v99_catena_combo_latched

    if (
        oyun_durumu != OYUN
        or oyun_alt_durumu != HARITA
        or oyuncu_hp <= 0
        or karakter_cinsiyet != "male"
        or not ADEFONSUS_YENI_SHEET_AKTIF
        or v92_training.get("catena_decollationis", 0) < 5
    ):
        v99_catena_combo_latched = False
        return _v99_free_move_raw()

    keys = pygame.key.get_pressed()
    dash_held = bool(keys[tus_atamasi("dash")])
    attack_held = bool(keys[tus_atamasi("attack")])
    if not dash_held or not attack_held:
        v99_catena_combo_latched = False
        return _v99_free_move_raw()

    direction = _v99_catena_direction_from_keys(keys)
    targets = v92_chain_targets(direction) if direction.length_squared() > 1e-8 else []

    # Fewer than two targets means this is not Catena; preserve ordinary dash.
    if len(targets) < V100_CATENA_MIN_TARGETS:
        return _v99_free_move_raw()

    now = pygame.time.get_ticks()
    if not v99_catena_combo_latched and _v94_hold_ready(now):
        if v92_chain_start(direction.x, direction.y):
            v99_catena_combo_latched = True
            dash_tus_kilitli = True
            return True

    # J+SHIFT is buffered while the heavy-charge threshold is being reached.
    dash_tus_kilitli = True
    result = _v99_free_move_raw()
    if dash_held and attack_held and not v92_chain_state.active:
        dash_tus_kilitli = True
    return result
# </POTBO_STAGE S2467>

# <POTBO_STAGE S2504>


def v105_grant_corona_aetherica():
    global v107_corona_test_cast_ready, v106_corona_last_cast_ms
    index = v105_find_inventory_item("corona_aetherica")
    if index is None:
        if not envantere_item_ekle(
            corona_aetherica_olustur(),
            kazanimi_goster=False,
        ):
            bildirim_goster(bt("Envanter dolu.", "Inventory is full."), V91_UI_RED_HOT)
            return True
        index = v105_find_inventory_item("corona_aetherica")
    if index is None:
        return True
    itemi_q_hizli_slota_ata(index)
    # Adefonsus starts with 50 max mana while Corona costs 70. CTRL+3 is explicitly
    # a test shortcut, so arm exactly one free/cooldown-free cast instead of mutating
    # the character's permanent mana stats. Normal acquired Corona still costs 70.
    v107_corona_test_cast_ready = True
    v106_corona_last_cast_ms = -1000000
    bildirim_goster(
        bt(
            "Corona Aetherica → Q. Sonraki Q test castı hazır.",
            "Corona Aetherica → Q. The next Q test cast is ready.",
        ),
        V91_UI_GOLD,
    )
    return True
# </POTBO_STAGE S2504>

# <POTBO_STAGE S2532>


# ---------------------------------------------------------
# CORONA AETHERICA
# Q forms three AETHER cores. While any core remains in orbit, J fires the next
# core instead of performing melee. Expiry scatters only the remaining cores.
# The top 'idle' row of corona_aetherica_cast.png is the only authored sprite row
# used here; the lower death/line row is intentionally ignored.
# ---------------------------------------------------------
# V107 fixes the test-cast contract: the normal spell remains a 70-mana spell,
# but CTRL+3 arms one free cast so a fresh 50-mana Adefonsus can actually test it.
v107_corona_test_cast_ready = False
# </POTBO_STAGE S2532>

# <POTBO_STAGE S2544>


def v106_corona_facing_direction():
    direction = pygame.Vector2(_adefo_yon_vektoru(oyuncu_yonu))
    if direction.length_squared() <= 1e-8:
        direction = pygame.Vector2(1.0, 0.0)
    return direction.normalize()
# </POTBO_STAGE S2544>

# <POTBO_STAGE S2614>



def v110_fulmen_facing():
    direction = pygame.Vector2(_adefo_yon_vektoru(oyuncu_yonu))
    if direction.length_squared() <= 1e-8:
        direction = pygame.Vector2(1.0, 0.0)
    return direction.normalize()
# </POTBO_STAGE S2614>

