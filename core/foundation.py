






# <POTBO_STAGE S0001>
import heapq
import json
import math
import os
import random
import re
import shutil
import sys
import time
from collections import deque
from dataclasses import dataclass, field
from typing import Any, Optional

import pygame
# </POTBO_STAGE S0001>

# <POTBO_STAGE S0003>


pygame.mouse.set_visible(False)
# </POTBO_STAGE S0003>

# <POTBO_STAGE S0006>
YUKSEKLIK = 720
FPS = 60
# </POTBO_STAGE S0006>

# <POTBO_STAGE S0009>

tam_ekran = True
dil = "TR"
# </POTBO_STAGE S0009>

# <POTBO_STAGE S0011>

fps_goster = False
parlaklik = 100

ekran_sarsintisi = True
etkilesim_ipuclari = True
# </POTBO_STAGE S0011>

# <POTBO_STAGE S0014>
az_hareket = False
metin_hizi = "normal"


DEBUG_LOGS = False
GELISTIRICI_MODU = os.environ.get("PATH_BLOODIED_DEV", "1").strip().lower() not in {"0", "false", "no", "off"}


def debug_log(*args):
    if DEBUG_LOGS:
        print(*args)


ekran = None
saat = pygame.time.Clock()


def ekran_olustur():
    global ekran

    bayraklar = pygame.SCALED

    if tam_ekran:
        bayraklar |= pygame.FULLSCREEN

    try:
        ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK), bayraklar)
    except pygame.error:
        ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))

    pygame.display.set_caption("Path of the Bloodied One — Agraphon Studios")


ekran_olustur()





BASE_DIR = os.path.abspath(getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__))))


def kullanici_veri_klasoru():
    """Return a writable per-user data directory without external dependencies."""
    if sys.platform.startswith("win"):
        kok = os.environ.get("LOCALAPPDATA") or os.environ.get("APPDATA")
        if not kok:
            kok = os.path.join(os.path.expanduser("~"), "AppData", "Local")
        return os.path.join(kok, "Agraphon Studios", "Path of the Bloodied One")
    if sys.platform == "darwin":
        return os.path.join(
            os.path.expanduser("~"),
            "Library",
            "Application Support",
            "Agraphon Studios",
            "Path of the Bloodied One",
        )
    kok = os.environ.get("XDG_DATA_HOME") or os.path.join(
        os.path.expanduser("~"), ".local", "share"
    )
    return os.path.join(kok, "agraphon-studios", "path-of-the-bloodied-one")


USER_DATA_DIR = kullanici_veri_klasoru()
# </POTBO_STAGE S0014>

# <POTBO_STAGE S0017>

SAVES = os.path.join(USER_DATA_DIR, "saves")
# </POTBO_STAGE S0017>

# <POTBO_STAGE S0041>


def mevcut_ilk_dosya(yollar):
    for yol in yollar:
        if os.path.exists(yol):
            return yol

    return None
# </POTBO_STAGE S0041>

# <POTBO_STAGE S0068>

os.makedirs(SAVES, exist_ok=True)


_legacy_saves = os.path.join(BASE_DIR, "saves")
if os.path.isdir(_legacy_saves) and os.path.abspath(_legacy_saves) != os.path.abspath(SAVES):
    for _legacy_name in os.listdir(_legacy_saves):
        if not _legacy_name.endswith(".json"):
            continue
        _legacy_src = os.path.join(_legacy_saves, _legacy_name)
        _legacy_dst = os.path.join(SAVES, _legacy_name)
        if not os.path.exists(_legacy_dst):
            try:
                shutil.copy2(_legacy_src, _legacy_dst)
            except OSError:
                pass




SIYAH = (0, 0, 0)
BEYAZ = (242, 240, 244)

KOYU_ARKA = (4, 3, 7)
KOYU_PANEL = (11, 9, 14)
KOYU_GRI = (22, 20, 28)

GRI = (120, 115, 130)
ACIK_GRI = (205, 200, 212)

KOYU_KIRMIZI = (65, 3, 13)
# </POTBO_STAGE S0068>

# <POTBO_STAGE S0070>
PARLAK_KIRMIZI = (225, 24, 46)

MOR = (95, 35, 125)
ACIK_MOR = (175, 80, 210)

MAVI = (55, 110, 240)
MANA_MAVI = (45, 150, 255)
YESIL = (50, 210, 95)
SARI = (245, 205, 65)
# </POTBO_STAGE S0070>

# <POTBO_STAGE S0077>


def t(anahtar):
    return METINLER[dil][anahtar]


def bt(turkce, ingilizce):
    """
    Oyun içinde doğrudan kullanılan metinleri seçili dile bağlar.
    Oyun adı ve özel isimler bu yardımcıdan geçirilmez.
    """
    return turkce if dil == "TR" else ingilizce
# </POTBO_STAGE S0077>

# <POTBO_STAGE S0083>
KARAKTER_OLUSTUR = "karakter_olustur"
LOADING = "loading"
OYUN = "oyun"
# </POTBO_STAGE S0083>

# <POTBO_STAGE S0087>
CIKIS_ONAY = "cikis_onay"
# </POTBO_STAGE S0087>

# <POTBO_STAGE S0089>
DURAKLATMA = "duraklatma"
# </POTBO_STAGE S0089>

# <POTBO_STAGE S0094>
OYUNDAN_CIKIS_ONAY = "oyundan_cikis_onay"
# </POTBO_STAGE S0094>

# <POTBO_STAGE S0099>
ayar_index = 0
ayar_kategori_index = 0
ayar_odak = "kategori"



ayar_scroll_baslangic = 0
# </POTBO_STAGE S0099>

# <POTBO_STAGE S0102>

cikis_index = 1
duraklatma_index = 0
# </POTBO_STAGE S0102>

# <POTBO_STAGE S0105>
oyundan_cikis_onay_index = 1
# </POTBO_STAGE S0105>

# <POTBO_STAGE S0111>

onemli_item_kuyrugu = []
onemli_item_acilis_zamani = 0
onemli_item_gosterim_aktif = False
onemli_item_gosterim_hazir_zamani = 0
onemli_item_gorsel_hazir_zamani = 0
ONEMLI_ITEM_SAHNE_GECIKMESI = 260
# </POTBO_STAGE S0111>

# <POTBO_STAGE S0113>

ONEMLI_ITEM_GOSTERIM_SURESI = 5000
ONEMLI_ITEM_GIRIS_KILIDI = ONEMLI_ITEM_GOSTERIM_SURESI
# </POTBO_STAGE S0113>

# <POTBO_STAGE S0117>

bonus_guc = 0
bonus_can = 0
bonus_mana = 0
bonus_kalan = 10

karakter_mesaji = ""



karakter_onay_gecisi_aktif = False
karakter_onay_gecisi_baslangic = 0
KARAKTER_ONAY_GECIS_SURESI = 2200
KARAKTER_ONAY_FADE_BASLANGICI = 620
# </POTBO_STAGE S0117>

# <POTBO_STAGE S0120>

MAKSIMUM_LEVEL = 50
# </POTBO_STAGE S0120>

# <POTBO_STAGE S0125>
mana_gorunen = 50.0
hp_gorunen = 100.0
# </POTBO_STAGE S0125>

# <POTBO_STAGE S0127>
mana_uyari_bitis = 0
# </POTBO_STAGE S0127>

# <POTBO_STAGE S0134>
gelistirici_yanma_efekti_aktif = True
# </POTBO_STAGE S0134>

# <POTBO_STAGE S0145>
common_enemies = []
# </POTBO_STAGE S0145>

# <POTBO_STAGE S0160>
OLU_CESET_YERLESME_MS = 340
# </POTBO_STAGE S0160>

# <POTBO_STAGE S0162>
OLU_CIKIS_FADE_MS = 720
# </POTBO_STAGE S0162>

# <POTBO_STAGE S0164>


seviye_anim_level = 0
seviye_anim_baslangic = 0
SEVIYE_ANIM_SURESI_MS = 1850
# </POTBO_STAGE S0164>

# <POTBO_STAGE S0174>

animasyon_index = 0
animasyon_zamani = 0
# </POTBO_STAGE S0174>

# <POTBO_STAGE S0177>

npc_x = 860.0
npc_y = 330.0
# </POTBO_STAGE S0177>

# <POTBO_STAGE S0180>

eadric_adi_ogrenildi = False
npc_intro_tamamlandi = False
ganimet_alindi = False
ganimet_asamasi = 0
ganimet_sonrasi_konusma_yapildi = False
# </POTBO_STAGE S0180>

# <POTBO_STAGE S0182>
eadric_tasi_alindi = False
# </POTBO_STAGE S0182>

# <POTBO_STAGE S0185>


ganimet_x = 1605.0
ganimet_y = 520.0


bildirim_kuyrugu = []
bildirim_aktif_baslangic = 0

bildirim_suresi = 4200
bildirim_son_fade = 900

son_tus_zamanlari = {}
TUS_BEKLEME_YON = 105
TUS_BEKLEME_AKSIYON = 180
TUS_BEKLEME_MODAL = 240
# </POTBO_STAGE S0185>

# <POTBO_STAGE S0189>
tus_atamalari = dict(VARSAYILAN_TUS_ATAMALARI)
tus_atama_bekleniyor = None
tus_atama_mesaji = ""
tus_atama_mesaj_bitis = 0
# </POTBO_STAGE S0189>

# <POTBO_STAGE S0191>
GELISTIRICI_TEST_TUSLARI = {
    pygame.K_u,
    pygame.K_i,
    pygame.K_l,
    pygame.K_o,
}
AYRILMIS_ATAMA_TUSLARI = {
    pygame.K_RETURN,
    pygame.K_KP_ENTER,
    pygame.K_SPACE,
    pygame.K_BACKSPACE,
    pygame.K_r,
}


def tus_atamasi(eylem):
    return tus_atamalari.get(eylem, VARSAYILAN_TUS_ATAMALARI[eylem])
# </POTBO_STAGE S0191>

# <POTBO_STAGE S0193>


def tus_gorunen_adi_deger(tus_kodu):
    ozel = {
        pygame.K_LSHIFT: "L SHIFT",
        pygame.K_RSHIFT: "R SHIFT",
        pygame.K_ESCAPE: "ESC",
        pygame.K_RETURN: "ENTER",
        pygame.K_KP_ENTER: "NUM ENTER",
        pygame.K_SPACE: "SPACE",
        pygame.K_TAB: "TAB",
        pygame.K_BACKSPACE: "BACKSPACE",
    }
    if tus_kodu in ozel:
        return ozel[tus_kodu]
    ad = pygame.key.name(int(tus_kodu)).strip()
    return ad.upper() if ad else f"KEY {tus_kodu}"


def tus_gorunen_adi(eylem):
    return tus_gorunen_adi_deger(tus_atamasi(eylem))
# </POTBO_STAGE S0193>

# <POTBO_STAGE S0195>


def tus_atamalarini_dogrula():
    global tus_atamalari
    temiz = {}
    kullanilan = set()
    for eylem, varsayilan in VARSAYILAN_TUS_ATAMALARI.items():
        aday = tus_atamalari.get(eylem, varsayilan)
        try:
            aday = int(aday)
        except (TypeError, ValueError):
            aday = varsayilan
        gecersiz = (
            aday <= 0
            or aday in AYRILMIS_ATAMA_TUSLARI
            or aday in SABIT_HIZLI_SLOT_TUSLARI
            or (aday == pygame.K_ESCAPE and eylem != "pause")
            or aday in kullanilan
        )
        if gecersiz:
            aday = varsayilan

            if aday in kullanilan:
                for alternatif in VARSAYILAN_TUS_ATAMALARI.values():
                    if (
                        alternatif not in kullanilan
                        and alternatif not in AYRILMIS_ATAMA_TUSLARI
                    ):
                        aday = alternatif
                        break
        temiz[eylem] = aday
        kullanilan.add(aday)
    tus_atamalari = temiz



son_secim_durumu = None
son_secim_imzasi = None
# </POTBO_STAGE S0195>

# <POTBO_STAGE S0198>

onemli_item_gorulenler = set()
# </POTBO_STAGE S0198>

# <POTBO_STAGE S0203>


def satir(konusmaci, metin):
    return {"speaker": konusmaci, "text": metin}


def secim(secenekler):
    return {"choices": secenekler}


def aksiyon(ad):
    return {"action": ad}


EADRIC_DINAMIK_KONUSMACI = "__EADRIC_DYNAMIC__"
# </POTBO_STAGE S0203>

# <POTBO_STAGE S0207>


def karakter_konusmaci():
    return secili_karakter_adi().upper()
# </POTBO_STAGE S0207>

# <POTBO_STAGE S0209>


def ortak_ganimet_ipucu():
    e = eadric_adi()

    return [
        satir(
            e,
            bt(
                "Taşların dili yok derler. Yalan.",
                "They say stones have no language. A lie.",
            ),
        ),
        satir(
            e,
            bt(
                "Şu sivri kayanın ardında mavi bir yudum aklı serinletir, "
                "kırmızı bir yudum eti ayağa kaldırır. Bir de birkaç sarı "
                "güneş parçası var…",
                "Behind that pointed rock, a blue draught cools the mind "
                "and a red one raises the flesh. There are also a few "
                "yellow fragments of sunlight…",
            ),
        ),
        satir(
            e,
            bt(
                "Sahipleri artık onları saymıyor.",
                "Their owners no longer count them.",
            ),
        ),
        satir(
            karakter_konusmaci(),
            bt(
                "Madem biliyorsun, neden kendin almadın?",
                "Since you know, why did you not take them yourself?",
            ),
        ),
        satir(
            e,
            bt(
                "Çünkü kayalıklar verdiklerini geri ister.",
                "Because the rocks demand back what they give.",
            ),
        ),
        satir(
            karakter_konusmaci(),
            bt("Ne demek bu?", "What does that mean?"),
        ),
        satir(
            e,
            bt(
                "Altını alırsın, sesini bırakırlar. Suyu içersin, rüyana "
                "girerler. Ben bir kez ödedim.",
                "Take the gold and they leave their voice behind. Drink "
                "the water and they enter your dreams. I paid once.",
            ),
        ),
    ]
# </POTBO_STAGE S0209>

# <POTBO_STAGE S0212>


def ilk_konusma_akisi():
    bilinmeyen = bt("İSİMSİZ ADAM", "NAMELESS MAN")

    giris = [
        satir(
            bilinmeyen,
            bt(
                "Dokuz… on… on bir… Hayır. Sen geldin, yine bozuldu.",
                "Nine… ten… eleven… No. You arrived, and it broke again.",
            ),
        )
    ]

    neyi_sayiyorsun = [
        aksiyon("eadric_tutum_merakli"),
        satir(
            bilinmeyen,
            bt(
                "Buradan geçenleri. Gidenleri saymıyorum. Gidenler bazen geri gelir.",
                "Those who pass through here. I do not count those who leave. "
                "Those who leave sometimes return.",
            ),
        ),
    ]

    sen_kimsin = [
        aksiyon("eadric_tutum_dogrudan"),
        satir(bilinmeyen, bt("Bugün mü?", "Today?")),
        satir(karakter_konusmaci(), bt("Adın.", "Your name.")),
        aksiyon("eadric_adini_ogren"),
        satir(
            eadric_adi(),
            bt(
                "Eadric. Sanırım. Biri o isimle bana borçluydu.",
                "Eadric. I think. Someone with that name owed me.",
            ),
        ),
    ]

    yolumdan_cekil = [
        aksiyon("eadric_tutum_sert"),
        satir(
            bilinmeyen,
            bt(
                "Yol senin değil. Yol, altında gömülü olanların.",
                "The road is not yours. It belongs to those buried beneath it.",
            ),
        ),
    ]

    ilk_secim = secim(
        [
            (
                bt("Neyi sayıyorsun?", "What are you counting?"),
                neyi_sayiyorsun,
            ),
            (bt("Sen kimsin?", "Who are you?"), sen_kimsin),
            (
                bt("Yolumdan çekil.", "Get out of my way."),
                yolumdan_cekil,
            ),
        ]
    )

    return (
        giris
        + [ilk_secim]
        + karakter_tanisma_bolumu()
        + [ikinci_secim_bolumu()]
        + [aksiyon("intro_tamam")]
    )
# </POTBO_STAGE S0212>

# <POTBO_STAGE S0216>


def hafif_piksellestir(kaynak, hedef_boyut=None, blok=2):
    """Görseli okunabilirliği bozmadan hafifçe pikselleştirir."""
    if kaynak is None:
        return None

    if hedef_boyut is None:
        hedef_boyut = kaynak.get_size()

    hedef_w = max(1, int(hedef_boyut[0]))
    hedef_h = max(1, int(hedef_boyut[1]))
    blok = max(1, int(blok))

    kucuk = pygame.transform.smoothscale(
        kaynak,
        (max(1, hedef_w // blok), max(1, hedef_h // blok)),
    )
    return pygame.transform.scale(kucuk, (hedef_w, hedef_h))
# </POTBO_STAGE S0216>

# <POTBO_STAGE S0218>


def saydam_kenarlari_kirp(kaynak):
    if kaynak is None:
        return None

    rect = kaynak.get_bounding_rect(min_alpha=5)

    if rect.width <= 1 or rect.height <= 1:
        return kaynak.copy()

    return kaynak.subsurface(rect).copy()
# </POTBO_STAGE S0218>

# <POTBO_STAGE S0250>


def _kareleri_ortak_canvas_yap(kareler, padding=2):
    """Animasyon boyunca piksel ölçeğini sabit tutup frame-jitter'ı önler."""
    kareler = [k for k in kareler if k is not None]
    if not kareler:
        return []

    genislik = max(k.get_width() for k in kareler) + padding * 2
    yukseklik = max(k.get_height() for k in kareler) + padding * 2
    sonuc = []

    for kare in kareler:
        canvas = pygame.Surface(
            (genislik, yukseklik), pygame.SRCALPHA, 32
        ).convert_alpha()
        hedef = kare.get_rect(midbottom=(genislik // 2, yukseklik - padding))
        canvas.blit(kare, hedef)
        sonuc.append(canvas)

    return sonuc
# </POTBO_STAGE S0250>

# <POTBO_STAGE S0252>


def _sinir_baglantili_fon_temizle(yuzey, fon_rengi, tolerans=6):
    """Yalnız çerçeveye bağlı fon piksellerini alpha=0 yapar.

    Explosion'daki siyah duman veya ground-fire'daki beyaz-sarı çekirdek gibi efektin
    kendi koyu/açık pikselleri içeride kaldığı sürece korunur; düz fon ise kenardan
    flood-fill ile sökülür. Bu yüzden basit colorkey'den daha güvenlidir.
    """
    if yuzey is None:
        return yuzey
    src = yuzey.copy().convert_alpha()
    w, h = src.get_size()
    if w <= 0 or h <= 0:
        return src
    hedef = tuple(int(v) for v in fon_rengi[:3])
    tol = max(0, int(tolerans))
    ziyaret = set()
    kuyruk = deque()

    def fon_mu(x, y):
        c = src.get_at((x, y))
        if c.a <= 1:
            return True
        return max(abs(int(c[i]) - hedef[i]) for i in range(3)) <= tol

    for x in range(w):
        if fon_mu(x, 0):
            kuyruk.append((x, 0))
        if h > 1 and fon_mu(x, h - 1):
            kuyruk.append((x, h - 1))
    for y in range(h):
        if fon_mu(0, y):
            kuyruk.append((0, y))
        if w > 1 and fon_mu(w - 1, y):
            kuyruk.append((w - 1, y))

    while kuyruk:
        x, y = kuyruk.popleft()
        if (x, y) in ziyaret or not (0 <= x < w and 0 <= y < h):
            continue
        if not fon_mu(x, y):
            continue
        ziyaret.add((x, y))
        src.set_at((x, y), (0, 0, 0, 0))
        if x > 0:
            kuyruk.append((x - 1, y))
        if x + 1 < w:
            kuyruk.append((x + 1, y))
        if y > 0:
            kuyruk.append((x, y - 1))
        if y + 1 < h:
            kuyruk.append((x, y + 1))
    return src
# </POTBO_STAGE S0252>

# <POTBO_STAGE S0256>
for _rat_row in range(4):
    for _rat_col in range(22):
        RAT_FRAME_RECTLERI.append((_rat_col * 42, 14 + _rat_row * 19, 42, 19))
# </POTBO_STAGE S0256>

# <POTBO_STAGE S0263>
_head_pickup_canvas = _kareleri_ortak_canvas_yap(_head_pickup_raw, padding=3)
_head_throw_canvas = _kareleri_ortak_canvas_yap(_head_throw_raw, padding=3)
_head_locomotion_indices = (0, 1, 2, 3, 2, 1)
_head_locomotion_canvas = [
    _head_pickup_canvas[i]
    for i in _head_locomotion_indices
    if 0 <= i < len(_head_pickup_canvas)
]
if len(_head_locomotion_canvas) < 2:
    _head_locomotion_canvas = _head_fragment_canvas
# </POTBO_STAGE S0263>

# <POTBO_STAGE S0267>


def _v28_beyaz_fon_temizle(src):
    """Beyaz/şeffaf preview fonunu kaldırıp gerçek parçayı sıkı bbox'a kırpar."""
    if src is None:
        return None
    temiz = src.copy().convert_alpha()
    w, h = temiz.get_size()
    temiz.lock()
    try:
        for y in range(h):
            for x in range(w):
                r, g, b, a = temiz.get_at((x, y))
                if a <= 8:
                    continue

                if r >= 244 and g >= 244 and b >= 244:
                    temiz.set_at((x, y), (r, g, b, 0))
    finally:
        temiz.unlock()
    bounds = temiz.get_bounding_rect(min_alpha=8)
    if bounds.width <= 0 or bounds.height <= 0:
        return None
    return temiz.subsurface(bounds).copy().convert_alpha()
# </POTBO_STAGE S0267>

# <POTBO_STAGE S0271>

_bers_walk = {}
_bers_idle = {}
# </POTBO_STAGE S0271>

# <POTBO_STAGE S0287>







def acik_arka_plani_saydam_yap(kaynak):
    if kaynak is None:
        return None

    sonuc = kaynak.copy()

    for y in range(sonuc.get_height()):
        for x in range(sonuc.get_width()):
            r, g, b, a = sonuc.get_at((x, y))

            en_buyuk = max(r, g, b)

            en_kucuk = min(r, g, b)

            acik_gri_mi = en_kucuk > 205 and en_buyuk - en_kucuk < 22

            beyaza_yakin_mi = r > 225 and g > 225 and b > 225

            if acik_gri_mi or beyaza_yakin_mi:
                sonuc.set_at((x, y), (0, 0, 0, 0))

    return sonuc


npc_resmi_temiz = acik_arka_plani_saydam_yap(npc_resmi_orijinal)
# </POTBO_STAGE S0287>

# <POTBO_STAGE S0295>


erkek_animasyonlari = animasyonlari_olustur(erkek_kareleri, "male")

kadin_animasyonlari = animasyonlari_olustur(kadin_kareleri, "female")
# </POTBO_STAGE S0295>

# <POTBO_STAGE S0297>


ERKEK_YON_ANIMASYONLARI = erkek_yon_animasyonlari()


def temiz_kareler(kareler):
    return [kare for kare in kareler if kare is not None]
# </POTBO_STAGE S0297>

# <POTBO_STAGE S0302>


def koyu_kaplama(alpha):
    kaplama = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)

    kaplama.fill((0, 0, 0, alpha))

    ekran.blit(kaplama, (0, 0))


def parlaklik_kaplamasi_ciz():
    """Parlaklık ayarını bütün ekranın son kompozitine uygular."""
    if parlaklik == 100:
        return

    kaplama = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)

    if parlaklik < 100:
        alpha = int((100 - parlaklik) / 50 * 165)
        kaplama.fill((0, 0, 0, max(0, min(190, alpha))))
    else:
        alpha = int((parlaklik - 100) / 20 * 42)
        kaplama.fill((255, 245, 238, max(0, min(55, alpha))))

    ekran.blit(kaplama, (0, 0))
# </POTBO_STAGE S0302>

# <POTBO_STAGE S0304>


def varsayilan_gotik_arka_plan():
    ekran.fill(KOYU_ARKA)

    ay = pygame.Surface((450, 450), pygame.SRCALPHA)

    for yaricap in range(205, 60, -7):
        alpha = max(2, int((210 - yaricap) * 0.16))

        pygame.draw.circle(ay, (130, 0, 20, alpha), (225, 225), yaricap)

    ekran.blit(ay, (GENISLIK // 2 - 225, -125))

    pygame.draw.rect(ekran, (8, 7, 11), (90, 335, 1100, 260))

    kuleler = [
        (65, 265, 105, 330),
        (190, 315, 95, 280),
        (1000, 305, 95, 290),
        (1120, 250, 100, 345),
    ]

    for x, y, w, h in kuleler:
        pygame.draw.rect(ekran, (8, 7, 11), (x, y, w, h))

        pygame.draw.polygon(
            ekran,
            (8, 7, 11),
            [
                (x - 12, y),
                (x + w // 2, y - 100),
                (x + w + 12, y),
            ],
        )

    pygame.draw.rect(ekran, (6, 5, 8), (0, 575, GENISLIK, 145))

    zaman = 0 if az_hareket else pygame.time.get_ticks() / 1000

    sis = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)

    for i in range(5):
        x = int(-250 + ((zaman * (16 + i * 3) + i * 310) % 1700))

        pygame.draw.ellipse(sis, (105, 95, 115, 12), (x, 485 + i * 34, 620, 95))

    ekran.blit(sis, (0, 0))
# </POTBO_STAGE S0304>

# <POTBO_STAGE S0307>
ekran_olustur()






def dosya_adi_temizle(metin):
    temiz = metin.strip()

    temiz = re.sub(r"[^a-zA-Z0-9ğüşöçıİĞÜŞÖÇ _-]", "", temiz)

    temiz = temiz.replace(" ", "_")

    return temiz[:24]
# </POTBO_STAGE S0307>

# <POTBO_STAGE S0309>


def item_alindi_bildirimi(item_adi, adet=1):
    bildirim_goster(f"{item_adi} {max(1, int(adet))}x", BEYAZ, BEYAZ, "item")
# </POTBO_STAGE S0309>

# <POTBO_STAGE S0312>


def oyun_sinematik_kilitli_mi():
    """Item prelüdü/kartı sırasında dünya simülasyonunu güvenli biçimde dondurur."""
    return bool(onemli_item_penceresi_acik_mi() or onemli_item_gorsel_hazir_zamani > 0)
# </POTBO_STAGE S0312>

# <POTBO_STAGE S0314>


LEVEL_RENK_PALETI = [
    (224, 196, 96),
    (92, 196, 126),
    (92, 154, 224),
    (173, 105, 211),
    (214, 52, 72),
]


def level_rengi(level):
    """1–9 beyaz; her onluk eşikte renk değişir ve 50'de kan kırmızısına ulaşır."""
    level = max(1, min(MAKSIMUM_LEVEL, int(level)))
    if level < 10:
        return BEYAZ

    onluk_index = min(len(LEVEL_RENK_PALETI) - 1, level // 10 - 1)
    return LEVEL_RENK_PALETI[onluk_index]


LEVEL_BALANCE_VERSION = 1
# </POTBO_STAGE S0314>

# <POTBO_STAGE S0316>


def seviye_atladi_bildirimi(level):
    global seviye_anim_level, seviye_anim_baslangic
    seviye_anim_level = int(level)
    seviye_anim_baslangic = pygame.time.get_ticks()
# </POTBO_STAGE S0316>

# <POTBO_STAGE S0327>


def resmi_oranli_sigdir(
    kaynak,
    hedef_rect,
    kenar_boslugu=8,
    yakinlastirma=1.0,
    pikselli=False,
):
    """
    Görseli oranını bozmadan hedef kutuya sığdırır.
    Görsel hiçbir yönden kutunun dışına taşmaz.
    """

    if kaynak is None:
        return None

    kullanilabilir_genislik = max(1, hedef_rect.width - kenar_boslugu * 2)

    kullanilabilir_yukseklik = max(1, hedef_rect.height - kenar_boslugu * 2)

    oran_x = kullanilabilir_genislik / kaynak.get_width()

    oran_y = kullanilabilir_yukseklik / kaynak.get_height()

    olcek = min(oran_x, oran_y)




    olcek *= max(1.0, yakinlastirma)

    yeni_genislik = max(1, int(kaynak.get_width() * olcek))

    yeni_yukseklik = max(1, int(kaynak.get_height() * olcek))

    hedef_boyut = (yeni_genislik, yeni_yukseklik)
    if pikselli:
        return hafif_piksellestir(kaynak, hedef_boyut, 2)

    return pygame.transform.smoothscale(kaynak, hedef_boyut)


def resmi_oranli_doldur(kaynak, hedef_rect):
    """
    Görseli oranını bozmadan hedef alanın tamamını kaplayacak ölçekte
    büyütür. Taşan bölüm clip veya subsurface ile güvenle kesilebilir.
    """
    if kaynak is None:
        return None

    oran_x = hedef_rect.width / max(1, kaynak.get_width())
    oran_y = hedef_rect.height / max(1, kaynak.get_height())
    olcek = max(oran_x, oran_y)

    yeni_genislik = max(1, int(round(kaynak.get_width() * olcek)))
    yeni_yukseklik = max(1, int(round(kaynak.get_height() * olcek)))

    return pygame.transform.smoothscale(kaynak, (yeni_genislik, yeni_yukseklik))







def karakter_secenekleri():
    return ["male", "female"]
# </POTBO_STAGE S0327>

# <POTBO_STAGE S0330>


def bonus_degistir(ozellik, miktar):
    global bonus_guc
    global bonus_can
    global bonus_mana
    global bonus_kalan

    if miktar > 0 and bonus_kalan <= 0:
        return

    if ozellik == "strength":
        if miktar < 0 and bonus_guc <= 0:
            return

        bonus_guc += miktar

    elif ozellik == "health":
        if miktar < 0 and bonus_can <= 0:
            return

        bonus_can += miktar

    elif ozellik == "mana":
        if miktar < 0 and bonus_mana <= 0:
            return

        bonus_mana += miktar

    bonus_kalan -= miktar
# </POTBO_STAGE S0330>

# <POTBO_STAGE S0345>


def aurum_potabile_olustur():
    kategori = bt("SİMYASAL İKSİR", "ALCHEMICAL POTION")
    return {
        "id": "aurum_potabile",
        "name": "Aurum Potabile",
        "category": kategori,
        "type": kategori,
        "important": True,
        "description": bt(
            "Saf altının uzun süreli çözündürme, damıtma ve yeniden "
            "yoğunlaştırma işlemleriyle hazırlanmış tıbbi bir özüdür. "
            "Simyacılar, çürümeye dirençli altının yetkinliğinin bu "
            "sıvıda bedene aktarılabileceğini; kanı kuvvetlendirerek "
            "dokuların doğal dengesini yeniden kuracağını düşünürler.",
            "A medicinal essence prepared by repeatedly dissolving, "
            "distilling and condensing pure gold. Alchemists believe the "
            "incorruptibility of gold can pass into the body through this "
            "liquid, strengthening the blood and restoring the natural "
            "balance of the tissues.",
        ),
        "heal": 55,
    }


def quinta_essentia_olustur():
    kategori = bt("SİMYASAL İKSİR", "ALCHEMICAL POTION")
    return {
        "id": "quinta_essentia",
        "name": "Quinta Essentia",
        "category": kategori,
        "type": kategori,
        "important": True,
        "description": bt(
            "Dört unsurdan bağımsız olduğu kabul edilen beşinci cevherin, "
            "tekrar tekrar damıtılarak maddeden ayrıştırılmış hâlidir. "
            "Bedeni değil, yaşamı harekete geçiren görünmez kuvveti "
            "beslediği ve büyüsel tükenmeyi giderdiği söylenir.",
            "The fifth essence, believed to exist independently of the "
            "four elements, separated from matter through repeated "
            "distillation. It is said to nourish the invisible force that "
            "animates life and to relieve magical exhaustion.",
        ),
        "mana": 40,
    }


def eadric_tasi_olustur():
    kategori = bt("GÖREV EŞYASI", "QUEST ITEM")
    return {
        "id": "eadric_stone",
        "name": bt("Eadric’in Taşı", "Eadric's Stone"),
        "category": kategori,
        "type": kategori,
        "important": True,
        "description": bt(
            "Eadric’in kayalıklardan uzattığı, zaman zaman ısındığı "
            "söylenen uğursuz taş. İki kez ısınırsa ateşe atılması, "
            "üç kez ısınırsa kaçılması gerektiğini söyledi.",
            "An ominous stone Eadric offered from among the rocks, said to "
            "warm at times. He said to cast it into the fire if it warms "
            "twice, and to run if it warms three times.",
        ),
    }
# </POTBO_STAGE S0345>

# <POTBO_STAGE S0347>


def onemli_item_kazanimi_ekle(item):
    """Her önemli eşyanın tanıtım kartını kayıt başına yalnızca bir kez kuyruğa alır."""
    if not isinstance(item, dict) or not item.get("important", False):
        return

    item_id = str(item.get("id", "")).strip()
    if not item_id or item_id in onemli_item_gorulenler:
        return

    onemli_item_gorulenler.add(item_id)
    onemli_item_kuyrugu.append(dict(item))
# </POTBO_STAGE S0347>

# <POTBO_STAGE S0350>


def onemli_item_penceresi_acik_mi():
    return bool(onemli_item_gosterim_aktif and onemli_item_kuyrugu)


def onemli_item_on_sunum_bekliyor_mu():
    return bool(onemli_item_kuyrugu and onemli_item_gorsel_hazir_zamani > 0)


def onemli_item_girdisi_hazir_mi():
    return (
        onemli_item_penceresi_acik_mi()
        and pygame.time.get_ticks() - onemli_item_acilis_zamani
        >= ONEMLI_ITEM_GIRIS_KILIDI
    )
# </POTBO_STAGE S0350>

# <POTBO_STAGE S0352>


def item_adedi(item):
    if not isinstance(item, dict):
        return 0
    try:
        return max(1, min(10, int(item.get("quantity", 1))))
    except (TypeError, ValueError):
        return 1
# </POTBO_STAGE S0352>

# <POTBO_STAGE S0356>


def can_iksiri_olustur():
    kategori = bt("TÜKETİLEBİLİR İKSİR", "CONSUMABLE POTION")
    return {
        "id": "health_potion",
        "name": ("Can İksiri" if dil == "TR" else "Health Potion"),
        "category": kategori,
        "type": kategori,
        "important": False,
        "description": (
            "Kullanıldığında 30 can yeniler. "
            "Geliştirici testlerinde kullanılabilen sıradan bir iyileştirme eşyasıdır."
            if dil == "TR"
            else "Restores 30 health when used. "
            "A standard healing item available for developer testing."
        ),
        "heal": 30,
    }
# </POTBO_STAGE S0356>

# <POTBO_STAGE S0364>


def q_hizli_slotu_temizle():
    global q_hizli_item_index
    q_hizli_item_index = None
    bildirim_goster(bt("Q hızlı slotu temizlendi.", "Q quick slot cleared."))
# </POTBO_STAGE S0364>

# <POTBO_STAGE S0377>


def _olcekli_polygon(noktalar):
    return [_olcekli_nokta(x, y) for x, y in noktalar]
# </POTBO_STAGE S0377>

# <POTBO_STAGE S0379>


def nokta_polygon_icinde_mi(nokta, polygon):
    """
    Ray-casting yöntemiyle noktanın polygon içinde olup olmadığını bulur.
    """

    x, y = nokta
    icerde = False

    j = len(polygon) - 1

    for i in range(len(polygon)):
        xi, yi = polygon[i]
        xj, yj = polygon[j]

        kesiyor = (yi > y) != (yj > y)

        if kesiyor:
            payda = yj - yi

            if payda == 0:
                payda = 0.000001

            sinir_x = (xj - xi) * (y - yi) / payda + xi

            if x < sinir_x:
                icerde = not icerde

        j = i

    return icerde
# </POTBO_STAGE S0379>

# <POTBO_STAGE S0412>


_v30_olum_koreografi_hazirla = _stage1__v30_olum_koreografi_hazirla
# </POTBO_STAGE S0412>

# <POTBO_STAGE S0414>


_v30_ozel_olum_ilk_efekti = _stage1__v30_ozel_olum_ilk_efekti
# </POTBO_STAGE S0414>

# <POTBO_STAGE S0417>


_v30_olum_koreografi_guncelle = _stage1__v30_olum_koreografi_guncelle
# </POTBO_STAGE S0417>

# <POTBO_STAGE S0419>


_v30_katil_koreografi_frame = _stage1__v30_katil_koreografi_frame
# </POTBO_STAGE S0419>

# <POTBO_STAGE S0428>


def _kapsul_rect_kesisiyor(rect, baslangic, bitis, yaricap):
    """Bir doğru parçasının kalınlaştırılmış (capsule) hali rect'e değiyor mu?

    Rect'i yarıçap kadar inflate edip segment clipping yapmak hızlı ve kararlı bir
    Minkowski yaklaşımıdır. Tek-frame sword hitbox'larının oyuncunun arasından
    tünellemesini ciddi biçimde azaltır.
    """
    r = rect.inflate(int(round(yaricap * 2.0)), int(round(yaricap * 2.0)))
    a = (int(round(baslangic.x)), int(round(baslangic.y)))
    b = (int(round(bitis.x)), int(round(bitis.y)))
    return bool(r.clipline(a, b)) or r.collidepoint(a) or r.collidepoint(b)
# </POTBO_STAGE S0428>

# <POTBO_STAGE S0430>


def _rect_en_yakin_nokta(rect, nokta):
    return pygame.Vector2(
        max(
            float(rect.left),
            min(float(rect.right), float(nokta.x)),
        ),
        max(
            float(rect.top),
            min(float(rect.bottom), float(nokta.y)),
        ),
    )
# </POTBO_STAGE S0430>

# <POTBO_STAGE S0434>


def _vektor_uzunluk_sinirla(vektor, maksimum):
    uzunluk = vektor.length()
    if uzunluk > maksimum > 0.0:
        return vektor * (maksimum / uzunluk)
    return vektor


def _vektor_dondur(vektor, derece):
    if vektor.length_squared() <= 0.000001:
        return pygame.Vector2(0.0, 0.0)
    return vektor.rotate(float(derece))
# </POTBO_STAGE S0434>

# <POTBO_STAGE S0436>


def _yonelim(a, b, c):
    deger = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    if abs(deger) < 1e-8:
        return 0
    return 1 if deger > 0 else -1


def _nokta_segment_uzerinde_mi(a, b, p):
    if _yonelim(a, b, p) != 0:
        return False
    return (
        min(a[0], b[0]) - 1e-6 <= p[0] <= max(a[0], b[0]) + 1e-6
        and min(a[1], b[1]) - 1e-6 <= p[1] <= max(a[1], b[1]) + 1e-6
    )


def _segmentler_kesisiyor_mu(a, b, c, d):
    o1 = _yonelim(a, b, c)
    o2 = _yonelim(a, b, d)
    o3 = _yonelim(c, d, a)
    o4 = _yonelim(c, d, b)
    if o1 != o2 and o3 != o4:
        return True
    if o1 == 0 and _nokta_segment_uzerinde_mi(a, b, c):
        return True
    if o2 == 0 and _nokta_segment_uzerinde_mi(a, b, d):
        return True
    if o3 == 0 and _nokta_segment_uzerinde_mi(c, d, a):
        return True
    if o4 == 0 and _nokta_segment_uzerinde_mi(c, d, b):
        return True
    return False
# </POTBO_STAGE S0436>

# <POTBO_STAGE S0440>

FIRE_AI_SCAN_MS = 92
FIRE_AI_GROUND_HARD_MARGIN = 13.0
FIRE_AI_PROJECTILE_CORRIDOR_MARGIN = 12.0
# </POTBO_STAGE S0440>

# <POTBO_STAGE S0451>


def _yon_vektoru(yon):
    if yon == "left":
        return pygame.Vector2(-1.0, 0.0)
    if yon == "right":
        return pygame.Vector2(1.0, 0.0)
    if yon == "up":
        return pygame.Vector2(0.0, -1.0)
    return pygame.Vector2(0.0, 1.0)
# </POTBO_STAGE S0451>

# <POTBO_STAGE S0456>


def _fire_ground_target_cooldown_key(hedef):
    if hedef is None:
        return "player"
    return "enemy:" + str(getattr(hedef, "uid", getattr(hedef, "tur", id(hedef))))
# </POTBO_STAGE S0456>

# <POTBO_STAGE S0459>


def _v27_alpha_merkez_rect(img, merkez_x, merkez_y):
    """Geometrik canvas değil görünür alpha kütlesini dünya merkezine sabitler."""
    bounds = img.get_bounding_rect()
    if bounds.width <= 0 or bounds.height <= 0:
        return img.get_rect(center=(int(round(merkez_x)), int(round(merkez_y))))
    ofx = (img.get_width() * 0.5) - bounds.centerx
    ofy = (img.get_height() * 0.5) - bounds.centery
    return img.get_rect(
        center=(
            int(round(merkez_x + ofx)),
            int(round(merkez_y + ofy)),
        )
    )
# </POTBO_STAGE S0459>

# <POTBO_STAGE S0468>


def oyundan_cikis_onay_ciz():
    standart_onay_penceresi_ciz(
        t("pause_exit_confirm"),
        oyundan_cikis_onay_index,
        "oyun",
    )
# </POTBO_STAGE S0468>

# <POTBO_STAGE S0473>


def ayar_secenekleri():
    kategoriler = ayar_kategorileri()
    guvenli_index = max(0, min(len(kategoriler) - 1, ayar_kategori_index))
    return kategoriler[guvenli_index][1]
# </POTBO_STAGE S0473>

# <POTBO_STAGE S0475>


def acik_kapali(deger):
    return t("on") if deger else t("off")
# </POTBO_STAGE S0475>

# <POTBO_STAGE S0479>


def ayar_scrollunu_guncelle(secenek_sayisi, gorunen_adet=5):
    """Seçim görünür pencerenin altına gelmeden scroll etmez; orta-sabitleme hatasını kaldırır."""
    global ayar_scroll_baslangic
    if secenek_sayisi <= gorunen_adet:
        ayar_scroll_baslangic = 0
        return 0

    maksimum = max(0, secenek_sayisi - gorunen_adet)
    if ayar_index < ayar_scroll_baslangic:
        ayar_scroll_baslangic = ayar_index
    elif ayar_index >= ayar_scroll_baslangic + gorunen_adet:
        ayar_scroll_baslangic = ayar_index - gorunen_adet + 1

    ayar_scroll_baslangic = max(0, min(maksimum, ayar_scroll_baslangic))
    return ayar_scroll_baslangic
# </POTBO_STAGE S0479>

# <POTBO_STAGE S0483>


def dongulu_deger(degerler, mevcut, yon):
    index = degerler.index(mevcut)
    return degerler[(index + yon) % len(degerler)]


def secili_ayar_anahtari():
    secenekler = ayar_secenekleri()
    if not secenekler:
        return None
    return secenekler[max(0, min(len(secenekler) - 1, ayar_index))]
# </POTBO_STAGE S0483>

# <POTBO_STAGE S0485>


def tus_atama_uygula(yeni_tus):
    global tus_atama_bekleniyor, tus_atama_mesaji, tus_atama_mesaj_bitis
    eylem = tus_atama_bekleniyor
    if eylem is None:
        return False

    if yeni_tus == pygame.K_BACKSPACE:
        tus_atama_bekleniyor = None
        tus_atama_mesaji = ""
        return False

    if yeni_tus == pygame.K_ESCAPE and eylem != "pause":
        tus_atama_bekleniyor = None
        tus_atama_mesaji = ""
        return False

    if yeni_tus in AYRILMIS_ATAMA_TUSLARI or yeni_tus in SABIT_HIZLI_SLOT_TUSLARI:
        tus_atama_mesaji = bt(
            "Bu tuş sistem tarafından ayrılmış.",
            "That key is reserved by the system.",
        )
        tus_atama_mesaj_bitis = pygame.time.get_ticks() + 1800
        return False

    eski_tus = tus_atamasi(eylem)
    diger = next(
        (ad for ad, kod in tus_atamalari.items() if ad != eylem and kod == yeni_tus),
        None,
    )
    if diger is not None:
        tus_atamalari[diger] = eski_tus
    tus_atamalari[eylem] = int(yeni_tus)
    tus_atama_bekleniyor = None
    tus_atama_mesaji = bt("Tuş ataması güncellendi.", "Key binding updated.")
    tus_atama_mesaj_bitis = pygame.time.get_ticks() + 1400
    ayarlari_kaydet()
    button_click_sesi_cal("menu1")
    return True
# </POTBO_STAGE S0485>

# <POTBO_STAGE S0502>


def _kesik_cizgi_ciz(
    yuzey,
    merkez,
    aci_deg,
    uzunluk,
    kalinlik,
    renk,
    alpha,
    kaydir=0.0,
):
    """Tapered görünümlü, keskin bir kılıç izi. Daire/halo üretmez."""
    aci = math.radians(float(aci_deg))
    yon = pygame.Vector2(math.cos(aci), math.sin(aci))
    dik = pygame.Vector2(-yon.y, yon.x)
    c = pygame.Vector2(merkez) + dik * float(kaydir)
    half = float(uzunluk) * 0.5

    noktalar = [
        c - yon * half,
        c - yon * half * 0.22,
        c + yon * half * 0.38,
        c + yon * half,
    ]
    widths = [
        max(1, int(kalinlik * 0.42)),
        max(1, int(kalinlik)),
        max(1, int(kalinlik * 0.52)),
    ]
    rgba = (*renk[:3], max(0, min(255, int(alpha))))
    for i in range(3):
        pygame.draw.line(yuzey, rgba, noktalar[i], noktalar[i + 1], widths[i])
# </POTBO_STAGE S0502>

# <POTBO_STAGE S0516>


def _v24_olum_katilini_ciz():
    actor = _v24_olum_katil_actor_bul()
    if actor is None:
        return None
    sil, rect = _v24_katil_siluet_surface_ve_rect(actor)
    if sil is None or rect is None:
        return actor
    ekran.blit(sil, rect)
    _v24_katil_silah_kanini_ciz(actor)
    return actor
# </POTBO_STAGE S0516>

# <POTBO_STAGE S0518>


def _v30_surface_bolge_sil(src, points):
    out = src.copy()
    mask = pygame.Surface(out.get_size(), pygame.SRCALPHA)
    mask.fill((255, 255, 255, 255))
    pygame.draw.polygon(mask, (255, 255, 255, 0), points)
    out.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    return out
# </POTBO_STAGE S0518>

# <POTBO_STAGE S0522>


_v30_patlama_birinci_katman_siluet_ciz = _stage1__v30_patlama_birinci_katman_siluet_ciz
# </POTBO_STAGE S0522>

# <POTBO_STAGE S0551>


def _vektor_hedefe_yaklastir(mevcut, hedef, maksimum_delta):
    fark = hedef - mevcut
    uzunluk = fark.length()
    if uzunluk <= maksimum_delta or uzunluk <= 1e-6:
        return pygame.Vector2(hedef)
    return mevcut + fark * (maksimum_delta / uzunluk)
# </POTBO_STAGE S0551>

# <POTBO_STAGE S0555>
V32_OLUM_KATIL_LAST_UPDATE_MS = 0
V32_OLUM_KATIL_CONTACT = False
# </POTBO_STAGE S0555>

# <POTBO_STAGE S0558>
_v31_katil_koreografi_frame = _v30_katil_koreografi_frame
# </POTBO_STAGE S0558>

# <POTBO_STAGE S0563>


def _v32_koreografi_gecen(simdi=None):
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if V32_OLUM_KATIL_READY_MS <= 0:
        return -1
    return max(0, int(simdi) - int(V32_OLUM_KATIL_READY_MS))
# </POTBO_STAGE S0563>

# <POTBO_STAGE S0565>


_v30_olum_koreografi_guncelle = _stage2__v30_olum_koreografi_guncelle
# </POTBO_STAGE S0565>

# <POTBO_STAGE S0567>


_v30_katil_koreografi_frame = _stage2__v30_katil_koreografi_frame


def _v32_tirtikli_polygon(w, h, cx, cy, rx, ry, rng, nokta=13):
    pts = []
    faz = rng.uniform(-0.18, 0.18)
    for i in range(max(8, int(nokta))):
        a = faz + math.tau * i / float(max(8, int(nokta)))
        radial = rng.uniform(0.68, 1.26)

        radial *= (
            1.0
            + 0.10 * math.sin(a * 3.0 + faz * 7.0)
            + 0.07 * math.sin(a * 5.0 - faz * 11.0)
        )
        x = cx + math.cos(a) * rx * radial
        y = cy + math.sin(a) * ry * radial
        pts.append(
            (
                int(max(0, min(w - 1, round(x)))),
                int(max(0, min(h - 1, round(y)))),
            )
        )
    return pts


def _v32_tirtikli_kopar(body, rng, cxr, cyr, rxr, ryr):
    w, h = body.get_size()
    cx, cy = w * float(cxr), h * float(cyr)
    pts = _v32_tirtikli_polygon(
        w,
        h,
        cx,
        cy,
        max(2.0, w * float(rxr)),
        max(2.0, h * float(ryr)),
        rng,
        nokta=rng.randint(10, 15),
    )
    maske = pygame.Surface((w, h), pygame.SRCALPHA)
    pygame.draw.polygon(maske, (255, 255, 255, 255), pts)
    parca = body.copy()
    parca.blit(maske, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    inv = pygame.Surface((w, h), pygame.SRCALPHA)
    inv.fill((255, 255, 255, 255))
    pygame.draw.polygon(inv, (255, 255, 255, 0), pts)
    kalan = body.copy()
    kalan.blit(inv, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    return (
        kalan,
        parca,
        pygame.Vector2(cx - w * 0.5, cy - h * 0.5),
    )
# </POTBO_STAGE S0567>

# <POTBO_STAGE S0569>


_v32_tirtikli_ceset_ciz = _stage1__v32_tirtikli_ceset_ciz
# </POTBO_STAGE S0569>

# <POTBO_STAGE S0573>


_v32_patlama_siluet_parcalari_ciz = _stage1__v32_patlama_siluet_parcalari_ciz
# </POTBO_STAGE S0573>

# <POTBO_STAGE S0594>


def _v33_full_piece_ciz(
    full_piece,
    extra_offset=(0.0, 0.0),
    extra_rot=0.0,
    simdi=None,
):
    crop, local = _v33_alpha_crop(full_piece)
    if crop is None:
        return
    _, _, angle, center = _v33_corpse_pose(simdi)


    local_rot = local.rotate(-angle)
    target = center + local_rot + pygame.Vector2(extra_offset)
    draw = pygame.transform.rotate(crop, angle + float(extra_rot))
    ekran.blit(
        draw,
        draw.get_rect(center=(int(round(target.x)), int(round(target.y)))),
    )
# </POTBO_STAGE S0594>

# <POTBO_STAGE S0596>



def _v32_tirtikli_ceset_ciz(mod="generic"):
    return _v33_tirtikli_ceset_ciz(mod)
# </POTBO_STAGE S0596>

# <POTBO_STAGE S0605>
V34_DEATH_TITLE_FADE_MS = 1800
# </POTBO_STAGE S0605>

# <POTBO_STAGE S0609>


def _v34_smoothstep01(v):
    p = max(0.0, min(1.0, float(v)))
    return p * p * (3.0 - 2.0 * p)
# </POTBO_STAGE S0609>

# <POTBO_STAGE S0619>


calisiyor = True
# </POTBO_STAGE S0619>

# <POTBO_STAGE S0622>
V34_DYNAMIC_ESCAPE_EPSILON = 1.0
V34_STATIC_ESCAPE_SAMPLE_EPSILON = 0
V34_SCRIPT_STEP = 3.0
V34_UNSTUCK_SEARCH_RADII = (
    4,
    8,
    12,
    18,
    24,
    32,
    42,
    54,
    68,
    84,
)
V34_UNSTUCK_ANGLES = tuple(range(0, 360, 15))
V34_SPECIAL_MIN_RADIUS = 68.0
V34_SPECIAL_RADIUS_STEPS = (
    116.0,
    108.0,
    100.0,
    92.0,
    84.0,
    76.0,
    68.0,
)
V34_SPECIAL_ENTRY_OVERSHOOT = 70.0
V34_SPECIAL_TRAIL_MAX = 30
# </POTBO_STAGE S0622>

# <POTBO_STAGE S0625>
V34_SPECIAL_FLASH_MS = (74, 92, 124)
V34_SPECIAL_IMPACT_RING_MS = 360
V34_SPECIAL_RECOVERY_GRACE_MS = 170
V34_SPECIAL_TARGET_LOCK_EXTRA_MS = 90
V34_SPECIAL_FIRST_TWO_HITS_NONLETHAL = True
V34_SPECIAL_CINEMA_BAR_MAX = 18
# </POTBO_STAGE S0625>

# <POTBO_STAGE S0627>
v34_last_safety_check_ms = pygame.time.get_ticks()
# </POTBO_STAGE S0627>

# <POTBO_STAGE S0629>
v34_special_locked_center = None
v34_special_effect_center = None
# </POTBO_STAGE S0629>

# <POTBO_STAGE S0632>
v34_special_trail = deque(maxlen=V34_SPECIAL_TRAIL_MAX)
# </POTBO_STAGE S0632>

# <POTBO_STAGE S0635>
v34_special_flash_until = 0
v34_special_flash_started = 0
v34_special_flash_strength = 0.0
v34_special_impact_ring_until = 0
v34_special_impact_ring_started = 0
v34_special_hit_display_until = 0
v34_special_hit_display_index = 0
v34_special_finish_pulse_until = 0
v34_special_finish_pulse_started = 0
v34_special_move_serial = 0
v34_special_exit_safe_pos = None
# </POTBO_STAGE S0635>

# <POTBO_STAGE S0637>
v34_special_recovery_grace_until = 0
# </POTBO_STAGE S0637>

# <POTBO_STAGE S0642>


def _v34_rect_overlap_alani(a, b):
    """İki pygame.Rect'in gerçek overlap alanını döndürür."""
    if not a.colliderect(b):
        return 0
    inter = a.clip(b)
    return max(0, int(inter.width)) * max(0, int(inter.height))
# </POTBO_STAGE S0642>

# <POTBO_STAGE S0651>


def _v34_polyline_static_clear(points, step=V34_SCRIPT_STEP):
    if not points:
        return False
    for i in range(len(points) - 1):
        if not _v34_segment_static_clear(points[i], points[i + 1], step=step):
            return False
    return True


def _v34_bezier_points(a, control, b, count=18):
    a = pygame.Vector2(a)
    control = pygame.Vector2(control)
    b = pygame.Vector2(b)
    pts = []
    for i in range(max(2, int(count)) + 1):
        t = i / max(2, int(count))
        inv = 1.0 - t
        pts.append(a * (inv * inv) + control * (2.0 * inv * t) + b * (t * t))
    return pts


def _v34_curve_static_clear(a, control, b):
    return _v34_polyline_static_clear(_v34_bezier_points(a, control, b), step=4.0)


def _v34_find_nearest_static_safe(desired, origin=None, max_radius=84.0):
    """Scripted endpoint'i yakın çevredeki en benzer geçerli world noktasına taşır."""
    desired = pygame.Vector2(desired)
    if _v34_static_position_valid(desired.x, desired.y):
        return desired

    if origin is None:
        origin = desired
    origin = pygame.Vector2(origin)
    best = None
    best_score = float("inf")
    for radius in V34_UNSTUCK_SEARCH_RADII:
        if radius > max_radius:
            break
        for angle in V34_UNSTUCK_ANGLES:
            v = pygame.Vector2(radius, 0.0).rotate(angle)
            candidate = desired + v
            if not _v34_static_position_valid(candidate.x, candidate.y):
                continue
            score = (
                candidate.distance_to(desired) + candidate.distance_to(origin) * 0.06
            )
            if score < best_score:
                best_score = score
                best = candidate
        if best is not None:
            return best
    return None
# </POTBO_STAGE S0651>

# <POTBO_STAGE S0660>


def _v34_special_hit_feedback(slot, center, direction):
    global \
        v34_special_flash_until, \
        v34_special_flash_started, \
        v34_special_flash_strength
    global v34_special_impact_ring_until, v34_special_impact_ring_started
    global v34_special_hit_display_until, v34_special_hit_display_index
    global v34_special_finish_pulse_until, v34_special_finish_pulse_started

    simdi = pygame.time.get_ticks()
    slot = max(0, min(2, int(slot)))
    flash_ms = V34_SPECIAL_FLASH_MS[slot]
    v34_special_flash_started = simdi
    v34_special_flash_until = simdi + flash_ms
    v34_special_flash_strength = (0.28, 0.42, 0.62)[slot]
    v34_special_impact_ring_started = simdi
    v34_special_impact_ring_until = simdi + V34_SPECIAL_IMPACT_RING_MS
    v34_special_hit_display_index = slot + 1
    v34_special_hit_display_until = simdi + 520
    if slot == 2:
        v34_special_finish_pulse_started = simdi
        v34_special_finish_pulse_until = simdi + 520
# </POTBO_STAGE S0660>

# <POTBO_STAGE S0668>


def _v34_special_screen_flash_ciz(simdi):
    if simdi >= v34_special_flash_until:
        return
    duration = max(1, v34_special_flash_until - v34_special_flash_started)
    t = max(
        0.0,
        min(1.0, (simdi - v34_special_flash_started) / duration),
    )
    alpha = int(255 * v34_special_flash_strength * (1.0 - t) ** 2)
    overlay = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    overlay.fill((255, 242, 245, alpha))
    ekran.blit(overlay, (0, 0))
# </POTBO_STAGE S0668>

# <POTBO_STAGE S0674>





_v33_oyun_ekrani_ciz = oyun_ekrani_ciz
# </POTBO_STAGE S0674>

# <POTBO_STAGE S0680>
V34_FX_BUDGET_CHECK_MS = 650
# </POTBO_STAGE S0680>

# <POTBO_STAGE S0683>
V34_MAX_ROCK_IMPACTS = 72
# </POTBO_STAGE S0683>

# <POTBO_STAGE S0685>
V34_MAX_GROUND_FIRES = 120
# </POTBO_STAGE S0685>

# <POTBO_STAGE S0687>
v34_input_buffer_last_tick = pygame.time.get_ticks()
v34_special_pause_started_ms = 0
v34_special_pause_was_gameplay = True
v34_fx_budget_last_check = pygame.time.get_ticks()
# </POTBO_STAGE S0687>

# <POTBO_STAGE S0695>





def _v34_trim_oldest_in_place(seq, maximum):
    excess = len(seq) - int(maximum)
    if excess <= 0:
        return 0
    del seq[:excess]
    return excess
# </POTBO_STAGE S0695>

# <POTBO_STAGE S0698>





def v34_quality_tick():
    """Her frame çağrılan düşük maliyetli kalite orchestrator'ı."""
    v34_special_pause_tick()
    v34_input_buffer_guncelle()
    v34_fx_budget_guncelle()
# </POTBO_STAGE S0698>

# <POTBO_STAGE S0700>
V34_CROWD_SEPARATION_INTERVAL_MS = 42
V34_CROWD_MIN_OVERLAP_RATIO = 0.20
# </POTBO_STAGE S0700>

# <POTBO_STAGE S0702>
V34_CROWD_PAIR_PUSH = 2.8
V34_CROWD_MAX_PAIRS_PER_TICK = 18
# </POTBO_STAGE S0702>

# <POTBO_STAGE S0704>
v34_crowd_last_tick = pygame.time.get_ticks()
# </POTBO_STAGE S0704>

# <POTBO_STAGE S0706>
v34_crowd_pair_separations = 0
# </POTBO_STAGE S0706>

# <POTBO_STAGE S0718>





_v34c_oyun_ekrani_ciz = oyun_ekrani_ciz
# </POTBO_STAGE S0718>

# <POTBO_STAGE S0720>





_v34c_quality_tick = v34_quality_tick
# </POTBO_STAGE S0720>

# <POTBO_STAGE S0723>


_v34c_oyun_ekrani_ciz_diag = oyun_ekrani_ciz


def oyun_ekrani_ciz():
    _v34c_oyun_ekrani_ciz_diag()
    _v34_diagnostics_overlay_ciz()
# </POTBO_STAGE S0723>

# <POTBO_STAGE S0725>
V34_WATCHDOG_INTERVAL_MS = 120
V34_THREAT_MAX_INDICATORS = 3
# </POTBO_STAGE S0725>

# <POTBO_STAGE S0727>
V34_THREAT_EDGE_MARGIN = 34
V34_THREAT_MIN_AGGRO_AGE_MS = 150
V34_TARGET_PREVIEW_RADIUS = 30
V34_TARGET_PREVIEW_MAX_ALPHA = 150
V34_FINITE_COORD_LIMIT = 100000.0
V34_STALE_SPECIAL_CLEANUP_MS = 600
# </POTBO_STAGE S0727>

# <POTBO_STAGE S0729>
v34_watchdog_last_tick = pygame.time.get_ticks()
v34_watchdog_fix_count = 0
v34_watchdog_last_fix = ""
v34_special_target_preview_cache = None
v34_special_target_preview_cache_ms = 0
v34_threat_indicator_cache = []
v34_threat_indicator_cache_ms = 0
v34_focus_lost_since = 0
v34_focus_recovery_count = 0
# </POTBO_STAGE S0729>

# <POTBO_STAGE S0733>


def _v34_line_to_screen_edge(direction, margin=V34_THREAT_EDGE_MARGIN):
    """Ekran merkezinden çıkan direction ray'ini güvenli UI dikdörtgenine keser."""
    d = pygame.Vector2(direction)
    if d.length_squared() <= 1e-6:
        d = pygame.Vector2(1.0, 0.0)
    d = d.normalize()
    center = pygame.Vector2(GENISLIK * 0.5, YUKSEKLIK * 0.5)
    left = float(margin)
    right = float(GENISLIK - margin)
    top = float(margin)
    bottom = float(YUKSEKLIK - margin)
    ts = []
    if abs(d.x) > 1e-6:
        ts.extend([(left - center.x) / d.x, (right - center.x) / d.x])
    if abs(d.y) > 1e-6:
        ts.extend([(top - center.y) / d.y, (bottom - center.y) / d.y])
    valid = []
    for tval in ts:
        if tval <= 0:
            continue
        p = center + d * tval
        if left - 0.5 <= p.x <= right + 0.5 and top - 0.5 <= p.y <= bottom + 0.5:
            valid.append((tval, p))
    if not valid:
        return center
    valid.sort(key=lambda x: x[0])
    return valid[0][1]
# </POTBO_STAGE S0733>

# <POTBO_STAGE S0735>


def _v34_value_is_finite(value):
    try:
        value = float(value)
    except (TypeError, ValueError):
        return False
    return math.isfinite(value) and abs(value) <= V34_FINITE_COORD_LIMIT


def _v34_watchdog_note(message):
    global v34_watchdog_fix_count, v34_watchdog_last_fix
    v34_watchdog_fix_count += 1
    v34_watchdog_last_fix = str(message)
    debug_log("V34 watchdog:", message)
# </POTBO_STAGE S0735>

# <POTBO_STAGE S0740>


_v34d_quality_tick = v34_quality_tick


def v34_quality_tick():
    _v34d_quality_tick()
    v34_state_watchdog_tick()


_v34d_oyun_ekrani_ciz = oyun_ekrani_ciz
# </POTBO_STAGE S0740>

# <POTBO_STAGE S0743>
V34_INTERACTION_GRACE = 1.12
V34_INTERACTION_CACHE_MS = 70
V34_FX_QUALITY_SAMPLE_MS = 900
V34_FX_QUALITY_LOW_FPS = 47.0
V34_FX_QUALITY_CRITICAL_FPS = 36.0
V34_FX_QUALITY_RECOVER_FPS = 56.0
V34_FX_QUALITY_MIN = 0.46
V34_FX_QUALITY_RECOVER_STEP = 0.10
V34_FX_QUALITY_DROP_STEP = 0.16

v34_special_armor_saves = 0
v34_interaction_target_cache = None
v34_interaction_target_cache_ms = 0
v34_interaction_error_count = 0
v34_fx_quality = 1.0
v34_fx_quality_last_sample = pygame.time.get_ticks()
v34_fx_quality_last_fps = float(FPS)
v34_fx_quality_drop_count = 0
v34_fx_quality_recover_count = 0
# </POTBO_STAGE S0743>

# <POTBO_STAGE S0746>


def _v34_interaction_candidate(kind, obj, x, y, score, action):
    return {
        "kind": str(kind),
        "obj": obj,
        "x": float(x),
        "y": float(y),
        "score": float(score),
        "action": action,
    }
# </POTBO_STAGE S0746>

# <POTBO_STAGE S0748>


def v34_interaction_target():
    global v34_interaction_target_cache, v34_interaction_target_cache_ms
    simdi = pygame.time.get_ticks()
    cached = v34_interaction_target_cache
    if (
        simdi - v34_interaction_target_cache_ms < V34_INTERACTION_CACHE_MS
        and cached is not None
    ):
        return cached
    v34_interaction_target_cache_ms = simdi
    candidates = _v34_interaction_candidates()
    v34_interaction_target_cache = candidates[0] if candidates else None
    return v34_interaction_target_cache
# </POTBO_STAGE S0748>

# <POTBO_STAGE S0751>


def v34_fx_quality_tick():
    global v34_fx_quality, v34_fx_quality_last_sample, v34_fx_quality_last_fps
    global v34_fx_quality_drop_count, v34_fx_quality_recover_count
    simdi = pygame.time.get_ticks()
    if simdi - v34_fx_quality_last_sample < V34_FX_QUALITY_SAMPLE_MS:
        return
    v34_fx_quality_last_sample = simdi
    try:
        fps = float(saat.get_fps())
    except Exception:
        fps = float(FPS)
    if fps <= 1.0:
        return
    v34_fx_quality_last_fps = fps

    old = v34_fx_quality
    if az_hareket:
        target = 0.52
        v34_fx_quality += (target - v34_fx_quality) * 0.50
    elif fps < V34_FX_QUALITY_CRITICAL_FPS:
        v34_fx_quality = max(
            V34_FX_QUALITY_MIN,
            v34_fx_quality - V34_FX_QUALITY_DROP_STEP * 1.6,
        )
    elif fps < V34_FX_QUALITY_LOW_FPS:
        v34_fx_quality = max(
            V34_FX_QUALITY_MIN,
            v34_fx_quality - V34_FX_QUALITY_DROP_STEP,
        )
    elif fps >= V34_FX_QUALITY_RECOVER_FPS:
        v34_fx_quality = min(1.0, v34_fx_quality + V34_FX_QUALITY_RECOVER_STEP)

    if v34_fx_quality < old - 0.01:
        v34_fx_quality_drop_count += 1
    elif v34_fx_quality > old + 0.01:
        v34_fx_quality_recover_count += 1


def _v34_fx_stride(base=1):
    quality = max(V34_FX_QUALITY_MIN, min(1.0, float(v34_fx_quality)))
    if quality >= 0.90:
        return max(1, int(base))
    if quality >= 0.70:
        return max(1, int(base) + 1)
    return max(2, int(base) + 2)
# </POTBO_STAGE S0751>

# <POTBO_STAGE S0755>


_v34e_quality_tick = v34_quality_tick


def v34_quality_tick():
    _v34e_quality_tick()
    v34_fx_quality_tick()


_v34e_oyun_ekrani_ciz = oyun_ekrani_ciz
# </POTBO_STAGE S0755>

# <POTBO_STAGE S0759>
V34F_CORRUPT_SUFFIX = ".corrupt"
V34F_AUDIT_INTERVAL_MS = 1100
V34F_FRAME_SPIKE_MS = 43.0
V34F_FRAME_SPIKE_WINDOW = 90
V34F_MAX_ISSUES = 48
V34F_SPECIAL_TARGET_MAX_DRIFT = 18.0
V34F_SPECIAL_TARGET_SNAP_SPEED = 0.72
V34F_SPECIAL_ECHO_LIFE_MS = 940
V34F_SPECIAL_ECHO_STRONG_MS = 260
V34F_SPECIAL_SPARK_LIFE_MS = (150, 220, 310)
V34F_SPECIAL_SPARK_COUNTS = (10, 16, 25)
V34F_SPECIAL_LANDING_LIFE_MS = 430
V34F_SPECIAL_VIGNETTE_MAX_ALPHA = 72
V34F_SPECIAL_FINAL_CUT_MS = 125
V34F_SPECIAL_FINAL_CUT_ALPHA = 84
# </POTBO_STAGE S0759>

# <POTBO_STAGE S0761>
V34F_SPECIAL_TARGET_LOCK_PAD_MS = 120
V34F_FOCUS_DEBOUNCE_MS = 80
# </POTBO_STAGE S0761>

# <POTBO_STAGE S0763>
V34F_RESOURCE_OVERFLOW_FACTOR = 1.25
# </POTBO_STAGE S0763>

# <POTBO_STAGE S0765>
V34F_STATIC_RECOVERY_COOLDOWN_MS = 600
V34F_DIAGNOSTIC_SAMPLE_MS = 500
# </POTBO_STAGE S0765>

# <POTBO_STAGE S0767>
v34f_corrupt_file_count = 0
# </POTBO_STAGE S0767>

# <POTBO_STAGE S0769>
v34f_last_restore_error = ""
v34f_last_audit_ms = 0
v34f_audit_count = 0
v34f_audit_fix_count = 0
v34f_audit_last_ok = True
v34f_audit_last_summary = {}
v34f_issues = deque(maxlen=V34F_MAX_ISSUES)
v34f_issue_counts = {}
v34f_frame_times_ms = deque(maxlen=V34F_FRAME_SPIKE_WINDOW)
v34f_frame_spike_count = 0
v34f_last_frame_probe_ms = pygame.time.get_ticks()
v34f_last_diagnostic_ms = 0
v34f_last_focus = True
v34f_focus_lost_ms = 0
v34f_focus_regained_ms = 0
v34f_focus_loss_count = 0
v34f_special_was_active = False
v34f_special_started_seen = False
v34f_special_finished_ms = 0
v34f_special_last_center = None
v34f_special_last_exit = None
v34f_special_last_final_direction = pygame.Vector2(1.0, 0.0)
v34f_special_target_anchor = None
# </POTBO_STAGE S0769>

# <POTBO_STAGE S0771>
v34f_special_target_snap_count = 0
v34f_special_input_quarantine_frames = 0
# </POTBO_STAGE S0771>

# <POTBO_STAGE S0773>
v34f_special_final_cut_started = 0
v34f_special_final_cut_until = 0
v34f_special_echoes = deque(maxlen=12)
v34f_special_sparks = deque(maxlen=160)
v34f_special_landing_marks = deque(maxlen=18)
v34f_special_hit_positions = [None, None, None]
v34f_special_hit_times = [0, 0, 0]
v34f_special_hit_directions = [pygame.Vector2(1.0, 0.0) for _ in range(3)]
v34f_special_last_serial_seen = -1
v34f_special_checked_serials = set()
v34f_post_special_recovery_until = 0
v34f_static_recovery_last_ms = 0
v34f_static_recovery_count = 0
v34f_runtime_started_ms = pygame.time.get_ticks()





def _v34f_now():
    return int(pygame.time.get_ticks())


def _v34f_finite(value, fallback=0.0):
    try:
        value = float(value)
    except (TypeError, ValueError, OverflowError):
        return float(fallback)
    if not math.isfinite(value):
        return float(fallback)
    return value


def _v34f_clamp(value, lo, hi):
    value = _v34f_finite(value, lo)
    return max(float(lo), min(float(hi), value))


def _v34f_vector(value, fallback=(0.0, 0.0)):
    try:
        v = pygame.Vector2(value)
    except Exception:
        v = pygame.Vector2(fallback)
    if not math.isfinite(v.x) or not math.isfinite(v.y):
        v = pygame.Vector2(fallback)
    return v
# </POTBO_STAGE S0773>

# <POTBO_STAGE S0775>


def _v34f_report_issue(code, detail="", fixed=False, severity="warning"):
    """Normal oyuncuya toast basmadan bounded diagnostic event üretir."""
    global v34f_audit_fix_count
    code = str(code or "unknown")
    detail = str(detail or "")[:260]
    severity = str(severity or "warning")
    event = {
        "time": _v34f_now(),
        "code": code,
        "detail": detail,
        "fixed": bool(fixed),
        "severity": severity,
    }
    v34f_issues.append(event)
    v34f_issue_counts[code] = int(v34f_issue_counts.get(code, 0)) + 1
    if fixed:
        v34f_audit_fix_count += 1
    if DEBUG_LOGS:
        debug_log(
            "V34F",
            severity,
            code,
            detail,
            "fixed=" + str(bool(fixed)),
        )
    return event


def _v34f_is_plain_json_object(payload):
    return isinstance(payload, dict)
# </POTBO_STAGE S0775>

# <POTBO_STAGE S0777>


def _v34f_write_bytes_atomic(path, raw):
    path = os.path.abspath(path)
    directory = os.path.dirname(path) or BASE_DIR
    os.makedirs(directory, exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "wb") as f:
        f.write(raw)
        f.flush()
        try:
            os.fsync(f.fileno())
        except OSError:
            pass
    os.replace(tmp, path)
# </POTBO_STAGE S0777>

# <POTBO_STAGE S0785>


def _v34f_special_target_alive(target):
    if target is None:
        return False
    try:
        return int(getattr(target, "hp", 0)) > 0
    except Exception:
        return False
# </POTBO_STAGE S0785>

# <POTBO_STAGE S0787>





def _v34f_direction_safe(direction, fallback=(1.0, 0.0)):
    d = _v34f_vector(direction, fallback)
    if d.length_squared() <= 1e-6:
        d = pygame.Vector2(fallback)
    if d.length_squared() <= 1e-6:
        d = pygame.Vector2(1.0, 0.0)
    return d.normalize()


def _v34f_spawn_hit_sparks(slot, center, direction, simdi):
    center = pygame.Vector2(center)
    d = _v34f_direction_safe(direction)
    n = pygame.Vector2(-d.y, d.x)
    count = V34F_SPECIAL_SPARK_COUNTS[max(0, min(2, slot))]
    quality = max(V34_FX_QUALITY_MIN, min(1.0, float(v34_fx_quality)))
    count = max(5, int(round(count * quality)))
    seed = (int(simdi) * 17) ^ (v34_special_move_serial * 7919) ^ (slot * 101)
    rng = random.Random(seed)
    life = V34F_SPECIAL_SPARK_LIFE_MS[slot]
    for i in range(count):
        forward = rng.uniform(26.0, 82.0) * (1.0 + slot * 0.12)
        side = rng.uniform(-64.0, 64.0) * (0.62 + slot * 0.18)
        velocity = d * forward + n * side
        start = center + n * rng.uniform(-10.0, 10.0) - d * rng.uniform(0.0, 6.0)
        spark_life = int(life * rng.uniform(0.72, 1.18))
        length = rng.uniform(5.0, 13.0) * (1.0 + slot * 0.18)
        v34f_special_sparks.append(
            (
                int(simdi),
                start,
                velocity,
                spark_life,
                length,
                slot,
            )
        )


def _v34f_add_special_echo(slot, center, direction, simdi):
    center = pygame.Vector2(center)
    direction = _v34f_direction_safe(direction)
    v34f_special_echoes.append(
        (
            int(simdi),
            slot,
            center,
            direction,
            float(v34_special_effect_radius),
        )
    )


def _v34f_add_landing_mark(center, direction, simdi):
    center = pygame.Vector2(center)
    direction = _v34f_direction_safe(direction)
    normal = pygame.Vector2(-direction.y, direction.x)
    seed = int(simdi) ^ (v34_special_move_serial * 31337)
    rng = random.Random(seed)
    for i in range(8):
        offset = normal * rng.uniform(-18.0, 18.0) - direction * rng.uniform(2.0, 18.0)
        velocity = -direction * rng.uniform(12.0, 38.0) + normal * rng.uniform(
            -24.0, 24.0
        )
        v34f_special_landing_marks.append(
            (
                int(simdi),
                center + offset,
                velocity,
                rng.uniform(2.0, 5.0),
            )
        )


_v34f_previous_special_hit_feedback = _v34_special_hit_feedback
# </POTBO_STAGE S0787>

# <POTBO_STAGE S0799>


def _v34f_special_master_vfx_ciz():
    simdi = _v34f_now()
    layer = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    _v34f_draw_echoes(layer, simdi)
    _v34f_draw_sparks(layer, simdi)
    _v34f_draw_landing(layer, simdi)
    ekran.blit(layer, (0, 0))
    _v34f_special_vignette_ciz(simdi)
    _v34f_final_cut_flash_ciz(simdi)


_v34f_previous_game_draw = oyun_ekrani_ciz
# </POTBO_STAGE S0799>

# <POTBO_STAGE S0805>





def v34f_frame_health_tick():
    global v34f_last_frame_probe_ms, v34f_frame_spike_count
    simdi = _v34f_now()
    delta = simdi - int(v34f_last_frame_probe_ms)
    v34f_last_frame_probe_ms = simdi
    if delta <= 0 or delta > 1000:
        return
    v34f_frame_times_ms.append(float(delta))
    if delta >= V34F_FRAME_SPIKE_MS:
        v34f_frame_spike_count += 1


def _v34f_frame_percentile(percent=0.95):
    if not v34f_frame_times_ms:
        return 0.0
    values = sorted(v34f_frame_times_ms)
    p = max(0.0, min(1.0, float(percent)))
    index = int(round((len(values) - 1) * p))
    return float(values[index])
# </POTBO_STAGE S0805>

# <POTBO_STAGE S0808>





def _v34f_special_completion_check():
    """Tamamlanan move normal durumda 3 hit üretmeli; QA için sessiz assertion yerine event."""
    if v34f_special_finished_ms <= 0:
        return

    serial = int(v34_special_move_serial)
    if serial in v34f_special_checked_serials:
        return
    times = list(v34f_special_hit_times)
    count = sum(1 for value in times if int(value) > 0)
    if count == 3 and times[0] <= times[1] <= times[2]:
        v34f_special_checked_serials.add(serial)
        return

    if v34f_special_started_seen:
        _v34f_report_issue(
            "special_incomplete_hits",
            f"serial={serial},count={count}",
            False,
            "error",
        )
        v34f_special_checked_serials.add(serial)
# </POTBO_STAGE S0808>

# <POTBO_STAGE S0810>





_v34f_previous_quality_tick = v34_quality_tick


def v34_quality_tick():
    _v34f_previous_quality_tick()
    v34f_frame_health_tick()
    v34f_focus_safety_tick()
    v34f_special_lifecycle_tick()
    _v34f_post_special_control_tick()
    v34f_runtime_audit_tick(False)
# </POTBO_STAGE S0810>

# <POTBO_STAGE S0812>


V34F_STARTUP_OK = _v34f_startup_self_check()
# </POTBO_STAGE S0812>

# <POTBO_STAGE S0818>
V34_SPECIAL_RADIUS_STEPS = (
    132.0,
    124.0,
    116.0,
    108.0,
    100.0,
    92.0,
    84.0,
    76.0,
    68.0,
)
V34_SPECIAL_ENTRY_OVERSHOOT = 90.0
# </POTBO_STAGE S0818>

# <POTBO_STAGE S0820>
V34_SPECIAL_FLASH_MS = (58, 76, 112)
V34_SPECIAL_IMPACT_RING_MS = 300
V34_SPECIAL_RECOVERY_GRACE_MS = 125
V34_SPECIAL_TARGET_LOCK_EXTRA_MS = 72


V34F_SPECIAL_ECHO_LIFE_MS = 820
V34F_SPECIAL_ECHO_STRONG_MS = 230
V34F_SPECIAL_SPARK_LIFE_MS = (135, 190, 265)
V34F_SPECIAL_SPARK_COUNTS = (14, 23, 38)
V34F_SPECIAL_FINAL_CUT_MS = 118
V34F_SPECIAL_FINAL_CUT_ALPHA = 118
# </POTBO_STAGE S0820>

# <POTBO_STAGE S0826>





V35_HEAVY_ASSIST_RANGE = 240.0
V35_HEAVY_ASSIST_MAX_LATERAL = 72.0
V35_HEAVY_ASSIST_BLEND = 0.26
# </POTBO_STAGE S0826>

# <POTBO_STAGE S0832>
V35_FLOW_WINDOW_MS = 1550
V35_FLOW_DECAY_STEP_MS = 620
# </POTBO_STAGE S0832>

# <POTBO_STAGE S0834>
v35_flow_last_hit_ms = 0
v35_flow_last_decay_ms = 0
v35_flow_pulse_until = 0
v35_flow_best = 0.0
v35_flow_hits = 0
# </POTBO_STAGE S0834>

# <POTBO_STAGE S0838>





def _v34_special_phase_values(p):
    """V35: 1.66 saniyede üç net fiziksel hit ve çok kısa impact holds."""
    return {
        "entry_end": 0.170,
        "hit1_hold_end": 0.202,
        "setup_end": 0.275,
        "slash1_end": 0.372,
        "hit2_hold_end": 0.410,
        "switch_end": 0.480,
        "slash2_end": 0.575,
        "hit3_hold_end": 0.625,
        "settle_end": 0.705,
    }





V35_INTENT_MAX_RANGE = 245.0
V35_INTENT_ALPHA = 88
# </POTBO_STAGE S0838>

# <POTBO_STAGE S0846>


_v35_game_draw_original = oyun_ekrani_ciz
# </POTBO_STAGE S0846>

# <POTBO_STAGE S0848>





_v35_quality_tick_original = v34_quality_tick
# </POTBO_STAGE S0848>

# <POTBO_STAGE S0851>



V35_SPECIAL_PHASE_OK, V35_SPECIAL_PHASE_DETAIL = _v34f_special_phase_contract()
# </POTBO_STAGE S0851>

# <POTBO_STAGE S0854>
V34F_SPECIAL_SPARK_COUNTS = (5, 8, 12)
V34F_SPECIAL_SPARK_LIFE_MS = (105, 145, 190)
V34F_SPECIAL_ECHO_LIFE_MS = 560
V34F_SPECIAL_ECHO_STRONG_MS = 165
V34F_SPECIAL_LANDING_LIFE_MS = 280
V34F_SPECIAL_FINAL_CUT_MS = 82
V34F_SPECIAL_FINAL_CUT_ALPHA = 96



v34_special_trail = deque(list(v34_special_trail)[-18:], maxlen=18)
# </POTBO_STAGE S0854>

# <POTBO_STAGE S0856>
v34f_special_sparks = deque(list(v34f_special_sparks)[-48:], maxlen=48)
v34f_special_echoes = deque(list(v34f_special_echoes)[-8:], maxlen=8)
v34f_special_landing_marks = deque(list(v34f_special_landing_marks)[-10:], maxlen=10)

v36_special_last_trail_ms = 0
# </POTBO_STAGE S0856>

# <POTBO_STAGE S0858>


def _v36_clip_rect_around_screen(center, half_w=250, half_h=205):
    cx, cy = int(round(center.x)), int(round(center.y))
    x0 = max(0, cx - int(half_w))
    y0 = max(0, cy - int(half_h))
    x1 = min(GENISLIK, cx + int(half_w))
    y1 = min(YUKSEKLIK, cy + int(half_h))
    if x1 <= x0 or y1 <= y0:
        return None
    return pygame.Rect(x0, y0, x1 - x0, y1 - y0)
# </POTBO_STAGE S0858>

# <POTBO_STAGE S0861>


def _v36_draw_slash_local(layer, rect, a, b, progress, alpha, final=False):
    if progress <= 0.0 or alpha <= 0:
        return
    sa = _v36_screen_local(pygame.Vector2(a), rect, -12.0)
    sb_full = _v36_screen_local(pygame.Vector2(b), rect, -12.0)
    sb = sa.lerp(sb_full, progress)
    p0 = (int(sa.x), int(sa.y))
    p1 = (int(sb.x), int(sb.y))
    pygame.draw.line(
        layer,
        (126, 6, 24, int(alpha * 0.48)),
        p0,
        p1,
        10 if final else 8,
    )
    pygame.draw.line(
        layer,
        (235, 30, 56, int(alpha * 0.78)),
        p0,
        p1,
        5 if final else 4,
    )
    pygame.draw.line(layer, (255, 241, 244, alpha), p0, p1, 1)
# </POTBO_STAGE S0861>

# <POTBO_STAGE S0871>


_v37_tus_girdisi_kabul_original = tus_girdisi_kabul
# </POTBO_STAGE S0871>

# <POTBO_STAGE S0886>







v37_dark_overlay = pygame.Surface(
    (GENISLIK, YUKSEKLIK), pygame.SRCALPHA
).convert_alpha()
v37_settings_grid = pygame.Surface(
    (GENISLIK, YUKSEKLIK), pygame.SRCALPHA
).convert_alpha()
v37_settings_grid.fill((0, 0, 0, 0))
V37_IMPACT_LAYER_SIZE = 300
v37_impact_layer = pygame.Surface(
    (V37_IMPACT_LAYER_SIZE, V37_IMPACT_LAYER_SIZE),
    pygame.SRCALPHA,
).convert_alpha()
# </POTBO_STAGE S0886>

# <POTBO_STAGE S0888>
for _x in range(0, GENISLIK, 32):
    pygame.draw.line(
        v37_settings_grid,
        (120, 0, 24, 10),
        (_x, 0),
        (_x, YUKSEKLIK),
        1,
    )
for _y in range(0, YUKSEKLIK, 32):
    pygame.draw.line(
        v37_settings_grid,
        (120, 0, 24, 8),
        (0, _y),
        (GENISLIK, _y),
        1,
    )

v37_vignette_cache = {}
v37_brightness_surface = pygame.Surface(
    (GENISLIK, YUKSEKLIK), pygame.SRCALPHA
).convert_alpha()
v37_brightness_key = None


def koyu_kaplama(alpha):
    alpha = max(0, min(255, int(alpha)))
    v37_dark_overlay.fill((0, 0, 0, alpha))
    ekran.blit(v37_dark_overlay, (0, 0))
# </POTBO_STAGE S0888>

# <POTBO_STAGE S0890>


def _v37_cached_vignette(bucket):
    bucket = max(0, min(6, int(bucket)))
    if bucket in v37_vignette_cache:
        return v37_vignette_cache[bucket]

    v37_vignette_cache.clear()
    tension = bucket / 6.0
    surf = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA).convert_alpha()
    layers = 46
    for i in range(layers):
        q = 1.0 - i / max(1.0, float(layers))
        alpha = int((2.7 + tension * 1.4) * q * q)
        if alpha <= 0:
            continue
        pygame.draw.rect(
            surf,
            (0, 0, 0, alpha),
            (i, i, GENISLIK - i * 2, YUKSEKLIK - i * 2),
            1,
        )
    if tension > 0.05:
        edge_alpha = int(10 + 9 * tension)
        edge = 18
        pygame.draw.rect(
            surf,
            (108, 0, 18, edge_alpha),
            (0, 0, GENISLIK, edge),
        )
        pygame.draw.rect(
            surf,
            (108, 0, 18, edge_alpha),
            (0, YUKSEKLIK - edge, GENISLIK, edge),
        )
        pygame.draw.rect(
            surf,
            (108, 0, 18, edge_alpha),
            (0, 0, edge, YUKSEKLIK),
        )
        pygame.draw.rect(
            surf,
            (108, 0, 18, edge_alpha),
            (GENISLIK - edge, 0, edge, YUKSEKLIK),
        )
    v37_vignette_cache[bucket] = surf
    return surf
# </POTBO_STAGE S0890>

# <POTBO_STAGE S0892>


def parlaklik_kaplamasi_ciz():
    global v37_brightness_key
    if parlaklik == 100:
        return
    key = int(parlaklik)
    if v37_brightness_key != key:
        if parlaklik < 100:
            alpha = int((100 - parlaklik) / 50 * 165)
            v37_brightness_surface.fill((0, 0, 0, max(0, min(190, alpha))))
        else:
            alpha = int((parlaklik - 100) / 20 * 42)
            v37_brightness_surface.fill((255, 245, 238, max(0, min(55, alpha))))
        v37_brightness_key = key
    ekran.blit(v37_brightness_surface, (0, 0))
# </POTBO_STAGE S0892>

# <POTBO_STAGE S0899>





V37_SPECIAL_STATIC_SANITY_MS = 120
V37_SPECIAL_PREFLIGHT_STEP = 5.5
V37_SPECIAL_PREFLIGHT_CURVE_SAMPLES = 10

V34_SPECIAL_RADIUS_STEPS = (132.0, 116.0, 100.0, 84.0, 68.0)
V37_SPECIAL_TRAIL_INTERVAL_MS = 54
V37_SPECIAL_TRAIL_LIFE_MS = 145
V37_SPECIAL_AFTERGLOW_MS = 170
V37_SPECIAL_MAX_SPARKS = (2, 3, 4)
V37_SPECIAL_AI_RECOVERY_MS = 130



V34_FX_BUDGET_CHECK_MS = 300
# </POTBO_STAGE S0899>

# <POTBO_STAGE S0902>
V34_MAX_ROCK_IMPACTS = 40
# </POTBO_STAGE S0902>

# <POTBO_STAGE S0904>
V34_MAX_GROUND_FIRES = 56
# </POTBO_STAGE S0904>

# <POTBO_STAGE S0907>
V34F_SPECIAL_SPARK_COUNTS = V37_SPECIAL_MAX_SPARKS
V34F_SPECIAL_SPARK_LIFE_MS = (70, 90, 115)
V34F_SPECIAL_ECHO_LIFE_MS = 180
V34F_SPECIAL_ECHO_STRONG_MS = 90
V34F_SPECIAL_LANDING_LIFE_MS = 0
V34F_SPECIAL_FINAL_CUT_MS = 62
V34F_SPECIAL_FINAL_CUT_ALPHA = 88

v34_special_trail = deque(maxlen=6)
# </POTBO_STAGE S0907>

# <POTBO_STAGE S0909>
v34f_special_sparks = deque(maxlen=12)
v34f_special_echoes = deque(maxlen=2)
v34f_special_landing_marks = deque(maxlen=0)

v37_special_last_trail_ms = -10000
v37_special_last_static_sanity_ms = -10000
v37_special_previous_active = False
v37_special_ai_pause_frames = 0
# </POTBO_STAGE S0909>

# <POTBO_STAGE S0912>


V37_SPECIAL_LAYER_SIZE = (400, 350)
v37_special_layer = pygame.Surface(
    V37_SPECIAL_LAYER_SIZE, pygame.SRCALPHA
).convert_alpha()
# </POTBO_STAGE S0912>

# <POTBO_STAGE S0916>


def _v37_curve_static_clear(a, control, b):
    a = pygame.Vector2(a)
    control = pygame.Vector2(control)
    b = pygame.Vector2(b)
    count = max(4, int(V37_SPECIAL_PREFLIGHT_CURVE_SAMPLES))
    for i in range(count + 1):
        t = i / count
        omt = 1.0 - t
        p = a * (omt * omt) + control * (2.0 * omt * t) + b * (t * t)
        if not _v34_static_position_valid(p.x, p.y):
            return False
    return True
# </POTBO_STAGE S0916>

# <POTBO_STAGE S0918>


_v37_special_scripted_position_apply_slow = _v34_special_scripted_position_apply
# </POTBO_STAGE S0918>

# <POTBO_STAGE S0920>


def _v34_special_register_trail(simdi, pos, phase="move"):
    global v37_special_last_trail_ms
    simdi = int(simdi)
    if (
        simdi - v37_special_last_trail_ms < V37_SPECIAL_TRAIL_INTERVAL_MS
        and v34_special_trail
    ):
        return
    v37_special_last_trail_ms = simdi
    v34_special_trail.append((simdi, pygame.Vector2(pos), str(phase)))


def _v34f_spawn_hit_sparks(slot, center, direction, simdi):
    slot = max(0, min(2, int(slot)))
    center = pygame.Vector2(center)
    d = _v34f_direction_safe(direction)
    n = pygame.Vector2(-d.y, d.x)
    count = V37_SPECIAL_MAX_SPARKS[slot]
    for i in range(count):
        sign = -1.0 if i % 2 == 0 else 1.0
        spread = (0.25 + 0.18 * i) * sign
        velocity = d.rotate(spread * 42.0) * (58.0 + slot * 16.0 + i * 8.0)
        start = center + n * sign * (3.0 + i * 2.0)
        life = V34F_SPECIAL_SPARK_LIFE_MS[slot]
        v34f_special_sparks.append(
            (
                int(simdi),
                start,
                velocity,
                life,
                7.0 + slot * 2.0,
                slot,
            )
        )


def _v34f_add_special_echo(slot, center, direction, simdi):

    return


def _v34f_add_landing_mark(center, direction, simdi):
    return


def _v37_draw_special_sparks(layer, rect, now):
    alive = []
    for born, start, velocity, life, length, slot in list(v34f_special_sparks):
        age = now - int(born)
        if age < 0 or age >= int(life):
            continue
        alive.append((born, start, velocity, life, length, slot))
        t = age / max(1.0, float(life))
        world = pygame.Vector2(start) + pygame.Vector2(velocity) * (age / 1000.0)
        d = _v34f_direction_safe(velocity)
        tail = world - d * float(length) * (1.0 - 0.3 * t)
        a = _v36_screen_local(world, rect, -14.0)
        b = _v36_screen_local(tail, rect, -14.0)
        alpha = int((160 + int(slot) * 22) * (1.0 - t))
        pygame.draw.line(layer, (255, 236, 240, alpha), a, b, 1)
    v34f_special_sparks.clear()
    v34f_special_sparks.extend(alive)
# </POTBO_STAGE S0920>

# <POTBO_STAGE S0922>


def _v34f_special_master_vfx_ciz():

    return


def _v35_special_signature_ciz():

    return
# </POTBO_STAGE S0922>

# <POTBO_STAGE S0927>


_v37_fx_budget_original = v34_fx_budget_guncelle


def v34_fx_budget_guncelle():
    return _v37_fx_budget_original()


_v37_crowd_separation_original = v34_crowd_separation_tick
# </POTBO_STAGE S0927>

# <POTBO_STAGE S0929>


_v37_state_watchdog_original = v34_state_watchdog_tick
# </POTBO_STAGE S0929>

# <POTBO_STAGE S0931>


_v37_runtime_audit_original = v34f_runtime_audit_tick
# </POTBO_STAGE S0931>

# <POTBO_STAGE S0937>
v38_impact_pause = True
# </POTBO_STAGE S0937>

# <POTBO_STAGE S0941>


_v38_settings_bootstrap()
# </POTBO_STAGE S0941>

# <POTBO_STAGE S0943>


_v38_ayar_kategorileri_original = ayar_kategorileri
_v38_ayar_aciklamasi_original = ayar_aciklamasi
_v38_ayar_etiketi_original = ayar_etiketi
_v38_ayar_degeri_original = ayar_degeri
_v38_ayari_degistir_original = ayari_degistir
# </POTBO_STAGE S0943>

# <POTBO_STAGE S0945>







V38_FIRE_AIR_TEMPERATURE_K = 293.15
V38_FIRE_CORE_TEMPERATURE_K = 1880.0
V38_FIRE_MIN_VISIBLE_TEMPERATURE_K = 780.0
V38_FIRE_THERMAL_COOLING_K = 0.42


V38_FIRE_PROJECTILE_V0 = 900.0
V38_FIRE_PROJECTILE_VINF = 760.0
V38_FIRE_PROJECTILE_DRAG_K = 1.18
V38_FIRE_PROJECTILE_MAX_TRAVEL = 1180.0
V38_FIRE_PROJECTILE_TTL_MS = 1650
V38_FIRE_PROJECTILE_RADIUS = 17.0
# </POTBO_STAGE S0945>

# <POTBO_STAGE S0947>
V38_FIRE_PROJECTILE_ARM_DISTANCE = 72.0
# </POTBO_STAGE S0947>

# <POTBO_STAGE S0950>


V38_FIRE_PRESSURE_SIGMA = 68.0
V38_FIRE_THERMAL_R50 = 104.0
# </POTBO_STAGE S0950>

# <POTBO_STAGE S0952>
V38_FIRE_THERMAL_RADIUS = 176.0
V38_FIRE_KNOCKBACK_BASE = 920.0
V38_FIRE_BURN_BASE = 104.0
# </POTBO_STAGE S0952>

# <POTBO_STAGE S0955>
V38_FIRE_SELF_KNOCKBACK_RADIUS = 138.0
# </POTBO_STAGE S0955>

# <POTBO_STAGE S0957>
V38_FIRE_SELF_BURN_RADIUS = 86.0
V38_FIRE_SELF_BURN_SCALE = 0.22
# </POTBO_STAGE S0957>

# <POTBO_STAGE S0960>





def _v38_clamp01(x):
    return max(0.0, min(1.0, float(x)))


def _v38_smoothstep(x):
    t = _v38_clamp01(x)
    return t * t * (3.0 - 2.0 * t)


def _v38_smootherstep(x):
    t = _v38_clamp01(x)
    return t * t * t * (t * (t * 6.0 - 15.0) + 10.0)


def _v38_sigmoid01(x, sharpness=8.0):
    """Normalize edilmiş lojistik eğri; 0 ve 1 uçlarını tam uçlara map eder."""
    t = _v38_clamp01(x)
    k = max(0.1, float(sharpness))
    lo = 1.0 / (1.0 + math.exp(k * 0.5))
    hi = 1.0 / (1.0 + math.exp(-k * 0.5))
    y = 1.0 / (1.0 + math.exp(-k * (t - 0.5)))
    return _v38_clamp01((y - lo) / max(1e-9, hi - lo))


def _v38_pressure_field(distance):
    d = max(0.0, float(distance))
    s = max(1.0, float(V38_FIRE_PRESSURE_SIGMA))
    return math.exp(-((d / s) ** 2))


def _v38_thermal_field(distance):
    d = max(0.0, float(distance))
    r = max(1.0, float(V38_FIRE_THERMAL_R50))
    return 1.0 / (1.0 + (d / r) ** 4)


def _v38_projectile_speed(age_s):
    t = max(0.0, float(age_s))
    return V38_FIRE_PROJECTILE_VINF + (
        V38_FIRE_PROJECTILE_V0 - V38_FIRE_PROJECTILE_VINF
    ) * math.exp(-V38_FIRE_PROJECTILE_DRAG_K * t)


def _v38_projectile_temperature(age_s):
    t = max(0.0, float(age_s))
    return V38_FIRE_AIR_TEMPERATURE_K + (
        V38_FIRE_CORE_TEMPERATURE_K - V38_FIRE_AIR_TEMPERATURE_K
    ) * math.exp(-V38_FIRE_THERMAL_COOLING_K * t)


def _v38_blackbody_visual_intensity(temp_k):
    """Stefan-Boltzmann T^4 bağıntısının normalize edilmiş oyun karşılığı.

    Gerçek W/m² hesaplamıyoruz; yalnız core temperature değişiminin parlaklıkta doğrusal
    değil kuvvetli okunmasını koruyoruz. Reference = initial core temperature.
    """
    t = max(V38_FIRE_AIR_TEMPERATURE_K, float(temp_k))
    ref = max(t, V38_FIRE_CORE_TEMPERATURE_K)
    ratio = (t / ref) ** 4
    return _v38_clamp01(ratio)


def _v38_effective_distance(center, target_pos, target_radius):
    geometric = pygame.Vector2(center).distance_to(pygame.Vector2(target_pos))


    return max(0.0, geometric - max(0.0, float(target_radius)) * 0.42), geometric
# </POTBO_STAGE S0960>

# <POTBO_STAGE S0964>


def _v38_burn_total_at(distance, exposure=1.0):
    if not gelistirici_yanma_efekti_aktif:
        return 0
    d = max(0.0, float(distance))
    if d > V38_FIRE_THERMAL_RADIUS:
        return 0
    h = _v38_thermal_field(d) * (0.20 + 0.80 * _v38_clamp01(exposure))
    raw = V38_FIRE_BURN_BASE * (h**1.30)
    return int(round(raw)) if raw >= 6.0 else 0
# </POTBO_STAGE S0964>

# <POTBO_STAGE S0968>
v38_fire_glow_cache = {}
v38_fire_explosion_core_cache = {}
# </POTBO_STAGE S0968>

# <POTBO_STAGE S0970>


def _v38_cache_limit(cache, limit=220):
    if len(cache) <= limit:
        return

    remove = max(1, len(cache) - int(limit * 0.72))
    for key in list(cache.keys())[:remove]:
        cache.pop(key, None)
# </POTBO_STAGE S0970>

# <POTBO_STAGE S0972>


def _v38_glow_surface(radius, intensity_bucket):
    radius = max(4, int(radius))
    bucket = max(0, min(10, int(intensity_bucket)))
    key = (radius, bucket)
    cached = v38_fire_glow_cache.get(key)
    if cached is not None:
        return cached
    size = radius * 2 + 8
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    c = size // 2
    strength = bucket / 10.0

    for i, frac in enumerate((1.0, 0.72, 0.46, 0.24)):
        rr = max(1, int(radius * frac))
        alpha = int((12 + 38 * strength) * (1.0 - i * 0.13))
        pygame.draw.circle(surf, (255, 84 + i * 22, 12, alpha), (c, c), rr)
    v38_fire_glow_cache[key] = surf
    _v38_cache_limit(v38_fire_glow_cache, 80)
    return surf
# </POTBO_STAGE S0972>

# <POTBO_STAGE S0976>


FireMagicProjectile.__init__ = _v38_fire_projectile_init
FireMagicProjectile._patlat = _v38_fire_projectile_explode
FireMagicProjectile.guncelle = _v38_fire_projectile_update
FireMagicProjectile.ciz = _v38_fire_projectile_draw
# </POTBO_STAGE S0976>

# <POTBO_STAGE S0979>


FireMagicExplosion.__init__ = _v38_fire_explosion_init
FireMagicExplosion._detonate = _v38_fire_explosion_detonate
FireMagicExplosion.ciz = _v38_fire_explosion_draw





V38_MAX_PROJECTILES = 6
V38_MAX_EXPLOSIONS = 5
V38_MAX_GROUND_FIRES = 72
# </POTBO_STAGE S0979>

# <POTBO_STAGE S0986>
V34_SPECIAL_RECOVERY_GRACE_MS = 92
V34_SPECIAL_TARGET_LOCK_EXTRA_MS = 48
V34_SPECIAL_FLASH_MS = (46, 56, 72)
V34_SPECIAL_IMPACT_RING_MS = 170
# </POTBO_STAGE S0986>

# <POTBO_STAGE S0990>
v38_special_arm_refund_active = False
# </POTBO_STAGE S0990>

# <POTBO_STAGE S0992>


def _v34_special_phase_values(p):
    """1.36 saniyelik üç-hit timeline.

    Motion occupancy ~%60, geri kalanı çok kısa impact hold + landing recovery'dir.
    Input lock bütün süre boyunca devam eder.
    """
    return {
        "entry_end": 0.142,
        "hit1_hold_end": 0.164,
        "setup_end": 0.232,
        "slash1_end": 0.318,
        "hit2_hold_end": 0.342,
        "switch_end": 0.406,
        "slash2_end": 0.494,
        "hit3_hold_end": 0.522,
        "settle_end": 0.620,
    }
# </POTBO_STAGE S0992>

# <POTBO_STAGE S0999>


def _v34_special_hit_feedback(slot, center, direction):
    global v34_special_flash_until, v34_special_flash_strength
    _v38_special_hit_feedback_original(slot, center, direction)
    if not v38_impact_pause:
        v34_special_flash_strength *= 0.62
        v34_special_flash_until = min(
            v34_special_flash_until,
            pygame.time.get_ticks() + 40,
        )
# </POTBO_STAGE S0999>

# <POTBO_STAGE S1001>


def _v38_temperature_bucket(temp_k):
    t = max(
        V38_FIRE_MIN_VISIBLE_TEMPERATURE_K,
        min(V38_FIRE_CORE_TEMPERATURE_K, float(temp_k)),
    )
    q = (t - V38_FIRE_MIN_VISIBLE_TEMPERATURE_K) / max(
        1.0,
        V38_FIRE_CORE_TEMPERATURE_K - V38_FIRE_MIN_VISIBLE_TEMPERATURE_K,
    )
    return max(0, min(7, int(round(q * 7.0))))


def _v38_temperature_from_bucket(bucket):
    b = max(0, min(7, int(bucket)))
    q = b / 7.0
    return V38_FIRE_MIN_VISIBLE_TEMPERATURE_K + q * (
        V38_FIRE_CORE_TEMPERATURE_K - V38_FIRE_MIN_VISIBLE_TEMPERATURE_K
    )
# </POTBO_STAGE S1001>

# <POTBO_STAGE S1003>


def _v38_material_response(actor):
    tur = str(getattr(actor, "tur", "default")) if actor is not None else "default"
    return V38_FIRE_MATERIAL_RESPONSE.get(tur, V38_FIRE_MATERIAL_RESPONSE["default"])


def _v38_momentum_bias(momentum, radial):
    """Moving detonation için küçük, sınırlandırılmış ön-yön bias.

    Tam isotropik blast yerine projectile'ın taşıdığı momentum ilk basınç cephesini
    gidiş yönünde en fazla +%8, arka yönde -%5 değiştirir. Thermal alan isotropiktir.
    """
    m = pygame.Vector2(momentum or (0.0, 0.0))
    r = pygame.Vector2(radial or (0.0, 0.0))
    if m.length_squared() <= 1e-8 or r.length_squared() <= 1e-8:
        return 1.0
    dot = max(-1.0, min(1.0, m.normalize().dot(r.normalize())))
    return 1.0 + (0.08 * dot if dot >= 0.0 else 0.05 * dot)
# </POTBO_STAGE S1003>

# <POTBO_STAGE S1008>


V38_BALANCE_DISTANCES = (
    0.0,
    12.0,
    24.0,
    36.0,
    48.0,
    60.0,
    72.0,
    84.0,
    96.0,
    108.0,
    120.0,
    132.0,
    144.0,
    156.0,
    168.0,
    180.0,
    192.0,
    204.0,
    214.0,
)


V38_BALANCE_EXPOSURES = (
    0.33,
    0.67,
    1.00,
)
# </POTBO_STAGE S1008>

# <POTBO_STAGE S1016>


def v38_projectile_equation_samples():
    samples = []
    for ms in (0, 150, 300, 500, 800, 1100, 1500):
        t = ms / 1000.0
        samples.append(
            {
                "ms": ms,
                "speed": round(_v38_projectile_speed(t), 2),
                "temperature_k": round(_v38_projectile_temperature(t), 1),
                "visual_intensity": round(
                    _v38_blackbody_visual_intensity(_v38_projectile_temperature(t)),
                    4,
                ),
            }
        )
    return samples
# </POTBO_STAGE S1016>

# <POTBO_STAGE S1019>





def _v38_monotonic_nonincreasing(values, eps=1e-6):
    vals = [float(x) for x in values]
    return all(vals[i + 1] <= vals[i] + eps for i in range(len(vals) - 1))
# </POTBO_STAGE S1019>

# <POTBO_STAGE S1022>


V38_FIRE_CONTRACT = _v38_fire_contract()
V38_SPECIAL_CONTRACT = _v38_special_contract()
V38_STARTUP_OK = all(V38_FIRE_CONTRACT.values()) and all(V38_SPECIAL_CONTRACT.values())
# </POTBO_STAGE S1022>

# <POTBO_STAGE S1025>


def v38_tuning_bounds_validate():
    result = {}
    for name, spec in V38_TUNING_LIMITS.items():
        getter = V38_TUNING_GETTERS.get(name)
        if getter is None:
            result[name] = {
                "ok": False,
                "reason": "getter_missing",
            }
            continue
        try:
            value = float(getter())
            lo = float(spec["min"])
            hi = float(spec["max"])
            result[name] = {
                "ok": lo <= value <= hi,
                "value": value,
                "min": lo,
                "max": hi,
                "unit": str(spec["unit"]),
            }
        except (TypeError, ValueError, OverflowError) as exc:
            result[name] = {
                "ok": False,
                "reason": type(exc).__name__,
            }
    return result


def v38_tuning_bounds_ok():
    return all(item.get("ok", False) for item in v38_tuning_bounds_validate().values())
# </POTBO_STAGE S1025>

# <POTBO_STAGE S1027>


def v38_cross_system_ok():
    return all(v38_cross_system_invariants().values())
# </POTBO_STAGE S1027>

# <POTBO_STAGE S1029>



_v38_diagnostics_base = v38_diagnostics
# </POTBO_STAGE S1029>

# <POTBO_STAGE S1032>




V38_TUNING_BOUNDS_OK = v38_tuning_bounds_ok()
V38_CROSS_SYSTEM_OK = v38_cross_system_ok()
V38_EQUATION_CATALOG_OK = all(
    bool(v) for k, v in v38_equation_catalog_validate().items() if k != "count"
)
V38_PROFESSIONAL_STARTUP_OK = (
    bool(V38_STARTUP_OK)
    and bool(V38_TUNING_BOUNDS_OK)
    and bool(V38_CROSS_SYSTEM_OK)
    and bool(V38_EQUATION_CATALOG_OK)
)
# </POTBO_STAGE S1032>

# <POTBO_STAGE S1036>


V38_REFERENCE_CURVES = v38_reference_curves()
V38_REFERENCE_INTERPRETATION = v38_reference_interpretation()
# </POTBO_STAGE S1036>

# <POTBO_STAGE S1040>


def v38_build_profile():
    return dict(V38_BUILD_PROFILE)
# </POTBO_STAGE S1040>

# <POTBO_STAGE S1042>


KARAKTER_ONAY_GECIS_SURESI = 2950
KARAKTER_ONAY_FADE_BASLANGICI = 980
# </POTBO_STAGE S1042>

# <POTBO_STAGE S1050>

V39_CHARACTER_ABOUT = {
    "TR": {
        "male": [
            "Hakkında",
            "Zırh boşluğu açan baskı kılıcı; guard kırınca momentumu büyür.",
            "Yara aldıkça geri çekilmez; düşük can eşiğinde vuruşları sertleşir.",
            "Dar alanda duvar ve beden kullanır; çizgisel ilerler, köşe savaşını sever.",
        ],
        "female": [
            "Hakkında",
            "Ritmi okuyan düellocu; ilk temas yerine ikinci açıklığı kovalar.",
            "Mana ve hareketi birlikte ekonomize eder; pozisyon bozulmadan baskı kurar.",
            "Çapraz açıları ve kısa geri çekilmeleri sever; açıkta kalanı cezalandırır.",
        ],
    },
    "EN": {
        "male": [
            "About",
            "A pressure blade that opens guard gaps and grows stronger after a break.",
            "He does not retreat once wounded; low health hardens his commitment.",
            "He uses walls and bodies well in tight spaces and prefers linear pressure.",
        ],
        "female": [
            "About",
            "A duelist who reads rhythm and hunts the second opening, not the first.",
            "She economizes mana and movement together and keeps pressure stable.",
            "She favors oblique angles and short resets, then punishes overextension.",
        ],
    },
}

KARAKTER_OZGECMISLERI["TR"]["male"]["style"] = (
    "İmza: Yüksek poise, geç yarılma, yara üstünden güç devşirme"
)
KARAKTER_OZGECMISLERI["TR"]["female"]["style"] = (
    "İmza: Tempo okuma, mana verimi, açı ve menzil manipülasyonu"
)
KARAKTER_OZGECMISLERI["EN"]["male"]["style"] = (
    "Signature: High poise, delayed fracture, power drawn from wounds"
)
KARAKTER_OZGECMISLERI["EN"]["female"]["style"] = (
    "Signature: Tempo reading, mana economy, angle and range manipulation"
)
# </POTBO_STAGE S1050>

# <POTBO_STAGE S1053>

V39_CHARACTER_SIGNATURES = {
    "male": {
        "vigor": 8,
        "power": 7,
        "focus": 3,
        "poise": 6,
        "edge": 2,
    },
    "female": {
        "vigor": 4,
        "power": 5,
        "focus": 8,
        "poise": 4,
        "edge": 7,
    },
}
# </POTBO_STAGE S1053>

# <POTBO_STAGE S1055>


def v39_clamp01(value):
    return max(0.0, min(1.0, float(value)))


_v39_yeni_oyun_baslat_original = yeni_oyun_baslat
# </POTBO_STAGE S1055>

# <POTBO_STAGE S1060>


_v39_resource_tick_ms = pygame.time.get_ticks()
# </POTBO_STAGE S1060>

# <POTBO_STAGE S1070>


class RockImpact:
    def __init__(self, x, y, simdi):
        self.x = float(x)
        self.y = float(y)
        self.started_ms = int(simdi)
        rng = random.Random(int(x * 31 + y * 17 + simdi))
        self.debris = []
        for _ in range(11):
            a = rng.random() * math.tau
            speed = rng.uniform(18.0, 56.0)
            lift = rng.uniform(0.6, 2.4)
            radius = rng.uniform(1.0, 3.2)
            self.debris.append(
                (
                    math.cos(a) * speed,
                    math.sin(a) * speed * 0.56,
                    lift,
                    radius,
                )
            )
        self.dust = []
        for _ in range(7):
            a = rng.random() * math.tau
            speed = rng.uniform(8.0, 28.0)
            self.dust.append(
                (
                    math.cos(a) * speed,
                    math.sin(a) * speed * 0.42,
                    rng.uniform(6.0, 11.0),
                )
            )

    def alive(self, simdi):
        return int(simdi) - self.started_ms < 430

    def ciz(self, simdi):
        age_ms = max(0, int(simdi) - self.started_ms)
        age = max(0.0, min(1.0, age_ms / 430.0))
        alpha = int(175 * (1.0 - age))
        if alpha <= 0:
            return
        sx = dunya_ekran_x(self.x)
        sy = dunya_ekran_y(self.y)
        for vx, vy, lift, size in self.debris:
            t = age * 0.42
            px = sx + vx * t * KAMERA_YAKINLASTIRMA
            py = sy + vy * t * KAMERA_YAKINLASTIRMA - lift * (1.0 - age) * 2.5
            rr = max(1, int(size * KAMERA_YAKINLASTIRMA))
            surf = pygame.Surface((rr * 2 + 3, rr * 2 + 3), pygame.SRCALPHA)
            pygame.draw.circle(surf, (106, 94, 82, alpha), (rr + 1, rr + 1), rr)
            pygame.draw.circle(
                surf,
                (54, 48, 44, alpha),
                (rr + 1, rr + 1),
                rr,
                1,
            )
            ekran.blit(surf, (int(px - rr - 1), int(py - rr - 1)))
        for vx, vy, size in self.dust:
            t = age * 0.34
            px = sx + vx * t * KAMERA_YAKINLASTIRMA
            py = sy + vy * t * KAMERA_YAKINLASTIRMA
            rr = max(2, int(size * (1.0 - age) * 0.34))
            surf = pygame.Surface((rr * 2 + 4, rr * 2 + 4), pygame.SRCALPHA)
            pygame.draw.ellipse(
                surf,
                (74, 66, 58, max(0, alpha // 2)),
                surf.get_rect(),
            )
            ekran.blit(surf, (int(px - rr - 2), int(py - rr - 2)))


v39_fire_detail_cache = {}


def _v39_fire_dir_vector(direction_name):
    if direction_name == "left":
        return (-1.0, 0.0)
    if direction_name == "right":
        return (1.0, 0.0)
    if direction_name == "up":
        return (0.0, -1.0)
    return (0.0, 1.0)


def _v39_fireball_detail_surface(radius, temp_bucket, direction_name, phase):
    key = (radius, temp_bucket, direction_name, phase)
    surf = v39_fire_detail_cache.get(key)
    if surf is not None:
        return surf
    size = max(24, radius * 5)
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    cx = size // 2
    cy = size // 2
    dx, dy = _v39_fire_dir_vector(direction_name)
    palette = [
        (
            (255, 236, 176, 160),
            (255, 162, 58, 120),
            (225, 76, 14, 96),
        ),
        (
            (255, 232, 166, 170),
            (255, 154, 52, 128),
            (214, 66, 12, 104),
        ),
        (
            (255, 224, 150, 178),
            (248, 140, 42, 132),
            (196, 54, 10, 108),
        ),
        (
            (252, 212, 136, 170),
            (236, 128, 38, 128),
            (172, 46, 10, 102),
        ),
        (
            (244, 200, 124, 160),
            (224, 114, 32, 124),
            (148, 40, 10, 94),
        ),
    ][max(0, min(4, temp_bucket))]
    wobble = (phase % 4) - 1.5
    back_x = cx - dx * radius * (1.15 + 0.08 * wobble)
    back_y = cy - dy * radius * (1.15 - 0.05 * wobble)
    side_x = -dy
    side_y = dx
    pygame.draw.ellipse(
        surf,
        palette[2],
        pygame.Rect(
            int(back_x - radius * 1.45),
            int(back_y - radius * 0.92),
            int(radius * 2.4),
            int(radius * 1.7),
        ),
    )
    pygame.draw.ellipse(
        surf,
        palette[1],
        pygame.Rect(
            int(cx - radius * 1.05 + side_x * wobble * 1.5),
            int(cy - radius * 0.78 + side_y * wobble * 1.5),
            int(radius * 2.0),
            int(radius * 1.45),
        ),
    )
    pygame.draw.ellipse(
        surf,
        palette[0],
        pygame.Rect(
            int(cx - radius * 0.68),
            int(cy - radius * 0.52),
            int(radius * 1.25),
            int(radius * 1.05),
        ),
    )
    for i in range(4):
        k = i / 3.0
        ex = (
            cx
            - dx * radius * (0.9 + 0.42 * k)
            + side_x * (wobble * 1.8 + (i - 1.5) * 2.6)
        )
        ey = cy - dy * radius * (0.9 + 0.42 * k) + side_y * ((1.5 - i) * 1.7)
        rr = max(1, int(radius * (0.18 + 0.07 * (3 - i))))
        pygame.draw.circle(
            surf,
            (255, 182, 92, 88 - i * 12),
            (int(ex), int(ey)),
            rr,
        )
    v39_fire_detail_cache[key] = surf
    if len(v39_fire_detail_cache) > 120:
        for _ in range(min(30, len(v39_fire_detail_cache))):
            v39_fire_detail_cache.pop(next(iter(v39_fire_detail_cache)), None)
    return surf


def _v39_blackbody_rgb(temperature_k):
    t = v39_clamp01(
        (float(temperature_k) - V38_FIRE_MIN_VISIBLE_TEMPERATURE_K)
        / max(
            1.0,
            V38_FIRE_CORE_TEMPERATURE_K - V38_FIRE_MIN_VISIBLE_TEMPERATURE_K,
        )
    )
    if t > 0.72:
        return (255, 242, 188)
    if t > 0.48:
        return (255, 198, 106)
    if t > 0.28:
        return (255, 150, 56)
    return (220, 92, 28)
# </POTBO_STAGE S1070>

# <POTBO_STAGE S1072>


FireMagicProjectile.ciz = _v39_fire_projectile_draw
# </POTBO_STAGE S1072>

# <POTBO_STAGE S1074>





V40_VERSION = "40.0"



KARAKTER_ONAY_GECIS_SURESI = 4400
KARAKTER_ONAY_FADE_BASLANGICI = 2650
# </POTBO_STAGE S1074>

# <POTBO_STAGE S1079>


_v40_bloodmaggot_parent = BloodMaggot
# </POTBO_STAGE S1079>

# <POTBO_STAGE S1086>


V40_HEAD_ROCK_FRAGMENTS = _v40_head_rock_fragments_build()
v40_rock_fragment_cache = {}
# </POTBO_STAGE S1086>

# <POTBO_STAGE S1089>


FireMagicProjectile.ciz = _v40_fire_projectile_draw
# </POTBO_STAGE S1089>

# <POTBO_STAGE S1093>

_v41_ayar_aciklamasi_original = ayar_aciklamasi
# </POTBO_STAGE S1093>

# <POTBO_STAGE S1095>


_v41_ayar_etiketi_original = ayar_etiketi
# </POTBO_STAGE S1095>

# <POTBO_STAGE S1099>


def gelistirici_test_girdisi_uygula(olay):
    return _v41_gelistirici_test_girdisi_original(olay)
# </POTBO_STAGE S1099>

# <POTBO_STAGE S1101>










V42_VERSION = "42.0"
# </POTBO_STAGE S1101>

# <POTBO_STAGE S1103>


_v42_rat_consume_original = AmbientRat._consume_tick


def _v42_rat_consume_tick(self, simdi):
    """Fare kanı temizler ama kan lekesinin boyutunu/merkezini asla değiştirmez."""
    if self.food_kind != "blood":
        return _v42_rat_consume_original(self, simdi)
    if not self._food_valid() or simdi < self.feed_tick_ms:
        return
    self.feed_tick_ms = int(simdi) + random.randint(310, 470)
    obj = self.food_obj
    mass = max(
        0.0,
        float(getattr(obj, "v42_stain_mass", 1.0)) - random.uniform(0.06, 0.11),
    )
    obj.v42_stain_mass = mass
    self.hunger = max(0.0, self.hunger - 0.020)
    self.feed_until = int(simdi) + 220

    if hasattr(obj, "fade_after_ms"):
        obj.fade_after_ms = min(
            int(obj.fade_after_ms),
            int(simdi) + int(70000 + mass * 8000),
        )
    if hasattr(obj, "vanish_after_ms"):
        obj.vanish_after_ms = min(
            int(obj.vanish_after_ms),
            int(simdi) + int(135000 + mass * 12000),
        )
    if mass <= 0.10:
        if hasattr(obj, "vanish_after_ms"):
            obj.vanish_after_ms = min(int(obj.vanish_after_ms), int(simdi) + 9000)
        self.food_obj = None
        self.food_kind = None


AmbientRat._consume_tick = _v42_rat_consume_tick
# </POTBO_STAGE S1103>

# <POTBO_STAGE S1112>


def _v43_rat_consume_tick(self, simdi):
    """Fare temizliği kanı saniyeler içinde kurutmaz; ekosistem yavaş çalışır."""
    if self.food_kind != "blood":
        return _v42_rat_consume_original(self, simdi)
    if not self._food_valid() or simdi < self.feed_tick_ms:
        return
    self.feed_tick_ms = int(simdi) + random.randint(360, 540)
    obj = self.food_obj
    mass = max(
        0.0,
        float(getattr(obj, "v42_stain_mass", 1.0)) - random.uniform(0.035, 0.065),
    )
    obj.v42_stain_mass = mass
    self.hunger = max(0.0, self.hunger - 0.018)
    self.feed_until = int(simdi) + 240


    if hasattr(obj, "fade_after_ms"):
        obj.fade_after_ms = min(
            int(obj.fade_after_ms),
            int(simdi) + int(7 * 60_000 + mass * 38_000),
        )
    if hasattr(obj, "vanish_after_ms"):
        obj.vanish_after_ms = min(
            int(obj.vanish_after_ms),
            int(simdi) + int(14 * 60_000 + mass * 62_000),
        )
    if mass <= 0.08:
        if hasattr(obj, "vanish_after_ms"):
            obj.vanish_after_ms = min(int(obj.vanish_after_ms), int(simdi) + 45_000)
        self.food_obj = None
        self.food_kind = None


AmbientRat._consume_tick = _v43_rat_consume_tick
# </POTBO_STAGE S1112>

# <POTBO_STAGE S1114>
v43_map_zoom_buffer = None
v43_map_zoom_buffer_size = None
# </POTBO_STAGE S1114>

# <POTBO_STAGE S1117>


_v43_dev_input_original = gelistirici_test_girdisi_uygula
# </POTBO_STAGE S1117>

# <POTBO_STAGE S1122>









V44_VERSION = "44.0"
# </POTBO_STAGE S1122>

# <POTBO_STAGE S1124>
V44_ARTERIAL_PALETTE = (
    (74, 3, 8),
    (86, 4, 10),
    (98, 5, 12),
    (110, 6, 14),
    (123, 7, 17),
    (136, 9, 20),
)
V44_VENOUS_PALETTE = (
    (31, 2, 6),
    (38, 2, 7),
    (44, 2, 8),
    (50, 3, 10),
    (57, 3, 11),
    (63, 4, 12),
)
V44_CLOTTED_PALETTE = (
    (24, 2, 4),
    (29, 2, 5),
    (34, 2, 6),
    (39, 3, 7),
    (45, 3, 8),
)
# </POTBO_STAGE S1124>

# <POTBO_STAGE S1130>
V44_SWORD_WIDTH_BONUS_PX = 1
# </POTBO_STAGE S1130>

# <POTBO_STAGE S1132>
v44_arterial_emitters = []
v44_microdrop_budget = 0
# </POTBO_STAGE S1132>

# <POTBO_STAGE S1135>
v44_last_hit_ms = -10000
v44_last_hit_energy = 0.0
v44_last_hit_shape = "radial"
v44_last_hit_target = ""
v44_last_hit_distance = 0.0
# </POTBO_STAGE S1135>

# <POTBO_STAGE S1137>


def v44_clamp(value, lo, hi):
    return max(float(lo), min(float(hi), float(value)))


def v44_clamp01(value):
    return v44_clamp(value, 0.0, 1.0)


def v44_smoothstep(value):
    t = v44_clamp01(value)
    return t * t * (3.0 - 2.0 * t)


def v44_smootherstep(value):
    t = v44_clamp01(value)
    return t * t * t * (t * (t * 6.0 - 15.0) + 10.0)


def v44_safe_vec(value, fallback=(1.0, 0.0)):
    try:
        vec = pygame.Vector2(value)
    except Exception:
        vec = pygame.Vector2(fallback)
    if vec.length_squared() <= 1e-8:
        vec = pygame.Vector2(fallback)
    if vec.length_squared() <= 1e-8:
        vec = pygame.Vector2(1.0, 0.0)
    return vec


def v44_direction_name_vector(name):
    if name == "left":
        return pygame.Vector2(-1.0, 0.0)
    if name == "right":
        return pygame.Vector2(1.0, 0.0)
    if name == "up":
        return pygame.Vector2(0.0, -1.0)
    return pygame.Vector2(0.0, 1.0)
# </POTBO_STAGE S1137>

# <POTBO_STAGE S1145>


def v44_color_mix(a, b, t):
    t = v44_clamp01(t)
    return (
        int(round(a[0] + (b[0] - a[0]) * t)),
        int(round(a[1] + (b[1] - a[1]) * t)),
        int(round(a[2] + (b[2] - a[2]) * t)),
    )


def v44_impact_cone(shape, arterial=False):
    if arterial or shape == "arterial_jet":
        return 23.0
    if shape == "longitudinal":
        return 18.0
    if shape == "fan_asymmetric":
        return 54.0
    return 128.0


def v44_impact_speed_range(shape, power, arterial=False):
    power = max(0.35, float(power))
    if arterial or shape == "arterial_jet":
        return (180.0 * power, 350.0 * power)
    if shape == "longitudinal":
        return (150.0 * power, 320.0 * power)
    if shape == "fan_asymmetric":
        return (90.0 * power, 230.0 * power)
    return (58.0 * power, 178.0 * power)


def v44_directional_sample(base, shape, arterial=False):
    base = v44_safe_vec(base).normalize()
    cone = v44_impact_cone(shape, arterial)
    if shape == "radial_asymmetric":

        if random.random() < 0.67:
            angle = random.triangular(-cone, cone, random.choice((-26.0, 18.0)))
        else:
            angle = random.uniform(-170.0, 170.0)
        return base.rotate(angle)
    if shape == "fan_asymmetric":
        mode = -12.0 if random.random() < 0.57 else 18.0
        return base.rotate(random.triangular(-cone, cone, mode))
    if shape == "longitudinal":
        angle = random.gauss(0.0, cone * 0.38)
        return base.rotate(v44_clamp(angle, -cone, cone))
    angle = random.gauss(0.0, cone * 0.42)
    return base.rotate(v44_clamp(angle, -cone, cone))


def v44_speed_sample(shape, power, arterial=False):
    lo, hi = v44_impact_speed_range(shape, power, arterial)
    if shape == "longitudinal" or arterial:
        return random.triangular(lo, hi, hi * 0.82)
    if shape == "radial_asymmetric":
        return random.triangular(lo, hi, lo * 0.72 + hi * 0.28)
    return random.triangular(lo, hi, (lo + hi) * 0.54)


def v44_particle_count_shape(base_count, shape, lethal=False):
    n = max(0, int(base_count))
    if shape == "longitudinal":
        n = int(round(n * 0.88))
    elif shape == "radial_asymmetric":
        n = int(round(n * 1.10))
    elif shape == "arterial_jet":
        n = int(round(n * 0.78))
    if lethal:
        n = int(round(n * 1.12))
    return max(0, n)
# </POTBO_STAGE S1145>

# <POTBO_STAGE S1147>



BloodParticle = V44BloodParticle
# </POTBO_STAGE S1147>

# <POTBO_STAGE S1150>


def v44_arterial_emitters_update(now):
    if not v44_arterial_emitters:
        return
    for emitter in list(v44_arterial_emitters):
        emitter.update(now)
    v44_arterial_emitters[:] = [e for e in v44_arterial_emitters if e.active]
# </POTBO_STAGE S1150>

# <POTBO_STAGE S1161>
V45_SWEETSPOT_INNER = 0.48
V45_SWEETSPOT_OUTER = 0.92
V45_SWEETSPOT_BONUS = 1.105
V45_HILT_PENALTY = 0.92
V45_TIP_PENALTY = 0.95
V45_ALIGNMENT_BONUS_MAX = 0.085
V45_CROSS_ANGLE_BONUS = 0.045
V45_HEAVY_POISE_BONUS = 1.18
# </POTBO_STAGE S1161>

# <POTBO_STAGE S1164>
V45_EDGE_MASTERY_LEVEL_STEP = 8
V45_TEMPO_MASTERY_LEVEL_STEP = 10
# </POTBO_STAGE S1164>

# <POTBO_STAGE S1169>
v45_last_sweetspot = 0.0
v45_last_alignment = 0.0
# </POTBO_STAGE S1169>

# <POTBO_STAGE S1183>




KARAKTER_ONAY_GECIS_SURESI = 2850
KARAKTER_ONAY_FADE_BASLANGICI = 2080
V46_CHARACTER_SAMPLE_MS = 2500
V46_CHARACTER_ENVELOPE = (
    (0, 0.00),
    (135, 0.02),
    (230, 0.12),
    (305, 0.28),
    (370, 0.16),
    (435, 0.52),
    (510, 0.88),
    (610, 1.00),
    (720, 0.91),
    (850, 0.66),
    (980, 0.39),
    (1130, 0.30),
    (1310, 0.20),
    (1510, 0.12),
    (1780, 0.07),
    (2100, 0.035),
    (2500, 0.00),
)
# </POTBO_STAGE S1183>

# <POTBO_STAGE S1186>
v46_character_switch_ms = pygame.time.get_ticks()
v46_character_card_energy = {"male": 0.0, "female": 0.0}


def v46_envelope_value(ms):
    ms = max(0, int(ms))
    points = V46_CHARACTER_ENVELOPE
    if ms <= points[0][0]:
        return float(points[0][1])
    if ms >= points[-1][0]:
        return float(points[-1][1])
    for i in range(1, len(points)):
        x1, y1 = points[i]
        if ms <= x1:
            x0, y0 = points[i - 1]
            t = (ms - x0) / max(1.0, x1 - x0)
            t = v44_smootherstep(t)
            return float(y0 + (y1 - y0) * t)
    return 0.0
# </POTBO_STAGE S1186>

# <POTBO_STAGE S1188>


_v46_character_card_original = karakter_karti_ciz


def karakter_karti_ciz(rect, cinsiyet, secili, onay_animasyonu=False):
    energy = v46_character_selection_energy(cinsiyet, onay_animasyonu)


    if onay_animasyonu:
        elapsed = pygame.time.get_ticks() - int(karakter_onay_gecisi_baslangic)
        env = v46_envelope_value(elapsed)
        expand = int(round(2.0 + env * 5.0))
        draw_rect = rect.inflate(expand * 2, expand * 2)
    else:
        draw_rect = rect.inflate(
            int(round(energy * 2.0)) * 2,
            int(round(energy * 2.0)) * 2,
        )
    _v46_character_card_original(draw_rect, cinsiyet, secili, onay_animasyonu)


    if secili:
        frame_alpha = int(75 + 92 * min(1.0, energy))
        plate = pygame.Surface(
            (draw_rect.width + 14, draw_rect.height + 14),
            pygame.SRCALPHA,
        )
        pygame.draw.rect(
            plate,
            (16, 7, 10, frame_alpha),
            plate.get_rect(),
            3,
        )
        pygame.draw.line(
            plate,
            (226, 42, 58, min(220, frame_alpha + 40)),
            (8, 5),
            (plate.get_width() - 9, 5),
            2,
        )
        ekran.blit(plate, plate.get_rect(center=draw_rect.center))
# </POTBO_STAGE S1188>

# <POTBO_STAGE S1193>


_v46_dev_input_original = gelistirici_test_girdisi_uygula
# </POTBO_STAGE S1193>

# <POTBO_STAGE S1195>



GELISTIRICI_TEST_TUSLARI.update({pygame.K_b, pygame.K_h, pygame.K_1})
# </POTBO_STAGE S1195>

# <POTBO_STAGE S1197>

V47_TELEMETRY_HISTORY = 48
V47_HIT_CONFIRM_MS = 145
V47_HEAVY_CONFIRM_MS = 210
V47_HIT_RING_RADIUS = 18
V47_HEAVY_RING_RADIUS = 27
V47_EDGE_TEXT_MS = 420
# </POTBO_STAGE S1197>

# <POTBO_STAGE S1199>
v47_hit_events = deque(maxlen=V47_TELEMETRY_HISTORY)
v47_last_confirm_ms = -10000
v47_last_confirm_pos = pygame.Vector2(0.0, 0.0)
v47_last_confirm_heavy = False
v47_last_confirm_quality = 1.0
# </POTBO_STAGE S1199>

# <POTBO_STAGE S1205>





V48_VERSION = "48.0"

V48_CHARACTER_DRIFT_PX = 4.0
V48_CHARACTER_SELECTED_DARKEN = 52
V48_CHARACTER_UNSELECTED_DARKEN = 96
V48_CHARACTER_LOCK_SHAKE_PX = 1.6
V48_CHARACTER_LOCK_SHAKE_END_MS = 900
V48_CHARACTER_TEXT_FADE_MS = 420
v48_character_switch_progress = 1.0
# </POTBO_STAGE S1205>

# <POTBO_STAGE S1207>
v48_character_switch_started_ms = pygame.time.get_ticks()
# </POTBO_STAGE S1207>

# <POTBO_STAGE S1210>





V49_VERSION = "49.0"

V49_AUDIT_INTERVAL_MS = 2300
# </POTBO_STAGE S1210>

# <POTBO_STAGE S1212>
V49_RAT_HARD_LIMIT = 28
V49_PROJECTILE_HARD_LIMIT = 64
V49_AUDIT_HISTORY = 32
v49_audit_next_ms = 0
v49_audit_history = deque(maxlen=V49_AUDIT_HISTORY)
v49_last_warnings = []
v49_runtime_repairs = 0


def v49_numeric_finite(value):
    try:
        return math.isfinite(float(value))
    except Exception:
        return False


def v49_actor_finite(actor):
    if actor is None:
        return True
    for key in ("x", "y"):
        if hasattr(actor, key) and not v49_numeric_finite(getattr(actor, key)):
            return False
    return True
# </POTBO_STAGE S1212>

# <POTBO_STAGE S1216>


_v49_quality_tick_original = v34_quality_tick


def v34_quality_tick():
    result = _v49_quality_tick_original()
    v49_runtime_audit(False)
    return result





V50_VERSION = "50.0"

V50_REQUIRED_TEST_KEYS = (
    "CTRL+I",
    "CTRL+L",
    "CTRL+O",
    "CTRL+U",
    "CTRL+1",
    "CTRL+B",
    "CTRL+H",
)
# </POTBO_STAGE S1216>

# <POTBO_STAGE S1220>


V50_STARTUP_OK = v50_startup_sanity()









V51_VERSION = "51.0"

V51_PARRY_WINDOW_MS = 118
V51_PARRY_LATE_GRACE_MS = 44
# </POTBO_STAGE S1220>

# <POTBO_STAGE S1222>
V51_RIPOSTE_WINDOW_MS = 720
# </POTBO_STAGE S1222>

# <POTBO_STAGE S1224>
V51_RIPOSTE_ALIGNMENT_BONUS = 0.055
# </POTBO_STAGE S1224>

# <POTBO_STAGE S1227>
V51_GUARD_RELEASE_LOCK_MS = 54
V51_BLADE_TRAIL_LIFE_MS = 120
V51_BLADE_TRAIL_MAX = 12
V51_BLADE_TRAIL_MIN_SPEED = 390.0
V51_BLADE_TRAIL_ALPHA = 126
V51_BLADE_TRAIL_HEAVY_ALPHA = 172
V51_HITBOX_DEBUG_ALPHA = 72
# </POTBO_STAGE S1227>

# <POTBO_STAGE S1229>
v51_parry_last_ms = -10000
v51_parry_source = ""
v51_riposte_until = 0
v51_riposte_armed = False
v51_riposte_consumed = False
v51_guard_release_until = 0
v51_blade_trails = deque(maxlen=V51_BLADE_TRAIL_MAX)
# </POTBO_STAGE S1229>

# <POTBO_STAGE S1231>
v51_hitbox_debug = False
v51_last_parry_quality = 0.0
# </POTBO_STAGE S1231>

# <POTBO_STAGE S1233>


def v51_riposte_active(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    return bool(
        v51_riposte_armed
        and not v51_riposte_consumed
        and int(now) <= int(v51_riposte_until)
    )


def v51_riposte_clear():
    global v51_riposte_armed, v51_riposte_consumed, v51_riposte_until
    v51_riposte_armed = False
    v51_riposte_consumed = False
    v51_riposte_until = 0


def v51_riposte_arm(source_name=""):
    global v51_riposte_armed, v51_riposte_consumed, v51_riposte_until
    v51_riposte_armed = True
    v51_riposte_consumed = False
    v51_riposte_until = pygame.time.get_ticks() + V51_RIPOSTE_WINDOW_MS
    if source_name:
        bildirim_goster(
            bt("RIPOSTE PENCERESİ", "RIPOSTE WINDOW"),
            (224, 212, 198),
        )
# </POTBO_STAGE S1233>

# <POTBO_STAGE S1238>


def v51_blade_trails_prune(now):
    while (
        v51_blade_trails
        and now - int(v51_blade_trails[0]["ms"]) > V51_BLADE_TRAIL_LIFE_MS
    ):
        v51_blade_trails.popleft()
# </POTBO_STAGE S1238>

# <POTBO_STAGE S1240>



_v51_dev_input_original = gelistirici_test_girdisi_uygula


def gelistirici_test_girdisi_uygula(olay):
    global v51_hitbox_debug
    if (
        GELISTIRICI_MODU
        and olay.type == pygame.KEYDOWN
        and (olay.mod & pygame.KMOD_CTRL)
        and olay.key == pygame.K_j
    ):
        v51_hitbox_debug = not v51_hitbox_debug
        bildirim_goster(
            bt(
                "Melee hitbox görünümü AÇIK."
                if v51_hitbox_debug
                else "Melee hitbox görünümü KAPALI.",
                "Melee hitbox view ON."
                if v51_hitbox_debug
                else "Melee hitbox view OFF.",
            ),
            SARI if v51_hitbox_debug else GRI,
        )
        return True
    return _v51_dev_input_original(olay)


GELISTIRICI_TEST_TUSLARI.update({pygame.K_j})


_v51_test_rows_original = v46_test_rows


def v46_test_rows():
    rows = list(_v51_test_rows_original())
    rows.append(
        (
            "CTRL + J",
            bt(
                "Melee hitbox: " + ("AÇIK" if v51_hitbox_debug else "KAPALI"),
                "Melee hitbox: " + ("ON" if v51_hitbox_debug else "OFF"),
            ),
        )
    )
    return rows



V50_REQUIRED_TEST_KEYS = (
    "CTRL+I",
    "CTRL+L",
    "CTRL+O",
    "CTRL+U",
    "CTRL+1",
    "CTRL+B",
    "CTRL+H",
    "CTRL+J",
)
# </POTBO_STAGE S1240>

# <POTBO_STAGE S1244>
v52_last_unlocked = ()
# </POTBO_STAGE S1244>

# <POTBO_STAGE S1246>


def v52_effect(name, default=0.0):
    return float(v52_effect_totals().get(str(name), default))
# </POTBO_STAGE S1246>

# <POTBO_STAGE S1249>


def v52_parry_window_bonus_ms():
    return int(round(v52_effect("parry_window")))


def v52_parry_refund_bonus():
    return float(v52_effect("parry_refund"))
# </POTBO_STAGE S1249>

# <POTBO_STAGE S1252>


def v52_longitudinal_bias():
    return float(v52_effect("longitudinal_bias"))


def v52_fan_bias():
    return float(v52_effect("fan_bias"))
# </POTBO_STAGE S1252>

# <POTBO_STAGE S1260>



_v52_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v52_v50_diagnostics_original()
    data["v52"] = v52_diagnostics()
    return data










V53_VERSION = "53.0"
# </POTBO_STAGE S1260>

# <POTBO_STAGE S1264>

v53_surface_cache = {}
v53_surface_cache_order = deque(maxlen=512)
v53_last_zone = "chest"
v53_last_tissue = "default"
v53_last_surface = "unknown"
# </POTBO_STAGE S1264>

# <POTBO_STAGE S1266>


def v53_weighted_choice(mapping):
    if not mapping:
        return None
    total = sum(max(0.0, float(v)) for v in mapping.values())
    if total <= 1e-9:
        return next(iter(mapping))
    roll = random.random() * total
    acc = 0.0
    for key, value in mapping.items():
        acc += max(0.0, float(value))
        if roll <= acc:
            return key
    return next(reversed(mapping))


def v53_zone_for_profile(profile, direction=None, lethal=False, speed=0.0):
    weights = dict(
        V53_ZONE_WEIGHTS_BY_PROFILE.get(
            str(profile), V53_ZONE_WEIGHTS_BY_PROFILE["slash"]
        )
    )
    d = v44_safe_vec(direction or (1.0, 0.0)).normalize()

    if d.y < -0.35:
        weights["head"] *= 1.28
        weights["neck"] *= 1.34
        weights["leg"] *= 0.72
    elif d.y > 0.35:
        weights["abdomen"] *= 1.18
        weights["leg"] *= 1.30
        weights["head"] *= 0.74
    if float(speed) > 700.0:
        weights["neck"] *= 1.12
        weights["arm"] *= 0.88
    if lethal and str(profile) in (
        "heavy_slash",
        "medium_slash",
    ):
        weights["neck"] *= 1.16
        weights["chest"] *= 1.08
    return str(v53_weighted_choice(weights) or "chest")


def v53_zone_values(zone):
    return dict(V53_BODY_ZONES.get(str(zone), V53_BODY_ZONES["chest"]))


def v53_arterial_probability(tissue, zone, profile, speed, lethal):
    z = v53_zone_values(zone)
    sharp = v44_profile_sharpness(profile)
    pressure = float(tissue.get("arterial_pressure", 0.86))
    density = float(tissue.get("vessel_density", 0.76))
    p = 0.045
    p += 0.19 * sharp
    p += 0.18 * max(0.0, float(z.get("arterial", 1.0)) - 0.7)
    p += 0.10 * pressure
    p += 0.06 * density
    p += 0.08 * v44_clamp01(float(speed) / 850.0)
    if lethal:
        p += 0.09
    if str(profile) in ("heavy_blunt", "medium_blunt"):
        p *= 0.52
    return v44_clamp(p, 0.02, 0.78)
# </POTBO_STAGE S1266>

# <POTBO_STAGE S1270>


def v53_surface_classify_rgb(rgb):
    if rgb is None:
        return "unknown"
    r, g, b = [int(v) for v in rgb[:3]]
    brightness = (r + g + b) / 3.0
    saturation = max(r, g, b) - min(r, g, b)
    if brightness < 47:
        return "mud"
    if g > r * 1.10 and g > b * 1.08:
        return "grass"
    if r > g * 1.14 and r > b * 1.18 and brightness < 122:
        return "dirt"
    if saturation < 24 and brightness > 76:
        return "stone"
    if r > g > b and 58 <= brightness <= 142:
        return "wood"
    if g >= r and brightness < 115:
        return "grass"
    return "unknown"


def v53_surface_at(x, y):
    global v53_last_surface
    cell = (int(float(x) // 24), int(float(y) // 24))
    cached = v53_surface_cache.get(cell)
    if cached is not None:
        v53_last_surface = cached
        return cached
    surface = v53_surface_classify_rgb(v53_surface_rgb(x, y))
    if len(v53_surface_cache) >= 512 and v53_surface_cache_order:
        old = v53_surface_cache_order.popleft()
        v53_surface_cache.pop(old, None)
    v53_surface_cache[cell] = surface
    v53_surface_cache_order.append(cell)
    v53_last_surface = surface
    return surface


def v53_surface_response(x, y):
    return dict(
        V53_SURFACE_RESPONSE.get(
            v53_surface_at(x, y),
            V53_SURFACE_RESPONSE["unknown"],
        )
    )
# </POTBO_STAGE S1270>

# <POTBO_STAGE S1274>


def v53_diagnostics():
    return {
        "version": V53_VERSION,
        "last_zone": str(v53_last_zone),
        "last_tissue": str(v53_last_tissue),
        "last_surface": str(v53_last_surface),
        "surface_cache": len(v53_surface_cache),
        "tissue_profiles": tuple(sorted(V53_TISSUE_PROFILES)),
        "surface_profiles": tuple(sorted(V53_SURFACE_RESPONSE)),
        "zones": tuple(V53_BODY_ZONES),
    }


_v53_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v53_v50_diagnostics_original()
    data["v53"] = v53_diagnostics()
    return data










V54_VERSION = "54.0"
# </POTBO_STAGE S1274>

# <POTBO_STAGE S1276>

V54_SWING_CURVE_SAMPLES = (
    (0.00, 0.00),
    (0.08, 0.06),
    (0.16, 0.18),
    (0.24, 0.39),
    (0.32, 0.64),
    (0.40, 0.84),
    (0.48, 0.98),
    (0.54, 1.00),
    (0.62, 0.94),
    (0.70, 0.78),
    (0.78, 0.55),
    (0.86, 0.31),
    (0.94, 0.12),
    (1.00, 0.00),
)

V54_HEAVY_CURVE_SAMPLES = (
    (0.00, 0.00),
    (0.06, 0.04),
    (0.12, 0.12),
    (0.18, 0.27),
    (0.24, 0.48),
    (0.30, 0.70),
    (0.36, 0.88),
    (0.43, 0.98),
    (0.49, 1.00),
    (0.56, 0.97),
    (0.64, 0.88),
    (0.72, 0.72),
    (0.80, 0.50),
    (0.88, 0.28),
    (0.95, 0.10),
    (1.00, 0.00),
)

v54_last_profile = "male_normal"
v54_last_progress = 0.0
v54_last_velocity = 0.0
v54_last_angular_velocity = 0.0
v54_last_tip_velocity = 0.0
v54_last_contact_quality = 0.0


def v54_curve_eval(points, t):
    t = v44_clamp01(t)
    if t <= points[0][0]:
        return float(points[0][1])
    if t >= points[-1][0]:
        return float(points[-1][1])
    for i in range(1, len(points)):
        x1, y1 = points[i]
        if t <= x1:
            x0, y0 = points[i - 1]
            local = (t - x0) / max(1e-9, x1 - x0)
            local = v44_smootherstep(local)
            return float(y0 + (y1 - y0) * local)
    return 0.0
# </POTBO_STAGE S1276>

# <POTBO_STAGE S1278>


def v54_profile():
    return V54_BLADE_PROFILES[v54_profile_key()]
# </POTBO_STAGE S1278>

# <POTBO_STAGE S1280>


def v54_tip_velocity_px_s(profile, angular_deg_s):
    radius = float(profile["blade_length_px"])
    angular_rad_s = math.radians(float(angular_deg_s))
    tip = angular_rad_s * radius * float(profile["tip_bias"])
    return max(0.0, tip)
# </POTBO_STAGE S1280>

# <POTBO_STAGE S1282>


def v54_edge_efficiency(enemy=None):
    profile = v54_profile()
    quality = v54_contact_quality(enemy)
    retention = float(profile["edge_retention"])
    return v44_clamp(0.78 + quality * 0.22, 0.72, 1.0) * retention
# </POTBO_STAGE S1282>

# <POTBO_STAGE S1287>


def v54_diagnostics():
    profile = v54_profile()
    return {
        "version": V54_VERSION,
        "profile": str(v54_last_profile),
        "progress": round(float(v54_last_progress), 4),
        "velocity": round(float(v54_last_velocity), 2),
        "angular_velocity": round(float(v54_last_angular_velocity), 2),
        "tip_velocity": round(float(v54_last_tip_velocity), 2),
        "contact_quality": round(float(v54_last_contact_quality), 4),
        "blade_length_px": float(profile["blade_length_px"]),
        "arc_deg": float(profile["arc_deg"]),
        "effective_mass": float(profile["effective_mass"]),
    }


_v54_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v54_v50_diagnostics_original()
    data["v54"] = v54_diagnostics()
    return data










V55_VERSION = "55.0"

V55_SMEAR_MIN_SPEED = 22.0
# </POTBO_STAGE S1287>

# <POTBO_STAGE S1290>
V55_SMEAR_RADIUS = 24.0
V55_SMEAR_SOURCE_RADIUS = 18.0
V55_SMEAR_SCALE = (0.18, 0.42)
V55_SMEAR_MAX_ACTIVE = 130
V55_POOL_CLUSTER_RADIUS = 22.0
V55_POOL_CLUSTER_MIN = 3
V55_POOL_VISIBLE_MAX = 54
V55_POOL_ALPHA = 58
V55_POOL_GLOSS_ALPHA = 76
V55_POOL_SCAN_INTERVAL_MS = 420
V55_TRANSFER_DECAY_PER_SEC = 0.08
V55_TRANSFER_GAIN = 0.18
V55_TRANSFER_MAX = 1.0
# </POTBO_STAGE S1290>

# <POTBO_STAGE S1293>
v55_pool_clusters = []
v55_pool_next_scan_ms = 0
v55_smear_count = 0
# </POTBO_STAGE S1293>

# <POTBO_STAGE S1295>


def v55_smear_rotation_from_velocity(velocity):
    v = pygame.Vector2(velocity)
    if v.length_squared() <= 1e-6:
        return random.uniform(0.0, 360.0)
    return -math.degrees(math.atan2(v.y, v.x)) + random.uniform(-7.0, 7.0)
# </POTBO_STAGE S1295>

# <POTBO_STAGE S1301>


_v55_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v55_v50_diagnostics_original()
    data["v55"] = v55_diagnostics()
    return data










V56_VERSION = "56.0"
# </POTBO_STAGE S1301>

# <POTBO_STAGE S1304>
v56_last_tick_ms = pygame.time.get_ticks()
# </POTBO_STAGE S1304>

# <POTBO_STAGE S1307>


def v56_actor_forward(actor):
    direction = str(
        getattr(
            actor,
            "direction",
            getattr(actor, "visual_direction", "down"),
        )
    )
    return v44_direction_name_vector(direction)
# </POTBO_STAGE S1307>

# <POTBO_STAGE S1309>


def v56_facing_quality(actor):
    to_player = v56_actor_to_player(actor, predicted=True)
    if to_player.length_squared() <= 1e-6:
        return 1.0
    forward = v56_actor_forward(actor)
    dot = max(
        -1.0,
        min(1.0, forward.normalize().dot(to_player.normalize())),
    )
    return (dot + 1.0) * 0.5


def v56_angle_ready(actor):
    cfg = v56_cfg(actor)
    quality = v56_facing_quality(actor)
    tolerance = float(cfg["angle_tolerance_deg"])
    required_dot = math.cos(math.radians(tolerance))
    required_quality = (required_dot + 1.0) * 0.5
    return quality >= required_quality
# </POTBO_STAGE S1309>

# <POTBO_STAGE S1311>


def v56_update_closing(actor, state):
    dist = v56_distance(actor)
    previous = float(state.get("last_distance", dist))
    state["closing_rate"] = previous - dist
    state["last_distance"] = dist
    return dist


def v56_repeat_penalty(actor, state):
    cfg = v56_cfg(actor)
    repeat = max(0, int(state.get("repeat_count", 0)) - 1)
    return min(520, repeat * int(cfg["repeat_penalty_ms"]))
# </POTBO_STAGE S1311>

# <POTBO_STAGE S1314>



_v56_inward_slot_original = _v43_inward_melee_slot
# </POTBO_STAGE S1314>

# <POTBO_STAGE S1319>


_v56_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v56_v50_diagnostics_original()
    data["v56"] = v56_diagnostics()
    return data










V57_VERSION = "57.0"
# </POTBO_STAGE S1319>

# <POTBO_STAGE S1321>
V57_FATIGUE_DECAY_PER_SEC = 0.32
V57_CLEAN_HIT_FLOW = 0.17
V57_HEAVY_HIT_FLOW = 0.12
V57_WHIFF_FATIGUE = 0.13
V57_HIT_FATIGUE_RELIEF = 0.055
V57_REPEAT_ANGLE_PENALTY = 0.035
V57_REPEAT_ANGLE_WINDOW_MS = 850
V57_RECOVERY_WINDOW_MS = 520
V57_CONTACT_WINDOW_MS = 220
# </POTBO_STAGE S1321>

# <POTBO_STAGE S1324>
V57_PRECISION_CENTER = 0.72
V57_PRECISION_WIDTH = 0.28
# </POTBO_STAGE S1324>

# <POTBO_STAGE S1326>


def v57_clamp01(value):
    return max(0.0, min(1.0, float(value)))


def v57_lerp(a, b, t):
    return float(a) + (float(b) - float(a)) * v57_clamp01(t)
# </POTBO_STAGE S1326>

# <POTBO_STAGE S1331>


def v57_repeat_direction_penalty(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    count = int(v57_state.get("repeat_direction_count", 0))
    last = int(v57_state.get("last_contact_ms", -10000))
    if now - last > V57_REPEAT_ANGLE_WINDOW_MS:
        return 0.0
    return min(0.09, max(0, count - 1) * V57_REPEAT_ANGLE_PENALTY)
# </POTBO_STAGE S1331>

# <POTBO_STAGE S1343>


_v57_game_draw_original = oyun_ekrani_ciz
# </POTBO_STAGE S1343>

# <POTBO_STAGE S1346>


_v57_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v57_v50_diagnostics_original()
    data["v57"] = v57_diagnostics()
    return data










V58_VERSION = "58.0"
# </POTBO_STAGE S1346>

# <POTBO_STAGE S1348>
V58_FILAMENT_MAX = 68
V58_LOBE_MAX = 42
V58_MIST_LIFE_MS = (180, 520)
V58_FILAMENT_LIFE_MS = (150, 390)
V58_LOBE_LIFE_MS = (210, 620)
V58_MIST_SPEED_THRESHOLD = 255.0
V58_FILAMENT_SPEED_THRESHOLD = 455.0
V58_LOBE_SPEED_THRESHOLD = 300.0
V58_WHITE_SPECULAR_SPEED = 430.0
V58_GRAVITY = 610.0
V58_AIR_DRAG = 1.48
V58_MIST_DRAG = 3.35
V58_MAX_SPAWN_PER_EVENT = 24

v58_mist = []
v58_filaments = []
v58_lobes = []
v58_last_update_ms = pygame.time.get_ticks()
v58_stats = {
    "events": 0,
    "mist_spawned": 0,
    "filaments_spawned": 0,
    "lobes_spawned": 0,
    "last_shape": "",
    "last_speed": 0.0,
    "last_arterial": False,
}


def v58_clamp(value, lo, hi):
    return max(float(lo), min(float(hi), float(value)))


def v58_clamp01(value):
    return v58_clamp(value, 0.0, 1.0)


def v58_safe_dir(value):
    try:
        vec = pygame.Vector2(value)
    except Exception:
        vec = pygame.Vector2(1.0, 0.0)
    if vec.length_squared() <= 1e-7:
        vec = pygame.Vector2(1.0, 0.0)
    return vec.normalize()


def v58_rotate(vec, degrees):
    try:
        return pygame.Vector2(vec).rotate(float(degrees))
    except Exception:
        return pygame.Vector2(vec)
# </POTBO_STAGE S1348>

# <POTBO_STAGE S1351>


def v58_event_speed(power, context):
    if isinstance(context, dict):
        ctx_speed = float(context.get("speed", 0.0) or 0.0)
        if ctx_speed > 1.0:
            return ctx_speed
    return max(80.0, float(power) * 420.0)
# </POTBO_STAGE S1351>

# <POTBO_STAGE S1353>


class V58MistParticle:
    __slots__ = (
        "pos",
        "vel",
        "radius",
        "color",
        "alpha",
        "created_ms",
        "life_ms",
        "phase",
        "phase_speed",
        "arterial",
        "seed",
        "alive",
    )

    def __init__(self, x, y, direction, speed, arterial=False, energy=1.0):
        base = v58_safe_dir(direction)
        spread = random.uniform(-42.0, 42.0)
        local = v58_rotate(base, spread)
        local_speed = (
            random.uniform(0.06, 0.22)
            * max(90.0, float(speed))
            * v58_clamp(energy, 0.6, 1.6)
        )
        self.pos = pygame.Vector2(
            float(x) + random.uniform(-2.0, 2.0),
            float(y) + random.uniform(-2.0, 2.0),
        )
        self.vel = local * local_speed + pygame.Vector2(
            random.uniform(-13, 13), random.uniform(-28, 7)
        )
        self.radius = random.uniform(0.65, 1.75)
        self.color = v58_color(arterial=arterial, dark_bias=random.random())
        self.alpha = random.randint(95, 190)
        self.created_ms = pygame.time.get_ticks()
        self.life_ms = random.randint(*V58_MIST_LIFE_MS)
        self.phase = random.uniform(0.0, math.tau)
        self.phase_speed = random.uniform(5.0, 11.0)
        self.arterial = bool(arterial)
        self.seed = random.random()
        self.alive = True

    def update(self, dt, now):
        age = int(now) - int(self.created_ms)
        if age >= self.life_ms:
            self.alive = False
            return
        self.phase += self.phase_speed * dt
        drift = pygame.Vector2(
            math.cos(self.phase) * 4.5,
            math.sin(self.phase * 0.73) * 2.0,
        )
        self.vel += drift * dt
        drag = math.exp(-V58_MIST_DRAG * dt)
        self.vel *= drag
        self.vel.y += V58_GRAVITY * 0.16 * dt
        self.pos += self.vel * dt
        if not v58_world_visible(self.pos.x, self.pos.y, margin=160.0):
            self.alive = False

    def draw(self, surface, silhouette=False):
        if not self.alive or not v58_world_visible(self.pos.x, self.pos.y):
            return
        age = pygame.time.get_ticks() - self.created_ms
        t = v58_clamp01(age / max(1.0, float(self.life_ms)))
        fade = (1.0 - t) ** 1.8
        alpha = int(self.alpha * fade)
        if alpha <= 2:
            return
        sx = dunya_ekran_x(self.pos.x)
        sy = dunya_ekran_y(self.pos.y)
        radius = max(1, int(round(self.radius * KAMERA_YAKINLASTIRMA)))
        if silhouette:
            color = (3, 2, 3, min(120, alpha))
        else:
            color = (*self.color, alpha)
        layer = pygame.Surface((radius * 4 + 4, radius * 4 + 4), pygame.SRCALPHA)
        center = layer.get_rect().center
        pygame.draw.circle(layer, color, center, radius)
        surface.blit(
            layer,
            (
                sx - layer.get_width() // 2,
                sy - layer.get_height() // 2,
            ),
        )
# </POTBO_STAGE S1353>

# <POTBO_STAGE S1355>


class V58ImpactLobe:
    __slots__ = (
        "origin",
        "direction",
        "radius",
        "width",
        "color",
        "created_ms",
        "life_ms",
        "rotation",
        "arterial",
        "alive",
        "jagged",
    )

    def __init__(
        self,
        x,
        y,
        direction,
        speed,
        arterial=False,
        asymmetry=0.6,
    ):
        self.origin = pygame.Vector2(float(x), float(y))
        self.direction = v58_safe_dir(direction)
        energy = v58_clamp(float(speed) / 520.0, 0.45, 1.65)
        self.radius = random.uniform(5.0, 11.0) * energy
        self.width = random.uniform(0.65, 1.55)
        self.color = v58_color(
            arterial=arterial,
            dark_bias=random.uniform(0.1, 0.8),
        )
        self.created_ms = pygame.time.get_ticks()
        self.life_ms = random.randint(*V58_LOBE_LIFE_MS)
        self.rotation = math.atan2(self.direction.y, self.direction.x)
        self.arterial = bool(arterial)
        self.alive = True
        self.jagged = [random.uniform(0.72, 1.24 + asymmetry * 0.22) for _ in range(9)]

    def update(self, dt, now):
        if int(now) - int(self.created_ms) >= self.life_ms:
            self.alive = False

    def draw(self, surface, silhouette=False):
        if not self.alive or not v58_world_visible(self.origin.x, self.origin.y):
            return
        now = pygame.time.get_ticks()
        t = v58_clamp01((now - self.created_ms) / max(1.0, float(self.life_ms)))
        grow = 0.65 + 0.55 * (1.0 - (1.0 - t) ** 3)
        fade = (1.0 - t) ** 1.3
        alpha = int(170 * fade)
        if alpha <= 3:
            return
        center = pygame.Vector2(
            dunya_ekran_x(self.origin.x),
            dunya_ekran_y(self.origin.y),
        )
        points = []
        for i, jag in enumerate(self.jagged):
            frac = i / max(1, len(self.jagged) - 1)
            angle = self.rotation + (-0.78 + frac * 1.56)
            forward = 1.0 + 0.65 * math.cos(angle - self.rotation)
            r = self.radius * jag * forward * grow * KAMERA_YAKINLASTIRMA
            p = center + pygame.Vector2(math.cos(angle), math.sin(angle)) * r
            points.append((int(p.x), int(p.y)))
        points.append((int(center.x), int(center.y)))
        if len(points) >= 3:
            color = (4, 3, 4, min(alpha, 110)) if silhouette else (*self.color, alpha)
            layer = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
            pygame.draw.polygon(layer, color, points)
            if not silhouette and self.arterial and alpha > 90 and len(points) >= 5:
                a = points[3]
                b = points[5]
                pygame.draw.line(
                    layer,
                    (244, 238, 238, min(120, alpha)),
                    a,
                    b,
                    1,
                )
            surface.blit(layer, (0, 0))


def v58_spawn_morphology(x, y, count, power, direction, arterial, context=None):
    context = context if isinstance(context, dict) else {}
    speed = v58_event_speed(power, context)
    shape = v58_event_shape(speed, arterial, context)
    base_dir = v58_safe_dir(
        direction if direction is not None else context.get("direction", (1.0, 0.0))
    )
    lethal = bool(context.get("lethal", False))
    energy = v58_clamp(float(power), 0.55, 2.0)
    v58_stats["events"] += 1
    v58_stats["last_shape"] = shape
    v58_stats["last_speed"] = speed
    v58_stats["last_arterial"] = bool(arterial)

    mist_count = 0
    filament_count = 0
    lobe_count = 0
    if speed >= V58_MIST_SPEED_THRESHOLD:
        mist_count = min(
            V58_MAX_SPAWN_PER_EVENT,
            max(1, int(round(count * (0.10 + speed / 4200.0)))),
        )
    if speed >= V58_FILAMENT_SPEED_THRESHOLD or shape in (
        "longitudinal",
        "arterial_jet",
    ):
        filament_count = min(
            9,
            max(
                1,
                int(round(count * (0.07 if not lethal else 0.12))),
            ),
        )
    if speed >= V58_LOBE_SPEED_THRESHOLD and count >= 4:
        lobe_count = min(
            3,
            1 + int(lethal) + int(arterial and random.random() < 0.55),
        )

    for _ in range(mist_count):
        if len(v58_mist) >= V58_MIST_MAX:
            break
        v58_mist.append(
            V58MistParticle(
                x,
                y,
                base_dir,
                speed,
                arterial=arterial,
                energy=energy,
            )
        )
        v58_stats["mist_spawned"] += 1

    for _ in range(filament_count):
        if len(v58_filaments) >= V58_FILAMENT_MAX:
            break
        v58_filaments.append(
            V58BloodFilament(
                x,
                y,
                base_dir,
                speed,
                arterial=arterial,
                energy=energy,
            )
        )
        v58_stats["filaments_spawned"] += 1

    for _ in range(lobe_count):
        if len(v58_lobes) >= V58_LOBE_MAX:
            break
        lobe_dir = v58_rotate(base_dir, random.uniform(-18.0, 18.0))
        asym = 0.82 if shape in ("fan_asymmetric", "radial_asymmetric") else 0.48
        v58_lobes.append(
            V58ImpactLobe(
                x,
                y,
                lobe_dir,
                speed,
                arterial=arterial,
                asymmetry=asym,
            )
        )
        v58_stats["lobes_spawned"] += 1


def v58_update(now=None):
    global v58_last_update_ms
    if now is None:
        now = pygame.time.get_ticks()
    dt = max(
        0.0,
        min(0.05, (int(now) - int(v58_last_update_ms)) / 1000.0),
    )
    v58_last_update_ms = int(now)
    if dt <= 0.0:
        return
    for collection in (v58_mist, v58_filaments, v58_lobes):
        for item in collection:
            item.update(dt, now)
        collection[:] = [item for item in collection if item.alive]
# </POTBO_STAGE S1355>

# <POTBO_STAGE S1357>


def v58_reset():
    global v58_last_update_ms
    v58_mist.clear()
    v58_filaments.clear()
    v58_lobes.clear()
    v58_last_update_ms = pygame.time.get_ticks()
# </POTBO_STAGE S1357>

# <POTBO_STAGE S1360>


def v58_diagnostics():
    return {
        "version": V58_VERSION,
        "mist": len(v58_mist),
        "filaments": len(v58_filaments),
        "lobes": len(v58_lobes),
        "events": int(v58_stats.get("events", 0)),
        "mist_spawned": int(v58_stats.get("mist_spawned", 0)),
        "filaments_spawned": int(v58_stats.get("filaments_spawned", 0)),
        "lobes_spawned": int(v58_stats.get("lobes_spawned", 0)),
        "last_shape": str(v58_stats.get("last_shape", "")),
        "last_speed": round(float(v58_stats.get("last_speed", 0.0)), 2),
        "last_arterial": bool(v58_stats.get("last_arterial", False)),
    }


_v58_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v58_v50_diagnostics_original()
    data["v58"] = v58_diagnostics()
    return data










V59_VERSION = "59.0"
# </POTBO_STAGE S1360>

# <POTBO_STAGE S1362>

V59_TECHNIQUE_FLASH_MS = 920
V59_TECHNIQUE_HISTORY_LIMIT = 12
# </POTBO_STAGE S1362>

# <POTBO_STAGE S1364>
V59_WOUNDED_RATIO = 0.62
V59_HIGH_FLOW = 0.58
# </POTBO_STAGE S1364>

# <POTBO_STAGE S1366>
V59_PRECISION_THRESHOLD = 0.72
V59_QUICK_SECOND_MS = 480
# </POTBO_STAGE S1366>

# <POTBO_STAGE S1369>


def v59_target_ratio(enemy):
    return max(
        0.0,
        min(
            1.0,
            float(getattr(enemy, "hp", 0.0))
            / max(1.0, float(getattr(enemy, "max_hp", 1.0))),
        ),
    )
# </POTBO_STAGE S1369>

# <POTBO_STAGE S1372>


def v59_riposte_active(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    try:
        return int(now) <= int(v51_riposte_until)
    except Exception:
        return False
# </POTBO_STAGE S1372>

# <POTBO_STAGE S1375>


def v59_choose_technique(enemy, before_hp, now=None):
    if now is None:
        now = pygame.time.get_ticks()
    best_id = None
    best_score = -1.0
    for technique_id, definition in V59_TECHNIQUES.items():
        score = v59_technique_score(
            technique_id, definition, enemy, int(now), before_hp
        )
        if score > best_score:
            best_score = score
            best_id = technique_id
    return best_id
# </POTBO_STAGE S1375>

# <POTBO_STAGE S1377>


def v59_name(technique_id):
    definition = V59_TECHNIQUES.get(technique_id, {})
    return str(definition.get("tr" if dil == "TR" else "en", technique_id or ""))


def v59_active_definition(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    technique_id = v59_state.get("active_id")
    if technique_id is None or int(now) > int(v59_state.get("active_until", 0)):
        return None
    return V59_TECHNIQUES.get(technique_id)
# </POTBO_STAGE S1377>

# <POTBO_STAGE S1383>


_v59_game_draw_original = oyun_ekrani_ciz


def oyun_ekrani_ciz():
    result = _v59_game_draw_original()
    v59_technique_toast_ciz()
    return result
# </POTBO_STAGE S1383>

# <POTBO_STAGE S1386>


_v59_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v59_v50_diagnostics_original()
    data["v59"] = v59_diagnostics()
    return data










V60_VERSION = "60.0"





V60_CHARACTER_WAVEFORM_MS = 2500
V60_CHARACTER_ENVELOPE = (
    (0, 0.000),
    (120, 0.000),
    (180, 0.018),
    (210, 0.072),
    (245, 0.255),
    (280, 0.392),
    (315, 0.205),
    (345, 0.118),
    (365, 0.102),
    (390, 0.315),
    (415, 0.705),
    (445, 0.925),
    (480, 1.000),
    (520, 0.930),
    (555, 0.795),
    (600, 0.610),
    (645, 0.430),
    (690, 0.295),
    (735, 0.235),
    (780, 0.205),
    (830, 0.155),
    (890, 0.128),
    (960, 0.086),
    (1040, 0.062),
    (1130, 0.047),
    (1250, 0.032),
    (1390, 0.022),
    (1560, 0.015),
    (1760, 0.010),
    (1990, 0.006),
    (2250, 0.003),
    (2500, 0.000),
)



KARAKTER_ONAY_GECIS_SURESI = 2850
KARAKTER_ONAY_FADE_BASLANGICI = 2075
V60_FADE_END_MS = 2850
V60_CARD_SPRING_K = 21.0
V60_CARD_SPRING_D = 8.8
V60_CARD_MAX_OFFSET = 7.0
V60_CARD_MAX_SCALE = 0.017
V60_PLATE_SWEEP_WIDTH = 82
V60_PLATE_SWEEP_ALPHA = 54
V60_BEAT_ACCENT_THRESHOLD = 0.18

v60_card_motion = {
    "male": {
        "offset": 0.0,
        "velocity": 0.0,
        "scale": 0.0,
        "scale_velocity": 0.0,
    },
    "female": {
        "offset": 0.0,
        "velocity": 0.0,
        "scale": 0.0,
        "scale_velocity": 0.0,
    },
}
v60_last_envelope = 0.0
v60_last_envelope_ms = 0
v60_peak_velocity = 0.0
v60_confirm_peak_seen = False


def v60_envelope_value(ms):
    ms = max(0, min(V60_CHARACTER_WAVEFORM_MS, int(ms)))
    points = V60_CHARACTER_ENVELOPE
    if ms <= points[0][0]:
        return float(points[0][1])
    for idx in range(1, len(points)):
        x1, y1 = points[idx]
        if ms <= x1:
            x0, y0 = points[idx - 1]
            p = (ms - x0) / max(1.0, float(x1 - x0))

            p = p * p * (3.0 - 2.0 * p)
            return float(y0 + (y1 - y0) * p)
    return 0.0


def v60_envelope_velocity(ms, sample_ms=18):
    before = v60_envelope_value(max(0, int(ms) - sample_ms))
    after = v60_envelope_value(min(V60_CHARACTER_WAVEFORM_MS, int(ms) + sample_ms))
    return (after - before) / max(1.0, float(sample_ms * 2))


def v60_envelope_impulse(ms):
    value = v60_envelope_value(ms)
    velocity = v60_envelope_velocity(ms)
    rising = max(0.0, velocity * 70.0)
    falling = max(0.0, -velocity * 38.0)
    return v44_clamp(value * 0.72 + rising * 0.23 + falling * 0.05, 0.0, 1.28)



def v46_envelope_value(ms):
    return v60_envelope_value(ms)


def v60_motion_step(cinsiyet, selected, confirm, now=None):
    global \
        v60_last_envelope, \
        v60_last_envelope_ms, \
        v60_peak_velocity, \
        v60_confirm_peak_seen
    if now is None:
        now = pygame.time.get_ticks()
    state = v60_card_motion[cinsiyet]
    dt = saat.get_time() / 1000.0 if saat.get_time() else 1.0 / FPS
    dt = max(1.0 / 240.0, min(0.05, dt))
    elapsed = int(now) - int(karakter_onay_gecisi_baslangic) if confirm else 0
    env = v60_envelope_value(elapsed) if confirm else 0.0
    impulse = v60_envelope_impulse(elapsed) if confirm else 0.0

    target_offset = 0.0
    target_scale = 0.0
    if selected:
        target_offset = 1.5
        target_scale = 0.004
    if confirm:

        target_offset += impulse * V60_CARD_MAX_OFFSET
        target_scale += env * V60_CARD_MAX_SCALE

    accel = (target_offset - state["offset"]) * V60_CARD_SPRING_K - state[
        "velocity"
    ] * V60_CARD_SPRING_D
    state["velocity"] += accel * dt
    state["offset"] += state["velocity"] * dt
    s_accel = (target_scale - state["scale"]) * (V60_CARD_SPRING_K * 0.90) - state[
        "scale_velocity"
    ] * (V60_CARD_SPRING_D * 1.05)
    state["scale_velocity"] += s_accel * dt
    state["scale"] += state["scale_velocity"] * dt
    state["offset"] = v44_clamp(state["offset"], -2.0, V60_CARD_MAX_OFFSET + 2.0)
    state["scale"] = v44_clamp(state["scale"], -0.004, V60_CARD_MAX_SCALE + 0.005)

    if confirm:
        velocity = abs(v60_envelope_velocity(elapsed))
        v60_peak_velocity = max(v60_peak_velocity, velocity)
        if env >= 0.95:
            v60_confirm_peak_seen = True
        v60_last_envelope = env
        v60_last_envelope_ms = elapsed
    return state


_v60_character_card_original = karakter_karti_ciz


def karakter_karti_ciz(rect, cinsiyet, secili, onay_animasyonu=False):
    state = v60_motion_step(cinsiyet, secili, onay_animasyonu)
    scale = float(state["scale"])
    grow_x = int(round(rect.width * scale))
    grow_y = int(round(rect.height * scale))
    draw_rect = rect.inflate(grow_x * 2, grow_y * 2)
    draw_rect.y += int(round(state["offset"]))
    result = _v60_character_card_original(draw_rect, cinsiyet, secili, onay_animasyonu)

    if secili:
        now = pygame.time.get_ticks()
        elapsed = now - int(karakter_onay_gecisi_baslangic) if onay_animasyonu else 0
        env = v60_envelope_value(elapsed) if onay_animasyonu else 0.12

        if env >= V60_BEAT_ACCENT_THRESHOLD:
            sweep_progress = v44_clamp01((elapsed - 360.0) / 520.0)
            sweep_x = int(
                draw_rect.left
                - V60_PLATE_SWEEP_WIDTH
                + (draw_rect.width + V60_PLATE_SWEEP_WIDTH * 2) * sweep_progress
            )
            clip = draw_rect.inflate(-8, -8).clip(
                pygame.Rect(0, 0, GENISLIK, YUKSEKLIK)
            )
            if clip.width > 0 and clip.height > 0:
                layer = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
                alpha = int(V60_PLATE_SWEEP_ALPHA * env)
                pygame.draw.line(
                    layer,
                    (246, 242, 242, alpha),
                    (sweep_x, clip.top + 5),
                    (sweep_x - 24, clip.bottom - 5),
                    1,
                )
                old_clip = ekran.get_clip()
                ekran.set_clip(clip)
                ekran.blit(layer, (0, 0))
                ekran.set_clip(old_clip)
    return result


def v60_confirm_vignette_ciz():
    if not karakter_onay_gecisi_aktif:
        return
    elapsed = pygame.time.get_ticks() - int(karakter_onay_gecisi_baslangic)
    env = v60_envelope_value(elapsed)

    darkness = int(10 + 28 * env)
    if elapsed >= KARAKTER_ONAY_FADE_BASLANGICI:
        fade_t = v44_clamp01(
            (elapsed - KARAKTER_ONAY_FADE_BASLANGICI)
            / max(
                1.0,
                V60_FADE_END_MS - KARAKTER_ONAY_FADE_BASLANGICI,
            )
        )
        darkness += int(38 * fade_t)
    if darkness <= 0:
        return
    layer = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    layer.fill((2, 0, 3, min(92, darkness)))
    ekran.blit(layer, (0, 0))
# </POTBO_STAGE S1386>

# <POTBO_STAGE S1388>


def v60_reset_motion():
    global \
        v60_last_envelope, \
        v60_last_envelope_ms, \
        v60_peak_velocity, \
        v60_confirm_peak_seen
    for state in v60_card_motion.values():
        state["offset"] = 0.0
        state["velocity"] = 0.0
        state["scale"] = 0.0
        state["scale_velocity"] = 0.0
    v60_last_envelope = 0.0
    v60_last_envelope_ms = 0
    v60_peak_velocity = 0.0
    v60_confirm_peak_seen = False


def v60_waveform_contract():
    peak_ms, peak_value = max(V60_CHARACTER_ENVELOPE, key=lambda item: item[1])
    nonzero_end = max(ms for ms, value in V60_CHARACTER_ENVELOPE if value > 0.002)
    return {
        "version": V60_VERSION,
        "duration_ms": V60_CHARACTER_WAVEFORM_MS,
        "peak_ms": int(peak_ms),
        "peak": float(peak_value),
        "tail_end_ms": int(nonzero_end),
        "transition_ms": int(KARAKTER_ONAY_GECIS_SURESI),
        "fade_start_ms": int(KARAKTER_ONAY_FADE_BASLANGICI),
        "peak_seen": bool(v60_confirm_peak_seen),
        "last_envelope": round(float(v60_last_envelope), 4),
    }


_v60_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v60_v50_diagnostics_original()
    data["v60"] = v60_waveform_contract()
    return data










V61_VERSION = "61.0"
# </POTBO_STAGE S1388>

# <POTBO_STAGE S1390>
V61_ZONE_POISE = {
    "head": 1.22,
    "neck": 1.18,
    "chest": 1.00,
    "abdomen": 0.92,
    "arm": 0.74,
    "leg": 0.82,
}
V61_DEPTH_GLANCE = 0.34
V61_DEPTH_CLEAN = 0.62
V61_DEPTH_DEEP = 0.82
V61_EXTRA_STUN_MIN_MS = 12
V61_EXTRA_STUN_MAX_MS = 96
V61_STAGGER_EXTENSION_MAX_MS = 145
V61_KNOCKBACK_MAX = 24.0
V61_IMPULSE_REFERENCE = 380.0

v61_reactions = {}
v61_last = {
    "uid": "",
    "kind": "none",
    "depth": 0.0,
    "impulse": 0.0,
    "poise_extra": 0.0,
    "stun_extra_ms": 0,
    "zone": "",
    "armor": 0.0,
}
# </POTBO_STAGE S1390>

# <POTBO_STAGE S1392>


def v61_armor(enemy):
    return float(V61_ARMOR_RESPONSE.get(str(getattr(enemy, "tur", "")), 0.08))


def v61_zone():
    ctx = v44_context_current() or {}
    zone = (
        str(ctx.get("body_zone", ctx.get("zone", "chest")))
        if isinstance(ctx, dict)
        else "chest"
    )
    if zone not in V61_ZONE_POISE:
        zone = "chest"
    return zone
# </POTBO_STAGE S1392>

# <POTBO_STAGE S1394>


def v61_reaction_kind(depth):
    if depth < V61_DEPTH_GLANCE:
        return "glance"
    if depth < V61_DEPTH_CLEAN:
        return "shallow"
    if depth < V61_DEPTH_DEEP:
        return "clean"
    return "deep"
# </POTBO_STAGE S1394>

# <POTBO_STAGE S1396>


def v61_cleanup(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    stale = [
        uid
        for uid, state in v61_reactions.items()
        if int(now) > int(state.get("until", 0))
    ]
    for uid in stale:
        v61_reactions.pop(uid, None)
# </POTBO_STAGE S1396>

# <POTBO_STAGE S1400>


_v61_game_draw_original = oyun_ekrani_ciz


def oyun_ekrani_ciz():
    result = _v61_game_draw_original()
    v61_reaction_debug_ciz()
    return result
# </POTBO_STAGE S1400>

# <POTBO_STAGE S1402>


_v61_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v61_v50_diagnostics_original()
    data["v61"] = v61_diagnostics()
    return data
# </POTBO_STAGE S1402>

# <POTBO_STAGE S1404>
V62_CLOT_MAX_AGE = 0.88
V62_CLOT_COUNT = (2, 7)
V62_MENISCUS_MAX_ALPHA = 82
V62_SPECULAR_MAX_ALPHA = 148
V62_EDGE_DARK_ALPHA = 74
V62_DETAIL_MIN_SCREEN_W = 10
V62_DETAIL_MAX_PER_FRAME = 210
v62_detail_draw_budget = 0
v62_last_budget_reset_ms = 0
# </POTBO_STAGE S1404>

# <POTBO_STAGE S1406>


def v62_hash01(seed, index, salt=0):
    value = (
        int(seed) * 1103515245 + 12345 + int(index) * 2654435761 + int(salt) * 97531
    ) & 0x7FFFFFFF
    return (value % 1000003) / 1000003.0


def v62_budget_take():
    global v62_detail_draw_budget, v62_last_budget_reset_ms
    now = pygame.time.get_ticks()

    bucket = now // 8
    if bucket != v62_last_budget_reset_ms:
        v62_last_budget_reset_ms = bucket
        v62_detail_draw_budget = V62_DETAIL_MAX_PER_FRAME
    if v62_detail_draw_budget <= 0:
        v62_stats["detail_skips"] += 1
        return False
    v62_detail_draw_budget -= 1
    return True
# </POTBO_STAGE S1406>

# <POTBO_STAGE S1408>


_v62_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v62_v50_diagnostics_original()
    data["v62"] = v62_diagnostics()
    return data
# </POTBO_STAGE S1408>

# <POTBO_STAGE S1410>



V63_FRAME_TARGET_MS = 1000.0 / FPS
V63_FRAME_EWMA_ALPHA = 0.055
V63_TIER_HYSTERESIS_MS = 900
V63_TIERS = {
    "high": {
        "mist": 150,
        "filament": 68,
        "lobe": 42,
        "detail": 210,
    },
    "balanced": {
        "mist": 112,
        "filament": 52,
        "lobe": 30,
        "detail": 160,
    },
    "constrained": {
        "mist": 72,
        "filament": 34,
        "lobe": 18,
        "detail": 105,
    },
}
v63_frame_ewma_ms = V63_FRAME_TARGET_MS
v63_tier = "high"
v63_tier_candidate = "high"
v63_candidate_since = pygame.time.get_ticks()
v63_pruned = {"mist": 0, "filament": 0, "lobe": 0}


def v63_choose_tier(frame_ms):
    ratio = float(frame_ms) / max(1.0, V63_FRAME_TARGET_MS)
    if ratio >= 1.38:
        return "constrained"
    if ratio >= 1.12:
        return "balanced"
    return "high"


def v63_update_budget(now=None):
    global v63_frame_ewma_ms, v63_tier, v63_tier_candidate, v63_candidate_since
    global V62_DETAIL_MAX_PER_FRAME
    if now is None:
        now = pygame.time.get_ticks()
    raw_ms = float(saat.get_time()) if saat.get_time() > 0 else V63_FRAME_TARGET_MS
    raw_ms = max(2.0, min(80.0, raw_ms))
    v63_frame_ewma_ms += (raw_ms - v63_frame_ewma_ms) * V63_FRAME_EWMA_ALPHA
    desired = v63_choose_tier(v63_frame_ewma_ms)
    if desired != v63_tier_candidate:
        v63_tier_candidate = desired
        v63_candidate_since = int(now)
    elif (
        desired != v63_tier
        and int(now) - int(v63_candidate_since) >= V63_TIER_HYSTERESIS_MS
    ):
        v63_tier = desired

    limits = V63_TIERS[v63_tier]
    V62_DETAIL_MAX_PER_FRAME = int(limits["detail"])
    collections = (
        ("mist", v58_mist),
        ("filament", v58_filaments),
        ("lobe", v58_lobes),
    )
    for name, collection in collections:
        limit = int(limits[name])
        if len(collection) > limit:
            remove = len(collection) - limit
            del collection[:remove]
            v63_pruned[name] += remove


def v63_spawn_allowance(kind):
    limit = int(V63_TIERS[v63_tier].get(kind, 0))
    collection = {
        "mist": v58_mist,
        "filament": v58_filaments,
        "lobe": v58_lobes,
    }.get(kind)
    if collection is None:
        return 0
    return max(0, limit - len(collection))
# </POTBO_STAGE S1410>

# <POTBO_STAGE S1412>


V58ImpactLobe.draw = _v63_lobe_draw
# </POTBO_STAGE S1412>

# <POTBO_STAGE S1414>


def v63_diagnostics():
    return {
        "version": V63_VERSION,
        "frame_ewma_ms": round(float(v63_frame_ewma_ms), 3),
        "tier": str(v63_tier),
        "limits": dict(V63_TIERS[v63_tier]),
        "pruned": dict(v63_pruned),
        "active": {
            "mist": len(v58_mist),
            "filament": len(v58_filaments),
            "lobe": len(v58_lobes),
        },
    }


_v63_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v63_v50_diagnostics_original()
    data["v63"] = v63_diagnostics()
    return data
# </POTBO_STAGE S1414>

# <POTBO_STAGE S1418>


_v64_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v64_v50_diagnostics_original()
    data["v64"] = v64_diagnostics()
    return data










V65_VERSION = "65.0"



V65_PRESSURE_CURVE = (
    (0.00, 1.00),
    (0.10, 0.96),
    (0.22, 0.84),
    (0.37, 0.71),
    (0.54, 0.56),
    (0.70, 0.41),
    (0.84, 0.28),
    (1.00, 0.13),
)
V65_HEARTBEAT_MS = (92, 126, 108, 142, 156, 176, 205)
V65_PRIMARY_JET_ANGLE = 8.0
V65_SECONDARY_JET_ANGLE = 23.0
V65_GRAVITY_TILT_DEG = 31.0
V65_MIN_PRESSURE = 0.10
V65_SECONDARY_CHANCE = 0.62
v65_stats = {
    "pulses": 0,
    "secondary": 0,
    "last_pressure": 0.0,
    "last_speed": 0.0,
    "last_angle": 0.0,
}


def v65_curve_sample(t):
    t = v44_clamp01(t)
    points = V65_PRESSURE_CURVE
    if t <= points[0][0]:
        return float(points[0][1])
    for idx in range(1, len(points)):
        x1, y1 = points[idx]
        if t <= x1:
            x0, y0 = points[idx - 1]
            p = (t - x0) / max(0.0001, x1 - x0)
            p = v44_smoothstep(p)
            return float(y0 + (y1 - y0) * p)
    return float(points[-1][1])
# </POTBO_STAGE S1418>

# <POTBO_STAGE S1422>


V44ArterialEmitter.update = _v65_arterial_update


def v65_diagnostics():
    return {
        "version": V65_VERSION,
        "active_emitters": len(v44_arterial_emitters),
        "pulses": int(v65_stats.get("pulses", 0)),
        "secondary": int(v65_stats.get("secondary", 0)),
        "last_pressure": round(float(v65_stats.get("last_pressure", 0.0)), 4),
        "last_speed": round(float(v65_stats.get("last_speed", 0.0)), 2),
        "last_angle": round(float(v65_stats.get("last_angle", 0.0)), 2),
    }


_v65_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v65_v50_diagnostics_original()
    data["v65"] = v65_diagnostics()
    return data










V66_VERSION = "66.0"
V66_AUDIT_INTERVAL_MS = 3100
V66_HISTORY_LIMIT = 20
v66_next_audit_ms = 0
v66_history = deque(maxlen=V66_HISTORY_LIMIT)
v66_repairs = 0
v66_last_issues = []


def v66_issue(code, detail=""):
    return {"code": str(code), "detail": str(detail)}


def v66_test_keys_normalized():
    rows = v46_test_rows()
    return [str(row[0]).replace(" ", "").upper() for row in rows]
# </POTBO_STAGE S1422>

# <POTBO_STAGE S1425>


def v66_diagnostics():
    record = v66_runtime_audit(True)
    return {
        "version": V66_VERSION,
        "issues": list(record.get("issues", [])) if record else [],
        "repairs_total": int(v66_repairs),
        "history": len(v66_history),
    }


_v66_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v66_v50_diagnostics_original()
    data["v66"] = v66_diagnostics()
    return data










V67_VERSION = "67.0"
V67_HISTORY = 18
V67_SAMPLE_MIN_MS = 6
V67_SAMPLE_MAX_MS = 55
V67_SPEED_BLEND = 0.72
V67_SPEED_MIN = 110.0
V67_SPEED_MAX = 1120.0
V67_CURVATURE_WINDOW = 5
V67_REACH_REFERENCE_PX = 6.0
v67_tip_history = deque(maxlen=V67_HISTORY)
# </POTBO_STAGE S1425>

# <POTBO_STAGE S1427>
v67_last_measured_speed = 0.0
v67_last_tangent = pygame.Vector2(1.0, 0.0)
v67_last_curvature = 0.0
v67_last_arc_length = 0.0
# </POTBO_STAGE S1427>

# <POTBO_STAGE S1436>


_v67_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v67_v50_diagnostics_original()
    data["v67"] = v67_diagnostics()
    return data










V68_VERSION = "68.0"
# </POTBO_STAGE S1436>

# <POTBO_STAGE S1438>
V68_MAX_CHANNEL = 154
# </POTBO_STAGE S1438>

# <POTBO_STAGE S1440>
v68_last_signature = "default"
v68_last_tone = (0, 0, 0)
# </POTBO_STAGE S1440>

# <POTBO_STAGE S1446>


def v68_diagnostics():
    return {
        "version": V68_VERSION,
        "last_signature": str(v68_last_signature),
        "last_tone": tuple(v68_last_tone),
        "signature_count": len(V68_SIGNATURES) - 1,
        "max_channel": V68_MAX_CHANNEL,
    }


_v68_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v68_v50_diagnostics_original()
    data["v68"] = v68_diagnostics()
    return data










V69_VERSION = "69.0"
V69_TRAJECTORY_ALPHA = 150
V69_REACH_MARK_ALPHA = 190
# </POTBO_STAGE S1446>

# <POTBO_STAGE S1449>


_v69_game_draw_original = oyun_ekrani_ciz


def oyun_ekrani_ciz():
    result = _v69_game_draw_original()
    v69_debug_trajectory_ciz()
    v69_debug_reach_label_ciz()
    return result


def v69_diagnostics():
    checks = v69_reach_assertions()
    return {
        "version": V69_VERSION,
        "checks": checks,
        "all_ok": all(checks.values()),
        "trajectory_samples": len(v67_tip_history),
    }


_v69_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v69_v50_diagnostics_original()
    data["v69"] = v69_diagnostics()
    return data










V70_VERSION = "70.0"

V70_REQUIRED_SYSTEMS = (
    "v44",
    "v45",
    "v46",
    "v49",
    "v51",
    "v52",
    "v53",
    "v54",
    "v55",
    "v56",
    "v57",
    "v58",
    "v59",
    "v60",
    "v61",
    "v62",
    "v63",
    "v64",
    "v65",
    "v66",
    "v67",
    "v68",
    "v69",
)
V70_EXPECTED_TEST_KEYS = (
    "CTRL+I",
    "CTRL+L",
    "CTRL+O",
    "CTRL+U",
    "CTRL+1",
    "CTRL+B",
    "CTRL+H",
    "CTRL+J",
)
v70_startup_report = {}
v70_startup_ok = False


def v70_safe_call(name, fn):
    try:
        return {"ok": True, "value": fn()}
    except Exception as exc:
        return {
            "ok": False,
            "error": f"{type(exc).__name__}: {exc}",
        }
# </POTBO_STAGE S1449>

# <POTBO_STAGE S1451>


def v70_refresh_startup_report():
    global v70_startup_report, v70_startup_ok, V50_STARTUP_OK
    v70_startup_report = v70_final_contract()
    v70_startup_ok = bool(v70_startup_report.get("all_ok", False))

    V50_STARTUP_OK = v70_startup_ok
    return v70_startup_report
# </POTBO_STAGE S1451>

# <POTBO_STAGE S1453>


_v70_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v70_v50_diagnostics_original()
    data["v70"] = {
        "version": V70_VERSION,
        "startup_ok": bool(v70_startup_ok),
        "contract": dict(v70_startup_report),
    }
    return data



v70_refresh_startup_report()










V71_VERSION = "71.0"
V71_HISTORY = 64
V71_MIN_SAMPLE = 3
V71_EXPECTED = {
    "longitudinal": {
        "anisotropy_min": 0.62,
        "spread_max_deg": 46.0,
    },
    "fan_asymmetric": {
        "anisotropy_min": 0.28,
        "spread_max_deg": 92.0,
    },
    "radial_asymmetric": {
        "anisotropy_min": 0.05,
        "spread_max_deg": 156.0,
    },
    "arterial_jet": {
        "anisotropy_min": 0.54,
        "spread_max_deg": 58.0,
    },
}
v71_events = deque(maxlen=V71_HISTORY)
v71_last = {
    "shape": "",
    "count": 0,
    "mean_speed": 0.0,
    "anisotropy": 0.0,
    "spread_deg": 0.0,
    "asymmetry": 0.0,
    "quality_ok": True,
}


def v71_particle_velocity(particle):
    try:
        vec = pygame.Vector2(particle.v)
    except Exception:
        vec = pygame.Vector2(
            float(getattr(particle, "vx", 0.0)),
            float(getattr(particle, "vy", 0.0)),
        )
    return vec


def v71_covariance(vectors):
    if not vectors:
        return 0.0, 0.0, 0.0
    xs = [float(v.x) for v in vectors]
    ys = [float(v.y) for v in vectors]
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    cxx = sum((x - mx) ** 2 for x in xs) / len(xs)
    cyy = sum((y - my) ** 2 for y in ys) / len(ys)
    cxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / len(xs)
    return cxx, cyy, cxy


def v71_eigenvalues_2x2(cxx, cyy, cxy):
    trace = cxx + cyy
    det = cxx * cyy - cxy * cxy
    disc = max(0.0, trace * trace * 0.25 - det)
    root = math.sqrt(disc)
    hi = trace * 0.5 + root
    lo = trace * 0.5 - root
    return max(0.0, hi), max(0.0, lo)


def v71_anisotropy(vectors):
    if len(vectors) < V71_MIN_SAMPLE:
        return 0.0
    cxx, cyy, cxy = v71_covariance(vectors)
    hi, lo = v71_eigenvalues_2x2(cxx, cyy, cxy)
    if hi + lo <= 1e-8:
        return 0.0
    return max(0.0, min(1.0, (hi - lo) / (hi + lo)))


def v71_circular_mean(vectors):
    dirs = []
    for vec in vectors:
        if vec.length_squared() > 1e-8:
            dirs.append(vec.normalize())
    if not dirs:
        return pygame.Vector2(1.0, 0.0)
    mean = pygame.Vector2(sum(v.x for v in dirs), sum(v.y for v in dirs))
    if mean.length_squared() <= 1e-8:
        return pygame.Vector2(1.0, 0.0)
    return mean.normalize()


def v71_angular_metrics(vectors):
    mean = v71_circular_mean(vectors)
    signed = []
    for vec in vectors:
        if vec.length_squared() <= 1e-8:
            continue
        n = vec.normalize()
        cross = mean.x * n.y - mean.y * n.x
        dot = max(-1.0, min(1.0, mean.dot(n)))
        signed.append(math.degrees(math.atan2(cross, dot)))
    if not signed:
        return 0.0, 0.0
    spread = max(signed) - min(signed)
    positive = sum(1 for a in signed if a >= 0.0)
    negative = len(signed) - positive
    asymmetry = abs(positive - negative) / max(1.0, float(len(signed)))
    return float(spread), float(asymmetry)


def v71_shape_quality(shape, anisotropy, spread_deg, asymmetry):
    expected = V71_EXPECTED.get(str(shape))
    if expected is None:
        return True
    if anisotropy < float(expected["anisotropy_min"]):
        return False
    if spread_deg > float(expected["spread_max_deg"]):
        return False

    if shape in ("fan_asymmetric", "radial_asymmetric") and asymmetry < 0.06:
        return False
    return True


def v71_measure_event(shape, particles, context=None):
    global v71_last
    vectors = [v71_particle_velocity(p) for p in particles]
    vectors = [v for v in vectors if v.length_squared() > 1e-8]
    speeds = [v.length() for v in vectors]
    mean_speed = sum(speeds) / len(speeds) if speeds else 0.0
    anisotropy = v71_anisotropy(vectors)
    spread_deg, asymmetry = v71_angular_metrics(vectors)
    quality = (
        v71_shape_quality(shape, anisotropy, spread_deg, asymmetry)
        if len(vectors) >= V71_MIN_SAMPLE
        else True
    )
    record = {
        "ms": pygame.time.get_ticks(),
        "shape": str(shape),
        "count": len(vectors),
        "mean_speed": float(mean_speed),
        "anisotropy": float(anisotropy),
        "spread_deg": float(spread_deg),
        "asymmetry": float(asymmetry),
        "quality_ok": bool(quality),
        "lethal": bool((context or {}).get("lethal", False))
        if isinstance(context, dict)
        else False,
        "arterial": bool((context or {}).get("arterial", False))
        if isinstance(context, dict)
        else False,
    }
    v71_events.append(record)
    v71_last = dict(record)
    return record
# </POTBO_STAGE S1453>

# <POTBO_STAGE S1455>


def v71_recent_quality(limit=12):
    events = list(v71_events)[-max(1, int(limit)) :]
    if not events:
        return 1.0
    return sum(1 for event in events if event.get("quality_ok", True)) / len(events)


def v71_shape_summary():
    summary = {}
    for shape in V71_EXPECTED:
        rows = [event for event in v71_events if event.get("shape") == shape]
        if not rows:
            summary[shape] = {"samples": 0}
            continue
        summary[shape] = {
            "samples": len(rows),
            "anisotropy": round(
                sum(float(r["anisotropy"]) for r in rows) / len(rows),
                4,
            ),
            "spread_deg": round(
                sum(float(r["spread_deg"]) for r in rows) / len(rows),
                2,
            ),
            "asymmetry": round(
                sum(float(r["asymmetry"]) for r in rows) / len(rows),
                4,
            ),
            "quality": round(
                sum(1 for r in rows if r.get("quality_ok", True)) / len(rows),
                3,
            ),
        }
    return summary
# </POTBO_STAGE S1455>

# <POTBO_STAGE S1457>


_v71_game_draw_original = oyun_ekrani_ciz


def oyun_ekrani_ciz():
    result = _v71_game_draw_original()
    v71_telemetry_line_ciz()
    return result


def v71_diagnostics():
    return {
        "version": V71_VERSION,
        "events": len(v71_events),
        "recent_quality": round(v71_recent_quality(), 3),
        "last": dict(v71_last),
        "by_shape": v71_shape_summary(),
    }


_v71_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v71_v50_diagnostics_original()
    data["v71"] = v71_diagnostics()
    return data



V50_STARTUP_OK = bool(v70_refresh_startup_report().get("all_ok", False))










V72_VERSION = "72.0"
# </POTBO_STAGE S1457>

# <POTBO_STAGE S1459>
v72_release_snapshot = {}
# </POTBO_STAGE S1459>

# <POTBO_STAGE S1461>


def v72_release_snapshot_refresh():
    global v72_release_snapshot, V50_STARTUP_OK
    checks = v72_release_checks()
    v72_release_snapshot = {
        "version": V72_VERSION,
        "target": V72_RELEASE_TARGET,
        "checks": checks,
        "passed": sum(1 for value in checks.values() if value),
        "total": len(checks),
        "all_ok": all(checks.values()),
        "test_keys": [row[0] for row in v46_test_rows()],
        "reach": v67_reach_contract(),
        "splatter_quality": v71_recent_quality(),
    }
    V50_STARTUP_OK = bool(v72_release_snapshot["all_ok"])
    return v72_release_snapshot


def v72_diagnostics():
    return dict(v72_release_snapshot_refresh())


_v72_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v72_v50_diagnostics_original()
    data["v72"] = dict(v72_release_snapshot)
    return data


v72_release_snapshot_refresh()
# </POTBO_STAGE S1461>

# <POTBO_STAGE S1463>


V72_RELEASE_SUMMARY = v72_release_summary_lines()
# </POTBO_STAGE S1463>

# <POTBO_STAGE S1465>


V73_NORMAL_AIR_COUNT = 0.92
V73_ARTERIAL_AIR_COUNT = 0.68
V73_DEATH_ARTERY_AIR_COUNT = 0.62
V73_BLAST_AIR_COUNT = 0.84
V73_NORMAL_VZ_SCALE = 0.88
V73_ARTERIAL_VZ_SCALE = 0.70
V73_BLAST_VZ_SCALE = 0.76
V73_GRAVITY_SCALE = 1.08
V73_GROUND_CONVERSION_DIVISOR = 3
V73_GROUND_CONVERSION_MAX = 12
V73_LANDING_SATELLITE_MAX = 5
# </POTBO_STAGE S1465>

# <POTBO_STAGE S1467>
V55_POOL_VISIBLE_MAX = max(int(V55_POOL_VISIBLE_MAX), 64)
V55_POOL_ALPHA = max(int(V55_POOL_ALPHA), 64)
# </POTBO_STAGE S1467>

# <POTBO_STAGE S1470>


def v73_safe_direction(value, fallback=(1.0, 0.0)):
    try:
        vec = pygame.Vector2(value)
    except Exception:
        vec = pygame.Vector2(fallback)
    if vec.length_squared() <= 1e-8:
        vec = pygame.Vector2(fallback)
    if vec.length_squared() <= 1e-8:
        vec = pygame.Vector2(1.0, 0.0)
    return vec.normalize()
# </POTBO_STAGE S1470>

# <POTBO_STAGE S1472>


def _v73_v44_particle_update(self, dt):
    if not getattr(self, "active", False):
        return _v73_v44_particle_update_original(self, dt)
    pre_active = bool(self.active)
    pre_z = float(getattr(self, "z", 0.0))
    pre_vz = float(getattr(self, "vz", 0.0))
    pre_v = pygame.Vector2(getattr(self, "v", (0.0, 0.0)))
    pre_speed = pre_v.length()
    result = _v73_v44_particle_update_original(self, dt)

    landed = (
        pre_active
        and not bool(getattr(self, "active", False))
        and float(getattr(self, "z", 1.0)) <= 0.01
        and (pre_z <= 7.0 or pre_vz < 0.0)
    )
    if not landed:
        return result

    micro = bool(getattr(self, "micro", False))
    arterial = bool(getattr(self, "arterial", False))
    parent_speed = float(getattr(self, "parent_speed", 0.0))
    impact_speed = max(pre_speed, parent_speed * 0.34)
    if micro and random.random() > 0.34:
        return result

    satellites = 1
    if impact_speed >= 90.0:
        satellites += 1
    if impact_speed >= 170.0:
        satellites += 1
    if impact_speed >= 270.0:
        satellites += 1
    if arterial and impact_speed >= 120.0:
        satellites += 1
    if micro:
        satellites = 1
    satellites = min(V73_LANDING_SATELLITE_MAX, satellites)

    base_scale = max(0.12, float(getattr(self, "scale", 0.7)))
    made = v73_ground_splatter(
        self.x,
        self.y,
        pre_v if pre_v.length_squared() > 1e-8 else (1.0, 0.0),
        satellites,
        scale_range=(0.10 * base_scale, 0.34 * base_scale),
        distance_range=(
            1.5,
            min(22.0, 5.0 + impact_speed * 0.055),
        ),
        cone_deg=46.0 if arterial else 76.0,
        backscatter=0.10 if arterial else 0.18,
        source="particle_landing",
    )
    v73_stats["landing_satellites"] += made
    return result


V44BloodParticle.guncelle = _v73_v44_particle_update
# </POTBO_STAGE S1472>

# <POTBO_STAGE S1481>


_v73_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v73_v50_diagnostics_original()
    data["v73"] = v73_diagnostics()
    return data
# </POTBO_STAGE S1481>

# <POTBO_STAGE S1484>
V74_DEATH_DRAW_MARGIN = 110.0

v74_current_particle = None
v74_particle_primary_committed = set()
v74_particle_last_clean = {}
# </POTBO_STAGE S1484>

# <POTBO_STAGE S1488>




_v74_particle_update_original = V44BloodParticle.guncelle
# </POTBO_STAGE S1488>

# <POTBO_STAGE S1490>


V44BloodParticle.guncelle = _v74_particle_update



_v74_mist_update_original = V58MistParticle.update
_v74_filament_update_original = V58BloodFilament.update
_v74_lobe_update_original = V58ImpactLobe.update
# </POTBO_STAGE S1490>

# <POTBO_STAGE S1492>


V58MistParticle.update = _v74_mist_update
V58BloodFilament.update = _v74_filament_update
V58ImpactLobe.update = _v74_lobe_update
# </POTBO_STAGE S1492>

# <POTBO_STAGE S1498>


_v74_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v74_v50_diagnostics_original()
    data["v74"] = v74_diagnostics()
    return data
# </POTBO_STAGE S1498>

# <POTBO_STAGE S1500>


V75_MAGGOT_FIRST_MIN_MS = 6 * 60 * 1000
V75_MAGGOT_FIRST_MAX_MS = 10 * 60 * 1000
V75_MAGGOT_WAVE_MIN_MS = 4 * 60 * 1000
V75_MAGGOT_WAVE_MAX_MS = 7 * 60 * 1000
V75_MAGGOT_LIFE_MIN_MS = 4 * 60 * 1000
V75_MAGGOT_LIFE_MAX_MS = 7 * 60 * 1000
V75_MAGGOT_SPREAD_MIN_MS = 36 * 1000
V75_MAGGOT_SPREAD_MAX_MS = 62 * 1000
V75_MAGGOT_FEED_INTERVAL_MS = 1000
V75_MAGGOT_MAX = 9
# </POTBO_STAGE S1500>

# <POTBO_STAGE S1502>
V75_RAT_CROWD_DAMPING = 0.72
# </POTBO_STAGE S1502>

# <POTBO_STAGE S1504>

V75_ECOLOGY_CLEANUP_INTERVAL_MS = 1800
v75_cleanup_next_ms = 0
# </POTBO_STAGE S1504>

# <POTBO_STAGE S1506>





_v75_maggot_init_original = BloodMaggot.__init__
_v75_maggot_update_original = BloodMaggot.guncelle
# </POTBO_STAGE S1506>

# <POTBO_STAGE S1508>


def v75_maggot_spread_point(maggot):
    """Kurtçuğun taşıdığı kanı yalnız gerçek temiz zemine bırak."""
    here = pygame.Vector2(float(maggot.x), float(maggot.y))
    source = pygame.Vector2(
        float(getattr(maggot, "anchor_x", here.x)),
        float(getattr(maggot, "anchor_y", here.y)),
    )
    outward = here - source
    if outward.length_squared() <= 1e-6:
        outward = pygame.Vector2(1.0, 0.0).rotate(random.uniform(0.0, 360.0))
    else:
        outward = outward.normalize()


    for _ in range(9):
        direction = outward.rotate(random.uniform(-72.0, 72.0))
        dist = random.uniform(10.0, 28.0)
        p = here + direction * dist
        if v74_floor_clean(p.x, p.y):
            return p
    return None
# </POTBO_STAGE S1508>

# <POTBO_STAGE S1510>


BloodMaggot.__init__ = _v75_maggot_init
BloodMaggot.guncelle = _v75_maggot_update
# </POTBO_STAGE S1510>

# <POTBO_STAGE S1513>


AmbientRat._consume_tick = _v75_rat_consume_tick
# </POTBO_STAGE S1513>

# <POTBO_STAGE S1515>


AmbientRat._find_food = _v75_rat_find_food
# </POTBO_STAGE S1515>

# <POTBO_STAGE S1517>


_v75_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v75_v50_diagnostics_original()
    data["v75"] = v75_ecology_diagnostics()
    return data
# </POTBO_STAGE S1517>

# <POTBO_STAGE S1522>



def _v34_special_hit_counter_ciz(simdi):
    return
# </POTBO_STAGE S1522>

# <POTBO_STAGE S1524>





V76_DEATH_BLACK = (0, 0, 0)
V76_DEATH_BLOOD = (72, 0, 8)
V76_DEATH_BODY = (
    142,
    12,
    24,
)
_v76_death_scratch = pygame.Surface(
    (GENISLIK, YUKSEKLIK), pygame.SRCALPHA
).convert_alpha()


def _v76_flat_layer(draw_fn, color, remove_black=False):
    """Mevcut koreografiyi koruyup bütün görünür pikselleri tek düz renge indirger."""
    global ekran
    old_screen = ekran
    _v76_death_scratch.fill((0, 0, 0, 0))
    ekran = _v76_death_scratch
    try:
        draw_fn()
    finally:
        ekran = old_screen

    src = _v76_death_scratch
    if remove_black:

        src = _v76_death_scratch.copy()
        src.set_colorkey(V76_DEATH_BLACK)
    mask = pygame.mask.from_surface(src, 1)
    if mask.count() <= 0:
        return
    flat = mask.to_surface(
        setcolor=(*color, 255),
        unsetcolor=(0, 0, 0, 0),
    ).convert_alpha()
    ekran.blit(flat, (0, 0))
# </POTBO_STAGE S1524>

# <POTBO_STAGE S1532>



_v76_brightness_original = parlaklik_kaplamasi_ciz
# </POTBO_STAGE S1532>

# <POTBO_STAGE S1535>


_v76_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v76_v50_diagnostics_original()
    data["v76"] = v76_diagnostics()
    return data
# </POTBO_STAGE S1535>

# <POTBO_STAGE S1537>
V77_DEATH_BLACK = (0, 0, 0)
V77_DEATH_BLOOD = (72, 0, 8)
V77_DEATH_BODY = (142, 12, 24)
V77_LAYER_MAX_COVERAGE = 0.42
# </POTBO_STAGE S1537>

# <POTBO_STAGE S1541>


def gelistirici_test_paneli_ciz():
    return
# </POTBO_STAGE S1541>

# <POTBO_STAGE S1543>





def _v77_semantic_layer(draw_fn, color, max_coverage=V77_LAYER_MAX_COVERAGE):
    """Bir sahne katmanını yeni, temiz bir yüzeyde çizip tek palette rengine indirger.

    Pure-black gölgeler maske dışında tutulur. Ayrıca bir renderer hatası yüzünden
    katman ekranın olağandışı büyük bölümünü kaplarsa katman reddedilir; böylece V76'daki
    tam-ekran kırmızı arızası fiziksel olarak tekrar oluşamaz.
    """
    global ekran
    old_screen = ekran
    scratch = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    scratch.fill((0, 0, 0, 0))
    ekran = scratch
    try:
        draw_fn()
    finally:
        ekran = old_screen



    opaque = pygame.Surface((GENISLIK, YUKSEKLIK)).convert()
    opaque.fill(V77_DEATH_BLACK)
    opaque.blit(scratch, (0, 0))
    opaque.set_colorkey(V77_DEATH_BLACK)
    mask = pygame.mask.from_surface(opaque, 1)
    count = mask.count()
    if count <= 0:
        return False
    if count / float(GENISLIK * YUKSEKLIK) > float(max_coverage):
        return False

    flat = mask.to_surface(
        setcolor=(*color, 255),
        unsetcolor=(0, 0, 0, 0),
    ).convert_alpha()
    ekran.blit(flat, (0, 0))
    return True
# </POTBO_STAGE S1543>

# <POTBO_STAGE S1552>


_v77_v50_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v77_v50_diagnostics_original()
    data["v77"] = v77_diagnostics()
    return data










V78_VERSION = "78.0"
# </POTBO_STAGE S1552>

# <POTBO_STAGE S1554>


def _v78_clamp01(v):
    return max(0.0, min(1.0, float(v)))


def _v78_smoothstep01(v):
    v = _v78_clamp01(v)
    return v * v * (3.0 - 2.0 * v)
# </POTBO_STAGE S1554>

# <POTBO_STAGE S1556>


def gotik_panel(rect, accent_color=PARLAK_KIRMIZI, alpha=235):
    v78_panel_draw(rect, accent_color, alpha, title_band=True)


def _v78_slot_surface(rect, accent, selected=False, taşıma=False, magic=False):
    bg = (12, 10, 14) if not magic else (15, 10, 10)
    if taşıma:
        accent = SARI
    elif selected:
        accent = accent
    else:
        accent = (92, 74, 83)
    pygame.draw.rect(ekran, bg, rect)
    pygame.draw.rect(ekran, accent, rect, 2 if (selected or taşıma) else 1)
    inner = rect.inflate(-8, -8)
    if inner.width > 0 and inner.height > 0:
        pygame.draw.rect(
            ekran,
            (26, 22, 28) if not magic else (28, 18, 18),
            inner,
            1,
        )
    if selected:
        pygame.draw.line(
            ekran,
            accent,
            (rect.left + 8, rect.top + 5),
            (rect.right - 8, rect.top + 5),
            1,
        )
# </POTBO_STAGE S1556>

# <POTBO_STAGE S1558>


def _v78_resource_bar(
    rect,
    oran,
    fill_color,
    back_color,
    border_color,
    trail_oran=None,
    trail_color=None,
):
    oran = _v78_clamp01(oran)
    pygame.draw.rect(ekran, back_color, rect)
    if trail_oran is not None and trail_color is not None:
        trail_oran = _v78_clamp01(trail_oran)
        tw = int(round(rect.width * trail_oran))
        if tw > 0:
            pygame.draw.rect(
                ekran,
                trail_color,
                pygame.Rect(rect.x, rect.y, tw, rect.height),
            )
    fw = int(round(rect.width * oran))
    if fw > 0:
        pygame.draw.rect(
            ekran,
            fill_color,
            pygame.Rect(rect.x, rect.y, fw, rect.height),
        )
    pygame.draw.rect(ekran, border_color, rect, 1)
# </POTBO_STAGE S1558>

# <POTBO_STAGE S1576>


_v78_prev_full_diag = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v78_prev_full_diag()
    data["v78"] = v78_diagnostics()
    return data
# </POTBO_STAGE S1576>

# <POTBO_STAGE S1579>


def _v79_clamp01(v):
    return max(0.0, min(1.0, float(v)))


def _v79_smoothstep(v):
    v = _v79_clamp01(v)
    return v * v * (3.0 - 2.0 * v)


def _v79_smootherstep(v):
    v = _v79_clamp01(v)
    return v * v * v * (v * (v * 6.0 - 15.0) + 10.0)


def _v79_coin_draw(x, y, size=22):
    if coin_sembol_resmi is None:
        return False
    icon = hafif_piksellestir(coin_sembol_resmi, (int(size), int(size)), 2)
    ekran.blit(icon, (int(x), int(y)))
    return True


def _v79_sharp_bar(
    rect,
    ratio,
    fill,
    back,
    border,
    shown_ratio=None,
    warning=False,
):
    rect = pygame.Rect(rect)
    ratio = _v79_clamp01(ratio)
    if shown_ratio is None:
        shown_ratio = ratio
    shown_ratio = _v79_clamp01(shown_ratio)


    pygame.draw.rect(ekran, (2, 2, 3), rect.inflate(4, 4))
    pygame.draw.rect(ekran, back, rect)


    if shown_ratio > ratio + 0.003:
        trail_w = int(round(rect.width * shown_ratio))
        if trail_w > 0:
            trail = pygame.Rect(rect.x, rect.y, trail_w, rect.height)
            pygame.draw.rect(ekran, (69, 34, 40), trail)

    fill_w = int(round(rect.width * ratio))
    if fill_w > 0:
        pygame.draw.rect(
            ekran,
            fill,
            pygame.Rect(rect.x, rect.y, fill_w, rect.height),
        )

    edge = PARLAK_KIRMIZI if warning else border
    pygame.draw.rect(ekran, edge, rect, 1)
    if rect.height >= 8:
        pygame.draw.line(
            ekran,
            (
                min(255, fill[0] + 35),
                min(255, fill[1] + 35),
                min(255, fill[2] + 35),
            ),
            (rect.left + 2, rect.top + 1),
            (rect.left + max(2, fill_w - 2), rect.top + 1),
            1,
        )
# </POTBO_STAGE S1579>

# <POTBO_STAGE S1587>





V79_DEATH_TITLE_DELAY_MS = 2500
V79_DEATH_TITLE_FADE_MS = 2700
# </POTBO_STAGE S1587>

# <POTBO_STAGE S1591>


V79_BAYER_4 = (
    (0, 8, 2, 10),
    (12, 4, 14, 6),
    (3, 11, 1, 9),
    (15, 7, 13, 5),
)
_v79_dither_cache = {}
_v79_title_cache = {}


def _v79_dither_level(progress):
    return max(0, min(16, int(round(_v79_clamp01(progress) * 16.0))))


def _v79_dither_pattern(size, level):
    w, h = max(1, int(size[0])), max(1, int(size[1]))
    level = max(0, min(16, int(level)))
    key = (w, h, level)
    cached = _v79_dither_cache.get(key)
    if cached is not None:
        return cached

    tile = pygame.Surface((4, 4), pygame.SRCALPHA)
    for y in range(4):
        for x in range(4):
            visible = V79_BAYER_4[y][x] < level
            tile.set_at((x, y), (255, 255, 255, 255 if visible else 0))

    pat = pygame.Surface((w, h), pygame.SRCALPHA)
    for yy in range(0, h, 4):
        for xx in range(0, w, 4):
            pat.blit(tile, (xx, yy))

    if len(_v79_dither_cache) > 96:
        _v79_dither_cache.clear()
    _v79_dither_cache[key] = pat
    return pat


def _v79_dither_blit(surface, dest, progress):
    level = _v79_dither_level(progress)
    if level <= 0:
        return
    if level >= 16:
        ekran.blit(surface, dest)
        return
    draw = surface.copy()
    draw.blit(
        _v79_dither_pattern(draw.get_size(), level),
        (0, 0),
        special_flags=pygame.BLEND_RGBA_MULT,
    )
    ekran.blit(draw, dest)
# </POTBO_STAGE S1591>

# <POTBO_STAGE S1605>


_v79_diag_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v79_diag_original()
    data["v79"] = v79_diagnostics()
    return data
# </POTBO_STAGE S1605>

# <POTBO_STAGE S1607>


KARAKTER_ONAY_GECIS_SURESI = 3400
KARAKTER_ONAY_FADE_BASLANGICI = 2360
# </POTBO_STAGE S1607>

# <POTBO_STAGE S1610>


def _v80_clamp01(v):
    return max(0.0, min(1.0, float(v)))


def _v80_smooth(v):
    v = _v80_clamp01(v)
    return v * v * (3.0 - 2.0 * v)
# </POTBO_STAGE S1610>

# <POTBO_STAGE S1614>


def _v80_death_age_ms():
    return max(
        0,
        pygame.time.get_ticks() - int(v80_death_fx.get("start_ms", 0) or 0),
    )
# </POTBO_STAGE S1614>

# <POTBO_STAGE S1619>


_v80_diag_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v80_diag_original()
    data["v80"] = v80_diagnostics()
    return data










V81_VERSION = "81.0"
V81_MAX_DROPLETS = 280
V81_MAX_SEEPS = 26

v81_death_blood = {
    "start_ms": 0,
    "seed": 0,
    "drops": [],
    "seeps": [],
    "burst_serial": 0,
}


def _v81_clamp01(v):
    return max(0.0, min(1.0, float(v)))


def _v81_smooth(v):
    v = _v81_clamp01(v)
    return v * v * (3.0 - 2.0 * v)


def _v81_rng(tag=0):
    seed = int(v81_death_blood.get("seed", 0) or 1)
    serial = int(v81_death_blood.get("burst_serial", 0))
    return random.Random(seed * 1009 + serial * 9176 + int(tag) * 7919)
# </POTBO_STAGE S1619>

# <POTBO_STAGE S1622>


def _v81_irregular_shape(rng, n=None):
    n = int(n or rng.randint(7, 10))
    factors = []
    bias = rng.uniform(-0.18, 0.22)
    for i in range(n):
        a = math.tau * i / float(n)
        f = rng.uniform(0.70, 1.28)
        f *= (
            1.0
            + 0.11 * math.sin(a * 2.0 + bias * 7.0)
            + 0.06 * math.sin(a * 5.0 - bias * 9.0)
        )
        factors.append(max(0.52, min(1.42, f)))
    return factors


def _v81_add_seep(origin, radius_x, radius_y, birth_ms, grow_ms, rng=None):
    if len(v81_death_blood["seeps"]) >= V81_MAX_SEEPS:
        return
    if rng is None:
        rng = _v81_rng(41)
    v81_death_blood["seeps"].append(
        {
            "origin": pygame.Vector2(origin),
            "rx": float(radius_x),
            "ry": float(radius_y),
            "birth_ms": int(birth_ms),
            "grow_ms": int(grow_ms),
            "angle": rng.uniform(0.0, math.tau),
            "shape": _v81_irregular_shape(rng, rng.randint(9, 12)),
        }
    )


def _v81_add_burst(
    origin,
    direction,
    count,
    intensity=1.0,
    delay_ms=0,
    spread_deg=34.0,
    height=19.0,
    distance_mul=1.0,
    seep=True,
    tag=0,
):
    if len(v81_death_blood["drops"]) >= V81_MAX_DROPLETS:
        return 0

    v81_death_blood["burst_serial"] = int(v81_death_blood.get("burst_serial", 0)) + 1
    rng = _v81_rng(tag)
    direction = pygame.Vector2(direction)
    if direction.length_squared() <= 1e-6:
        direction = _v81_impact_direction()
    direction = direction.normalize()
    origin = pygame.Vector2(origin)
    intensity = max(0.35, float(intensity))
    count = max(
        1,
        min(
            int(count),
            V81_MAX_DROPLETS - len(v81_death_blood["drops"]),
        ),
    )



    side_bias = rng.uniform(-0.42, 0.42) * float(spread_deg)
    long_tail_side = -1.0 if rng.random() < 0.5 else 1.0
    now = pygame.time.get_ticks()

    for i in range(count):
        q = i / max(1.0, float(count - 1))
        if rng.random() < 0.12:
            angle = rng.uniform(82.0, 148.0) * rng.choice((-1.0, 1.0))
            dist_scale = rng.uniform(0.22, 0.58)
        elif rng.random() < 0.24:
            angle = side_bias + long_tail_side * rng.uniform(
                spread_deg * 0.30, spread_deg * 0.92
            )
            dist_scale = rng.uniform(0.72, 1.22)
        else:
            angle = rng.gauss(side_bias * 0.36, max(3.0, spread_deg * 0.31))
            angle = max(
                -spread_deg * 1.18,
                min(spread_deg * 1.18, angle),
            )

            dist_scale = min(1.55, max(0.18, rng.lognormvariate(-0.12, 0.38)))

        d = direction.rotate(angle)
        if d.length_squared() <= 1e-6:
            d = direction
        d = d.normalize()

        flight_ms = int(rng.uniform(300.0, 820.0) * (0.88 + intensity * 0.13))
        travel = rng.uniform(24.0, 67.0) * intensity * distance_mul * dist_scale
        lateral_noise = pygame.Vector2(-d.y, d.x) * rng.uniform(-5.5, 5.5)
        landing = origin + d * travel + lateral_noise


        if not v74_floor_clean(landing.x, landing.y):
            safe = v74_trace_clean_floor(
                landing.x,
                landing.y,
                direction=d,
                last_clean=origin,
            )
            if safe is not None:
                landing = pygame.Vector2(safe)
            else:
                landing = origin + d * min(16.0, travel * 0.35)

        size = rng.uniform(0.85, 2.35) * (0.76 + intensity * 0.28)
        stain_rx = (
            rng.uniform(1.8, 5.8)
            * (0.68 + intensity * 0.34)
            * (0.78 + dist_scale * 0.18)
        )
        stain_ry = stain_rx * rng.uniform(0.34, 0.76)
        drop = {
            "birth_ms": now
            + int(delay_ms)
            + rng.randint(0, max(3, int(45 * min(1.5, intensity)))),
            "flight_ms": flight_ms,
            "origin": origin
            + pygame.Vector2(rng.uniform(-2.2, 2.2), rng.uniform(-1.5, 1.5)),
            "landing": landing,
            "height": max(5.0, float(height) * rng.uniform(0.66, 1.28)),
            "size": size,
            "rx": stain_rx,
            "ry": stain_ry,
            "angle": math.radians(rng.uniform(-34.0, 34.0)),
            "shape": _v81_irregular_shape(rng),
            "grow_ms": rng.randint(640, 1460),
            "decal_added": False,
            "satellite": rng.random() < 0.38,
            "sat_dx": rng.uniform(-7.0, 7.0),
            "sat_dy": rng.uniform(-4.5, 4.5),
            "sat_r": rng.uniform(0.8, 2.2),
        }
        v81_death_blood["drops"].append(drop)

    if seep and len(v81_death_blood["seeps"]) < V81_MAX_SEEPS:
        _v81_add_seep(
            origin,
            rng.uniform(8.0, 14.0) * (0.82 + intensity * 0.30),
            rng.uniform(4.0, 8.0) * (0.82 + intensity * 0.24),
            now + int(delay_ms) + rng.randint(260, 520),
            rng.randint(2100, 4300),
            rng,
        )
    return count


def _v81_add_arterial_sequence(
    origin,
    direction,
    intensity=1.0,
    start_delay=0,
    height=22.0,
    tag=0,
):

    pulse_plan = (
        (0, 27, 1.00, 30.0, 1.00),
        (145, 22, 0.90, 34.0, 0.96),
        (335, 17, 0.72, 39.0, 0.88),
        (585, 11, 0.54, 46.0, 0.76),
    )
    total = 0
    for i, (delay, count, pressure, spread, dist) in enumerate(pulse_plan):
        if len(v81_death_blood["drops"]) >= V81_MAX_DROPLETS:
            break

        rng = _v81_rng(tag * 17 + i)
        pulse_dir = pygame.Vector2(direction).rotate(
            rng.uniform(-7.0, 7.0) + i * rng.uniform(-2.5, 3.5)
        )
        total += _v81_add_burst(
            origin,
            pulse_dir,
            max(5, int(round(count * intensity))),
            intensity=max(0.45, intensity * pressure),
            delay_ms=int(start_delay + delay),
            spread_deg=spread,
            height=height * (0.92 + pressure * 0.20),
            distance_mul=dist,
            seep=(i == 0),
            tag=tag * 101 + i,
        )
    return total
# </POTBO_STAGE S1622>

# <POTBO_STAGE S1624>


def _v81_drop_position(drop, now):
    age = int(now) - int(drop["birth_ms"])
    if age <= 0:
        return None, 0.0, False
    flight = max(1, int(drop["flight_ms"]))
    p = _v81_clamp01(age / float(flight))
    ground = pygame.Vector2(drop["origin"]).lerp(pygame.Vector2(drop["landing"]), p)
    arc = float(drop["height"]) * 4.0 * p * (1.0 - p)
    return ground, arc, p >= 1.0
# </POTBO_STAGE S1624>

# <POTBO_STAGE S1627>


def _v81_draw_seep(seep, now):
    age = int(now) - int(seep["birth_ms"])
    if age <= 0:
        return
    p = _v81_smooth(age / max(1.0, float(seep["grow_ms"])))

    scale = 0.10 + 0.90 * p
    pts = _v81_polygon_points(
        seep["origin"],
        seep["rx"],
        seep["ry"],
        seep["angle"],
        seep["shape"],
        scale,
    )
    if len(pts) >= 3:
        pygame.draw.polygon(ekran, V77_DEATH_BLOOD, pts)
# </POTBO_STAGE S1627>

# <POTBO_STAGE S1634>


_v81_diag_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v81_diag_original()
    data["v81"] = v81_diagnostics()
    return data
# </POTBO_STAGE S1634>

# <POTBO_STAGE S1636>
V81_SLOT_IDLE = (92, 74, 83)
V81_SLOT_MAGIC = (216, 103, 32)
# </POTBO_STAGE S1636>

# <POTBO_STAGE S1638>


def _v81_clamp(v, lo, hi):
    return max(lo, min(hi, v))
# </POTBO_STAGE S1638>

# <POTBO_STAGE S1641>


def _v81_jagged_bar(
    rect,
    ratio,
    fill,
    back,
    border,
    shown_ratio=None,
    warning=False,
    chunk_px=18,
    coarse=True,
):
    rect = pygame.Rect(rect)
    ratio = _v79_clamp01(ratio)
    if shown_ratio is None:
        shown_ratio = ratio
    shown_ratio = _v79_clamp01(shown_ratio)

    _v81_bar_frame(rect, border, back)

    inner = rect.inflate(-2, -2)
    pygame.draw.rect(ekran, back, inner)

    if shown_ratio > ratio + 0.003:
        trail_w = int(round(inner.width * shown_ratio))
        if trail_w > 0:
            trail = pygame.Rect(inner.x, inner.y, trail_w, inner.height)
            pygame.draw.rect(ekran, (70, 36, 41), trail)

    fill_w = int(round(inner.width * ratio))
    if fill_w > 0:
        fill_rect = pygame.Rect(inner.x, inner.y, fill_w, inner.height)
        pygame.draw.rect(ekran, fill, fill_rect)
        highlight = (
            min(255, fill[0] + 34),
            min(255, fill[1] + 34),
            min(255, fill[2] + 34),
        )
        low = (
            max(0, fill[0] - 34),
            max(0, fill[1] - 34),
            max(0, fill[2] - 34),
        )
        pygame.draw.line(
            ekran,
            highlight,
            (fill_rect.left, fill_rect.top),
            (fill_rect.right - 1, fill_rect.top),
            1,
        )
        pygame.draw.line(
            ekran,
            low,
            (fill_rect.left, fill_rect.bottom - 1),
            (fill_rect.right - 1, fill_rect.bottom - 1),
            1,
        )

    step = max(10, int(chunk_px))
    for x in range(inner.left + step, inner.right, step):
        pygame.draw.line(
            ekran,
            (24, 20, 24),
            (x, inner.top),
            (x, inner.bottom - 1),
            1,
        )
        if coarse:
            notch_h = 2 if ((x - inner.left) // step) % 2 == 0 else 3
            pygame.draw.rect(
                ekran,
                V81_HUD_DARK,
                pygame.Rect(x - 1, inner.top, 2, notch_h),
            )
            pygame.draw.rect(
                ekran,
                V81_HUD_DARK,
                pygame.Rect(x - 1, inner.bottom - notch_h, 2, notch_h),
            )

    lip_color = PARLAK_KIRMIZI if warning else border
    pygame.draw.rect(ekran, lip_color, rect, 1)
    if coarse and rect.height >= 12:
        for x in range(rect.left + 9, rect.right - 7, step):
            tooth = [
                (x, rect.top - 1),
                (x + 4, rect.top - 4),
                (x + 8, rect.top - 1),
            ]
            pygame.draw.lines(ekran, border, False, tooth, 1)
# </POTBO_STAGE S1641>

# <POTBO_STAGE S1647>


def _v81_death_ground_anchor(rect, blood=False):
    shadow = pygame.Rect(0, 0, max(20, rect.width - 10), max(5, rect.height // 8))
    shadow.center = (rect.centerx, rect.bottom - 4)
    pygame.draw.ellipse(ekran, V77_DEATH_BLACK, shadow)
    if blood:
        smear = shadow.inflate(
            -max(4, shadow.width // 4),
            -max(1, shadow.height // 3),
        )
        pygame.draw.ellipse(ekran, V77_DEATH_BLOOD, smear)
# </POTBO_STAGE S1647>

# <POTBO_STAGE S1651>


_v81_game_draw_original = oyun_ekrani_ciz
# </POTBO_STAGE S1651>

# <POTBO_STAGE S1654>


_v81_diag_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v81_diag_original()
    data["v81"] = v81_diagnostics()
    return data
# </POTBO_STAGE S1654>

# <POTBO_STAGE S1660>

v82_hit_fx = []
V82_HIT_FX_MAX = 36


def _v82_clamp01(v):
    return max(0.0, min(1.0, float(v)))


def _v82_smooth(v):
    v = _v82_clamp01(v)
    return v * v * (3.0 - 2.0 * v)
# </POTBO_STAGE S1660>

# <POTBO_STAGE S1662>


def _v82_gothic_bar(
    rect,
    ratio,
    fill,
    back,
    border,
    shown_ratio=None,
    warning=False,
):
    rect = pygame.Rect(rect)
    ratio = _v82_clamp01(ratio)
    shown_ratio = ratio if shown_ratio is None else _v82_clamp01(shown_ratio)


    inner = _v82_gothic_shell(
        rect.inflate(8, 6),
        PARLAK_KIRMIZI if warning else border,
        back,
        cut=7,
    )
    inner = pygame.Rect(rect)
    pygame.draw.rect(ekran, back, inner)

    if shown_ratio > ratio + 0.003:
        tw = int(round(inner.width * shown_ratio))
        if tw > 0:
            pygame.draw.rect(
                ekran,
                (67, 29, 37),
                pygame.Rect(inner.x, inner.y, tw, inner.height),
            )

    fw = int(round(inner.width * ratio))
    if fw > 0:
        fr = pygame.Rect(inner.x, inner.y, fw, inner.height)
        pygame.draw.rect(ekran, fill, fr)

        hi = tuple(min(255, int(c) + 31) for c in fill)
        lo = tuple(max(0, int(c) - 28) for c in fill)
        pygame.draw.line(
            ekran,
            hi,
            (fr.left, fr.top),
            (fr.right - 1, fr.top),
            1,
        )
        if fr.height >= 5:
            pygame.draw.line(
                ekran,
                lo,
                (fr.left, fr.bottom - 1),
                (fr.right - 1, fr.bottom - 1),
                1,
            )


    step = 34
    for x in range(inner.left + step, inner.right, step):
        pygame.draw.line(
            ekran,
            (19, 16, 20),
            (x, inner.top + 2),
            (x, inner.bottom - 3),
            1,
        )
        if inner.height >= 14:
            pygame.draw.polygon(
                ekran,
                V82_UI_DARK,
                [
                    (x - 2, inner.top),
                    (x + 2, inner.top),
                    (x, inner.top + 3),
                ],
            )
            pygame.draw.polygon(
                ekran,
                V82_UI_DARK,
                [
                    (x - 2, inner.bottom - 1),
                    (x + 2, inner.bottom - 1),
                    (x, inner.bottom - 4),
                ],
            )


    pygame.draw.line(
        ekran,
        border,
        (inner.right - 1, inner.top + 3),
        (inner.right - 1, inner.bottom - 4),
        1,
    )
# </POTBO_STAGE S1662>

# <POTBO_STAGE S1664>


def _v82_slot_polygon(rect, cut=5):
    r = pygame.Rect(rect)
    c = max(2, min(int(cut), r.width // 5, r.height // 5))
    return [
        (r.left + c, r.top),
        (r.right - c, r.top),
        (r.right, r.top + c),
        (r.right, r.bottom - c),
        (r.right - c, r.bottom),
        (r.left + c, r.bottom),
        (r.left, r.bottom - c),
        (r.left, r.top + c),
    ]
# </POTBO_STAGE S1664>

# <POTBO_STAGE S1667>





def _v82_drop_seed(drop, salt=0):
    return (
        int(drop.get("birth_ms", 0)) * 17
        + int(float(drop.get("rx", 1.0)) * 101)
        + int(float(drop.get("ry", 1.0)) * 211)
        + int(salt) * 7919
    ) & 0x7FFFFFFF
# </POTBO_STAGE S1667>

# <POTBO_STAGE S1682>


_v82_diag_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v82_diag_original()
    data["v82"] = v82_diagnostics()
    return data
# </POTBO_STAGE S1682>

# <POTBO_STAGE S1688>


def _v83_clamp(v, lo, hi):
    return max(lo, min(hi, v))


def _v83_poly(rect, cut=8):
    r = pygame.Rect(rect)
    c = max(2, min(int(cut), r.width // 6, r.height // 4))
    return [
        (r.left + c, r.top),
        (r.right - c, r.top),
        (r.right, r.top + c),
        (r.right, r.bottom - c),
        (r.right - c, r.bottom),
        (r.left + c, r.bottom),
        (r.left, r.bottom - c),
        (r.left, r.top + c),
    ]
# </POTBO_STAGE S1688>

# <POTBO_STAGE S1690>


def _v83_bar(
    rect,
    ratio,
    fill,
    back,
    edge,
    shown_ratio=None,
    warning=False,
    marks=5,
):
    rect = pygame.Rect(rect)
    ratio = _v82_clamp01(ratio)
    shown_ratio = ratio if shown_ratio is None else _v82_clamp01(shown_ratio)
    _v83_bar_shell(rect, PARLAK_KIRMIZI if warning else edge)
    pygame.draw.rect(ekran, back, rect)
    if shown_ratio > ratio + 0.002:
        tw = int(round(rect.width * shown_ratio))
        if tw > 0:
            pygame.draw.rect(
                ekran,
                (68, 29, 36),
                pygame.Rect(rect.x, rect.y, tw, rect.height),
            )
    fw = int(round(rect.width * ratio))
    if fw > 0:
        fr = pygame.Rect(rect.x, rect.y, fw, rect.height)
        pygame.draw.rect(ekran, fill, fr)
        hi = tuple(min(255, c + 26) for c in fill)
        lo = tuple(max(0, c - 26) for c in fill)
        pygame.draw.line(
            ekran,
            hi,
            (fr.left, fr.top),
            (fr.right - 1, fr.top),
            1,
        )
        if fr.height >= 4:
            pygame.draw.line(
                ekran,
                lo,
                (fr.left, fr.bottom - 1),
                (fr.right - 1, fr.bottom - 1),
                1,
            )
    if marks > 1:
        step = max(18, rect.width // marks)
        for x in range(rect.left + step, rect.right, step):
            pygame.draw.line(
                ekran,
                (22, 18, 24),
                (x, rect.top),
                (x, rect.bottom - 1),
                1,
            )
    pygame.draw.rect(ekran, edge, rect, 1)
# </POTBO_STAGE S1690>

# <POTBO_STAGE S1696>


_v83_hit_feedback_original = _v82_apply_hit_feedback
# </POTBO_STAGE S1696>

# <POTBO_STAGE S1698>



def _v83_death_split_surface(surface, center, rot_deg, gap_px):
    draw = pygame.transform.rotate(surface, rot_deg)
    w, h = draw.get_size()
    if w < 2 or h < 2:
        ekran.blit(draw, draw.get_rect(center=center))
        return
    mid = h // 2
    top = pygame.Surface((w, max(1, mid)), pygame.SRCALPHA)
    top.blit(draw, (0, 0), pygame.Rect(0, 0, w, max(1, mid)))
    bot_h = max(1, h - mid)
    bottom = pygame.Surface((w, bot_h), pygame.SRCALPHA)
    bottom.blit(draw, (0, 0), pygame.Rect(0, mid, w, bot_h))
    cx, cy = center
    top_rect = top.get_rect(center=(int(cx - gap_px * 0.25), int(cy - gap_px)))
    bottom_rect = bottom.get_rect(center=(int(cx + gap_px * 0.25), int(cy + gap_px)))
    ekran.blit(top, top_rect)
    ekran.blit(bottom, bottom_rect)
# </POTBO_STAGE S1698>

# <POTBO_STAGE S1701>


_v83_death_fx_original = _v80_make_death_fx
# </POTBO_STAGE S1701>

# <POTBO_STAGE S1710>


_v83_diag_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v83_diag_original()
    data["v83"] = v83_diagnostics()
    return data
# </POTBO_STAGE S1710>

# <POTBO_STAGE S1712>

V84_BLACK = (0, 0, 0)
V84_BLOOD = (116, 0, 18)
# </POTBO_STAGE S1712>

# <POTBO_STAGE S1714>
V84_BODY = (226, 18, 39)
V84_BODY_HOT = (248, 45, 60)
# </POTBO_STAGE S1714>

# <POTBO_STAGE S1716>

V84_PERFECT_GUARD_STRICT_MS = 132
V84_PERFECT_GUARD_STANDARD_MS = 156
V84_PERFECT_GUARD_FRONT_DOT_STRICT = 0.18
V84_PERFECT_GUARD_FRONT_DOT_STANDARD = 0.08
V84_RIPOSTE_WINDOW_MS = 740
# </POTBO_STAGE S1716>

# <POTBO_STAGE S1718>
V84_RIPOSTE_TARGET_GRACE_PX = 132.0
# </POTBO_STAGE S1718>

# <POTBO_STAGE S1721>
V84_WOUND_MAX = 96
# </POTBO_STAGE S1721>

# <POTBO_STAGE S1723>

V84_GUARD_POISE_FRACTIONS = {
    "light": 0.46,
    "medium": 0.36,
    "heavy": 0.24,
}

V84_GUARD_OPENING_MS = {
    "light": 760,
    "medium": 710,
    "heavy": 640,
}
# </POTBO_STAGE S1723>

# <POTBO_STAGE S1725>


def v84_clamp(value, lo, hi):
    return max(float(lo), min(float(hi), float(value)))


def v84_clamp01(value):
    return v84_clamp(value, 0.0, 1.0)


def v84_smoothstep(value):
    t = v84_clamp01(value)
    return t * t * (3.0 - 2.0 * t)


def v84_smootherstep(value):
    t = v84_clamp01(value)
    return t * t * t * (t * (t * 6.0 - 15.0) + 10.0)


def v84_safe_vector(value, fallback=(1.0, 0.0)):
    try:
        vector = pygame.Vector2(value)
    except (TypeError, ValueError):
        vector = pygame.Vector2(fallback)
    if vector.length_squared() <= 1e-8:
        vector = pygame.Vector2(fallback)
    if vector.length_squared() <= 1e-8:
        vector = pygame.Vector2(1.0, 0.0)
    return vector
# </POTBO_STAGE S1725>

# <POTBO_STAGE S1730>


def v84_point_segment_distance(point, start, end):
    point_v = pygame.Vector2(point)
    start_v = pygame.Vector2(start)
    end_v = pygame.Vector2(end)
    segment = end_v - start_v
    length_sq = segment.length_squared()
    if length_sq <= 1e-8:
        return point_v.distance_to(start_v), 0.0, start_v
    t = v84_clamp01((point_v - start_v).dot(segment) / length_sq)
    closest = start_v + segment * t
    return point_v.distance_to(closest), t, closest


def v84_direction_name(vector):
    vector = v84_safe_vector(vector)
    if abs(vector.x) >= abs(vector.y):
        return "right" if vector.x >= 0.0 else "left"
    return "down" if vector.y >= 0.0 else "up"
# </POTBO_STAGE S1730>

# <POTBO_STAGE S1734>


def v84_clip_halfplane(polygon, line_point, normal, keep_positive):
    if not polygon:
        return []
    point = pygame.Vector2(line_point)
    n = v84_safe_vector(normal)

    def signed(vertex):
        value = (pygame.Vector2(vertex) - point).dot(n)
        return value if keep_positive else -value

    output = []
    previous = pygame.Vector2(polygon[-1])
    previous_distance = signed(previous)
    for raw_current in polygon:
        current = pygame.Vector2(raw_current)
        current_distance = signed(current)
        previous_inside = previous_distance >= -1e-6
        current_inside = current_distance >= -1e-6
        if current_inside != previous_inside:
            denominator = previous_distance - current_distance
            if abs(denominator) > 1e-8:
                t = previous_distance / denominator
                crossing = previous.lerp(current, v84_clamp01(t))
                output.append((crossing.x, crossing.y))
        if current_inside:
            output.append((current.x, current.y))
        previous = current
        previous_distance = current_distance
    return output


def v84_polygon_mask(size, polygon):
    width, height = max(1, int(size[0])), max(1, int(size[1]))
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    if len(polygon) >= 3:
        pygame.draw.polygon(
            surface,
            (255, 255, 255, 255),
            [(int(round(x)), int(round(y))) for x, y in polygon],
        )
    return pygame.mask.from_surface(surface, 1)


@dataclass
class V84Fragment:
    mask: Any
    size: tuple
    tone: tuple = V84_BODY
    gap: pygame.Vector2 = field(default_factory=lambda: pygame.Vector2(0.0, 0.0))
    velocity: pygame.Vector2 = field(default_factory=lambda: pygame.Vector2(0.0, 0.0))
    position: pygame.Vector2 = field(default_factory=lambda: pygame.Vector2(0.0, 0.0))
    rotation: float = 0.0
    angular_velocity: float = 0.0
    released: bool = False
    surface: Any = None

    def refresh_surface(self):
        self.surface = self.mask.to_surface(
            setcolor=(*self.tone, 255),
            unsetcolor=(0, 0, 0, 0),
        ).convert_alpha()

    def pixel_count(self):
        try:
            return int(self.mask.count())
        except (AttributeError, TypeError):
            return 0

    def centroid(self):
        try:
            x, y = self.mask.centroid()
            return pygame.Vector2(float(x), float(y))
        except (AttributeError, TypeError, ValueError):
            return pygame.Vector2(
                float(self.size[0]) * 0.5,
                float(self.size[1]) * 0.5,
            )

    def update(self, dt):
        if not self.released:
            return
        self.position += self.velocity * float(dt)
        self.velocity.x *= math.exp(-1.15 * float(dt))
        self.velocity.y += 430.0 * float(dt)
        self.rotation += self.angular_velocity * float(dt)
        self.angular_velocity *= math.exp(-0.75 * float(dt))

    def draw(self, anchor_midbottom):
        if self.surface is None:
            self.refresh_surface()
        width, height = self.size
        center = pygame.Vector2(
            float(anchor_midbottom[0]),
            float(anchor_midbottom[1]) - float(height) * 0.5,
        )
        center += self.gap + self.position
        image = self.surface
        if abs(self.rotation) > 0.01:
            image = pygame.transform.rotate(image, self.rotation)
        rect = image.get_rect(center=(int(round(center.x)), int(round(center.y))))
        ekran.blit(image, rect)
# </POTBO_STAGE S1734>

# <POTBO_STAGE S1738>


v84_guard_pressed_ms = -10000
v84_guard_press_serial = 0
v84_guard_last_contact_ms = -10000
v84_guard_last_quality = 0.0
# </POTBO_STAGE S1738>

# <POTBO_STAGE S1740>
v84_guard_flash_until = 0
v84_guard_flash_started_ms = 0
v84_guard_label_until = 0
v84_poise_break_windows = {}
# </POTBO_STAGE S1740>

# <POTBO_STAGE S1742>
v84_riposte_state = V84RiposteState()
# </POTBO_STAGE S1742>

# <POTBO_STAGE S1744>
v84_perfect_guard_total = 0
v84_riposte_total = 0
v84_normal_guard_total = 0
# </POTBO_STAGE S1744>

# <POTBO_STAGE S1748>


def v84_guard_quality(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    elapsed = int(now) - int(v84_guard_pressed_ms)
    window = max(1, v84_perfect_guard_window_ms())
    if elapsed < 0 or elapsed > window:
        return 0.0
    normalized = elapsed / float(window)


    center_distance = abs(normalized - 0.48) / 0.52
    return v84_clamp(
        1.0 - 0.24 * v84_smoothstep(center_distance),
        0.76,
        1.0,
    )
# </POTBO_STAGE S1748>

# <POTBO_STAGE S1750>


def v84_actor_poise_max(actor):
    if actor is None:
        return 0.0
    cfg = getattr(actor, "cfg", {}) or {}
    return max(0.0, float(cfg.get("poise_max", 0.0)))
# </POTBO_STAGE S1750>

# <POTBO_STAGE S1783>


v84_wounds = {}
# </POTBO_STAGE S1783>

# <POTBO_STAGE S1786>


def v84_actor_has_open_wound(actor):
    now = pygame.time.get_ticks()
    return any(wound.alive(now) for wound in v84_wounds_for_actor(actor))
# </POTBO_STAGE S1786>

# <POTBO_STAGE S1788>


def v84_wound_tick(now, dt):
    stale = []
    for key, wound in list(v84_wounds.items()):
        if not wound.alive(now):
            stale.append(key)
            continue
        wound.pressure *= math.exp(-0.085 * float(dt))
        if int(now) >= int(wound.next_emit_ms):
            v84_wound_emit(wound, now)
    for key in stale:
        v84_wounds.pop(key, None)
# </POTBO_STAGE S1788>

# <POTBO_STAGE S1791>


_v84_dev_input_original = gelistirici_test_girdisi_uygula
# </POTBO_STAGE S1791>

# <POTBO_STAGE S1793>


GELISTIRICI_TEST_TUSLARI.update({pygame.K_y})
# </POTBO_STAGE S1793>

# <POTBO_STAGE S1799>


@dataclass
class V84DeathState:
    built: bool = False
    seed: int = 0
    profile: str = ""
    source: str = ""
    source_position: pygame.Vector2 = field(
        default_factory=lambda: pygame.Vector2(0.0, 0.0)
    )
    fracture: Any = None
    created_ms: int = 0
    last_tick_ms: int = 0
    cut_count: int = 0
    direction: pygame.Vector2 = field(default_factory=lambda: pygame.Vector2(1.0, 0.0))

    def reset(self):
        self.built = False
        self.seed = 0
        self.profile = ""
        self.source = ""
        self.source_position = pygame.Vector2(0.0, 0.0)
        self.fracture = None
        self.created_ms = 0
        self.last_tick_ms = 0
        self.cut_count = 0
        self.direction = pygame.Vector2(1.0, 0.0)


v84_death_state = V84DeathState()
# </POTBO_STAGE S1799>

# <POTBO_STAGE S1808>


def karakter_zemin_golgesi_ciz(
    x,
    y,
    genislik,
    yukseklik,
    alpha=72,
):
    """Keskin, küçük bir temas plakası; oval aura üretmez."""
    width = max(6, int(round(genislik)))
    height = max(3, int(round(yukseklik)))
    left = int(round(float(x) - width * 0.5))
    top = int(round(float(y) - height * 0.5))
    cut = max(1, min(height - 1, width // 8))
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    color = (0, 0, 0, max(0, min(150, int(alpha))))
    polygon = (
        (cut, 0),
        (width - cut - 1, 0),
        (width - 1, height // 2),
        (width - cut * 2, height - 1),
        (cut * 2, height - 1),
        (0, height // 2),
    )
    pygame.draw.polygon(surface, color, polygon)
    ekran.blit(surface, (left, top))
# </POTBO_STAGE S1808>

# <POTBO_STAGE S1811>


def v84_guard_flash_draw():
    now = pygame.time.get_ticks()
    if int(now) >= int(v84_guard_flash_until):
        return
    duration = max(
        1.0,
        float(v84_guard_flash_until - v84_guard_flash_started_ms),
    )
    progress = v84_clamp01((int(now) - int(v84_guard_flash_started_ms)) / duration)
    alpha = int(round(72 * (1.0 - v84_smoothstep(progress))))
    layer = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    layer.fill((*V84_BODY, alpha))
    ekran.blit(layer, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)
# </POTBO_STAGE S1811>

# <POTBO_STAGE S1813>


_v84_game_draw_original = oyun_ekrani_ciz
# </POTBO_STAGE S1813>

# <POTBO_STAGE S1820>


def v84_fracture_contract():
    surface = pygame.Surface((24, 36), pygame.SRCALPHA)
    pygame.draw.polygon(
        surface,
        (*V84_BODY, 255),
        (
            (12, 1),
            (22, 9),
            (20, 34),
            (4, 34),
            (2, 9),
        ),
    )
    field = V84FractureField(surface, max_fragments=16)
    before = sum(fragment.pixel_count() for fragment in field.fragments)
    field.cut(27.0, 0.0, 1.0)
    field.cut(-34.0, 0.08, 1.0)
    after = sum(fragment.pixel_count() for fragment in field.fragments)
    return {
        "pixel_conservation": before == after,
        "split_created": len(field.fragments) >= 3,
        "fragment_cap_respected": len(field.fragments) <= 16,
        "before_pixels": before,
        "after_pixels": after,
        "fragments": len(field.fragments),
    }
# </POTBO_STAGE S1820>

# <POTBO_STAGE S1822>


_v84_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v84_diagnostics_original()
    data["v84"] = v84_diagnostics()
    return data


V84_STARTUP_CONTRACT = {
    "timing": v84_timing_contract(),
    "palette": v84_palette_contract(),
}
# </POTBO_STAGE S1822>

# <POTBO_STAGE S1825>


def v85_fragment_runtime_defaults(fragment):
    if not hasattr(fragment, "height_z"):
        fragment.height_z = 0.0
    if not hasattr(fragment, "vertical_velocity"):
        fragment.vertical_velocity = 0.0
    if not hasattr(fragment, "settled"):
        fragment.settled = False
    if not hasattr(fragment, "ground_y_scale"):
        fragment.ground_y_scale = 0.54
    if not hasattr(fragment, "bounce_count"):
        fragment.bounce_count = 0
    if not hasattr(fragment, "release_delay"):
        fragment.release_delay = 0.0


def v85_fragment_launch(
    fragment,
    direction,
    speed,
    vertical_speed,
    angular_speed,
    delay=0.0,
):
    v85_fragment_runtime_defaults(fragment)
    ground_direction = v84_safe_vector(direction).normalize()
    fragment.velocity = ground_direction * max(0.0, float(speed))
    fragment.vertical_velocity = max(0.0, float(vertical_speed))
    fragment.height_z = max(0.0, float(fragment.height_z))
    fragment.angular_velocity = float(angular_speed)
    fragment.released = True
    fragment.settled = False
    fragment.release_delay = max(0.0, float(delay))
    fragment.bounce_count = 0


def _v85_fragment_update(self, dt):
    if not self.released:
        return
    v85_fragment_runtime_defaults(self)
    dt = max(0.0, min(0.05, float(dt)))
    if self.release_delay > 0.0:
        self.release_delay = max(0.0, self.release_delay - dt)
        return
    if self.settled:
        return



    self.position += self.velocity * dt
    self.height_z += self.vertical_velocity * dt
    self.vertical_velocity -= 520.0 * dt
    self.rotation += self.angular_velocity * dt
    self.velocity *= math.exp(-1.45 * dt)
    self.angular_velocity *= math.exp(-1.25 * dt)

    if self.height_z <= 0.0 and self.vertical_velocity < 0.0:
        self.height_z = 0.0
        impact = abs(self.vertical_velocity)
        self.bounce_count += 1
        if impact > 82.0 and self.bounce_count <= 2:
            self.vertical_velocity = impact * (0.24 if self.bounce_count == 1 else 0.13)
            self.velocity *= 0.64
            self.angular_velocity *= 0.58
        else:
            self.vertical_velocity = 0.0
            self.velocity *= 0.24
            if self.velocity.length() < 10.0:
                self.velocity.update(0.0, 0.0)
                self.angular_velocity = 0.0
                self.settled = True


def _v85_fragment_draw(self, anchor_midbottom, base_rotation=0.0):
    if self.surface is None:
        self.refresh_surface()
    v85_fragment_runtime_defaults(self)
    width, height = self.size
    base_center = pygame.Vector2(
        float(anchor_midbottom[0]),
        float(anchor_midbottom[1]) - float(height) * 0.5,
    )
    rotated_gap = pygame.Vector2(self.gap).rotate(-float(base_rotation))
    ground = pygame.Vector2(
        self.position.x,
        self.position.y * float(self.ground_y_scale),
    )
    center = base_center + rotated_gap + ground
    center.y -= self.height_z * 0.74

    if self.released and self.height_z > 1.0:
        ground_center = base_center + rotated_gap + ground
        shadow_w = max(3, min(15, int(width * 0.18)))
        shadow_h = max(2, min(6, int(height * 0.07)))
        pygame.draw.polygon(
            ekran,
            V84_BLACK,
            (
                (
                    int(ground_center.x - shadow_w),
                    int(ground_center.y),
                ),
                (
                    int(ground_center.x),
                    int(ground_center.y - shadow_h),
                ),
                (
                    int(ground_center.x + shadow_w),
                    int(ground_center.y),
                ),
                (
                    int(ground_center.x),
                    int(ground_center.y + shadow_h),
                ),
            ),
        )

    image = self.surface
    rotation = float(base_rotation) + float(self.rotation)
    if abs(rotation) > 0.01:
        image = pygame.transform.rotate(image, rotation)
    rect = image.get_rect(center=(int(round(center.x)), int(round(center.y))))
    ekran.blit(image, rect)


def _v85_fracture_draw(self, anchor_midbottom, base_rotation=0.0):
    ordered = sorted(
        self.fragments,
        key=lambda fragment: (
            0 if fragment.released else 1,
            float(getattr(fragment, "position", pygame.Vector2()).y),
        ),
    )
    for fragment in ordered:
        fragment.draw(anchor_midbottom, base_rotation)
# </POTBO_STAGE S1825>

# <POTBO_STAGE S1827>


V84Fragment.update = _v85_fragment_update
V84Fragment.draw = _v85_fragment_draw
V84FractureField.draw = _v85_fracture_draw
V84FractureField.release = _v85_fracture_release


def v85_fracture_cut_one(
    field,
    angle,
    offset_ratio,
    gap_px,
    seed,
    detach=True,
):
    if field is None or field.released:
        return 0
    if len(field.fragments) >= int(field.max_fragments):
        return 0
    rng = random.Random(int(seed) ^ (len(field.fragments) * 0x9E37))
    candidates = [
        (index, fragment)
        for index, fragment in enumerate(field.fragments)
        if not fragment.released and fragment.pixel_count() >= 18
    ]
    candidates.sort(key=lambda pair: pair[1].pixel_count(), reverse=True)
    if not candidates:
        return 0

    for candidate_index, fragment in candidates[:5]:




        angle_offsets = (
            0.0,
            6.0,
            -6.0,
            12.0,
            -12.0,
            20.0,
            -20.0,
            34.0,
            -34.0,
            90.0,
        )
        width, height = field.size
        opaque = [
            (x, y)
            for y in range(height)
            for x in range(width)
            if fragment.mask.get_at((x, y))
        ]
        if len(opaque) < 8:
            continue
        side_sign = (
            1
            if float(offset_ratio) > 0.001
            else -1
            if float(offset_ratio) < -0.001
            else rng.choice((-1, 1))
        )
        for attempt, angle_offset in enumerate(angle_offsets):
            local_angle = float(angle) + angle_offset
            direction = pygame.Vector2(1.0, 0.0).rotate(local_angle)
            normal = direction.rotate(90.0).normalize()
            projections = sorted(
                float(x) * normal.x + float(y) * normal.y for x, y in opaque
            )
            fraction = v84_clamp(
                0.068 + abs(float(offset_ratio)) * 0.10 + (attempt % 5) * 0.018,
                0.055,
                0.18,
            )
            if side_sign > 0:
                quantile = 1.0 - fraction
            else:
                quantile = fraction
            projection_index = max(
                1,
                min(
                    len(projections) - 2,
                    int(round((len(projections) - 1) * quantile)),
                ),
            )
            threshold = projections[projection_index]
            line_point = normal * threshold
            positive_mask, _ = field._side_masks(line_point, normal)
            positive = fragment.mask.overlap_mask(positive_mask, (0, 0))
            negative = fragment.mask.copy()
            negative.erase(positive, (0, 0))
            positive_count = int(positive.count())
            negative_count = int(negative.count())
            total = max(1, fragment.pixel_count())
            minimum = max(3, int(total * 0.025))
            if positive_count < minimum or negative_count < minimum:
                continue

            child_a = V84Fragment(
                positive,
                field.size,
                tone=fragment.tone,
                gap=pygame.Vector2(fragment.gap) + normal * float(gap_px),
            )
            child_b = V84Fragment(
                negative,
                field.size,
                tone=fragment.tone,
                gap=pygame.Vector2(fragment.gap) - normal * float(gap_px),
            )
            child_a.refresh_surface()
            child_b.refresh_surface()
            if child_a.pixel_count() <= child_b.pixel_count():
                detached, main = child_a, child_b
            else:
                detached, main = child_b, child_a

            replacement = [main, detached] if detach else [child_a, child_b]
            field.fragments[candidate_index : candidate_index + 1] = replacement
            field.cut_count += 1
            if detach:
                cut_normal = direction.rotate(90.0)
                if detached.gap.dot(cut_normal) < main.gap.dot(cut_normal):
                    cut_normal *= -1.0
                v85_fragment_launch(
                    detached,
                    cut_normal.rotate(rng.uniform(-18.0, 18.0)),
                    rng.uniform(42.0, 96.0),
                    rng.uniform(54.0, 128.0),
                    rng.uniform(-430.0, 430.0),
                )
            return 1
    return 0
# </POTBO_STAGE S1827>

# <POTBO_STAGE S1837>





V85_MORTAL_FINAL_HIT_MS = 780
# </POTBO_STAGE S1837>

# <POTBO_STAGE S1839>
V85_DEATH_COLLAPSE_MS = 430
V85_DEATH_RELEASE_MS = 350
V85_DEATH_ARTERIAL_MS = 3200
V85_DEATH_FLOW_GROW_MS = 2600
# </POTBO_STAGE S1839>

# <POTBO_STAGE S1844>
V73_DEATH_ARTERY_AIR_COUNT = 0.52
# </POTBO_STAGE S1844>

# <POTBO_STAGE S1846>


@dataclass
class V85DeathState:
    built: bool = False
    seed: int = 0
    profile: str = ""
    source: str = ""
    source_position: pygame.Vector2 = field(
        default_factory=lambda: pygame.Vector2(0.0, 0.0)
    )
    fracture: Any = None
    created_ms: int = 0
    last_tick_ms: int = 0
    cut_count: int = 0
    direction: pygame.Vector2 = field(default_factory=lambda: pygame.Vector2(1.0, 0.0))
    variant: str = "minor"
    artery_zone: str = "neck"
    released: bool = False
    rotation_sign: float = 1.0
    ground_flows: list = field(default_factory=list)
    tissue_spawned: int = 0

    def reset(self):
        self.built = False
        self.seed = 0
        self.profile = ""
        self.source = ""
        self.source_position = pygame.Vector2(0.0, 0.0)
        self.fracture = None
        self.created_ms = 0
        self.last_tick_ms = 0
        self.cut_count = 0
        self.direction = pygame.Vector2(1.0, 0.0)
        self.variant = "minor"
        self.artery_zone = "neck"
        self.released = False
        self.rotation_sign = 1.0
        self.ground_flows = []
        self.tissue_spawned = 0


v85_mortal_wound_state = V85MortalWoundState()
v85_forcing_final_hit = False
v84_death_state = V85DeathState()
# </POTBO_STAGE S1846>

# <POTBO_STAGE S1857>


def v85_ground_flow_build(origin, direction, seed, count):
    rng = random.Random(int(seed) ^ 0xF10A85)
    origin = pygame.Vector2(origin)
    base_angle = v84_safe_vector(direction).as_polar()[1]
    flows = []
    for index in range(max(1, int(count))):
        angle = (
            base_angle + rng.uniform(-74.0, 74.0)
            if index < max(2, count // 3)
            else rng.uniform(-180.0, 180.0)
        )
        heading = pygame.Vector2(1.0, 0.0).rotate(angle)
        point = origin + heading.rotate(90.0) * rng.uniform(-5.0, 5.0)
        points = [point.copy()]
        target_length = rng.uniform(34.0, 124.0)
        traveled = 0.0
        while traveled < target_length and len(points) < 15:
            step = min(rng.uniform(6.0, 12.0), target_length - traveled)
            heading = heading.rotate(rng.uniform(-9.0, 9.0)).normalize()
            candidate = point + heading * step
            if "v74_floor_clean" in globals() and not v74_floor_clean(
                candidate.x, candidate.y
            ):
                break
            points.append(candidate.copy())
            point = candidate
            traveled += step
        if len(points) >= 2:
            flows.append(
                {
                    "points": points,
                    "delay": rng.randint(30, 680),
                    "duration": rng.randint(1350, 2750),
                    "width": rng.choice((1, 1, 2, 2, 3)),
                    "pool": rng.uniform(2.0, 6.0),
                }
            )
    return flows
# </POTBO_STAGE S1857>

# <POTBO_STAGE S1859>


def v85_local_shape_points(center, vertices, angle, scale):
    rotation = pygame.Vector2(1.0, 0.0).rotate(float(angle))
    tangent = rotation.rotate(90.0)
    return [
        (
            int(round(center[0] + (x * rotation.x + y * tangent.x) * scale)),
            int(round(center[1] + (x * rotation.y + y * tangent.y) * scale)),
        )
        for x, y in vertices
    ]
# </POTBO_STAGE S1859>

# <POTBO_STAGE S1862>


def v85_death_release(state):
    if state.released:
        return
    state.released = True
    if state.fracture is not None:
        power = {
            "decap": 0.62,
            "bisect": 0.76,
            "torso": 0.94,
            "shatter": 1.30,
        }.get(state.variant, 0.70)
        state.fracture.release(
            impulse=state.direction,
            power=power,
            seed=state.seed,
        )
# </POTBO_STAGE S1862>

# <POTBO_STAGE S1873>





V85_HOLD_CROSS_MS = 178
V85_HOLD_EXIT_CLEARANCE = 54.0
# </POTBO_STAGE S1873>

# <POTBO_STAGE S1875>


v85_hold_cross_state = V85HoldCrossState()
# </POTBO_STAGE S1875>

# <POTBO_STAGE S1883>


def v85_cut_rect_points(rect, cut=0):
    rect = pygame.Rect(rect)
    cut = max(0, min(int(cut), rect.width // 3, rect.height // 3))
    if cut <= 0:
        return (
            rect.topleft,
            rect.topright,
            rect.bottomright,
            rect.bottomleft,
        )
    return (
        (rect.left + cut, rect.top),
        (rect.right - cut, rect.top),
        (rect.right, rect.top + cut),
        (rect.right, rect.bottom - cut),
        (rect.right - cut, rect.bottom),
        (rect.left + cut, rect.bottom),
        (rect.left, rect.bottom - cut),
        (rect.left, rect.top + cut),
    )
# </POTBO_STAGE S1883>

# <POTBO_STAGE S1885>


def slot_ciz(
    rect,
    secili=False,
    numara=None,
    item_index=None,
    tasima_kaynagi=False,
):
    v85_slot_shell(
        rect,
        selected=secili,
        transfer=tasima_kaynagi,
        magic=False,
    )
    v85_slot_contents(rect, numara, item_index)
# </POTBO_STAGE S1885>

# <POTBO_STAGE S1890>


_v85_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v85_diagnostics_original()
    data["v85"] = v85_diagnostics()
    return data


V85_STARTUP_CONTRACT = v85_diagnostics()
# </POTBO_STAGE S1890>

# <POTBO_STAGE S1899>





V84_PERFECT_GUARD_STRICT_MS = 184
V84_PERFECT_GUARD_STANDARD_MS = 212
V84_PERFECT_GUARD_FRONT_DOT_STRICT = 0.04
V84_PERFECT_GUARD_FRONT_DOT_STANDARD = -0.10
V84_RIPOSTE_WINDOW_MS = 800
# </POTBO_STAGE S1899>

# <POTBO_STAGE S1901>
V86_GUARD_INTENT_BUFFER_MS = 84
v86_guard_intent_until_ms = -10000
# </POTBO_STAGE S1901>

# <POTBO_STAGE S1903>


_v86_dev_input_original = gelistirici_test_girdisi_uygula
# </POTBO_STAGE S1903>

# <POTBO_STAGE S1907>
V86_DEATH_HISTORY_MS = 16000
V86_DEATH_MAX_BODY_PIECES = 38
V81_MAX_DROPLETS = max(V81_MAX_DROPLETS, 480)
# </POTBO_STAGE S1907>

# <POTBO_STAGE S1909>


@dataclass
class V86CorpsePiece:
    surface: Any
    local_center: pygame.Vector2
    position: pygame.Vector2 = field(default_factory=lambda: pygame.Vector2(0.0, 0.0))
    velocity: pygame.Vector2 = field(default_factory=lambda: pygame.Vector2(0.0, 0.0))
    z: float = 0.0
    vz: float = 0.0
    rotation: float = 0.0
    angular_velocity: float = 0.0
    delay: float = 0.0
    burning: bool = False
    settled: bool = False
    bounce_count: int = 0
    tone: tuple = V84_BODY

    def update(self, dt):
        dt = max(0.0, min(0.05, float(dt)))
        if self.delay > 0.0:
            self.delay = max(0.0, self.delay - dt)
            return
        if self.settled:
            return
        self.position += self.velocity * dt
        self.z += self.vz * dt
        self.vz -= 570.0 * dt
        self.velocity *= math.exp(-1.38 * dt)
        self.rotation += self.angular_velocity * dt
        self.angular_velocity *= math.exp(-1.12 * dt)
        if self.z <= 0.0 and self.vz < 0.0:
            self.z = 0.0
            impact = abs(self.vz)
            self.bounce_count += 1
            if impact > 92.0 and self.bounce_count <= 2:
                self.vz = impact * (0.23 if self.bounce_count == 1 else 0.11)
                self.velocity *= 0.61
                self.angular_velocity *= 0.55
            else:
                self.vz = 0.0
                self.velocity *= 0.19
                if self.velocity.length() < 9.0:
                    self.velocity.update(0.0, 0.0)
                    self.angular_velocity = 0.0
                    self.settled = True


@dataclass
class V86Debris:
    position: pygame.Vector2
    velocity: pygame.Vector2
    z: float
    vz: float
    size: float
    rotation: float
    angular_velocity: float
    kind: str = "rock"
    burning: bool = False
    settled: bool = False

    def update(self, dt):
        if self.settled:
            return
        dt = max(0.0, min(0.05, float(dt)))
        self.position += self.velocity * dt
        self.z += self.vz * dt
        self.vz -= 590.0 * dt
        self.velocity *= math.exp(-1.46 * dt)
        self.rotation += self.angular_velocity * dt
        if self.z <= 0.0 and self.vz < 0.0:
            self.z = 0.0
            if abs(self.vz) > 95.0:
                self.vz = abs(self.vz) * 0.17
                self.velocity *= 0.54
            else:
                self.vz = 0.0
                self.velocity.update(0.0, 0.0)
                self.settled = True


@dataclass
class V86DeathRock:
    start: pygame.Vector2
    target: pygame.Vector2
    started_ms: int
    impact_ms: int
    arc_height: float = 52.0
    second: bool = False
# </POTBO_STAGE S1909>

# <POTBO_STAGE S1911>


v86_death_state = V86DeathState()


def v86_mask_surface(mask, tone=V84_BODY):
    if mask is None or int(mask.count()) <= 0:
        return None
    return mask.to_surface(
        setcolor=(*tone, 255), unsetcolor=(0, 0, 0, 0)
    ).convert_alpha()


def v86_root_refresh(state):
    state.root_surface = v86_mask_surface(state.remaining_mask)


def v86_mask_bounds(mask):
    rectangles = list(mask.get_bounding_rects()) if mask is not None else []
    if not rectangles:
        return None
    result = pygame.Rect(rectangles[0])
    for rect in rectangles[1:]:
        result.union_ip(rect)
    return result


def v86_piece_from_mask(mask, tone=V84_BODY):
    if mask is None or int(mask.count()) <= 0:
        return None
    bounds = v86_mask_bounds(mask)
    if bounds is None or bounds.width <= 0 or bounds.height <= 0:
        return None
    full = v86_mask_surface(mask, tone)
    cropped = full.subsurface(bounds).copy()
    width, height = mask.get_size()
    local = pygame.Vector2(
        bounds.centerx - width * 0.5,
        bounds.centery - height * 0.5,
    )
    return V86CorpsePiece(cropped, local, tone=tone)


def v86_take_mask(state, predicate):
    if state.remaining_mask is None:
        return None
    width, height = state.base_size
    selected = pygame.Mask((width, height), fill=False)
    for y in range(height):
        for x in range(width):
            if state.remaining_mask.get_at((x, y)) and predicate(x, y):
                selected.set_at((x, y), 1)
    if selected.count() <= 0:
        return None
    state.remaining_mask.erase(selected, (0, 0))
    v86_root_refresh(state)
    return selected


def v86_launch_piece(
    state,
    mask,
    direction,
    speed,
    vertical_speed,
    angular_speed,
    delay=0.0,
    burning=False,
    tone=V84_BODY,
):
    if len(state.pieces) >= V86_DEATH_MAX_BODY_PIECES:
        return None
    piece = v86_piece_from_mask(mask, tone)
    if piece is None:
        return None
    direction = v84_safe_vector(direction).normalize()
    piece.velocity = direction * max(0.0, float(speed))
    piece.vz = max(0.0, float(vertical_speed))
    piece.z = 0.0
    piece.angular_velocity = float(angular_speed)
    piece.delay = max(0.0, float(delay))
    piece.burning = bool(burning)
    state.pieces.append(piece)
    return piece


def v86_remaining_points(state):
    if state.remaining_mask is None:
        return []
    width, height = state.base_size
    return [
        (x, y)
        for y in range(height)
        for x in range(width)
        if state.remaining_mask.get_at((x, y))
    ]


def v86_bite_mask(state, fraction, rng):
    points = v86_remaining_points(state)
    if not points:
        return None
    minimum_remainder = max(18, int(state.original_pixels * 0.19))
    available = max(0, len(points) - minimum_remainder)
    target_count = min(
        available,
        max(5, int(round(state.original_pixels * float(fraction)))),
    )
    if target_count <= 0:
        return None
    point_set = set(points)
    boundary = []
    cardinal = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for point in points:
        x, y = point
        if any((x + dx, y + dy) not in point_set for dx, dy in cardinal):
            boundary.append(point)
    if not boundary:
        boundary = points


    preferred_band = rng.randrange(4)
    banded = [
        point
        for point in boundary
        if int(point[1] * 4 / max(1, state.base_size[1])) == preferred_band
    ]
    seed = rng.choice(banded or boundary)
    selected = {seed}
    frontier = [seed]
    neighbors = (
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (-1, 1),
        (1, -1),
        (-1, -1),
    )
    while frontier and len(selected) < target_count:
        current = frontier.pop(rng.randrange(len(frontier)))
        ordered = list(neighbors)
        rng.shuffle(ordered)
        for dx, dy in ordered:
            candidate = (current[0] + dx, current[1] + dy)
            if candidate in point_set and candidate not in selected:
                selected.add(candidate)
                frontier.append(candidate)
                if len(selected) >= target_count:
                    break
        if not frontier and len(selected) < target_count:
            edge = [
                p
                for p in selected
                if any(
                    (p[0] + dx, p[1] + dy) in point_set
                    and (p[0] + dx, p[1] + dy) not in selected
                    for dx, dy in cardinal
                )
            ]
            frontier.extend(edge)
    mask = pygame.Mask(state.base_size, fill=False)
    for point in selected:
        mask.set_at(point, 1)
    state.remaining_mask.erase(mask, (0, 0))
    v86_root_refresh(state)
    return mask


def v86_partition_mask(mask, count, seed):
    if mask is None or mask.count() <= 0:
        return []
    width, height = mask.get_size()
    points = [
        (x, y) for y in range(height) for x in range(width) if mask.get_at((x, y))
    ]
    if not points:
        return []
    rng = random.Random(int(seed) ^ 0x86B0B)
    count = max(1, min(int(count), len(points)))
    seeds = [rng.choice(points)]


    while len(seeds) < count:
        sample = points if len(points) < 420 else rng.sample(points, 420)
        candidate = max(
            sample,
            key=lambda point: min(
                (point[0] - sx) ** 2 + (point[1] - sy) ** 2 for sx, sy in seeds
            )
            + rng.uniform(-6.0, 6.0),
        )
        if candidate in seeds:
            candidate = rng.choice(points)
        seeds.append(candidate)
    regions = [pygame.Mask((width, height), fill=False) for _ in seeds]
    for x, y in points:
        index = min(
            range(len(seeds)),
            key=lambda i: (
                (x - seeds[i][0]) ** 2
                + (y - seeds[i][1]) ** 2
                + ((i * 17 + x * 3 + y * 5) % 7) * 0.23
            ),
        )
        regions[index].set_at((x, y), 1)
    return [region for region in regions if region.count() >= 2]


def v86_spawn_debris(
    state, origin, direction, count, power, kind="organ", burning=False
):
    rng = random.Random(state.seed ^ len(state.debris) * 0x91A3 ^ int(power * 101))
    base = v84_safe_vector(direction).normalize()
    for index in range(max(0, int(count))):
        heading = base.rotate(rng.uniform(-92.0, 92.0))
        if index % 9 == 7:
            heading *= -1.0
        state.debris.append(
            V86Debris(
                position=pygame.Vector2(origin),
                velocity=heading * rng.uniform(64.0, 205.0) * float(power),
                z=rng.uniform(4.0, 16.0),
                vz=rng.uniform(75.0, 220.0) * float(power),
                size=rng.uniform(1.6, 4.8) * (1.18 if kind == "organ" else 1.0),
                rotation=rng.uniform(-180.0, 180.0),
                angular_velocity=rng.uniform(-620.0, 620.0),
                kind=str(kind),
                burning=bool(burning),
            )
        )
# </POTBO_STAGE S1911>

# <POTBO_STAGE S1913>


def v86_start_fall(state, now, duration=430, push=None, rotation=None):
    if state.fall_started_ms > 0:
        return
    state.fall_started_ms = int(now)
    state.fall_duration_ms = max(180, int(duration))
    if push is not None:
        state.body_push = pygame.Vector2(push)
    if rotation is None:
        rotation = -90.0 if state.source_position.x <= state.body_anchor.x else 90.0
    state.fall_target_rotation = float(rotation)
# </POTBO_STAGE S1913>

# <POTBO_STAGE S1924>


def v86_head_region_shatter(state, now):
    if "head_shatter" in state.events:
        return
    state.events.add("head_shatter")
    height = state.base_size[1]
    head_mask = v86_take_mask(state, lambda _x, y: y < height * 0.31)
    direction = v86_impact_direction(state)
    if head_mask is not None:
        regions = v86_partition_mask(head_mask, 10, state.seed ^ 0x4EAD86)
        rng = random.Random(state.seed ^ 0x486EAD)
        for index, region in enumerate(regions):
            v86_launch_piece(
                state,
                region,
                direction.rotate(rng.uniform(-78.0, 78.0)),
                rng.uniform(145.0, 310.0) * state.intensity,
                rng.uniform(150.0, 310.0) * min(1.45, state.intensity),
                rng.uniform(-790.0, 790.0),
                delay=index * 0.008,
            )


    eye_direction = direction.rotate(-31.0)
    state.debris.append(
        V86Debris(
            position=state.body_anchor + pygame.Vector2(0.0, -24.0),
            velocity=eye_direction * 238.0 * state.intensity,
            z=14.0,
            vz=236.0 * min(1.4, state.intensity),
            size=3.6,
            rotation=0.0,
            angular_velocity=520.0,
            kind="eye",
        )
    )
    v86_blood_event(
        state,
        direction,
        2.24,
        zone="head",
        tag=610,
        organs=12,
        arterial=True,
    )
    v86_spawn_debris(
        state,
        state.body_anchor + pygame.Vector2(0.0, -23.0),
        direction,
        17,
        1.32 * state.intensity,
        "organ",
    )
    state.head_destroyed = True
    v86_start_fall(
        state,
        now,
        390,
        push=direction * 29.0,
        rotation=-90.0 if direction.x >= 0.0 else 90.0,
    )
    kamera_hit_sarsintisi_baslat(14.8, 315)


def v86_rock_shatter(state, second=False):
    rng = random.Random(state.seed ^ (0x8622 if second else 0x8611))
    origin = state.body_anchor + pygame.Vector2(0.0, -25.0)
    direction = v86_impact_direction(state)
    v86_spawn_debris(
        state,
        origin,
        direction,
        15 if second else 10,
        1.32 if second else 0.92,
        "rock",
    )
    for _ in range(6 if second else 4):
        point = origin + pygame.Vector2(rng.uniform(-5.0, 5.0), rng.uniform(-4.0, 4.0))
        state.debris.append(
            V86Debris(
                position=point,
                velocity=direction.rotate(rng.uniform(-110.0, 110.0))
                * rng.uniform(90.0, 215.0),
                z=rng.uniform(2.0, 12.0),
                vz=rng.uniform(85.0, 205.0),
                size=rng.uniform(2.0, 4.2),
                rotation=rng.uniform(-180.0, 180.0),
                angular_velocity=rng.uniform(-680.0, 680.0),
                kind="rock",
            )
        )
# </POTBO_STAGE S1924>

# <POTBO_STAGE S1927>


def v86_frame_progress(frames, progress):
    if not frames:
        return None
    progress = v84_clamp01(progress)
    return frames[min(len(frames) - 1, int(progress * len(frames)))]
# </POTBO_STAGE S1927>

# <POTBO_STAGE S1929>


_v86_killer_frame_original = _v30_katil_koreografi_frame


def _v30_katil_koreografi_frame(actor, simdi):
    if v86_death_state.active and actor is v86_death_state.killer:
        return v86_death_actor_frame(actor, simdi)
    return _v86_killer_frame_original(actor, simdi)


_v86_old_death_choreography_update = _v30_olum_koreografi_guncelle


def _v30_olum_koreografi_guncelle(simdi):
    if v86_death_state.active:
        return
    return _v86_old_death_choreography_update(simdi)







def v86_ground_shadow(center, width, height):
    width = max(3, int(round(width)))
    height = max(2, int(round(height)))
    cx, cy = int(round(center[0])), int(round(center[1]))
    pygame.draw.polygon(
        ekran,
        V84_BLACK,
        (
            (cx - width, cy),
            (cx, cy - height),
            (cx + width, cy),
            (cx, cy + height),
        ),
    )


def v86_flame_draw(center, size, seed, now):
    size = max(2.0, float(size))
    phase = (int(now) // 54 + int(seed)) % 7
    cx, cy = float(center[0]), float(center[1])
    lean = ((phase * 5) % 7 - 3) * 0.55
    outer = (
        (int(cx - size * 0.74), int(cy + size * 0.34)),
        (int(cx - size * 0.30), int(cy - size * 0.54)),
        (int(cx + lean), int(cy - size * (1.26 + phase * 0.035))),
        (int(cx + size * 0.31), int(cy - size * 0.43)),
        (int(cx + size * 0.75), int(cy + size * 0.34)),
    )
    inner = (
        (int(cx - size * 0.34), int(cy + size * 0.24)),
        (int(cx + lean * 0.45), int(cy - size * 0.64)),
        (int(cx + size * 0.36), int(cy + size * 0.24)),
    )
    pygame.draw.polygon(ekran, V84_BLOOD, outer)
    pygame.draw.polygon(ekran, V84_BODY_HOT, inner)
# </POTBO_STAGE S1929>

# <POTBO_STAGE S1934>


def v86_death_victim_draw(now):
    state = v86_death_state
    ordered = sorted(
        state.pieces,
        key=lambda piece: (
            piece.position.y,
            piece.local_center.y,
            piece.z,
        ),
    )
    for piece in ordered:
        v86_piece_draw(state, piece, now)
    v86_root_draw(state, now)
    for index, item in enumerate(
        sorted(state.debris, key=lambda debris: (debris.position.y, debris.z))
    ):
        v86_debris_draw(item, now, index)
# </POTBO_STAGE S1934>

# <POTBO_STAGE S1942>


_v86_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v86_diagnostics_original()
    data["v86"] = v86_diagnostics()
    return data


V86_STARTUP_CONTRACT = v86_diagnostics()
# </POTBO_STAGE S1942>

# <POTBO_STAGE S1946>
V87_SPECIAL_CUT_RED = (226, 22, 48)
V87_SPECIAL_CUT_CORE = (255, 244, 247)
V87_SPECIAL_RING = (250, 235, 239)
# </POTBO_STAGE S1946>

# <POTBO_STAGE S1948>




V87_GROUND_FIRE_ATLAS_SHA256 = (
    "e89cd0d2f3b6e62b0167310deb4119b9728e872a33e2a279d2a36d551aff1c97"
)
V87_GROUND_FIRE_ATLAS_BASE64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAJsAAACRCAMAAADjJDrYAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUg"
    "SW1hZ2VSZWFkeXHJZTwAAAMAUExURcOmWfnKWC0qJ//gpOt3SM7Dq/OpEraVa/jnuOe8e6WGZsKXalNHDJR2ZHIJDfTRj/vu"
    "x6qEW++uUY2AXvidE25KMOSMOv/98ntjTMV3W2tXRf3qdtameP332//eFfWYevv55YssBrqrjoh1MygeE2pSN1JMR8GbcnZn"
    "Vv/++smie8lXEohyWP/kKXFaKFhiapZEMZieIN2DGqk0J/vZa31wKv/6hP/naPzVnRkZGOSJE//4fTktIf7youh9EBUWDlZD"
    "L3ZYD9OVLGRMM//ZDtuNVpOIGPC9m8mpYko5JmpdUv1kDNu8l/XCEKVEEG1paV9HLKxhKc24h/z5ta2raPz3xFclGxkbJJyD"
    "Y3NeRtujlrGLE7BbSP3VPvvsjIVxQNWXc0YwG/ijK/XEQjoXEPbmmItoJfvcfIpwPO3VtHpdO2w6KLORdbCPaEU5BsiYF6pL"
    "LWEvHP/zbP/oQLuYdPXesAMDA/q6O7VjFjYuC5OGeZV6XPu7Hd60hb+aeVEZB4BrXK6YSOeuMXxzbYFrU9dfEJoZEJprTX4n"
    "Iop0X5x8WjaFH3dsZauKbqSVfdlyNX5ON0VBKNtnEMmMZpE2Id6miSklHmRaUJJ0VUg9R4UdG7+TZoxraEY9K5N/RmpbJKaQ"
    "a45fQj4uH0c8MqYeHUg1KN9tEJl0Uv///IltX/3NJ2FRUY5vX+B+NkEzIP37rJ0IDX12VkpASd3IiFU+IpuQe3Q3KyN/EzdE"
    "UK9IC/vlXzAeETMHAMl1KPTnzUpVXh4rN7CddcFpN15QPcZ8Ps9sEHtcYfrIsv7TKgAKGlBCNJtQD+rl2suSb4NuS9evUGxg"
    "T2VlXruXOXmaSMSpgv7SG8q6nrGJYpB4X+/rn45wUfFrIVVVVdaOa6WOTp9/Z7KaStRhHl0vIM6wS9+YEO+aHI+CX4prXtid"
    "YrmVdeBvEOFxELWSbOu7Mu8kHGeUPObCE/3IEpBmLuXem82jGPjHrsJlKf/wj9dpKtp3LuNvJ//8iNFWDvv7A/eXEv///25h"
    "dgEAAAEAdFJOU///////////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////////////////////////////////////////////////////////"
    "/////////////////////////////////////////////////////////////////wBT9wclAAAgAUlEQVR42s2cf3xUV5XA"
    "p6WpKYGRtI1JA1waCAMP26BAgoHQUHtVQptXaG2A2l9grLEgWtvSxda22hbpT6u2QcBaTfXlzZBfJAXKD6stWrW7/uiu3brd"
    "Xau7K13R/eG6n3V33/3ct+ece+97972ZCVD9Yx+QDG9m3vvOueece+45504m/P91ZGQYSvP4FN9r3hcKOELO8CEP8YGg0+pM"
    "0SFOgU1y/YY3wyYlokkpOeMhwys5jsP4ePcfl20qHvoxXU7/zNCdSjCowz7FpWKj04DGBV2ChQ7813G4NJLjp8Q2dXjRzJ6h"
    "4UXDSm4Bw0vQjTOMLZOMpQA5igT/JM4jFw9lgBACXyGiWwIak0IEIf4pHlYhx0ObOjxzuGdoKsGNBDwMAqnHdxmwmc+GN+NK"
    "p0gkSTp4DC8NiEgI5ji+UCLiP0U0CcyAFug3n4DNfKzhRcuGhx1/Zs8wwY18UwYBN7on/WX4TkaAQpHRCR4ELUHAuLmuBEmj"
    "2IS2BZ87TKpR5RLRiE1/jJNlQ7Rlvj/T96f39Bg4ZuyUtFqENBLifi7k/dGFOGctjq8GH4YTHkgcUbJF3wchOgTOQfKc40VQ"
    "FYMAJCtYeTgR/1yEbNXVju/4fk/P0KJQw8U+RILK4UCJXy75lZBn3nkuve8WpO1kSx1fGYE6QBdI0+gEJz1FjcVHQoCaSpK3"
    "MAYhy7LhienLFg0vqh6q9uGozQ8NLTp7OsFlLP8mJcCBADds2LBEnnmIvUdE4wIiAAnRazgDkcAPH34CCPKgBkruOABGf5EL"
    "tABeyJXkpAUkkmz4a/r066qHhoaqa6+srZ05NHXqdBLciM2mhCLEuRs6N5x57fkXLhPaAuSFS/m5wpcKzRcoj4Dg0EiRC3CY"
    "PyyQlWwbzrWAiiJhgi0syXb29Oqmpqah6vOvnH7lzOf/Yrp6wciILTfOwI3AjeW5Z74y1V/8B6F8lWzhtbW15+KAwN0KheMX"
    "KTrfD5ANZcUEd4aBrHaqJKMG6ZFwA268dJpNKONSrvrs6qbq6qarej50Ve3f/H4or1+Zt/SNMydo+SDASXnnta/AbZETfra0"
    "tCytrYUHYUH6fkEu8S6633g+pmQF4whGcZ2gASXpo2RRbsSmjVxYMhTKthidq64eWnbd7z90WnX1+UNDz1dXVyfmL+WqgqWL"
    "l94OV3/radfeeRGi+eA+RAufurSWo2kUCiCrQP7mN1+QQg2fUGygdv4wn+ooThwqBan9J7OMMjlv0I/qqqqKoQ/3/Pi0puqe"
    "np7qqtTcql387RsW3Q53/dz7ri1MR1lMDe5Ew+NLl54riK2AbBd599Oo+g4XvlCYzAddQGsQyhUKbdEi7TDIuNGD2/6l6sYK"
    "MIamKhhZAC1mE2hvt7/tFrAx+a5F18Ig8qngKuSZwCYJTSIcnLroN4gWMumD9YJmob2imspnHE1n4IQocrRMhT/KX1t00VEU"
    "k6ipCudCUHE/OHv6BJoYpfz+YhhcjnMmSUMU4I6FgpDq/j56CeVM0Dad65TbwyclhU9J1yt0rEBWRXDJmSLTVSpeMsEYD/5Q"
    "2/KJT7BpzrveijL7vrN4MZmdvgwOH6AJFSH5SKX9HL4IRY9xUpgKXvSQklEGdCnwLzSoSnjZffTrK9n6rjJs+EElu2XpYnlt"
    "8N/nT/8l+13h2kp/8eLF3L6TUOEkXF9IcCIwpDQZEBtNDM4wS8tDs7GYjWm50amB7D6Aa56UydZf3rVv3+WXt6bZKJoAtbnw"
    "wldeWcqnvIfzW65yahcLP5TpweFhAb2WQMMgrUI2iEfQBQMbF6moz5IbfSwQe8ApWiBRDuwEuMy+SSuy9fWX77u8vr6+tWhM"
    "1QXIef5OtDD/Sqf2c+DRUHeKAsUCaRYFKKinUtbWOqFUs73UwXBCz0huMCVCkEJsjNiUdyG47KRsa64e0b71rR8MlGATykMJ"
    "fuktU2Hm3UBopSJWNX7KDmg45ZW1ZJvMGUZ3lDABIzeG0zWxBahw6JXhqf7+sH9nduvWSdmtrbl9gPbcvn1HBorYqqpqamiE"
    "Lh362/f5y/ilvl9TVXrFoOYmgiM0UTs8jO4D0IpCSpSXQA8qSGaSlJQMlpED7O8f2Lp151OZ7LdaAe3qq5977sjOgYEkW9Xg"
    "WRzgpLy0ZmhIfOFXl8qamrPOKgkn0fEKWeAB05YAcM+QoQwVsem5QzIMoGgmUdKm36GCG9gJtrB1Z2uuAdkadu7cOZBke7jq"
    "LIZ0NTXw83/vF0OI1t9f7BBBbg5Df+L7ZMXytEFx5VWDQ3i8LUy8XoPhzAyfJuDEz5SsOZNGygM7tyJbNvsD9+qrr96Z3ZlN"
    "yq2/f3Bw8KyzAK3mUu7Dz35AqyqFFnqMHxeS5ldRA7c5bXC1EB+u+TCwoQIl2VABW9DfMIGxC0NKUlim4eANILnmTHYgm802"
    "uPv2dQ0kxhTnC8AY7EfVJbjLHobHor/0UlNKT1mqEDXwib7znaZBMVqFn6c/MfXQHAbzIOgAThk+RqZCmxzFf0pwcBfQua0w"
    "tDu7uroa4F/KFgAOD+KsQTH2qxsVo1WFosbDKaLgAVvN4H99Z3VTU83OGmJDQUdvIu+HJOAKr5sKnkOaQ4jktAaSs44S/i1U"
    "cPoRCLLMgrK/vwbhhOeJmtU1NatXP/98TU0sNUtuBkL/EjFxyjU1qqO9sdR8qiUSXbeqHJgaf6BDh4Ngq2tqIpHhu0oIu2jm"
    "Tx+AdbM62tvbS7NZ8UpYNQ5dvzoIyBxxmFN1CskVodH25PP59o7G9gNIl2ArXtd6419SKadWUY21oYzQTsyGaLhGaG/v6Djw"
    "ThsuE8VViWlpfLbQgKgDAM8aVxVEmf9qtkZgyx+A8WwHtpsb8/aYFrGdCE6NPo1fVfy4vMxOzHbgALJ13NwO/ztwIMlmkh5e"
    "OgU4HlzENS5YcTYkyZYnuEYU2xnfuxntdU8+YQtMehaT98dkHkvIKRXQyeTw5PPAhgN6oP0M5UwiNgUSeHH+r+SQ/hFs9uKl"
    "BBvSgdzyew7QkNpyU28MlOAkKwf35tkoerOf4hFzfBuQWz7fodBiNpVTwRhbZVqlSQMmbyVPAY6nFoDW/3U2TV3SYm5vB43b"
    "k0BDuVEKrTPQUDrHEuica5QAKvY05cXGRElBCs3GDZvFnEdb2EMDavkQWtIyncCAwQ04vlmahKVIrnxPZnCF5KIcm5V9S8hN"
    "seGRt/L5KnrXiR9ttUEY+prWvB2fl6k7lFE0oRIOouSzNpv9EfKkcflYappNMj8aQ6UwoH1+YJL2eD1cHugrnpiNh0VsPHmC"
    "ciMssJUEptR8Kg7hgMB933fVCzFlSpKDdZYv41viok/GObXx2HDZmMgqqHy10jXtQ5garKQ/yKfZAspKu4YN4DCmRRaVjlei"
    "wmyfVA6Gp9iKUgzMoEQqovhEzKYUiQmjR+2J4Kix0bApu/Rd6cKEgFYgA5+plGjQYG7PVNlARh5wHDZu/pkPwJXTEGohGLNx"
    "lSaE4Kijw4IjJ6f0TS12ueu6aP3o4Lh0CI0Dm0eXgofG+Umy3zJySzw2VihQS1AHcQGthA6KRKtVkhsGRxacDoIbVU0Qx5S5"
    "rjTJcF/pHGdOA7kT/CP1tIueL8nG7fDFTlPyiA2hGMlNjyuMC8oQs7XhHhxQlFxjPhkLhxlXsXHpYnUQqLiv5j/O0BaYKiIZ"
    "i0IJMmlP39EYC61RYdrrK3cntdxoXLE+grlcYtuj2drbU3AZFBegBTCkmMyQ6NtIeQNHNpBUGKqgeoNLmiftCTeaFEWUAtcF"
    "MfN5BOELfFYonQN1QzY1z+5Bnwtw5N8ScBm8uKtUXdKQqUs3wITaoEYR59ZAozHuOEk2SlWq6hulwGWR96KVvUqQk1cWmK3B"
    "5Wmg8g57SHI3UxCST7ExnBXIg0lLoxsaGmheRe2X2puATrLA4a4d9oiAxWx67kB5SNJ3JUBaw1NiOMCkCK7pGbKZvAOw3azj"
    "yhiuHdjwfiAGFpKl2gXJiI0bNHgxXNDF8kK0wEME7SG03EhOkvSdxGVyr1Svkarwiet6blLWKuhNxJVwDtlQYDxtdrpuKnGm"
    "MmjoAV2JP2F2ZUZspNYq+NCYWH0gr68CDxHoTAiICyZCqivhS4gR4TA6atdxZeOeaEjbUW52/VYqXxzIBs2G5hFGbCAzV0/9"
    "hg0ZaDxxkJANJMaVrxFxUoRzKolgLlZVm3icFEG2PZosMgcwjgz6Njtvih8SLtAQh9PcoOEdOdMDH0TVKTViqOmYi6GCVhBp"
    "UzIpwnVShJJfUR4CRzSfJMOTtJZxE+4cKyAGLbRqKC7WluGjuqR4UXUKU5gqU45JfaoNgoeItOlkkiIq5sXQzTLTjrCYDQ20"
    "ocGahEhsaAWU5gVHCOaBzlDfRJV4qZqK2sSoTKN/WWn28ZIiFFcmQ7doDeiO0w7ClSN2ceRh6sAYFLXJjdJYVFfj0mhTC0tr"
    "04kPxVay9jHe+yW2D4AlSxIb+DdskYgikXefjDaNt+axY95TZqOsOAOzdcn4XBfs1uHy1FJs3gkzQcUx70mxYfWdmllIXC6u"
    "dFjRemt8EXlFAYtXFFLlS9faxl15qig4DKRa7LiSnUh7vHL9VSx+gVci63L08OHD47IVScRFb0eOhWZbV54QqgSbnc/AF0iN"
    "Z19s4tpvfPnLXz5lNmuN6J5IYJJ+8eS5BK4XsVEI+/TT+vzaW790ydNFPkSOwxZSOC6Zo6zTHSdBImM2lpSlTH4Ej2s2+Lhf"
    "qltpgD5669p1R/XjVatOig1NQUqnSG5iHPFJS0j2xWUUKntSNRHNe+SCipX6+U0TXz/69NEbgGzGbdtXlWZL3lWFncXGWUJu"
    "XhGb9Oz/4EMtL89E9+EdEz+CcNPmzFn7UtuqVav+HqV227EiNll20S6L0l4lzNszL4zyOlyzeVH4DkOKDtwDf60d5cSJFX99"
    "bN3R2fX31d1008KF27/64NrtM1bdlM7hvzk2HsuN1kPkAaOFGV2UGCkO9PA3QzQ/qgL/9oGV5xw7tr3tiitWrly4/Zyvrv3J"
    "JStX3pRi4+OwlXNbWvM93TiHyhT3zCkJhR7zQrVMUo1NmNkILJv51ANzj7VtB7LbbgO4Y8fOuWThA98wbLopR2WOZCmF4uXZ"
    "ePyLK7lFUy6GphAcgGXCqpcsXnIfm61k6qKfumc7sN22cuXK7dsXLoShTbHpplMhT5ArFyUgPdVcyihwZiZhhj1dHrhtkBum"
    "UwJwHziY2MKRukP99sOHDVtFRcVXrr9p3SMZi4PpVFRBnAybTJsBVx2mICpsggtUoOrw44HnebTsYC1YfEXtEz6jxIuR2yP1"
    "s+nYDmTbv1JZWVnRc/1H5+G8UAij9k92imxWrAF34rhgBikFvo/jh+cc5qGzDbCa62BhGBPybIGvB1wfr398aPY555xzbGPd"
    "JdtnV1TOmFFZUX3rrRiHFHQaNik3yU+FDZtEfRg5n4oBPi3DkM33qFTtYPjiUKIKTgiXJ2a2cPaxcy5YWV9fv+5nc7746mUV"
    "Cz9+2xM/VDFSQRmoaWKSmo0VZ93Ls2EvjwNzr+fpzlVi0+2DHJD16geZFgjX8+JhmT209lj9uroHH3m1+laq7lx22Q2mVwrH"
    "lJEWUMuO0Gw2CUtg6KZCkyNUT2A7YQhi8mID9DDPSNNr1LJLxwI3oTJDfetee7BqzrQS8RuxYX+p7osShWK2ZBXKYotzmJRS"
    "AYPkidrTcdDBBUAa2KJfEJK9nnAdkUEWcuTYuIE3FIVkBl6WYQuTbEo/Pb3e12w0jAv48eRqMvLUpQ43zcZI3Txik4WgNJuI"
    "Gx0IKMWmVEmXTqS1wF4Apupp0/K8cp68DFvI1Rzo4TKpIMvJLWJLJi6F9tWWjKIpSycZPUuUXjpySqHJJBvHVBmsVpCNF6TO"
    "/5hgq5iNSbvz1PQCWzJKR6fpM+Ow2Z4rA2MIJobxmedhh16hEARJtrTCxXJLsNkySkWnJ9MQ4JqlU0puVDoAdcNFb9x5X4bN"
    "oxYsaVV+pKXYvKxITmCXsghN2UJASQJPepi8C0yiVtr53FjUnkqvmSItZXNl0ULvJNhkCTaYclP+jTIFcE8Ps6dYGxJ2cC+S"
    "94QpURcxpOq95DIsXb+U4xXtU29wpVk3pdgKJDYeHKdG9gLhRGxktVpFBbkwjM4KlG4mNlaGTZRV8khVZOrpIMmGXXbYQlkA"
    "eaDYkI0bbZJGbla4iXKTooA6h86d5MZL1H6FLEPphqrOlgimlWtWtduYDTwICE4EHlUEIbyB/zGLjTMR+VhB6uYEio1j2I+J"
    "NlNa43ZDg/UfWcSm0Lid2tDbvGw79XDHBDhcD1XNo80JBdW4zNU0QUnv2P97BawpCU4d0p6nEm+6JGk3ByTunCDEpHwgU2tP"
    "bsqFttw8znFrAqobbZnAfkBuVrgqwytCSzm8gu9jBa9ALfLHJSWYTBRvF2tlPPVxYXcYYE7PvNCE5iZ2TEy7mfC4R4KDuNl3"
    "mHLEUa1MVQJUqU3rD3wGH6shoKOsBedgVD+TyNTlDqmS+3CdzrjkxQwr16PP4zwFC7TcQpaYFzi2nOKtsLnTw0lLswWoUSqb"
    "SzMBNy4E8zZAQfkbT8uN6xpNxCYdB17SGXnnuOxDgQXVF1UlAMYTyxV6b6EluAzevlDgnjx4UAwOejgfUhBGtQtqFAarPBQX"
    "dUHfKM3PBMNAF9UUQwWmE4kR24c+48hmfTZAyYyN8diZY0lU55KJkWlDwsSttHvMGHZPFgYHB/Hlph6EVxTBIQZ/QW6HIkVH"
    "NswX0qYeLK2A9aBmYswcdDazaAn+7iNB85G368WWrJxwJNOstA1eHSCajEVEQyppeSNdO8fllQkIkK1AAycOHULF0mwyaGFq"
    "vw51R+CiCrXbBbLO5majUpk/CzozRzpJLuB0MkEmc0SXElVVS5oQGTcAMpULQDfmRqZqs3nJRC+87iBuuCC5gR2rYjjMcNgN"
    "6wS03YgXODaSCIllh05YAHZr5e+eIDtl89tpxN6xP+DNnWPNproDqNx0TeCwuYGjXYISm2lEsHsaE2ycerILqFNSsEOHvKCg"
    "Cs5qh5gfUJ4VlJU8N7EFnbJzknrv2d1joDjdzSiWzJTKgLCbla4HE47IqFUG7QDZmGpRp3Ie10yZRH7MFhtmAwuFQ9SZLTiq"
    "WcHsiSU4tDzkwpqo4FiDwCpEoFIX//PnF/8j6BSysUzlmMLulmoHZGYCaqC62xgC4R8pXYqAXNdlFpunvWCyrIUqTu4FKxoY"
    "SBGbNHvr8AeAeTg14HzPHNnpUv8/CHpJ59v5xR9wuzMQunZyZENsqs8y1Kn9uAMTy4phppI+VOAyDlDwEhh0U5AybHG2kUds"
    "+GEKTLFJj3xgSDuLxEGP9gKqkgfQwWOQRDeoDt5QsiXBdzvZf7r7m8dwu6OTAWzDRoYq96uCogybxyrvxoDWRbT5LtmvzSaj"
    "lGMcqUnadYSjGcDdBwvI5hek6ozDyQpd8uCgKidj9ghGrRs/NhXMg4u/28k/tv8dNwKb7HSwiwLu2q1uCVyS73e7Xbohwo1g"
    "3ceV8+fPh9eBAGUyT+5F0TePSpXk/ZkA984KqHvEFir/x8AdDtI+MqbjCNndDWqN110AJv7dziWi223WbOBqu2M2LNfv7+5W"
    "NWXePHb3CJgDd+ezZ901cg3IUEqbTUpTBtcRuwcKVghU6R+L/6jzBSnKrUXcShzSQHv1BQ67GNjcx2+ky1fCkEpiGyO2/Vz+"
    "67ZtOr3NmsdGAnAj7rPP8mfnr7F3OGbi+VcFLtojCnAfBdrxCoNaoG06BXmwmE1fxp0AQypR3RTbv1/cKT7ghs3ENkGiFnUj"
    "nmIDldoWZd4zOG+4jvvsGsafXbMGla01nrPIWXpWllYv7XAmU10KcBw8eHAw2nRUHDbKzs7uLtRjHFMedH8sEGeeCWwEB5bQ"
    "iSruGoUDtVK+TLExNwNo4PpAcHgz3XCRIeWHoaf4zXK9gzCqchDPEpigjX92hjdZcpETAtndhbIBtg+++z/+JfinJRtDIzi3"
    "M+ikDg5Xw3UBnBJF8xiYuOu2PovCXQOCw6khYlMdHRT7WIJjHLVdb7JXO05LrX/N6LpjaKhdnMbtuhU3fnDRkoYuvDPeY6wT"
    "5jhUFtOBgtOIq0LS5gw8B5PKGuAF1zZ/DYjfqrVhzpGpnI8cvy2/0TqRZMtMGAM23oVs357w3qazP+N+vlXLLXouYgu7u1xS"
    "gTC8uxkmIObyNW4XCNNdg7/zVoxEuVqZ1CCvBFtjko1bz317QvOaNa2stRVu/+1M81+e/ePVyBbeaD+nUImtu7tVuq14r3yG"
    "jY7e7QLS4cOjgIZs+UjfAtoIJ62UWmm2RsNGNUYVMZVvQIejd8uWLSfRS5Dho/no6IrQSG7oZEPDxlPVBS+qf0ZoqoLGLbbS"
    "uY7e07e8+OKL4Skc8ZYdnUfCbGgQLaW01/HGY6MwkDJGnixRUert1Q9yuS1bek8Cpz+1u8Vi41aK1ER8ni0/z9Y2zc+o7h6t"
    "/iy43rZcBLenNwJdv/7kAKv6Y7l5PIaAyFv7EY9ZbFQZjZQtVF+V4NE/HiZq8cS2N1eRiySXA7rzgGxGZXZ9MU9obwSqSkku"
    "E0apbRSat03KZKuiKocm2OiLOzDzRLm4KGnvmRFty+2dkosad9evX49s6yv3ri8lqKrEgfuXIrgMXj9Of3kwB5sEoC2RpNwC"
    "6ubD2iN1HSWdD9jmllyuomIvdvL01tfUbNuW3bt+b3bG+g6bTEtJAdGeP/zdb3ahGTZuehFIbmb1bmyD6wYAYwqUP9ThApXO"
    "eLLVYmBgdBTgcrm9e/dm26+4IpcDtr17cx25XEdCaABCUuq3RpNYa2qU4LTcJKWHwfa2RQlAXdtW4YKMbYGZ7xzgSm6pLkj0"
    "pgOjWxoRrj0LZJWVCq5jW26LJot1q19JKTnARuVU/IZxP+o4N60cNMcrn8fNRKb26+FeamUgMJzHA51EShnEwGhrY2sulwW2"
    "yhz+3rYNhjbBVmXGtSZCBXn1V1nmYLOxKL3j4bdPSNqzEMbfA0KjSj2r+nskJG1jZyaFb30jT3608ZnG7JYthq2iouL6pvVb"
    "BqItZ7bstABxKFHTFFwU94KiYYHBibpoGZVAyZFwbcPYAtnYrtvU9ZJEBlHyLQgTAeAbo63P0JEFsuz1U6ZMqWhq6sDJKPYW"
    "SrcS4xk/DuPvD8HQMoi6xzB/mXDAqvejvb0j6i4nLo8Wz0wZSMhtuPy2xmf2ojnknsk+WTFlxgyAax+lmdLsBFWy09swS8wN"
    "GZ3/wWQOfl9EJDfVs8CTzk7nxrnaGcFII6n5HZMcIebjIjYEy9HRkX2momJkZMqMkabRqG9R65vZfpkiU/NqhsyTzA2/aENa"
    "+VCpShEq9LTSJGG0/UfqJCRTvYQcq+IKrF2D4aiCv5tBcE2to/ltoQ2XdL395DwMmWILImcWTfBMh5x6tR9X1glTyc00lqPg"
    "YFHxApZQmWlqViLLIRgc18+44uWRkdZRuwNPSys0o2yjWuvTZCd5qPZ/UD8F08lhbie0aaLaFoIKaKug74B5IQgc/er8G+1b"
    "9JGlY8v117fCMZrsDtS+LFLBqtRXiZC+0V0SUTgwYUsyJcZkuoSB2glOGnRAR1YgeOeFEPPF5lO8YULFe+hPfpSO4sbFMt9q"
    "Yq1PE/ltPZ1SQ29A7d/JtJza+4ZsQcQWBC9Qd0PJglYuZ75USB1tbX3492idfbI69T061to5zQaTrCv1t13IdF8SZishKAgD"
    "vWsQU+dYE2WpirJaufS15uovz9loyx/7Wv+rn33ssR/dcQedufziOT2bm56aVf2Wix+2o9jSbHAn9KycvkJKJrvQqHxC86/U"
    "E4HHnBBLuliftNH6+sAa6vtaE3BtffdsumvaxNdm9z608WvrnsRTu9/bM2nWL37x6Vmb37tbkTXacite93G13S1gqW8rwUEN"
    "9LyrfS1aju5TjEf07r8Dplw9oik4rWxtKydjI82TvcuXP/TOx7CJcebc3ZM2N80CtEm7537Siv0jthUbU8Vi+uI/yjMXD6oV"
    "UZo1BS4fqLBLaQb4mR1Bpr6+vtYuFx7kWpXfbWsDtskPQTTc+9A7N26seyScu3nWrFmb4Zj06aa5P3mLxXbeT+7D3z/fVbcx"
    "3QonqXlHlqioB0WVXLVTD+GyI9/8ZiaTGRnJdnWB5Fpbuw7DorgPFq60Jn5w+eTwoYeA7clVG3vb+pb/1Vt27968eeYnJ219"
    "+JObN1ftropWTCC3ea/fF856KrOr7t6Njz56772nm5Q/CUh9LU1R+T0oBqYdN4z6r7PZEfBpA29AkAnjeRgPIMRj06Yw/Ojs"
    "18O23qNz1p7xvY19bX2z0ZPsnjt3UhP8q7o1jq9pTOf97EePPrViV13dvY/eW1dXp+ECV+p4Mc0mebHtqN0+Km8RvjEAZJvw"
    "yCcPRAvDOZvC3ifXvf/9R88AT7L8NTz100mT5sxrmlQ1J0yxhfPuesdTu07fUYdo819eMzmO/yWTJdoZZalCCUdXYpphNxHF"
    "JvsI1TltEL2T7/m3z/b2tc2ui3MGjansgbKFquqbdn3+9B2PAtpzjz5692Rr9Xdy24jx+5LKPrljx9e/njq17sneyZOXt/XV"
    "WWjtMVzC997Vk9n18ul1E+dfffVzH/mHFyemu29Ogq3sc8vbdtTduyN18rfLe3tXLn8wTgJ14IasxqTgtA95dcWuVa9fcOzj"
    "yPbCG6+Hp3qUaeTbsWNH3UttpeDCtesmz37NRlNhdRgtTCK23654fNVdNzw++YtPPPFE+GaOoiG9+eW2trlzL6hb3tZ2OsFN"
    "LvfWRjOKGFaXmLPm/XzFNeGf5lixgq67YtfX21564I662UfrH1v90twLdrRNLkMXm4E5tAQz4Z/6uOaa9/zztBUrFi58/LHP"
    "PnLXvDnz5s2bNm3aHPhR7uso0mhGgn96tkd+fc15N9zww/N+fdcfe6X/A49Zyp9TouiVAAAAAElFTkSuQmCC"
)
# </POTBO_STAGE S1948>

# <POTBO_STAGE S1950>


def v87_group_ground_fire_frames(frames):
    families = {"compact": [], "tall": [], "wide": []}
    for frame in frames:
        ratio = frame.get_width() / max(1.0, float(frame.get_height()))
        if ratio < 0.78:
            families["tall"].append(frame)
        elif ratio > 1.28:
            families["wide"].append(frame)
        else:
            families["compact"].append(frame)
    return {name: items for name, items in families.items() if items}
# </POTBO_STAGE S1950>

# <POTBO_STAGE S1953>

v87_death_fire_cache = {}
# </POTBO_STAGE S1953>

# <POTBO_STAGE S1956>


_v87_root_draw_original = v86_root_draw


def v86_root_draw(state, now):
    _v87_root_draw_original(state, now)
    if not state.burning_root or state.root_surface is None:
        return



    anchor = v86_body_anchor_screen(state)
    width, height = state.base_size
    fall = 0.0
    if state.fall_started_ms > 0:
        fall = v84_clamp01(
            (int(now) - int(state.fall_started_ms))
            / max(1.0, float(state.fall_duration_ms))
        )
    center = pygame.Vector2(
        anchor.x,
        anchor.y - height * (0.50 - 0.36 * fall),
    )
    rng = random.Random(int(state.seed) ^ 0x87F1AE)
    for index in range(9):
        local = pygame.Vector2(
            rng.uniform(-width * 0.34, width * 0.34),
            rng.uniform(-height * 0.34, height * 0.34),
        ).rotate(-float(state.body_rotation))
        v86_flame_draw(
            center + local,
            rng.uniform(3.8, 6.4),
            state.seed + 101 + index * 37,
            now,
        )
# </POTBO_STAGE S1956>

# <POTBO_STAGE S1961>


_v87_death_actor_frame_original = v86_death_actor_frame
# </POTBO_STAGE S1961>

# <POTBO_STAGE S1964>


def v86_bite_mask(state, fraction, rng):
    mask = _v87_bite_mask_original(state, fraction, rng)
    if mask is None or state.remaining_mask is None:
        return mask
    minimum_remainder = max(18, int(state.original_pixels * 0.19))
    available = max(0, int(state.remaining_mask.count()) - minimum_remainder)
    budget = min(available, max(0, int(mask.count() * 0.18)))
    if budget <= 0:
        return mask

    width, height = state.base_size
    bounds = v86_mask_bounds(mask)
    if bounds is None:
        return mask
    area = bounds.inflate(2, 2).clip(pygame.Rect(0, 0, width, height))
    candidates = []
    neighbors = (
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (-1, 1),
        (1, -1),
        (-1, -1),
    )
    for y in range(area.top, area.bottom):
        for x in range(area.left, area.right):
            if not state.remaining_mask.get_at((x, y)):
                continue
            contacts = 0
            for dx, dy in neighbors:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    contacts += int(mask.get_at((nx, ny)))
            if contacts >= 2:
                candidates.append((x, y, contacts))
    rng.shuffle(candidates)
    candidates.sort(key=lambda item: item[2], reverse=True)
    for x, y, _contacts in candidates[:budget]:
        mask.set_at((x, y), 1)
        state.remaining_mask.set_at((x, y), 0)
    v86_root_refresh(state)
    return mask
# </POTBO_STAGE S1964>

# <POTBO_STAGE S1966>


_v87_ground_splatter_original = v73_ground_splatter
# </POTBO_STAGE S1966>

# <POTBO_STAGE S1971>


_v87_draw_seep_original = _v81_draw_seep
# </POTBO_STAGE S1971>

# <POTBO_STAGE S1975>


_v87_death_update_original = v86_death_update
# </POTBO_STAGE S1975>

# <POTBO_STAGE S1979>


_v87_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v87_diagnostics_original()
    data["v87"] = v87_diagnostics()
    return data


V87_STARTUP_CONTRACT = v87_diagnostics()
# </POTBO_STAGE S1979>

# <POTBO_STAGE S1982>
V88_PARTICLE_ROOT = os.path.join(V88_EFFECTS_ROOT, "particles")
# </POTBO_STAGE S1982>

# <POTBO_STAGE S1984>
V88_REVIEW_ROOT = os.path.join(BASE_DIR, "upload")
# </POTBO_STAGE S1984>

# <POTBO_STAGE S1986>


def v88_first_existing(paths):
    """Return the first real file while keeping candidate order deterministic."""
    seen = set()
    for raw in paths:
        path = os.path.normpath(str(raw))
        key = os.path.normcase(os.path.abspath(path))
        if key in seen:
            continue
        seen.add(key)
        if os.path.isfile(path):
            return path
    return ""
# </POTBO_STAGE S1986>

# <POTBO_STAGE S1995>
v88_lethal_event = None
v88_attribution_stats = {
    "scoped_melee": 0,
    "scoped_projectile": 0,
    "lethal_frozen": 0,
    "exact_fallback": 0,
    "ambiguous_rejected": 0,
    "post_lethal_rejected": 0,
}
# </POTBO_STAGE S1995>

# <POTBO_STAGE S1997>


def v88_name_key(value):
    return "".join(ch for ch in str(value or "").lower() if ch.isalnum())
# </POTBO_STAGE S1997>

# <POTBO_STAGE S2021>


_v88_death_scene_begin_original = v86_death_scene_begin
# </POTBO_STAGE S2021>

# <POTBO_STAGE S2025>


_v88_melee_death_update_original = v86_update_melee_death
# </POTBO_STAGE S2025>

# <POTBO_STAGE S2027>


_v88_death_actor_frame_original = v86_death_actor_frame
# </POTBO_STAGE S2027>

# <POTBO_STAGE S2029>






V88_DEATH_FLOW_LIMIT = 9
V88_DEATH_FLOW_COMMIT_STAGES = 7
V88_DEATH_FLOW_MIN_LENGTH = 12.0
V88_DEATH_FLOW_MAX_LENGTH = 62.0
V88_DEATH_FLOW_MAX_WIDTH = 17.0


@dataclass
class V88DeathBloodFlow:
    flow_id: int
    scene_seed: int
    birth_ms: int
    last_feed_ms: int
    last_update_ms: int
    origin: pygame.Vector2
    direction: pygame.Vector2
    seed: int
    target_length: float
    target_width: float
    visible_length: float = 0.8
    visible_width: float = 0.45
    mass: float = 1.0
    speed: float = 13.0
    width_speed: float = 3.2
    phase: float = 0.0
    wave_count: int = 2
    lateral_amplitude: float = 1.8
    committed_stage: int = 0
    fully_committed: bool = False
    source_tags: set = field(default_factory=set)

    def feed(self, severity, direction, tag, now):
        severity = max(0.35, float(severity))
        incoming = v84_safe_vector(direction, self.direction).normalize()
        blended = self.direction * max(0.6, self.mass) + incoming * severity
        self.direction = v84_safe_vector(blended, self.direction).normalize()
        self.mass = min(18.0, self.mass + severity)
        self.target_length = min(
            V88_DEATH_FLOW_MAX_LENGTH,
            self.target_length + 2.2 + severity * 2.7,
        )
        self.target_width = min(
            V88_DEATH_FLOW_MAX_WIDTH,
            self.target_width + 0.55 + severity * 0.58,
        )
        self.speed = min(22.0, self.speed + severity * 0.22)
        self.width_speed = min(6.4, self.width_speed + severity * 0.08)
        self.last_feed_ms = int(now)
        self.source_tags.add(int(tag))

    def update(self, now):
        now = int(now)
        dt = max(
            0.0,
            min(0.08, (now - int(self.last_update_ms)) / 1000.0),
        )
        self.last_update_ms = now
        if dt <= 0.0:
            return
        remaining = max(0.0, self.target_length - self.visible_length)

        pressure = 0.34 + 0.66 * min(1.0, remaining / 14.0)
        self.visible_length = min(
            self.target_length,
            self.visible_length + self.speed * pressure * dt,
        )
        width_remaining = max(0.0, self.target_width - self.visible_width)
        width_pressure = 0.28 + 0.72 * min(1.0, width_remaining / 4.0)
        self.visible_width = min(
            self.target_width,
            self.visible_width + self.width_speed * width_pressure * dt,
        )

    def progress(self):
        return v84_clamp01(self.visible_length / max(0.01, float(self.target_length)))
# </POTBO_STAGE S2029>

# <POTBO_STAGE S2031>
v88_death_flow_serial = 0
# </POTBO_STAGE S2031>

# <POTBO_STAGE S2033>


def v88_next_flow_id():
    global v88_death_flow_serial
    v88_death_flow_serial += 1
    return int(v88_death_flow_serial)


def v88_flow_ground_origin(state, zone):


    side = {
        "head": -3.0,
        "neck": -2.0,
        "torso": 0.0,
        "waist": 2.0,
        "legs": 4.0,
    }.get(str(zone), 0.0)
    return pygame.Vector2(state.body_anchor) + pygame.Vector2(0.0, 1.5 + side)
# </POTBO_STAGE S2033>

# <POTBO_STAGE S2035>


def v88_flow_angle_similarity(first, second):
    a = v84_safe_vector(first).normalize()
    b = v84_safe_vector(second).normalize()
    return float(a.dot(b))
# </POTBO_STAGE S2035>

# <POTBO_STAGE S2037>


def v88_flow_create(state, origin, direction, severity, tag, now):
    direction = v84_safe_vector(direction).normalize()
    severity = max(0.45, float(severity) * float(state.intensity))
    rng = random.Random(
        int(state.seed)
        ^ int(tag) * 0x88F10
        ^ int(origin.x * 31.0)
        ^ int(origin.y * 47.0)
    )
    direction = direction.rotate(rng.uniform(-19.0, 19.0))
    desired_length = v84_clamp(
        10.0 + severity * rng.uniform(6.8, 9.6),
        V88_DEATH_FLOW_MIN_LENGTH,
        V88_DEATH_FLOW_MAX_LENGTH,
    )
    clear_length = v88_flow_clear_length(origin, direction, desired_length)
    if clear_length <= 0.0:
        return None
    flow = V88DeathBloodFlow(
        flow_id=v88_next_flow_id(),
        scene_seed=int(state.seed),
        birth_ms=int(now),
        last_feed_ms=int(now),
        last_update_ms=int(now),
        origin=pygame.Vector2(origin),
        direction=direction,
        seed=rng.randint(1, 2_000_000),
        target_length=min(desired_length, clear_length),
        target_width=min(
            V88_DEATH_FLOW_MAX_WIDTH,
            2.6 + severity * rng.uniform(1.45, 2.15),
        ),
        mass=severity,
        speed=rng.uniform(10.8, 15.4) + severity * 0.72,
        width_speed=rng.uniform(2.45, 3.85) + severity * 0.20,
        phase=rng.uniform(0.0, math.tau),
        wave_count=rng.choice((2, 2, 3)),
        lateral_amplitude=rng.uniform(1.1, 2.6),
        source_tags={int(tag)},
    )
    v88_death_blood_flows.append(flow)
    v88_flow_stats["created"] += 1
    return flow
# </POTBO_STAGE S2037>

# <POTBO_STAGE S2039>


def v88_flow_center(flow, t, visible_length=None):
    t = v84_clamp01(t)
    length = (
        float(flow.visible_length) if visible_length is None else float(visible_length)
    )
    forward = flow.direction * (length * t)
    normal = pygame.Vector2(-flow.direction.y, flow.direction.x)
    wave = math.sin(flow.phase + t * math.tau * float(flow.wave_count))
    second = math.sin(flow.phase * 1.73 + t * math.tau * 0.72)
    lateral = (
        wave * flow.lateral_amplitude * (0.18 + 0.82 * t)
        + second * flow.lateral_amplitude * 0.28 * t
    )
    return flow.origin + forward + normal * lateral


def v88_flow_half_width(flow, t, edge_sign=1.0):
    t = v84_clamp01(t)
    rng = random.Random(flow.seed ^ int(t * 1000.0) * 131)
    body = math.sin(math.pi * min(1.0, t * 1.08)) ** 0.72
    taper = 1.0 - 0.54 * (t**2.2)
    source_pool = 0.42 + 0.58 * (1.0 - t) ** 1.8
    irregular = rng.uniform(0.82, 1.14)
    asymmetry = 1.0 + float(edge_sign) * rng.uniform(-0.13, 0.13)
    return max(
        0.65,
        (0.58 + float(flow.visible_width) * (0.30 * source_pool + 0.70 * body) * taper)
        * irregular
        * asymmetry,
    )
# </POTBO_STAGE S2039>

# <POTBO_STAGE S2041>


def v88_flow_branch_data(flow, branch_index):
    rng = random.Random(flow.seed ^ 0xB12A88 ^ branch_index * 8191)
    start_t = rng.uniform(0.28, 0.74)
    sign = -1.0 if branch_index % 2 == 0 else 1.0
    angle = sign * rng.uniform(25.0, 58.0)
    length = rng.uniform(4.5, 11.5) * min(1.0, flow.mass / 3.0)
    width = rng.uniform(0.7, 1.8) + flow.visible_width * 0.08
    return start_t, angle, length, width
# </POTBO_STAGE S2041>

# <POTBO_STAGE S2044>


def v88_flow_commit_point(flow, stage, lane):
    stage_t = stage / float(V88_DEATH_FLOW_COMMIT_STAGES)
    t = v84_clamp01(0.08 + stage_t * 0.88)
    center = v88_flow_center(flow, t, visible_length=flow.target_length)
    tangent_before = v88_flow_center(
        flow,
        max(0.0, t - 0.03),
        visible_length=flow.target_length,
    )
    tangent_after = v88_flow_center(
        flow,
        min(1.0, t + 0.03),
        visible_length=flow.target_length,
    )
    tangent = v84_safe_vector(
        tangent_after - tangent_before,
        flow.direction,
    ).normalize()
    normal = pygame.Vector2(-tangent.y, tangent.x)
    rng = random.Random(flow.seed ^ stage * 0xC088 ^ lane * 977)
    lateral = normal * rng.uniform(-1.0, 1.0) * (0.45 + flow.target_width * 0.28)
    longitudinal = tangent * rng.uniform(-1.2, 1.2)
    return center + lateral + longitudinal
# </POTBO_STAGE S2044>

# <POTBO_STAGE S2046>


def v88_flow_progressive_commit(flow, force=False):
    if force:
        target_stage = V88_DEATH_FLOW_COMMIT_STAGES
    else:
        target_stage = min(
            V88_DEATH_FLOW_COMMIT_STAGES,
            int(math.floor(flow.progress() * V88_DEATH_FLOW_COMMIT_STAGES)),
        )
    while int(flow.committed_stage) < int(target_stage):
        flow.committed_stage += 1
        v88_flow_commit_stage(
            flow,
            flow.committed_stage,
            forced=bool(force),
        )
    if flow.committed_stage >= V88_DEATH_FLOW_COMMIT_STAGES:
        flow.fully_committed = True
# </POTBO_STAGE S2046>

# <POTBO_STAGE S2048>


_v88_death_update_original = v86_death_update


def v86_death_update(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    result = _v88_death_update_original(now)
    if v86_death_state.active:
        v88_death_flows_update(now)
        v88_enforce_death_physics_ownership()
    return result
# </POTBO_STAGE S2048>

# <POTBO_STAGE S2054>


_v88_full_diagnostics_original = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v88_full_diagnostics_original()
    data["v88"] = v88_diagnostics()
    return data


V88_STARTUP_CONTRACT = v88_diagnostics()
# </POTBO_STAGE S2054>

# <POTBO_STAGE S2056>













V89_VERSION = "89.0"
V89_GAME_TITLE = "Path of the Bloodied One"
pygame.display.set_caption(V89_GAME_TITLE)
# </POTBO_STAGE S2056>

# <POTBO_STAGE S2063>
v89_small_fire_cache = {}
v89_ground_fire_cache = {}


def v89_clamp01(value):
    return max(0.0, min(1.0, float(value)))


def v89_color_mix(first, second, amount):
    amount = v89_clamp01(amount)
    return tuple(
        max(
            0,
            min(
                255,
                int(round(float(a) + (float(b) - float(a)) * amount)),
            ),
        )
        for a, b in zip(first[:3], second[:3])
    )
# </POTBO_STAGE S2063>

# <POTBO_STAGE S2066>
v89_footprint_grid = {}
# </POTBO_STAGE S2066>

# <POTBO_STAGE S2068>
v89_tile_use_serial = 0
# </POTBO_STAGE S2068>

# <POTBO_STAGE S2071>


class V89BloodFootprint:
    def __init__(self, x, y, angle, side, intensity, now):
        self.x = float(x)
        self.y = float(y)
        self.angle = float(angle)
        self.side = -1 if int(side) < 0 else 1
        self.intensity = v89_clamp01(intensity)
        self.created_ms = int(now)
        self.dry_after_ms = int(now) + int(34_000 + 24_000 * self.intensity)
        self.v89_scorch = 0.0
# </POTBO_STAGE S2071>

# <POTBO_STAGE S2073>


def v75_cleanup_consumed_blood(simdi):

    return 0
# </POTBO_STAGE S2073>

# <POTBO_STAGE S2075>





V89_MAGGOT_MAX = 10
V89_MAGGOT_REPRODUCTION_MIN_MS = 28_000
V89_MAGGOT_REPRODUCTION_MAX_MS = 48_000
V89_MAGGOT_FEED_INTERVAL_MS = 920
# </POTBO_STAGE S2075>

# <POTBO_STAGE S2077>
V89_FIRE_ECOLOGY_INTERVAL_MS = 240
# </POTBO_STAGE S2077>

# <POTBO_STAGE S2081>


def v89_nearest_fire(point, radius):
    point = pygame.Vector2(point)
    best = None
    best_d2 = float(radius) ** 2
    for fire in v89_active_fire_points():
        distance = point.distance_squared_to(fire)
        if distance <= best_d2:
            best = fire
            best_d2 = distance
    return best
# </POTBO_STAGE S2081>

# <POTBO_STAGE S2083>


_v89_maggot_init_raw = BloodMaggot.__init__
_v89_maggot_motion_raw = _v75_maggot_update_original
# </POTBO_STAGE S2083>

# <POTBO_STAGE S2085>


BloodMaggot.__init__ = _v89_maggot_init
BloodMaggot.guncelle = _v89_maggot_update


_v89_rat_init_raw = AmbientRat.__init__
_v89_rat_update_raw = AmbientRat.guncelle
_v89_rat_consume_raw = AmbientRat._consume_tick
# </POTBO_STAGE S2085>

# <POTBO_STAGE S2088>


def _v89_rat_consume(self, simdi):
    if self.food_kind == "blood":
        self.food_kind = None
        self.food_obj = None
        return
    return _v89_rat_consume_raw(self, simdi)


def _v89_rat_update(self, dt, simdi):
    fire = v89_nearest_fire((self.x, self.y), 112.0)
    if fire is not None:
        here = pygame.Vector2(float(self.x), float(self.y))
        away = here - fire
        if away.length_squared() <= 1e-8:
            away = pygame.Vector2(1.0, 0.0).rotate(random.uniform(0.0, 360.0))
        away = away.normalize()
        target = here + away * 165.0
        if self._aday_gecerli(target):
            self.target = target
        self.behavior = "flee"
        self.flee_until = int(simdi) + 980
        self.food_kind = None
        self.food_obj = None
        self.food_refresh_ms = int(simdi) + 1050
        self.smell_refresh_ms = int(simdi) + 1050
    return _v89_rat_update_raw(self, dt, simdi)


AmbientRat.__init__ = _v89_rat_init
AmbientRat._find_food = _v89_rat_find_food
AmbientRat._consume_tick = _v89_rat_consume
AmbientRat.guncelle = _v89_rat_update
# </POTBO_STAGE S2088>

# <POTBO_STAGE S2090>
_v89_ground_fire_update_raw = GroundFirePatch.guncelle


def _v89_ground_fire_init(self, x, y, simdi, index=0):
    _v89_ground_fire_init_raw(self, x, y, simdi, index=index)
    rng = random.Random(int(float(x) * 71 + float(y) * 113 + int(simdi) + index * 997))
    self.v89_frame_index = rng.randrange(max(1, len(V89_GROUND_FIRE_FRAMES)))
    self.v89_flip = bool(rng.randrange(2))
    self.v89_ecology_next_ms = int(simdi)
    self.v89_pulse_phase = rng.randrange(6)
# </POTBO_STAGE S2090>

# <POTBO_STAGE S2093>


GroundFirePatch.__init__ = _v89_ground_fire_init
GroundFirePatch.guncelle = _v89_ground_fire_update
GroundFirePatch.ciz = _v89_ground_fire_draw
# </POTBO_STAGE S2093>

# <POTBO_STAGE S2101>
v89_icon_cache = {}
# </POTBO_STAGE S2101>

# <POTBO_STAGE S2105>


def slot_ciz(
    rect,
    secili=False,
    numara=None,
    item_index=None,
    tasima_kaynagi=False,
):
    v85_slot_shell(
        rect,
        selected=bool(secili),
        transfer=bool(tasima_kaynagi),
        magic=False,
    )
    v85_slot_contents(rect, numara, item_index)
# </POTBO_STAGE S2105>

# <POTBO_STAGE S2112>





def v89_replace_ecology_hints(mapping):
    if not isinstance(mapping, dict):
        return
    ecology_tokens = {
        "TR": ("kurtçuk", "Fareler", "Kan 20", "kanın yayılması"),
        "EN": ("maggot", "Maggot", "Rats", "Blood fully", "Blood dries", "Blood spread"),
    }
    additions = {
        "TR": [
            "Kan 20 dakikada kurur; leke zamanla ya da ekosistem yüzünden asla silinmez.",
            "Kurtçuklar ıslak kan serumunu ve yumuşak organları tüketerek çoğalır; üç fare kurtçukları ve organları avlar.",
            "Ateş kanı hızla kurutup kömürleştirir ve kurtçukları öldürür; zemindeki kan izi yine kalır.",
        ],
        "EN": [
            "Blood dries in 20 minutes; neither age nor ecology ever removes the stain.",
            "Maggots reproduce by feeding on wet blood serum and soft organs; three rats hunt maggots and organs.",
            "Fire rapidly dries and chars blood and kills maggots, but the stain remains on the ground.",
        ],
    }
    for language in ("TR", "EN"):
        pool = mapping.get(language)
        if not isinstance(pool, list):
            continue
        filtered = []
        for entry in pool:
            text_value = str(entry)
            if any(token in text_value for token in ecology_tokens[language]):
                continue
            filtered.append(entry)
        filtered.extend(additions[language])
        mapping[language] = filtered


v89_replace_ecology_hints(IPUCLARI)
# </POTBO_STAGE S2112>

# <POTBO_STAGE S2115>


_v89_full_diagnostics_raw = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v89_full_diagnostics_raw()
    data["v89"] = v89_diagnostics()
    return data


V89_STARTUP_CONTRACT = v89_diagnostics()
# </POTBO_STAGE S2115>

# <POTBO_STAGE S2119>
if _v89_smoke_prefix:
    try:
        print(json.dumps(v89_smoke_test(_v89_smoke_prefix), ensure_ascii=False, indent=2))
    finally:
        calisiyor = False
# </POTBO_STAGE S2119>

# <POTBO_STAGE S2122>

V90_DRACO_FRAME_RECTS = (
    (0, 0, 20, 33),
    (20, 0, 45, 35),
    (63, 0, 32, 39),
    (95, 0, 57, 43),
    (153, 0, 60, 52),
    (214, 0, 72, 62),
    (287, 0, 85, 65),
    (372, 0, 86, 63),
    (455, 0, 113, 63),
)
# </POTBO_STAGE S2122>

# <POTBO_STAGE S2124>


V90_DRACO_FRAMES = v90_draco_frames_load()
# </POTBO_STAGE S2124>

# <POTBO_STAGE S2127>

V90_DRACO_MANA_COST = 54
# </POTBO_STAGE S2127>

# <POTBO_STAGE S2129>
V90_DRACO_COOLDOWN_MS = 7200
# </POTBO_STAGE S2129>

# <POTBO_STAGE S2131>
V90_DRACO_SELL_PRICE = 910
V90_DRACO_BUYBACK_PRICE = 980
# </POTBO_STAGE S2131>

# <POTBO_STAGE S2133>


_v90_item_description_raw = item_aciklamasi
# </POTBO_STAGE S2133>

# <POTBO_STAGE S2135>


_v90_q_eligible_raw = item_q_hizli_kullanima_uygun_mu
# </POTBO_STAGE S2135>

# <POTBO_STAGE S2146>


def v90_clamp(value, low=0.0, high=1.0):
    return max(float(low), min(float(high), float(value)))


def v90_smoothstep(value):
    value = v90_clamp(value)
    return value * value * (3.0 - 2.0 * value)
# </POTBO_STAGE S2146>

# <POTBO_STAGE S2149>


def v90_profile_factors(profile):
    name = str(profile or "").lower()
    if any(token in name for token in ("slash", "cut", "pierce", "bite", "claw")):
        return 1.00, 1.20, 0.68
    if any(token in name for token in ("blunt", "crush", "impact", "rock")):
        return 1.12, 0.24, 1.18
    if any(token in name for token in ("fire", "burn")):
        return 0.72, 0.08, 0.92
    return 0.92, 0.54, 0.78
# </POTBO_STAGE S2149>

# <POTBO_STAGE S2159>


_v90_item_use_raw = secili_itemi_kullan
# </POTBO_STAGE S2159>

# <POTBO_STAGE S2161>






V90_DRACO_CAST_MS = 260
V90_DRACO_SPEED = 520.0
V90_DRACO_MAX_TRAVEL = 720.0
V90_DRACO_BITE_MS = 150
V90_DRACO_COIL_MS = 430
V90_DRACO_COLLAPSE_MS = 170
V90_DRACO_SILENCE_MS = 500
V90_DRACO_RUPTURE_MS = 280
# </POTBO_STAGE S2161>

# <POTBO_STAGE S2163>

v90_draco_last_cast_ms = -10000
v90_draco_transform_cache = {}
v90_draco_glow_cache = {}
v90_ash_cache = {}
# </POTBO_STAGE S2163>

# <POTBO_STAGE S2165>
v90_ash_marks = []
# </POTBO_STAGE S2165>

# <POTBO_STAGE S2168>


@dataclass
class V90AshMark:
    x: float
    y: float
    born_ms: int
    ttl_ms: int
    scale: float
    seed: int

    def alive(self, now):
        return int(now) - int(self.born_ms) <= int(self.ttl_ms)
# </POTBO_STAGE S2168>

# <POTBO_STAGE S2170>


def v90_actor_alive(actor):
    return bool(
        actor is not None
        and getattr(actor, "active", False)
        and int(getattr(actor, "hp", 0)) > 0
    )
# </POTBO_STAGE S2170>

# <POTBO_STAGE S2174>


def v90_spawn_ash(position, now, seed):
    position = pygame.Vector2(position)
    v90_ash_marks.append(
        V90AshMark(
            position.x,
            position.y + 17.0,
            int(now),
            22000,
            random.Random(int(seed)).uniform(0.82, 1.18),
            int(seed),
        )
    )
    if len(v90_ash_marks) > 120:
        del v90_ash_marks[:-120]
    v90_draco_stats["ash_marks"] += 1
# </POTBO_STAGE S2174>

# <POTBO_STAGE S2177>


v90_draco_state = V90DracoState()
# </POTBO_STAGE S2177>

# <POTBO_STAGE S2185>






_v90_q_use_raw = q_hizli_itemi_kullan
# </POTBO_STAGE S2185>

# <POTBO_STAGE S2199>


_v90_new_game_raw = yeni_oyun_baslat
# </POTBO_STAGE S2199>

# <POTBO_STAGE S2203>
for _language, _entries in V90_ECOLOGY_HINTS.items():
    for _entry in _entries:
        if _entry not in IPUCLARI[_language]:
            IPUCLARI[_language].append(_entry)
# </POTBO_STAGE S2203>

# <POTBO_STAGE S2205>


_v90_full_diagnostics_raw = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v90_full_diagnostics_raw()
    data["v90"] = v90_diagnostics()
    return data


V90_STARTUP_CONTRACT = v90_diagnostics()
# </POTBO_STAGE S2205>

# <POTBO_STAGE S2209>
if _v90_smoke_prefix:
    try:
        print(json.dumps(v90_smoke_test(_v90_smoke_prefix), ensure_ascii=False, indent=2))
    finally:
        calisiyor = False
# </POTBO_STAGE S2209>

# <POTBO_STAGE S2211>
pygame.display.set_caption("Path of the Bloodied One — Agraphon Studios")
# </POTBO_STAGE S2211>

# <POTBO_STAGE S2213>
V91_DEATH_BODY = (224, 58, 67)
V91_DEATH_BLOOD = (84, 0, 12)
V91_DEATH_BLACK = (0, 0, 0)
# </POTBO_STAGE S2213>

# <POTBO_STAGE S2217>





v91_test_panel_visible = False
# </POTBO_STAGE S2217>

# <POTBO_STAGE S2220>


_v91_dev_input_raw = gelistirici_test_girdisi_uygula
# </POTBO_STAGE S2220>

# <POTBO_STAGE S2222>
V38_MAX_GROUND_FIRES = 28
v91_small_flame_transform_cache = {}
v91_ground_cluster_cache = {}
v91_impact_cluster_cache = {}
# </POTBO_STAGE S2222>

# <POTBO_STAGE S2225>


FireMagicProjectile.ciz = _v91_fire_projectile_draw
# </POTBO_STAGE S2225>

# <POTBO_STAGE S2228>


FireMagicExplosion.ciz = _v91_fire_explosion_draw


_v91_ground_fire_init_raw = GroundFirePatch.__init__


def _v91_ground_fire_init(self, x, y, simdi, index=0):
    _v91_ground_fire_init_raw(self, x, y, simdi, index=index)
    self.v91_cluster_seed = int(
        float(x) * 97 + float(y) * 131 + index * 997
    )
# </POTBO_STAGE S2228>

# <POTBO_STAGE S2231>


GroundFirePatch.__init__ = _v91_ground_fire_init
GroundFirePatch.ciz = _v91_ground_fire_draw





V91_DRACO_LONG_RECTS = (
    (0, 72, 153, 49),
    (181, 73, 160, 49),
    (374, 73, 194, 49),
    (0, 133, 232, 42),
    (290, 137, 278, 38),
    (0, 190, 262, 15),
    (298, 190, 270, 15),
)
# </POTBO_STAGE S2231>

# <POTBO_STAGE S2233>


V91_DRACO_LONG_FRAMES = v91_draco_long_frames_load()
v91_draco_alpha_cache = {}


def v91_draco_distance_form(travelled):
    if (
        not V91_DRACO_LONG_FRAMES
        or float(travelled) < 104.0
    ):
        return None
    ratio = v90_clamp(
        (float(travelled) - 104.0)
        / max(1.0, V90_DRACO_MAX_TRAVEL - 104.0)
    )
    index = min(
        len(V91_DRACO_LONG_FRAMES) - 1,
        int(ratio * len(V91_DRACO_LONG_FRAMES)),
    )
    frame = V91_DRACO_LONG_FRAMES[index]
    if index <= 2:
        height = 43.0
    elif index <= 4:
        height = 30.0
    else:
        height = 11.0
    return frame, height
# </POTBO_STAGE S2233>

# <POTBO_STAGE S2235>


_v91_draco_bind_raw = V90DracoState.bind_target
# </POTBO_STAGE S2235>

# <POTBO_STAGE S2237>


V90DracoState.bind_target = _v91_draco_bind_target
# </POTBO_STAGE S2237>

# <POTBO_STAGE S2239>


V90DracoState.apply_rupture = _v91_draco_apply_rupture

_v91_rupture_draw_raw = v90_draw_rupture
# </POTBO_STAGE S2239>

# <POTBO_STAGE S2243>
V81_MAX_DROPLETS = 128
V88_DEATH_FLOW_LIMIT = min(V88_DEATH_FLOW_LIMIT, 6)
V89_FIRE_ECOLOGY_INTERVAL_MS = 360
# </POTBO_STAGE S2243>

# <POTBO_STAGE S2248>





v91_death_layer_cache = {}
v91_death_flame_cache = {}


def v91_mask_color_surface(source, color):
    mask = pygame.mask.from_surface(source, 8)
    return mask.to_surface(
        setcolor=(*tuple(color[:3]), 255),
        unsetcolor=(0, 0, 0, 0),
    ).convert_alpha()


def v91_capture_death_layer(
    cache_key, bucket, draw_callback, color
):
    key = (
        cache_key,
        int(bucket),
        int(v86_death_state.seed),
    )
    cached = v91_death_layer_cache.get(key)
    if cached is not None:
        return cached
    global ekran
    target = ekran
    layer = pygame.Surface(
        (GENISLIK, YUKSEKLIK), pygame.SRCALPHA
    )
    ekran = layer
    try:
        draw_callback()
    finally:
        ekran = target
    result = v91_mask_color_surface(layer, color)
    if len(v91_death_layer_cache) >= 8:
        for old in list(v91_death_layer_cache)[:3]:
            v91_death_layer_cache.pop(old, None)
    v91_death_layer_cache[key] = result
    return result
# </POTBO_STAGE S2248>

# <POTBO_STAGE S2254>


_v91_full_diagnostics_raw = v50_full_diagnostics


def v50_full_diagnostics():
    data = _v91_full_diagnostics_raw()
    data["v91"] = v91_diagnostics()
    return data


V91_STARTUP_CONTRACT = v91_diagnostics()
# </POTBO_STAGE S2254>

# <POTBO_STAGE S2258>
if _v91_smoke_prefix:
    try:
        print(
            json.dumps(
                v91_smoke_test(_v91_smoke_prefix),
                ensure_ascii=False,
                indent=2,
            )
        )
    finally:
        calisiyor = False
# </POTBO_STAGE S2258>

# <POTBO_STAGE S2261>


def _v92_trim(surface):
    if surface is None:
        return None
    bounds = surface.get_bounding_rect(min_alpha=2)
    if bounds.width <= 0 or bounds.height <= 0:
        return None
    return surface.subsurface(bounds).copy().convert_alpha()
# </POTBO_STAGE S2261>

# <POTBO_STAGE S2267>


def v59_technique_toast_ciz():
    return None


v92_level_stats = {
    "strength": 0.0,
    "speed": 0.0,
    "endurance": 0.0,
}


def v92_level_curve(level):
    level = max(1, min(MAKSIMUM_LEVEL, int(level)))
    p = (level - 1) / max(1.0, float(MAKSIMUM_LEVEL - 1))


    return {
        "strength": 0.18 + 0.22 * math.sqrt(p),
        "speed": 0.0042 + 0.0031 * math.sqrt(p),
        "endurance": 0.72 + 0.38 * math.sqrt(p),
    }
# </POTBO_STAGE S2267>

# <POTBO_STAGE S2273>





v92_next_footprint_distance = 13.0
v92_foot_rng = random.Random(0xB10D92)
# </POTBO_STAGE S2273>

# <POTBO_STAGE S2276>
V90_DRACO_SELL_PRICE = 1500
V90_DRACO_BUYBACK_PRICE = 1760
# </POTBO_STAGE S2276>

# <POTBO_STAGE S2279>

_v92_tight_icon_raw = v89_tight_icon
# </POTBO_STAGE S2279>

# <POTBO_STAGE S2282>


_v92_draco_draw_raw = v90_draco_draw
# </POTBO_STAGE S2282>

# <POTBO_STAGE S2284>


_v92_draco_reset_raw = V90DracoState.reset


def _v92_draco_reset(self):
    _v92_draco_reset_raw(self)
    self.trail = deque(maxlen=26)
    self.v92_left_screen = False


V90DracoState.reset = _v92_draco_reset

_v92_draco_update_raw = V90DracoState.update
# </POTBO_STAGE S2284>

# <POTBO_STAGE S2286>


V90DracoState.update = _v92_draco_update
# </POTBO_STAGE S2286>

# <POTBO_STAGE S2288>


V90DracoState.apply_rupture = _v92_draco_apply_rupture
# </POTBO_STAGE S2288>

# <POTBO_STAGE S2290>







def gelistirici_test_paneli_ciz():
    return None


v91_test_panel_visible = False
# </POTBO_STAGE S2290>

# <POTBO_STAGE S2294>

_v92_dev_raw = gelistirici_test_girdisi_uygula
# </POTBO_STAGE S2294>

# <POTBO_STAGE S2298>

V92_MEDOLI_COUNTERS_TR = (
    "Hanus dudak büker: 'Kusur dediğin şey, başka elde özellik diye satılır.'",
    "Hanus coinleri tartar; sayarken bir tanesini bilerek iki kez saymış gibi yapar.",
    "'Bu raftaki sonuncu,' der. Arkadaki sandığın kapağını ayağıyla kapatması pek ikna edici değildir.",
    "'Bugün fiyatlar arttı,' der; nedenini sorunca konuyu değiştirir.",
    "Hanus önce kabul edecekmiş gibi başını sallar, sonra küçük bir ek ücret sıkıştırır.",
    "'Bunu senden başkasına daha pahalı verirdim.' Sözünün doğruluğu belli değildir.",
    "Hanus malı ışığa tutup senin görmediğin bir üstünlük varmış gibi sessizce bekler.",
    "'Ben zararına satış yapmam.' Terazinin ibresi ise onun tarafına hafif eğiktir.",
)
V92_MEDOLI_COUNTERS_EN = (
    "Hanus curls his lip: 'What you call a defect is a feature in another market.'",
    "Hanus counts the coins and appears to count one of them twice on purpose.",
    "'Last one on the shelf,' he says while nudging a crate shut with his boot.",
    "'Prices rose today.' Asked why, he changes the subject.",
    "Hanus nods as if accepting, then tries to slip in a small surcharge.",
    "'I'd charge anyone else more.' There is no reason to trust that statement.",
    "Hanus holds the goods to the light and waits as if he can see a virtue you cannot.",
    "'I do not sell at a loss.' The scale needle still leans faintly his way.",
)
# </POTBO_STAGE S2298>

# <POTBO_STAGE S2300>
v92_armor_weight = "balanced"
v92_armor_rating = 0.0
v92_training = {"decussatio_rubra": 0, "catena_decollationis": 0}
# </POTBO_STAGE S2300>

# <POTBO_STAGE S2302>


_v92_game_draw_raw = oyun_ekrani_ciz
# </POTBO_STAGE S2302>

# <POTBO_STAGE S2305>


_v92_interaction_candidates_raw = _v34_interaction_candidates
# </POTBO_STAGE S2305>

# <POTBO_STAGE S2307>


def v92_equipment_speed_multiplier():
    if v92_armor_weight == "light":
        return 1.035
    if v92_armor_weight == "heavy":
        return 0.955
    return 1.0
# </POTBO_STAGE S2307>

# <POTBO_STAGE S2312>
V92_X_SPECIAL_MAX_RANGE = 220.0
# </POTBO_STAGE S2312>

# <POTBO_STAGE S2316>
V92_CHAIN_MAX_FORWARD = 385.0
V92_CHAIN_MAX_LATERAL = 138.0
V92_CHAIN_LINK_RANGE = 190.0
V92_CHAIN_HIT_SCALE = 1.42
# </POTBO_STAGE S2316>

# <POTBO_STAGE S2318>
V92_CHAIN_NORMAL_MS_PER_LINK = 94
# </POTBO_STAGE S2318>

# <POTBO_STAGE S2321>


v92_chain_state = V92ChainState()
# </POTBO_STAGE S2321>

# <POTBO_STAGE S2329>


_v92_cinematic_lock_raw = oyun_sinematik_kilitli_mi


def oyun_sinematik_kilitli_mi():
    return bool(v92_chain_state.active) or _v92_cinematic_lock_raw()
# </POTBO_STAGE S2329>

# <POTBO_STAGE S2332>





V91_DEATH_BODY = (168, 31, 47)
V84_BODY = (178, 16, 34)
V84_BODY_HOT = (205, 34, 48)
# </POTBO_STAGE S2332>

# <POTBO_STAGE S2337>


_v92_new_game_raw = yeni_oyun_baslat
# </POTBO_STAGE S2337>

# <POTBO_STAGE S2339>



v92_resource_balance_refresh()
# </POTBO_STAGE S2339>

# <POTBO_STAGE S2342>
TUS_BEKLEME_YON = 78
TUS_BEKLEME_AKSIYON = 105
TUS_BEKLEME_MODAL = 118
# </POTBO_STAGE S2342>

# <POTBO_STAGE S2345>
V63_TIERS["high"].update({"mist": 96, "filament": 44, "lobe": 24, "detail": 128})
V63_TIERS["balanced"].update({"mist": 64, "filament": 30, "lobe": 16, "detail": 86})
V63_TIERS["constrained"].update({"mist": 38, "filament": 18, "lobe": 10, "detail": 52})


def v63_choose_tier(frame_ms):
    ratio = float(frame_ms) / max(1.0, V63_FRAME_TARGET_MS)
    if ratio >= 1.22:
        return "constrained"
    if ratio >= 1.06:
        return "balanced"
    return "high"
# </POTBO_STAGE S2345>

# <POTBO_STAGE S2347>






V55_POOL_SCAN_INTERVAL_MS = 760
# </POTBO_STAGE S2347>

# <POTBO_STAGE S2351>


def _v94_trim(surface):
    if surface is None:
        return None
    bounds = surface.get_bounding_rect(min_alpha=2)
    if bounds.width <= 0 or bounds.height <= 0:
        return None
    return surface.subsurface(bounds).copy().convert_alpha()
# </POTBO_STAGE S2351>

# <POTBO_STAGE S2353>


def _v94_frame_score(frame):
    frame = _v94_trim(frame)
    if frame is None:
        return -1.0
    mask = pygame.mask.from_surface(frame, 1)
    area = float(mask.count())
    w, h = frame.get_size()
    if area <= 0 or w <= 0 or h <= 0:
        return -1.0


    flipped = pygame.transform.flip(frame, True, False)
    mirror = pygame.mask.from_surface(flipped, 1)
    overlap = mask.overlap_area(mirror, (0, 0)) / max(1.0, area)
    density = area / max(1.0, float(w * h))
    return area * (0.72 + 0.28 * overlap) + density * 120.0


def _v94_best(frames):
    scored = [(_v94_frame_score(frame), _v94_trim(frame)) for frame in frames]
    scored = [(score, frame) for score, frame in scored if frame is not None]
    if not scored:
        return None
    return max(scored, key=lambda pair: pair[0])[1]
# </POTBO_STAGE S2353>

# <POTBO_STAGE S2355>


def _v94_projection_bands(values, threshold, min_len):
    result = []
    start = None
    for index, value in enumerate(values):
        if value > threshold and start is None:
            start = index
        elif value <= threshold and start is not None:
            if index - start >= min_len:
                result.append((start, index))
            start = None
    if start is not None and len(values) - start >= min_len:
        result.append((start, len(values)))
    return result
# </POTBO_STAGE S2355>

# <POTBO_STAGE S2357>




def v91_draco_distance_form(travelled):
    return None
# </POTBO_STAGE S2357>

# <POTBO_STAGE S2361>
V92_CHAIN_NORMAL_MS_PER_LINK = 74
V94_CHAIN_RECOVERY_MS = 920
v94_chain_next_ready_ms = 0
# </POTBO_STAGE S2361>

# <POTBO_STAGE S2364>


_v94_chain_start_previous = v92_chain_start
# </POTBO_STAGE S2364>

# <POTBO_STAGE S2369>





v94_test_panel_visible = False
_v94_dev_previous = gelistirici_test_girdisi_uygula
# </POTBO_STAGE S2369>

# <POTBO_STAGE S2374>
TUS_BEKLEME_YON = 105
TUS_BEKLEME_AKSIYON = 180
TUS_BEKLEME_MODAL = 240
# </POTBO_STAGE S2374>

# <POTBO_STAGE S2376>


def v95_currency(amount):
    amount = int(amount)
    return bt(f"{amount} altın", f"{amount} coin" if amount == 1 else f"{amount} coins")
# </POTBO_STAGE S2376>

# <POTBO_STAGE S2382>






V90_DRACO_CAST_MS = 430
V90_DRACO_SPEED = 690.0
V90_DRACO_BITE_MS = 135
V90_DRACO_COIL_MS = 355
V90_DRACO_COLLAPSE_MS = 145
V90_DRACO_RUPTURE_MS = 330



V95_DRACO_FLIGHT_INDICES = tuple(
    i for i in (6, 7, 8) if 0 <= i < len(V90_DRACO_FRAMES)
)
if not V95_DRACO_FLIGHT_INDICES and V90_DRACO_FRAMES:
    V95_DRACO_FLIGHT_INDICES = (len(V90_DRACO_FRAMES) - 1,)


def v91_draco_distance_form(travelled):
    return None


_v95_draco_update_previous = V90DracoState.update
# </POTBO_STAGE S2382>

# <POTBO_STAGE S2384>


V90DracoState.update = _v95_draco_update
# </POTBO_STAGE S2384>

# <POTBO_STAGE S2388>


_v95_draco_rupture_previous = V90DracoState.apply_rupture
# </POTBO_STAGE S2388>

# <POTBO_STAGE S2390>


V90DracoState.apply_rupture = _v95_draco_apply_rupture
# </POTBO_STAGE S2390>

# <POTBO_STAGE S2392>


V55_POOL_SCAN_INTERVAL_MS = 980
# </POTBO_STAGE S2392>

# <POTBO_STAGE S2395>
v96_son_ikna_sansi = 0.0
v96_son_ikna_basarili = None
v96_hanus_hile_yakalandi = False
v96_hanus_hile_sayisi = 0


def v96_ikna_ustaligi():
    return max(1, min(10, 1 + int(v96_ikna_xp) // 4))
# </POTBO_STAGE S2395>

# <POTBO_STAGE S2397>

V96_HANUS_BASARI_TR = (
    "Peki, o kadar da kör değilmişsin. Biraz inerim.",
    "Tamam. Bu cümle coin etti; rakamı biraz kırıyorum.",
    "İyi bastırdın. Fiyatı aşağı çekiyorum ama fazla sevinme.",
    "Olur. Bu tur senin. Biraz daha yaklaşırım.",
)
V96_HANUS_BASARISIZ_TR = (
    "Güzel deneme. Ama o rakamla mal bende kalır.",
    "Beni ikna etmedin. Fiyat hâlâ benim söylediğim yerde.",
    "O hikâyeyi başkasına anlat. Ben rakamla konuşurum.",
    "Hayır. O kadar kolay coin bırakmam.",
)
V96_HANUS_BASARI_EN = (
    "Fine. You are not blind after all. I will come down a little.",
    "All right. That argument was worth coin. I will trim the number.",
    "Good pressure. I will lower it, but do not celebrate yet.",
    "Fine. That round is yours. I will move a little.",
)
V96_HANUS_BASARISIZ_EN = (
    "Nice try. At that number the goods stay with me.",
    "You did not convince me. My price still stands.",
    "Tell that story to someone else. I deal in numbers.",
    "No. I do not give coin away that easily.",
)
V96_REINALD_BASARI_TR = (
    "Mantıklı. O kısmı işçilikten düşerim.",
    "Haklısın. Hesabı yeniden yaparım.",
    "Bu şartla olur. Biraz aşağı inerim.",
    "Peki. O kalemi fiyattan çıkarıyorum.",
)
V96_REINALD_BASARISIZ_TR = (
    "Hayır. O şartta düzgün iş çıkaramam.",
    "O rakama inmem. Malzemenin bir bedeli var.",
    "Bunu kabul edersem işten çalarım. Yapmam.",
    "Olmaz. Fiyatı düşürmek için daha sağlam bir sebep söyle.",
)
V96_REINALD_BASARI_EN = (
    "Reasonable. I can remove that part from the labor cost.",
    "You are right. I will run the numbers again.",
    "Under that condition, yes. I can come down a little.",
    "Fine. I will remove that line from the price.",
)
V96_REINALD_BASARISIZ_EN = (
    "No. I cannot do proper work under that condition.",
    "I will not go that low. Material has a cost.",
    "If I accept that, I cut corners. I do not do that.",
    "No. Give me a better reason to lower the price.",
)
# </POTBO_STAGE S2397>

# <POTBO_STAGE S2401>
V97_HANUS_NAME = "HANUS"
V97_REINALD_NAME = "REINALD"
# </POTBO_STAGE S2401>

# <POTBO_STAGE S2414>





_v97_game_draw_raw = oyun_ekrani_ciz
# </POTBO_STAGE S2414>

# <POTBO_STAGE S2421>
V98_STATUS_ICON_CACHE = {}
# </POTBO_STAGE S2421>

# <POTBO_STAGE S2426>


V98_UNIVERSAL_FIRE_FRAMES = _v98_universal_fire_frames_load()
V98_FIRE_SCALE_CACHE = {}
# </POTBO_STAGE S2426>

# <POTBO_STAGE S2430>


GroundFirePatch.ciz = _v98_ground_fire_draw
# </POTBO_STAGE S2430>

# <POTBO_STAGE S2432>


v98_projectile_trail_fires = []
V98_FIRE_TRAIL_START_DISTANCE = 54.0
V98_FIRE_TRAIL_STEP = 31.0
V98_FIRE_TRAIL_MAX = 70

_v98_fire_projectile_update_raw = FireMagicProjectile.guncelle


def _v98_fire_projectile_update(self, dt, simdi):
    if not hasattr(self, "v98_next_trail_distance"):
        self.v98_next_trail_distance = float(V98_FIRE_TRAIL_START_DISTANCE)
        self.v98_trail_seed = random.randint(0, 1_000_000)

    result = _v98_fire_projectile_update_raw(self, dt, simdi)

    if not V98_UNIVERSAL_FIRE_FRAMES:
        return result

    travelled = max(0.0, float(getattr(self, "travelled", 0.0)))
    spawned = 0
    while self.v98_next_trail_distance <= travelled and spawned < 4:
        distance = float(self.v98_next_trail_distance)
        pos = pygame.Vector2(self.start) + pygame.Vector2(self.direction) * distance
        v98_projectile_trail_fires.append(
            V98ProjectileTrailFire(
                pos.x,
                pos.y,
                simdi,
                self.v98_trail_seed + int(distance),
            )
        )
        self.v98_next_trail_distance += float(V98_FIRE_TRAIL_STEP)
        spawned += 1

    if len(v98_projectile_trail_fires) > V98_FIRE_TRAIL_MAX:
        del v98_projectile_trail_fires[:-V98_FIRE_TRAIL_MAX]
    return result


FireMagicProjectile.guncelle = _v98_fire_projectile_update
# </POTBO_STAGE S2432>

# <POTBO_STAGE S2434>










V99_VERSION = "99.0"
# </POTBO_STAGE S2434>

# <POTBO_STAGE S2446>
v98_projectile_trail_fires.clear()
# </POTBO_STAGE S2446>

# <POTBO_STAGE S2448>
V99_EXPLOSION_FIRE_SPAWN_RADIUS = max(72.0, V99_EXPLOSION_FIRE_VISUAL_RADIUS - 30.0)
V99_EXPLOSION_FIRE_MIN = 34
V99_EXPLOSION_FIRE_MAX = 46
# </POTBO_STAGE S2448>

# <POTBO_STAGE S2450>


FireMagicExplosion._detonate = _v99_fire_explosion_detonate
# </POTBO_STAGE S2450>

# <POTBO_STAGE S2452>


GroundFirePatch.ciz = _v99_ground_fire_draw
# </POTBO_STAGE S2452>

# <POTBO_STAGE S2466>
V92_CHAIN_NORMAL_MS_PER_LINK = 76
V100_CATENA_MIN_TARGETS = 2
# </POTBO_STAGE S2466>

# <POTBO_STAGE S2472>


FireMagicProjectile.ciz = _v100_fire_projectile_draw

v98_projectile_trail_fires.clear()
# </POTBO_STAGE S2472>

# <POTBO_STAGE S2474>


v100_negotiation = V100NegotiationState()

V100_HANUS_LINES = (
    {"tr": "Hanus, bu rakam malın değerinden yüksek. Daha gerçekçi bir fiyat söyle.", "en": "Hanus, that number is above the value of the goods. Give me a realistic price.", "lev": 1.05, "risk": 0.17, "tone": "reason"},
    {"tr": "Bugün senden alırım; ama beni tekrar müşteri olarak görmek istiyorsan fiyatı indir.", "en": "I will buy from you today, but if you want me back, lower the price.", "lev": 1.12, "risk": 0.20, "tone": "relationship"},
    {"tr": "Peşin ödeyeceğim. Bunun karşılığında daha iyi bir rakam istiyorum.", "en": "I will pay immediately. In return, I want a better number.", "lev": 0.98, "risk": 0.10, "tone": "deal"},
    {"tr": "Bu kadar kâr sana yeter. Aradaki farkı biraz paylaş.", "en": "That is enough profit for you. Share some of the margin.", "lev": 1.18, "risk": 0.26, "tone": "pressure"},
    {"tr": "Başka tezgâhlara da bakabilirim. Beni burada tutacak bir fiyat söyle.", "en": "I can check other stalls. Give me a price that keeps me here.", "lev": 1.24, "risk": 0.32, "tone": "walkaway"},
    {"tr": "Malı beğendim, ama ilk söylediğin rakamı kabul etmiyorum.", "en": "I like the goods, but I will not accept your first number.", "lev": 1.00, "risk": 0.13, "tone": "firm"},
)

V100_REINALD_LINES = (
    {"tr": "Reinald, işçiliğine lafım yok; ama bu malzeme hesabı fazla. Yeniden hesapla.", "en": "Reinald, I trust your workmanship, but the material estimate is high. Run it again.", "lev": 1.10, "risk": 0.14, "tone": "reason"},
    {"tr": "İş acil değil. Boş zamanında yaparsan işçilikten biraz düşebilir misin?", "en": "The work is not urgent. If you do it in your spare time, can you reduce the labor cost?", "lev": 1.02, "risk": 0.08, "tone": "schedule"},
    {"tr": "Süsleme istemiyorum; yalnız işe yarayan kısmı yap. Fiyatı buna göre düşür.", "en": "I do not want decoration; do only what matters. Lower the price accordingly.", "lev": 1.16, "risk": 0.12, "tone": "scope"},
    {"tr": "Bir sonraki işi de sana getiririm. Bu işte bana biraz pay bırak.", "en": "I will bring you the next job too. Leave me some room on this one.", "lev": 1.08, "risk": 0.15, "tone": "relationship"},
    {"tr": "Bu rakamı kabul edersem malzemeyi ayrıca sorgularım. Baştan temiz bir hesap yapalım.", "en": "If I accept that number I will audit the material separately. Let us make a clean estimate now.", "lev": 1.20, "risk": 0.24, "tone": "firm"},
    {"tr": "İşi senden almak istiyorum; fakat bu fiyat bütçemi aşıyor. Ortada buluşalım.", "en": "I want you to do the work, but that price exceeds my budget. Meet me in the middle.", "lev": 1.00, "risk": 0.09, "tone": "deal"},
)
# </POTBO_STAGE S2474>

# <POTBO_STAGE S2478>


_v100_selection_signature_base = secim_imzasi_al
# </POTBO_STAGE S2478>

# <POTBO_STAGE S2487>


def _v102_upgrade_fallback(kind, size):
    """PNG bulunmazsa harf yerine basit grafik sembol kullan."""
    size = max(18, int(size))
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    gold = (245, 192, 54, 255)
    white = (255, 244, 208, 255)
    red = (210, 47, 52, 255)
    c = size // 2
    t = max(2, size // 14)

    if kind == "weapon":

        pygame.draw.line(surf, gold, (size * 0.23, size * 0.78), (size * 0.76, size * 0.20), t + 2)
        pygame.draw.line(surf, white, (size * 0.26, size * 0.75), (size * 0.74, size * 0.22), max(1, t // 2))
        pygame.draw.line(surf, red, (size * 0.20, size * 0.65), (size * 0.36, size * 0.81), t)
    elif kind == "armor":
        pts = [
            (c, int(size * 0.14)),
            (int(size * 0.76), int(size * 0.25)),
            (int(size * 0.70), int(size * 0.66)),
            (c, int(size * 0.86)),
            (int(size * 0.30), int(size * 0.66)),
            (int(size * 0.24), int(size * 0.25)),
        ]
        pygame.draw.polygon(surf, gold, pts, t)
        pygame.draw.line(surf, white, (c, int(size * 0.21)), (c, int(size * 0.72)), max(1, t // 2))
    else:

        pts = [
            (int(size * 0.12), c),
            (int(size * 0.30), c),
            (int(size * 0.40), int(size * 0.72)),
            (int(size * 0.52), int(size * 0.25)),
            (int(size * 0.62), int(size * 0.58)),
            (int(size * 0.74), c),
            (int(size * 0.88), c),
        ]
        pygame.draw.lines(surf, gold, False, pts, t + 1)
        pygame.draw.lines(surf, white, False, pts, max(1, t // 2))
    return surf
# </POTBO_STAGE S2487>

# <POTBO_STAGE S2493>
V103_TEXT_CACHE_LIMIT = 960


def _v103_renk_anahtari(renk):
    try:
        return tuple(int(v) for v in renk)
    except TypeError:
        return renk
# </POTBO_STAGE S2493>

# <POTBO_STAGE S2495>






V103_SHADOW_CACHE = {}


def karakter_zemin_golgesi_ciz(x, y, genislik, yukseklik, alpha=72):
    width = max(6, int(round(genislik)))
    height = max(3, int(round(yukseklik)))
    alpha_i = max(0, min(150, int(alpha)))
    key = (width, height, alpha_i)
    surface = V103_SHADOW_CACHE.get(key)
    if surface is None:
        surface = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        cut = max(1, min(height - 1, width // 8))
        polygon = (
            (cut, 0),
            (width - cut - 1, 0),
            (width - 1, height // 2),
            (width - cut * 2, height - 1),
            (cut * 2, height - 1),
            (0, height // 2),
        )
        pygame.draw.polygon(surface, (0, 0, 0, alpha_i), polygon)
        if len(V103_SHADOW_CACHE) >= 48:
            V103_SHADOW_CACHE.clear()
        V103_SHADOW_CACHE[key] = surface
    left = int(round(float(x) - width * 0.5))
    top = int(round(float(y) - height * 0.5))
    ekran.blit(surface, (left, top))
# </POTBO_STAGE S2495>

# <POTBO_STAGE S2498>
V103_PARTICLE_DRAW_BUDGET = {
    "high": 128,
    "balanced": 96,
    "constrained": 72,
}
# </POTBO_STAGE S2498>

# <POTBO_STAGE S2505>


_v105_dev_input_previous = gelistirici_test_girdisi_uygula
# </POTBO_STAGE S2505>

# <POTBO_STAGE S2507>


GELISTIRICI_TEST_TUSLARI.add(pygame.K_3)
# </POTBO_STAGE S2507>

# <POTBO_STAGE S2509>

_v105_tile_objects_previous = v89_tile_objects
# </POTBO_STAGE S2509>

# <POTBO_STAGE S2511>
V105_MAGGOT_FIRST_MAX_MS = 90_000
# </POTBO_STAGE S2511>

# <POTBO_STAGE S2516>











V106_VERSION = "107.0"
# </POTBO_STAGE S2516>

# <POTBO_STAGE S2520>


V106_CRITICAL_WASH_CACHE = {}
# </POTBO_STAGE S2520>

# <POTBO_STAGE S2522>


_v106_game_draw_previous = oyun_ekrani_ciz


def oyun_ekrani_ciz():
    result = _v106_game_draw_previous()
    v106_critical_screen_wash()
    return result
# </POTBO_STAGE S2522>

# <POTBO_STAGE S2528>






V106_EADRIC_MANA_BASE_PER_SEC = 0.72
V106_EADRIC_MANA_POOL_FACTOR = 0.0026
v106_mana_tick_ms = pygame.time.get_ticks()
# </POTBO_STAGE S2528>

# <POTBO_STAGE S2535>

V106_CORONA_MANA_COST = 50
V106_CORONA_COOLDOWN_MS = 12000
V106_CORONA_ORBIT_MS = 6500
V106_CORONA_ORBIT_RADIUS = 56.0
V106_CORONA_PROJECTILE_SPEED = 520.0
V106_CORONA_PROJECTILE_LIFE_MS = 1500
V106_CORONA_CONTACT_COOLDOWN_MS = 430
# </POTBO_STAGE S2535>

# <POTBO_STAGE S2537>
v106_corona_last_cast_ms = -1000000
v106_corona_transform_cache = {}
# </POTBO_STAGE S2537>

# <POTBO_STAGE S2539>


V106_CORONA_FRAMES = v106_corona_frames_load()
# </POTBO_STAGE S2539>

# <POTBO_STAGE S2542>


@dataclass
class V106CoronaProjectile:
    x: float
    y: float
    direction: pygame.Vector2
    born_ms: int
    core_id: int
    active: bool = True
    last_ms: int = 0
    trail: Any = field(default_factory=lambda: deque(maxlen=5))

    def __post_init__(self):
        self.direction = pygame.Vector2(self.direction)
        if self.direction.length_squared() <= 1e-8:
            self.direction = pygame.Vector2(1.0, 0.0)
        self.direction = self.direction.normalize()
        self.last_ms = int(self.born_ms)
        self.trail.append((float(self.x), float(self.y)))


@dataclass
class V106CoronaImpact:
    x: float
    y: float
    born_ms: int


class V106CoronaState:
    def __init__(self):
        self.reset()

    def reset(self):
        self.active = False
        self.started_ms = 0
        self.expires_ms = 0
        self.cores = []
        self.projectiles = []
        self.impacts = []
        self.contact_next = {}
        self.seed = 0


v106_corona = V106CoronaState()


def v106_corona_active_orbs():
    return bool(v106_corona.active and v106_corona.cores)


def v106_corona_phase_angle(now):
    age = max(0.0, (int(now) - int(v106_corona.started_ms)) / 1000.0)
    ramp = min(1.0, age / 0.85)
    speed = 2.35 + 6.65 * (ramp * ramp * (3.0 - 2.0 * ramp))
    return age * speed
# </POTBO_STAGE S2542>

# <POTBO_STAGE S2547>


def v106_corona_launch(core_id, origin, direction, now):
    projectile = V106CoronaProjectile(
        float(origin.x),
        float(origin.y),
        pygame.Vector2(direction),
        int(now),
        int(core_id),
    )
    v106_corona.projectiles.append(projectile)
    return projectile
# </POTBO_STAGE S2547>

# <POTBO_STAGE S2550>


_v106_q_use_previous = q_hizli_itemi_kullan
# </POTBO_STAGE S2550>

# <POTBO_STAGE S2558>










V108_VERSION = "108.0"






V108_DEV_UNLIMITED_SPELLS = set()
# </POTBO_STAGE S2558>

# <POTBO_STAGE S2560>


_v108_grant_bind_raw = v91_grant_and_bind_spell


def v91_grant_and_bind_spell(item_id):
    ok = bool(_v108_grant_bind_raw(item_id))
    if ok:
        V108_DEV_UNLIMITED_SPELLS.add(str(item_id))
    return ok
# </POTBO_STAGE S2560>

# <POTBO_STAGE S2562>


_v108_q_use_raw = q_hizli_itemi_kullan
# </POTBO_STAGE S2562>

# <POTBO_STAGE S2565>
V106_CORONA_PROJECTILE_SPEED = 760.0
V106_CORONA_CONTACT_COOLDOWN_MS = 280
# </POTBO_STAGE S2565>

# <POTBO_STAGE S2567>
V108_CORONA_BRIGHT_CACHE = {}


def v106_corona_phase_angle(now):
    age = max(0.0, (int(now) - int(v106_corona.started_ms)) / 1000.0)

    ramp = min(1.0, age / 0.46)
    smooth = ramp * ramp * (3.0 - 2.0 * ramp)
    speed = 4.4 + 12.8 * smooth

    return age * speed + math.sin(age * 23.0) * (0.025 + 0.055 * smooth)
# </POTBO_STAGE S2567>

# <POTBO_STAGE S2571>



_v108_q_slot_draw_raw = v89_q_slot_draw
# </POTBO_STAGE S2571>

# <POTBO_STAGE S2575>


_v108_game_draw_raw = oyun_ekrani_ciz
# </POTBO_STAGE S2575>

# <POTBO_STAGE S2578>










V109_VERSION = "109.0"
# </POTBO_STAGE S2578>

# <POTBO_STAGE S2580>
V109_CORONA_GLOW_CACHE = {}
# </POTBO_STAGE S2580>

# <POTBO_STAGE S2582>


def v109_corona_glow_surface(size, alpha=255):
    size = max(8, int(size))
    alpha_bucket = max(0, min(255, int(alpha // 32) * 32))
    key = (size, alpha_bucket)
    cached = V109_CORONA_GLOW_CACHE.get(key)
    if cached is not None:
        return cached
    extent = max(size + 10, int(round(size * 1.85)))
    surf = pygame.Surface((extent, extent), pygame.SRCALPHA).convert_alpha()
    c = extent // 2
    a = max(0.0, min(1.0, alpha / 255.0))

    pygame.draw.circle(surf, (220, 242, 255, int(15 * a)), (c, c), max(2, int(extent * 0.48)))
    pygame.draw.circle(surf, (231, 247, 255, int(23 * a)), (c, c), max(2, int(extent * 0.35)))
    pygame.draw.circle(surf, (244, 252, 255, int(31 * a)), (c, c), max(2, int(extent * 0.24)))
    if len(V109_CORONA_GLOW_CACHE) >= 48:
        for old in list(V109_CORONA_GLOW_CACHE)[:12]:
            V109_CORONA_GLOW_CACHE.pop(old, None)
    V109_CORONA_GLOW_CACHE[key] = surf
    return surf
# </POTBO_STAGE S2582>

# <POTBO_STAGE S2584>
V109_CORONA_HOMING_RELEASE_RANGE = 390.0
V109_CORONA_HOMING_TURN_DEG_PER_SEC = 145.0
V109_CORONA_DIRECT_HIT_RADIUS = 28.0
V109_CORONA_REPULSION_RADIUS = 112.0
V109_CORONA_REPULSION_SPEED = 148.0
# </POTBO_STAGE S2584>

# <POTBO_STAGE S2586>


def v109_corona_target_valid(actor):
    return bool(actor is not None and v90_actor_alive(actor))


def v109_corona_find_target(projectile):
    origin = pygame.Vector2(float(projectile.x), float(projectile.y))
    forward = pygame.Vector2(projectile.direction)
    if forward.length_squared() <= 1e-8:
        forward = pygame.Vector2(1.0, 0.0)
    else:
        forward = forward.normalize()
    best = None
    best_score = 10**18
    for actor in _v35_physical_targets():
        if not v109_corona_target_valid(actor):
            continue
        center = v90_actor_center(actor)
        delta = center - origin
        dist = delta.length()
        if dist <= 1e-6 or dist > V109_CORONA_HOMING_RANGE:
            continue
        desired = delta / dist
        dot = forward.dot(desired)

        if dot < 0.08:
            continue
        score = dist * (1.0 + (1.0 - dot) * 0.42)
        if score < best_score:
            best_score = score
            best = actor
    return best


def v109_corona_steer(projectile, dt):
    target = getattr(projectile, "v109_target", None)
    if target is not None:
        if not v109_corona_target_valid(target):
            target = None
        else:
            delta = v90_actor_center(target) - pygame.Vector2(projectile.x, projectile.y)
            if delta.length() > V109_CORONA_HOMING_RELEASE_RANGE:
                target = None
    if target is None:
        target = v109_corona_find_target(projectile)
    projectile.v109_target = target
    if target is None:
        return

    desired = v90_actor_center(target) - pygame.Vector2(projectile.x, projectile.y)
    if desired.length_squared() <= 1e-8:
        return
    desired = desired.normalize()
    current = pygame.Vector2(projectile.direction)
    if current.length_squared() <= 1e-8:
        current = desired
    else:
        current = current.normalize()
    angle = current.angle_to(desired)
    max_turn = float(V109_CORONA_HOMING_TURN_DEG_PER_SEC) * max(0.0, float(dt))
    angle = max(-max_turn, min(max_turn, angle))
    projectile.direction = current.rotate(angle).normalize()


def v109_segment_closest(a, b, p):
    a = pygame.Vector2(a)
    b = pygame.Vector2(b)
    p = pygame.Vector2(p)
    ab = b - a
    denom = ab.length_squared()
    if denom <= 1e-10:
        return 0.0, a, p.distance_to(a)
    t = max(0.0, min(1.0, (p - a).dot(ab) / denom))
    closest = a + ab * t
    return t, closest, p.distance_to(closest)
# </POTBO_STAGE S2586>

# <POTBO_STAGE S2588>


def v109_corona_repulsion(projectile, dt):
    center = pygame.Vector2(float(projectile.x), float(projectile.y))
    for actor in _v35_physical_targets():
        if not v109_corona_target_valid(actor):
            continue
        delta = v90_actor_center(actor) - center
        dist = delta.length()
        if dist <= V109_CORONA_DIRECT_HIT_RADIUS or dist >= V109_CORONA_REPULSION_RADIUS:
            continue
        if dist <= 1e-6:
            direction = pygame.Vector2(1.0, 0.0)
        else:
            direction = delta / dist
        falloff = 1.0 - dist / V109_CORONA_REPULSION_RADIUS
        push = V109_CORONA_REPULSION_SPEED * (falloff ** 1.20) * max(0.0, float(dt))
        if push > 0.02:
            v106_corona_knockback(actor, direction, push)


_v109_corona_launch_raw = v106_corona_launch


def v106_corona_launch(core_id, origin, direction, now):
    projectile = _v109_corona_launch_raw(core_id, origin, direction, now)
    projectile.v109_target = v109_corona_find_target(projectile)
    return projectile


_v109_corona_apply_hit_raw = v106_corona_apply_hit
# </POTBO_STAGE S2588>

# <POTBO_STAGE S2593>


_v109_game_draw_raw = oyun_ekrani_ciz


def oyun_ekrani_ciz():
    v109_consumable_flash_update()
    return _v109_game_draw_raw()
# </POTBO_STAGE S2593>

# <POTBO_STAGE S2595>
V109_EADRIC_BAR_SQUARES = 6.0
v109_eadric_next_tick_ms = pygame.time.get_ticks() + V109_EADRIC_TICK_MS
# </POTBO_STAGE S2595>

# <POTBO_STAGE S2597>
_v109_has_eadric_stone_raw = v106_has_eadric_stone
# </POTBO_STAGE S2597>

# <POTBO_STAGE S2601>


_v110_item_desc_raw = item_aciklamasi
# </POTBO_STAGE S2601>

# <POTBO_STAGE S2603>


_v110_q_ok_raw = item_q_hizli_kullanima_uygun_mu
# </POTBO_STAGE S2603>

# <POTBO_STAGE S2605>





GELISTIRICI_TEST_TUSLARI.add(pygame.K_4)
# </POTBO_STAGE S2605>

# <POTBO_STAGE S2608>


_v110_dev_input_raw = gelistirici_test_girdisi_uygula
# </POTBO_STAGE S2608>

# <POTBO_STAGE S2610>


_v110_test_panel_raw = gelistirici_test_paneli_ciz
# </POTBO_STAGE S2610>

# <POTBO_STAGE S2616>



def v110_polyline_points(start, end, jitter=16.0, segments=7, seed=0):
    start = pygame.Vector2(start)
    end = pygame.Vector2(end)
    delta = end - start
    distance = max(1.0, delta.length())
    direction = delta.normalize() if distance > 1e-6 else pygame.Vector2(1.0, 0.0)
    normal = pygame.Vector2(-direction.y, direction.x)
    rng = random.Random(int(seed))
    points = [start]
    segment_count = max(5, int(segments))
    for i in range(1, segment_count):
        t = i / float(segment_count)
        base = start.lerp(end, t)
        taper = 1.0 - abs(t - 0.5) * 1.35
        offset = normal * rng.uniform(-jitter, jitter) * taper
        points.append(base + offset)
    points.append(end)
    return points



def v110_build_branches(points, seed=0):
    if len(points) < 3:
        return []
    rng = random.Random(int(seed) ^ 0xA51C)
    branches = []
    for idx in range(1, len(points) - 1):
        if rng.random() > 0.38:
            continue
        a = pygame.Vector2(points[idx])
        b = pygame.Vector2(points[idx + 1])
        direction = b - a
        if direction.length_squared() <= 1e-6:
            continue
        direction = direction.normalize()
        normal = pygame.Vector2(-direction.y, direction.x)
        length = rng.uniform(14.0, 38.0)
        side = -1.0 if rng.random() < 0.5 else 1.0
        tip = a + direction * length * rng.uniform(0.35, 0.7) + normal * side * length
        branches.append(v110_polyline_points(a, tip, jitter=8.0, segments=3, seed=rng.randint(0, 10**6)))
    return branches
# </POTBO_STAGE S2616>

# <POTBO_STAGE S2618>



def v110_apply_stun(actor, ms):
    if actor is None:
        return
    now = pygame.time.get_ticks()
    for attr in ("hit_stun_until", "recovery_until", "stagger_until"):
        if hasattr(actor, attr):
            setattr(actor, attr, max(int(getattr(actor, attr, 0)), int(now) + int(ms)))
# </POTBO_STAGE S2618>

# <POTBO_STAGE S2620>


_v110_q_use_raw = q_hizli_itemi_kullan
# </POTBO_STAGE S2620>

# <POTBO_STAGE S2623>



def v110_draw_polyline(points, color, width=1):
    if len(points) < 2:
        return
    screen = [v110_screen_point((p.x, p.y) if isinstance(p, pygame.Vector2) else p) for p in points]
    if width <= 1:
        pygame.draw.aalines(ekran, color, False, screen)
    else:
        pygame.draw.lines(ekran, color, False, screen, int(width))
        try:
            pygame.draw.aalines(ekran, color, False, screen)
        except pygame.error:
            pass
# </POTBO_STAGE S2623>

# <POTBO_STAGE S2629>


_v110_brightness_raw = parlaklik_kaplamasi_ciz
# </POTBO_STAGE S2629>

# <POTBO_STAGE S2636>


_v111_brightness_raw = parlaklik_kaplamasi_ciz
# </POTBO_STAGE S2636>

# <POTBO_STAGE S2638>


def _v112_visible_hostiles():
    visible = []
    for actor in v90_hostiles():
        try:
            if "_v103_obj_visible" in globals() and not _v103_obj_visible(actor, 220.0):
                continue
        except Exception:
            pass
        visible.append(actor)
    return visible
# </POTBO_STAGE S2638>

# <POTBO_STAGE S2642>



def v112_polyline_prefix(points, progress):
    if not points:
        return []
    if progress >= 0.999:
        return list(points)
    progress = max(0.0, min(1.0, float(progress)))
    seg_lengths = []
    total = 0.0
    for i in range(len(points) - 1):
        a = pygame.Vector2(points[i])
        b = pygame.Vector2(points[i + 1])
        d = a.distance_to(b)
        seg_lengths.append(d)
        total += d
    if total <= 1e-6:
        return [points[0]]
    target = total * progress
    out = [points[0]]
    run = 0.0
    for i, seg_len in enumerate(seg_lengths):
        a = pygame.Vector2(points[i])
        b = pygame.Vector2(points[i + 1])
        if run + seg_len <= target:
            out.append(points[i + 1])
            run += seg_len
            continue
        remain = max(0.0, target - run)
        t = 0.0 if seg_len <= 1e-6 else remain / seg_len
        out.append(a.lerp(b, t))
        break
    return out
# </POTBO_STAGE S2642>

# <POTBO_STAGE S2646>


_v112_brightness_raw = parlaklik_kaplamasi_ciz
# </POTBO_STAGE S2646>

# <POTBO_STAGE S2648>


def v113_polyline_tail(points, progress):

    try:
        return v112_polyline_prefix(points, progress)
    except Exception:
        return list(points)



def v113_draw_additive_glow(points, widths_alphas, color=(196, 225, 255)):
    if len(points) < 2:
        return
    layer = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA).convert_alpha()
    screen = [v110_screen_point((p.x, p.y) if isinstance(p, pygame.Vector2) else p) for p in points]
    for width, alpha in widths_alphas:
        col = (color[0], color[1], color[2], max(0, min(255, int(alpha))))
        try:
            pygame.draw.lines(layer, col, False, screen, max(1, int(width)))
            pygame.draw.aalines(layer, col[:3], False, screen)
        except pygame.error:
            pass
    ekran.blit(layer, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)
# </POTBO_STAGE S2648>

# <POTBO_STAGE S2652>


_v113_brightness_raw = parlaklik_kaplamasi_ciz
# </POTBO_STAGE S2652>

# <POTBO_STAGE S2654>


def v114_glow_line(layer, points, widths_alphas, color=(196, 224, 255)):
    if len(points) < 2:
        return
    screen = [v110_screen_point((p.x, p.y) if isinstance(p, pygame.Vector2) else p) for p in points]
    for width, alpha in widths_alphas:
        col = (color[0], color[1], color[2], max(0, min(255, int(alpha))))
        try:
            pygame.draw.lines(layer, col, False, screen, max(1, int(width)))
        except pygame.error:
            pass
# </POTBO_STAGE S2654>

# <POTBO_STAGE S2661>


_v114_brightness_raw = parlaklik_kaplamasi_ciz
# </POTBO_STAGE S2661>

# <POTBO_STAGE S2671>



_v117_ground_draw_raw = v111_draw_ground_electric
# </POTBO_STAGE S2671>

# <POTBO_STAGE S2673>


_v117_brightness_raw = parlaklik_kaplamasi_ciz
# </POTBO_STAGE S2673>

