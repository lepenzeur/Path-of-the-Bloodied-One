# Path of the Bloodied One — categorized source stages
#
# This file is intentionally executed by core/bootstrap.py in original source order.
# Keeping one shared runtime namespace avoids gameplay regressions while the former
# 90k-line monolith is physically separated by responsibility. Do not import this
# file directly; edit the stage code normally and launch root main.py.

# <POTBO_STAGE S0033>

# Kılıç boşluğu keserken sessizdir. Bu sample'lar yalnız gerçek melee temasında
# çağrılır: Crawler/Berserker/Heads Thrower/Tarkard = no armor, Torrmund = armor.
STAB_NO_ARMOR_SES_ADAYLARI = [
    os.path.join(ASSETS, "sounds", "combat", "stabNoArmor.wav"),
    os.path.join(ASSETS, "sounds", "stabNoArmor.wav"),
    os.path.join(BASE_DIR, "stabNoArmor.wav"),
]
# </POTBO_STAGE S0033>

# <POTBO_STAGE S0035>

# Common enemy sprite sheet yolları.
# İki sheet de tek dosyadan, çalışma anında chroma-key ile şeffaflaştırılır.
COMMON_ENEMY_KLASORU = os.path.join(ASSETS, "enemies", "common_enemy")

CRAWLER_SHEET_ADAYLARI = [
    os.path.join(COMMON_ENEMY_KLASORU, "crawler_spriteSheet.png"),
    os.path.join(ASSETS, "enemies", "crawler", "crawler_spriteSheet.png"),
    os.path.join(BASE_DIR, "crawler_spriteSheet(3).png"),
    os.path.join(BASE_DIR, "crawler_spriteSheet(1).png"),
    os.path.join(BASE_DIR, "crawler_spriteSheet.png"),
]

BERSERKER_SHEET_ADAYLARI = [
    os.path.join(COMMON_ENEMY_KLASORU, "berserker_spriteSheet.png"),
    os.path.join(
        ASSETS,
        "enemies",
        "berserker",
        "berserker_spriteSheet.png",
    ),
    os.path.join(BASE_DIR, "berserker_spriteSheet.png"),
]

# Tarkard common enemy değildir; özel dünya aktörüdür. Yine de ortak navigation /
# combat fiziğini kullandığı için asset yolu ayrı tutulur ve eski proje kökü de
# güvenli fallback olarak desteklenir.
TARKARD_KLASORU = os.path.join(ASSETS, "enemies", "special")
TARKARD_SHEET_ADAYLARI = [
    os.path.join(TARKARD_KLASORU, "tarkard_spriteSheet.png"),
    os.path.join(ASSETS, "enemies", "tarkard", "tarkard_spriteSheet.png"),
    os.path.join(BASE_DIR, "tarkard_spriteSheet.png"),
]

# Sir Torrmund da common enemy değildir. Özel isimli, tekil dünya aktörüdür.
# Asset adı iki yaygın yazımı destekler; böylece elle klasöre kopyalarken küçük
# bir dosya adı farkı oyunu sessizce spritesız bırakmaz.
TORRMUND_KLASORU = os.path.join(ASSETS, "enemies", "special")
TORRMUND_SHEET_ADAYLARI = [
    os.path.join(TORRMUND_KLASORU, "sirTorrmund_spriteSheet.png"),
    os.path.join(TORRMUND_KLASORU, "sir_torrmund_spriteSheet.png"),
    os.path.join(
        ASSETS,
        "enemies",
        "torrmund",
        "sirTorrmund_spriteSheet.png",
    ),
    os.path.join(BASE_DIR, "sirTorrmund_spriteSheet(1).png"),
    os.path.join(BASE_DIR, "sirTorrmund_spriteSheet.png"),
]
# </POTBO_STAGE S0035>

# <POTBO_STAGE S0037>

HEADSTHROWER_SHEET_ADAYLARI = [
    os.path.join(COMMON_ENEMY_KLASORU, "headsThrower_spriteSheet.png"),
    os.path.join(COMMON_ENEMY_KLASORU, "headsthrower_spriteSheet.png"),
    os.path.join(
        ASSETS,
        "enemies",
        "headsthrower",
        "headsThrower_spriteSheet.png",
    ),
    os.path.join(BASE_DIR, "headsThrower_spriteSheet.png"),
]
# </POTBO_STAGE S0037>

# <POTBO_STAGE S0140>
# Ağır darbe kontrol katmanı. Tarkard'ın vuruşu oyuncuyu yalnızca hasarlamaz;
# gerçek collision-aware knockback ve iki saniyelik bilinç kaybı uygular.
# Bu değişkenler global input kilidinden ayrıdır: pause her zaman erişilebilir kalır.
oyuncu_baygin_bitis = 0
# </POTBO_STAGE S0140>

# <POTBO_STAGE S0142>
# Sir Torrmund'un kesici infazı knockback üretmez; bunun yerine kısa, keskin bir
# ekran yarığı ve ölüm kilidi bırakır. Efekt state'i save'e yazılmaz.
oyuncu_kesik_efekti_bitis = 0
# </POTBO_STAGE S0142>

# <POTBO_STAGE S0144>
# =========================================================
# COMMON ENEMY DURUMU
# Crawler ve Berserker aynı fizik / aggro / saldırı omurgasını paylaşır.
# Yaklaşmak tek başına aggro üretmez: düşman yalnızca oyuncudan darbe
# aldıktan sonra saldırganlaşır.
# =========================================================
COMMON_ENEMY_TURLERI = ("crawler", "berserker", "headsthrower")
# </POTBO_STAGE S0144>

# <POTBO_STAGE S0146>
common_enemy_son_guncelleme = pygame.time.get_ticks()
common_enemy_onceki_oyuncu_konumu = None
common_enemy_oyuncu_hizi = pygame.Vector2(0.0, 0.0)
# Bu değer, yeni sistemin kayıt formatını gelecekte güvenle evrimleştirmek içindir.
COMMON_ENEMY_SAVE_VERSION = 9
# Tarkard semantik olarak common enemy değildir. common_enemies listesine hiçbir
# zaman girmez; save/load, interaction ve çizim katmanlarında özel aktör olarak yaşar.
tarkard_actor = None
tarkard_adi_ogrenildi = False
tarkard_konusuldu = False
# Sir Torrmund ikinci özel aktördür. Common enemy listesine girmez ve Tarkard ile
# aynı unique-id / save mantığını paylaşmaz.
torrmund_actor = None
torrmund_konusuldu = False
# geçici dünya aktörleri. Projectile ve fareler save'e yazılmaz; bir kayıt
# yüklenirken sıfırlanırlar. Böylece eski bir kayanın yeni kayda taşınması veya
# kamera dışında kalmış bir ambient farenin save'i şişirmesi mümkün olmaz.
enemy_projectiles = []
enemy_rock_impacts = []
ambient_rats = []
ambient_rat_next_spawn_ms = 0
AMBIENT_RAT_MAX = 3
# </POTBO_STAGE S0146>

# <POTBO_STAGE S0158>
oyuncu_olum_torrmund_senaryo = ""
# </POTBO_STAGE S0158>

# <POTBO_STAGE S0163>
# Ağır kesici sınıfı, özel tek-vuruş kontratı olmayan gelecek düşmanlarda bile
# sıradan kılıç hasarına düşmez. Torrmund kendi infaz fonksiyonuyla %100 lethal kalır.
AGIR_KESICI_MIN_MAX_HP_ORANI = 0.68
# </POTBO_STAGE S0163>

# <POTBO_STAGE S0204>
TARKARD_DINAMIK_KONUSMACI = "__TARKARD_DYNAMIC__"


def tarkard_adi():
    """Tarkard kendini açıklayana kadar konuşmacı adını gizler."""
    return TARKARD_DINAMIK_KONUSMACI
# </POTBO_STAGE S0204>

# <POTBO_STAGE S0206>


def konusmaci_gorunen_adi(konusmaci):
    if konusmaci == EADRIC_DINAMIK_KONUSMACI:
        if eadric_adi_ogrenildi:
            return "EADRIC"
        return bt("İSİMSİZ ADAM", "NAMELESS MAN")

    if konusmaci == TARKARD_DINAMIK_KONUSMACI:
        if tarkard_adi_ogrenildi:
            return "TARKARD"
        return bt("İSİMSİZ SAVAŞÇI", "NAMELESS WARRIOR")

    return str(konusmaci)
# </POTBO_STAGE S0206>

# <POTBO_STAGE S0208>


def karakter_lakabi():
    """Sir Torrmund diyaloğunda karakterin dünyadaki yerleşik lakabını döndürür."""
    if karakter_cinsiyet == "male":
        return bt("Kirli Şövalye", "the Tainted Knight")
    return bt("Adsız Kılıç", "the Nameless Blade")
# </POTBO_STAGE S0208>

# <POTBO_STAGE S0238>


def silah_temas_sesi_cal(hedef_turu):
    """Oyuncu kılıcı GERÇEKTEN hedefe değdiğinde materyal temas sample'ı çalar.

    Boş swing bu fonksiyona hiç ulaşmaz. Spell/ground-fire hasarları da çağırmaz.
    """
    if not pygame.mixer.get_init():
        return
    tur = str(hedef_turu or "").lower().strip()
    cfg = globals().get("COMMON_ENEMY_CONFIG", {}).get(tur, {})
    tam_zirhli = bool(cfg.get("fully_armored", tur == "torrmund"))
    if tam_zirhli:
        ses = stab_with_armor_sesi
        gain = 0.92
    elif tur in (
        "crawler",
        "berserker",
        "headsthrower",
        "tarkard",
    ):
        ses = stab_no_armor_sesi
        gain = 0.88
    else:
        return
    if ses is None:
        return
    ses.set_volume(max(0.0, min(1.0, _efekt_ses_orani() * gain)))
    ses.play()
# </POTBO_STAGE S0238>

# <POTBO_STAGE S0249>


def _sprite_sheet_karelerini_cikar(
    yol, arka_plan_rengi, rectler, ozel_transparan_rgblar=()
):
    """
    Sprite sheet'i bir kez yükler ve frame'leri gerçek alfa yüzeylerine keser.

    Önemli ayrım: yalnız ``set_colorkey`` kullanmıyoruz. Kaynak dosya hâlâ
    magenta RGB taşısa bile frame önce SRCALPHA canvas'a alınır, sonra frame'in
    kendi sol-üst referans fonu yakınsa ikinci kez temizlenir. Böylece özellikle
    Berserker'da #FF00FF fonun ölçekleme/convert zincirinde tekrar görünmesi
    engellenir. Pixel-art için smoothscale kullanılmaz.
    """
    sheet = resim_yukle(yol) if yol else None
    if sheet is None:
        return []

    sheet = sheet.copy().convert_alpha()
    # Opaque kaynaklar için hızlı ilk katman. Zaten alpha'lı PNG'lerde zararsızdır.
    sheet.set_colorkey(arka_plan_rengi, pygame.RLEACCEL)
    kareler = []

    ref_r, ref_g, ref_b = [int(v) for v in arka_plan_rengi]
    # Magenta kenarlarda renk sızıntısına karşı küçük tolerans; beyaz crawler'da
    # kaynak zaten alpha olduğundan yalnız gerçekten fon olan pikseller etkilenir.
    tolerans = 10 if arka_plan_rengi == (255, 0, 255) else 3

    for x, y, w, h in rectler:
        alan = pygame.Rect(int(x), int(y), int(w), int(h))
        alan = alan.clip(sheet.get_rect())
        if alan.width <= 0 or alan.height <= 0:
            continue

        ham = pygame.Surface(alan.size, pygame.SRCALPHA, 32).convert_alpha()
        ham.fill((0, 0, 0, 0))
        ham.blit(sheet, (0, 0), alan)

        # colorkey yalnız hız için ilk katmandır; gerçek güvence fiziksel
        # alpha temizliğidir. Önceki sürüm yalnız #FF00FF magentada bu döngüye
        # giriyordu. Sphaera'nın #990099 moru bu nedenle bazı Pygame/convert_alpha
        # zincirlerinde opaque kalabiliyordu. Rat/HeadsThrower'da da kaynak dosya
        # #00FF00 + #008080 iki fon taşıyor. Artık tüm chroma profilleri açıkça
        # alpha=0'a çevrilir. İşlem sadece asset yüklenirken bir kez çalışır.
        temiz_rgb = {tuple(int(c) for c in rgb) for rgb in ozel_transparan_rgblar}
        chroma_temizligi_gerekli = arka_plan_rengi in (
            (255, 0, 255),
            (153, 0, 153),
            (0, 255, 0),
            (0, 128, 128),
        ) or bool(temiz_rgb)
        if chroma_temizligi_gerekli:
            if arka_plan_rengi in (
                (255, 0, 255),
                (153, 0, 153),
            ):
                tolerans = 8
            elif arka_plan_rengi in (
                (0, 255, 0),
                (0, 128, 128),
            ):
                tolerans = 5
            else:
                tolerans = 3

            def _rgb_yakin(rgb, hedef, tol):
                return max(abs(int(rgb[i]) - int(hedef[i])) for i in range(3)) <= tol

            px = pygame.PixelArray(ham)
            try:
                for px_x in range(ham.get_width()):
                    for px_y in range(ham.get_height()):
                        renk = ham.get_at((px_x, px_y))
                        rgb = (renk.r, renk.g, renk.b)
                        ana_fon = _rgb_yakin(rgb, (ref_r, ref_g, ref_b), tolerans)

                        # Yeşil sprite sheet'ler iki ayrı background kullanır.
                        # Referans yalnız lime olsa bile teal dış canvas da sökülür.
                        yesil_teal_fon = False
                        if arka_plan_rengi in (
                            (0, 255, 0),
                            (0, 128, 128),
                        ):
                            yesil_teal_fon = (
                                _rgb_yakin(rgb, (0, 255, 0), 5)
                                or _rgb_yakin(rgb, (0, 248, 0), 5)
                                or _rgb_yakin(rgb, (0, 128, 128), 5)
                            )

                        ozel_fon = any(_rgb_yakin(rgb, hedef, 3) for hedef in temiz_rgb)
                        if renk.a <= 1 or ana_fon or yesil_teal_fon or ozel_fon:
                            px[px_x, px_y] = (0, 0, 0, 0)
            finally:
                del px

        sinir = ham.get_bounding_rect(min_alpha=1)
        if sinir.width <= 0 or sinir.height <= 0:
            continue
        kareler.append(ham.subsurface(sinir).copy())

    return kareler


def _tarkard_sprite_sheet_karelerini_cikar(yol, rectler):
    """
    Tarkard ve Sir Torrmund sheet'lerinde iki ayrı fon rengi vardır: dış canvas
    #008080 ve frame kutuları #00F800. İkisini de gerçek alpha=0 yapar. Yalnız colorkey kullanmak
    ölçekleme sırasında yeşil/teal halo üretebildiği için piksel alfa fiziksel olarak
    temizlenir. Kaynak zaten temiz PNG ise işlem idempotenttir.
    """
    sheet = resim_yukle(yol) if yol else None
    if sheet is None:
        return []
    sheet = sheet.copy().convert_alpha()
    kareler = []
    fonlar = ((0, 128, 128), (0, 248, 0))

    for x, y, w, h in rectler:
        alan = pygame.Rect(int(x), int(y), int(w), int(h)).clip(sheet.get_rect())
        if alan.width <= 0 or alan.height <= 0:
            continue
        ham = pygame.Surface(alan.size, pygame.SRCALPHA, 32).convert_alpha()
        ham.fill((0, 0, 0, 0))
        ham.blit(sheet, (0, 0), alan)
        px = pygame.PixelArray(ham)
        try:
            for px_x in range(ham.get_width()):
                for px_y in range(ham.get_height()):
                    renk = ham.get_at((px_x, px_y))
                    if renk.a <= 1:
                        px[px_x, px_y] = (0, 0, 0, 0)
                        continue
                    rgb = (renk.r, renk.g, renk.b)
                    if any(
                        max(abs(rgb[i] - fon[i]) for i in range(3)) <= 2
                        for fon in fonlar
                    ):
                        px[px_x, px_y] = (0, 0, 0, 0)
        finally:
            del px

        sinir = ham.get_bounding_rect(min_alpha=1)
        if sinir.width > 0 and sinir.height > 0:
            kareler.append(ham.subsurface(sinir).copy())
    return kareler
# </POTBO_STAGE S0249>

# <POTBO_STAGE S0254>


# Crawler sheet'i düzenli grid değildir; görseldeki gerçek sprite sınırları.
CRAWLER_FRAME_RECTLERI = [
    (5, 2, 29, 45),
    (45, 2, 29, 45),
    (82, 2, 27, 45),
    (115, 2, 28, 45),
    (150, 2, 29, 45),
    (186, 2, 29, 45),
    (219, 2, 35, 45),
    (258, 2, 39, 45),
    (302, 2, 37, 45),
    (3, 53, 37, 62),
    (48, 53, 29, 62),
    (89, 53, 29, 62),
    (125, 53, 78, 62),
    (212, 53, 67, 62),
    (289, 53, 61, 62),
    (2, 133, 57, 38),
    (72, 133, 50, 38),
    (133, 133, 36, 38),
    (176, 133, 32, 38),
    (222, 133, 27, 38),
]

# Berserker, klasik 3-frame locomotion + 4-frame attack satır düzeni taşır.
BERSERKER_FRAME_RECTLERI = [
    (12, 10, 52, 79),
    (92, 10, 59, 79),
    (172, 10, 58, 79),
    (5, 105, 56, 80),
    (85, 105, 59, 80),
    (165, 105, 60, 80),
    (16, 202, 52, 79),
    (89, 202, 59, 79),
    (170, 202, 58, 79),
    (19, 297, 56, 80),
    (96, 297, 59, 80),
    (175, 297, 60, 80),
    (20, 388, 59, 81),
    (158, 388, 74, 81),
    (280, 388, 79, 81),
    (398, 388, 74, 81),
    (17, 484, 59, 81),
    (145, 484, 76, 81),
    (281, 484, 78, 81),
    (383, 484, 61, 81),
    (41, 580, 59, 81),
    (128, 580, 74, 81),
    (241, 580, 79, 81),
    (368, 580, 74, 81),
    (44, 676, 59, 81),
    (139, 676, 76, 81),
    (241, 676, 78, 81),
    (396, 676, 61, 81),
]

# Tarkard sheet düzenli grid değildir. Rect'ler gönderilen 1144x696 kaynaktaki
# gerçek frame adalarını takip eder. Son beş kare palette varyantlarıdır ve ana
# Tarkard animasyonunda kullanılmaz; ileride kabile varyantları için korunur.
TARKARD_FRAME_RECTLERI = [
    (2, 2, 88, 88),
    (92, 10, 88, 80),
    (182, 10, 80, 80),
    (2, 94, 88, 88),
    (92, 94, 88, 88),
    (182, 94, 88, 88),
    (272, 94, 88, 88),
    (362, 94, 88, 88),
    (452, 94, 88, 88),
    (2, 186, 80, 80),
    (84, 186, 88, 80),
    (174, 186, 80, 80),
    (256, 186, 112, 80),
    (370, 186, 112, 80),
    (802, 270, 104, 120),
    (908, 270, 104, 120),
    (590, 278, 104, 112),
    (696, 278, 104, 112),
    (166, 286, 104, 104),
    (272, 286, 104, 104),
    (378, 286, 104, 104),
    (484, 286, 104, 104),
    (2, 310, 80, 80),
    (84, 310, 80, 80),
    (2, 394, 96, 88),
    (2, 486, 80, 40),
    (2, 530, 88, 72),
    (2, 606, 88, 88),
    (92, 606, 88, 88),
    (182, 606, 88, 88),
    (272, 606, 88, 88),
    (362, 606, 88, 88),
]

# Sir Torrmund sheet'inin gerçek non-teal frame adaları. Son dört kare palette
# varyantıdır; ana karakter animasyonuna dahil edilmez. Rect'ler yalnız kaynak
# 894x669 sheet'e aittir ve transparan temizleme öncesi koordinatlardır.
TORRMUND_FRAME_RECTLERI = [
    (2, 2, 112, 88),
    (116, 2, 112, 88),
    (230, 2, 112, 88),
    (2, 94, 112, 88),
    (116, 94, 112, 88),
    (230, 94, 112, 88),
    (344, 94, 112, 88),
    (2, 186, 96, 72),
    (100, 187, 96, 80),
    (198, 187, 168, 72),
    (368, 189, 144, 72),
    (514, 189, 144, 72),
    (660, 190, 136, 64),
    (198, 271, 184, 128),
    (100, 272, 96, 112),
    (2, 277, 96, 112),
    (384, 316, 176, 80),
    (562, 316, 168, 80),
    (732, 316, 160, 80),
    (2, 403, 104, 88),
    (2, 495, 104, 80),
    (2, 579, 112, 88),
    (116, 579, 112, 88),
    (230, 579, 112, 88),
    (344, 579, 112, 88),
]
# </POTBO_STAGE S0254>

# <POTBO_STAGE S0257>

# Heads Thrower kaynak sheet'inde sequence'ler farklı hücre genişliğine sahiptir.
# İlk pickup karelerinde label ile çakışmamak için yalnız o hücrelerin üstü daraltılır.
HEADSTHROWER_IDLE_RECTLERI = [(_i * 28, 189, 28, 44) for _i in range(18)]
HEADSTHROWER_PICKUP_RECTLERI = [
    (_i * 72, 258 if _i < 4 else 246, 72, 72 if _i < 4 else 84) for _i in range(19)
]
HEADSTHROWER_THROW_RECTLERI = [(_i * 59, 342, 59, 84) for _i in range(13)]
# Pickup'ın taş baş üstündeyken net olduğu bir kareden yalnız kaya adası kesilir.
HEADSTHROWER_ROCK_RECTLERI = [(1014, 246, 46, 38)]

crawler_sheet_yolu = mevcut_ilk_dosya(CRAWLER_SHEET_ADAYLARI)
berserker_sheet_yolu = mevcut_ilk_dosya(BERSERKER_SHEET_ADAYLARI)
tarkard_sheet_yolu = mevcut_ilk_dosya(TARKARD_SHEET_ADAYLARI)
torrmund_sheet_yolu = mevcut_ilk_dosya(TORRMUND_SHEET_ADAYLARI)
# </POTBO_STAGE S0257>

# <POTBO_STAGE S0259>
headsthrower_sheet_yolu = mevcut_ilk_dosya(HEADSTHROWER_SHEET_ADAYLARI)

_crawler_tum_kareler = _sprite_sheet_karelerini_cikar(
    crawler_sheet_yolu, (255, 255, 255), CRAWLER_FRAME_RECTLERI
)

_berserker_tum_kareler = _sprite_sheet_karelerini_cikar(
    berserker_sheet_yolu,
    (255, 0, 255),
    BERSERKER_FRAME_RECTLERI,
    ozel_transparan_rgblar=((31, 31, 31),),
)

_tarkard_tum_kareler = _tarkard_sprite_sheet_karelerini_cikar(
    tarkard_sheet_yolu, TARKARD_FRAME_RECTLERI
)

_torrmund_tum_kareler = _tarkard_sprite_sheet_karelerini_cikar(
    torrmund_sheet_yolu, TORRMUND_FRAME_RECTLERI
)
# </POTBO_STAGE S0259>

# <POTBO_STAGE S0261>

_head_idle_raw = _sprite_sheet_karelerini_cikar(
    headsthrower_sheet_yolu,
    (0, 255, 0),
    HEADSTHROWER_IDLE_RECTLERI,
    ozel_transparan_rgblar=((0, 128, 128),),
)
_head_pickup_raw = _sprite_sheet_karelerini_cikar(
    headsthrower_sheet_yolu,
    (0, 255, 0),
    HEADSTHROWER_PICKUP_RECTLERI,
    ozel_transparan_rgblar=((0, 128, 128),),
)
_head_throw_raw = _sprite_sheet_karelerini_cikar(
    headsthrower_sheet_yolu,
    (0, 255, 0),
    HEADSTHROWER_THROW_RECTLERI,
    ozel_transparan_rgblar=((0, 128, 128),),
)
_head_rock_raw = _sprite_sheet_karelerini_cikar(
    headsthrower_sheet_yolu,
    (0, 255, 0),
    HEADSTHROWER_ROCK_RECTLERI,
    ozel_transparan_rgblar=((0, 128, 128),),
)
# </POTBO_STAGE S0261>

# <POTBO_STAGE S0264>

_frame_listesi_dogrula(_head_pickup_canvas, 19, "HeadsThrower pickup")
_frame_listesi_dogrula(_head_throw_canvas, 13, "HeadsThrower throw")
_frame_listesi_dogrula(
    _head_locomotion_canvas,
    2,
    "HeadsThrower full-body locomotion",
)

HEADSTHROWER_SPRITELERI = {
    "idle": _head_locomotion_canvas[:1],
    "walk": _head_locomotion_canvas,
    "pickup": _head_pickup_canvas,
    "throw": _head_throw_canvas,
}
HEADSTHROWER_ROCK_SPRITE = _head_rock_raw[0] if _head_rock_raw else None
# </POTBO_STAGE S0264>

# <POTBO_STAGE S0270>


# Crawler'ın kaynak sheet'inde bazı karelerin ayak tabanında ayrı bir koyu yatay
# gölge bulunur. Dünya gölgesi zaten kodla çizildiği için bu ikinci katmanı yalnız
# frame'in en alt bandında, yatay ve gövdeden izole koyu gri pikseller üzerinden
# temizleriz. Gövde konturu renkli/parlak komşuluğa sahipse korunur.
def _crawler_gomme_golge_temizle(kare):
    if kare is None:
        return kare
    src = kare.copy().convert_alpha()
    bbox = src.get_bounding_rect(min_alpha=1)
    if bbox.height <= 0:
        return src
    alt = bbox.bottom - 1
    y0 = max(bbox.top, alt - 10)
    sil = []
    for y in range(y0, alt + 1):
        aday_x = []
        for x in range(bbox.left, bbox.right):
            c = src.get_at((x, y))
            if c.a <= 0:
                continue
            sat = max(c.r, c.g, c.b) - min(c.r, c.g, c.b)
            lum = (c.r + c.g + c.b) / 3.0
            if sat <= 4 and 24 <= lum <= 92:
                aday_x.append(x)
        aday_set = set(aday_x)
        for x in aday_x:
            yatay = sum(
                1
                for xx in range(
                    max(bbox.left, x - 4),
                    min(bbox.right, x + 5),
                )
                if xx in aday_set
            )
            if yatay < 3:
                continue
            govde_yakini = False
            for yy in range(max(bbox.top, y - 3), min(bbox.bottom, y + 2)):
                for xx in range(
                    max(bbox.left, x - 2),
                    min(bbox.right, x + 3),
                ):
                    n = src.get_at((xx, yy))
                    if n.a <= 0:
                        continue
                    nsat = max(n.r, n.g, n.b) - min(n.r, n.g, n.b)
                    nlum = (n.r + n.g + n.b) / 3.0
                    if nsat > 12 or nlum > 112:
                        govde_yakini = True
                        break
                if govde_yakini:
                    break
            if not govde_yakini:
                sil.append((x, y))
    for pos in sil:
        src.set_at(pos, (0, 0, 0, 0))
    return src


_crawler_tum_kareler = [_crawler_gomme_golge_temizle(k) for k in _crawler_tum_kareler]

# Crawler sheet tek bir uzun hareket dizisi gibi görünse de locomotion ile
# saldırı aynı kare havuzundan seçilirse yaratık yürürken vuruyormuş hissi verir.
# Alt satır (15..19) düşük profilli sürünme/locomotion; üst+orta bölüm (0..14)
# ise dönüşüm/vuruş zinciridir. Bu iki durum artık kesinlikle karışmaz.
_crawler_idle = _kareleri_ortak_canvas_yap(
    [_crawler_tum_kareler[i] for i in (19,) if i < len(_crawler_tum_kareler)]
)
_crawler_walk = _kareleri_ortak_canvas_yap(
    [
        _crawler_tum_kareler[i]
        for i in (15, 16, 17, 18, 17, 16)
        if i < len(_crawler_tum_kareler)
    ]
)
_crawler_attack = _kareleri_ortak_canvas_yap(
    [_crawler_tum_kareler[i] for i in range(0, min(15, len(_crawler_tum_kareler)))]
)

# Berserker sheet'in ilk dört locomotion satırı cardinal değil, diyagonal bakış
# yönleridir: ön-sağ, arka-sağ, ön-sol, arka-sol. Eski down/left/right/up eşlemesi
# bu yüzden özellikle sağ/sol takipte yaratığı geri geri yürütüyordu.
BERSERKER_GORSEL_YON_SIRASI = (
    "down_right",
    "up_right",
    "down_left",
    "up_left",
)
_bers_walk_duz = _kareleri_ortak_canvas_yap(_berserker_tum_kareler[:12])
_bers_attack_duz = _kareleri_ortak_canvas_yap(_berserker_tum_kareler[12:28])
# </POTBO_STAGE S0270>

# <POTBO_STAGE S0273>
for _yon_index, _yon in enumerate(BERSERKER_GORSEL_YON_SIRASI):
    _bas = _yon_index * 3
    _satir = _bers_walk_duz[_bas : _bas + 3]
    _bers_walk[_yon] = _satir
    _bers_idle[_yon] = [_satir[1]] if len(_satir) >= 2 else _satir

    _atak_bas = _yon_index * 4
    _bers_attack[_yon] = _bers_attack_duz[_atak_bas : _atak_bas + 4]

COMMON_ENEMY_SPRITELERI = {
    "crawler": {
        "idle": _crawler_idle,
        "walk": _crawler_walk or _crawler_idle,
        "attack": _crawler_attack or _crawler_walk or _crawler_idle,
    },
    "berserker": {
        "idle": _bers_idle,
        "walk": _bers_walk,
        "attack": _bers_attack,
    },
}

# Tarkard'ın ana palette animasyonları. 0..8 ağır locomotion, 9..13 yumruk/
# gauntlet smash, 14..21 geniş dairesel darbe, 22..23 kısa hazırlık/guard,
# 25 düşüş, 26 diz çökme/stagger olarak ayrılır.
_tarkard_idle = _kareleri_ortak_canvas_yap(
    [_tarkard_tum_kareler[i] for i in (0, 1, 0, 2) if i < len(_tarkard_tum_kareler)],
    padding=4,
)
_tarkard_walk = _kareleri_ortak_canvas_yap(
    [
        _tarkard_tum_kareler[i]
        for i in (0, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3)
        if i < len(_tarkard_tum_kareler)
    ],
    padding=4,
)
_tarkard_heavy = _kareleri_ortak_canvas_yap(
    [_tarkard_tum_kareler[i] for i in range(9, min(14, len(_tarkard_tum_kareler)))],
    padding=5,
)
_tarkard_whirl = _kareleri_ortak_canvas_yap(
    [_tarkard_tum_kareler[i] for i in range(14, min(22, len(_tarkard_tum_kareler)))],
    padding=5,
)
_tarkard_guard = _kareleri_ortak_canvas_yap(
    [_tarkard_tum_kareler[i] for i in (22, 23) if i < len(_tarkard_tum_kareler)],
    padding=4,
)
_tarkard_stagger = _kareleri_ortak_canvas_yap(
    [_tarkard_tum_kareler[i] for i in (26, 24) if i < len(_tarkard_tum_kareler)],
    padding=4,
)
TARKARD_SPRITELERI = {
    "idle": _tarkard_idle,
    "walk": _tarkard_walk or _tarkard_idle,
    "heavy": _tarkard_heavy or _tarkard_guard or _tarkard_idle,
    "whirl": _tarkard_whirl or _tarkard_heavy or _tarkard_idle,
    "stagger": _tarkard_stagger or _tarkard_idle,
}

# Sir Torrmund: 0..2 ağır idle, 3..6 kontrollü yürüyüş, 7..12 yatay infaz
# zinciri, 13..18 dikey/alt cleave zinciri, 19..20 kısa guard/recovery.
_torrmund_idle = _kareleri_ortak_canvas_yap(
    [_torrmund_tum_kareler[i] for i in (0, 1, 0, 2) if i < len(_torrmund_tum_kareler)],
    padding=5,
)
_torrmund_walk = _kareleri_ortak_canvas_yap(
    [
        _torrmund_tum_kareler[i]
        for i in (3, 4, 5, 6, 5, 4)
        if i < len(_torrmund_tum_kareler)
    ],
    padding=5,
)
_torrmund_execution = _kareleri_ortak_canvas_yap(
    [_torrmund_tum_kareler[i] for i in range(7, min(13, len(_torrmund_tum_kareler)))],
    padding=6,
)
_torrmund_cleave = _kareleri_ortak_canvas_yap(
    [
        _torrmund_tum_kareler[i]
        for i in (14, 15, 13, 16, 17, 18)
        if i < len(_torrmund_tum_kareler)
    ],
    padding=6,
)
_torrmund_guard = _kareleri_ortak_canvas_yap(
    [_torrmund_tum_kareler[i] for i in (19, 20) if i < len(_torrmund_tum_kareler)],
    padding=5,
)
TORRMUND_SPRITELERI = {
    "idle": _torrmund_idle,
    "walk": _torrmund_walk or _torrmund_idle,
    "execution": _torrmund_execution or _torrmund_guard or _torrmund_idle,
    "cleave": _torrmund_cleave or _torrmund_execution or _torrmund_idle,
    "stagger": _torrmund_guard or _torrmund_idle,
}
# </POTBO_STAGE S0273>

# <POTBO_STAGE S0374>


def common_enemy_carpisma_rect(dusman, x=None, y=None):
    """Common enemy için yalnızca yere basan dar fiziksel gövdeyi döndürür."""
    if x is None:
        x = dusman.x
    if y is None:
        y = dusman.y
    yari_genislik = int(dusman.cfg["body_half_width"])
    yukseklik = int(dusman.cfg["body_height"])
    return pygame.Rect(
        int(round(x)) - yari_genislik,
        int(round(y)) - yukseklik,
        yari_genislik * 2,
        yukseklik,
    )
# </POTBO_STAGE S0374>

# <POTBO_STAGE S0398>


def tarkard_konusma_akisi():
    """Tarkard pasifken konuşulur; adını öfkeyle haykırdığı dallar savaşla biter."""
    t = tarkard_adi()
    if tarkard_konusuldu:
        if karakter_cinsiyet == "male":
            return [
                satir(
                    t,
                    bt(
                        "Hâlâ önümde dikilirsin. Ya yoluna var, ya da kılıcını çek.",
                        "You still stand before me. Take your road, or draw your blade.",
                    ),
                )
            ]
        return [
            satir(
                t,
                bt(
                    "Geçeceksen geç, güneyli. Yoksa meydan burada.",
                    "Pass if you mean to pass, southerner. Otherwise, the ground is here.",
                ),
            )
        ]

    if karakter_cinsiyet == "male":
        return [
            satir(
                t,
                bt(
                    "Sen de kim oluyorsun, küçük bok? Bu patikada ne ararsın?",
                    "And who are you, little shit? What business have you on this road?",
                ),
            ),
            satir(
                t,
                bt(
                    "Bana karşı mı dikilirsin, sikik?",
                    "Do you mean to stand against me, fucker?",
                ),
            ),
            secim(
                [
                    (
                        bt(
                            "Senin gibi götün teki, benim ağzıma kürdandır.",
                            "An arse like you is no more than a toothpick to me.",
                        ),
                        [
                            aksiyon("tarkard_adini_ogren"),
                            satir(
                                t,
                                bt(
                                    "SENİ OROSPU ÇOCUĞU! BEN TARKARD! KODRAKİ'NİN GÜLLESİ, "
                                    "SÜRTÜKLERİN EFENDİSİYİM! BU YAŞIMA DEK YALNIZ BİR KEZ "
                                    "YENİLDİM. ŞİMDİ AĞZINA SIÇACAĞIM SENİN!",
                                    "YOU SON OF A BITCH! I AM TARKARD! THE CANNONBALL OF KODRAKI, "
                                    "LORD OF WENCHES! IN ALL MY YEARS I HAVE BEEN BEATEN ONLY ONCE. "
                                    "NOW I'LL SHIT IN YOUR MOUTH!",
                                ),
                            ),
                            aksiyon("tarkard_savas_baslat"),
                        ],
                    ),
                    (
                        bt(
                            "Yalnız yolumdan geçiyorum.",
                            "I am only passing through.",
                        ),
                        [
                            satir(
                                t,
                                bt(
                                    "Demek benimle kapışmaya götün yemedi? Kılıcı götünde taşıyan "
                                    "senin gibilere diyeceğim yok. Yolun açık; geç.",
                                    "So you haven't the balls to face me? I've no quarrel with men "
                                    "who carry their swords up their arses. The road is open; pass.",
                                ),
                            ),
                            aksiyon("tarkard_konusma_tamam"),
                        ],
                    ),
                    (
                        bt("Hayır, efendim.", "No, sir."),
                        [
                            satir(
                                t,
                                bt(
                                    "Orospum musun da bana efendim dersin? Kıllı götlerle işim olmaz. Geç.",
                                    "Are you my whore, calling me sir? I've no use for hairy arses. Pass.",
                                ),
                            ),
                            aksiyon("tarkard_konusma_tamam"),
                        ],
                    ),
                ]
            ),
        ]

    return [
        satir(
            t,
            bt(
                "Yoksa kendini bana teslim etmeye mi geldin, güneyli güzellik?",
                "Have you come to surrender yourself to me, southern beauty?",
            ),
        ),
        secim(
            [
                (
                    bt(
                        "Yıkıl karşımdan, götlek.",
                        "Get out of my way, coward.",
                    ),
                    [
                        aksiyon("tarkard_adini_ogren"),
                        satir(
                            t,
                            bt(
                                "SENİ OROSPU ÇOCUĞU! BEN TARKARD! KODRAKİ'NİN GÜLLESİ, "
                                "SÜRTÜKLERİN EFENDİSİYİM! BU YAŞIMA DEK YALNIZ BİR KEZ "
                                "YENİLDİM. ŞİMDİ AĞZINA SIÇACAĞIM SENİN!",
                                "YOU SON OF A BITCH! I AM TARKARD! THE CANNONBALL OF KODRAKI, "
                                "LORD OF WENCHES! IN ALL MY YEARS I HAVE BEEN BEATEN ONLY ONCE. "
                                "NOW I'LL SHIT IN YOUR MOUTH!",
                            ),
                        ),
                        aksiyon("tarkard_savas_baslat"),
                    ],
                ),
                (
                    bt(
                        "Güneyli olduğumu nereden anladın?",
                        "How did you know I am southern?",
                    ),
                    [
                        satir(
                            t,
                            bt(
                                "Güneyli güzelliğini nerede görsem tanırım. Tatları da pek güzel olur.",
                                "I know southern beauty wherever I see it. They taste fine as well.",
                            ),
                        ),
                        aksiyon("tarkard_konusma_tamam"),
                    ],
                ),
                (
                    bt(
                        "Yalnız geçiyorum.",
                        "I am only passing through.",
                    ),
                    [
                        satir(
                            t,
                            bt(
                                "Çadırıma davetlisin. Peor Gölü'ne yakındır. Şimdilik geçebilirsin.",
                                "You are invited to my tent. It stands near Lake Peor. For now, you may pass.",
                            ),
                        ),
                        aksiyon("tarkard_konusma_tamam"),
                    ],
                ),
            ]
        ),
    ]
# </POTBO_STAGE S0398>

# <POTBO_STAGE S0400>


def tarkard_yakin_mi():
    if tarkard_actor is None or not getattr(tarkard_actor, "active", False):
        return False
    if getattr(tarkard_actor, "aggro", False):
        return False
    return abs(oyuncu_x - tarkard_actor.x) < 86 and abs(oyuncu_y - tarkard_actor.y) < 68


def tarkard_konusmasini_baslat():
    if not tarkard_yakin_mi():
        return False
    return diyalog_baslat(tarkard_konusma_akisi())


def torrmund_yakin_mi():
    if torrmund_actor is None or not getattr(torrmund_actor, "active", False):
        return False
    if getattr(torrmund_actor, "aggro", False):
        return False
    return (
        abs(oyuncu_x - torrmund_actor.x) < 92 and abs(oyuncu_y - torrmund_actor.y) < 72
    )


def torrmund_konusmasini_baslat():
    if not torrmund_yakin_mi():
        return False
    return diyalog_baslat(torrmund_konusma_akisi())
# </POTBO_STAGE S0400>

# <POTBO_STAGE S0411>


def _v24_olum_katil_adayi_bul(kaynak_x, kaynak_y, kaynak_adi=""):
    """Lethal kaynağı gerçek dünya aktörüne bağlar.

    Önce isim/tür eşleşmesi, sonra kaynak koordinatına Öklid uzaklığı kullanılır.
    Projectile adları (ör. headsthrower_rock) sahibinin türüne indirgenir.
    """
    try:
        aktorler = [a for a in combat_enemy_aktorleri() if getattr(a, "active", False)]
    except Exception:
        return None
    if not aktorler:
        return None

    ad = str(kaynak_adi or "").strip().lower()
    tur_ipucu = ""
    if "torrmund" in ad:
        tur_ipucu = "torrmund"
    elif "tarkard" in ad:
        tur_ipucu = "tarkard"
    elif "headsthrower" in ad or "heads thrower" in ad:
        tur_ipucu = "headsthrower"
    elif "berserker" in ad:
        tur_ipucu = "berserker"
    elif "crawler" in ad:
        tur_ipucu = "crawler"

    k = pygame.Vector2(float(kaynak_x), float(kaynak_y))
    en_iyi = None
    en_iyi_skor = float("inf")
    for a in aktorler:
        a_ad = str(getattr(a, "name", "")).strip().lower()
        a_tur = str(getattr(a, "tur", "")).strip().lower()
        isim_eslesme = bool(ad) and (a_ad == ad or a_ad in ad or ad in a_ad)
        tur_eslesme = bool(tur_ipucu) and a_tur == tur_ipucu
        # İsim/tür eşleşmesi 10.000 puanlık öncelik alır; aynı türden birden fazla
        # aktör varsa gerçek darbeye en yakın olan seçilir.
        mesafe = pygame.Vector2(
            float(getattr(a, "x", 0.0)),
            float(getattr(a, "y", 0.0)),
        ).distance_to(k)
        ceza = 0.0 if isim_eslesme else (180.0 if tur_eslesme else 10000.0)
        skor = ceza + mesafe
        if skor < en_iyi_skor:
            en_iyi_skor = skor
            en_iyi = a

    # İsim/tür hiç uyuşmadıysa uzaktaki rastgele bir karakteri "katil" ilan etme.
    if en_iyi_skor >= 10000.0:
        return None
    return en_iyi


def _v24_olum_katil_actor_bul():
    uid = str(oyuncu_olum_katil_uid or "")
    tur = str(oyuncu_olum_katil_tur or "")
    try:
        aktorler = combat_enemy_aktorleri()
    except Exception:
        return None
    if uid:
        for a in aktorler:
            if str(getattr(a, "uid", "")) == uid:
                return a
    if tur:
        for a in aktorler:
            if str(getattr(a, "tur", "")) == tur:
                return a
    return None


def _stage1__v30_olum_koreografi_hazirla(katil_tur, profil, kaynak_adi=""):
    """Katil tipine göre ölüm sahnesinin 0-4 s koreografisini tek kez seçer."""
    global oyuncu_olum_alt_turu, oyuncu_olum_koreografi_seed
    global oyuncu_olum_torrmund_senaryo, oyuncu_olum_ikiye_bolundu
    global oyuncu_olum_kesim_acisi, oyuncu_olum_kesim_ofset_orani

    tur = str(katil_tur or "").lower()
    oyuncu_olum_koreografi_seed = random.randint(1, 2_000_000)
    oyuncu_olum_torrmund_senaryo = ""

    if tur == "crawler":
        oyuncu_olum_alt_turu = "crawler"
        oyuncu_olum_ikiye_bolundu = False
    elif tur == "berserker":
        oyuncu_olum_alt_turu = "berserker"
        oyuncu_olum_ikiye_bolundu = False
    elif tur == "headsthrower":
        oyuncu_olum_alt_turu = "headshot"
        oyuncu_olum_ikiye_bolundu = False
    elif tur == "tarkard":
        oyuncu_olum_alt_turu = "tarkard_crush"
        oyuncu_olum_ikiye_bolundu = False
    elif tur == "torrmund":
        rng = random.Random(oyuncu_olum_koreografi_seed)
        if rng.random() < 0.54:
            oyuncu_olum_torrmund_senaryo = "bisect"
            oyuncu_olum_alt_turu = "torrmund_bisect"
            oyuncu_olum_ikiye_bolundu = True
        else:
            ikinci = rng.random() < 0.46
            oyuncu_olum_torrmund_senaryo = "decap_cleave" if ikinci else "decap"
            oyuncu_olum_alt_turu = (
                "torrmund_decap_cleave" if ikinci else "torrmund_decap"
            )
            oyuncu_olum_ikiye_bolundu = False
        oyuncu_olum_kesim_acisi = random.uniform(14.0, 32.0) * random.choice(
            (-1.0, 1.0)
        )
        oyuncu_olum_kesim_ofset_orani = random.uniform(0.48, 0.57)
    else:
        oyuncu_olum_alt_turu = ""
# </POTBO_STAGE S0411>

# <POTBO_STAGE S0418>


def _stage1__v30_katil_koreografi_frame(actor, simdi):
    if actor is None or oyuncu_olum_baslangic_ms <= 0:
        return None
    tur = str(getattr(actor, "tur", ""))
    alt = str(oyuncu_olum_alt_turu or "")
    e = max(0, int(simdi) - int(oyuncu_olum_baslangic_ms))
    try:
        if tur == "crawler" and alt == "crawler" and 430 <= e < 1500:
            frames = COMMON_ENEMY_SPRITELERI.get("crawler", {}).get("attack", [])
            if frames:
                cycle = 178
                local = (e - 430) % cycle
                return frames[
                    min(
                        len(frames) - 1,
                        int(local / max(1, cycle / len(frames))),
                    )
                ]
        if tur == "berserker" and alt == "berserker" and 430 <= e < 1580:
            frames = (
                COMMON_ENEMY_SPRITELERI.get("berserker", {})
                .get("attack", {})
                .get(
                    str(getattr(actor, "visual_direction", "right")),
                    [],
                )
            )
            if frames:
                cycle = 192
                local = (e - 430) % cycle
                return frames[
                    min(
                        len(frames) - 1,
                        int(local / max(1, cycle / len(frames))),
                    )
                ]
        if tur == "tarkard" and alt == "tarkard_crush" and 430 <= e < 1240:
            frames = TARKARD_SPRITELERI.get("whirl", [])
            if frames:
                q = e - 430
                return frames[
                    min(
                        len(frames) - 1,
                        int(q / max(1, 760 / len(frames))),
                    )
                ]
        if tur == "torrmund" and alt.startswith("torrmund_"):
            if alt == "torrmund_decap_cleave" and 1180 <= e < 2050:
                frames = TORRMUND_SPRITELERI.get("cleave", [])
                if frames:
                    q = e - 1180
                    return frames[
                        min(
                            len(frames) - 1,
                            int(q / max(1, 760 / len(frames))),
                        )
                    ]
            if e < 930:
                frames = TORRMUND_SPRITELERI.get("execution", [])
                if frames:
                    return frames[
                        min(
                            len(frames) - 1,
                            int(e / max(1, 840 / len(frames))),
                        )
                    ]
    except Exception:
        return None
    return None
# </POTBO_STAGE S0418>

# <POTBO_STAGE S0423>


COMMON_ENEMY_CONFIG = {
    "crawler": {
        "name_tr": "Sürünen",
        "name_en": "Crawler",
        "level": 2,
        "max_hp": 115,
        "move_speed": 146.0,
        "acceleration": 790.0,
        "steering_lambda": 11.8,
        "arrival_sigma": 58.0,
        "stop_radius": 43.0,
        "attack_range": 62.0,
        "attack_contact_gap": 18.0,
        "attack_start_contact_gap": 25.0,
        "attack_damage": 10,
        "attack_cooldown_ms": 1080,
        "attack_frame_ms": 76,
        "attack_impact_frame": 12,
        "attack_recovery_ms": 205,
        "walk_frame_ms": 102,
        "idle_frame_ms": 235,
        "body_half_width": 18,
        "body_height": 20,
        "nav_margin": 3,
        "attack_half_width": 42,
        "attack_half_height": 28,
        "sprite_scale": 1.44,
        "separation_radius": 60.0,
        "separation_strength": 112.0,
        "prediction_max": 0.07,
        "hit_stun_ms": 145,
        "path_replan_ms": 520,
        "path_lookahead": 78.0,
        "clearance_weight": 0.21,
        "turn_weight": 0.075,
        "evade_chance": 0.72,
        "evade_cooldown_ms": 690,
        "evade_ms": 340,
        "evade_speed": 214.0,
        "evade_distance": 58.0,
        "evade_ring_min": 74.0,
        "evade_ring_max": 118.0,
        "poise_max": 42.0,
        "poise_regen_per_sec": 18.0,
        "poise_damage_scale": 1.35,
        "stagger_ms": 390,
        "spawn_min_player_distance": 300.0,
        "preferred_spawns": [
            (1215.0, 570.0),
            (1110.0, 555.0),
            (690.0, 555.0),
        ],
    },
    "berserker": {
        "name_tr": "Çılgın Savaşçı",
        "name_en": "Berserker",
        "level": 8,
        "max_hp": 435,
        # Oyuncu temel yürüyüşü yaklaşık 240 px/s civarında. Berserker artık
        # gerçekten "hızlı" hissedilecek ama telegraph okunabilir kalacak düzeyde.
        "move_speed": 248.0,
        "acceleration": 1180.0,
        "steering_lambda": 13.2,
        "arrival_sigma": 72.0,
        "stop_radius": 50.0,
        "attack_range": 76.0,
        "attack_contact_gap": 25.0,
        "attack_start_contact_gap": 34.0,
        "attack_damage": 28,
        "attack_cooldown_ms": 835,
        "attack_frame_ms": 90,
        "attack_impact_frame": 2,
        "attack_recovery_ms": 285,
        "walk_frame_ms": 62,
        "idle_frame_ms": 205,
        "body_half_width": 22,
        "body_height": 24,
        "nav_margin": 5,
        "attack_half_width": 51,
        "attack_half_height": 38,
        "sprite_scale": 0.96,
        "separation_radius": 82.0,
        "separation_strength": 178.0,
        "prediction_max": 0.30,
        "hit_stun_ms": 80,
        "path_replan_ms": 430,
        "path_lookahead": 124.0,
        "clearance_weight": 0.31,
        "turn_weight": 0.052,
        "combat_radius": 80.0,
        "combat_strafe_strength": 0.14,
        "flank_refresh_ms": 470,
        "backdash_chance": 0.12,
        "backdash_cooldown_ms": 3200,
        "backdash_speed": 590.0,
        "backdash_ms": 170,
        "chase_dash_speed": 610.0,
        "chase_dash_ms": 190,
        "chase_dash_min_wait_ms": 6500,
        "chase_dash_max_wait_ms": 9200,
        "chase_dash_trigger_distance": 285.0,
        "chase_dash_cooldown_ms": 6200,
        # Sabırsızlık, Berserker'ı sabit hızlı bir füze olmaktan çıkarır. Oyuncuya
        # uzun süre baskı kuramazsa yürüyüşü kademeli hızlanır; temas kurunca söner.
        "impatience_delay_ms": 1800,
        "impatience_rise_sec": 4.4,
        "impatience_decay_sec": 1.45,
        "impatience_speed_bonus": 0.18,
        "poise_max": 118.0,
        "poise_regen_per_sec": 24.0,
        "poise_damage_scale": 0.82,
        "stagger_ms": 315,
        "enrage_hp_ratio": 0.44,
        "enrage_speed_mul": 1.10,
        # Okunabilir Berserker state-machine ayarları: uzun süreli dairesel orbit
        # yerine kısa baskı/commit pencereleri ve başarısız saldırı sonrası kısa reset.
        "pressure_commit_ms": 920,
        "post_miss_reposition_ms": 690,
        "close_speed_mul": 0.88,
        "attack_cooldown_jitter_ms": 180,
        "spawn_min_player_distance": 520.0,
        "preferred_spawns": [
            (1180.0, 345.0),
            (1260.0, 270.0),
            (1160.0, 470.0),
        ],
    },
    "headsthrower": {
        "name_tr": "Kafa Fırlatıcı",
        "name_en": "Heads Thrower",
        "level": 5,
        # Zırhsız ve kırılgan: oyunun başlangıç hasarında bile genellikle tek vuruş.
        "max_hp": 20,
        "move_speed": 142.0,
        "acceleration": 760.0,
        "steering_lambda": 10.4,
        "arrival_sigma": 68.0,
        "stop_radius": 34.0,
        # Melee kullanmaz; bu alanlar ortak motor/future-save uyumluluğu içindir.
        "attack_range": 0.0,
        "attack_contact_gap": 0.0,
        "attack_start_contact_gap": 0.0,
        "attack_damage": 0,
        "attack_cooldown_ms": 2550,
        "attack_frame_ms": 62,
        "attack_impact_frame": 6,
        "attack_recovery_ms": 640,
        "walk_frame_ms": 82,
        "idle_frame_ms": 108,
        "body_half_width": 15,
        "body_height": 34,
        "nav_margin": 3,
        "attack_half_width": 0,
        "attack_half_height": 0,
        "sprite_scale": 1.02,
        "separation_radius": 64.0,
        "separation_strength": 108.0,
        "prediction_max": 0.34,
        "hit_stun_ms": 185,
        "path_replan_ms": 460,
        "path_lookahead": 98.0,
        "clearance_weight": 0.28,
        "turn_weight": 0.061,
        "poise_max": 12.0,
        "poise_regen_per_sec": 8.0,
        "poise_damage_scale": 1.8,
        "stagger_ms": 430,
        # Ranged band. Yakında kalırsa kaçar, çok uzaktaysa veya LOS kapalıysa
        # yeni bir atış koridoru arar. Taş fırlatmadan önce pickup telegraph vardır.
        "ranged_min": 205.0,
        "ranged_preferred": 305.0,
        "ranged_max": 445.0,
        "ranged_throw_damage": 42,
        "ranged_throw_cooldown_min_ms": 2350,
        "ranged_throw_cooldown_max_ms": 3150,
        "ranged_pickup_frame_ms": 58,
        "ranged_throw_frame_ms": 64,
        "ranged_throw_release_frame": 7,
        "ranged_projectile_flight_min_ms": 690,
        "ranged_projectile_flight_max_ms": 910,
        "ranged_projectile_arc": 72.0,
        "ranged_projectile_hit_radius": 30.0,
        "ranged_reposition_refresh_ms": 520,
        "spawn_min_player_distance": 430.0,
        "preferred_spawns": [
            (1430.0, 505.0),
            (1370.0, 310.0),
            (920.0, 280.0),
        ],
    },
    # Rat config yalnız collision/clearance yardımcılarını tekrar kullanmak için
    # burada yaşar. COMMON_ENEMY_TURLERI içinde olmadığı için asla düşman spawnı olmaz.
    "rat": {
        "name_tr": "Fare",
        "name_en": "Rat",
        "max_hp": 1,
        "move_speed": 128.0,
        "acceleration": 980.0,
        "steering_lambda": 14.0,
        "arrival_sigma": 30.0,
        "stop_radius": 0.0,
        "attack_range": 0.0,
        "attack_contact_gap": 0.0,
        "attack_start_contact_gap": 0.0,
        "attack_damage": 0,
        "attack_cooldown_ms": 999999,
        "attack_frame_ms": 100,
        "attack_impact_frame": 0,
        "attack_recovery_ms": 0,
        "walk_frame_ms": 48,
        "idle_frame_ms": 100,
        "body_half_width": 5,
        "body_height": 7,
        "nav_margin": 1,
        "attack_half_width": 0,
        "attack_half_height": 0,
        "sprite_scale": 0.48,
        "separation_radius": 18.0,
        "separation_strength": 30.0,
        "prediction_max": 0.0,
        "hit_stun_ms": 0,
        "path_replan_ms": 999999,
        "path_lookahead": 0.0,
        "clearance_weight": 0.10,
        "turn_weight": 0.02,
        "poise_max": 0.0,
        "poise_regen_per_sec": 0.0,
        "poise_damage_scale": 0.0,
        "stagger_ms": 0,
        "spawn_min_player_distance": 0.0,
        "preferred_spawns": [],
    },
    "tarkard": {
        "name_tr": "Tarkard",
        "name_en": "Tarkard",
        "level": 25,
        "max_hp": 700,
        "move_speed": 126.0,
        "acceleration": 610.0,
        "steering_lambda": 8.9,
        "arrival_sigma": 86.0,
        "stop_radius": 61.0,
        "attack_range": 90.0,
        "attack_contact_gap": 36.0,
        "attack_start_contact_gap": 46.0,
        # Gerçek hasar özel sınıfta max HP'nin %75'i olarak çözülür.
        "attack_damage": 75,
        "attack_cooldown_ms": 1680,
        "attack_frame_ms": 126,
        "attack_impact_frame": 3,
        "attack_recovery_ms": 610,
        "walk_frame_ms": 148,
        "idle_frame_ms": 270,
        "body_half_width": 27,
        "body_height": 29,
        "nav_margin": 7,
        "attack_half_width": 61,
        "attack_half_height": 45,
        "sprite_scale": 1.08,
        "separation_radius": 96.0,
        "separation_strength": 205.0,
        "prediction_max": 0.18,
        "hit_stun_ms": 52,
        "path_replan_ms": 390,
        "path_lookahead": 118.0,
        "clearance_weight": 0.38,
        "turn_weight": 0.048,
        "combat_radius": 104.0,
        "combat_strafe_strength": 0.22,
        "flank_refresh_ms": 430,
        "poise_max": 260.0,
        "poise_regen_per_sec": 34.0,
        "poise_damage_scale": 0.48,
        "stagger_ms": 470,
        "spawn_min_player_distance": 360.0,
        "preferred_spawns": [
            (620.0, 480.0),
            (610.0, 330.0),
            (1090.0, 525.0),
        ],
    },
    "torrmund": {
        "name_tr": "Sir Torrmund",
        "name_en": "Sir Torrmund",
        "fully_armored": True,
        "level": 25,
        "max_hp": 1000,
        "move_speed": 112.0,
        "acceleration": 545.0,
        "steering_lambda": 8.1,
        "arrival_sigma": 92.0,
        "stop_radius": 61.0,
        "attack_range": 88.0,
        "attack_contact_gap": 24.0,
        "attack_start_contact_gap": 31.0,
        # Gerçek vuruş özel sınıfta ölümcül kesme olarak uygulanır.
        "attack_damage": 9999,
        "attack_cooldown_ms": 2240,
        "attack_frame_ms": 145,
        "attack_impact_frame": 4,
        "attack_recovery_ms": 920,
        "walk_frame_ms": 158,
        "idle_frame_ms": 285,
        "body_half_width": 28,
        "body_height": 31,
        "nav_margin": 8,
        "attack_half_width": 61,
        "attack_half_height": 40,
        "sprite_scale": 1.05,
        "separation_radius": 106.0,
        "separation_strength": 220.0,
        "prediction_max": 0.24,
        "hit_stun_ms": 42,
        "path_replan_ms": 370,
        "path_lookahead": 132.0,
        "clearance_weight": 0.44,
        "turn_weight": 0.043,
        "combat_radius": 94.0,
        "combat_strafe_strength": 0.16,
        "flank_refresh_ms": 470,
        "poise_max": 380.0,
        "poise_regen_per_sec": 42.0,
        "poise_damage_scale": 0.36,
        "stagger_ms": 520,
        "spawn_min_player_distance": 500.0,
        "preferred_spawns": [
            (980.0, 520.0),
            (1325.0, 520.0),
            (1015.0, 300.0),
        ],
    },
}

COMMON_ENEMY_NAV_GRID = 18
COMMON_ENEMY_NAV_DIAGONAL = math.sqrt(2.0)
COMMON_ENEMY_NAV_MAX_DUGUM = 4200
COMMON_ENEMY_NAV_HEURISTIC_WEIGHT = 1.015
COMMON_ENEMY_NAV_GOAL_RING = 7

# performans mimarisi:
# - fizik / animasyon 60 Hz kalır,
# - lokal steering yaklaşık 14-20 Hz hesaplanır ve aradaki karelerde karar korunur,
# - Theta* tek karede binlerce node çözmek yerine frame-budget ile artımlı ilerler.
COMMON_ENEMY_LOCAL_HORIZONS = (0.115, 0.225)
COMMON_ENEMY_LOCAL_TICK_MS = {
    "crawler": 72,
    "berserker": 64,
    "headsthrower": 70,
    "tarkard": 78,
    "torrmund": 86,
}
COMMON_ENEMY_NAV_FOLLOW_TICK_MS = {
    "crawler": 96,
    "berserker": 84,
    "headsthrower": 92,
    "tarkard": 82,
    "torrmund": 88,
}
COMMON_ENEMY_PATH_BUDGET_PER_FRAME = 410
COMMON_ENEMY_PATH_BUDGET_PER_ENEMY = {
    "crawler": 96,
    "berserker": 116,
    "headsthrower": 112,
    "tarkard": 126,
    "torrmund": 132,
}
COMMON_ENEMY_NAV_LOS_CACHE_MAX = 18000
COMMON_ENEMY_DEBUG_NAV = False
COMMON_ENEMY_PERF_DEBUG = False

# Navigation cache map boyutu değişince otomatik invalid olur.
_common_enemy_nav_gecerlilik_cache = {}
_common_enemy_nav_clearance_cache = {}
_common_enemy_nav_los_cache = {}
_common_enemy_nav_cache_boyutu = None
_common_enemy_collision_bbox_cache = []
_common_enemy_path_budget_remaining = COMMON_ENEMY_PATH_BUDGET_PER_FRAME
_common_enemy_path_budget_frame = -1

# Oyuncunun yalnız hızı değil ivmesi de yumuşatılır. Berserker kısa tahminlerde
# bunu kullanır; Crawler ise bilerek çok az prediction kullanır.
common_enemy_oyuncu_ivmesi = pygame.Vector2(0.0, 0.0)
common_enemy_onceki_oyuncu_hizi = pygame.Vector2(0.0, 0.0)
# </POTBO_STAGE S0423>

# <POTBO_STAGE S0429>


def _rectler_arasi_kenar_mesafesi(a, b):
    """İki axis-aligned rect'in en yakın kenarları arasındaki Öklid mesafesi.

    Overlap varsa 0 döner. Merkez mesafesi yerine kenar mesafesi kullanmak sprite
    boyutu farklı düşmanlarda aynı "temas" hissini korur; özellikle büyük Tarkard
    ve Torrmund'un merkezleri uzak olsa bile ellerinin/gövdesinin gerçekten yakında
    olup olmadığını doğru ayırır.
    """
    dx = max(float(a.left - b.right), float(b.left - a.right), 0.0)
    dy = max(float(a.top - b.bottom), float(b.top - a.bottom), 0.0)
    return math.hypot(dx, dy)
# </POTBO_STAGE S0429>

# <POTBO_STAGE S0431>


def common_enemy_saldiri_los_acik_mi(dusman, adim=4.5):
    """Melee için ince ground-plane LOS.

    Navigation LOS enemy'nin bütün body footprint'ini hedef noktaya kadar taşımayı
    sınar; bu pathfinding için doğrudur ama melee için fazla katıdır. Oyuncu kayanın
    kenarında durduğunda enemy gövdesi oyuncunun merkezine sığmasa bile eli/kılıcı
    ona dokunabilir. Bu fonksiyon yalnız iki ayağın arasındaki ince statik engeli
    arar: duvardan vurmayı engeller, fakat "görsel olarak değdi ama hasar gelmedi"
    hatasını yaratmaz.
    """
    if dusman is None:
        return False
    bas = pygame.Vector2(float(dusman.x), float(dusman.y) - 7.0)
    son = pygame.Vector2(float(oyuncu_x), float(oyuncu_y) - 7.0)
    fark = son - bas
    mesafe = fark.length()
    if mesafe <= 1.0:
        return True

    sayi = max(2, int(math.ceil(mesafe / max(3.5, float(adim)))))
    # Endpoint'leri bilerek atla: source/target kendi geçerli ayak alanında olabilir,
    # asıl aradığımız ikisinin ARASINDA solid polygon bulunup bulunmadığıdır.
    for i in range(1, sayi):
        p = bas.lerp(son, i / sayi)
        if harita_pikseli_engel_mi(p.x, p.y):
            return False

    a = (int(round(bas.x)), int(round(bas.y)))
    b = (int(round(son.x)), int(round(son.y)))
    # Solid NPC/merchant gövdesinin içinden de kılıç geçmez. Çok yakın endpoint
    # overlap'larında clipline false-positive üretmemesi için rectler hafif daraltılır.
    for blocker in (
        npc_carpisma_rect(),
        merchant_carpisma_rect(),
    ):
        r = blocker.inflate(-4, -4)
        if r.width > 0 and r.height > 0 and r.clipline(a, b):
            if not r.collidepoint(a) and not r.collidepoint(b):
                return False
    return True
# </POTBO_STAGE S0431>

# <POTBO_STAGE S0433>


def _common_enemy_adi(cfg):
    return cfg["name_tr"] if dil == "TR" else cfg["name_en"]
# </POTBO_STAGE S0433>

# <POTBO_STAGE S0435>


def _common_enemy_yon_bul(dx, dy, mevcut="down"):
    if abs(dx) < 0.001 and abs(dy) < 0.001:
        return mevcut
    if abs(dx) >= abs(dy):
        return "right" if dx > 0 else "left"
    return "down" if dy > 0 else "up"


def _berserker_gorsel_yon_bul(dx, dy, mevcut="down_right"):
    mevcut = mevcut if mevcut in BERSERKER_GORSEL_YON_SIRASI else "down_right"
    onceki_dikey, onceki_yatay = mevcut.split("_", 1)
    esik = 3.0

    if dx > esik:
        yatay = "right"
    elif dx < -esik:
        yatay = "left"
    else:
        yatay = onceki_yatay

    if dy > esik:
        dikey = "down"
    elif dy < -esik:
        dikey = "up"
    else:
        dikey = onceki_dikey

    return f"{dikey}_{yatay}"


def _common_enemy_nav_cache_dogrula():
    global _common_enemy_nav_cache_boyutu
    global _common_enemy_collision_bbox_cache
    boyut = (HARITA_GENISLIK, HARITA_YUKSEKLIK)
    if _common_enemy_nav_cache_boyutu != boyut:
        _common_enemy_nav_gecerlilik_cache.clear()
        _common_enemy_nav_clearance_cache.clear()
        _common_enemy_nav_los_cache.clear()
        _common_enemy_nav_cache_boyutu = boyut
        _common_enemy_collision_bbox_cache = []
        for polygon in collision_polygonlari():
            if not polygon:
                continue
            xs = [p[0] for p in polygon]
            ys = [p[1] for p in polygon]
            bbox = pygame.Rect(
                int(min(xs)),
                int(min(ys)),
                max(1, int(max(xs) - min(xs) + 1)),
                max(1, int(max(ys) - min(ys) + 1)),
            )
            _common_enemy_collision_bbox_cache.append((bbox, polygon))


def _common_enemy_path_budget_sifirla(simdi):
    """Her render frame'inde pathfinder'a sabit CPU bütçesi verir."""
    global _common_enemy_path_budget_remaining
    global _common_enemy_path_budget_frame
    frame = int(simdi)
    if _common_enemy_path_budget_frame != frame:
        _common_enemy_path_budget_frame = frame
        _common_enemy_path_budget_remaining = COMMON_ENEMY_PATH_BUDGET_PER_FRAME


def _common_enemy_path_budget_al(tur):
    global _common_enemy_path_budget_remaining
    istenen = int(COMMON_ENEMY_PATH_BUDGET_PER_ENEMY.get(tur, 120))
    verilen = max(0, min(istenen, _common_enemy_path_budget_remaining))
    _common_enemy_path_budget_remaining -= verilen
    return verilen
# </POTBO_STAGE S0435>

# <POTBO_STAGE S0439>


def _common_enemy_hizli_statik_gecerli_mi(tur, x, y):
    """
    Local steering için iki aşamalı statik test.

    Geniş bir nav hücresindeysek cached occupancy yeterlidir. Kaya/duvar sınırına
    yakın hücrelerde kesin rect-polygon testi devreye girer. Böylece AI yüzlerce
    polygon testi yapmak yerine pahalı geometriyi yalnız gerektiğinde kullanır.
    """
    h = (
        int(float(x) // COMMON_ENEMY_NAV_GRID),
        int(float(y) // COMMON_ENEMY_NAV_GRID),
    )
    if not _common_enemy_hucre(tur, h):
        return False
    if _common_enemy_hucre_clearance(tur, h) >= 2.0:
        return True
    return common_enemy_statik_konum_gecerli_mi(tur, x, y, navigation=False)


def common_enemy_spawn_gecerli_mi(tur, x, y, digerler=None):
    if not common_enemy_statik_konum_gecerli_mi(tur, x, y, navigation=False):
        return False

    cfg = COMMON_ENEMY_CONFIG[tur]
    yarim = int(cfg["body_half_width"])
    yuk = int(cfg["body_height"])
    rect = pygame.Rect(
        int(round(x)) - yarim,
        int(round(y)) - yuk,
        yarim * 2,
        yuk,
    )

    if rect.inflate(18, 12).colliderect(oyuncu_carpisma_rect(oyuncu_x, oyuncu_y)):
        return False

    for diger in digerler or []:
        if not getattr(diger, "active", True):
            continue
        if rect.inflate(28, 20).colliderect(common_enemy_carpisma_rect(diger)):
            return False
    return True


def common_enemy_dogrudan_yol_acik_mi(tur, baslangic, hedef, adim=7.0, navigation=True):
    """Body-width line of travel. 7px sampling ince kaya köşelerini kaçırmaz."""
    bas = pygame.Vector2(baslangic)
    son = pygame.Vector2(hedef)
    fark = son - bas
    mesafe = fark.length()
    if mesafe <= 0.001:
        return True

    sayi = max(1, int(math.ceil(mesafe / max(4.0, float(adim)))))
    for i in range(1, sayi + 1):
        p = bas.lerp(son, i / sayi)
        if not common_enemy_statik_konum_gecerli_mi(
            tur, p.x, p.y, navigation=navigation
        ):
            return False
    return True


def _common_enemy_hucre_merkezi(hucre, grid=COMMON_ENEMY_NAV_GRID):
    return pygame.Vector2((hucre[0] + 0.5) * grid, (hucre[1] + 0.5) * grid)


def _common_enemy_hucre(tur, hucre):
    _common_enemy_nav_cache_dogrula()
    anahtar = (tur, int(hucre[0]), int(hucre[1]))
    if anahtar not in _common_enemy_nav_gecerlilik_cache:
        p = _common_enemy_hucre_merkezi(hucre)
        _common_enemy_nav_gecerlilik_cache[anahtar] = (
            common_enemy_statik_konum_gecerli_mi(tur, p.x, p.y, navigation=True)
        )
    return _common_enemy_nav_gecerlilik_cache[anahtar]


def _common_enemy_hucre_clearance(tur, hucre):
    """
    Ucuz, cache'li koridor açıklığı tahmini.

    V4 her hücre için 8 yönde 4 halka tarıyordu. Theta* ilk kez bir bölgeye
    girdiğinde bu işlem yüzlerce ekstra rect-polygon testine dönüşebiliyordu.
    V5 yakın halkaları önem sırasına göre örnekler; steering/path cost için aynı
    davranışsal sinyali çok daha düşük maliyetle verir.
    """
    _common_enemy_nav_cache_dogrula()
    anahtar = (tur, int(hucre[0]), int(hucre[1]))
    if anahtar in _common_enemy_nav_clearance_cache:
        return _common_enemy_nav_clearance_cache[anahtar]
    if not _common_enemy_hucre(tur, hucre):
        _common_enemy_nav_clearance_cache[anahtar] = 0.0
        return 0.0

    cx, cy = int(hucre[0]), int(hucre[1])
    cardinal1 = ((1, 0), (-1, 0), (0, 1), (0, -1))
    diagonal1 = ((1, 1), (-1, 1), (1, -1), (-1, -1))
    cardinal2 = ((2, 0), (-2, 0), (0, 2), (0, -2))
    diagonal2 = ((2, 2), (-2, 2), (2, -2), (-2, -2))

    if any(not _common_enemy_hucre(tur, (cx + dx, cy + dy)) for dx, dy in cardinal1):
        deger = 0.55
    elif any(not _common_enemy_hucre(tur, (cx + dx, cy + dy)) for dx, dy in diagonal1):
        deger = 1.05
    elif any(not _common_enemy_hucre(tur, (cx + dx, cy + dy)) for dx, dy in cardinal2):
        deger = 1.75
    elif any(not _common_enemy_hucre(tur, (cx + dx, cy + dy)) for dx, dy in diagonal2):
        deger = 2.45
    else:
        deger = 3.35

    _common_enemy_nav_clearance_cache[anahtar] = deger
    return deger


def _common_enemy_en_yakin_gecerli_hucre(
    tur,
    merkez_hucre,
    hedef_nokta,
    maksimum_ring=COMMON_ENEMY_NAV_GOAL_RING,
):
    adaylar = []
    hedef_v = pygame.Vector2(hedef_nokta)
    for r in range(0, maksimum_ring + 1):
        if r == 0:
            hucreler = [merkez_hucre]
        else:
            hucreler = []
            cx, cy = merkez_hucre
            for dx in range(-r, r + 1):
                hucreler.append((cx + dx, cy - r))
                hucreler.append((cx + dx, cy + r))
            for dy in range(-r + 1, r):
                hucreler.append((cx - r, cy + dy))
                hucreler.append((cx + r, cy + dy))

        for h in hucreler:
            if not _common_enemy_hucre(tur, h):
                continue
            p = _common_enemy_hucre_merkezi(h)
            clearance = _common_enemy_hucre_clearance(tur, h)
            skor = (p - hedef_v).length_squared() - clearance * 42.0
            adaylar.append((skor, h))
        if adaylar:
            adaylar.sort(key=lambda x: x[0])
            return adaylar[0][1]
    return None


def _common_enemy_hucre_los(tur, a_h, b_h):
    """
    Body-clearance grid LOS. Dünya statik olduğu için sonuç simetrik ve kalıcıdır;
    V5 aynı koridoru tekrar tekrar taramaz.
    """
    _common_enemy_nav_cache_dogrula()
    a = (int(a_h[0]), int(a_h[1]))
    b = (int(b_h[0]), int(b_h[1]))
    if a <= b:
        anahtar = (tur, a[0], a[1], b[0], b[1])
    else:
        anahtar = (tur, b[0], b[1], a[0], a[1])
    sonuc = _common_enemy_nav_los_cache.get(anahtar)
    if sonuc is not None:
        return sonuc

    ax, ay = a
    bx, by = b
    dx = bx - ax
    dy = by - ay
    adim = max(abs(dx), abs(dy))
    if adim <= 0:
        sonuc = _common_enemy_hucre(tur, (ax, ay))
    else:
        sonuc = True
        onceki = (ax, ay)
        for i in range(0, adim + 1):
            oran = i / adim
            hx = int(round(ax + dx * oran))
            hy = int(round(ay + dy * oran))
            h = (hx, hy)
            if not _common_enemy_hucre(tur, h):
                sonuc = False
                break
            if h != onceki:
                sx = h[0] - onceki[0]
                sy = h[1] - onceki[1]
                if sx and sy:
                    if not _common_enemy_hucre(tur, (onceki[0] + sx, onceki[1])):
                        sonuc = False
                        break
                    if not _common_enemy_hucre(tur, (onceki[0], onceki[1] + sy)):
                        sonuc = False
                        break
                onceki = h

    if len(_common_enemy_nav_los_cache) >= COMMON_ENEMY_NAV_LOS_CACHE_MAX:
        # Python dict insertion-order'dır; en eski yaklaşık %12.5'i topluca atmak
        # her eklemede pop yapmaktan daha ucuzdur.
        silinecek = max(256, COMMON_ENEMY_NAV_LOS_CACHE_MAX // 8)
        for k in list(_common_enemy_nav_los_cache.keys())[:silinecek]:
            _common_enemy_nav_los_cache.pop(k, None)
    _common_enemy_nav_los_cache[anahtar] = bool(sonuc)
    return bool(sonuc)


def _common_enemy_octile(a, b):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return (dx + dy) + (COMMON_ENEMY_NAV_DIAGONAL - 2.0) * min(dx, dy)


def _common_enemy_path_turn_cost(parent, current, nxt, agirlik):
    if parent is None or parent == current:
        return 0.0
    a = pygame.Vector2(current[0] - parent[0], current[1] - parent[1])
    b = pygame.Vector2(nxt[0] - current[0], nxt[1] - current[1])
    if a.length_squared() <= 0.0 or b.length_squared() <= 0.0:
        return 0.0
    dot = max(-1.0, min(1.0, a.normalize().dot(b.normalize())))
    return (1.0 - dot) * float(agirlik)


def common_enemy_astar_yol_bul(
    tur,
    baslangic,
    hedef,
    maksimum_dugum=COMMON_ENEMY_NAV_MAX_DUGUM,
    yasak_hucreler=None,
):
    """
    Clearance-aware Theta*.

    İsmi geriye uyumluluk için astar olarak kaldı; algoritma parent LOS kullanarak
    klasik A* grid zigzag'ını any-angle segmente indirir. Cost fonksiyonu:

        J = Σ distance + λc / (clearance + ε) + λt * turn_cost

    Bu nedenle iki rota benzer uzunluktaysa gövdeyi kayaya sürten değil daha geniş
    koridoru seçer. Heuristic ağırlığı 1.015; pratikte çok daha hızlıyken optimuma
    çok yakın kalır.
    """
    grid = COMMON_ENEMY_NAV_GRID
    bas = pygame.Vector2(baslangic)
    son = pygame.Vector2(hedef)
    bas_h = (int(bas.x // grid), int(bas.y // grid))
    hedef_h = (int(son.x // grid), int(son.y // grid))
    yasak = set(yasak_hucreler or ())

    if not _common_enemy_hucre(tur, bas_h):
        bas_h = _common_enemy_en_yakin_gecerli_hucre(tur, bas_h, bas, 4)
        if bas_h is None:
            return []
    if not _common_enemy_hucre(tur, hedef_h):
        hedef_h = _common_enemy_en_yakin_gecerli_hucre(tur, hedef_h, son)
        if hedef_h is None:
            return []

    cfg = COMMON_ENEMY_CONFIG[tur]
    clear_w = float(cfg.get("clearance_weight", 0.2))
    turn_w = float(cfg.get("turn_weight", 0.06))
    komsular = (
        (-1, 0, 1.0),
        (1, 0, 1.0),
        (0, -1, 1.0),
        (0, 1, 1.0),
        (-1, -1, COMMON_ENEMY_NAV_DIAGONAL),
        (1, -1, COMMON_ENEMY_NAV_DIAGONAL),
        (-1, 1, COMMON_ENEMY_NAV_DIAGONAL),
        (1, 1, COMMON_ENEMY_NAV_DIAGONAL),
    )

    acik = []
    sayac = 0
    g = {bas_h: 0.0}
    parent = {bas_h: bas_h}
    kapali = set()
    heapq.heappush(
        acik,
        (
            _common_enemy_octile(bas_h, hedef_h),
            0.0,
            sayac,
            bas_h,
        ),
    )

    islenen = 0
    while acik and islenen < maksimum_dugum:
        _, mevcut_g, _, mevcut = heapq.heappop(acik)
        if mevcut in kapali:
            continue
        kapali.add(mevcut)
        islenen += 1

        if mevcut == hedef_h:
            zincir = [mevcut]
            guard = 0
            while zincir[-1] != bas_h and guard < maksimum_dugum:
                zincir.append(parent[zincir[-1]])
                guard += 1
            zincir.reverse()
            noktalar = [_common_enemy_hucre_merkezi(h) for h in zincir[1:]]
            # Son gerçek hedef navigation açısından geçerliyse exact goal kullan.
            if noktalar and common_enemy_statik_konum_gecerli_mi(
                tur, son.x, son.y, navigation=True
            ):
                noktalar[-1] = son
            return noktalar

        for dx, dy, taban_maliyet in komsular:
            komsu = (mevcut[0] + dx, mevcut[1] + dy)
            if komsu in kapali or komsu in yasak or not _common_enemy_hucre(tur, komsu):
                continue
            if dx and dy:
                # Diagonal corner cutting kesin yasak.
                if not _common_enemy_hucre(tur, (mevcut[0] + dx, mevcut[1])):
                    continue
                if not _common_enemy_hucre(tur, (mevcut[0], mevcut[1] + dy)):
                    continue

            aday_parent = mevcut
            aday_g = mevcut_g + taban_maliyet
            mevcut_parent = parent.get(mevcut, mevcut)

            # Theta*: parent -> neighbour görüşü açıksa current node'u aradan çıkar.
            if mevcut_parent != mevcut and _common_enemy_hucre_los(
                tur, mevcut_parent, komsu
            ):
                dist = pygame.Vector2(
                    komsu[0] - mevcut_parent[0],
                    komsu[1] - mevcut_parent[1],
                ).length()
                aday_parent = mevcut_parent
                aday_g = g.get(mevcut_parent, mevcut_g) + dist

            clearance = _common_enemy_hucre_clearance(tur, komsu)
            dar_ceza = clear_w * max(0.0, 3.15 - clearance) ** 2
            donus_ceza = _common_enemy_path_turn_cost(
                parent.get(aday_parent),
                aday_parent,
                komsu,
                turn_w,
            )
            yeni_g = aday_g + dar_ceza + donus_ceza

            if yeni_g + 1e-6 >= g.get(komsu, float("inf")):
                continue

            g[komsu] = yeni_g
            parent[komsu] = aday_parent
            sayac += 1
            h = _common_enemy_octile(komsu, hedef_h) * COMMON_ENEMY_NAV_HEURISTIC_WEIGHT
            heapq.heappush(acik, (yeni_g + h, yeni_g, sayac, komsu))

    return []


class CommonEnemyThetaJob:
    """
    Frame-budgeted Theta* araması.

    V4'ün en büyük spike kaynağı bütün Theta* aramasının tek frame'de bitirilmesiydi.
    Bu sınıf aynı maliyet modelini korur fakat aramayı küçük node paketleri halinde
    sürdürür. Fizik akarken rota birkaç kare içinde olgunlaşır; tek kare FPS çöküşü
    oluşmaz.
    """

    def __init__(self, tur, baslangic, hedef, yasak_hucreler=None):
        self.tur = tur
        self.cfg = COMMON_ENEMY_CONFIG[tur]
        self.grid = COMMON_ENEMY_NAV_GRID
        self.requested_goal = pygame.Vector2(hedef)
        self.yasak = set(yasak_hucreler or ())
        self.done = False
        self.success = False
        self.result = []
        self.processed = 0
        self.counter = 0

        bas = pygame.Vector2(baslangic)
        son = pygame.Vector2(hedef)
        bas_h = (
            int(bas.x // self.grid),
            int(bas.y // self.grid),
        )
        hedef_h = (
            int(son.x // self.grid),
            int(son.y // self.grid),
        )
        if not _common_enemy_hucre(tur, bas_h):
            bas_h = _common_enemy_en_yakin_gecerli_hucre(tur, bas_h, bas, 4)
        if not _common_enemy_hucre(tur, hedef_h):
            hedef_h = _common_enemy_en_yakin_gecerli_hucre(tur, hedef_h, son)

        self.start = bas_h
        self.goal = hedef_h
        self.open = []
        self.g = {}
        self.parent = {}
        self.closed = set()
        self.neighbors = (
            (-1, 0, 1.0),
            (1, 0, 1.0),
            (0, -1, 1.0),
            (0, 1, 1.0),
            (-1, -1, COMMON_ENEMY_NAV_DIAGONAL),
            (1, -1, COMMON_ENEMY_NAV_DIAGONAL),
            (-1, 1, COMMON_ENEMY_NAV_DIAGONAL),
            (1, 1, COMMON_ENEMY_NAV_DIAGONAL),
        )

        if bas_h is None or hedef_h is None:
            self.done = True
            return
        self.g[bas_h] = 0.0
        self.parent[bas_h] = bas_h
        heapq.heappush(
            self.open,
            (
                _common_enemy_octile(bas_h, hedef_h),
                0.0,
                0,
                bas_h,
            ),
        )

    def _bitir(self, node):
        zincir = [node]
        guard = 0
        while zincir[-1] != self.start and guard < COMMON_ENEMY_NAV_MAX_DUGUM:
            onceki = self.parent.get(zincir[-1])
            if onceki is None or onceki == zincir[-1]:
                self.done = True
                self.success = False
                self.result = []
                return
            zincir.append(onceki)
            guard += 1
        zincir.reverse()
        noktalar = [_common_enemy_hucre_merkezi(h) for h in zincir[1:]]
        if noktalar and common_enemy_statik_konum_gecerli_mi(
            self.tur,
            self.requested_goal.x,
            self.requested_goal.y,
            navigation=True,
        ):
            noktalar[-1] = pygame.Vector2(self.requested_goal)
        self.result = noktalar
        self.done = True
        self.success = True

    def step(self, node_budget):
        if self.done or node_budget <= 0:
            return
        clear_w = float(self.cfg.get("clearance_weight", 0.2))
        turn_w = float(self.cfg.get("turn_weight", 0.06))
        limit = min(
            COMMON_ENEMY_NAV_MAX_DUGUM,
            self.processed + int(node_budget),
        )

        while self.open and not self.done and self.processed < limit:
            _, mevcut_g, _, mevcut = heapq.heappop(self.open)
            if mevcut in self.closed:
                continue
            self.closed.add(mevcut)
            self.processed += 1

            if mevcut == self.goal:
                self._bitir(mevcut)
                break

            for dx, dy, taban_maliyet in self.neighbors:
                komsu = (mevcut[0] + dx, mevcut[1] + dy)
                if (
                    komsu in self.closed
                    or komsu in self.yasak
                    or not _common_enemy_hucre(self.tur, komsu)
                ):
                    continue
                if dx and dy:
                    if not _common_enemy_hucre(self.tur, (mevcut[0] + dx, mevcut[1])):
                        continue
                    if not _common_enemy_hucre(self.tur, (mevcut[0], mevcut[1] + dy)):
                        continue

                aday_parent = mevcut
                aday_g = mevcut_g + taban_maliyet
                mevcut_parent = self.parent.get(mevcut, mevcut)
                if mevcut_parent != mevcut and _common_enemy_hucre_los(
                    self.tur, mevcut_parent, komsu
                ):
                    dist = math.hypot(
                        komsu[0] - mevcut_parent[0],
                        komsu[1] - mevcut_parent[1],
                    )
                    aday_parent = mevcut_parent
                    aday_g = self.g.get(mevcut_parent, mevcut_g) + dist

                clearance = _common_enemy_hucre_clearance(self.tur, komsu)
                dar_ceza = clear_w * max(0.0, 3.15 - clearance) ** 2
                donus_ceza = _common_enemy_path_turn_cost(
                    self.parent.get(aday_parent),
                    aday_parent,
                    komsu,
                    turn_w,
                )
                yeni_g = aday_g + dar_ceza + donus_ceza
                if yeni_g + 1e-6 >= self.g.get(komsu, float("inf")):
                    continue

                self.g[komsu] = yeni_g
                self.parent[komsu] = aday_parent
                self.counter += 1
                h = (
                    _common_enemy_octile(komsu, self.goal)
                    * COMMON_ENEMY_NAV_HEURISTIC_WEIGHT
                )
                heapq.heappush(
                    self.open,
                    (yeni_g + h, yeni_g, self.counter, komsu),
                )

        if not self.open and not self.done:
            self.done = True
            self.success = False
            self.result = []
        elif self.processed >= COMMON_ENEMY_NAV_MAX_DUGUM and not self.done:
            self.done = True
            self.success = False
            self.result = []


def common_enemy_guvenli_spawn_bul(tur, digerler=None):
    cfg = COMMON_ENEMY_CONFIG[tur]
    minimum_oyuncu = float(cfg["spawn_min_player_distance"])
    altin_aci = math.pi * (3.0 - math.sqrt(5.0))

    for merkez_x, merkez_y in cfg["preferred_spawns"]:
        for i in range(112):
            if i == 0:
                x, y = merkez_x, merkez_y
            else:
                yaricap = 20.0 * math.sqrt(i)
                aci = i * altin_aci
                x = merkez_x + math.cos(aci) * yaricap
                y = merkez_y + math.sin(aci) * yaricap * 0.72
            if math.hypot(x - oyuncu_x, y - oyuncu_y) < minimum_oyuncu:
                continue
            if common_enemy_spawn_gecerli_mi(tur, x, y, digerler):
                return float(x), float(y)

    for y in range(178, max(179, HARITA_YUKSEKLIK - 74), 38):
        for x in range(105, max(106, HARITA_GENISLIK - 90), 44):
            if math.hypot(x - oyuncu_x, y - oyuncu_y) < minimum_oyuncu:
                continue
            if common_enemy_spawn_gecerli_mi(tur, x, y, digerler):
                return float(x), float(y)
    return float(cfg["preferred_spawns"][0][0]), float(cfg["preferred_spawns"][0][1])


def _common_enemy_yon_vektoru(yon):
    return {
        "left": pygame.Vector2(-1.0, 0.0),
        "right": pygame.Vector2(1.0, 0.0),
        "up": pygame.Vector2(0.0, -1.0),
        "down": pygame.Vector2(0.0, 1.0),
    }.get(str(yon), pygame.Vector2(1.0, 0.0))


def _common_enemy_oyuncu_yon_vektoru():
    return _common_enemy_yon_vektoru(oyuncu_yonu)


def _common_enemy_kesisim_hedefi(
    enemy_pos,
    hedef_pos,
    hedef_hiz,
    takip_hizi,
    maksimum_t,
    hedef_ivme=None,
):
    """
    Sabit hızlı pursuer için analitik intercept zamanı çözer:

        ||r + v t||² = s² t²

    Berserker için çözümden sonra sınırlı ivme düzeltmesi eklenir. Çözüm yoksa
    mesafe/hız temelli güvenli look-ahead kullanılır.
    """
    p = pygame.Vector2(enemy_pos)
    q = pygame.Vector2(hedef_pos)
    v = pygame.Vector2(hedef_hiz)
    r = q - p
    s = max(1.0, float(takip_hizi))

    a = v.dot(v) - s * s
    b = 2.0 * r.dot(v)
    c = r.dot(r)
    t_hit = None

    if abs(a) < 1e-7:
        if abs(b) > 1e-7:
            aday = -c / b
            if aday > 0.0:
                t_hit = aday
    else:
        disc = b * b - 4.0 * a * c
        if disc >= 0.0:
            kok = math.sqrt(disc)
            t1 = (-b - kok) / (2.0 * a)
            t2 = (-b + kok) / (2.0 * a)
            pozitif = [t for t in (t1, t2) if t > 0.0]
            if pozitif:
                t_hit = min(pozitif)

    if t_hit is None:
        t_hit = r.length() / s * 0.38
    t_hit = max(0.0, min(float(maksimum_t), t_hit))

    sonuc = q + v * t_hit
    if hedef_ivme is not None and t_hit > 0.0:
        a_vec = _vektor_uzunluk_sinirla(pygame.Vector2(hedef_ivme), 760.0)
        sonuc += a_vec * (0.5 * t_hit * t_hit * 0.34)
    return sonuc


def _common_enemy_dinamik_rect_gecerli(enemy, x, y, digerler, oyuncuyu_engel_say=True):
    rect = enemy.collision_rect(x, y)
    if oyuncuyu_engel_say and rect.colliderect(
        oyuncu_carpisma_rect(oyuncu_x, oyuncu_y)
    ):
        return False
    for diger in digerler:
        if diger is enemy or not getattr(diger, "active", False):
            continue
        tahmin_x = diger.x + getattr(diger, "vx", 0.0) * 0.08
        tahmin_y = diger.y + getattr(diger, "vy", 0.0) * 0.08
        if rect.inflate(4, 3).colliderect(
            common_enemy_carpisma_rect(diger, tahmin_x, tahmin_y)
        ):
            return False
    return True


def combat_enemy_aktorleri():
    sonuc = [
        d
        for d in common_enemies
        if getattr(d, "active", False) and getattr(d, "hp", 0) > 0
    ]
    for d in (tarkard_actor, torrmund_actor):
        if d is not None and getattr(d, "active", False) and getattr(d, "hp", 0) > 0:
            sonuc.append(d)
    return sonuc


def enemy_friendly_melee_vur(attacker, simdi):
    if not getattr(attacker, "attacking", False):
        return 0
    alan = attacker._attack_rect()
    vurulan = 0
    for hedef in combat_enemy_aktorleri():
        if (
            hedef is attacker
            or str(getattr(hedef, "uid", "")) in attacker.attack_friendly_hits
        ):
            continue
        hr = hedef.collision_rect().inflate(8, 12)
        if not alan.colliderect(hr):
            continue
        a = pygame.Vector2(attacker.x, attacker.y - 10)
        b = pygame.Vector2(hedef.x, hedef.y - 10)
        if not _ince_dunya_los_acik_mi(a, b, 5.0):
            continue
        attacker.attack_friendly_hits.add(str(getattr(hedef, "uid", "")))
        hedef.hasar_al(int(attacker.cfg.get("attack_damage", 1)), attacker)
        vurulan += 1
    return vurulan


# =========================================================
# ENEMY FIRE AWARENESS / DISTINCT BEHAVIOUR AI
# =========================================================
# Fireball dodge yalniz Crawler ve Berserker'a aittir. Heads Thrower, Tarkard
# ve Torrmund projectile'i arcade refleksiyle yana kacmaz. Buna karsilik BUTUN
# dusmanlar kalici zemin alevini tehdit kabul eder ve kendi dovus karakterlerine
# uygun bicimde alev alanindan cikmaya calisir.
# ground_style:
# skittish -> Crawler: cabuk ve zikzakli emniyet cizgisi.
# pressure -> Berserker: alevden cikar ama oyuncuya baskiyi tamamen birakmaz.
# ranged -> Heads Thrower: atis mesafesini koruyacak guvenli banda cekilir.
# tank -> Tarkard: projectile'dan kacmaz, yerdeki alevden en kisa saglam
# rotayla yuruyerek cikar.
# tank_guard -> Torrmund: ayni agirlikta, daha kontrollu ve acik zemini tercih eder.
FIRE_ENEMY_AI = {
    "crawler": {
        "ground_style": "skittish",
        "ground_radius": 132.0,
        "ground_speed_mul": 1.34,
        "ground_distance": 78.0,
        "ground_hold_ms": 315,
        "ground_panic_margin": 12.0,
        "projectile_dash": True,
        "projectile_awareness": 440.0,
        "projectile_chance": 0.74,
        "reaction_ms": (88, 158),
        "dash_speed": 390.0,
        "dash_ms": 165,
        "dash_distance": 58.0,
        "dash_cooldown_ms": 1100,
    },
    "berserker": {
        "ground_style": "pressure",
        "ground_radius": 142.0,
        "ground_speed_mul": 1.22,
        "ground_distance": 86.0,
        "ground_hold_ms": 340,
        "ground_panic_margin": 10.0,
        "projectile_dash": True,
        "projectile_awareness": 480.0,
        "projectile_chance": 0.64,
        "reaction_ms": (108, 188),
        "dash_speed": 430.0,
        "dash_ms": 178,
        "dash_distance": 68.0,
        "dash_cooldown_ms": 1320,
    },
    "headsthrower": {
        "ground_style": "ranged",
        "ground_radius": 166.0,
        "ground_speed_mul": 1.27,
        "ground_distance": 108.0,
        "ground_hold_ms": 410,
        "ground_panic_margin": 15.0,
        "projectile_dash": False,
        "projectile_awareness": 0.0,
        "projectile_chance": 0.0,
        "reaction_ms": (9999, 9999),
        "dash_speed": 0.0,
        "dash_ms": 0,
        "dash_distance": 0.0,
        "dash_cooldown_ms": 999999,
    },
    "tarkard": {
        "ground_style": "tank",
        "ground_radius": 152.0,
        "ground_speed_mul": 1.02,
        "ground_distance": 74.0,
        "ground_hold_ms": 430,
        "ground_panic_margin": 8.0,
        "projectile_dash": False,
        "projectile_awareness": 0.0,
        "projectile_chance": 0.0,
        "reaction_ms": (9999, 9999),
        "dash_speed": 0.0,
        "dash_ms": 0,
        "dash_distance": 0.0,
        "dash_cooldown_ms": 999999,
    },
    "torrmund": {
        "ground_style": "tank_guard",
        "ground_radius": 156.0,
        "ground_speed_mul": 0.98,
        "ground_distance": 72.0,
        "ground_hold_ms": 460,
        "ground_panic_margin": 8.0,
        "projectile_dash": False,
        "projectile_awareness": 0.0,
        "projectile_chance": 0.0,
        "reaction_ms": (9999, 9999),
        "dash_speed": 0.0,
        "dash_ms": 0,
        "dash_distance": 0.0,
        "dash_cooldown_ms": 999999,
    },
}
# </POTBO_STAGE S0439>

# <POTBO_STAGE S0441>


class CommonEnemy:
    def __init__(self, uid, tur, x, y):
        self.uid = str(uid)
        self.tur = tur if tur in COMMON_ENEMY_CONFIG else "crawler"
        self.cfg = COMMON_ENEMY_CONFIG[self.tur]
        self.level = int(self.cfg.get("level", 1))
        self.x = float(x)
        self.y = float(y)
        self.vx = 0.0
        self.vy = 0.0
        self.max_hp = int(self.cfg["max_hp"])
        self.hp = self.max_hp
        self.active = True
        self.aggro = False
        self.direction = "left" if self.tur in ("crawler", "tarkard") else "down"
        self.visual_direction = (
            "left" if self.tur in ("crawler", "tarkard") else "down_right"
        )

        # Combat state.
        self.attacking = False
        self.attack_started_ms = -10000
        self.last_attack_ms = -10000
        self.attack_damage_applied = False
        self.attack_connected = False
        self.attack_friendly_hits = set()
        self.recovery_until = 0
        self.last_player_attack_id = -1
        self.last_observed_player_attack_id = -1
        self.hit_stun_until = 0
        self.hit_flash_until = 0
        self.stagger_until = 0
        self.poise = float(self.cfg.get("poise_max", 0.0))
        self.last_poise_hit_ms = -10000
        self.anim_epoch = pygame.time.get_ticks() + (
            sum(ord(c) for c in self.uid) % 173
        )

        # Basit fakat gerçek davranış belleği: oyuncunun swing ritminin EWMA'sı.
        self.player_attack_interval_ema = 760.0
        self.last_player_attack_seen_ms = -10000
        self.player_attack_samples = 0

        # Global navigation / path following.
        self.nav_path = []
        self.nav_index = 0
        self.nav_next_replan_ms = 0
        self.nav_last_goal = pygame.Vector2(self.x, self.y)
        self.nav_goal = pygame.Vector2(self.x, self.y)
        self.nav_bad_cells = {}
        self.nav_failure_count = 0
        self.stuck_ms = 0.0
        self.last_move_distance = 0.0
        self.last_progress_distance = None
        self.wall_follow_until = 0
        self.wall_follow_sign = (
            1.0 if (sum(ord(c) for c in self.uid) % 2 == 0) else -1.0
        )
        self.nav_job = None
        self.nav_goal_cell = None
        self.nav_follow_target = pygame.Vector2(self.x, self.y)
        self.nav_follow_refresh_ms = 0
        self.nav_direct_key = None
        self.nav_direct_value = False

        # Multi-rate local planner cache. Karar 60 kez/s yeniden hesaplanmaz;
        # fizik aradaki karelerde aynı niyeti yumuşakça uygular.
        faz = sum(ord(c) for c in self.uid) % 23
        self.local_plan_until = pygame.time.get_ticks() + faz
        self.local_plan_input_dir = pygame.Vector2(0.0, 0.0)
        self.local_plan_target = pygame.Vector2(self.x, self.y)
        self.local_plan_output_dir = pygame.Vector2(0.0, 0.0)
        self.local_plan_speed_ratio = 0.0

        # Yakın dövüş LOS'u yalnız menzile yaklaşınca ve kısa TTL ile ölçülür.
        self.attack_los_until = 0
        self.attack_los_value = False
        self.attack_los_enemy_pos = pygame.Vector2(self.x, self.y)
        self.attack_los_player_pos = pygame.Vector2(self.x, self.y)

        # Tactical slot cache.
        self.tactical_target = pygame.Vector2(self.x, self.y)
        self.tactical_refresh_ms = 0
        self.orbit_sign = self.wall_follow_sign

        # Crawler evade.
        self.evade_until = 0
        self.evade_target = None
        self.defense_cooldown_until = 0
        self.crawler_commit_until = 0

        # fire-awareness. Scan rate limitedir; 24-38 ground-fire patch'i her
        # enemy için her render frame'inde taranmaz.
        self.fire_ai_next_scan_ms = 0
        self.fire_avoid_until = 0
        self.fire_avoid_target = None
        self.fire_projectile_pending_id = None
        self.fire_projectile_react_at = 0
        self.fire_projectile_ignore_until = 0
        self.fire_dash_until = 0
        self.fire_dash_velocity = pygame.Vector2(0.0, 0.0)
        self.fire_dash_cooldown_until = 0
        self.fire_last_threat_id = None
        # smooth short-dash state. Konum tek framede ziplatilmaz; smoothstep
        # egriyle hizlanip yavaslayarak collision-aware ilerler.
        self.fire_dash_started_ms = 0
        self.fire_dash_direction = pygame.Vector2(0.0, 0.0)
        self.fire_dash_distance_total = 0.0
        self.fire_dash_duration_ms = 0
        self.fire_dash_last_ease = 0.0

        # Berserker dash / pressure state.
        self.dash_until = 0
        self.dash_velocity = pygame.Vector2(0.0, 0.0)
        self.dash_kind = None
        self.dash_cooldown_until = 0
        simdi = pygame.time.get_ticks()
        self.last_pressure_ms = simdi
        self.next_chase_dash_ms = (
            simdi
            + random.randint(
                int(self.cfg.get("chase_dash_min_wait_ms", 999999)),
                int(self.cfg.get("chase_dash_max_wait_ms", 999999)),
            )
            if self.tur == "berserker"
            else 10**12
        )
        self.impatience = 0.0
        self.last_dash_ms = -10000
        # Berserker kısa, okunabilir commitment pencereleri kullanır. Böylece
        # hedefin çevresinde matematiksel olarak kusursuz ama görsel olarak garip
        # daireler çizmek yerine karar verir, saldırır ve kısa süre yeniden konumlanır.
        self.pressure_commit_until = 0
        self.post_miss_reposition_until = 0
        self.next_attack_variance_ms = 0

        # Health bar trailing value; hasarın ağırlığını görsel olarak daha net verir.
        self.hp_display = float(self.hp)
        self.hp_trail = float(self.hp)
        self.hp_trail_hold_until = 0
        self._son_cizim_rect = None

    @property
    def name(self):
        return _common_enemy_adi(self.cfg)

    def collision_rect(self, x=None, y=None):
        return common_enemy_carpisma_rect(self, x, y)

    def to_save(self):
        return {
            "id": self.uid,
            "type": self.tur,
            "x": round(self.x, 3),
            "y": round(self.y, 3),
            "hp": int(self.hp),
            "active": bool(self.active),
            "aggro": bool(self.aggro),
            "direction": self.direction,
            "visual_direction": self.visual_direction,
            "poise": round(float(self.poise), 3),
        }

    def _faz_hiz_carpani(self):
        if self.tur != "berserker":
            return 1.0
        oran = self.hp / max(1.0, float(self.max_hp))
        if oran <= float(self.cfg.get("enrage_hp_ratio", 0.0)):
            return float(self.cfg.get("enrage_speed_mul", 1.0))
        return 1.0

    def _anlik_move_speed(self):
        hiz = float(self.cfg["move_speed"]) * self._faz_hiz_carpani()
        if self.tur == "berserker":
            hiz *= 1.0 + max(0.0, min(1.0, self.impatience)) * float(
                self.cfg.get("impatience_speed_bonus", 0.0)
            )
        return hiz

    def _berserker_sabirsizlik_guncelle(self, dt, simdi, mesafe):
        if self.tur != "berserker":
            return
        gecikme = int(self.cfg.get("impatience_delay_ms", 1000))
        baski_kurulamadi = mesafe > 145.0 and simdi - self.last_pressure_ms >= gecikme
        if baski_kurulamadi:
            sure = max(
                0.25,
                float(self.cfg.get("impatience_rise_sec", 3.0)),
            )
            self.impatience = min(1.0, self.impatience + dt / sure)
        else:
            sure = max(
                0.25,
                float(self.cfg.get("impatience_decay_sec", 1.2)),
            )
            self.impatience = max(0.0, self.impatience - dt / sure)

    def _poise_guncelle(self, dt, simdi):
        if simdi < self.stagger_until:
            return
        if simdi - self.last_poise_hit_ms < 620:
            return
        maksimum = float(self.cfg.get("poise_max", 0.0))
        self.poise = min(
            maksimum,
            self.poise + float(self.cfg.get("poise_regen_per_sec", 0.0)) * dt,
        )

    def hasar_al(self, miktar, kaynak=None):
        if not self.active:
            return 0
        miktar = max(1, int(miktar))
        simdi = pygame.time.get_ticks()
        oyuncudan = (
            kaynak is None
            or kaynak == "player"
            or bool(getattr(kaynak, "is_player_magic", False))
        )
        eski_aggro = self.aggro
        self.hp = max(0, self.hp - miktar)
        if oyuncudan:
            self.aggro = True
        self.hp_trail_hold_until = simdi + 260
        self.hit_stun_until = max(
            self.hit_stun_until,
            simdi + int(self.cfg["hit_stun_ms"]),
        )
        self.hit_flash_until = simdi + 120
        self.last_poise_hit_ms = simdi
        if self.tur == "berserker":
            self.impatience = min(1.0, self.impatience + 0.10)
        self.poise -= miktar * float(self.cfg.get("poise_damage_scale", 1.0))
        if self.poise <= 0.0 and self.hp > 0:
            self.poise = float(self.cfg.get("poise_max", 0.0))
            self.stagger_until = simdi + int(self.cfg.get("stagger_ms", 300))
            self.hit_stun_until = max(self.hit_stun_until, self.stagger_until)
            self.attacking = False
            self.dash_kind = None
            self.dash_until = 0
            self.recovery_until = self.stagger_until
        if oyuncudan and not eski_aggro and self.tur == "berserker":
            self.last_pressure_ms = simdi
            self.next_chase_dash_ms = simdi + random.randint(
                int(self.cfg["chase_dash_min_wait_ms"]),
                int(self.cfg["chase_dash_max_wait_ms"]),
            )
        if bool(getattr(kaynak, "is_player_magic", False)):
            sx, sy = (
                float(getattr(kaynak, "x", oyuncu_x)),
                float(getattr(kaynak, "y", oyuncu_y)),
            )
        else:
            sx, sy = (
                (oyuncu_x, oyuncu_y)
                if oyuncudan
                else (
                    float(getattr(kaynak, "x", self.x)),
                    float(getattr(kaynak, "y", self.y)),
                )
            )
        darbe_profili = darbe_profili_belirle(kaynak, self.tur)
        kanli_darbe_efekti(
            self.x,
            self.y - 9.0,
            darbe_profili,
            lethal=self.hp <= 0,
            yon=pygame.Vector2(self.x - sx, self.y - sy),
        )
        itme = pygame.Vector2(self.x - sx, self.y - sy)
        if itme.length_squared() > 0.001:
            taban = {
                "crawler": 82.0,
                "berserker": 50.0,
                "headsthrower": 72.0,
                "tarkard": 27.0,
                "torrmund": 18.0,
            }.get(self.tur, 46.0)
            if simdi < self.stagger_until:
                taban *= 1.45
            itme = itme.normalize() * taban
            self.vx += itme.x
            self.vy += itme.y
        self.nav_next_replan_ms = 0
        if oyuncudan:
            dunya_olayi_kaydet(
                "hit_given",
                damage=miktar,
                count=1,
                enemy=self.tur,
            )
            bildirim_goster(
                bt(
                    f"{self.name} -{miktar} hasar aldı.",
                    f"{self.name} took -{miktar} damage.",
                ),
                PARLAK_KIRMIZI,
            )
            oyuncu_heavy = (
                karakter_cinsiyet == "male" and oyuncu_saldiri_modu == "hold_release"
            )
            impact_turu = "slash_heavy" if oyuncu_heavy else "slash"
            combat_impact_spawn(
                self.x,
                self.y - 14,
                impact_turu,
                min(2.4, 0.8 + miktar / 90.0),
                pygame.Vector2(self.x - sx, self.y - sy),
            )
            if oyuncu_heavy:
                kamera_hit_sarsintisi_baslat(5.8, 150)
        else:
            dunya_olayi_kaydet(
                "friendly_fire",
                damage=miktar,
                source=str(getattr(kaynak, "tur", "enemy")),
                target=self.tur,
            )
            combat_impact_spawn(
                self.x,
                self.y - 13,
                combat_darbe_turu(getattr(kaynak, "tur", "enemy")),
                min(2.4, 0.8 + miktar / 80.0),
                pygame.Vector2(self.x - sx, self.y - sy),
            )
            self.aggro = eski_aggro or self.tur == "headsthrower"
        if self.hp <= 0:
            self.active = False
            self.attacking = False
            self.dash_until = 0
            self.dash_kind = None
            self.vx = self.vy = 0.0
            if oyuncudan:
                bildirim_goster(
                    bt(
                        f"{self.name} yenildi.",
                        f"{self.name} defeated.",
                    ),
                    SARI,
                )
        return miktar

    def _attack_frames(self):
        if self.tur == "crawler":
            return COMMON_ENEMY_SPRITELERI["crawler"].get("attack", [])
        return (
            COMMON_ENEMY_SPRITELERI["berserker"]
            .get("attack", {})
            .get(self.visual_direction, [])
        )

    def _attack_frame_index(self, simdi):
        kareler = self._attack_frames()
        if not kareler:
            return 0
        gecen = max(0, simdi - self.attack_started_ms)
        return min(
            len(kareler) - 1,
            int(gecen // int(self.cfg["attack_frame_ms"])),
        )

    def _attack_total_ms(self):
        return max(1, len(self._attack_frames())) * int(self.cfg["attack_frame_ms"])

    def _attack_rect(self):
        r = self.collision_rect()
        yarim_w = int(self.cfg["attack_half_width"])
        yarim_h = int(self.cfg["attack_half_height"])
        merkez_x, merkez_y = r.center

        if self.tur == "crawler":
            if self.direction == "left":
                return pygame.Rect(
                    merkez_x - yarim_w * 2,
                    merkez_y - yarim_h,
                    yarim_w * 2,
                    yarim_h * 2,
                )
            return pygame.Rect(
                merkez_x,
                merkez_y - yarim_h,
                yarim_w * 2,
                yarim_h * 2,
            )
        if self.direction == "left":
            return pygame.Rect(
                merkez_x - yarim_w * 2,
                merkez_y - yarim_h,
                yarim_w * 2,
                yarim_h * 2,
            )
        if self.direction == "right":
            return pygame.Rect(
                merkez_x,
                merkez_y - yarim_h,
                yarim_w * 2,
                yarim_h * 2,
            )
        if self.direction == "up":
            return pygame.Rect(
                merkez_x - yarim_h,
                merkez_y - yarim_w * 2,
                yarim_h * 2,
                yarim_w * 2,
            )
        return pygame.Rect(
            merkez_x - yarim_h,
            merkez_y,
            yarim_h * 2,
            yarim_w * 2,
        )

    def _attack_active_frame_araligi(self):
        """Sprite zincirine göre gerçek active frame penceresi.

        Eski sistem yalnız impact frame'in ilk görüldüğü milisaniyede temas test
        ediyordu. 60 FPS / hareketli hedefte kılıç görsel olarak gövdeden geçse bile
        hasar kaçabiliyordu. Artık swing birkaç frame boyunca fiziksel olarak aktif.
        """
        if self.tur == "crawler":
            # Kaynak sheet'te gerçek temas yalnız ikinci satırın ortasındaki büyük
            # rüzgâr/pençe yayıdır (attack sequence raw index 12). Hazırlık ve
            # recovery kareleri artık hasar vermez.
            return (12, 12)
        if self.tur == "berserker":
            return (1, 3)
        variant = getattr(self, "attack_variant", "")
        if self.tur == "tarkard":
            return (3, 6) if variant == "whirl" else (2, 4)
        if self.tur == "torrmund":
            return (2, 5) if variant == "cleave" else (3, 5)
        impact = int(self.cfg.get("attack_impact_frame", 1))
        return (max(0, impact - 1), impact + 1)

    def _melee_contact_gap(self, baslangic=False):
        """Görsel melee için maksimum fiziksel kenar boşluğu.

        `attack_range` AI'nın ne zaman saldırı hazırlayabileceğini söyler; hasarın
        gerçekten bağlanması ise bu çok daha sıkı contact gate'ten geçer. Böylece
        büyük sprite/arc değerleri hiçbir düşmana uzaktan görünmez vuruş vermez.
        """
        anahtar = "attack_start_contact_gap" if baslangic else "attack_contact_gap"
        varsayilan = 24.0 if self.tur == "berserker" else 18.0
        return float(
            self.cfg.get(
                anahtar,
                self.cfg.get("attack_contact_gap", varsayilan),
            )
        )

    def _attack_contact_gate(self, baslangic=False):
        """Saldırı kökü ile oyuncu gövdesi arasında makul yakınlık ve ön-yüz şartı.

        V9'daki foot-rect -> torso-rect edge gap, farklı boydaki sprite'larda gerçek
        teması reddedebiliyordu: ayak collision'ı geride kalırken ekrandaki el/kılıç
        oyuncuya çoktan değmiş olabiliyordu. V10 gate'i yalnız *imkânsız uzaktan*
        darbeyi keser. Asıl hit kararı aşağıdaki fiziksel capsule/sweep kesişimidir.
        """
        hurt = oyuncu_savas_hurtbox_rect(oyuncu_x, oyuncu_y)
        body_h = float(self.cfg.get("body_height", 22))
        origin = pygame.Vector2(float(self.x), float(self.y) - body_h * 0.64)
        yakin = _rect_en_yakin_nokta(hurt, origin)
        root_dist = origin.distance_to(yakin)

        limitler = {
            "crawler": (66.0, 76.0),
            "berserker": (68.0, 80.0),
            "tarkard": (96.0, 108.0),
            "torrmund": (88.0, 98.0),
        }
        aktif_limit, bas_limit = limitler.get(self.tur, (76.0, 88.0))
        if root_dist > (bas_limit if baslangic else aktif_limit):
            return False

        variant = getattr(self, "attack_variant", "")
        if self.tur == "tarkard" and variant == "whirl":
            return True

        facing = _common_enemy_yon_vektoru(self.direction)
        if facing.length_squared() <= 1e-6:
            return False
        facing = facing.normalize()
        fark = pygame.Vector2(hurt.center) - origin
        if fark.length_squared() <= 1e-6:
            return True
        # Başlatma cone'u okunabilir olsun; active sweep ise yan tarafta gerçekten
        # değen kol/kılıcı kaçırmamak için daha affedicidir.
        dot = facing.dot(fark.normalize())
        return dot >= (0.02 if baslangic else -0.18)

    def _attack_baslatma_temasi_var_mi(self):
        return self._attack_contact_gate(baslangic=True)

    def _attack_temas_var_mi(self, simdi):
        """Görsel swing'e yaklaşık capsule/arc teması.

        Amaç hasarı büyütmek değil, ekrandaki silahın oyuncuya değdiği an ile
        collision sonucunu aynılaştırmaktır. Duvar LOS'u ayrıca çağıran tarafta
        korunur. Yön saldırı başında kilitlendiği için input-reading yapılmaz.
        """
        # hiçbir melee saldırı yalnız büyük sprite/capsule menzili yüzünden
        # uzaktan bağlanamaz. Önce gerçek body-to-hurtbox temas mesafesi geçmelidir.
        if not self._attack_contact_gate(baslangic=False):
            return False

        hurt = oyuncu_savas_hurtbox_rect(oyuncu_x, oyuncu_y)
        govde = self.collision_rect()
        if govde.inflate(12, 18).colliderect(hurt):
            return True

        facing = _common_enemy_yon_vektoru(self.direction)
        if facing.length_squared() <= 1e-6:
            facing = pygame.Vector2(1.0, 0.0)
        facing = facing.normalize()
        origin = pygame.Vector2(
            self.x,
            self.y - float(self.cfg.get("body_height", 20)) * 0.62,
        )

        frame = self._attack_frame_index(simdi)
        active_start, active_end = self._attack_active_frame_araligi()
        span = max(1.0, float(active_end - active_start + 1))
        p = max(0.0, min(1.0, (frame - active_start + 0.5) / span))

        variant = getattr(self, "attack_variant", "")
        if self.tur == "crawler":
            reach, radius, sweep = (
                62.0,
                18.0,
                (-11.0, 0.0, 11.0),
            )
        elif self.tur == "berserker":
            reach, radius = 64.0, 21.0
            merkez_aci = -48.0 + 92.0 * p
            sweep = (
                merkez_aci - 12.0,
                merkez_aci,
                merkez_aci + 12.0,
            )
        elif self.tur == "tarkard" and variant == "whirl":
            # Dairesel saldırıda kılıcın bütün 360° izi vardır fakat iç yarıçap
            # küçük tutulur; çok uzaktaki hedefe görünmez hasar vermez.
            merkez = pygame.Vector2(hurt.center)
            return origin.distance_to(merkez) <= 78.0
        elif self.tur == "tarkard":
            reach, radius = 90.0, 26.0
            merkez_aci = -34.0 + 66.0 * p
            sweep = (
                merkez_aci - 10.0,
                merkez_aci,
                merkez_aci + 10.0,
            )
        elif self.tur == "torrmund" and variant == "cleave":
            reach, radius = 90.0, 20.0
            merkez_aci = -24.0 + 48.0 * p
            sweep = (
                merkez_aci - 9.0,
                merkez_aci,
                merkez_aci + 9.0,
            )
        elif self.tur == "torrmund":
            reach, radius = 96.0, 19.0
            merkez_aci = -42.0 + 82.0 * p
            sweep = (
                merkez_aci - 11.0,
                merkez_aci,
                merkez_aci + 11.0,
            )
        else:
            reach = float(self.cfg.get("attack_range", 70.0))
            radius = 20.0
            sweep = (0.0,)

        for aci in sweep:
            yon = facing.rotate(aci)
            # Silah izi gövdeden biraz ileride başlar; arkadaki oyuncuyu yanlışlıkla
            # kesmez, fakat çok yakın temasta yukarıdaki body overlap devreye girer.
            bas = origin + yon * 10.0
            son = origin + yon * reach
            if _kapsul_rect_kesisiyor(hurt, bas, son, radius):
                return True
        return False

    def _saldiri_baslat(self, simdi):
        self.attacking = True
        self.attack_started_ms = simdi
        self.last_attack_ms = simdi
        if self.tur == "berserker":
            jitter = int(self.cfg.get("attack_cooldown_jitter_ms", 0))
            self.next_attack_variance_ms = (
                random.randint(-jitter, jitter) if jitter > 0 else 0
            )
            self.pressure_commit_until = 0
        self.attack_damage_applied = False
        self.attack_connected = False
        self.attack_friendly_hits.clear()
        self.dash_until = 0
        self.dash_kind = None
        # Attack yönü burada kilitlenir. Animasyon boyunca hedefin yanına geçmesi
        # sprite'ın vuruş ortasında 180° dönmesine neden olmaz.
        fark = pygame.Vector2(oyuncu_x - self.x, oyuncu_y - self.y)
        self._yonleri_hareketten_guncelle(fark, zorla=True)
        self.vx *= 0.22
        self.vy *= 0.22
        dunya_olayi_kaydet("enemy_attack", enemy=self.tur)

    def _saldiri_guncelle(self, simdi):
        global oyuncu_hp
        if not self.attacking:
            return False

        kare = self._attack_frame_index(simdi)
        aktif_bas, aktif_son = self._attack_active_frame_araligi()

        # Temas tek bir milisaniyeye indirgenmez. Active frame penceresinin her
        # render tick'inde, yalnız henüz bağlanmadıysa fiziksel swing sınanır.
        if aktif_bas <= kare <= aktif_son:
            enemy_friendly_melee_vur(self, simdi)
        if aktif_bas <= kare <= aktif_son and not self.attack_connected:
            if self._attack_temas_var_mi(simdi):
                los = common_enemy_saldiri_los_acik_mi(self)
                if los and oyuncu_hp > 0:
                    if oyuncu_savunma_darbe_karsila(self.tur, self.x, self.y, self):
                        self.attack_connected = True
                        self.attack_damage_applied = True
                        self.last_pressure_ms = simdi
                    else:
                        profil = darbe_profili_belirle(self, "player")
                        hasar = int(self.cfg["attack_damage"])
                        if profil == "heavy_slash":
                            hasar = max(
                                hasar,
                                int(
                                    math.ceil(
                                        float(oyuncu_max_hp)
                                        * AGIR_KESICI_MIN_MAX_HP_ORANI
                                    )
                                ),
                            )
                        oyuncu_hp = max(0, oyuncu_hp - hasar)
                        oyuncu_kanli_hasar_kaydi(
                            self.x,
                            self.y,
                            profil,
                            hasar,
                            self.name,
                        )
                        self.attack_connected = True
                        self.attack_damage_applied = True
                        self.last_pressure_ms = simdi
                        dunya_olayi_kaydet(
                            "hit_taken",
                            damage=hasar,
                            count=1,
                            enemy=self.tur,
                        )
                        combat_impact_spawn(
                            oyuncu_x,
                            oyuncu_y - 12,
                            combat_darbe_turu(self.tur),
                            1.35 if self.tur == "berserker" else 1.0,
                            pygame.Vector2(
                                oyuncu_x - self.x,
                                oyuncu_y - self.y,
                            ),
                        )
                        kamera_hit_sarsintisi_baslat(
                            5.8 if self.tur == "berserker" else 3.4,
                            190,
                        )
                        bildirim_goster(
                            bt(
                                f"{self.name} sana -{hasar} hasar verdi.",
                                f"{self.name} dealt -{hasar} damage.",
                            ),
                            PARLAK_KIRMIZI,
                        )

        if kare > aktif_son:
            self.attack_damage_applied = True

        if simdi - self.attack_started_ms >= self._attack_total_ms():
            self.attacking = False
            self.attack_damage_applied = False
            recovery = int(self.cfg.get("attack_recovery_ms", 180))
            # Miss biraz daha okunabilir punish window bırakır.
            if not self.attack_connected:
                recovery = int(recovery * (1.14 if self.tur == "berserker" else 1.08))
                if self.tur == "berserker":
                    self.post_miss_reposition_until = simdi + int(
                        self.cfg.get("post_miss_reposition_ms", 520)
                    )
                    self.orbit_sign *= -1.0
            self.recovery_until = simdi + recovery
        return True

    def _attack_los_cached(self, simdi):
        enemy_p = pygame.Vector2(self.x, self.y)
        player_p = pygame.Vector2(oyuncu_x, oyuncu_y)
        ttl = 58 if self.tur == "berserker" else 76
        if (
            simdi < self.attack_los_until
            and (enemy_p - self.attack_los_enemy_pos).length_squared() < 81.0
            and (player_p - self.attack_los_player_pos).length_squared() < 81.0
        ):
            return self.attack_los_value
        self.attack_los_value = common_enemy_saldiri_los_acik_mi(self, adim=5.0)
        self.attack_los_until = simdi + ttl
        self.attack_los_enemy_pos = enemy_p
        self.attack_los_player_pos = player_p
        return self.attack_los_value

    def _separation(self, digerler):
        kuvvet = pygame.Vector2(0.0, 0.0)
        yaricap = float(self.cfg["separation_radius"])
        for diger in digerler:
            if diger is self or not getattr(diger, "active", False):
                continue
            fark = pygame.Vector2(self.x - diger.x, self.y - diger.y)
            d2 = fark.length_squared()
            if d2 <= 0.0001 or d2 >= yaricap * yaricap:
                continue
            d = math.sqrt(d2)
            agirlik = (1.0 - d / yaricap) ** 2
            kuvvet += (fark / d) * agirlik * float(self.cfg["separation_strength"])
        return kuvvet

    def _hareket_gecerli(self, yeni_x, yeni_y, digerler, oyuncuyu_engel_say=True):
        if not common_enemy_statik_konum_gecerli_mi(
            self.tur, yeni_x, yeni_y, navigation=False
        ):
            return False
        if not _common_enemy_dinamik_rect_gecerli(
            self, yeni_x, yeni_y, digerler, oyuncuyu_engel_say
        ):
            return False
        return True

    def _lokal_aciklik(self, nokta):
        """Navigation clearance cache'inden ucuz 0..1 lokal açıklık ölçüsü."""
        p = pygame.Vector2(nokta)
        h = (
            int(p.x // COMMON_ENEMY_NAV_GRID),
            int(p.y // COMMON_ENEMY_NAV_GRID),
        )
        return max(
            0.0,
            min(
                1.0,
                _common_enemy_hucre_clearance(self.tur, h) / 3.0,
            ),
        )

    def _fire_ai_profile(self):
        return FIRE_ENEMY_AI.get(self.tur, FIRE_ENEMY_AI["crawler"])

    def _fire_nokta_tehlikeli_mi(self, nokta, margin=0.0):
        """Local steering probe'un aktif alevin içine rota seçmesini engeller."""
        if not player_magic_ground_fires:
            return False
        p = pygame.Vector2(nokta)
        limit = float(FIRE_MAGIC_GROUND_FIRE_TOUCH_RADIUS) + float(margin)
        limit2 = limit * limit
        for patch in player_magic_ground_fires:
            if not getattr(patch, "active", False):
                continue
            dx = p.x - float(patch.x)
            dy = p.y - float(patch.y)
            if dx * dx + dy * dy <= limit2:
                return True
        return False

    def _fire_ground_tehdit_vektoru(self, simdi):
        """Yakın ground-fire kümesinden ağırlıklı kaçış vektörü ve güven skoru."""
        if not player_magic_ground_fires:
            return None
        profil = self._fire_ai_profile()
        radius = float(profil.get("ground_radius", 0.0))
        if radius <= 0.0:
            return None
        here = pygame.Vector2(self.x, self.y)
        itme = pygame.Vector2(0.0, 0.0)
        en_yakin = 10**9
        adet = 0
        for patch in player_magic_ground_fires:
            if not getattr(patch, "active", False):
                continue
            q = pygame.Vector2(float(patch.x), float(patch.y))
            fark = here - q
            d2 = fark.length_squared()
            if d2 > radius * radius:
                continue
            d = math.sqrt(max(0.0001, d2))
            en_yakin = min(en_yakin, d)
            adet += 1
            if d <= 0.5:
                # Tam merkezin üstünde deterministik ama uid'e göre farklı yön.
                seed = (sum(ord(c) for c in self.uid) * 37 + int(simdi // 100)) % 360
                yon = pygame.Vector2(1.0, 0.0).rotate(seed)
            else:
                yon = fark / d
            w = ((radius - d) / max(1.0, radius)) ** 1.55
            itme += yon * (0.35 + w * 1.65)
        if adet <= 0 or itme.length_squared() <= 1e-6:
            return None
        return itme.normalize(), float(en_yakin), int(adet)

    def _fire_ground_kacis_hedefi_sec(self, simdi, digerler, kacis_yonu):
        """Dusman turune gore farkli, fakat hep alev-disinda kalan kacis hedefi."""
        here = pygame.Vector2(self.x, self.y)
        player = pygame.Vector2(oyuncu_x, oyuncu_y)
        profil = self._fire_ai_profile()
        style = str(profil.get("ground_style", "skittish"))
        dist = float(profil.get("ground_distance", 78.0))
        dist = max(52.0, min(122.0, dist))

        # Crawler daha kirik/organik acilar dener; agir siniflar en kisa guvenli
        # cizgiyi tercih eder. Heads Thrower ise ranged bandini koruyan noktayi arar.
        if style == "skittish":
            acilar = (0, 20, -20, 42, -42, 68, -68, 96, -96)
        elif style == "pressure":
            acilar = (0, 18, -18, 36, -36, 58, -58, 82, -82)
        elif style == "ranged":
            acilar = (0, 24, -24, 48, -48, 72, -72, 104, -104)
        else:
            acilar = (0, 16, -16, 32, -32, 52, -52, 76, -76)

        adaylar = []
        for aci in acilar:
            yon = pygame.Vector2(kacis_yonu).rotate(aci)
            if yon.length_squared() <= 1e-6:
                continue
            yon = yon.normalize()
            p = here + yon * dist
            if not self._hareket_gecerli(p.x, p.y, digerler, oyuncuyu_engel_say=False):
                continue
            if self._fire_nokta_tehlikeli_mi(
                p, margin=FIRE_AI_GROUND_HARD_MARGIN + 7.0
            ):
                continue

            min_fire = 9999.0
            for patch in player_magic_ground_fires:
                if getattr(patch, "active", False):
                    min_fire = min(
                        min_fire,
                        p.distance_to((float(patch.x), float(patch.y))),
                    )
            aciklik = self._lokal_aciklik(p)
            player_dist = p.distance_to(player)
            skor = min_fire * 0.74 + aciklik * 34.0

            if style == "skittish":
                # Duvara yapismak yerine acik yan cikis; ayni turde herkes birebir
                # ayni yonde kacmasin diye cok kucuk karar gurultusu.
                skor += 10.0 if 18 <= abs(aci) <= 70 else 0.0
                skor -= abs(aci) * 0.035
                skor += random.uniform(-2.5, 2.5)
            elif style == "pressure":
                # Alevden kesinlikle cik, ama mumkunse oyuncuyla temas mesafesini
                # gereksiz yere acma. Berserker'in karakteri baskidir.
                skor -= player_dist * 0.055
                skor -= abs(aci) * 0.045
            elif style == "ranged":
                preferred = float(self.cfg.get("ranged_preferred", 260.0))
                skor -= abs(player_dist - preferred) * 0.22
                skor += aciklik * 18.0
            elif style == "tank":
                # Tarkard paniklemez: en direkt, fiziksel olarak saglam cikisi alir.
                skor -= abs(aci) * 0.13
                skor += aciklik * 12.0
            elif style == "tank_guard":
                # Torrmund daha da muhafazakar; duvar/alev arasina sikismayacak
                # acik zemini, sonra en kisa sapmayi tercih eder.
                skor += aciklik * 28.0
                skor -= abs(aci) * 0.15

            adaylar.append((skor, p))

        if not adaylar:
            return here + pygame.Vector2(kacis_yonu) * min(42.0, dist)
        adaylar.sort(key=lambda item: item[0], reverse=True)
        if style == "skittish" and len(adaylar) > 1 and random.random() < 0.22:
            return pygame.Vector2(adaylar[1][1])
        return pygame.Vector2(adaylar[0][1])

    def _fire_projectile_tehdit(self):
        """En yakın gerçek uçuş-koridoru tehdidini (projectile, tti, lateral) döndürür."""
        profil = self._fire_ai_profile()
        awareness = float(profil.get("projectile_awareness", 0.0))
        if awareness <= 0.0 or not player_magic_projectiles:
            return None
        here = pygame.Vector2(self.x, self.y - 7.0)
        best = None
        own_r = _magic_hedef_yaricapi(self)
        corridor = (
            own_r
            + float(FIRE_MAGIC_PROJECTILE_RADIUS)
            + FIRE_AI_PROJECTILE_CORRIDOR_MARGIN
        )
        for projectile in player_magic_projectiles:
            if not getattr(projectile, "active", False):
                continue
            pos = pygame.Vector2(float(projectile.x), float(projectile.y))
            direction = pygame.Vector2(getattr(projectile, "direction", (0.0, 0.0)))
            if direction.length_squared() <= 1e-6:
                continue
            direction = direction.normalize()
            rel = here - pos
            along = rel.dot(direction)
            if along < 4.0 or along > awareness:
                continue
            lateral_v = rel - direction * along
            lateral = lateral_v.length()
            if lateral > corridor:
                continue
            speed = max(
                1.0,
                pygame.Vector2(
                    getattr(
                        projectile,
                        "v",
                        direction * FIRE_MAGIC_PROJECTILE_SPEED,
                    )
                ).length(),
            )
            tti = along / speed
            # Çok uzaktaki teorik çizgiye değil, 0.75 s içindeki gerçek tehdide tepki.
            if tti > 0.78:
                continue
            score = tti + lateral / max(1.0, corridor) * 0.12
            if best is None or score < best[0]:
                best = (
                    score,
                    projectile,
                    tti,
                    lateral,
                    direction,
                )
        return None if best is None else best[1:]

    def _fire_dash_baslat(self, simdi, digerler, projectile, projectile_dir):
        profil = self._fire_ai_profile()
        # yalniz Crawler ve Berserker projectile dodge yapabilir.
        if not bool(profil.get("projectile_dash", False)):
            return False
        if simdi < self.fire_dash_cooldown_until:
            return False
        if self.attacking or simdi < self.stagger_until or simdi < self.hit_stun_until:
            return False
        chance = float(profil.get("projectile_chance", 0.0))
        if chance <= 0.0 or random.random() >= chance:
            self.fire_projectile_ignore_until = simdi + 420
            return False

        here = pygame.Vector2(self.x, self.y)
        d = pygame.Vector2(projectile_dir)
        if d.length_squared() <= 1e-6:
            return False
        d = d.normalize()
        lateral = pygame.Vector2(-d.y, d.x)
        dash_dist = float(profil.get("dash_distance", 0.0))
        dash_ms = int(profil.get("dash_ms", 0))
        if dash_dist <= 1.0 or dash_ms <= 0:
            return False

        proj_pos = pygame.Vector2(float(projectile.x), float(projectile.y))
        adaylar = []
        for sign in (-1.0, 1.0):
            # Kisa ve smooth dash: saf 90 derece robot hareketi yerine az miktarda
            # geriye kavis. Berserker biraz daha ileri-baski karakterini korur.
            back = (
                random.uniform(0.035, 0.11)
                if self.tur == "berserker"
                else random.uniform(0.07, 0.15)
            )
            yon = lateral * sign - d * back
            if yon.length_squared() <= 1e-6:
                continue
            yon = yon.normalize()
            end = here + yon * dash_dist
            gecis = True
            for oran in (0.25, 0.50, 0.75, 1.0):
                q = here + yon * dash_dist * oran
                if not self._hareket_gecerli(
                    q.x, q.y, digerler, oyuncuyu_engel_say=False
                ):
                    gecis = False
                    break
                if self._fire_nokta_tehlikeli_mi(q, margin=FIRE_AI_GROUND_HARD_MARGIN):
                    gecis = False
                    break
            if not gecis:
                continue
            rel = end - proj_pos
            along = rel.dot(d)
            closest = proj_pos + d * max(0.0, along)
            line_clear = end.distance_to(closest)
            skor = line_clear + self._lokal_aciklik(end) * 25.0
            # Berserker acik alanda oyuncuya daha yakin biten tarafi hafifce sever.
            if self.tur == "berserker":
                skor -= end.distance_to((oyuncu_x, oyuncu_y)) * 0.025
            adaylar.append((skor, yon))

        if not adaylar:
            self.fire_projectile_ignore_until = simdi + 250
            return False
        adaylar.sort(key=lambda item: item[0], reverse=True)
        sec = adaylar[1] if len(adaylar) > 1 and random.random() < 0.16 else adaylar[0]
        yon = pygame.Vector2(sec[1])

        self.fire_dash_started_ms = int(simdi)
        self.fire_dash_duration_ms = int(dash_ms)
        self.fire_dash_until = int(simdi) + int(dash_ms)
        self.fire_dash_direction = yon
        self.fire_dash_distance_total = float(dash_dist)
        self.fire_dash_last_ease = 0.0
        # velocity sadece facing/animasyon icin ilk tahmini tasir; gercek hareket
        # asagidaki smoothstep konum integrasyonudur.
        nominal_speed = dash_dist / max(0.001, dash_ms / 1000.0)
        self.fire_dash_velocity = yon * nominal_speed
        self.fire_dash_cooldown_until = simdi + int(
            profil.get("dash_cooldown_ms", 1200)
        )
        self.fire_projectile_pending_id = None
        self.fire_projectile_react_at = 0
        self.dash_kind = None
        self.dash_until = 0
        self.evade_target = None
        self.evade_until = 0
        if hasattr(self, "ranged_state"):
            self.ranged_state = "idle"
        self._yonleri_hareketten_guncelle(yon, zorla=True)
        return True

    def _fire_dash_guncelle(self, dt, simdi, digerler):
        if self.fire_dash_until <= 0:
            return False
        if simdi >= self.fire_dash_until or self.fire_dash_duration_ms <= 0:
            self.fire_dash_until = 0
            self.fire_dash_started_ms = 0
            self.fire_dash_last_ease = 0.0
            self.fire_dash_velocity *= 0.18
            self.vx *= 0.38
            self.vy *= 0.38
            self.recovery_until = max(self.recovery_until, simdi + 70)
            return False

        p = max(
            0.0,
            min(
                1.0,
                (simdi - self.fire_dash_started_ms)
                / max(1.0, float(self.fire_dash_duration_ms)),
            ),
        )
        # smoothstep: baslangic ve bitiste hiz sifira yaklasir. Kisa dodge hizli
        # gorunur fakat teleport veya sabit-hiz kayma hissi vermez.
        ease = p * p * (3.0 - 2.0 * p)
        delta_ease = max(0.0, ease - float(self.fire_dash_last_ease))
        self.fire_dash_last_ease = ease
        step = self.fire_dash_direction * (self.fire_dash_distance_total * delta_ease)
        if step.length_squared() <= 1e-8:
            return True

        target = pygame.Vector2(self.x, self.y) + step
        moved = self._hareketi_uygula(
            step.x,
            step.y,
            digerler,
            target,
            oyuncuyu_engel_say=False,
        )
        approx_dt = max(1.0 / 240.0, float(dt))
        velocity = step / approx_dt
        self.vx, self.vy = velocity.x, velocity.y
        self.fire_dash_velocity = velocity
        self._yonleri_hareketten_guncelle(self.fire_dash_direction, zorla=True)
        if moved < max(0.22, step.length() * 0.18):
            self.fire_dash_until = simdi
        return True

    def _fire_ai_guncelle(self, dt, simdi, digerler):
        """V38 projectile reflex + tur-bazli ground-fire avoidance.

        Yalniz Crawler/Berserker fireball'a short dash atar. Tum turler ise alev
        zemininin icine girdiklerinde mevcut commitment'i bozup cikmayi dener.
        """
        if self._fire_dash_guncelle(dt, simdi, digerler):
            return True

        profil = self._fire_ai_profile()
        projectile_dash = bool(profil.get("projectile_dash", False))
        committed = bool(
            self.attacking
            or (
                hasattr(self, "ranged_state")
                and self.ranged_state in ("pickup", "throw")
            )
        )

        if simdi >= self.fire_ai_next_scan_ms:
            self.fire_ai_next_scan_ms = (
                simdi + FIRE_AI_SCAN_MS + (sum(ord(c) for c in self.uid) % 27)
            )

            # Fireball reflex sadece hafif/orta mobil siniflara ait.
            if (
                projectile_dash
                and not committed
                and simdi >= self.fire_projectile_ignore_until
            ):
                threat = self._fire_projectile_tehdit()
                if threat is not None:
                    projectile, tti, lateral, direction = threat
                    pid = id(projectile)
                    if self.fire_projectile_pending_id != pid:
                        lo, hi = profil.get("reaction_ms", (120, 220))
                        urgency = max(
                            0.0,
                            min(1.0, (0.46 - float(tti)) / 0.46),
                        )
                        delay = random.randint(int(lo), int(hi))
                        delay = max(
                            48,
                            int(delay * (1.0 - urgency * 0.34)),
                        )
                        self.fire_projectile_pending_id = pid
                        self.fire_projectile_react_at = simdi + delay
                        self.fire_last_threat_id = pid
                    elif simdi >= self.fire_projectile_react_at:
                        if self._fire_dash_baslat(
                            simdi,
                            digerler,
                            projectile,
                            direction,
                        ):
                            return True
                        self.fire_projectile_pending_id = None
                        self.fire_projectile_react_at = 0
                else:
                    self.fire_projectile_pending_id = None
                    self.fire_projectile_react_at = 0
            elif not projectile_dash:
                # Heavy/ranged siniflarda eski pending dodge state'i tasinmasin.
                self.fire_projectile_pending_id = None
                self.fire_projectile_react_at = 0

            ground = self._fire_ground_tehdit_vektoru(simdi)
            if ground is not None:
                kacis_yonu, en_yakin, adet = ground
                radius = float(profil.get("ground_radius", 110.0))
                panic_limit = float(FIRE_MAGIC_GROUND_FIRE_TOUCH_RADIUS) + float(
                    profil.get("ground_panic_margin", 8.0)
                )
                alevin_icinde = en_yakin <= panic_limit

                # Yakindaki alev yuzunden her swing'i sihirli bicimde iptal etmezler;
                # ama alev gercekten bedenlerine degiyorsa tum siniflar hayatta kalma
                # refleksiyle commitment'i keser. Tarkard/Torrmund dahi projectile'dan
                # kacmazken yanmakta olduklari zeminde durmaz.
                if alevin_icinde and committed:
                    self.attacking = False
                    self.attack_damage_applied = True
                    self.recovery_until = min(
                        max(self.recovery_until, simdi + 55),
                        simdi + 120,
                    )
                    if hasattr(self, "ranged_state"):
                        self.ranged_state = "idle"
                    committed = False

                if en_yakin <= radius and (not committed or alevin_icinde):
                    self.fire_avoid_target = self._fire_ground_kacis_hedefi_sec(
                        simdi, digerler, kacis_yonu
                    )
                    self.fire_avoid_until = simdi + int(
                        profil.get("ground_hold_ms", 360)
                    )
                    self.nav_next_replan_ms = 0
                    self.local_plan_until = 0

        if (
            committed
            or self.fire_avoid_target is None
            or simdi >= self.fire_avoid_until
        ):
            if simdi >= self.fire_avoid_until:
                self.fire_avoid_target = None
            return False

        here = pygame.Vector2(self.x, self.y)
        target = pygame.Vector2(self.fire_avoid_target)
        vec = target - here
        if vec.length_squared() < 8.0 * 8.0:
            self.fire_avoid_target = None
            return False
        direction = vec.normalize()
        speed = self._anlik_move_speed() * float(profil.get("ground_speed_mul", 1.15))
        target_vel = direction * speed
        target_vel += self._separation(digerler) * 0.28
        target_vel = _vektor_uzunluk_sinirla(target_vel, speed)
        current = pygame.Vector2(self.vx, self.vy)

        # Hafif siniflar alevden daha hizli yon degistirir; tanklar panik halinde
        # kaymaz, agir ama kararlı bir sekilde guvenli zemine doner.
        style = str(profil.get("ground_style", "skittish"))
        response_k = {
            "skittish": 19.0,
            "pressure": 17.0,
            "ranged": 16.0,
            "tank": 11.5,
            "tank_guard": 10.5,
        }.get(style, 15.0)
        response = 1.0 - math.exp(-response_k * dt)
        accel_mul = {
            "skittish": 1.38,
            "pressure": 1.28,
            "ranged": 1.22,
            "tank": 0.94,
            "tank_guard": 0.88,
        }.get(style, 1.15)
        dv = _vektor_uzunluk_sinirla(
            (target_vel - current) * response,
            float(self.cfg["acceleration"]) * accel_mul * dt,
        )
        current += dv
        self.vx, self.vy = current.x, current.y
        self._yonleri_hareketten_guncelle(current, zorla=True)
        self._hareketi_uygula(
            self.vx * dt,
            self.vy * dt,
            digerler,
            target,
            oyuncuyu_engel_say=False,
        )
        return True

    def _candidate_velocity(
        self,
        istenen_yon,
        hiz,
        hedef,
        digerler,
        simdi=None,
        force=False,
    ):
        """
        V6 adaptive local planner.

        Açık arazide tek bir cached straight-ahead testi yeterlidir. Engel çevresinde
        aday açı sayısı otomatik yükselir. Karar multi-rate cache'de tutulduğu için
        60 FPS fizik korunurken pahalı geometrik düşünme 14-20 Hz civarında kalır.
        """
        if simdi is None:
            simdi = pygame.time.get_ticks()
        istenen = pygame.Vector2(istenen_yon)
        if istenen.length_squared() <= 1e-6 or hiz <= 0.01:
            return pygame.Vector2(0.0, 0.0)
        istenen = istenen.normalize()
        hedef_v = pygame.Vector2(hedef)

        cache_uygun = (
            not force
            and simdi < self.local_plan_until
            and self.local_plan_input_dir.length_squared() > 0.5
            and self.local_plan_input_dir.dot(istenen) > 0.90
            and self.local_plan_target.distance_squared_to(hedef_v) < 48.0 * 48.0
            and self.stuck_ms < 180.0
        )
        if cache_uygun:
            if self.local_plan_output_dir.length_squared() <= 1e-6:
                return pygame.Vector2(0.0, 0.0)
            return self.local_plan_output_dir * hiz * self.local_plan_speed_ratio

        bas = pygame.Vector2(self.x, self.y)
        mevcut = pygame.Vector2(self.vx, self.vy)
        onceki_mesafe = bas.distance_to(hedef_v)
        current_cell = (
            int(self.x // COMMON_ENEMY_NAV_GRID),
            int(self.y // COMMON_ENEMY_NAV_GRID),
        )
        aciklik0 = _common_enemy_hucre_clearance(self.tur, current_cell)

        # Açık alanda candidate fan açmaya gerek yok. Bir ileri probe + dynamic
        # occupancy, düz pursuit'in güvenli olup olmadığını belirler.
        probe = bas + istenen * min(68.0, max(26.0, hiz * 0.19))
        duz_guvenli = (
            aciklik0 >= 2.0
            and _common_enemy_hizli_statik_gecerli_mi(self.tur, probe.x, probe.y)
            and _common_enemy_dinamik_rect_gecerli(
                self, probe.x, probe.y, digerler, True
            )
            and not self._fire_nokta_tehlikeli_mi(
                probe, margin=FIRE_AI_GROUND_HARD_MARGIN
            )
        )
        if duz_guvenli:
            sonuc = istenen * hiz
        else:
            # Sıkışmaya yaklaştıkça açısal çözünürlük artar. Normal koşuda 5,
            # Problemli koridorda 9-11 yön yeterlidir; daha geniş örnekleme gereksiz maliyet yaratır.
            if self.stuck_ms > 180.0 or aciklik0 < 1.0:
                acilar = (
                    0,
                    14,
                    -14,
                    30,
                    -30,
                    48,
                    -48,
                    68,
                    -68,
                    92,
                    -92,
                )
            else:
                acilar = (0, 18, -18, 38, -38, 62, -62)

            en_iyi = None
            for derece in acilar:
                yon = istenen.rotate(derece)
                hiz_mul = (
                    1.0 if abs(derece) <= 38 else (0.88 if abs(derece) <= 68 else 0.72)
                )
                aday_v = yon * hiz * hiz_mul
                gecerli = True
                min_aciklik = 1.0
                dinamik_ceza = 0.0

                for ufuk in COMMON_ENEMY_LOCAL_HORIZONS:
                    pos = bas + aday_v * ufuk
                    if not _common_enemy_hizli_statik_gecerli_mi(
                        self.tur, pos.x, pos.y
                    ):
                        gecerli = False
                        break
                    if not _common_enemy_dinamik_rect_gecerli(
                        self, pos.x, pos.y, digerler, True
                    ):
                        dinamik_ceza += 1.0
                        if ufuk == COMMON_ENEMY_LOCAL_HORIZONS[0]:
                            gecerli = False
                            break
                    if self._fire_nokta_tehlikeli_mi(
                        pos, margin=FIRE_AI_GROUND_HARD_MARGIN
                    ):
                        gecerli = False
                        break
                    min_aciklik = min(min_aciklik, self._lokal_aciklik(pos))

                if not gecerli:
                    continue

                son = bas + aday_v * COMMON_ENEMY_LOCAL_HORIZONS[-1]
                ilerleme = onceki_mesafe - son.distance_to(hedef_v)
                alignment = istenen.dot(yon)
                inertia = (
                    mevcut.normalize().dot(yon)
                    if mevcut.length_squared() > 25.0
                    else 0.0
                )
                side_bonus = 0.0
                if derece != 0 and math.copysign(1.0, derece) == self.wall_follow_sign:
                    side_bonus = 0.05
                skor = (
                    ilerleme * 1.72
                    + alignment * 1.28
                    + inertia * 0.30
                    + min_aciklik * 1.10
                    + side_bonus
                    - abs(derece) * 0.0038
                    - dinamik_ceza * 1.55
                )
                if en_iyi is None or skor > en_iyi[0]:
                    en_iyi = (skor, aday_v)

            if en_iyi is not None:
                sonuc = en_iyi[1]
            else:
                self.wall_follow_until = max(self.wall_follow_until, simdi + 260)
                sonuc = pygame.Vector2(0.0, 0.0)
                for derece in (
                    82 * self.wall_follow_sign,
                    -82 * self.wall_follow_sign,
                    126 * self.wall_follow_sign,
                ):
                    yon = istenen.rotate(derece)
                    pos = bas + yon * min(27.0, hiz * 0.09)
                    if self._hareket_gecerli(pos.x, pos.y, digerler):
                        sonuc = yon * hiz * 0.55
                        break

        if sonuc.length_squared() > 1e-6:
            self.local_plan_output_dir = sonuc.normalize()
            self.local_plan_speed_ratio = max(
                0.0, min(1.05, sonuc.length() / max(1.0, hiz))
            )
        else:
            self.local_plan_output_dir = pygame.Vector2(0.0, 0.0)
            self.local_plan_speed_ratio = 0.0
        self.local_plan_input_dir = istenen
        self.local_plan_target = hedef_v
        self.local_plan_until = simdi + int(
            COMMON_ENEMY_LOCAL_TICK_MS.get(self.tur, 64)
        )
        return sonuc

    def _hareketi_uygula(
        self,
        dx,
        dy,
        digerler,
        hedef_nokta=None,
        oyuncuyu_engel_say=True,
    ):
        """Continuous-feel collision: açık harekette fast-path, engelde tangent recovery."""
        baslangic = pygame.Vector2(self.x, self.y)
        hareket_v = pygame.Vector2(dx, dy)
        toplam = hareket_v.length()
        if toplam <= 0.0001:
            self.last_move_distance = 0.0
            return 0.0

        # Küçük normal adımlarda tek exact test yeterlidir; sub-step yalnız hızlı harekette gerekir.
        # yaptığı için hızlı Berserker gereksiz geometri maliyeti üretiyordu.
        son = baslangic + hareket_v
        if toplam <= 4.75 and self._hareket_gecerli(
            son.x, son.y, digerler, oyuncuyu_engel_say
        ):
            self.x, self.y = son.x, son.y
            self.last_move_distance = toplam
            return toplam

        adim_sayisi = max(1, int(math.ceil(toplam / 4.5)))
        temel = hareket_v / adim_sayisi
        hedef_v = pygame.Vector2(hedef_nokta) if hedef_nokta is not None else None

        for _ in range(adim_sayisi):
            normal_hedef = pygame.Vector2(self.x, self.y) + temel
            if self._hareket_gecerli(
                normal_hedef.x,
                normal_hedef.y,
                digerler,
                oyuncuyu_engel_say,
            ):
                self.x, self.y = normal_hedef.x, normal_hedef.y
                continue

            # Yalnız gerçekten bloklandığında tangent fan açılır.
            en_iyi = None
            for derece in (22, -22, 44, -44, 68, -68, 90, -90):
                sapma = _vektor_dondur(temel, derece)
                pos = pygame.Vector2(self.x, self.y) + sapma
                if not self._hareket_gecerli(
                    pos.x, pos.y, digerler, oyuncuyu_engel_say
                ):
                    continue
                ilerleme = 0.0
                if hedef_v is not None:
                    once = pygame.Vector2(self.x, self.y).distance_to(hedef_v)
                    ilerleme = once - pos.distance_to(hedef_v)
                yon_koruma = (
                    temel.normalize().dot(sapma.normalize())
                    if sapma.length_squared() > 1e-6
                    else 0.0
                )
                side = (
                    0.05 if math.copysign(1.0, derece) == self.wall_follow_sign else 0.0
                )
                skor = (
                    ilerleme * 3.0
                    + yon_koruma * 0.66
                    + self._lokal_aciklik(pos) * 0.30
                    + side
                )
                if en_iyi is None or skor > en_iyi[0]:
                    en_iyi = (skor, sapma, pos)

            if en_iyi is not None:
                _, sapma, pos = en_iyi
                self.x, self.y = pos.x, pos.y
                hiz = math.hypot(self.vx, self.vy)
                if hiz > 1.0 and sapma.length_squared() > 1e-6:
                    yeni = sapma.normalize() * hiz
                    self.vx = self.vx * 0.38 + yeni.x * 0.62
                    self.vy = self.vy * 0.38 + yeni.y * 0.62
                continue

            # Axis slide son güvenlik katmanı.
            x_ok = self._hareket_gecerli(
                self.x + temel.x,
                self.y,
                digerler,
                oyuncuyu_engel_say,
            )
            y_ok = self._hareket_gecerli(
                self.x,
                self.y + temel.y,
                digerler,
                oyuncuyu_engel_say,
            )
            if x_ok:
                self.x += temel.x
                self.vy *= 0.52
            elif y_ok:
                self.y += temel.y
                self.vx *= 0.52
            else:
                self.vx *= 0.18
                self.vy *= 0.18
                self.nav_next_replan_ms = 0
                self.local_plan_until = 0
                break

        hareket = pygame.Vector2(self.x, self.y).distance_to(baslangic)
        self.last_move_distance = hareket
        return hareket

    def _temiz_bad_cells(self, simdi):
        if not self.nav_bad_cells:
            return
        self.nav_bad_cells = {h: t for h, t in self.nav_bad_cells.items() if t > simdi}

    def _rota_hedefi(self, simdi, hedef, force_replan=False):
        """
        Cached grid LOS -> incremental Theta* -> cached pure-pursuit lookahead.

        En kritik V6 farkı: bu fonksiyon hiçbir karede 4000 node'u tek başına
        çözmez ve path üzerindeki dokuz node'u her render frame'inde yeniden taramaz.
        """
        konum = pygame.Vector2(self.x, self.y)
        hedef = pygame.Vector2(hedef)
        self._temiz_bad_cells(simdi)
        start_cell = (
            int(konum.x // COMMON_ENEMY_NAV_GRID),
            int(konum.y // COMMON_ENEMY_NAV_GRID),
        )
        goal_cell = (
            int(hedef.x // COMMON_ENEMY_NAV_GRID),
            int(hedef.y // COMMON_ENEMY_NAV_GRID),
        )

        direct_key = (start_cell, goal_cell)
        if direct_key != self.nav_direct_key:
            self.nav_direct_key = direct_key
            self.nav_direct_value = _common_enemy_hucre_los(
                self.tur, start_cell, goal_cell
            )

        if self.nav_direct_value and self.stuck_ms < 190.0:
            self.nav_path = []
            self.nav_index = 0
            self.nav_job = None
            self.nav_last_goal = hedef
            self.nav_goal = hedef
            self.nav_goal_cell = goal_cell
            self.nav_follow_target = hedef
            return hedef

        # Oyuncunun her birkaç piksel hareketi rota çözdürmez. Goal gridde en az iki
        # hücre kaymışsa veya mevcut rota gerçekten problemliyse yeni iş başlatılır.
        goal_shift = True
        if self.nav_goal_cell is not None:
            goal_shift = _common_enemy_octile(self.nav_goal_cell, goal_cell) >= 2.0
        job_mismatch = self.nav_job is not None and self.nav_job.goal != goal_cell
        replan_due = simdi >= self.nav_next_replan_ms
        needs_plan = force_replan or not self.nav_path or (goal_shift and replan_due)

        if needs_plan and (self.nav_job is None or self.nav_job.done or job_mismatch):
            self.nav_job = CommonEnemyThetaJob(
                self.tur,
                konum,
                hedef,
                yasak_hucreler=set(self.nav_bad_cells.keys()),
            )
            self.nav_goal_cell = goal_cell
            self.nav_last_goal = hedef
            self.nav_goal = hedef
            self.nav_next_replan_ms = simdi + int(self.cfg.get("path_replan_ms", 430))

        if self.nav_job is not None and not self.nav_job.done:
            budget = _common_enemy_path_budget_al(self.tur)
            if budget > 0:
                self.nav_job.step(budget)

        if self.nav_job is not None and self.nav_job.done:
            if self.nav_job.success and self.nav_job.result:
                self.nav_path = [pygame.Vector2(p) for p in self.nav_job.result]
                self.nav_index = 0
                self.nav_failure_count = max(0, self.nav_failure_count - 1)
                self.nav_follow_refresh_ms = 0
            elif not self.nav_path:
                self.nav_failure_count += 1
            self.nav_job = None

        if not self.nav_path:
            # Job birkaç kare sürerken enemy duvara abanmaz. Stable wall-follow local
            # hedefi seçer; candidate steering bunun güvenli alt yönünü bulur.
            fark = hedef - konum
            if fark.length_squared() <= 1e-6:
                return hedef
            yan = fark.normalize().rotate(76.0 * self.wall_follow_sign)
            self.nav_follow_target = konum + yan * (
                78.0 if self.tur == "berserker" else 66.0
            )
            return pygame.Vector2(self.nav_follow_target)

        while (
            self.nav_index < len(self.nav_path) - 1
            and konum.distance_to(self.nav_path[self.nav_index]) <= 21.0
        ):
            self.nav_index += 1
            self.nav_follow_refresh_ms = 0

        if simdi < self.nav_follow_refresh_ms:
            return pygame.Vector2(self.nav_follow_target)

        # En ileri görünür path node'u grid LOS cache ile seçilir. Bu işlem artık
        # yalnız 10-14 kez/s yapılır; aynı hücre çiftinin LOS'u da kalıcı cache'dedir.
        en_ileri = self.nav_index
        sinir = min(len(self.nav_path) - 1, self.nav_index + 7)
        for i in range(sinir, self.nav_index, -1):
            p = pygame.Vector2(self.nav_path[i])
            h = (
                int(p.x // COMMON_ENEMY_NAV_GRID),
                int(p.y // COMMON_ENEMY_NAV_GRID),
            )
            if _common_enemy_hucre_los(self.tur, start_cell, h):
                en_ileri = i
                break
        self.nav_index = en_ileri

        lookahead = float(self.cfg.get("path_lookahead", 80.0))
        hedef_p = pygame.Vector2(self.nav_path[self.nav_index])
        kalan = lookahead
        i = self.nav_index
        bas_p = konum
        while i < len(self.nav_path):
            p = pygame.Vector2(self.nav_path[i])
            seg = p - bas_p
            uzun = seg.length()
            if uzun >= kalan and uzun > 1e-6:
                hedef_p = bas_p + seg * (kalan / uzun)
                break
            kalan -= uzun
            bas_p = p
            hedef_p = p
            i += 1

        self.nav_follow_target = pygame.Vector2(hedef_p)
        self.nav_follow_refresh_ms = simdi + int(
            COMMON_ENEMY_NAV_FOLLOW_TICK_MS.get(self.tur, 84)
        )
        return pygame.Vector2(self.nav_follow_target)

    def _yonleri_hareketten_guncelle(self, vektor, zorla=False):
        if self.attacking and not zorla:
            return
        if vektor.length_squared() <= 4.0:
            return
        if self.tur == "crawler":
            if abs(vektor.x) > 1.5:
                self.direction = "right" if vektor.x > 0 else "left"
                self.visual_direction = self.direction
        else:
            self.direction = _common_enemy_yon_bul(vektor.x, vektor.y, self.direction)
            self.visual_direction = _berserker_gorsel_yon_bul(
                vektor.x, vektor.y, self.visual_direction
            )

    def _oyuncu_swing_ritmini_ogren(self, simdi):
        if saldiri_baslangic == self.last_observed_player_attack_id:
            return False
        self.last_observed_player_attack_id = saldiri_baslangic
        if self.last_player_attack_seen_ms > 0:
            aralik = simdi - self.last_player_attack_seen_ms
            if 180 <= aralik <= 2600:
                alfa = 0.22 if self.player_attack_samples > 2 else 0.42
                self.player_attack_interval_ema += (
                    aralik - self.player_attack_interval_ema
                ) * alfa
                self.player_attack_samples += 1
        self.last_player_attack_seen_ms = simdi
        return True

    def _crawler_kacis_baslat(self, simdi, digerler):
        konum = pygame.Vector2(self.x, self.y)
        oyuncu = pygame.Vector2(oyuncu_x, oyuncu_y)
        radial = konum - oyuncu
        if radial.length_squared() <= 1e-6:
            radial = pygame.Vector2(1.0, 0.0)
        radial = radial.normalize()
        tangent = pygame.Vector2(-radial.y, radial.x)
        saldiri_rect = oyuncu_saldiri_vurus_rect()

        adaylar = []
        for isaret in (-1.0, 1.0):
            for radial_bias in (0.10, 0.24, -0.05):
                yon = tangent * isaret + radial * radial_bias
                if yon.length_squared() <= 1e-6:
                    continue
                yon = yon.normalize()
                hedef = konum + yon * float(self.cfg["evade_distance"])
                oyuncu_mesafe = hedef.distance_to(oyuncu)
                if (
                    not float(self.cfg["evade_ring_min"])
                    <= oyuncu_mesafe
                    <= float(self.cfg["evade_ring_max"])
                ):
                    continue
                if not self._hareket_gecerli(hedef.x, hedef.y, digerler):
                    continue
                if not common_enemy_dogrudan_yol_acik_mi(
                    self.tur,
                    konum,
                    hedef,
                    adim=5.0,
                    navigation=False,
                ):
                    continue
                rect = self.collision_rect(hedef.x, hedef.y)
                guven = pygame.Vector2(rect.center).distance_to(
                    pygame.Vector2(saldiri_rect.center)
                )
                aciklik = self._lokal_aciklik(hedef)
                # Yakın kal; ama hitbox merkezinden uzaklaş.
                ring = -abs(oyuncu_mesafe - 92.0) * 0.16
                skor = guven * 0.86 + ring + aciklik * 24.0
                adaylar.append((skor, hedef))

        if not adaylar:
            return False
        adaylar.sort(key=lambda x: x[0], reverse=True)
        self.evade_target = adaylar[0][1]
        self.evade_until = simdi + int(self.cfg["evade_ms"])
        self.defense_cooldown_until = simdi + int(self.cfg["evade_cooldown_ms"])
        self.crawler_commit_until = self.evade_until + 430
        return True

    def _dash_yonu_sec(self, ana_yon, digerler, mesafe, backdash=False):
        """Ucuz broad-phase + exact finalist ile güvenli dash koridoru seçer."""
        ana_yon = pygame.Vector2(ana_yon)
        if ana_yon.length_squared() <= 1e-6:
            return None
        ana_yon = ana_yon.normalize()
        acilar = (
            (0, 16, -16, 34, -34, 56, -56, 78, -78)
            if backdash
            else (0, 12, -12, 26, -26, 44, -44)
        )
        oyuncu = pygame.Vector2(oyuncu_x, oyuncu_y)
        bas = pygame.Vector2(self.x, self.y)
        adaylar = []

        for derece in acilar:
            yon = ana_yon.rotate(derece)
            min_aciklik = 1.0
            gecis = True
            for oran in (0.25, 0.50, 0.75, 1.0):
                pos = bas + yon * mesafe * oran
                if not _common_enemy_hizli_statik_gecerli_mi(self.tur, pos.x, pos.y):
                    gecis = False
                    break
                if not _common_enemy_dinamik_rect_gecerli(
                    self, pos.x, pos.y, digerler, True
                ):
                    gecis = False
                    break
                min_aciklik = min(min_aciklik, self._lokal_aciklik(pos))
            if not gecis:
                continue
            son = bas + yon * mesafe
            skor = ana_yon.dot(yon) * 2.0 + min_aciklik * 1.15 - abs(derece) * 0.006
            if backdash:
                skor += (son.distance_to(oyuncu) - bas.distance_to(oyuncu)) * 0.022
            adaylar.append((skor, yon))

        adaylar.sort(key=lambda x: x[0], reverse=True)
        for _, yon in adaylar[:3]:
            son = bas + yon * mesafe
            if not common_enemy_dogrudan_yol_acik_mi(
                self.tur, bas, son, adim=7.0, navigation=False
            ):
                continue
            if not _common_enemy_dinamik_rect_gecerli(
                self, son.x, son.y, digerler, True
            ):
                continue
            return yon
        return None

    def _dash_baslat(self, tur, yon, simdi, digerler):
        if self.tur != "berserker" or self.attacking or simdi < self.recovery_until:
            return False
        if simdi < self.dash_cooldown_until:
            return False

        if tur == "back":
            hiz = float(self.cfg["backdash_speed"])
            sure = int(self.cfg["backdash_ms"])
            cooldown = int(self.cfg["backdash_cooldown_ms"])
        else:
            hiz = float(self.cfg["chase_dash_speed"]) * self._faz_hiz_carpani()
            sure = int(self.cfg["chase_dash_ms"])
            cooldown = int(self.cfg.get("chase_dash_cooldown_ms", 2700))

        mesafe = hiz * (sure / 1000.0)
        test_mesafesi = mesafe
        if tur == "chase":
            oyuncuya_mesafe = pygame.Vector2(self.x, self.y).distance_to(
                pygame.Vector2(oyuncu_x, oyuncu_y)
            )
            test_mesafesi = min(
                mesafe,
                max(
                    38.0,
                    oyuncuya_mesafe - float(self.cfg["stop_radius"]) - 12.0,
                ),
            )

        secilen = self._dash_yonu_sec(
            yon,
            digerler,
            test_mesafesi,
            backdash=(tur == "back"),
        )
        if secilen is None:
            return False

        self.dash_kind = tur
        self.dash_until = simdi + sure
        self.dash_cooldown_until = simdi + cooldown
        self.dash_velocity = secilen * hiz
        self.last_dash_ms = simdi
        self.vx, self.vy = (
            self.dash_velocity.x,
            self.dash_velocity.y,
        )
        self._yonleri_hareketten_guncelle(self.dash_velocity)
        return True

    def _dash_guncelle(self, dt, simdi, digerler):
        if self.tur != "berserker" or simdi >= self.dash_until:
            if self.dash_kind is not None:
                biten_tur = self.dash_kind
                self.dash_kind = None
                self.dash_velocity *= 0.30
                # Dash'ten saldırıya anlık snap yok. Kısa ayak toplama süresi hareketi
                # daha fiziksel ve okunabilir yapar; chase dash yine tehditkârdır.
                ayak_toplama = 165 if biten_tur == "back" else 225
                self.recovery_until = max(self.recovery_until, simdi + ayak_toplama)
            return False

        self._yonleri_hareketten_guncelle(self.dash_velocity)
        hedef = pygame.Vector2(self.x, self.y) + self.dash_velocity * max(
            0.045, dt * 3.2
        )
        hareket = self._hareketi_uygula(
            self.dash_velocity.x * dt,
            self.dash_velocity.y * dt,
            digerler,
            hedef,
        )
        if hareket < 0.42:
            self.dash_until = simdi
            self.dash_kind = None
            self.nav_next_replan_ms = 0
            self.stuck_ms += 120.0
        return True

    def _oyuncu_saldirisina_reaksiyon(self, simdi, digerler):
        if not oyuncu_saldiriyor:
            return
        yeni_swing = self._oyuncu_swing_ritmini_ogren(simdi)
        if not yeni_swing:
            return

        saldiri = oyuncu_saldiri_vurus_rect()
        tehdit = saldiri.inflate(44 if self.tur == "berserker" else 40, 32)
        if not tehdit.colliderect(self.collision_rect()):
            return
        if self.attacking or simdi < self.hit_stun_until or simdi < self.stagger_until:
            return

        if self.tur == "crawler":
            # Art arda her swing'de kusursuz dodge yok. Crawler zeki ama okunabilir.
            can_orani = self.hp / max(1.0, self.max_hp)
            sans = float(self.cfg["evade_chance"]) + (0.08 if can_orani < 0.35 else 0.0)
            if simdi >= self.defense_cooldown_until and random.random() < min(
                0.82, sans
            ):
                self._crawler_kacis_baslat(simdi, digerler)
        else:
            mesafe = pygame.Vector2(self.x, self.y).distance_to((oyuncu_x, oyuncu_y))
            if (
                simdi >= self.dash_cooldown_until
                and mesafe < 126.0
                and oyuncu_saldiri_vurus_penceresi_aktif_mi(simdi)
            ):
                # Berserker artık her telegraph'a psişik biçimde cevap vermez. Yalnız
                # kılıcın gerçekten aktif penceresine girerken ve yakınındaysa geri kaçar.
                ritim_bonus = (
                    0.025
                    if self.player_attack_samples >= 3
                    and self.player_attack_interval_ema < 650
                    else 0.0
                )
                sans = min(
                    0.26,
                    float(self.cfg["backdash_chance"]) + ritim_bonus,
                )
                if random.random() < sans:
                    away = pygame.Vector2(self.x - oyuncu_x, self.y - oyuncu_y)
                    if away.length_squared() <= 1e-6:
                        away = pygame.Vector2(-1.0, 0.0)
                    self._dash_baslat("back", away, simdi, digerler)

    def _crawler_evade_guncelle(self, dt, simdi, digerler):
        if (
            self.tur != "crawler"
            or self.evade_target is None
            or simdi >= self.evade_until
        ):
            self.evade_target = None
            return False

        konum = pygame.Vector2(self.x, self.y)
        yol = pygame.Vector2(self.evade_target) - konum
        if yol.length() <= 8.0:
            self.evade_target = None
            return False
        yon = yol.normalize()
        hedef_hiz = self._candidate_velocity(
            yon,
            float(self.cfg["evade_speed"]),
            self.evade_target,
            digerler,
            simdi,
            force=False,
        )
        mevcut = pygame.Vector2(self.vx, self.vy)
        cevap = 1.0 - math.exp(-17.0 * dt)
        yeni = mevcut + (hedef_hiz - mevcut) * cevap
        self.vx, self.vy = yeni.x, yeni.y
        self._yonleri_hareketten_guncelle(yeni)
        self._hareketi_uygula(
            self.vx * dt,
            self.vy * dt,
            digerler,
            self.evade_target,
        )
        return True

    def _berserker_chase_dash_kontrol(self, simdi, digerler, rota_hedefi, mesafe):
        if self.tur != "berserker" or not self.aggro or self.attacking:
            return False

        if mesafe <= 138.0:
            self.last_pressure_ms = simdi
            self.next_chase_dash_ms = simdi + random.randint(
                int(self.cfg["chase_dash_min_wait_ms"]),
                int(self.cfg["chase_dash_max_wait_ms"]),
            )
            return False

        if (
            mesafe < float(self.cfg["chase_dash_trigger_distance"])
            or simdi < self.next_chase_dash_ms
            or simdi < self.dash_cooldown_until
            or simdi < self.recovery_until
        ):
            return False

        konum = pygame.Vector2(self.x, self.y)
        yon = pygame.Vector2(rota_hedefi) - konum
        if yon.length_squared() <= 9.0:
            return False

        basladi = self._dash_baslat("chase", yon, simdi, digerler)
        if basladi:
            self.next_chase_dash_ms = simdi + random.randint(
                int(self.cfg.get("chase_dash_min_wait_ms", 3250)),
                int(self.cfg.get("chase_dash_max_wait_ms", 4750)),
            )
        else:
            # Engel dash koridorunu kapattıysa hemen tekrar spamlamaz; path takip eder.
            self.next_chase_dash_ms = simdi + 900
        return basladi

    def _taktik_hedef_sec(self, simdi, oyuncu_tahmin, digerler, oyuncu_hiz_vektoru):
        """
        Oyuncu merkezini değil ulaşılabilir bir melee slotunu hedefler.

        Bu tek değişiklik final yaklaşımda önemli: enemy artık player collider'ın
        merkezine path üretip son 20 pikselde sürekli collision'a basmaz.
        """
        if simdi < self.tactical_refresh_ms and self.tactical_target is not None:
            return pygame.Vector2(self.tactical_target)

        konum = pygame.Vector2(self.x, self.y)
        oyuncu = pygame.Vector2(oyuncu_tahmin)
        fark = konum - oyuncu
        if fark.length_squared() <= 1e-6:
            fark = pygame.Vector2(1.0, 0.0)
        radial = fark.normalize()

        if self.tur == "crawler":
            # Crawler düz saldırır. Yalnız hedef slot geçersizse küçük açılarla alternatif arar.
            radius = max(43.0, float(self.cfg["attack_range"]) - 12.0)
            acilar = (0, 18, -18, 35, -35, 58, -58)
            adaylar = []
            for aci in acilar:
                yon = radial.rotate(aci)
                p = oyuncu + yon * radius
                if not common_enemy_statik_konum_gecerli_mi(
                    self.tur, p.x, p.y, navigation=True
                ):
                    continue
                sapma = abs(aci) * 0.06
                mesafe = konum.distance_to(p)
                aciklik = self._lokal_aciklik(p)
                adaylar.append((mesafe + sapma - aciklik * 9.0, p))
            hedef = min(adaylar, key=lambda x: x[0])[1] if adaylar else oyuncu
            self.tactical_target = pygame.Vector2(hedef)
            self.tactical_refresh_ms = simdi + 420
            return pygame.Vector2(hedef)

        # Berserker: saldırı hazır değilken combat ring üzerinde dolaşır; cooldown
        # dolduğunda ring'i attack menziline daraltır ve gerçekten içeri girer.
        # Böylece strafe zekâsı enemy'yi sonsuza dek menzil dışında tutmaz.
        attack_hazir = (
            simdi - self.last_attack_ms
            >= max(
                220,
                int(self.cfg["attack_cooldown_ms"])
                + int(getattr(self, "next_attack_variance_ms", 0)),
            )
            and simdi >= self.recovery_until
        )
        radius = (
            max(54.0, float(self.cfg["attack_range"]) - 11.0)
            if attack_hazir
            else float(self.cfg["combat_radius"])
        )
        face = _common_enemy_oyuncu_yon_vektoru()
        adaylar = []
        base_angle = math.degrees(math.atan2(radial.y, radial.x))
        for ofset in (
            0,
            28,
            -28,
            56,
            -56,
            88,
            -88,
            122,
            -122,
            160,
            -160,
            180,
        ):
            aci = base_angle + ofset
            yon = pygame.Vector2(1.0, 0.0).rotate(aci)
            p = oyuncu + yon * radius
            if not common_enemy_statik_konum_gecerli_mi(
                self.tur, p.x, p.y, navigation=True
            ):
                continue

            d = konum.distance_to(p)
            aciklik = self._lokal_aciklik(p)
            approach_dir = p - oyuncu
            if approach_dir.length_squared() > 1e-6:
                approach_dir = approach_dir.normalize()
            frontness = face.dot(approach_dir)
            flank_bonus = max(0.0, -frontness) * 22.0 + (1.0 - abs(frontness)) * 9.0
            konum_h = (
                int(konum.x // COMMON_ENEMY_NAV_GRID),
                int(konum.y // COMMON_ENEMY_NAV_GRID),
            )
            p_h = (
                int(p.x // COMMON_ENEMY_NAV_GRID),
                int(p.y // COMMON_ENEMY_NAV_GRID),
            )
            los_bonus = 16.0 if _common_enemy_hucre_los(self.tur, konum_h, p_h) else 0.0
            other_penalty = 0.0
            for diger in digerler:
                if diger is self or not getattr(diger, "active", False):
                    continue
                dd = pygame.Vector2(diger.x, diger.y).distance_to(p)
                if dd < 105.0:
                    other_penalty += (105.0 - dd) * 0.38

            velocity_align = 0.0
            if oyuncu_hiz_vektoru.length_squared() > 25.0:
                # Hareket eden oyuncunun kaçış yönünün ilerisindeki slot biraz daha değerli.
                toward = p - oyuncu
                if toward.length_squared() > 1e-6:
                    velocity_align = (
                        oyuncu_hiz_vektoru.normalize().dot(toward.normalize()) * 10.0
                    )

            skor = (
                d
                - aciklik * 24.0
                - flank_bonus
                - los_bonus
                - velocity_align
                + other_penalty
            )
            adaylar.append((skor, p))

        if adaylar:
            adaylar.sort(key=lambda x: x[0])
            hedef = adaylar[0][1]
        else:
            hedef = oyuncu
        self.tactical_target = pygame.Vector2(hedef)
        self.tactical_refresh_ms = simdi + int(self.cfg.get("flank_refresh_ms", 320))
        return pygame.Vector2(hedef)

    def _berserker_combat_yon(self, simdi, oyuncu, mesafe, temel_yon):
        """Berserker'ın hareketini okunabilir üç faza böler: av, baskı, commit.

        Eski sürümde cooldown boyunca sabit tangent orbit kullandığı için yaratık
        oyuncunun çevresinde yapay bir uydu gibi davranabiliyordu. V7'de strafe yalnız
        kısa reposition pencerelerinde oluşur; saldırı yaklaşınca doğrudan karar verir.
        """
        if self.tur != "berserker":
            return temel_yon

        attack_cd = max(
            220,
            int(self.cfg["attack_cooldown_ms"])
            + int(getattr(self, "next_attack_variance_ms", 0)),
        )
        cooldown_kalan = attack_cd - (simdi - self.last_attack_ms)
        konum = pygame.Vector2(self.x, self.y)
        radial = konum - oyuncu
        if radial.length_squared() <= 1e-6:
            return temel_yon
        radial = radial.normalize()

        # Uzakta: rota ve intercept kararına sadık kal. Gereksiz strafe yok.
        if mesafe >= 168.0:
            self.pressure_commit_until = 0
            return temel_yon

        # Saldırı çok yakında hazır olacaksa kısa bir commit penceresi aç ve hedefe
        # kararlı gir. Bu, küçük zigzagları keser ve saldırıyı okunur kılar.
        if cooldown_kalan <= 260 and simdi >= self.recovery_until:
            if self.pressure_commit_until <= simdi:
                self.pressure_commit_until = simdi + int(
                    self.cfg.get("pressure_commit_ms", 720)
                )
            return temel_yon

        if simdi < self.pressure_commit_until:
            return temel_yon

        # Başarısız saldırı sonrası yalnız kısa süre yana reset. Tam daire çizmez.
        if simdi < self.post_miss_reposition_until:
            tangent = pygame.Vector2(-radial.y, radial.x) * self.orbit_sign
            radius_hatasi = mesafe - float(self.cfg["combat_radius"])
            duzeltme = -radial * max(-0.45, min(0.45, radius_hatasi / 82.0))
            combat = tangent * float(self.cfg["combat_strafe_strength"]) + duzeltme
            return combat.normalize() if combat.length_squared() > 0.01 else temel_yon

        # Normal cooldown: yalnız hafif bir açı kır; sürekli çevreleme yok.
        if cooldown_kalan > 360 and 86.0 < mesafe < 145.0:
            tangent = pygame.Vector2(-radial.y, radial.x) * self.orbit_sign
            karisim = pygame.Vector2(temel_yon) * 0.88 + tangent * 0.12
            if karisim.length_squared() > 0.01:
                return karisim.normalize()
        return temel_yon

    def _stuck_progress_guncelle(self, dt, simdi, hedef, hareket):
        hedef_v = pygame.Vector2(hedef)
        yeni_mesafe = pygame.Vector2(self.x, self.y).distance_to(hedef_v)
        if self.last_progress_distance is None:
            self.last_progress_distance = yeni_mesafe
            return

        ilerleme = self.last_progress_distance - yeni_mesafe
        hiz = math.hypot(self.vx, self.vy)
        if hiz > 42.0 and (hareket < 0.55 or ilerleme < -0.25 or abs(ilerleme) < 0.035):
            self.stuck_ms += dt * 1000.0
        else:
            self.stuck_ms = max(0.0, self.stuck_ms - dt * 1450.0)
        self.last_progress_distance = yeni_mesafe

        if self.stuck_ms > 250.0:
            self.nav_next_replan_ms = 0
            hucre = (
                int(self.x // COMMON_ENEMY_NAV_GRID),
                int(self.y // COMMON_ENEMY_NAV_GRID),
            )
            # Bulunduğu hücreyi değil, mevcut path'in hemen önündeki problemli hücreyi cezalandır.
            if self.nav_path and self.nav_index < len(self.nav_path):
                p = pygame.Vector2(self.nav_path[self.nav_index])
                hucre = (
                    int(p.x // COMMON_ENEMY_NAV_GRID),
                    int(p.y // COMMON_ENEMY_NAV_GRID),
                )
            self.nav_bad_cells[hucre] = simdi + 1050
            self.wall_follow_until = simdi + 420

        if self.stuck_ms > 780.0:
            # Uzun kilitte side bias'ı tersine çevir. Aynı kaya köşesine aynı taraftan
            # tekrar tekrar basmayı engeller.
            self.wall_follow_sign *= -1.0
            self.orbit_sign *= -1.0
            self.stuck_ms = 260.0
            self.nav_failure_count += 1

    def _hp_bar_guncelle(self, dt, simdi):
        hedef = float(self.hp)
        a = 1.0 - math.exp(-14.0 * dt)
        self.hp_display += (hedef - self.hp_display) * a
        if simdi >= self.hp_trail_hold_until:
            b = 1.0 - math.exp(-4.8 * dt)
            self.hp_trail += (hedef - self.hp_trail) * b
        self.hp_display = max(0.0, min(float(self.max_hp), self.hp_display))
        self.hp_trail = max(
            self.hp_display,
            min(float(self.max_hp), self.hp_trail),
        )

    def guncelle(self, dt, simdi, digerler, oyuncu_hiz_vektoru):
        if not self.active or self.hp <= 0:
            return

        self._poise_guncelle(dt, simdi)
        self._hp_bar_guncelle(dt, simdi)

        # Reaksiyon yalnız yeni swing başladığında gerçek iş yapar.
        self._oyuncu_saldirisina_reaksiyon(simdi, digerler)

        if (
            oyuncu_saldiri_vurus_penceresi_aktif_mi(simdi)
            and saldiri_baslangic != self.last_player_attack_id
        ):
            if oyuncu_saldiri_vurus_rect().colliderect(self.collision_rect()):
                if common_enemy_saldiri_los_acik_mi(self, adim=5.0):
                    self.last_player_attack_id = saldiri_baslangic
                    silah_temas_sesi_cal(self.tur)
                    self.hasar_al(oyuncu_saldiri_hasar_miktari())

        # yalnız Crawler/Berserker projectile dash; tüm türler ground-fire kaçışı yapar.
        # Dodge i-frame sağlamaz; ateş topu fiziksel olarak hâlâ yakalayabilir.
        if self._fire_ai_guncelle(dt, simdi, digerler):
            return
        if self._dash_guncelle(dt, simdi, digerler):
            return
        if self._crawler_evade_guncelle(dt, simdi, digerler):
            return

        # Pasif durumda pathfinding / steering / LOS hiç çalışmaz.
        if not self.aggro:
            self.vx *= math.exp(-8.5 * dt)
            self.vy *= math.exp(-8.5 * dt)
            return

        if self._saldiri_guncelle(simdi):
            return

        if simdi < self.stagger_until:
            self.vx *= math.exp(-9.0 * dt)
            self.vy *= math.exp(-9.0 * dt)
            self._hareketi_uygula(
                self.vx * dt,
                self.vy * dt,
                digerler,
                (oyuncu_x, oyuncu_y),
            )
            return

        if simdi < self.hit_stun_until:
            self._hareketi_uygula(
                self.vx * dt,
                self.vy * dt,
                digerler,
                (oyuncu_x, oyuncu_y),
            )
            return

        konum = pygame.Vector2(self.x, self.y)
        oyuncu = pygame.Vector2(oyuncu_x, oyuncu_y)
        fark = oyuncu - konum
        mesafe = max(0.0001, fark.length())
        self._berserker_sabirsizlik_guncelle(dt, simdi, mesafe)
        self._yonleri_hareketten_guncelle(fark)

        # Exact LOS yalnız gerçekten saldırı menziline yaklaşınca ölçülür.
        if (
            mesafe <= float(self.cfg["attack_range"]) + 7.0
            and simdi - self.last_attack_ms
            >= max(
                220,
                int(self.cfg["attack_cooldown_ms"])
                + int(getattr(self, "next_attack_variance_ms", 0)),
            )
            and simdi >= self.recovery_until
            and oyuncu_hp > 0
            and self._attack_baslatma_temasi_var_mi()
            and self._attack_los_cached(simdi)
        ):
            self._saldiri_baslat(simdi)
            return

        if simdi < self.recovery_until:
            self.vx *= math.exp(-7.0 * dt)
            self.vy *= math.exp(-7.0 * dt)
            self._hareketi_uygula(self.vx * dt, self.vy * dt, digerler, oyuncu)
            return

        if self.tur == "berserker":
            oyuncu_tahmin = _common_enemy_kesisim_hedefi(
                konum,
                oyuncu,
                oyuncu_hiz_vektoru,
                self._anlik_move_speed(),
                float(self.cfg["prediction_max"]),
                common_enemy_oyuncu_ivmesi,
            )
        else:
            tahmin = min(
                float(self.cfg["prediction_max"]),
                mesafe / max(1.0, self._anlik_move_speed()) * 0.22,
            )
            oyuncu_tahmin = oyuncu + oyuncu_hiz_vektoru * tahmin

        taktik_hedef = self._taktik_hedef_sec(
            simdi, oyuncu_tahmin, digerler, oyuncu_hiz_vektoru
        )
        rota_hedefi = self._rota_hedefi(
            simdi,
            taktik_hedef,
            force_replan=self.stuck_ms > 300.0 or self.nav_failure_count > 3,
        )

        if self._berserker_chase_dash_kontrol(simdi, digerler, rota_hedefi, mesafe):
            return

        yol = pygame.Vector2(rota_hedefi) - konum
        d = max(0.0001, yol.length())
        yon = yol / d

        # Crawler dodge sonrası tekrar daha düz saldırır; exact LOS yerine static
        # grid LOS kullanılır ve aynı hücre çiftinde sonuç cache'den gelir.
        if self.tur == "crawler" and simdi < self.crawler_commit_until:
            duz = oyuncu_tahmin - konum
            if duz.length_squared() > 1e-6:
                a_h = (
                    int(konum.x // COMMON_ENEMY_NAV_GRID),
                    int(konum.y // COMMON_ENEMY_NAV_GRID),
                )
                b_h = (
                    int(oyuncu_tahmin.x // COMMON_ENEMY_NAV_GRID),
                    int(oyuncu_tahmin.y // COMMON_ENEMY_NAV_GRID),
                )
                if _common_enemy_hucre_los(self.tur, a_h, b_h):
                    yon = duz.normalize()

        yon = self._berserker_combat_yon(simdi, oyuncu, mesafe, yon)

        kalan = max(0.0, konum.distance_to(taktik_hedef) - 2.0)
        hiz_orani = math.tanh(kalan / max(1.0, float(self.cfg["arrival_sigma"])))
        if self.nav_path:
            hiz_orani = max(
                0.90 if self.tur == "berserker" else 0.82,
                hiz_orani,
            )

        hiz = self._anlik_move_speed() * hiz_orani
        if self.tur == "berserker" and mesafe < 150.0:
            hiz *= float(self.cfg.get("close_speed_mul", 0.82))

        hedef_hiz = self._candidate_velocity(yon, hiz, rota_hedefi, digerler, simdi)
        hedef_hiz += self._separation(digerler)
        hedef_hiz = _vektor_uzunluk_sinirla(
            hedef_hiz, max(1.0, self._anlik_move_speed())
        )

        mevcut = pygame.Vector2(self.vx, self.vy)
        cevap = 1.0 - math.exp(-float(self.cfg["steering_lambda"]) * dt)
        delta_v = (hedef_hiz - mevcut) * cevap
        delta_v = _vektor_uzunluk_sinirla(delta_v, float(self.cfg["acceleration"]) * dt)
        yeni_hiz = mevcut + delta_v
        self.vx, self.vy = yeni_hiz.x, yeni_hiz.y
        self._yonleri_hareketten_guncelle(yeni_hiz)

        hareket = self._hareketi_uygula(
            self.vx * dt, self.vy * dt, digerler, rota_hedefi
        )
        self._stuck_progress_guncelle(dt, simdi, taktik_hedef, hareket)

    def _animasyon_kareleri(self):
        hiz = math.hypot(self.vx, self.vy)
        savunma_hareketi = self.evade_target is not None or self.dash_kind is not None
        durum = (
            "attack"
            if self.attacking
            else ("walk" if hiz > 12.0 and (self.aggro or savunma_hareketi) else "idle")
        )

        if self.tur == "crawler":
            return durum, COMMON_ENEMY_SPRITELERI["crawler"].get(durum, [])
        yonlu = COMMON_ENEMY_SPRITELERI["berserker"].get(durum, {})
        kareler = (
            yonlu.get(self.visual_direction, []) if isinstance(yonlu, dict) else []
        )
        return durum, kareler

    def _animasyon_kare(self, simdi):
        durum, kareler = self._animasyon_kareleri()
        if not kareler:
            return durum, None
        if durum == "attack":
            index = self._attack_frame_index(simdi)
        else:
            sure = int(
                self.cfg["walk_frame_ms"]
                if durum == "walk"
                else self.cfg["idle_frame_ms"]
            )
            if durum == "walk" and self.dash_kind is not None:
                sure = max(38, int(sure * 0.64))
            # Berserker sabırsızlaştıkça yürüyüş frekansı fiziksel hızı izler;
            # böylece sprite kayıyormuş gibi görünmez.
            if durum == "walk" and self.tur == "berserker":
                anim_mul = self._anlik_move_speed() / max(
                    1.0, float(self.cfg["move_speed"])
                )
                sure = max(
                    48,
                    int(sure / max(1.0, math.sqrt(anim_mul))),
                )
            index = int(max(0, simdi - self.anim_epoch) // max(1, sure)) % len(kareler)
        return durum, kareler[index]

    def ciz_govde(self):
        if not self.active or self.hp <= 0:
            self._son_cizim_rect = None
            return

        simdi = pygame.time.get_ticks()
        ekran_x = dunya_ekran_x(self.x)
        ekran_y = dunya_ekran_y(self.y)

        # Sprite içindeki eski Berserker gölgesi asset/runtime temizliğinde kaldırılır.
        # Dünya gölgesi tek kaynaktır; böylece çift oval görünmez.
        karakter_zemin_golgesi_ciz(
            ekran_x,
            ekran_y - 1,
            (48 if self.tur == "berserker" else 43) * KAMERA_YAKINLASTIRMA,
            (13 if self.tur == "berserker" else 11) * KAMERA_YAKINLASTIRMA,
            82,
        )

        _, kare = self._animasyon_kare(simdi)
        rect = None
        if kare is not None:
            faktor = float(self.cfg["sprite_scale"]) * KAMERA_YAKINLASTIRMA
            boyut = (
                max(1, int(round(kare.get_width() * faktor))),
                max(1, int(round(kare.get_height() * faktor))),
            )
            yon_anahtari = (
                self.direction if self.tur == "crawler" else self.visual_direction
            )
            anahtar = (
                "common_enemy_v10",
                id(kare),
                boyut,
                self.tur,
                yon_anahtari,
            )
            cizilecek = sprite_olcek_onbellegi.get(anahtar)
            if cizilecek is None:
                cizilecek = pygame.transform.scale(kare, boyut)
                if self.tur == "crawler" and self.direction == "right":
                    cizilecek = pygame.transform.flip(cizilecek, True, False)
                sprite_olcek_onbellegi[anahtar] = cizilecek

            rect = cizilecek.get_rect(midbottom=(ekran_x, ekran_y + 2))
            ekran.blit(cizilecek, rect)
            if simdi < self.hit_flash_until:
                sprite_maskeli_parlama_ciz(cizilecek, rect, (214, 54, 60), 108)
            fire_magic_burn_overlay_sprite_ciz(self, cizilecek, rect)
        else:
            govde = pygame.Rect(ekran_x - 18, ekran_y - 54, 36, 50)
            pygame.draw.ellipse(ekran, (36, 9, 14), govde)
            pygame.draw.ellipse(
                ekran,
                PARLAK_KIRMIZI if self.aggro else KAN_KIRMIZISI,
                govde,
                3,
            )
            rect = govde
        self._son_cizim_rect = rect

    def ciz_ui(self):
        if not self.active or self.hp <= 0:
            return

        ekran_x = dunya_ekran_x(self.x)
        ekran_y = dunya_ekran_y(self.y)
        rect = getattr(self, "_son_cizim_rect", None)
        oran = max(
            0.0,
            min(
                1.0,
                self.hp_display / max(1.0, float(self.max_hp)),
            ),
        )
        trail_oran = max(
            oran,
            min(
                1.0,
                self.hp_trail / max(1.0, float(self.max_hp)),
            ),
        )

        bar_genislik = 150 if self.tur == "berserker" else 118
        bar_yukseklik = 15
        bar_ust = (rect.top if rect is not None else ekran_y - 70) - 27
        bar = pygame.Rect(
            ekran_x - bar_genislik // 2,
            bar_ust,
            bar_genislik,
            bar_yukseklik,
        )

        # Hasar sonrası çok kısa trailing blade: önce eski HP silueti, üstüne gerçek HP.
        if trail_oran > oran + 0.008:
            gotik_bicak_bari_ciz(
                bar,
                trail_oran,
                (73, 37, 39),
                (18, 5, 8),
                (120, 72, 75),
                "",
                False,
                False,
            )

        gotik_bicak_bari_ciz(
            bar,
            oran,
            (116, 4, 24),
            (22, 5, 9),
            (196, 26, 45),
            f"{self.hp}/{self.max_hp}",
            False,
            False,
        )
        yazi_yaz(
            self.name,
            bar.centerx,
            bar.top - 8,
            BEYAZ,
            mini_font,
            True,
        )

    def ciz_debug_nav(self):
        if not COMMON_ENEMY_DEBUG_NAV or not self.active:
            return
        for i in range(self.nav_index, len(self.nav_path)):
            p = self.nav_path[i]
            sx, sy = dunya_ekran_x(p.x), dunya_ekran_y(p.y)
            pygame.draw.circle(ekran, (238, 205, 76), (int(sx), int(sy)), 3)
            if i > self.nav_index:
                q = self.nav_path[i - 1]
                pygame.draw.line(
                    ekran,
                    (150, 118, 44),
                    (
                        int(dunya_ekran_x(q.x)),
                        int(dunya_ekran_y(q.y)),
                    ),
                    (int(sx), int(sy)),
                    1,
                )

    def ciz(self):
        self.ciz_govde()
        self.ciz_ui()


class HeadsThrowerRockProjectile:
    """Heads Thrower'ın hedefe kilitlenmeyen, okunabilir balistik taşı.

    Dünya x/y'si yerdeki izdüşümdür; `z` yalnız render yüksekliğidir. Böylece top-down
    collision ile görsel yay birbirine karışmaz. Hedef release anında sabitlenir:
    oyuncu sonradan yön değiştirirse taş onu psişik biçimde takip etmez.
    """

    def __init__(
        self,
        owner_uid,
        start,
        target,
        damage,
        simdi,
        flight_ms,
        arc_height,
        hit_radius,
    ):
        self.owner_uid = str(owner_uid)
        self.start = pygame.Vector2(start)
        self.target = pygame.Vector2(target)
        self.x = float(self.start.x)
        self.y = float(self.start.y)
        self.z = 0.0
        self.damage = int(damage)
        self.started_ms = int(simdi)
        self.flight_ms = max(360, int(flight_ms))
        self.arc_height = max(24.0, float(arc_height))
        self.hit_radius = max(12.0, float(hit_radius))
        self.active = True
        self.impacted = False
        self.rotation_seed = (sum(ord(c) for c in self.owner_uid) * 37 + simdi) % 360
        self.last_ground = pygame.Vector2(self.start)

    def progress(self, simdi):
        return max(
            0.0,
            min(
                1.0,
                (int(simdi) - self.started_ms) / max(1.0, float(self.flight_ms)),
            ),
        )

    def _impact(self, simdi):
        global oyuncu_hp
        if self.impacted:
            return
        self.impacted = True
        self.active = False
        impact = pygame.Vector2(self.x, self.y)
        oyuncu = pygame.Vector2(oyuncu_x, oyuncu_y - 8.0)
        mesafe = impact.distance_to(oyuncu)
        if oyuncu_hp > 0 and mesafe <= self.hit_radius:
            if oyuncu_savunma_darbe_karsila("headsthrower", self.x, self.y, None):
                kamera_hit_sarsintisi_baslat(2.2, 90)
            else:
                hasar = min(int(self.damage), max(0, int(oyuncu_hp)))
                oyuncu_hp = max(0, oyuncu_hp - hasar)
                oyuncu_kanli_hasar_kaydi(
                    self.x,
                    self.y,
                    "medium_blunt",
                    hasar,
                    "headsthrower_rock",
                )
                dunya_olayi_kaydet(
                    "hit_taken",
                    damage=hasar,
                    count=1,
                    enemy="headsthrower_rock",
                )
                kamera_hit_sarsintisi_baslat(5.2, 220)
                bildirim_goster(
                    bt(
                        f"Fırlatılan taş sana -{hasar} hasar verdi.",
                        f"The thrown rock dealt -{hasar} damage.",
                    ),
                    PARLAK_KIRMIZI,
                )
        else:
            kamera_hit_sarsintisi_baslat(1.7, 90)
        owner = next(
            (
                d
                for d in combat_enemy_aktorleri()
                if str(getattr(d, "uid", "")) == self.owner_uid
            ),
            None,
        )
        for hedef in combat_enemy_aktorleri():
            if hedef is owner:
                continue
            if (
                impact.distance_to((float(hedef.x), float(hedef.y) - 8.0))
                <= self.hit_radius + _magic_hedef_yaricapi(hedef) * 0.45
            ):
                hedef.hasar_al(
                    self.damage,
                    owner if owner is not None else "enemy",
                )
        combat_impact_spawn(self.x, self.y, "shock", 1.25, pygame.Vector2(0, 1))
        enemy_rock_impacts.append(RockImpact(self.x, self.y, simdi))

    def guncelle(self, dt, simdi):
        if not self.active:
            return
        p = self.progress(simdi)
        # Ground travel, release'te sabitlenmiş hedefe yumuşak fakat okunabilir gider.
        q = p * p * (3.0 - 2.0 * p)
        ground = self.start.lerp(self.target, q)
        self.last_ground = pygame.Vector2(self.x, self.y)
        self.x, self.y = ground.x, ground.y
        self.z = 4.0 * self.arc_height * p * (1.0 - p)

        # Çok alçalmışken yüksek duvar/solid zeminin içine gömülmesin. Yüksek arkta
        # küçük kayaların üstünden geçebilir; inişte solid'e çarparsa orada düşer.
        if p > 0.72 and self.z < 26.0 and harita_pikseli_engel_mi(self.x, self.y - 4.0):
            self._impact(simdi)
            return
        if p >= 1.0:
            self._impact(simdi)

    def ciz(self):
        if not self.active:
            return
        sx = dunya_ekran_x(self.x)
        sy = dunya_ekran_y(self.y)
        zpx = self.z * KAMERA_YAKINLASTIRMA
        # Yerdeki gölge, oyuncunun taşın nereye ineceğini sezmesini sağlar.
        shadow_w = max(
            5,
            int(round((13.0 - min(7.0, self.z * 0.05)) * KAMERA_YAKINLASTIRMA)),
        )
        shadow = pygame.Surface((shadow_w * 2 + 4, 10), pygame.SRCALPHA)
        pygame.draw.ellipse(shadow, (0, 0, 0, 82), shadow.get_rect())
        ekran.blit(
            shadow,
            (int(sx - shadow.get_width() / 2), int(sy - 5)),
        )

        if HEADSTHROWER_ROCK_SPRITE is not None:
            factor = 0.72 * KAMERA_YAKINLASTIRMA
            size = (
                max(
                    1,
                    int(round(HEADSTHROWER_ROCK_SPRITE.get_width() * factor)),
                ),
                max(
                    1,
                    int(round(HEADSTHROWER_ROCK_SPRITE.get_height() * factor)),
                ),
            )
            phase = int((pygame.time.get_ticks() - self.started_ms) / 85) % 4
            key = (
                "heads_rock",
                id(HEADSTHROWER_ROCK_SPRITE),
                size,
                phase,
            )
            img = sprite_olcek_onbellegi.get(key)
            if img is None:
                img = pygame.transform.scale(HEADSTHROWER_ROCK_SPRITE, size)
                img = pygame.transform.rotate(img, phase * 90)
                sprite_olcek_onbellegi[key] = img
            rect = img.get_rect(center=(int(sx), int(sy - zpx - 8)))
            ekran.blit(img, rect)
        else:
            r = max(4, int(8 * KAMERA_YAKINLASTIRMA))
            pos = (int(sx), int(sy - zpx - 8))
            pygame.draw.circle(ekran, (64, 60, 55), pos, r)
            pygame.draw.circle(ekran, (30, 28, 27), pos, r, 2)
# </POTBO_STAGE S0441>

# <POTBO_STAGE S0443>


class HeadsThrowerEnemy(CommonEnemy):
    """Kırılgan fakat tehlikeli menzilli common enemy.

    Heads Thrower doğduğu anda avcıdır. AI üç hedef
    arasında karar verir: görüş hattı açmak, ideal taş menzilini korumak ve crowd'dan
    ayrılmak. Projectile release anında hedefi sabitler; dodge edilebilir ve adildir.
    """

    def __init__(self, uid, x, y):
        super().__init__(uid, "headsthrower", x, y)
        self.aggro = True
        self.direction = "right"
        self.visual_direction = "right"
        self.ranged_state = "idle"
        self.ranged_state_started_ms = -10000
        self.ranged_released = False
        self.next_throw_ms = pygame.time.get_ticks() + random.randint(900, 1700)
        self.reposition_target = pygame.Vector2(self.x, self.y)
        self.reposition_refresh_ms = 0
        self.last_los_value = False
        self.last_los_until = 0
        self.last_los_player = pygame.Vector2(-9999.0, -9999.0)
        self.last_los_self = pygame.Vector2(-9999.0, -9999.0)
        self.walk_anim_distance = 0.0
        self.walk_anim_last_pos = pygame.Vector2(self.x, self.y)

    def _yonleri_hareketten_guncelle(self, vektor, zorla=False):
        if self.ranged_state in ("pickup", "throw") and not zorla:
            return
        if vektor.length_squared() <= 2.0:
            return
        if abs(vektor.x) > 0.35:
            self.visual_direction = "right" if vektor.x >= 0 else "left"
            self.direction = self.visual_direction

    def _projectile_los(self, simdi, from_pos=None, to_pos=None, use_cache=True):
        bas = pygame.Vector2(
            from_pos if from_pos is not None else (self.x, self.y - 26.0)
        )
        son = pygame.Vector2(
            to_pos if to_pos is not None else (oyuncu_x, oyuncu_y - 24.0)
        )
        if use_cache and simdi < self.last_los_until:
            if (bas - self.last_los_self).length_squared() < 100.0 and (
                son - self.last_los_player
            ).length_squared() < 100.0:
                return self.last_los_value
        val = dunya_ince_los_acik_mi(bas, son, adim=6.0, npc_bloklar=True)
        if use_cache:
            self.last_los_value = val
            self.last_los_until = simdi + 105
            self.last_los_self = pygame.Vector2(bas)
            self.last_los_player = pygame.Vector2(son)
        return val

    def _atisa_basla(self, simdi):
        self.ranged_state = "pickup"
        self.ranged_state_started_ms = simdi
        self.ranged_released = False
        self.vx *= 0.12
        self.vy *= 0.12
        self._yonleri_hareketten_guncelle(
            pygame.Vector2(oyuncu_x - self.x, oyuncu_y - self.y),
            zorla=True,
        )
        dunya_olayi_kaydet("enemy_attack", enemy="headsthrower")

    def _tas_firlat(self, simdi):
        if self.ranged_released:
            return
        self.ranged_released = True
        start = pygame.Vector2(self.x, self.y - 30.0)
        player = pygame.Vector2(oyuncu_x, oyuncu_y - 10.0)
        # Lead bilinçli olarak kusursuz değildir. Uzakta biraz daha tahmin eder,
        # fakat release sonrası hedef sabit kalır ve oyuncu gerçek dodge yapabilir.
        dist = start.distance_to(player)
        lead_t = max(
            0.06,
            min(
                float(self.cfg.get("prediction_max", 0.34)),
                dist / 850.0,
            ),
        )
        lead = common_enemy_oyuncu_hizi * lead_t
        lead = _vektor_uzunluk_sinirla(lead, 74.0)
        target = player + lead
        target.x = max(28.0, min(HARITA_GENISLIK - 28.0, target.x))
        target.y = max(30.0, min(HARITA_YUKSEKLIK - 22.0, target.y))
        flight = random.randint(
            int(self.cfg["ranged_projectile_flight_min_ms"]),
            int(self.cfg["ranged_projectile_flight_max_ms"]),
        )
        enemy_projectiles.append(
            HeadsThrowerRockProjectile(
                self.uid,
                start,
                target,
                int(self.cfg["ranged_throw_damage"]),
                simdi,
                flight,
                float(self.cfg["ranged_projectile_arc"]),
                float(self.cfg["ranged_projectile_hit_radius"]),
            )
        )

    def _ranged_state_guncelle(self, dt, simdi):
        if self.ranged_state == "idle":
            return False
        self.vx *= math.exp(-11.0 * dt)
        self.vy *= math.exp(-11.0 * dt)
        if self.ranged_state == "pickup":
            frames = max(
                1,
                len(HEADSTHROWER_SPRITELERI.get("pickup", [])),
            )
            duration = frames * int(self.cfg["ranged_pickup_frame_ms"])
            if simdi - self.ranged_state_started_ms >= duration:
                self.ranged_state = "throw"
                self.ranged_state_started_ms = simdi
                self.ranged_released = False
            return True
        if self.ranged_state == "throw":
            frame_ms = int(self.cfg["ranged_throw_frame_ms"])
            release_ms = int(self.cfg["ranged_throw_release_frame"]) * frame_ms
            elapsed = simdi - self.ranged_state_started_ms
            if elapsed >= release_ms and not self.ranged_released:
                self._tas_firlat(simdi)
            frames = max(1, len(HEADSTHROWER_SPRITELERI.get("throw", [])))
            if elapsed >= frames * frame_ms:
                self.ranged_state = "recovery"
                self.ranged_state_started_ms = simdi
                self.next_throw_ms = simdi + random.randint(
                    int(self.cfg["ranged_throw_cooldown_min_ms"]),
                    int(self.cfg["ranged_throw_cooldown_max_ms"]),
                )
            return True
        if self.ranged_state == "recovery":
            if simdi - self.ranged_state_started_ms >= int(
                self.cfg["attack_recovery_ms"]
            ):
                self.ranged_state = "idle"
                self.reposition_refresh_ms = 0
            return True
        return False

    def _ring_hedefi_sec(self, simdi, digerler):
        if simdi < self.reposition_refresh_ms:
            return pygame.Vector2(self.reposition_target)
        self.reposition_refresh_ms = simdi + int(
            self.cfg.get("ranged_reposition_refresh_ms", 520)
        )
        player = pygame.Vector2(oyuncu_x, oyuncu_y)
        here = pygame.Vector2(self.x, self.y)
        preferred = float(self.cfg["ranged_preferred"])
        candidates = []
        seed = (sum(ord(c) for c in self.uid) * 17 + simdi // 700) % 360
        for k in range(14):
            angle = math.radians(seed + k * (360.0 / 14.0))
            radial = preferred + (
                22.0 if k % 3 == 0 else (-18.0 if k % 3 == 1 else 0.0)
            )
            p = player + pygame.Vector2(math.cos(angle), math.sin(angle)) * radial
            if not common_enemy_statik_konum_gecerli_mi(
                self.tur, p.x, p.y, navigation=True
            ):
                continue
            # Hedefte atış hattı açık olsun; aksi halde yalnız hareket hedefi olarak
            # son çare kabul edilir ve büyük ceza alır.
            los = self._projectile_los(
                simdi,
                (p.x, p.y - 26.0),
                (player.x, player.y - 24.0),
                use_cache=False,
            )
            crowd = 0.0
            for d in digerler:
                if d is self or not getattr(d, "active", False):
                    continue
                dd = p.distance_to((d.x, d.y))
                if dd < 88.0:
                    crowd += (88.0 - dd) * 1.6
            travel = here.distance_to(p)
            # Aynı tarafta kilitlenmek yerine zamanla farklı ring noktaları seçebilir.
            score = travel + crowd + (0.0 if los else 220.0)
            candidates.append((score, p))
        if candidates:
            candidates.sort(key=lambda item: item[0])
            self.reposition_target = pygame.Vector2(candidates[0][1])
        else:
            self.reposition_target = pygame.Vector2(player)
        return pygame.Vector2(self.reposition_target)

    def _taktik_ranged_hedef(self, simdi, digerler, mesafe, los):
        player = pygame.Vector2(oyuncu_x, oyuncu_y)
        here = pygame.Vector2(self.x, self.y)
        rmin = float(self.cfg["ranged_min"])
        rpref = float(self.cfg["ranged_preferred"])
        rmax = float(self.cfg["ranged_max"])
        away = here - player
        if away.length_squared() <= 1e-6:
            away = pygame.Vector2(1.0, 0.0)
        away = away.normalize()
        if mesafe < rmin:
            target = player + away * (rpref + 35.0)
            if common_enemy_statik_konum_gecerli_mi(
                self.tur, target.x, target.y, navigation=True
            ):
                return target
            return self._ring_hedefi_sec(simdi, digerler)
        if mesafe > rmax or not los:
            return self._ring_hedefi_sec(simdi, digerler)
        # İdeal bandın içindeyse gereksiz orbit yapma; küçük separation dışında dur.
        return pygame.Vector2(here)

    def guncelle(self, dt, simdi, digerler, oyuncu_hiz_vektoru):
        if not self.active or self.hp <= 0:
            return
        self._poise_guncelle(dt, simdi)
        self._hp_bar_guncelle(dt, simdi)

        if (
            oyuncu_saldiri_vurus_penceresi_aktif_mi(simdi)
            and saldiri_baslangic != self.last_player_attack_id
        ):
            if oyuncu_saldiri_vurus_rect().colliderect(self.collision_rect()):
                if common_enemy_saldiri_los_acik_mi(self, adim=5.0):
                    self.last_player_attack_id = saldiri_baslangic
                    silah_temas_sesi_cal(self.tur)
                    self.hasar_al(oyuncu_saldiri_hasar_miktari())
                    if not self.active:
                        return

        # Heads Thrower ayrı ranged state-machine kullandığı için base guncelle'ye
        # uğramaz; fire-awareness burada açıkça uygulanır.
        if self._fire_ai_guncelle(dt, simdi, digerler):
            return

        if not self.aggro:
            self.vx *= math.exp(-9.0 * dt)
            self.vy *= math.exp(-9.0 * dt)
            return
        if simdi < self.stagger_until or simdi < self.hit_stun_until:
            self.ranged_state = "idle"
            self.vx *= math.exp(-8.0 * dt)
            self.vy *= math.exp(-8.0 * dt)
            self._hareketi_uygula(
                self.vx * dt,
                self.vy * dt,
                digerler,
                (oyuncu_x, oyuncu_y),
            )
            return
        if self._ranged_state_guncelle(dt, simdi):
            return

        player = pygame.Vector2(oyuncu_x, oyuncu_y)
        here = pygame.Vector2(self.x, self.y)
        mesafe = here.distance_to(player)
        los = self._projectile_los(simdi)
        rmin = float(self.cfg["ranged_min"])
        rmax = float(self.cfg["ranged_max"])
        if (
            rmin <= mesafe <= rmax
            and los
            and simdi >= self.next_throw_ms
            and oyuncu_hp > 0
        ):
            self._atisa_basla(simdi)
            return

        tactical = self._taktik_ranged_hedef(simdi, digerler, mesafe, los)
        if tactical.distance_to(here) < 10.0:
            self.vx *= math.exp(-8.0 * dt)
            self.vy *= math.exp(-8.0 * dt)
            self._separation(digerler)
            return
        route = self._rota_hedefi(simdi, tactical, force_replan=self.stuck_ms > 280.0)
        path_vec = pygame.Vector2(route) - here
        if path_vec.length_squared() <= 1e-6:
            return
        direction = path_vec.normalize()
        speed = float(self.cfg["move_speed"])
        target_vel = self._candidate_velocity(direction, speed, route, digerler, simdi)
        target_vel += self._separation(digerler)
        target_vel = _vektor_uzunluk_sinirla(target_vel, speed)
        current = pygame.Vector2(self.vx, self.vy)
        response = 1.0 - math.exp(-float(self.cfg["steering_lambda"]) * dt)
        dv = _vektor_uzunluk_sinirla(
            (target_vel - current) * response,
            float(self.cfg["acceleration"]) * dt,
        )
        current += dv
        self.vx, self.vy = current.x, current.y
        self._yonleri_hareketten_guncelle(current)
        moved = self._hareketi_uygula(self.vx * dt, self.vy * dt, digerler, tactical)
        self._stuck_progress_guncelle(dt, simdi, tactical, moved)

    def _animasyon_kare(self, simdi):
        if self.ranged_state == "pickup":
            frames = HEADSTHROWER_SPRITELERI.get("pickup", [])
            ms = int(self.cfg["ranged_pickup_frame_ms"])
            idx = (
                min(
                    len(frames) - 1,
                    max(
                        0,
                        (simdi - self.ranged_state_started_ms) // max(1, ms),
                    ),
                )
                if frames
                else 0
            )
            return "pickup", frames[idx] if frames else None
        if self.ranged_state == "throw":
            frames = HEADSTHROWER_SPRITELERI.get("throw", [])
            ms = int(self.cfg["ranged_throw_frame_ms"])
            idx = (
                min(
                    len(frames) - 1,
                    max(
                        0,
                        (simdi - self.ranged_state_started_ms) // max(1, ms),
                    ),
                )
                if frames
                else 0
            )
            return "throw", frames[idx] if frames else None
        # Walk frame'i zamana değil gerçekten kat edilen mesafeye bağlıdır. Collision
        # veya steering karakteri durdurursa animasyon da durur; "sprite sürükleniyor"
        # hissinin ana nedeni olan skating böylece ortadan kalkar.
        pos = pygame.Vector2(self.x, self.y)
        adim = pos.distance_to(self.walk_anim_last_pos)
        if adim < 72.0:
            self.walk_anim_distance += adim
        self.walk_anim_last_pos = pos
        moving = math.hypot(self.vx, self.vy) > 8.0 and adim > 0.02
        if moving:
            frames = HEADSTHROWER_SPRITELERI.get("walk", [])
            if not frames:
                frames = HEADSTHROWER_SPRITELERI.get("idle", [])
            if not frames:
                return "walk", None
            stride_px = 8.5
            idx = int(self.walk_anim_distance / stride_px) % len(frames)
            return "walk", frames[idx]

        frames = HEADSTHROWER_SPRITELERI.get("idle", [])
        return ("idle", frames[0] if frames else None)

    def ciz_govde(self):
        if not self.active or self.hp <= 0:
            self._son_cizim_rect = None
            return
        simdi = pygame.time.get_ticks()
        sx = dunya_ekran_x(self.x)
        sy = dunya_ekran_y(self.y)
        karakter_zemin_golgesi_ciz(
            sx,
            sy - 1,
            34 * KAMERA_YAKINLASTIRMA,
            9 * KAMERA_YAKINLASTIRMA,
            70,
        )
        _, frame = self._animasyon_kare(simdi)
        rect = None
        if frame is not None:
            factor = float(self.cfg["sprite_scale"]) * KAMERA_YAKINLASTIRMA
            size = (
                max(1, int(frame.get_width() * factor)),
                max(1, int(frame.get_height() * factor)),
            )
            key = (
                "headsthrower_v10",
                id(frame),
                size,
                self.visual_direction,
            )
            img = sprite_olcek_onbellegi.get(key)
            if img is None:
                img = pygame.transform.scale(frame, size)
                # Kaynak sequence sağa bakar.
                if self.visual_direction == "left":
                    img = pygame.transform.flip(img, True, False)
                sprite_olcek_onbellegi[key] = img
            rect = img.get_rect(midbottom=(int(sx), int(sy + 2)))
            ekran.blit(img, rect)
            if simdi < self.hit_flash_until:
                sprite_maskeli_parlama_ciz(img, rect, (214, 52, 58), 112)
            fire_magic_burn_overlay_sprite_ciz(self, img, rect)
        self._son_cizim_rect = rect
# </POTBO_STAGE S0443>

# <POTBO_STAGE S0445>


def common_enemy_olustur(uid, tur, x, y):
    if tur == "headsthrower":
        return HeadsThrowerEnemy(uid, x, y)
    return CommonEnemy(uid, tur, x, y)


def enemy_projectiles_guncelle(dt, simdi):
    for projectile in list(enemy_projectiles):
        projectile.guncelle(dt, simdi)
    enemy_projectiles[:] = [p for p in enemy_projectiles if getattr(p, "active", False)]
    enemy_rock_impacts[:] = [fx for fx in enemy_rock_impacts if fx.alive(simdi)]


def _ambient_rat_spawn_noktasi():
    """
    Kamera çevresinde collision-free rat spawn arar; oyuncunun dibinde doğmaz.
    Görünür alan başarısızsa harita üzerinde daha geniş spiral fallback kullanır.
    """
    left = float(kamera_x)
    top = float(kamera_y)
    vw = GENISLIK / max(0.01, KAMERA_YAKINLASTIRMA)
    vh = YUKSEKLIK / max(0.01, KAMERA_YAKINLASTIRMA)

    for _ in range(32):
        x = random.uniform(left + 55.0, max(left + 56.0, left + vw - 55.0))
        y = random.uniform(top + 70.0, max(top + 71.0, top + vh - 45.0))
        if pygame.Vector2(x - oyuncu_x, y - oyuncu_y).length() < 125.0:
            continue
        if common_enemy_statik_konum_gecerli_mi("rat", x, y, navigation=False):
            return pygame.Vector2(x, y)

    # Golden-angle fallback around player.
    golden = math.radians(137.507764)
    center = pygame.Vector2(oyuncu_x, oyuncu_y)
    for i in range(48):
        r = 120.0 + 7.0 * i
        p = center + pygame.Vector2(math.cos(i * golden), math.sin(i * golden)) * r
        if common_enemy_statik_konum_gecerli_mi("rat", p.x, p.y, navigation=False):
            return p
    return None


def ambient_rat_spawn_deneme(simdi):
    global ambient_rat_next_spawn_ms

    aktif = [r for r in ambient_rats if r.active]
    if len(aktif) >= AMBIENT_RAT_MAX:
        return
    if simdi < ambient_rat_next_spawn_ms:
        return

    spawn = _ambient_rat_spawn_noktasi()
    if spawn is not None:
        ambient_rats.append(AmbientRat(spawn.x, spawn.y, simdi))
        # Aktif fare varken bu zaman kullanılmaz. Despawn olduğunda bir sonraki
        # güncellemede kısa bir gecikmeyle yenisi gelir.
        ambient_rat_next_spawn_ms = int(simdi) + 1300
    else:
        ambient_rat_next_spawn_ms = int(simdi) + 900


def ambient_rats_guncelle(dt, simdi):
    global ambient_rat_next_spawn_ms

    ambient_rat_spawn_deneme(simdi)
    for rat in list(ambient_rats):
        rat.guncelle(dt, simdi)
    ambient_rats[:] = [r for r in ambient_rats if r.active]

    if not ambient_rats:
        ambient_rat_next_spawn_ms = min(
            int(ambient_rat_next_spawn_ms), int(simdi) + 900
        )
# </POTBO_STAGE S0445>

# <POTBO_STAGE S0447>


class TarkardEnemy(CommonEnemy):
    """
    Özel isimli dünya aktörü. CommonEnemy yalnız motor taban sınıfıdır; Tarkard
    common_enemies popülasyonuna eklenmez.

    Davranış prensibi:
      * ağır ve kontrollü locomotion,
      * yüksek poise / düşük hit-stun,
      * obstacle-aware Theta* ile en iyi erişilebilir melee slotu,
      * oyuncu swing'ini input-read etmeden, yalnız görünür swing durumunda ön cephe
        cezası kullanarak yaklaşma açısını değiştirir,
      * tek bağlantıda %75 max-HP hasarı + stamina break + 2 s knockdown.
    """

    def __init__(self, uid, x, y):
        super().__init__(uid, "tarkard", x, y)
        self.direction = "left"
        self.visual_direction = "left"
        self.attack_variant = "heavy"
        self.heavy_miss_chain = 0
        self.last_variant_change_ms = -10000
        self.guard_memory_until = 0

    @property
    def name(self):
        return (
            "Tarkard"
            if tarkard_adi_ogrenildi
            else bt("İsimsiz Savaşçı", "Nameless Warrior")
        )

    def _oyuncu_saldirisina_reaksiyon(self, simdi, digerler):
        # Tarkard crawler gibi kaçmaz, Berserker gibi back-dash atmaz. Swing'i
        # görünce yalnız yaklaşma slotunu yeniden değerlendirir; bu fair ve okunabilir.
        if not oyuncu_saldiriyor:
            return
        if saldiri_baslangic == self.last_observed_player_attack_id:
            return
        self._oyuncu_swing_ritmini_ogren(simdi)
        self.tactical_refresh_ms = 0
        self.guard_memory_until = simdi + 520

    def _yonleri_hareketten_guncelle(self, vektor, zorla=False):
        if self.attacking and not zorla:
            return
        if vektor.length_squared() <= 4.0:
            return
        self.direction = _common_enemy_yon_bul(vektor.x, vektor.y, self.direction)
        # Sheet iki yönlü olmadığı için yalnız horizontal facing kullanılır.
        if abs(vektor.x) > 1.3:
            self.visual_direction = "right" if vektor.x > 0 else "left"

    def _attack_frames(self):
        return TARKARD_SPRITELERI.get(
            self.attack_variant,
            TARKARD_SPRITELERI.get("heavy", []),
        )

    def _attack_total_ms(self):
        kareler = self._attack_frames()
        kare_sure = int(self.cfg["attack_frame_ms"])
        if self.attack_variant == "whirl":
            kare_sure = max(92, int(kare_sure * 0.92))
        return max(1, len(kareler)) * kare_sure

    def _attack_frame_index(self, simdi):
        kareler = self._attack_frames()
        if not kareler:
            return 0
        kare_sure = int(self.cfg["attack_frame_ms"])
        if self.attack_variant == "whirl":
            kare_sure = max(92, int(kare_sure * 0.92))
        return min(
            len(kareler) - 1,
            int(max(0, simdi - self.attack_started_ms) // kare_sure),
        )

    def _saldiri_baslat(self, simdi):
        oyuncu_hiz = common_enemy_oyuncu_hizi.length()
        mesafe = pygame.Vector2(self.x, self.y).distance_to((oyuncu_x, oyuncu_y))
        # Whirl, sürekli çevresinde koşan oyuncuyu cezalandırır; yine de seyrek ve
        # daha uzun recovery'li olduğu için rastgele haksız bir AoE spam değildir.
        whirl_uygun = (
            mesafe < 89.0
            and oyuncu_hiz > 115.0
            and simdi - self.last_variant_change_ms > 2600
            and random.random() < 0.34
        )
        self.attack_variant = "whirl" if whirl_uygun else "heavy"
        self.last_variant_change_ms = simdi
        super()._saldiri_baslat(simdi)

    def _attack_rect(self):
        if self.attack_variant == "whirl":
            r = self.collision_rect()
            # Dairesel sprite hareketini yaklaşıkleyen geniş fakat okunabilir alan.
            return pygame.Rect(r.centerx - 70, r.centery - 56, 140, 112)
        return super()._attack_rect()

    def _saldiri_guncelle(self, simdi):
        if not self.attacking:
            return False

        kare = self._attack_frame_index(simdi)
        aktif_bas, aktif_son = self._attack_active_frame_araligi()
        if aktif_bas <= kare <= aktif_son:
            enemy_friendly_melee_vur(self, simdi)
        if aktif_bas <= kare <= aktif_son and not self.attack_connected:
            if self._attack_temas_var_mi(simdi):
                los = common_enemy_saldiri_los_acik_mi(self)
                if los and oyuncu_hp > 0:
                    if oyuncu_savunma_darbe_karsila("tarkard", self.x, self.y, self):
                        self.attack_connected = True
                        self.attack_damage_applied = True
                        self.heavy_miss_chain = 0
                        self.last_pressure_ms = simdi
                    else:
                        hasar = oyuncu_agir_darbe_uygula(self.x, self.y, self.name)
                        if hasar > 0:
                            self.attack_connected = True
                            self.attack_damage_applied = True
                            self.heavy_miss_chain = 0
                            self.last_pressure_ms = simdi

        if kare > aktif_son:
            self.attack_damage_applied = True

        if simdi - self.attack_started_ms >= self._attack_total_ms():
            if not self.attack_connected:
                self.heavy_miss_chain = min(4, self.heavy_miss_chain + 1)
            self.attacking = False
            self.attack_damage_applied = False
            recovery = int(self.cfg.get("attack_recovery_ms", 610))
            if self.attack_variant == "whirl":
                recovery = int(recovery * 1.24)
            if not self.attack_connected:
                recovery = int(recovery * 1.17)
            self.recovery_until = simdi + recovery
        return True

    def _taktik_hedef_sec(self, simdi, oyuncu_tahmin, digerler, oyuncu_hiz_vektoru):
        if simdi < self.tactical_refresh_ms and self.tactical_target is not None:
            return pygame.Vector2(self.tactical_target)

        konum = pygame.Vector2(self.x, self.y)
        oyuncu = pygame.Vector2(oyuncu_tahmin)
        radial = konum - oyuncu
        if radial.length_squared() <= 1e-6:
            radial = pygame.Vector2(1.0, 0.0)
        base = math.degrees(math.atan2(radial.y, radial.x))
        attack_ready = (
            simdi - self.last_attack_ms >= int(self.cfg["attack_cooldown_ms"])
            and simdi >= self.recovery_until
        )
        radius = 72.0 if attack_ready else float(self.cfg.get("combat_radius", 92.0))
        face = _common_enemy_oyuncu_yon_vektoru()
        swing_tehdidi = oyuncu_saldiriyor and simdi < self.guard_memory_until
        adaylar = []

        # Ağır karakter kısa yolu seçer ama dar collision koridoruna girmekten ve
        # oyuncunun aktif kılıç cephesine körlemesine basmaktan kaçınır.
        for ofset in (
            0,
            24,
            -24,
            48,
            -48,
            76,
            -76,
            112,
            -112,
            152,
            -152,
            180,
        ):
            yon = pygame.Vector2(1.0, 0.0).rotate(base + ofset)
            p = oyuncu + yon * radius
            if not common_enemy_statik_konum_gecerli_mi(
                self.tur, p.x, p.y, navigation=True
            ):
                continue
            aciklik = self._lokal_aciklik(p)
            path_len = konum.distance_to(p)
            approach = p - oyuncu
            frontness = (
                face.dot(approach.normalize())
                if approach.length_squared() > 1e-6
                else 0.0
            )
            sword_front_penalty = max(0.0, frontness) * (34.0 if swing_tehdidi else 9.0)
            dynamic_penalty = 0.0
            for diger in digerler:
                if diger is self or not getattr(diger, "active", False):
                    continue
                dd = pygame.Vector2(diger.x, diger.y).distance_to(p)
                if dd < 118.0:
                    dynamic_penalty += (118.0 - dd) * 0.44
            h0 = (
                int(konum.x // COMMON_ENEMY_NAV_GRID),
                int(konum.y // COMMON_ENEMY_NAV_GRID),
            )
            h1 = (
                int(p.x // COMMON_ENEMY_NAV_GRID),
                int(p.y // COMMON_ENEMY_NAV_GRID),
            )
            los_bonus = 15.0 if _common_enemy_hucre_los(self.tur, h0, h1) else 0.0
            skor = (
                path_len
                + sword_front_penalty
                + dynamic_penalty
                - aciklik * 30.0
                - los_bonus
            )
            adaylar.append((skor, p))

        hedef = min(adaylar, key=lambda x: x[0])[1] if adaylar else oyuncu
        self.tactical_target = pygame.Vector2(hedef)
        self.tactical_refresh_ms = simdi + int(self.cfg.get("flank_refresh_ms", 430))
        return pygame.Vector2(hedef)

    def _animasyon_kareleri(self):
        hiz = math.hypot(self.vx, self.vy)
        simdi = pygame.time.get_ticks()
        if self.attacking:
            return "attack", self._attack_frames()
        if simdi < self.stagger_until:
            return "stagger", TARKARD_SPRITELERI.get("stagger", [])
        if hiz > 10.0 and self.aggro:
            return "walk", TARKARD_SPRITELERI.get("walk", [])
        return "idle", TARKARD_SPRITELERI.get("idle", [])

    def ciz_govde(self):
        if not self.active or self.hp <= 0:
            self._son_cizim_rect = None
            return
        simdi = pygame.time.get_ticks()
        ekran_x = dunya_ekran_x(self.x)
        ekran_y = dunya_ekran_y(self.y)
        karakter_zemin_golgesi_ciz(
            ekran_x,
            ekran_y - 1,
            55 * KAMERA_YAKINLASTIRMA,
            15 * KAMERA_YAKINLASTIRMA,
            88,
        )
        _, kare = self._animasyon_kare(simdi)
        rect = None
        if kare is not None:
            faktor = float(self.cfg["sprite_scale"]) * KAMERA_YAKINLASTIRMA
            boyut = (
                max(1, int(round(kare.get_width() * faktor))),
                max(1, int(round(kare.get_height() * faktor))),
            )
            anahtar = (
                "tarkard_v6",
                id(kare),
                boyut,
                self.visual_direction,
            )
            cizilecek = sprite_olcek_onbellegi.get(anahtar)
            if cizilecek is None:
                cizilecek = pygame.transform.scale(kare, boyut)
                # Kaynak sheet sağa dönük kabul edilir; sola yönelirken gerçek flip.
                if self.visual_direction == "left":
                    cizilecek = pygame.transform.flip(cizilecek, True, False)
                sprite_olcek_onbellegi[anahtar] = cizilecek
            rect = cizilecek.get_rect(midbottom=(ekran_x, ekran_y + 2))
            ekran.blit(cizilecek, rect)
            if simdi < self.hit_flash_until:
                sprite_maskeli_parlama_ciz(cizilecek, rect, (210, 54, 58), 106)
            fire_magic_burn_overlay_sprite_ciz(self, cizilecek, rect)
        else:
            govde = pygame.Rect(ekran_x - 24, ekran_y - 72, 48, 67)
            pygame.draw.ellipse(ekran, (42, 17, 20), govde)
            pygame.draw.ellipse(
                ekran,
                PARLAK_KIRMIZI if self.aggro else GRI,
                govde,
                3,
            )
            rect = govde
        self._son_cizim_rect = rect

    def ciz_ui(self):
        if not self.active or self.hp <= 0:
            return
        ekran_x = dunya_ekran_x(self.x)
        ekran_y = dunya_ekran_y(self.y)
        rect = getattr(self, "_son_cizim_rect", None)
        oran = max(
            0.0,
            min(
                1.0,
                self.hp_display / max(1.0, float(self.max_hp)),
            ),
        )
        trail_oran = max(
            oran,
            min(
                1.0,
                self.hp_trail / max(1.0, float(self.max_hp)),
            ),
        )
        bar = pygame.Rect(
            ekran_x - 88,
            (rect.top if rect is not None else ekran_y - 86) - 29,
            176,
            16,
        )
        if trail_oran > oran + 0.008:
            gotik_bicak_bari_ciz(
                bar,
                trail_oran,
                (78, 42, 44),
                (18, 5, 8),
                (126, 76, 79),
                "",
                False,
                False,
            )
        gotik_bicak_bari_ciz(
            bar,
            oran,
            (106, 3, 18),
            (19, 4, 7),
            (210, 31, 47),
            f"{self.hp}/{self.max_hp}",
            False,
            False,
        )
        yazi_yaz(
            self.name,
            bar.centerx,
            bar.top - 8,
            BEYAZ,
            mini_font,
            True,
        )
        if tarkard_adi_ogrenildi and self.aggro:
            yazi_yaz(
                bt(
                    "KODRAKİ'NİN BÜYÜK SAVAŞÇISI",
                    "GREAT WARRIOR OF KODRAKI",
                ),
                bar.centerx,
                bar.top - 22,
                GRI,
                mini_font,
                True,
            )


class SirTorrmundEnemy(TarkardEnemy):
    """Monthiem şövalyesi: ağır, disiplinli ve tek hatada öldürücü özel aktör.

    Tasarım kontratı:
      * 1000 HP ve çok yüksek poise,
      * dash yok; rota kalitesi / menzil disiplini ile tehdit oluşturur,
      * iki farklı uzun telegraph'lı kesme kullanır,
      * bağlantı kurarsa oyuncuyu savurmaz; doğrudan ölümcül kesme uygular,
      * oyuncunun swing'ine kusursuz input-reading yapmaz, yalnız görünür tehdit
        cephesine yaklaşma maliyeti ekler,
      * collision / Theta* / stuck recovery ortak güvenli motoru kullanır.
    """

    def __init__(self, uid, x, y):
        # TarkardEnemy.__init__ turu sabit "tarkard" yaptığı için doğrudan CommonEnemy.
        CommonEnemy.__init__(self, uid, "torrmund", x, y)
        self.direction = "left"
        self.visual_direction = "left"
        self.attack_variant = "execution"
        self.last_variant_change_ms = -10000
        self.guard_memory_until = 0
        self.heavy_miss_chain = 0
        self.execution_lock_until = 0

    @property
    def name(self):
        return "Sir Torrmund"

    def _oyuncu_saldirisina_reaksiyon(self, simdi, digerler):
        # Kaçmaz. Oyuncunun görünür swing'ini yalnız rota/slot maliyeti olarak hatırlar.
        if not oyuncu_saldiriyor:
            return
        if saldiri_baslangic == self.last_observed_player_attack_id:
            return
        self._oyuncu_swing_ritmini_ogren(simdi)
        self.guard_memory_until = simdi + 610
        self.tactical_refresh_ms = 0

    def _yonleri_hareketten_guncelle(self, vektor, zorla=False):
        if self.attacking and not zorla:
            return
        if vektor.length_squared() <= 4.0:
            return
        self.direction = _common_enemy_yon_bul(vektor.x, vektor.y, self.direction)
        if abs(vektor.x) > 1.2:
            self.visual_direction = "right" if vektor.x > 0 else "left"

    def _attack_frames(self):
        return TORRMUND_SPRITELERI.get(
            self.attack_variant,
            TORRMUND_SPRITELERI.get("execution", []),
        )

    def _attack_total_ms(self):
        frames = self._attack_frames()
        frame_ms = int(self.cfg["attack_frame_ms"])
        if self.attack_variant == "cleave":
            frame_ms = int(frame_ms * 1.10)
        return max(1, len(frames)) * max(1, frame_ms)

    def _attack_frame_index(self, simdi):
        frames = self._attack_frames()
        if not frames:
            return 0
        frame_ms = int(self.cfg["attack_frame_ms"])
        if self.attack_variant == "cleave":
            frame_ms = int(frame_ms * 1.10)
        return min(
            len(frames) - 1,
            int(max(0, simdi - self.attack_started_ms) // max(1, frame_ms)),
        )

    def _saldiri_baslat(self, simdi):
        mesafe = pygame.Vector2(self.x, self.y).distance_to((oyuncu_x, oyuncu_y))
        oyuncu_hiz = common_enemy_oyuncu_hizi.length()
        # Dikey cleave, oyuncu çok yaklaşmış ve yön değiştirmeyi zorluyorsa seyrek gelir;
        # yatay execution standart imzadır. Her ikisi de uzun telegraph taşır.
        cleave = (
            mesafe < 96.0
            and oyuncu_hiz > 95.0
            and simdi - self.last_variant_change_ms > 2800
            and random.random() < 0.30
        )
        self.attack_variant = "cleave" if cleave else "execution"
        self.last_variant_change_ms = simdi
        CommonEnemy._saldiri_baslat(self, simdi)
        self.execution_lock_until = simdi + self._attack_total_ms()

    def _attack_rect(self):
        r = self.collision_rect()
        # Uzun kılıç. Arkaya değil facing yönüne taşan bir kesme alanı.
        yon = _common_enemy_yon_vektoru(self.direction)
        if self.attack_variant == "cleave":
            merkez = pygame.Vector2(r.center) + yon * 34.0
            return pygame.Rect(int(merkez.x - 58), int(merkez.y - 43), 116, 86)
        merkez = pygame.Vector2(r.center) + yon * 40.0
        return pygame.Rect(int(merkez.x - 64), int(merkez.y - 36), 128, 72)

    def _saldiri_guncelle(self, simdi):
        if not self.attacking:
            return False

        frame = self._attack_frame_index(simdi)
        aktif_bas, aktif_son = self._attack_active_frame_araligi()
        if aktif_bas <= frame <= aktif_son:
            enemy_friendly_melee_vur(self, simdi)
        if aktif_bas <= frame <= aktif_son and not self.attack_connected:
            if self._attack_temas_var_mi(simdi):
                los = common_enemy_saldiri_los_acik_mi(self)
                if los and oyuncu_hp > 0:
                    if oyuncu_savunma_darbe_karsila("torrmund", self.x, self.y, self):
                        self.attack_connected = True
                        self.attack_damage_applied = True
                        self.heavy_miss_chain = 0
                        self.last_pressure_ms = simdi
                    else:
                        hasar = oyuncu_infaz_darbesi_uygula(
                            self.x,
                            self.y,
                            self.name,
                            self.direction,
                        )
                        if hasar > 0:
                            self.attack_connected = True
                            self.attack_damage_applied = True
                            self.heavy_miss_chain = 0
                            self.last_pressure_ms = simdi

        if frame > aktif_son:
            self.attack_damage_applied = True

        if simdi - self.attack_started_ms >= self._attack_total_ms():
            if not self.attack_connected:
                self.heavy_miss_chain = min(4, self.heavy_miss_chain + 1)
            self.attacking = False
            self.attack_damage_applied = False
            recovery = int(self.cfg.get("attack_recovery_ms", 920))
            if self.attack_variant == "cleave":
                recovery = int(recovery * 1.10)
            if not self.attack_connected:
                # Tek vuruş ölümcül olduğu için kaçırması oyuncuya gerçek punish penceresi açar.
                recovery = int(recovery * 1.24)
            self.recovery_until = simdi + recovery
        return True

    def _taktik_hedef_sec(self, simdi, oyuncu_tahmin, digerler, oyuncu_hiz_vektoru):
        # Tarkard'ın ağır slot seçimini kullan, fakat Torrmund daha disiplinli:
        # kılıç menzili nedeniyle daha geniş halka ve daha kuvvetli ön-açı cezası.
        if simdi < self.tactical_refresh_ms and self.tactical_target is not None:
            return pygame.Vector2(self.tactical_target)

        konum = pygame.Vector2(self.x, self.y)
        oyuncu = pygame.Vector2(oyuncu_tahmin)
        radial = konum - oyuncu
        if radial.length_squared() <= 1e-6:
            radial = pygame.Vector2(1.0, 0.0)
        base = math.degrees(math.atan2(radial.y, radial.x))
        ready = (
            simdi - self.last_attack_ms >= int(self.cfg["attack_cooldown_ms"])
            and simdi >= self.recovery_until
        )
        radius = 86.0 if ready else float(self.cfg.get("combat_radius", 104.0))
        face = _common_enemy_oyuncu_yon_vektoru()
        swing = oyuncu_saldiriyor and simdi < self.guard_memory_until
        adaylar = []

        for ofset in (
            0,
            20,
            -20,
            38,
            -38,
            62,
            -62,
            92,
            -92,
            126,
            -126,
            180,
        ):
            yon = pygame.Vector2(1.0, 0.0).rotate(base + ofset)
            p = oyuncu + yon * radius
            if not common_enemy_statik_konum_gecerli_mi(
                self.tur, p.x, p.y, navigation=True
            ):
                continue
            aciklik = self._lokal_aciklik(p)
            path_len = konum.distance_to(p)
            approach = p - oyuncu
            frontness = (
                face.dot(approach.normalize())
                if approach.length_squared() > 1e-6
                else 0.0
            )
            sword_penalty = max(0.0, frontness) * (42.0 if swing else 8.0)
            crowd_penalty = 0.0
            for diger in digerler:
                if diger is self or not getattr(diger, "active", False):
                    continue
                dd = pygame.Vector2(diger.x, diger.y).distance_to(p)
                if dd < 126.0:
                    crowd_penalty += (126.0 - dd) * 0.48
            h0 = (
                int(konum.x // COMMON_ENEMY_NAV_GRID),
                int(konum.y // COMMON_ENEMY_NAV_GRID),
            )
            h1 = (
                int(p.x // COMMON_ENEMY_NAV_GRID),
                int(p.y // COMMON_ENEMY_NAV_GRID),
            )
            los_bonus = 18.0 if _common_enemy_hucre_los(self.tur, h0, h1) else 0.0
            skor = path_len + sword_penalty + crowd_penalty - aciklik * 36.0 - los_bonus
            adaylar.append((skor, p))

        hedef = min(adaylar, key=lambda x: x[0])[1] if adaylar else oyuncu
        self.tactical_target = pygame.Vector2(hedef)
        self.tactical_refresh_ms = simdi + int(self.cfg.get("flank_refresh_ms", 470))
        return pygame.Vector2(hedef)

    def _animasyon_kareleri(self):
        hiz = math.hypot(self.vx, self.vy)
        simdi = pygame.time.get_ticks()
        if self.attacking:
            return "attack", self._attack_frames()
        if simdi < self.stagger_until:
            return "stagger", TORRMUND_SPRITELERI.get("stagger", [])
        if hiz > 9.0 and self.aggro:
            return "walk", TORRMUND_SPRITELERI.get("walk", [])
        return "idle", TORRMUND_SPRITELERI.get("idle", [])

    def ciz_govde(self):
        if not self.active or self.hp <= 0:
            self._son_cizim_rect = None
            return
        simdi = pygame.time.get_ticks()
        ekran_x = dunya_ekran_x(self.x)
        ekran_y = dunya_ekran_y(self.y)
        karakter_zemin_golgesi_ciz(
            ekran_x,
            ekran_y - 1,
            56 * KAMERA_YAKINLASTIRMA,
            14 * KAMERA_YAKINLASTIRMA,
            86,
        )
        _, kare = self._animasyon_kare(simdi)
        rect = None
        if kare is not None:
            faktor = float(self.cfg["sprite_scale"]) * KAMERA_YAKINLASTIRMA
            boyut = (
                max(1, int(round(kare.get_width() * faktor))),
                max(1, int(round(kare.get_height() * faktor))),
            )
            anahtar = (
                "torrmund_v7",
                id(kare),
                boyut,
                self.visual_direction,
            )
            cizilecek = sprite_olcek_onbellegi.get(anahtar)
            if cizilecek is None:
                cizilecek = pygame.transform.scale(kare, boyut)
                # Kaynak karakter sağa bakar; sol-facing yalnız runtime flip'tir.
                if self.visual_direction == "left":
                    cizilecek = pygame.transform.flip(cizilecek, True, False)
                sprite_olcek_onbellegi[anahtar] = cizilecek
            rect = cizilecek.get_rect(midbottom=(ekran_x, ekran_y + 2))
            ekran.blit(cizilecek, rect)
            if simdi < self.hit_flash_until:
                sprite_maskeli_parlama_ciz(cizilecek, rect, (205, 64, 68), 104)
            fire_magic_burn_overlay_sprite_ciz(self, cizilecek, rect)
        else:
            rect = pygame.Rect(ekran_x - 25, ekran_y - 76, 50, 70)
            pygame.draw.rect(ekran, (26, 25, 29), rect)
            pygame.draw.rect(ekran, (145, 145, 150), rect, 2)
        self._son_cizim_rect = rect

    def ciz_ui(self):
        if not self.active or self.hp <= 0:
            return
        ekran_x = dunya_ekran_x(self.x)
        ekran_y = dunya_ekran_y(self.y)
        rect = getattr(self, "_son_cizim_rect", None)
        oran = max(
            0.0,
            min(
                1.0,
                self.hp_display / max(1.0, float(self.max_hp)),
            ),
        )
        trail = max(
            oran,
            min(
                1.0,
                self.hp_trail / max(1.0, float(self.max_hp)),
            ),
        )
        bar = pygame.Rect(
            ekran_x - 96,
            (rect.top if rect is not None else ekran_y - 90) - 30,
            192,
            16,
        )
        if trail > oran + 0.008:
            gotik_bicak_bari_ciz(
                bar,
                trail,
                (72, 67, 67),
                (15, 8, 9),
                (132, 122, 122),
                "",
                False,
                False,
            )
        gotik_bicak_bari_ciz(
            bar,
            oran,
            (88, 8, 18),
            (17, 5, 7),
            (218, 218, 220),
            f"{self.hp}/{self.max_hp}",
            False,
            False,
        )
        yazi_yaz(
            "Sir Torrmund",
            bar.centerx,
            bar.top - 9,
            BEYAZ,
            mini_font,
            True,
        )
        if self.aggro:
            yazi_yaz(
                bt("MONTHIEM ŞÖVALYESİ", "KNIGHT OF MONTHIEM"),
                bar.centerx,
                bar.top - 23,
                GRI,
                mini_font,
                True,
            )
# </POTBO_STAGE S0447>

# <POTBO_STAGE S0449>


def common_enemy_durumunu_yukle(veri):
    global common_enemies
    global common_enemy_son_guncelleme
    global common_enemy_onceki_oyuncu_konumu
    global common_enemy_oyuncu_hizi
    global common_enemy_oyuncu_ivmesi
    global common_enemy_onceki_oyuncu_hizi

    if not isinstance(veri, list):
        common_enemy_sistemi_sifirla()
        return

    yuklenenler = []
    gorulen_turler = set()

    for index, kayit in enumerate(veri):
        if not isinstance(kayit, dict):
            continue
        tur = str(kayit.get("type", "crawler"))
        if tur not in COMMON_ENEMY_TURLERI or tur in gorulen_turler:
            continue

        try:
            x = float(kayit.get("x"))
            y = float(kayit.get("y"))
        except (TypeError, ValueError):
            x, y = common_enemy_guvenli_spawn_bul(tur, yuklenenler)

        if not common_enemy_spawn_gecerli_mi(tur, x, y, yuklenenler):
            x, y = common_enemy_guvenli_spawn_bul(tur, yuklenenler)

        dusman = common_enemy_olustur(
            str(kayit.get("id", f"{tur}_{index + 1}")),
            tur,
            x,
            y,
        )
        try:
            dusman.hp = max(
                0,
                min(
                    dusman.max_hp,
                    int(kayit.get("hp", dusman.max_hp)),
                ),
            )
        except (TypeError, ValueError):
            dusman.hp = dusman.max_hp
        try:
            dusman.poise = max(
                0.0,
                min(
                    float(dusman.cfg.get("poise_max", 0.0)),
                    float(kayit.get("poise", dusman.poise)),
                ),
            )
        except (TypeError, ValueError):
            pass
        dusman.hp_display = float(dusman.hp)
        dusman.hp_trail = float(dusman.hp)
        dusman.active = bool(kayit.get("active", dusman.hp > 0)) and dusman.hp > 0
        dusman.aggro = (
            (dusman.tur == "headsthrower") or bool(kayit.get("aggro", False))
        ) and dusman.active

        kayit_yonu = str(kayit.get("direction", dusman.direction))
        if kayit_yonu in ("left", "right", "up", "down"):
            dusman.direction = kayit_yonu

        kayit_gorsel_yonu = str(kayit.get("visual_direction", dusman.visual_direction))
        if dusman.tur == "crawler":
            if kayit_gorsel_yonu in ("left", "right"):
                dusman.visual_direction = kayit_gorsel_yonu
            else:
                dusman.visual_direction = (
                    dusman.direction
                    if dusman.direction in ("left", "right")
                    else "left"
                )
        elif dusman.tur == "headsthrower":
            if kayit_gorsel_yonu in ("left", "right"):
                dusman.visual_direction = kayit_gorsel_yonu
                dusman.direction = kayit_gorsel_yonu
        elif kayit_gorsel_yonu in BERSERKER_GORSEL_YON_SIRASI:
            dusman.visual_direction = kayit_gorsel_yonu

        yuklenenler.append(dusman)
        gorulen_turler.add(tur)

    for tur in COMMON_ENEMY_TURLERI:
        if tur in gorulen_turler:
            continue
        x, y = common_enemy_guvenli_spawn_bul(tur, yuklenenler)
        yuklenenler.append(
            common_enemy_olustur(f"{tur}_{len(yuklenenler) + 1}", tur, x, y)
        )

    common_enemies = yuklenenler
    common_enemy_son_guncelleme = pygame.time.get_ticks()
    common_enemy_onceki_oyuncu_konumu = (oyuncu_x, oyuncu_y)
    common_enemy_oyuncu_hizi = pygame.Vector2(0.0, 0.0)
    common_enemy_onceki_oyuncu_hizi = pygame.Vector2(0.0, 0.0)
    common_enemy_oyuncu_ivmesi = pygame.Vector2(0.0, 0.0)
    gecici_dunya_aktorlerini_sifirla()


def tarkard_durumunu_yukle(veri):
    global tarkard_actor

    if not isinstance(veri, dict):
        tx, ty = common_enemy_guvenli_spawn_bul("tarkard", common_enemies)
        tarkard_actor = TarkardEnemy("tarkard_unique", tx, ty)
        return

    try:
        x = float(veri.get("x"))
        y = float(veri.get("y"))
    except (TypeError, ValueError):
        x, y = common_enemy_guvenli_spawn_bul("tarkard", common_enemies)

    if not common_enemy_spawn_gecerli_mi("tarkard", x, y, common_enemies):
        x, y = common_enemy_guvenli_spawn_bul("tarkard", common_enemies)

    t = TarkardEnemy(str(veri.get("id", "tarkard_unique")), x, y)
    try:
        t.hp = max(0, min(t.max_hp, int(veri.get("hp", t.max_hp))))
    except (TypeError, ValueError):
        t.hp = t.max_hp
    try:
        t.poise = max(
            0.0,
            min(
                float(t.cfg.get("poise_max", 0.0)),
                float(veri.get("poise", t.poise)),
            ),
        )
    except (TypeError, ValueError):
        pass
    t.hp_display = float(t.hp)
    t.hp_trail = float(t.hp)
    t.active = bool(veri.get("active", t.hp > 0)) and t.hp > 0
    t.aggro = bool(veri.get("aggro", False)) and t.active
    direction = str(veri.get("direction", t.direction))
    if direction in ("left", "right", "up", "down"):
        t.direction = direction
    visual = str(veri.get("visual_direction", t.visual_direction))
    if visual in ("left", "right"):
        t.visual_direction = visual
    tarkard_actor = t


def torrmund_durumunu_yukle(veri):
    global torrmund_actor

    blockers = list(common_enemies)
    if tarkard_actor is not None and getattr(tarkard_actor, "active", False):
        blockers.append(tarkard_actor)

    if not isinstance(veri, dict):
        x, y = common_enemy_guvenli_spawn_bul("torrmund", blockers)
        torrmund_actor = SirTorrmundEnemy("torrmund_unique", x, y)
        return

    try:
        x = float(veri.get("x"))
        y = float(veri.get("y"))
    except (TypeError, ValueError):
        x, y = common_enemy_guvenli_spawn_bul("torrmund", blockers)

    if not common_enemy_spawn_gecerli_mi("torrmund", x, y, blockers):
        x, y = common_enemy_guvenli_spawn_bul("torrmund", blockers)

    aktor = SirTorrmundEnemy(str(veri.get("id", "torrmund_unique")), x, y)
    try:
        aktor.hp = max(
            0,
            min(aktor.max_hp, int(veri.get("hp", aktor.max_hp))),
        )
    except (TypeError, ValueError):
        aktor.hp = aktor.max_hp
    try:
        aktor.poise = max(
            0.0,
            min(
                float(aktor.cfg.get("poise_max", 0.0)),
                float(veri.get("poise", aktor.poise)),
            ),
        )
    except (TypeError, ValueError):
        pass
    aktor.hp_display = float(aktor.hp)
    aktor.hp_trail = float(aktor.hp)
    aktor.active = bool(veri.get("active", aktor.hp > 0)) and aktor.hp > 0
    aktor.aggro = bool(veri.get("aggro", False)) and aktor.active
    direction = str(veri.get("direction", aktor.direction))
    if direction in ("left", "right", "up", "down"):
        aktor.direction = direction
    visual = str(veri.get("visual_direction", aktor.visual_direction))
    if visual in ("left", "right"):
        aktor.visual_direction = visual
    torrmund_actor = aktor
# </POTBO_STAGE S0449>

# <POTBO_STAGE S0462>


def common_enemy_guncelle():
    global common_enemy_son_guncelleme
    global common_enemy_onceki_oyuncu_konumu
    global common_enemy_oyuncu_hizi
    global common_enemy_oyuncu_ivmesi
    global common_enemy_onceki_oyuncu_hizi

    if oyun_alt_durumu != HARITA or oyuncu_hp <= 0:
        return

    simdi = pygame.time.get_ticks()
    _common_enemy_path_budget_sifirla(simdi)
    dt = max(
        0.0,
        min(
            0.045,
            (simdi - common_enemy_son_guncelleme) / 1000.0,
        ),
    )
    common_enemy_son_guncelleme = simdi
    if dt <= 0.0:
        return

    if common_enemy_onceki_oyuncu_konumu is None:
        common_enemy_onceki_oyuncu_konumu = (oyuncu_x, oyuncu_y)

    onceki_x, onceki_y = common_enemy_onceki_oyuncu_konumu
    ham_hiz = pygame.Vector2((oyuncu_x - onceki_x) / dt, (oyuncu_y - onceki_y) / dt)
    ham_hiz = _vektor_uzunluk_sinirla(ham_hiz, max(390.0, oyuncu_hizi * 105.0))
    alfa = 1.0 - math.exp(-dt / 0.070)
    common_enemy_oyuncu_hizi += (ham_hiz - common_enemy_oyuncu_hizi) * alfa

    ham_ivme = (common_enemy_oyuncu_hizi - common_enemy_onceki_oyuncu_hizi) / max(
        0.001, dt
    )
    ham_ivme = _vektor_uzunluk_sinirla(ham_ivme, 1250.0)
    ivme_alfa = 1.0 - math.exp(-dt / 0.105)
    common_enemy_oyuncu_ivmesi += (ham_ivme - common_enemy_oyuncu_ivmesi) * ivme_alfa
    common_enemy_onceki_oyuncu_hizi = pygame.Vector2(common_enemy_oyuncu_hizi)
    common_enemy_onceki_oyuncu_konumu = (oyuncu_x, oyuncu_y)

    # Update sırasının sürekli aynı enemy lehine dynamic avoidance üretmemesi için
    # frame parity ile ters çevir. Yalnız iki common enemy olsa da fairness sağlar.
    tum_taktik_aktorler = list(common_enemies)
    if tarkard_actor is not None and getattr(tarkard_actor, "active", False):
        tum_taktik_aktorler.append(tarkard_actor)
    if torrmund_actor is not None and getattr(torrmund_actor, "active", False):
        tum_taktik_aktorler.append(torrmund_actor)

    aktifler = [d for d in tum_taktik_aktorler if getattr(d, "active", False)]
    if (simdi // 17) % 2:
        aktifler.reverse()
    for dusman in aktifler:
        # Patlama impulse'u aktifken AI steering aynı frame fiziksel savrulmayı
        # geri çekmesin. Burn tick'leri de burada, aktör güncellemesinden önce işler.
        if fire_magic_enemy_status_preupdate(dusman, dt, simdi, tum_taktik_aktorler):
            continue
        dusman.guncelle(
            dt,
            simdi,
            tum_taktik_aktorler,
            common_enemy_oyuncu_hizi,
        )

    # Projectile ve ambient fauna fizik tick'i enemy AI'dan ayrıdır; pathfinding
    # bütçesi tüketmezler. Bu sayede Heads Thrower sayısı artsa bile Theta* frame
    # bütçesi taş animasyonuna harcanmaz.
    enemy_projectiles_guncelle(dt, simdi)
    ambient_rats_guncelle(dt, simdi)
    fire_magic_guncelle(dt, simdi)


def common_enemy_ciz():
    aktorler = list(common_enemies)
    if tarkard_actor is not None and getattr(tarkard_actor, "active", False):
        aktorler.append(tarkard_actor)
    if torrmund_actor is not None and getattr(torrmund_actor, "active", False):
        aktorler.append(torrmund_actor)
    for dusman in sorted(aktorler, key=lambda d: d.y):
        dusman.ciz_govde()
    for dusman in aktorler:
        dusman.ciz_ui()
        dusman.ciz_debug_nav()
# </POTBO_STAGE S0462>

# <POTBO_STAGE S0500>


def combat_darbe_turu(tur):
    return {
        "crawler": "slash",
        "berserker": "shock",
        "headsthrower": "shock",
        "tarkard": "shock_heavy",
        "torrmund": "slash_heavy",
    }.get(str(tur), "shock")
# </POTBO_STAGE S0500>

# <POTBO_STAGE S0505>


def _savunma_sinifi(kaynak_turu):
    tur = str(kaynak_turu).lower()
    if tur in ("tarkard", "torrmund"):
        return "heavy"
    if tur in ("berserker", "headsthrower"):
        return "medium"
    return "light"
# </POTBO_STAGE S0505>

# <POTBO_STAGE S0514>


def _v24_katil_siluet_surface_ve_rect(actor):
    """Katilin mevcut saldırı/idle karesini kırmızı silhouette'e çevirir."""
    if actor is None or not getattr(actor, "active", False):
        return None, None
    simdi = pygame.time.get_ticks()
    frame = _v30_katil_koreografi_frame(actor, simdi)
    if frame is None:
        try:
            _, frame = actor._animasyon_kare(simdi)
        except Exception:
            frame = None
    if frame is None:
        return None, None

    cfg = getattr(actor, "cfg", {}) or {}
    factor = float(cfg.get("sprite_scale", 1.0)) * KAMERA_YAKINLASTIRMA
    size = (
        max(1, int(round(frame.get_width() * factor))),
        max(1, int(round(frame.get_height() * factor))),
    )
    img = pygame.transform.scale(frame, size)
    tur = str(getattr(actor, "tur", ""))
    yon = str(
        getattr(
            actor,
            "visual_direction",
            getattr(actor, "direction", ""),
        )
    )

    # Normal dünya renderer'ındaki orientation kuralları birebir korunur.
    if tur == "crawler":
        if str(getattr(actor, "direction", "left")) == "right":
            img = pygame.transform.flip(img, True, False)
    elif tur in ("headsthrower", "tarkard", "torrmund"):
        if yon == "left":
            img = pygame.transform.flip(img, True, False)

    mask = pygame.mask.from_surface(img)
    sil = mask.to_surface(
        setcolor=(225, 9, 30, 255), unsetcolor=(0, 0, 0, 0)
    ).convert_alpha()
    sx = int(round(dunya_ekran_x(float(getattr(actor, "x", oyuncu_x)))))
    sy = int(round(dunya_ekran_y(float(getattr(actor, "y", oyuncu_y)))))
    return sil, sil.get_rect(midbottom=(sx, sy + 2))
# </POTBO_STAGE S0514>

# <POTBO_STAGE S0519>


def _stage1__v30_oyuncu_ozel_ceset_ciz():
    """True ise corpse render tamamlandı; generic yatay renderer çalışmamalı."""
    alt = str(oyuncu_olum_alt_turu or "")
    if alt not in (
        "crawler",
        "berserker",
        "headshot",
        "tarkard_crush",
        "torrmund_decap",
        "torrmund_decap_cleave",
    ):
        return False
    sil = _v30_oyuncu_base_siluet()
    if sil is None:
        return False
    w, h = sil.get_size()
    e = max(0, pygame.time.get_ticks() - oyuncu_olum_baslangic_ms)

    if alt == "crawler":
        hits = sum(
            1 for k in oyuncu_olum_koreografi_vuruslari if str(k).startswith("crawler_")
        )
        # Ceset yerine oturduktan sonra altı hızlı ısırık giderek küçük parçalar alır.
        # Gövde tamamen yok olmaz; 2., 4. ve 6. darbede üç lokal eksilme oluşur.
        rng = random.Random(int(oyuncu_olum_koreografi_seed or 1))
        for i in range(min(3, hits // 2)):
            side = -1 if (i + oyuncu_olum_koreografi_seed) % 2 else 1
            cy = int(h * rng.uniform(0.34, 0.72))
            rw = max(3, int(w * rng.uniform(0.18, 0.27)))
            rh = max(3, int(h * rng.uniform(0.10, 0.17)))
            cx = int(w * (0.78 if side > 0 else 0.22))
            pygame.draw.ellipse(
                sil,
                (0, 0, 0, 0),
                pygame.Rect(cx - rw // 2, cy - rh // 2, rw, rh),
            )
        _v30_yatan_siluet_yerlestir(sil)
        return True

    if alt == "berserker":
        hits = sum(
            1 for k in oyuncu_olum_koreografi_vuruslari if str(k).startswith("bers_")
        )
        rng = random.Random(int(oyuncu_olum_koreografi_seed or 1) + 91)
        # Daha kesici: 2., 4. ve 6. saldırı küçük çapraz kama koparır.
        for i in range(min(3, hits // 2)):
            y0 = int(h * (0.12 + i * 0.18))
            if (oyuncu_olum_koreografi_seed + i) % 2:
                pts = [
                    (0, y0),
                    (int(w * 0.40), y0 + 2),
                    (int(w * 0.30), min(h, y0 + int(h * 0.18))),
                    (0, min(h, y0 + int(h * 0.13))),
                ]
            else:
                pts = [
                    (int(w * 0.60), y0 + 2),
                    (w, y0),
                    (w, min(h, y0 + int(h * 0.13))),
                    (int(w * 0.70), min(h, y0 + int(h * 0.18))),
                ]
            sil = _v30_surface_bolge_sil(sil, pts)
        _v30_yatan_siluet_yerlestir(sil)
        return True

    if alt == "headshot":
        # Head Thrower kayası: kafa bölgesi yok, boyun altı gövde korunur.
        pygame.draw.ellipse(
            sil,
            (0, 0, 0, 0),
            pygame.Rect(
                int(w * 0.27),
                -2,
                int(w * 0.46),
                max(5, int(h * 0.25)),
            ),
        )
        _v30_yatan_siluet_yerlestir(sil)
        return True

    if alt == "tarkard_crush":
        # Whirl ceset yere oturduktan sonra gelir. Bedenin çoğu kalır ama boss darbesi
        # üç küçük bölgeyi ezer/koparır; "tam sağlam ceset" görünümü kalmaz.
        squash = 1.0
        if 500 <= e <= 1050:
            pulse = math.sin((e - 500) / 550.0 * math.pi)
            squash = 1.0 - 0.16 * max(0.0, pulse)
        if "tarkard_whirl" in oyuncu_olum_koreografi_vuruslari:
            rng = random.Random(int(oyuncu_olum_koreografi_seed or 1) + 404)
            for i in range(3):
                rw = max(3, int(w * rng.uniform(0.13, 0.20)))
                rh = max(3, int(h * rng.uniform(0.08, 0.13)))
                cx = int(w * rng.uniform(0.28, 0.76))
                cy = int(h * rng.uniform(0.28, 0.78))
                pygame.draw.ellipse(
                    sil,
                    (0, 0, 0, 0),
                    pygame.Rect(cx - rw // 2, cy - rh // 2, rw, rh),
                )
        if squash < 0.999:
            sil = pygame.transform.scale(sil, (w, max(2, int(round(h * squash)))))
        _v30_yatan_siluet_yerlestir(sil)
        return True

    if alt in ("torrmund_decap", "torrmund_decap_cleave"):
        # Kafayı gerçek player silhouette'inden ayır. İkinci cleave varsa 1.42 s sonra
        # başsız gövde ayrıca çapraz iki parçaya ayrılır.
        head_h = max(5, int(round(h * 0.24)))
        head_w = max(5, int(round(w * 0.48)))
        head_x = max(0, (w - head_w) // 2)
        head_rect = pygame.Rect(head_x, 0, head_w, head_h).clip(sil.get_rect())
        head = sil.subsurface(head_rect).copy()
        body = sil.copy()
        # Tam üst şeridi değil, kafa çevresindeki oval alanı temizle; omuzlar kalır.
        pygame.draw.ellipse(
            body,
            (0, 0, 0, 0),
            pygame.Rect(
                max(0, head_x - 1),
                -2,
                min(w, head_w + 2),
                head_h + 4,
            ),
        )

        if alt == "torrmund_decap_cleave" and e >= 1420:
            cut = math.radians(float(oyuncu_olum_kesim_acisi))
            cy = h * float(oyuncu_olum_kesim_ofset_orani)
            slope = math.tan(cut)
            ly = cy - slope * w * 0.5
            ry = cy + slope * w * 0.5
            ma = pygame.Surface((w, h), pygame.SRCALPHA)
            mb = pygame.Surface((w, h), pygame.SRCALPHA)
            pygame.draw.polygon(
                ma,
                (255, 255, 255, 255),
                [(0, -h), (w, -h), (w, int(ry)), (0, int(ly))],
            )
            pygame.draw.polygon(
                mb,
                (255, 255, 255, 255),
                [
                    (0, int(ly)),
                    (w, int(ry)),
                    (w, h * 2),
                    (0, h * 2),
                ],
            )
            a, b = body.copy(), body.copy()
            a.blit(ma, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            b.blit(mb, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            q = min(1.0, (e - 1420) / 230.0)
            q = 1.0 - (1.0 - q) ** 3
            normal = pygame.Vector2(-math.sin(cut), math.cos(cut))
            _v30_yatan_siluet_yerlestir(
                a,
                ekstra_rot=-7 * q,
                offset=(-normal.x * 13 * q, -normal.y * 13 * q),
            )
            _v30_yatan_siluet_yerlestir(
                b,
                ekstra_rot=7 * q,
                offset=(normal.x * 13 * q, normal.y * 13 * q),
            )
        else:
            _v30_yatan_siluet_yerlestir(body)

        # Baş gerçek crop olarak boyun noktasından çıkar; tüm beden merkezi etrafında dönmez.
        t = min(1.8, e / 1000.0)
        sign = -1.0 if oyuncu_yonu in ("left", "up") else 1.0
        sx = float(dunya_ekran_x(oyuncu_x))
        sy = float(dunya_ekran_y(oyuncu_y) - 31.0)
        hx = sx + sign * (62.0 * t)
        hy = sy - 86.0 * t + 0.5 * 165.0 * t * t
        hdraw = pygame.transform.rotate(head, 390.0 * t * sign)
        ekran.blit(
            hdraw,
            hdraw.get_rect(center=(int(round(hx)), int(round(hy)))),
        )
        return True

    return False
# </POTBO_STAGE S0519>

# <POTBO_STAGE S0542>


def _gelistirici_x_skill_aktorleri():
    aktorler = list(common_enemies)
    if tarkard_actor is not None:
        aktorler.append(tarkard_actor)
    if torrmund_actor is not None:
        aktorler.append(torrmund_actor)
    return [
        a
        for a in aktorler
        if a is not None
        and getattr(a, "active", False)
        and int(getattr(a, "hp", 0)) > 0
    ]
# </POTBO_STAGE S0542>

# <POTBO_STAGE S0545>


def _gelistirici_x_skill_vur(slot, yon=None):
    """Üç fiziksel dash'in her birini bağımsız ve yalnız bir kez gerçek hit'e çevirir."""
    global gelistirici_x_skill_vurus_maskesi
    slot = int(slot)
    bit = 1 << slot
    if gelistirici_x_skill_vurus_maskesi & bit:
        return
    gelistirici_x_skill_vurus_maskesi |= bit
    hedef = gelistirici_x_skill_hedef
    if (
        hedef is None
        or not getattr(hedef, "active", False)
        or int(getattr(hedef, "hp", 0)) <= 0
    ):
        return

    carpan = GELISTIRICI_X_SKILL_HASAR_CARPANLARI[max(0, min(2, slot))]
    hasar = max(1, int(round(float(oyuncu_hasari) * float(carpan))))
    if yon is None or pygame.Vector2(yon).length_squared() <= 1e-6:
        if slot == 0 and len(gelistirici_x_skill_yol) >= 2:
            yon = gelistirici_x_skill_yol[1] - gelistirici_x_skill_yol[0]
        elif slot == 1:
            yon = pygame.Vector2(1.0, -1.0)
        else:
            yon = pygame.Vector2(1.0, 1.0)
    yon = pygame.Vector2(yon)
    if yon.length_squared() > 1e-6:
        yon = yon.normalize()

    silah_temas_sesi_cal(str(getattr(hedef, "tur", "crawler")))
    hedef.hasar_al(hasar, kaynak="player")
    gucler = (1.78, 2.22, 2.65)
    sarsintilar = ((5.2, 105), (6.8, 132), (9.0, 175))
    idx = max(0, min(2, slot))
    combat_impact_spawn(
        float(hedef.x),
        float(hedef.y) - 14.0,
        "slash_heavy",
        gucler[idx],
        yon,
    )
    kamera_hit_sarsintisi_baslat(sarsintilar[idx][0], sarsintilar[idx][1])
    dunya_olayi_kaydet("developer_x_special_hit", index=slot + 1, damage=hasar)
# </POTBO_STAGE S0545>

# <POTBO_STAGE S0562>


def _v32_katil_temasa_yaklastir(simdi):
    """Post-mortem saldırıdan önce katili gerçek temas menziline getirir.

    CommonEnemy'nin collision-aware hareket çözümünü kullanır; oyuncu artık ölü olduğu
    için yalnız player-body dinamik engeli devre dışıdır. Böylece saldırı karesinde el/
    silah ucu cesede gerçekten ulaşır, fakat katil duvarların içinden geçmez.
    """
    global \
        V32_OLUM_KATIL_READY_MS, \
        V32_OLUM_KATIL_LAST_UPDATE_MS, \
        V32_OLUM_KATIL_CONTACT

    actor = _v24_olum_katil_actor_bul()
    if actor is None:
        if V32_OLUM_KATIL_READY_MS <= 0 and oyuncu_olum_baslangic_ms > 0:
            V32_OLUM_KATIL_READY_MS = max(
                int(simdi),
                int(oyuncu_olum_baslangic_ms) + OLU_CESET_YERLESME_MS,
            )
        return V32_OLUM_KATIL_READY_MS

    tur = str(getattr(actor, "tur", ""))
    # Ranged Head Thrower'ın öldürücü taşı zaten kafa temasını temsil eder; cesede
    # yürütülmez. Torrmund'un ilk öldürücü kılıcı da zaten melee temasındadır.
    if tur not in ("crawler", "berserker", "tarkard"):
        if V32_OLUM_KATIL_READY_MS <= 0 and oyuncu_olum_baslangic_ms > 0:
            V32_OLUM_KATIL_READY_MS = max(
                int(simdi),
                int(oyuncu_olum_baslangic_ms) + OLU_CESET_YERLESME_MS,
            )
        return V32_OLUM_KATIL_READY_MS

    if V32_OLUM_KATIL_LAST_UPDATE_MS <= 0:
        V32_OLUM_KATIL_LAST_UPDATE_MS = int(simdi)
    dt = max(
        0.0,
        min(
            0.045,
            (int(simdi) - int(V32_OLUM_KATIL_LAST_UPDATE_MS)) / 1000.0,
        ),
    )
    V32_OLUM_KATIL_LAST_UPDATE_MS = int(simdi)

    # Cesedin gövde merkezi. Weapon-point fonksiyonundaki yukarı ofsetle aynı dünya
    # düzleminde hedeflenir; merkez-mesafe yerine gerçek el/silah ucunun uzaklığı ölçülür.
    hedef = pygame.Vector2(float(oyuncu_x), float(oyuncu_y) - 14.0)
    merkezden = pygame.Vector2(
        float(oyuncu_x) - float(actor.x),
        float(oyuncu_y) - float(actor.y),
    )
    if merkezden.length_squared() > 1e-6:
        try:
            actor._yonleri_hareketten_guncelle(merkezden, zorla=True)
        except Exception:
            pass

    silah = _v24_katil_silah_kan_noktasi(actor)
    if silah is None:
        silah = pygame.Vector2(float(actor.x), float(actor.y) - 12.0)
    fark = hedef - silah
    temas_esigi = {
        "crawler": 10.5,
        "berserker": 12.5,
        "tarkard": 14.0,
    }.get(tur, 13.0)
    merkez_min = {
        "crawler": 19.0,
        "berserker": 23.0,
        "tarkard": 27.0,
    }.get(tur, 23.0)
    merkez_mesafe = pygame.Vector2(float(actor.x), float(actor.y)).distance_to(
        pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    )

    temas = fark.length() <= temas_esigi or merkez_mesafe <= merkez_min
    if not temas and dt > 0.0 and fark.length_squared() > 1e-6:
        hiz = {
            "crawler": 166.0,
            "berserker": 186.0,
            "tarkard": 154.0,
        }.get(tur, 160.0)
        step = fark.normalize() * min(fark.length(), hiz * dt)
        once = pygame.Vector2(float(actor.x), float(actor.y))
        try:
            actor._hareketi_uygula(
                step.x,
                step.y,
                [],
                hedef_nokta=hedef,
                oyuncuyu_engel_say=False,
            )
        except Exception:
            # Yalnız CommonEnemy navigation metodu bulunmayan özel bir aktör olursa
            # static collision'ı delmeden küçük bir doğrudan nudge denenir.
            nx, ny = (
                float(actor.x) + step.x,
                float(actor.y) + step.y,
            )
            try:
                if common_enemy_statik_konum_gecerli_mi(tur, nx, ny, navigation=False):
                    actor.x, actor.y = nx, ny
            except Exception:
                pass
        sonra = pygame.Vector2(float(actor.x), float(actor.y))
        hareket = sonra - once
        if hareket.length_squared() > 1e-6:
            try:
                actor._yonleri_hareketten_guncelle(hareket, zorla=True)
            except Exception:
                pass

        silah = _v24_katil_silah_kan_noktasi(actor)
        if silah is None:
            silah = pygame.Vector2(float(actor.x), float(actor.y) - 12.0)
        fark = hedef - silah
        merkez_mesafe = pygame.Vector2(float(actor.x), float(actor.y)).distance_to(
            pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
        )
        temas = fark.length() <= temas_esigi or merkez_mesafe <= merkez_min

    if temas:
        V32_OLUM_KATIL_CONTACT = True
        try:
            actor.vx = 0.0
            actor.vy = 0.0
        except Exception:
            pass
        # Saldırı ancak hem ceset yere yerleştikten hem de el/silah temas menziline
        # girdikten sonra başlar. Bu iki koşul aynı anda sağlanmazsa animasyon bekler.
        if int(simdi) >= int(oyuncu_olum_baslangic_ms) + OLU_CESET_YERLESME_MS:
            if V32_OLUM_KATIL_READY_MS <= 0:
                V32_OLUM_KATIL_READY_MS = int(simdi)
    return V32_OLUM_KATIL_READY_MS
# </POTBO_STAGE S0562>

# <POTBO_STAGE S0566>


def _v32_yurume_frame(actor, simdi):
    tur = str(getattr(actor, "tur", ""))
    try:
        if tur == "crawler":
            frames = COMMON_ENEMY_SPRITELERI.get("crawler", {}).get("walk", [])
        elif tur == "berserker":
            frames = (
                COMMON_ENEMY_SPRITELERI.get("berserker", {})
                .get("walk", {})
                .get(
                    str(
                        getattr(
                            actor,
                            "visual_direction",
                            "down_right",
                        )
                    ),
                    [],
                )
            )
        elif tur == "tarkard":
            frames = TARKARD_SPRITELERI.get("walk", [])
        else:
            frames = []
        if frames:
            return frames[(int(simdi) // 92) % len(frames)]
    except Exception:
        pass
    return None


def _stage2__v30_katil_koreografi_frame(actor, simdi):
    """Yaklaşırken walk, temastan sonra gerçek attack zinciri."""
    if actor is None or oyuncu_olum_baslangic_ms <= 0:
        return None
    tur = str(getattr(actor, "tur", ""))
    alt = str(oyuncu_olum_alt_turu or "")

    if tur in ("crawler", "berserker", "tarkard") and alt in (
        "crawler",
        "berserker",
        "tarkard_crush",
    ):
        if V32_OLUM_KATIL_READY_MS <= 0:
            return _v32_yurume_frame(actor, simdi)
        e = _v32_koreografi_gecen(simdi)
        try:
            if tur == "crawler" and 0 <= e < 920:
                frames = COMMON_ENEMY_SPRITELERI.get("crawler", {}).get("attack", [])
                if frames:
                    cycle = 135
                    local = e % cycle
                    return frames[
                        min(
                            len(frames) - 1,
                            int(local / max(1, cycle / len(frames))),
                        )
                    ]
            if tur == "berserker" and 0 <= e < 1040:
                frames = (
                    COMMON_ENEMY_SPRITELERI.get("berserker", {})
                    .get("attack", {})
                    .get(
                        str(
                            getattr(
                                actor,
                                "visual_direction",
                                "right",
                            )
                        ),
                        [],
                    )
                )
                if frames:
                    cycle = 155
                    local = e % cycle
                    return frames[
                        min(
                            len(frames) - 1,
                            int(local / max(1, cycle / len(frames))),
                        )
                    ]
            if tur == "tarkard" and 0 <= e < 900:
                frames = TARKARD_SPRITELERI.get("whirl", [])
                if frames:
                    return frames[
                        min(
                            len(frames) - 1,
                            int(e / max(1, 780 / len(frames))),
                        )
                    ]
        except Exception:
            return None
        return None

    # Torrmund ve ranged headshot'un önceden kurulmuş animasyon kontratını koru.
    return _v31_katil_koreografi_frame(actor, simdi)
# </POTBO_STAGE S0566>

# <POTBO_STAGE S0568>


def _stage1__v32_tirtikli_ceset_ciz(mod="generic"):
    sil = _v30_oyuncu_base_siluet()
    if sil is None:
        return False
    simdi = pygame.time.get_ticks()
    e_abs = max(0, int(simdi) - int(oyuncu_olum_baslangic_ms))
    local = _v32_koreografi_gecen(simdi)
    seed = int(oyuncu_olum_koreografi_seed or oyuncu_olum_ates_seed or 47531)
    rng = random.Random(seed + sum(ord(c) for c in str(mod)) * 19)

    # mod -> (kopma sayısı, yatay/vertical yarıçap aralığı, doğum zamanları)
    if mod == "crawler":
        hits = sum(
            1 for k in oyuncu_olum_koreografi_vuruslari if str(k).startswith("crawler_")
        )
        adet = min(6, hits)
        times = (70, 205, 340, 475, 610, 745)
        rxr, ryr = (0.11, 0.17), (0.055, 0.095)
    elif mod == "berserker":
        hits = sum(
            1 for k in oyuncu_olum_koreografi_vuruslari if str(k).startswith("bers_")
        )
        adet = min(6, hits)
        times = (80, 235, 390, 545, 700, 855)
        rxr, ryr = (0.13, 0.20), (0.065, 0.11)
    elif mod == "tarkard_crush":
        adet = 5 if "tarkard_whirl" in oyuncu_olum_koreografi_vuruslari else 0
        times = (110,) * 5
        rxr, ryr = (0.14, 0.22), (0.07, 0.12)
    elif mod == "headshot":
        adet = 5
        times = (0, 0, 0, 0, 0)
        rxr, ryr = (0.10, 0.17), (0.045, 0.08)
    elif mod == "fire":
        adet = 4 if e_abs >= OLU_CESET_YERLESME_MS else 0
        times = (0, 40, 80, 120)
        rxr, ryr = (0.09, 0.15), (0.05, 0.085)
    else:
        adet = 3 if e_abs >= OLU_CESET_YERLESME_MS else 0
        times = (0, 75, 150)
        rxr, ryr = (0.10, 0.16), (0.055, 0.09)

    body = sil.copy()
    kopanlar = []
    for i in range(adet):
        if mod == "headshot":
            cxr = rng.uniform(0.34, 0.66)
            cyr = rng.uniform(0.05, 0.24)
        else:
            # Parçaları bedenin farklı dış bölgelerine dağıt; birbirini izleyen temiz
            # kesim düzlemleri yerine dağınık yırtılma noktaları oluşur.
            angle = rng.uniform(0.0, math.tau)
            cxr = 0.5 + math.cos(angle) * rng.uniform(0.20, 0.34)
            cyr = 0.53 + math.sin(angle) * rng.uniform(0.18, 0.36)
            cxr = max(0.16, min(0.84, cxr))
            cyr = max(0.10, min(0.88, cyr))
        body, parca, local_pos = _v32_tirtikli_kopar(
            body,
            rng,
            cxr,
            cyr,
            rng.uniform(*rxr),
            rng.uniform(*ryr),
        )
        if pygame.mask.from_surface(parca).count() > 1:
            kopanlar.append(
                (
                    i,
                    parca,
                    local_pos,
                    rng.uniform(-28.0, 28.0),
                    rng.uniform(7.0, 18.0),
                )
            )

    # Tarkard'ın crush hareketinde gövde hafifçe basılır; parçalanma tırtıklı kalır.
    if mod == "tarkard_crush" and local >= 0 and local < 780:
        pulse = math.sin(max(0.0, min(1.0, local / 780.0)) * math.pi)
        if pulse > 0.0:
            bw, bh = body.get_size()
            body = pygame.transform.scale(
                body,
                (
                    bw,
                    max(2, int(round(bh * (1.0 - 0.13 * pulse)))),
                ),
            )

    _v30_yatan_siluet_yerlestir(body)

    for i, parca, local_pos, rot, mesafe in kopanlar:
        birth = int(times[min(i, len(times) - 1)])
        if mod in ("crawler", "berserker", "tarkard_crush"):
            qtime = max(0, local - birth) if local >= 0 else 0
        else:
            qtime = max(0, e_abs - OLU_CESET_YERLESME_MS - birth)
        q = max(0.0, min(1.0, qtime / 230.0))
        q = 1.0 - (1.0 - q) ** 3
        if q <= 0.0 and mod != "headshot":
            continue
        d = pygame.Vector2(local_pos)
        if d.length_squared() <= 1e-6:
            d = pygame.Vector2(1.0, 0.0).rotate(rng.uniform(0.0, 360.0))
        else:
            d = d.normalize()
        # Kopan parça yalnız birkaç piksel ayrılır: beden tanınabilir kalır ama artık
        # kusursuz tek parça değildir. Crawler/Berserker'da vuruş sırasına göre büyür.
        strength = (
            1.15 if mod == "berserker" else (1.35 if mod == "tarkard_crush" else 1.0)
        )
        off = d * mesafe * strength * q
        _v30_yatan_siluet_yerlestir(parca, ekstra_rot=rot * q, offset=(off.x, off.y))
    return True
# </POTBO_STAGE S0568>

# <POTBO_STAGE S0570>


def _stage2__v30_oyuncu_ozel_ceset_ciz():
    """Torrmund dışındaki özel ölümlerde çok noktalı tırtıklı koparma."""
    alt = str(oyuncu_olum_alt_turu or "")
    if alt == "crawler":
        return _v32_tirtikli_ceset_ciz("crawler")
    if alt == "berserker":
        return _v32_tirtikli_ceset_ciz("berserker")
    if alt == "headshot":
        return _v32_tirtikli_ceset_ciz("headshot")
    if alt == "tarkard_crush":
        return _v32_tirtikli_ceset_ciz("tarkard_crush")

    # Torrmund'un kılıcı kasıtlı olarak temiz kesim dilini korur; bu onun silahının
    # ayırt edici infaz karakteridir. Eski fonksiyonun yalnız Torrmund bölümünü burada
    # Bu dal generic corpse renderer tarafından tamamlanır.
    return False
# </POTBO_STAGE S0570>

# <POTBO_STAGE S0575>


def _oyuncu_yatay_siluet_ciz():
    """V32 corpse dispatcher: temiz bisect yalnız Torrmund; diğerleri tırtıklı."""
    # Bombanın ikinci/orta halkası doğrudan blast parçalarıyla görünür.
    if oyuncu_olum_turu == "blast_mid":
        _v32_patlama_siluet_parcalari_ciz("blast_mid")
        return

    alt = str(oyuncu_olum_alt_turu or "")
    if alt in (
        "crawler",
        "berserker",
        "headshot",
        "tarkard_crush",
    ):
        _v30_oyuncu_ozel_ceset_ciz()
        return

    # Torrmund'un iki özel kılıç senaryosu clean sword renderer'ı kullanır.
    # kaybetmemek adına burada özgün mantığa benzer şekilde eski yatay fonksiyonu
    # çağırmak mümkün değildir (isim artık override edildi). Bu yüzden Torrmund'un
    # clean kesimini minimum bir local renderer ile koruyoruz.
    if alt in ("torrmund_decap", "torrmund_decap_cleave"):
        sil = _v30_oyuncu_base_siluet()
        if sil is None:
            return
        w, h = sil.get_size()
        e = max(
            0,
            pygame.time.get_ticks() - oyuncu_olum_baslangic_ms,
        )
        head_h = max(5, int(round(h * 0.24)))
        head_w = max(5, int(round(w * 0.48)))
        head_x = max(0, (w - head_w) // 2)
        head_rect = pygame.Rect(head_x, 0, head_w, head_h).clip(sil.get_rect())
        head = sil.subsurface(head_rect).copy()
        body = sil.copy()
        pygame.draw.ellipse(
            body,
            (0, 0, 0, 0),
            pygame.Rect(
                max(0, head_x - 1),
                -2,
                min(w, head_w + 2),
                head_h + 4,
            ),
        )
        if alt == "torrmund_decap_cleave" and e >= 1420:
            cut = math.radians(float(oyuncu_olum_kesim_acisi))
            cy = h * float(oyuncu_olum_kesim_ofset_orani)
            slope = math.tan(cut)
            ly = cy - slope * w * 0.5
            ry = cy + slope * w * 0.5
            ma = pygame.Surface((w, h), pygame.SRCALPHA)
            mb = pygame.Surface((w, h), pygame.SRCALPHA)
            pygame.draw.polygon(
                ma,
                (255, 255, 255, 255),
                [(0, -h), (w, -h), (w, int(ry)), (0, int(ly))],
            )
            pygame.draw.polygon(
                mb,
                (255, 255, 255, 255),
                [
                    (0, int(ly)),
                    (w, int(ry)),
                    (w, h * 2),
                    (0, h * 2),
                ],
            )
            a, b = body.copy(), body.copy()
            a.blit(ma, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            b.blit(mb, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            q = min(1.0, (e - 1420) / 230.0)
            q = 1.0 - (1.0 - q) ** 3
            normal = pygame.Vector2(-math.sin(cut), math.cos(cut))
            _v30_yatan_siluet_yerlestir(
                a,
                ekstra_rot=-7 * q,
                offset=(-normal.x * 13 * q, -normal.y * 13 * q),
            )
            _v30_yatan_siluet_yerlestir(
                b,
                ekstra_rot=7 * q,
                offset=(normal.x * 13 * q, normal.y * 13 * q),
            )
        else:
            _v30_yatan_siluet_yerlestir(body)
        tt = min(1.8, e / 1000.0)
        sign = -1.0 if oyuncu_yonu in ("left", "up") else 1.0
        sx = float(dunya_ekran_x(oyuncu_x))
        sy = float(dunya_ekran_y(oyuncu_y) - 31.0)
        hx = sx + sign * (62.0 * tt)
        hy = sy - 86.0 * tt + 0.5 * 165.0 * tt * tt
        hdraw = pygame.transform.rotate(head, 390.0 * tt * sign)
        ekran.blit(
            hdraw,
            hdraw.get_rect(center=(int(round(hx)), int(round(hy)))),
        )
        return

    # Torrmund bisect hala oyuncu_olum_ikiye_bolundu flag'iyle gelir. Bu tek durumda
    # Temiz iki düzlemli kılıç kesimi için kısa renderer.
    if oyuncu_olum_ikiye_bolundu and str(oyuncu_olum_katil_tur or "") == "torrmund":
        sil = _v30_oyuncu_base_siluet()
        if sil is None:
            return
        gecen = max(
            0,
            pygame.time.get_ticks() - oyuncu_olum_baslangic_ms,
        )
        ease = (
            1.0
            - (
                1.0
                - max(
                    0.0,
                    min(
                        1.0,
                        gecen / float(OLU_CESET_YERLESME_MS),
                    ),
                )
            )
            ** 3
        )
        w, hh = sil.get_size()
        cut_deg = float(oyuncu_olum_kesim_acisi)
        cut_rad = math.radians(cut_deg)
        merkez_y = max(
            2.0,
            min(
                hh - 2.0,
                hh * float(oyuncu_olum_kesim_ofset_orani),
            ),
        )
        egim = math.tan(cut_rad)
        sol_y = merkez_y - egim * (w * 0.5)
        sag_y = merkez_y + egim * (w * 0.5)
        ma = pygame.Surface((w, hh), pygame.SRCALPHA)
        mb = pygame.Surface((w, hh), pygame.SRCALPHA)
        pygame.draw.polygon(
            ma,
            (255, 255, 255, 255),
            [
                (0, -hh),
                (w, -hh),
                (w, int(sag_y)),
                (0, int(sol_y)),
            ],
        )
        pygame.draw.polygon(
            mb,
            (255, 255, 255, 255),
            [
                (0, int(sol_y)),
                (w, int(sag_y)),
                (w, hh * 2),
                (0, hh * 2),
            ],
        )
        a, b = sil.copy(), sil.copy()
        a.blit(ma, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        b.blit(mb, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        q = max(0.0, min(1.0, gecen / 210.0))
        q = 1.0 - (1.0 - q) ** 3
        normal = pygame.Vector2(-math.sin(cut_rad), math.cos(cut_rad))
        _v30_yatan_siluet_yerlestir(
            a,
            ekstra_rot=-8 * q,
            offset=(-normal.x * 20 * q, -normal.y * 20 * q),
        )
        _v30_yatan_siluet_yerlestir(
            b,
            ekstra_rot=8 * q,
            offset=(normal.x * 20 * q, normal.y * 20 * q),
        )
        return

    # Fire death yalnız gerçek burn tick'inden gelebilir; gövde yine birkaç tırtıklı
    # parçaya ayrılır ama patlama kadar atomize olmaz.
    if oyuncu_olum_turu == "fire":
        _v32_tirtikli_ceset_ciz("fire")
        return

    _v32_tirtikli_ceset_ciz("generic")


# =========================================================
# COMBAT IMPACT + GROUND BLOOD + DEATH MUSIC
# =========================================================
# - zemin kanının mutlak olarak bütün aktörlerin altında çizilmesini,
# - oyuncu hasar flaşını,
# - Crawler'ın gerçek çift temasını ve küçük hit-sekmesini,
# - ölüm sonrası Crawler/Berserker temas koreografisini,
# - Tarkard'ın post-mortem ikinci saldırısının kaldırılmasını,
# - bomba ölüm yarıçapının sıkılaştırılmasını,
# - corpse sprite'ının siyah dikdörtgen üretmeden gerçek alpha parçalarına bölünmesini,
# - daha yoğun fakat kamera-cull dostu kan / organ / kemik üretimini,
# - daha yavaş game-over başlık fade'i ve gameovermusic'i uygular.

# Daha yavaş game-over başlık geçişi. Dört saniyelik saf ölüm tablosu korunur.
OLU_MENU_FADE_IN_MS = 1700
# </POTBO_STAGE S0575>

# <POTBO_STAGE S0583>


# Crawler saldırısında yalnız rüzgârlı impact karesi gerçek temas üretir.
# ilk darbede tüm swing'i kapatıyordu; artık iki ayrı active slot vardır.
_v32_common_saldiri_baslat_v33 = CommonEnemy._saldiri_baslat
_v32_common_saldiri_guncelle_v33 = CommonEnemy._saldiri_guncelle
# </POTBO_STAGE S0583>

# <POTBO_STAGE S0585>


def _v33_common_saldiri_guncelle(self, simdi):
    global oyuncu_hp
    if self.tur != "crawler":
        once_hp = int(oyuncu_hp)
        sonuc = _v32_common_saldiri_guncelle_v33(self, simdi)
        # Berserker'ın normal vuruşu da birkaç piksellik gövde tepkisi üretir.
        # Tarkard'ın kendi ağır knockback'i ve Torrmund'un sabit kesişi burada ezilmez.
        if self.tur == "berserker" and int(oyuncu_hp) > 0 and int(oyuncu_hp) < once_hp:
            _v33_oyuncu_kucuk_sektir(self.x, self.y, 66.0, 108)
        return sonuc
    if not self.attacking:
        return False

    kare = self._attack_frame_index(simdi)
    aktif_bas, aktif_son = self._attack_active_frame_araligi()
    slots = getattr(self, "attack_player_hit_slots", None)
    if slots is None:
        slots = set()
        self.attack_player_hit_slots = slots

    if aktif_bas <= kare <= aktif_son:
        enemy_friendly_melee_vur(self, simdi)
        orta = (aktif_bas + aktif_son) // 2
        slot = 0 if kare <= orta else 1
        if slot not in slots and self._attack_temas_var_mi(simdi):
            los = common_enemy_saldiri_los_acik_mi(self)
            if los and oyuncu_hp > 0:
                if oyuncu_savunma_darbe_karsila(self.tur, self.x, self.y, self):
                    slots.add(slot)
                    self.attack_connected = True
                    self.last_pressure_ms = simdi
                else:
                    profil = darbe_profili_belirle(self, "player")
                    hasar = int(self.cfg["attack_damage"])
                    oyuncu_hp = max(0, oyuncu_hp - hasar)
                    oyuncu_kanli_hasar_kaydi(self.x, self.y, profil, hasar, self.name)
                    slots.add(slot)
                    self.attack_connected = True
                    self.last_pressure_ms = simdi
                    dunya_olayi_kaydet(
                        "hit_taken",
                        damage=hasar,
                        count=1,
                        enemy=self.tur,
                    )
                    combat_impact_spawn(
                        oyuncu_x,
                        oyuncu_y - 12,
                        "slash",
                        0.98 if slot == 0 else 1.12,
                        pygame.Vector2(oyuncu_x - self.x, oyuncu_y - self.y),
                    )
                    kamera_hit_sarsintisi_baslat(2.7 if slot == 0 else 3.4, 105)
                    # İlk temas çok küçük; ikinci temas biraz daha okunur. İkinci hit'i
                    # menzil dışına itmeyecek kadar kısadır.
                    _v33_oyuncu_kucuk_sektir(
                        self.x,
                        self.y,
                        34.0 if slot == 0 else 52.0,
                        72 if slot == 0 else 96,
                    )
                    bildirim_goster(
                        bt(
                            f"{self.name} sana -{hasar} hasar verdi.",
                            f"{self.name} dealt -{hasar} damage.",
                        ),
                        PARLAK_KIRMIZI,
                    )

    if kare > aktif_son:
        self.attack_damage_applied = True
    else:
        self.attack_damage_applied = len(slots) >= 2

    if simdi - self.attack_started_ms >= self._attack_total_ms():
        self.attacking = False
        self.attack_damage_applied = False
        recovery = int(self.cfg.get("attack_recovery_ms", 180))
        if not self.attack_connected:
            recovery = int(recovery * 1.08)
        self.recovery_until = simdi + recovery
        self.attack_player_hit_slots = set()
    return True


CommonEnemy._saldiri_baslat = _v33_common_saldiri_baslat
CommonEnemy._saldiri_guncelle = _v33_common_saldiri_guncelle

# Heads Thrower taşı da küçük fiziksel sekme üretir; özel heavy boss knockback'lerine
# dokunulmaz. Projectile sınıfının orijinal impact'ini yeniden yazmak yerine kill kayıt
# Kaynak adı üzerinden kan kaydı wrapper'ında ekstra itme uygulanmaz;
# taşın kendi impact'i için minimal wrapper kullanılır.
_v32_rock_impact_v33 = HeadsThrowerRockProjectile._impact
# </POTBO_STAGE S0585>

# <POTBO_STAGE S0587>


HeadsThrowerRockProjectile._impact = _v33_rock_impact
# </POTBO_STAGE S0587>

# <POTBO_STAGE S0591>


# Tarkard death renderer, ölüm sonrası yeni whirl başlatmaz. İlk lethal saldırının
# frozen/current frame'i actor._animasyon_kare fallback'iyle görünür.
_v32_katil_frame_v33 = _v30_katil_koreografi_frame


def _v30_katil_koreografi_frame(actor, simdi):
    if (
        actor is not None
        and str(getattr(actor, "tur", "")) == "tarkard"
        and str(oyuncu_olum_alt_turu or "") == "tarkard_crush"
    ):
        return None
    return _v32_katil_frame_v33(actor, simdi)
# </POTBO_STAGE S0591>

# <POTBO_STAGE S0595>


def _v33_tirtikli_ceset_ciz(mod="generic"):
    sil = _v30_oyuncu_base_siluet()
    if sil is None:
        return False
    simdi = pygame.time.get_ticks()
    e_abs = max(0, simdi - int(oyuncu_olum_baslangic_ms))
    local = _v32_koreografi_gecen(simdi)
    seed = int(oyuncu_olum_koreografi_seed or oyuncu_olum_ates_seed or 47531)
    rng = random.Random(seed + sum(ord(c) for c in str(mod)) * 23)

    # Her ölümde beden gerçekten birkaç alpha parçasına ayrılır. Crawler/Berserker
    # ceset yerleştikten sonra her gerçek post-mortem hit'te bir yeni kopma ekler.
    if mod == "crawler":
        hits = sum(
            1 for k in oyuncu_olum_koreografi_vuruslari if str(k).startswith("crawler_")
        )
        adet = 2 + min(6, hits)
        times = (0, 40, 70, 205, 340, 475, 610, 745)
        rxr, ryr = (0.085, 0.145), (0.045, 0.082)
    elif mod == "berserker":
        hits = sum(
            1 for k in oyuncu_olum_koreografi_vuruslari if str(k).startswith("bers_")
        )
        adet = 3 + min(6, hits)
        times = (0, 30, 60, 80, 235, 390, 545, 700, 855)
        rxr, ryr = (0.10, 0.17), (0.052, 0.095)
    elif mod == "tarkard_crush":
        # Post-mortem saldırı yok: parçalanma doğrudan ölümcül ilk darbenin sonucudur.
        adet = 8 if e_abs >= OLU_CESET_YERLESME_MS else 0
        times = (0, 0, 20, 35, 50, 70, 90, 110)
        rxr, ryr = (0.11, 0.19), (0.06, 0.105)
    elif mod == "headshot":
        adet = 7 if e_abs >= 90 else 0
        times = (0, 0, 20, 35, 50, 70, 90)
        rxr, ryr = (0.09, 0.16), (0.042, 0.078)
    elif mod == "fire":
        adet = 5 if e_abs >= OLU_CESET_YERLESME_MS else 0
        times = (0, 35, 70, 105, 140)
        rxr, ryr = (0.075, 0.13), (0.044, 0.075)
    else:
        adet = 4 if e_abs >= OLU_CESET_YERLESME_MS else 0
        times = (0, 45, 90, 135)
        rxr, ryr = (0.085, 0.145), (0.048, 0.082)

    body = sil.copy()
    kopanlar = []
    w, h = sil.get_size()
    for i in range(adet):
        if mod == "headshot":
            cxr = rng.uniform(0.31, 0.69)
            cyr = rng.uniform(0.04, 0.25)
        else:
            angle_seed = rng.uniform(0.0, math.tau)
            cxr = 0.5 + math.cos(angle_seed) * rng.uniform(0.20, 0.35)
            cyr = 0.52 + math.sin(angle_seed) * rng.uniform(0.18, 0.37)
            cxr = max(0.14, min(0.86, cxr))
            cyr = max(0.09, min(0.90, cyr))
        body, parca, local_pos = _v32_tirtikli_kopar(
            body,
            rng,
            cxr,
            cyr,
            rng.uniform(*rxr),
            rng.uniform(*ryr),
        )
        if pygame.mask.from_surface(parca, 1).count() > 1:
            kopanlar.append(
                (
                    i,
                    parca,
                    local_pos,
                    rng.uniform(-34.0, 34.0),
                    rng.uniform(8.0, 22.0),
                    rng.uniform(-18.0, 18.0),
                )
            )

    # Ana gövde de crop edilerek çizilir; full-canvas siyah/şeffaf kutu ASLA blit edilmez.
    _v33_full_piece_ciz(body, simdi=simdi)

    for i, parca, local_pos, rot, mesafe, tangent in kopanlar:
        birth = int(times[min(i, len(times) - 1)])
        if mod in ("crawler", "berserker") and i >= (2 if mod == "crawler" else 3):
            qtime = max(0, local - birth) if local >= 0 else 0
        else:
            qtime = max(0, e_abs - OLU_CESET_YERLESME_MS - birth)
        q = max(0.0, min(1.0, qtime / 255.0))
        q = 1.0 - (1.0 - q) ** 3
        d = pygame.Vector2(local_pos)
        if d.length_squared() <= 1e-6:
            d = pygame.Vector2(1.0, 0.0).rotate(rng.uniform(0.0, 360.0))
        d = d.normalize().rotate(tangent)
        strength = (
            1.28 if mod == "berserker" else (1.48 if mod == "tarkard_crush" else 1.0)
        )
        off = d * mesafe * strength * q
        _v33_full_piece_ciz(
            parca,
            extra_offset=off,
            extra_rot=rot * q,
            simdi=simdi,
        )
    return True
# </POTBO_STAGE S0595>

# <POTBO_STAGE S0598>


# Generic corpse dispatcher'ı yeniden bağla: Torrmund clean blade özel kalır; diğer
# Bu ölümler tırtıklı actual-alpha parçalarını kullanır.
def _v30_oyuncu_ozel_ceset_ciz():
    alt = str(oyuncu_olum_alt_turu or "")
    if alt == "crawler":
        return _v33_tirtikli_ceset_ciz("crawler")
    if alt == "berserker":
        return _v33_tirtikli_ceset_ciz("berserker")
    if alt == "headshot":
        return _v33_tirtikli_ceset_ciz("headshot")
    if alt == "tarkard_crush":
        return _v33_tirtikli_ceset_ciz("tarkard_crush")
    return False
# </POTBO_STAGE S0598>

# <POTBO_STAGE S0604>


# =========================================================
# TORRMUND FINISHERS + CRAWLER IMPACT + DEATH TIMELINE
# =========================================================
# - Crawler yalnız sheet'teki büyük rüzgâr yayı karesinde tek kez hasar verir.
# - Torrmund'a eski, tek darbede merkezden ikiye ayıran finisher geri eklenir.
# - Başlık daima "YOU ARE DEAD"; 3.6 sn sonra görünmeye başlar.
# - Başlık ilk görünür pikselinde gameovermusic başlar, en fazla 10 sn çalar.
# - Müzik penceresi bittikten sonra butonlar 1.6 sn'de fade-in olur.
# - Death -> Load -> ESC aynı ölüm tablosuna döner.
# - Death -> Main Menu aynı tablonun üzerinde ARE YOU SURE? ister.

V34_DEATH_TITLE_DELAY_MS = 3600
# </POTBO_STAGE S0604>

# <POTBO_STAGE S0614>


# ---------------------------------------------------------
# CRAWLER: tek gerçek impact, büyük wind-arc frame (raw attack index 12)
# ---------------------------------------------------------
_v33_common_saldiri_guncelle_v34 = CommonEnemy._saldiri_guncelle


def _v34_common_saldiri_guncelle(self, simdi):
    global oyuncu_hp
    if self.tur != "crawler":
        return _v33_common_saldiri_guncelle_v34(self, simdi)
    if not self.attacking:
        return False

    kare = self._attack_frame_index(simdi)
    aktif_bas, aktif_son = self._attack_active_frame_araligi()  # V34: (12, 12)

    # Yalnız büyük rüzgâr yayı karesi fiziksel saldırıdır. Hazırlık pozları ve yere
    # kapanma/recovery kareleri hitbox üretmez. Tek swing = tek hasar olayı.
    if aktif_bas <= kare <= aktif_son:
        enemy_friendly_melee_vur(self, simdi)
        if not self.attack_connected and self._attack_temas_var_mi(simdi):
            los = common_enemy_saldiri_los_acik_mi(self)
            if los and oyuncu_hp > 0:
                if oyuncu_savunma_darbe_karsila(self.tur, self.x, self.y, self):
                    self.attack_connected = True
                    self.attack_damage_applied = True
                    self.last_pressure_ms = simdi
                else:
                    profil = darbe_profili_belirle(self, "player")
                    hasar = int(self.cfg["attack_damage"])
                    oyuncu_hp = max(0, oyuncu_hp - hasar)
                    oyuncu_kanli_hasar_kaydi(self.x, self.y, profil, hasar, self.name)
                    self.attack_connected = True
                    self.attack_damage_applied = True
                    self.last_pressure_ms = simdi
                    dunya_olayi_kaydet(
                        "hit_taken",
                        damage=hasar,
                        count=1,
                        enemy=self.tur,
                    )
                    combat_impact_spawn(
                        oyuncu_x,
                        oyuncu_y - 12,
                        "slash",
                        1.12,
                        pygame.Vector2(oyuncu_x - self.x, oyuncu_y - self.y),
                    )
                    kamera_hit_sarsintisi_baslat(3.5, 112)
                    _v33_oyuncu_kucuk_sektir(self.x, self.y, 48.0, 92)
                    bildirim_goster(
                        bt(
                            f"{self.name} sana -{hasar} hasar verdi.",
                            f"{self.name} dealt -{hasar} damage.",
                        ),
                        PARLAK_KIRMIZI,
                    )

    if kare > aktif_son:
        self.attack_damage_applied = True

    if simdi - self.attack_started_ms >= self._attack_total_ms():
        self.attacking = False
        self.attack_damage_applied = False
        recovery = int(self.cfg.get("attack_recovery_ms", 180))
        if not self.attack_connected:
            recovery = int(recovery * 1.08)
        self.recovery_until = simdi + recovery
        self.attack_player_hit_slots = set()
    return True


CommonEnemy._saldiri_guncelle = _v34_common_saldiri_guncelle


# ---------------------------------------------------------
# TORRMUND: üçüncü finisher = eski merkezden tek-vuruş bisect
# ---------------------------------------------------------
def _v30_olum_koreografi_hazirla(katil_tur, profil, kaynak_adi=""):
    global oyuncu_olum_alt_turu, oyuncu_olum_koreografi_seed
    global oyuncu_olum_torrmund_senaryo, oyuncu_olum_ikiye_bolundu
    global oyuncu_olum_kesim_acisi, oyuncu_olum_kesim_ofset_orani

    tur = str(katil_tur or "").lower()
    oyuncu_olum_koreografi_seed = random.randint(1, 2_000_000)
    oyuncu_olum_torrmund_senaryo = ""

    if tur == "crawler":
        oyuncu_olum_alt_turu = "crawler"
        oyuncu_olum_ikiye_bolundu = False
    elif tur == "berserker":
        oyuncu_olum_alt_turu = "berserker"
        oyuncu_olum_ikiye_bolundu = False
    elif tur == "headsthrower":
        oyuncu_olum_alt_turu = "headshot"
        oyuncu_olum_ikiye_bolundu = False
    elif tur == "tarkard":
        oyuncu_olum_alt_turu = "tarkard_crush"
        oyuncu_olum_ikiye_bolundu = False
    elif tur == "torrmund":
        rng = random.Random(oyuncu_olum_koreografi_seed)
        roll = rng.random()
        if roll < 0.28:
            # ek finisher: eski ölümün daha merkezî, neredeyse yatay temiz kesimi.
            # Tek lethal vuruştur; post-mortem ikinci saldırı yoktur.
            oyuncu_olum_torrmund_senaryo = "center_bisect"
            oyuncu_olum_alt_turu = "torrmund_center_bisect"
            oyuncu_olum_ikiye_bolundu = True
            oyuncu_olum_kesim_acisi = rng.uniform(-5.0, 5.0)
            oyuncu_olum_kesim_ofset_orani = rng.uniform(0.492, 0.518)
        elif roll < 0.62:
            # Mevcut çapraz bisect korunur.
            oyuncu_olum_torrmund_senaryo = "bisect"
            oyuncu_olum_alt_turu = "torrmund_bisect"
            oyuncu_olum_ikiye_bolundu = True
            oyuncu_olum_kesim_acisi = rng.uniform(14.0, 32.0) * rng.choice((-1.0, 1.0))
            oyuncu_olum_kesim_ofset_orani = rng.uniform(0.48, 0.57)
        else:
            # Kafa uçurma; yalnız bu dal bazen farklı heavy cleave ile devam eder.
            ikinci = rng.random() < 0.46
            oyuncu_olum_torrmund_senaryo = "decap_cleave" if ikinci else "decap"
            oyuncu_olum_alt_turu = (
                "torrmund_decap_cleave" if ikinci else "torrmund_decap"
            )
            oyuncu_olum_ikiye_bolundu = False
            oyuncu_olum_kesim_acisi = rng.uniform(14.0, 32.0) * rng.choice((-1.0, 1.0))
            oyuncu_olum_kesim_ofset_orani = rng.uniform(0.48, 0.57)
    else:
        oyuncu_olum_alt_turu = ""
# </POTBO_STAGE S0614>

# <POTBO_STAGE S0645>


def _v34_dynamic_blockers(exclude=None):
    """Oyuncu için yumuşak body blocker listesi.

    Dynamic aktörler normal yürüyüşte katıdır; ancak mevcut overlap'tan dışarı
    çıkmaya çalışan hareket engellenmez. Special move bunları bilinçli olarak
    görmezden gelir, çünkü tekniğin amacı düşmanın bedeninin içinden geçmektir.
    """
    result = []
    for actor in common_enemies:
        if actor is exclude:
            continue
        if getattr(actor, "active", False):
            result.append(common_enemy_carpisma_rect(actor))
    for actor in (tarkard_actor, torrmund_actor):
        if actor is None or actor is exclude:
            continue
        if getattr(actor, "active", False):
            result.append(common_enemy_carpisma_rect(actor))
    return result
# </POTBO_STAGE S0645>

# <POTBO_STAGE S0710>


# Orijinal CommonEnemy.hasar_al referansını wrapper ile AYNI isimde tutma.
# Aksi halde wrapper tanımı bu adı yeniden bağlayıp ilk hasarda kendini çağırır
# ve RecursionError üretir. Attribute işareti wrapper'ı idempotent de yapar;
# geliştirme sırasında aynı patch ikinci kez çalıştırılsa bile wrapper zincirlenmez.
_v34c_commonenemy_hasar_al_original = getattr(
    CommonEnemy.hasar_al,
    "_v34_original_hasar_al",
    CommonEnemy.hasar_al,
)


def _v34c_commonenemy_hasar_al_wrapper(self, miktar, kaynak=None):
    before_hp = int(getattr(self, "hp", 0))
    before_active = bool(getattr(self, "active", False))
    result = _v34c_commonenemy_hasar_al_original(self, miktar, kaynak)
    after_hp = int(getattr(self, "hp", 0))
    after_active = bool(getattr(self, "active", False))
    if _v34_source_is_player_damage(kaynak) and before_hp > after_hp:
        actual = max(0, before_hp - after_hp)
        killed = before_active and not after_active
        _v34_combo_register_hit(actual, killed=killed)
    return result


_v34c_commonenemy_hasar_al_wrapper._v34_original_hasar_al = (
    _v34c_commonenemy_hasar_al_original
)
CommonEnemy.hasar_al = _v34c_commonenemy_hasar_al_wrapper
# </POTBO_STAGE S0710>

# <POTBO_STAGE S0714>


def _v34_actor_list():
    actors = [a for a in common_enemies if getattr(a, "active", False)]
    for a in (tarkard_actor, torrmund_actor):
        if a is not None and getattr(a, "active", False):
            actors.append(a)
    return actors


def _v34_actor_move_static_safe(actor, candidate, others, ignore_player=False):
    """Actor'ın mevcut navigation checker'ını kullanarak küçük separation adımı uygular."""
    try:
        return bool(
            actor._hareket_gecerli(
                candidate.x,
                candidate.y,
                others,
                oyuncuyu_engel_say=not ignore_player,
            )
        )
    except (AttributeError, TypeError):
        # Fallback yalnız static world query; body footprint için enemy helper kullanılır.
        try:
            return bool(
                _common_enemy_hizli_statik_gecerli_mi(
                    actor.tur, candidate.x, candidate.y
                )
            )
        except Exception:
            return False


def _v34_push_actor_from_player(actor, actors):
    global v34_crowd_player_separations
    player_rect = oyuncu_carpisma_rect(oyuncu_x, oyuncu_y)
    rect = common_enemy_carpisma_rect(actor)
    if not rect.colliderect(player_rect):
        return False
    overlap = _v34_rect_overlap_alani(rect, player_rect)
    min_area = max(
        1,
        min(
            rect.width * rect.height,
            player_rect.width * player_rect.height,
        ),
    )
    if overlap / min_area < V34_CROWD_MIN_OVERLAP_RATIO:
        return False

    away = pygame.Vector2(
        float(actor.x) - float(oyuncu_x),
        float(actor.y) - float(oyuncu_y),
    )
    if away.length_squared() <= 1e-6:
        away = pygame.Vector2(1.0, 0.0).rotate(
            (hash(str(getattr(actor, "uid", ""))) % 360)
        )
    away = away.normalize()
    candidate = (
        pygame.Vector2(float(actor.x), float(actor.y)) + away * V34_CROWD_PLAYER_PUSH
    )
    others = [a for a in actors if a is not actor]
    if _v34_actor_move_static_safe(actor, candidate, others, ignore_player=True):
        actor.x = float(candidate.x)
        actor.y = float(candidate.y)
        try:
            actor.vx += away.x * 18.0
            actor.vy += away.y * 18.0
        except Exception:
            pass
        v34_crowd_player_separations += 1
        return True
    return False


def _v34_push_actor_pair(a, b, actors):
    global v34_crowd_pair_separations
    ra = common_enemy_carpisma_rect(a)
    rb = common_enemy_carpisma_rect(b)
    if not ra.colliderect(rb):
        return False
    overlap = _v34_rect_overlap_alani(ra, rb)
    min_area = max(1, min(ra.width * ra.height, rb.width * rb.height))
    if overlap / min_area < V34_CROWD_MIN_OVERLAP_RATIO:
        return False

    delta = pygame.Vector2(float(a.x) - float(b.x), float(a.y) - float(b.y))
    if delta.length_squared() <= 1e-6:
        seed = (
            hash(str(getattr(a, "uid", "a"))) ^ hash(str(getattr(b, "uid", "b")))
        ) % 360
        delta = pygame.Vector2(1.0, 0.0).rotate(seed)
    direction = delta.normalize()
    moved = False

    # Her aktör diğerini geçici olarak blocker listesinden çıkarır; amaç mevcut
    # interpenetration'ı azaltmaktır. Diğer bütün aktörler ve static world korunur.
    others_a = [x for x in actors if x is not a and x is not b]
    ca = pygame.Vector2(float(a.x), float(a.y)) + direction * V34_CROWD_PAIR_PUSH
    if _v34_actor_move_static_safe(a, ca, others_a, ignore_player=False):
        a.x = float(ca.x)
        a.y = float(ca.y)
        moved = True

    others_b = [x for x in actors if x is not a and x is not b]
    cb = pygame.Vector2(float(b.x), float(b.y)) - direction * V34_CROWD_PAIR_PUSH
    if _v34_actor_move_static_safe(b, cb, others_b, ignore_player=False):
        b.x = float(cb.x)
        b.y = float(cb.y)
        moved = True

    if moved:
        v34_crowd_pair_separations += 1
    return moved
# </POTBO_STAGE S0714>

# <POTBO_STAGE S0716>


_v34c_common_enemy_guncelle = common_enemy_guncelle


def common_enemy_guncelle():
    result = _v34c_common_enemy_guncelle()
    v34_crowd_separation_tick()
    return result
# </POTBO_STAGE S0716>

# <POTBO_STAGE S0738>


def _v34_fix_actor_numbers():
    fixed = False
    for actor in _v34_actor_list():
        if _v34_value_is_finite(getattr(actor, "x", None)) and _v34_value_is_finite(
            getattr(actor, "y", None)
        ):
            continue
        # Non-finite AI coordinate'u pathfinder'a göndermek bütün navigation cache'ini
        # zehirleyebilir. Oyuncudan uzağa, fakat harita içinde en yakın static-safe nokta.
        base = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
        found = None
        for radius in (90, 120, 160, 220, 300):
            for angle in range(0, 360, 30):
                p = base + pygame.Vector2(radius, 0.0).rotate(angle)
                try:
                    if _common_enemy_hizli_statik_gecerli_mi(actor.tur, p.x, p.y):
                        found = p
                        break
                except Exception:
                    pass
            if found is not None:
                break
        if found is not None:
            actor.x = float(found.x)
            actor.y = float(found.y)
            try:
                actor.vx = 0.0
                actor.vy = 0.0
            except Exception:
                pass
            fixed = True
    return fixed
# </POTBO_STAGE S0738>

# <POTBO_STAGE S0747>


def _v34_interaction_candidates():
    player = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    candidates = []

    if (
        torrmund_actor is not None
        and getattr(torrmund_actor, "active", False)
        and not getattr(torrmund_actor, "aggro", False)
    ):
        pos = pygame.Vector2(float(torrmund_actor.x), float(torrmund_actor.y))
        dx = abs(player.x - pos.x) / (92.0 * V34_INTERACTION_GRACE)
        dy = abs(player.y - pos.y) / (72.0 * V34_INTERACTION_GRACE)
        if dx <= 1.0 and dy <= 1.0:
            candidates.append(
                _v34_interaction_candidate(
                    "torrmund",
                    torrmund_actor,
                    pos.x,
                    pos.y,
                    player.distance_to(pos),
                    torrmund_konusmasini_baslat,
                )
            )

    if (
        tarkard_actor is not None
        and getattr(tarkard_actor, "active", False)
        and not getattr(tarkard_actor, "aggro", False)
    ):
        pos = pygame.Vector2(float(tarkard_actor.x), float(tarkard_actor.y))
        # Tarkard'ın mevcut yakin_mi kontratını koru; yalnız score nearest olur.
        if tarkard_yakin_mi():
            candidates.append(
                _v34_interaction_candidate(
                    "tarkard",
                    tarkard_actor,
                    pos.x,
                    pos.y,
                    player.distance_to(pos),
                    tarkard_konusmasini_baslat,
                )
            )

    mpos = pygame.Vector2(float(merchant_x), float(merchant_y))
    # Merchant helper zaten collision dışında etkileşim menzilini ayarlıyor.
    if merchant_yakin_mi():
        candidates.append(
            _v34_interaction_candidate(
                "merchant",
                None,
                mpos.x,
                mpos.y,
                player.distance_to(mpos),
                merchant_ac,
            )
        )

    if npc_intro_tamamlandi and not ganimet_alindi:
        gpos = pygame.Vector2(float(ganimet_x), float(ganimet_y))
        if (
            abs(player.x - gpos.x) < 40.0 * V34_INTERACTION_GRACE
            and abs(player.y - gpos.y) < 36.0 * V34_INTERACTION_GRACE
        ):
            # Loot biraz yüksek priority; doğrudan ayağın altındaki ganimet NPC konuşmasına yenilmez.
            candidates.append(
                _v34_interaction_candidate(
                    "loot",
                    None,
                    gpos.x,
                    gpos.y,
                    max(0.0, player.distance_to(gpos) - 8.0),
                    ganimeti_al,
                )
            )

    npos = pygame.Vector2(float(npc_x), float(npc_y))
    ndx = (player.x - npos.x) / (82.0 * V34_INTERACTION_GRACE)
    ndy = (player.y - npos.y) / (62.0 * V34_INTERACTION_GRACE)
    if ndx * ndx + ndy * ndy <= 1.0:
        candidates.append(
            _v34_interaction_candidate(
                "eadric",
                None,
                npos.x,
                npos.y,
                player.distance_to(npos),
                npc_konusmasini_baslat,
            )
        )

    candidates.sort(key=lambda c: c["score"])
    return candidates
# </POTBO_STAGE S0747>

# <POTBO_STAGE S0823>

# Enemy attack contact gate: AI saldırıya biraz önceden hazırlanabilir, fakat gerçek
# damage ancak gövde/silah oyuncuya makul mesafeye geldiğinde bağlanır.
V35_ENEMY_ACTIVE_ROOT_LIMIT = {
    "crawler": 54.0,
    "berserker": 61.0,
    "tarkard": 80.0,
    "torrmund": 82.0,
}
V35_ENEMY_START_ROOT_LIMIT = {
    "crawler": 66.0,
    "berserker": 73.0,
    "tarkard": 94.0,
    "torrmund": 96.0,
}
V35_ENEMY_SWEEP = {
    "crawler": (52.0, 14.0),
    "berserker": (59.0, 17.0),
    "tarkard": (80.0, 21.0),
    "torrmund": (84.0, 19.0),
}
V35_FRIENDLY_CENTER_LIMIT = {
    "crawler": 78.0,
    "berserker": 86.0,
    "tarkard": 112.0,
    "torrmund": 114.0,
}
# </POTBO_STAGE S0823>

# <POTBO_STAGE S0825>


def _v35_enemy_root(self):
    body_h = float(self.cfg.get("body_height", 22.0))
    return pygame.Vector2(float(self.x), float(self.y) - body_h * 0.64)


def _v35_enemy_attack_contact_gate(self, baslangic=False):
    """Damage gate'i sprite merkezinden değil oyuncu hurtbox'ının en yakın noktasından ölçer."""
    hurt = oyuncu_savas_hurtbox_rect(oyuncu_x, oyuncu_y)
    origin = _v35_enemy_root(self)
    nearest = _rect_en_yakin_nokta(hurt, origin)
    root_dist = origin.distance_to(nearest)
    tur = str(getattr(self, "tur", ""))
    limits = V35_ENEMY_START_ROOT_LIMIT if baslangic else V35_ENEMY_ACTIVE_ROOT_LIMIT
    limit = float(limits.get(tur, 70.0 if baslangic else 60.0))
    if root_dist > limit:
        return False

    # Çok yakın beden teması yön cone'una takılmaz; karakterler gerçekten çarpışmıştır.
    body = self.collision_rect().inflate(8, 22)
    if body.colliderect(hurt):
        return True

    variant = str(getattr(self, "attack_variant", ""))
    if tur == "tarkard" and variant == "whirl":
        return root_dist <= (90.0 if baslangic else 72.0)

    facing = _common_enemy_yon_vektoru(self.direction)
    if facing.length_squared() <= 1e-6:
        return False
    facing = facing.normalize()
    delta = pygame.Vector2(hurt.center) - origin
    if delta.length_squared() <= 1e-6:
        return True
    dot = facing.dot(delta.normalize())
    # Startup daha belirgin ön-yüz ister. Active arc ise yan tarafta gerçekten geçen
    # kılıcı kaçırmamak için daha geniş ama arkaya vurmayan bir cone kullanır.
    threshold = 0.10 if baslangic else -0.06
    if tur in ("tarkard", "torrmund") and not baslangic:
        threshold = -0.12
    return dot >= threshold


def _v35_enemy_attack_contact(self, simdi):
    if not _v35_enemy_attack_contact_gate(self, baslangic=False):
        return False

    hurt = oyuncu_savas_hurtbox_rect(oyuncu_x, oyuncu_y)
    body = self.collision_rect()
    if body.inflate(10, 20).colliderect(hurt):
        return True

    tur = str(getattr(self, "tur", ""))
    facing = _common_enemy_yon_vektoru(self.direction)
    if facing.length_squared() <= 1e-6:
        facing = pygame.Vector2(1.0, 0.0)
    facing = facing.normalize()
    origin = _v35_enemy_root(self)

    frame = self._attack_frame_index(simdi)
    active_start, active_end = self._attack_active_frame_araligi()
    span = max(1.0, float(active_end - active_start + 1))
    p = max(0.0, min(1.0, (frame - active_start + 0.5) / span))
    variant = str(getattr(self, "attack_variant", ""))

    if tur == "tarkard" and variant == "whirl":
        # Dairesel saldırı görsel olarak 360 derecedir fakat radius artık yalnız
        # beden yakınındaki gerçek halka alanını kapsar.
        nearest = _rect_en_yakin_nokta(hurt, origin)
        return origin.distance_to(nearest) <= 70.0

    reach, radius = V35_ENEMY_SWEEP.get(tur, (64.0, 17.0))
    if tur == "crawler":
        sweep = (-9.0, 0.0, 9.0)
    elif tur == "berserker":
        center_angle = -44.0 + 86.0 * p
        sweep = (
            center_angle - 9.0,
            center_angle,
            center_angle + 9.0,
        )
    elif tur == "tarkard":
        center_angle = -31.0 + 61.0 * p
        sweep = (
            center_angle - 8.0,
            center_angle,
            center_angle + 8.0,
        )
    elif tur == "torrmund" and variant == "cleave":
        center_angle = -22.0 + 44.0 * p
        sweep = (
            center_angle - 7.0,
            center_angle,
            center_angle + 7.0,
        )
    elif tur == "torrmund":
        center_angle = -38.0 + 74.0 * p
        sweep = (
            center_angle - 8.0,
            center_angle,
            center_angle + 8.0,
        )
    else:
        sweep = (0.0,)

    for angle in sweep:
        direction = facing.rotate(angle)
        start = origin + direction * 10.0
        end = origin + direction * reach
        if _kapsul_rect_kesisiyor(hurt, start, end, radius):
            return True
    return False


# Class metotlarını bir kere V35 contact modeline bağla. Subclass'lar aynı base
# implementation'ı kullandığı için hepsi aynı fiziksel mesafe standardını paylaşır.
CommonEnemy._attack_contact_gate = _v35_enemy_attack_contact_gate
CommonEnemy._attack_baslatma_temasi_var_mi = (
    lambda self: _v35_enemy_attack_contact_gate(self, True)
)
CommonEnemy._attack_temas_var_mi = _v35_enemy_attack_contact


def enemy_friendly_melee_vur(attacker, simdi):
    """V35: enemy-enemy friendly fire da dev attack_rect yüzünden uzaktan bağlanmaz."""
    if not getattr(attacker, "attacking", False):
        return 0
    area = attacker._attack_rect()
    attacker_pos = pygame.Vector2(float(attacker.x), float(attacker.y - 10.0))
    limit = float(
        V35_FRIENDLY_CENTER_LIMIT.get(str(getattr(attacker, "tur", "")), 92.0)
    )
    hit_count = 0
    for target in combat_enemy_aktorleri():
        if target is attacker:
            continue
        uid = str(getattr(target, "uid", ""))
        if uid in attacker.attack_friendly_hits:
            continue
        target_rect = target.collision_rect().inflate(5, 9)
        if not area.colliderect(target_rect):
            continue
        target_pos = pygame.Vector2(float(target.x), float(target.y - 10.0))
        if attacker_pos.distance_to(target_pos) > limit:
            continue
        if not _ince_dunya_los_acik_mi(attacker_pos, target_pos, 4.5):
            continue
        attacker.attack_friendly_hits.add(uid)
        target.hasar_al(int(attacker.cfg.get("attack_damage", 1)), attacker)
        hit_count += 1
    return hit_count
# </POTBO_STAGE S0825>

# <POTBO_STAGE S0828>


def _v35_physical_targets():
    result = []
    for actor in list(common_enemies) + [
        tarkard_actor,
        torrmund_actor,
    ]:
        if actor is None or not getattr(actor, "active", False):
            continue
        if int(getattr(actor, "hp", 0)) <= 0:
            continue
        result.append(actor)
    return result
# </POTBO_STAGE S0828>

# <POTBO_STAGE S0836>


# Recursion-safe wrapper: orijinal referans class attribute altında tutulur; wrapper
# kendi global adına hiçbir zaman geri çağrı yapmaz.
if not hasattr(CommonEnemy, "_v35_hasar_al_original"):
    CommonEnemy._v35_hasar_al_original = CommonEnemy.hasar_al


def _v35_commonenemy_hasar_al(self, miktar, kaynak=None):
    hp_before = int(getattr(self, "hp", 0))
    result = CommonEnemy._v35_hasar_al_original(self, miktar, kaynak)
    hp_after = int(getattr(self, "hp", 0))
    if hp_after < hp_before:
        from_player = kaynak is None or kaynak == "player"
        player_magic = (
            bool(getattr(kaynak, "is_player_magic", False))
            if kaynak is not None
            else False
        )
        if from_player and not player_magic:
            # Special'ın üç fiziksel vuruşu da ritme dahildir fakat tek teknik flow'u
            # anında gereğinden fazla taşırmasın diye daha küçük katkı verir.
            if gelistirici_x_skill_aktif_mi():
                _v35_register_player_melee_hit(0.58)
            else:
                _v35_register_player_melee_hit(1.0)
    return result


CommonEnemy.hasar_al = _v35_commonenemy_hasar_al
# </POTBO_STAGE S0836>

# <POTBO_STAGE S0839>


def _v35_enemy_intent_ciz():
    """Attack startup'ında saldırganın altında çok hafif bir direction cue çizer."""
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA or oyuncu_hp <= 0:
        return
    if gelistirici_x_skill_aktif_mi():
        return
    player = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    layer = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    simdi = pygame.time.get_ticks()
    for actor in _v35_physical_targets():
        if not getattr(actor, "attacking", False):
            continue
        pos = pygame.Vector2(float(actor.x), float(actor.y))
        dist = pos.distance_to(player)
        if dist > V35_INTENT_MAX_RANGE:
            continue
        try:
            frame = actor._attack_frame_index(simdi)
            active_start, _ = actor._attack_active_frame_araligi()
        except Exception:
            continue
        if frame >= active_start:
            continue
        total_pre = max(1, active_start)
        p = max(0.0, min(1.0, frame / total_pre))
        alpha = int(V35_INTENT_ALPHA * (0.35 + 0.65 * p))
        center = pygame.Vector2(dunya_ekran_x(actor.x), dunya_ekran_y(actor.y + 2.0))
        facing = _common_enemy_yon_vektoru(getattr(actor, "direction", "down"))
        if facing.length_squared() <= 1e-6:
            continue
        facing = facing.normalize()
        normal = pygame.Vector2(-facing.y, facing.x)
        tip = center + facing * (19 + 4 * p)
        left = center - facing * 4 + normal * 9
        right = center - facing * 4 - normal * 9
        pygame.draw.polygon(layer, (202, 28, 48, alpha), [tip, left, right], 1)
        pygame.draw.circle(
            layer,
            (238, 218, 222, int(alpha * 0.62)),
            (int(center.x), int(center.y)),
            3,
            1,
        )
    ekran.blit(layer, (0, 0))
# </POTBO_STAGE S0839>

# <POTBO_STAGE S0847>


def oyun_ekrani_ciz():
    _v35_game_draw_original()
    if oyuncu_hp <= 0:
        return
    _v35_enemy_intent_ciz()
    _v35_special_signature_ciz()
    _v35_flow_hud_ciz()
# </POTBO_STAGE S0847>

# <POTBO_STAGE S0864>


def _v35_enemy_intent_ciz():
    """V36: yalnız görünür startup aktörleri için 42x42 küçük cue surface üretir."""
    if (
        oyun_durumu != OYUN
        or oyun_alt_durumu != HARITA
        or oyuncu_hp <= 0
        or gelistirici_x_skill_aktif_mi()
    ):
        return
    player = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    simdi = pygame.time.get_ticks()
    for actor in _v35_physical_targets():
        if not getattr(actor, "attacking", False):
            continue
        pos = pygame.Vector2(float(actor.x), float(actor.y))
        if pos.distance_to(player) > V35_INTENT_MAX_RANGE:
            continue
        try:
            frame = actor._attack_frame_index(simdi)
            active_start, _ = actor._attack_active_frame_araligi()
        except Exception:
            continue
        if frame >= active_start:
            continue
        p = max(0.0, min(1.0, frame / max(1, active_start)))
        alpha = int(V35_INTENT_ALPHA * (0.35 + 0.65 * p))
        facing = _common_enemy_yon_vektoru(getattr(actor, "direction", "down"))
        if facing.length_squared() <= 1e-6:
            continue
        facing = facing.normalize()
        normal = pygame.Vector2(-facing.y, facing.x)
        cue = pygame.Surface((42, 42), pygame.SRCALPHA)
        center = pygame.Vector2(21, 21)
        tip = center + facing * (15 + 3 * p)
        left = center - facing * 3 + normal * 7
        right = center - facing * 3 - normal * 7
        pygame.draw.polygon(cue, (202, 28, 48, alpha), [tip, left, right], 1)
        pygame.draw.circle(
            cue,
            (238, 218, 222, int(alpha * 0.58)),
            (21, 21),
            2,
            1,
        )
        sx = int(dunya_ekran_x(actor.x) - 21)
        sy = int(dunya_ekran_y(actor.y + 2.0) - 21)
        ekran.blit(cue, (sx, sy))
# </POTBO_STAGE S0864>

# <POTBO_STAGE S0898>


def _v35_enemy_intent_ciz():
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA or oyuncu_hp <= 0:
        return
    if gelistirici_x_skill_aktif_mi():
        return
    player = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    now = pygame.time.get_ticks()
    for actor in _v35_physical_targets():
        if not getattr(actor, "attacking", False):
            continue
        pos = pygame.Vector2(float(actor.x), float(actor.y))
        if pos.distance_to(player) > V35_INTENT_MAX_RANGE:
            continue
        try:
            frame = actor._attack_frame_index(now)
            active_start, _ = actor._attack_active_frame_araligi()
        except Exception:
            continue
        if frame >= active_start:
            continue
        p = max(0.0, min(1.0, frame / max(1.0, float(active_start))))
        alpha = int(V35_INTENT_ALPHA * (0.35 + 0.65 * p))
        facing = _common_enemy_yon_vektoru(getattr(actor, "direction", "down"))
        if facing.length_squared() <= 1e-6:
            continue
        facing = facing.normalize()
        normal = pygame.Vector2(-facing.y, facing.x)
        center = pygame.Vector2(21, 21)
        tip = center + facing * (15 + 3 * p)
        left = center - facing * 4 + normal * 8
        right = center - facing * 4 - normal * 8
        cue = pygame.Surface((42, 42), pygame.SRCALPHA)
        pygame.draw.polygon(cue, (202, 28, 48, alpha), [tip, left, right], 1)
        pygame.draw.circle(
            cue,
            (238, 218, 222, int(alpha * 0.62)),
            (21, 21),
            3,
            1,
        )
        sx = int(dunya_ekran_x(actor.x) - 21)
        sy = int(dunya_ekran_y(actor.y + 2.0) - 21)
        ekran.blit(cue, (sx, sy))
# </POTBO_STAGE S0898>

# <POTBO_STAGE S0925>


_v37_common_enemy_guncelle_original = common_enemy_guncelle


def common_enemy_guncelle():
    global v37_special_ai_pause_frames
    active = gelistirici_x_skill_aktif_mi()
    if active or v37_special_previous_active:
        # v37_special_previous_active special'ın bittiği ilk simulation frame'inde
        # bir ek guard verir; sonraki quality tick AI recovery grace'i kurar.
        v37_special_ai_pause_frames += 1
        return
    return _v37_common_enemy_guncelle_original()
# </POTBO_STAGE S0925>

# <POTBO_STAGE S0933>


# ---------------------------------------------------------
# FINAL GAME COMPOSITOR
# ---------------------------------------------------------
def oyun_ekrani_ciz():
    """V37 tek oyun-frame compositor'ı.

    V34C/D/E/F/V35'te üst üste eklenmiş yedi render wrapper'ını bypass eder.
    Base world renderer bir kez çalışır; feedback katmanları açık ve deterministik
    sırada birer kez çizilir. Special'ın ana VFX'i base renderer içindeki final
    gelistirici_x_skill_efekt_ciz() üzerinden zaten tek compositor olarak gelir.
    """
    _v33_oyun_ekrani_ciz()
    if oyuncu_hp <= 0:
        return

    # Input/attack dili.
    _v34_special_ready_prompt_ciz()

    # Combat readability.
    _v34_damage_feedback_ciz()
    _v34_combo_ui_ciz()
    _v34_special_recovery_control_hint_ciz()
    _v34_diagnostics_overlay_ciz()

    # World awareness. Special active iken ilgili fonksiyonların kendi guard'ları vardır.
    _v34_special_target_preview_ciz()
    _v34_special_path_preview_ciz()
    _v34_threat_indicators_ciz()
    _v34_interaction_target_marker_ciz()
    _v35_enemy_intent_ciz()

    # Minimal sürekli combat-flow göstergesi en üst okunabilir HUD katmanıdır.
    _v35_flow_hud_ciz()
# </POTBO_STAGE S0933>

# <POTBO_STAGE S0953>
V38_FIRE_MIN_ENEMY_DAMAGE = 4
# </POTBO_STAGE S0953>

# <POTBO_STAGE S0962>


def _v38_enemy_damage_at(distance, exposure=1.0):
    d = max(0.0, float(distance))
    if d > V38_FIRE_DAMAGE_RADIUS:
        return 0
    expf = _v38_clamp01(exposure)
    pressure = _v38_pressure_field(d)
    thermal = _v38_thermal_field(d)
    # Partial cover: pressure daha sert gölgelenir, sıcak gaz az miktarda kenardan sarar.
    pressure *= expf**1.35
    thermal *= 0.18 + 0.82 * expf
    raw = V38_FIRE_DAMAGE_PRESSURE * pressure + V38_FIRE_DAMAGE_THERMAL * thermal
    if raw < V38_FIRE_MIN_ENEMY_DAMAGE:
        return 0
    return int(round(raw))
# </POTBO_STAGE S0962>

# <POTBO_STAGE S0965>


def _v38_self_damage_at(distance, exposure=1.0):
    if not v38_fire_self_damage:
        return 0
    d = max(0.0, float(distance))
    if d > V38_FIRE_SELF_DAMAGE_RADIUS:
        return 0
    base = _v38_enemy_damage_at(d, exposure)
    if base <= 0:
        return 0
    # Owner risk merkezde gerçek, sınırda hızla sıfır. Self damage hiçbir zaman
    # maksimum canın %58'inden fazlasını tek detonation'da alamaz.
    edge = 1.0 - _v38_smoothstep(d / V38_FIRE_SELF_DAMAGE_RADIUS)
    scaled = base * V38_FIRE_SELF_DAMAGE_SCALE * edge
    cap = max(
        1,
        int(round(float(oyuncu_max_hp) * V38_FIRE_SELF_DAMAGE_MAX_HP_FRACTION)),
    )
    dmg = min(cap, int(round(scaled)))
    return dmg if dmg >= V38_FIRE_SELF_MIN_DAMAGE else 0
# </POTBO_STAGE S0965>

# <POTBO_STAGE S0984>


# ---------------------------------------------------------
# MELEE CONTACT INTEGRITY: ENEMIES
# ---------------------------------------------------------
V38_ENEMY_ACTIVE_ROOT_STRICT = {
    "crawler": 43.0,
    "berserker": 49.0,
    "tarkard": 66.0,
    "torrmund": 70.0,
}
V38_ENEMY_ACTIVE_ROOT_STANDARD = {
    "crawler": 48.0,
    "berserker": 55.0,
    "tarkard": 72.0,
    "torrmund": 76.0,
}
V38_ENEMY_START_ROOT = {
    "crawler": 61.0,
    "berserker": 68.0,
    "tarkard": 88.0,
    "torrmund": 90.0,
}
V38_ENEMY_SWEEP_STRICT = {
    "crawler": (44.0, 10.5),
    "berserker": (51.0, 12.5),
    "tarkard": (68.0, 14.5),
    "torrmund": (72.0, 14.0),
}
V38_ENEMY_SWEEP_STANDARD = {
    "crawler": (48.0, 12.0),
    "berserker": (55.0, 14.0),
    "tarkard": (73.0, 16.0),
    "torrmund": (77.0, 15.5),
}


def _v38_enemy_root(actor):
    body_h = float(actor.cfg.get("body_height", 22.0))
    return pygame.Vector2(float(actor.x), float(actor.y) - body_h * 0.64)


def _v38_enemy_contact_gate(actor, baslangic=False):
    hurt = oyuncu_savas_hurtbox_rect(oyuncu_x, oyuncu_y)
    origin = _v38_enemy_root(actor)
    nearest = _rect_en_yakin_nokta(hurt, origin)
    dist = origin.distance_to(nearest)
    tur = str(getattr(actor, "tur", ""))
    if baslangic:
        limit = V38_ENEMY_START_ROOT.get(tur, 66.0)
    else:
        limits = (
            V38_ENEMY_ACTIVE_ROOT_STRICT
            if v38_combat_precision == "strict"
            else V38_ENEMY_ACTIVE_ROOT_STANDARD
        )
        limit = limits.get(tur, 56.0)
    if dist > limit:
        return False

    # Gerçek body overlap varsa yön cone'u aranmaz.
    if actor.collision_rect().inflate(6, 16).colliderect(hurt):
        return True

    facing = _common_enemy_yon_vektoru(actor.direction)
    if facing.length_squared() <= 1e-8:
        return False
    delta = pygame.Vector2(hurt.center) - origin
    if delta.length_squared() <= 1e-8:
        return True
    dot = facing.normalize().dot(delta.normalize())
    if baslangic:
        return dot >= 0.14
    # Active swing yan kenarı kapsar ama artık karakterin arkasına kapsül uzamaz.
    threshold = -0.02 if tur in ("tarkard", "torrmund") else 0.02
    return dot >= threshold


def _v38_enemy_contact(actor, simdi):
    if not _v38_enemy_contact_gate(actor, baslangic=False):
        return False
    hurt = oyuncu_savas_hurtbox_rect(oyuncu_x, oyuncu_y)
    body = actor.collision_rect()
    if body.inflate(7, 16).colliderect(hurt):
        return True

    tur = str(getattr(actor, "tur", ""))
    facing = _common_enemy_yon_vektoru(actor.direction)
    if facing.length_squared() <= 1e-8:
        facing = pygame.Vector2(1.0, 0.0)
    facing = facing.normalize()
    origin = _v38_enemy_root(actor)
    variant = str(getattr(actor, "attack_variant", ""))

    frame = actor._attack_frame_index(simdi)
    active_start, active_end = actor._attack_active_frame_araligi()
    span = max(1.0, float(active_end - active_start + 1))
    p = _v38_clamp01((frame - active_start + 0.5) / span)

    if tur == "tarkard" and variant == "whirl":
        nearest = _rect_en_yakin_nokta(hurt, origin)
        limit = 61.0 if v38_combat_precision == "strict" else 67.0
        return origin.distance_to(nearest) <= limit

    sweeps = (
        V38_ENEMY_SWEEP_STRICT
        if v38_combat_precision == "strict"
        else V38_ENEMY_SWEEP_STANDARD
    )
    reach, radius = sweeps.get(tur, (52.0, 12.0))
    if tur == "crawler":
        angles = (-7.0, 0.0, 7.0)
    elif tur == "berserker":
        center_angle = -39.0 + 78.0 * p
        angles = (
            center_angle - 6.0,
            center_angle,
            center_angle + 6.0,
        )
    elif tur == "tarkard":
        center_angle = -27.0 + 54.0 * p
        angles = (
            center_angle - 6.0,
            center_angle,
            center_angle + 6.0,
        )
    elif tur == "torrmund" and variant == "cleave":
        center_angle = -19.0 + 38.0 * p
        angles = (
            center_angle - 5.0,
            center_angle,
            center_angle + 5.0,
        )
    elif tur == "torrmund":
        center_angle = -31.0 + 62.0 * p
        angles = (
            center_angle - 6.0,
            center_angle,
            center_angle + 6.0,
        )
    else:
        angles = (0.0,)

    for angle in angles:
        direction = facing.rotate(angle)
        start = origin + direction * 9.0
        end = origin + direction * reach
        if _kapsul_rect_kesisiyor(hurt, start, end, radius):
            return True
    return False


CommonEnemy._attack_contact_gate = _v38_enemy_contact_gate
CommonEnemy._attack_baslatma_temasi_var_mi = lambda self: _v38_enemy_contact_gate(
    self, True
)
CommonEnemy._attack_temas_var_mi = _v38_enemy_contact


# Friendly fire de aynı "dev attack rect" problemine geri düşmesin.
def enemy_friendly_melee_vur(attacker, simdi):
    if not getattr(attacker, "attacking", False):
        return 0
    attacker_pos = pygame.Vector2(float(attacker.x), float(attacker.y - 10.0))
    tur = str(getattr(attacker, "tur", ""))
    sweep = (
        V38_ENEMY_SWEEP_STRICT
        if v38_combat_precision == "strict"
        else V38_ENEMY_SWEEP_STANDARD
    )
    reach, radius = sweep.get(tur, (52.0, 12.0))
    hit_count = 0
    facing = _common_enemy_yon_vektoru(getattr(attacker, "direction", "down"))
    if facing.length_squared() <= 1e-8:
        facing = pygame.Vector2(0.0, 1.0)
    facing = facing.normalize()
    origin = _v38_enemy_root(attacker)
    for target in combat_enemy_aktorleri():
        if target is attacker:
            continue
        uid = str(getattr(target, "uid", ""))
        if uid in attacker.attack_friendly_hits:
            continue
        target_rect = target.collision_rect().inflate(3, 6)
        # Tek sweep centerline + target rect capsule. Friendly-fire için geniş arc
        # gerekmiyor; savaş okunurluğu oyuncu hit testinden daha önemli.
        start = origin + facing * 8.0
        end = origin + facing * reach
        if not _kapsul_rect_kesisiyor(target_rect, start, end, radius):
            continue
        target_pos = pygame.Vector2(float(target.x), float(target.y - 10.0))
        if attacker_pos.distance_to(target_pos) > reach + 34.0:
            continue
        if not _ince_dunya_los_acik_mi(attacker_pos, target_pos, 6.0):
            continue
        attacker.attack_friendly_hits.add(uid)
        target.hasar_al(int(attacker.cfg.get("attack_damage", 1)), attacker)
        hit_count += 1
    return hit_count
# </POTBO_STAGE S0984>

# <POTBO_STAGE S1002>


# Materyal katsayıları "armor = fire immune" gibi kaba bir sınıflama değildir.
# pressure: blast pressure'a mekanik hassasiyet
# thermal : kısa süreli ısı dozuna hassasiyet
# burn    : devam eden yanma dozunun çarpanı
# impulse : knockback susceptibility
# core    : çok yakın merkezde minimum aktarım katsayısı
V38_FIRE_MATERIAL_RESPONSE = {
    "crawler": {
        "pressure": 1.06,
        "thermal": 1.18,
        "burn": 1.22,
        "impulse": 1.15,
        "core": 1.00,
        "label": "light_flesh",
    },
    "berserker": {
        "pressure": 1.02,
        "thermal": 1.04,
        "burn": 1.02,
        "impulse": 0.92,
        "core": 1.00,
        "label": "dense_flesh",
    },
    "headsthrower": {
        "pressure": 1.08,
        "thermal": 1.14,
        "burn": 1.16,
        "impulse": 1.10,
        "core": 1.00,
        "label": "light_flesh",
    },
    "tarkard": {
        "pressure": 0.96,
        "thermal": 0.82,
        "burn": 0.72,
        "impulse": 0.70,
        "core": 0.92,
        "label": "heavy_hide",
    },
    "torrmund": {
        "pressure": 0.90,
        "thermal": 0.70,
        "burn": 0.58,
        "impulse": 0.58,
        "core": 0.88,
        "label": "armored_human",
    },
    "default": {
        "pressure": 1.00,
        "thermal": 1.00,
        "burn": 1.00,
        "impulse": 1.00,
        "core": 1.00,
        "label": "generic",
    },
}
# </POTBO_STAGE S1002>

# <POTBO_STAGE S1004>


def _v38_enemy_damage_for_actor(actor, distance, exposure, momentum=None, radial=None):
    d = max(0.0, float(distance))
    if d > V38_FIRE_DAMAGE_RADIUS:
        return 0
    material = _v38_material_response(actor)
    expf = _v38_clamp01(exposure)
    p = _v38_pressure_field(d) * (expf**1.35)
    h = _v38_thermal_field(d) * (0.18 + 0.82 * expf)
    bias = _v38_momentum_bias(momentum, radial)
    core_blend = 1.0 - _v38_smoothstep(d / 72.0)
    pressure_factor = float(material["pressure"]) * bias
    thermal_factor = float(material["thermal"])
    raw = (
        V38_FIRE_DAMAGE_PRESSURE * p * pressure_factor
        + V38_FIRE_DAMAGE_THERMAL * h * thermal_factor
    )
    # Core çok yakın olduğunda zırhlı hedef bile blast'ı tamamen yok sayamaz.
    raw *= (1.0 - core_blend) + core_blend * max(float(material["core"]), 0.82)
    return int(round(raw)) if raw >= V38_FIRE_MIN_ENEMY_DAMAGE else 0


def _v38_enemy_burn_for_actor(actor, distance, exposure):
    base = _v38_burn_total_at(distance, exposure)
    if base <= 0:
        return 0
    response = _v38_material_response(actor)
    return max(0, int(round(base * float(response["burn"]))))


def _v38_enemy_knockback_for_actor(actor, distance, exposure):
    base = _v38_knockback_at(distance, exposure)
    response = _v38_material_response(actor)
    return max(0.0, base * float(response["impulse"]))
# </POTBO_STAGE S1004>

# <POTBO_STAGE S1007>


# ---------------------------------------------------------
# EQUATION CATALOG / BALANCE INTROSPECTION
# ---------------------------------------------------------
# Bu katalog gameplay döngüsünde çalışmaz. Kod içinden tuning yaparken denklem ile
# parametre arasındaki bağı kaybetmemek için tek merkezden okunabilir bir şema sağlar.
V38_EQUATION_CATALOG = {
    "pressure": {
        "equation": "P(d)=exp(-(d/sigma_p)^2)",
        "domain": "d>=0",
        "parameters": ("V38_FIRE_PRESSURE_SIGMA",),
        "purpose": "blast pressure falloff",
    },
    "thermal": {
        "equation": "H(d)=1/(1+(d/r50)^4)",
        "domain": "d>=0",
        "parameters": ("V38_FIRE_THERMAL_R50",),
        "purpose": "thermal exposure falloff",
    },
    "enemy_damage": {
        "equation": "D=Dp*P*Mp + Dh*H*Mh",
        "domain": "0<=d<=R_damage",
        "parameters": (
            "V38_FIRE_DAMAGE_PRESSURE",
            "V38_FIRE_DAMAGE_THERMAL",
            "V38_FIRE_MATERIAL_RESPONSE",
        ),
        "purpose": "continuous direct damage",
    },
    "self_damage": {
        "equation": "Ds=min(HP*c, D*s*(1-smoothstep(d/Rs)))",
        "domain": "0<=d<=R_self",
        "parameters": (
            "V38_FIRE_SELF_DAMAGE_RADIUS",
            "V38_FIRE_SELF_DAMAGE_SCALE",
            "V38_FIRE_SELF_DAMAGE_MAX_HP_FRACTION",
        ),
        "purpose": "bounded owner risk",
    },
    "knockback": {
        "equation": "K=K0*P^0.72*Mimpulse",
        "domain": "0<=d<=R_damage",
        "parameters": (
            "V38_FIRE_KNOCKBACK_BASE",
            "V38_FIRE_MATERIAL_RESPONSE",
        ),
        "purpose": "blast impulse",
    },
    "burn": {
        "equation": "B=B0*H^1.30*Mburn",
        "domain": "0<=d<=R_thermal",
        "parameters": (
            "V38_FIRE_BURN_BASE",
            "V38_FIRE_MATERIAL_RESPONSE",
        ),
        "purpose": "thermal after-effect",
    },
    "projectile_speed": {
        "equation": "v(t)=v_inf+(v0-v_inf)e^(-kt)",
        "domain": "t>=0",
        "parameters": (
            "V38_FIRE_PROJECTILE_V0",
            "V38_FIRE_PROJECTILE_VINF",
            "V38_FIRE_PROJECTILE_DRAG_K",
        ),
        "purpose": "confinement flight speed",
    },
    "projectile_temperature": {
        "equation": "T(t)=Tair+(T0-Tair)e^(-kT*t)",
        "domain": "t>=0",
        "parameters": (
            "V38_FIRE_AIR_TEMPERATURE_K",
            "V38_FIRE_CORE_TEMPERATURE_K",
            "V38_FIRE_THERMAL_COOLING_K",
        ),
        "purpose": "visual thermal decay",
    },
    "radiance": {
        "equation": "I~(T/T0)^4",
        "domain": "T>=Tair",
        "parameters": ("V38_FIRE_CORE_TEMPERATURE_K",),
        "purpose": "Stefan-Boltzmann-inspired glow",
    },
    "special_ease": {
        "equation": "f(t)=t^2/(t^2+(1-t)^2)",
        "domain": "0<=t<=1",
        "parameters": (),
        "purpose": "smooth fast authored dash",
    },
    "special_stamina": {
        "equation": "S_total=3*S_hit",
        "domain": "three physical hits",
        "parameters": ("V38_SPECIAL_STAMINA_PER_HIT",),
        "purpose": "visible three-step stamina spend",
    },
}
# </POTBO_STAGE S1007>

# <POTBO_STAGE S1009>


def v38_material_balance_grid():
    rows = []
    for material_name in (
        "crawler",
        "berserker",
        "headsthrower",
        "tarkard",
        "torrmund",
    ):
        proxy = type("V38MaterialProxy", (), {"tur": material_name})()
        for exposure in V38_BALANCE_EXPOSURES:
            for distance in V38_BALANCE_DISTANCES:
                rows.append(
                    {
                        "material": material_name,
                        "distance": distance,
                        "exposure": exposure,
                        "damage": _v38_enemy_damage_for_actor(
                            proxy, distance, exposure
                        ),
                        "burn": _v38_enemy_burn_for_actor(proxy, distance, exposure),
                        "knockback": round(
                            _v38_enemy_knockback_for_actor(proxy, distance, exposure),
                            1,
                        ),
                    }
                )
    return rows


def v38_equation_catalog_validate():
    required = {
        "pressure",
        "thermal",
        "enemy_damage",
        "self_damage",
        "knockback",
        "burn",
        "projectile_speed",
        "projectile_temperature",
        "radiance",
        "special_ease",
        "special_stamina",
    }
    present = set(V38_EQUATION_CATALOG)
    return {
        "all_required": required.issubset(present),
        "no_empty_equations": all(
            bool(v.get("equation")) for v in V38_EQUATION_CATALOG.values()
        ),
        "no_empty_purpose": all(
            bool(v.get("purpose")) for v in V38_EQUATION_CATALOG.values()
        ),
        "count": len(V38_EQUATION_CATALOG),
    }


def v38_runtime_balance_summary():
    center_damage = {}
    edge_damage = {}
    center_knock = {}
    burn_96 = {}
    for material_name in (
        "crawler",
        "berserker",
        "headsthrower",
        "tarkard",
        "torrmund",
    ):
        proxy = type("V38MaterialProxy", (), {"tur": material_name})()
        center_damage[material_name] = _v38_enemy_damage_for_actor(proxy, 0.0, 1.0)
        edge_damage[material_name] = _v38_enemy_damage_for_actor(proxy, 180.0, 1.0)
        center_knock[material_name] = round(
            _v38_enemy_knockback_for_actor(proxy, 0.0, 1.0), 1
        )
        burn_96[material_name] = _v38_enemy_burn_for_actor(proxy, 96.0, 1.0)
    return {
        "center_damage": center_damage,
        "edge_damage_180": edge_damage,
        "center_knockback": center_knock,
        "burn_at_96": burn_96,
        "self_center": _v38_self_damage_at(0.0, 1.0),
        "self_96": _v38_self_damage_at(96.0, 1.0),
        "self_126": _v38_self_damage_at(126.0, 1.0),
    }
# </POTBO_STAGE S1009>

# <POTBO_STAGE S1012>


# ---------------------------------------------------------
# CONTACT QA GRID
# ---------------------------------------------------------
# Gameplay sırasında çalışmaz. Tuning sırasında menzil sayılarını tek bakışta
# karşılaştırmak ve "startup range < active hit range" gibi terslikleri yakalamak içindir.
V38_CONTACT_QA_CASES = (
    ("crawler", 43.0, 44.0, 10.5),
    ("berserker", 49.0, 51.0, 12.5),
    ("tarkard", 66.0, 68.0, 14.5),
    ("torrmund", 70.0, 72.0, 14.0),
)


def v38_contact_contract():
    strict_active = V38_ENEMY_ACTIVE_ROOT_STRICT
    standard_active = V38_ENEMY_ACTIVE_ROOT_STANDARD
    checks = {}
    for (
        tur,
        expected_active,
        expected_reach,
        expected_radius,
    ) in V38_CONTACT_QA_CASES:
        reach, radius = V38_ENEMY_SWEEP_STRICT[tur]
        checks[tur] = {
            "active_root": strict_active[tur],
            "standard_root": standard_active[tur],
            "startup_root": V38_ENEMY_START_ROOT[tur],
            "reach": reach,
            "radius": radius,
            "strict_matches_table": abs(strict_active[tur] - expected_active) < 1e-6,
            "reach_matches_table": abs(reach - expected_reach) < 1e-6,
            "radius_matches_table": abs(radius - expected_radius) < 1e-6,
            "startup_outside_active": V38_ENEMY_START_ROOT[tur] > strict_active[tur],
            "standard_not_smaller": standard_active[tur] >= strict_active[tur],
        }
    return checks
# </POTBO_STAGE S1012>

# <POTBO_STAGE S1015>


def v38_fire_equation_samples():
    """Dengeyi konsoldan hızlı görmek için deterministik mesafe tablosu."""
    samples = []
    for d in (0, 24, 48, 72, 96, 120, 150, 180, 214, 240):
        samples.append(
            {
                "distance": float(d),
                "pressure": round(_v38_pressure_field(d), 4),
                "thermal": round(_v38_thermal_field(d), 4),
                "enemy_damage": int(_v38_enemy_damage_at(d, 1.0)),
                "self_damage": int(_v38_self_damage_at(d, 1.0)),
                "burn_total": int(_v38_burn_total_at(d, 1.0)),
                "knockback": round(_v38_knockback_at(d, 1.0), 1),
            }
        )
    return samples
# </POTBO_STAGE S1015>

# <POTBO_STAGE S1017>


def v38_contact_profile():
    nr, nw, hr, hw = _v38_player_reach_values()
    sweep = (
        V38_ENEMY_SWEEP_STRICT
        if v38_combat_precision == "strict"
        else V38_ENEMY_SWEEP_STANDARD
    )
    active = (
        V38_ENEMY_ACTIVE_ROOT_STRICT
        if v38_combat_precision == "strict"
        else V38_ENEMY_ACTIVE_ROOT_STANDARD
    )
    return {
        "precision": v38_combat_precision,
        "player_normal": (nr, nw),
        "player_heavy": (hr, hw),
        "enemy_active_root": dict(active),
        "enemy_sweep": dict(sweep),
    }
# </POTBO_STAGE S1017>

# <POTBO_STAGE S1034>


def v38_reference_curves():
    rows = []
    for distance in V38_REFERENCE_DISTANCES:
        rows.append(
            {
                "distance": distance,
                "pressure": round(_v38_pressure_field(distance), 5),
                "thermal": round(_v38_thermal_field(distance), 5),
                "generic_damage": _v38_enemy_damage_at(distance, 1.0),
                "self_damage": _v38_self_damage_at(distance, 1.0),
                "burn": _v38_burn_total_at(distance, 1.0),
                "knockback": round(_v38_knockback_at(distance, 1.0), 2),
            }
        )
    return rows
# </POTBO_STAGE S1034>

# <POTBO_STAGE S1048>
V38_ENEMY_ACTIVE_ROOT_STRICT.update(
    {
        "crawler": 40.0,
        "berserker": 46.0,
        "tarkard": 63.0,
        "torrmund": 67.0,
    }
)
V38_ENEMY_ACTIVE_ROOT_STANDARD.update(
    {
        "crawler": 45.0,
        "berserker": 52.0,
        "tarkard": 69.0,
        "torrmund": 73.0,
    }
)
V38_ENEMY_SWEEP_STRICT.update(
    {
        "crawler": (41.0, 9.5),
        "berserker": (48.0, 11.5),
        "tarkard": (65.0, 13.5),
        "torrmund": (69.0, 13.0),
    }
)
V38_ENEMY_SWEEP_STANDARD.update(
    {
        "crawler": (45.0, 11.0),
        "berserker": (52.0, 13.0),
        "tarkard": (70.0, 15.0),
        "torrmund": (74.0, 14.5),
    }
)
# </POTBO_STAGE S1048>

# <POTBO_STAGE S1051>

IPUCLARI = {
    "TR": [
        "Bazen ilk vuruş yol açar; öldüren ikinci adımdır.",
        "Dar geçitte geri değil, çapraza oyna.",
        "Ateş topu kalabalığı dağıtır; tek hedefi değil düzeni vurur.",
        "Tarkard seni korkutursa avantajı ona verdin demektir.",
        "Uzun takaslar stamina ile biter; kılıç yalnız bahanedir.",
        "Kan yerde kalır. Çoksa, orada biri uzun süre direnmiştir.",
        "Heads Thrower çizgi ister; çizgiyi bozarsan eli de bozulur.",
        "Savunma, kaçamadığın darbeyi utandırma sanatıdır.",
    ],
    "EN": [
        "Sometimes the first strike only opens the road; the second one kills.",
        "In a narrow pass, step across the line rather than back from it.",
        "A fireball breaks formations; aim for order, not only flesh.",
        "If Tarkard frightens you, you have already given him tempo.",
        "Long trades end with stamina before they end with steel.",
        "Blood stays. If there is much of it, someone resisted there.",
        "Heads Thrower needs a lane; break the lane and you break the cast.",
        "Defense is the art of shaming the blow you failed to evade.",
    ],
}
# </POTBO_STAGE S1051>

# <POTBO_STAGE S1081>
_v40_ambient_rat_parent = AmbientRat
# </POTBO_STAGE S1081>

# <POTBO_STAGE S1083>


_v40_ambient_rats_guncelle_original = ambient_rats_guncelle
# </POTBO_STAGE S1083>

# <POTBO_STAGE S1085>


# ---------------------------------------------------------
# HEADS THROWER ROCK: GERÇEK SPRITE PARÇALARI
# ---------------------------------------------------------
def _v40_head_rock_fragments_build():
    src = HEADSTHROWER_ROCK_SPRITE
    if src is None:
        return []
    bounds = src.get_bounding_rect(min_alpha=8)
    if bounds.width < 4 or bounds.height < 4:
        return []
    tight = src.subsurface(bounds).copy().convert_alpha()
    w, h = tight.get_size()
    pieces = []
    rects = [
        pygame.Rect(0, 0, max(2, w // 2 + 1), max(2, h // 2 + 1)),
        pygame.Rect(
            max(0, w // 2 - 1),
            0,
            max(2, w - w // 2 + 1),
            max(2, h // 2 + 1),
        ),
        pygame.Rect(
            0,
            max(0, h // 2 - 1),
            max(2, w // 2 + 1),
            max(2, h - h // 2 + 1),
        ),
        pygame.Rect(
            max(0, w // 2 - 1),
            max(0, h // 2 - 1),
            max(2, w - w // 2 + 1),
            max(2, h - h // 2 + 1),
        ),
    ]
    for r in rects:
        r = r.clip(tight.get_rect())
        if r.width > 1 and r.height > 1:
            p = tight.subsurface(r).copy().convert_alpha()
            b = p.get_bounding_rect(min_alpha=8)
            if b.width > 0 and b.height > 0:
                pieces.append(p.subsurface(b).copy().convert_alpha())
    return pieces
# </POTBO_STAGE S1085>

# <POTBO_STAGE S1104>


# Daha geniş ama hâlâ kısa/örtük loading ipucu havuzu. Tutorial paragrafı yerine
# dünyayı ve sistemleri sezdiren tek cümleler kullanılır.
IPUCLARI = {
    "TR": [
        "Bazen ilk vuruş yol açar; öldüren ikinci adımdır.",
        "Dar geçitte geri değil, çapraza oyna.",
        "Ateş topu kalabalığı dağıtır; tek hedefi değil düzeni vurur.",
        "Tarkard seni korkutursa avantajı ona verdin demektir.",
        "Uzun takaslar stamina ile biter; kılıç yalnız bahanedir.",
        "Kan yerde kalır. Çoksa, orada biri uzun süre direnmiştir.",
        "Heads Thrower çizgi ister; çizgiyi bozarsan eli de bozulur.",
        "Savunma, kaçamadığın darbeyi utandırma sanatıdır.",
        "Bir düşmanın hazırlığı saldırının kendisinden daha çok şey söyler.",
        "Köşeye sıkışan herkes zayıf değildir; bazıları orayı seçmiştir.",
        "Alev duvarı sevmez. Patlama ise duvarın ardını yalnız kısmen hatırlar.",
        "Stamina boşsa menzil de cesaret de olduğundan uzun görünür.",
        "Kısa dash bazen kaçış değil, bir sonraki vuruşun başlangıcıdır.",
        "Aynı NPC ikinci kez aynı kişi olmayabilir; dünya arada değişir.",
        "Yerdeki organlar yalnız görüntü değildir. Küçük şeyler onları fark eder.",
        "Fare senden korkar; açlık korkudan sonra gelir.",
        "Kurtçuk gördüğün kan artık taze değildir.",
        "Zırh darbeyi durdurabilir; ritmi durduramaz.",
        "Büyünün merkezi öldürür, kenarı düzeni bozar.",
        "Düşmanın arkasına geçmek her zaman güvenli olmak demek değildir.",
        "Karanlık bir yol bazen gizli değildir; yalnız bakılmamıştır.",
        "F5 iyi bir alışkanlıktır. İyi alışkanlıklar kahramanlıktan ucuzdur.",
    ],
    "EN": [
        "Sometimes the first strike only opens the road; the second one kills.",
        "In a narrow pass, step across the line rather than back from it.",
        "A fireball breaks formations; aim for order, not only flesh.",
        "If Tarkard frightens you, you have already given him tempo.",
        "Long trades end with stamina before they end with steel.",
        "Blood stays. If there is much of it, someone resisted there.",
        "Heads Thrower needs a lane; break the lane and you break the cast.",
        "Defense is the art of shaming the blow you failed to evade.",
        "An enemy's preparation often says more than the strike itself.",
        "Not everyone trapped in a corner is weak; some chose the corner.",
        "Fire dislikes walls. A blast only partly remembers what lies behind one.",
        "With no stamina, both range and courage look longer than they are.",
        "A short dash is sometimes the beginning of the next strike, not an escape.",
        "The same NPC may not be the same person when the world has changed.",
        "Organs on the ground are not only scenery. Small things notice them.",
        "A rat fears you first; hunger comes second.",
        "If there are maggots, the blood is no longer fresh.",
        "Armor can stop a blow. It cannot stop rhythm.",
        "The center of a spell kills; its edge breaks order.",
        "Standing behind an enemy does not always mean standing safely.",
        "A dark road is not always hidden. Sometimes no one looked.",
        "F5 is a cheap habit. Heroism is more expensive.",
    ],
}
# </POTBO_STAGE S1104>

# <POTBO_STAGE S1110>

# ---------------------------------------------------------
# MELEE CLOSING CONTRACT
# ---------------------------------------------------------
# V39/V42'de hasar teması bilinçli olarak sıkılaştırılmıştı. Ancak AI'nın saldırı
# başlatma halkası ve tactical ready slotu aynı oranda daralmadığı için özellikle
# Tarkard / Torrmund, oyuncuya doğru yürümeyi erken bırakıp artık yetişemeyecek bir
# swing'e commit edebiliyordu. Çözüm hitbox'ı tekrar büyütmek değildir:
# saldırı başlamadan önce gerçekten active-hit geometrisine girmek zorundadır.
V43_MELEE_READY_SLOT = {
    "crawler": 37.0,
    "berserker": 43.0,
    "tarkard": 50.0,
    "torrmund": 53.0,
}

# Startup gate active gate'ten büyük olmaz. Böylece telegraph başladığı konum,
# karakter yerinde kalsa bile active frame geldiğinde mekanik olarak hâlâ erişilebilirdir.
V38_ENEMY_START_ROOT.update(
    {
        "crawler": float(V38_ENEMY_ACTIVE_ROOT_STRICT["crawler"]),
        "berserker": float(V38_ENEMY_ACTIVE_ROOT_STRICT["berserker"]),
        "tarkard": float(V38_ENEMY_ACTIVE_ROOT_STRICT["tarkard"]),
        "torrmund": float(V38_ENEMY_ACTIVE_ROOT_STRICT["torrmund"]),
    }
)


def _v43_melee_attack_ready(actor, simdi):
    cooldown = int(actor.cfg.get("attack_cooldown_ms", 1000))
    if getattr(actor, "tur", "") == "berserker":
        cooldown = max(
            220,
            cooldown + int(getattr(actor, "next_attack_variance_ms", 0)),
        )
    return (
        int(simdi) - int(getattr(actor, "last_attack_ms", -100000)) >= cooldown
        and int(simdi) >= int(getattr(actor, "recovery_until", 0))
        and not bool(getattr(actor, "attacking", False))
    )


def _v43_inward_melee_slot(actor, target, simdi, player_prediction):
    tur = str(getattr(actor, "tur", ""))
    desired = V43_MELEE_READY_SLOT.get(tur)
    if desired is None or not _v43_melee_attack_ready(actor, simdi):
        return pygame.Vector2(target)

    player = pygame.Vector2(player_prediction)
    target = pygame.Vector2(target)
    radial = target - player
    if radial.length_squared() <= 1e-6:
        radial = pygame.Vector2(float(actor.x), float(actor.y)) - player
    if radial.length_squared() <= 1e-6:
        radial = pygame.Vector2(1.0, 0.0)
    radial = radial.normalize()

    # En yakın slot ideal; dar duvar geometrisinde 3 küçük dış halka fallback'i var.
    # Bunlar oyuncudan uzaklaştırma değil, yalnız enemy footprint'ine yer bulma payıdır.
    for radius in (
        desired,
        desired + 4.0,
        desired + 8.0,
        desired + 12.0,
    ):
        candidate = player + radial * radius
        if common_enemy_statik_konum_gecerli_mi(
            tur, candidate.x, candidate.y, navigation=True
        ):
            actor.tactical_target = pygame.Vector2(candidate)
            actor.tactical_refresh_ms = min(
                int(getattr(actor, "tactical_refresh_ms", simdi + 90)),
                int(simdi) + 105,
            )
            return pygame.Vector2(candidate)
    return target


_v43_common_tactical_original = CommonEnemy._taktik_hedef_sec


def _v43_common_tactical(self, simdi, oyuncu_tahmin, digerler, oyuncu_hiz_vektoru):
    target = _v43_common_tactical_original(
        self, simdi, oyuncu_tahmin, digerler, oyuncu_hiz_vektoru
    )
    if str(getattr(self, "tur", "")) in (
        "crawler",
        "berserker",
    ):
        return _v43_inward_melee_slot(self, target, simdi, oyuncu_tahmin)
    return target


CommonEnemy._taktik_hedef_sec = _v43_common_tactical

_v43_tarkard_tactical_original = TarkardEnemy._taktik_hedef_sec


def _v43_tarkard_tactical(self, simdi, oyuncu_tahmin, digerler, oyuncu_hiz_vektoru):
    target = _v43_tarkard_tactical_original(
        self, simdi, oyuncu_tahmin, digerler, oyuncu_hiz_vektoru
    )
    return _v43_inward_melee_slot(self, target, simdi, oyuncu_tahmin)


TarkardEnemy._taktik_hedef_sec = _v43_tarkard_tactical

_v43_torrmund_tactical_original = SirTorrmundEnemy._taktik_hedef_sec


def _v43_torrmund_tactical(self, simdi, oyuncu_tahmin, digerler, oyuncu_hiz_vektoru):
    target = _v43_torrmund_tactical_original(
        self, simdi, oyuncu_tahmin, digerler, oyuncu_hiz_vektoru
    )
    return _v43_inward_melee_slot(self, target, simdi, oyuncu_tahmin)


SirTorrmundEnemy._taktik_hedef_sec = _v43_torrmund_tactical
# </POTBO_STAGE S1110>

# <POTBO_STAGE S1155>


# CommonEnemy damage context: lethal blood shape hit speed'e göre seçilir.
_v44_commonenemy_damage_original = CommonEnemy.hasar_al
# </POTBO_STAGE S1155>

# <POTBO_STAGE S1158>


CommonEnemy.hasar_al = _v44_commonenemy_damage
# </POTBO_STAGE S1158>

# <POTBO_STAGE S1178>


# V44 damage wrapper'ını bir üst katmanda gerçek melee kalite çarpanıyla zenginleştir.
_v45_commonenemy_damage_original = CommonEnemy.hasar_al
# </POTBO_STAGE S1178>

# <POTBO_STAGE S1180>


CommonEnemy.hasar_al = _v45_commonenemy_damage


_v45_common_enemy_update_original = common_enemy_guncelle
# </POTBO_STAGE S1180>

# <POTBO_STAGE S1201>


# V45 wrapper'ın üstünde yalnız log/hit confirm. Hasar bir daha değişmez.
_v47_commonenemy_damage_original = CommonEnemy.hasar_al


def _v47_commonenemy_damage(self, miktar, kaynak=None):
    before_hp = int(getattr(self, "hp", 0))
    result = _v47_commonenemy_damage_original(self, miktar, kaynak)
    after_hp = int(getattr(self, "hp", 0))
    if _v44_is_player_melee_source(kaynak) and before_hp > after_hp:
        v47_record_hit(self, before_hp - after_hp, before_hp, after_hp)
    return result


CommonEnemy.hasar_al = _v47_commonenemy_damage
# </POTBO_STAGE S1201>

# <POTBO_STAGE S1213>


def v49_world_actor_list():
    actors = []
    try:
        actors.extend(common_enemies)
    except Exception:
        pass
    for name in ("tarkard_actor", "torrmund_actor"):
        actor = globals().get(name)
        if actor is not None:
            actors.append(actor)
    return actors
# </POTBO_STAGE S1213>

# <POTBO_STAGE S1236>


# Riposte only changes the next clean player melee hit inside its short timing window.
_v51_commonenemy_damage_original = CommonEnemy.hasar_al


def _v51_commonenemy_damage(self, miktar, kaynak=None):
    global v51_riposte_consumed, oyuncu_stamina
    if not _v44_is_player_melee_source(kaynak) or not v51_riposte_active():
        return _v51_commonenemy_damage_original(self, miktar, kaynak)
    bonus = V51_RIPOSTE_DAMAGE_BONUS
    if v45_last_alignment >= 1.04:
        bonus += V51_RIPOSTE_ALIGNMENT_BONUS
    adjusted = max(1, int(round(float(miktar) * bonus)))
    result = _v51_commonenemy_damage_original(self, adjusted, kaynak)
    v51_riposte_consumed = True
    oyuncu_stamina = min(
        float(oyuncu_max_stamina),
        float(oyuncu_stamina) + V51_RIPOSTE_STAMINA_REFUND,
    )
    v45_skill_flash("edge_control")
    return result


CommonEnemy.hasar_al = _v51_commonenemy_damage
# </POTBO_STAGE S1236>

# <POTBO_STAGE S1256>


# Final melee damage skill scalar; wraps without changing magic/friendly fire.
_v52_commonenemy_damage_original = CommonEnemy.hasar_al


def _v52_commonenemy_damage(self, miktar, kaynak=None):
    if not _v44_is_player_melee_source(kaynak):
        return _v52_commonenemy_damage_original(self, miktar, kaynak)
    adjusted = max(1, int(round(float(miktar) * v52_damage_multiplier())))
    return _v52_commonenemy_damage_original(self, adjusted, kaynak)


CommonEnemy.hasar_al = _v52_commonenemy_damage
# </POTBO_STAGE S1256>

# <POTBO_STAGE S1284>


# Contact quality slightly modifies player melee damage, but only inside ±8%.
_v54_commonenemy_damage_original = CommonEnemy.hasar_al


def _v54_commonenemy_damage(self, miktar, kaynak=None):
    if not _v44_is_player_melee_source(kaynak):
        return _v54_commonenemy_damage_original(self, miktar, kaynak)
    quality = v54_contact_quality(self)
    edge = v54_edge_efficiency(self)
    scalar = 0.96 + quality * 0.08
    scalar *= v44_clamp(0.98 + (edge - 0.86) * 0.18, 0.97, 1.03)
    adjusted = max(1, int(round(float(miktar) * scalar)))
    return _v54_commonenemy_damage_original(self, adjusted, kaynak)


CommonEnemy.hasar_al = _v54_commonenemy_damage
# </POTBO_STAGE S1284>

# <POTBO_STAGE S1289>
V55_SMEAR_ENEMY_INTERVAL_MS = 210
# </POTBO_STAGE S1289>

# <POTBO_STAGE S1292>
v55_enemy_motion = {}
# </POTBO_STAGE S1292>

# <POTBO_STAGE S1300>


def v55_diagnostics():
    return {
        "version": V55_VERSION,
        "player_transfer": round(float(v55_player_transfer), 4),
        "enemy_transfer_states": len(v55_enemy_motion),
        "pool_clusters": len(v55_pool_clusters),
        "smears_created": int(v55_smear_count),
        "pool_scan_next": int(v55_pool_next_scan_ms),
    }
# </POTBO_STAGE S1300>

# <POTBO_STAGE S1302>

V56_ENEMY_RHYTHM = {
    "crawler": {
        "ideal_range": 35.0,
        "commit_range": 44.0,
        "angle_tolerance_deg": 68.0,
        "reposition_ms": 220,
        "miss_grace_ms": 190,
        "repeat_penalty_ms": 120,
        "side_step": 7.0,
        "prediction_ms": 92,
    },
    "berserker": {
        "ideal_range": 42.0,
        "commit_range": 52.0,
        "angle_tolerance_deg": 58.0,
        "reposition_ms": 310,
        "miss_grace_ms": 250,
        "repeat_penalty_ms": 160,
        "side_step": 9.0,
        "prediction_ms": 118,
    },
    "tarkard": {
        "ideal_range": 49.0,
        "commit_range": 61.0,
        "angle_tolerance_deg": 52.0,
        "reposition_ms": 390,
        "miss_grace_ms": 320,
        "repeat_penalty_ms": 210,
        "side_step": 8.0,
        "prediction_ms": 138,
    },
    "torrmund": {
        "ideal_range": 52.0,
        "commit_range": 64.0,
        "angle_tolerance_deg": 48.0,
        "reposition_ms": 420,
        "miss_grace_ms": 340,
        "repeat_penalty_ms": 230,
        "side_step": 7.0,
        "prediction_ms": 146,
    },
    "headsthrower": {
        "ideal_range": 62.0,
        "commit_range": 74.0,
        "angle_tolerance_deg": 62.0,
        "reposition_ms": 280,
        "miss_grace_ms": 230,
        "repeat_penalty_ms": 150,
        "side_step": 10.0,
        "prediction_ms": 110,
    },
}

v56_enemy_state = {}
# </POTBO_STAGE S1302>

# <POTBO_STAGE S1305>


def v56_cfg(actor):
    return V56_ENEMY_RHYTHM.get(
        str(getattr(actor, "tur", "crawler")),
        V56_ENEMY_RHYTHM["crawler"],
    )


def v56_state(actor):
    uid = str(getattr(actor, "uid", id(actor)))
    state = v56_enemy_state.get(uid)
    if state is None:
        state = {
            "uid": uid,
            "last_attack_seen": int(getattr(actor, "last_attack_ms", -10000)),
            "last_commit_ms": -10000,
            "last_miss_ms": -10000,
            "repeat_count": 0,
            "lane_sign": random.choice((-1.0, 1.0)),
            "lane_hold_until": 0,
            "last_distance": 9999.0,
            "closing_rate": 0.0,
            "last_player_side": 0.0,
        }
        v56_enemy_state[uid] = state
    return state
# </POTBO_STAGE S1305>

# <POTBO_STAGE S1316>


# Track repeated attacks and misses from generic common enemy update without touching damage.
_v56_common_attack_update_original = (
    CommonEnemy._saldiri_guncelle if hasattr(CommonEnemy, "_saldiri_guncelle") else None
)
# </POTBO_STAGE S1316>

# <POTBO_STAGE S1318>


def v56_diagnostics():
    nearest = None
    nearest_dist = float("inf")
    for actor in v49_world_actor_list():
        if actor is None or not bool(getattr(actor, "active", False)):
            continue
        dist = v56_distance(actor)
        if dist < nearest_dist:
            nearest = actor
            nearest_dist = dist
    if nearest is None:
        return {
            "version": V56_VERSION,
            "tracked": len(v56_enemy_state),
            "nearest": None,
            "player_velocity": (
                round(v56_player_velocity.x, 2),
                round(v56_player_velocity.y, 2),
            ),
        }
    state = v56_state(nearest)
    return {
        "version": V56_VERSION,
        "tracked": len(v56_enemy_state),
        "nearest": str(getattr(nearest, "tur", "enemy")),
        "distance": round(nearest_dist, 2),
        "facing_quality": round(v56_facing_quality(nearest), 4),
        "closing_rate": round(float(state.get("closing_rate", 0.0)), 4),
        "repeat_count": int(state.get("repeat_count", 0)),
        "player_velocity": (
            round(v56_player_velocity.x, 2),
            round(v56_player_velocity.y, 2),
        ),
    }
# </POTBO_STAGE S1318>

# <POTBO_STAGE S1336>


# Melee damage chain'inin en dışına küçük tempo/yorulma katsayısı eklenir.
_v57_commonenemy_damage_original = CommonEnemy.hasar_al


def _v57_commonenemy_damage(self, miktar, kaynak=None):
    player_melee = _v44_is_player_melee_source(kaynak) and bool(oyuncu_saldiriyor)
    if not player_melee:
        return _v57_commonenemy_damage_original(self, miktar, kaynak)
    before_hp = float(getattr(self, "hp", 0.0))
    scalar = v57_flow_damage_scalar()
    v57_state["last_damage_scalar"] = scalar
    adjusted = max(1, int(round(float(miktar) * scalar)))
    result = _v57_commonenemy_damage_original(self, adjusted, kaynak)
    if float(getattr(self, "hp", before_hp)) < before_hp:
        v57_record_contact(self, adjusted, before_hp)
    return result


CommonEnemy.hasar_al = _v57_commonenemy_damage
# </POTBO_STAGE S1336>

# <POTBO_STAGE S1379>


# Technique damage seçimi damage chain'in dışında, mevcut precision/skill bonuslarının
# üstüne kontrollü eklenir. Aynı hit yalnız bir technique tetikleyebilir.
_v59_commonenemy_damage_original = CommonEnemy.hasar_al


def _v59_commonenemy_damage(self, miktar, kaynak=None):
    player_melee = _v44_is_player_melee_source(kaynak) and bool(oyuncu_saldiriyor)
    if not player_melee:
        return _v59_commonenemy_damage_original(self, miktar, kaynak)
    now = pygame.time.get_ticks()
    before_hp = float(getattr(self, "hp", 0.0))
    technique_id = v59_choose_technique(self, before_hp, now)
    definition = v59_activate(technique_id, now) if technique_id else None
    scalar = float(definition.get("damage", 1.0)) if definition else 1.0
    adjusted = max(1, int(round(float(miktar) * scalar)))
    result = _v59_commonenemy_damage_original(self, adjusted, kaynak)
    after_hp = float(getattr(self, "hp", before_hp))
    if after_hp < before_hp:
        direction = v57_attack_direction()
        v59_state["previous_direction"] = str(v59_state.get("last_direction", ""))
        v59_state["last_direction"] = direction
        previous_contact = int(v59_state.get("last_contact_ms", -10000))
        if now - previous_contact <= 850:
            v59_state["contact_index"] = min(
                9, int(v59_state.get("contact_index", 0)) + 1
            )
        else:
            v59_state["contact_index"] = 1
        v59_state["last_contact_ms"] = int(now)
    return result


CommonEnemy.hasar_al = _v59_commonenemy_damage
# </POTBO_STAGE S1379>

# <POTBO_STAGE S1389>

# CommonEnemy zaten temel poise kullanıyor. Bu katman poise kaybını yalnız damage'e değil,
# bıçağın anlık hızı, açı kalitesi, temas bölgesi ve hedef kütlesine bağlar. Sonuç:
# hızlı sıyırma ile ağır, derin temas aynı stagger davranışını üretmez.
V61_ENEMY_MASS = {
    "crawler": 0.72,
    "berserker": 1.18,
    "headsthrower": 0.86,
    "tarkard": 1.32,
    "torrmund": 1.72,
}
V61_ARMOR_RESPONSE = {
    "crawler": 0.02,
    "berserker": 0.10,
    "headsthrower": 0.04,
    "tarkard": 0.22,
    "torrmund": 0.48,
}
# </POTBO_STAGE S1389>

# <POTBO_STAGE S1391>


def v61_mass(enemy):
    return float(V61_ENEMY_MASS.get(str(getattr(enemy, "tur", "")), 1.0))
# </POTBO_STAGE S1391>

# <POTBO_STAGE S1397>


_v61_commonenemy_damage_original = CommonEnemy.hasar_al


def _v61_commonenemy_damage(self, miktar, kaynak=None):
    player_melee = _v44_is_player_melee_source(kaynak) and bool(oyuncu_saldiriyor)
    if not player_melee:
        return _v61_commonenemy_damage_original(self, miktar, kaynak)
    before_hp = float(getattr(self, "hp", 0.0))
    result = _v61_commonenemy_damage_original(self, miktar, kaynak)
    after_hp = float(getattr(self, "hp", before_hp))
    if after_hp < before_hp:
        v61_apply_reaction(self, before_hp - after_hp, before_hp)
    return result


CommonEnemy.hasar_al = _v61_commonenemy_damage
# </POTBO_STAGE S1397>

# <POTBO_STAGE S1437>

# Türlerin hepsi aynı kırmızıya düşmesin: doku profili + uid küçük tonal imza üretir.
# Renk farkı kontrollü tutulur; hiçbir profil parlak arcade kırmızısına çıkmaz.
V68_SIGNATURES = {
    "crawler": {"red": -10, "green": 0, "blue": 1, "sat": 0.94},
    "berserker": {
        "red": 5,
        "green": 0,
        "blue": -1,
        "sat": 1.04,
    },
    "headsthrower": {
        "red": -4,
        "green": 1,
        "blue": 2,
        "sat": 0.98,
    },
    "tarkard": {"red": -15, "green": 0, "blue": 3, "sat": 0.90},
    "torrmund": {"red": 2, "green": 1, "blue": 0, "sat": 0.97},
    "player_male": {
        "red": 4,
        "green": 0,
        "blue": 0,
        "sat": 1.02,
    },
    "player_female": {
        "red": 7,
        "green": 0,
        "blue": -1,
        "sat": 1.03,
    },
    "default": {"red": 0, "green": 0, "blue": 0, "sat": 1.0},
}
# </POTBO_STAGE S1437>

# <POTBO_STAGE S1441>


def v68_context_signature_key():
    ctx = v44_context_current() or {}
    if not isinstance(ctx, dict):
        return "default"
    tissue_key = str(ctx.get("tissue_key", ""))
    if tissue_key in V68_SIGNATURES:
        return tissue_key
    target = str(ctx.get("target", ""))
    if target in V68_SIGNATURES:
        return target
    enemy_type = str(ctx.get("enemy_type", ""))
    if enemy_type in V68_SIGNATURES:
        return enemy_type
    if target == "player":
        return "player_female" if karakter_cinsiyet == "female" else "player_male"
    return "default"
# </POTBO_STAGE S1441>

# <POTBO_STAGE S1445>


def _v44_damage_context_for_enemy(enemy, amount, source):
    context = _v68_damage_context_original(enemy, amount, source)
    context["enemy_type"] = str(getattr(enemy, "tur", "default"))
    context["target_uid"] = str(getattr(enemy, "uid", ""))
    context["tissue_key"] = str(getattr(enemy, "tur", "default"))
    return context
# </POTBO_STAGE S1445>

# <POTBO_STAGE S1511>


# ---------------------------------------------------------
# RAT ECOLOGY: KURTÇUK AVCISI + YAVAŞ KAN/ORGAN TEMİZLİĞİ
# ---------------------------------------------------------
def v75_local_feeding_rats(rat, kind, radius=48.0):
    here = pygame.Vector2(float(rat.x), float(rat.y))
    count = 0
    for other in ambient_rats:
        if not getattr(other, "active", False):
            continue
        if getattr(other, "food_kind", None) != kind:
            continue
        if (
            here - pygame.Vector2(float(other.x), float(other.y))
        ).length_squared() <= float(radius) ** 2:
            count += 1
    return max(1, count)
# </POTBO_STAGE S1511>

# <POTBO_STAGE S1519>


# ---------------------------------------------------------
# SADE / İŞE YARAR LOADING İPUÇLARI
# ---------------------------------------------------------
IPUCLARI = {
    "TR": [
        "J'ye kısa bas: normal saldırı.",
        "J'yi tutup bırak: ağır saldırı; daha çok stamina ister.",
        "Staminanın son kısmını dash veya savunma için sakla.",
        "K ile savun; uzun süre tutmak staminayı hızla tüketir.",
        "Düşmanın hazırlık animasyonu saldırının yönünü ele verir.",
        "Heads Thrower'a düz bir atış hattı bırakma.",
        "Tarkard ağır saldırıdan sonra kısa süre açık verir.",
        "Q hızlı slot büyüler içindir.",
        "Ateş büyüsünü kaçış yolunu kapatmayacak noktaya bırak.",
        "Zor bir savaştan önce F5 ile kaydet.",
        "Kan 20 dakikada tamamen kurur; kendi kendine silinmez.",
        "Fareler kurtçukları ve organları yer; kan lekeleri kalıcıdır.",
    ],
    "EN": [
        "Tap J for a normal attack.",
        "Hold and release J for a heavy attack; it costs more stamina.",
        "Keep the last part of your stamina for a dash or guard.",
        "Hold K to guard; holding it too long drains stamina quickly.",
        "An enemy's wind-up usually reveals the direction of the attack.",
        "Do not give Heads Thrower a clean firing lane.",
        "Tarkard is briefly exposed after a heavy attack.",
        "The Q quick slot is used for spells.",
        "Place fire where it will not block your own escape.",
        "Save with F5 before a difficult fight.",
        "Blood fully dries in 20 minutes and does not vanish by itself.",
        "Rats eat maggots and organs; every blood stain remains permanently.",
    ],
}
# </POTBO_STAGE S1519>

# <POTBO_STAGE S1564>


# -----------------------
# Enemy recoil and rage.
# -----------------------
V78_RAGE_PROFILES = {
    "crawler": {
        "threshold": 0.46,
        "move_mul": 1.14,
        "attack_mul": 0.86,
    },
    "berserker": {
        "threshold": 0.48,
        "move_mul": 1.17,
        "attack_mul": 0.80,
    },
    "headsthrower": {
        "threshold": 0.42,
        "move_mul": 1.08,
        "attack_mul": 0.84,
    },
    "tarkard": {
        "threshold": 0.34,
        "move_mul": 1.06,
        "attack_mul": 0.92,
    },
    "torrmund": {
        "threshold": 0.36,
        "move_mul": 1.07,
        "attack_mul": 0.94,
    },
}
V78_RECOIL_SCALE = {
    "crawler": 0.36,
    "berserker": 0.26,
    "headsthrower": 0.44,
    "tarkard": 0.04,
    "torrmund": 0.0,
}


def v78_enemy_rage(actor):
    profile = V78_RAGE_PROFILES.get(str(getattr(actor, "tur", "")))
    if not profile:
        return 0.0
    hp = float(getattr(actor, "hp", 0.0))
    max_hp = max(1.0, float(getattr(actor, "max_hp", 1.0)))
    ratio = hp / max_hp
    threshold = float(profile["threshold"])
    if ratio >= threshold:
        return 0.0
    return _v78_smoothstep01((threshold - ratio) / max(0.001, threshold))


_v78_common_move_original = CommonEnemy._anlik_move_speed


def _v78_common_move_speed(self):
    base = _v78_common_move_original(self)
    rage = v78_enemy_rage(self)
    if rage <= 0.0:
        return base
    profile = V78_RAGE_PROFILES.get(self.tur)
    if not profile:
        return base
    mul = 1.0 + (float(profile["move_mul"]) - 1.0) * rage
    return base * mul


CommonEnemy._anlik_move_speed = _v78_common_move_speed


_v78_common_attack_total_original = CommonEnemy._attack_total_ms


def _v78_common_attack_total(self):
    total = _v78_common_attack_total_original(self)
    profile = V78_RAGE_PROFILES.get(str(getattr(self, "tur", "")))
    rage = v78_enemy_rage(self)
    if not profile or rage <= 0.0:
        return total
    mul = 1.0 + (float(profile["attack_mul"]) - 1.0) * rage
    return max(1, int(round(total * mul)))


CommonEnemy._attack_total_ms = _v78_common_attack_total


_v78_tarkard_attack_total_original = TarkardEnemy._attack_total_ms
_v78_torrmund_attack_total_original = SirTorrmundEnemy._attack_total_ms


def _v78_tarkard_attack_total(self):
    total = _v78_tarkard_attack_total_original(self)
    rage = v78_enemy_rage(self)
    if rage <= 0.0:
        return total
    mul = 1.0 + (V78_RAGE_PROFILES["tarkard"]["attack_mul"] - 1.0) * rage
    return max(1, int(round(total * mul)))


def _v78_torrmund_attack_total(self):
    total = _v78_torrmund_attack_total_original(self)
    rage = v78_enemy_rage(self)
    if rage <= 0.0:
        return total
    mul = 1.0 + (V78_RAGE_PROFILES["torrmund"]["attack_mul"] - 1.0) * rage
    return max(1, int(round(total * mul)))


TarkardEnemy._attack_total_ms = _v78_tarkard_attack_total
SirTorrmundEnemy._attack_total_ms = _v78_torrmund_attack_total


_v78_common_hasar_original = CommonEnemy.hasar_al
# </POTBO_STAGE S1564>

# <POTBO_STAGE S1566>


CommonEnemy.hasar_al = _v78_common_hasar


_v78_common_saldiri_baslat_original = CommonEnemy._saldiri_baslat


def _v78_common_saldiri_baslat(self, simdi):
    _v78_common_saldiri_baslat_original(self, simdi)
    if self.tur == "berserker":
        rage = v78_enemy_rage(self)
        if rage > 0.0:
            waited = random.randint(
                int(self.cfg.get("chase_dash_min_wait_ms", 2800) * (1.0 - 0.22 * rage)),
                int(self.cfg.get("chase_dash_max_wait_ms", 4600) * (1.0 - 0.18 * rage)),
            )
            self.next_chase_dash_ms = min(
                int(self.next_chase_dash_ms),
                int(simdi) + max(700, waited),
            )


CommonEnemy._saldiri_baslat = _v78_common_saldiri_baslat


_v78_heads_thrower_state_original = HeadsThrowerEnemy._ranged_state_guncelle


def _v78_heads_thrower_state(self, dt, simdi):
    result = _v78_heads_thrower_state_original(self, dt, simdi)
    rage = v78_enemy_rage(self)
    if result and self.ranged_state == "recovery" and rage > 0.0:
        self.ranged_state_started_ms -= int(55 * rage)
    return result


HeadsThrowerEnemy._ranged_state_guncelle = _v78_heads_thrower_state


_v78_heads_thrower_tactic_original = HeadsThrowerEnemy._taktik_ranged_hedef


def _v78_headsthrower_tactic(self, simdi, digerler, mesafe, los):
    target = pygame.Vector2(
        _v78_heads_thrower_tactic_original(self, simdi, digerler, mesafe, los)
    )
    rage = v78_enemy_rage(self)
    player = pygame.Vector2(oyuncu_x, oyuncu_y)
    here = pygame.Vector2(self.x, self.y)
    away = here - player
    if away.length_squared() <= 1e-6:
        away = pygame.Vector2(1.0, 0.0)
    away = away.normalize()
    # Korkak karakter: fazla yaklaşınca alan açar; canı düşünce daha da huzursuz olur.
    if mesafe < float(self.cfg.get("ranged_preferred", 305.0)) - 12.0 or rage > 0.25:
        extra = 18.0 + 34.0 * rage
        pushed = target + away * extra
        if common_enemy_statik_konum_gecerli_mi(
            self.tur, pushed.x, pushed.y, navigation=True
        ):
            target = pushed
    return target


HeadsThrowerEnemy._taktik_ranged_hedef = _v78_headsthrower_tactic


_v78_tarkard_tactic_original = TarkardEnemy._taktik_hedef_sec


def _v78_tarkard_tactic(self, simdi, oyuncu_tahmin, digerler, oyuncu_hiz_vektoru):
    hedef = pygame.Vector2(
        _v78_tarkard_tactic_original(
            self,
            simdi,
            oyuncu_tahmin,
            digerler,
            oyuncu_hiz_vektoru,
        )
    )
    # Tarkard kaba güce güvenir: gereksiz geniş flank yerine daha doğrudan yaklaşsın.
    oyuncu = pygame.Vector2(oyuncu_tahmin)
    straight = oyuncu + (hedef - oyuncu) * 0.70
    if common_enemy_statik_konum_gecerli_mi(
        self.tur, straight.x, straight.y, navigation=True
    ):
        return straight
    return hedef


TarkardEnemy._taktik_hedef_sec = _v78_tarkard_tactic


def _v78_player_stronger_against_torrmund(actor):
    player_ratio = float(oyuncu_hp) / max(1.0, float(oyuncu_max_hp))
    enemy_ratio = float(getattr(actor, "hp", 0.0)) / max(
        1.0, float(getattr(actor, "max_hp", 1.0))
    )
    level_edge = float(globals().get("oyuncu_level", 1)) >= max(
        18.0, float(getattr(actor, "level", 25)) - 4.0
    )
    return level_edge or (player_ratio > 0.68 and enemy_ratio < 0.52)


_v78_torrmund_tactic_original = SirTorrmundEnemy._taktik_hedef_sec


def _v78_torrmund_tactic(self, simdi, oyuncu_tahmin, digerler, oyuncu_hiz_vektoru):
    hedef = pygame.Vector2(
        _v78_torrmund_tactic_original(
            self,
            simdi,
            oyuncu_tahmin,
            digerler,
            oyuncu_hiz_vektoru,
        )
    )
    if _v78_player_stronger_against_torrmund(self):
        oyuncu = pygame.Vector2(oyuncu_tahmin)
        away = hedef - oyuncu
        if away.length_squared() <= 1e-6:
            away = pygame.Vector2(self.x - oyuncu.x, self.y - oyuncu.y)
        if away.length_squared() <= 1e-6:
            away = pygame.Vector2(1.0, 0.0)
        away = away.normalize()
        cautious = oyuncu + away * 102.0
        if common_enemy_statik_konum_gecerli_mi(
            self.tur, cautious.x, cautious.y, navigation=True
        ):
            hedef = cautious
    return hedef


SirTorrmundEnemy._taktik_hedef_sec = _v78_torrmund_tactic


_v78_torrmund_attack_start_original = SirTorrmundEnemy._saldiri_baslat


def _v78_torrmund_attack_start(self, simdi):
    if _v78_player_stronger_against_torrmund(self) and random.random() < 0.42:
        self.attack_variant = "cleave"
    _v78_torrmund_attack_start_original(self, simdi)


SirTorrmundEnemy._saldiri_baslat = _v78_torrmund_attack_start
# </POTBO_STAGE S1566>

# <POTBO_STAGE S1586>

# AI kararları biraz daha sık güncellenir; hareket fizik katmanı yine dt tabanlıdır.
COMMON_ENEMY_LOCAL_TICK_MS.update(
    {
        "crawler": 62,
        "berserker": 55,
        "headsthrower": 61,
        "tarkard": 68,
        "torrmund": 74,
    }
)
COMMON_ENEMY_NAV_FOLLOW_TICK_MS.update(
    {
        "crawler": 84,
        "berserker": 74,
        "headsthrower": 81,
        "tarkard": 75,
        "torrmund": 79,
    }
)

# Türlerin kişiliği korunarak hareket/atak akıcılığı artırılır.
_v79_enemy_tuning = {
    "crawler": {
        "move_speed": 153.0,
        "acceleration": 920.0,
        "steering_lambda": 13.0,
        "attack_cooldown_ms": 1010,
        "attack_frame_ms": 72,
    },
    "berserker": {
        "move_speed": 258.0,
        "acceleration": 1370.0,
        "steering_lambda": 14.4,
        "attack_cooldown_ms": 780,
        "attack_frame_ms": 84,
    },
    "headsthrower": {
        "move_speed": 150.0,
        "acceleration": 900.0,
        "steering_lambda": 11.6,
        "attack_recovery_ms": 570,
    },
    "tarkard": {
        "move_speed": 132.0,
        "acceleration": 720.0,
        "steering_lambda": 9.7,
        "attack_cooldown_ms": 1580,
        "attack_frame_ms": 118,
    },
    "torrmund": {
        "move_speed": 118.0,
        "acceleration": 650.0,
        "steering_lambda": 8.9,
        "attack_cooldown_ms": 2100,
        "attack_frame_ms": 136,
    },
}
for _v79_enemy_type, _v79_values in _v79_enemy_tuning.items():
    if _v79_enemy_type in COMMON_ENEMY_CONFIG:
        COMMON_ENEMY_CONFIG[_v79_enemy_type].update(_v79_values)

# Heads Thrower'ın taşı hâlâ okunabilir; yalnız boşta bekleme daha azdır.
if "headsthrower" in COMMON_ENEMY_CONFIG:
    COMMON_ENEMY_CONFIG["headsthrower"].update(
        {
            "ranged_throw_cooldown_min_ms": 2160,
            "ranged_throw_cooldown_max_ms": 2860,
            "ranged_projectile_flight_min_ms": 650,
            "ranged_projectile_flight_max_ms": 855,
        }
    )
# </POTBO_STAGE S1586>

# <POTBO_STAGE S1623>


def _v81_reset_death_blood():
    global v81_death_blood
    v81_death_blood = {
        "start_ms": pygame.time.get_ticks(),
        "seed": int(
            oyuncu_olum_koreografi_seed
            or oyuncu_olum_patlama_seed
            or oyuncu_olum_ates_seed
            or random.randint(1, 2_000_000)
        ),
        "drops": [],
        "seeps": [],
        "burst_serial": 0,
    }

    alt = str(oyuncu_olum_alt_turu or "")
    dtype = str(oyuncu_olum_turu or "blood")
    impact = _v81_impact_direction()
    f, side = _v81_body_basis()

    # İlk öldürücü darbenin yarası. Hazır göl değil: önce fışkırma, sonra düşen
    # damlaların oluşturduğu lekeler ve yara çevresindeki yavaş sızıntı.
    if dtype == "blood":
        if alt == "headshot":
            origin = _v81_wound_origin(0.0, -7.0)
            _v81_add_arterial_sequence(
                origin,
                impact.rotate(random.uniform(-10.0, 10.0)),
                0.90,
                0,
                31.0,
                21,
            )
        elif alt.startswith("torrmund_"):
            origin = _v81_wound_origin(random.uniform(-2.0, 2.0), -1.0)
            if "bisect" in alt:
                # Büyük kesik tek noktadan kusursuz fan üretmez; iki damar hattı birbirinden
                # az farklı açılarla boşalır.
                _v81_add_arterial_sequence(
                    origin + side * 4.0,
                    impact.rotate(-19.0),
                    1.24,
                    0,
                    25.0,
                    31,
                )
                _v81_add_arterial_sequence(
                    origin - side * 5.0,
                    impact.rotate(24.0),
                    1.02,
                    75,
                    22.0,
                    32,
                )
            else:
                _v81_add_arterial_sequence(
                    origin,
                    impact.rotate(-8.0),
                    1.18,
                    0,
                    28.0,
                    33,
                )
        elif alt == "tarkard_crush":
            origin = _v81_wound_origin(random.uniform(-4.0, 4.0), 1.0)
            _v81_add_arterial_sequence(
                origin,
                impact.rotate(random.uniform(-18.0, 18.0)),
                1.08,
                0,
                20.0,
                41,
            )
            _v81_add_burst(
                origin + side * 5.0,
                impact.rotate(62.0),
                18,
                0.80,
                110,
                58.0,
                15.0,
                0.70,
                True,
                42,
            )
        else:
            origin = _v81_wound_origin(
                random.uniform(-3.5, 3.5),
                random.uniform(-4.0, 3.0),
            )
            _v81_add_arterial_sequence(origin, impact, 1.0, 0, 22.0, 11)

    elif dtype in ("blast_core", "blast_inner", "blast_mid"):
        origin = _v81_wound_origin(0.0, 0.0)
        # Patlama, karakterin yönüne göre ileri + iki yan kola ayrılır. "up/down" ekran
        # ekseni değil karakterin ileri/geri doğrultusudur.
        dirs = (f.rotate(-68.0), f.rotate(4.0), f.rotate(72.0))
        for i, d in enumerate(dirs):
            _v81_add_burst(
                origin + side * ((i - 1) * 3.5),
                d,
                37 if i == 1 else 29,
                1.18 if i == 1 else 0.98,
                i * 42,
                38.0 if i == 1 else 48.0,
                31.0 if i == 1 else 25.0,
                1.18 if i == 1 else 0.94,
                True,
                61 + i,
            )

    elif dtype == "fire":
        origin = _v81_wound_origin(0.0, 0.0)
        _v81_add_burst(
            origin,
            impact.rotate(12.0),
            22,
            0.68,
            0,
            44.0,
            15.0,
            0.62,
            True,
            71,
        )
# </POTBO_STAGE S1623>

# <POTBO_STAGE S1629>


def _v81_final_attack_frame(actor):
    tur = str(getattr(actor, "tur", ""))
    try:
        if tur == "headsthrower":
            frames = HEADSTHROWER_SPRITELERI.get("idle", [])
        elif tur == "tarkard":
            frames = (
                actor._attack_frames()
                if hasattr(actor, "_attack_frames")
                else TARKARD_SPRITELERI.get("heavy", [])
            )
        elif tur == "torrmund":
            frames = (
                actor._attack_frames()
                if hasattr(actor, "_attack_frames")
                else TORRMUND_SPRITELERI.get("execution", [])
            )
        else:
            frames = []
        return frames[-1] if frames else None
    except Exception:
        return None


def _v30_katil_koreografi_frame(actor, simdi):
    if actor is None or oyuncu_olum_baslangic_ms <= 0:
        return None
    tur = str(getattr(actor, "tur", ""))
    alt = str(oyuncu_olum_alt_turu or "")

    # Yalnız bu üç durumda ölüm sonrası yeni saldırı animasyonu vardır.
    if tur == "crawler" and alt == "crawler":
        return _v81_katil_frame_original(actor, simdi)
    if tur == "berserker" and alt == "berserker":
        return _v81_katil_frame_original(actor, simdi)
    if tur == "torrmund" and alt == "torrmund_decap_cleave":
        return _v81_katil_frame_original(actor, simdi)

    # Diğer katiller öldürücü darbenin son pozunda/idle'da donar; yeni swing yok.
    frozen = _v81_final_attack_frame(actor)
    if frozen is not None:
        return frozen
    return None


def _v81_post_hit_blood(kind, index, base, now):
    f, side = _v81_body_basis()
    rng = _v81_rng(200 + index * 13 + sum(ord(c) for c in str(kind)))
    if kind == "crawler":
        origin = _v81_wound_origin(rng.uniform(-7.0, 7.0), rng.uniform(-5.0, 5.0))
        d = pygame.Vector2(base).rotate(rng.uniform(-32.0, 35.0))
        _v81_add_burst(
            origin,
            d,
            rng.randint(18, 25),
            0.88 + index * 0.035,
            0,
            52.0,
            rng.uniform(12.0, 20.0),
            0.82,
            True,
            211 + index,
        )
    elif kind == "berserker":
        origin = _v81_wound_origin(rng.uniform(-8.0, 8.0), rng.uniform(-5.0, 6.0))
        d = pygame.Vector2(base).rotate(rng.uniform(-26.0, 28.0))
        _v81_add_burst(
            origin,
            d,
            rng.randint(25, 34),
            1.12 + index * 0.045,
            0,
            46.0,
            rng.uniform(17.0, 26.0),
            0.96,
            True,
            311 + index,
        )
    elif kind == "torrmund_second":
        # İkinci infaz darbesi bedeni ikiye ayırır: iki ayrı yara hattı aynı yöne
        # kusursuz simetriyle değil, farklı basınçlarla boşalır.
        o1 = _v81_wound_origin(-5.5, 0.0)
        o2 = _v81_wound_origin(6.5, 1.5)
        _v81_add_arterial_sequence(
            o1,
            pygame.Vector2(base).rotate(-31.0),
            1.28,
            0,
            27.0,
            411,
        )
        _v81_add_arterial_sequence(
            o2,
            pygame.Vector2(base).rotate(37.0),
            1.08,
            55,
            24.0,
            412,
        )
# </POTBO_STAGE S1629>

# <POTBO_STAGE S1674>


def _v82_hit_kind(enemy, lethal=False, heavy=False):
    uid = str(getattr(enemy, "uid", ""))
    state = (
        v61_reactions.get(uid, {})
        if isinstance(globals().get("v61_reactions"), dict)
        else {}
    )
    kind = str(state.get("kind", "clean"))
    depth = float(state.get("depth", 0.62))
    armor = float(state.get("armor", 0.0))
    fully_armored = (
        bool(getattr(enemy, "cfg", {}).get("fully_armored", False))
        or str(getattr(enemy, "tur", "")) == "torrmund"
    )
    if lethal:
        return "lethal", depth, armor
    if fully_armored or armor >= 0.72:
        return "armor", depth, armor
    if heavy:
        return "heavy", depth, armor
    if kind == "deep" or depth >= 0.78:
        return "deep", depth, armor
    if kind == "glance" or depth <= 0.38:
        return "glance", depth, armor
    return "clean", depth, armor
# </POTBO_STAGE S1674>

# <POTBO_STAGE S1677>


_v82_common_hasar_original = CommonEnemy.hasar_al
# </POTBO_STAGE S1677>

# <POTBO_STAGE S1679>


CommonEnemy.hasar_al = _v82_common_hasar
# </POTBO_STAGE S1679>

# <POTBO_STAGE S1724>

V84_RIPOSTE_PROFILES = {
    "crawler": {
        "damage": 1.78,
        "poise": 0.78,
        "stagger_ms": 470,
        "armor": "unarmored",
    },
    "headsthrower": {
        "damage": 1.66,
        "poise": 0.70,
        "stagger_ms": 450,
        "armor": "unarmored",
    },
    "berserker": {
        "damage": 1.48,
        "poise": 0.60,
        "stagger_ms": 420,
        "armor": "hide",
    },
    "tarkard": {
        "damage": 1.28,
        "poise": 0.38,
        "stagger_ms": 300,
        "armor": "plate",
    },
    "torrmund": {
        "damage": 1.20,
        "poise": 0.31,
        "stagger_ms": 250,
        "armor": "boss_plate",
    },
}
# </POTBO_STAGE S1724>

# <POTBO_STAGE S1728>


def v84_hostile_actors(include_suspended=True):
    result = []
    seen = set()
    candidates = list(common_enemies)
    candidates.extend((tarkard_actor, torrmund_actor))
    for actor in candidates:
        if actor is None:
            continue
        key = id(actor)
        if key in seen:
            continue
        seen.add(key)
        if v84_actor_alive(actor, include_suspended=include_suspended):
            result.append(actor)
    return result
# </POTBO_STAGE S1728>

# <POTBO_STAGE S1732>


def v84_fallback_actor_surface(actor):
    tur = str(getattr(actor, "tur", "enemy"))
    sizes = {
        "crawler": (46, 48),
        "berserker": (58, 74),
        "headsthrower": (54, 70),
        "tarkard": (68, 86),
        "torrmund": (72, 96),
    }
    width, height = sizes.get(tur, (54, 70))
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    points = [
        (width // 2, 1),
        (width - 8, height // 4),
        (width - 3, height - 13),
        (width * 3 // 4, height - 2),
        (width // 2, height - 9),
        (width // 4, height - 2),
        (3, height - 13),
        (8, height // 4),
    ]
    pygame.draw.polygon(surface, (*V84_BODY, 255), points)
    return surface.convert_alpha()


def v84_actor_silhouette(actor):
    frame = v84_actor_frame(actor)
    if frame is None:
        return v84_fallback_actor_surface(actor)
    cfg = getattr(actor, "cfg", {}) or {}
    factor = float(cfg.get("sprite_scale", 1.0)) * KAMERA_YAKINLASTIRMA
    size = (
        max(1, int(round(frame.get_width() * factor))),
        max(1, int(round(frame.get_height() * factor))),
    )
    image = pygame.transform.scale(frame, size)
    tur = str(getattr(actor, "tur", ""))
    direction = str(
        getattr(
            actor,
            "visual_direction",
            getattr(actor, "direction", "left"),
        )
    )
    if tur == "crawler":
        if str(getattr(actor, "direction", "left")) == "right":
            image = pygame.transform.flip(image, True, False)
    elif tur in ("headsthrower", "tarkard", "torrmund"):
        if direction == "left":
            image = pygame.transform.flip(image, True, False)
    mask = pygame.mask.from_surface(image, 1)
    return mask.to_surface(
        setcolor=(*V84_BODY, 255),
        unsetcolor=(0, 0, 0, 0),
    ).convert_alpha()
# </POTBO_STAGE S1732>

# <POTBO_STAGE S1763>


def v84_execution_target_score(actor, facing, override):
    distance = v84_actor_distance(actor)
    to_target = pygame.Vector2(
        float(actor.x) - float(oyuncu_x),
        float(actor.y) - float(oyuncu_y),
    )
    alignment = 0.0
    if to_target.length_squared() > 1e-8:
        alignment = facing.dot(to_target.normalize())
    eligible_bonus = -92.0 if v84_execution_naturally_eligible(actor) else 0.0
    boss_penalty = (
        8.0 if str(getattr(actor, "tur", "")) in ("tarkard", "torrmund") else 0.0
    )
    override_bias = (
        0.0 if override else max(0.0, distance - V84_EXECUTION_NATURAL_RANGE) * 5.0
    )
    return distance - alignment * 34.0 + eligible_bonus + boss_penalty + override_bias
# </POTBO_STAGE S1763>

# <POTBO_STAGE S1784>


def v84_wound_zone(actor, seed):
    tur = str(getattr(actor, "tur", "enemy"))
    tables = {
        "crawler": (
            "neck",
            "thorax",
            "forelimb",
            "abdomen",
        ),
        "berserker": (
            "neck",
            "shoulder",
            "abdomen",
            "thigh",
        ),
        "headsthrower": (
            "neck",
            "arm",
            "chest",
            "abdomen",
        ),
        "tarkard": (
            "armor_gap",
            "armpit",
            "inner_elbow",
            "hamstring",
        ),
        "torrmund": (
            "gorget_gap",
            "pauldron_gap",
            "inner_elbow",
            "knee_gap",
        ),
    }
    options = tables.get(
        tur,
        ("neck", "chest", "abdomen", "limb"),
    )
    return options[int(seed) % len(options)]
# </POTBO_STAGE S1784>

# <POTBO_STAGE S1789>


_v84_enemy_damage_original = CommonEnemy.hasar_al


def _v84_enemy_damage(self, miktar, kaynak=None):
    now = pygame.time.get_ticks()
    riposte = v84_riposte_matches(self, kaynak)
    profile = darbe_profili_belirle(
        kaynak,
        str(getattr(self, "tur", "enemy")),
    )
    incoming_damage = max(1, int(miktar))
    adjusted = incoming_damage
    if riposte:
        riposte_profile = v84_riposte_profile(self)
        adjusted = max(
            1,
            int(
                round(
                    incoming_damage
                    * float(riposte_profile["damage"])
                    * (0.96 + 0.08 * v84_riposte_state.quality)
                )
            ),
        )
    before_hp = int(getattr(self, "hp", 0))
    result = _v84_enemy_damage_original(
        self,
        adjusted,
        kaynak,
    )
    after_hp = int(getattr(self, "hp", 0))
    landed = before_hp > after_hp or int(result or 0) > 0
    if not landed:
        return result

    is_melee = _v44_is_player_melee_source(kaynak)
    if is_melee:
        source_x = float(oyuncu_x)
        source_y = float(oyuncu_y)
        direction = pygame.Vector2(
            float(self.x) - source_x,
            float(self.y) - source_y,
        )
        v84_wound_register(
            self,
            max(1, before_hp - after_hp),
            profile,
            direction,
            source="melee",
            now=now,
        )

    if riposte:
        riposte_profile = v84_riposte_profile(self)
        maximum = v84_actor_poise_max(self)
        broken = v84_apply_poise_damage(
            self,
            maximum * float(riposte_profile["poise"]),
            now,
            int(riposte_profile["stagger_ms"]),
        )
        # Bosses keep their posture and phase logic.  Their poise advantage is
        # substantial, but the riposte never applies a floor knockdown.
        if str(getattr(self, "tur", "")) in (
            "tarkard",
            "torrmund",
        ):
            self.stagger_until = min(
                int(getattr(self, "stagger_until", now)),
                int(now) + int(riposte_profile["stagger_ms"]),
            )
            self.hit_stun_until = min(
                int(getattr(self, "hit_stun_until", now)),
                int(now) + int(riposte_profile["stagger_ms"]),
            )
        direction = pygame.Vector2(
            float(self.x) - oyuncu_x,
            float(self.y) - oyuncu_y,
        )
        direction = v84_safe_vector(direction).normalize()
        combat_impact_spawn(
            float(self.x),
            float(self.y) - 14.0,
            "slash_heavy",
            2.05,
            direction,
        )
        kan_parcacigi_patlat(
            float(self.x),
            float(self.y) - 12.0,
            random.randint(18, 27),
            1.28,
            yon=direction,
            arterial=bool(broken),
        )
        kamera_hit_sarsintisi_baslat(6.4, 168)
        v84_riposte_state.consumed = True
        v84_refresh_execution_window(self, now)
        dunya_olayi_kaydet(
            "riposte_hit",
            enemy=str(getattr(self, "tur", "enemy")),
            damage=max(1, before_hp - after_hp),
            poise_break=bool(broken),
            armor=v84_riposte_state.armor_breach,
        )
    elif after_hp > 0:
        v84_refresh_execution_window(self, now)
    return result


CommonEnemy.hasar_al = _v84_enemy_damage
# </POTBO_STAGE S1789>

# <POTBO_STAGE S1794>


_v84_common_update_original = common_enemy_guncelle


def common_enemy_guncelle():
    global v84_combat_last_tick_ms
    now = pygame.time.get_ticks()
    delta = max(
        0.0,
        min(
            0.05,
            (int(now) - int(v84_combat_last_tick_ms)) / 1000.0,
        ),
    )
    v84_combat_last_tick_ms = int(now)
    result = _v84_common_update_original()
    v84_execution_update(now)
    v84_wound_tick(now, delta)
    return result
# </POTBO_STAGE S1794>

# <POTBO_STAGE S1817>


_v84_integrity_update_original = common_enemy_guncelle


def common_enemy_guncelle():
    result = _v84_integrity_update_original()
    v84_integrity_tick(pygame.time.get_ticks())
    return result
# </POTBO_STAGE S1817>

# <POTBO_STAGE S1871>


_v85_common_update_original = common_enemy_guncelle


def common_enemy_guncelle():
    result = _v85_common_update_original()
    v85_mortal_wound_update(pygame.time.get_ticks())
    return result
# </POTBO_STAGE S1871>

# <POTBO_STAGE S1879>


_v85_hold_enemy_damage_original = CommonEnemy.hasar_al


def _v85_hold_enemy_damage(self, miktar, kaynak=None):
    is_hold = (
        oyuncu_saldiriyor
        and oyuncu_saldiri_modu == "hold_release"
        and _v44_is_player_melee_source(kaynak)
    )
    state = v85_hold_cross_state
    if (
        is_hold
        and state.hit_registered
        and int(state.attack_id) == int(saldiri_baslangic)
    ):
        # One heavy release is exactly one physical contact: it cannot damage a
        # second hurtbox or tick the original target again on a later active frame.
        return 0
    before = int(getattr(self, "hp", 0))
    result = _v85_hold_enemy_damage_original(self, miktar, kaynak)
    after = int(getattr(self, "hp", 0))
    if is_hold and before > after and not state.hit_registered:
        v85_hold_cross_begin(self, pygame.time.get_ticks())
    return result


CommonEnemy.hasar_al = _v85_hold_enemy_damage
# </POTBO_STAGE S1879>

# <POTBO_STAGE S1881>


_v85_hold_common_update_original = common_enemy_guncelle


def common_enemy_guncelle():
    result = _v85_hold_common_update_original()
    v85_hold_cross_update(pygame.time.get_ticks())
    return result
# </POTBO_STAGE S1881>

# <POTBO_STAGE S1906>
V86_CRAWLER_HIT_COUNT = 18
V86_CRAWLER_HIT_STEP_MS = 64
V86_BERSERKER_HIT_COUNT = 14
V86_BERSERKER_HIT_STEP_MS = 78
# </POTBO_STAGE S1906>

# <POTBO_STAGE S1916>


def v86_move_killer_to_front(state, now, dt):
    killer = state.killer
    if killer is None:
        if state.ready_ms <= 0:
            state.ready_ms = int(state.started_ms)
            state.attack_ms = state.ready_ms + V86_DEATH_FRONT_WAIT_MS
        return
    if state.ready_ms > 0:
        v86_face_killer_to_player(killer)
        return
    current = pygame.Vector2(float(killer.x), float(killer.y))
    target = pygame.Vector2(state.approach_target)
    delta = target - current
    if delta.length() <= 3.0:
        killer.x, killer.y = float(target.x), float(target.y)
        killer.vx = killer.vy = 0.0
        state.ready_ms = int(now)
        state.attack_ms = int(now) + V86_DEATH_FRONT_WAIT_MS
        state.phase = "wait"
        v86_face_killer_to_player(killer)
        return
    speed = {
        "crawler": 235.0,
        "berserker": 205.0,
        "tarkard": 178.0,
        "torrmund": 164.0,
    }.get(state.killer_type, 190.0)
    step = delta.normalize() * min(delta.length(), speed * float(dt))
    candidate = current + step
    try:
        valid = common_enemy_statik_konum_gecerli_mi(
            state.killer_type,
            candidate.x,
            candidate.y,
            navigation=True,
        )
    except (NameError, TypeError, ValueError):
        valid = True
    if not valid:
        axis_candidates = (
            pygame.Vector2(current.x + step.x, current.y),
            pygame.Vector2(current.x, current.y + step.y),
        )
        candidate = current
        for axis_candidate in axis_candidates:
            try:
                axis_valid = common_enemy_statik_konum_gecerli_mi(
                    state.killer_type,
                    axis_candidate.x,
                    axis_candidate.y,
                    navigation=True,
                )
            except (NameError, TypeError, ValueError):
                axis_valid = True
            if axis_valid:
                candidate = axis_candidate
                break
    killer.x, killer.y = float(candidate.x), float(candidate.y)
    killer.vx, killer.vy = (
        float(step.x / max(dt, 1e-6)),
        float(step.y / max(dt, 1e-6)),
    )
    state.phase = "approach"
    v86_face_killer_to_player(killer)
# </POTBO_STAGE S1916>

# <POTBO_STAGE S1926>


def v86_update_melee_death(state, now, dt):
    if state.death_kind not in ("crawler", "berserker", "tarkard", "torrmund"):
        return
    if not (state.one_shot and state.death_kind in ("tarkard", "torrmund")):
        v86_move_killer_to_front(state, now, dt)
    attack = int(state.attack_ms)
    if attack <= 0 or now < attack:
        return
    if state.death_kind == "crawler":
        for index in range(V86_CRAWLER_HIT_COUNT):
            if now >= attack + index * V86_CRAWLER_HIT_STEP_MS:
                v86_eroding_hit(state, index, berserker=False)
        finish = attack + (V86_CRAWLER_HIT_COUNT - 1) * V86_CRAWLER_HIT_STEP_MS
        if now >= finish + 125:
            v86_start_fall(
                state,
                finish + 125,
                470,
                push=v86_impact_direction(state) * 7.0,
            )
    elif state.death_kind == "berserker":
        for index in range(V86_BERSERKER_HIT_COUNT):
            if now >= attack + index * V86_BERSERKER_HIT_STEP_MS:
                v86_eroding_hit(state, index, berserker=True)
        finish = attack + (V86_BERSERKER_HIT_COUNT - 1) * V86_BERSERKER_HIT_STEP_MS
        if now >= finish + 110:
            v86_start_fall(
                state,
                finish + 110,
                390,
                push=v86_impact_direction(state) * 13.0,
            )
    elif state.death_kind == "tarkard":
        v86_tripartite_tarkard(state, now)
    elif state.death_kind == "torrmund":
        if state.one_shot:
            v86_torrmund_waist_bisect(state, now)
        else:
            v86_torrmund_decap(state, now)
            if now >= attack + 1220:
                v86_torrmund_second_cleave(state, now)


def v86_death_update(now=None):
    state = v86_death_state
    if not state.active:
        return
    if now is None:
        now = pygame.time.get_ticks()
    dt = max(
        0.0,
        min(0.05, (int(now) - int(state.last_tick_ms)) / 1000.0),
    )
    state.last_tick_ms = int(now)

    if state.death_kind in ("crawler", "berserker", "tarkard", "torrmund"):
        v86_update_melee_death(state, int(now), dt)
    elif state.death_kind == "headsthrower":
        v86_update_heads_thrower(state, int(now), dt)
    elif state.death_kind == "bomb":
        if int(now) >= int(state.attack_ms):
            v86_bomb_fragment(state, int(now))
    elif state.death_kind == "fire":
        if int(now) >= int(state.attack_ms) and "fire_fall" not in state.events:
            state.events.add("fire_fall")
            push = v86_impact_direction(state) * (18.0 if state.shockwave else 0.0)
            v86_start_fall(
                state,
                int(now),
                520 if state.shockwave else 760,
                push=push,
                rotation=state.fall_target_rotation,
            )
            if state.shockwave:
                kamera_hit_sarsintisi_baslat(9.8, 270)
    elif int(now) >= int(state.attack_ms) and "generic_fall" not in state.events:
        state.events.add("generic_fall")
        direction = v86_impact_direction(state)
        v86_blood_event(
            state,
            direction,
            1.12,
            zone="torso",
            tag=810,
            organs=3,
            arterial=True,
        )
        v86_start_fall(state, int(now), 450, push=direction * 7.0)

    if state.fall_started_ms > 0:
        p = v84_smootherstep(
            (int(now) - int(state.fall_started_ms))
            / max(1.0, float(state.fall_duration_ms))
        )
        state.body_rotation = state.fall_target_rotation * p
        state.body_offset = state.body_push * p
        state.body_offset.y += 4.0 * p
    elif state.death_kind == "fire":
        age = int(now) - int(state.started_ms)
        state.body_rotation = math.sin(age * 0.019) * 6.5
    else:
        state.body_rotation *= math.exp(-8.0 * dt)

    for piece in state.pieces:
        piece.update(dt)
    for debris in state.debris:
        debris.update(dt)
    state.rocks[:] = [
        rock for rock in state.rocks if int(now) <= int(rock.impact_ms) + 90
    ]
# </POTBO_STAGE S1926>

# <POTBO_STAGE S1928>


def v86_death_actor_frame(actor, now):
    state = v86_death_state
    if not state.active or actor is not state.killer:
        return None
    enemy_type = state.killer_type
    attack = int(state.attack_ms)
    try:
        crawler_finish = (
            attack + (V86_CRAWLER_HIT_COUNT - 1) * V86_CRAWLER_HIT_STEP_MS + 105
        )
        if (
            enemy_type == "crawler"
            and attack > 0
            and attack - 70 <= now <= crawler_finish
        ):
            frames = COMMON_ENEMY_SPRITELERI.get("crawler", {}).get("attack", [])
            if frames:
                local = max(0, now - attack)
                hit_phase = local % V86_CRAWLER_HIT_STEP_MS
                impact_index = min(len(frames) - 1, 12)
                return frames[
                    max(0, impact_index - 1)
                    if hit_phase < V86_CRAWLER_HIT_STEP_MS * 0.42
                    else impact_index
                ]
        berserker_finish = (
            attack + (V86_BERSERKER_HIT_COUNT - 1) * V86_BERSERKER_HIT_STEP_MS + 115
        )
        if (
            enemy_type == "berserker"
            and attack > 0
            and attack - 90 <= now <= berserker_finish
        ):
            direction = str(getattr(actor, "visual_direction", "right"))
            frames = (
                COMMON_ENEMY_SPRITELERI.get("berserker", {})
                .get("attack", {})
                .get(direction, [])
            )
            local = max(0, now - attack) % V86_BERSERKER_HIT_STEP_MS
            return v86_frame_progress(frames, local / V86_BERSERKER_HIT_STEP_MS)
        if enemy_type == "headsthrower" and attack > 0:
            local = now - attack
            if 520 <= local < 1120:
                frames = HEADSTHROWER_SPRITELERI.get("pickup", [])
                return v86_frame_progress(frames, (local - 520) / 600.0)
            if -320 <= local < 80 or 1080 <= local < 1600:
                frames = HEADSTHROWER_SPRITELERI.get("throw", [])
                start = -320 if local < 80 else 1080
                duration = 400.0 if local < 80 else 500.0
                return v86_frame_progress(frames, (local - start) / duration)
        if enemy_type == "tarkard" and attack > 0:
            frames = TARKARD_SPRITELERI.get("heavy", [])
            return v86_frame_progress(frames, (now - (attack - 520)) / 780.0)
        if enemy_type == "torrmund" and attack > 0:
            if not state.one_shot and now >= attack + 650:
                frames = TORRMUND_SPRITELERI.get("cleave", [])
                return v86_frame_progress(frames, (now - attack - 650) / 740.0)
            frames = TORRMUND_SPRITELERI.get("execution", [])
            return v86_frame_progress(frames, (now - (attack - 560)) / 790.0)
        _, frame = actor._animasyon_kare(int(now))
        return frame
    except (AttributeError, IndexError, KeyError, TypeError, ValueError):
        return None
# </POTBO_STAGE S1928>

# <POTBO_STAGE S1933>


def v86_rock_draw(rock, now, index):
    if int(now) < int(rock.started_ms) or int(now) > int(rock.impact_ms):
        return
    progress = v84_clamp01(
        (int(now) - int(rock.started_ms))
        / max(1.0, float(int(rock.impact_ms) - int(rock.started_ms)))
    )
    ground = rock.start.lerp(rock.target, v84_smootherstep(progress))
    height = 4.0 * float(rock.arc_height) * progress * (1.0 - progress)
    sx = float(dunya_ekran_x(ground.x))
    sy = float(dunya_ekran_y(ground.y)) - height * KAMERA_YAKINLASTIRMA - 24.0
    v86_ground_shadow(
        (dunya_ekran_x(ground.x), dunya_ekran_y(ground.y) - 1.0),
        8 if rock.second else 6,
        2,
    )
    image = None
    if HEADSTHROWER_ROCK_SPRITE is not None:
        scale = (0.80 if rock.second else 0.68) * KAMERA_YAKINLASTIRMA
        size = (
            max(1, int(round(HEADSTHROWER_ROCK_SPRITE.get_width() * scale))),
            max(1, int(round(HEADSTHROWER_ROCK_SPRITE.get_height() * scale))),
        )
        source = pygame.transform.scale(HEADSTHROWER_ROCK_SPRITE, size)
        mask = pygame.mask.from_surface(source, 1)
        image = mask.to_surface(
            setcolor=(*V84_BODY, 255), unsetcolor=(0, 0, 0, 0)
        ).convert_alpha()
        image = pygame.transform.rotate(image, progress * (610.0 + index * 73.0))
    if image is not None:
        ekran.blit(image, image.get_rect(center=(int(sx), int(sy))))
    else:
        radius = 8 if rock.second else 6
        pygame.draw.polygon(
            ekran,
            V84_BODY,
            (
                (int(sx - radius), int(sy)),
                (int(sx - radius * 0.25), int(sy - radius)),
                (int(sx + radius), int(sy - radius * 0.22)),
                (int(sx + radius * 0.42), int(sy + radius)),
            ),
        )


def v86_killer_draw(actor, now):
    if actor is None:
        return
    frame = v86_death_actor_frame(actor, now)
    if frame is None:
        surface = v84_fallback_actor_surface(actor)
    else:
        cfg = getattr(actor, "cfg", {}) or {}
        factor = float(cfg.get("sprite_scale", 1.0)) * KAMERA_YAKINLASTIRMA
        size = (
            max(1, int(round(frame.get_width() * factor))),
            max(1, int(round(frame.get_height() * factor))),
        )
        source = pygame.transform.scale(frame, size)
        enemy_type = str(getattr(actor, "tur", ""))
        direction = str(
            getattr(actor, "visual_direction", getattr(actor, "direction", "left"))
        )
        if enemy_type == "crawler":
            if str(getattr(actor, "direction", "left")) == "right":
                source = pygame.transform.flip(source, True, False)
        elif enemy_type in ("headsthrower", "tarkard", "torrmund"):
            if direction == "left":
                source = pygame.transform.flip(source, True, False)
        mask = pygame.mask.from_surface(source, 1)
        surface = mask.to_surface(
            setcolor=(*V84_BODY, 255), unsetcolor=(0, 0, 0, 0)
        ).convert_alpha()
    sx = float(dunya_ekran_x(float(getattr(actor, "x", oyuncu_x))))
    sy = float(dunya_ekran_y(float(getattr(actor, "y", oyuncu_y))))
    v86_ground_shadow(
        (sx, sy + 1.0),
        max(10.0, surface.get_width() * 0.34),
        max(2.0, surface.get_height() * 0.055),
    )
    rect = surface.get_rect(midbottom=(int(round(sx)), int(round(sy + 2.0))))
    ekran.blit(surface, rect)
    state = v86_death_state
    if state.death_kind != "fire" and int(now) >= int(state.attack_ms or now):
        point = _v24_katil_silah_kan_noktasi(actor)
        if point is not None:
            px = int(round(dunya_ekran_x(point.x)))
            py = int(round(dunya_ekran_y(point.y)))
            pygame.draw.line(ekran, V84_BLOOD, (px - 4, py), (px + 4, py + 2), 2)
# </POTBO_STAGE S1933>

# <POTBO_STAGE S1941>


def v84_timing_contract():
    burst = V84_EXECUTION_BEAT_TIMES[3 : 3 + V86_EXECUTION_BURST_COUNT]
    burst_intervals = tuple(later - earlier for earlier, later in zip(burst, burst[1:]))
    return {
        "strict_guard_ms": V84_PERFECT_GUARD_STRICT_MS,
        "standard_guard_ms": V84_PERFECT_GUARD_STANDARD_MS,
        "guard_immediate_intent_ms": V86_GUARD_INTENT_BUFFER_MS,
        "rear_attacks_rejected": V84_PERFECT_GUARD_FRONT_DOT_STANDARD > -0.25,
        "projectiles_rejected": not v84_direct_melee_source(
            "headsthrower_rock", oyuncu_x, oyuncu_y, None
        ),
        "execution_beats_monotonic": all(
            later > earlier
            for earlier, later in zip(
                V84_EXECUTION_BEAT_TIMES, V84_EXECUTION_BEAT_TIMES[1:]
            )
        ),
        "three_slow_fast_slow_openers": len(V86_EXECUTION_OPENERS) == 3,
        "asymmetric_x_burst_count": len(burst),
        "burst_is_ultrafast": bool(burst_intervals) and max(burst_intervals) <= 70,
        "retreat_ms": V86_EXECUTION_RETREAT_END_MS - V86_EXECUTION_REPOSITION_END_MS,
        "final_after_retreat": V86_EXECUTION_FINAL_IMPACT_MS
        > V86_EXECUTION_RETREAT_END_MS,
        "progress_bar": False,
        "total_ms": V86_EXECUTION_TOTAL_MS,
    }


def v86_diagnostics():
    return {
        "version": V86_VERSION,
        "execution": v84_timing_contract(),
        "guard": {
            "strict_ms": V84_PERFECT_GUARD_STRICT_MS,
            "standard_ms": V84_PERFECT_GUARD_STANDARD_MS,
            "riposte_ms": V84_RIPOSTE_WINDOW_MS,
            "instant_key_intent": True,
            "rear_and_non_melee_filters_preserved": True,
        },
        "death": {
            "active": bool(v86_death_state.active),
            "kind": str(v86_death_state.death_kind),
            "killer_front_wait_ms": V86_DEATH_FRONT_WAIT_MS,
            "crawler_hits": V86_CRAWLER_HIT_COUNT,
            "berserker_hits": V86_BERSERKER_HIT_COUNT,
            "solid_ground_plane_pieces": True,
            "fracture_seams": False,
            "bomb_directional_cones": 3,
            "bomb_pieces_burn": True,
            "v74_persistent_blood": True,
            "title_delay_ms": V79_DEATH_TITLE_DELAY_MS,
            "title_fade_ms": V79_DEATH_TITLE_FADE_MS,
            "menu_fade_ms": V79_DEATH_MENU_FADE_MS,
        },
    }
# </POTBO_STAGE S1941>

# <POTBO_STAGE S1944>


# =========================================================
# END V86
# =========================================================


# =========================================================
# V87 - SPECIAL-SLASH PARITY / PERSISTENT BLOOD / DEATH CADENCE
# =========================================================
# V87 is deliberately an authority layer rather than a second combat system.
# It reuses the existing special-move palette and blood ecology, corrects the
# Berserker's eight-way visual direction, and retimes authored death impacts so
# animation anticipation always precedes the physical cut.

V87_VERSION = "87.0"

# The old 64/78 ms loops were below readable animation cadence.  Crawler remains
# the faster predator; Berserker gets a visibly heavier anticipation/recovery.
V86_CRAWLER_HIT_STEP_MS = 158
V86_BERSERKER_HIT_STEP_MS = 230
V87_CRAWLER_IMPACT_MS = 88
V87_BERSERKER_IMPACT_MS = 143
V87_CRAWLER_RECOVERY_MS = 330
V87_BERSERKER_RECOVERY_MS = 440
# </POTBO_STAGE S1944>

# <POTBO_STAGE S1959>


def v86_face_killer_to_player(killer):
    if killer is None:
        return
    delta = pygame.Vector2(
        float(oyuncu_x) - float(killer.x),
        float(oyuncu_y) - float(killer.y),
    )
    killer.direction = v84_direction_name(delta)
    if not hasattr(killer, "visual_direction"):
        return
    if str(getattr(killer, "tur", "")) == "berserker":
        current = str(getattr(killer, "visual_direction", "down_right"))
        killer.visual_direction = _berserker_gorsel_yon_bul(delta.x, delta.y, current)
    elif abs(delta.x) > 0.5:
        killer.visual_direction = "right" if delta.x >= 0.0 else "left"
# </POTBO_STAGE S1959>

# <POTBO_STAGE S1962>


def v86_death_actor_frame(actor, now):
    state = v86_death_state
    if not state.active or actor is not state.killer:
        return None
    enemy_type = str(state.killer_type)
    attack = int(state.attack_ms)
    if enemy_type not in ("crawler", "berserker") or attack <= 0:
        return _v87_death_actor_frame_original(actor, now)

    if enemy_type == "crawler":
        count = V86_CRAWLER_HIT_COUNT
        step = V86_CRAWLER_HIT_STEP_MS
        impact = V87_CRAWLER_IMPACT_MS
        recovery = V87_CRAWLER_RECOVERY_MS
        frames = COMMON_ENEMY_SPRITELERI.get("crawler", {}).get("attack", [])
    else:
        count = V86_BERSERKER_HIT_COUNT
        step = V86_BERSERKER_HIT_STEP_MS
        impact = V87_BERSERKER_IMPACT_MS
        recovery = V87_BERSERKER_RECOVERY_MS
        directional = COMMON_ENEMY_SPRITELERI.get("berserker", {}).get("attack", {})
        visual = str(getattr(actor, "visual_direction", "down_right"))
        frames = directional.get(visual, []) if isinstance(directional, dict) else []
        if not frames and isinstance(directional, dict) and directional:
            # Defensive recovery for old saves that contain a four-way direction.
            v86_face_killer_to_player(actor)
            visual = str(getattr(actor, "visual_direction", "down_right"))
            frames = directional.get(visual, [])
        if not frames and isinstance(directional, dict):
            frames = next((items for items in directional.values() if items), [])

    end = attack + (count - 1) * step + impact + recovery
    if now < attack:
        return frames[0] if frames else _v87_death_actor_frame_original(actor, now)
    if now > end:
        return _v87_death_actor_frame_original(actor, now)
    local = max(0, int(now) - attack)
    if local >= count * step:
        # The final strike resolves into a held recovery stance.  Modulo must not
        # silently begin a phantom extra swing while the victim starts falling.
        return frames[0] if frames else _v87_death_actor_frame_original(actor, now)
    cycle = local % max(1, step)
    progress = v87_repeating_attack_progress(cycle, step, impact)
    return v86_frame_progress(frames, progress)


def v86_update_melee_death(state, now, dt):
    if state.death_kind not in ("crawler", "berserker", "tarkard", "torrmund"):
        return
    if not (state.one_shot and state.death_kind in ("tarkard", "torrmund")):
        v86_move_killer_to_front(state, now, dt)
    attack = int(state.attack_ms)
    if attack <= 0 or now < attack:
        return

    if state.death_kind == "crawler":
        state.phase = "crawler_authored_hits"
        for index in range(V86_CRAWLER_HIT_COUNT):
            impact = attack + index * V86_CRAWLER_HIT_STEP_MS + V87_CRAWLER_IMPACT_MS
            if now >= impact:
                v86_eroding_hit(state, index, berserker=False)
        last_impact = (
            attack
            + (V86_CRAWLER_HIT_COUNT - 1) * V86_CRAWLER_HIT_STEP_MS
            + V87_CRAWLER_IMPACT_MS
        )
        if now >= last_impact + V87_CRAWLER_RECOVERY_MS:
            v86_start_fall(
                state,
                last_impact + V87_CRAWLER_RECOVERY_MS,
                620,
                push=v86_impact_direction(state) * 7.0,
            )
    elif state.death_kind == "berserker":
        state.phase = "berserker_authored_hits"
        for index in range(V86_BERSERKER_HIT_COUNT):
            impact = (
                attack + index * V86_BERSERKER_HIT_STEP_MS + V87_BERSERKER_IMPACT_MS
            )
            if now >= impact:
                v86_eroding_hit(state, index, berserker=True)
        last_impact = (
            attack
            + (V86_BERSERKER_HIT_COUNT - 1) * V86_BERSERKER_HIT_STEP_MS
            + V87_BERSERKER_IMPACT_MS
        )
        if now >= last_impact + V87_BERSERKER_RECOVERY_MS:
            v86_start_fall(
                state,
                last_impact + V87_BERSERKER_RECOVERY_MS,
                560,
                push=v86_impact_direction(state) * 13.0,
            )
    elif state.death_kind == "tarkard":
        v86_tripartite_tarkard(state, now)
    elif state.death_kind == "torrmund":
        if state.one_shot:
            v86_torrmund_waist_bisect(state, now)
        else:
            v86_torrmund_decap(state, now)
            if now >= attack + 1220:
                v86_torrmund_second_cleave(state, now)
# </POTBO_STAGE S1962>

# <POTBO_STAGE S1967>


def v73_ground_splatter(
    x,
    y,
    direction,
    count,
    scale_range=(0.16, 0.48),
    distance_range=(3.0, 18.0),
    cone_deg=48.0,
    backscatter=0.12,
    source="impact",
):
    source_name = str(source)
    lo, hi = float(distance_range[0]), float(distance_range[1])
    if source_name in {"lethal_ground", "lethal_followthrough"}:
        hi = min(hi, 23.0 if source_name == "lethal_ground" else 18.0)
        lo = min(lo, hi * 0.34)
    elif source_name.startswith("execution_cut"):
        hi = min(hi, 25.0 if "final" in source_name else 14.0)
        lo = min(lo, hi * 0.30)
    elif source_name == "particle_landing" and bool(
        getattr(v74_current_particle, "v87_enemy_death", False)
    ):
        hi = min(hi, 14.0)
        lo = min(lo, 3.0)
    return _v87_ground_splatter_original(
        x,
        y,
        direction,
        count,
        scale_range=scale_range,
        distance_range=(lo, hi),
        cone_deg=cone_deg,
        backscatter=backscatter,
        source=source,
    )
# </POTBO_STAGE S1967>

# <POTBO_STAGE S1980>
V87_STARTUP_OK = all(
    (
        V87_STARTUP_CONTRACT["execution_special_palette_exact"],
        V87_STARTUP_CONTRACT["crawler_hit_step_ms"] >= 150,
        V87_STARTUP_CONTRACT["berserker_hit_step_ms"] >= 220,
        V87_STARTUP_CONTRACT["berserker_eight_way_direction"],
        V87_STARTUP_CONTRACT["embedded_ground_fire_frames"] >= 8,
        V87_STARTUP_CONTRACT["enemy_death_velocity_scale"][1] <= 0.70,
    )
)
# </POTBO_STAGE S1980>

# <POTBO_STAGE S1998>


def v88_actor_pool(include_inactive=False):
    """Return unique combat actors; ordering can never decide attribution."""
    actors = []
    seen = set()
    providers = []
    if callable(globals().get("combat_enemy_aktorleri")):
        providers.append(lambda: combat_enemy_aktorleri())
    if callable(globals().get("v84_hostile_actors")):
        providers.append(lambda: v84_hostile_actors(include_suspended=include_inactive))
    for provider in providers:
        try:
            supplied = list(provider())
        except (AttributeError, NameError, TypeError, ValueError):
            continue
        for actor in supplied:
            if actor is None or id(actor) in seen:
                continue
            if not include_inactive and not bool(getattr(actor, "active", True)):
                continue
            seen.add(id(actor))
            actors.append(actor)
    return actors
# </POTBO_STAGE S1998>

# <POTBO_STAGE S2000>


def v88_source_type_hint(source_name):
    key = v88_name_key(source_name)
    if "headsthrower" in key or "headthrower" in key:
        return "headsthrower"
    if "torrmund" in key:
        return "torrmund"
    if "tarkard" in key:
        return "tarkard"
    if "berserker" in key:
        return "berserker"
    if "crawler" in key:
        return "crawler"
    return ""
# </POTBO_STAGE S2000>

# <POTBO_STAGE S2007>


# Scope every direct melee resolver.  Subclasses own distinct attack methods, so
# each one is wrapped explicitly instead of relying on class-name inference.
_v88_common_attack_update_original = CommonEnemy._saldiri_guncelle
# </POTBO_STAGE S2007>

# <POTBO_STAGE S2009>


CommonEnemy._saldiri_guncelle = _v88_common_attack_update


_v88_tarkard_attack_update_original = TarkardEnemy._saldiri_guncelle


def _v88_tarkard_attack_update(self, simdi):
    provenance = v88_make_damage_source(self, "melee", self)
    result = v88_call_with_damage_source(
        provenance,
        _v88_tarkard_attack_update_original,
        self,
        simdi,
    )
    v88_enforce_death_physics_ownership()
    return result


TarkardEnemy._saldiri_guncelle = _v88_tarkard_attack_update


_v88_torrmund_attack_update_original = SirTorrmundEnemy._saldiri_guncelle


def _v88_torrmund_attack_update(self, simdi):
    provenance = v88_make_damage_source(self, "melee", self)
    result = v88_call_with_damage_source(
        provenance,
        _v88_torrmund_attack_update_original,
        self,
        simdi,
    )
    v88_enforce_death_physics_ownership()
    return result


SirTorrmundEnemy._saldiri_guncelle = _v88_torrmund_attack_update


_v88_rock_init_original = HeadsThrowerRockProjectile.__init__
# </POTBO_STAGE S2009>

# <POTBO_STAGE S2011>


HeadsThrowerRockProjectile.__init__ = _v88_rock_init


_v88_rock_impact_original = HeadsThrowerRockProjectile._impact
# </POTBO_STAGE S2011>

# <POTBO_STAGE S2013>


HeadsThrowerRockProjectile._impact = _v88_rock_impact
# </POTBO_STAGE S2013>

# <POTBO_STAGE S2016>


def oyuncu_agir_darbe_uygula(kaynak_x, kaynak_y, kaynak_adi="Tarkard"):
    result = _v88_heavy_player_hit_original(kaynak_x, kaynak_y, kaynak_adi)
    v88_enforce_death_physics_ownership()
    return result
# </POTBO_STAGE S2016>

# <POTBO_STAGE S2018>


def oyuncu_infaz_darbesi_uygula(
    kaynak_x,
    kaynak_y,
    kaynak_adi="Sir Torrmund",
    saldiri_yonu="right",
):
    result = _v88_execution_player_hit_original(
        kaynak_x,
        kaynak_y,
        kaynak_adi,
        saldiri_yonu,
    )
    v88_enforce_death_physics_ownership()
    return result
# </POTBO_STAGE S2018>

# <POTBO_STAGE S2023>


# ---------------------------------------------------------
# Readable post-mortem cadence with no frame-hitch catch-up
# ---------------------------------------------------------
# Previous values (158/230 ms) could show 4-6 contacts per second.  These cycles
# preserve Crawler as the faster predator while giving every strike a readable
# anticipation, contact and recovery.  More importantly, one update may author at
# most one hit: a slow frame can delay choreography but can never dump several cuts
# into the same rendered frame.

V86_CRAWLER_HIT_STEP_MS = 430
V86_BERSERKER_HIT_STEP_MS = 620
V87_CRAWLER_IMPACT_MS = 215
V87_BERSERKER_IMPACT_MS = 340
V87_CRAWLER_RECOVERY_MS = 640
V87_BERSERKER_RECOVERY_MS = 780


def v88_repeating_death_spec(kind):
    if str(kind) == "crawler":
        return {
            "count": V86_CRAWLER_HIT_COUNT,
            "step_ms": V86_CRAWLER_HIT_STEP_MS,
            "impact_ms": V87_CRAWLER_IMPACT_MS,
            "final_recovery_ms": V87_CRAWLER_RECOVERY_MS,
            "fall_ms": 720,
            "push": 7.0,
            "berserker": False,
        }
    return {
        "count": V86_BERSERKER_HIT_COUNT,
        "step_ms": V86_BERSERKER_HIT_STEP_MS,
        "impact_ms": V87_BERSERKER_IMPACT_MS,
        "final_recovery_ms": V87_BERSERKER_RECOVERY_MS,
        "fall_ms": 680,
        "push": 13.0,
        "berserker": True,
    }
# </POTBO_STAGE S2023>

# <POTBO_STAGE S2026>


def v86_update_melee_death(state, now, dt):
    kind = str(state.death_kind)
    if kind not in ("crawler", "berserker"):
        return _v88_melee_death_update_original(state, now, dt)

    v86_move_killer_to_front(state, now, dt)
    attack = int(state.attack_ms)
    if attack <= 0 or int(now) < attack:
        return

    spec = v88_repeating_death_spec(kind)
    v88_repeating_death_scheduler_ready(state, attack, kind)
    hits_this_update = 0
    if int(state.v88_hits_done) < int(spec["count"]) and int(now) >= int(
        state.v88_next_hit_ms
    ):
        index = int(state.v88_hits_done)
        v86_eroding_hit(
            state,
            index,
            berserker=bool(spec["berserker"]),
        )
        state.v88_hits_done = index + 1
        state.v88_last_hit_ms = int(now)
        hits_this_update = 1
        if state.v88_hits_done < int(spec["count"]):
            state.v88_next_hit_ms = int(now) + int(spec["step_ms"])
        else:
            state.v88_next_hit_ms = 0
            state.v88_scheduler_complete_ms = int(now) + int(spec["final_recovery_ms"])
    state.v88_max_hits_in_one_update = max(
        int(getattr(state, "v88_max_hits_in_one_update", 0)),
        hits_this_update,
    )
    state.phase = f"{kind}_readable_hit_{int(state.v88_hits_done):02d}"

    if (
        int(state.v88_hits_done) >= int(spec["count"])
        and int(state.v88_scheduler_complete_ms) > 0
        and int(now) >= int(state.v88_scheduler_complete_ms)
    ):
        v86_start_fall(
            state,
            int(state.v88_scheduler_complete_ms),
            int(spec["fall_ms"]),
            push=v86_impact_direction(state) * float(spec["push"]),
        )
# </POTBO_STAGE S2026>

# <POTBO_STAGE S2028>


def v88_repeating_actor_frames(actor, kind):
    if kind == "crawler":
        return COMMON_ENEMY_SPRITELERI.get("crawler", {}).get("attack", [])
    directional = COMMON_ENEMY_SPRITELERI.get("berserker", {}).get("attack", {})
    if not isinstance(directional, dict):
        return []
    visual = str(getattr(actor, "visual_direction", "down_right"))
    frames = directional.get(visual, [])
    if not frames:
        v86_face_killer_to_player(actor)
        visual = str(getattr(actor, "visual_direction", "down_right"))
        frames = directional.get(visual, [])
    if not frames:
        frames = next((items for items in directional.values() if items), [])
    return frames


def v86_death_actor_frame(actor, now):
    state = v86_death_state
    kind = str(getattr(state, "death_kind", ""))
    if (
        not state.active
        or actor is not state.killer
        or kind not in ("crawler", "berserker")
    ):
        return _v88_death_actor_frame_original(actor, now)

    attack = int(state.attack_ms)
    if attack <= 0:
        return _v88_death_actor_frame_original(actor, now)
    frames = v88_repeating_actor_frames(actor, kind)
    if not frames:
        return _v88_death_actor_frame_original(actor, now)

    spec = v88_repeating_death_spec(kind)
    v88_repeating_death_scheduler_ready(state, attack, kind)
    hits_done = int(getattr(state, "v88_hits_done", 0))
    impact_ms = int(spec["impact_ms"])
    step_ms = int(spec["step_ms"])
    last_hit = int(getattr(state, "v88_last_hit_ms", 0))
    next_hit = int(getattr(state, "v88_next_hit_ms", 0))

    if hits_done <= 0:
        cycle_start = attack
    elif hits_done >= int(spec["count"]):
        cycle_start = last_hit - impact_ms
    else:
        previous_start = last_hit - impact_ms
        next_start = next_hit - impact_ms
        cycle_start = next_start if int(now) >= next_start else previous_start

    if int(now) < cycle_start:
        return frames[0]
    local = int(now) - cycle_start
    if local > step_ms:
        return frames[-1]
    progress = v87_repeating_attack_progress(local, step_ms, impact_ms)
    return v86_frame_progress(frames, progress)
# </POTBO_STAGE S2028>

# <POTBO_STAGE S2052>


def v88_attribution_diagnostics():
    event = v88_lethal_event
    return {
        "mode": "immutable_source_identity",
        "nearest_enemy_fallback": False,
        "projectile_owner_uid": True,
        "one_lethal_owner": True,
        "active_event": (
            {
                "event_id": int(event.event_id),
                "provenance_id": int(event.provenance_id),
                "attacker_uid": str(event.attacker_uid),
                "attacker_type": str(event.attacker_type),
                "source_kind": str(event.source_kind),
                "source_name": str(event.source_name),
            }
            if event is not None
            else None
        ),
        "recent": list(v88_recent_damage_events[-8:]),
        "stats": dict(v88_attribution_stats),
    }


def v88_death_diagnostics():
    state = v86_death_state
    return {
        "active": bool(state.active),
        "kind": str(state.death_kind),
        "impact_linked": bool(getattr(state, "v88_impact_linked", False)),
        "source_kind": str(getattr(state, "v88_source_kind", "")),
        "crawler_hit_step_ms": V86_CRAWLER_HIT_STEP_MS,
        "crawler_impact_ms": V87_CRAWLER_IMPACT_MS,
        "berserker_hit_step_ms": V86_BERSERKER_HIT_STEP_MS,
        "berserker_impact_ms": V87_BERSERKER_IMPACT_MS,
        "max_hits_per_update": 1,
        "runtime_max_hits_in_one_update": int(
            getattr(state, "v88_max_hits_in_one_update", 0)
        ),
        "torrmund_lethal_impact_replayed": False,
        "tarkard_lethal_impact_replayed": False,
        "combat_knockback_after_death": False,
        "title_delay_ms": V79_DEATH_TITLE_DELAY_MS,
        "title_fade_ms": V79_DEATH_TITLE_FADE_MS,
        "menu_fade_ms": V79_DEATH_MENU_FADE_MS,
    }
# </POTBO_STAGE S2052>

# <POTBO_STAGE S2079>
AMBIENT_RAT_MAX = 3
# </POTBO_STAGE S2079>

# <POTBO_STAGE S2172>


def v90_hostiles():
    if callable(globals().get("v84_hostile_actors")):
        return [
            actor
            for actor in v84_hostile_actors(include_suspended=False)
            if v90_actor_alive(actor)
        ]
    actors = [
        actor
        for actor in common_enemies
        if v90_actor_alive(actor)
    ]
    for actor in (tarkard_actor, torrmund_actor):
        if v90_actor_alive(actor):
            actors.append(actor)
    return actors
# </POTBO_STAGE S2172>

# <POTBO_STAGE S2179>


CommonEnemy.hasar_al = _v90_enemy_damage
# </POTBO_STAGE S2179>

# <POTBO_STAGE S2244>
COMMON_ENEMY_PATH_BUDGET_PER_FRAME = min(
    COMMON_ENEMY_PATH_BUDGET_PER_FRAME, 270
)
COMMON_ENEMY_PATH_BUDGET_PER_ENEMY.update(
    {
        "crawler": 68,
        "berserker": 82,
        "headsthrower": 78,
        "tarkard": 88,
        "torrmund": 92,
    }
)
# </POTBO_STAGE S2244>

# <POTBO_STAGE S2293>


_v92_enemy_update_raw = CommonEnemy.guncelle


def _v92_enemy_update(self, dt, simdi, digerler, oyuncu_hiz_vektoru):
    if getattr(self, "v92_passive", False):
        self.aggro = False
        self.attacking = False
        self.vx = 0.0
        self.vy = 0.0
        if hasattr(self, "attack_connected"):
            self.attack_connected = True
        if hasattr(self, "attack_damage_applied"):
            self.attack_damage_applied = True
        try:
            self._hp_bar_guncelle(dt, simdi)
        except Exception:
            pass
        return None
    return _v92_enemy_update_raw(self, dt, simdi, digerler, oyuncu_hiz_vektoru)


CommonEnemy.guncelle = _v92_enemy_update
# </POTBO_STAGE S2293>

# <POTBO_STAGE S2295>


def gelistirici_test_girdisi_uygula(olay):
    global oyuncu_altin
    if olay.type != pygame.KEYDOWN:
        return _v92_dev_raw(olay)
    # Quote and every legacy developer overlay key are intentionally swallowed.
    if olay.key == pygame.K_QUOTE:
        return True
    ctrl = bool(olay.mod & pygame.KMOD_CTRL)
    if ctrl:
        if olay.key == pygame.K_1:
            return v92_test_fire_cast()
        if olay.key == pygame.K_2:
            return v92_test_draco_cast()
        if olay.key == pygame.K_i:
            oyuncu_altin += 1000
            bildirim_goster(bt("+1000 coin", "+1000 coin"), V91_UI_GOLD)
            return True
        if olay.key == pygame.K_u:
            oyuncu_level_ayarla(min(MAKSIMUM_LEVEL, oyuncu_level + 1), bildirim=True)
            return True
        if olay.key == pygame.K_o:
            return v92_spawn_passive_headsthrowers()
        # Do not pass any Ctrl chord to the historical developer chain.
        return False
    return _v92_dev_raw(olay)
# </POTBO_STAGE S2295>

# <POTBO_STAGE S2327>


_v92_common_update_raw = common_enemy_guncelle


def common_enemy_guncelle():
    result = _v92_common_update_raw()
    v92_chain_update(pygame.time.get_ticks())
    return result
# </POTBO_STAGE S2327>

# <POTBO_STAGE S2405>


# Enemy navigation/steering must also regard Reinald as solid.
_v97_common_enemy_static_raw = common_enemy_statik_konum_gecerli_mi
# </POTBO_STAGE S2405>

# <POTBO_STAGE S2407>


_v97_common_enemy_fast_raw = _common_enemy_hizli_statik_gecerli_mi
# </POTBO_STAGE S2407>

# <POTBO_STAGE S2409>


_v97_melee_los_raw = common_enemy_saldiri_los_acik_mi
# </POTBO_STAGE S2409>

# <POTBO_STAGE S2413>


# Clear navigation caches once so any cells cached before V97 are rebuilt with
# Reinald's body included.
try:
    _common_enemy_nav_gecerlilik_cache.clear()
except Exception:
    pass
try:
    _common_enemy_nav_clearance_cache.clear()
except Exception:
    pass
# </POTBO_STAGE S2413>

# <POTBO_STAGE S2469>


# ---------------------------------------------------------
# CINEMATIC CLOCK: gameplay simulation pauses during execution scenes, but the
# authored execution timeline keeps advancing independently. This removes the
# Catena freeze caused by tying its update to common_enemy_guncelle().
# ---------------------------------------------------------
_v100_cinematic_lock_base = oyun_sinematik_kilitli_mi
# </POTBO_STAGE S2469>

