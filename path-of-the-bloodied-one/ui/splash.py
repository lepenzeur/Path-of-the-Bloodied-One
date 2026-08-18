# Path of the Bloodied One — categorized source stages
#
# This file is intentionally executed by core/bootstrap.py in original source order.
# Keeping one shared runtime namespace avoids gameplay regressions while the former
# 90k-line monolith is physically separated by responsibility. Do not import this
# file directly; edit the stage code normally and launch root main.py.

# <POTBO_STAGE S0489>


# =========================================================
# AÇILIŞ / SPLASH EKRANI
# =========================================================


def alfa_metin_ciz(metin, x, y, font, renk, alfa):
    alfa = max(0, min(255, int(alfa)))

    yuzey = font.render(metin, True, renk).convert_alpha()

    yuzey.set_alpha(alfa)

    ekran.blit(yuzey, yuzey.get_rect(center=(x, y)))
# </POTBO_STAGE S0489>

# <POTBO_STAGE S0491>


def splash_alfa(gecen, baslangic, bitis, fade_suresi=900):
    if gecen < baslangic:
        return 0

    if gecen > bitis:
        return 0

    if gecen < baslangic + fade_suresi:
        return (gecen - baslangic) / fade_suresi * 255

    if gecen > bitis - fade_suresi:
        return (bitis - gecen) / fade_suresi * 255

    return 255
# </POTBO_STAGE S0491>

# <POTBO_STAGE S0493>


def sinematik_menu_gecisi(tetikleyen_tus=None):
    """
    Açılıştaki ana-menü geçişinin ORİJİNAL ritmini korur:
    2.4 sn başlık çekilişi + 0.65 sn siyah bekleme + 2.3 sn merkezden açılma.

    Yalnız input hand-off düzeltilmiştir. pygame-ce 2.5.x key-state nesnesi
    iterate edilmez; splash'ı başlatan tuşun KEYUP olayı doğrudan izlenir.
    """
    global ui_buton_click_baslangic, son_secim_durumu, son_secim_imzasi

    ses_basladi = oyun_baslangic_sesini_oynat()
    tetikleyen_tus_birakildi = tetikleyen_tus is None

    if ses_basladi:
        pygame.time.delay(80)

    def _gecis_olaylarini_isle():
        nonlocal tetikleyen_tus_birakildi
        for gecis_olayi in pygame.event.get():
            if gecis_olayi.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit()
            if (
                tetikleyen_tus is not None
                and gecis_olayi.type == pygame.KEYUP
                and gecis_olayi.key == tetikleyen_tus
            ):
                tetikleyen_tus_birakildi = True

    # 1) ORİJİNAL 2400 ms başlık çekilişi.
    baslangic = pygame.time.get_ticks()
    sure = 2400

    while True:
        simdi = pygame.time.get_ticks()
        gecen = simdi - baslangic
        _gecis_olaylarini_isle()

        oran = min(1.0, gecen / sure)
        ekran.fill(SIYAH)
        alfa = int(255 * (1.0 - oran))
        olcek = 1.0 - 0.035 * oran

        road = baslik_font.render(
            "PATH OF THE", True, (220, 220, 220)
        ).convert_alpha()
        bleedied = baslik_font.render(
            "BLOODIED ONE", True, (205, 18, 42)
        ).convert_alpha()

        road = pygame.transform.smoothscale(
            road,
            (
                max(1, int(road.get_width() * olcek)),
                max(1, int(road.get_height() * olcek)),
            ),
        )
        bleedied = pygame.transform.smoothscale(
            bleedied,
            (
                max(1, int(bleedied.get_width() * olcek)),
                max(1, int(bleedied.get_height() * olcek)),
            ),
        )

        road.set_alpha(alfa)
        bleedied.set_alpha(alfa)

        road_merkez = (GENISLIK // 2, YUKSEKLIK // 2 - 90)
        bleedied_merkez = (GENISLIK // 2, YUKSEKLIK // 2 + 4)

        ekran.blit(road, road.get_rect(center=road_merkez))
        ekran.blit(bleedied, bleedied.get_rect(center=bleedied_merkez))

        alfa_metin_ciz(
            ("HERHANGİ BİR TUŞA BAS" if dil == "TR" else "PRESS ANY KEY"),
            GENISLIK // 2,
            YUKSEKLIK // 2 + 138,
            kucuk_font,
            (225, 215, 218),
            int(alfa * 0.85),
        )

        glow_oran = max(0.0, 1.0 - oran)
        if glow_oran > 0:
            glow_alpha = int(175 * glow_oran)
            road_glow = road.copy()
            road_glow.set_alpha(int(glow_alpha * 0.72))
            bleedied_glow = bleedied.copy()
            bleedied_glow.set_alpha(glow_alpha)

            glow_offsets = [
                (-8, 0),
                (8, 0),
                (0, -8),
                (0, 8),
                (-5, -5),
                (5, -5),
                (-5, 5),
                (5, 5),
                (-12, 0),
                (12, 0),
            ]

            for dx, dy in glow_offsets:
                ekran.blit(
                    road_glow,
                    road_glow.get_rect(
                        center=(road_merkez[0] + dx, road_merkez[1] + dy)
                    ),
                )
                ekran.blit(
                    bleedied_glow,
                    bleedied_glow.get_rect(
                        center=(bleedied_merkez[0] + dx, bleedied_merkez[1] + dy)
                    ),
                )

            ekran.blit(road, road.get_rect(center=road_merkez))
            ekran.blit(bleedied, bleedied.get_rect(center=bleedied_merkez))

        pygame.display.flip()
        saat.tick(FPS)

        if oran >= 1.0:
            break

    # 2) ORİJİNAL 650 ms siyah bekleme.
    bekleme_baslangic = pygame.time.get_ticks()
    while pygame.time.get_ticks() - bekleme_baslangic < 650:
        _gecis_olaylarini_isle()
        ekran.fill(SIYAH)
        pygame.display.flip()
        saat.tick(FPS)

    # 3) ORİJİNAL 2300 ms merkezden yukarı/aşağı açılma.
    menu_yuzeyi = menu_onizleme_yuzeyi_olustur()
    gecis_baslangic = pygame.time.get_ticks()
    gecis_suresi = 2300

    while True:
        simdi = pygame.time.get_ticks()
        gecen = simdi - gecis_baslangic
        _gecis_olaylarini_isle()

        oran = min(1.0, gecen / gecis_suresi)
        yumusak = 1.0 - (1.0 - oran) ** 3

        ekran.fill(SIYAH)
        alfa = int(255 * yumusak)

        menu_kopya = menu_yuzeyi.copy()
        menu_kopya.set_alpha(alfa)

        acik_yukseklik = max(2, int(YUKSEKLIK * yumusak))
        acik_rect = pygame.Rect(
            0,
            YUKSEKLIK // 2 - acik_yukseklik // 2,
            GENISLIK,
            acik_yukseklik,
        )

        ekran.set_clip(acik_rect)
        ekran.blit(menu_kopya, (0, 0))
        ekran.set_clip(None)

        kenar_alfa = int(155 * (1.0 - oran))
        if kenar_alfa > 0:
            kenar = pygame.Surface((GENISLIK, 4), pygame.SRCALPHA)
            kenar.fill((220, 15, 40, kenar_alfa))
            ekran.blit(kenar, (0, acik_rect.top - 2))
            ekran.blit(kenar, (0, acik_rect.bottom - 2))

        pygame.display.flip()
        saat.tick(FPS)

        if oran >= 1.0:
            break

    # Yalnız input bug fix: pygame.key.get_pressed() ITERATE EDİLMEZ.
    if not tetikleyen_tus_birakildi and tetikleyen_tus is not None:
        release_deadline = pygame.time.get_ticks() + 260
        while pygame.time.get_ticks() < release_deadline:
            released_now = False
            for release_event in pygame.event.get():
                if release_event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit()
                if (
                    release_event.type == pygame.KEYUP
                    and release_event.key == tetikleyen_tus
                ):
                    tetikleyen_tus_birakildi = True
                    released_now = True
            if released_now:
                break
            saat.tick(FPS)

    pygame.event.clear()
    son_tus_zamanlari.clear()
    ui_buton_click_baslangic = -10000
    son_secim_durumu = ANA_MENU
    son_secim_imzasi = secim_imzasi_al()


def splash_ekrani_goster():
    """
    İlk üç aşama toplam yaklaşık 15 saniye sürer.
    Son aşamada herhangi bir tuşa basılana kadar bekler.
    """

    baslangic = pygame.time.get_ticks()
    son_asama_hazir = False

    while True:
        simdi = pygame.time.get_ticks()
        gecen = simdi - baslangic

        for olay in pygame.event.get():
            if olay.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if son_asama_hazir and olay.type == pygame.KEYDOWN:
                sinematik_menu_gecisi(olay.key)
                return

        ekran.fill(SIYAH)

        # 0.0 - 4.8 saniye: Stüdyo adı
        if gecen < 4800:
            alfa = splash_alfa(gecen, 0, 4800, 1200)

            alfa_metin_ciz(
                "FAKE KING",
                GENISLIK // 2,
                YUKSEKLIK // 2 - 24,
                menu_baslik_font,
                (235, 25, 50),
                alfa,
            )

            alfa_metin_ciz(
                "STUDIOS",
                GENISLIK // 2,
                YUKSEKLIK // 2 + 48,
                normal_font,
                (210, 195, 200),
                alfa,
            )

        # 4.8 - 9.5 saniye: VS Code işareti
        elif gecen < 9500:
            alfa = splash_alfa(gecen, 4800, 9500, 1100)

            vscode_isareti_ciz(GENISLIK // 2, YUKSEKLIK // 2, alfa)

        # 9.5 - 15 saniye: Oyun adı ani giriş + hafif fade
        else:
            sahne_gecen = gecen - 9500

            if sahne_gecen < 250:
                baslik_alfa = int(sahne_gecen / 250 * 255)
            else:
                baslik_alfa = 255

            alfa_metin_ciz(
                "PATH OF THE",
                GENISLIK // 2,
                YUKSEKLIK // 2 - 90,
                baslik_font,
                (220, 220, 220),
                baslik_alfa,
            )

            alfa_metin_ciz(
                "BLOODIED ONE",
                GENISLIK // 2,
                YUKSEKLIK // 2 + 4,
                baslik_font,
                (205, 18, 42),
                baslik_alfa,
            )

            # Press any key yazısı 15. saniyede fade ile gelir.
            if gecen >= 15000:
                son_asama_hazir = True

                press_alfa = min(255, (gecen - 15000) / 1200 * 255)

                # Hafif nefes alan görünüm.
                nabiz = 0.72 + 0.28 * (0.5 + 0.5 * math.sin(simdi / 430))

                alfa_metin_ciz(
                    ("HERHANGİ BİR TUŞA BAS" if dil == "TR" else "PRESS ANY KEY"),
                    GENISLIK // 2,
                    YUKSEKLIK // 2 + 138,
                    kucuk_font,
                    (225, 215, 218),
                    press_alfa * nabiz,
                )

        pygame.display.flip()
        saat.tick(FPS)
# </POTBO_STAGE S0493>

# <POTBO_STAGE S0496>

if not os.environ.get("PATH_BLOODIED_SKIP_SPLASH", "").strip():
    splash_ekrani_goster()
# </POTBO_STAGE S0496>

# <POTBO_STAGE S1127>
V44_BLOOD_SPLASH_DECAL_FACTOR = 0.74
# </POTBO_STAGE S1127>

# <POTBO_STAGE S1263>

V53_SURFACE_RESPONSE = {
    "grass": {
        "absorption": 0.70,
        "spread": 0.82,
        "gloss": 0.52,
        "darken": 0.12,
        "lifetime": 0.92,
        "micro_splash": 0.18,
    },
    "dirt": {
        "absorption": 0.84,
        "spread": 0.76,
        "gloss": 0.34,
        "darken": 0.18,
        "lifetime": 0.86,
        "micro_splash": 0.08,
    },
    "stone": {
        "absorption": 0.24,
        "spread": 1.16,
        "gloss": 1.12,
        "darken": 0.04,
        "lifetime": 1.12,
        "micro_splash": 0.34,
    },
    "wood": {
        "absorption": 0.48,
        "spread": 0.94,
        "gloss": 0.72,
        "darken": 0.10,
        "lifetime": 0.98,
        "micro_splash": 0.22,
    },
    "mud": {
        "absorption": 0.92,
        "spread": 0.68,
        "gloss": 0.30,
        "darken": 0.24,
        "lifetime": 0.78,
        "micro_splash": 0.05,
    },
    "unknown": {
        "absorption": 0.52,
        "spread": 1.00,
        "gloss": 0.78,
        "darken": 0.08,
        "lifetime": 1.00,
        "micro_splash": 0.16,
    },
}
# </POTBO_STAGE S1263>

# <POTBO_STAGE S1272>


class PersistentBloodDecal(_v53_decal_parent):
    def __init__(self, x, y, scale=None, rotation=None, sprite_index=None):
        response = v53_surface_response(x, y)
        spread = float(response.get("spread", 1.0))
        incoming_scale = scale
        if incoming_scale is not None:
            incoming_scale = float(incoming_scale) * spread
        super().__init__(
            x,
            y,
            scale=incoming_scale,
            rotation=rotation,
            sprite_index=sprite_index,
        )
        self.v53_surface = v53_surface_at(x, y)
        self.v53_absorption = float(response.get("absorption", 0.52))
        self.v53_spread = spread
        self.v53_gloss_factor = float(response.get("gloss", 0.78))
        self.v53_lifetime_factor = float(response.get("lifetime", 1.0))
        self.v53_micro_splash = float(response.get("micro_splash", 0.16))
        self.v44_gloss *= self.v53_gloss_factor
        created = int(getattr(self, "created_ms", pygame.time.get_ticks()))
        dry_span = max(
            30_000,
            int(
                getattr(
                    self,
                    "dry_after_ms",
                    created + V43_BLOOD_DRY_MIN_MS,
                )
            )
            - created,
        )
        fade_span = max(
            dry_span,
            int(
                getattr(
                    self,
                    "fade_after_ms",
                    created + V43_BLOOD_FADE_MIN_MS,
                )
            )
            - created,
        )
        vanish_span = max(
            fade_span,
            int(
                getattr(
                    self,
                    "vanish_after_ms",
                    created + V43_BLOOD_FADE_MAX_MS,
                )
            )
            - created,
        )
        absorption_speed = 1.0 - 0.26 * self.v53_absorption
        self.dry_after_ms = created + int(dry_span * absorption_speed)
        self.fade_after_ms = created + int(fade_span * self.v53_lifetime_factor)
        self.vanish_after_ms = created + int(vanish_span * self.v53_lifetime_factor)
# </POTBO_STAGE S1272>

# <POTBO_STAGE S1668>


def _v82_draw_landing_splash(drop, now, land_age):
    if land_age < 0 or land_age > 190:
        return
    p = _v82_clamp01(land_age / 190.0)
    rng = random.Random(_v82_drop_seed(drop, 31))
    c = pygame.Vector2(drop["landing"])
    count = 3 + (1 if float(drop.get("size", 1.0)) > 1.75 else 0)
    for i in range(count):
        ang = rng.uniform(0.0, 360.0) + i * (360.0 / count)
        d = pygame.Vector2(1.0, 0.0).rotate(ang)
        reach = (2.0 + rng.uniform(1.0, 5.0)) * (0.35 + 0.65 * (1.0 - p))
        a = c + d * 1.0
        b = c + d * reach
        _v80_draw_world_line(a, b, V77_DEATH_BLOOD, 1)
        if p < 0.52 and i % 2 == 0:
            _v80_draw_world_circle(b, 1, V77_DEATH_BODY)
# </POTBO_STAGE S1668>

# <POTBO_STAGE S1670>


def _v77_death_blood_layer():
    if int(v81_death_blood.get("start_ms", 0)) <= 0:
        return
    now = pygame.time.get_ticks()

    # 1) ağır sızıntılar / pooling
    for seep in v81_death_blood.get("seeps", []):
        _v81_draw_seep(seep, now)
        _v82_draw_seep_wet_edge(seep, now)

    # 2) balistik damlalar, iniş sıçraması, ardından viskoz creep
    for index, drop in enumerate(v81_death_blood.get("drops", [])):
        pos, height, landed = _v81_drop_position(drop, now)
        if pos is None:
            continue
        if landed:
            _v81_draw_stain(drop, now)
            landing_time = int(drop["birth_ms"]) + int(drop["flight_ms"])
            land_age = int(now) - landing_time
            _v82_draw_landing_splash(drop, now, land_age)
            _v82_draw_viscous_creep(drop, now)
            continue

        age = int(now) - int(drop["birth_ms"])
        flight = max(1, int(drop["flight_ms"]))
        p = _v82_clamp01(age / float(flight))
        sx = float(dunya_ekran_x(pos.x))
        sy = float(dunya_ekran_y(pos.y)) - float(height) * KAMERA_YAKINLASTIRMA

        # Hızlı damlada ince kuyruk, yavaş damlada yuvarlak baş: teardrop hissi.
        tail_p = max(
            0.0,
            p - (0.034 + min(0.040, float(drop["size"]) * 0.009)),
        )
        tail_ground = pygame.Vector2(drop["origin"]).lerp(
            pygame.Vector2(drop["landing"]), tail_p
        )
        tail_arc = float(drop["height"]) * 4.0 * tail_p * (1.0 - tail_p)
        tx = float(dunya_ekran_x(tail_ground.x))
        ty = float(dunya_ekran_y(tail_ground.y)) - tail_arc * KAMERA_YAKINLASTIRMA
        radius = max(1, int(round(float(drop["size"]))))
        pygame.draw.line(
            ekran,
            V77_DEATH_BLOOD,
            (int(round(tx)), int(round(ty))),
            (int(round(sx)), int(round(sy))),
            1 if radius <= 1 else 2,
        )
        pygame.draw.ellipse(
            ekran,
            V77_DEATH_BLOOD,
            pygame.Rect(
                int(round(sx)) - radius,
                int(round(sy)) - max(1, radius // 2),
                radius * 2 + 1,
                max(2, radius + 1),
            ),
        )
        if radius >= 2 and index % 4 == 0 and p < 0.78:
            pygame.draw.circle(
                ekran,
                V77_DEATH_BODY,
                (int(round(sx)), int(round(sy - 1))),
                1,
            )
# </POTBO_STAGE S1670>

