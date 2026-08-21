






# <POTBO_STAGE S0007>


KAMERA_YAKINLASTIRMA = 1.12
# </POTBO_STAGE S0007>

# <POTBO_STAGE S0026>

HARITA_YOLU = os.path.join(ASSETS, "maps", "map_01_grasslands.png")
# </POTBO_STAGE S0026>

# <POTBO_STAGE S0095>

HARITA = "harita"
# </POTBO_STAGE S0095>

# <POTBO_STAGE S0097>
oyun_alt_durumu = HARITA
# </POTBO_STAGE S0097>

# <POTBO_STAGE S0129>
kamera_sarsinti_bitis = 0
kamera_sarsinti_gucu = 0.0
# </POTBO_STAGE S0129>

# <POTBO_STAGE S0165>


oyuncu_x = 175.0
# </POTBO_STAGE S0165>

# <POTBO_STAGE S0168>


dunya_durumu = varsayilan_dunya_durumu()
dunya_olay_gunlugu = deque(maxlen=72)
dunya_son_guncelleme = pygame.time.get_ticks()
dunya_onceki_konum = (oyuncu_x, oyuncu_y)
dunya_son_combat_zamani = -10000
# </POTBO_STAGE S0168>

# <POTBO_STAGE S0178>

kamera_x = 0.0
kamera_y = 0.0
# </POTBO_STAGE S0178>

# <POTBO_STAGE S0211>


def ikinci_secim_bolumu():
    e = eadric_adi()

    secenek_1 = ortak_ganimet_ipucu()

    secenek_2 = [
        satir(
            e,
            bt(
                "Hayır. Hayır işleyenlerin mezarı sığ olur.",
                "No. The graves of the charitable are shallow.",
            ),
        ),
        satir(
            karakter_konusmaci(),
            bt(
                "Öyleyse neden hâlâ konuşuyorsun?",
                "Then why are you still speaking?",
            ),
        ),
        satir(
            e,
            bt(
                "Çünkü susarsam taşlar konuşuyor.",
                "Because when I fall silent, the stones speak.",
            ),
        ),
        satir(
            karakter_konusmaci(),
            bt("Ne söylüyorlar?", "What do they say?"),
        ),
    ] + ortak_ganimet_ipucu()

    secenek_3 = [
        satir(
            e,
            bt(
                "Kuzgunlar akıl yemez. Göz yerler. Hatıralar içeride kalsın diye.",
                "Ravens do not eat minds. They eat eyes, so memories remain inside.",
            ),
        ),
        satir(karakter_konusmaci(), "…"),
    ] + ortak_ganimet_ipucu()

    return secim(
        [
            (
                bt(
                    "Bu taşlık ne saklar?",
                    "What do these rocks conceal?",
                ),
                secenek_1,
            ),
            (
                bt(
                    "Yolcuya bir hayrın dokunacak mı?",
                    "Will you do a traveler any good?",
                ),
                secenek_2,
            ),
            (
                bt(
                    "Aklını kuzgunlara mı yedirdin?",
                    "Did you feed your mind to the ravens?",
                ),
                secenek_3,
            ),
        ]
    )
# </POTBO_STAGE S0211>

# <POTBO_STAGE S0225>

cave1_haritasi = resim_yukle(HARITA_YOLU, None, False, True)

if cave1_haritasi is not None:
    HARITA_GENISLIK = cave1_haritasi.get_width()
    HARITA_YUKSEKLIK = cave1_haritasi.get_height()
else:
    HARITA_GENISLIK = GENISLIK
    HARITA_YUKSEKLIK = YUKSEKLIK

if cave1_haritasi is not None:
    harita_yakin_resmi = pygame.transform.scale(
        cave1_haritasi,
        (
            max(
                1,
                int(round(HARITA_GENISLIK * KAMERA_YAKINLASTIRMA)),
            ),
            max(
                1,
                int(round(HARITA_YUKSEKLIK * KAMERA_YAKINLASTIRMA)),
            ),
        ),
    )
else:
    harita_yakin_resmi = None
# </POTBO_STAGE S0225>

# <POTBO_STAGE S0288>

if npc_resmi_temiz is not None:
    npc_resmi = pygame.transform.scale(
        npc_resmi_temiz,
        (
            int(round(76 * KAMERA_YAKINLASTIRMA)),
            int(round(90 * KAMERA_YAKINLASTIRMA)),
        ),
    )
else:
    npc_resmi = None
# </POTBO_STAGE S0288>

# <POTBO_STAGE S0311>


def dunya_durumunu_sifirla():
    global dunya_durumu, dunya_olay_gunlugu
    global dunya_son_guncelleme, dunya_onceki_konum, dunya_son_combat_zamani
    dunya_durumu = varsayilan_dunya_durumu()
    dunya_olay_gunlugu = deque(maxlen=72)
    dunya_son_guncelleme = pygame.time.get_ticks()
    dunya_onceki_konum = (oyuncu_x, oyuncu_y)
    dunya_son_combat_zamani = -10000
# </POTBO_STAGE S0311>

# <POTBO_STAGE S0313>


def dunya_simulasyon_guncelle():
    """Aktif harita zamanını, yolculuğu ve tehdit basıncını normalize eder."""
    global dunya_son_guncelleme, dunya_onceki_konum

    simdi = pygame.time.get_ticks()
    dt = max(0.0, min(0.1, (simdi - dunya_son_guncelleme) / 1000.0))
    dunya_son_guncelleme = simdi

    aktif = (
        oyun_durumu == OYUN
        and oyun_alt_durumu == HARITA
        and not oyun_sinematik_kilitli_mi()
    )
    if not aktif:
        dunya_onceki_konum = (oyuncu_x, oyuncu_y)
        return

    dunya_durumu["elapsed_ms"] = int(dunya_durumu.get("elapsed_ms", 0)) + int(dt * 1000)

    onceki_x, onceki_y = dunya_onceki_konum
    mesafe = math.hypot(oyuncu_x - onceki_x, oyuncu_y - onceki_y)

    if mesafe <= 28.0:
        dunya_durumu["distance_travelled"] = round(
            float(dunya_durumu.get("distance_travelled", 0.0)) + mesafe,
            2,
        )
    dunya_onceki_konum = (oyuncu_x, oyuncu_y)

    hp_oran = max(
        0.0,
        min(1.0, oyuncu_hp / max(1.0, float(oyuncu_max_hp))),
    )
    stamina_oran = max(
        0.0,
        min(
            1.0,
            oyuncu_stamina / max(1.0, float(oyuncu_max_stamina)),
        ),
    )

    dusman_baskisi = 0.0
    taktik_aktorler = list(common_enemies)
    if tarkard_actor is not None:
        taktik_aktorler.append(tarkard_actor)
    if torrmund_actor is not None:
        taktik_aktorler.append(torrmund_actor)
    for dusman in taktik_aktorler:
        if not getattr(dusman, "active", False) or not getattr(dusman, "aggro", False):
            continue
        dusman_mesafe = math.hypot(oyuncu_x - dusman.x, oyuncu_y - dusman.y)

        yerel_baski = max(0.0, min(1.0, 1.0 - dusman_mesafe / 420.0))
        dusman_baskisi = max(dusman_baskisi, yerel_baski)

    can_baskisi = max(0.0, (0.55 - hp_oran) / 0.55)
    stamina_baskisi = max(0.0, (0.28 - stamina_oran) / 0.28) * 0.28
    yakin_savas = max(
        0.0,
        1.0 - max(0, simdi - dunya_son_combat_zamani) / 3200.0,
    )

    hedef_tehdit = max(dusman_baskisi, can_baskisi * 0.9, yakin_savas * 0.74)
    hedef_tehdit = min(1.0, hedef_tehdit + stamina_baskisi)
    dunya_durumu["threat"] = round(hedef_tehdit, 4)

    mevcut = max(0.0, min(1.0, float(dunya_durumu.get("tension", 0.0))))

    sure = 0.75 if hedef_tehdit > mevcut else 2.4
    oran = 1.0 - math.exp(-dt / max(0.001, sure))
    dunya_durumu["tension"] = round(mevcut + (hedef_tehdit - mevcut) * oran, 4)
# </POTBO_STAGE S0313>

# <POTBO_STAGE S0337>







def kamerayi_guncelle():
    global kamera_x
    global kamera_y

    gorunen_genislik = GENISLIK / KAMERA_YAKINLASTIRMA
    gorunen_yukseklik = YUKSEKLIK / KAMERA_YAKINLASTIRMA


    hedef_x = oyuncu_x - gorunen_genislik * 0.50
    hedef_y = oyuncu_y - gorunen_yukseklik * 0.58

    maksimum_x = max(0.0, HARITA_GENISLIK - gorunen_genislik)
    maksimum_y = max(0.0, HARITA_YUKSEKLIK - gorunen_yukseklik)

    kamera_x += (hedef_x - kamera_x) * 0.13
    kamera_y += (hedef_y - kamera_y) * 0.13

    kamera_x = max(0.0, min(maksimum_x, kamera_x))
    kamera_y = max(0.0, min(maksimum_y, kamera_y))

    if pygame.time.get_ticks() < kamera_sarsinti_bitis:
        kamera_x += random.uniform(-kamera_sarsinti_gucu, kamera_sarsinti_gucu)
        kamera_y += random.uniform(
            -kamera_sarsinti_gucu * 0.75,
            kamera_sarsinti_gucu * 0.75,
        )


def dunya_ekran_x(dunya_x):
    return int(round((dunya_x - kamera_x) * KAMERA_YAKINLASTIRMA))


def dunya_ekran_y(dunya_y):
    return int(round((dunya_y - kamera_y) * KAMERA_YAKINLASTIRMA))
# </POTBO_STAGE S0337>

# <POTBO_STAGE S0341>







def npc_ciz():
    npc_ekran_x = dunya_ekran_x(npc_x)
    npc_ekran_y = dunya_ekran_y(npc_y)

    karakter_zemin_golgesi_ciz(
        npc_ekran_x,
        npc_ekran_y - 1,
        42 * KAMERA_YAKINLASTIRMA,
        11 * KAMERA_YAKINLASTIRMA,
        64,
    )

    if npc_resmi is not None:
        rect = npc_resmi.get_rect(midbottom=(npc_ekran_x, npc_ekran_y))

        ekran.blit(npc_resmi, rect)
    else:
        pygame.draw.rect(
            ekran,
            YESIL,
            (npc_ekran_x - 28, npc_ekran_y - 74, 56, 74),
        )
# </POTBO_STAGE S0341>

# <POTBO_STAGE S0348>


def yeni_item_sahnesi_musait_mi():
    """New-item kartı yalnızca çıplak oyun haritası görünürken açılabilir."""
    return oyun_durumu == OYUN and oyun_alt_durumu == HARITA
# </POTBO_STAGE S0348>

# <POTBO_STAGE S0372>


def oyuncu_carpisma_rect(x, y):

    return pygame.Rect(int(round(x)) - 12, int(round(y)) - 14, 24, 14)


def npc_carpisma_rect():
    return pygame.Rect(int(round(npc_x)) - 21, int(round(npc_y)) - 22, 42, 22)
# </POTBO_STAGE S0372>

# <POTBO_STAGE S0376>


def _olcekli_nokta(x, y):
    """
    Kullanıcının işaretlediği 1671x864 referans haritasındaki
    koordinatları gerçek harita boyutuna uyarlar.
    """

    return (
        int(x * HARITA_GENISLIK / 1671),
        int(y * HARITA_YUKSEKLIK / 864),
    )
# </POTBO_STAGE S0376>

# <POTBO_STAGE S0378>


_collision_polygon_onbellegi = None
_collision_polygon_onbellek_boyutu = None


def collision_polygonlari():
    """
    Haritadaki büyük doğal engelleri ölçeklenebilir polygonlar olarak
    döndürür. Sonuç harita boyutu değişmediği sürece önbellekte tutulur.
    """
    global _collision_polygon_onbellegi
    global _collision_polygon_onbellek_boyutu

    boyut = (HARITA_GENISLIK, HARITA_YUKSEKLIK)

    if (
        _collision_polygon_onbellegi is not None
        and _collision_polygon_onbellek_boyutu == boyut
    ):
        return _collision_polygon_onbellegi

    ham_polygonlar = [

        [
            (0, 0),
            (1671, 0),
            (1671, 132),
            (1625, 129),
            (1580, 134),
            (1558, 151),
            (1518, 151),
            (1470, 140),
            (1418, 135),
            (1365, 126),
            (1296, 123),
            (1240, 136),
            (1170, 138),
            (1090, 135),
            (1030, 126),
            (960, 126),
            (880, 132),
            (810, 136),
            (745, 136),
            (690, 126),
            (610, 126),
            (520, 126),
            (420, 131),
            (330, 130),
            (245, 116),
            (180, 116),
            (90, 126),
            (0, 123),
        ],

        [
            (80, 310),
            (92, 264),
            (121, 224),
            (164, 201),
            (220, 196),
            (290, 197),
            (349, 214),
            (390, 250),
            (409, 293),
            (413, 330),
            (403, 362),
            (379, 390),
            (335, 404),
            (280, 405),
            (220, 397),
            (170, 375),
            (128, 348),
            (93, 323),
        ],

        [
            (752, 274),
            (768, 257),
            (800, 252),
            (824, 232),
            (850, 205),
            (886, 203),
            (907, 209),
            (915, 224),
            (902, 242),
            (926, 242),
            (946, 229),
            (966, 231),
            (965, 247),
            (981, 243),
            (991, 250),
            (979, 260),
            (995, 266),
            (987, 280),
            (1009, 279),
            (1026, 294),
            (1047, 293),
            (1051, 321),
            (1037, 348),
            (1026, 365),
            (1012, 378),
            (992, 373),
            (974, 355),
            (959, 337),
            (945, 321),
            (928, 306),
            (912, 301),
            (893, 306),
            (874, 306),
            (858, 299),
            (842, 291),
            (821, 286),
            (800, 287),
            (778, 293),
            (759, 289),
        ],

        [
            (1362, 468),
            (1368, 427),
            (1392, 397),
            (1430, 385),
            (1472, 387),
            (1510, 403),
            (1532, 431),
            (1545, 460),
            (1562, 474),
            (1593, 477),
            (1599, 492),
            (1585, 504),
            (1550, 507),
            (1530, 531),
            (1490, 540),
            (1445, 536),
            (1408, 524),
            (1380, 502),
        ],

        [
            (0, 666),
            (65, 668),
            (150, 655),
            (220, 658),
            (300, 640),
            (390, 648),
            (470, 650),
            (540, 646),
            (620, 646),
            (700, 641),
            (780, 645),
            (860, 646),
            (940, 650),
            (1010, 659),
            (1080, 668),
            (1160, 664),
            (1230, 650),
            (1320, 646),
            (1400, 652),
            (1490, 650),
            (1570, 651),
            (1635, 646),
            (1671, 640),
            (1671, 864),
            (0, 864),
        ],
    ]

    _collision_polygon_onbellegi = [
        _olcekli_polygon(noktalar) for noktalar in ham_polygonlar
    ]
    _collision_polygon_onbellek_boyutu = boyut

    return _collision_polygon_onbellegi
# </POTBO_STAGE S0378>

# <POTBO_STAGE S0380>


def harita_pikseli_engel_mi(x, y):
    """
    Collision yalnızca kullanıcı tarafından maviyle işaretlenen alanlarda çalışır.
    """

    nokta = (int(x), int(y))

    for polygon in collision_polygonlari():
        if nokta_polygon_icinde_mi(nokta, polygon):
            return True

    return False
# </POTBO_STAGE S0380>

# <POTBO_STAGE S0406>







































def darbe_profili_belirle(kaynak=None, hedef_turu=""):
    """Darbeyi kan/gore yoğunluğuna çevirir; ağır bayıltıcı ve kesici ayrıdır.

    Yeni düşmanlar `damage_profile="heavy_slash"` veya cfg içindeki aynı alanla
    ağır kesici sınıfına katılabilir. Böylece Torrmund'a özel hard-code kopyalamak gerekmez.
    """
    ozel_profil = str(getattr(kaynak, "damage_profile", "") or "").lower()
    if (
        not ozel_profil
        and hasattr(kaynak, "cfg")
        and isinstance(getattr(kaynak, "cfg", None), dict)
    ):
        ozel_profil = str(kaynak.cfg.get("damage_profile", "") or "").lower()
    if ozel_profil in {
        "burn",
        "light_slash",
        "slash",
        "medium_blunt",
        "medium_slash",
        "magic_heavy",
        "heavy_blunt",
        "heavy_slash",
    }:
        return ozel_profil
    tur = str(getattr(kaynak, "tur", kaynak or "")).lower()
    if tur == "tarkard":
        return "heavy_blunt"
    if tur == "torrmund":
        return "heavy_slash"
    if tur == "berserker":
        return "medium_slash"
    if tur == "headsthrower":
        return "medium_blunt"
    if tur == "crawler":
        return "light_slash"
    if tur in ("fire_magic", "fire_magic_explosion"):
        return "magic_heavy"
    if tur in ("fire_magic_burn", "burn"):
        return "burn"
    if tur in ("player", "none", ""):
        if karakter_cinsiyet == "male" and oyuncu_saldiri_modu == "hold_release":
            return "heavy_slash"
        return "slash"
    return "slash"
# </POTBO_STAGE S0406>

# <POTBO_STAGE S0427>


def oyuncu_savas_hurtbox_rect(x=None, y=None):
    """Fizik collision'ından ayrı savaş hurtbox'ı.

    Oyuncunun hareket collision'ı yalnız ayaklarda kalır; bunu büyütmek harita
    dolaşımını bozardı. Savaşta ise gövde/kollar da hedef olmalıdır. Bu nedenle
    melee temasları için ayaklardan omuza uzanan dar bir hurtbox kullanılır.
    """
    if x is None:
        x = oyuncu_x
    if y is None:
        y = oyuncu_y



    return pygame.Rect(int(round(x)) - 17, int(round(y)) - 48, 34, 44)
# </POTBO_STAGE S0427>

# <POTBO_STAGE S0437>


def _rect_polygon_cakisiyor_mu(rect, polygon):
    """
    Collision polygonunu yalnız birkaç sample point ile değil gerçek body rect ile
    sınar. Böylece A* 'merkez geçiyor ama omuz kayaya giriyor' rotası üretmez.
    """
    if not polygon:
        return False

    sol, sag = rect.left, rect.right
    ust, alt = rect.top, rect.bottom
    rect_koseler = (
        (sol, ust),
        (sag, ust),
        (sag, alt),
        (sol, alt),
    )

    for p in rect_koseler:
        if nokta_polygon_icinde_mi(p, polygon):
            return True

    for px, py in polygon:
        if sol <= px <= sag and ust <= py <= alt:
            return True

    rect_kenarlar = (
        (rect_koseler[0], rect_koseler[1]),
        (rect_koseler[1], rect_koseler[2]),
        (rect_koseler[2], rect_koseler[3]),
        (rect_koseler[3], rect_koseler[0]),
    )
    onceki = polygon[-1]
    for mevcut in polygon:
        for a, b in rect_kenarlar:
            if _segmentler_kesisiyor_mu(a, b, onceki, mevcut):
                return True
        onceki = mevcut
    return False
# </POTBO_STAGE S0437>

# <POTBO_STAGE S0442>


class RockImpact:
    def __init__(self, x, y, simdi):
        self.x = float(x)
        self.y = float(y)
        self.started_ms = int(simdi)
        rng = random.Random(int(x * 31 + y * 17 + simdi))
        self.debris = []
        for _ in range(7):
            a = rng.random() * math.tau
            speed = rng.uniform(12.0, 34.0)
            self.debris.append(
                (
                    math.cos(a) * speed,
                    math.sin(a) * speed * 0.48,
                    rng.uniform(1.0, 2.6),
                )
            )

    def alive(self, simdi):
        return int(simdi) - self.started_ms < 330

    def ciz(self, simdi):
        age = max(
            0.0,
            min(1.0, (int(simdi) - self.started_ms) / 330.0),
        )
        alpha = int(150 * (1.0 - age))
        if alpha <= 0:
            return
        sx = dunya_ekran_x(self.x)
        sy = dunya_ekran_y(self.y)
        for vx, vy, size in self.debris:
            t = age * 0.34
            px = sx + vx * t * KAMERA_YAKINLASTIRMA
            py = sy + vy * t * KAMERA_YAKINLASTIRMA
            rr = max(1, int(size * KAMERA_YAKINLASTIRMA))
            surf = pygame.Surface((rr * 2 + 2, rr * 2 + 2), pygame.SRCALPHA)
            pygame.draw.circle(surf, (108, 94, 78, alpha), (rr + 1, rr + 1), rr)
            ekran.blit(surf, (int(px - rr - 1), int(py - rr - 1)))
# </POTBO_STAGE S0442>

# <POTBO_STAGE S0444>


class AmbientRat:
    """
    Kalıcı olmayan fakat sahnede sürekli var olması hedeflenen ambient fare.

    Önceki sürümde fare yalnız görünür bir noktadan ekran dışına koşup siliniyordu.
    V12'de gerçek bir mikro-fauna state machine'i vardır:
      roam -> investigate -> flee -> roam.

    Ağır pathfinding kullanmaz. 9 yönlü local probe + düşük frekanslı hedef seçimi
    sayesinde neredeyse bedava çalışır; collision içine girmez ve oyuncunun ayağında
    dönüp durmaz.
    """

    def __init__(self, x, y, simdi):
        self.x = float(x)
        self.y = float(y)
        self.v = pygame.Vector2(0.0, 0.0)
        self.heading = pygame.Vector2(1.0, 0.0)
        self.turn_rate_deg = random.uniform(360.0, 470.0)
        self.active = True
        self.started_ms = int(simdi)
        self.frame_seed = random.randint(0, 2000)
        self.direction = "right"
        self.wobble_seed = random.random() * math.tau
        self.speed_base = random.uniform(78.0, 103.0)
        self.speed_flee = random.uniform(145.0, 178.0)

        self.scale_factor = random.uniform(0.44, 0.72)
        self.target = pygame.Vector2(self.x, self.y)
        self.target_refresh_ms = 0
        self.stuck_ms = 0.0
        self.last_pos = pygame.Vector2(self.x, self.y)
        self.behavior = "roam"
        self.flee_until = 0
        self.food_refresh_ms = 0
        self.life_until = int(simdi) + random.randint(52000, 88000)
        self._yeni_roam_hedefi(simdi, force=True)

    def _dir_name(self, v):
        if abs(v.x) > abs(v.y) * 1.15:
            return "right" if v.x >= 0 else "left"
        return "down" if v.y >= 0 else "up"

    def _aday_gecerli(self, p):
        return (
            20.0 <= p.x <= HARITA_GENISLIK - 20.0
            and 24.0 <= p.y <= HARITA_YUKSEKLIK - 18.0
            and common_enemy_statik_konum_gecerli_mi("rat", p.x, p.y, navigation=False)
        )

    def _yeni_roam_hedefi(self, simdi, force=False):
        if not force and simdi < self.target_refresh_ms:
            return
        here = pygame.Vector2(self.x, self.y)
        rng = random.Random(
            int(self.frame_seed * 131 + simdi // 700 + self.x * 7 + self.y * 11)
        )
        adaylar = []
        for i in range(18):
            aci = rng.random() * math.tau
            mesafe = rng.uniform(80.0, 250.0)
            p = here + pygame.Vector2(math.cos(aci), math.sin(aci)) * mesafe
            if not self._aday_gecerli(p):
                continue


            los = _ince_dunya_los_acik_mi(here, p, 9.0)
            merkez_ceza = max(0.0, 70.0 - p.distance_to((oyuncu_x, oyuncu_y)))
            skor = merkez_ceza + (0.0 if los else 85.0) + rng.uniform(0.0, 22.0)
            adaylar.append((skor, p))
        if adaylar:
            adaylar.sort(key=lambda item: item[0])
            self.target = pygame.Vector2(adaylar[0][1])
        else:
            self.target = pygame.Vector2(here)
        self.target_refresh_ms = int(simdi) + rng.randint(1900, 3900)

    def _flee_hedefi(self, simdi):
        here = pygame.Vector2(self.x, self.y)
        player = pygame.Vector2(oyuncu_x, oyuncu_y)
        away = here - player
        if away.length_squared() <= 1e-6:
            away = pygame.Vector2(1.0, 0.0)
        away = away.normalize()




        side = pygame.Vector2(-away.y, away.x)
        sign = -1.0 if (self.frame_seed + simdi // 300) % 2 else 1.0
        ideal = away * 0.88 + side * 0.32 * sign
        if ideal.length_squared() > 1e-6:
            ideal = ideal.normalize()

        for angle in (
            0,
            18,
            -18,
            35,
            -35,
            58,
            -58,
            88,
            -88,
            135,
            -135,
        ):
            d = ideal.rotate(angle)
            p = here + d * 150.0
            if self._aday_gecerli(p):
                return p
        return here + away * 55.0

    def _local_direction(self, desired, dt):
        """Kısa-horizon steering; ilk geçerli yön yerine en akıcı güvenli yönü skorlar."""
        here = pygame.Vector2(self.x, self.y)
        desired = pygame.Vector2(desired)
        if desired.length_squared() <= 1e-8:
            return pygame.Vector2(0.0, 0.0)
        desired = desired.normalize()
        current = pygame.Vector2(self.heading)
        if current.length_squared() <= 1e-8:
            current = desired
        else:
            current = current.normalize()

        probe_distance = max(13.0, self.speed_flee * max(dt, 1 / 60) * 3.0)
        adaylar = []
        for angle in (
            0,
            10,
            -10,
            20,
            -20,
            34,
            -34,
            50,
            -50,
            70,
            -70,
            96,
            -96,
            128,
            -128,
            160,
            -160,
        ):
            d = desired.rotate(angle)
            probe1 = here + d * probe_distance
            probe2 = here + d * probe_distance * 1.85
            if not self._aday_gecerli(probe1):
                continue
            ileri_acik = 1.0 if self._aday_gecerli(probe2) else 0.0
            hedef_align = d.dot(desired)
            inertia = d.dot(current)


            skor = (
                hedef_align * 1.55
                + inertia * 0.82
                + ileri_acik * 0.55
                - abs(angle) / 240.0
            )
            adaylar.append((skor, d))
        if not adaylar:
            return pygame.Vector2(0.0, 0.0)
        adaylar.sort(key=lambda item: item[0], reverse=True)
        return pygame.Vector2(adaylar[0][1]).normalize()

    def _hareketi_kaydirarak_uygula(self, step):
        """Tam vektör sweep + tangent slide; x/y ayrı bounce jitter'ını kaldırır."""
        step = pygame.Vector2(step)
        uzun = step.length()
        if uzun <= 1e-7:
            return False
        parca_sayisi = max(1, int(math.ceil(uzun / 3.5)))
        sub = step / parca_sayisi
        moved_any = False
        for _ in range(parca_sayisi):
            hedef = pygame.Vector2(self.x, self.y) + sub
            if common_enemy_statik_konum_gecerli_mi(
                "rat", hedef.x, hedef.y, navigation=False
            ):
                self.x, self.y = hedef.x, hedef.y
                moved_any = True
                continue


            candidates = [
                pygame.Vector2(sub.x, 0.0),
                pygame.Vector2(0.0, sub.y),
                sub.rotate(28.0) * 0.72,
                sub.rotate(-28.0) * 0.72,
            ]
            candidates.sort(key=lambda v: v.dot(self.heading), reverse=True)
            slid = False
            for cand in candidates:
                q = pygame.Vector2(self.x, self.y) + cand
                if common_enemy_statik_konum_gecerli_mi(
                    "rat", q.x, q.y, navigation=False
                ):
                    self.x, self.y = q.x, q.y
                    moved_any = True
                    slid = True
                    break
            if not slid:
                break
        return moved_any

    def guncelle(self, dt, simdi):
        if not self.active:
            return

        here = pygame.Vector2(self.x, self.y)
        player = pygame.Vector2(oyuncu_x, oyuncu_y)
        player_dist = here.distance_to(player)

        if player_dist < 118.0:
            self.behavior = "flee"
            self.flee_until = int(simdi) + 900
            self.target = self._flee_hedefi(simdi)
            self.target_refresh_ms = int(simdi) + 420
        elif self.behavior == "flee" and simdi >= self.flee_until:
            self.behavior = "roam"
            self._yeni_roam_hedefi(simdi, force=True)
        else:


            if simdi >= self.food_refresh_ms:
                besin = kan_et_hedefi_bul(here, 560.0)
                self.food_refresh_ms = int(simdi) + random.randint(450, 700)
                if besin is not None:
                    self.behavior = "investigate"
                    self.target = besin
                    self.target_refresh_ms = int(simdi) + 760
                elif self.behavior == "investigate":
                    self.behavior = "roam"
                    self._yeni_roam_hedefi(simdi, force=True)
            if self.behavior == "roam" and (
                here.distance_to(self.target) < 20.0 or simdi >= self.target_refresh_ms
            ):
                self._yeni_roam_hedefi(simdi, force=True)

        to = self.target - here
        if to.length_squared() <= 3.0:
            self.v *= math.exp(-8.0 * dt)
            self._yeni_roam_hedefi(simdi, force=True)
            return

        desired = to.normalize()

        wobble_amp = (
            0.035
            if self.behavior == "flee"
            else (0.048 if self.behavior == "investigate" else 0.085)
        )
        wobble = (
            math.sin((simdi - self.started_ms) * 0.0047 + self.wobble_seed) * wobble_amp
        )
        desired = desired.rotate_rad(wobble)

        chosen = self._local_direction(desired, dt)
        if chosen.length_squared() <= 1e-6:
            self.stuck_ms += dt * 1000.0
            self.v *= math.exp(-8.0 * dt)
            if self.stuck_ms > 300.0:
                self._yeni_roam_hedefi(simdi, force=True)
            if self.stuck_ms > 1900.0:
                self.active = False
            return

        self.stuck_ms = max(0.0, self.stuck_ms - dt * 980.0)
        speed = self.speed_flee if self.behavior == "flee" else self.speed_base

        mesafe_hedef = here.distance_to(self.target)
        arrival = (
            max(0.42, min(1.0, mesafe_hedef / 34.0)) if self.behavior != "flee" else 1.0
        )
        speed *= arrival


        current_angle = math.degrees(math.atan2(self.heading.y, self.heading.x))
        target_angle = math.degrees(math.atan2(chosen.y, chosen.x))
        delta = (target_angle - current_angle + 180.0) % 360.0 - 180.0
        max_turn = self.turn_rate_deg * max(0.0, dt)
        delta = max(-max_turn, min(max_turn, delta))
        self.heading = self.heading.rotate(delta)
        if self.heading.length_squared() > 1e-8:
            self.heading = self.heading.normalize()
        else:
            self.heading = chosen

        target_v = self.heading * speed
        response = 1.0 - math.exp(-(10.5 if self.behavior == "flee" else 8.6) * dt)
        self.v += (target_v - self.v) * response
        self.v = _vektor_uzunluk_sinirla(self.v, speed * 1.03)

        moved = self._hareketi_kaydirarak_uygula(self.v * dt)
        if not moved:
            self.stuck_ms += dt * 1000.0
            self.v *= 0.45
            self.heading = self.heading.rotate(
                38.0 if (self.frame_seed + int(simdi / 180)) % 2 else -38.0
            )

        if self.v.length_squared() > 4.0:
            self.direction = self._dir_name(self.v)



        sx = dunya_ekran_x(self.x)
        sy = dunya_ekran_y(self.y)
        outside = sx < -80 or sx > GENISLIK + 80 or sy < -80 or sy > YUKSEKLIK + 80
        if simdi >= self.life_until and outside:
            self.active = False

    def ciz(self):
        if not self.active:
            return


        kaynak_yon = "right" if self.direction in ("left", "right") else self.direction
        frames = RAT_SPRITELERI.get(kaynak_yon) or RAT_SPRITELERI.get("right", [])
        if not frames:
            return

        simdi = pygame.time.get_ticks()
        speed_ratio = min(
            1.6,
            max(
                0.55,
                self.v.length() / max(1.0, self.speed_base),
            ),
        )
        frame_ms = max(32, int(55 / math.sqrt(speed_ratio)))
        idx = ((simdi + self.frame_seed) // frame_ms) % len(frames)
        frame = frames[idx]

        factor = self.scale_factor * KAMERA_YAKINLASTIRMA
        size = (
            max(1, int(frame.get_width() * factor)),
            max(1, int(frame.get_height() * factor)),
        )
        flip_x = self.direction == "left"
        key = (
            "ambient_rat_v15",
            id(frame),
            size,
            kaynak_yon,
            flip_x,
        )
        img = sprite_olcek_onbellegi.get(key)
        if img is None:
            img = pygame.transform.scale(frame, size)
            if flip_x:
                img = pygame.transform.flip(img, True, False)
            sprite_olcek_onbellegi[key] = img

        sx = dunya_ekran_x(self.x)
        sy = dunya_ekran_y(self.y)
        sh = pygame.Surface(
            (
                max(6, int(13 * KAMERA_YAKINLASTIRMA)),
                max(3, int(4 * KAMERA_YAKINLASTIRMA)),
            ),
            pygame.SRCALPHA,
        )
        pygame.draw.ellipse(sh, (0, 0, 0, 48), sh.get_rect())
        ekran.blit(
            sh,
            (
                int(sx - sh.get_width() / 2),
                int(sy - sh.get_height() / 2),
            ),
        )
        rect = img.get_rect(midbottom=(int(sx), int(sy + 1)))
        ekran.blit(img, rect)
# </POTBO_STAGE S0444>

# <POTBO_STAGE S0452>


def _ince_dunya_los_acik_mi(a, b, adim=6.0):
    """
    Patlama/ateş görüş hattı için gövde-genişliğinde nav testi değil, ince world ray.

    Bu ayrım önemlidir: pathfinding clearance'ı combat LOS olarak kullanılırsa kaya
    kenarında görsel olarak açık olan patlama yanlışlıkla engellenir. Ray, yalnız
    gerçek solid pikseli örnekler.
    """
    a = pygame.Vector2(a)
    b = pygame.Vector2(b)
    fark = b - a
    mesafe = fark.length()
    if mesafe <= 1.0:
        return True
    yon = fark / mesafe
    t = min(float(adim), mesafe)
    while t < mesafe:
        p = a + yon * t
        if harita_pikseli_engel_mi(p.x, p.y):
            return False
        t += float(adim)
    return True
# </POTBO_STAGE S0452>

# <POTBO_STAGE S0455>


def _fire_ground_spawn_noktalari(x, y, adet, radius):
    """
    Golden-angle + jitter disk sampling.

    O(N²) Poisson benzeri minimum mesafe kontrolü kullanır. V29'da 24-38 patch
    üretildiği için minimum aralık küçültüldü; yine de aynı pikselde üst üste dev
    alev yığını oluşmaz. Collision içindeki ve duvar arkasındaki noktalar reddedilir.
    """
    merkez = pygame.Vector2(float(x), float(y))
    accepted = []
    seed = int(x * 41.0 + y * 73.0 + pygame.time.get_ticks())
    rng = random.Random(seed)
    golden = math.radians(137.507764)

    deneme = max(18, int(adet) * 6)
    for i in range(deneme):
        if len(accepted) >= int(adet):
            break

        rr = float(radius) * math.sqrt((i + 0.6) / float(deneme + 0.6))
        rr *= rng.uniform(0.62, 1.0)
        aci = i * golden + rng.uniform(-0.16, 0.16)
        p = merkez + pygame.Vector2(math.cos(aci), math.sin(aci) * 0.72) * rr

        if (
            p.x < 18
            or p.y < 22
            or p.x > HARITA_GENISLIK - 18
            or p.y > HARITA_YUKSEKLIK - 18
        ):
            continue
        if harita_pikseli_engel_mi(p.x, p.y):
            continue
        if not _ince_dunya_los_acik_mi(merkez, p, 6.0):
            continue
        if any(p.distance_to(q) < 13.5 for q in accepted):
            continue
        accepted.append(p)


    if not accepted and not harita_pikseli_engel_mi(merkez.x, merkez.y):
        accepted.append(merkez)
    return accepted
# </POTBO_STAGE S0455>

# <POTBO_STAGE S0499>


def kamera_hit_sarsintisi_baslat(guc=4.0, sure=170):
    global kamera_sarsinti_bitis, kamera_sarsinti_gucu
    if ekran_sarsintisi and not az_hareket:
        kamera_sarsinti_gucu = float(guc)
        kamera_sarsinti_bitis = pygame.time.get_ticks() + int(sure)
# </POTBO_STAGE S0499>

# <POTBO_STAGE S0503>


def combat_impact_fx_ciz():
    """
    V16 melee impact dili: normal vuruşta tek hızlı kesik, ağır vuruşta daha geniş
    çift kesik + kısa kızıl ikincil iz. Kare, yuvarlak aura veya sprite arka planı yok.
    """
    simdi = pygame.time.get_ticks()
    kalan_fx = []
    for f in combat_impact_fx:
        gecen = simdi - int(f.get("start", simdi))
        life = max(1, int(f.get("life", 180)))
        if gecen >= life:
            continue
        kalan_fx.append(f)

        tur = str(f.get("type", "slash"))
        if tur not in ("slash", "slash_heavy"):
            continue

        p = max(0.0, min(1.0, gecen / float(life)))

        alpha = int(255 * (1.0 - p) ** 1.45)
        if alpha <= 0:
            continue

        sx = dunya_ekran_x(float(f.get("x", 0.0)))
        sy = dunya_ekran_y(float(f.get("y", 0.0)))
        guc = max(0.6, min(2.8, float(f.get("power", 1.0))))
        base_angle = float(f.get("angle", 0.0)) + 32.0

        heavy = tur == "slash_heavy"
        boy = int(
            (64 if not heavy else 104)
            * min(1.35, 0.82 + guc * 0.22)
            * KAMERA_YAKINLASTIRMA
        )
        pad = max(18, boy // 2 + 18)
        surf = pygame.Surface((pad * 2, pad * 2), pygame.SRCALPHA)
        c = pygame.Vector2(pad, pad)

        if heavy:


            _kesik_cizgi_ciz(
                surf,
                c,
                base_angle - 9,
                boy,
                8,
                (118, 8, 18),
                int(alpha * 0.78),
                -3,
            )
            _kesik_cizgi_ciz(
                surf,
                c,
                base_angle - 9,
                boy,
                3,
                (252, 236, 224),
                alpha,
                -1,
            )
            _kesik_cizgi_ciz(
                surf,
                c,
                base_angle + 57,
                int(boy * 0.78),
                6,
                (172, 18, 24),
                int(alpha * 0.70),
                4,
            )
            _kesik_cizgi_ciz(
                surf,
                c,
                base_angle + 57,
                int(boy * 0.78),
                2,
                (255, 248, 238),
                int(alpha * 0.92),
                3,
            )
        else:
            _kesik_cizgi_ciz(
                surf,
                c,
                base_angle,
                boy,
                5,
                (132, 8, 18),
                int(alpha * 0.72),
                2,
            )
            _kesik_cizgi_ciz(
                surf,
                c,
                base_angle,
                boy,
                2,
                (255, 244, 236),
                alpha,
                0,
            )

        ekran.blit(surf, surf.get_rect(center=(sx, sy)))

    combat_impact_fx[:] = kalan_fx
# </POTBO_STAGE S0503>

# <POTBO_STAGE S0517>


def _v30_oyuncu_base_siluet():
    kareler = aktif_animasyon_kareleri("idle")
    if not kareler:
        return None
    src = kareler[0]
    h = int(round(66 * KAMERA_YAKINLASTIRMA))
    sc = h / max(1.0, float(src.get_height()))
    img = pygame.transform.scale(src, (max(1, int(round(src.get_width() * sc))), h))
    return (
        pygame.mask.from_surface(img)
        .to_surface(setcolor=(224, 10, 31, 255), unsetcolor=(0, 0, 0, 0))
        .convert_alpha()
    )


def _v30_yatan_siluet_yerlestir(surface, ekstra_rot=0.0, offset=(0.0, 0.0)):
    if surface is None:
        return
    gecen = max(0, pygame.time.get_ticks() - oyuncu_olum_baslangic_ms)
    p = max(0.0, min(1.0, gecen / float(OLU_CESET_YERLESME_MS)))
    ease = 1.0 - (1.0 - p) ** 3
    hedef_aci = -90.0 if oyuncu_yonu in ("right", "down") else 90.0
    draw = pygame.transform.rotate(surface, hedef_aci * ease + float(ekstra_rot))
    sx = float(dunya_ekran_x(oyuncu_x)) + float(offset[0])
    sy = float(dunya_ekran_y(oyuncu_y) - 8 + 7 * ease) + float(offset[1])
    shadow = pygame.Rect(
        0,
        0,
        max(30, draw.get_width() - 7),
        max(4, int(7 * KAMERA_YAKINLASTIRMA)),
    )
    shadow.center = (int(sx), int(sy + 12))
    pygame.draw.ellipse(ekran, (0, 0, 0), shadow)
    ekran.blit(
        draw,
        draw.get_rect(center=(int(round(sx)), int(round(sy)))),
    )
# </POTBO_STAGE S0517>

# <POTBO_STAGE S0521>


def _stage1__v30_patlama_birinci_katman_siluet_ciz():
    """Birinci shell'de de beden parçalanır; merkezden daha iri/az shard kullanır."""
    sil = _v30_oyuncu_base_siluet()
    if sil is None:
        return
    e = max(0, pygame.time.get_ticks() - oyuncu_olum_baslangic_ms)
    t = min(2.0, e / 1000.0)
    rng = random.Random(int(oyuncu_olum_patlama_seed or 1))
    sw, sh = sil.get_size()
    base = pygame.Vector2(oyuncu_olum_patlama_yonu)
    if base.length_squared() <= 1e-6:
        base = pygame.Vector2(1, 0)
    base = base.normalize()
    sx, sy = (
        float(dunya_ekran_x(oyuncu_x)),
        float(dunya_ekran_y(oyuncu_y) - 8),
    )



    cols, rows = 5, 4
    for row in range(rows):
        for col in range(cols):
            x0 = int(round(col * sw / cols))
            x1 = int(round((col + 1) * sw / cols))
            y0 = int(round(row * sh / rows))
            y1 = int(round((row + 1) * sh / rows))
            if x1 <= x0 or y1 <= y0:
                continue
            shard = sil.subsurface((x0, y0, x1 - x0, y1 - y0)).copy()
            mw, mh = shard.get_size()
            pm = pygame.Surface((mw, mh), pygame.SRCALPHA)
            jx = max(1, int(mw * 0.20))
            jy = max(1, int(mh * 0.20))
            pts = [
                (
                    rng.randint(0, min(jx, mw - 1)),
                    rng.randint(0, min(jy, mh - 1)),
                ),
                (
                    max(
                        0,
                        mw - 1 - rng.randint(0, min(jx, mw - 1)),
                    ),
                    rng.randint(0, min(jy, mh - 1)),
                ),
                (
                    max(
                        0,
                        mw - 1 - rng.randint(0, min(jx, mw - 1)),
                    ),
                    max(
                        0,
                        mh - 1 - rng.randint(0, min(jy, mh - 1)),
                    ),
                ),
                (
                    rng.randint(0, min(jx, mw - 1)),
                    max(
                        0,
                        mh - 1 - rng.randint(0, min(jy, mh - 1)),
                    ),
                ),
            ]
            pygame.draw.polygon(pm, (255, 255, 255, 255), pts)
            shard.blit(pm, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            local = pygame.Vector2(
                (x0 + x1) * 0.5 - sw * 0.5,
                (y0 + y1) * 0.5 - sh * 0.5,
            )
            d = base.rotate(rng.uniform(-62, 62))
            sp = rng.uniform(180, 380) + max(0.0, local.dot(base)) * 1.8
            px = sx + local.x + d.x * sp * t
            py = (
                sy
                + local.y
                + d.y * sp * t
                - rng.uniform(45, 125) * t
                + 0.5 * rng.uniform(210, 320) * t * t
            )
            draw = pygame.transform.rotate(shard, rng.uniform(-500, 500) * t)
            ekran.blit(draw, draw.get_rect(center=(int(px), int(py))))
# </POTBO_STAGE S0521>

# <POTBO_STAGE S0523>


def _stage1__oyuncu_yatay_siluet_ciz():
    if _v30_oyuncu_ozel_ceset_ciz():
        return
    kareler = aktif_animasyon_kareleri("idle")
    if not kareler:
        return
    src = kareler[0]
    h = int(round(66 * KAMERA_YAKINLASTIRMA))
    scale = h / max(1.0, float(src.get_height()))
    img = pygame.transform.scale(src, (max(1, int(src.get_width() * scale)), h))
    mask = pygame.mask.from_surface(img)
    sil = mask.to_surface(
        setcolor=(224, 10, 31, 255), unsetcolor=(0, 0, 0, 0)
    ).convert_alpha()

    gecen = (
        max(
            0,
            pygame.time.get_ticks() - oyuncu_olum_baslangic_ms,
        )
        if oyuncu_olum_baslangic_ms > 0
        else 560
    )

    fall_p = max(0.0, min(1.0, gecen / float(OLU_CESET_YERLESME_MS)))
    ease = 1.0 - (1.0 - fall_p) ** 3
    hedef_aci = -90.0 if oyuncu_yonu in ("right", "down") else 90.0
    sx = dunya_ekran_x(oyuncu_x)
    sy = dunya_ekran_y(oyuncu_y) - 8 + int(7 * ease)

    if oyuncu_olum_ikiye_bolundu and sil.get_height() >= 8:



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

        ust_mask = pygame.Surface((w, hh), pygame.SRCALPHA)
        alt_mask = pygame.Surface((w, hh), pygame.SRCALPHA)
        pygame.draw.polygon(
            ust_mask,
            (255, 255, 255, 255),
            [
                (0, -hh),
                (w, -hh),
                (w, int(round(sag_y))),
                (0, int(round(sol_y))),
            ],
        )
        pygame.draw.polygon(
            alt_mask,
            (255, 255, 255, 255),
            [
                (0, int(round(sol_y))),
                (w, int(round(sag_y))),
                (w, hh * 2),
                (0, hh * 2),
            ],
        )
        ust = sil.copy()
        alt = sil.copy()
        ust.blit(
            ust_mask,
            (0, 0),
            special_flags=pygame.BLEND_RGBA_MULT,
        )
        alt.blit(
            alt_mask,
            (0, 0),
            special_flags=pygame.BLEND_RGBA_MULT,
        )


        split_p = max(0.0, min(1.0, gecen / 210.0))
        split_ease = 1.0 - (1.0 - split_p) ** 3
        ana_rot = hedef_aci * ease


        ust_rot = pygame.transform.rotate(
            ust,
            ana_rot - (7.0 + abs(cut_deg) * 0.10) * split_ease,
        )
        alt_rot = pygame.transform.rotate(
            alt,
            ana_rot + (6.0 + abs(cut_deg) * 0.08) * split_ease,
        )



        normal = pygame.Vector2(-math.sin(cut_rad), math.cos(cut_rad))
        normal = normal.rotate(-ana_rot)
        if normal.length_squared() <= 1e-6:
            normal = pygame.Vector2(0.0, 1.0)
        else:
            normal = normal.normalize()
        bosluk = (4.0 + 20.0 * split_ease) * split_ease
        merkez = pygame.Vector2(sx, sy)
        ust_merkez = (
            merkez
            - normal * bosluk
            + pygame.Vector2(-2.0 * split_ease, -2.5 * split_ease)
        )
        alt_merkez = (
            merkez
            + normal * bosluk
            + pygame.Vector2(2.5 * split_ease, 3.5 * split_ease)
        )

        shadow = pygame.Rect(
            0,
            0,
            max(44, int(h * 1.10)),
            max(5, int(8 * KAMERA_YAKINLASTIRMA)),
        )
        shadow.center = (int(sx), int(sy + 13))
        pygame.draw.ellipse(ekran, (0, 0, 0), shadow)
        ekran.blit(
            ust_rot,
            ust_rot.get_rect(center=(int(ust_merkez.x), int(ust_merkez.y))),
        )
        ekran.blit(
            alt_rot,
            alt_rot.get_rect(center=(int(alt_merkez.x), int(alt_merkez.y))),
        )

        if split_p > 0.06:
            yarik = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
            alpha = int(185 * min(1.0, split_p * 1.8))

            tang = pygame.Vector2(math.cos(cut_rad), math.sin(cut_rad)).rotate(-ana_rot)
            a = merkez - tang * (8.0 + 6.0 * split_ease)
            b = merkez + tang * (8.0 + 6.0 * split_ease)
            pygame.draw.line(
                yarik,
                (232, 7, 28, alpha),
                a,
                b,
                max(2, int(3 * KAMERA_YAKINLASTIRMA)),
            )
            ekran.blit(yarik, (0, 0))
        return



    if gecen >= OLU_CESET_YERLESME_MS and oyuncu_olum_turu in (
        "blood",
        "fire",
    ):
        rng = random.Random(
            int(oyuncu_olum_koreografi_seed or oyuncu_olum_ates_seed or 31337)
        )
        body = sil.copy()
        shards = []
        parca_adet = 2 if oyuncu_olum_turu == "fire" else 3
        w0, h0 = body.get_size()
        for i in range(parca_adet):
            rw = max(3, int(w0 * rng.uniform(0.12, 0.19)))
            rh = max(3, int(h0 * rng.uniform(0.08, 0.14)))
            cx = int(w0 * rng.uniform(0.20, 0.80))
            cy = int(h0 * rng.uniform(0.28, 0.82))
            rect = pygame.Rect(cx - rw // 2, cy - rh // 2, rw, rh).clip(body.get_rect())
            if rect.width <= 1 or rect.height <= 1:
                continue
            shard = body.subsurface(rect).copy()
            pygame.draw.ellipse(body, (0, 0, 0, 0), rect)
            shards.append(
                (
                    shard,
                    rng.uniform(-1, 1),
                    rng.uniform(-1, 1),
                    rng.uniform(-18, 18),
                )
            )
        draw_body = pygame.transform.rotate(body, hedef_aci * ease)
        shadow = pygame.Rect(
            0,
            0,
            max(32, draw_body.get_width() - 8),
            max(5, int(8 * KAMERA_YAKINLASTIRMA)),
        )
        shadow.center = (int(sx), int(sy + 12))
        pygame.draw.ellipse(ekran, (0, 0, 0), shadow)
        ekran.blit(
            draw_body,
            draw_body.get_rect(center=(int(sx), int(sy))),
        )
        q = min(
            1.0,
            max(0.0, (gecen - OLU_CESET_YERLESME_MS) / 260.0),
        )
        q = 1 - (1 - q) ** 3
        for i, (sh, ox, oy, rr) in enumerate(shards):
            d = pygame.Vector2(ox, oy)
            if d.length_squared() < 0.1:
                d = pygame.Vector2(1, 0)
            d = d.normalize().rotate(-hedef_aci * ease)
            out = pygame.transform.rotate(sh, hedef_aci * ease + rr * q)
            off = d * (5.0 + 4.0 * i) * q
            ekran.blit(
                out,
                out.get_rect(center=(int(sx + off.x), int(sy + off.y))),
            )
        return



    sil = pygame.transform.rotate(sil, hedef_aci * ease)
    shadow = pygame.Rect(
        0,
        0,
        max(32, sil.get_width() - 8),
        max(5, int(8 * KAMERA_YAKINLASTIRMA)),
    )
    shadow.center = (int(sx), int(sy + 12))
    pygame.draw.ellipse(ekran, (0, 0, 0), shadow)
    ekran.blit(sil, sil.get_rect(center=(int(sx), int(sy))))
# </POTBO_STAGE S0523>

# <POTBO_STAGE S0525>


def _stage1__v26_oyuncu_patlama_siluet_parcalari_ciz():
    """Oyuncu sprite'ını runtime'da düzensiz 2x4 parçalara ayırıp blast yönünde uçurur.

    Her frame aynı seed ile aynı maskeler yeniden kurulur; bu nedenle parça sınırları
    titremez. Konum analitik balistik denklemle hesaplandığından ek fizik state'i gerekmez.
    """
    if oyuncu_olum_turu != "blast_core":
        return
    kareler = aktif_animasyon_kareleri("idle")
    if not kareler:
        return
    src = kareler[0]
    h = int(round(66 * KAMERA_YAKINLASTIRMA))
    sc = h / max(1.0, float(src.get_height()))
    img = pygame.transform.scale(src, (max(1, int(round(src.get_width() * sc))), h))
    mask = pygame.mask.from_surface(img)
    sil = mask.to_surface(
        setcolor=(224, 10, 31, 255), unsetcolor=(0, 0, 0, 0)
    ).convert_alpha()

    sw, sh = sil.get_size()
    sx = float(dunya_ekran_x(oyuncu_x))
    sy = float(dunya_ekran_y(oyuncu_y) - 8)
    t = max(
        0.0,
        min(
            2.4,
            (pygame.time.get_ticks() - oyuncu_olum_baslangic_ms) / 1000.0,
        ),
    )
    rng = random.Random(int(oyuncu_olum_patlama_seed or 7331))

    base = pygame.Vector2(oyuncu_olum_patlama_yonu)
    if base.length_squared() <= 1e-6:
        base = pygame.Vector2(1.0, 0.0)
    base = base.normalize()


    cols, rows = 6, 6
    for row in range(rows):
        for col in range(cols):
            x0 = int(round(col * sw / cols))
            x1 = int(round((col + 1) * sw / cols))
            y0 = int(round(row * sh / rows))
            y1 = int(round((row + 1) * sh / rows))
            if x1 <= x0 or y1 <= y0:
                continue
            shard = sil.subsurface((x0, y0, x1 - x0, y1 - y0)).copy()



            mw, mh = shard.get_size()
            pmask = pygame.Surface((mw, mh), pygame.SRCALPHA)
            jitter_x = max(1, int(mw * 0.24))
            jitter_y = max(1, int(mh * 0.24))
            pts = [
                (
                    rng.randint(0, min(jitter_x, mw - 1)),
                    rng.randint(0, min(jitter_y, mh - 1)),
                ),
                (
                    max(
                        0,
                        mw - 1 - rng.randint(0, min(jitter_x, mw - 1)),
                    ),
                    rng.randint(0, min(jitter_y, mh - 1)),
                ),
                (
                    max(
                        0,
                        mw - 1 - rng.randint(0, min(jitter_x, mw - 1)),
                    ),
                    max(
                        0,
                        mh - 1 - rng.randint(0, min(jitter_y, mh - 1)),
                    ),
                ),
                (
                    rng.randint(0, min(jitter_x, mw - 1)),
                    max(
                        0,
                        mh - 1 - rng.randint(0, min(jitter_y, mh - 1)),
                    ),
                ),
            ]
            pygame.draw.polygon(pmask, (255, 255, 255, 255), pts)
            shard.blit(
                pmask,
                (0, 0),
                special_flags=pygame.BLEND_RGBA_MULT,
            )

            local = pygame.Vector2(
                (x0 + x1) * 0.5 - sw * 0.5,
                (y0 + y1) * 0.5 - sh * 0.5,
            )
            spread = base.rotate(rng.uniform(-72.0, 72.0))


            hiz = rng.uniform(235.0, 510.0) + max(0.0, local.dot(base)) * 2.6
            vx = spread.x * hiz
            vy = spread.y * hiz - rng.uniform(55.0, 175.0)
            gravity = rng.uniform(220.0, 360.0)
            px = sx + local.x + vx * t
            py = sy + local.y + vy * t + 0.5 * gravity * t * t
            rot = rng.uniform(-32.0, 32.0) + rng.uniform(-760.0, 760.0) * t
            draw = pygame.transform.rotate(shard, rot)
            ekran.blit(
                draw,
                draw.get_rect(center=(int(round(px)), int(round(py)))),
            )
# </POTBO_STAGE S0525>

# <POTBO_STAGE S0536>


def oyuncu_zorlanmis_hareket_guncelle():
    """Knockback'i teleport yerine sub-step collision ile çözer."""
    global oyuncu_x, oyuncu_y, oyuncu_zorlanmis_hiz
    global oyuncu_zorlanmis_son_guncelleme, oyuncu_zorlanmis_bitis

    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA or oyuncu_hp <= 0:
        oyuncu_zorlanmis_son_guncelleme = pygame.time.get_ticks()
        oyuncu_zorlanmis_hiz.update(0.0, 0.0)
        oyuncu_zorlanmis_bitis = 0
        return

    simdi = pygame.time.get_ticks()
    dt = max(
        0.0,
        min(
            0.035,
            (simdi - oyuncu_zorlanmis_son_guncelleme) / 1000.0,
        ),
    )
    oyuncu_zorlanmis_son_guncelleme = simdi
    if dt <= 0.0:
        return
    if simdi >= oyuncu_zorlanmis_bitis or oyuncu_zorlanmis_hiz.length_squared() < 16.0:
        oyuncu_zorlanmis_hiz.update(0.0, 0.0)
        return

    hareket = oyuncu_zorlanmis_hiz * dt
    uzun = hareket.length()
    adim_sayisi = max(1, int(math.ceil(uzun / 4.0)))
    adim = hareket / adim_sayisi

    for _ in range(adim_sayisi):
        moved = False
        nx = oyuncu_x + adim.x
        ny = oyuncu_y + adim.y
        if hareket_gecerli_mi(nx, oyuncu_y):
            oyuncu_x = nx
            moved = True
        else:
            oyuncu_zorlanmis_hiz.x *= -0.08
        if hareket_gecerli_mi(oyuncu_x, ny):
            oyuncu_y = ny
            moved = True
        else:
            oyuncu_zorlanmis_hiz.y *= -0.08
        if not moved:
            oyuncu_zorlanmis_hiz *= 0.18
            break


    oyuncu_zorlanmis_hiz *= math.exp(-4.25 * dt)
# </POTBO_STAGE S0536>

# <POTBO_STAGE S0543>


def _gelistirici_x_skill_hedef_sec(yuz_yonu):
    """Hold yönündeki yaşayan düşmanlardan en doğal special-move hedefini seçer."""
    oyuncu = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    yon = pygame.Vector2(yuz_yonu)
    if yon.length_squared() <= 1e-6:
        return None
    yon = yon.normalize()
    ekran_merkezi = pygame.Vector2(GENISLIK * 0.5, YUKSEKLIK * 0.5)
    en_iyi = None
    en_iyi_skor = float("inf")
    for aktor in _gelistirici_x_skill_aktorleri():
        hedef = pygame.Vector2(float(aktor.x), float(aktor.y))
        fark = hedef - oyuncu
        mesafe = fark.length()
        if mesafe <= 1e-6 or mesafe > GELISTIRICI_X_SKILL_TETIK_MENZILI:
            continue
        ileri = fark.dot(yon)
        if ileri <= -20.0:
            continue
        yanal = abs(fark.x * yon.y - fark.y * yon.x)
        if yanal > 170.0:
            continue
        ekran_p = pygame.Vector2(dunya_ekran_x(aktor.x), dunya_ekran_y(aktor.y))
        merkez_skoru = ekran_p.distance_to(ekran_merkezi)
        skor = yanal * 1.8 + merkez_skoru * 0.30 + mesafe * 0.12
        if skor < en_iyi_skor:
            en_iyi_skor = skor
            en_iyi = aktor
    return en_iyi


def _gelistirici_x_skill_nokta(hedef, ox, oy):
    x = max(
        35.0,
        min(HARITA_GENISLIK - 35.0, float(hedef.x) + float(ox)),
    )
    y = max(
        35.0,
        min(HARITA_YUKSEKLIK - 25.0, float(hedef.y) + float(oy)),
    )
    return pygame.Vector2(x, y)
# </POTBO_STAGE S0543>

# <POTBO_STAGE S0547>


def _gelistirici_x_skill_kesik_ciz(
    katman, a, b, progress, alpha, cekirdek=(255, 242, 245)
):
    if progress <= 0.0 or alpha <= 0:
        return
    progress = _gelistirici_x_skill_ease_out(progress)
    aa = pygame.Vector2(dunya_ekran_x(a.x), dunya_ekran_y(a.y - 12.0))
    bb_full = pygame.Vector2(dunya_ekran_x(b.x), dunya_ekran_y(b.y - 12.0))
    bb = aa.lerp(bb_full, progress)
    p0 = (int(round(aa.x)), int(round(aa.y)))
    p1 = (int(round(bb.x)), int(round(bb.y)))
    pygame.draw.line(katman, (205, 16, 42, int(alpha * 0.34)), p0, p1, 12)
    pygame.draw.line(katman, (236, 32, 58, int(alpha * 0.62)), p0, p1, 6)
    pygame.draw.line(katman, (*cekirdek, alpha), p0, p1, 2)
    pygame.draw.circle(
        katman,
        (255, 245, 248, min(255, int(alpha * 0.92))),
        p1,
        4,
    )
# </POTBO_STAGE S0547>

# <POTBO_STAGE S0550>


def oyuncu_dash_guncelle(simdi=None):
    """Aktif dash'in yalnız bu frame'e düşen mesafesini collision-safe uygular."""
    global oyuncu_x, oyuncu_y, dash_aktif_bitis, dash_aktif_son_ease, dash_aktif_yonu
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if dash_aktif_yonu.length_squared() <= 0.0 or dash_aktif_bitis <= 0:
        return False
    p = max(
        0.0,
        min(
            1.0,
            (int(simdi) - dash_aktif_baslangic) / max(1.0, float(DASH_SURESI_MS)),
        ),
    )
    ease = 1.0 - (1.0 - p) ** 3
    delta_ease = max(0.0, ease - dash_aktif_son_ease)
    dash_aktif_son_ease = ease
    kalan = DASH_MESAFESI * delta_ease
    hareket = False
    yon = dash_aktif_yonu.normalize()
    while kalan > 0.0001:
        adim = min(DASH_ADIMI, kalan)
        nx = max(
            35.0,
            min(HARITA_GENISLIK - 35.0, oyuncu_x + yon.x * adim),
        )
        ny = max(
            35.0,
            min(HARITA_YUKSEKLIK - 25.0, oyuncu_y + yon.y * adim),
        )
        ilerledi = False
        if hareket_gecerli_mi(nx, oyuncu_y):
            oyuncu_x = nx
            ilerledi = True
        if hareket_gecerli_mi(oyuncu_x, ny):
            oyuncu_y = ny
            ilerledi = True
        if not ilerledi:
            dash_aktif_bitis = 0
            dash_aktif_yonu = pygame.Vector2(0.0, 0.0)
            break
        hareket = True
        kalan -= adim
    if p >= 1.0 or int(simdi) >= dash_aktif_bitis:
        dash_aktif_bitis = 0
        dash_aktif_yonu = pygame.Vector2(0.0, 0.0)
        dash_aktif_son_ease = 0.0
    return hareket
# </POTBO_STAGE S0550>

# <POTBO_STAGE S0552>


def oyuncu_serbest_hareket_guncelle():
    """İvmeli yürüyüş + temporal dash. Cooldown sırasında normal hareket daima sürer."""
    global oyuncu_x, oyuncu_y, oyuncu_yonu, oyuncu_hareket_ediyor
    global oyuncu_hareket_hiz_vektoru, oyuncu_hareket_son_guncelleme, dash_tus_kilitli
    simdi = pygame.time.get_ticks()
    dt = max(
        0.0,
        min(
            0.045,
            (simdi - oyuncu_hareket_son_guncelleme) / 1000.0,
        ),
    )
    oyuncu_hareket_son_guncelleme = simdi
    if dt <= 0.0:
        return
    if (
        oyun_durumu != OYUN
        or oyun_alt_durumu != HARITA
        or oyun_sinematik_kilitli_mi()
        or oyuncu_hp <= 0
    ):
        oyuncu_hareket_hiz_vektoru.update(0.0, 0.0)
        oyuncu_hareket_ediyor = False
        return

    if gelistirici_x_skill_guncelle(simdi):
        oyuncu_hareket_hiz_vektoru.update(0.0, 0.0)
        oyuncu_hareket_ediyor = True
        return

    tuslar = potbo_pressed_state()
    input_v = pygame.Vector2(
        int(bool(tuslar[tus_atamasi("move_right")]))
        - int(bool(tuslar[tus_atamasi("move_left")])),
        int(bool(tuslar[tus_atamasi("move_down")]))
        - int(bool(tuslar[tus_atamasi("move_up")])),
    )
    if input_v.length_squared() > 1.0:
        input_v = input_v.normalize()

    if input_v.length_squared() > 0.0:
        if abs(input_v.y) > abs(input_v.x):
            oyuncu_yonu = "down" if input_v.y > 0 else "up"
        elif input_v.x != 0:
            oyuncu_yonu = "right" if input_v.x > 0 else "left"

    dash_basili = bool(tuslar[tus_atamasi("dash")])
    if dash_basili and input_v.length_squared() > 0.0 and not dash_tus_kilitli:
        oyuncu_dash_yap(input_v.x, input_v.y)
        dash_tus_kilitli = True
    elif not dash_basili or input_v.length_squared() <= 0.0:
        dash_tus_kilitli = False

    if oyuncu_dash_aktif_mi(simdi):
        oyuncu_dash_guncelle(simdi)
        oyuncu_hareket_ediyor = True


        if input_v.length_squared() > 0.0:
            oyuncu_hareket_hiz_vektoru = input_v * (OYUNCU_YURUYUS_HIZI * 0.64)
        return

    if oyuncu_kontrol_kilitli_mi(simdi):
        oyuncu_hareket_hiz_vektoru = _vektor_hedefe_yaklastir(
            oyuncu_hareket_hiz_vektoru,
            pygame.Vector2(),
            OYUNCU_YAVASLAMA * dt,
        )
        return



    hareket_carpani = 1.0
    if oyuncu_savunuyor:
        hareket_carpani = 0.36
    if oyuncu_saldiriyor:
        if (
            karakter_cinsiyet == "male"
            and ADEFONSUS_YENI_SHEET_AKTIF
            and oyuncu_saldiri_modu in ("charge", "hold_release")
        ):
            oyuncu_hareket_hiz_vektoru = _vektor_hedefe_yaklastir(
                oyuncu_hareket_hiz_vektoru,
                pygame.Vector2(),
                OYUNCU_YAVASLAMA * dt,
            )
            return
        hareket_carpani = 0.32

    hedef_hiz = input_v * OYUNCU_YURUYUS_HIZI * hareket_carpani
    if input_v.length_squared() <= 0.0:
        ivme = OYUNCU_YAVASLAMA
    elif (
        oyuncu_hareket_hiz_vektoru.length_squared() > 1.0
        and oyuncu_hareket_hiz_vektoru.dot(hedef_hiz) < 0
    ):
        ivme = OYUNCU_DONUS_IVMESI
    else:
        ivme = OYUNCU_HIZLANMA
    oyuncu_hareket_hiz_vektoru = _vektor_hedefe_yaklastir(
        oyuncu_hareket_hiz_vektoru, hedef_hiz, ivme * dt
    )

    once = pygame.Vector2(oyuncu_x, oyuncu_y)
    delta = oyuncu_hareket_hiz_vektoru * dt
    nx = max(35.0, min(HARITA_GENISLIK - 35.0, oyuncu_x + delta.x))
    ny = max(35.0, min(HARITA_YUKSEKLIK - 25.0, oyuncu_y + delta.y))
    if hareket_gecerli_mi(nx, oyuncu_y):
        oyuncu_x = nx
    else:
        oyuncu_hareket_hiz_vektoru.x = 0.0
    if hareket_gecerli_mi(oyuncu_x, ny):
        oyuncu_y = ny
    else:
        oyuncu_hareket_hiz_vektoru.y = 0.0
    oyuncu_hareket_ediyor = pygame.Vector2(oyuncu_x, oyuncu_y).distance_to(once) > 0.025
# </POTBO_STAGE S0552>

# <POTBO_STAGE S0582>





def _v33_oyuncu_kucuk_sektir(kaynak_x, kaynak_y, hiz=54.0, sure=92):
    global oyuncu_zorlanmis_hiz, oyuncu_zorlanmis_bitis, oyuncu_zorlanmis_son_guncelleme
    if oyuncu_hp <= 0:
        return
    d = pygame.Vector2(
        float(oyuncu_x) - float(kaynak_x),
        float(oyuncu_y) - float(kaynak_y),
    )
    if d.length_squared() <= 1e-6:
        d = pygame.Vector2(1.0, 0.0)
    d = d.normalize()
    yeni = d * float(hiz)

    if oyuncu_zorlanmis_hiz.length() < yeni.length():
        oyuncu_zorlanmis_hiz = yeni
    else:
        oyuncu_zorlanmis_hiz += yeni * 0.28
    simdi = pygame.time.get_ticks()
    oyuncu_zorlanmis_bitis = max(int(oyuncu_zorlanmis_bitis), simdi + int(sure))
    oyuncu_zorlanmis_son_guncelleme = simdi
# </POTBO_STAGE S0582>

# <POTBO_STAGE S0593>


def _v33_corpse_pose(simdi=None):
    if simdi is None:
        simdi = pygame.time.get_ticks()
    gecen = max(0, int(simdi) - int(oyuncu_olum_baslangic_ms))
    p = max(0.0, min(1.0, gecen / float(OLU_CESET_YERLESME_MS)))
    ease = 1.0 - (1.0 - p) ** 3
    hedef_aci = -90.0 if oyuncu_yonu in ("right", "down") else 90.0
    angle = hedef_aci * ease
    center = pygame.Vector2(
        float(dunya_ekran_x(oyuncu_x)),
        float(dunya_ekran_y(oyuncu_y) - 8 + 7 * ease),
    )
    return gecen, ease, angle, center
# </POTBO_STAGE S0593>

# <POTBO_STAGE S0636>
v34_special_path_valid = False
# </POTBO_STAGE S0636>

# <POTBO_STAGE S0639>
v34_special_path_debug = []
# </POTBO_STAGE S0639>

# <POTBO_STAGE S0641>
v34_collision_soft_escape_events = 0
v34_collision_hard_recovery_events = 0
# </POTBO_STAGE S0641>

# <POTBO_STAGE S0643>


def _v34_player_bounds_ok(x, y):
    return (
        V34_PLAYER_SAFE_MARGIN_X
        <= float(x)
        <= HARITA_GENISLIK - V34_PLAYER_SAFE_MARGIN_X
        and V34_PLAYER_SAFE_MARGIN_TOP
        <= float(y)
        <= HARITA_YUKSEKLIK - V34_PLAYER_SAFE_MARGIN_BOTTOM
    )


def _v34_player_map_block_count(x, y):
    """Oyuncu ayak örneklerinin kaçının static map polygonunda olduğunu sayar."""
    count = 0
    for px, py in oyuncu_ayak_noktalari(float(x), float(y)):
        if harita_pikseli_engel_mi(px, py):
            count += 1
    return count
# </POTBO_STAGE S0643>

# <POTBO_STAGE S0647>


def _v34_dynamic_position_valid(x, y, baseline=None, exclude=None):
    """Dynamic overlap'ı sert kilit yerine monotonic escape kuralıyla çözer."""
    global v34_collision_soft_escape_events
    test_rect = oyuncu_carpisma_rect(x, y)
    baseline_rect = oyuncu_carpisma_rect(*baseline) if baseline is not None else None

    for blocker in _v34_dynamic_blockers(exclude=exclude):
        new_area = _v34_rect_overlap_alani(test_rect, blocker)
        if new_area <= 0:
            continue
        if baseline_rect is None:
            return False
        old_area = _v34_rect_overlap_alani(baseline_rect, blocker)
        if old_area <= 0:
            return False

        if new_area > old_area + V34_DYNAMIC_ESCAPE_EPSILON:
            return False
        v34_collision_soft_escape_events += 1
    return True
# </POTBO_STAGE S0647>

# <POTBO_STAGE S0649>


def hareket_gecerli_mi(yeni_x, yeni_y):
    """V34: sub-step collision + overlap escape.

    Eski kontratın en büyük sorunu, düşman oyuncunun içine girdiğinde oyuncunun
    overlap'tan çıkmaya çalışırken dahi her yeni pozisyonu reddetmesiydi. Burada
    her ara adım mevcut oyuncu pozisyonuna göre değerlendirilir: yeni overlap
    artmıyorsa hareket kaçış olarak kabul edilir. Static polygonlar için de aynı
    prensip, engel içindeki ayak örneği sayısı üzerinden uygulanır.
    """
    start_x = float(oyuncu_x)
    start_y = float(oyuncu_y)
    fark_x = float(yeni_x) - start_x
    fark_y = float(yeni_y) - start_y
    mesafe = max(abs(fark_x), abs(fark_y))
    adim_sayisi = max(1, int(math.ceil(mesafe / 2.0)))
    baseline = (start_x, start_y)

    for adim in range(1, adim_sayisi + 1):
        oran = adim / adim_sayisi
        tx = start_x + fark_x * oran
        ty = start_y + fark_y * oran
        if not _v34_player_position_valid(tx, ty, dynamic=True, baseline=baseline):
            return False
    return True
# </POTBO_STAGE S0649>

# <POTBO_STAGE S0652>


def _v34_player_depenetrate(force=False):
    """Oyuncuyu invalid static geometry'den en yakın güvenli noktaya çıkarır.

    Normal bir duvara yürümek teleport üretmez. Bu yalnız mevcut pozisyon gerçekten
    geçersizse çalışır; dolayısıyla wall-push davranışını bozmaz.
    """
    global oyuncu_x, oyuncu_y, v34_last_safe_player_pos
    global v34_player_recovery_count, v34_collision_hard_recovery_events

    current = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    current_static_ok = _v34_static_position_valid(current.x, current.y)
    current_full_ok = _v34_player_position_valid(current.x, current.y, dynamic=True)
    if current_full_ok and not force:
        v34_last_safe_player_pos = current
        return False


    if (
        v34_last_safe_player_pos is not None
        and current.distance_to(v34_last_safe_player_pos) <= 110.0
        and _v34_player_position_valid(
            v34_last_safe_player_pos.x,
            v34_last_safe_player_pos.y,
            dynamic=True,
        )
    ):
        oyuncu_x = float(v34_last_safe_player_pos.x)
        oyuncu_y = float(v34_last_safe_player_pos.y)
        v34_player_recovery_count += 1
        v34_collision_hard_recovery_events += 1
        return True



    if current_static_ok and not force:
        return False

    for radius in V34_UNSTUCK_SEARCH_RADII:
        for angle in V34_UNSTUCK_ANGLES:
            candidate = current + pygame.Vector2(radius, 0.0).rotate(angle)
            if _v34_player_position_valid(candidate.x, candidate.y, dynamic=True):
                oyuncu_x = float(candidate.x)
                oyuncu_y = float(candidate.y)
                v34_last_safe_player_pos = candidate
                v34_player_recovery_count += 1
                v34_collision_hard_recovery_events += 1
                return True
    return False


def _v34_player_safety_tick():
    global v34_last_safe_player_pos, v34_last_safety_check_ms, v34_player_was_invalid
    simdi = pygame.time.get_ticks()
    if simdi - v34_last_safety_check_ms < 90:
        return
    v34_last_safety_check_ms = simdi
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA or oyuncu_hp <= 0:
        return
    if gelistirici_x_skill_aktif_mi(simdi):
        return

    pos = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    if _v34_player_position_valid(pos.x, pos.y, dynamic=True):
        v34_last_safe_player_pos = pos
        v34_player_was_invalid = False
        return

    v34_player_was_invalid = True


    if not _v34_static_position_valid(pos.x, pos.y):
        _v34_player_depenetrate(False)
# </POTBO_STAGE S0652>

# <POTBO_STAGE S0655>


def _v34_dash_trail_ciz():
    if not v34_dash_trail:
        return
    simdi = pygame.time.get_ticks()
    katman = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    alive = []
    for t0, p in list(v34_dash_trail):
        age = simdi - t0
        if age > 190:
            continue
        alive.append((t0, p))
    v34_dash_trail.clear()
    v34_dash_trail.extend(alive)
    if len(alive) < 2:
        return
    for i in range(1, len(alive)):
        age = simdi - alive[i][0]
        fade = max(0.0, 1.0 - age / 190.0)
        a = alive[i - 1][1]
        b = alive[i][1]
        pa = (dunya_ekran_x(a.x), dunya_ekran_y(a.y - 8.0))
        pb = (dunya_ekran_x(b.x), dunya_ekran_y(b.y - 8.0))
        pygame.draw.line(katman, (210, 210, 220, int(46 * fade)), pa, pb, 7)
        pygame.draw.line(katman, (244, 242, 247, int(82 * fade)), pa, pb, 2)
    ekran.blit(katman, (0, 0))
# </POTBO_STAGE S0655>

# <POTBO_STAGE S0657>


def _v34_special_path_controls(path, center, radius):
    start, entry, p1, p2, p3, p4 = path
    out = entry - center
    if out.length_squared() <= 1e-6:
        out = pygame.Vector2(-1.0, 1.0)
    setup_control = center + out.normalize() * (radius * 1.10)
    switch_control = center + pygame.Vector2(0.0, -radius * 1.34)
    return setup_control, switch_control


def _v34_special_path_clear(path, center, radius):
    if len(path) < 6:
        return False
    start, entry, p1, p2, p3, p4 = path
    setup_control, switch_control = _v34_special_path_controls(path, center, radius)

    return (
        _v34_segment_static_clear(start, entry, 2.7)
        and _v34_curve_static_clear(entry, setup_control, p1)
        and _v34_segment_static_clear(p1, p2, 2.5)
        and _v34_curve_static_clear(p2, switch_control, p3)
        and _v34_segment_static_clear(p3, p4, 2.5)
    )


def _gelistirici_x_skill_yol_kur(hedef, baslangic):
    """V34: authored X geometrisini koruyup çevreye sığan en büyük radius'u seçer."""
    global v34_special_effect_radius, v34_special_locked_center
    global v34_special_path_valid, v34_special_path_debug

    center = pygame.Vector2(float(hedef.x), float(hedef.y))
    v34_special_locked_center = center.copy()
    v34_special_path_debug = []

    for radius in V34_SPECIAL_RADIUS_STEPS:
        path = _v34_special_candidate_path(hedef, baslangic, radius)
        clear = _v34_special_path_clear(path, center, radius)
        v34_special_path_debug.append((radius, clear, [p.copy() for p in path]))
        if clear:
            v34_special_effect_radius = float(radius)
            v34_special_path_valid = True
            return path



    radius = V34_SPECIAL_MIN_RADIUS
    raw = _v34_special_candidate_path(hedef, baslangic, radius)
    repaired = [raw[0]]
    for p in raw[1:]:
        safe = _v34_find_nearest_static_safe(p, origin=center, max_radius=54.0)
        repaired.append(safe if safe is not None else p)
    v34_special_effect_radius = radius
    v34_special_path_valid = _v34_special_path_clear(repaired, center, radius)
    return repaired
# </POTBO_STAGE S0657>

# <POTBO_STAGE S0665>





def _v34_world_to_screen_vec(p, yoff=0.0):
    p = pygame.Vector2(p)
    return pygame.Vector2(
        float(dunya_ekran_x(p.x)),
        float(dunya_ekran_y(p.y + yoff)),
    )


def _v34_special_trail_ciz(katman, simdi):
    if len(v34_special_trail) < 2:
        return
    items = list(v34_special_trail)
    for i in range(1, len(items)):
        t0, a, phase_a = items[i - 1]
        t1, b, phase_b = items[i]
        age = simdi - t1
        if age > 430:
            continue
        fade = max(0.0, 1.0 - age / 430.0)
        if "slash" in phase_b:
            base_alpha = 118
            width = 10
        elif phase_b == "entry":
            base_alpha = 82
            width = 7
        else:
            base_alpha = 44
            width = 5
        sa = _v34_world_to_screen_vec(a, -9.0)
        sb = _v34_world_to_screen_vec(b, -9.0)
        pygame.draw.line(
            katman,
            (126, 8, 24, int(base_alpha * 0.65 * fade)),
            sa,
            sb,
            width + 6,
        )
        pygame.draw.line(
            katman,
            (238, 52, 72, int(base_alpha * fade)),
            sa,
            sb,
            width,
        )
        pygame.draw.line(
            katman,
            (255, 235, 240, int(base_alpha * 0.85 * fade)),
            sa,
            sb,
            max(1, width // 4),
        )


def _v34_special_afterimages_ciz(katman, simdi):
    alive = []
    for t0, p, facing, phase in list(v34_special_afterimages):
        age = simdi - t0
        if age > 260:
            continue
        alive.append((t0, p, facing, phase))
        fade = max(0.0, 1.0 - age / 260.0)
        s = _v34_world_to_screen_vec(p, -17.0)

        body_w = 18 if "slash" in phase else 15
        body_h = 32 if "slash" in phase else 28
        rect = pygame.Rect(0, 0, body_w, body_h)
        rect.center = (int(s.x), int(s.y))
        pygame.draw.ellipse(katman, (160, 12, 34, int(76 * fade)), rect)
        pygame.draw.line(
            katman,
            (246, 218, 225, int(92 * fade)),
            (rect.centerx, rect.top + 3),
            (rect.centerx, rect.bottom - 4),
            2,
        )
    v34_special_afterimages.clear()
    v34_special_afterimages.extend(alive)
# </POTBO_STAGE S0665>

# <POTBO_STAGE S0667>


def _v34_special_impact_ring_ciz(katman, simdi):
    if simdi >= v34_special_impact_ring_until or v34_special_effect_center is None:
        return
    duration = max(
        1,
        v34_special_impact_ring_until - v34_special_impact_ring_started,
    )
    t = max(
        0.0,
        min(
            1.0,
            (simdi - v34_special_impact_ring_started) / duration,
        ),
    )
    ease = 1.0 - (1.0 - t) ** 3
    radius = int(8 + ease * 54)
    alpha = int(190 * (1.0 - t))
    c = _v34_world_to_screen_vec(v34_special_effect_center, -13.0)
    pygame.draw.circle(
        katman,
        (255, 236, 240, alpha),
        (int(c.x), int(c.y)),
        radius,
        2,
    )
    pygame.draw.circle(
        katman,
        (198, 18, 42, int(alpha * 0.68)),
        (int(c.x), int(c.y)),
        max(2, radius - 6),
        1,
    )


def _v34_special_finish_pulse_ciz(katman, simdi):
    if simdi >= v34_special_finish_pulse_until or v34_special_effect_center is None:
        return
    duration = max(
        1,
        v34_special_finish_pulse_until - v34_special_finish_pulse_started,
    )
    t = max(
        0.0,
        min(
            1.0,
            (simdi - v34_special_finish_pulse_started) / duration,
        ),
    )
    c = _v34_world_to_screen_vec(v34_special_effect_center, -13.0)
    max_r = 112
    r = int(18 + max_r * (1.0 - (1.0 - t) ** 2))
    alpha = int(126 * (1.0 - t))
    pygame.draw.circle(katman, (224, 18, 48, alpha), (int(c.x), int(c.y)), r, 3)
    if t < 0.35:
        core = int(14 + 22 * t / 0.35)
        pygame.draw.circle(
            katman,
            (255, 244, 246, int(190 * (1.0 - t / 0.35))),
            (int(c.x), int(c.y)),
            core,
            2,
        )
# </POTBO_STAGE S0667>

# <POTBO_STAGE S0670>


def _v34_special_hit_counter_ciz(simdi):
    if simdi >= v34_special_hit_display_until or v34_special_effect_center is None:
        return
    remaining = max(
        0.0,
        min(1.0, (v34_special_hit_display_until - simdi) / 520.0),
    )
    center = _v34_world_to_screen_vec(v34_special_effect_center, -76.0)
    roman = ("I", "II", "III")[max(0, min(2, v34_special_hit_display_index - 1))]
    alpha = int(220 * min(1.0, remaining * 1.7))

    text = mini_font.render(roman, True, (245, 232, 236))
    text.set_alpha(alpha)
    rect = text.get_rect(center=(int(center.x), int(center.y)))
    ekran.blit(text, rect)
# </POTBO_STAGE S0670>

# <POTBO_STAGE S0673>





_v33_kamerayi_guncelle = kamerayi_guncelle


def kamerayi_guncelle():
    """Normal kamerayı korur; special sırasında hedef ve oyuncuyu aynı kompozisyonda tutar."""
    global kamera_x, kamera_y
    _v33_kamerayi_guncelle()
    simdi = pygame.time.get_ticks()
    if not gelistirici_x_skill_aktif_mi(simdi) or v34_special_locked_center is None:
        return

    visible_w = GENISLIK / KAMERA_YAKINLASTIRMA
    visible_h = YUKSEKLIK / KAMERA_YAKINLASTIRMA
    player = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    center = pygame.Vector2(v34_special_locked_center)
    focus = player.lerp(center, 0.58)
    target_x = focus.x - visible_w * 0.50
    target_y = focus.y - visible_h * 0.54

    kamera_x += (target_x - kamera_x) * 0.20
    kamera_y += (target_y - kamera_y) * 0.20
    max_x = max(0.0, HARITA_GENISLIK - visible_w)
    max_y = max(0.0, HARITA_YUKSEKLIK - visible_h)
    kamera_x = max(0.0, min(max_x, kamera_x))
    kamera_y = max(0.0, min(max_y, kamera_y))
# </POTBO_STAGE S0673>

# <POTBO_STAGE S0677>





def v34_collision_diagnostics():
    """Developer console için küçük, allocation-light collision snapshot."""
    pos = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    return {
        "version": V34_POLISH_VERSION,
        "player": (round(pos.x, 2), round(pos.y, 2)),
        "static_valid": _v34_static_position_valid(pos.x, pos.y),
        "full_valid": _v34_player_position_valid(pos.x, pos.y, dynamic=True),
        "map_block_samples": _v34_player_map_block_count(pos.x, pos.y),
        "soft_escape_events": int(v34_collision_soft_escape_events),
        "hard_recoveries": int(v34_collision_hard_recovery_events),
        "special_active": bool(gelistirici_x_skill_aktif_mi()),
        "special_path_valid": bool(v34_special_path_valid),
        "special_radius": float(v34_special_effect_radius),
        "special_hits": int(gelistirici_x_skill_vurus_maskesi),
    }
# </POTBO_STAGE S0677>

# <POTBO_STAGE S0690>


def gelistirici_x_skill_sifirla(tam_reset=False):
    """Eski reset kontratını korur; V34 transient director state'ini de temizler."""
    global v34_special_locked_center, v34_special_effect_center, v34_special_path_valid
    global v34_special_exit_safe_pos, v34_special_recovery_grace_until
    global v34_special_flash_until, v34_special_impact_ring_until
    global v34_special_hit_display_until, v34_special_finish_pulse_until
    global v34_special_pause_started_ms

    _v34a_gelistirici_x_skill_sifirla(tam_reset)
    if tam_reset:
        v34_special_locked_center = None
        v34_special_effect_center = None
        v34_special_path_valid = False
        v34_special_exit_safe_pos = None
        v34_special_recovery_grace_until = 0
        v34_special_flash_until = 0
        v34_special_impact_ring_until = 0
        v34_special_hit_display_until = 0
        v34_special_finish_pulse_until = 0
        v34_special_pause_started_ms = 0
        v34_special_trail.clear()
        v34_special_afterimages.clear()





def v34_special_pause_tick():
    """Special move'un authored zaman çizgisini pause süresinden arındırır.

    pygame.get_ticks() pause menüsünde akmaya devam ettiği için yalnız update'i durdurmak
    yeterli değildir; resume anında progress bir anda 1.0 olurdu. Burada special'ın
    başlangıç/bitiş ve hedef stun timestamp'leri pause süresi kadar ileri taşınır.
    """
    global v34_special_pause_started_ms
    global \
        gelistirici_x_skill_baslangic_ms, \
        gelistirici_x_skill_bitis_ms, \
        gelistirici_x_skill_iz_bitis
    global v34_special_recovery_grace_until
    global v34_special_flash_started, v34_special_flash_until
    global v34_special_impact_ring_started, v34_special_impact_ring_until
    global v34_special_hit_display_until
    global v34_special_finish_pulse_started, v34_special_finish_pulse_until

    simdi = pygame.time.get_ticks()
    pending = gelistirici_x_skill_baslangic_ms > 0
    gameplay = oyun_durumu == OYUN and oyun_alt_durumu == HARITA

    if pending and not gameplay:
        if v34_special_pause_started_ms <= 0:
            v34_special_pause_started_ms = int(simdi)
        return

    if pending and gameplay and v34_special_pause_started_ms > 0:
        delta = max(0, int(simdi) - int(v34_special_pause_started_ms))
        v34_special_pause_started_ms = 0
        if delta <= 0:
            return

        gelistirici_x_skill_baslangic_ms += delta
        gelistirici_x_skill_bitis_ms += delta
        gelistirici_x_skill_iz_bitis += delta
        v34_special_recovery_grace_until += delta

        if v34_special_flash_until > 0:
            v34_special_flash_started += delta
            v34_special_flash_until += delta
        if v34_special_impact_ring_until > 0:
            v34_special_impact_ring_started += delta
            v34_special_impact_ring_until += delta
        if v34_special_hit_display_until > 0:
            v34_special_hit_display_until += delta
        if v34_special_finish_pulse_until > 0:
            v34_special_finish_pulse_started += delta
            v34_special_finish_pulse_until += delta

        hedef = gelistirici_x_skill_hedef
        if hedef is not None:
            try:
                hedef.hit_stun_until = int(getattr(hedef, "hit_stun_until", 0)) + delta
                hedef.recovery_until = int(getattr(hedef, "recovery_until", 0)) + delta
            except Exception:
                pass
# </POTBO_STAGE S0690>

# <POTBO_STAGE S0694>





_v34a_kamerayi_guncelle = kamerayi_guncelle


def kamerayi_guncelle():
    """V34 special framing + normal locomotion look-ahead."""
    global kamera_x, kamera_y
    _v34a_kamerayi_guncelle()
    simdi = pygame.time.get_ticks()
    if gelistirici_x_skill_aktif_mi(simdi):
        return
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA or oyuncu_hp <= 0:
        return

    velocity = pygame.Vector2(oyuncu_hareket_hiz_vektoru)
    if oyuncu_dash_aktif_mi(simdi) and dash_aktif_yonu.length_squared() > 1e-6:
        velocity = dash_aktif_yonu.normalize() * (OYUNCU_YURUYUS_HIZI * 1.45)
    if velocity.length_squared() <= 16.0:
        return

    max_look = 34.0
    look = velocity * 0.085
    if look.length() > max_look:
        look.scale_to_length(max_look)


    kamera_x += look.x * 0.055
    kamera_y += look.y * 0.040

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
# </POTBO_STAGE S0694>

# <POTBO_STAGE S0715>


def v34_crowd_separation_tick():
    """Kalabalık body overlap'larını düşük frekansta çözer; AI pathfinding'i değiştirmez."""
    global v34_crowd_last_tick
    simdi = pygame.time.get_ticks()
    if simdi - v34_crowd_last_tick < V34_CROWD_SEPARATION_INTERVAL_MS:
        return
    v34_crowd_last_tick = simdi
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA or oyuncu_hp <= 0:
        return
    if gelistirici_x_skill_aktif_mi(simdi):

        return

    actors = _v34_actor_list()
    if not actors:
        return
    for actor in actors:
        _v34_push_actor_from_player(actor, actors)

    pairs = 0
    for i in range(len(actors)):
        for j in range(i + 1, len(actors)):
            if pairs >= V34_CROWD_MAX_PAIRS_PER_TICK:
                return
            if _v34_push_actor_pair(actors[i], actors[j], actors):
                pairs += 1
# </POTBO_STAGE S0715>

# <POTBO_STAGE S0717>





def _v34_special_recovery_control_hint_ciz():
    """Special bittiği ilk 170 ms'de çok küçük kontrol dönüş işareti.

    Bu bir tutorial yazısı değildir; yalnız oyuncunun authored sequence'in gerçekten
    bittiğini periferik olarak hissetmesi için ayak çevresinde sönen ince halkadır.
    """
    simdi = pygame.time.get_ticks()
    if (
        v34_special_recovery_grace_until <= 0
        or simdi >= v34_special_recovery_grace_until
    ):
        return
    if gelistirici_x_skill_aktif_mi(simdi):
        return
    remaining = max(
        0.0,
        min(
            1.0,
            (v34_special_recovery_grace_until - simdi) / V34_SPECIAL_RECOVERY_GRACE_MS,
        ),
    )
    center = (
        dunya_ekran_x(oyuncu_x),
        dunya_ekran_y(oyuncu_y - 2.0),
    )
    radius = int(12 + 14 * (1.0 - remaining))
    alpha = int(100 * remaining)
    layer = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    pygame.draw.ellipse(
        layer,
        (230, 220, 226, alpha),
        pygame.Rect(
            center[0] - radius,
            center[1] - radius // 3,
            radius * 2,
            max(4, radius // 2),
        ),
        1,
    )
    ekran.blit(layer, (0, 0))
# </POTBO_STAGE S0717>

# <POTBO_STAGE S0722>







def _v34_diagnostics_overlay_ciz():
    if not (GELISTIRICI_MODU and DEBUG_LOGS):
        return
    data = v34_collision_diagnostics()
    lines = [
        f"V34 collision: {'OK' if data['full_valid'] else 'INVALID'}",
        f"soft escapes: {data['soft_escape_events']}  rescues: {data['hard_recoveries']}",
        f"crowd player/pair: {v34_crowd_player_separations}/{v34_crowd_pair_separations}",
        f"buffer attack/dash: {v34_input_buffer_attack_count}/{v34_input_buffer_dash_count}",
        f"combo best: {v34_combo_best}",
    ]
    x = GENISLIK - 330
    y = YUKSEKLIK - 130
    bg = pygame.Surface((304, 112), pygame.SRCALPHA)
    bg.fill((4, 3, 6, 160))
    ekran.blit(bg, (x - 10, y - 8))
    for i, line in enumerate(lines):
        surf = mini_font.render(line, True, (190, 186, 196))
        ekran.blit(surf, (x, y + i * 20))
# </POTBO_STAGE S0722>

# <POTBO_STAGE S0726>
V34_THREAT_WORLD_RANGE = 760.0
# </POTBO_STAGE S0726>

# <POTBO_STAGE S0732>


def _v34_special_target_preview_ciz():
    target = _v34_special_target_preview_target()
    if target is None or gelistirici_x_skill_aktif_mi():
        return
    simdi = pygame.time.get_ticks()
    pulse = 0.5 + 0.5 * math.sin(simdi / 115.0)
    alpha = int(82 + (V34_TARGET_PREVIEW_MAX_ALPHA - 82) * pulse)
    cx = dunya_ekran_x(target.x)
    cy = dunya_ekran_y(target.y - 12.0)
    radius = int(V34_TARGET_PREVIEW_RADIUS + 2.0 * pulse)
    layer = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)



    for start in (18, 108, 198, 288):
        rect = pygame.Rect(cx - radius, cy - radius, radius * 2, radius * 2)
        pygame.draw.arc(
            layer,
            (226, 34, 58, alpha),
            rect,
            math.radians(start),
            math.radians(start + 42),
            2,
        )
    dot_r = 2
    for angle in (45, 135, 225, 315):
        v = pygame.Vector2(radius + 4, 0).rotate(angle)
        pygame.draw.circle(
            layer,
            (250, 232, 236, int(alpha * 0.82)),
            (int(cx + v.x), int(cy + v.y)),
            dot_r,
        )
    ekran.blit(layer, (0, 0))


def _v34_special_path_preview_ciz():
    """R basılı tutulurken, release öncesi iki slash doğrultusunu çok soluk gösterir."""
    if not gelistirici_x_skill_r_basildi or gelistirici_x_skill_aktif_mi():
        return
    target = _v34_special_target_preview_target()
    if target is None:
        return
    center = pygame.Vector2(float(target.x), float(target.y))
    r = min(96.0, GELISTIRICI_X_SKILL_YARI_CAP)
    h = r * 0.78
    points = (
        (
            center + pygame.Vector2(-r, +h),
            center + pygame.Vector2(+r, -h),
        ),
        (
            center + pygame.Vector2(-r, -h),
            center + pygame.Vector2(+r, +h),
        ),
    )
    layer = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    for a, b in points:
        sa = _v34_world_to_screen_vec(a, -12.0)
        sb = _v34_world_to_screen_vec(b, -12.0)
        pygame.draw.line(layer, (198, 24, 48, 48), sa, sb, 3)
        pygame.draw.line(layer, (248, 232, 236, 62), sa, sb, 1)
    ekran.blit(layer, (0, 0))


def _v34_threat_candidates():
    global v34_threat_indicator_cache, v34_threat_indicator_cache_ms
    simdi = pygame.time.get_ticks()
    if simdi - v34_threat_indicator_cache_ms < 95:
        return list(v34_threat_indicator_cache)
    v34_threat_indicator_cache_ms = simdi
    player = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    candidates = []
    for actor in _v34_actor_list():
        if not bool(getattr(actor, "aggro", False)):
            continue
        pos = pygame.Vector2(float(actor.x), float(actor.y))
        dist = pos.distance_to(player)
        if dist > V34_THREAT_WORLD_RANGE:
            continue
        sx = dunya_ekran_x(pos.x)
        sy = dunya_ekran_y(pos.y - 18.0)
        onscreen = -18 <= sx <= GENISLIK + 18 and -18 <= sy <= YUKSEKLIK + 18
        if onscreen:
            continue
        threat = float(getattr(actor, "max_hp", 1))
        score = dist - min(80.0, threat * 0.03)
        candidates.append((score, actor, pos))
    candidates.sort(key=lambda item: item[0])
    v34_threat_indicator_cache = candidates[:V34_THREAT_MAX_INDICATORS]
    return list(v34_threat_indicator_cache)
# </POTBO_STAGE S0732>

# <POTBO_STAGE S0734>


def _v34_threat_indicators_ciz():
    if oyun_alt_durumu != HARITA or oyuncu_hp <= 0 or gelistirici_x_skill_aktif_mi():
        return
    threats = _v34_threat_candidates()
    if not threats:
        return
    player = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    layer = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    for rank, (_, actor, pos) in enumerate(threats):
        direction_world = pos - player
        if direction_world.length_squared() <= 1e-6:
            continue

        d = direction_world.normalize()
        edge = _v34_line_to_screen_edge(d)
        inward = -d * 7.0
        tangent = pygame.Vector2(-d.y, d.x)
        tip = edge
        p1 = edge + inward + tangent * 5.0
        p2 = edge + inward - tangent * 5.0
        alpha = 150 - rank * 22
        pygame.draw.polygon(layer, (210, 28, 48, alpha), [tip, p1, p2])
        pygame.draw.circle(
            layer,
            (244, 224, 228, int(alpha * 0.72)),
            (
                int(edge.x + inward.x * 1.8),
                int(edge.y + inward.y * 1.8),
            ),
            2,
        )
    ekran.blit(layer, (0, 0))
# </POTBO_STAGE S0734>

# <POTBO_STAGE S0737>


def _v34_fix_special_linger(simdi):
    global gelistirici_x_skill_hedef, gelistirici_x_skill_yol
    global v34_special_locked_center, v34_special_effect_center, v34_special_path_valid
    if gelistirici_x_skill_baslangic_ms > 0:
        return False
    if (
        gelistirici_x_skill_iz_bitis <= 0
        or simdi <= gelistirici_x_skill_iz_bitis + V34_STALE_SPECIAL_CLEANUP_MS
    ):
        return False
    gelistirici_x_skill_hedef = None
    gelistirici_x_skill_yol = []
    v34_special_locked_center = None
    v34_special_effect_center = None
    v34_special_path_valid = False
    return True
# </POTBO_STAGE S0737>

# <POTBO_STAGE S0741>


def oyun_ekrani_ciz():
    _v34d_oyun_ekrani_ciz()
    if oyuncu_hp <= 0:
        return
    _v34_special_target_preview_ciz()
    _v34_special_path_preview_ciz()
    _v34_threat_indicators_ciz()
# </POTBO_STAGE S0741>

# <POTBO_STAGE S0745>


def oyuncu_kanli_hasar_kaydi(kaynak_x, kaynak_y, profil, hasar, kaynak_adi=""):
    """Special'ın authored üç-hit gövdesini lethal interruption'dan korur.

    Bu tam invulnerability değildir: HP normal şekilde azalır. Yalnız incoming hit
    special'ın ilk %78'inde HP'yi 0'a indirmişse kayıt işlenmeden önce 1 HP'ye çekilir.
    Böylece teknik üç vuruşu tamamlar; oyuncu finalden sonra 1 HP ile gerçek tehlikede kalır.
    """
    global oyuncu_hp, v34_special_armor_saves
    if int(hasar) > 0 and oyuncu_hp <= 0 and v34_special_cinematic_armor_active():
        oyuncu_hp = 1
        v34_special_armor_saves += 1
        dunya_olayi_kaydet(
            "special_cinematic_armor",
            source=str(kaynak_adi or profil),
            prevented_lethal=True,
            serial=v34_special_move_serial,
        )
    return _v34e_oyuncu_kanli_hasar_kaydi(kaynak_x, kaynak_y, profil, hasar, kaynak_adi)
# </POTBO_STAGE S0745>

# <POTBO_STAGE S0750>


def _v34_interaction_target_marker_ciz():
    if not etkilesim_ipuclari or oyun_alt_durumu != HARITA or oyuncu_hp <= 0:
        return
    if gelistirici_x_skill_aktif_mi():
        return
    target = v34_interaction_target()
    if target is None:
        return
    x = dunya_ekran_x(target["x"])
    y = dunya_ekran_y(target["y"] - 5.0)
    simdi = pygame.time.get_ticks()
    pulse = 0.5 + 0.5 * math.sin(simdi / 180.0)
    radius = int(10 + 2 * pulse)
    alpha = int(50 + 35 * pulse)
    layer = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    pygame.draw.ellipse(
        layer,
        (236, 230, 238, alpha),
        pygame.Rect(
            x - radius,
            y - radius // 3,
            radius * 2,
            max(4, radius // 2),
        ),
        1,
    )
    ekran.blit(layer, (0, 0))
# </POTBO_STAGE S0750>

# <POTBO_STAGE S0752>




_v34e_special_register_trail = _v34_special_register_trail
# </POTBO_STAGE S0752>

# <POTBO_STAGE S0757>
























V34F_VERSION = "34F"
# </POTBO_STAGE S0757>

# <POTBO_STAGE S0760>
V34F_SPECIAL_CAMERA_PUNCH = (1.8, 2.8, 4.4)
V34F_SPECIAL_CAMERA_PUNCH_MS = (95, 125, 175)
# </POTBO_STAGE S0760>

# <POTBO_STAGE S0772>
v34f_special_camera_punch_started = 0
v34f_special_camera_punch_until = 0
v34f_special_camera_punch_slot = 0
v34f_special_camera_punch_direction = pygame.Vector2(1.0, 0.0)
# </POTBO_STAGE S0772>

# <POTBO_STAGE S0779>


def _v34f_corrupt_path(path):
    stamp = _v34f_now()
    return os.path.abspath(path) + f"{V34F_CORRUPT_SUFFIX}.{stamp}"
# </POTBO_STAGE S0779>

# <POTBO_STAGE S0788>


def _v34_special_hit_feedback(slot, center, direction):
    global v34f_special_camera_punch_started, v34f_special_camera_punch_until
    global v34f_special_camera_punch_slot, v34f_special_camera_punch_direction
    global v34f_special_final_cut_started, v34f_special_final_cut_until
    global v34f_special_last_final_direction, v34f_special_last_center

    _v34f_previous_special_hit_feedback(slot, center, direction)
    simdi = _v34f_now()
    slot = max(0, min(2, int(slot)))
    center = pygame.Vector2(center)
    direction = _v34f_direction_safe(direction)
    v34f_special_hit_positions[slot] = center.copy()
    v34f_special_hit_times[slot] = simdi
    v34f_special_hit_directions[slot] = direction.copy()
    v34f_special_last_center = center.copy()
    v34f_special_camera_punch_started = simdi
    v34f_special_camera_punch_until = simdi + V34F_SPECIAL_CAMERA_PUNCH_MS[slot]
    v34f_special_camera_punch_slot = slot
    v34f_special_camera_punch_direction = direction.copy()
    _v34f_spawn_hit_sparks(slot, center, direction, simdi)
    _v34f_add_special_echo(slot, center, direction, simdi)
    if slot == 2:
        v34f_special_last_final_direction = direction.copy()
        v34f_special_final_cut_started = simdi
        v34f_special_final_cut_until = simdi + V34F_SPECIAL_FINAL_CUT_MS
# </POTBO_STAGE S0788>

# <POTBO_STAGE S0792>





def _v34f_shift_special_timeline(delta):
    """Window focus dışındayken authored time'ın arkada akmasını engeller."""
    global \
        gelistirici_x_skill_baslangic_ms, \
        gelistirici_x_skill_bitis_ms, \
        gelistirici_x_skill_iz_bitis
    global v34_special_recovery_grace_until
    global v34_special_flash_started, v34_special_flash_until
    global v34_special_impact_ring_started, v34_special_impact_ring_until
    global v34_special_hit_display_until
    global v34_special_finish_pulse_started, v34_special_finish_pulse_until
    global v34f_special_camera_punch_started, v34f_special_camera_punch_until
    global v34f_special_final_cut_started, v34f_special_final_cut_until

    delta = max(0, int(delta))
    if delta <= 0:
        return
    if gelistirici_x_skill_baslangic_ms > 0:
        gelistirici_x_skill_baslangic_ms += delta
        gelistirici_x_skill_bitis_ms += delta
        gelistirici_x_skill_iz_bitis += delta
        v34_special_recovery_grace_until += delta
    if v34_special_flash_until > 0:
        v34_special_flash_started += delta
        v34_special_flash_until += delta
    if v34_special_impact_ring_until > 0:
        v34_special_impact_ring_started += delta
        v34_special_impact_ring_until += delta
    if v34_special_hit_display_until > 0:
        v34_special_hit_display_until += delta
    if v34_special_finish_pulse_until > 0:
        v34_special_finish_pulse_started += delta
        v34_special_finish_pulse_until += delta
    if v34f_special_camera_punch_until > 0:
        v34f_special_camera_punch_started += delta
        v34f_special_camera_punch_until += delta
    if v34f_special_final_cut_until > 0:
        v34f_special_final_cut_started += delta
        v34f_special_final_cut_until += delta
    target = gelistirici_x_skill_hedef
    if target is not None:
        try:
            target.hit_stun_until = int(getattr(target, "hit_stun_until", 0)) + delta
            target.recovery_until = int(getattr(target, "recovery_until", 0)) + delta
        except Exception:
            pass


def v34f_focus_safety_tick():
    global \
        v34f_last_focus, \
        v34f_focus_lost_ms, \
        v34f_focus_regained_ms, \
        v34f_focus_loss_count
    global oyuncu_savunuyor, dash_tus_kilitli
    simdi = _v34f_now()
    try:
        focused = bool(pygame.key.get_focused())
    except Exception:
        focused = True

    if v34f_last_focus and not focused:
        v34f_focus_lost_ms = simdi
        v34f_focus_loss_count += 1
    elif not v34f_last_focus and focused:
        v34f_focus_regained_ms = simdi
        lost_for = max(0, simdi - int(v34f_focus_lost_ms)) if v34f_focus_lost_ms else 0


        pause_compensation_pending = int(v34_special_pause_started_ms) > 0
        if (
            lost_for >= V34F_FOCUS_DEBOUNCE_MS
            and gelistirici_x_skill_baslangic_ms > 0
            and not pause_compensation_pending
            and oyun_durumu == OYUN
            and oyun_alt_durumu == HARITA
        ):
            _v34f_shift_special_timeline(lost_for)
        if not gelistirici_x_skill_aktif_mi(simdi):
            oyuncu_hareket_hiz_vektoru.update(0.0, 0.0)
            oyuncu_savunuyor = False
            dash_tus_kilitli = False
        v34f_focus_lost_ms = 0
    v34f_last_focus = focused
# </POTBO_STAGE S0792>

# <POTBO_STAGE S0794>





_v34f_previous_camera_update = kamerayi_guncelle


def kamerayi_guncelle():
    global kamera_x, kamera_y
    _v34f_previous_camera_update()
    simdi = _v34f_now()
    if simdi >= v34f_special_camera_punch_until:
        return
    duration = max(
        1,
        v34f_special_camera_punch_until - v34f_special_camera_punch_started,
    )
    t = max(
        0.0,
        min(
            1.0,
            (simdi - v34f_special_camera_punch_started) / duration,
        ),
    )
    envelope = (1.0 - t) ** 2
    slot = max(0, min(2, int(v34f_special_camera_punch_slot)))
    d = _v34f_direction_safe(v34f_special_camera_punch_direction)
    n = pygame.Vector2(-d.y, d.x)
    strength = V34F_SPECIAL_CAMERA_PUNCH[slot] * envelope

    kamera_x += -d.x * strength + n.x * strength * 0.22
    kamera_y += -d.y * strength + n.y * strength * 0.22
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





def _v34f_draw_sparks(layer, simdi):
    alive = []
    for born, start, velocity, life, length, slot in list(v34f_special_sparks):
        age = simdi - born
        if age < 0 or age >= life:
            continue
        alive.append((born, start, velocity, life, length, slot))
        t = max(0.0, min(1.0, age / max(1.0, float(life))))
        drag = 1.0 - 0.42 * t
        world = start + velocity * (age / 1000.0) * drag
        d = _v34f_direction_safe(velocity)
        tail = world - d * length * (1.0 - 0.35 * t)
        a = _v34_world_to_screen_vec(world, -15.0)
        b = _v34_world_to_screen_vec(tail, -15.0)
        alpha = int((195 + slot * 18) * (1.0 - t) ** 1.4)
        width = 1 if slot == 0 else 2
        pygame.draw.line(layer, (255, 234, 238, alpha), a, b, width)
        if slot >= 1 and alpha > 70:
            pygame.draw.circle(
                layer,
                (218, 24, 50, int(alpha * 0.58)),
                (int(a.x), int(a.y)),
                2,
            )
    v34f_special_sparks.clear()
    v34f_special_sparks.extend(alive)
# </POTBO_STAGE S0794>

# <POTBO_STAGE S0796>


def _v34f_draw_landing(layer, simdi):
    alive = []
    for born, start, velocity, size in list(v34f_special_landing_marks):
        age = simdi - born
        if age < 0 or age >= V34F_SPECIAL_LANDING_LIFE_MS:
            continue
        alive.append((born, start, velocity, size))
        t = max(
            0.0,
            min(1.0, age / float(V34F_SPECIAL_LANDING_LIFE_MS)),
        )
        world = start + velocity * (age / 1000.0) * (1.0 - 0.55 * t)
        screen = _v34_world_to_screen_vec(world, 0.0)
        alpha = int(74 * (1.0 - t) ** 1.5)
        r = max(1, int(size * (1.0 + t * 0.7)))
        pygame.draw.circle(
            layer,
            (188, 178, 184, alpha),
            (int(screen.x), int(screen.y)),
            r,
        )
    v34f_special_landing_marks.clear()
    v34f_special_landing_marks.extend(alive)
# </POTBO_STAGE S0796>

# <POTBO_STAGE S0798>


def _v34f_final_cut_flash_ciz(simdi):
    if simdi >= v34f_special_final_cut_until:
        return
    duration = max(
        1,
        v34f_special_final_cut_until - v34f_special_final_cut_started,
    )
    t = max(
        0.0,
        min(
            1.0,
            (simdi - v34f_special_final_cut_started) / duration,
        ),
    )
    alpha = int(V34F_SPECIAL_FINAL_CUT_ALPHA * (1.0 - t) ** 3)
    if alpha <= 0:
        return
    layer = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    layer.fill((12, 0, 3, alpha))

    center_world = v34f_special_last_center or pygame.Vector2(
        float(oyuncu_x), float(oyuncu_y)
    )
    center = _v34_world_to_screen_vec(center_world, -12.0)
    d = _v34f_direction_safe(v34f_special_last_final_direction)
    span = max(GENISLIK, YUKSEKLIK) * 0.34
    a = center - d * span
    b = center + d * span
    pygame.draw.line(layer, (255, 244, 247, int(alpha * 1.65)), a, b, 2)
    ekran.blit(layer, (0, 0))
# </POTBO_STAGE S0798>

# <POTBO_STAGE S0801>


def _v34f_repair_player_coordinates():
    global oyuncu_x, oyuncu_y, v34f_static_recovery_last_ms, v34f_static_recovery_count
    simdi = _v34f_now()
    if simdi - v34f_static_recovery_last_ms < V34F_STATIC_RECOVERY_COOLDOWN_MS:
        return False
    v34f_static_recovery_last_ms = simdi
    if _v34f_player_coordinates_valid():
        return False
    fallback = None
    try:
        if v34_last_safe_player_pos is not None:
            fallback = pygame.Vector2(v34_last_safe_player_pos)
    except Exception:
        fallback = None
    if (
        fallback is None
        or not math.isfinite(fallback.x)
        or not math.isfinite(fallback.y)
    ):
        fallback = pygame.Vector2(HARITA_GENISLIK * 0.5, HARITA_YUKSEKLIK * 0.5)
    oyuncu_x = float(max(0.0, min(float(HARITA_GENISLIK), fallback.x)))
    oyuncu_y = float(max(0.0, min(float(HARITA_YUKSEKLIK), fallback.y)))
    v34f_static_recovery_count += 1
    _v34f_report_issue(
        "player_coordinate_recovered",
        f"to={oyuncu_x:.1f},{oyuncu_y:.1f}",
        True,
        "error",
    )
    return True
# </POTBO_STAGE S0801>

# <POTBO_STAGE S0804>


def _v34f_special_runtime_contract():
    problems = []
    simdi = _v34f_now()
    if gelistirici_x_skill_aktif_mi(simdi):
        if len(gelistirici_x_skill_yol) < 6:
            problems.append("active_without_path")
        if gelistirici_x_skill_hedef is None:
            problems.append("active_without_target")
        if gelistirici_x_skill_bitis_ms <= gelistirici_x_skill_baslangic_ms:
            problems.append("invalid_timeline")
        if not oyuncu_kontrol_kilitli_mi(simdi):
            problems.append("active_without_control_lock")
        if dash_aktif_bitis > simdi:
            problems.append("normal_dash_leaked_into_special")
    return problems
# </POTBO_STAGE S0804>

# <POTBO_STAGE S0807>





def v34f_diagnostics():
    simdi = _v34f_now()
    phase_ok, phase_detail = _v34f_special_phase_contract()
    active = gelistirici_x_skill_aktif_mi(simdi)
    player_pos = (
        round(float(oyuncu_x), 2),
        round(float(oyuncu_y), 2),
    )
    target = gelistirici_x_skill_hedef
    target_pos = None
    if target is not None:
        try:
            target_pos = (
                round(float(target.x), 2),
                round(float(target.y), 2),
            )
        except Exception:
            target_pos = None
    return {
        "version": V34F_VERSION,
        "runtime_ms": simdi - int(v34f_runtime_started_ms),
        "player": player_pos,
        "resources": _v34f_resource_snapshot(),
        "special": {
            "active": bool(active),
            "serial": int(v34_special_move_serial),
            "hits_mask": int(gelistirici_x_skill_vurus_maskesi),
            "path_valid": bool(v34_special_path_valid),
            "radius": round(float(v34_special_effect_radius), 2),
            "target": _v34f_actor_uid(target),
            "target_pos": target_pos,
            "target_anchor": tuple(v34f_special_target_anchor)
            if v34f_special_target_anchor is not None
            else None,
            "target_snaps": int(v34f_special_target_snap_count),
            "input_quarantine_frames": int(v34f_special_input_quarantine_frames),
            "phase_contract": phase_detail,
            "phase_ok": bool(phase_ok),
        },
        "collision": v34_collision_diagnostics(),
        "persistence": {
            "backup_writes": int(v34f_backup_write_count),
            "backup_restores": int(v34f_backup_restore_count),
            "backup_skips": int(v34f_backup_skip_count),
            "corrupt_files": int(v34f_corrupt_file_count),
            "last_backup_error": str(v34f_last_backup_error),
            "last_restore_error": str(v34f_last_restore_error),
        },
        "performance": {
            "frame_p95_ms": round(_v34f_frame_percentile(0.95), 2),
            "frame_spikes": int(v34f_frame_spike_count),
            "fx_quality": round(float(v34_fx_quality), 3),
            "fps": round(float(v34_fx_quality_last_fps), 2),
        },
        "audit": dict(v34f_audit_last_summary),
        "issue_counts": dict(v34f_issue_counts),
        "recent_issues": list(v34f_issues)[-8:],
    }
# </POTBO_STAGE S0807>

# <POTBO_STAGE S0816>




GELISTIRICI_X_SKILL_SURE_MS = 1660
# </POTBO_STAGE S0816>

# <POTBO_STAGE S0821>
V34F_SPECIAL_CAMERA_PUNCH = (2.35, 3.85, 6.35)
V34F_SPECIAL_CAMERA_PUNCH_MS = (82, 108, 152)
# </POTBO_STAGE S0821>

# <POTBO_STAGE S0829>


def _v35_heavy_assist_direction(base_dir):
    base = pygame.Vector2(base_dir)
    if base.length_squared() <= 1e-6:
        return pygame.Vector2(0.0, 1.0)
    base = base.normalize()
    player = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    best = None
    best_score = float("inf")
    for actor in _v35_physical_targets():
        target = pygame.Vector2(float(actor.x), float(actor.y))
        delta = target - player
        dist = delta.length()
        if dist <= 1e-6 or dist > V35_HEAVY_ASSIST_RANGE:
            continue
        forward = delta.dot(base)
        if forward <= 8.0:
            continue
        lateral = abs(delta.x * base.y - delta.y * base.x)
        if lateral > V35_HEAVY_ASSIST_MAX_LATERAL:
            continue
        if not dunya_ince_los_acik_mi(player, target, adim=5.0):
            continue
        score = lateral * 2.2 + dist * 0.16
        if score < best_score:
            best_score = score
            best = delta.normalize()
    if best is None:
        return base

    blended = base * (1.0 - V35_HEAVY_ASSIST_BLEND) + best * V35_HEAVY_ASSIST_BLEND
    return blended.normalize() if blended.length_squared() > 1e-6 else base
# </POTBO_STAGE S0829>

# <POTBO_STAGE S0840>





V35_CAMERA_DASH_LEAD = 18.0
V35_CAMERA_HEAVY_LEAD = 23.0
V35_CAMERA_SPECIAL_LEAD = 31.0
v35_camera_lead = pygame.Vector2(0.0, 0.0)
# </POTBO_STAGE S0840>

# <POTBO_STAGE S0842>


_v35_camera_original = kamerayi_guncelle
# </POTBO_STAGE S0842>

# <POTBO_STAGE S0845>


def _v35_special_signature_ciz():
    """Üçüncü hit çevresinde kısa, keskin bir X resonance; ekstra hasar üretmez."""
    simdi = pygame.time.get_ticks()
    if v34_special_hit_display_index != 3 or simdi >= v34_special_hit_display_until:
        return
    center_world = v34_special_effect_center
    if center_world is None:
        return

    age = 520 - max(0, v34_special_hit_display_until - simdi)
    if age < 0 or age > 150:
        return
    t = max(0.0, min(1.0, age / 150.0))
    alpha = int(174 * (1.0 - t) ** 1.6)
    radius = float(v34_special_effect_radius) * (0.62 + 0.18 * t)
    c = pygame.Vector2(center_world)
    segments = (
        (
            c + pygame.Vector2(-radius, radius * 0.78),
            c + pygame.Vector2(radius, -radius * 0.78),
        ),
        (
            c + pygame.Vector2(-radius, -radius * 0.78),
            c + pygame.Vector2(radius, radius * 0.78),
        ),
    )
    layer = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    for a, b in segments:
        sa = _v34_world_to_screen_vec(a, -12.0)
        sb = _v34_world_to_screen_vec(b, -12.0)
        pygame.draw.line(layer, (82, 0, 12, int(alpha * 0.55)), sa, sb, 13)
        pygame.draw.line(layer, (232, 24, 52, alpha), sa, sb, 5)
        pygame.draw.line(
            layer,
            (255, 246, 248, min(255, int(alpha * 1.18))),
            sa,
            sb,
            1,
        )
    ekran.blit(layer, (0, 0))
# </POTBO_STAGE S0845>

# <POTBO_STAGE S0853>













V36_VERSION = 36



DASH_SURESI_MS = 120



V35_CAMERA_HEAVY_LEAD = 0.0


V34_SPECIAL_AFTERIMAGE_INTERVAL_MS = 64
# </POTBO_STAGE S0853>

# <POTBO_STAGE S0859>


def _v36_screen_local(world, rect, y_offset=-12.0):
    return pygame.Vector2(
        dunya_ekran_x(float(world.x)) - rect.x,
        dunya_ekran_y(float(world.y) + float(y_offset)) - rect.y,
    )
# </POTBO_STAGE S0859>

# <POTBO_STAGE S0862>


def gelistirici_x_skill_efekt_ciz():
    """V36 compact special renderer.

    V34/V35'te bir special frame'i birden fazla 1280x720 SRCALPHA surface ayırıyordu.
    Burada slash/trail/afterimage/impact aynı küçük bölgesel surface üzerinde çizilir.
    """
    simdi = pygame.time.get_ticks()
    active_or_echo = simdi < int(gelistirici_x_skill_iz_bitis)
    if not active_or_echo or len(gelistirici_x_skill_yol) < 6:
        return

    center_world = v34_special_effect_center
    if center_world is None:
        center_world = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    center_screen = pygame.Vector2(
        dunya_ekran_x(center_world.x),
        dunya_ekran_y(center_world.y - 12.0),
    )
    rect = _v36_clip_rect_around_screen(center_screen, 255, 215)
    if rect is None:
        return
    layer = pygame.Surface(rect.size, pygame.SRCALPHA)


    items = list(v34_special_trail)
    for i in range(1, len(items)):
        _, a, _ = items[i - 1]
        t1, b, phase_b = items[i]
        age = simdi - int(t1)
        if age < 0 or age > 280:
            continue
        fade = 1.0 - age / 280.0
        width = 8 if "slash" in phase_b else 4
        alpha = int((104 if "slash" in phase_b else 54) * fade)
        sa = _v36_screen_local(pygame.Vector2(a), rect, -9.0)
        sb = _v36_screen_local(pygame.Vector2(b), rect, -9.0)
        pygame.draw.line(layer, (178, 14, 38, alpha), sa, sb, width)
        if "slash" in phase_b:
            pygame.draw.line(
                layer,
                (252, 222, 228, min(180, alpha + 28)),
                sa,
                sb,
                1,
            )


    alive_after = []
    for t0, p0, facing, phase_name in list(v34_special_afterimages):
        age = simdi - int(t0)
        if age < 0 or age > 180:
            continue
        alive_after.append((t0, p0, facing, phase_name))
        fade = 1.0 - age / 180.0
        s = _v36_screen_local(pygame.Vector2(p0), rect, -17.0)
        r = pygame.Rect(
            0,
            0,
            16 if "slash" in phase_name else 13,
            29 if "slash" in phase_name else 25,
        )
        r.center = (int(s.x), int(s.y))
        pygame.draw.ellipse(layer, (164, 12, 34, int(58 * fade)), r)
        pygame.draw.line(
            layer,
            (246, 224, 229, int(72 * fade)),
            (r.centerx, r.top + 3),
            (r.centerx, r.bottom - 4),
            1,
        )
    v34_special_afterimages.clear()
    v34_special_afterimages.extend(alive_after)

    _, _, p1, p2, p3, p4 = [pygame.Vector2(v) for v in gelistirici_x_skill_yol]
    prog1 = _v36_special_phase_progress(simdi, "setup_end", "slash1_end")
    prog2 = _v36_special_phase_progress(simdi, "switch_end", "slash2_end")
    if simdi <= gelistirici_x_skill_bitis_ms:
        a1, a2 = 195, 220
    else:
        fade = max(
            0.0,
            min(
                1.0,
                (gelistirici_x_skill_iz_bitis - simdi) / 240.0,
            ),
        )
        a1, a2 = int(160 * fade), int(190 * fade)
    _v36_draw_slash_local(layer, rect, p1, p2, prog1, a1, False)
    _v36_draw_slash_local(layer, rect, p3, p4, prog2, a2, True)


    if simdi < v34_special_impact_ring_until:
        duration = max(
            1,
            v34_special_impact_ring_until - v34_special_impact_ring_started,
        )
        t = max(
            0.0,
            min(
                1.0,
                (simdi - v34_special_impact_ring_started) / duration,
            ),
        )
        c = _v36_screen_local(pygame.Vector2(center_world), rect, -13.0)
        rr = int(9 + 48 * (1.0 - (1.0 - t) ** 3))
        aa = int(160 * (1.0 - t))
        pygame.draw.circle(
            layer,
            (250, 235, 239, aa),
            (int(c.x), int(c.y)),
            rr,
            2,
        )
        pygame.draw.circle(
            layer,
            (198, 18, 42, int(aa * 0.58)),
            (int(c.x), int(c.y)),
            max(2, rr - 5),
            1,
        )

    if simdi < v34_special_finish_pulse_until:
        duration = max(
            1,
            v34_special_finish_pulse_until - v34_special_finish_pulse_started,
        )
        t = max(
            0.0,
            min(
                1.0,
                (simdi - v34_special_finish_pulse_started) / duration,
            ),
        )
        c = _v36_screen_local(pygame.Vector2(center_world), rect, -13.0)
        rr = int(18 + 84 * (1.0 - (1.0 - t) ** 2))
        aa = int(96 * (1.0 - t))
        pygame.draw.circle(
            layer,
            (224, 18, 48, aa),
            (int(c.x), int(c.y)),
            rr,
            2,
        )

    ekran.blit(layer, rect.topleft)
    _v34_special_hit_counter_ciz(simdi)


def _v34f_special_master_vfx_ciz():
    """V36: sparks/echo/landing'i tek küçük local surface'te işler.

    Vignette ve full-screen final flash kaldırıldı; final slash'ın lokal beyaz çekirdeği
    ve kamera punch'ı korunur. Mekanik hiçbir şekilde bu render fonksiyonuna bağlı değil.
    """
    simdi = _v34f_now()
    active = gelistirici_x_skill_aktif_mi(simdi)
    if (
        not active
        and not v34f_special_echoes
        and not v34f_special_sparks
        and not v34f_special_landing_marks
    ):
        return
    center_world = v34_special_effect_center or v34f_special_last_center
    if center_world is None:
        center_world = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    center_world = pygame.Vector2(center_world)
    center_screen = pygame.Vector2(
        dunya_ekran_x(center_world.x),
        dunya_ekran_y(center_world.y - 12.0),
    )
    rect = _v36_clip_rect_around_screen(center_screen, 285, 235)
    if rect is None:
        return
    layer = pygame.Surface(rect.size, pygame.SRCALPHA)

    alive_echoes = []
    for born, slot, center, direction, radius in list(v34f_special_echoes):
        age = simdi - int(born)
        if age < 0 or age >= V34F_SPECIAL_ECHO_LIFE_MS:
            continue
        alive_echoes.append((born, slot, center, direction, radius))
        t = age / max(1.0, float(V34F_SPECIAL_ECHO_LIFE_MS))
        a, b = _v34f_echo_segment(
            int(slot),
            pygame.Vector2(center),
            direction,
            float(radius),
        )
        sa = _v36_screen_local(a, rect, -12.0)
        sb = _v36_screen_local(b, rect, -12.0)
        fade = (1.0 - t) ** 1.7
        if int(slot) == 0:
            pygame.draw.line(
                layer,
                (235, 220, 225, int(34 * fade)),
                sa,
                sb,
                1,
            )
        else:
            outer = int((64 + int(slot) * 14) * fade)
            pygame.draw.line(
                layer,
                (118, 4, 20, outer),
                sa,
                sb,
                6 if int(slot) == 2 else 5,
            )
            pygame.draw.line(
                layer,
                (238, 35, 60, min(190, int(outer * 1.25))),
                sa,
                sb,
                3,
            )
            pygame.draw.line(
                layer,
                (255, 241, 244, min(220, int(120 * fade))),
                sa,
                sb,
                1,
            )
    v34f_special_echoes.clear()
    v34f_special_echoes.extend(alive_echoes)

    alive_sparks = []
    for born, start, velocity, life, length, slot in list(v34f_special_sparks):
        age = simdi - int(born)
        if age < 0 or age >= int(life):
            continue
        alive_sparks.append((born, start, velocity, life, length, slot))
        t = age / max(1.0, float(life))
        world = pygame.Vector2(start) + pygame.Vector2(velocity) * (age / 1000.0) * (
            1.0 - 0.45 * t
        )
        d = _v34f_direction_safe(velocity)
        tail = world - d * float(length) * (1.0 - 0.35 * t)
        a = _v36_screen_local(world, rect, -15.0)
        b = _v36_screen_local(tail, rect, -15.0)
        alpha = int((185 + int(slot) * 14) * (1.0 - t) ** 1.5)
        pygame.draw.line(
            layer,
            (255, 235, 239, alpha),
            a,
            b,
            1 if int(slot) < 2 else 2,
        )
    v34f_special_sparks.clear()
    v34f_special_sparks.extend(alive_sparks)

    alive_landing = []
    for born, start, velocity, size in list(v34f_special_landing_marks):
        age = simdi - int(born)
        if age < 0 or age >= V34F_SPECIAL_LANDING_LIFE_MS:
            continue
        alive_landing.append((born, start, velocity, size))
        t = age / max(1.0, float(V34F_SPECIAL_LANDING_LIFE_MS))
        world = pygame.Vector2(start) + pygame.Vector2(velocity) * (age / 1000.0) * (
            1.0 - 0.58 * t
        )
        s = _v36_screen_local(world, rect, 0.0)
        alpha = int(58 * (1.0 - t) ** 1.4)
        pygame.draw.circle(
            layer,
            (188, 178, 184, alpha),
            (int(s.x), int(s.y)),
            max(1, int(size)),
        )
    v34f_special_landing_marks.clear()
    v34f_special_landing_marks.extend(alive_landing)


    if simdi < v34f_special_final_cut_until:
        duration = max(
            1,
            v34f_special_final_cut_until - v34f_special_final_cut_started,
        )
        t = max(
            0.0,
            min(
                1.0,
                (simdi - v34f_special_final_cut_started) / duration,
            ),
        )
        alpha = int(V34F_SPECIAL_FINAL_CUT_ALPHA * (1.0 - t) ** 3)
        c = _v36_screen_local(center_world, rect, -12.0)
        d = _v34f_direction_safe(v34f_special_last_final_direction)
        span = min(rect.width, rect.height) * 0.46
        pygame.draw.line(
            layer,
            (255, 245, 247, min(220, int(alpha * 1.6))),
            c - d * span,
            c + d * span,
            2,
        )

    ekran.blit(layer, rect.topleft)


def _v35_special_signature_ciz():
    """V36: final X signature için tam ekran surface yerine küçük lokal surface."""
    simdi = pygame.time.get_ticks()
    if v34_special_hit_display_index != 3 or simdi >= v34_special_hit_display_until:
        return
    center_world = v34_special_effect_center
    if center_world is None:
        return
    age = 520 - max(0, v34_special_hit_display_until - simdi)
    if age < 0 or age > 135:
        return
    t = max(0.0, min(1.0, age / 135.0))
    alpha = int(160 * (1.0 - t) ** 1.7)
    radius = float(v34_special_effect_radius) * (0.60 + 0.16 * t)
    c = pygame.Vector2(center_world)
    center_screen = pygame.Vector2(dunya_ekran_x(c.x), dunya_ekran_y(c.y - 12.0))
    rect = _v36_clip_rect_around_screen(
        center_screen, int(radius + 36), int(radius + 36)
    )
    if rect is None:
        return
    layer = pygame.Surface(rect.size, pygame.SRCALPHA)
    segments = (
        (
            c + pygame.Vector2(-radius, radius * 0.78),
            c + pygame.Vector2(radius, -radius * 0.78),
        ),
        (
            c + pygame.Vector2(-radius, -radius * 0.78),
            c + pygame.Vector2(radius, radius * 0.78),
        ),
    )
    for a, b in segments:
        sa = _v36_screen_local(a, rect, -12.0)
        sb = _v36_screen_local(b, rect, -12.0)
        pygame.draw.line(layer, (82, 0, 12, int(alpha * 0.48)), sa, sb, 9)
        pygame.draw.line(layer, (232, 24, 52, alpha), sa, sb, 4)
        pygame.draw.line(
            layer,
            (255, 246, 248, min(255, int(alpha * 1.12))),
            sa,
            sb,
            1,
        )
    ekran.blit(layer, rect.topleft)
# </POTBO_STAGE S0862>

# <POTBO_STAGE S0865>





_v36_camera_previous = kamerayi_guncelle


def kamerayi_guncelle():
    global v35_camera_lead
    if (
        oyuncu_saldiriyor
        and oyuncu_saldiri_modu in ("charge", "hold_release")
        and not gelistirici_x_skill_aktif_mi()
    ):
        v35_camera_lead.update(0.0, 0.0)
    _v36_camera_previous()
    if (
        oyuncu_saldiriyor
        and oyuncu_saldiri_modu in ("charge", "hold_release")
        and not gelistirici_x_skill_aktif_mi()
    ):

        v35_camera_lead.update(0.0, 0.0)


def v36_diagnostics():
    base = v35_diagnostics()
    base["v36"] = {
        "version": V36_VERSION,
        "dash_ms": int(DASH_SURESI_MS),
        "heavy_camera_lead": float(V35_CAMERA_HEAVY_LEAD),
        "afterimage_interval_ms": int(V34_SPECIAL_AFTERIMAGE_INTERVAL_MS),
        "spark_counts": tuple(int(v) for v in V34F_SPECIAL_SPARK_COUNTS),
        "trail_budget": int(v34_special_trail.maxlen or 0),
        "afterimage_budget": int(v34_special_afterimages.maxlen or 0),
        "spark_budget": int(v34f_special_sparks.maxlen or 0),
    }
    return base























V37_VERSION = 37
# </POTBO_STAGE S0865>

# <POTBO_STAGE S0891>


def genel_vinyet_ciz():
    try:
        tension = max(
            0.0,
            min(1.0, float(dunya_durumu.get("tension", 0.0))),
        )
    except (TypeError, ValueError, NameError):
        tension = 0.0
    bucket = int(round(tension * 6.0))
    ekran.blit(_v37_cached_vignette(bucket), (0, 0))
# </POTBO_STAGE S0891>

# <POTBO_STAGE S0893>


def combat_impact_fx_ciz():
    """Allocation-free melee impact renderer.

    Bütün slash impact'leri aynı 300x300 alpha buffer'ı sırayla temizleyip kullanır.
    Special'ın üç hit'i aynı frame aralığında üst üste gelse bile Surface churn oluşmaz.
    """
    simdi = pygame.time.get_ticks()
    kalan_fx = []
    center = pygame.Vector2(V37_IMPACT_LAYER_SIZE * 0.5, V37_IMPACT_LAYER_SIZE * 0.5)
    for f in combat_impact_fx:
        gecen = simdi - int(f.get("start", simdi))
        life = max(1, int(f.get("life", 180)))
        if gecen >= life:
            continue
        kalan_fx.append(f)
        tur = str(f.get("type", "slash"))
        if tur not in ("slash", "slash_heavy"):
            continue

        p = max(0.0, min(1.0, gecen / float(life)))
        alpha = int(255 * (1.0 - p) ** 1.45)
        if alpha <= 0:
            continue
        sx = dunya_ekran_x(float(f.get("x", 0.0)))
        sy = dunya_ekran_y(float(f.get("y", 0.0)))
        guc = max(0.6, min(2.8, float(f.get("power", 1.0))))
        base_angle = float(f.get("angle", 0.0)) + 32.0
        heavy = tur == "slash_heavy"
        boy = int(
            (64 if not heavy else 104)
            * min(1.35, 0.82 + guc * 0.22)
            * KAMERA_YAKINLASTIRMA
        )

        v37_impact_layer.fill((0, 0, 0, 0))
        if heavy:
            _kesik_cizgi_ciz(
                v37_impact_layer,
                center,
                base_angle - 9,
                boy,
                8,
                (118, 8, 18),
                int(alpha * 0.78),
                -3,
            )
            _kesik_cizgi_ciz(
                v37_impact_layer,
                center,
                base_angle - 9,
                boy,
                3,
                (252, 236, 224),
                alpha,
                -1,
            )
            _kesik_cizgi_ciz(
                v37_impact_layer,
                center,
                base_angle + 57,
                int(boy * 0.78),
                6,
                (172, 18, 24),
                int(alpha * 0.70),
                4,
            )
            _kesik_cizgi_ciz(
                v37_impact_layer,
                center,
                base_angle + 57,
                int(boy * 0.78),
                2,
                (255, 248, 238),
                int(alpha * 0.92),
                3,
            )
        else:
            _kesik_cizgi_ciz(
                v37_impact_layer,
                center,
                base_angle,
                boy,
                5,
                (132, 8, 18),
                int(alpha * 0.72),
                2,
            )
            _kesik_cizgi_ciz(
                v37_impact_layer,
                center,
                base_angle,
                boy,
                2,
                (255, 244, 236),
                alpha,
                0,
            )
        ekran.blit(
            v37_impact_layer,
            (int(sx - center.x), int(sy - center.y)),
        )
    combat_impact_fx[:] = kalan_fx
# </POTBO_STAGE S0893>

# <POTBO_STAGE S0895>





def _v34_interaction_target_marker_ciz():
    if not etkilesim_ipuclari or oyun_alt_durumu != HARITA or oyuncu_hp <= 0:
        return
    target = v34_interaction_target()
    if target is None:
        return
    sx = dunya_ekran_x(target["x"])
    sy = dunya_ekran_y(target["y"] - 5.0)
    now = pygame.time.get_ticks()
    pulse = 0.5 + 0.5 * math.sin(now / 180.0)
    radius = int(10 + 2 * pulse)
    alpha = int(50 + 35 * pulse)
    w = radius * 2 + 8
    h = max(12, radius + 6)
    layer = pygame.Surface((w, h), pygame.SRCALPHA)
    pygame.draw.ellipse(
        layer,
        (236, 230, 238, alpha),
        pygame.Rect(
            4,
            h // 2 - max(2, radius // 5),
            radius * 2,
            max(4, radius // 2),
        ),
        1,
    )
    ekran.blit(layer, (sx - w // 2, sy - h // 2))


def _v34_special_recovery_control_hint_ciz():
    now = pygame.time.get_ticks()
    if v34_special_recovery_grace_until <= 0 or now >= v34_special_recovery_grace_until:
        return
    if gelistirici_x_skill_aktif_mi(now):
        return
    remaining = max(
        0.0,
        min(
            1.0,
            (v34_special_recovery_grace_until - now)
            / max(1.0, V34_SPECIAL_RECOVERY_GRACE_MS),
        ),
    )
    center = (
        dunya_ekran_x(oyuncu_x),
        dunya_ekran_y(oyuncu_y - 2.0),
    )
    radius = int(12 + 14 * (1.0 - remaining))
    alpha = int(92 * remaining)
    w = radius * 2 + 6
    h = max(10, radius + 6)
    layer = pygame.Surface((w, h), pygame.SRCALPHA)
    pygame.draw.ellipse(
        layer,
        (230, 220, 226, alpha),
        pygame.Rect(
            3,
            h // 2 - max(2, radius // 6),
            radius * 2,
            max(4, radius // 2),
        ),
        1,
    )
    ekran.blit(layer, (center[0] - w // 2, center[1] - h // 2))
# </POTBO_STAGE S0895>

# <POTBO_STAGE S0897>


def _v34_dash_trail_ciz():
    if not v34_dash_trail:
        return
    now = pygame.time.get_ticks()
    alive = []
    for t0, p in list(v34_dash_trail):
        if now - int(t0) <= 150:
            alive.append((int(t0), pygame.Vector2(p)))
    v34_dash_trail.clear()
    v34_dash_trail.extend(alive)
    if len(alive) < 2:
        return

    screen_points = [
        pygame.Vector2(dunya_ekran_x(p.x), dunya_ekran_y(p.y - 8.0)) for _, p in alive
    ]
    min_x = max(0, int(min(p.x for p in screen_points)) - 12)
    max_x = min(GENISLIK, int(max(p.x for p in screen_points)) + 12)
    min_y = max(0, int(min(p.y for p in screen_points)) - 12)
    max_y = min(YUKSEKLIK, int(max(p.y for p in screen_points)) + 12)
    if max_x <= min_x or max_y <= min_y:
        return
    rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    layer = pygame.Surface(rect.size, pygame.SRCALPHA)
    for i in range(1, len(alive)):
        age = now - alive[i][0]
        fade = max(0.0, 1.0 - age / 150.0)
        a = screen_points[i - 1] - pygame.Vector2(rect.x, rect.y)
        b = screen_points[i] - pygame.Vector2(rect.x, rect.y)
        pygame.draw.line(layer, (210, 210, 220, int(34 * fade)), a, b, 5)
        pygame.draw.line(layer, (246, 242, 247, int(72 * fade)), a, b, 1)
    ekran.blit(layer, rect.topleft)


def _v34_special_target_preview_ciz():
    target = _v34_special_target_preview_target()
    if target is None or gelistirici_x_skill_aktif_mi():
        return
    now = pygame.time.get_ticks()
    pulse = 0.5 + 0.5 * math.sin(now / 115.0)
    alpha = int(76 + (V34_TARGET_PREVIEW_MAX_ALPHA - 76) * pulse)
    cx = dunya_ekran_x(target.x)
    cy = dunya_ekran_y(target.y - 12.0)
    radius = int(V34_TARGET_PREVIEW_RADIUS + 2.0 * pulse)
    size = radius * 2 + 16
    layer = pygame.Surface((size, size), pygame.SRCALPHA)
    local_rect = pygame.Rect(8, 8, radius * 2, radius * 2)
    for start in (18, 108, 198, 288):
        pygame.draw.arc(
            layer,
            (226, 34, 58, alpha),
            local_rect,
            math.radians(start),
            math.radians(start + 42),
            2,
        )
    ekran.blit(layer, (cx - size // 2, cy - size // 2))


def _v34_special_path_preview_ciz():
    if not gelistirici_x_skill_r_basildi or gelistirici_x_skill_aktif_mi():
        return
    target = _v34_special_target_preview_target()
    if target is None:
        return
    center = pygame.Vector2(float(target.x), float(target.y))
    r = min(96.0, GELISTIRICI_X_SKILL_YARI_CAP)
    h = r * 0.78
    segments = (
        (
            center + pygame.Vector2(-r, +h),
            center + pygame.Vector2(+r, -h),
        ),
        (
            center + pygame.Vector2(-r, -h),
            center + pygame.Vector2(+r, +h),
        ),
    )
    center_screen = pygame.Vector2(
        dunya_ekran_x(center.x), dunya_ekran_y(center.y - 12.0)
    )
    rect = _v36_clip_rect_around_screen(center_screen, int(r + 18), int(h + 18))
    if rect is None:
        return
    layer = pygame.Surface(rect.size, pygame.SRCALPHA)
    for a, b in segments:
        sa = _v36_screen_local(a, rect, -12.0)
        sb = _v36_screen_local(b, rect, -12.0)
        pygame.draw.line(layer, (198, 24, 48, 42), sa, sb, 2)
        pygame.draw.line(layer, (248, 232, 236, 56), sa, sb, 1)
    ekran.blit(layer, rect.topleft)


def _v34_threat_indicators_ciz():
    if oyun_alt_durumu != HARITA or oyuncu_hp <= 0 or gelistirici_x_skill_aktif_mi():
        return
    threats = _v34_threat_candidates()
    if not threats:
        return
    player = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    for rank, (_, actor, pos) in enumerate(threats):
        d = pygame.Vector2(pos) - player
        if d.length_squared() <= 1e-6:
            continue
        d = d.normalize()
        edge = _v34_line_to_screen_edge(d)
        inward = -d * 7.0
        tangent = pygame.Vector2(-d.y, d.x)
        tip = pygame.Vector2(10, 10)
        p1 = tip + inward + tangent * 5.0
        p2 = tip + inward - tangent * 5.0
        alpha = max(72, 150 - rank * 22)
        icon = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.polygon(icon, (210, 28, 48, alpha), [tip, p1, p2])
        pygame.draw.circle(
            icon,
            (244, 224, 228, int(alpha * 0.72)),
            (10, 10),
            2,
        )
        ekran.blit(icon, (int(edge.x) - 10, int(edge.y) - 10))
# </POTBO_STAGE S0897>

# <POTBO_STAGE S0906>


V34_SPECIAL_AFTERIMAGE_INTERVAL_MS = 9999
# </POTBO_STAGE S0906>

# <POTBO_STAGE S0917>


def _v34_special_path_clear(path, center, radius):

    if len(path) < 6:
        return False
    start, entry, p1, p2, p3, p4 = [pygame.Vector2(v) for v in path]
    setup_control, switch_control = _v34_special_path_controls(
        path, pygame.Vector2(center), float(radius)
    )
    step = float(V37_SPECIAL_PREFLIGHT_STEP)
    return (
        _v34_segment_static_clear(start, entry, step)
        and _v37_curve_static_clear(entry, setup_control, p1)
        and _v34_segment_static_clear(p1, p2, step)
        and _v37_curve_static_clear(p2, switch_control, p3)
        and _v34_segment_static_clear(p3, p4, step)
    )
# </POTBO_STAGE S0917>

# <POTBO_STAGE S0919>


def _v34_special_scripted_position_apply(desired, previous=None):
    """Preflight edilmiş authored path üzerinde O(1) body motion.

    Rota special başında segment + bezier footprint testlerinden zaten geçer.
    Static dünya special boyunca değişmediği için aynı path'i her frame 3 px alt
    adımlarla yeniden taramak gereksizdir. Seyrek sanity check yalnız beklenmedik
    runtime değişikliğinde eski güvenli resolver'a geri döner.
    """
    global oyuncu_x, oyuncu_y, v37_special_last_static_sanity_ms
    desired = pygame.Vector2(desired)
    if not math.isfinite(desired.x) or not math.isfinite(desired.y):
        return pygame.Vector2(float(oyuncu_x), float(oyuncu_y))

    desired.x = max(
        V34_PLAYER_SAFE_MARGIN_X,
        min(
            HARITA_GENISLIK - V34_PLAYER_SAFE_MARGIN_X,
            desired.x,
        ),
    )
    desired.y = max(
        V34_PLAYER_SAFE_MARGIN_TOP,
        min(
            HARITA_YUKSEKLIK - V34_PLAYER_SAFE_MARGIN_BOTTOM,
            desired.y,
        ),
    )

    now = pygame.time.get_ticks()
    if (
        not v34_special_path_valid
        or now - v37_special_last_static_sanity_ms >= V37_SPECIAL_STATIC_SANITY_MS
    ):
        v37_special_last_static_sanity_ms = now
        if not _v34_static_position_valid(desired.x, desired.y):
            return _v37_special_scripted_position_apply_slow(desired, previous)

    oyuncu_x = float(desired.x)
    oyuncu_y = float(desired.y)
    return desired.copy()
# </POTBO_STAGE S0919>

# <POTBO_STAGE S0921>


def gelistirici_x_skill_efekt_ciz():
    """Tek lokal layer: body trail + iki slash + impact + minimal sparks.

    Afterimage karakter siluetleri, ayrı echo surface'leri, landing parçacıkları ve
    ikinci master VFX compositor kaldırıldı. Şiddet; hızlı beden rotası, üç gerçek hit,
    ses, kamera punch ve yüksek kontrastlı slash çekirdeğinden gelir.
    """
    now = pygame.time.get_ticks()
    active = gelistirici_x_skill_aktif_mi(now)
    visible = (
        active or now < int(gelistirici_x_skill_iz_bitis) or bool(v34f_special_sparks)
    )
    if not visible or len(gelistirici_x_skill_yol) < 6:
        return

    center_world = v34_special_effect_center or v34f_special_last_center
    if center_world is None:
        center_world = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    center_world = pygame.Vector2(center_world)
    center_screen = pygame.Vector2(
        dunya_ekran_x(center_world.x),
        dunya_ekran_y(center_world.y - 12.0),
    )
    layer_w, layer_h = V37_SPECIAL_LAYER_SIZE
    rect = pygame.Rect(
        int(center_screen.x - layer_w * 0.5),
        int(center_screen.y - layer_h * 0.5),
        layer_w,
        layer_h,
    )
    if not rect.colliderect(ekran.get_rect()):
        return
    layer = v37_special_layer
    layer.fill((0, 0, 0, 0))


    items = list(v34_special_trail)
    alive_trail = []
    for item in items:
        if now - int(item[0]) <= V37_SPECIAL_TRAIL_LIFE_MS:
            alive_trail.append(item)
    v34_special_trail.clear()
    v34_special_trail.extend(alive_trail)
    for i in range(1, len(alive_trail)):
        t1, a, _ = alive_trail[i - 1]
        t2, b, phase = alive_trail[i]
        age = now - int(t2)
        fade = max(0.0, 1.0 - age / max(1.0, V37_SPECIAL_TRAIL_LIFE_MS))
        sa = _v36_screen_local(pygame.Vector2(a), rect, -9.0)
        sb = _v36_screen_local(pygame.Vector2(b), rect, -9.0)
        width = 5 if "slash" in str(phase) else 3
        pygame.draw.line(layer, (150, 8, 30, int(92 * fade)), sa, sb, width)
        pygame.draw.line(layer, (246, 225, 230, int(118 * fade)), sa, sb, 1)

    _, _, p1, p2, p3, p4 = [pygame.Vector2(v) for v in gelistirici_x_skill_yol]
    prog1 = _v36_special_phase_progress(now, "setup_end", "slash1_end")
    prog2 = _v36_special_phase_progress(now, "switch_end", "slash2_end")

    def draw_slash(a, b, progress, final=False):
        if progress <= 0.0:
            return
        sa = _v36_screen_local(a, rect, -12.0)
        sb = _v36_screen_local(b, rect, -12.0)
        end = sa.lerp(sb, progress)

        pygame.draw.line(layer, (88, 0, 14, 155), sa, end, 9 if final else 7)
        pygame.draw.line(
            layer,
            (226, 22, 48, 220),
            sa,
            end,
            4 if final else 3,
        )
        pygame.draw.line(layer, (255, 244, 247, 245), sa, end, 1)

    draw_slash(p1, p2, prog1, False)
    draw_slash(p3, p4, prog2, True)


    if now < v34_special_impact_ring_until:
        duration = max(
            1,
            v34_special_impact_ring_until - v34_special_impact_ring_started,
        )
        q = max(
            0.0,
            min(
                1.0,
                (now - v34_special_impact_ring_started) / duration,
            ),
        )
        c = _v36_screen_local(center_world, rect, -13.0)
        rr = int(8 + 38 * (1.0 - (1.0 - q) ** 3))
        aa = int(138 * (1.0 - q))
        pygame.draw.circle(
            layer,
            (250, 235, 239, aa),
            (int(c.x), int(c.y)),
            rr,
            2,
        )

    _v37_draw_special_sparks(layer, rect, now)


    if v34_special_hit_display_index == 3 and now < v34_special_hit_display_until:
        age = 520 - max(0, v34_special_hit_display_until - now)
        if 0 <= age <= V37_SPECIAL_AFTERGLOW_MS:
            q = age / max(1.0, float(V37_SPECIAL_AFTERGLOW_MS))
            aa = int(145 * (1.0 - q) ** 1.5)
            c = pygame.Vector2(center_world)
            r = float(v34_special_effect_radius) * (0.66 + 0.08 * q)
            h = r * 0.78
            for a, b in (
                (
                    c + pygame.Vector2(-r, +h),
                    c + pygame.Vector2(+r, -h),
                ),
                (
                    c + pygame.Vector2(-r, -h),
                    c + pygame.Vector2(+r, +h),
                ),
            ):
                sa = _v36_screen_local(a, rect, -12.0)
                sb = _v36_screen_local(b, rect, -12.0)
                pygame.draw.line(layer, (216, 18, 44, aa), sa, sb, 3)
                pygame.draw.line(
                    layer,
                    (255, 245, 248, min(220, aa + 45)),
                    sa,
                    sb,
                    1,
                )

    ekran.blit(layer, rect.topleft)
    _v34_special_hit_counter_ciz(now)
# </POTBO_STAGE S0921>

# <POTBO_STAGE S0926>


_v37_dunya_simulasyon_guncelle_original = dunya_simulasyon_guncelle


def dunya_simulasyon_guncelle():
    global dunya_son_guncelleme, dunya_onceki_konum
    if gelistirici_x_skill_aktif_mi():

        dunya_son_guncelleme = pygame.time.get_ticks()
        dunya_onceki_konum = (oyuncu_x, oyuncu_y)
        return
    return _v37_dunya_simulasyon_guncelle_original()
# </POTBO_STAGE S0926>

# <POTBO_STAGE S0946>
V38_FIRE_PROJECTILE_COLLISION_STEP = 7.0
# </POTBO_STAGE S0946>

# <POTBO_STAGE S0961>


def _v38_exposure_fraction(center, target_pos, target_radius):
    """Üç ince ray ile duvar gölgelemesi.

    Tek binary LOS, büyük hedefin yarısı duvar arkasındayken ya %0 ya %100 sonucu
    veriyordu. Merkez + iki tangent sample, yalnız patlama anında çalıştığı için ucuzdur.
    """
    c = pygame.Vector2(center)
    p = pygame.Vector2(target_pos)
    d = p - c
    if d.length_squared() <= 1e-8:
        return 1.0
    n = pygame.Vector2(-d.y, d.x).normalize()
    offset = min(12.0, max(3.0, float(target_radius) * 0.45))
    samples = (p, p + n * offset, p - n * offset)
    clear = sum(1 for s in samples if _ince_dunya_los_acik_mi(c, s, 7.0))
    if clear <= 0:
        return 0.0
    return clear / float(len(samples))
# </POTBO_STAGE S0961>

# <POTBO_STAGE S0974>





def _v38_fire_projectile_init(self, x, y, direction, simdi):
    self.x = float(x)
    self.y = float(y)
    self.start = pygame.Vector2(x, y)
    self.direction = pygame.Vector2(direction)
    if self.direction.length_squared() <= 1e-8:
        self.direction = pygame.Vector2(1.0, 0.0)
    self.direction = self.direction.normalize()
    self.start_ms = int(simdi)
    self.active = True
    self.anim_epoch = int(simdi)
    self.travelled = 0.0
    self.speed = float(V38_FIRE_PROJECTILE_V0)
    self.temperature_k = float(V38_FIRE_CORE_TEMPERATURE_K)
    self.reaction_progress = 1.0
    self.v = self.direction * self.speed
    self.is_player_magic = True
# </POTBO_STAGE S0974>

# <POTBO_STAGE S0987>
V34F_SPECIAL_CAMERA_PUNCH = (2.15, 3.30, 5.10)
V34F_SPECIAL_CAMERA_PUNCH_MS = (64, 78, 104)
# </POTBO_STAGE S0987>

# <POTBO_STAGE S0996>


def _gelistirici_x_skill_vur(slot, yon=None):
    """Hit başarıyla commit olduğu karede stamina bir kez düşer: 18 + 18 + 18."""
    before_mask = int(gelistirici_x_skill_vurus_maskesi)
    ok = _v38_special_hit_original(slot, yon)
    if not ok:
        return False
    slot = max(0, min(2, int(slot)))
    bit = 1 << slot

    if not (before_mask & bit):
        paid = _v38_special_pay_hit(slot, pygame.time.get_ticks())
        dunya_olayi_kaydet(
            "developer_x_special_stamina",
            index=slot + 1,
            spent=round(float(paid), 2),
            total_spent=round(float(v38_special_stamina_spent), 2),
        )
    return True
# </POTBO_STAGE S0996>

# <POTBO_STAGE S0998>








_v38_special_hit_feedback_original = _v34_special_hit_feedback
# </POTBO_STAGE S0998>

# <POTBO_STAGE S1023>








V38_TUNING_LIMITS = {
    "V38_FIRE_CORE_TEMPERATURE_K": {
        "min": 1200.0,
        "max": 2600.0,
        "unit": "K",
        "role": "visual core temperature",
    },
    "V38_FIRE_THERMAL_COOLING_K": {
        "min": 0.05,
        "max": 1.50,
        "unit": "1/s",
        "role": "projectile thermal exponential decay",
    },
    "V38_FIRE_PROJECTILE_V0": {
        "min": 450.0,
        "max": 1300.0,
        "unit": "world_px/s",
        "role": "initial projectile speed",
    },
    "V38_FIRE_PROJECTILE_VINF": {
        "min": 300.0,
        "max": 1150.0,
        "unit": "world_px/s",
        "role": "confinement terminal-like speed",
    },
    "V38_FIRE_PROJECTILE_DRAG_K": {
        "min": 0.05,
        "max": 4.00,
        "unit": "1/s",
        "role": "velocity exponential decay",
    },
    "V38_FIRE_PROJECTILE_MAX_TRAVEL": {
        "min": 480.0,
        "max": 1700.0,
        "unit": "world_px",
        "role": "hard safety range",
    },
    "V38_FIRE_PROJECTILE_TTL_MS": {
        "min": 700.0,
        "max": 3200.0,
        "unit": "ms",
        "role": "hard safety lifetime",
    },
    "V38_FIRE_PROJECTILE_RADIUS": {
        "min": 8.0,
        "max": 28.0,
        "unit": "world_px",
        "role": "physical collision sphere radius",
    },
    "V38_FIRE_PRESSURE_SIGMA": {
        "min": 35.0,
        "max": 110.0,
        "unit": "world_px",
        "role": "Gaussian blast pressure width",
    },
    "V38_FIRE_THERMAL_R50": {
        "min": 55.0,
        "max": 160.0,
        "unit": "world_px",
        "role": "50 percent thermal exposure radius",
    },
    "V38_FIRE_DAMAGE_PRESSURE": {
        "min": 120.0,
        "max": 850.0,
        "unit": "hp_model",
        "role": "pressure damage coefficient",
    },
    "V38_FIRE_DAMAGE_THERMAL": {
        "min": 40.0,
        "max": 320.0,
        "unit": "hp_model",
        "role": "thermal direct-damage coefficient",
    },
    "V38_FIRE_DAMAGE_RADIUS": {
        "min": 100.0,
        "max": 300.0,
        "unit": "world_px",
        "role": "enemy direct damage cutoff",
    },
    "V38_FIRE_THERMAL_RADIUS": {
        "min": 90.0,
        "max": 260.0,
        "unit": "world_px",
        "role": "burn dose cutoff",
    },
    "V38_FIRE_KNOCKBACK_BASE": {
        "min": 250.0,
        "max": 1500.0,
        "unit": "world_px/s",
        "role": "core impulse coefficient",
    },
    "V38_FIRE_BURN_BASE": {
        "min": 20.0,
        "max": 220.0,
        "unit": "hp_total",
        "role": "maximum burn dose",
    },
    "V38_FIRE_SELF_DAMAGE_RADIUS": {
        "min": 50.0,
        "max": 160.0,
        "unit": "world_px",
        "role": "owner direct damage cutoff",
    },
    "V38_FIRE_SELF_DAMAGE_SCALE": {
        "min": 0.05,
        "max": 0.65,
        "unit": "ratio",
        "role": "owner versus enemy direct damage scale",
    },
    "V38_FIRE_SELF_DAMAGE_MAX_HP_FRACTION": {
        "min": 0.15,
        "max": 0.90,
        "unit": "ratio",
        "role": "single self-detonation hp cap",
    },
    "V38_FIRE_SELF_BURN_RADIUS": {
        "min": 30.0,
        "max": 130.0,
        "unit": "world_px",
        "role": "owner burn cutoff",
    },
    "V38_FIRE_CAST_STAMINA_COST": {
        "min": 0.0,
        "max": 35.0,
        "unit": "stamina",
        "role": "normal spell physical commitment cost",
    },
    "V38_PLAYER_NORMAL_REACH_STRICT": {
        "min": 28.0,
        "max": 58.0,
        "unit": "world_px",
        "role": "strict player normal broad-phase reach",
    },
    "V38_PLAYER_HEAVY_REACH_STRICT": {
        "min": 38.0,
        "max": 82.0,
        "unit": "world_px",
        "role": "strict player heavy local reach",
    },
    "GELISTIRICI_X_SKILL_SURE_MS": {
        "min": 980.0,
        "max": 1900.0,
        "unit": "ms",
        "role": "complete authored special lock duration",
    },
    "V38_SPECIAL_STAMINA_PER_HIT": {
        "min": 8.0,
        "max": 28.0,
        "unit": "stamina",
        "role": "each physical special dash-hit cost",
    },
}
# </POTBO_STAGE S1023>

# <POTBO_STAGE S1109>










V43_VERSION = "43.0"
# </POTBO_STAGE S1109>

# <POTBO_STAGE S1113>





V43_CAMERA_BASE_ZOOM = 1.12
V43_CAMERA_ZOOM_STEPS = (
    1.12,
    1.50,
    2.00,
    3.00,
    4.00,
    5.00,
    6.00,
)
V43_CAMERA_ZOOM_MAX = 6.0
# </POTBO_STAGE S1113>

# <POTBO_STAGE S1115>


def _v43_camera_recenter():
    global kamera_x, kamera_y
    visible_w = GENISLIK / max(0.01, float(KAMERA_YAKINLASTIRMA))
    visible_h = YUKSEKLIK / max(0.01, float(KAMERA_YAKINLASTIRMA))
    target_x = float(oyuncu_x) - visible_w * 0.50
    target_y = float(oyuncu_y) - visible_h * 0.58
    kamera_x = max(
        0.0,
        min(max(0.0, HARITA_GENISLIK - visible_w), target_x),
    )
    kamera_y = max(
        0.0,
        min(max(0.0, HARITA_YUKSEKLIK - visible_h), target_y),
    )
# </POTBO_STAGE S1115>

# <POTBO_STAGE S1118>


def gelistirici_test_girdisi_uygula(olay):
    if (
        GELISTIRICI_MODU
        and olay.type == pygame.KEYDOWN
        and (olay.mod & pygame.KMOD_CTRL)
        and olay.key == pygame.K_1
    ):
        v43_camera_zoom_cycle()
        return True
    return _v43_dev_input_original(olay)


def _v43_map_draw():
    """6x zoom'da bütün haritayı 6x Surface'e çevirmeden yalnız görünen parçayı büyütür."""
    global v43_map_zoom_buffer, v43_map_zoom_buffer_size
    if cave1_haritasi is None:
        ekran.fill((95, 75, 60))
        return

    zoom = max(0.01, float(KAMERA_YAKINLASTIRMA))
    if abs(zoom - V43_CAMERA_BASE_ZOOM) < 0.001 and harita_yakin_resmi is not None:
        ekran.blit(
            harita_yakin_resmi,
            (
                -int(round(kamera_x * zoom)),
                -int(round(kamera_y * zoom)),
            ),
        )
        return

    visible_w = GENISLIK / zoom
    visible_h = YUKSEKLIK / zoom
    src_w = min(HARITA_GENISLIK, max(2, int(math.ceil(visible_w)) + 2))
    src_h = min(HARITA_YUKSEKLIK, max(2, int(math.ceil(visible_h)) + 2))
    src_x = int(math.floor(float(kamera_x)))
    src_y = int(math.floor(float(kamera_y)))
    src_x = max(0, min(max(0, HARITA_GENISLIK - src_w), src_x))
    src_y = max(0, min(max(0, HARITA_YUKSEKLIK - src_h), src_y))
    source = cave1_haritasi.subsurface(pygame.Rect(src_x, src_y, src_w, src_h))

    target_size = (
        max(GENISLIK, int(round(src_w * zoom))),
        max(YUKSEKLIK, int(round(src_h * zoom))),
    )
    if v43_map_zoom_buffer is None or v43_map_zoom_buffer_size != target_size:
        v43_map_zoom_buffer = pygame.Surface(target_size).convert()
        v43_map_zoom_buffer_size = target_size

    pygame.transform.scale(source, target_size, v43_map_zoom_buffer)
    offset_x = int(round((src_x - float(kamera_x)) * zoom))
    offset_y = int(round((src_y - float(kamera_y)) * zoom))
    ekran.blit(v43_map_zoom_buffer, (offset_x, offset_y))
# </POTBO_STAGE S1118>

# <POTBO_STAGE S1120>




_v33_oyun_ekrani_ciz = _v43_base_world_renderer
# </POTBO_STAGE S1120>

# <POTBO_STAGE S1202>


def v47_hit_confirm_ciz():
    now = pygame.time.get_ticks()
    elapsed = now - int(v47_last_confirm_ms)
    duration = V47_HEAVY_CONFIRM_MS if v47_last_confirm_heavy else V47_HIT_CONFIRM_MS
    if elapsed < 0 or elapsed >= duration:
        return
    t = v44_clamp01(elapsed / max(1.0, duration))
    alpha = int(190 * (1.0 - v44_smoothstep(t)))
    radius = (
        V47_HEAVY_RING_RADIUS if v47_last_confirm_heavy else V47_HIT_RING_RADIUS
    ) * (0.74 + 0.58 * v44_smoothstep(t))
    sx = dunya_ekran_x(v47_last_confirm_pos.x)
    sy = dunya_ekran_y(v47_last_confirm_pos.y)
    rr = max(4, int(round(radius * KAMERA_YAKINLASTIRMA)))
    surf = pygame.Surface((rr * 2 + 8, rr * 2 + 8), pygame.SRCALPHA)
    color = (
        (245, 235, 232, alpha)
        if v47_last_confirm_quality >= 1.08
        else (178, 78, 88, alpha)
    )
    pygame.draw.ellipse(surf, color, pygame.Rect(4, rr // 2 + 2, rr * 2, rr), 1)
    if v47_last_confirm_heavy:
        pygame.draw.line(
            surf,
            color,
            (rr // 2, rr + 4),
            (rr * 3 // 2, rr - 2),
            1,
        )
    ekran.blit(surf, surf.get_rect(center=(int(sx), int(sy))))
# </POTBO_STAGE S1202>

# <POTBO_STAGE S1204>



_v47_base_world_renderer_original = _v33_oyun_ekrani_ciz


def _v47_base_world_renderer():
    _v47_base_world_renderer_original()
    if oyuncu_hp > 0:
        v47_hit_confirm_ciz()
    v47_combat_telemetry_ciz()


_v33_oyun_ekrani_ciz = _v47_base_world_renderer
# </POTBO_STAGE S1204>

# <POTBO_STAGE S1234>


def v51_parry_feedback(source_x, source_y, class_name, quality):
    incoming = pygame.Vector2(oyuncu_x - float(source_x), oyuncu_y - float(source_y))
    if incoming.length_squared() <= 1e-6:
        incoming = v44_player_facing_vector()
    power = 1.30 + 0.70 * quality
    combat_impact_spawn(
        oyuncu_x,
        oyuncu_y - 12.0,
        "slash_heavy" if class_name == "heavy" else "slash",
        power,
        incoming,
    )
    kamera_hit_sarsintisi_baslat(3.0 + 2.7 * quality, 100 + int(58 * quality))
# </POTBO_STAGE S1234>

# <POTBO_STAGE S1237>


def v51_blade_tip_world():
    reach = v45_attack_reach_current()
    direction = v44_player_facing_vector()
    root = pygame.Vector2(float(oyuncu_x), float(oyuncu_y - 18.0))
    return root + direction * reach


def v51_blade_root_world():
    direction = v44_player_facing_vector()
    root = pygame.Vector2(float(oyuncu_x), float(oyuncu_y - 18.0))
    return root + direction * 5.0


def v51_blade_trail_sample():
    now = pygame.time.get_ticks()
    if not oyuncu_saldiriyor:
        return
    if not oyuncu_saldiri_vurus_penceresi_aktif_mi(now):
        return
    speed = v44_attack_speed_estimate()
    if speed < V51_BLADE_TRAIL_MIN_SPEED:
        return
    root = v51_blade_root_world()
    tip = v51_blade_tip_world()

    tangent = v44_player_facing_vector().rotate(90.0)
    phase = math.sin(now * 0.018)
    root += tangent * phase * 2.2
    tip += tangent * phase * (5.0 if oyuncu_saldiri_modu == "hold_release" else 3.2)
    v51_blade_trails.append(
        {
            "ms": now,
            "root": pygame.Vector2(root),
            "tip": pygame.Vector2(tip),
            "heavy": str(oyuncu_saldiri_modu) == "hold_release",
            "speed": speed,
        }
    )
# </POTBO_STAGE S1237>

# <POTBO_STAGE S1239>


def v51_blade_trail_ciz():
    now = pygame.time.get_ticks()
    v51_blade_trails_prune(now)
    if not v51_blade_trails:
        return
    for item in list(v51_blade_trails):
        age = now - int(item["ms"])
        t = v44_clamp01(age / max(1.0, V51_BLADE_TRAIL_LIFE_MS))
        alpha0 = V51_BLADE_TRAIL_HEAVY_ALPHA if item["heavy"] else V51_BLADE_TRAIL_ALPHA
        alpha = int(alpha0 * (1.0 - v44_smoothstep(t)))
        if alpha <= 2:
            continue
        root = item["root"]
        tip = item["tip"]
        p0 = (
            int(dunya_ekran_x(root.x)),
            int(dunya_ekran_y(root.y)),
        )
        p1 = (
            int(dunya_ekran_x(tip.x)),
            int(dunya_ekran_y(tip.y)),
        )
        min_x = min(p0[0], p1[0]) - 6
        min_y = min(p0[1], p1[1]) - 6
        max_x = max(p0[0], p1[0]) + 6
        max_y = max(p0[1], p1[1]) + 6
        surf = pygame.Surface(
            (max(2, max_x - min_x), max(2, max_y - min_y)),
            pygame.SRCALPHA,
        )
        q0 = (p0[0] - min_x, p0[1] - min_y)
        q1 = (p1[0] - min_x, p1[1] - min_y)
        pygame.draw.line(surf, (246, 236, 232, alpha), q0, q1, 1)
        if item["heavy"]:
            offset = pygame.Vector2(q1) - pygame.Vector2(q0)
            if offset.length_squared() > 0.1:
                normal = offset.normalize().rotate(90.0) * 1.5
                pygame.draw.line(
                    surf,
                    (123, 24, 34, max(0, alpha // 2)),
                    (
                        int(q0[0] + normal.x),
                        int(q0[1] + normal.y),
                    ),
                    (
                        int(q1[0] + normal.x),
                        int(q1[1] + normal.y),
                    ),
                    1,
                )
        ekran.blit(surf, (min_x, min_y))


def v51_hitbox_debug_ciz():
    if not GELISTIRICI_MODU or not v51_hitbox_debug:
        return
    rect = oyuncu_saldiri_vurus_rect()
    screen_rect = pygame.Rect(
        int(dunya_ekran_x(rect.x)),
        int(dunya_ekran_y(rect.y)),
        max(1, int(rect.width * KAMERA_YAKINLASTIRMA)),
        max(1, int(rect.height * KAMERA_YAKINLASTIRMA)),
    )
    surf = pygame.Surface(screen_rect.size, pygame.SRCALPHA)
    surf.fill((214, 32, 56, V51_HITBOX_DEBUG_ALPHA))
    pygame.draw.rect(surf, (255, 226, 226, 180), surf.get_rect(), 1)
    ekran.blit(surf, screen_rect)


_v51_world_renderer_original = _v33_oyun_ekrani_ciz


def _v51_world_renderer():
    v51_blade_trail_sample()
    _v51_world_renderer_original()
    v51_blade_trail_ciz()
    v51_hitbox_debug_ciz()


_v33_oyun_ekrani_ciz = _v51_world_renderer
# </POTBO_STAGE S1239>

# <POTBO_STAGE S1258>


_v52_world_renderer_original = _v33_oyun_ekrani_ciz


def _v52_world_renderer():
    _v52_world_renderer_original()
    v52_skill_strip_ciz()


_v33_oyun_ekrani_ciz = _v52_world_renderer
# </POTBO_STAGE S1258>

# <POTBO_STAGE S1269>


def v53_surface_rgb(x, y):
    if cave1_haritasi is None:
        return None
    try:
        ix = max(
            0,
            min(
                cave1_haritasi.get_width() - 1,
                int(round(float(x))),
            ),
        )
        iy = max(
            0,
            min(
                cave1_haritasi.get_height() - 1,
                int(round(float(y))),
            ),
        )
        color = cave1_haritasi.get_at((ix, iy))
        return (int(color.r), int(color.g), int(color.b))
    except Exception:
        return None
# </POTBO_STAGE S1269>

# <POTBO_STAGE S1297>


def v55_pool_ciz():
    now = pygame.time.get_ticks()
    clusters = v55_pool_scan(now)
    for cluster in clusters:
        wet = float(cluster["wet"])
        if wet <= 0.02:
            continue
        sx = dunya_ekran_x(cluster["x"])
        sy = dunya_ekran_y(cluster["y"])
        if sx < -80 or sx > GENISLIK + 80 or sy < -80 or sy > YUKSEKLIK + 80:
            continue
        radius = (
            v44_clamp(
                math.sqrt(float(cluster["mass"])) * 3.4,
                6.0,
                24.0,
            )
            * KAMERA_YAKINLASTIRMA
        )
        rx = max(4, int(radius * 1.34))
        ry = max(3, int(radius * 0.62))
        surf = pygame.Surface((rx * 2 + 6, ry * 2 + 6), pygame.SRCALPHA)
        alpha = int(V55_POOL_ALPHA * wet)
        pygame.draw.ellipse(
            surf,
            (38, 1, 5, alpha),
            pygame.Rect(3, 3, rx * 2, ry * 2),
        )
        if wet > 0.45 and cluster["surface"] in (
            "stone",
            "wood",
            "unknown",
        ):
            glint_alpha = int(V55_POOL_GLOSS_ALPHA * wet)
            pygame.draw.line(
                surf,
                (250, 244, 240, glint_alpha),
                (max(4, rx // 2), max(3, ry // 2)),
                (
                    min(rx * 2, rx + rx // 2),
                    max(3, ry // 2 - 1),
                ),
                1,
            )
        ekran.blit(surf, surf.get_rect(center=(int(sx), int(sy))))


_v55_world_sim_original = dunya_simulasyon_guncelle
# </POTBO_STAGE S1297>

# <POTBO_STAGE S1299>


_v55_world_renderer_original = _v33_oyun_ekrani_ciz


def _v55_world_renderer():
    _v55_world_renderer_original()
    v55_pool_ciz()


_v33_oyun_ekrani_ciz = _v55_world_renderer
# </POTBO_STAGE S1299>

# <POTBO_STAGE S1327>


def v57_attack_active():
    return bool(oyuncu_saldiriyor and oyun_durumu == OYUN and oyun_alt_durumu == HARITA)
# </POTBO_STAGE S1327>

# <POTBO_STAGE S1338>


_v57_world_update_original = dunya_simulasyon_guncelle


def dunya_simulasyon_guncelle():
    result = _v57_world_update_original()
    v57_update()
    return result
# </POTBO_STAGE S1338>

# <POTBO_STAGE S1349>


def v58_world_visible(x, y, margin=90.0):
    left = float(kamera_x) - margin
    top = float(kamera_y) - margin
    right = float(kamera_x) + GENISLIK / max(0.01, KAMERA_YAKINLASTIRMA) + margin
    bottom = float(kamera_y) + YUKSEKLIK / max(0.01, KAMERA_YAKINLASTIRMA) + margin
    return left <= float(x) <= right and top <= float(y) <= bottom
# </POTBO_STAGE S1349>

# <POTBO_STAGE S1399>


_v61_world_update_original = dunya_simulasyon_guncelle


def dunya_simulasyon_guncelle():
    result = _v61_world_update_original()
    v61_cleanup()
    return result


def v61_reaction_debug_ciz():
    if not (GELISTIRICI_MODU and v45_combat_telemetry_enabled):
        return
    now = pygame.time.get_ticks()
    for enemy in common_enemies:
        if not getattr(enemy, "active", False):
            continue
        state = v61_reactions.get(str(getattr(enemy, "uid", "")))
        if not state or now > int(state.get("until", 0)):
            continue
        sx = dunya_ekran_x(float(enemy.x))
        sy = dunya_ekran_y(float(enemy.y) - 34.0)
        label = f"{state['kind']} d{state['depth']:.2f} i{state['impulse']:.2f}"
        text = mini_font.render(label, True, (234, 221, 224))
        bg = pygame.Surface(
            (text.get_width() + 8, text.get_height() + 4),
            pygame.SRCALPHA,
        )
        bg.fill((4, 3, 5, 178))
        bg.blit(text, (4, 2))
        ekran.blit(bg, (sx - bg.get_width() // 2, sy))
# </POTBO_STAGE S1399>

# <POTBO_STAGE S1411>




def _v63_lobe_draw(self, surface, silhouette=False):
    if not self.alive or not v58_world_visible(self.origin.x, self.origin.y):
        return
    now = pygame.time.get_ticks()
    t = v58_clamp01((now - self.created_ms) / max(1.0, float(self.life_ms)))
    grow = 0.65 + 0.55 * (1.0 - (1.0 - t) ** 3)
    alpha = int(170 * (1.0 - t) ** 1.3)
    if alpha <= 3:
        return
    center = pygame.Vector2(
        dunya_ekran_x(self.origin.x),
        dunya_ekran_y(self.origin.y),
    )
    world_points = []
    for i, jag in enumerate(self.jagged):
        frac = i / max(1, len(self.jagged) - 1)
        angle = self.rotation + (-0.78 + frac * 1.56)
        forward = 1.0 + 0.65 * math.cos(angle - self.rotation)
        radius = self.radius * jag * forward * grow * KAMERA_YAKINLASTIRMA
        p = center + pygame.Vector2(math.cos(angle), math.sin(angle)) * radius
        world_points.append((int(p.x), int(p.y)))
    world_points.append((int(center.x), int(center.y)))
    min_x = min(p[0] for p in world_points) - 3
    min_y = min(p[1] for p in world_points) - 3
    max_x = max(p[0] for p in world_points) + 3
    max_y = max(p[1] for p in world_points) + 3
    if max_x < 0 or min_x > GENISLIK or max_y < 0 or min_y > YUKSEKLIK:
        return
    width = max(4, max_x - min_x + 1)
    height = max(4, max_y - min_y + 1)
    layer = pygame.Surface((width, height), pygame.SRCALPHA)
    points = [(x - min_x, y - min_y) for x, y in world_points]
    color = (4, 3, 4, min(alpha, 110)) if silhouette else (*self.color, alpha)
    pygame.draw.polygon(layer, color, points)
    if not silhouette and self.arterial and alpha > 90 and len(points) >= 5:
        pygame.draw.line(
            layer,
            (244, 238, 238, min(120, alpha)),
            points[3],
            points[5],
            1,
        )
    surface.blit(layer, (min_x, min_y))
# </POTBO_STAGE S1411>

# <POTBO_STAGE S1413>


_v63_world_update_original = dunya_simulasyon_guncelle


def dunya_simulasyon_guncelle():
    result = _v63_world_update_original()
    v63_update_budget()
    return result
# </POTBO_STAGE S1413>

# <POTBO_STAGE S1424>


_v66_world_update_original = dunya_simulasyon_guncelle


def dunya_simulasyon_guncelle():
    result = _v66_world_update_original()
    v66_runtime_audit(False)
    return result
# </POTBO_STAGE S1424>

# <POTBO_STAGE S1429>


def v67_sample_tip(now=None):
    global \
        v67_last_attack_id, \
        v67_last_measured_speed, \
        v67_last_tangent, \
        v67_last_curvature, \
        v67_last_arc_length
    if now is None:
        now = pygame.time.get_ticks()
    if not oyuncu_saldiriyor:
        if v67_tip_history and int(now) - int(v67_tip_history[-1][0]) > 120:
            v67_clear_trajectory()
        return

    attack_id = int(globals().get("saldiri_baslangic", -1))
    if attack_id != v67_last_attack_id:
        v67_last_attack_id = attack_id
        v67_clear_trajectory()
    tip = pygame.Vector2(v51_blade_tip_world())
    if v67_tip_history:
        last_ms, last_tip = v67_tip_history[-1]
        delta_ms = int(now) - int(last_ms)
        if delta_ms < V67_SAMPLE_MIN_MS:
            return
        if delta_ms > V67_SAMPLE_MAX_MS:
            v67_tip_history.clear()
        else:
            delta = tip - last_tip
            distance = delta.length()
            if distance > 0.001:
                speed = distance / max(0.001, delta_ms / 1000.0)
                speed = v44_clamp(speed, V67_SPEED_MIN, V67_SPEED_MAX)
                if v67_last_measured_speed <= 0.0:
                    v67_last_measured_speed = speed
                else:
                    v67_last_measured_speed += (speed - v67_last_measured_speed) * 0.48
                v67_last_tangent = delta.normalize()
                v67_last_arc_length += distance
    v67_tip_history.append((int(now), tip))

    if len(v67_tip_history) >= V67_CURVATURE_WINDOW:
        points = list(v67_tip_history)[-V67_CURVATURE_WINDOW:]
        vectors = []
        for idx in range(1, len(points)):
            vec = points[idx][1] - points[idx - 1][1]
            if vec.length_squared() > 1e-7:
                vectors.append(vec.normalize())
        if len(vectors) >= 2:
            angle_sum = 0.0
            for idx in range(1, len(vectors)):
                a = vectors[idx - 1]
                b = vectors[idx]
                cross = a.x * b.y - a.y * b.x
                dot = max(-1.0, min(1.0, a.dot(b)))
                angle_sum += math.atan2(cross, dot)
            v67_last_curvature = angle_sum / max(1, len(vectors) - 1)
# </POTBO_STAGE S1429>

# <POTBO_STAGE S1433>


_v67_world_update_original = dunya_simulasyon_guncelle


def dunya_simulasyon_guncelle():
    result = _v67_world_update_original()
    v67_sample_tip()
    return result
# </POTBO_STAGE S1433>

# <POTBO_STAGE S1447>


def v69_debug_trajectory_ciz():
    if not (GELISTIRICI_MODU and v51_hitbox_debug and oyuncu_saldiriyor):
        return
    if len(v67_tip_history) < 2:
        return
    points = []
    now = pygame.time.get_ticks()
    samples = list(v67_tip_history)
    for ms, point in samples:
        age = max(0, now - int(ms))
        alpha = max(
            35,
            int(V69_TRAJECTORY_ALPHA * (1.0 - min(1.0, age / 260.0))),
        )
        points.append(
            (
                dunya_ekran_x(point.x),
                dunya_ekran_y(point.y),
                alpha,
            )
        )
    if len(points) < 2:
        return
    layer = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    for idx in range(1, len(points)):
        x0, y0, a0 = points[idx - 1]
        x1, y1, a1 = points[idx]
        alpha = min(a0, a1)
        pygame.draw.line(layer, (246, 228, 231, alpha), (x0, y0), (x1, y1), 1)

    last = pygame.Vector2(points[-1][0], points[-1][1])
    tangent = v67_measured_direction() * 30.0 * KAMERA_YAKINLASTIRMA
    pygame.draw.line(layer, (245, 204, 63, 180), last, last + tangent, 1)
    ekran.blit(layer, (0, 0))


def v69_debug_reach_label_ciz():
    if not (GELISTIRICI_MODU and v51_hitbox_debug):
        return
    nr, nw, hr, hw = _v38_player_reach_values()
    active_reach = hr if oyuncu_saldiri_modu == "hold_release" else nr
    active_width = hw if oyuncu_saldiri_modu == "hold_release" else nw
    sx = dunya_ekran_x(oyuncu_x)
    sy = dunya_ekran_y(oyuncu_y - 45.0)
    label = (
        f"reach {active_reach}px  width {active_width}px  +{V44_SWORD_REACH_BONUS_PX}px"
    )
    text = mini_font.render(label, True, (246, 225, 228))
    bg = pygame.Surface(
        (text.get_width() + 10, text.get_height() + 6),
        pygame.SRCALPHA,
    )
    bg.fill((5, 3, 6, 190))
    pygame.draw.rect(bg, (112, 38, 49, 190), bg.get_rect(), 1)
    bg.blit(text, (5, 3))
    ekran.blit(bg, (sx - bg.get_width() // 2, sy - bg.get_height()))
# </POTBO_STAGE S1447>

# <POTBO_STAGE S1483>
V74_COLLISION_BACKTRACE_STEP_PX = 2.0
# </POTBO_STAGE S1483>

# <POTBO_STAGE S1485>
v74_death_camera_anchor = None
v74_stats = {
    "particle_landings": 0,
    "collision_backtracks": 0,
    "forced_air_expiry_landings": 0,
    "mist_landings": 0,
    "filament_landings": 0,
    "lobe_landings": 0,
}


def v74_floor_clean(x, y):
    x = float(x)
    y = float(y)
    return (
        0.0 <= x < float(HARITA_GENISLIK)
        and 0.0 <= y < float(HARITA_YUKSEKLIK)
        and not harita_pikseli_engel_mi(x, y)
    )


def v74_trace_clean_floor(end_x, end_y, direction=None, last_clean=None):
    """Collision'a kan basmadan yalnız geliş hattı üzerinde temiz zemin bulur.

    Öncelik parçacığın gerçekten geçtiği son temiz noktadır. O yoksa hız yönünün
    tersine kısa segment taraması yapılır. Yanal/radyal arama yapılmadığı için leke
    başka bir yüzeye ışınlanmaz.
    """
    end = pygame.Vector2(float(end_x), float(end_y))
    if v74_floor_clean(end.x, end.y):
        return end

    if last_clean is not None:
        try:
            candidate = pygame.Vector2(last_clean)
            if v74_floor_clean(candidate.x, candidate.y):
                v74_stats["collision_backtracks"] += 1
                return candidate
        except Exception:
            pass

    try:
        vec = pygame.Vector2(direction) if direction is not None else pygame.Vector2()
    except Exception:
        vec = pygame.Vector2()
    if vec.length_squared() <= 1e-8:
        return None
    vec = vec.normalize()
    distance = V74_COLLISION_BACKTRACE_STEP_PX
    while distance <= V74_COLLISION_BACKTRACE_PX:
        candidate = end - vec * distance
        if v74_floor_clean(candidate.x, candidate.y):
            v74_stats["collision_backtracks"] += 1
            return candidate
        distance += V74_COLLISION_BACKTRACE_STEP_PX
    return None
# </POTBO_STAGE S1485>

# <POTBO_STAGE S1487>




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
    count = max(0, int(count))
    if count <= 0:
        return 0
    base = v73_safe_direction(direction)
    origin = pygame.Vector2(float(x), float(y))
    lo_scale, hi_scale = (
        float(scale_range[0]),
        float(scale_range[1]),
    )
    lo_dist, hi_dist = (
        float(distance_range[0]),
        float(distance_range[1]),
    )
    created = 0

    for i in range(count):
        placed = False

        for attempt in range(12):
            if random.random() < float(backscatter):
                angle = random.choice((-1.0, 1.0)) * random.uniform(78.0, 154.0)
            else:
                mode = -9.0 if (i % 3) else 12.0
                angle = random.triangular(-float(cone_deg), float(cone_deg), mode)
            d = base.rotate(angle)
            r01 = random.random() ** 1.55
            dist = lo_dist + (hi_dist - lo_dist) * r01
            tangent = pygame.Vector2(-d.y, d.x)
            p = origin + d * dist + tangent * random.uniform(-1.6, 1.6)
            if not v74_floor_clean(p.x, p.y):
                continue
            size = random.uniform(lo_scale, hi_scale)
            if i == 0 and count >= 4:
                size *= random.uniform(1.08, 1.24)
            decal = v74_create_persistent_decal(p.x, p.y, size)
            if decal is not None:
                decal.v73_ground_source = str(source)
                created += 1




                if size >= 0.18 and random.random() < 0.42:
                    drip_count = 1 if random.random() < 0.68 else 2
                    tangent2 = pygame.Vector2(-d.y, d.x)
                    for _ in range(drip_count):
                        drip_pos = (
                            p
                            + d * random.uniform(0.8, 5.5)
                            + tangent2 * random.uniform(-3.0, 3.0)
                        )
                        if not v74_floor_clean(drip_pos.x, drip_pos.y):
                            continue
                        drip_scale = max(
                            0.055,
                            size * random.uniform(0.16, 0.38),
                        )
                        drip = v74_create_persistent_decal(
                            drip_pos.x, drip_pos.y, drip_scale
                        )
                        if drip is not None:
                            drip.v73_ground_source = f"{source}_drip"
                            created += 1

                placed = True
                break



        if not placed and v74_floor_clean(origin.x, origin.y):
            decal = v74_create_persistent_decal(
                origin.x,
                origin.y,
                random.uniform(lo_scale, hi_scale),
            )
            if decal is not None:
                decal.v73_ground_source = str(source)
                created += 1
    return created
# </POTBO_STAGE S1487>

# <POTBO_STAGE S1494>


def kamerayi_guncelle():
    global kamera_x, kamera_y, v74_death_camera_anchor
    if oyuncu_hp <= 0 and oyuncu_olum_baslangic_ms > 0:
        if v74_death_camera_anchor is None:
            v74_death_camera_anchor = (
                float(kamera_x),
                float(kamera_y),
            )
        kamera_x, kamera_y = v74_death_camera_anchor
        return
    v74_death_camera_anchor = None
    return _v74_camera_original()
# </POTBO_STAGE S1494>

# <POTBO_STAGE S1496>


def oyuncu_olum_sahnesini_sifirla():
    global v74_death_camera_anchor
    v74_death_camera_anchor = None
    v74_particle_primary_committed.clear()
    v74_particle_last_clean.clear()
    return _v74_death_reset_original()
# </POTBO_STAGE S1496>

# <POTBO_STAGE S1602>


def _v79_snapshot_bounds(entries, margin=26):
    if not entries:
        return pygame.Rect(0, 0, 1, 1)
    xs, ys = [], []
    for e in entries:
        xs.append(int(round(dunya_ekran_x(float(e.get("x", oyuncu_x))))))
        ys.append(int(round(dunya_ekran_y(float(e.get("y", oyuncu_y))))))
    left = max(0, min(xs) - margin)
    top = max(0, min(ys) - margin)
    right = min(GENISLIK, max(xs) + margin)
    bottom = min(YUKSEKLIK, max(ys) + margin)
    return pygame.Rect(left, top, max(1, right - left), max(1, bottom - top))
# </POTBO_STAGE S1602>

# <POTBO_STAGE S1612>


def _v80_world_from_local(lateral, forward, base=None):
    if base is None:
        base = pygame.Vector2(float(oyuncu_x), float(oyuncu_y - 12.0))
    f, side = _v80_player_basis()
    return pygame.Vector2(base) + side * float(lateral) + f * float(forward)
# </POTBO_STAGE S1612>

# <POTBO_STAGE S1615>


def _v80_draw_world_line(a, b, color, width=1):
    pygame.draw.line(
        ekran,
        color,
        (
            int(round(dunya_ekran_x(a.x))),
            int(round(dunya_ekran_y(a.y))),
        ),
        (
            int(round(dunya_ekran_x(b.x))),
            int(round(dunya_ekran_y(b.y))),
        ),
        int(max(1, width)),
    )


def _v80_draw_world_circle(pos, radius, color):
    pygame.draw.circle(
        ekran,
        color,
        (
            int(round(dunya_ekran_x(pos.x))),
            int(round(dunya_ekran_y(pos.y))),
        ),
        int(max(1, radius)),
    )


def _v80_draw_world_ellipse(center, rx, ry, color):
    sx = int(round(dunya_ekran_x(center.x)))
    sy = int(round(dunya_ekran_y(center.y)))
    pygame.draw.ellipse(
        ekran,
        color,
        pygame.Rect(
            sx - int(rx),
            sy - int(ry),
            max(2, int(rx * 2)),
            max(2, int(ry * 2)),
        ),
    )
# </POTBO_STAGE S1615>

# <POTBO_STAGE S1625>


def _v81_polygon_points(center_world, rx, ry, angle, factors, scale=1.0):
    sx = float(dunya_ekran_x(center_world.x))
    sy = float(dunya_ekran_y(center_world.y))
    pts = []
    n = max(3, len(factors))
    ca, sa = math.cos(float(angle)), math.sin(float(angle))
    for i, factor in enumerate(factors):
        a = math.tau * i / float(n)
        lx = math.cos(a) * float(rx) * float(factor) * scale
        ly = math.sin(a) * float(ry) * float(factor) * scale
        x = lx * ca - ly * sa
        y = lx * sa + ly * ca
        pts.append((int(round(sx + x)), int(round(sy + y))))
    return pts
# </POTBO_STAGE S1625>

# <POTBO_STAGE S1639>


def _v81_world_to_screen(pos):
    return int(round(dunya_ekran_x(float(pos.x)))), int(
        round(dunya_ekran_y(float(pos.y)))
    )
# </POTBO_STAGE S1639>

# <POTBO_STAGE S1645>


def _v81_irregular_pool_world(center, rx, ry, color, seed):
    rng = random.Random(int(seed) & 0x7FFFFFFF)
    _v80_draw_world_ellipse(center, rx, ry, color)
    lobes = 3 + max(0, int(round((rx + ry) / 9.0)))
    for i in range(min(8, lobes)):
        angle = (360.0 / max(1, lobes)) * i + rng.uniform(-24.0, 24.0)
        dist = rng.uniform(max(1.0, rx * 0.18), max(2.0, rx * 0.52))
        off = pygame.Vector2(1.0, 0.0).rotate(angle) * dist
        blob = (
            pygame.Vector2(center)
            + off
            + pygame.Vector2(rng.uniform(-1.5, 1.5), rng.uniform(-0.5, 1.2))
        )
        brx = max(1.0, rx * rng.uniform(0.18, 0.38))
        bry = max(1.0, ry * rng.uniform(0.18, 0.42))
        _v80_draw_world_ellipse(blob, brx, bry, color)
# </POTBO_STAGE S1645>

# <POTBO_STAGE S1649>


def _v30_yatan_siluet_yerlestir(surface, ekstra_rot=0.0, offset=(0.0, 0.0)):
    if surface is None:
        return
    gecen = max(0, pygame.time.get_ticks() - oyuncu_olum_baslangic_ms)
    p = max(0.0, min(1.0, gecen / float(OLU_CESET_YERLESME_MS)))
    ease = 1.0 - (1.0 - p) ** 3
    hedef_aci = -90.0 if oyuncu_yonu in ("right", "down") else 90.0
    draw = pygame.transform.rotate(surface, hedef_aci * ease + float(ekstra_rot))
    sx = float(dunya_ekran_x(oyuncu_x)) + float(offset[0])
    sy = float(dunya_ekran_y(oyuncu_y) - 7 + 8 * ease) + float(offset[1])
    sx = _v81_clamp(sx, 110, GENISLIK - 110)
    sy = _v81_clamp(sy, 98, YUKSEKLIK - 88)
    shadow = pygame.Rect(
        0,
        0,
        max(34, draw.get_width() - 2),
        max(7, int(9 * KAMERA_YAKINLASTIRMA)),
    )
    shadow.center = (int(sx), int(sy + 13))
    pygame.draw.ellipse(ekran, (0, 0, 0), shadow)
    smear = shadow.inflate(-max(8, shadow.width // 4), -max(2, shadow.height // 3))
    pygame.draw.ellipse(ekran, V77_DEATH_BLOOD, smear)
    ekran.blit(
        draw,
        draw.get_rect(center=(int(round(sx)), int(round(sy)))),
    )
# </POTBO_STAGE S1649>

# <POTBO_STAGE S1669>


def _v82_draw_viscous_creep(drop, now):
    landing_time = int(drop["birth_ms"]) + int(drop["flight_ms"])
    age = int(now) - landing_time
    if age < 520:
        return


    if _v82_drop_seed(drop, 7) % 100 >= 37:
        return
    grow = _v82_smooth((age - 520) / 1700.0)
    rng = random.Random(_v82_drop_seed(drop, 9))
    origin = pygame.Vector2(drop["landing"])
    length = (4.0 + rng.uniform(2.0, 11.0)) * grow
    drift = rng.choice((-1.0, 1.0)) * rng.uniform(0.3, 1.8)
    prev = origin
    segments = 3
    for step in range(1, segments + 1):
        s = step / float(segments)
        pos = origin + pygame.Vector2(drift * math.sin(s * math.pi), length * s)
        _v80_draw_world_line(prev, pos, V77_DEATH_BLOOD, 1)
        prev = pos
    if grow > 0.72:
        _v80_draw_world_circle(
            prev,
            1 if float(drop.get("size", 1.0)) < 1.8 else 2,
            V77_DEATH_BLOOD,
        )


def _v82_draw_seep_wet_edge(seep, now):
    age = int(now) - int(seep["birth_ms"])
    if age <= 0:
        return
    p = _v82_clamp01(age / max(1.0, float(seep["grow_ms"])))
    if p < 0.12 or p > 0.78:
        return
    rng = random.Random(int(seep["birth_ms"]) ^ int(float(seep["rx"]) * 1009))


    for i in range(2):
        a = rng.uniform(math.pi * 0.08, math.pi * 0.92)
        x = float(seep["origin"].x) + math.cos(a) * float(seep["rx"]) * (
            0.35 + 0.58 * p
        )
        y = float(seep["origin"].y) + abs(math.sin(a)) * float(seep["ry"]) * (
            0.30 + 0.62 * p
        )
        _v80_draw_world_circle(pygame.Vector2(x, y), 1, V77_DEATH_BODY)
# </POTBO_STAGE S1669>

# <POTBO_STAGE S1676>


def _v82_apply_hit_feedback(enemy, kind, damage):
    now = pygame.time.get_ticks()
    shake = {
        "glance": (1.0, 42),
        "clean": (1.8, 58),
        "deep": (2.8, 76),
        "armor": (2.4, 68),
        "heavy": (6.1, 132),
        "lethal": (7.0, 158),
    }.get(kind, (1.6, 54))
    kamera_hit_sarsintisi_baslat(*shake)


    extra = {
        "glance": 62,
        "clean": 92,
        "deep": 122,
        "armor": 76,
        "heavy": 148,
        "lethal": 0,
    }.get(kind, 84)
    if extra > 0 and getattr(enemy, "active", False):
        try:
            enemy.hit_stun_until = max(
                int(getattr(enemy, "hit_stun_until", 0)),
                now + extra,
            )
            enemy.hit_flash_until = max(
                int(getattr(enemy, "hit_flash_until", 0)),
                now + min(150, extra + 24),
            )
        except Exception:
            pass


def _v82_hit_fx_draw():
    now = pygame.time.get_ticks()
    alive = []
    for fx in v82_hit_fx:
        age = now - int(fx.get("start", now))
        life = max(1, int(fx.get("life", 110)))
        if age >= life:
            continue
        alive.append(fx)
        p = _v82_clamp01(age / float(life))
        kind = str(fx.get("kind", "clean"))
        sx = int(round(dunya_ekran_x(float(fx.get("x", 0.0)))))
        sy = int(round(dunya_ekran_y(float(fx.get("y", 0.0)))))
        base = pygame.Vector2(1.0, 0.0).rotate(float(fx.get("angle", 0.0)) + 32.0)
        perp = pygame.Vector2(-base.y, base.x)
        rng = random.Random(int(fx.get("seed", 1)))
        contraction = max(0.0, 1.0 - p)

        if kind == "glance":
            half = 8 + int(5 * contraction)
            a = pygame.Vector2(sx, sy) - base * half
            b = pygame.Vector2(sx, sy) + base * half
            pygame.draw.line(ekran, (220, 207, 204), a, b, 1)
            for i in range(2):
                q = (
                    pygame.Vector2(sx, sy)
                    + perp * rng.uniform(-5, 5)
                    + base * rng.uniform(2, 9)
                )
                pygame.draw.circle(ekran, (118, 8, 18), (int(q.x), int(q.y)), 1)

        elif kind == "armor":

            for i in range(7):
                d = base.rotate(rng.uniform(-72.0, 72.0))
                length = rng.uniform(4.0, 13.0) * contraction
                a = pygame.Vector2(sx, sy) + d * 2.0
                b = pygame.Vector2(sx, sy) + d * (2.0 + length)
                col = (248, 230, 176) if i % 2 == 0 else (218, 174, 68)
                pygame.draw.line(ekran, col, a, b, 1)
                if i < 3:
                    pygame.draw.circle(ekran, col, (int(b.x), int(b.y)), 1)

        else:
            heavy = kind in ("deep", "heavy", "lethal")
            half = (13 if not heavy else 19) + int((7 if heavy else 4) * contraction)
            a = pygame.Vector2(sx, sy) - base * half
            b = pygame.Vector2(sx, sy) + base * half
            pygame.draw.line(
                ekran,
                (252, 239, 229),
                a,
                b,
                2 if kind in ("heavy", "lethal") and p < 0.45 else 1,
            )
            pygame.draw.line(
                ekran,
                (137, 7, 20),
                a + perp * 2,
                b + perp * 2,
                2 if heavy else 1,
            )
            if heavy:
                b2 = base.rotate(58.0)
                half2 = int(half * 0.72)
                pygame.draw.line(
                    ekran,
                    (189, 18, 27),
                    pygame.Vector2(sx, sy) - b2 * half2,
                    pygame.Vector2(sx, sy) + b2 * half2,
                    1,
                )

            droplets = 3 if kind == "clean" else (5 if kind == "deep" else 7)
            if kind == "lethal":
                droplets = 10
            for i in range(droplets):
                d = base.rotate(rng.uniform(-58.0, 58.0))
                q = pygame.Vector2(sx, sy) + d * rng.uniform(4.0, 17.0) * (
                    0.35 + 0.65 * contraction
                )
                q += perp * rng.uniform(-3.0, 3.0)
                r = 1 if i > 1 else (2 if kind in ("heavy", "lethal") else 1)
                pygame.draw.circle(ekran, (126, 5, 18), (int(q.x), int(q.y)), r)

    v82_hit_fx[:] = alive
# </POTBO_STAGE S1676>

# <POTBO_STAGE S1697>


def _v82_apply_hit_feedback(enemy, kind, damage):
    _v83_hit_feedback_original(enemy, kind, damage)
    extra_shake = {
        "glance": (0.6, 18),
        "clean": (0.9, 24),
        "deep": (1.3, 28),
        "armor": (1.1, 24),
        "heavy": (1.7, 34),
        "lethal": (2.0, 42),
    }.get(str(kind), (0.8, 22))
    kamera_hit_sarsintisi_baslat(*extra_shake)
# </POTBO_STAGE S1697>

# <POTBO_STAGE S1699>


def _v83_death_victim_layer():
    if oyuncu_olum_turu in (
        "fire",
        "blast_core",
        "blast_inner",
    ):
        return _v77_death_victim_layer()
    sil = _v30_oyuncu_base_siluet()
    if sil is None:
        return _v77_death_fallback_victim()
    age = max(
        0,
        pygame.time.get_ticks() - int(oyuncu_olum_baslangic_ms or 0),
    )
    p = _v82_clamp01(age / 220.0)
    settle = _v82_clamp01(max(0.0, age - 120.0) / 220.0)
    ease = _v82_smooth(p)
    target_rot = -90.0 if oyuncu_yonu in ("right", "down") else 90.0
    rot = target_rot * (0.18 + 0.82 * ease)
    sx = float(dunya_ekran_x(oyuncu_x))
    sy = float(dunya_ekran_y(oyuncu_y) - 6 + 9 * ease)
    sx = _v83_clamp(sx, 110, GENISLIK - 110)
    sy = _v83_clamp(sy, 98, YUKSEKLIK - 88)


    shadow = pygame.Rect(
        0,
        0,
        max(40, int(58 * KAMERA_YAKINLASTIRMA)),
        max(7, int(9 * KAMERA_YAKINLASTIRMA)),
    )
    shadow.center = (int(sx), int(sy + 13))
    pygame.draw.ellipse(ekran, (0, 0, 0), shadow)
    pygame.draw.ellipse(
        ekran,
        V77_DEATH_BLOOD,
        shadow.inflate(
            -max(8, shadow.width // 4),
            -max(2, shadow.height // 3),
        ),
    )

    gap = 13.0 if age < 220 else 8.0 - 2.0 * settle
    _v83_death_split_surface(sil, (int(round(sx)), int(round(sy))), rot, gap)


    if age < 200:
        cut_p = 1.0 - _v82_clamp01(age / 200.0)
        line_len = 28 + int(18 * cut_p)
        sign = 1 if oyuncu_yonu in ("right", "down") else -1
        a = (int(sx - line_len * 0.55), int(sy - 5 * sign))
        b = (int(sx + line_len * 0.55), int(sy + 7 * sign))
        pygame.draw.line(ekran, V77_DEATH_BODY, a, b, 2)
        pygame.draw.line(ekran, V77_DEATH_BLOOD, a, b, 1)
# </POTBO_STAGE S1699>

# <POTBO_STAGE S1736>


@dataclass
class V84SlashTrace:
    world_center: pygame.Vector2
    angle: float
    length: float
    created_ms: int
    seed: int
    final: bool = False
# </POTBO_STAGE S1736>

# <POTBO_STAGE S1765>


def v84_execution_safe_point(target, direction, distance):
    direction = v84_safe_vector(direction).normalize()
    target_position = pygame.Vector2(
        float(target.x),
        float(target.y),
    )
    for scale in (1.0, 0.86, 0.72, 0.58):
        point = target_position + direction * float(distance) * scale
        point.x = v84_clamp(point.x, 38.0, HARITA_GENISLIK - 38.0)
        point.y = v84_clamp(point.y, 42.0, HARITA_YUKSEKLIK - 28.0)
        try:
            valid = hareket_gecerli_mi(point.x, point.y)
        except (NameError, TypeError, ValueError):
            valid = True
        if valid:
            return point
    return pygame.Vector2(
        v84_clamp(oyuncu_x, 38.0, HARITA_GENISLIK - 38.0),
        v84_clamp(oyuncu_y, 42.0, HARITA_YUKSEKLIK - 28.0),
    )
# </POTBO_STAGE S1765>

# <POTBO_STAGE S1772>


def v84_execution_apply_cut(index, now):
    state = v84_execution_state
    target = state.target
    if target is None or state.fracture is None:
        return
    angle, length_scale, offset = v84_execution_cut_parameters(
        index,
        state,
    )
    final = index == len(V84_EXECUTION_BEAT_TIMES) - 1
    gap = 0.72 + min(1.7, index * 0.11)
    state.fracture.cut(
        angle,
        offset_ratio=offset,
        gap_px=gap,
    )
    trace = V84SlashTrace(
        world_center=pygame.Vector2(
            float(target.x),
            float(target.y) - 23.0,
        ),
        angle=float(angle),
        length=max(
            66.0,
            max(state.fracture.size)
            * float(length_scale)
            / max(0.6, KAMERA_YAKINLASTIRMA),
        ),
        created_ms=int(now),
        seed=int(state.seed) + index * 37,
        final=bool(final),
    )
    state.slashes.append(trace)
    state.cuts_landed += 1
    v84_execution_cut_blood(
        target,
        index,
        angle,
        final=final,
    )
    shake = 2.3 + min(3.2, index * 0.24)
    duration = 72 + min(70, index * 6)
    if final:
        shake = 8.4
        duration = 210
    kamera_hit_sarsintisi_baslat(shake, duration)
    if final:
        v84_execution_finalize(now, trace)
# </POTBO_STAGE S1772>

# <POTBO_STAGE S1775>


def v84_execution_interrupt(reason="incoming_hit"):
    global v84_execution_interruptions
    global v84_execution_last_end_ms
    state = v84_execution_state
    if not state.active or state.final_applied:
        return False
    now = pygame.time.get_ticks()
    state.interrupted = True
    state.interrupt_reason = str(reason)
    v84_execution_restore_target_after_interrupt(now)
    v84_execution_interruptions += 1
    v84_execution_last_end_ms = int(now)
    dunya_olayi_kaydet(
        "execution_interrupt",
        reason=str(reason),
        enemy=str(getattr(state.target, "tur", "enemy")),
        cuts=int(state.cuts_landed),
    )
    bildirim_goster(
        bt(
            "İnfaz darbe ile bozuldu.",
            "The execution was broken by a hit.",
        ),
        PARLAK_KIRMIZI,
    )
    state.reset()
    return True
# </POTBO_STAGE S1775>

# <POTBO_STAGE S1792>


def gelistirici_test_girdisi_uygula(olay):
    global v84_guard_pressed_ms
    global v84_guard_press_serial
    if olay.type != pygame.KEYDOWN:
        return _v84_dev_input_original(olay)
    now = pygame.time.get_ticks()
    if olay.key == tus_atamasi("block"):
        v84_guard_pressed_ms = int(now)
        v84_guard_press_serial += 1

    ctrl = bool(olay.mod & pygame.KMOD_CTRL)
    if ctrl and olay.key == pygame.K_y:
        if oyun_durumu == OYUN and oyun_alt_durumu == HARITA and oyuncu_hp > 0:
            v84_execution_start(
                target=None,
                override=True,
                source="ctrl_y_infinite",
            )
        return True

    if (
        not ctrl
        and olay.key == tus_atamasi("attack")
        and oyun_durumu == OYUN
        and oyun_alt_durumu == HARITA
        and v84_riposte_active(now)
    ):
        return v84_riposte_commit(now)
    return _v84_dev_input_original(olay)
# </POTBO_STAGE S1792>

# <POTBO_STAGE S1804>


def v84_death_body_screen_anchor():
    return (
        int(round(dunya_ekran_x(oyuncu_x))),
        int(round(dunya_ekran_y(oyuncu_y) + 2)),
    )
# </POTBO_STAGE S1804>

# <POTBO_STAGE S1806>


def v84_death_arterial_draw(now):
    state = v84_death_state
    if not state.built or str(oyuncu_olum_turu) != "blood":
        return
    age = max(0, int(now) - int(state.created_ms))
    if age > 3300:
        return
    pressure = max(0.0, 1.0 - age / 3300.0)
    pulse = 0.58 + 0.42 * max(
        0.0,
        math.sin(age * 0.033),
    )
    base = v84_safe_vector(state.direction).normalize()
    origin = pygame.Vector2(
        float(oyuncu_x),
        float(oyuncu_y) - 12.0,
    )
    rng = random.Random(state.seed ^ 0xA77E)
    for branch in range(5):
        direction = base.rotate(rng.uniform(-44.0, 44.0) + branch * 7.0)
        length = rng.uniform(28.0, 66.0) * pressure * (pulse if branch < 3 else 0.72)
        lift = rng.uniform(13.0, 29.0) * pressure
        points = []
        for step in range(8):
            t = step / 7.0
            point = (
                origin
                + direction * length * t
                + pygame.Vector2(
                    0.0,
                    -lift * math.sin(t * math.pi) + 18.0 * t * t,
                )
            )
            points.append(
                (
                    int(dunya_ekran_x(point.x)),
                    int(dunya_ekran_y(point.y)),
                )
            )
        pygame.draw.lines(
            ekran,
            V84_BLOOD_HOT if branch < 2 else V84_BLOOD,
            False,
            points,
            2 if branch < 2 and pressure > 0.38 else 1,
        )
        if branch < 3:
            tip = points[-1]
            pygame.draw.polygon(
                ekran,
                V84_BLOOD_HOT,
                (
                    (tip[0], tip[1] - 2),
                    (tip[0] + 3, tip[1]),
                    (tip[0], tip[1] + 2),
                    (tip[0] - 2, tip[1]),
                ),
            )


def v84_death_victim_draw(now):
    state = v84_death_state
    age = max(0, int(now) - int(state.created_ms or now))
    if (
        not state.built
        or state.fracture is None
        or str(oyuncu_olum_turu) == "fire"
        or age < 145
    ):
        _v83_death_victim_layer()
        return
    anchor = v84_death_body_screen_anchor()
    state.fracture.draw(anchor)


    if age < 520:
        radius = max(2, int(round(6.0 * (1.0 - age / 650.0))))
        center = (
            anchor[0],
            anchor[1] - int(20 * KAMERA_YAKINLASTIRMA),
        )
        pygame.draw.polygon(
            ekran,
            V84_BODY_HOT,
            (
                (center[0], center[1] - radius),
                (center[0] + radius, center[1]),
                (center[0], center[1] + radius),
                (center[0] - radius, center[1]),
            ),
        )
# </POTBO_STAGE S1806>

# <POTBO_STAGE S1809>


def v84_execution_trace_draw(trace, now):
    age = max(0, int(now) - int(trace.created_ms))
    if age > V84_EXECUTION_TRACE_LIFE_MS:
        return
    progress = v84_smootherstep(min(1.0, age / (94.0 if trace.final else 72.0)))
    fade = 1.0 - v84_smoothstep(
        max(0.0, age - 130.0) / max(1.0, V84_EXECUTION_TRACE_LIFE_MS - 130.0)
    )
    direction = pygame.Vector2(1.0, 0.0).rotate(trace.angle)
    full_half = float(trace.length) * 0.5
    visible_half = full_half * progress
    start = trace.world_center - direction * visible_half
    end = trace.world_center + direction * visible_half
    p0 = (
        int(dunya_ekran_x(start.x)),
        int(dunya_ekran_y(start.y)),
    )
    p1 = (
        int(dunya_ekran_x(end.x)),
        int(dunya_ekran_y(end.y)),
    )
    if fade <= 0.12:
        color = V84_BLOOD
    else:
        color = V84_BODY_HOT if trace.final else V84_BODY
    pygame.draw.line(
        ekran,
        V84_BLOOD,
        p0,
        p1,
        7 if trace.final else 4,
    )
    pygame.draw.line(
        ekran,
        color,
        p0,
        p1,
        2 if trace.final else 1,
    )


def v84_execution_threats_draw():
    player = pygame.Vector2(oyuncu_x, oyuncu_y)
    for actor in v84_hostile_actors(include_suspended=False):
        delta = pygame.Vector2(actor.x, actor.y) - player
        distance = delta.length()
        if distance <= 1e-8 or distance > 230.0:
            continue
        direction = delta.normalize()
        center_world = player + direction * min(86.0, distance * 0.52)
        center = pygame.Vector2(
            dunya_ekran_x(center_world.x),
            dunya_ekran_y(center_world.y),
        )
        normal = direction.rotate(90.0)
        tip = center + direction * 8.0
        back = center - direction * 6.0
        pygame.draw.polygon(
            ekran,
            V84_BLOOD,
            (
                (int(tip.x), int(tip.y)),
                (
                    int(back.x + normal.x * 5.0),
                    int(back.y + normal.y * 5.0),
                ),
                (
                    int(back.x - normal.x * 5.0),
                    int(back.y - normal.y * 5.0),
                ),
            ),
        )
# </POTBO_STAGE S1809>

# <POTBO_STAGE S1828>


def v85_execution_safe_point(point, center):
    point = pygame.Vector2(point)
    point.x = v84_clamp(point.x, 36.0, HARITA_GENISLIK - 36.0)
    point.y = v84_clamp(point.y, 40.0, HARITA_YUKSEKLIK - 28.0)
    try:
        if _v34_static_position_valid(point.x, point.y):
            return point
        repaired = _v34_find_nearest_static_safe(
            point,
            origin=pygame.Vector2(center),
            max_radius=72.0,
        )
        if repaired is not None:
            return pygame.Vector2(repaired)
    except (NameError, TypeError, ValueError):
        pass
    return point
# </POTBO_STAGE S1828>

# <POTBO_STAGE S1832>


def v84_execution_apply_cut(index, now):
    global v85_execution_flash_started_ms
    global v85_execution_flash_until_ms
    state = v84_execution_state
    target = state.target
    if target is None or state.fracture is None:
        return
    angle, length_scale, offset = v84_execution_cut_parameters(index, state)
    final = index == len(V84_EXECUTION_BEAT_TIMES) - 1
    made = v85_fracture_cut_one(
        state.fracture,
        angle,
        offset,
        0.64 + min(1.45, index * 0.085),
        state.seed + index * 991,
        detach=not final,
    )
    state.detached_fragments = int(getattr(state, "detached_fragments", 0)) + int(made)
    trace = V84SlashTrace(
        world_center=pygame.Vector2(float(target.x), float(target.y) - 23.0),
        angle=float(angle),
        length=max(
            72.0,
            max(state.fracture.size)
            * float(length_scale)
            / max(0.6, KAMERA_YAKINLASTIRMA),
        ),
        created_ms=int(now),
        seed=int(state.seed) + index * 37,
        final=bool(final),
    )
    state.slashes.append(trace)
    state.cuts_landed += 1
    v84_execution_cut_blood(target, index, angle, final=final)
    if not final:
        v85_execution_cut_tissue(target, index, angle)
    shake = 2.6 + min(3.8, index * 0.28)
    duration = 76 + min(68, index * 5)
    if 3 <= index <= 12:
        shake = 3.8 + (index % 3) * 0.55
        duration = 58
    if final:
        shake = 11.8
        duration = 286
        v85_execution_flash_started_ms = int(now)
        v85_execution_flash_until_ms = int(now) + 190
        state.final_dash_impact = True
    kamera_hit_sarsintisi_baslat(shake, duration)
    if final:
        v84_execution_finalize(now, trace)
# </POTBO_STAGE S1832>

# <POTBO_STAGE S1835>


def v85_execution_motion_draw(now):
    state = v84_execution_state
    trail = list(getattr(state, "motion_trail", []))
    if not trail:
        return
    for index in range(1, len(trail)):
        t0, p0, phase0 = trail[index - 1]
        t1, p1, phase1 = trail[index]
        age = int(now) - int(t1)
        fade = v84_clamp01(1.0 - age / float(V85_EXECUTION_TRAIL_LIFE_MS))
        if fade <= 0.0:
            continue
        a = (
            int(dunya_ekran_x(p0.x)),
            int(dunya_ekran_y(p0.y - 9.0)),
        )
        b = (
            int(dunya_ekran_x(p1.x)),
            int(dunya_ekran_y(p1.y - 9.0)),
        )
        fast = phase1 in ("burst", "final_dash")
        pygame.draw.line(ekran, V84_BLOOD, a, b, 6 if fast else 3)
        pygame.draw.line(ekran, V84_BODY, a, b, 2 if fast else 1)

    player = v84_player_silhouette()
    if player is None:
        return
    samples = (
        trail[-8:] if state.motion_phase in ("burst", "final_dash") else trail[-3:]
    )
    for sample_index, (created, pos, phase) in enumerate(samples):
        age = int(now) - int(created)
        alpha = int(92 * v84_clamp01(1.0 - age / float(V85_EXECUTION_TRAIL_LIFE_MS)))
        if alpha <= 4:
            continue
        ghost = player.copy()
        ghost.set_alpha(alpha)
        rect = ghost.get_rect(
            midbottom=(
                int(dunya_ekran_x(pos.x)),
                int(dunya_ekran_y(pos.y)),
            )
        )
        ekran.blit(ghost, rect)
# </POTBO_STAGE S1835>

# <POTBO_STAGE S1852>


def v85_mortal_wound_update(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    state = v85_mortal_wound_state
    if not state.active:
        return False
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA:
        return True
    age = int(now) - int(state.started_ms)
    if age >= V85_MORTAL_ATTACK_RESTART_MS:
        v85_mortal_attack_restart(now)
    if age >= V85_MORTAL_FINAL_HIT_MS:
        v85_mortal_final_hit(now)
    return True
# </POTBO_STAGE S1852>

# <POTBO_STAGE S1864>


def v85_death_body_anchor():
    return (
        int(round(dunya_ekran_x(oyuncu_x))),
        int(round(dunya_ekran_y(oyuncu_y) + 3.0)),
    )


def v85_death_ground_flows_draw(now):
    state = v84_death_state
    if not state.built or state.variant == "fire":
        return
    for index, flow in enumerate(state.ground_flows):
        age = int(now) - int(state.created_ms) - int(flow["delay"])
        if age <= 0:
            continue
        progress = v84_smootherstep(age / max(1.0, float(flow["duration"])))
        points = flow["points"]
        visible = max(
            2,
            min(
                len(points),
                1 + int(math.ceil((len(points) - 1) * progress)),
            ),
        )
        screen_points = [
            (
                int(dunya_ekran_x(point.x)),
                int(dunya_ekran_y(point.y)),
            )
            for point in points[:visible]
        ]
        pygame.draw.lines(
            ekran,
            V84_BLOOD,
            False,
            screen_points,
            int(flow["width"]),
        )
        tip = screen_points[-1]
        pool = max(1, int(round(float(flow["pool"]) * progress)))
        pygame.draw.polygon(
            ekran,
            V84_BLOOD,
            (
                (tip[0] - pool, tip[1]),
                (tip[0], tip[1] - max(1, pool // 2)),
                (tip[0] + pool * 2, tip[1]),
                (tip[0], tip[1] + max(1, pool // 2)),
            ),
        )
# </POTBO_STAGE S1864>

# <POTBO_STAGE S1866>


def v85_death_arterial_core_draw(now):
    state = v84_death_state
    if not state.built or str(oyuncu_olum_turu) != "blood":
        return
    age = max(0, int(now) - int(state.created_ms))
    if age >= V85_DEATH_ARTERIAL_MS:
        return
    pressure = max(0.0, 1.0 - age / float(V85_DEATH_ARTERIAL_MS))
    heartbeat = max(0.0, math.sin(age * 0.030)) ** 3
    strength = pressure * (0.34 + 0.66 * heartbeat)
    origin = v85_death_artery_origin(state)
    base = v84_safe_vector(state.direction).normalize()
    rng = random.Random(state.seed ^ 0xA785)
    for branch in range(4):
        direction = base.rotate(rng.uniform(-34.0, 34.0) + branch * 4.0)
        length = rng.uniform(31.0, 74.0) * strength * (1.0 - branch * 0.09)
        lift = rng.uniform(12.0, 26.0) * strength
        points = []
        for step in range(9):
            t = step / 8.0
            point = origin + direction * length * t
            point.y += -lift * math.sin(math.pi * t) + 17.0 * t * t
            points.append(
                (
                    int(dunya_ekran_x(point.x)),
                    int(dunya_ekran_y(point.y)),
                )
            )
        pygame.draw.lines(
            ekran,
            V84_BLOOD_HOT if branch < 2 else V84_BLOOD,
            False,
            points,
            2 if branch < 2 and strength > 0.32 else 1,
        )
        if strength > 0.12:
            tip = points[-1]
            pygame.draw.polygon(
                ekran,
                V84_BLOOD_HOT,
                (
                    (tip[0], tip[1] - 2),
                    (tip[0] + 3, tip[1]),
                    (tip[0], tip[1] + 2),
                    (tip[0] - 2, tip[1]),
                ),
            )
# </POTBO_STAGE S1866>

# <POTBO_STAGE S1895>


def v86_execution_trace(target, state, index, angle, length_scale, now, final=False):
    trace = V84SlashTrace(
        world_center=pygame.Vector2(float(target.x), float(target.y) - 23.0),
        angle=float(angle),
        length=max(
            72.0,
            max(state.fracture.size)
            * float(length_scale)
            / max(0.6, KAMERA_YAKINLASTIRMA),
        ),
        created_ms=int(now),
        seed=int(state.seed) + index * 53,
        final=bool(final),
    )
    trace.v86_pair = -1
    trace.v86_attack_index = int(index)
    state.slashes.append(trace)
    return trace
# </POTBO_STAGE S1895>

# <POTBO_STAGE S1897>


def v84_execution_trace_draw(trace, now):
    age = int(now) - int(trace.created_ms)
    if age < 0 or age > V84_EXECUTION_TRACE_LIFE_MS:
        return
    fade = v84_clamp01(1.0 - age / float(V84_EXECUTION_TRACE_LIFE_MS))
    fade = fade * fade
    center = pygame.Vector2(
        dunya_ekran_x(trace.world_center.x),
        dunya_ekran_y(trace.world_center.y),
    )
    direction = pygame.Vector2(1.0, 0.0).rotate(trace.angle)
    normal = direction.rotate(90.0)
    half = float(trace.length) * KAMERA_YAKINLASTIRMA * 0.5
    rng = random.Random(int(trace.seed) ^ 0x86A5)
    bend = normal * rng.uniform(-5.0, 5.0)
    start = center - direction * half
    end = center + direction * half
    middle = center + bend
    points = [
        (int(round(start.x)), int(round(start.y))),
        (int(round(middle.x)), int(round(middle.y))),
        (int(round(end.x)), int(round(end.y))),
    ]
    outer = max(2, int(round((7 if trace.final else 5) * fade)))
    inner = max(1, int(round((3 if trace.final else 2) * fade)))
    pygame.draw.lines(ekran, V84_BLACK, False, points, outer + 4)
    pygame.draw.lines(ekran, V84_BLOOD, False, points, outer)
    pygame.draw.lines(ekran, V84_BODY_HOT, False, points, inner)


    if (
        3
        <= int(getattr(trace, "v86_attack_index", -1))
        < (3 + V86_EXECUTION_BURST_COUNT)
    ):
        echo_half = half * rng.uniform(0.22, 0.34)
        echo_center = center + normal * rng.uniform(-10.0, 10.0)
        a = echo_center - direction * echo_half
        b = echo_center + direction * echo_half
        pygame.draw.line(
            ekran,
            V84_BLOOD_HOT,
            (int(a.x), int(a.y)),
            (int(b.x), int(b.y)),
            1,
        )

    endpoint_size = 3 if trace.final else 2
    for point in (points[0], points[-1]):
        pygame.draw.polygon(
            ekran,
            V84_BODY,
            (
                (point[0], point[1] - endpoint_size),
                (point[0] + endpoint_size, point[1]),
                (point[0], point[1] + endpoint_size),
                (point[0] - endpoint_size, point[1]),
            ),
        )
# </POTBO_STAGE S1897>

# <POTBO_STAGE S1904>


def gelistirici_test_girdisi_uygula(olay):
    global oyuncu_savunuyor, v86_guard_intent_until_ms
    if olay.type == pygame.KEYDOWN and olay.key == tus_atamasi("block"):

        if bool(getattr(olay, "repeat", False)):
            return False
        now = pygame.time.get_ticks()
        if (
            oyun_durumu == OYUN
            and oyun_alt_durumu == HARITA
            and oyuncu_hp > 0
            and not oyuncu_kontrol_kilitli_mi(now)
        ):
            oyuncu_savunuyor = True
            v86_guard_intent_until_ms = int(now) + V86_GUARD_INTENT_BUFFER_MS
    return _v86_dev_input_original(olay)
# </POTBO_STAGE S1904>

# <POTBO_STAGE S1930>


def v86_body_anchor_screen(state):
    world = state.body_anchor + state.body_offset
    return pygame.Vector2(
        float(dunya_ekran_x(world.x)),
        float(dunya_ekran_y(world.y)),
    )
# </POTBO_STAGE S1930>

# <POTBO_STAGE S1932>


def v86_piece_screen_center(state, piece):
    anchor_world = state.body_anchor + piece.position
    anchor = pygame.Vector2(
        float(dunya_ekran_x(anchor_world.x)),
        float(dunya_ekran_y(anchor_world.y)),
    )
    width, height = state.base_size
    center = anchor + pygame.Vector2(
        piece.local_center.x,
        piece.local_center.y - height * 0.5,
    )
    center.y -= piece.z * 0.74 * KAMERA_YAKINLASTIRMA
    return center


def v86_piece_draw(state, piece, now):
    center = v86_piece_screen_center(state, piece)
    if piece.z > 1.0:
        ground_world = state.body_anchor + piece.position
        ground = (
            dunya_ekran_x(ground_world.x) + piece.local_center.x,
            dunya_ekran_y(ground_world.y)
            + piece.local_center.y
            - state.base_size[1] * 0.5,
        )
        v86_ground_shadow(
            ground,
            max(3.0, piece.surface.get_width() * 0.28),
            max(1.5, piece.surface.get_height() * 0.07),
        )
    image = piece.surface
    if abs(piece.rotation) > 0.01:
        image = pygame.transform.rotate(image, piece.rotation)
    ekran.blit(
        image,
        image.get_rect(center=(int(round(center.x)), int(round(center.y)))),
    )
    if piece.burning:
        v86_flame_draw(
            (
                center.x,
                center.y + max(1.0, image.get_height() * 0.16),
            ),
            max(3.0, min(7.5, image.get_width() * 0.32)),
            state.seed + int(piece.local_center.x * 17),
            now,
        )


def v86_debris_draw(item, now, index):
    sx = float(dunya_ekran_x(item.position.x))
    ground_y = float(dunya_ekran_y(item.position.y))
    sy = ground_y - item.z * 0.74 * KAMERA_YAKINLASTIRMA
    size = max(1, int(round(item.size * KAMERA_YAKINLASTIRMA)))
    if item.z > 1.0:
        v86_ground_shadow((sx, ground_y), size + 1, max(1, size // 2))
    direction = pygame.Vector2(1.0, 0.0).rotate(item.rotation)
    side = direction.rotate(90.0)
    if item.kind == "eye":
        points = (
            (int(sx - direction.x * size), int(sy - direction.y * size)),
            (int(sx + side.x * size), int(sy + side.y * size)),
            (int(sx + direction.x * size), int(sy + direction.y * size)),
            (int(sx - side.x * size), int(sy - side.y * size)),
        )
        pygame.draw.polygon(ekran, V84_BODY_HOT, points)
        pygame.draw.rect(ekran, V84_BLACK, pygame.Rect(int(sx), int(sy), 2, 2))
    elif item.kind == "rock":
        points = (
            (int(sx - size), int(sy)),
            (int(sx - size * 0.35), int(sy - size)),
            (int(sx + size), int(sy - size * 0.25)),
            (int(sx + size * 0.45), int(sy + size)),
        )
        pygame.draw.polygon(ekran, V84_BODY, points)
        pygame.draw.line(ekran, V84_BLACK, points[0], points[2], 1)
    else:
        points = (
            (int(sx - size), int(sy - size * 0.2)),
            (int(sx - size * 0.2), int(sy - size)),
            (int(sx + size), int(sy - size * 0.3)),
            (int(sx + size * 0.55), int(sy + size)),
            (int(sx - size * 0.65), int(sy + size * 0.65)),
        )
        pygame.draw.polygon(ekran, V84_BLOOD, points)
        if size >= 2:
            inset = [
                (
                    int(sx + (x - sx) * 0.62),
                    int(sy + (y - sy) * 0.62),
                )
                for x, y in points
            ]
            pygame.draw.polygon(ekran, V84_BODY_HOT, inset)
    if item.burning:
        v86_flame_draw((sx, sy), max(3.0, size * 1.25), index * 19, now)
# </POTBO_STAGE S1932>

# <POTBO_STAGE S1958>


def v84_execution_trace_draw(trace, now):
    age = int(now) - int(trace.created_ms)
    life = int(V84_EXECUTION_TRACE_LIFE_MS)
    fade = v87_execution_cut_alpha(age, life)
    if fade <= 0.0:
        return

    reveal = v84_smootherstep(v84_clamp01(age / float(V87_EXECUTION_CUT_REVEAL_MS)))
    center = pygame.Vector2(
        dunya_ekran_x(trace.world_center.x),
        dunya_ekran_y(trace.world_center.y),
    )
    direction = pygame.Vector2(1.0, 0.0).rotate(float(trace.angle))
    half = float(trace.length) * KAMERA_YAKINLASTIRMA * 0.5
    start = center - direction * half
    end = start.lerp(center + direction * half, reveal)

    layer = v87_execution_slash_layer
    layer.fill((0, 0, 0, 0))
    side = V87_EXECUTION_SLASH_LAYER_SIZE
    local_center = pygame.Vector2(side * 0.5, side * 0.5)
    local_start = local_center + (start - center)
    local_end = local_center + (end - center)
    final = bool(getattr(trace, "final", False))
    dark_width = 9 if final else 7
    red_width = 4 if final else 3
    alpha = max(0, min(255, int(round(255 * fade))))
    pygame.draw.line(
        layer,
        (*V87_SPECIAL_CUT_DARK, int(155 * fade)),
        local_start,
        local_end,
        dark_width,
    )
    pygame.draw.line(
        layer,
        (*V87_SPECIAL_CUT_RED, int(220 * fade)),
        local_start,
        local_end,
        red_width,
    )
    pygame.draw.line(
        layer,
        (*V87_SPECIAL_CUT_CORE, min(245, alpha)),
        local_start,
        local_end,
        1,
    )



    companion = bool(getattr(trace, "v86_cross", False))
    if not companion and 0 <= age < 140:
        q = v84_clamp01(age / 140.0)
        radius = int(round(8 + 38 * (1.0 - (1.0 - q) ** 3)))
        ring_alpha = int(round(138 * (1.0 - q) * fade))
        pygame.draw.circle(
            layer,
            (*V87_SPECIAL_RING, ring_alpha),
            (int(local_center.x), int(local_center.y)),
            radius,
            2,
        )

    if not companion and 0 <= age < V87_EXECUTION_SPARK_LIFE_MS:
        rng = random.Random(int(trace.seed) ^ 0x87A5)
        spark_fade = 1.0 - age / float(V87_EXECUTION_SPARK_LIFE_MS)
        for index in range(3 if final else 2):
            spark_direction = direction.rotate(
                rng.choice((-1.0, 1.0)) * rng.uniform(31.0, 68.0)
            )
            travel = (8.0 + index * 5.0) * (1.0 - spark_fade * 0.35)
            spark_end = local_center + spark_direction * travel
            spark_start = spark_end - spark_direction * (5.0 + index * 2.0)
            pygame.draw.line(
                layer,
                (*V87_SPECIAL_CUT_CORE, int(190 * spark_fade)),
                spark_start,
                spark_end,
                1,
            )

    top_left = (
        int(round(center.x - side * 0.5)),
        int(round(center.y - side * 0.5)),
    )
    ekran.blit(layer, top_left)
# </POTBO_STAGE S1958>

# <POTBO_STAGE S2032>
v88_flow_stats = {
    "created": 0,
    "fed": 0,
    "progressive_commits": 0,
    "forced_commits": 0,
    "collision_shortened": 0,
    "single_drop_commits": 0,
}
# </POTBO_STAGE S2032>

# <POTBO_STAGE S2034>


def v88_flow_clear_length(origin, direction, desired):
    origin = pygame.Vector2(origin)
    direction = v84_safe_vector(direction).normalize()
    if not v74_floor_clean(origin.x, origin.y):
        safe_origin = v74_trace_clean_floor(
            origin.x,
            origin.y,
            direction=-direction,
        )
        if safe_origin is None:
            return 0.0
        origin.update(safe_origin)
    clear = 0.0
    distance = 2.0
    desired = max(0.0, float(desired))
    while distance <= desired:
        point = origin + direction * distance
        if not v74_floor_clean(point.x, point.y):
            v88_flow_stats["collision_shortened"] += 1
            break
        clear = distance
        distance += 2.0
    return max(2.0, clear) if desired > 0.0 else 0.0
# </POTBO_STAGE S2034>

# <POTBO_STAGE S2040>


def v88_world_to_screen(point):
    return (
        int(round(dunya_ekran_x(float(point.x)))),
        int(round(dunya_ekran_y(float(point.y)))),
    )


def v88_flow_polygon(flow, samples=13, inset=0.0):
    samples = max(5, int(samples))
    left = []
    right = []
    for index in range(samples):
        t = index / float(samples - 1)
        before = v88_flow_center(flow, max(0.0, t - 0.025))
        after = v88_flow_center(flow, min(1.0, t + 0.025))
        tangent = v84_safe_vector(after - before, flow.direction).normalize()
        normal = pygame.Vector2(-tangent.y, tangent.x)
        left_width = max(0.35, v88_flow_half_width(flow, t, -1.0) - inset)
        right_width = max(0.35, v88_flow_half_width(flow, t, 1.0) - inset)
        center = v88_flow_center(flow, t)
        left.append(v88_world_to_screen(center + normal * left_width))
        right.append(v88_world_to_screen(center - normal * right_width))
    return left + list(reversed(right))
# </POTBO_STAGE S2040>

# <POTBO_STAGE S2042>


def v88_flow_draw_branch(flow, branch_index):
    start_t, angle, length, width = v88_flow_branch_data(flow, branch_index)
    if flow.progress() < start_t:
        return
    branch_progress = v84_smootherstep(
        (flow.progress() - start_t) / max(0.01, 1.0 - start_t)
    )
    start = v88_flow_center(flow, start_t)
    direction = flow.direction.rotate(angle)
    end = start + direction * length * branch_progress
    start_screen = v88_world_to_screen(start)
    end_screen = v88_world_to_screen(end)
    pygame.draw.line(
        ekran,
        V77_DEATH_BLOOD,
        start_screen,
        end_screen,
        max(1, int(round(width + 1.0))),
    )
    pygame.draw.line(
        ekran,
        V84_BLOOD,
        start_screen,
        end_screen,
        max(1, int(round(width))),
    )
# </POTBO_STAGE S2042>

# <POTBO_STAGE S2058>
V89_SMALL_FIRE_PATH = os.path.join(
    ASSETS,
    "ambient",
    "fire",
    "ambient_small_flame_cycle.png",
)
# </POTBO_STAGE S2058>

# <POTBO_STAGE S2086>


def _v89_rat_init(self, x, y, simdi):
    _v89_rat_init_raw(self, x, y, simdi)


    self.life_until = 2**62
# </POTBO_STAGE S2086>

# <POTBO_STAGE S2118>


_v89_smoke_prefix = os.environ.get("PATH_BLOODIED_SMOKE_PREFIX", "").strip()
# </POTBO_STAGE S2118>

# <POTBO_STAGE S2123>


def v90_draco_frames_load():
    """Extract only the authored dragon row and remove its flat green canvas."""
    if not os.path.isfile(V90_DRACO_CAST_PATH):
        return []
    try:
        sheet = pygame.image.load(V90_DRACO_CAST_PATH).convert_alpha()
    except pygame.error:
        return []
    frames = []
    for spec in V90_DRACO_FRAME_RECTS:
        area = pygame.Rect(spec).clip(sheet.get_rect())
        if area.width <= 0 or area.height <= 0:
            continue
        frame = sheet.subsurface(area).copy().convert_alpha()
        pixels = pygame.PixelArray(frame)
        try:
            for px in range(frame.get_width()):
                for py in range(frame.get_height()):
                    color = frame.get_at((px, py))



                    green_canvas = (
                        color.r < 154
                        and color.g > color.r * 1.18
                        and color.g > color.b * 1.16
                    )
                    if color.a <= 1 or green_canvas:
                        pixels[px, py] = (0, 0, 0, 0)
        finally:
            del pixels
        bounds = frame.get_bounding_rect(min_alpha=2)
        if bounds.width > 0 and bounds.height > 0:
            frames.append(frame.subsurface(bounds).copy().convert_alpha())
    return frames
# </POTBO_STAGE S2123>

# <POTBO_STAGE S2125>
V90_DRACO_ITEM_IMAGE = item_resmi_yukle(V90_DRACO_ITEM_PATH)
# </POTBO_STAGE S2125>

# <POTBO_STAGE S2171>


def v90_actor_center(actor):
    if actor is None:
        return pygame.Vector2()
    try:
        rect = actor.collision_rect()
        return pygame.Vector2(float(rect.centerx), float(rect.centery))
    except (AttributeError, TypeError):
        return pygame.Vector2(float(actor.x), float(actor.y) - 16.0)
# </POTBO_STAGE S2171>

# <POTBO_STAGE S2181>


def v90_draw_draco_sprite(
    world_position,
    frame,
    height,
    direction,
    alpha=255,
    body=True,
    glow_strength=1.0,
):
    image = v90_draco_transformed(
        frame,
        float(height) * KAMERA_YAKINLASTIRMA,
        direction,
    )
    if image is None:
        return
    center = (
        int(round(dunya_ekran_x(world_position[0]))),
        int(round(dunya_ekran_y(world_position[1]))),
    )
    rect = image.get_rect(center=center)


    glow_alpha = max(0, min(112, int(72 * glow_strength * alpha / 255.0)))
    if glow_alpha > 0:
        glow = v90_mask_tint(image, (255, 75, 8), glow_alpha)
        for offset in ((-2, 0), (2, 0), (0, -2), (0, 2), (0, 0)):
            ekran.blit(glow, rect.move(offset))
        v90_draco_stats["mask_glow_draws"] += 1
    if body:
        if alpha >= 252:
            ekran.blit(image, rect)
        else:
            body_image = image.copy()
            body_image.set_alpha(max(0, min(255, int(alpha))))
            ekran.blit(body_image, rect)
    else:
        silhouette = v90_mask_tint(image, (255, 58, 6), alpha)
        ekran.blit(silhouette, rect)


def v90_draw_rupture(center, progress, seed):
    center = pygame.Vector2(center)
    sx = int(round(dunya_ekran_x(center.x)))
    sy = int(round(dunya_ekran_y(center.y)))
    progress = v90_clamp(progress)
    rng = random.Random(int(seed))
    reach = (6.0 + 22.0 * math.sin(progress * math.pi)) * KAMERA_YAKINLASTIRMA
    layer = pygame.Surface((86, 104), pygame.SRCALPHA)
    local = pygame.Vector2(layer.get_width() / 2, layer.get_height() / 2)
    for branch in range(5):
        angle = rng.uniform(-160.0, 20.0) + branch * 57.0
        direction = pygame.Vector2(1.0, 0.0).rotate(angle)
        normal = direction.rotate(90.0)
        points = [local]
        for part in range(1, 4):
            fraction = part / 3.0
            points.append(
                local
                + direction * reach * fraction
                + normal * rng.uniform(-2.2, 2.2)
            )
        alpha = int(round(235 * math.sin(progress * math.pi)))
        pygame.draw.lines(layer, (186, 20, 3, alpha), False, points, 5)
        pygame.draw.lines(layer, (255, 168, 14, min(255, alpha + 15)), False, points, 2)
        pygame.draw.lines(layer, (255, 244, 177, min(255, alpha + 20)), False, points, 1)
    ekran.blit(layer, layer.get_rect(center=(sx, sy)))
    if V89_SMALL_FIRE_FRAMES:
        frame = V89_SMALL_FIRE_FRAMES[
            min(len(V89_SMALL_FIRE_FRAMES) - 1, int(progress * len(V89_SMALL_FIRE_FRAMES)))
        ]
        v90_draw_draco_sprite(
            center,
            frame,
            20 + 14 * math.sin(progress * math.pi),
            (1.0, 0.0),
            alpha=int(220 * math.sin(progress * math.pi)),
            body=True,
            glow_strength=0.72,
        )
# </POTBO_STAGE S2181>

# <POTBO_STAGE S2189>
_v90_last_world_tick_ms = pygame.time.get_ticks()
# </POTBO_STAGE S2189>

# <POTBO_STAGE S2194>


_v90_transient_reset_raw = gecici_dunya_aktorlerini_sifirla
# </POTBO_STAGE S2194>

# <POTBO_STAGE S2208>


_v90_smoke_prefix = os.environ.get("PATH_BLOODIED_V90_SMOKE_PREFIX", "").strip()
# </POTBO_STAGE S2208>

# <POTBO_STAGE S2230>


def _v91_ground_fire_draw(self):
    if (
        not getattr(self, "active", False)
        or not V89_SMALL_FIRE_FRAMES
    ):
        return
    now = pygame.time.get_ticks()
    age = v89_clamp01(
        (now - int(self.start_ms))
        / max(1.0, float(getattr(self, "duration_ms", 1)))
    )
    fade_in = min(1.0, age / 0.08)
    fade_out = (
        1.0
        if age < 0.72
        else max(0.0, (1.0 - age) / 0.28)
    )
    alpha_bucket = max(
        0, min(8, int(round(8 * fade_in * fade_out)))
    )
    if alpha_bucket <= 0:
        return
    frame_bucket = (
        now // 88 + int(getattr(self, "v89_pulse_phase", 0))
    ) % len(V89_SMALL_FIRE_FRAMES)
    cluster = v91_ground_fire_cluster(
        getattr(
            self,
            "v91_cluster_seed",
            getattr(self, "seed", 0),
        ),
        getattr(self, "scale", 1.0),
        KAMERA_YAKINLASTIRMA,
        frame_bucket,
        alpha_bucket,
    )
    if cluster is None:
        return
    position = (
        int(round(dunya_ekran_x(self.x))),
        int(round(dunya_ekran_y(self.y) + 3)),
    )
    ekran.blit(cluster, cluster.get_rect(midbottom=position))
# </POTBO_STAGE S2230>

# <POTBO_STAGE S2232>


def v91_draco_long_frames_load():
    if not os.path.isfile(V90_DRACO_CAST_PATH):
        return []
    try:
        sheet = pygame.image.load(V90_DRACO_CAST_PATH).convert_alpha()
    except pygame.error:
        return []
    frames = []
    for spec in V91_DRACO_LONG_RECTS:
        area = pygame.Rect(spec).clip(sheet.get_rect())
        if area.width <= 0 or area.height <= 0:
            continue
        frame = sheet.subsurface(area).copy().convert_alpha()
        for px in range(frame.get_width()):
            for py in range(frame.get_height()):
                color = frame.get_at((px, py))
                if (
                    color.a <= 1
                    or (
                        color.r < 154
                        and color.g > color.r * 1.18
                        and color.g > color.b * 1.16
                    )
                ):
                    frame.set_at((px, py), (0, 0, 0, 0))
        bounds = frame.get_bounding_rect(min_alpha=2)
        if bounds.width > 2 and bounds.height > 1:
            frames.append(
                frame.subsurface(bounds).copy().convert_alpha()
            )
    return frames
# </POTBO_STAGE S2232>

# <POTBO_STAGE S2234>


def v90_draw_draco_sprite(
    world_position,
    frame,
    height,
    direction,
    alpha=255,
    body=True,
    glow_strength=1.0,
):


    if (
        body
        and v90_draco_state.active
        and v90_draco_state.phase == "flight"
        and any(frame is candidate for candidate in V90_DRACO_FRAMES)
    ):
        long_form = v91_draco_distance_form(
            v90_draco_state.travelled
        )
        if long_form is not None:
            frame, height = long_form
    image = v90_draco_transformed(
        frame,
        float(height) * KAMERA_YAKINLASTIRMA,
        direction,
    )
    if image is None:
        return
    center = (
        int(round(dunya_ekran_x(world_position[0]))),
        int(round(dunya_ekran_y(world_position[1]))),
    )
    rect = image.get_rect(center=center)
    alpha = max(0, min(255, int(alpha)))
    if body:
        draw = image
        if alpha < 248:
            bucket = max(16, int(round(alpha / 16.0)) * 16)
            key = (id(image), bucket)
            draw = v91_draco_alpha_cache.get(key)
            if draw is None:
                draw = image.copy()
                draw.set_alpha(bucket)
                v91_draco_alpha_cache[key] = draw
                if len(v91_draco_alpha_cache) >= 180:
                    for old in list(v91_draco_alpha_cache)[:45]:
                        v91_draco_alpha_cache.pop(old, None)
        ekran.blit(draw, rect)


        glow_alpha = max(
            0,
            min(
                72,
                int(
                    46
                    * glow_strength
                    * alpha
                    / 255.0
                ),
            ),
        )
        if glow_alpha > 0:
            glow = v90_mask_tint(
                image, (255, 74, 9), glow_alpha
            )
            ekran.blit(
                glow,
                rect,
                special_flags=pygame.BLEND_RGBA_ADD,
            )
            v90_draco_stats["mask_glow_draws"] += 1
    else:
        silhouette = v90_mask_tint(
            image, (255, 58, 6), alpha
        )
        ekran.blit(silhouette, rect)
# </POTBO_STAGE S2234>

# <POTBO_STAGE S2240>


def v90_draw_rupture(center, progress, seed):
    _v91_rupture_draw_raw(center, progress, seed)
    cluster = v91_impact_flame_cluster(
        int(seed) ^ 0xCA1C,
        v90_clamp(progress),
        KAMERA_YAKINLASTIRMA,
    )
    if cluster is not None:
        point = (
            int(round(dunya_ekran_x(center[0]))),
            int(round(dunya_ekran_y(center[1]))),
        )
        ekran.blit(cluster, cluster.get_rect(center=point))
# </POTBO_STAGE S2240>

# <POTBO_STAGE S2257>


_v91_smoke_prefix = os.environ.get(
    "PATH_BLOODIED_V91_SMOKE_PREFIX", ""
).strip()
# </POTBO_STAGE S2257>

# <POTBO_STAGE S2324>


def v92_chain_polyline_position(progress):
    points = v92_chain_state.points
    if len(points) < 2:
        return pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    lengths = [points[i].distance_to(points[i + 1]) for i in range(len(points) - 1)]
    total = max(1e-6, sum(lengths))
    target_distance = max(0.0, min(1.0, progress)) * total
    walked = 0.0
    for i, length in enumerate(lengths):
        if walked + length >= target_distance:
            local = (target_distance - walked) / max(1e-6, length)

            local = 1.0 - (1.0 - local) ** 2.6
            return pygame.Vector2(points[i]).lerp(points[i + 1], local)
        walked += length
    return pygame.Vector2(points[-1])
# </POTBO_STAGE S2324>

# <POTBO_STAGE S2349>




_v94_world_update_full = dunya_simulasyon_guncelle
v94_world_next_ms = 0


def dunya_simulasyon_guncelle():
    global v94_world_next_ms
    now = pygame.time.get_ticks()
    sensitive = bool(
        oyuncu_saldiriyor
        or v92_chain_state.active
        or getattr(v84_execution_state, "active", False)
        or v90_draco_state.active
    )
    interval = 0 if sensitive else (30 if float(v63_frame_ewma_ms) > 15.8 else 20)
    if interval and int(now) < int(v94_world_next_ms):
        return None
    v94_world_next_ms = int(now) + int(interval)
    return _v94_world_update_full()
# </POTBO_STAGE S2349>

# <POTBO_STAGE S2385>


def v90_draw_draco_sprite(
    world_position,
    frame,
    height,
    direction,
    alpha=255,
    body=True,
    glow_strength=1.0,
):
    image = v90_draco_transformed(
        frame,
        float(height) * KAMERA_YAKINLASTIRMA,
        direction,
    )
    if image is None:
        return
    center = (
        int(round(dunya_ekran_x(world_position[0]))),
        int(round(dunya_ekran_y(world_position[1]))),
    )
    rect = image.get_rect(center=center)
    alpha = max(0, min(255, int(alpha)))

    if body:
        draw = image
        if alpha < 248:
            bucket = max(16, int(round(alpha / 16.0)) * 16)
            key = (id(image), bucket)
            draw = v91_draco_alpha_cache.get(key)
            if draw is None:
                draw = image.copy()
                draw.set_alpha(bucket)
                v91_draco_alpha_cache[key] = draw
        ekran.blit(draw, rect)

        hot_alpha = max(
            0,
            min(
                112,
                int(76 * float(glow_strength) * alpha / 255.0),
            ),
        )
        if hot_alpha > 0:
            hot = v90_mask_tint(image, (255, 96, 10), hot_alpha)
            ekran.blit(hot, rect, special_flags=pygame.BLEND_RGBA_ADD)
            core_alpha = min(58, int(hot_alpha * 0.45))
            if core_alpha > 0:
                core = v90_mask_tint(image, (255, 222, 122), core_alpha)
                ekran.blit(core, rect, special_flags=pygame.BLEND_RGBA_ADD)
            v90_draco_stats["mask_glow_draws"] += 1
    else:

        silhouette = v90_mask_tint(
            image,
            (255, 82, 8),
            min(255, int(alpha * 1.22)),
        )
        ekran.blit(silhouette, rect, special_flags=pygame.BLEND_RGBA_ADD)
# </POTBO_STAGE S2385>

# <POTBO_STAGE S2393>



_v95_world_sim_previous = dunya_simulasyon_guncelle
v95_world_sim_next_ms = 0


def dunya_simulasyon_guncelle():
    global v95_world_sim_next_ms
    now = pygame.time.get_ticks()
    sensitive = bool(
        oyuncu_saldiriyor
        or v92_chain_state.active
        or getattr(v84_execution_state, "active", False)
        or v90_draco_state.active
        or oyuncu_hp <= 0
    )
    if sensitive:
        return _v95_world_sim_previous()

    frame_ms = float(v63_frame_ewma_ms)
    interval = 24
    if frame_ms > 20.0:
        interval = 48
    elif frame_ms > 17.0:
        interval = 34

    if int(now) < int(v95_world_sim_next_ms):
        return None
    v95_world_sim_next_ms = int(now) + int(interval)
    return _v95_world_sim_previous()
# </POTBO_STAGE S2393>

# <POTBO_STAGE S2411>


_v97_thin_los_raw = dunya_ince_los_acik_mi
# </POTBO_STAGE S2411>

# <POTBO_STAGE S2485>


V102_UPGRADE_ICON_PATHS = {
    "weapon": (
        os.path.join(ASSETS, "ui", "weapon_icon.png"),
        os.path.join(ASSETS, "ui", "weapon_icon.webp"),
        os.path.join(BASE_DIR, "weapon_icon.png"),
    ),
    "armor": (
        os.path.join(ASSETS, "ui", "armor_icon.png"),
        os.path.join(ASSETS, "ui", "armor_icon.webp"),
        os.path.join(BASE_DIR, "armor_icon.png"),
    ),
    "endurance": (
        os.path.join(ASSETS, "ui", "endurance_icon.png"),
        os.path.join(ASSETS, "ui", "endurance_icon.webp"),
        os.path.join(BASE_DIR, "endurance_icon.png"),
    ),
}
# </POTBO_STAGE S2485>

# <POTBO_STAGE S2491>












V103_VERSION = "103.0"
# </POTBO_STAGE S2491>

# <POTBO_STAGE S2497>







V103_RENDER_MARGIN = 150.0
# </POTBO_STAGE S2497>

# <POTBO_STAGE S2499>


def v103_world_visible(x, y, margin=V103_RENDER_MARGIN):
    try:
        zoom = max(0.01, float(KAMERA_YAKINLASTIRMA))
        x = float(x)
        y = float(y)
    except (TypeError, ValueError):
        return True
    margin = float(margin) / zoom
    return (
        float(kamera_x) - margin <= x <= float(kamera_x) + GENISLIK / zoom + margin
        and float(kamera_y) - margin <= y <= float(kamera_y) + YUKSEKLIK / zoom + margin
    )


def _v103_obj_visible(obj, margin=V103_RENDER_MARGIN):
    if obj is None:
        return False
    x = getattr(obj, "x", None)
    y = getattr(obj, "y", None)
    if x is None or y is None:

        return True
    return v103_world_visible(x, y, margin)
# </POTBO_STAGE S2499>

# <POTBO_STAGE S2521>


def v106_critical_screen_wash():
    if (
        oyun_durumu != OYUN
        or oyun_alt_durumu != HARITA
        or oyuncu_hp <= 0
        or v106_player_condition() != "critical"
    ):
        return
    hp_ratio = max(0.0, min(1.0, float(oyuncu_hp) / max(1.0, float(oyuncu_max_hp))))
    depth = max(0.0, min(1.0, (0.28 - hp_ratio) / 0.28))
    pulse = 0.86 + 0.14 * math.sin(pygame.time.get_ticks() * 0.0065)
    alpha = int(round((26 + 34 * depth) * pulse))
    bucket = max(1, min(8, int(round(alpha / 8.0))))
    layer = V106_CRITICAL_WASH_CACHE.get(bucket)
    if layer is None:
        layer = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA).convert_alpha()
        layer.fill((118, 0, 13, bucket * 8))
        V106_CRITICAL_WASH_CACHE[bucket] = layer
    ekran.blit(layer, (0, 0))
# </POTBO_STAGE S2521>

# <POTBO_STAGE S2531>


def stamina_guncelle():
    global oyuncu_mana, oyuncu_max_mana, mana_gorunen, v106_mana_tick_ms
    mana_before = float(oyuncu_mana)
    max_mana_before = float(oyuncu_max_mana)
    now = pygame.time.get_ticks()
    previous_tick = int(v106_mana_tick_ms)
    v106_mana_tick_ms = int(now)
    dt = max(0.0, min(0.08, (int(now) - previous_tick) / 1000.0))




    oyuncu_max_mana = mana_before
    try:
        result = _v106_stamina_update_previous()
    finally:
        oyuncu_max_mana = max_mana_before
    oyuncu_mana = min(float(oyuncu_mana), mana_before)

    if (
        dt > 0.0
        and oyun_durumu == OYUN
        and oyun_alt_durumu == HARITA
        and oyuncu_hp > 0
        and v106_has_eadric_stone()
        and float(oyuncu_mana) < float(oyuncu_max_mana)
    ):
        rate = min(
            1.30,
            V106_EADRIC_MANA_BASE_PER_SEC
            + float(oyuncu_max_mana) * V106_EADRIC_MANA_POOL_FACTOR,
        )
        oyuncu_mana = min(float(oyuncu_max_mana), float(oyuncu_mana) + rate * dt)

    smoothing = min(1.0, max(0.0, dt) * 11.0)
    mana_gorunen += (float(oyuncu_mana) - float(mana_gorunen)) * smoothing
    return result
# </POTBO_STAGE S2531>

# <POTBO_STAGE S2534>
v107_corona_asset_path = ""
# </POTBO_STAGE S2534>

# <POTBO_STAGE S2546>


def v106_corona_knockback(actor, direction, distance):
    if actor is None or not hasattr(actor, "x") or not hasattr(actor, "y"):
        return
    direction = pygame.Vector2(direction)
    if direction.length_squared() <= 1e-8:
        return
    direction = direction.normalize()
    remaining = max(0.0, float(distance))
    while remaining > 0.01:
        step = min(4.0, remaining)
        nx = max(28.0, min(HARITA_GENISLIK - 28.0, float(actor.x) + direction.x * step))
        ny = max(28.0, min(HARITA_YUKSEKLIK - 22.0, float(actor.y) + direction.y * step))
        if harita_pikseli_engel_mi(nx, ny):
            break
        actor.x = nx
        actor.y = ny
        remaining -= step


def v106_corona_apply_hit(actor, position, direction, projectile=True):
    if not v90_actor_alive(actor):
        return
    source = v106_corona_source(position.x, position.y)
    if projectile:
        damage = max(
            132,
            int(round(126 + float(oyuncu_guc) * 3.8 + float(oyuncu_level) * 2.4)),
        )
        stagger_ms = 720
        knockback = 34.0
    else:
        damage = max(12, int(round(V106_CORONA_CONTACT_DAMAGE + oyuncu_level * 0.20)))
        stagger_ms = 260
        knockback = 18.0
    actor.hasar_al(int(damage), source)
    now = pygame.time.get_ticks()
    for attr in ("hit_stun_until", "recovery_until", "stagger_until"):
        if hasattr(actor, attr):
            setattr(actor, attr, max(int(getattr(actor, attr, 0)), int(now) + stagger_ms))
    v106_corona_knockback(actor, direction, knockback)
    if projectile:
        kamera_hit_sarsintisi_baslat(10.0 if az_hareket else 15.0, 230)
# </POTBO_STAGE S2546>

# <POTBO_STAGE S2548>


def v106_corona_fire_next(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    if not v106_corona_active_orbs():
        return False
    core_id = v106_corona.cores.pop(0)
    origin = v106_corona_orb_position(core_id, now)
    v106_corona_launch(core_id, origin, v106_corona_facing_direction(), now)
    if not v106_corona.cores:
        v106_corona.active = False
    dunya_olayi_kaydet("corona_core_release", remaining=len(v106_corona.cores))
    return True


def v106_corona_scatter_remaining(now):
    if not v106_corona.cores:
        v106_corona.active = False
        return
    rng = random.Random(v106_corona.seed ^ int(now) ^ len(v106_corona.cores) * 7919)
    count = len(v106_corona.cores)
    base = rng.random() * math.tau
    cores = list(v106_corona.cores)
    v106_corona.cores.clear()
    for index, core_id in enumerate(cores):
        angle = base + index * (math.tau / max(1, count)) + rng.uniform(-0.18, 0.18)
        direction = pygame.Vector2(math.cos(angle), math.sin(angle))
        origin = v106_corona_orb_position(core_id, now)
        v106_corona_launch(core_id, origin, direction, now)
    v106_corona.active = False
    dunya_olayi_kaydet("corona_scatter", count=count)
# </POTBO_STAGE S2548>

# <POTBO_STAGE S2554>


def v106_corona_draw_orb(world_pos, now, core_id, size=27, alpha=255):
    sx = int(round(dunya_ekran_x(world_pos.x)))
    sy = int(round(dunya_ekran_y(world_pos.y) - 24.0 * KAMERA_YAKINLASTIRMA))
    frame_index = (int(now) // 105 + int(core_id)) % max(1, len(V106_CORONA_FRAMES) or 1)
    image = v106_corona_sprite(frame_index, size, alpha)
    if image is not None:
        ekran.blit(image, image.get_rect(center=(sx, sy)))
    else:
        radius = max(3, int(size // 3))
        pygame.draw.circle(ekran, (74, 214, 255), (sx, sy), radius)
        pygame.draw.circle(ekran, (235, 252, 255), (sx, sy), max(1, radius // 3))


def v106_corona_draw(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA:
        return

    if v106_corona.active and v106_corona.cores:
        center = (int(round(dunya_ekran_x(oyuncu_x))), int(round(dunya_ekran_y(oyuncu_y) - 24.0 * KAMERA_YAKINLASTIRMA)))
        age = int(now) - int(v106_corona.started_ms)
        if age >= 520:
            rx = int(round(V106_CORONA_ORBIT_RADIUS * KAMERA_YAKINLASTIRMA))
            ry = max(6, int(round(rx * 0.62)))

            pygame.draw.ellipse(
                ekran,
                (58, 151, 203),
                pygame.Rect(center[0] - rx, center[1] - ry, rx * 2, ry * 2),
                1,
            )
        for core_id in v106_corona.cores:
            position = v106_corona_orb_position(core_id, now)
            if age >= 700:

                for back, alpha in ((44, 58), (24, 104)):
                    ghost_pos = v106_corona_orb_position(core_id, int(now) - back)
                    v106_corona_draw_orb(ghost_pos, now - back, core_id, 24, alpha)
            v106_corona_draw_orb(position, now, core_id, 28, 255)

    for projectile in v106_corona.projectiles:
        trail = list(projectile.trail)
        for index, (tx, ty) in enumerate(trail[:-1]):
            alpha = max(36, 42 + index * 22)
            v106_corona_draw_orb(pygame.Vector2(tx, ty), now, projectile.core_id, 18 + index, alpha)
        v106_corona_draw_orb(
            pygame.Vector2(projectile.x, projectile.y),
            now,
            projectile.core_id,
            30,
            255,
        )

    for impact in v106_corona.impacts:
        age = max(0, int(now) - int(impact.born_ms))
        p = max(0.0, min(1.0, age / 260.0))
        sx = int(round(dunya_ekran_x(impact.x)))
        sy = int(round(dunya_ekran_y(impact.y) - 18.0 * KAMERA_YAKINLASTIRMA))
        radius = max(2, int(round((18.0 - 10.0 * p) * KAMERA_YAKINLASTIRMA)))
        color = (198, 244, 255) if p < 0.45 else (54, 151, 205)
        pygame.draw.circle(ekran, color, (sx, sy), radius, 1)


_v106_world_sim_previous = dunya_simulasyon_guncelle


def dunya_simulasyon_guncelle():
    result = _v106_world_sim_previous()
    v106_corona_update(pygame.time.get_ticks())
    return result
# </POTBO_STAGE S2554>

# <POTBO_STAGE S2556>


_v106_transient_reset_previous = gecici_dunya_aktorlerini_sifirla


def gecici_dunya_aktorlerini_sifirla():
    global v106_corona_last_cast_ms, v107_corona_test_cast_ready
    result = _v106_transient_reset_previous()
    v106_corona.reset()
    v106_corona_last_cast_ms = -1000000
    v107_corona_test_cast_ready = False
    return result
# </POTBO_STAGE S2556>

# <POTBO_STAGE S2570>


def v106_corona_draw_orb(world_pos, now, core_id, size=27, alpha=255):
    sx = int(round(dunya_ekran_x(world_pos.x)))
    sy = int(round(dunya_ekran_y(world_pos.y) - 24.0 * KAMERA_YAKINLASTIRMA))
    frame_index = (int(now) // 58 + int(core_id)) % max(1, len(V106_CORONA_FRAMES) or 1)
    image = v108_corona_white_hot_sprite(frame_index, size, alpha)
    if image is not None:
        ekran.blit(image, image.get_rect(center=(sx, sy)))
    else:
        radius = max(3, int(size // 3))
        pygame.draw.circle(ekran, (252, 252, 252), (sx, sy), radius)
        pygame.draw.circle(ekran, (255, 255, 255), (sx, sy), max(1, radius // 2))


def v106_corona_apply_hit(actor, position, direction, projectile=True):
    if not v90_actor_alive(actor):
        return
    source = v106_corona_source(position.x, position.y)
    if projectile:
        damage = max(
            158,
            int(round(150 + float(oyuncu_guc) * 4.25 + float(oyuncu_level) * 3.1)),
        )
        stagger_ms = 860
        knockback = 46.0
    else:
        damage = max(18, int(round(V106_CORONA_CONTACT_DAMAGE + oyuncu_level * 0.28)))
        stagger_ms = 340
        knockback = 27.0
    actor.hasar_al(int(damage), source)
    now = pygame.time.get_ticks()
    for attr in ("hit_stun_until", "recovery_until", "stagger_until"):
        if hasattr(actor, attr):
            setattr(actor, attr, max(int(getattr(actor, attr, 0)), int(now) + stagger_ms))
    v106_corona_knockback(actor, direction, knockback)
    if projectile:
        kamera_hit_sarsintisi_baslat(13.0 if az_hareket else 19.0, 260)


def v106_corona_draw(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA:
        return

    if v106_corona.active and v106_corona.cores:
        center = (
            int(round(dunya_ekran_x(oyuncu_x))),
            int(round(dunya_ekran_y(oyuncu_y) - 24.0 * KAMERA_YAKINLASTIRMA)),
        )
        age = int(now) - int(v106_corona.started_ms)
        if age >= 300:
            rx = int(round(V106_CORONA_ORBIT_RADIUS * KAMERA_YAKINLASTIRMA))
            ry = max(6, int(round(rx * 0.62)))
            orbit_rect = pygame.Rect(center[0] - rx, center[1] - ry, rx * 2, ry * 2)

            phase = (int(now) * 0.012) % math.tau
            for offset, width in ((0.0, 1), (0.17, 1)):
                pygame.draw.arc(
                    ekran,
                    (250, 250, 250),
                    orbit_rect,
                    phase + offset,
                    phase + offset + math.pi * 1.46,
                    width,
                )
        for core_id in v106_corona.cores:
            position = v106_corona_orb_position(core_id, now)
            if age >= 420:

                for back, alpha, size in ((52, 46, 22), (31, 82, 24), (15, 132, 26)):
                    ghost_pos = v106_corona_orb_position(core_id, int(now) - back)
                    v106_corona_draw_orb(ghost_pos, int(now) - back, core_id, size, alpha)
            v106_corona_draw_orb(position, now, core_id, 31, 255)

    for projectile in v106_corona.projectiles:
        trail = list(projectile.trail)
        for index, (tx, ty) in enumerate(trail[:-1]):
            alpha = max(42, 52 + index * 29)
            v106_corona_draw_orb(
                pygame.Vector2(tx, ty), now, projectile.core_id, 19 + index * 2, alpha
            )
        v106_corona_draw_orb(
            pygame.Vector2(projectile.x, projectile.y),
            now,
            projectile.core_id,
            34,
            255,
        )

    for impact in v106_corona.impacts:
        age = max(0, int(now) - int(impact.born_ms))
        p = max(0.0, min(1.0, age / 260.0))
        sx = int(round(dunya_ekran_x(impact.x)))
        sy = int(round(dunya_ekran_y(impact.y) - 18.0 * KAMERA_YAKINLASTIRMA))
        radius = max(2, int(round((21.0 - 12.0 * p) * KAMERA_YAKINLASTIRMA)))
        pygame.draw.circle(ekran, (255, 255, 255), (sx, sy), radius, 1)
        if p < 0.42:
            pygame.draw.circle(ekran, (250, 250, 250), (sx, sy), max(1, radius // 2), 1)
# </POTBO_STAGE S2570>

# <POTBO_STAGE S2583>


def v106_corona_draw_orb(world_pos, now, core_id, size=27, alpha=255):
    sx = int(round(dunya_ekran_x(world_pos.x)))
    sy = int(round(dunya_ekran_y(world_pos.y) - 24.0 * KAMERA_YAKINLASTIRMA))
    frame_index = (int(now) // 58 + int(core_id)) % max(1, len(V106_CORONA_FRAMES) or 1)


    if int(alpha) >= 176:
        glow = v109_corona_glow_surface(size, alpha)
        ekran.blit(glow, glow.get_rect(center=(sx, sy)))

    image = v108_corona_white_hot_sprite(frame_index, size, alpha)
    if image is not None:
        ekran.blit(image, image.get_rect(center=(sx, sy)))
    else:
        radius = max(3, int(size // 3))
        pygame.draw.circle(ekran, (224, 245, 255), (sx, sy), radius)
        pygame.draw.circle(ekran, (255, 255, 255), (sx, sy), max(1, radius // 2))








V109_CORONA_HOMING_RANGE = 300.0
# </POTBO_STAGE S2583>

# <POTBO_STAGE S2585>
V109_CORONA_WORLD_MARGIN = 72.0
# </POTBO_STAGE S2585>

# <POTBO_STAGE S2587>


def v109_corona_first_wall(a, b):
    a = pygame.Vector2(a)
    b = pygame.Vector2(b)
    delta = b - a
    length = delta.length()
    if length <= 1e-6:
        return None
    steps = max(1, int(math.ceil(length / 7.0)))
    for index in range(1, steps + 1):
        t = index / float(steps)
        pos = a + delta * t
        if harita_pikseli_engel_mi(pos.x, pos.y):
            return t, pos
    return None
# </POTBO_STAGE S2587>

# <POTBO_STAGE S2589>


def v106_corona_apply_hit(actor, position, direction, projectile=True):
    result = _v109_corona_apply_hit_raw(actor, position, direction, projectile=projectile)
    if projectile:

        kamera_hit_sarsintisi_baslat(30.0, 350)
    return result
# </POTBO_STAGE S2589>

# <POTBO_STAGE S2592>


def oyuncu_parlama_baslat(tur):
    tur = str(tur)
    now = pygame.time.get_ticks()
    if tur == "potion":
        world_ready = (
            oyun_durumu == OYUN
            and oyun_alt_durumu == HARITA
            and oyuncu_hp > 0
        )
        busy = int(now) < int(oyuncu_parlama_bitis)
        if (not world_ready) or busy or V109_CONSUMABLE_FLASH_QUEUE:
            V109_CONSUMABLE_FLASH_QUEUE.append(tur)
            return
    return _v109_player_flash_raw(tur)


def v109_consumable_flash_update():
    if not V109_CONSUMABLE_FLASH_QUEUE:
        return
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA or oyuncu_hp <= 0:
        return
    now = pygame.time.get_ticks()
    if int(now) < int(oyuncu_parlama_bitis):
        return
    tur = V109_CONSUMABLE_FLASH_QUEUE.popleft()
    _v109_player_flash_raw(tur)
# </POTBO_STAGE S2592>

# <POTBO_STAGE S2599>



_v109_transient_reset_raw = gecici_dunya_aktorlerini_sifirla


def gecici_dunya_aktorlerini_sifirla():
    global v109_eadric_next_tick_ms
    result = _v109_transient_reset_raw()
    V109_CONSUMABLE_FLASH_QUEUE.clear()
    v109_eadric_next_tick_ms = pygame.time.get_ticks() + V109_EADRIC_TICK_MS
    return result
# </POTBO_STAGE S2599>

# <POTBO_STAGE S2622>



def v110_screen_point(world_point):
    return (
        int(round(dunya_ekran_x(float(world_point[0])))),
        int(round(dunya_ekran_y(float(world_point[1])))),
    )
# </POTBO_STAGE S2622>

# <POTBO_STAGE S2625>


_v110_world_sim_raw = dunya_simulasyon_guncelle
# </POTBO_STAGE S2625>

# <POTBO_STAGE S2630>


def _v110_draw_white_silhouettes():
    player_sx = int(round(dunya_ekran_x(float(oyuncu_x))))
    player_sy = int(round(dunya_ekran_y(float(oyuncu_y))))
    pygame.draw.ellipse(ekran, (255, 255, 255), (player_sx - 12, player_sy - 48, 24, 48), 0)
    for actor in v90_hostiles():
        center = v90_actor_center(actor)
        sx, sy = v110_screen_point((center.x, center.y))
        pygame.draw.ellipse(ekran, (255, 255, 255), (sx - 10, sy - 28, 20, 36), 0)
# </POTBO_STAGE S2630>

# <POTBO_STAGE S2632>


_v110_transient_reset_raw = gecici_dunya_aktorlerini_sifirla
# </POTBO_STAGE S2632>

# <POTBO_STAGE S2640>


_v112_reset_world_raw = gecici_dunya_aktorlerini_sifirla
# </POTBO_STAGE S2640>

# <POTBO_STAGE S2655>



def v114_irregular_impact_paths(center, seed=0):
    center = pygame.Vector2(center)
    rng = random.Random(int(seed) ^ 0xD14C)
    paths = []
    for _ in range(rng.randint(5, 7)):
        angle = rng.uniform(0.0, math.tau)
        length = rng.uniform(16.0, 42.0)
        flatten = rng.uniform(0.30, 0.85)
        tip = pygame.Vector2(
            center.x + math.cos(angle) * length,
            center.y + math.sin(angle) * length * flatten,
        )
        path = v110_polyline_points(
            center,
            tip,
            jitter=6.0,
            segments=rng.randint(3, 4),
            seed=rng.randint(0, 10**6),
        )
        paths.append(path)
    return paths
# </POTBO_STAGE S2655>

# <POTBO_STAGE S2657>

def _v114_state_reset(self):
    _v114_state_reset_raw(self)
    self.impact_paths = []
# </POTBO_STAGE S2657>

# <POTBO_STAGE S2665>


_v115_world_sim_raw = dunya_simulasyon_guncelle
# </POTBO_STAGE S2665>

# <POTBO_STAGE S2667>


_v115_reset_raw = gecici_dunya_aktorlerini_sifirla
# </POTBO_STAGE S2667>

