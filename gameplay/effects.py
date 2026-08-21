






# <POTBO_STAGE S0002>











pygame.init()
# </POTBO_STAGE S0002>

# <POTBO_STAGE S0038>




BLOOD_EFFECT_KLASORU = os.path.join(ASSETS, "effects", "blood")
BLOOD_PARTICLE_KLASORU = os.path.join(BLOOD_EFFECT_KLASORU, "particles")
BLOOD_DECAL_KLASORU = os.path.join(BLOOD_EFFECT_KLASORU, "decals")
GORE_KLASORU = os.path.join(ASSETS, "effects", "gore")

BLOOD_PARTICLE_YOLLARI = [
    os.path.join(BLOOD_PARTICLE_KLASORU, f"bleed{i}.png") for i in range(1, 7)
]
BLOOD_DECAL_YOLLARI = [
    os.path.join(BLOOD_DECAL_KLASORU, "bloodsplat1.png"),
    os.path.join(BLOOD_DECAL_KLASORU, "bloodsplat2.png"),
]
GORE_GORSEL_YOLLARI = {
    "foot": os.path.join(GORE_KLASORU, "foot.png"),
    "intestine": os.path.join(GORE_KLASORU, "intestine.png"),
    "leg": os.path.join(GORE_KLASORU, "leg.png"),
    "liver": os.path.join(GORE_KLASORU, "liver.png"),
    "ribcage": os.path.join(GORE_KLASORU, "ribcage.png"),
}






GORE_ATLAS_ADAYLARI = [
    os.path.join(GORE_KLASORU, "blood_effects_sheet.png"),
    os.path.join(BLOOD_EFFECT_KLASORU, "dead_ahead_blood_effects.png"),
    os.path.join(
        BLOOD_EFFECT_KLASORU,
        "Mobile - Dead Ahead - Effects - Blood Effects(2).png",
    ),
    os.path.join(
        BLOOD_EFFECT_KLASORU,
        "Mobile - Dead Ahead - Effects - Blood Effects(1).png",
    ),
    os.path.join(
        BASE_DIR,
        "Mobile - Dead Ahead - Effects - Blood Effects(2).png",
    ),
    os.path.join(
        BASE_DIR,
        "Mobile - Dead Ahead - Effects - Blood Effects(1).png",
    ),
]




GORE_ATLAS_NORMALIZE_CROPLARI = {
    "skull": (
        0.0 / 470.0,
        560.0 / 1065.0,
        56.0 / 470.0,
        66.0 / 1065.0,
    ),
    "spinal_cord": (
        388.0 / 470.0,
        784.0 / 1065.0,
        66.0 / 470.0,
        92.0 / 1065.0,
    ),
}




V28_EXTRA_GORE_ATLAS_ADAYLARI = [
    os.path.join(GORE_KLASORU, "zombie_crisis_gore.png"),
    os.path.join(
        GORE_KLASORU,
        "PC _ Computer - Zombie Crisis - Miscellaneous - Gore.png",
    ),
    os.path.join(
        BASE_DIR,
        "PC _ Computer - Zombie Crisis - Miscellaneous - Gore.png",
    ),
]
V28_EXTRA_GORE_CROPLARI = {

    "organ_round_a": (
        18.0 / 366.0,
        6.0 / 550.0,
        38.0 / 366.0,
        42.0 / 550.0,
    ),
    "organ_round_b": (
        116.0 / 366.0,
        6.0 / 550.0,
        40.0 / 366.0,
        42.0 / 550.0,
    ),

    "organ_mass_a": (
        7.0 / 366.0,
        194.0 / 550.0,
        66.0 / 366.0,
        78.0 / 550.0,
    ),
    "organ_mass_b": (
        105.0 / 366.0,
        194.0 / 550.0,
        68.0 / 366.0,
        74.0 / 550.0,
    ),

    "bone_long_a": (
        18.0 / 366.0,
        282.0 / 550.0,
        38.0 / 366.0,
        76.0 / 550.0,
    ),
    "bone_long_b": (
        116.0 / 366.0,
        290.0 / 550.0,
        38.0 / 366.0,
        70.0 / 550.0,
    ),
    "bone_cluster_a": (
        10.0 / 366.0,
        378.0 / 550.0,
        50.0 / 366.0,
        52.0 / 550.0,
    ),
    "bone_cluster_b": (
        108.0 / 366.0,
        378.0 / 550.0,
        48.0 / 366.0,
        50.0 / 550.0,
    ),

    "flesh_shard_a": (
        8.0 / 366.0,
        438.0 / 550.0,
        48.0 / 366.0,
        72.0 / 550.0,
    ),
    "flesh_shard_b": (
        104.0 / 366.0,
        438.0 / 550.0,
        54.0 / 366.0,
        48.0 / 550.0,
    ),
}



BLOOD_WORM_SHEET_ADAYLARI = [
    os.path.join(AMBIENT_KLASORU, "blood_worms.png"),
    os.path.join(ASSETS, "creatures", "blood_worms.png"),
    os.path.join(GORE_KLASORU, "blood_worms.png"),
    os.path.join(
        BASE_DIR,
        "NES - Star Trek_ 25th Anniversary - Enemies - Blood Worms.png",
    ),
]
# </POTBO_STAGE S0038>

# <POTBO_STAGE S0069>
KAN_KIRMIZISI = (130, 6, 25)
# </POTBO_STAGE S0069>

# <POTBO_STAGE S0108>

one_cikan_slotlar = [None] * 5
# </POTBO_STAGE S0108>

# <POTBO_STAGE S0110>

one_cikan_tasima_kaynagi = None


one_cikan_atama_item_index = None
# </POTBO_STAGE S0110>

# <POTBO_STAGE S0147>



blood_particles = []
blood_decals = []
gore_chunks = []
blood_maggots = []


BLOOD_MAGGOT_MAX = 6
BLOOD_MAGGOT_FIRST_MIN_MS = 45000
BLOOD_MAGGOT_FIRST_MAX_MS = 80000
BLOOD_MAGGOT_WAVE_MIN_MS = 90000
BLOOD_MAGGOT_WAVE_MAX_MS = 150000

blood_maggot_scan_next_ms = 0
blood_maggot_scan_cursor = 0
kan_gore_son_guncelleme = pygame.time.get_ticks()


BLOOD_PARTICLE_GROUND_Z = 4.5
# </POTBO_STAGE S0147>

# <POTBO_STAGE S0149>






oyuncu_olum_baslangic_ms = 0
# </POTBO_STAGE S0149>

# <POTBO_STAGE S0152>
oyuncu_olum_gore_uretildi = False
# </POTBO_STAGE S0152>

# <POTBO_STAGE S0156>
oyuncu_olum_katil_kan_sonraki_ms = 0



oyuncu_olum_turu = "blood"
# </POTBO_STAGE S0156>

# <POTBO_STAGE S0176>



gore_sprite_onbellegi = {}
blood_decal_onbellegi = {}
GORE_CACHE_MAX = 1400
BLOOD_DECAL_CACHE_MAX = 420
# </POTBO_STAGE S0176>

# <POTBO_STAGE S0197>
aktif_gorevler = {}
# </POTBO_STAGE S0197>

# <POTBO_STAGE S0266>


BLOOD_PARTICLE_SPRITELERI = [
    img
    for img in (_v19_alpha_gorsel_yukle(yol) for yol in BLOOD_PARTICLE_YOLLARI)
    if img is not None
]
BLOOD_DECAL_SPRITELERI = [
    img
    for img in (_v19_alpha_gorsel_yukle(yol) for yol in BLOOD_DECAL_YOLLARI)
    if img is not None
]


def v104_sadelestirilmis_kan_decal(img):
    """Kan lekesindeki uzun, düz uzantıları yumuşatıp daha sade bir dökülme bırakır."""
    if img is None:
        return None
    try:
        src = img.copy().convert_alpha()
    except pygame.error:
        return img
    bbox = src.get_bounding_rect(min_alpha=1)
    if bbox.width <= 0 or bbox.height <= 0:
        return src

    cropped = src.subsurface(bbox).copy().convert_alpha()
    w, h = cropped.get_size()
    down_w = max(4, int(round(w * (0.58 if w > h * 1.35 else 0.68))))
    down_h = max(4, int(round(h * 0.68)))

    blob = pygame.transform.smoothscale(cropped, (down_w, down_h))
    blob = pygame.transform.smoothscale(blob, (w, h)).convert_alpha()
    mask = pygame.mask.from_surface(blob, 84)
    if mask.count() <= 0:
        return src

    alpha_mask = mask.to_surface(
        setcolor=(255, 255, 255, 255), unsetcolor=(0, 0, 0, 0)
    ).convert_alpha()
    simplified = cropped.copy().convert_alpha()
    simplified.blit(alpha_mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    out = pygame.Surface(src.get_size(), pygame.SRCALPHA).convert_alpha()
    out.blit(simplified, bbox.topleft)
    return out


if BLOOD_DECAL_SPRITELERI:
    BLOOD_DECAL_SPRITELERI[:] = [
        v104_sadelestirilmis_kan_decal(img) for img in BLOOD_DECAL_SPRITELERI
    ]


def _v24_gore_preview_arka_planini_sil(src):
    """Dead Ahead preview fonunu matematiksel RGB mesafesiyle şeffaflaştırır.

    Sheet'in üç baskın fon rengi vardır. Her piksel için
        d^2 = (r-r0)^2 + (g-g0)^2 + (b-b0)^2
    hesaplanır; herhangi bir fon merkezine yeterince yakınsa alpha=0 yapılır.
    Bu yöntem yalnız kırmızı/kahverengi organı bırakır, yeşil hücreyi taşımaz.
    """
    if src is None:
        return None

    temiz = src.copy().convert_alpha()
    fonlar = (
        (39, 57, 28),
        (37, 95, 56),
        (24, 35, 15),
    )
    esik2 = 18 * 18
    w, h = temiz.get_size()

    temiz.lock()
    try:
        for y in range(h):
            for x in range(w):
                r, g, b, a = temiz.get_at((x, y))
                if a <= 8:
                    continue
                en_yakin = min(
                    (r - fr) * (r - fr) + (g - fg) * (g - fg) + (b - fb) * (b - fb)
                    for fr, fg, fb in fonlar
                )
                if en_yakin <= esik2:
                    temiz.set_at((x, y), (r, g, b, 0))
    finally:
        temiz.unlock()



    bounds = temiz.get_bounding_rect(min_alpha=8)
    if bounds.width <= 0 or bounds.height <= 0:
        return None
    return temiz.subsurface(bounds).copy().convert_alpha()


def _v24_normalize_crop(src, oran_rect):
    """Normalize edilmiş atlas koordinatını gerçek pygame.Rect'e dönüştürür."""
    if src is None:
        return None
    nx, ny, nw, nh = oran_rect
    sw, sh = src.get_size()
    x = int(round(float(nx) * sw))
    y = int(round(float(ny) * sh))
    w = max(1, int(round(float(nw) * sw)))
    h = max(1, int(round(float(nh) * sh)))
    rect = pygame.Rect(x, y, w, h).clip(src.get_rect())
    if rect.width <= 0 or rect.height <= 0:
        return None
    return _v24_gore_preview_arka_planini_sil(src.subsurface(rect).copy())


def _v24_gore_atlas_spriteleri_yukle():
    yol = mevcut_ilk_dosya(GORE_ATLAS_ADAYLARI)
    if not yol:
        return {}
    atlas = _v19_alpha_gorsel_yukle(yol)
    if atlas is None:
        return {}

    sonuc = {}
    for ad, oran_rect in GORE_ATLAS_NORMALIZE_CROPLARI.items():
        img = _v24_normalize_crop(atlas, oran_rect)
        if img is not None:
            sonuc[ad] = img
    return sonuc


GORE_SPRITELERI = {
    ad: _v19_alpha_gorsel_yukle(yol) for ad, yol in GORE_GORSEL_YOLLARI.items()
}
GORE_SPRITELERI = {ad: img for ad, img in GORE_SPRITELERI.items() if img is not None}
GORE_SPRITELERI.update(_v24_gore_atlas_spriteleri_yukle())
# </POTBO_STAGE S0266>

# <POTBO_STAGE S0268>


def _v28_extra_gore_atlas_spriteleri_yukle():
    yol = mevcut_ilk_dosya(V28_EXTRA_GORE_ATLAS_ADAYLARI)
    if not yol:
        return {}
    atlas = _v19_alpha_gorsel_yukle(yol)
    if atlas is None:
        return {}
    sonuc = {}
    sw, sh = atlas.get_size()
    for ad, oran_rect in V28_EXTRA_GORE_CROPLARI.items():
        nx, ny, nw, nh = oran_rect
        rect = pygame.Rect(
            int(round(nx * sw)),
            int(round(ny * sh)),
            max(1, int(round(nw * sw))),
            max(1, int(round(nh * sh))),
        ).clip(atlas.get_rect())
        if rect.width <= 0 or rect.height <= 0:
            continue
        img = _v28_beyaz_fon_temizle(atlas.subsurface(rect).copy())
        if img is not None:
            sonuc[ad] = img
    return sonuc


def _v28_blood_worm_spriteleri_yukle():
    yol = mevcut_ilk_dosya(BLOOD_WORM_SHEET_ADAYLARI)
    if not yol:
        return []
    sheet = _v19_alpha_gorsel_yukle(yol)
    if sheet is None:
        return []
    sw, sh = sheet.get_size()

    rectler = [(2 + 12 * i, 6, 12, 12) for i in range(6)]
    kareler = []
    for x, y, w, h in rectler:
        rect = pygame.Rect(
            int(round(x / 76.0 * sw)),
            int(round(y / 24.0 * sh)),
            max(1, int(round(w / 76.0 * sw))),
            max(1, int(round(h / 24.0 * sh))),
        ).clip(sheet.get_rect())
        if rect.width <= 0 or rect.height <= 0:
            continue
        frame = sheet.subsurface(rect).copy().convert_alpha()
        bounds = frame.get_bounding_rect(min_alpha=8)
        if bounds.width <= 0 or bounds.height <= 0:
            continue
        parca = frame.subsurface(bounds).copy().convert_alpha()
        canvas = pygame.Surface((12, 12), pygame.SRCALPHA)
        canvas.blit(parca, parca.get_rect(center=(6, 6)))
        kareler.append(canvas)
    return kareler


GORE_SPRITELERI.update(_v28_extra_gore_atlas_spriteleri_yukle())
BLOOD_WORM_SPRITELERI = _v28_blood_worm_spriteleri_yukle()
# </POTBO_STAGE S0268>

# <POTBO_STAGE S0301>


def gotik_panel(rect, kenarlik=KAN_KIRMIZISI, alpha=238):
    golge = rect.move(7, 8)

    pygame.draw.rect(ekran, (0, 0, 0), golge, border_radius=0)

    panel_surface = pygame.Surface(rect.size, pygame.SRCALPHA)

    panel_surface.fill((KOYU_PANEL[0], KOYU_PANEL[1], KOYU_PANEL[2], alpha))

    ekran.blit(panel_surface, rect.topleft)

    pygame.draw.rect(ekran, kenarlik, rect, 2, border_radius=0)

    uzunluk = 18

    noktalar = [
        (rect.left, rect.top),
        (rect.right, rect.top),
        (rect.left, rect.bottom),
        (rect.right, rect.bottom),
    ]

    for x, y in noktalar:
        yon_x = 1 if x == rect.left else -1

        yon_y = 1 if y == rect.top else -1

        pygame.draw.line(
            ekran,
            PARLAK_KIRMIZI,
            (x, y),
            (x + yon_x * uzunluk, y),
            2,
        )

        pygame.draw.line(
            ekran,
            PARLAK_KIRMIZI,
            (x, y),
            (x, y + yon_y * uzunluk),
            2,
        )
# </POTBO_STAGE S0301>

# <POTBO_STAGE S0319>


def oyun_kaydet():
    global aktif_kayit
    global kayit_animasyon_bitis



    if oyuncu_hp <= 0:
        return False

    dunya_olayi_kaydet("save")

    temiz_ad = dosya_adi_temizle(oyuncu_adi)

    if not temiz_ad:
        temiz_ad = "save"

    if aktif_kayit is None:
        aktif_kayit = benzersiz_kayit_yolu(temiz_ad)

    veri = {
        "player_name": oyuncu_adi,
        "gender": karakter_cinsiyet,
        "level": oyuncu_level,
        "level_balance_version": LEVEL_BALANCE_VERSION,
        "gold": oyuncu_altin,
        "strength": oyuncu_guc,
        "damage": oyuncu_hasari,
        "hp": oyuncu_hp,
        "max_hp": oyuncu_max_hp,
        "mana": oyuncu_mana,
        "max_mana": oyuncu_max_mana,
        "stamina": oyuncu_stamina,
        "max_stamina": oyuncu_max_stamina,
        "inventory": envanter_itemleri,
        "featured_slots": one_cikan_slotlar,
        "featured_selected": envanter_secili_slot,
        "q_quick_slot": q_hizli_item_index,
        "eadric_name_known": eadric_adi_ogrenildi,
        "fire_magic_from_eadric": fire_magic_eadric_alindi,
        "eadric_fire_declines": eadric_fire_magic_reddetme,
        "eadric_fire_offer_lock": eadric_fire_magic_teklif_kilit_konusma,
        "npc_intro_done": npc_intro_tamamlandi,
        "loot_taken": ganimet_alindi,
        "loot_stage": ganimet_asamasi,
        "post_loot_done": ganimet_sonrasi_konusma_yapildi,
        "cave_route_known": magara_yolu_ogrenildi,
        "eadric_stone_taken": eadric_tasi_alindi,
        "eadric_attitude": eadric_tutumu,
        "tarkard_name_known": tarkard_adi_ogrenildi,
        "tarkard_spoken": tarkard_konusuldu,
        "torrmund_spoken": torrmund_konusuldu,
        "merchant_upgrades": merchant_yukseltmeler,
        "quests": aktif_gorevler,
        "important_items_seen": sorted(onemli_item_gorulenler),
        "merchant_buyback": merchant_geri_alim_listesi,
        "merchant_products_seen": sorted(merchant_gorulen_urunler),

        "world_state": dict(dunya_durumu),
        "world_event_log": list(dunya_olay_gunlugu)[-72:],

        "common_enemy_version": COMMON_ENEMY_SAVE_VERSION,
        "common_enemies": [dusman.to_save() for dusman in common_enemies],

        "tarkard": tarkard_actor.to_save() if tarkard_actor is not None else None,
        "torrmund": torrmund_actor.to_save() if torrmund_actor is not None else None,

        "x": oyuncu_x,
        "y": oyuncu_y,
    }

    try:


        _v34_json_atomic_write(aktif_kayit, veri, indent=4)
        _v34_json_atomic_write(SON_KAYIT_DOSYASI, {"path": aktif_kayit}, indent=4)
        kayit_animasyon_bitis = pygame.time.get_ticks() + 1500
        return True

    except OSError as exc:
        debug_log("Save write failed:", exc)
        return False
# </POTBO_STAGE S0319>

# <POTBO_STAGE S0324>







def kayit_adi_ekrani_ciz():
    varsayilan_gotik_arka_plan()

    koyu_kaplama(185)

    panel = pygame.Rect(355, 235, 570, 250)

    gotik_panel(panel, KAN_KIRMIZISI, 245)

    yazi_yaz(
        t("save_name_title"),
        panel.centerx,
        panel.y + 45,
        PARLAK_KIRMIZI,
        menu_baslik_font,
        True,
    )

    giris = pygame.Rect(panel.x + 70, panel.y + 105, panel.width - 140, 52)

    pygame.draw.rect(ekran, (5, 4, 8), giris, border_radius=0)

    pygame.draw.rect(ekran, PARLAK_KIRMIZI, giris, 2, border_radius=0)

    imlec = "|" if pygame.time.get_ticks() // 500 % 2 == 0 else ""

    yazi_yaz(
        kayit_adi_girdisi + imlec,
        giris.x + 14,
        giris.y + 14,
        BEYAZ,
        normal_font,
    )



    if kayit_mesaji:
        yazi_yaz(
            kayit_mesaji,
            panel.centerx,
            panel.y + 220,
            PARLAK_KIRMIZI,
            kucuk_font,
            True,
        )
# </POTBO_STAGE S0324>

# <POTBO_STAGE S0329>


def karakter_olusturma_ciz():
    varsayilan_gotik_arka_plan()
    koyu_kaplama(185)

    yazi_yaz(
        t("create_title"),
        GENISLIK // 2,
        42,
        PARLAK_KIRMIZI,
        menu_baslik_font,
        True,
    )

    erkek_kart = pygame.Rect(45, 92, 315, 545)
    kadin_kart = pygame.Rect(920, 92, 315, 545)
    orta_panel = pygame.Rect(385, 92, 510, 545)

    karakter_karti_ciz(
        erkek_kart,
        "male",
        karakter_cinsiyet == "male",
        karakter_onay_gecisi_aktif and karakter_cinsiyet == "male",
    )
    karakter_karti_ciz(
        kadin_kart,
        "female",
        karakter_cinsiyet == "female",
        karakter_onay_gecisi_aktif and karakter_cinsiyet == "female",
    )

    gotik_panel(orta_panel, KAN_KIRMIZISI, 242)

    yazi_yaz(
        oyuncu_adi,
        orta_panel.centerx,
        140,
        BEYAZ,
        oyun_buyuk_font,
        True,
    )

    pygame.draw.line(
        ekran,
        KAN_KIRMIZISI,
        (orta_panel.x + 48, 178),
        (orta_panel.right - 48, 178),
        1,
    )

    bilgi = KARAKTER_OZGECMISLERI[dil][karakter_cinsiyet]

    yazi_yaz(
        bilgi["title"],
        orta_panel.centerx,
        216,
        PARLAK_KIRMIZI,
        normal_font,
        True,
    )
    yazi_yaz(
        bilgi["name"],
        orta_panel.centerx,
        250,
        BEYAZ,
        kucuk_font,
        True,
    )

    biyografi_satirlari = metni_satirlara_bol(
        bilgi["bio"], mini_font, orta_panel.width - 72
    )

    biyografi_y = 282
    for satir_metni in biyografi_satirlari[:11]:
        yazi_yaz(
            satir_metni,
            orta_panel.centerx,
            biyografi_y,
            ACIK_GRI,
            mini_font,
            True,
        )
        biyografi_y += 18

    yazi_yaz(
        bilgi["style"],
        orta_panel.centerx,
        min(biyografi_y + 16, 505),
        SARI,
        mini_font,
        True,
    )

    baslat_rect = pygame.Rect(orta_panel.x + 72, 553, orta_panel.width - 144, 52)

    baslat_rect = buton_click_anim_rect(baslat_rect, True)

    pygame.draw.rect(ekran, (62, 4, 16), baslat_rect, border_radius=0)
    pygame.draw.rect(ekran, PARLAK_KIRMIZI, baslat_rect, 2, border_radius=0)
    yazi_yaz(
        t("start_game"),
        baslat_rect.centerx,
        baslat_rect.centery,
        BEYAZ,
        menu_font,
        True,
    )

    if karakter_mesaji:
        yazi_yaz(
            karakter_mesaji,
            GENISLIK // 2,
            656,
            PARLAK_KIRMIZI,
            kucuk_font,
            True,
        )



    if karakter_onay_gecisi_aktif:
        gecen = max(
            0,
            pygame.time.get_ticks() - karakter_onay_gecisi_baslangic,
        )
        fade_sure = max(
            1,
            KARAKTER_ONAY_GECIS_SURESI - KARAKTER_ONAY_FADE_BASLANGICI,
        )
        fade_oran = max(
            0.0,
            min(
                1.0,
                (gecen - KARAKTER_ONAY_FADE_BASLANGICI) / fade_sure,
            ),
        )
        fade_oran = fade_oran * fade_oran * (3.0 - 2.0 * fade_oran)
        if fade_oran > 0.0:
            fade = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
            fade.fill((0, 0, 0, int(round(255 * fade_oran))))
            ekran.blit(fade, (0, 0))
# </POTBO_STAGE S0329>

# <POTBO_STAGE S0335>


def kontrol_satiri(tus, aciklama, x, y, genislik):
    tus_rect = pygame.Rect(x, y, 190, 38)

    aciklama_rect = pygame.Rect(x + 205, y, genislik - 205, 38)

    pygame.draw.rect(ekran, (38, 4, 13), tus_rect, border_radius=0)

    pygame.draw.rect(ekran, KAN_KIRMIZISI, tus_rect, 1, border_radius=0)

    pygame.draw.rect(ekran, (12, 10, 15), aciklama_rect, border_radius=0)

    yazi_yaz(
        tus,
        tus_rect.centerx,
        tus_rect.centery,
        BEYAZ,
        kucuk_font,
        True,
    )

    yazi_yaz(
        aciklama,
        aciklama_rect.x + 12,
        aciklama_rect.y + 9,
        ACIK_GRI,
        kucuk_font,
    )
# </POTBO_STAGE S0335>

# <POTBO_STAGE S0353>


def envanterden_bir_azalt(item_index):
    """Stack içinden bir adet tüketir; son adet ise slotu boşaltır."""
    global q_hizli_item_index
    if not isinstance(item_index, int) or not 0 <= item_index < len(envanter_itemleri):
        return False
    item = envanter_itemleri[item_index]
    if not isinstance(item, dict):
        return False
    adet = item_adedi(item)
    if adet > 1:
        item["quantity"] = adet - 1
    else:
        one_cikan_referanslarini_temizle(item_index)
        if q_hizli_item_index == item_index:
            q_hizli_item_index = None
        envanter_itemleri[item_index] = None
    return True
# </POTBO_STAGE S0353>

# <POTBO_STAGE S0359>


def secili_one_cikan_item_index():
    if not 0 <= envanter_secili_slot < len(one_cikan_slotlar):
        return None

    item_index = one_cikan_slotlar[envanter_secili_slot]

    if not isinstance(item_index, int):
        return None

    if not 0 <= item_index < len(envanter_itemleri):
        return None

    return item_index


def secili_one_cikan_itemi_kullan():
    item_index = secili_one_cikan_item_index()

    if item_index is None:
        bildirim_goster(
            bt(
                "Seçili öne çıkan slot boş.",
                "The selected featured slot is empty.",
            )
        )
        return

    secili_itemi_kullan(item_index)
# </POTBO_STAGE S0359>

# <POTBO_STAGE S0361>


def one_cikan_referanslarini_temizle(item_index):
    """Tüketilen veya atılan eşyanın öne çıkan slot bağlantılarını kaldırır."""
    for slot_index, bagli_item_index in enumerate(one_cikan_slotlar):
        if bagli_item_index == item_index:
            one_cikan_slotlar[slot_index] = None
# </POTBO_STAGE S0361>

# <POTBO_STAGE S0367>


def secili_itemi_one_cikana_ata(item_index, hedef_slot):
    """
    Itemi yalnız tek featured slotta tutar. Item zaten başka featured slottaysa
    hedefteki item eski slota geçer; böylece gerçek bir swap oluşur. Item daha
    önce featured değilse hedefteki item yalnız featured bağını kaybeder.
    """
    if not isinstance(item_index, int) or not 0 <= item_index < len(envanter_itemleri):
        return False
    if not isinstance(hedef_slot, int) or not 0 <= hedef_slot < 5:
        return False
    if not isinstance(envanter_itemleri[item_index], dict):
        return False
    if item_buyu_mu(envanter_itemleri[item_index]):
        bildirim_goster(
            bt(
                "Büyüler 1-5 öne çıkan slotlara atanamaz; Q slotunu kullan.",
                "Spells cannot be assigned to featured slots 1-5; use the Q slot.",
            )
        )
        return False

    one_cikan_slotlarini_normalize_et()
    eski_slot = next(
        (i for i, bagli in enumerate(one_cikan_slotlar) if bagli == item_index),
        None,
    )
    if eski_slot == hedef_slot:
        bildirim_goster(
            bt(
                f"Eşya zaten {hedef_slot + 1}. öne çıkan slotta.",
                f"Item is already in featured slot {hedef_slot + 1}.",
            )
        )
        return True

    hedefteki_item = one_cikan_slotlar[hedef_slot]



    for i, bagli in enumerate(one_cikan_slotlar):
        if bagli == item_index:
            one_cikan_slotlar[i] = None

    one_cikan_slotlar[hedef_slot] = item_index
    if eski_slot is not None and eski_slot != hedef_slot:
        one_cikan_slotlar[eski_slot] = hedefteki_item

    one_cikan_slotlarini_normalize_et()
    bildirim_goster(
        bt(
            f"Eşya {hedef_slot + 1}. öne çıkan slota atandı.",
            f"Item assigned to featured slot {hedef_slot + 1}.",
        )
    )
    dunya_olayi_kaydet(
        "featured_assign",
        item_id=str(envanter_itemleri[item_index].get("id", "")),
        slot=hedef_slot + 1,
    )
    return True


def secili_one_cikandan_cikar(slot_index=None):
    if slot_index is None:
        slot_index = envanter_secili_slot

    if not isinstance(slot_index, int) or not 0 <= slot_index < 5:
        return

    if one_cikan_slotlar[slot_index] is None:
        return

    one_cikan_slotlar[slot_index] = None

    bildirim_goster(
        bt(
            f"{slot_index + 1}. öne çıkan slot temizlendi.",
            f"Featured slot {slot_index + 1} cleared.",
        )
    )
# </POTBO_STAGE S0367>

# <POTBO_STAGE S0369>


def one_cikan_tasimayi_baslat(slot_index=None):
    global one_cikan_tasima_kaynagi

    if slot_index is None:
        slot_index = envanter_secili_slot

    if not isinstance(slot_index, int) or not 0 <= slot_index < 5:
        return

    item_index = one_cikan_slotlar[slot_index]
    if not isinstance(item_index, int):
        return
    if not 0 <= item_index < len(envanter_itemleri):
        return
    if envanter_itemleri[item_index] is None:
        return

    one_cikan_tasima_kaynagi = slot_index


def one_cikan_slotlari_takasla(kaynak_slot, hedef_slot):
    global one_cikan_tasima_kaynagi

    if not (
        isinstance(kaynak_slot, int)
        and isinstance(hedef_slot, int)
        and 0 <= kaynak_slot < 5
        and 0 <= hedef_slot < 5
    ):
        one_cikan_tasima_kaynagi = None
        return

    if kaynak_slot != hedef_slot:
        (
            one_cikan_slotlar[kaynak_slot],
            one_cikan_slotlar[hedef_slot],
        ) = (
            one_cikan_slotlar[hedef_slot],
            one_cikan_slotlar[kaynak_slot],
        )

    one_cikan_tasima_kaynagi = None
    one_cikan_slotlarini_normalize_et()


def envanter_itemlerini_takasla(kaynak, hedef):
    """İki slotu değiştirir; öne çıkan ve Q atamaları eşyanın kendisini takip eder."""
    global envanter_tasima_kaynagi, q_hizli_item_index

    if not (
        isinstance(kaynak, int)
        and isinstance(hedef, int)
        and 0 <= kaynak < len(envanter_itemleri)
        and 0 <= hedef < len(envanter_itemleri)
    ):
        envanter_tasima_kaynagi = None
        return

    if kaynak != hedef:
        envanter_itemleri[kaynak], envanter_itemleri[hedef] = (
            envanter_itemleri[hedef],
            envanter_itemleri[kaynak],
        )

        for index, slot_index in enumerate(one_cikan_slotlar):
            if slot_index == kaynak:
                one_cikan_slotlar[index] = hedef
            elif slot_index == hedef:
                one_cikan_slotlar[index] = kaynak

        if q_hizli_item_index == kaynak:
            q_hizli_item_index = hedef
        elif q_hizli_item_index == hedef:
            q_hizli_item_index = kaynak

    envanter_tasima_kaynagi = None
    one_cikan_slotlarini_normalize_et()
    q_hizli_slot_normalize_et()
# </POTBO_STAGE S0369>

# <POTBO_STAGE S0384>


def one_cikan_item_paneli_ciz():
    panel = hud_sag_rect()
    gotik_panel(panel, KAN_KIRMIZISI, 225)



    slot_boyut = 68
    bosluk = 12
    grup_w = slot_boyut * 5 + bosluk * 4

    q_boyut = slot_boyut
    ayirici_bosluk = 30
    toplam = grup_w + ayirici_bosluk + q_boyut
    baslangic_x = panel.centerx - toplam // 2
    y = panel.y + 41

    for i in range(5):
        rect = pygame.Rect(
            baslangic_x + i * (slot_boyut + bosluk),
            y,
            slot_boyut,
            slot_boyut,
        )
        slot_ciz(
            rect,
            secili=(i == envanter_secili_slot),
            numara=i + 1,
            item_index=one_cikan_slotlar[i],
        )

    ayir_x = baslangic_x + grup_w + ayirici_bosluk // 2
    pygame.draw.line(
        ekran,
        (77, 56, 63),
        (ayir_x, y - 4),
        (ayir_x, y + slot_boyut + 4),
        1,
    )

    q_hizli_slot_normalize_et()
    qx = baslangic_x + grup_w + ayirici_bosluk
    q_rect = pygame.Rect(qx, y, q_boyut, q_boyut)
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
        q_rect.x + 11,
        q_rect.y + 10,
        (255, 177, 70) if q_is_magic else SARI,
        mini_font,
        True,
    )
    if q_debug_spell:


        item_ikonu_ciz("fire_magic", q_rect.inflate(-12, -12), False)
        spell_okulu_sembol_ciz(
            "IGNIS",
            pygame.Rect(q_rect.right - 23, q_rect.bottom - 23, 19, 19),
        )
        yazi_yaz(
            "∞",
            q_rect.centerx,
            q_rect.y + 12,
            (255, 238, 178),
            mini_font,
            True,
        )
    elif isinstance(q_item, int) and 0 <= q_item < len(envanter_itemleri):
        item = envanter_itemleri[q_item]
        if isinstance(item, dict):
            item_ikonu_ciz(item.get("id"), q_rect.inflate(-12, -12), False)
            if item.get("spell_school"):
                spell_okulu_sembol_ciz(
                    item.get("spell_school"),
                    pygame.Rect(
                        q_rect.right - 23,
                        q_rect.bottom - 23,
                        19,
                        19,
                    ),
                )



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
# </POTBO_STAGE S0384>

# <POTBO_STAGE S0388>


def one_cikan_atama_penceresi_ciz(panel):
    if one_cikan_atama_item_index is None:
        return
    if not 0 <= one_cikan_atama_item_index < len(envanter_itemleri):
        return
    item = envanter_itemleri[one_cikan_atama_item_index]
    if not isinstance(item, dict):
        return

    modal = pygame.Rect(panel.centerx - 310, panel.centery - 104, 620, 208)
    pygame.draw.rect(ekran, (4, 3, 7), modal)
    pygame.draw.rect(ekran, PARLAK_KIRMIZI, modal, 3)
    yazi_yaz(
        bt("ÖNE ÇIKAN SLOTU SEÇ", "SELECT FEATURED SLOT"),
        modal.centerx,
        modal.y + 34,
        PARLAK_KIRMIZI,
        normal_font,
        True,
    )
    yazi_yaz(
        str(item.get("name", "")),
        modal.centerx,
        modal.y + 66,
        ACIK_GRI,
        mini_font,
        True,
    )

    kutu_w = 88
    bosluk = 20
    toplam = kutu_w * 5 + bosluk * 4
    bas_x = modal.centerx - toplam // 2
    y = modal.y + 96
    mevcut_slot = next(
        (i for i, x in enumerate(one_cikan_slotlar) if x == one_cikan_atama_item_index),
        None,
    )

    for i in range(5):
        rect = pygame.Rect(bas_x + i * (kutu_w + bosluk), y, kutu_w, 76)
        hedef_dolu = one_cikan_slotlar[i] is not None
        pygame.draw.rect(
            ekran,
            (22, 7, 12) if hedef_dolu else (9, 8, 12),
            rect,
        )
        pygame.draw.rect(
            ekran,
            PARLAK_KIRMIZI if i == mevcut_slot else (94, 72, 82),
            rect,
            2 if i == mevcut_slot else 1,
        )
        yazi_yaz(
            str(i + 1),
            rect.centerx,
            rect.y + 16,
            SARI,
            kucuk_font,
            True,
        )
        bagli = one_cikan_slotlar[i]
        if isinstance(bagli, int) and 0 <= bagli < len(envanter_itemleri):
            bagli_item = envanter_itemleri[bagli]
            if isinstance(bagli_item, dict):
                ikon_rect = pygame.Rect(rect.centerx - 20, rect.y + 31, 40, 36)
                item_ikonu_ciz(bagli_item.get("id"), ikon_rect, False)
# </POTBO_STAGE S0388>

# <POTBO_STAGE S0405>







def bildirim_ciz():
    global bildirim_aktif_baslangic

    if not bildirim_kuyrugu:
        return

    simdi = pygame.time.get_ticks()
    if bildirim_aktif_baslangic <= 0:
        bildirim_aktif_baslangic = simdi
    gecen = simdi - bildirim_aktif_baslangic

    if gecen >= bildirim_suresi:
        bildirim_kuyrugu.pop(0)
        bildirim_aktif_baslangic = simdi
        gecen = 0

        if not bildirim_kuyrugu:
            return

    baslangic_y = hud_sol_rect().bottom + 8
    panel_w = 330
    panel_h = 42
    gap = 6

    for index, kayit in enumerate(bildirim_kuyrugu[:4]):
        alpha = 232
        y_ofset = 0

        if isinstance(kayit, dict):
            metin = str(kayit.get("text", ""))
            yazi_rengi = kayit.get("color", BEYAZ)
            cerceve_rengi = kayit.get("border", yazi_rengi)
        else:
            metin = str(kayit)
            yazi_rengi = BEYAZ
            cerceve_rengi = KAN_KIRMIZISI


        if index == 0 and gecen > bildirim_suresi - bildirim_son_fade:
            kalan = max(
                0.0,
                (bildirim_suresi - gecen) / bildirim_son_fade,
            )
            alpha = int(232 * kalan)
            y_ofset = -int((1.0 - kalan) * 8)

        panel = pygame.Rect(
            28,
            baslangic_y + index * (panel_h + gap) + y_ofset,
            panel_w,
            panel_h,
        )

        yuzey = pygame.Surface(panel.size, pygame.SRCALPHA)
        yuzey.fill((11, 9, 14, max(0, alpha)))
        pygame.draw.rect(
            yuzey,
            (*cerceve_rengi, max(0, alpha)),
            yuzey.get_rect(),
            2,
        )
        ekran.blit(yuzey, panel.topleft)

        yazi = kucuk_font.render(metin, True, yazi_rengi).convert_alpha()
        yazi.set_alpha(max(0, alpha))
        yazi_rect = yazi.get_rect(center=panel.center)
        ekran.blit(yazi, yazi_rect)
# </POTBO_STAGE S0405>

# <POTBO_STAGE S0408>


_kan_profil_degerleri = _stage1__kan_profil_degerleri


class PersistentBloodDecal:
    def __init__(self, x, y, scale=None, rotation=None, sprite_index=None):
        self.x = float(x)
        self.y = float(y)
        self.scale = float(scale if scale is not None else random.uniform(0.70, 1.72))
        self.rotation = float(
            rotation if rotation is not None else random.uniform(0.0, 360.0)
        )
        self.sprite_index = int(
            sprite_index
            if sprite_index is not None
            else random.randrange(max(1, len(BLOOD_DECAL_SPRITELERI)))
        )
        self.created_ms = pygame.time.get_ticks()
        self.maggot_next_ms = self.created_ms + random.randint(
            BLOOD_MAGGOT_FIRST_MIN_MS, BLOOD_MAGGOT_FIRST_MAX_MS
        )
        self.maggot_waves = 0

    def ciz(self, silhouette=False):
        sx, sy = dunya_ekran_x(self.x), dunya_ekran_y(self.y)
        if sx < -80 or sx > GENISLIK + 80 or sy < -80 or sy > YUKSEKLIK + 80:
            return
        if BLOOD_DECAL_SPRITELERI:
            src = BLOOD_DECAL_SPRITELERI[
                self.sprite_index % len(BLOOD_DECAL_SPRITELERI)
            ]
            factor = self.scale * KAMERA_YAKINLASTIRMA


            raw_h = max(2, int(src.get_height() * factor))
            qh = max(2, int(round(raw_h / 2.0)) * 2)
            oran = src.get_width() / max(1.0, float(src.get_height()))
            size = (max(2, int(round(qh * oran))), qh)
            qrot = int(round(self.rotation / 15.0)) * 15
            key = (id(src), size, qrot, bool(silhouette))
            img = blood_decal_onbellegi.get(key)
            if img is None:
                img = pygame.transform.scale(src, size)
                img = pygame.transform.rotate(img, qrot)
                if silhouette:
                    mask = pygame.mask.from_surface(img)
                    img = mask.to_surface(
                        setcolor=(142, 0, 12, 220),
                        unsetcolor=(0, 0, 0, 0),
                    ).convert_alpha()
                if len(blood_decal_onbellegi) >= BLOOD_DECAL_CACHE_MAX:
                    for _ in range(min(70, len(blood_decal_onbellegi))):
                        blood_decal_onbellegi.pop(
                            next(iter(blood_decal_onbellegi)),
                            None,
                        )
                blood_decal_onbellegi[key] = img
            ekran.blit(img, img.get_rect(center=(int(sx), int(sy))))
        else:
            pygame.draw.ellipse(
                ekran,
                (112, 0, 14),
                (int(sx) - 5, int(sy) - 2, 10, 4),
            )


class BloodParticle:
    def __init__(self, x, y, planar, guc=1.0, arterial=False):
        self.x = float(x)
        self.y = float(y)
        self.v = pygame.Vector2(planar)
        self.z = random.uniform(4.0, 18.0) * guc
        self.vz = random.uniform(95.0, 190.0) * guc
        self.gravity = random.uniform(330.0, 470.0)
        self.active = True
        self.scale = random.uniform(0.56, 1.18) * min(1.25, guc)
        self.sprite_index = random.randrange(max(1, len(BLOOD_PARTICLE_SPRITELERI)))
        self.arterial = bool(arterial)

    def guncelle(self, dt):
        if not self.active:
            return
        self.x += self.v.x * dt
        self.y += self.v.y * dt
        self.v *= math.exp(-1.65 * dt)
        self.z += self.vz * dt
        self.vz -= self.gravity * dt



        if self.z <= 1.5 and self.vz < 0.0:
            self.z = 0.0
            self.active = False
            kan_lekesi_ekle(
                self.x,
                self.y,
                random.uniform(0.42, 1.15) * self.scale,
            )

    def zemin_katmani_mi(self):
        return self.active and self.z <= BLOOD_PARTICLE_GROUND_Z and self.vz <= 0.0

    def ciz(self, silhouette=False):
        if not self.active:
            return
        sx, sy = (
            dunya_ekran_x(self.x),
            dunya_ekran_y(self.y) - self.z * KAMERA_YAKINLASTIRMA,
        )
        if BLOOD_PARTICLE_SPRITELERI:
            src = BLOOD_PARTICLE_SPRITELERI[
                self.sprite_index % len(BLOOD_PARTICLE_SPRITELERI)
            ]
            factor = self.scale * KAMERA_YAKINLASTIRMA
            size = (
                max(2, int(src.get_width() * factor)),
                max(2, int(src.get_height() * factor)),
            )
            key = (
                "blood_particle_v19",
                id(src),
                size,
                bool(silhouette),
            )
            img = sprite_olcek_onbellegi.get(key)
            if img is None:
                img = pygame.transform.scale(src, size)
                if silhouette:
                    mask = pygame.mask.from_surface(img)
                    img = mask.to_surface(
                        setcolor=(232, 8, 30, 255),
                        unsetcolor=(0, 0, 0, 0),
                    ).convert_alpha()
                sprite_olcek_onbellegi[key] = img
            ekran.blit(img, img.get_rect(center=(int(sx), int(sy))))
        else:
            pygame.draw.circle(
                ekran,
                (226, 7, 28),
                (int(sx), int(sy)),
                max(1, int(2 * self.scale)),
            )


class GoreChunk:
    def __init__(self, kind, x, y, guc=1.0, small=False):
        self.kind = str(kind)
        self.x = float(x)
        self.y = float(y)
        aci = random.uniform(0.0, math.tau)
        hiz = random.uniform(70.0, 185.0) * guc
        self.v = pygame.Vector2(math.cos(aci), math.sin(aci)) * hiz
        self.z = random.uniform(8.0, 22.0)
        self.vz = random.uniform(120.0, 250.0) * guc
        self.rotation = random.uniform(0.0, 360.0)
        self.angular = random.uniform(-280.0, 280.0)
        self.scale = random.uniform(0.28, 0.50) if small else random.uniform(0.46, 0.78)



        kemik_carpani = {
            "ribcage": 0.26,
            "spinal_cord": 0.14,
            "skull": 0.37,
            "leg": 0.55,
            "foot": 0.50,
            "bone_long_a": 0.34,
            "bone_long_b": 0.34,
            "bone_cluster_a": 0.40,
            "bone_cluster_b": 0.40,
        }.get(self.kind, 1.0)
        self.scale *= kemik_carpani


        doku_carpani = {
            "liver": 0.58,
            "intestine": 0.62,
            "organ_mass_a": 0.50,
            "organ_mass_b": 0.50,
            "organ_round_a": 0.56,
            "organ_round_b": 0.56,
            "flesh_shard_a": 0.72,
            "flesh_shard_b": 0.72,
        }.get(self.kind, 1.0)
        self.scale *= doku_carpani
        self.settled = False
        self.bounces = 0
        self.trail_ms = 0
        self.trail_count = 0

    def guncelle(self, dt, simdi):
        if self.settled:
            return
        self.x += self.v.x * dt
        self.y += self.v.y * dt
        self.z += self.vz * dt
        self.vz -= 500.0 * dt
        self.v *= math.exp(-1.35 * dt)
        self.rotation = (self.rotation + self.angular * dt) % 360.0



        if (
            self.trail_count < 2
            and simdi >= self.trail_ms
            and self.v.length_squared() > 1200.0
        ):
            self.trail_ms = int(simdi) + random.randint(150, 240)
            if random.random() < 0.34:
                kan_lekesi_ekle(self.x, self.y, random.uniform(0.24, 0.48))
                self.trail_count += 1
        if self.z <= 0.0 and self.vz < 0.0:
            self.z = 0.0
            self.bounces += 1
            if self.bounces <= 1 and abs(self.vz) > 90.0:
                self.vz = -self.vz * 0.28
                self.v *= 0.64
                self.angular *= 0.55
            else:
                self.settled = True
                self.v.update(0.0, 0.0)
                self.vz = 0.0
                self.angular = 0.0
                kan_lekesi_ekle(self.x, self.y, random.uniform(0.75, 1.35))

    def ciz(self, silhouette=False):
        src = GORE_SPRITELERI.get(self.kind)
        sx = dunya_ekran_x(self.x)
        sy = dunya_ekran_y(self.y) - self.z * KAMERA_YAKINLASTIRMA
        if sx < -100 or sx > GENISLIK + 100 or sy < -100 or sy > YUKSEKLIK + 100:
            return
        if src is None:
            pygame.draw.circle(
                ekran,
                (118, 0, 16),
                (int(sx), int(sy)),
                max(2, int(6 * self.scale)),
            )
            return
        factor = self.scale * KAMERA_YAKINLASTIRMA
        size = (
            max(3, int(src.get_width() * factor)),
            max(3, int(src.get_height() * factor)),
        )


        max_h_world = {
            "skull": 10.0,
            "ribcage": 13.0,
            "spinal_cord": 19.0,
            "leg": 17.0,
            "foot": 9.0,
            "bone_long_a": 16.0,
            "bone_long_b": 16.0,
            "bone_cluster_a": 12.0,
            "bone_cluster_b": 12.0,
            "liver": 12.0,
            "intestine": 16.0,
            "organ_mass_a": 14.0,
            "organ_mass_b": 14.0,
            "organ_round_a": 11.0,
            "organ_round_b": 11.0,
            "flesh_shard_a": 8.0,
            "flesh_shard_b": 8.0,
        }.get(self.kind)
        if max_h_world is not None:
            max_h = max(
                3,
                int(round(max_h_world * KAMERA_YAKINLASTIRMA)),
            )
            if size[1] > max_h:
                oran = max_h / max(1.0, float(size[1]))
                size = (
                    max(3, int(round(size[0] * oran))),
                    max_h,
                )


        qrot = int(round(self.rotation / 15.0)) * 15
        if size[1] > 4:
            qh = max(3, int(round(size[1] / 2.0)) * 2)
            oran = size[0] / max(1.0, float(size[1]))
            size = (max(3, int(round(qh * oran))), qh)
        key = (id(src), size, qrot, bool(silhouette))
        img = gore_sprite_onbellegi.get(key)
        if img is None:
            img = pygame.transform.scale(src, size)
            img = pygame.transform.rotate(img, qrot)
            if silhouette:
                mask = pygame.mask.from_surface(img)
                img = mask.to_surface(
                    setcolor=(205, 5, 25, 255),
                    unsetcolor=(0, 0, 0, 0),
                ).convert_alpha()
            if len(gore_sprite_onbellegi) >= GORE_CACHE_MAX:
                for _ in range(min(220, len(gore_sprite_onbellegi))):
                    gore_sprite_onbellegi.pop(next(iter(gore_sprite_onbellegi)), None)
            gore_sprite_onbellegi[key] = img
        ekran.blit(img, img.get_rect(center=(int(sx), int(sy))))


class BloodMaggot:
    """Yaşlanan kan lekesinin çevresinde kısa mesafede kıvrılan küçük kurtçuk."""

    def __init__(self, decal, simdi):
        self.source_decal = decal
        self.anchor_x = float(decal.x)
        self.anchor_y = float(decal.y)
        aci = random.uniform(0.0, math.tau)
        r = random.uniform(2.0, 18.0) * min(1.35, max(0.75, float(decal.scale)))
        self.x = self.anchor_x + math.cos(aci) * r
        self.y = self.anchor_y + math.sin(aci) * r * 0.62
        self.v = pygame.Vector2(0.0, 0.0)
        self.target = pygame.Vector2(self.x, self.y)
        self.active = True
        self.frame_seed = random.randint(0, 3000)
        self.scale_factor = random.uniform(0.18, 0.25)
        self.speed = random.uniform(3.5, 7.0)
        self.next_target_ms = int(simdi)
        self.life_until = int(simdi) + random.randint(28000, 50000)
        self.phase = random.random() * math.tau

    def _yeni_hedef(self, simdi):
        a = random.uniform(0.0, math.tau)
        r = random.uniform(3.0, 28.0)
        self.target = pygame.Vector2(
            self.anchor_x + math.cos(a) * r,
            self.anchor_y + math.sin(a) * r * 0.62,
        )
        self.next_target_ms = int(simdi) + random.randint(430, 1250)

    def guncelle(self, dt, simdi):
        if not self.active:
            return
        if simdi >= self.life_until:
            self.active = False
            return
        if (
            simdi >= self.next_target_ms
            or pygame.Vector2(self.x, self.y).distance_to(self.target) < 2.0
        ):
            self._yeni_hedef(simdi)
        here = pygame.Vector2(self.x, self.y)
        to = self.target - here
        if to.length_squared() > 0.3:
            d = to.normalize()

            d = d.rotate_rad(math.sin(simdi * 0.011 + self.phase) * 0.22)
            hedef_v = d * self.speed
            self.v += (hedef_v - self.v) * (1.0 - math.exp(-9.0 * dt))
        else:
            self.v *= math.exp(-7.0 * dt)
        self.x += self.v.x * dt
        self.y += self.v.y * dt

    def ciz(self):
        if not self.active:
            return
        sx = dunya_ekran_x(self.x)
        sy = dunya_ekran_y(self.y)
        if sx < -32 or sx > GENISLIK + 32 or sy < -32 or sy > YUKSEKLIK + 32:
            return
        if not BLOOD_WORM_SPRITELERI:
            pygame.draw.ellipse(
                ekran,
                (112, 42, 20),
                (int(sx) - 2, int(sy) - 1, 5, 3),
            )
            return
        simdi = pygame.time.get_ticks()
        frame_ms = 105
        idx = ((simdi + self.frame_seed) // frame_ms) % len(BLOOD_WORM_SPRITELERI)
        frame = BLOOD_WORM_SPRITELERI[idx]
        factor = self.scale_factor * KAMERA_YAKINLASTIRMA
        size = (
            max(2, int(round(frame.get_width() * factor))),
            max(2, int(round(frame.get_height() * factor))),
        )
        flip_x = self.v.x < -0.2
        key = ("blood_maggot_v28", id(frame), size, flip_x)
        img = sprite_olcek_onbellegi.get(key)
        if img is None:
            img = pygame.transform.scale(frame, size)
            if flip_x:
                img = pygame.transform.flip(img, True, False)
            sprite_olcek_onbellegi[key] = img
        ekran.blit(img, img.get_rect(center=(int(sx), int(sy))))


def _v28_maggot_dalgalari_uret(simdi):
    """Kurtçuklar mikro-detaydır; üretim seyrek ve tarama bütçelidir.

    V30'da her frame bütün kalıcı decal listesi geziliyordu. Kan kalıcı olduğundan
    uzun oturumlarda bu O(N) tarama gereksiz CPU tüketiyordu. Burada yaklaşık
    0.9 saniyede bir, en fazla 72 decal incelenir; bir lekede en fazla bir kurtçuk
    olur ve dünyadaki toplam tavan altıdır.
    """
    global blood_maggot_scan_next_ms, blood_maggot_scan_cursor
    if not BLOOD_WORM_SPRITELERI or not blood_decals:
        return
    if int(simdi) < int(blood_maggot_scan_next_ms):
        return
    blood_maggot_scan_next_ms = int(simdi) + 900

    kalan = BLOOD_MAGGOT_MAX - sum(1 for k in blood_maggots if k.active)
    if kalan <= 0:
        return

    n = len(blood_decals)
    tarama = min(n, 72)
    for j in range(tarama):
        idx = (blood_maggot_scan_cursor + j) % n
        decal = blood_decals[idx]
        if simdi < getattr(decal, "maggot_next_ms", 10**18):
            continue
        mevcut = any(
            kurt.active and getattr(kurt, "source_decal", None) is decal
            for kurt in blood_maggots
        )
        if mevcut:
            decal.maggot_next_ms = int(simdi) + random.randint(
                BLOOD_MAGGOT_WAVE_MIN_MS,
                BLOOD_MAGGOT_WAVE_MAX_MS,
            )
            continue


        if random.random() < 0.34:
            blood_maggots.append(BloodMaggot(decal, simdi))
            kalan -= 1
        decal.maggot_waves = int(getattr(decal, "maggot_waves", 0)) + 1
        decal.maggot_next_ms = int(simdi) + random.randint(
            BLOOD_MAGGOT_WAVE_MIN_MS, BLOOD_MAGGOT_WAVE_MAX_MS
        )
        if kalan <= 0:
            break
    blood_maggot_scan_cursor = (blood_maggot_scan_cursor + tarama) % max(1, n)


def blood_maggots_guncelle(dt, simdi):
    _v28_maggot_dalgalari_uret(simdi)
    for kurt in blood_maggots:
        kurt.guncelle(dt, simdi)
    blood_maggots[:] = [k for k in blood_maggots if k.active]


def kan_lekesi_ekle(x, y, scale=None):
    blood_decals.append(PersistentBloodDecal(x, y, scale=scale))


def kan_parcacigi_patlat(x, y, adet, guc=1.0, yon=None, arterial=False):
    base = pygame.Vector2(yon) if yon is not None else pygame.Vector2(1.0, 0.0)
    if base.length_squared() <= 1e-6:
        base = pygame.Vector2(1.0, 0.0)
    base = base.normalize()
    for _ in range(max(0, int(adet))):
        d = base.rotate(
            random.uniform(-58.0, 58.0) if arterial else random.uniform(-110.0, 110.0)
        )
        speed = random.uniform(48.0, 155.0) * guc
        if arterial:
            speed *= 1.34
        blood_particles.append(
            BloodParticle(
                x,
                y,
                d * speed,
                guc=max(0.55, guc),
                arterial=arterial,
            )
        )
# </POTBO_STAGE S0408>

# <POTBO_STAGE S0410>


gore_olum_patlamasi = _stage1_gore_olum_patlamasi


def gore_patlama_infazi(x, y, merkez_x, merkez_y):
    """Patlama ölümü: yoğun anatomik debris + blast yönlü yüksek enerji.

    Parça sayısı özellikle normal ağır ölümden belirgin biçimde fazladır. İlk grup
    okunabilir anatomi, kalan grup küçük et/kemik kırıntısıdır; böylece vahşet artarken
    dev kemik sprite'ları ekranı kaplamaz.
    """
    merkez = pygame.Vector2(float(merkez_x), float(merkez_y))
    kurban = pygame.Vector2(float(x), float(y))
    ana_yon = kurban - merkez
    if ana_yon.length_squared() <= 1e-6:
        ana_yon = pygame.Vector2(1.0, 0.0).rotate(random.uniform(0.0, 360.0))
    ana_yon = ana_yon.normalize()

    kinds = list(GORE_SPRITELERI.keys()) or [
        "liver",
        "intestine",
    ]
    havuz = [
        "intestine",
        "liver",
        "organ_mass_a",
        "organ_mass_b",
        "flesh_shard_a",
        "flesh_shard_b",
        "organ_round_a",
        "organ_round_b",
        "intestine",
        "liver",
        "ribcage",
        "spinal_cord",
        "skull",
        "leg",
        "foot",
        "bone_long_a",
        "bone_long_b",
        "bone_cluster_a",
        "bone_cluster_b",
        "intestine",
        "liver",
        "flesh_shard_a",
        "flesh_shard_b",
    ]
    havuz = [k for k in havuz if k in kinds] or kinds

    adet = random.randint(74, 92)
    for i in range(adet):
        kind = havuz[i % len(havuz)] if i < len(havuz) else random.choice(havuz)
        small = i >= 10 or random.random() < 0.22
        parca = GoreChunk(
            kind,
            x,
            y,
            guc=random.uniform(1.70, 2.35),
            small=small,
        )


        if random.random() < 0.18:
            d = ana_yon.rotate(random.uniform(105.0, 255.0))
        else:
            d = ana_yon.rotate(random.uniform(-78.0, 78.0))
        if d.length_squared() <= 1e-6:
            d = ana_yon
        d = d.normalize()
        hiz = random.uniform(390.0, 760.0) * (0.78 if small else 1.0)
        parca.v = d * hiz
        parca.vz = random.uniform(300.0, 590.0) * (0.88 if small else 1.0)
        parca.angular = random.uniform(-980.0, 980.0)
        gore_chunks.append(parca)


    kan_parcacigi_patlat(x, y - 8.0, random.randint(150, 188), 2.72, yon=ana_yon)

    kan_parcacigi_patlat(
        x,
        y - 10.0,
        random.randint(54, 72),
        3.04,
        yon=ana_yon,
        arterial=True,
    )
    for _ in range(random.randint(18, 24)):
        kan_lekesi_ekle(
            x + random.uniform(-28.0, 28.0),
            y + random.uniform(-20.0, 20.0),
            random.uniform(0.72, 1.72),
        )


def kanli_darbe_efekti(x, y, profil="slash", lethal=False, yon=None):
    parcacik, leke, guc = _kan_profil_degerleri(profil, lethal)

    base = (
        pygame.Vector2(yon)
        if yon is not None
        else pygame.Vector2(
            random.uniform(-1.0, 1.0),
            random.uniform(-0.30, 0.30),
        )
    )
    if base.length_squared() <= 1e-6:
        base = pygame.Vector2(1.0, 0.0).rotate(random.uniform(-35.0, 35.0))
    base = base.normalize()



    if lethal:
        parcacik = int(parcacik * 1.16)
        leke += 4
        guc *= 1.06

    for _ in range(leke):
        ofsx = random.triangular(-18.0, 18.0, random.choice((-6.0, 8.0))) * guc
        ofsy = random.triangular(-10.0, 14.0, 5.0) * guc
        kan_lekesi_ekle(
            x + ofsx,
            y + ofsy,
            random.uniform(0.46, 1.36) * guc,
        )

    kan_parcacigi_patlat(x, y, parcacik, guc, yon=base)

    if lethal:

        kan_parcacigi_patlat(
            x,
            y - random.uniform(2.0, 5.0),
            random.randint(24, 40),
            guc * 1.28,
            yon=base.rotate(random.uniform(-14.0, 14.0)),
            arterial=True,
        )


        kan_parcacigi_patlat(
            x + random.uniform(-2.0, 2.0),
            y - random.uniform(0.0, 4.0),
            random.randint(12, 22),
            guc * 0.92,
            yon=base.rotate(random.choice((-1.0, 1.0)) * random.uniform(42.0, 82.0)),
            arterial=False,
        )


        v73_ground_splatter(
            x,
            y + 2.0,
            base,
            random.randint(18, 26),
            scale_range=(0.22 * guc, 0.72 * guc),
            distance_range=(3.0, 42.0),
            cone_deg=124.0,
            backscatter=0.30,
            source="lethal_ground",
        )


        for _ in range(random.randint(4, 8)):
            kan_lekesi_ekle(
                x + random.uniform(-16.0, 16.0),
                y + random.uniform(-4.0, 16.0),
                random.uniform(0.22, 0.58) * guc,
            )

        gore_olum_patlamasi(x, y, profil, yon=base)
# </POTBO_STAGE S0410>

# <POTBO_STAGE S0413>


def _v30_kucuk_gore_jet(x, y, adet, yon, guc=1.0, organ_agirlikli=True):
    kinds = list(GORE_SPRITELERI.keys()) or [
        "liver",
        "intestine",
    ]
    havuz = (
        [
            "flesh_shard_a",
            "flesh_shard_b",
            "organ_round_a",
            "organ_round_b",
            "intestine",
            "liver",
            "bone_cluster_a",
            "bone_long_a",
            "skull",
        ]
        if organ_agirlikli
        else [
            "flesh_shard_a",
            "flesh_shard_b",
            "bone_cluster_a",
            "bone_long_a",
        ]
    )
    havuz = [k for k in havuz if k in kinds] or kinds
    base = pygame.Vector2(yon)
    if base.length_squared() <= 1e-6:
        base = pygame.Vector2(1.0, 0.0)
    base = base.normalize()
    for i in range(max(0, int(adet))):
        parca = GoreChunk(random.choice(havuz), x, y, guc=guc, small=True)
        d = base.rotate(random.uniform(-70.0, 70.0))
        if random.random() < 0.15:
            d *= -1.0
        parca.v = d.normalize() * random.uniform(130.0, 315.0) * guc
        parca.vz = random.uniform(120.0, 300.0) * guc
        parca.angular = random.uniform(-650.0, 650.0)
        gore_chunks.append(parca)


def _stage1__v30_ozel_olum_ilk_efekti(alt_tur, x, y, yon):
    """Katile özgü ilk ölüm darbesi. True dönerse generic lethal gore atlanır."""
    alt = str(alt_tur or "")
    base = pygame.Vector2(yon)
    if base.length_squared() <= 1e-6:
        base = pygame.Vector2(1.0, 0.0)
    base = base.normalize()
    if alt == "crawler":


        kan_parcacigi_patlat(x, y, random.randint(8, 12), 0.82, yon=base)
        return True
    if alt == "berserker":
        kan_parcacigi_patlat(x, y, random.randint(12, 18), 0.96, yon=base)
        return True
    if alt == "headshot":

        kan_parcacigi_patlat(x, y - 24.0, random.randint(48, 66), 1.52, yon=base)
        _v30_kucuk_gore_jet(x, y - 24.0, random.randint(9, 14), base, 1.24, True)
        return True
    if alt == "tarkard_crush":


        kan_parcacigi_patlat(x, y, random.randint(16, 22), 1.10, yon=base)
        return True
    if alt.startswith("torrmund_"):
        kan_parcacigi_patlat(
            x,
            y - 8.0,
            random.randint(70, 92),
            1.90,
            yon=base,
            arterial=True,
        )
        _v30_kucuk_gore_jet(x, y - 8.0, random.randint(20, 28), base, 1.34, True)
        return True
    return False
# </POTBO_STAGE S0413>

# <POTBO_STAGE S0415>


def gore_patlama_birinci_katman_infazi(x, y, merkez_x, merkez_y):
    """422-428 shell: merkezden zayıf ama yine gerçek parçalama üretir.

    Ana merkez kadar atomize etmez; buna rağmen beden tek parça kalmaz. Görsel
    parçalanmanın önemli kısmı player sprite shard renderer'da olduğundan burada
    entity sayısını kontrol altında tutup anatomi/kan yoğunluğunu koruyoruz.
    """
    merkez = pygame.Vector2(float(merkez_x), float(merkez_y))
    yon = pygame.Vector2(float(x), float(y)) - merkez
    if yon.length_squared() <= 1e-6:
        yon = pygame.Vector2(1.0, 0.0).rotate(random.uniform(0, 360))
    yon = yon.normalize()
    _v30_kucuk_gore_jet(x, y, random.randint(40, 54), yon, 1.55, True)
    kan_parcacigi_patlat(x, y - 8.0, random.randint(104, 132), 2.16, yon=yon)
    kan_parcacigi_patlat(
        x,
        y - 10.0,
        random.randint(32, 44),
        2.34,
        yon=yon,
        arterial=True,
    )
    for _ in range(random.randint(10, 14)):
        kan_lekesi_ekle(
            x + random.uniform(-22, 22),
            y + random.uniform(-15, 15),
            random.uniform(0.55, 1.25),
        )
# </POTBO_STAGE S0415>

# <POTBO_STAGE S0420>


def _stage1_oyuncu_kanli_hasar_kaydi(kaynak_x, kaynak_y, profil, hasar, kaynak_adi=""):
    global oyuncu_son_darbe_profili, oyuncu_son_darbe_kaynagi, oyuncu_olum_gore_uretildi
    global \
        oyuncu_olum_ikiye_bolundu, \
        oyuncu_olum_kesim_acisi, \
        oyuncu_olum_kesim_ofset_orani
    global \
        oyuncu_olum_katil_uid, \
        oyuncu_olum_katil_tur, \
        oyuncu_olum_katil_kan_sonraki_ms
    global oyuncu_olum_turu, oyuncu_olum_ates_seed
    global oyuncu_olum_patlama_seed, oyuncu_olum_patlama_yonu
    global oyuncu_olum_alt_turu, oyuncu_olum_koreografi_seed

    oyuncu_son_darbe_profili = str(profil or "slash")
    oyuncu_son_darbe_kaynagi = str(kaynak_adi or "")
    lethal = oyuncu_hp <= 0 and not oyuncu_olum_gore_uretildi



    if lethal:
        _olum_sarsinti = {
            "light_slash": (4.2, 120),
            "slash": (5.6, 145),
            "medium_blunt": (7.5, 185),
            "medium_slash": (8.2, 195),
            "heavy_blunt": (12.5, 285),
            "heavy_slash": (14.0, 245),
            "magic_heavy": (20.5, 540),
            "burn": (4.8, 170),
        }.get(oyuncu_son_darbe_profili, (5.4, 145))
        kamera_hit_sarsintisi_baslat(*_olum_sarsinti)




    if oyuncu_son_darbe_profili in (
        "burn",
        "fire_burn",
        "magic_burn",
    ):
        if lethal:
            oyuncu_olum_turu = "fire"
            oyuncu_olum_alt_turu = "fire"
            oyuncu_olum_ates_seed = random.randint(1, 2_000_000)
            oyuncu_olum_ikiye_bolundu = False
            oyuncu_olum_gore_uretildi = True


            kan_parcacigi_patlat(
                oyuncu_x,
                oyuncu_y - 7.0,
                random.randint(7, 11),
                0.66,
                yon=pygame.Vector2(
                    oyuncu_x - float(kaynak_x),
                    oyuncu_y - float(kaynak_y),
                ),
            )
            for _ in range(random.randint(1, 2)):
                kan_lekesi_ekle(
                    oyuncu_x + random.uniform(-7.0, 7.0),
                    oyuncu_y + random.uniform(-4.0, 6.0),
                    random.uniform(0.38, 0.70),
                )

            katil = _v24_olum_katil_adayi_bul(kaynak_x, kaynak_y, kaynak_adi)
            if katil is not None:
                oyuncu_olum_katil_uid = str(getattr(katil, "uid", ""))
                oyuncu_olum_katil_tur = str(getattr(katil, "tur", ""))
                oyuncu_olum_katil_kan_sonraki_ms = 0
            else:
                oyuncu_olum_katil_uid = ""
                oyuncu_olum_katil_tur = ""
                oyuncu_olum_katil_kan_sonraki_ms = 0
        return




    if (
        lethal
        and oyuncu_son_darbe_profili == "magic_heavy"
        and str(kaynak_adi)
        in (
            "fire_magic_explosion_core",
            "fire_magic_explosion_inner",
        )
    ):
        merkez_mi = str(kaynak_adi) == "fire_magic_explosion_core"
        oyuncu_olum_turu = "blast_core" if merkez_mi else "blast_inner"
        oyuncu_olum_alt_turu = oyuncu_olum_turu
        oyuncu_olum_ikiye_bolundu = False
        oyuncu_olum_patlama_seed = random.randint(1, 2_000_000)
        blast_yon = pygame.Vector2(
            oyuncu_x - float(kaynak_x),
            oyuncu_y - float(kaynak_y),
        )
        if blast_yon.length_squared() <= 1e-6:
            blast_yon = pygame.Vector2(1.0, 0.0).rotate(random.uniform(0.0, 360.0))
        oyuncu_olum_patlama_yonu = blast_yon.normalize()
        oyuncu_olum_katil_uid = ""
        oyuncu_olum_katil_tur = ""
        oyuncu_olum_katil_kan_sonraki_ms = 0
        if merkez_mi:
            gore_patlama_infazi(oyuncu_x, oyuncu_y - 8.0, kaynak_x, kaynak_y)
        else:
            gore_patlama_birinci_katman_infazi(
                oyuncu_x, oyuncu_y - 8.0, kaynak_x, kaynak_y
            )
        oyuncu_olum_gore_uretildi = True
        return

    yon = pygame.Vector2(oyuncu_x - float(kaynak_x), oyuncu_y - float(kaynak_y))
    if lethal:
        oyuncu_olum_turu = "blood"
        katil = _v24_olum_katil_adayi_bul(kaynak_x, kaynak_y, kaynak_adi)
        if katil is not None:
            oyuncu_olum_katil_uid = str(getattr(katil, "uid", ""))
            oyuncu_olum_katil_tur = str(getattr(katil, "tur", ""))
            oyuncu_olum_katil_kan_sonraki_ms = pygame.time.get_ticks()
            _v30_olum_koreografi_hazirla(
                oyuncu_olum_katil_tur,
                oyuncu_son_darbe_profili,
                kaynak_adi,
            )
        else:
            oyuncu_olum_katil_uid = ""
            oyuncu_olum_katil_tur = ""
            oyuncu_olum_katil_kan_sonraki_ms = 0
            oyuncu_olum_alt_turu = ""
    if (
        lethal
        and oyuncu_son_darbe_profili == "heavy_slash"
        and oyuncu_olum_katil_tur != "torrmund"
    ):
        oyuncu_olum_ikiye_bolundu = True
        oyuncu_olum_kesim_acisi = random.uniform(13.0, 34.0) * random.choice(
            (-1.0, 1.0)
        )
        oyuncu_olum_kesim_ofset_orani = random.uniform(0.46, 0.58)
    ozel = lethal and _v30_ozel_olum_ilk_efekti(
        oyuncu_olum_alt_turu, oyuncu_x, oyuncu_y - 9.0, yon
    )
    if not ozel:
        kanli_darbe_efekti(
            oyuncu_x,
            oyuncu_y - 9.0,
            oyuncu_son_darbe_profili,
            lethal=lethal,
            yon=yon,
        )
    if lethal:
        oyuncu_olum_gore_uretildi = True
# </POTBO_STAGE S0420>

# <POTBO_STAGE S0422>


def kan_gore_dunyasini_temizle():
    global kan_gore_son_guncelleme, blood_maggot_scan_next_ms, blood_maggot_scan_cursor
    blood_particles.clear()
    blood_decals.clear()
    gore_chunks.clear()
    blood_maggots.clear()
    blood_maggot_scan_next_ms = 0
    blood_maggot_scan_cursor = 0
    kan_gore_son_guncelleme = pygame.time.get_ticks()


def kan_gore_guncelle():
    global kan_gore_son_guncelleme
    simdi = pygame.time.get_ticks()
    dt = max(
        0.0,
        min(0.045, (simdi - kan_gore_son_guncelleme) / 1000.0),
    )
    kan_gore_son_guncelleme = simdi
    if dt <= 0.0:
        return
    for p in list(blood_particles):
        p.guncelle(dt)
    blood_particles[:] = [p for p in blood_particles if p.active]
    for parca in gore_chunks:
        parca.guncelle(dt, simdi)
    blood_maggots_guncelle(dt, simdi)


def kan_lekelerini_ciz(silhouette=False):


    marj = 90.0 / max(0.01, KAMERA_YAKINLASTIRMA)
    left = float(kamera_x) - marj
    top = float(kamera_y) - marj
    right = float(kamera_x) + GENISLIK / max(0.01, KAMERA_YAKINLASTIRMA) + marj
    bottom = float(kamera_y) + YUKSEKLIK / max(0.01, KAMERA_YAKINLASTIRMA) + marj
    for leke in blood_decals:
        if left <= leke.x <= right and top <= leke.y <= bottom:
            leke.ciz(silhouette=silhouette)


def kan_et_hedefi_bul(konum, maksimum=520.0):
    """Fare için en yakın besini allocation/sort yapmadan bulur."""
    p = pygame.Vector2(konum)
    max2 = float(maksimum) * float(maksimum)
    best_score = float("inf")
    best = None
    for parca in gore_chunks:
        dx = float(parca.x) - p.x
        dy = float(parca.y) - p.y
        d2 = dx * dx + dy * dy
        if d2 <= max2:
            score = math.sqrt(d2) * 0.62
            if score < best_score:
                best_score = score
                best = (float(parca.x), float(parca.y))
    for leke in blood_decals:
        dx = float(leke.x) - p.x
        dy = float(leke.y) - p.y
        d2 = dx * dx + dy * dy
        if d2 <= max2:
            score = math.sqrt(d2) * 0.94 + 18.0
            if score < best_score:
                best_score = score
                best = (float(leke.x), float(leke.y))
    return pygame.Vector2(best) if best is not None else None
# </POTBO_STAGE S0422>

# <POTBO_STAGE S0464>


dunya_aktorlerini_derinlige_gore_ciz = _stage1_dunya_aktorlerini_derinlige_gore_ciz
# </POTBO_STAGE S0464>

# <POTBO_STAGE S0467>


def duraklatma_menusu_ciz():


    oyun_ekrani_ciz()
    koyu_kaplama(185)

    panel = pygame.Rect(GENISLIK // 2 - 290, 116, 580, 488)

    gotik_panel(panel, PARLAK_KIRMIZI, 245)

    yazi_yaz(
        t("pause_title"),
        panel.centerx,
        panel.y + 62,
        PARLAK_KIRMIZI,
        menu_baslik_font,
        True,
    )

    pygame.draw.line(
        ekran,
        KAN_KIRMIZISI,
        (panel.x + 58, panel.y + 108),
        (panel.right - 58, panel.y + 108),
        1,
    )

    for index, secenek in enumerate(duraklatma_secenekleri()):
        rect = pygame.Rect(
            panel.centerx - 170,
            panel.y + 154 + index * 70,
            340,
            36,
        )
        secili = index == duraklatma_index
        menu_susleme_ciz(rect, secili)
        yazi_yaz(
            secenek,
            rect.centerx,
            rect.centery,
            BEYAZ if secili else (155, 145, 150),
            menu_font if secili else normal_font,
            True,
        )


def standart_onay_penceresi_ciz(soru, secili_index, arka_plan="oyun"):
    """
    Ana menüdeki özel çıkış onayı hariç bütün onay pencerelerinin
    ortak görsel düzeni.
    """

    if arka_plan == "menu":
        varsayilan_gotik_arka_plan()
    else:
        oyun_ekrani_ciz()

    koyu_kaplama(210)

    panel = pygame.Rect(GENISLIK // 2 - 350, 200, 700, 320)

    gotik_panel(panel, PARLAK_KIRMIZI, 250)

    yazi_yaz(
        soru,
        panel.centerx,
        panel.y + 58,
        PARLAK_KIRMIZI,
        normal_font,
        True,
    )

    pygame.draw.line(
        ekran,
        KAN_KIRMIZISI,
        (panel.x + 75, panel.y + 98),
        (panel.right - 75, panel.y + 98),
        1,
    )

    for index, secenek in enumerate([t("yes"), t("no")]):
        rect = pygame.Rect(
            panel.x + 115,
            panel.y + 122 + index * 70,
            panel.width - 230,
            50,
        )

        secili = index == secili_index
        rect = buton_click_anim_rect(rect, secili)

        pygame.draw.rect(
            ekran,
            (62, 4, 16) if secili else (8, 7, 11),
            rect,
            border_radius=0,
        )

        pygame.draw.rect(
            ekran,
            PARLAK_KIRMIZI if secili else GRI,
            rect,
            2 if secili else 1,
            border_radius=0,
        )

        yazi_yaz(
            secenek,
            rect.centerx,
            rect.centery,
            BEYAZ if secili else ACIK_GRI,
            menu_font,
            True,
        )
# </POTBO_STAGE S0467>

# <POTBO_STAGE S0481>


def tam_ayarlar_ciz():
    ayarlar_arka_plani_ciz()

    yazi_yaz(
        t("settings_title"),
        GENISLIK // 2,
        64,
        PARLAK_KIRMIZI,
        menu_baslik_font,
        True,
    )

    kategori_panel = pygame.Rect(58, 118, 270, 540)
    secenek_panel = pygame.Rect(350, 118, 872, 540)
    gotik_panel(kategori_panel, KAN_KIRMIZISI, 244)

    kategoriler = ayar_kategorileri()
    kategori, secenekler = kategoriler[ayar_kategori_index]
    if kategori != "kontroller":
        gotik_panel(secenek_panel, KAN_KIRMIZISI, 244)

    for index, (kategori_adi, _) in enumerate(kategoriler):
        rect = pygame.Rect(
            kategori_panel.x + 24,
            kategori_panel.y + 34 + index * 78,
            kategori_panel.width - 48,
            54,
        )
        secili = index == ayar_kategori_index
        odakta = ayar_odak == "kategori" and secili

        pygame.draw.rect(
            ekran,
            (62, 4, 16) if odakta else ((25, 9, 15) if secili else (8, 7, 11)),
            rect,
        )
        pygame.draw.rect(
            ekran,
            PARLAK_KIRMIZI if odakta else ((120, 12, 32) if secili else (62, 56, 64)),
            rect,
            2 if odakta else 1,
        )
        yazi_yaz(
            ayar_kategori_adi(kategori_adi),
            rect.centerx,
            rect.centery,
            BEYAZ if secili else GRI,
            kucuk_font,
            True,
        )


    if kategori == "kontroller":
        kontrol_atamalari_paneli_ciz(secenek_panel, secenekler)
        return

    yazi_yaz(
        ayar_kategori_adi(kategori),
        secenek_panel.x + 36,
        secenek_panel.y + 34,
        PARLAK_KIRMIZI,
        normal_font,
    )
    pygame.draw.line(
        ekran,
        (92, 14, 28),
        (secenek_panel.x + 36, secenek_panel.y + 64),
        (secenek_panel.right - 36, secenek_panel.y + 64),
        1,
    )

    gorunen_adet = 5
    baslangic = ayar_scrollunu_guncelle(len(secenekler), gorunen_adet)

    for gorunen_index, index in enumerate(
        range(
            baslangic,
            min(len(secenekler), baslangic + gorunen_adet),
        )
    ):
        ayar = secenekler[index]
        rect = pygame.Rect(
            secenek_panel.x + 36,
            secenek_panel.y + 86 + gorunen_index * 82,
            secenek_panel.width - 72,
            66,
        )
        ayar_satiri_ciz(
            rect,
            ayar,
            ayar_odak == "secenek" and index == ayar_index,
        )

    if len(secenekler) > gorunen_adet:
        yazi_yaz(
            f"{ayar_index + 1}/{len(secenekler)}",
            secenek_panel.right - 48,
            secenek_panel.y + 34,
            GRI,
            mini_font,
            True,
        )

    if tus_atama_mesaji and pygame.time.get_ticks() < tus_atama_mesaj_bitis:
        yazi_yaz(
            tus_atama_mesaji,
            secenek_panel.centerx,
            secenek_panel.bottom - 24,
            SARI,
            mini_font,
            True,
        )
# </POTBO_STAGE S0481>

# <POTBO_STAGE S0488>







def credits_ciz():
    varsayilan_gotik_arka_plan()
    koyu_kaplama(190)

    panel = pygame.Rect(190, 48, 900, 624)
    gotik_panel(panel, KAN_KIRMIZISI, 244)


    harf_aralikli_yazi_yaz(
        t("credits_title"),
        panel.centerx,
        panel.y + 48,
        PARLAK_KIRMIZI,
        kucuk_font,
        4,
        True,
    )

    yazi_yaz(
        "PATH OF THE BLOODIED ONE",
        panel.centerx,
        panel.y + 96,
        BEYAZ,
        oyun_buyuk_font,
        True,
    )

    harf_aralikli_yazi_yaz(
        "AGRAPHON STUDIOS",
        panel.centerx,
        panel.y + 132,
        (180, 44, 62),
        mini_font,
        2,
        True,
    )

    cizgi_y = panel.y + 164
    pygame.draw.line(
        ekran,
        (92, 17, 29),
        (panel.x + 72, cizgi_y),
        (panel.centerx - 18, cizgi_y),
        1,
    )
    pygame.draw.polygon(
        ekran,
        PARLAK_KIRMIZI,
        [
            (panel.centerx, cizgi_y - 6),
            (panel.centerx + 6, cizgi_y),
            (panel.centerx, cizgi_y + 6),
            (panel.centerx - 6, cizgi_y),
        ],
    )
    pygame.draw.line(
        ekran,
        (92, 17, 29),
        (panel.centerx + 18, cizgi_y),
        (panel.right - 72, cizgi_y),
        1,
    )

    etiket_x = panel.x + 92
    icerik_x = panel.x + 390


    harf_aralikli_yazi_yaz(
        bt("GELİŞTİRME VE YAPIM", "DEVELOPMENT AND PRODUCTION"),
        etiket_x,
        panel.y + 226,
        (148, 63, 78),
        mini_font,
        1,
        False,
    )

    isimler = ["Agraphon Studios"]
    for index, isim in enumerate(isimler):
        yazi_yaz(
            isim,
            icerik_x,
            panel.y + 202 + index * 42,
            BEYAZ,
            normal_font,
        )

    ayirici_y = panel.y + 346
    pygame.draw.line(
        ekran,
        (64, 30, 39),
        (panel.x + 92, ayirici_y),
        (panel.right - 92, ayirici_y),
        1,
    )

    harf_aralikli_yazi_yaz(
        bt("TEKNOLOJİK ALTYAPI", "TECHNOLOGY STACK"),
        etiket_x,
        panel.y + 410,
        (148, 63, 78),
        mini_font,
        1,
        False,
    )
    yazi_yaz(
        "Python  •  Pygame",
        icerik_x,
        panel.y + 394,
        BEYAZ,
        normal_font,
    )

    pygame.draw.line(
        ekran,
        (64, 30, 39),
        (panel.x + 92, panel.y + 474),
        (panel.right - 92, panel.y + 474),
        1,
    )

    yazi_yaz(
        t("thanks"),
        panel.centerx,
        panel.y + 532,
        ACIK_GRI,
        kucuk_font,
        True,
    )
# </POTBO_STAGE S0488>

# <POTBO_STAGE S0508>


def _stage1_oyuncu_olum_sahnesini_sifirla():
    global \
        oyuncu_olum_baslangic_ms, \
        oyuncu_olum_menu_index, \
        oyuncu_olum_arter_sonraki_ms
    global oyuncu_olum_gore_uretildi, oyuncu_olum_ikiye_bolundu
    global oyuncu_olum_kesim_acisi, oyuncu_olum_kesim_ofset_orani
    global oyuncu_son_darbe_profili, oyuncu_son_darbe_kaynagi
    global \
        oyuncu_olum_katil_uid, \
        oyuncu_olum_katil_tur, \
        oyuncu_olum_katil_kan_sonraki_ms
    global oyuncu_olum_turu, oyuncu_olum_ates_seed
    global oyuncu_olum_patlama_seed, oyuncu_olum_patlama_yonu
    global oyuncu_olum_alt_turu, oyuncu_olum_koreografi_seed
    global oyuncu_olum_koreografi_vuruslari, oyuncu_olum_torrmund_senaryo
    global oyuncu_savunuyor, savunma_zincir_vurus
    global oyuncu_olum_cikis_baslangic_ms, oyuncu_olum_cikis_hedefi
    oyuncu_olum_baslangic_ms = 0
    oyuncu_olum_menu_index = 0
    oyuncu_olum_arter_sonraki_ms = 0
    oyuncu_olum_gore_uretildi = False
    oyuncu_olum_ikiye_bolundu = False
    oyuncu_olum_kesim_acisi = 22.0
    oyuncu_olum_kesim_ofset_orani = 0.52
    oyuncu_son_darbe_profili = "slash"
    oyuncu_son_darbe_kaynagi = ""
    oyuncu_olum_katil_uid = ""
    oyuncu_olum_katil_tur = ""
    oyuncu_olum_katil_kan_sonraki_ms = 0
    oyuncu_olum_turu = "blood"
    oyuncu_olum_ates_seed = 0
    oyuncu_olum_patlama_seed = 0
    oyuncu_olum_patlama_yonu = pygame.Vector2(1.0, 0.0)
    oyuncu_olum_alt_turu = ""
    oyuncu_olum_koreografi_seed = 0
    oyuncu_olum_koreografi_vuruslari.clear()
    oyuncu_olum_torrmund_senaryo = ""
    oyuncu_savunuyor = False
    savunma_zincir_vurus = 0
    oyuncu_olum_cikis_baslangic_ms = 0
    oyuncu_olum_cikis_hedefi = None
# </POTBO_STAGE S0508>

# <POTBO_STAGE S0513>


def oyuncu_olum_durumu_guncelle():
    global \
        oyuncu_olum_baslangic_ms, \
        oyuncu_olum_arter_sonraki_ms, \
        oyuncu_olum_gore_uretildi
    global oyuncu_olum_cikis_baslangic_ms, oyuncu_olum_cikis_hedefi
    global oyun_durumu, oyun_alt_durumu, cikis_index, cikis_donus_durumu
    global load_game_donus_durumu, ana_menu_onay_donus_durumu, ana_menu_onay_index
    global oyuncu_zorlanmis_hiz, oyuncu_zorlanmis_bitis
    global oyuncu_hareket_hiz_vektoru, oyuncu_hareket_ediyor
    global dash_aktif_bitis, dash_aktif_yonu, dash_aktif_son_ease, dash_tus_kilitli
    if oyuncu_hp > 0:
        return
    simdi = pygame.time.get_ticks()
    if oyuncu_olum_baslangic_ms <= 0:
        oyuncu_olum_baslangic_ms = simdi
        oyuncu_olum_arter_sonraki_ms = simdi
        oyuncu_saldiri_durumunu_sifirla()




        oyuncu_hareket_hiz_vektoru.update(0.0, 0.0)
        oyuncu_hareket_ediyor = False
        oyuncu_zorlanmis_hiz.update(0.0, 0.0)
        oyuncu_zorlanmis_bitis = 0
        dash_aktif_bitis = 0
        dash_aktif_yonu = pygame.Vector2(0.0, 0.0)
        dash_aktif_son_ease = 0.0
        dash_tus_kilitli = True

        if not oyuncu_olum_gore_uretildi:
            if oyuncu_olum_turu in (
                "fire",
                "blast_core",
                "blast_inner",
            ):


                oyuncu_olum_gore_uretildi = True
            else:

                kanli_darbe_efekti(
                    oyuncu_x,
                    oyuncu_y - 8,
                    oyuncu_son_darbe_profili,
                    lethal=True,
                )
                oyuncu_olum_gore_uretildi = True


    if oyuncu_olum_cikis_baslangic_ms > 0:
        if simdi - oyuncu_olum_cikis_baslangic_ms >= OLU_CIKIS_FADE_MS:
            hedef = oyuncu_olum_cikis_hedefi
            if hedef == "restart":
                if not oyuncu_olum_restart_yap():


                    oyuncu_olum_cikis_baslangic_ms = 0
                    oyuncu_olum_cikis_hedefi = None
                    load_game_donus_durumu = OYUN
                    oyun_durumu = LOAD_GAME
            elif hedef == "load":


                oyuncu_olum_cikis_baslangic_ms = 0
                oyuncu_olum_cikis_hedefi = None
                load_game_donus_durumu = OYUN
                oyun_durumu = LOAD_GAME
            elif hedef == "main_menu":


                oyuncu_olum_cikis_baslangic_ms = 0
                oyuncu_olum_cikis_hedefi = None
                ana_menu_onay_index = 1
                ana_menu_onay_donus_durumu = OYUN
                oyun_durumu = ANA_MENU_ONAY
            elif hedef == "quit":



                oyuncu_olum_cikis_baslangic_ms = 0
                oyuncu_olum_cikis_hedefi = None
                cikis_index = 1
                cikis_donus_durumu = OYUN
                oyun_durumu = CIKIS_ONAY
        return

    _v30_olum_koreografi_guncelle(simdi)

    if oyuncu_olum_turu == "blood" and simdi >= oyuncu_olum_arter_sonraki_ms:


        oyuncu_olum_arter_sonraki_ms = simdi + random.randint(90, 145)
        ana_yon = _adefo_yon_vektoru(oyuncu_yonu)
        for side in (-1, 1):
            jet_yon = ana_yon.rotate(
                side * random.uniform(8.0, 26.0) + random.uniform(-18.0, 18.0)
            )
            kan_parcacigi_patlat(
                oyuncu_x + random.uniform(-1.5, 1.5),
                oyuncu_y - 12 + random.uniform(-1.0, 2.0),
                random.randint(4, 8),
                random.uniform(0.92, 1.12) if side > 0 else random.uniform(1.04, 1.18),
                yon=jet_yon,
                arterial=True,
            )


def oyuncu_olum_restart_yap():
    """Son yaşayan save'i yükler; blood_decals/gore_chunks bilinçli olarak korunur."""
    global oyun_durumu, oyun_alt_durumu
    if (
        aktif_kayit
        and os.path.exists(aktif_kayit)
        and oyun_yukle(aktif_kayit, gore_koru=True)
    ):
        oyun_alt_durumu = HARITA
        loading_baslat()
        return True
    return False
# </POTBO_STAGE S0513>

# <POTBO_STAGE S0515>


def _v24_katil_silah_kan_noktasi(actor):
    """Silah varsa ucuna, yoksa ön ele yakın yaklaşık dünya noktası döndürür."""
    if actor is None:
        return None
    tur = str(getattr(actor, "tur", ""))
    direction = str(getattr(actor, "direction", "right"))
    yon = _common_enemy_yon_vektoru(direction)
    if yon.length_squared() <= 1e-6:
        yon = pygame.Vector2(1.0, 0.0)
    yon = yon.normalize()



    ileri = {
        "torrmund": 58.0,
        "tarkard": 29.0,
        "berserker": 31.0,
        "headsthrower": 21.0,
        "crawler": 15.0,
    }.get(tur, 22.0)
    yukari = {
        "torrmund": 31.0,
        "tarkard": 27.0,
        "berserker": 23.0,
        "headsthrower": 21.0,
        "crawler": 12.0,
    }.get(tur, 20.0)
    return pygame.Vector2(float(actor.x), float(actor.y) - yukari) + yon * ileri


def _v24_katil_silah_kanini_ciz(actor):
    if oyuncu_olum_turu == "fire":
        return
    """Ölüm ekranında el/silah ucundan sürekli damlayan kanı çizer."""
    nokta = _v24_katil_silah_kan_noktasi(actor)
    if nokta is None:
        return
    sx = float(dunya_ekran_x(nokta.x))
    sy = float(dunya_ekran_y(nokta.y))
    simdi = pygame.time.get_ticks()


    pygame.draw.line(
        ekran,
        (245, 12, 34),
        (int(round(sx)), int(round(sy - 2))),
        (int(round(sx)), int(round(sy + 5))),
        max(1, int(round(2 * KAMERA_YAKINLASTIRMA))),
    )



    periyot = 820.0
    for i, faz in enumerate((0.0, 0.34, 0.68)):
        p = ((simdi / periyot) + faz) % 1.0
        ease = p * p
        y = sy + 5.0 + ease * 24.0
        x = sx + math.sin((p + i) * math.tau) * 1.3
        alpha = 255 if p < 0.88 else int(255 * max(0.0, (1.0 - p) / 0.12))
        r = 2 if p < 0.55 else 1
        katman = pygame.Surface((6, 6), pygame.SRCALPHA)
        pygame.draw.circle(katman, (239, 8, 30, alpha), (3, 3), r)
        ekran.blit(katman, (int(round(x - 3)), int(round(y - 3))))
# </POTBO_STAGE S0515>

# <POTBO_STAGE S0530>


def _stage1_oyuncu_olum_sahnesi_ciz():


    ekran.fill(SIYAH)


    katil = _v24_olum_katil_actor_bul()
    katil_arkada = katil is not None and float(getattr(katil, "y", oyuncu_y)) <= float(
        oyuncu_y
    )
    if katil_arkada:
        _v24_olum_katilini_ciz()

    if oyuncu_olum_turu == "fire":

        kan_lekelerini_ciz(silhouette=True)
        for p in blood_particles:
            p.ciz(silhouette=True)
        _oyuncu_yatay_siluet_ciz()
        _v25_oyuncu_olum_ates_ciz()
    elif oyuncu_olum_turu == "blast_core":

        kan_lekelerini_ciz(silhouette=True)
        for parca in sorted(gore_chunks, key=lambda g: g.y):
            parca.ciz(silhouette=True)
        for p in blood_particles:
            p.ciz(silhouette=True)
        _v26_oyuncu_patlama_siluet_parcalari_ciz()
    elif oyuncu_olum_turu == "blast_inner":

        kan_lekelerini_ciz(silhouette=True)
        for parca in sorted(gore_chunks, key=lambda g: g.y):
            parca.ciz(silhouette=True)
        for p in blood_particles:
            p.ciz(silhouette=True)
        _v30_patlama_birinci_katman_siluet_ciz()
    else:
        kan_lekelerini_ciz(silhouette=True)
        for parca in sorted(gore_chunks, key=lambda g: g.y):
            parca.ciz(silhouette=True)
        for p in blood_particles:
            p.ciz(silhouette=True)
        _oyuncu_yatay_siluet_ciz()

    if katil is not None and not katil_arkada:
        _v24_olum_katilini_ciz()

    if oyuncu_olum_baslangic_ms <= 0:
        return
    simdi = pygame.time.get_ticks()
    gecen = simdi - oyuncu_olum_baslangic_ms
    sahne_fade = min(1.0, max(0.0, gecen / 620.0))
    veil = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    veil.fill((0, 0, 0, int(48 + 58 * sahne_fade)))
    ekran.blit(veil, (0, 0))

    menu_alpha = oyuncu_olum_menu_fade_orani(simdi)
    cikis_p = oyuncu_olum_cikis_orani(simdi)
    if menu_alpha > 0.0:
        layer = _oyuncu_olum_menu_layer_ciz()
        layer.set_alpha(int(round(255 * menu_alpha * (1.0 - cikis_p))))
        ekran.blit(layer, (0, 0))



    if cikis_p > 0.0:
        kapanis = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
        kapanis.fill((0, 0, 0, int(round(255 * cikis_p))))
        ekran.blit(kapanis, (0, 0))
# </POTBO_STAGE S0530>

# <POTBO_STAGE S0572>


def _stage1__v32_patlama_siluet_parcalari_ciz(tur="blast_core"):
    """Bombada sprite yok olmaz; çok sayıda parça balistik uçup zemine yerleşir."""
    sil = _v30_oyuncu_base_siluet()
    if sil is None:
        return
    sw, sh = sil.get_size()
    sx = float(dunya_ekran_x(oyuncu_x))
    sy = float(dunya_ekran_y(oyuncu_y) - 8)
    t = max(
        0.0,
        min(
            5.0,
            (pygame.time.get_ticks() - oyuncu_olum_baslangic_ms) / 1000.0,
        ),
    )
    rng = random.Random(
        int(oyuncu_olum_patlama_seed or 7331) + sum(ord(c) for c in str(tur)) * 41
    )
    base = pygame.Vector2(oyuncu_olum_patlama_yonu)
    if base.length_squared() <= 1e-6:
        base = pygame.Vector2(1.0, 0.0)
    base = base.normalize()

    if tur == "blast_core":
        cols, rows = (
            6,
            5,
        )
        speed_rng = (250.0, 500.0)
        spread = 78.0
        ground_spread = 1.0
    elif tur == "blast_inner":
        cols, rows = 5, 4
        speed_rng = (190.0, 385.0)
        spread = 62.0
        ground_spread = 0.82
    else:
        cols, rows = (
            4,
            3,
        )
        speed_rng = (135.0, 270.0)
        spread = 48.0
        ground_spread = 0.64

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

            rr = random.Random(rng.randint(1, 2_000_000))
            pts = _v32_tirtikli_polygon(
                mw,
                mh,
                mw * 0.5,
                mh * 0.5,
                max(1.0, mw * 0.62),
                max(1.0, mh * 0.62),
                rr,
                nokta=rr.randint(7, 9),
            )
            pygame.draw.polygon(pmask, (255, 255, 255, 255), pts)
            shard.blit(
                pmask,
                (0, 0),
                special_flags=pygame.BLEND_RGBA_MULT,
            )
            if pygame.mask.from_surface(shard).count() <= 0:
                continue

            local_pos = pygame.Vector2(
                (x0 + x1) * 0.5 - sw * 0.5,
                (y0 + y1) * 0.5 - sh * 0.5,
            )
            d = base.rotate(rng.uniform(-spread, spread))
            speed = rng.uniform(*speed_rng) + max(0.0, local_pos.dot(base)) * 1.8
            vx = d.x * speed
            vy = d.y * speed * 0.32 - rng.uniform(70.0, 150.0)
            gravity = rng.uniform(300.0, 420.0)
            ground_y = (
                sy + rng.uniform(11.0, 23.0) + max(-4.0, min(5.0, local_pos.y * 0.10))
            )
            start_y = sy + local_pos.y


            c = start_y - ground_y
            disc = max(0.0, vy * vy - 2.0 * gravity * c)
            land_t = max(
                0.16,
                (-vy + math.sqrt(disc)) / max(1.0, gravity),
            )
            air_t = min(t, land_t)
            px = sx + local_pos.x + vx * air_t
            py = start_y + vy * air_t + 0.5 * gravity * air_t * air_t
            if t > land_t:
                slide_t = min(0.42, t - land_t)
                px += vx * 0.13 * ground_spread * slide_t
                py = ground_y
            rot_t = min(t, land_t + 0.42)
            rot = rng.uniform(-24.0, 24.0) + rng.uniform(-680.0, 680.0) * rot_t
            draw = pygame.transform.rotate(shard, rot)
            ekran.blit(
                draw,
                draw.get_rect(center=(int(round(px)), int(round(py)))),
            )
# </POTBO_STAGE S0572>

# <POTBO_STAGE S0589>





_v32_ozel_ilk_v33 = _v30_ozel_olum_ilk_efekti


def _v30_ozel_olum_ilk_efekti(alt_tur, x, y, yon):
    alt = str(alt_tur or "")
    base = pygame.Vector2(yon)
    if base.length_squared() <= 1e-6:
        base = pygame.Vector2(1.0, 0.0)
    base = base.normalize()

    if alt == "tarkard_crush":


        kan_parcacigi_patlat(
            x,
            y - 6.0,
            random.randint(88, 116),
            1.86,
            yon=base,
            arterial=True,
        )
        _v30_kucuk_gore_jet(x, y - 7.0, random.randint(32, 42), base, 1.44, True)
        for _ in range(random.randint(7, 10)):
            kan_lekesi_ekle(
                x + random.uniform(-18, 18),
                y + random.uniform(-10, 12),
                random.uniform(0.58, 1.28),
            )
        return True

    if alt.startswith("torrmund_"):
        kan_parcacigi_patlat(
            x,
            y - 8.0,
            random.randint(104, 136),
            2.08,
            yon=base,
            arterial=True,
        )
        _v30_kucuk_gore_jet(x, y - 8.0, random.randint(30, 42), base, 1.48, True)
        for _ in range(random.randint(6, 9)):
            kan_lekesi_ekle(
                x + random.uniform(-17, 17),
                y + random.uniform(-9, 11),
                random.uniform(0.55, 1.26),
            )
        return True

    return _v32_ozel_ilk_v33(alt_tur, x, y, yon)
# </POTBO_STAGE S0589>

# <POTBO_STAGE S0592>





def _v33_alpha_crop(full_surface):
    if full_surface is None:
        return None, pygame.Vector2(0.0, 0.0)
    mask = pygame.mask.from_surface(full_surface, 1)
    rects = mask.get_bounding_rects()
    if not rects:
        return None, pygame.Vector2(0.0, 0.0)
    rect = rects[0].copy()
    for r in rects[1:]:
        rect.union_ip(r)
    rect = rect.clip(full_surface.get_rect())
    if rect.width <= 0 or rect.height <= 0:
        return None, pygame.Vector2(0.0, 0.0)
    crop = full_surface.subsurface(rect).copy().convert_alpha()
    local = pygame.Vector2(
        rect.centerx - full_surface.get_width() * 0.5,
        rect.centery - full_surface.get_height() * 0.5,
    )
    return crop, local
# </POTBO_STAGE S0592>

# <POTBO_STAGE S0597>




def _v32_patlama_siluet_parcalari_ciz(tur="blast_core"):
    sil = _v30_oyuncu_base_siluet()
    if sil is None:
        return
    sw, sh = sil.get_size()
    sx = float(dunya_ekran_x(oyuncu_x))
    sy = float(dunya_ekran_y(oyuncu_y) - 8)
    t = max(
        0.0,
        min(
            5.0,
            (pygame.time.get_ticks() - oyuncu_olum_baslangic_ms) / 1000.0,
        ),
    )
    rng = random.Random(
        int(oyuncu_olum_patlama_seed or 7331) + sum(ord(c) for c in str(tur)) * 41
    )
    base = pygame.Vector2(oyuncu_olum_patlama_yonu)
    if base.length_squared() <= 1e-6:
        base = pygame.Vector2(1.0, 0.0)
    base = base.normalize()

    if tur == "blast_core":
        cols, rows = 7, 6
        speed_rng = (285.0, 555.0)
        spread = 82.0
        ground_spread = 1.0
    elif tur == "blast_inner":
        cols, rows = 6, 5
        speed_rng = (215.0, 425.0)
        spread = 66.0
        ground_spread = 0.84
    else:
        cols, rows = 4, 3
        speed_rng = (135.0, 270.0)
        spread = 48.0
        ground_spread = 0.64

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
            rr = random.Random(rng.randint(1, 2_000_000))
            pmask = pygame.Surface((mw, mh), pygame.SRCALPHA)
            pts = _v32_tirtikli_polygon(
                mw,
                mh,
                mw * 0.5,
                mh * 0.5,
                max(1.0, mw * 0.66),
                max(1.0, mh * 0.66),
                rr,
                nokta=rr.randint(8, 11),
            )
            pygame.draw.polygon(pmask, (255, 255, 255, 255), pts)
            shard.blit(
                pmask,
                (0, 0),
                special_flags=pygame.BLEND_RGBA_MULT,
            )
            crop, crop_local = _v33_alpha_crop(shard)
            if crop is None:
                continue

            local_pos = pygame.Vector2(
                (x0 + x1) * 0.5 - sw * 0.5,
                (y0 + y1) * 0.5 - sh * 0.5,
            )

            local_pos += crop_local
            d = base.rotate(rng.uniform(-spread, spread))
            speed = rng.uniform(*speed_rng) + max(0.0, local_pos.dot(base)) * 1.9
            vx = d.x * speed
            vy = d.y * speed * 0.32 - rng.uniform(78.0, 168.0)
            gravity = rng.uniform(315.0, 445.0)
            ground_y = (
                sy + rng.uniform(11.0, 24.0) + max(-4.0, min(5.0, local_pos.y * 0.10))
            )
            start_y = sy + local_pos.y
            c = start_y - ground_y
            disc = max(0.0, vy * vy - 2.0 * gravity * c)
            land_t = max(
                0.16,
                (-vy + math.sqrt(disc)) / max(1.0, gravity),
            )
            air_t = min(t, land_t)
            px = sx + local_pos.x + vx * air_t
            py = start_y + vy * air_t + 0.5 * gravity * air_t * air_t
            if t > land_t:
                slide_t = min(0.44, t - land_t)
                px += vx * 0.13 * ground_spread * slide_t
                py = ground_y
            rot_t = min(t, land_t + 0.44)
            rot = rng.uniform(-28.0, 28.0) + rng.uniform(-760.0, 760.0) * rot_t
            draw = pygame.transform.rotate(crop, rot)
            ekran.blit(
                draw,
                draw.get_rect(center=(int(round(px)), int(round(py)))),
            )
# </POTBO_STAGE S0597>

# <POTBO_STAGE S0600>





def _v33_enemy_blast_extra_gore(dusman, shell_id, merkez):
    if dusman is None:
        return
    x, y = (
        float(getattr(dusman, "x", 0.0)),
        float(getattr(dusman, "y", 0.0)) - 8.0,
    )
    d = pygame.Vector2(x, y) - pygame.Vector2(merkez)
    if d.length_squared() <= 1e-6:
        d = pygame.Vector2(1.0, 0.0).rotate(random.uniform(0, 360))
    d = d.normalize()
    if int(shell_id) == 675:
        _v30_kucuk_gore_jet(x, y, random.randint(38, 52), d, 1.72, True)
        kan_parcacigi_patlat(
            x,
            y,
            random.randint(86, 116),
            2.10,
            yon=d,
            arterial=True,
        )
    elif int(shell_id) == 425:
        _v30_kucuk_gore_jet(x, y, random.randint(24, 34), d, 1.44, True)
        kan_parcacigi_patlat(
            x,
            y,
            random.randint(58, 82),
            1.78,
            yon=d,
            arterial=True,
        )
# </POTBO_STAGE S0600>

# <POTBO_STAGE S0602>





def _stage2_oyuncu_olum_sahnesi_ciz():
    ekran.fill(SIYAH)



    kan_lekelerini_ciz(silhouette=True)
    for p in blood_particles:
        if p.active:
            p.ciz(silhouette=True)


    for parca in sorted(gore_chunks, key=lambda g: g.y):
        parca.ciz(silhouette=True)

    katil = _v24_olum_katil_actor_bul()
    katil_arkada = katil is not None and float(getattr(katil, "y", oyuncu_y)) <= float(
        oyuncu_y
    )
    if katil_arkada:
        _v24_olum_katilini_ciz()

    if oyuncu_olum_turu == "fire":
        _oyuncu_yatay_siluet_ciz()
        _v25_oyuncu_olum_ates_ciz()
    elif oyuncu_olum_turu == "blast_core":
        _v26_oyuncu_patlama_siluet_parcalari_ciz()
    elif oyuncu_olum_turu == "blast_inner":
        _v30_patlama_birinci_katman_siluet_ciz()
    else:
        _oyuncu_yatay_siluet_ciz()

    if katil is not None and not katil_arkada:
        _v24_olum_katilini_ciz()

    if oyuncu_olum_baslangic_ms <= 0:
        return
    simdi = pygame.time.get_ticks()
    gecen = simdi - oyuncu_olum_baslangic_ms
    sahne_fade = min(1.0, max(0.0, gecen / 620.0))
    veil = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    veil.fill((0, 0, 0, int(36 + 42 * sahne_fade)))
    ekran.blit(veil, (0, 0))

    menu_alpha = oyuncu_olum_menu_fade_orani(simdi)
    _v33_gameover_music_tick(menu_alpha)
    cikis_p = oyuncu_olum_cikis_orani(simdi)
    if menu_alpha > 0.0:
        layer = _oyuncu_olum_menu_layer_ciz()
        layer.set_alpha(int(round(255 * menu_alpha * (1.0 - cikis_p))))
        ekran.blit(layer, (0, 0))
    if cikis_p > 0.0:
        kapanis = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
        kapanis.fill((0, 0, 0, int(round(255 * cikis_p))))
        ekran.blit(kapanis, (0, 0))
# </POTBO_STAGE S0602>

# <POTBO_STAGE S0616>


def oyuncu_olum_sahnesi_ciz():
    ekran.fill(SIYAH)



    kan_lekelerini_ciz(silhouette=True)
    for p in blood_particles:
        if p.active:
            p.ciz(silhouette=True)

    for parca in sorted(gore_chunks, key=lambda g: g.y):
        parca.ciz(silhouette=True)

    katil = _v24_olum_katil_actor_bul()
    katil_arkada = katil is not None and float(getattr(katil, "y", oyuncu_y)) <= float(
        oyuncu_y
    )
    if katil_arkada:
        _v24_olum_katilini_ciz()

    if oyuncu_olum_turu == "fire":
        _oyuncu_yatay_siluet_ciz()
        _v25_oyuncu_olum_ates_ciz()
    elif oyuncu_olum_turu == "blast_core":
        _v26_oyuncu_patlama_siluet_parcalari_ciz()
    elif oyuncu_olum_turu == "blast_inner":
        _v30_patlama_birinci_katman_siluet_ciz()
    else:
        _oyuncu_yatay_siluet_ciz()

    if katil is not None and not katil_arkada:
        _v24_olum_katilini_ciz()

    if oyuncu_olum_baslangic_ms <= 0:
        return

    simdi = pygame.time.get_ticks()
    gecen = simdi - oyuncu_olum_baslangic_ms
    sahne_fade = min(1.0, max(0.0, gecen / 620.0))
    veil = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    veil.fill((0, 0, 0, int(36 + 42 * sahne_fade)))
    ekran.blit(veil, (0, 0))

    title_alpha = oyuncu_olum_baslik_fade_orani(simdi)
    _v34_gameover_music_tick(title_alpha, simdi)

    cikis_p = oyuncu_olum_cikis_orani(simdi)
    layer = _oyuncu_olum_menu_layer_ciz()
    if cikis_p > 0.0:
        layer.set_alpha(int(round(255 * (1.0 - cikis_p))))
    ekran.blit(layer, (0, 0))

    if cikis_p > 0.0:
        kapanis = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
        kapanis.fill((0, 0, 0, int(round(255 * cikis_p))))
        ekran.blit(kapanis, (0, 0))
# </POTBO_STAGE S0616>

# <POTBO_STAGE S0618>


def ana_menu_onay_ciz():
    if not (ana_menu_onay_donus_durumu == OYUN and oyuncu_hp <= 0):
        return _v33_ana_menu_onay_ciz_v34()

    oyuncu_olum_sahnesi_ciz()
    koyu_kaplama(210)
    panel = pygame.Rect(GENISLIK // 2 - 350, 200, 700, 320)
    gotik_panel(panel, PARLAK_KIRMIZI, 250)
    yazi_yaz(
        t("main_menu_confirm"),
        panel.centerx,
        panel.y + 58,
        PARLAK_KIRMIZI,
        normal_font,
        True,
    )
    pygame.draw.line(
        ekran,
        KAN_KIRMIZISI,
        (panel.x + 75, panel.y + 98),
        (panel.right - 75, panel.y + 98),
        1,
    )
    for index, secenek in enumerate([t("yes"), t("no")]):
        rect = pygame.Rect(
            panel.x + 115,
            panel.y + 122 + index * 70,
            panel.width - 230,
            50,
        )
        secili = index == ana_menu_onay_index
        pygame.draw.rect(
            ekran,
            (62, 4, 16) if secili else (8, 7, 11),
            rect,
            border_radius=0,
        )
        pygame.draw.rect(
            ekran,
            PARLAK_KIRMIZI if secili else GRI,
            rect,
            2 if secili else 1,
            border_radius=0,
        )
        yazi_yaz(
            secenek,
            rect.centerx,
            rect.centery,
            BEYAZ if secili else ACIK_GRI,
            menu_font,
            True,
        )
# </POTBO_STAGE S0618>

# <POTBO_STAGE S0678>

















V34_ATTACK_BUFFER_MS = 145
# </POTBO_STAGE S0678>

# <POTBO_STAGE S0681>
V34_MAX_BLOOD_PARTICLES = 900
# </POTBO_STAGE S0681>

# <POTBO_STAGE S0795>


def _v34f_echo_segment(slot, center, direction, radius):
    direction = _v34f_direction_safe(direction)
    if slot == 0:

        half = radius * 0.46
        return (
            center - direction * half,
            center + direction * half,
        )
    if slot == 1:
        return (
            center + pygame.Vector2(-radius, radius * 0.78),
            center + pygame.Vector2(radius, -radius * 0.78),
        )
    return (
        center + pygame.Vector2(-radius, -radius * 0.78),
        center + pygame.Vector2(radius, radius * 0.78),
    )


def _v34f_draw_echoes(layer, simdi):
    alive = []
    for born, slot, center, direction, radius in list(v34f_special_echoes):
        age = simdi - born
        if age < 0 or age >= V34F_SPECIAL_ECHO_LIFE_MS:
            continue
        alive.append((born, slot, center, direction, radius))
        t = max(
            0.0,
            min(1.0, age / float(V34F_SPECIAL_ECHO_LIFE_MS)),
        )
        a, b = _v34f_echo_segment(slot, pygame.Vector2(center), direction, radius)
        sa = _v34_world_to_screen_vec(a, -12.0)
        sb = _v34_world_to_screen_vec(b, -12.0)
        strong = max(0.0, 1.0 - age / float(V34F_SPECIAL_ECHO_STRONG_MS))
        fade = (1.0 - t) ** 1.65
        if slot == 0:
            alpha = int(42 * fade)
            pygame.draw.line(layer, (235, 220, 225, alpha), sa, sb, 2)
            continue

        outer_alpha = int((72 + slot * 18) * fade)
        core_alpha = int((112 + slot * 26) * fade * (0.65 + 0.35 * strong))
        pygame.draw.line(
            layer,
            (120, 4, 20, outer_alpha),
            sa,
            sb,
            9 if slot == 2 else 7,
        )
        pygame.draw.line(
            layer,
            (236, 32, 58, int(outer_alpha * 1.18)),
            sa,
            sb,
            4,
        )
        pygame.draw.line(layer, (255, 239, 243, core_alpha), sa, sb, 1)
    v34f_special_echoes.clear()
    v34f_special_echoes.extend(alive)
# </POTBO_STAGE S0795>

# <POTBO_STAGE S0844>





def _v35_flow_hud_ciz():
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA or oyuncu_hp <= 0:
        return
    if v35_combat_flow <= 0.01:
        return
    simdi = pygame.time.get_ticks()
    pulse = 1.0
    if simdi < v35_flow_pulse_until:
        pulse = 1.0 + 0.18 * ((v35_flow_pulse_until - simdi) / 160.0)


    x0 = GENISLIK - 92
    y0 = YUKSEKLIK - 52
    layer = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    full = int(v35_combat_flow)
    frac = max(0.0, min(1.0, v35_combat_flow - full))
    for i in range(3):
        alpha = 38
        if i < full:
            alpha = int(155 * pulse)
        elif i == full and frac > 0:
            alpha = int(38 + 110 * frac)
        a = pygame.Vector2(x0 + i * 18, y0 + 9)
        b = pygame.Vector2(x0 + i * 18 + 11, y0 - 9)
        pygame.draw.line(layer, (126, 8, 24, min(180, alpha)), a, b, 5)
        pygame.draw.line(
            layer,
            (248, 230, 234, min(230, int(alpha * 1.18))),
            a,
            b,
            1,
        )
    ekran.blit(layer, (0, 0))
# </POTBO_STAGE S0844>

# <POTBO_STAGE S0900>
V34_MAX_BLOOD_PARTICLES = 420
# </POTBO_STAGE S0900>

# <POTBO_STAGE S0905>
V37_MAX_VISIBLE_GORE = 96
# </POTBO_STAGE S0905>

# <POTBO_STAGE S0910>
v37_special_gore_next_ms = 0
# </POTBO_STAGE S0910>

# <POTBO_STAGE S0913>



_v37_kan_parcacigi_patlat_original = kan_parcacigi_patlat


def kan_parcacigi_patlat(x, y, adet, guc=1.0, yon=None, arterial=False):
    if v37_special_damage_context:
        adet = max(2, int(round(float(adet) * 0.42)))
        guc = float(guc) * 1.10
    return _v37_kan_parcacigi_patlat_original(
        x, y, adet, guc, yon=yon, arterial=arterial
    )


_v37_gore_olum_patlamasi_original = gore_olum_patlamasi


def gore_olum_patlamasi(x, y, profil="slash", yon=None):
    if v37_special_damage_context:


        return _stage1_gore_olum_patlamasi(x, y, profil, yon=yon)
    return _v37_gore_olum_patlamasi_original(x, y, profil, yon=yon)
# </POTBO_STAGE S0913>

# <POTBO_STAGE S0915>


_v37_kan_gore_guncelle_original = kan_gore_guncelle


def kan_gore_guncelle():


    global v37_special_gore_next_ms
    now = pygame.time.get_ticks()
    if gelistirici_x_skill_aktif_mi(now):
        if now < v37_special_gore_next_ms:
            return
        v37_special_gore_next_ms = now + 33
    else:
        v37_special_gore_next_ms = 0
    return _v37_kan_gore_guncelle_original()
# </POTBO_STAGE S0915>

# <POTBO_STAGE S0934>





def v37_diagnostics():
    base = v36_diagnostics()
    base["v37"] = {
        "version": V37_VERSION,
        "ui_pending": bool(v37_ui_action_pending()),
        "vignette_cache": len(v37_vignette_cache),
        "brightness_cache": 1 if v37_brightness_key is not None else 0,
        "special_trail_budget": int(v34_special_trail.maxlen or 0),
        "special_spark_budget": int(v34f_special_sparks.maxlen or 0),
        "special_ai_pause_frames": int(v37_special_ai_pause_frames),
        "special_static_sanity_ms": int(V37_SPECIAL_STATIC_SANITY_MS),
        "special_layer_size": tuple(V37_SPECIAL_LAYER_SIZE),
        "impact_layer_size": int(V37_IMPACT_LAYER_SIZE),
        "special_gore_tick_ms": 33,
        "special_particle_scale": 0.42,
        "blood_particle_budget": int(V34_MAX_BLOOD_PARTICLES),
        "combat_impact_budget": int(V34_MAX_COMBAT_IMPACTS),
        "visible_gore_budget": int(V37_MAX_VISIBLE_GORE),
        "special_preflight_step": float(V37_SPECIAL_PREFLIGHT_STEP),
        "special_radius_candidates": tuple(float(v) for v in V34_SPECIAL_RADIUS_STEPS),
        "character_select_transition_ms": int(KARAKTER_ONAY_GECIS_SURESI),
    }
    return base
# </POTBO_STAGE S0934>

# <POTBO_STAGE S1049>


BLOOD_MAGGOT_MAX = 4
# </POTBO_STAGE S1049>

# <POTBO_STAGE S1064>


def oyun_yukle(dosya_yolu, gore_koru=False):
    global aktif_diyalog, diyalog_index, diyalog_secim_index
    global diyalog_onemli_item_bekliyor, oyun_alt_durumu, _v39_resource_tick_ms
    ok = _v39_oyun_yukle_original(dosya_yolu, gore_koru=gore_koru)
    if ok:
        aktif_diyalog = []
        diyalog_index = 0
        diyalog_secim_index = 0
        diyalog_onemli_item_bekliyor = False
        if oyun_alt_durumu in (DIYALOG, DIYALOG_SECIM):
            oyun_alt_durumu = HARITA
        _v39_resource_tick_ms = pygame.time.get_ticks()
    return ok
# </POTBO_STAGE S1064>

# <POTBO_STAGE S1069>


class PersistentBloodDecal:
    def __init__(self, x, y, scale=None, rotation=None, sprite_index=None):
        self.x = float(x)
        self.y = float(y)
        self.scale = float(scale if scale is not None else random.uniform(0.70, 1.72))
        self.rotation = float(
            rotation if rotation is not None else random.uniform(0.0, 360.0)
        )
        self.sprite_index = int(
            sprite_index
            if sprite_index is not None
            else random.randrange(max(1, len(BLOOD_DECAL_SPRITELERI)))
        )
        self.created_ms = pygame.time.get_ticks()
        self.maggot_next_ms = self.created_ms + random.randint(
            BLOOD_MAGGOT_FIRST_MIN_MS, BLOOD_MAGGOT_FIRST_MAX_MS
        )
        self.maggot_waves = 0
        yakin = 0
        for onceki in blood_decals[-18:]:
            if (float(onceki.x) - self.x) ** 2 + (
                float(onceki.y) - self.y
            ) ** 2 <= 90.0 * 90.0:
                yakin += 1
        self.cluster_factor = min(10, yakin)
        self.dry_after_ms = self.created_ms + random.randint(95000, 140000)
        self.fade_after_ms = (
            self.created_ms
            + random.randint(255000, 330000)
            + self.cluster_factor * 14000
        )
        self.vanish_after_ms = (
            self.fade_after_ms
            + random.randint(90000, 165000)
            + self.cluster_factor * 16000
        )

    def expired(self, simdi):
        return int(simdi) >= int(self.vanish_after_ms)

    def ciz(self, silhouette=False):
        sx, sy = dunya_ekran_x(self.x), dunya_ekran_y(self.y)
        if sx < -80 or sx > GENISLIK + 80 or sy < -80 or sy > YUKSEKLIK + 80:
            return
        simdi = pygame.time.get_ticks()
        dry_p = v39_clamp01(
            (simdi - self.dry_after_ms)
            / max(
                1.0,
                float(self.fade_after_ms - self.dry_after_ms),
            )
        )
        fade_p = v39_clamp01(
            (simdi - self.fade_after_ms)
            / max(
                1.0,
                float(self.vanish_after_ms - self.fade_after_ms),
            )
        )
        dry_bucket = min(4, int(dry_p * 4.999))
        alpha_bucket = max(
            36,
            min(
                255,
                int(round((255 * (1.0 - 0.86 * fade_p)) / 16.0)) * 16,
            ),
        )
        if BLOOD_DECAL_SPRITELERI:
            src = BLOOD_DECAL_SPRITELERI[
                self.sprite_index % len(BLOOD_DECAL_SPRITELERI)
            ]
            factor = self.scale * KAMERA_YAKINLASTIRMA
            raw_h = max(2, int(src.get_height() * factor))
            qh = max(2, int(round(raw_h / 2.0)) * 2)
            oran = src.get_width() / max(1.0, float(src.get_height()))
            size = (max(2, int(round(qh * oran))), qh)
            qrot = int(round(self.rotation / 15.0)) * 15
            key = (
                "v39_blood",
                id(src),
                size,
                qrot,
                dry_bucket,
                alpha_bucket,
                bool(silhouette),
            )
            img = blood_decal_onbellegi.get(key)
            if img is None:
                img = pygame.transform.scale(src, size)
                img = pygame.transform.rotate(img, qrot)
                if silhouette:
                    mask = pygame.mask.from_surface(img)
                    renk = (142, 0, 12, alpha_bucket)
                    img = mask.to_surface(
                        setcolor=renk, unsetcolor=(0, 0, 0, 0)
                    ).convert_alpha()
                else:
                    renkler = [
                        (255, 255, 255),
                        (206, 156, 156),
                        (152, 106, 86),
                        (96, 66, 56),
                        (58, 38, 34),
                    ]
                    img = img.copy()
                    img.fill(
                        (*renkler[dry_bucket], 255),
                        special_flags=pygame.BLEND_RGBA_MULT,
                    )
                    img.set_alpha(alpha_bucket)
                if len(blood_decal_onbellegi) >= BLOOD_DECAL_CACHE_MAX + 180:
                    for _ in range(min(90, len(blood_decal_onbellegi))):
                        blood_decal_onbellegi.pop(
                            next(iter(blood_decal_onbellegi)),
                            None,
                        )
                blood_decal_onbellegi[key] = img
            ekran.blit(img, img.get_rect(center=(int(sx), int(sy))))
        else:
            renkler = [
                (112, 0, 14),
                (88, 18, 18),
                (72, 30, 28),
                (50, 28, 26),
                (34, 24, 22),
            ]
            surf = pygame.Surface((14, 8), pygame.SRCALPHA)
            pygame.draw.ellipse(
                surf,
                (*renkler[dry_bucket], alpha_bucket),
                surf.get_rect(),
            )
            ekran.blit(surf, (int(sx) - 7, int(sy) - 4))


class BloodMaggot:
    """Daha iri fakat daha az sayıda, kısa menzilli kurtçuk."""

    def __init__(self, decal, simdi):
        self.source_decal = decal
        self.anchor_x = float(decal.x)
        self.anchor_y = float(decal.y)
        aci = random.uniform(0.0, math.tau)
        r = random.uniform(2.0, 16.0) * min(1.38, max(0.82, float(decal.scale)))
        self.x = self.anchor_x + math.cos(aci) * r
        self.y = self.anchor_y + math.sin(aci) * r * 0.62
        self.v = pygame.Vector2(0.0, 0.0)
        self.target = pygame.Vector2(self.x, self.y)
        self.active = True
        self.frame_seed = random.randint(0, 3000)
        self.scale_factor = random.uniform(0.24, 0.34)
        self.speed = random.uniform(2.9, 5.2)
        self.next_target_ms = int(simdi)
        self.life_until = int(simdi) + random.randint(26000, 46000)
        self.phase = random.random() * math.tau

    def _yeni_hedef(self, simdi):
        a = random.uniform(0.0, math.tau)
        r = random.uniform(3.0, 24.0)
        self.target = pygame.Vector2(
            self.anchor_x + math.cos(a) * r,
            self.anchor_y + math.sin(a) * r * 0.62,
        )
        self.next_target_ms = int(simdi) + random.randint(520, 1450)

    def guncelle(self, dt, simdi):
        if not self.active:
            return
        if simdi >= self.life_until or getattr(
            self.source_decal, "expired", lambda _s: False
        )(simdi):
            self.active = False
            return
        if (
            simdi >= self.next_target_ms
            or pygame.Vector2(self.x, self.y).distance_to(self.target) < 2.0
        ):
            self._yeni_hedef(simdi)
        here = pygame.Vector2(self.x, self.y)
        to = self.target - here
        if to.length_squared() > 0.3:
            d = to.normalize().rotate_rad(math.sin(simdi * 0.0105 + self.phase) * 0.24)
            hedef_v = d * self.speed
            self.v += (hedef_v - self.v) * (1.0 - math.exp(-8.0 * dt))
        else:
            self.v *= math.exp(-7.0 * dt)
        self.x += self.v.x * dt
        self.y += self.v.y * dt

    def ciz(self):
        if not self.active:
            return
        sx = dunya_ekran_x(self.x)
        sy = dunya_ekran_y(self.y)
        if sx < -32 or sx > GENISLIK + 32 or sy < -32 or sy > YUKSEKLIK + 32:
            return
        if not BLOOD_WORM_SPRITELERI:
            pygame.draw.ellipse(
                ekran,
                (124, 46, 22),
                (int(sx) - 3, int(sy) - 2, 7, 4),
            )
            return
        simdi = pygame.time.get_ticks()
        frame_ms = 105
        idx = ((simdi + self.frame_seed) // frame_ms) % len(BLOOD_WORM_SPRITELERI)
        frame = BLOOD_WORM_SPRITELERI[idx]
        factor = self.scale_factor * KAMERA_YAKINLASTIRMA
        size = (
            max(3, int(round(frame.get_width() * factor))),
            max(3, int(round(frame.get_height() * factor))),
        )
        flip_x = self.v.x < -0.2
        key = ("blood_maggot_v39", id(frame), size, flip_x)
        img = sprite_olcek_onbellegi.get(key)
        if img is None:
            img = pygame.transform.scale(frame, size)
            if flip_x:
                img = pygame.transform.flip(img, True, False)
            sprite_olcek_onbellegi[key] = img
        ekran.blit(img, img.get_rect(center=(int(sx), int(sy))))


def kan_gore_guncelle():
    global kan_gore_son_guncelleme
    simdi = pygame.time.get_ticks()
    dt = max(
        0.0,
        min(0.045, (simdi - kan_gore_son_guncelleme) / 1000.0),
    )
    kan_gore_son_guncelleme = simdi
    if dt <= 0.0:
        return
    for p in list(blood_particles):
        p.guncelle(dt)
    blood_particles[:] = [p for p in blood_particles if p.active]
    for parca in gore_chunks:
        parca.guncelle(dt, simdi)
    blood_decals[:] = [
        leke
        for leke in blood_decals
        if not getattr(leke, "expired", lambda _s: False)(simdi)
    ]
    blood_maggots_guncelle(dt, simdi)
# </POTBO_STAGE S1069>

# <POTBO_STAGE S1073>


def karakter_olusturma_ciz():
    varsayilan_gotik_arka_plan()
    koyu_kaplama(185)

    yazi_yaz(
        t("create_title"),
        GENISLIK // 2,
        42,
        PARLAK_KIRMIZI,
        menu_baslik_font,
        True,
    )

    erkek_kart = pygame.Rect(45, 92, 315, 545)
    kadin_kart = pygame.Rect(920, 92, 315, 545)
    orta_panel = pygame.Rect(385, 92, 510, 545)

    karakter_karti_ciz(
        erkek_kart,
        "male",
        karakter_cinsiyet == "male",
        karakter_onay_gecisi_aktif and karakter_cinsiyet == "male",
    )
    karakter_karti_ciz(
        kadin_kart,
        "female",
        karakter_cinsiyet == "female",
        karakter_onay_gecisi_aktif and karakter_cinsiyet == "female",
    )

    gotik_panel(orta_panel, KAN_KIRMIZISI, 242)

    yazi_yaz(
        oyuncu_adi,
        orta_panel.centerx,
        140,
        BEYAZ,
        oyun_buyuk_font,
        True,
    )
    pygame.draw.line(
        ekran,
        KAN_KIRMIZISI,
        (orta_panel.x + 48, 178),
        (orta_panel.right - 48, 178),
        1,
    )

    bilgi = KARAKTER_OZGECMISLERI[dil][karakter_cinsiyet]
    about_lines = V39_CHARACTER_ABOUT[dil][karakter_cinsiyet]

    yazi_yaz(
        bilgi["title"],
        orta_panel.centerx,
        214,
        PARLAK_KIRMIZI,
        normal_font,
        True,
    )
    yazi_yaz(
        bilgi["name"],
        orta_panel.centerx,
        248,
        BEYAZ,
        kucuk_font,
        True,
    )

    baslik_renk = SARI
    biyografi_y = 284
    yazi_yaz(
        about_lines[0],
        orta_panel.x + 36,
        biyografi_y,
        baslik_renk,
        mini_font,
    )
    biyografi_y += 26

    biyografi_satirlari = metni_satirlara_bol(
        bilgi["bio"], mini_font, orta_panel.width - 72
    )
    for satir_metni in biyografi_satirlari[:6]:
        yazi_yaz(
            satir_metni,
            orta_panel.centerx,
            biyografi_y,
            ACIK_GRI,
            mini_font,
            True,
        )
        biyografi_y += 18

    biyografi_y += 10
    for satir_metni in about_lines[1:]:
        sar = metni_satirlara_bol("• " + satir_metni, mini_font, orta_panel.width - 72)
        for parca in sar[:2]:
            yazi_yaz(
                parca,
                orta_panel.x + 36,
                biyografi_y,
                BEYAZ,
                mini_font,
            )
            biyografi_y += 18
        biyografi_y += 3

    yazi_yaz(
        bilgi["style"],
        orta_panel.centerx,
        520,
        SARI,
        mini_font,
        True,
    )
    pygame.draw.line(
        ekran,
        (84, 58, 66),
        (orta_panel.x + 36, 542),
        (orta_panel.right - 36, 542),
        1,
    )
    footer = bt(
        "← / → Seç   •   ENTER Başlat   •   ESC Geri",
        "← / → Choose   •   ENTER Start   •   ESC Back",
    )
    yazi_yaz(footer, orta_panel.centerx, 575, BEYAZ, kucuk_font, True)

    if karakter_mesaji:
        yazi_yaz(
            karakter_mesaji,
            GENISLIK // 2,
            656,
            PARLAK_KIRMIZI,
            kucuk_font,
            True,
        )

    if karakter_onay_gecisi_aktif:
        gecen = max(
            0,
            pygame.time.get_ticks() - karakter_onay_gecisi_baslangic,
        )
        fade_sure = max(
            1,
            KARAKTER_ONAY_GECIS_SURESI - KARAKTER_ONAY_FADE_BASLANGICI,
        )
        fade_oran = max(
            0.0,
            min(
                1.0,
                (gecen - KARAKTER_ONAY_FADE_BASLANGICI) / fade_sure,
            ),
        )
        fade_oran = fade_oran * fade_oran * (3.0 - 2.0 * fade_oran)
        if fade_oran > 0.0:
            fade = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
            fade.fill((0, 0, 0, int(round(255 * fade_oran))))
            ekran.blit(fade, (0, 0))
# </POTBO_STAGE S1073>

# <POTBO_STAGE S1075>


V34_MAX_BLOOD_PARTICLES = 300
V37_MAX_VISIBLE_GORE = 72
V40_BLOOD_GRID_CELL = 96.0
V40_BLOOD_PER_CELL_MAX = 20
V40_BLOOD_GLOBAL_MAX = 920
V40_BLOOD_VISIBLE_MAX = 300
V40_BLOOD_CLEANUP_INTERVAL_MS = 2200
V40_BLOOD_SAFE_SEARCH = (0.0, 4.0, 8.0, 12.0)

v40_blood_grid = {}
v40_blood_cleanup_next_ms = 0
v40_gore_cleanup_next_ms = 0





def _v40_rat_sheet_reload():
    yol = mevcut_ilk_dosya(RAT_SHEET_ADAYLARI)
    if not yol:
        return False
    raw = _sprite_sheet_karelerini_cikar(
        yol,
        (0, 255, 0),
        RAT_FRAME_RECTLERI,
        ozel_transparan_rgblar=((0, 128, 128),),
    )
    if len(raw) < 22:
        return False
    for ri, name in enumerate(("right", "left", "down", "up")):
        start = ri * 22
        frames = _kareleri_ortak_canvas_yap(raw[start : start + 22])
        if frames:
            RAT_SPRITELERI[name] = frames
    return True
# </POTBO_STAGE S1075>

# <POTBO_STAGE S1078>


def karakter_olusturma_ciz():
    varsayilan_gotik_arka_plan()
    koyu_kaplama(185)
    yazi_yaz(
        t("create_title"),
        GENISLIK // 2,
        42,
        PARLAK_KIRMIZI,
        menu_baslik_font,
        True,
    )

    erkek_kart = pygame.Rect(45, 92, 315, 545)
    kadin_kart = pygame.Rect(920, 92, 315, 545)
    orta_panel = pygame.Rect(385, 92, 510, 545)

    karakter_karti_ciz(
        erkek_kart,
        "male",
        karakter_cinsiyet == "male",
        karakter_onay_gecisi_aktif and karakter_cinsiyet == "male",
    )
    karakter_karti_ciz(
        kadin_kart,
        "female",
        karakter_cinsiyet == "female",
        karakter_onay_gecisi_aktif and karakter_cinsiyet == "female",
    )
    gotik_panel(orta_panel, KAN_KIRMIZISI, 242)

    yazi_yaz(
        oyuncu_adi,
        orta_panel.centerx,
        128,
        BEYAZ,
        oyun_buyuk_font,
        True,
    )
    pygame.draw.line(
        ekran,
        KAN_KIRMIZISI,
        (orta_panel.x + 48, 166),
        (orta_panel.right - 48, 166),
        1,
    )

    bilgi = KARAKTER_OZGECMISLERI[dil][karakter_cinsiyet]
    yazi_yaz(
        bilgi["title"],
        orta_panel.centerx,
        192,
        PARLAK_KIRMIZI,
        normal_font,
        True,
    )
    yazi_yaz(
        bilgi["name"],
        orta_panel.centerx,
        220,
        BEYAZ,
        kucuk_font,
        True,
    )

    about_label = bt("HAKKINDA", "ABOUT")
    yazi_yaz(about_label, orta_panel.x + 34, 250, SARI, mini_font)



    bio_lines = metni_satirlara_bol(
        bilgi["bio"], v40_char_bio_font, orta_panel.width - 68
    )
    profile_wrapped = []
    for metin in V40_CHARACTER_PROFILE[dil][karakter_cinsiyet]:
        profile_wrapped.extend(
            metni_satirlara_bol(
                "• " + metin,
                v40_char_profile_font,
                orta_panel.width - 70,
            )
        )
        profile_wrapped.append("")
    if profile_wrapped and profile_wrapped[-1] == "":
        profile_wrapped.pop()

    top_y = 274
    profile_header_space = 25
    footer_y = 603
    usable = footer_y - top_y - profile_header_space - 14
    total_lines = len(bio_lines) + len(profile_wrapped)
    line_h = 15 if total_lines <= 17 else 14 if total_lines <= 20 else 13
    y = top_y
    for line in bio_lines:
        yazi_yaz(
            line,
            orta_panel.x + 34,
            y,
            ACIK_GRI,
            v40_char_bio_font,
        )
        y += line_h

    y += 10
    yazi_yaz(
        bt("SAVAŞ PROFİLİ", "COMBAT PROFILE"),
        orta_panel.x + 34,
        y,
        SARI,
        mini_font,
    )
    y += 22
    for line in profile_wrapped:
        if line:
            yazi_yaz(
                line,
                orta_panel.x + 34,
                y,
                BEYAZ,
                v40_char_profile_font,
            )
        y += line_h





    if karakter_mesaji:
        yazi_yaz(
            karakter_mesaji,
            GENISLIK // 2,
            656,
            PARLAK_KIRMIZI,
            kucuk_font,
            True,
        )

    if karakter_onay_gecisi_aktif:
        gecen = max(
            0,
            pygame.time.get_ticks() - karakter_onay_gecisi_baslangic,
        )

        fade_sure = max(
            1,
            KARAKTER_ONAY_GECIS_SURESI - KARAKTER_ONAY_FADE_BASLANGICI,
        )
        fade_oran = max(
            0.0,
            min(
                1.0,
                (gecen - KARAKTER_ONAY_FADE_BASLANGICI) / fade_sure,
            ),
        )
        fade_oran = fade_oran * fade_oran * (3.0 - 2.0 * fade_oran)
        if fade_oran > 0.0:
            fade = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
            fade.fill((0, 0, 0, int(round(255 * fade_oran))))
            ekran.blit(fade, (0, 0))





_v40_kan_gore_temizle_original = kan_gore_dunyasini_temizle


def kan_gore_dunyasini_temizle():
    _v40_kan_gore_temizle_original()
    v40_blood_grid.clear()


def _v40_blood_cell(x, y):
    return (
        int(math.floor(float(x) / V40_BLOOD_GRID_CELL)),
        int(math.floor(float(y) / V40_BLOOD_GRID_CELL)),
    )


def _v40_blood_grid_rebuild():
    v40_blood_grid.clear()
    for leke in blood_decals:
        cell = _v40_blood_cell(leke.x, leke.y)
        v40_blood_grid.setdefault(cell, []).append(leke)


def _v40_blood_nearby(pos, radius):
    p = pygame.Vector2(pos)
    r = max(0.0, float(radius))
    cx0 = int(math.floor((p.x - r) / V40_BLOOD_GRID_CELL))
    cx1 = int(math.floor((p.x + r) / V40_BLOOD_GRID_CELL))
    cy0 = int(math.floor((p.y - r) / V40_BLOOD_GRID_CELL))
    cy1 = int(math.floor((p.y + r) / V40_BLOOD_GRID_CELL))
    out = []
    for cy in range(cy0, cy1 + 1):
        for cx in range(cx0, cx1 + 1):
            out.extend(v40_blood_grid.get((cx, cy), ()))
    return out


def _v40_blood_safe_floor(x, y):
    p = pygame.Vector2(float(x), float(y))
    if not harita_pikseli_engel_mi(p.x, p.y):
        return p

    for radius in V40_BLOOD_SAFE_SEARCH[1:]:
        for angle in range(0, 360, 45):
            q = p + pygame.Vector2(radius, 0).rotate(angle)
            if not harita_pikseli_engel_mi(q.x, q.y):
                return q
    return None


def kan_lekesi_ekle(x, y, scale=None):
    safe = _v40_blood_safe_floor(x, y)
    if safe is None:
        return None
    cell = _v40_blood_cell(safe.x, safe.y)
    bucket = v40_blood_grid.setdefault(cell, [])
    incoming = float(scale if scale is not None else random.uniform(0.70, 1.72))



    if (
        len(bucket) >= V40_BLOOD_PER_CELL_MAX
        or len(blood_decals) >= V40_BLOOD_GLOBAL_MAX
    ):
        if bucket:
            target = min(
                bucket,
                key=lambda d: abs(d.x - safe.x) + abs(d.y - safe.y),
            )
            target.scale = min(2.05, float(target.scale) + incoming * 0.045)
            now = pygame.time.get_ticks()
            if hasattr(target, "fade_after_ms"):
                target.fade_after_ms = max(int(target.fade_after_ms), now + 150000)
            if hasattr(target, "vanish_after_ms"):
                target.vanish_after_ms = max(int(target.vanish_after_ms), now + 300000)
            return target
        return None

    decal = PersistentBloodDecal(safe.x, safe.y, scale=incoming)
    blood_decals.append(decal)
    bucket.append(decal)
    return decal


def kan_lekelerini_ciz(silhouette=False):
    if not blood_decals:
        return
    margin = 90.0 / max(0.01, KAMERA_YAKINLASTIRMA)
    left = float(kamera_x) - margin
    top = float(kamera_y) - margin
    right = float(kamera_x) + GENISLIK / max(0.01, KAMERA_YAKINLASTIRMA) + margin
    bottom = float(kamera_y) + YUKSEKLIK / max(0.01, KAMERA_YAKINLASTIRMA) + margin
    cx0 = int(math.floor(left / V40_BLOOD_GRID_CELL))
    cx1 = int(math.floor(right / V40_BLOOD_GRID_CELL))
    cy0 = int(math.floor(top / V40_BLOOD_GRID_CELL))
    cy1 = int(math.floor(bottom / V40_BLOOD_GRID_CELL))
    visible = []
    for cy in range(cy0, cy1 + 1):
        for cx in range(cx0, cx1 + 1):
            visible.extend(v40_blood_grid.get((cx, cy), ()))
    if len(visible) > V40_BLOOD_VISIBLE_MAX:


        recent = visible[-220:]
        older = visible[:-220]
        if older:
            step = max(
                1,
                len(older) // max(1, V40_BLOOD_VISIBLE_MAX - len(recent)),
            )
            visible = (
                older[::step][: max(0, V40_BLOOD_VISIBLE_MAX - len(recent))] + recent
            )
        else:
            visible = recent
    for leke in visible:
        if left <= leke.x <= right and top <= leke.y <= bottom:
            leke.ciz(silhouette=silhouette)


def kan_et_hedefi_bul(konum, maksimum=520.0):
    """Spatial-grid blood query; gore taraması da son/aktif parçalarla sınırlı."""
    p = pygame.Vector2(konum)
    max2 = float(maksimum) ** 2
    best_score = float("inf")
    best = None
    for parca in gore_chunks[-180:]:
        if getattr(parca, "v40_consumed", False):
            continue
        dx = float(parca.x) - p.x
        dy = float(parca.y) - p.y
        d2 = dx * dx + dy * dy
        if d2 <= max2:
            score = math.sqrt(d2) * 0.62
            if score < best_score:
                best_score = score
                best = (float(parca.x), float(parca.y))
    for leke in _v40_blood_nearby(p, maksimum):
        dx = float(leke.x) - p.x
        dy = float(leke.y) - p.y
        d2 = dx * dx + dy * dy
        if d2 <= max2:
            score = math.sqrt(d2) * 0.94 + 18.0
            if score < best_score:
                best_score = score
                best = (float(leke.x), float(leke.y))
    return pygame.Vector2(best) if best is not None else None
# </POTBO_STAGE S1078>

# <POTBO_STAGE S1080>


class BloodMaggot(_v40_bloodmaggot_parent):
    def __init__(self, decal, simdi):
        super().__init__(decal, simdi)
        self.scale_factor = random.uniform(0.32, 0.44)
        self.speed = random.uniform(2.8, 5.0)





V40_RAT_EDIBLE_GORE = {
    "intestine",
    "liver",
    "organ_mass_a",
    "organ_mass_b",
    "organ_round_a",
    "organ_round_b",
    "flesh_shard_a",
    "flesh_shard_b",
}
# </POTBO_STAGE S1080>

# <POTBO_STAGE S1082>


class AmbientRat(_v40_ambient_rat_parent):
    def __init__(self, x, y, simdi):
        super().__init__(x, y, simdi)
        self.hunger = random.uniform(0.42, 0.92)
        self.smell_refresh_ms = int(simdi) + random.randint(180, 520)
        self.food_kind = None
        self.food_obj = None
        self.feed_until = 0
        self.feed_tick_ms = 0
        self.last_food_pos = pygame.Vector2(self.x, self.y)
        self.curiosity = random.uniform(0.75, 1.25)

    def _food_valid(self):
        obj = self.food_obj
        if obj is None:
            return False
        if self.food_kind == "maggot":
            return bool(getattr(obj, "active", False))
        if self.food_kind == "gore":
            return obj in gore_chunks and not getattr(obj, "v40_consumed", False)
        if self.food_kind == "blood":
            return obj in blood_decals and not getattr(
                obj, "expired", lambda _s: False
            )(pygame.time.get_ticks())
        return False

    def _food_position(self):
        if not self._food_valid():
            return None
        return pygame.Vector2(float(self.food_obj.x), float(self.food_obj.y))

    def _find_food(self, here, simdi):
        candidates = []

        for maggot in blood_maggots:
            if not maggot.active:
                continue
            pos = pygame.Vector2(maggot.x, maggot.y)
            dist = here.distance_to(pos)
            if dist <= 430.0:
                candidates.append((dist * 0.52, "maggot", maggot, pos))


        for gore in gore_chunks[-160:]:
            if getattr(gore, "v40_consumed", False):
                continue
            if str(getattr(gore, "kind", "")) not in V40_RAT_EDIBLE_GORE:
                continue
            pos = pygame.Vector2(float(gore.x), float(gore.y))
            dist = here.distance_to(pos)
            if dist <= 470.0:
                settled_bonus = -18.0 if getattr(gore, "settled", False) else 12.0
                candidates.append(
                    (
                        dist * 0.72 + settled_bonus,
                        "gore",
                        gore,
                        pos,
                    )
                )


        for decal in _v40_blood_nearby(here, 520.0):
            pos = pygame.Vector2(float(decal.x), float(decal.y))
            dist = here.distance_to(pos)
            if dist <= 520.0:
                age = max(
                    0,
                    simdi - int(getattr(decal, "created_ms", simdi)),
                )
                fresh_bonus = -min(35.0, age / 7000.0)
                candidates.append(
                    (
                        dist * 0.96 + 28.0 + fresh_bonus,
                        "blood",
                        decal,
                        pos,
                    )
                )

        if not candidates:
            self.food_kind = None
            self.food_obj = None
            return
        candidates.sort(key=lambda item: item[0])

        best = candidates[0]
        if self.hunger < 0.22 and best[1] == "blood" and random.random() < 0.72:
            self.food_kind = None
            self.food_obj = None
            return
        self.food_kind = best[1]
        self.food_obj = best[2]
        self.last_food_pos = pygame.Vector2(best[3])

    def _consume_tick(self, simdi):
        if not self._food_valid() or simdi < self.feed_tick_ms:
            return
        self.feed_tick_ms = int(simdi) + random.randint(310, 470)
        obj = self.food_obj
        if self.food_kind == "maggot":
            obj.active = False
            self.hunger = max(0.0, self.hunger - 0.34)
            self.feed_until = int(simdi) + 520
            self.food_obj = None
            self.food_kind = None
            return
        if self.food_kind == "gore":
            obj.scale = max(
                0.06,
                float(obj.scale) - random.uniform(0.022, 0.040),
            )
            obj.v40_bites = int(getattr(obj, "v40_bites", 0)) + 1
            self.hunger = max(0.0, self.hunger - 0.055)
            self.feed_until = int(simdi) + 260
            if obj.scale <= 0.11 or obj.v40_bites >= 8:
                obj.v40_consumed = True
                self.food_obj = None
                self.food_kind = None
            return
        if self.food_kind == "blood":
            obj.scale = max(
                0.18,
                float(obj.scale) - random.uniform(0.012, 0.026),
            )
            self.hunger = max(0.0, self.hunger - 0.020)

            obj.fade_after_ms = min(int(obj.fade_after_ms), int(simdi) + 65000)
            obj.vanish_after_ms = min(int(obj.vanish_after_ms), int(simdi) + 125000)
            self.feed_until = int(simdi) + 220
            if obj.scale <= 0.20:
                obj.vanish_after_ms = min(int(obj.vanish_after_ms), int(simdi) + 9000)
                self.food_obj = None
                self.food_kind = None

    def guncelle(self, dt, simdi):
        if not self.active:
            return
        here = pygame.Vector2(self.x, self.y)
        player_dist = here.distance_to((oyuncu_x, oyuncu_y))
        self.hunger = min(1.0, self.hunger + max(0.0, dt) * 0.010)


        if player_dist < 128.0:
            self.food_obj = None
            self.food_kind = None
            self.feed_until = 0
            return super().guncelle(dt, simdi)

        if simdi < self.feed_until:
            self.v *= math.exp(-9.5 * dt)
            self.behavior = "feed"
            self._consume_tick(simdi)
            return

        if simdi >= self.smell_refresh_ms or not self._food_valid():
            self._find_food(here, simdi)
            base = 330 if self.hunger > 0.55 else 520
            self.smell_refresh_ms = int(simdi) + random.randint(base, base + 260)

        food_pos = self._food_position()
        if food_pos is not None:
            self.behavior = "investigate"
            self.target = food_pos
            self.target_refresh_ms = int(simdi) + 850

            self.food_refresh_ms = int(simdi) + 900

        super().guncelle(dt, simdi)
        if not self.active:
            return

        food_pos = self._food_position()
        if food_pos is not None:
            dist = pygame.Vector2(self.x, self.y).distance_to(food_pos)
            threshold = (
                13.0
                if self.food_kind == "maggot"
                else 15.5
                if self.food_kind == "gore"
                else 12.0
            )
            if dist <= threshold:
                self.feed_until = int(simdi) + random.randint(280, 520)
                self.v *= 0.25
                self._consume_tick(simdi)
# </POTBO_STAGE S1082>

# <POTBO_STAGE S1084>


def ambient_rats_guncelle(dt, simdi):
    global v40_gore_cleanup_next_ms
    _v40_ambient_rats_guncelle_original(dt, simdi)
    if simdi >= v40_gore_cleanup_next_ms:
        v40_gore_cleanup_next_ms = int(simdi) + 1200
        gore_chunks[:] = [
            g for g in gore_chunks if not getattr(g, "v40_consumed", False)
        ]





def kan_gore_guncelle():
    global kan_gore_son_guncelleme, v40_blood_cleanup_next_ms
    simdi = pygame.time.get_ticks()
    dt = max(
        0.0,
        min(0.045, (simdi - kan_gore_son_guncelleme) / 1000.0),
    )
    kan_gore_son_guncelleme = simdi
    if dt <= 0.0:
        return
    for p in list(blood_particles):
        p.guncelle(dt)
    blood_particles[:] = [p for p in blood_particles if p.active]
    for parca in gore_chunks:
        if not getattr(parca, "settled", False):
            parca.guncelle(dt, simdi)
    blood_maggots_guncelle(dt, simdi)

    if simdi >= v40_blood_cleanup_next_ms:
        v40_blood_cleanup_next_ms = int(simdi) + V40_BLOOD_CLEANUP_INTERVAL_MS
        if blood_decals:
            blood_decals[:] = [
                d
                for d in blood_decals
                if not getattr(d, "expired", lambda _s: False)(simdi)
            ]
        _v40_blood_grid_rebuild()
# </POTBO_STAGE S1084>

# <POTBO_STAGE S1090>


_v40_blood_grid_rebuild()









V41_VERSION = "41.0"
# </POTBO_STAGE S1090>

# <POTBO_STAGE S1097>





V41_BLOOD_MAX_VERTICAL_SNAP = 2
V41_BLOOD_MERGE_RADIUS = 7.0


def _v40_blood_safe_floor(x, y):
    """Kan lekesinin x koordinatı asla değiştirilmez.

    Önceki V40 4/8/12 px dairesel arama yaptığı için kan başka bir zemine sıçramış
    gibi görünüyordu. V41 yalnız aynı x üzerinde 0..2 px düşey tolerans kullanır.
    Bu da bir pixel-mask sınırındaki küçük yuvarlamayı düzeltmek içindir. Uygun
    zemin yoksa decal yaratılmaz; başka yere taşınmaz.
    """
    x = float(x)
    y = float(y)
    for dy in (0.0, 1.0, 2.0, -1.0):
        if abs(dy) > V41_BLOOD_MAX_VERTICAL_SNAP:
            continue
        py = y + dy
        if not harita_pikseli_engel_mi(x, py):
            return pygame.Vector2(x, py)
    return None


def kan_lekesi_ekle(x, y, scale=None):
    safe = _v40_blood_safe_floor(x, y)
    if safe is None:
        return None

    cell = _v40_blood_cell(safe.x, safe.y)
    bucket = v40_blood_grid.setdefault(cell, [])
    incoming = float(scale if scale is not None else random.uniform(0.70, 1.72))



    nearest = None
    nearest_d2 = V41_BLOOD_MERGE_RADIUS * V41_BLOOD_MERGE_RADIUS
    for decal in bucket:
        dx = float(decal.x) - safe.x
        dy = float(decal.y) - safe.y
        d2 = dx * dx + dy * dy
        if d2 <= nearest_d2:
            nearest_d2 = d2
            nearest = decal

    if nearest is not None and (
        len(bucket) >= V40_BLOOD_PER_CELL_MAX
        or len(blood_decals) >= V40_BLOOD_GLOBAL_MAX
        or random.random() < 0.18
    ):
        nearest.scale = min(2.10, float(nearest.scale) + incoming * 0.035)
        now = pygame.time.get_ticks()
        if hasattr(nearest, "fade_after_ms"):
            nearest.fade_after_ms = max(int(nearest.fade_after_ms), now + 145000)
        if hasattr(nearest, "vanish_after_ms"):
            nearest.vanish_after_ms = max(int(nearest.vanish_after_ms), now + 290000)
        return nearest


    if (
        len(bucket) >= V40_BLOOD_PER_CELL_MAX
        or len(blood_decals) >= V40_BLOOD_GLOBAL_MAX
    ):
        return None

    decal = PersistentBloodDecal(safe.x, safe.y, scale=incoming)
    blood_decals.append(decal)
    bucket.append(decal)
    return decal





def duraklatma_menusu_ciz():
    oyun_ekrani_ciz()
    koyu_kaplama(185)

    panel = pygame.Rect(GENISLIK // 2 - 330, 82, 660, 560)
    gotik_panel(panel, PARLAK_KIRMIZI, 245)

    yazi_yaz(
        t("pause_title"),
        panel.centerx,
        panel.y + 54,
        PARLAK_KIRMIZI,
        menu_baslik_font,
        True,
    )
    pygame.draw.line(
        ekran,
        KAN_KIRMIZISI,
        (panel.x + 62, panel.y + 96),
        (panel.right - 62, panel.y + 96),
        1,
    )

    for index, secenek in enumerate(duraklatma_secenekleri()):
        rect = pygame.Rect(
            panel.centerx - 170,
            panel.y + 126 + index * 62,
            340,
            36,
        )
        secili = index == duraklatma_index
        menu_susleme_ciz(rect, secili)
        yazi_yaz(
            secenek,
            rect.centerx,
            rect.centery,
            BEYAZ if secili else (155, 145, 150),
            menu_font if secili else normal_font,
            True,
        )

    line_y = panel.y + 405
    pygame.draw.line(
        ekran,
        (84, 58, 66),
        (panel.x + 48, line_y),
        (panel.right - 48, line_y),
        1,
    )
    yazi_yaz(
        bt("KONTROL ŞEMASI", "CONTROL SCHEME"),
        panel.centerx,
        line_y + 25,
        SARI,
        mini_font,
        True,
    )

    world_line = bt(
        "E Etkileşim   •   1-5 Öne Çıkan Seç   •   F Kullan   •   Q Hızlı Eşya/Büyü   •   TAB Envanter",
        "E Interact   •   1-5 Select Featured   •   F Use   •   Q Quick Item/Spell   •   TAB Inventory",
    )
    combat_line = bt(
        "J Saldırı / Hold   •   K Savunma   •   SHIFT Dash   •   ENTER/SPACE yalnız arayüz onayı",
        "J Attack / Hold   •   K Block   •   SHIFT Dash   •   ENTER/SPACE confirm UI only",
    )
    yazi_yaz(
        world_line,
        panel.centerx,
        line_y + 52,
        ACIK_GRI,
        mini_font,
        True,
    )
    yazi_yaz(
        combat_line,
        panel.centerx,
        line_y + 76,
        ACIK_GRI,
        mini_font,
        True,
    )
# </POTBO_STAGE S1097>

# <POTBO_STAGE S1100>


def v41_control_snapshot():
    return {
        "version": V41_VERSION,
        "defaults": {
            "interact": tus_gorunen_adi("interact"),
            "featured_use": tus_gorunen_adi("quick_use"),
            "quick_slot": tus_gorunen_adi("q_quick_use"),
            "inventory": tus_gorunen_adi("inventory"),
            "attack": tus_gorunen_adi("attack"),
            "block": tus_gorunen_adi("block"),
            "dash": tus_gorunen_adi("dash"),
        },
        "ui_confirm": [tus_gorunen_adi_deger(k) for k in ONAY_TUSLARI],
        "interact_confirms_general_ui": False,
        "interact_confirms_dialogue": True,
        "blood_radial_relocation": False,
        "blood_vertical_tolerance_px": V41_BLOOD_MAX_VERTICAL_SNAP,
    }
# </POTBO_STAGE S1100>

# <POTBO_STAGE S1102>







V42_BLOOD_MERGE_RADIUS = 5.5
V42_BLOOD_VISIBLE_RECENT = 190
V42_BLOOD_VISIBLE_OLDER = max(0, V40_BLOOD_VISIBLE_MAX - V42_BLOOD_VISIBLE_RECENT)


def _v40_blood_safe_floor(x, y):
    """Kan yalnız düştüğü dünya noktasına yerleşir; hiçbir snap/projection yoktur."""
    x = float(x)
    y = float(y)
    if harita_pikseli_engel_mi(x, y):
        return None
    return pygame.Vector2(x, y)


def _v42_blood_render_key(decal):
    key = getattr(decal, "v42_render_key", None)
    if key is not None:
        return int(key)

    xi = int(round(float(decal.x) * 17.0))
    yi = int(round(float(decal.y) * 19.0))
    created = int(getattr(decal, "created_ms", 0))
    sprite = int(getattr(decal, "sprite_index", 0))
    key = (
        (xi * 73856093) ^ (yi * 19349663) ^ (created * 83492791) ^ (sprite * 2654435761)
    ) & 0x7FFFFFFF
    decal.v42_render_key = key
    return key


def kan_lekesi_ekle(x, y, scale=None):
    """Yere oturduktan sonra hiçbir kan lekesinin geometrisi değişmez."""
    safe = _v40_blood_safe_floor(x, y)
    if safe is None:
        return None

    cell = _v40_blood_cell(safe.x, safe.y)
    bucket = v40_blood_grid.setdefault(cell, [])
    incoming = float(scale if scale is not None else random.uniform(0.70, 1.72))

    nearest = None
    nearest_d2 = V42_BLOOD_MERGE_RADIUS * V42_BLOOD_MERGE_RADIUS
    for decal in bucket:
        dx = float(decal.x) - safe.x
        dy = float(decal.y) - safe.y
        d2 = dx * dx + dy * dy
        if d2 <= nearest_d2:
            nearest_d2 = d2
            nearest = decal



    if nearest is not None and (
        len(bucket) >= V40_BLOOD_PER_CELL_MAX
        or len(blood_decals) >= V40_BLOOD_GLOBAL_MAX
        or random.random() < 0.20
    ):
        now = pygame.time.get_ticks()
        nearest.v42_stain_mass = min(
            5.0,
            float(getattr(nearest, "v42_stain_mass", 1.0)) + incoming * 0.13,
        )
        if hasattr(nearest, "fade_after_ms"):
            nearest.fade_after_ms = max(
                int(nearest.fade_after_ms),
                now + int(140000 + nearest.v42_stain_mass * 10000),
            )
        if hasattr(nearest, "vanish_after_ms"):
            nearest.vanish_after_ms = max(
                int(nearest.vanish_after_ms),
                now + int(275000 + nearest.v42_stain_mass * 16000),
            )
        return nearest

    if (
        len(bucket) >= V40_BLOOD_PER_CELL_MAX
        or len(blood_decals) >= V40_BLOOD_GLOBAL_MAX
    ):
        return None

    decal = PersistentBloodDecal(safe.x, safe.y, scale=incoming)
    decal.v42_stain_mass = 1.0
    _v42_blood_render_key(decal)
    blood_decals.append(decal)
    bucket.append(decal)
    return decal


def kan_lekelerini_ciz(silhouette=False):
    """Bütçe aşımında eski lekeler stabil seçilir; sampling deseni her yeni damlada zıplamaz."""
    if not blood_decals:
        return
    margin = 90.0 / max(0.01, KAMERA_YAKINLASTIRMA)
    left = float(kamera_x) - margin
    top = float(kamera_y) - margin
    right = float(kamera_x) + GENISLIK / max(0.01, KAMERA_YAKINLASTIRMA) + margin
    bottom = float(kamera_y) + YUKSEKLIK / max(0.01, KAMERA_YAKINLASTIRMA) + margin
    cx0 = int(math.floor(left / V40_BLOOD_GRID_CELL))
    cx1 = int(math.floor(right / V40_BLOOD_GRID_CELL))
    cy0 = int(math.floor(top / V40_BLOOD_GRID_CELL))
    cy1 = int(math.floor(bottom / V40_BLOOD_GRID_CELL))
    visible = []
    for cy in range(cy0, cy1 + 1):
        for cx in range(cx0, cx1 + 1):
            visible.extend(v40_blood_grid.get((cx, cy), ()))

    if len(visible) > V40_BLOOD_VISIBLE_MAX:


        visible_by_age = sorted(
            visible,
            key=lambda d: int(getattr(d, "created_ms", 0)),
            reverse=True,
        )
        recent = visible_by_age[:V42_BLOOD_VISIBLE_RECENT]
        older = visible_by_age[V42_BLOOD_VISIBLE_RECENT:]
        older.sort(key=_v42_blood_render_key)
        visible = recent + older[:V42_BLOOD_VISIBLE_OLDER]

    for leke in visible:
        if left <= leke.x <= right and top <= leke.y <= bottom:
            leke.ciz(silhouette=silhouette)
# </POTBO_STAGE S1102>

# <POTBO_STAGE S1108>



def v42_blood_geometry_snapshot(limit=24):
    out = []
    for decal in blood_decals[-max(1, int(limit)) :]:
        out.append(
            (
                round(float(decal.x), 3),
                round(float(decal.y), 3),
                round(float(decal.scale), 4),
                round(float(decal.rotation), 3),
                int(decal.sprite_index),
                round(
                    float(getattr(decal, "v42_stain_mass", 1.0)),
                    3,
                ),
            )
        )
    return out
# </POTBO_STAGE S1108>

# <POTBO_STAGE S1111>









V43_BLOOD_DRY_MIN_MS = 7 * 60 * 1000
V43_BLOOD_DRY_MAX_MS = 11 * 60 * 1000
V43_BLOOD_FADE_MIN_MS = 22 * 60 * 1000
V43_BLOOD_FADE_MAX_MS = 32 * 60 * 1000
V43_BLOOD_VANISH_EXTRA_MIN_MS = 24 * 60 * 1000
V43_BLOOD_VANISH_EXTRA_MAX_MS = 38 * 60 * 1000

_v43_blood_decal_init_original = PersistentBloodDecal.__init__


def _v43_blood_decal_init(self, *args, **kwargs):
    _v43_blood_decal_init_original(self, *args, **kwargs)
    created = int(getattr(self, "created_ms", pygame.time.get_ticks()))
    cluster = max(0, min(10, int(getattr(self, "cluster_factor", 0))))
    self.dry_after_ms = created + random.randint(
        V43_BLOOD_DRY_MIN_MS, V43_BLOOD_DRY_MAX_MS
    )
    self.fade_after_ms = (
        created
        + random.randint(V43_BLOOD_FADE_MIN_MS, V43_BLOOD_FADE_MAX_MS)
        + cluster * 70_000
    )
    self.vanish_after_ms = (
        self.fade_after_ms
        + random.randint(
            V43_BLOOD_VANISH_EXTRA_MIN_MS,
            V43_BLOOD_VANISH_EXTRA_MAX_MS,
        )
        + cluster * 95_000
    )


PersistentBloodDecal.__init__ = _v43_blood_decal_init
# </POTBO_STAGE S1111>

# <POTBO_STAGE S1116>


def v43_camera_zoom_cycle():
    global KAMERA_YAKINLASTIRMA
    current = float(KAMERA_YAKINLASTIRMA)
    next_zoom = V43_CAMERA_ZOOM_STEPS[0]
    for step in V43_CAMERA_ZOOM_STEPS:
        if step > current + 0.035:
            next_zoom = step
            break
    else:

        next_zoom = V43_CAMERA_ZOOM_STEPS[0]

    KAMERA_YAKINLASTIRMA = min(V43_CAMERA_ZOOM_MAX, float(next_zoom))
    _v43_camera_recenter()


    sprite_olcek_onbellegi.clear()
    blood_decal_onbellegi.clear()
    gore_sprite_onbellegi.clear()
    try:
        sprite_parlama_alpha_onbellegi.clear()
    except Exception:
        pass

    bildirim_goster(
        bt(
            f"Geliştirici kamera: {KAMERA_YAKINLASTIRMA:.2f}x"
            + (
                " — sonraki Ctrl+1 sıfırlar"
                if KAMERA_YAKINLASTIRMA >= V43_CAMERA_ZOOM_MAX
                else ""
            ),
            f"Developer camera: {KAMERA_YAKINLASTIRMA:.2f}x"
            + (
                " — next Ctrl+1 resets"
                if KAMERA_YAKINLASTIRMA >= V43_CAMERA_ZOOM_MAX
                else ""
            ),
        ),
        SARI,
    )
    return KAMERA_YAKINLASTIRMA
# </POTBO_STAGE S1116>

# <POTBO_STAGE S1121>


def v43_diagnostics():
    return {
        "version": V43_VERSION,
        "camera_zoom": float(KAMERA_YAKINLASTIRMA),
        "camera_zoom_max": float(V43_CAMERA_ZOOM_MAX),
        "melee_ready_slot": dict(V43_MELEE_READY_SLOT),
        "startup_root": {
            k: float(V38_ENEMY_START_ROOT[k])
            for k in (
                "crawler",
                "berserker",
                "tarkard",
                "torrmund",
            )
        },
        "active_root": {
            k: float(V38_ENEMY_ACTIVE_ROOT_STRICT[k])
            for k in (
                "crawler",
                "berserker",
                "tarkard",
                "torrmund",
            )
        },
        "blood_dry_minutes": (
            V43_BLOOD_DRY_MIN_MS / 60000.0,
            V43_BLOOD_DRY_MAX_MS / 60000.0,
        ),
        "blood_fade_minutes": (
            V43_BLOOD_FADE_MIN_MS / 60000.0,
            V43_BLOOD_FADE_MAX_MS / 60000.0,
        ),
    }
# </POTBO_STAGE S1121>

# <POTBO_STAGE S1123>




V44_BLOOD_PALETTE = (
    (44, 1, 5),
    (52, 2, 7),
    (60, 2, 8),
    (67, 3, 9),
    (74, 3, 11),
    (82, 4, 12),
    (91, 5, 14),
    (101, 5, 16),
    (111, 6, 18),
    (121, 7, 20),
    (132, 8, 22),
    (145, 10, 25),
)
# </POTBO_STAGE S1123>

# <POTBO_STAGE S1125>

V44_BLOOD_MAX_PARTICLES = 430
V44_BLOOD_MICRODROP_LIMIT = 70
V44_BLOOD_WHITE_GLINT_ALPHA = 210
V44_BLOOD_WHITE_GLINT_MIN_SPEED = 135.0
V44_BLOOD_STREAK_SPEED = 245.0
V44_BLOOD_LONGITUDINAL_SPEED = 520.0
V44_BLOOD_FAST_KILL_SPEED = 650.0
V44_BLOOD_SLOW_KILL_SPEED = 330.0
V44_BLOOD_DECAL_GLOSS_LIFE_MS = 8 * 60 * 1000
V44_BLOOD_WET_SHEEN_LIFE_MS = 13 * 60 * 1000
V44_BLOOD_AIR_DRAG = 1.28
V44_BLOOD_SURFACE_TENSION = 0.73
V44_BLOOD_COHESION_BREAK_SPEED = 540.0
V44_BLOOD_PULSE_INTERVAL = (78, 132)
# </POTBO_STAGE S1125>

# <POTBO_STAGE S1128>
V44_BLOOD_ASYMMETRY_BIAS = 0.62
# </POTBO_STAGE S1128>

# <POTBO_STAGE S1131>




v44_blood_context_stack = []
# </POTBO_STAGE S1131>

# <POTBO_STAGE S1136>
v44_last_blood_debug = {}
v44_blood_debug_overlay = False
# </POTBO_STAGE S1136>

# <POTBO_STAGE S1139>


def v44_context_current():
    if not v44_blood_context_stack:
        return None
    return v44_blood_context_stack[-1]


def v44_context_push(context):
    v44_blood_context_stack.append(dict(context or {}))


def v44_context_pop():
    if v44_blood_context_stack:
        return v44_blood_context_stack.pop()
    return None
# </POTBO_STAGE S1139>

# <POTBO_STAGE S1142>


def v44_impact_shape_from_speed(speed, lethal=False, arterial=False):
    """Hızlı kesik -> uzunlamasına; yavaş/az moment -> dairesel ama asimetrik."""
    speed = max(0.0, float(speed))
    if arterial:
        return "arterial_jet"
    if speed >= V44_BLOOD_FAST_KILL_SPEED:
        return "longitudinal"
    if speed <= V44_BLOOD_SLOW_KILL_SPEED:
        return "radial_asymmetric"
    q = v44_clamp01(
        (speed - V44_BLOOD_SLOW_KILL_SPEED)
        / max(
            1.0,
            V44_BLOOD_FAST_KILL_SPEED - V44_BLOOD_SLOW_KILL_SPEED,
        )
    )
    if lethal and q > 0.62:
        return "longitudinal"
    if q < 0.36:
        return "radial_asymmetric"
    return "fan_asymmetric"
# </POTBO_STAGE S1142>

# <POTBO_STAGE S1144>


def v44_blood_palette_for(arterial=False, oxygenation=None, age01=0.0, clot=False):
    if clot:
        palette = V44_CLOTTED_PALETTE
    elif arterial:
        palette = V44_ARTERIAL_PALETTE
    elif oxygenation is not None and float(oxygenation) < 0.42:
        palette = V44_VENOUS_PALETTE
    else:
        palette = V44_BLOOD_PALETTE
    idx = random.randrange(len(palette))
    if age01 > 0.0:
        idx = max(0, idx - int(round(v44_clamp01(age01) * 3.0)))
    return tuple(palette[idx])
# </POTBO_STAGE S1144>

# <POTBO_STAGE S1146>


class V44BloodParticle(BloodParticle):
    """Procedural dark-blood particle with velocity-aware morphology.

    Sprite kaynakları hâlâ fallback olabilir; ancak görünür damla şekli procedural
    çizildiği için tek atlasın renk/şekil tekrarına bağımlı değildir. Her damla kendi
    hematokrit proxy'si, oksijenlenme, viskozite ve yüzey gerilimi taşır.
    """

    def __init__(
        self,
        x,
        y,
        planar,
        guc=1.0,
        arterial=False,
        profile="slash",
        shape="fan_asymmetric",
        oxygenation=None,
        micro=False,
        parent_speed=0.0,
    ):
        super().__init__(x, y, planar, guc=guc, arterial=arterial)
        self.profile = str(profile)
        self.shape = str(shape)
        self.micro = bool(micro)
        self.oxygenation = float(
            oxygenation
            if oxygenation is not None
            else random.uniform(0.68, 0.96)
            if arterial
            else random.uniform(0.26, 0.72)
        )
        self.viscosity = v44_profile_viscosity(profile) * random.uniform(0.86, 1.18)
        self.hematocrit = random.uniform(0.38, 0.52)
        self.surface_tension = V44_BLOOD_SURFACE_TENSION * random.uniform(0.88, 1.12)
        self.cohesion = random.uniform(0.58, 0.98)
        self.wetness = random.uniform(0.88, 1.0)
        self.tone = v44_blood_palette_for(
            arterial=arterial, oxygenation=self.oxygenation
        )
        self.highlight_phase = random.uniform(0.0, math.tau)
        self.highlight_side = random.choice((-1, 1))
        self.stretch_bias = random.uniform(0.78, 1.28)
        self.drag_bias = random.uniform(0.88, 1.14)
        self.breakup_done = bool(micro)
        self.parent_speed = float(parent_speed)
        self.age = 0.0
        self.max_age = random.uniform(1.8, 3.4) if micro else random.uniform(2.5, 4.6)
        self.scale *= random.uniform(0.72, 1.12)
        if self.micro:
            self.scale *= random.uniform(0.35, 0.62)
            self.z *= random.uniform(0.72, 1.05)
            self.vz *= random.uniform(0.70, 1.02)
        if self.shape == "longitudinal":
            self.vz *= random.uniform(0.78, 0.98)
        elif self.shape == "radial_asymmetric":
            self.vz *= random.uniform(1.02, 1.28)

    def _breakup_possible(self):
        speed = self.v.length()
        return (
            not self.breakup_done
            and not self.micro
            and speed >= V44_BLOOD_COHESION_BREAK_SPEED
            and self.z > 4.0
            and self.cohesion < 0.82
            and len(blood_particles) < V44_BLOOD_MAX_PARTICLES - 4
        )

    def _spawn_microdrops(self):
        global v44_microdrop_budget
        if v44_microdrop_budget >= V44_BLOOD_MICRODROP_LIMIT:
            self.breakup_done = True
            return
        self.breakup_done = True
        speed = self.v.length()
        if speed <= 1e-5:
            return
        direction = self.v.normalize()
        count = random.randint(1, 3)
        for _ in range(count):
            if len(blood_particles) >= V44_BLOOD_MAX_PARTICLES:
                break
            if v44_microdrop_budget >= V44_BLOOD_MICRODROP_LIMIT:
                break
            d = direction.rotate(random.uniform(-17.0, 17.0))
            child_speed = speed * random.uniform(0.44, 0.72)
            child = V44BloodParticle(
                self.x,
                self.y,
                d * child_speed,
                guc=max(0.45, self.scale * 0.88),
                arterial=self.arterial,
                profile=self.profile,
                shape=self.shape,
                oxygenation=self.oxygenation * random.uniform(0.96, 1.02),
                micro=True,
                parent_speed=speed,
            )
            child.z = self.z + random.uniform(-1.0, 1.8)
            child.vz = self.vz * random.uniform(0.68, 0.94) + random.uniform(
                -16.0, 28.0
            )
            blood_particles.append(child)
            v44_microdrop_budget += 1

    def guncelle(self, dt):
        if not self.active:
            return
        dt = max(0.0, min(0.045, float(dt)))
        self.age += dt
        if self.age > self.max_age:
            self.active = False
            return

        speed = self.v.length()
        drag = V44_BLOOD_AIR_DRAG * self.drag_bias

        drag *= 1.18 if self.micro else 1.0
        drag *= 1.0 + max(0.0, self.viscosity - 1.0) * 0.16
        self.x += self.v.x * dt
        self.y += self.v.y * dt
        self.v *= math.exp(-drag * dt)
        self.z += self.vz * dt
        self.vz -= self.gravity * dt
        self.wetness = max(
            0.0,
            self.wetness - dt * random.uniform(0.010, 0.018),
        )

        if self._breakup_possible() and random.random() < min(0.32, dt * 6.0):
            self._spawn_microdrops()

        if self.z <= 1.35 and self.vz < 0.0:
            self.z = 0.0
            self.active = False
            landing_speed = max(12.0, self.v.length())
            stretch = v44_clamp(landing_speed / 240.0, 0.42, 1.48)
            scale = random.uniform(0.34, 0.92) * self.scale * (0.82 + 0.18 * stretch)
            if self.micro:
                scale *= 0.48
            kan_lekesi_ekle(self.x, self.y, scale)

    def zemin_katmani_mi(self):
        return self.active and self.z <= BLOOD_PARTICLE_GROUND_Z and self.vz <= 0.0

    def ciz(self, silhouette=False):
        if not self.active:
            return
        sx = dunya_ekran_x(self.x)
        sy = dunya_ekran_y(self.y) - self.z * KAMERA_YAKINLASTIRMA
        if sx < -90 or sx > GENISLIK + 90 or sy < -90 or sy > YUKSEKLIK + 90:
            return

        speed = self.v.length()
        zoom = max(0.5, float(KAMERA_YAKINLASTIRMA))
        base_r = max(1.0, 1.65 * self.scale * zoom)
        longness = (
            1.0
            + v44_clamp(speed / V44_BLOOD_STREAK_SPEED, 0.0, 2.7) * self.stretch_bias
        )
        if self.shape == "longitudinal":
            longness *= 1.32
        if self.micro:
            longness = min(longness, 2.2)
        length = max(2, int(round(base_r * (2.0 + 2.1 * longness))))
        width = max(
            1,
            int(round(base_r * (1.45 if not self.micro else 1.05))),
        )
        angle = -math.degrees(math.atan2(self.v.y, self.v.x)) if speed > 0.01 else 0.0

        tone = self.tone
        if silhouette:
            tone = (92, 0, 9)
        pad = max(4, width + 3)
        surf = pygame.Surface(
            (length + pad * 2, width * 2 + pad * 2),
            pygame.SRCALPHA,
        )
        rect = pygame.Rect(pad, pad, length, width * 2)
        pygame.draw.ellipse(surf, (*tone, 244), rect)

        if length >= 8:
            tail_h = max(1, width)
            pygame.draw.polygon(
                surf,
                (*v44_color_mix(tone, (18, 0, 3), 0.24), 220),
                [
                    (pad, pad + width),
                    (
                        pad + max(2, length // 3),
                        pad + width - tail_h,
                    ),
                    (
                        pad + max(2, length // 3),
                        pad + width + tail_h,
                    ),
                ],
            )



        if (
            not silhouette
            and self.wetness > 0.52
            and speed >= V44_BLOOD_WHITE_GLINT_MIN_SPEED
            and width >= 2
        ):
            glint_len = max(2, int(length * random.uniform(0.18, 0.34)))
            gy = pad + max(1, int(width * 0.50))
            gx = pad + max(1, int(length * 0.18))
            alpha = int(V44_BLOOD_WHITE_GLINT_ALPHA * self.wetness)
            pygame.draw.line(
                surf,
                (255, 247, 242, alpha),
                (gx, gy),
                (min(pad + length - 1, gx + glint_len), gy),
                1,
            )

        if abs(angle) > 0.5:
            surf = pygame.transform.rotate(surf, angle)
        ekran.blit(surf, surf.get_rect(center=(int(sx), int(sy))))
# </POTBO_STAGE S1146>

# <POTBO_STAGE S1148>


_v44_decal_parent = PersistentBloodDecal


class PersistentBloodDecal(_v44_decal_parent):
    """Koyu, varyasyonlu ve ıslakken beyaz mikro-specular taşıyan kalıcı leke."""

    def __init__(self, x, y, scale=None, rotation=None, sprite_index=None):
        super().__init__(
            x,
            y,
            scale=scale,
            rotation=rotation,
            sprite_index=sprite_index,
        )
        self.v44_oxygenation = random.uniform(0.22, 0.76)
        self.v44_tone = v44_blood_palette_for(oxygenation=self.v44_oxygenation)
        self.v44_tone_index = random.randrange(8)
        self.v44_gloss = random.uniform(0.34, 0.94)
        self.v44_gloss_angle = random.uniform(-34.0, 34.0)
        self.v44_gloss_offset = random.uniform(-0.24, 0.24)
        self.v44_edge_darkness = random.uniform(0.10, 0.28)
        self.v44_seed = random.randrange(1, 2**30)
        self.v44_stain_mass = max(
            0.16,
            float(scale if scale is not None else self.scale),
        )
        created = int(getattr(self, "created_ms", pygame.time.get_ticks()))
        self.v44_gloss_end_ms = created + int(
            V44_BLOOD_DECAL_GLOSS_LIFE_MS * random.uniform(0.72, 1.28)
        )
        self.v44_sheen_end_ms = created + int(
            V44_BLOOD_WET_SHEEN_LIFE_MS * random.uniform(0.80, 1.22)
        )

    def _v44_age01(self, now):
        created = int(getattr(self, "created_ms", now))
        dry = int(
            getattr(
                self,
                "dry_after_ms",
                created + V43_BLOOD_DRY_MIN_MS,
            )
        )
        fade = int(
            getattr(
                self,
                "fade_after_ms",
                dry + V43_BLOOD_FADE_MIN_MS,
            )
        )
        if now <= dry:
            return 0.0
        return v44_clamp01((now - dry) / max(1.0, fade - dry))

    def _v44_color(self, now):
        age = self._v44_age01(now)
        fresh = self.v44_tone
        old = v44_blood_palette_for(oxygenation=0.25, age01=age, clot=age > 0.72)
        return v44_color_mix(fresh, old, v44_smoothstep(age))

    def ciz(self, silhouette=False):
        sx = dunya_ekran_x(self.x)
        sy = dunya_ekran_y(self.y)
        if sx < -110 or sx > GENISLIK + 110 or sy < -110 or sy > YUKSEKLIK + 110:
            return
        now = pygame.time.get_ticks()
        tone = (84, 0, 9) if silhouette else self._v44_color(now)
        age01 = self._v44_age01(now)

        if BLOOD_DECAL_SPRITELERI:
            src = BLOOD_DECAL_SPRITELERI[
                self.sprite_index % len(BLOOD_DECAL_SPRITELERI)
            ]
            factor = self.scale * KAMERA_YAKINLASTIRMA
            raw_h = max(2, int(src.get_height() * factor))
            qh = max(2, int(round(raw_h / 2.0)) * 2)
            ratio = src.get_width() / max(1.0, float(src.get_height()))
            size = (max(2, int(round(qh * ratio))), qh)
            qrot = int(round(self.rotation / 10.0)) * 10
            tone_bucket = tuple(int(v // 8 * 8) for v in tone)
            key = (
                "v44_blood_decal",
                id(src),
                size,
                qrot,
                tone_bucket,
                bool(silhouette),
                int(age01 * 5),
            )
            img = blood_decal_onbellegi.get(key)
            if img is None:
                img = pygame.transform.scale(src, size).convert_alpha()

                tint = pygame.Surface(img.get_size(), pygame.SRCALPHA)
                tint.fill((*tone_bucket, 255))
                img.blit(
                    tint,
                    (0, 0),
                    special_flags=pygame.BLEND_RGBA_MULT,
                )
                img = pygame.transform.rotate(img, qrot)
                if len(blood_decal_onbellegi) >= BLOOD_DECAL_CACHE_MAX:
                    for _ in range(min(80, len(blood_decal_onbellegi))):
                        blood_decal_onbellegi.pop(
                            next(iter(blood_decal_onbellegi)),
                            None,
                        )
                blood_decal_onbellegi[key] = img
            rect = img.get_rect(center=(int(sx), int(sy)))
            ekran.blit(img, rect)


            if not silhouette and now < self.v44_sheen_end_ms and self.v44_gloss > 0.0:
                life = v44_clamp01(
                    (self.v44_sheen_end_ms - now)
                    / max(
                        1.0,
                        self.v44_sheen_end_ms - self.created_ms,
                    )
                )
                alpha = int(190 * self.v44_gloss * v44_smoothstep(life))
                if alpha > 12 and rect.width >= 7 and rect.height >= 4:
                    glint = pygame.Surface(rect.size, pygame.SRCALPHA)
                    cx = rect.width * (0.48 + self.v44_gloss_offset)
                    cy = rect.height * 0.38
                    gl = max(
                        2,
                        int(rect.width * (0.12 + 0.11 * self.v44_gloss)),
                    )
                    direction = pygame.Vector2(gl, 0).rotate(self.v44_gloss_angle)
                    p0 = (
                        int(cx - direction.x * 0.5),
                        int(cy - direction.y * 0.5),
                    )
                    p1 = (
                        int(cx + direction.x * 0.5),
                        int(cy + direction.y * 0.5),
                    )
                    pygame.draw.line(glint, (255, 248, 246, alpha), p0, p1, 1)
                    ekran.blit(glint, rect)
            return


        radius_x = max(3, int(6 * self.scale * KAMERA_YAKINLASTIRMA))
        radius_y = max(2, int(3 * self.scale * KAMERA_YAKINLASTIRMA))
        pygame.draw.ellipse(
            ekran,
            tone,
            (
                int(sx) - radius_x,
                int(sy) - radius_y,
                radius_x * 2,
                radius_y * 2,
            ),
        )
        if not silhouette and now < self.v44_gloss_end_ms and radius_x >= 4:
            pygame.draw.line(
                ekran,
                (245, 240, 238),
                (
                    int(sx - radius_x * 0.34),
                    int(sy - radius_y * 0.35),
                ),
                (
                    int(sx + radius_x * 0.08),
                    int(sy - radius_y * 0.42),
                ),
                1,
            )






def v44_blood_spawn_context(
    profile="slash",
    lethal=False,
    source="player",
    target="enemy",
    speed=None,
    direction=None,
    damage=0,
    arterial=False,
):
    if speed is None:
        speed = v44_attack_speed_estimate()
    if direction is None:
        direction = v44_player_facing_vector()
    shape = v44_impact_shape_from_speed(speed, lethal=lethal, arterial=arterial)
    return {
        "profile": str(profile),
        "lethal": bool(lethal),
        "source": str(source),
        "target": str(target),
        "speed": float(speed),
        "direction": tuple(v44_safe_vec(direction)),
        "damage": int(max(0, damage)),
        "arterial": bool(arterial),
        "shape": shape,
        "sharpness": v44_profile_sharpness(profile),
        "viscosity": v44_profile_viscosity(profile),
        "created_ms": pygame.time.get_ticks(),
    }



def kan_parcacigi_patlat(x, y, adet, guc=1.0, yon=None, arterial=False):
    global v44_microdrop_budget, v44_last_blood_debug
    ctx = v44_context_current() or {}
    profile = str(ctx.get("profile", "slash"))
    lethal = bool(ctx.get("lethal", False))
    strike_speed = float(ctx.get("speed", 0.0) or 0.0)
    if strike_speed <= 0.0:
        strike_speed = 560.0 if arterial else 430.0
    shape = str(
        ctx.get("shape") or v44_impact_shape_from_speed(strike_speed, lethal, arterial)
    )
    base = v44_safe_vec(
        yon if yon is not None else ctx.get("direction", (1.0, 0.0))
    ).normalize()
    count = v44_particle_count_shape(adet, shape, lethal=lethal)


    room = max(0, V44_BLOOD_MAX_PARTICLES - len(blood_particles))
    count = min(count, room)
    if count <= 0:
        return 0

    power = max(0.42, float(guc))
    if strike_speed > 0.0:
        power *= v44_clamp(0.78 + strike_speed / 1150.0, 0.78, 1.64)
    oxygenation_base = 0.86 if arterial else random.uniform(0.32, 0.70)
    spawned = 0
    for i in range(count):
        d = v44_directional_sample(base, shape, arterial=arterial)
        speed = v44_speed_sample(shape, power, arterial=arterial)


        if shape == "longitudinal" and i < max(1, count // 3):
            speed *= random.uniform(1.14, 1.48)
        if shape == "radial_asymmetric" and random.random() < 0.30:
            speed *= random.uniform(0.48, 0.78)
        particle = BloodParticle(
            x,
            y,
            d * speed,
            guc=max(0.50, power),
            arterial=arterial,
            profile=profile,
            shape=shape,
            oxygenation=v44_clamp(
                oxygenation_base + random.uniform(-0.10, 0.08),
                0.16,
                0.98,
            ),
            parent_speed=strike_speed,
        )
        if arterial:
            particle.vz *= random.uniform(0.72, 1.08)
            particle.z += random.uniform(1.0, 5.0)
        blood_particles.append(particle)
        spawned += 1

    v44_microdrop_budget = max(0, v44_microdrop_budget - max(1, count // 12))
    v44_last_blood_debug = {
        "shape": shape,
        "profile": profile,
        "speed": round(strike_speed, 1),
        "count": spawned,
        "power": round(power, 3),
        "arterial": bool(arterial),
        "lethal": lethal,
    }
    return spawned
# </POTBO_STAGE S1148>

# <POTBO_STAGE S1151>


_v44_kan_gore_update_original = kan_gore_guncelle


def kan_gore_guncelle():
    global v44_microdrop_budget
    v44_microdrop_budget = max(0, v44_microdrop_budget - 2)
    result = _v44_kan_gore_update_original()
    v44_arterial_emitters_update(pygame.time.get_ticks())

    if len(blood_particles) > V44_BLOOD_MAX_PARTICLES:
        del blood_particles[:-V44_BLOOD_MAX_PARTICLES]
    return result


_v44_player_blood_damage_original = oyuncu_kanli_hasar_kaydi


def oyuncu_kanli_hasar_kaydi(kaynak_x, kaynak_y, profil, hasar, kaynak_adi=""):
    before_hp = float(oyuncu_hp)
    result = _v44_player_blood_damage_original(
        kaynak_x, kaynak_y, profil, hasar, kaynak_adi
    )
    lethal = bool(oyuncu_hp <= 0 or (before_hp > 0 and float(hasar) >= before_hp))
    if lethal and str(profil) != "burn" and str(oyuncu_olum_turu) != "fire":
        v44_player_death_arterial_start(kaynak_x, kaynak_y, profile=profil)
    return result
# </POTBO_STAGE S1151>

# <POTBO_STAGE S1157>


def _v44_damage_context_for_enemy(enemy, amount, source):
    player_melee = _v44_is_player_melee_source(source)
    profile = darbe_profili_belirle(source, getattr(enemy, "tur", "enemy"))
    src = _v44_source_position(source)
    target = pygame.Vector2(float(enemy.x), float(enemy.y - 9.0))
    direction = target - src
    if direction.length_squared() <= 1e-6:
        direction = (
            v44_player_facing_vector() if player_melee else pygame.Vector2(1.0, 0.0)
        )
    if player_melee:
        speed = v44_attack_speed_estimate()
    else:
        vx = float(getattr(source, "vx", 0.0))
        vy = float(getattr(source, "vy", 0.0))
        speed = max(280.0, math.hypot(vx, vy))
    lethal = int(getattr(enemy, "hp", 0)) - int(amount) <= 0
    return v44_blood_spawn_context(
        profile=profile,
        lethal=lethal,
        source="player"
        if player_melee
        else str(getattr(source, "tur", source or "enemy")),
        target=str(getattr(enemy, "tur", "enemy")),
        speed=speed,
        direction=direction,
        damage=int(amount),
        arterial=False,
    )


def _v44_commonenemy_damage(self, miktar, kaynak=None):
    global v44_last_hit_ms, v44_last_hit_energy, v44_last_hit_shape
    global v44_last_hit_target, v44_last_hit_distance
    context = _v44_damage_context_for_enemy(self, miktar, kaynak)
    v44_context_push(context)
    before_hp = int(getattr(self, "hp", 0))
    try:
        result = _v44_commonenemy_damage_original(self, miktar, kaynak)
    finally:
        v44_context_pop()
    after_hp = int(getattr(self, "hp", 0))

    if _v44_is_player_melee_source(kaynak):
        v44_last_hit_ms = pygame.time.get_ticks()
        v44_last_hit_energy = v44_attack_energy_estimate(
            oyuncu_saldiri_modu, result or miktar
        )
        v44_last_hit_shape = str(context["shape"])
        v44_last_hit_target = str(getattr(self, "tur", "enemy"))
        v44_last_hit_distance = pygame.Vector2(self.x, self.y).distance_to(
            (oyuncu_x, oyuncu_y)
        )



    if before_hp > 0 and after_hp <= 0 and str(context.get("profile")) != "burn":
        speed = float(context.get("speed", 0.0))
        shape = v44_impact_shape_from_speed(speed, lethal=True)
        direction = v44_safe_vec(context.get("direction", (1.0, 0.0))).normalize()
        extra_count = (
            22
            if shape == "longitudinal"
            else 30
            if shape == "radial_asymmetric"
            else 26
        )
        extra_power = 1.24 + v44_clamp01(speed / 900.0) * 0.62
        death_ctx = dict(context)
        death_ctx["lethal"] = True
        death_ctx["shape"] = shape
        v44_context_push(death_ctx)
        try:
            kan_parcacigi_patlat(
                self.x,
                self.y - 11.0,
                extra_count,
                guc=extra_power,
                yon=direction,
                arterial=False,
            )
            if shape == "longitudinal":

                kan_parcacigi_patlat(
                    self.x,
                    self.y - 8.0,
                    10,
                    guc=extra_power * 0.86,
                    yon=direction.rotate(random.uniform(8.0, 18.0)),
                    arterial=False,
                )
            else:

                kan_parcacigi_patlat(
                    self.x,
                    self.y - 7.0,
                    12,
                    guc=extra_power * 0.66,
                    yon=direction.rotate(random.choice((-74.0, 66.0))),
                    arterial=False,
                )
        finally:
            v44_context_pop()
    return result
# </POTBO_STAGE S1157>

# <POTBO_STAGE S1159>





V45_VERSION = "45.0"
# </POTBO_STAGE S1159>

# <POTBO_STAGE S1162>
V45_HEMORRHAGE_MAX_STACKS = 6
V45_HEMORRHAGE_DECAY_MS = 6600
V45_HEMORRHAGE_TICK_MS = 1120
V45_HEMORRHAGE_BASE_DAMAGE = 1
V45_HEMORRHAGE_HEAVY_BURST_THRESHOLD = 4
V45_HEMORRHAGE_HEAVY_BURST_DAMAGE = 7
V45_HEMORRHAGE_BLOOD_COUNT = 5
# </POTBO_STAGE S1162>

# <POTBO_STAGE S1168>
v45_bleed_state = {}
# </POTBO_STAGE S1168>

# <POTBO_STAGE S1171>


V45_SKILL_DEFINITIONS = {
    "edge_control": {
        "name_tr": "KESKİN KONTROL",
        "name_en": "EDGE CONTROL",
        "unlock_level": 4,
        "description_tr": "Kılıcın orta/ucu ile hizalı temaslarda küçük hasar ve kan yönü bonusu.",
        "description_en": "Aligned mid/edge contact grants a small damage and blood-direction bonus.",
    },
    "tempo_chain": {
        "name_tr": "TEMPO ZİNCİRİ",
        "name_en": "TEMPO CHAIN",
        "unlock_level": 7,
        "description_tr": "Doğru ritimde ardışık vuruşlar 4 kademeye kadar momentum toplar.",
        "description_en": "Well-timed consecutive strikes build momentum through four stages.",
    },
    "deep_cut": {
        "name_tr": "DERİN KESİK",
        "name_en": "DEEP CUT",
        "unlock_level": 10,
        "description_tr": "Kesici darbeler hemoraji biriktirir; ağır vuruş yüksek stack'i patlatır.",
        "description_en": "Slashing hits build hemorrhage; a heavy strike can rupture high stacks.",
    },
    "execution_read": {
        "name_tr": "İNFAZ OKUMASI",
        "name_en": "EXECUTION READ",
        "unlock_level": 14,
        "description_tr": "Çok düşük canlı hedefte temiz temas hasarı artar; broad hitbox verilmez.",
        "description_en": "Clean contact gains damage against critically wounded targets without broadening hitboxes.",
    },
    "blood_memory": {
        "name_tr": "KAN HAFIZASI",
        "name_en": "BLOOD MEMORY",
        "unlock_level": 18,
        "description_tr": "Aynı hedefe ritmik vuruşta hemoraji süresi daha yavaş düşer.",
        "description_en": "Rhythmic hits on the same target preserve hemorrhage slightly longer.",
    },
    "arterial_precision": {
        "name_tr": "ARTERYEL HASSASİYET",
        "name_en": "ARTERIAL PRECISION",
        "unlock_level": 24,
        "description_tr": "Ağır ve hizalı lethal kesiklerde kan püskürmesi daha dar/uzun okunur.",
        "description_en": "Aligned lethal heavy cuts produce a narrower, longer arterial-looking spray.",
    },
}
# </POTBO_STAGE S1171>

# <POTBO_STAGE S1177>


def v45_bleed_entry(enemy):
    uid = str(getattr(enemy, "uid", id(enemy)))
    entry = v45_bleed_state.get(uid)
    if entry is None:
        entry = {
            "uid": uid,
            "enemy": enemy,
            "stacks": 0,
            "last_apply_ms": -10000,
            "next_tick_ms": 0,
            "expires_ms": 0,
            "last_direction": (1.0, 0.0),
        }
        v45_bleed_state[uid] = entry
    else:
        entry["enemy"] = enemy
    return entry


def v45_bleed_apply(enemy, profile, direction, heavy=False):
    if not v45_skill_unlocked("deep_cut"):
        return 0
    if str(profile) not in (
        "light_slash",
        "slash",
        "medium_slash",
        "heavy_slash",
    ):
        return 0
    now = pygame.time.get_ticks()
    entry = v45_bleed_entry(enemy)
    add = 2 if heavy else 1
    if v45_skill_unlocked("arterial_precision") and heavy and v45_last_alignment > 1.04:
        add += 1
    entry["stacks"] = min(V45_HEMORRHAGE_MAX_STACKS, int(entry["stacks"]) + add)
    entry["last_apply_ms"] = now
    memory = (
        1.22
        if v45_skill_unlocked("blood_memory")
        and str(getattr(enemy, "uid", "")) == str(v45_combo_last_target_uid)
        else 1.0
    )
    entry["expires_ms"] = now + int(V45_HEMORRHAGE_DECAY_MS * memory)
    entry["next_tick_ms"] = max(
        int(entry.get("next_tick_ms", 0)),
        now + V45_HEMORRHAGE_TICK_MS,
    )
    d = v44_safe_vec(direction)
    entry["last_direction"] = tuple(d.normalize())
    v45_skill_flash("deep_cut")
    return int(entry["stacks"])


def v45_bleed_burst_if_ready(enemy, profile):
    if str(profile) != "heavy_slash":
        return 0
    entry = v45_bleed_entry(enemy)
    stacks = int(entry.get("stacks", 0))
    if stacks < V45_HEMORRHAGE_HEAVY_BURST_THRESHOLD:
        return 0
    burst = (
        V45_HEMORRHAGE_HEAVY_BURST_DAMAGE
        + max(0, stacks - V45_HEMORRHAGE_HEAVY_BURST_THRESHOLD) * 2
    )
    entry["stacks"] = max(0, stacks - 3)
    entry["expires_ms"] = pygame.time.get_ticks() + V45_HEMORRHAGE_DECAY_MS
    direction = v44_safe_vec(entry.get("last_direction", (1.0, 0.0))).normalize()
    context = v44_blood_spawn_context(
        profile="heavy_slash",
        lethal=False,
        source="hemorrhage_burst",
        target=str(getattr(enemy, "tur", "enemy")),
        speed=720.0,
        direction=direction,
        damage=burst,
    )
    v44_context_push(context)
    try:
        kan_parcacigi_patlat(
            enemy.x,
            enemy.y - 10.0,
            13 + stacks * 2,
            guc=1.18 + 0.08 * stacks,
            yon=direction,
            arterial=True,
        )
    finally:
        v44_context_pop()
    v45_skill_flash("deep_cut")
    return int(burst)


def v45_bleed_tick():
    now = pygame.time.get_ticks()
    stale = []
    for uid, entry in list(v45_bleed_state.items()):
        enemy = entry.get("enemy")
        if enemy is None or not bool(getattr(enemy, "active", False)):
            stale.append(uid)
            continue
        if now >= int(entry.get("expires_ms", 0)):
            entry["stacks"] = max(0, int(entry.get("stacks", 0)) - 1)
            if entry["stacks"] <= 0:
                stale.append(uid)
                continue
            entry["expires_ms"] = now + int(V45_HEMORRHAGE_DECAY_MS * 0.72)
        if entry["stacks"] > 0 and now >= int(entry.get("next_tick_ms", 0)):
            entry["next_tick_ms"] = now + V45_HEMORRHAGE_TICK_MS


            damage = V45_HEMORRHAGE_BASE_DAMAGE + int(entry["stacks"] >= 5)
            if int(getattr(enemy, "hp", 0)) > 1:
                enemy.hp = max(1, int(enemy.hp) - damage)
                direction = v44_safe_vec(entry.get("last_direction", (1.0, 0.0)))
                context = v44_blood_spawn_context(
                    profile="light_slash",
                    lethal=False,
                    source="hemorrhage_tick",
                    target=str(getattr(enemy, "tur", "enemy")),
                    speed=210.0,
                    direction=direction,
                    damage=damage,
                )
                context["shape"] = "radial_asymmetric"
                v44_context_push(context)
                try:
                    kan_parcacigi_patlat(
                        enemy.x + random.uniform(-2.0, 2.0),
                        enemy.y - random.uniform(6.0, 14.0),
                        V45_HEMORRHAGE_BLOOD_COUNT,
                        guc=0.62,
                        yon=direction,
                        arterial=False,
                    )
                finally:
                    v44_context_pop()
    for uid in stale:
        v45_bleed_state.pop(uid, None)
# </POTBO_STAGE S1177>

# <POTBO_STAGE S1179>


def _v45_commonenemy_damage(self, miktar, kaynak=None):
    player_melee = _v44_is_player_melee_source(kaynak)
    if not player_melee:
        return _v45_commonenemy_damage_original(self, miktar, kaynak)

    now = pygame.time.get_ticks()
    uid = str(getattr(self, "uid", id(self)))
    stage = v45_combo_stage(now, uid)
    profile = darbe_profili_belirle(kaynak, getattr(self, "tur", "enemy"))
    multiplier = v45_melee_multiplier(self, stage)
    adjusted = max(1, int(round(float(miktar) * multiplier)))
    direction = pygame.Vector2(float(self.x) - oyuncu_x, float(self.y) - oyuncu_y)
    heavy = str(oyuncu_saldiri_modu) == "hold_release"


    burst = v45_bleed_burst_if_ready(self, profile) if heavy else 0
    if burst > 0:
        adjusted += burst

    before_hp = int(getattr(self, "hp", 0))
    result = _v45_commonenemy_damage_original(self, adjusted, kaynak)
    if before_hp > 0:
        v45_bleed_apply(self, profile, direction, heavy=heavy)


    if v45_skill_unlocked("tempo_chain") and v45_last_sweetspot > 1.045:
        idx = max(0, min(len(V45_COMBO_STAMINA_REFUND) - 1, stage - 1))
        refund = float(V45_COMBO_STAMINA_REFUND[idx])
        if refund > 0.0:
            globals()["oyuncu_stamina"] = min(
                float(oyuncu_max_stamina),
                float(oyuncu_stamina) + refund,
            )
    return result
# </POTBO_STAGE S1179>

# <POTBO_STAGE S1181>


def common_enemy_guncelle():
    result = _v45_common_enemy_update_original()
    v45_bleed_tick()
    if pygame.time.get_ticks() - int(v45_combo_last_hit_ms) > V45_COMBO_RESET_MS:
        v45_combo_reset()
    return result
# </POTBO_STAGE S1181>

# <POTBO_STAGE S1192>



def v46_blood_calibration_burst():
    origin = pygame.Vector2(oyuncu_x, oyuncu_y - 10.0)
    facing = v44_player_facing_vector()
    tests = (
        ("longitudinal", 780.0, -18.0, 22, 1.42),
        ("fan_asymmetric", 520.0, 8.0, 24, 1.18),
        ("radial_asymmetric", 260.0, 34.0, 28, 0.96),
        ("arterial_jet", 820.0, -38.0, 18, 1.36),
    )
    for shape, speed, angle, count, power in tests:
        direction = facing.rotate(angle)
        context = v44_blood_spawn_context(
            profile="heavy_slash" if speed > 600 else "slash",
            lethal=shape in ("longitudinal", "arterial_jet"),
            source="developer_calibration",
            target="none",
            speed=speed,
            direction=direction,
            damage=0,
            arterial=shape == "arterial_jet",
        )
        context["shape"] = shape
        v44_context_push(context)
        try:
            kan_parcacigi_patlat(
                origin.x,
                origin.y,
                count,
                power,
                yon=direction,
                arterial=shape == "arterial_jet",
            )
        finally:
            v44_context_pop()
    bildirim_goster(
        bt(
            "Kan fizik kalibrasyonu üretildi.",
            "Blood physics calibration emitted.",
        ),
        PARLAK_KIRMIZI,
    )
# </POTBO_STAGE S1192>

# <POTBO_STAGE S1194>


def gelistirici_test_girdisi_uygula(olay):
    global v45_combat_telemetry_enabled
    if (
        GELISTIRICI_MODU
        and olay.type == pygame.KEYDOWN
        and (olay.mod & pygame.KMOD_CTRL)
    ):
        if olay.key == pygame.K_b:
            v46_blood_calibration_burst()
            return True
        if olay.key == pygame.K_h:
            v45_combat_telemetry_enabled = not v45_combat_telemetry_enabled
            bildirim_goster(
                bt(
                    "Combat telemetri AÇIK."
                    if v45_combat_telemetry_enabled
                    else "Combat telemetri KAPALI.",
                    "Combat telemetry ON."
                    if v45_combat_telemetry_enabled
                    else "Combat telemetry OFF.",
                ),
                SARI if v45_combat_telemetry_enabled else GRI,
            )
            return True
    return _v46_dev_input_original(olay)
# </POTBO_STAGE S1194>

# <POTBO_STAGE S1200>


def v47_record_hit(enemy, damage, before_hp, after_hp):
    global \
        v47_last_confirm_ms, \
        v47_last_confirm_pos, \
        v47_last_confirm_heavy, \
        v47_last_confirm_quality
    now = pygame.time.get_ticks()
    event = {
        "ms": now,
        "target": str(getattr(enemy, "tur", "enemy")),
        "uid": str(getattr(enemy, "uid", "")),
        "damage": int(damage),
        "lethal": before_hp > 0 and after_hp <= 0,
        "mode": str(oyuncu_saldiri_modu),
        "combo": int(v45_combo_count),
        "sweetspot": round(float(v45_last_sweetspot), 4),
        "alignment": round(float(v45_last_alignment), 4),
        "multiplier": round(float(v45_last_damage_multiplier), 4),
        "blood_shape": str(v44_last_hit_shape),
        "swing_speed": round(v44_attack_speed_estimate(), 2),
        "distance": round(v45_contact_distance(enemy), 2),
    }
    v47_hit_events.append(event)
    v47_last_confirm_ms = now
    v47_last_confirm_pos = pygame.Vector2(float(enemy.x), float(enemy.y - 12.0))
    v47_last_confirm_heavy = str(oyuncu_saldiri_modu) == "hold_release"
    v47_last_confirm_quality = float(v45_last_damage_multiplier)
    return event
# </POTBO_STAGE S1200>

# <POTBO_STAGE S1203>


def v47_combat_telemetry_ciz():
    if not GELISTIRICI_MODU or not v45_combat_telemetry_enabled:
        return
    w = 350
    h = 152
    rect = pygame.Rect(GENISLIK - w - 14, 14, w, h)
    v46_heavy_plate(rect, active=False, alpha=196)
    last = v47_hit_events[-1] if v47_hit_events else None
    yazi_yaz(
        "COMBAT TELEMETRY",
        rect.x + 12,
        rect.y + 12,
        SARI,
        mini_font,
    )
    if last is None:
        yazi_yaz(
            bt(
                "Henüz melee teması yok.",
                "No melee contact yet.",
            ),
            rect.x + 12,
            rect.y + 38,
            GRI,
            mini_font,
        )
        return
    rows = [
        f"target {last['target']}   dmg {last['damage']}   lethal {int(last['lethal'])}",
        f"combo {last['combo']}   mode {last['mode']}   speed {last['swing_speed']:.0f}px/s",
        f"sweet {last['sweetspot']:.3f}   align {last['alignment']:.3f}   x{last['multiplier']:.3f}",
        f"distance {last['distance']:.1f}   blood {last['blood_shape']}",
        f"particles {len(blood_particles)}   decals {len(blood_decals)}   gore {len(gore_chunks)}",
    ]
    yy = rect.y + 37
    for line in rows:
        yazi_yaz(line, rect.x + 12, yy, ACIK_GRI, mini_font)
        yy += 21
# </POTBO_STAGE S1203>

# <POTBO_STAGE S1211>
V49_BLOOD_HARD_LIMIT = 520
V49_DECAL_HARD_LIMIT = 980
V49_GORE_HARD_LIMIT = 220
# </POTBO_STAGE S1211>

# <POTBO_STAGE S1215>


def v49_budget_trim():
    global v49_runtime_repairs
    repaired = []
    if len(blood_particles) > V49_BLOOD_HARD_LIMIT:
        drop = len(blood_particles) - V49_BLOOD_HARD_LIMIT
        del blood_particles[:drop]
        repaired.append(f"blood_particles -{drop}")
    if len(blood_decals) > V49_DECAL_HARD_LIMIT:
        drop = len(blood_decals) - V49_DECAL_HARD_LIMIT
        del blood_decals[:drop]
        _v40_blood_grid_rebuild()
        repaired.append(f"blood_decals -{drop}")
    if len(gore_chunks) > V49_GORE_HARD_LIMIT:
        settled = [g for g in gore_chunks if getattr(g, "settled", False)]
        remove_count = len(gore_chunks) - V49_GORE_HARD_LIMIT
        for g in settled[:remove_count]:
            try:
                gore_chunks.remove(g)
            except ValueError:
                pass
        if len(gore_chunks) > V49_GORE_HARD_LIMIT:
            del gore_chunks[: len(gore_chunks) - V49_GORE_HARD_LIMIT]
        repaired.append("gore budget")
    try:
        if len(ambient_rats) > V49_RAT_HARD_LIMIT:
            del ambient_rats[:-V49_RAT_HARD_LIMIT]
            repaired.append("rat budget")
    except Exception:
        pass
    if repaired:
        v49_runtime_repairs += len(repaired)
    return repaired


def v49_runtime_audit(force=False):
    global v49_audit_next_ms, v49_last_warnings
    now = pygame.time.get_ticks()
    if not force and now < v49_audit_next_ms:
        return v49_audit_history[-1] if v49_audit_history else {}
    v49_audit_next_ms = now + V49_AUDIT_INTERVAL_MS
    warnings = []

    if not v49_numeric_finite(oyuncu_x) or not v49_numeric_finite(oyuncu_y):
        warnings.append("player_nonfinite")
    if not v49_numeric_finite(oyuncu_hp) or not v49_numeric_finite(oyuncu_stamina):
        warnings.append("resource_nonfinite")
    for actor in v49_world_actor_list():
        if not v49_actor_finite(actor):
            warnings.append(
                f"actor_nonfinite:{getattr(actor, 'tur', type(actor).__name__)}"
            )
            v49_repair_nonfinite_actor(actor)

    repaired = v49_budget_trim()
    if repaired:
        warnings.extend("trim:" + item for item in repaired)


    grid_count = sum(len(items) for items in v40_blood_grid.values())
    if blood_decals and abs(grid_count - len(blood_decals)) > max(
        8, len(blood_decals) // 8
    ):
        _v40_blood_grid_rebuild()
        warnings.append("blood_grid_rebuilt")


    stale_bleed = [
        uid
        for uid, entry in v45_bleed_state.items()
        if not bool(getattr(entry.get("enemy"), "active", False))
    ]
    for uid in stale_bleed:
        v45_bleed_state.pop(uid, None)

    snapshot = {
        "ms": now,
        "warnings": tuple(warnings),
        "blood_particles": len(blood_particles),
        "blood_decals": len(blood_decals),
        "gore": len(gore_chunks),
        "bleed_targets": len(v45_bleed_state),
        "combo": int(v45_combo_count),
        "zoom": float(KAMERA_YAKINLASTIRMA),
        "repairs": int(v49_runtime_repairs),
    }
    v49_last_warnings = list(warnings)
    v49_audit_history.append(snapshot)
    return snapshot
# </POTBO_STAGE S1215>

# <POTBO_STAGE S1217>
V50_SYSTEM_CONTRACT = {
    "blood": {
        "dark_palette": True,
        "per_particle_variation": True,
        "white_specular": True,
        "velocity_morphology": True,
        "arterial_player_death": True,
        "fast_kill_longitudinal": True,
        "slow_kill_radial_asymmetric": True,
        "survival_arts_removed": True,
    },
    "combat": {
        "player_sword_bonus_px": V44_SWORD_REACH_BONUS_PX,
        "directional_hitbox_preserved": True,
        "sweetspot": True,
        "edge_alignment": True,
        "combo": True,
        "hemorrhage": True,
        "execution_skill": True,
    },
    "ui": {
        "heavy_plate": True,
        "fluid_interpolation": True,
        "character_audio_envelope_ms": V46_CHARACTER_SAMPLE_MS,
        "all_test_keys_bottom_right": True,
    },
    "runtime": {
        "finite_actor_guard": True,
        "fx_hard_budgets": True,
        "spatial_grid_repair": True,
    },
}


def v50_blood_contract_check():
    dark_enough = all(max(color) <= 145 for color in V44_BLOOD_PALETTE)
    palette_unique = len(set(V44_BLOOD_PALETTE)) == len(V44_BLOOD_PALETTE)
    shape_fast = v44_impact_shape_from_speed(V44_BLOOD_FAST_KILL_SPEED + 1, lethal=True)
    shape_slow = v44_impact_shape_from_speed(V44_BLOOD_SLOW_KILL_SPEED - 1, lethal=True)
    return {
        "palette_dark": dark_enough,
        "palette_unique": palette_unique,
        "fast_shape": shape_fast,
        "slow_shape": shape_slow,
        "fast_ok": shape_fast == "longitudinal",
        "slow_ok": shape_slow == "radial_asymmetric",
        "arterial_pulses": len(V44_PLAYER_DEATH_ARTERIAL_PULSES),
        "particle_limit": V44_BLOOD_MAX_PARTICLES,
        "decal_limit": V40_BLOOD_GLOBAL_MAX,
    }


def v50_combat_contract_check():
    strict = _v38_player_reach_values()
    return {
        "reach": tuple(strict),
        "bonus_px": V44_SWORD_REACH_BONUS_PX,
        "combo_max": V45_COMBO_MAX,
        "combo_window_ms": V45_COMBO_WINDOW_MS,
        "hemorrhage_max": V45_HEMORRHAGE_MAX_STACKS,
        "skills": {
            key: {
                "unlock_level": int(value["unlock_level"]),
                "unlocked": v45_skill_unlocked(key),
            }
            for key, value in V45_SKILL_DEFINITIONS.items()
        },
    }
# </POTBO_STAGE S1217>

# <POTBO_STAGE S1219>


def v50_full_diagnostics():
    return {
        "version": V50_VERSION,
        "v44": v50_blood_contract_check(),
        "v45": v50_combat_contract_check(),
        "v46": v50_ui_contract_check(),
        "v49": v49_runtime_audit(True),
        "system_contract": V50_SYSTEM_CONTRACT,
        "last_blood": dict(v44_last_blood_debug),
        "last_hit": dict(v47_hit_events[-1]) if v47_hit_events else None,
    }


def v50_startup_sanity():
    blood = v50_blood_contract_check()
    ui = v50_ui_contract_check()
    return (
        bool(blood["palette_dark"])
        and bool(blood["palette_unique"])
        and bool(blood["fast_ok"])
        and bool(blood["slow_ok"])
        and bool(ui["all_required_visible"])
        and V44_SWORD_REACH_BONUS_PX > 0
    )
# </POTBO_STAGE S1219>

# <POTBO_STAGE S1225>
V51_RIPOSTE_BLOOD_SPEED_BONUS = 120.0
# </POTBO_STAGE S1225>

# <POTBO_STAGE S1242>




V52_SKILL_CATALOG = {
    "shared_edge_familiarity": {
        "branch": "shared",
        "level": 3,
        "name_tr": "Kenar Aşinalığı",
        "name_en": "Edge Familiarity",
        "effects": {"alignment": 0.015},
        "tags": ("melee", "precision"),
    },
    "shared_breath_control": {
        "branch": "shared",
        "level": 5,
        "name_tr": "Nefes Kontrolü",
        "name_en": "Breath Control",
        "effects": {"stamina_refund": 0.35},
        "tags": ("stamina", "tempo"),
    },
    "shared_wet_edge": {
        "branch": "shared",
        "level": 8,
        "name_tr": "Islak Kenar",
        "name_en": "Wet Edge",
        "effects": {"blood_speed": 0.035, "blood_count": 0.025},
        "tags": ("blood", "melee"),
    },
    "shared_second_intention": {
        "branch": "shared",
        "level": 12,
        "name_tr": "İkinci Niyet",
        "name_en": "Second Intention",
        "effects": {"combo_window": 28.0},
        "tags": ("combo", "timing"),
    },
    "shared_hemorrhage_read": {
        "branch": "shared",
        "level": 16,
        "name_tr": "Hemoraji Okuması",
        "name_en": "Hemorrhage Read",
        "effects": {"hemorrhage_duration": 0.08},
        "tags": ("blood", "skill"),
    },
    "shared_execution_discipline": {
        "branch": "shared",
        "level": 22,
        "name_tr": "İnfaz Disiplini",
        "name_en": "Execution Discipline",
        "effects": {"execution": 0.025},
        "tags": ("execution", "precision"),
    },
    "shared_surface_memory": {
        "branch": "shared",
        "level": 28,
        "name_tr": "Yüzey Hafızası",
        "name_en": "Surface Memory",
        "effects": {"decal_life": 0.08},
        "tags": ("blood", "world"),
    },
    "shared_contact_economy": {
        "branch": "shared",
        "level": 34,
        "name_tr": "Temas Ekonomisi",
        "name_en": "Contact Economy",
        "effects": {
            "stamina_refund": 0.55,
            "combo_damage": 0.012,
        },
        "tags": ("stamina", "combo"),
    },
    "shared_final_measure": {
        "branch": "shared",
        "level": 42,
        "name_tr": "Son Ölçü",
        "name_en": "Final Measure",
        "effects": {"sweetspot": 0.018, "execution": 0.018},
        "tags": ("precision", "execution"),
    },
    "male_weight_transfer": {
        "branch": "male",
        "level": 4,
        "name_tr": "Ağırlık Transferi",
        "name_en": "Weight Transfer",
        "effects": {"heavy_energy": 0.045},
        "tags": ("heavy", "melee"),
    },
    "male_guarded_shoulders": {
        "branch": "male",
        "level": 6,
        "name_tr": "Kilitlemiş Omuz",
        "name_en": "Guarded Shoulders",
        "effects": {"parry_window": 8.0},
        "tags": ("guard", "parry"),
    },
    "male_half_sword": {
        "branch": "male",
        "level": 9,
        "name_tr": "Yarım Kılıç",
        "name_en": "Half Sword",
        "effects": {"hilt_penalty_reduction": 0.025},
        "tags": ("precision", "heavy"),
    },
    "male_committed_arc": {
        "branch": "male",
        "level": 13,
        "name_tr": "Taahhütlü Yay",
        "name_en": "Committed Arc",
        "effects": {"heavy_damage": 0.025, "blood_speed": 0.04},
        "tags": ("heavy", "blood"),
    },
    "male_shoulder_drive": {
        "branch": "male",
        "level": 17,
        "name_tr": "Omuz Sürüşü",
        "name_en": "Shoulder Drive",
        "effects": {"heavy_energy": 0.055, "poise": 0.05},
        "tags": ("heavy", "poise"),
    },
    "male_deep_channel": {
        "branch": "male",
        "level": 21,
        "name_tr": "Derin Kanal",
        "name_en": "Deep Channel",
        "effects": {"hemorrhage_add": 0.22},
        "tags": ("hemorrhage", "heavy"),
    },
    "male_red_line": {
        "branch": "male",
        "level": 26,
        "name_tr": "Kırmızı Hat",
        "name_en": "Red Line",
        "effects": {"longitudinal_bias": 0.08},
        "tags": ("blood", "heavy"),
    },
    "male_counterweight": {
        "branch": "male",
        "level": 31,
        "name_tr": "Karşı Ağırlık",
        "name_en": "Counterweight",
        "effects": {"riposte": 0.035, "parry_refund": 0.70},
        "tags": ("parry", "riposte"),
    },
    "male_execution_step": {
        "branch": "male",
        "level": 37,
        "name_tr": "İnfaz Adımı",
        "name_en": "Execution Step",
        "effects": {"execution": 0.035, "heavy_damage": 0.02},
        "tags": ("execution", "heavy"),
    },
    "male_final_commitment": {
        "branch": "male",
        "level": 46,
        "name_tr": "Son Taahhüt",
        "name_en": "Final Commitment",
        "effects": {
            "heavy_damage": 0.04,
            "heavy_energy": 0.06,
            "poise": 0.06,
        },
        "tags": ("heavy", "mastery"),
    },
    "female_angle_entry": {
        "branch": "female",
        "level": 4,
        "name_tr": "Açılı Giriş",
        "name_en": "Angle Entry",
        "effects": {"cross_angle": 0.018},
        "tags": ("precision", "mobility"),
    },
    "female_short_recovery": {
        "branch": "female",
        "level": 6,
        "name_tr": "Kısa Toparlanma",
        "name_en": "Short Recovery",
        "effects": {"combo_window": 22.0},
        "tags": ("tempo", "combo"),
    },
    "female_tip_language": {
        "branch": "female",
        "level": 9,
        "name_tr": "Uç Dili",
        "name_en": "Tip Language",
        "effects": {"tip_penalty_reduction": 0.022},
        "tags": ("precision", "reach"),
    },
    "female_second_cut": {
        "branch": "female",
        "level": 13,
        "name_tr": "İkinci Kesik",
        "name_en": "Second Cut",
        "effects": {"combo_damage": 0.018},
        "tags": ("combo", "melee"),
    },
    "female_flow_state": {
        "branch": "female",
        "level": 17,
        "name_tr": "Akış Durumu",
        "name_en": "Flow State",
        "effects": {
            "stamina_refund": 0.55,
            "blood_speed": 0.025,
        },
        "tags": ("tempo", "stamina"),
    },
    "female_capillary_read": {
        "branch": "female",
        "level": 21,
        "name_tr": "Kılcal Okuma",
        "name_en": "Capillary Read",
        "effects": {"hemorrhage_duration": 0.10},
        "tags": ("hemorrhage", "precision"),
    },
    "female_narrow_fan": {
        "branch": "female",
        "level": 26,
        "name_tr": "Dar Yelpaze",
        "name_en": "Narrow Fan",
        "effects": {"fan_bias": 0.08},
        "tags": ("blood", "precision"),
    },
    "female_countertempo": {
        "branch": "female",
        "level": 31,
        "name_tr": "Karşı Tempo",
        "name_en": "Countertempo",
        "effects": {"riposte": 0.025, "combo_window": 26.0},
        "tags": ("riposte", "tempo"),
    },
    "female_last_opening": {
        "branch": "female",
        "level": 37,
        "name_tr": "Son Açıklık",
        "name_en": "Last Opening",
        "effects": {"execution": 0.03, "sweetspot": 0.018},
        "tags": ("execution", "precision"),
    },
    "female_final_measure": {
        "branch": "female",
        "level": 46,
        "name_tr": "Son Ölçüm",
        "name_en": "Final Measure",
        "effects": {
            "combo_damage": 0.028,
            "cross_angle": 0.022,
            "stamina_refund": 0.55,
        },
        "tags": ("tempo", "mastery"),
    },
}

V52_EFFECT_LIMITS = {
    "alignment": (0.0, 0.08),
    "stamina_refund": (0.0, 3.0),
    "blood_speed": (0.0, 0.20),
    "blood_count": (0.0, 0.16),
    "combo_window": (0.0, 130.0),
    "hemorrhage_duration": (0.0, 0.35),
    "execution": (0.0, 0.12),
    "decal_life": (0.0, 0.30),
    "combo_damage": (0.0, 0.08),
    "sweetspot": (0.0, 0.08),
    "heavy_energy": (0.0, 0.20),
    "parry_window": (0.0, 40.0),
    "hilt_penalty_reduction": (0.0, 0.10),
    "heavy_damage": (0.0, 0.12),
    "poise": (0.0, 0.20),
    "hemorrhage_add": (0.0, 0.65),
    "longitudinal_bias": (0.0, 0.22),
    "riposte": (0.0, 0.12),
    "parry_refund": (0.0, 2.0),
    "cross_angle": (0.0, 0.08),
    "tip_penalty_reduction": (0.0, 0.10),
    "fan_bias": (0.0, 0.22),
}
# </POTBO_STAGE S1242>

# <POTBO_STAGE S1248>


def v52_blood_speed_multiplier():
    return 1.0 + v52_effect("blood_speed")


def v52_blood_count_multiplier():
    return 1.0 + v52_effect("blood_count")
# </POTBO_STAGE S1248>

# <POTBO_STAGE S1251>


def v52_hemorrhage_duration_multiplier():
    return 1.0 + v52_effect("hemorrhage_duration")
# </POTBO_STAGE S1251>

# <POTBO_STAGE S1254>



_v52_blood_emit_original = kan_parcacigi_patlat


def kan_parcacigi_patlat(x, y, adet, guc=1.0, yon=None, arterial=False):
    count = int(round(max(0, int(adet)) * v52_blood_count_multiplier()))
    power = float(guc) * v52_blood_speed_multiplier()
    return _v52_blood_emit_original(x, y, count, power, yon=yon, arterial=arterial)
# </POTBO_STAGE S1254>

# <POTBO_STAGE S1261>

V53_TISSUE_PROFILES = {
    "crawler": {
        "blood_volume": 0.76,
        "arterial_pressure": 0.74,
        "vessel_density": 0.84,
        "clotting": 0.48,
        "viscosity": 0.92,
        "oxygenation": 0.58,
        "body_height": 30.0,
        "body_mass": 0.54,
        "skin_resistance": 0.62,
        "fat_fraction": 0.10,
    },
    "berserker": {
        "blood_volume": 1.14,
        "arterial_pressure": 0.92,
        "vessel_density": 0.86,
        "clotting": 0.56,
        "viscosity": 1.04,
        "oxygenation": 0.64,
        "body_height": 58.0,
        "body_mass": 1.28,
        "skin_resistance": 0.86,
        "fat_fraction": 0.15,
    },
    "headsthrower": {
        "blood_volume": 0.88,
        "arterial_pressure": 0.78,
        "vessel_density": 0.82,
        "clotting": 0.50,
        "viscosity": 0.96,
        "oxygenation": 0.60,
        "body_height": 48.0,
        "body_mass": 0.78,
        "skin_resistance": 0.70,
        "fat_fraction": 0.12,
    },
    "tarkard": {
        "blood_volume": 1.36,
        "arterial_pressure": 0.86,
        "vessel_density": 0.70,
        "clotting": 0.72,
        "viscosity": 1.14,
        "oxygenation": 0.55,
        "body_height": 78.0,
        "body_mass": 1.74,
        "skin_resistance": 1.26,
        "fat_fraction": 0.22,
    },
    "torrmund": {
        "blood_volume": 1.05,
        "arterial_pressure": 0.94,
        "vessel_density": 0.74,
        "clotting": 0.62,
        "viscosity": 1.02,
        "oxygenation": 0.69,
        "body_height": 74.0,
        "body_mass": 1.22,
        "skin_resistance": 1.18,
        "fat_fraction": 0.18,
    },
    "player_male": {
        "blood_volume": 1.08,
        "arterial_pressure": 0.98,
        "vessel_density": 0.80,
        "clotting": 0.60,
        "viscosity": 1.02,
        "oxygenation": 0.72,
        "body_height": 68.0,
        "body_mass": 1.15,
        "skin_resistance": 0.82,
        "fat_fraction": 0.16,
    },
    "player_female": {
        "blood_volume": 0.94,
        "arterial_pressure": 0.92,
        "vessel_density": 0.82,
        "clotting": 0.58,
        "viscosity": 0.98,
        "oxygenation": 0.74,
        "body_height": 64.0,
        "body_mass": 0.92,
        "skin_resistance": 0.76,
        "fat_fraction": 0.18,
    },
    "default": {
        "blood_volume": 1.0,
        "arterial_pressure": 0.86,
        "vessel_density": 0.76,
        "clotting": 0.58,
        "viscosity": 1.0,
        "oxygenation": 0.62,
        "body_height": 60.0,
        "body_mass": 1.0,
        "skin_resistance": 0.80,
        "fat_fraction": 0.16,
    },
}

V53_BODY_ZONES = {
    "head": {
        "height_range": (0.00, 0.16),
        "blood": 0.72,
        "arterial": 0.58,
        "gore": 1.12,
        "streak": 0.92,
        "pain": 1.16,
    },
    "neck": {
        "height_range": (0.16, 0.28),
        "blood": 1.28,
        "arterial": 1.72,
        "gore": 0.84,
        "streak": 1.18,
        "pain": 1.24,
    },
    "chest": {
        "height_range": (0.28, 0.51),
        "blood": 1.04,
        "arterial": 1.04,
        "gore": 1.00,
        "streak": 1.00,
        "pain": 1.00,
    },
    "abdomen": {
        "height_range": (0.51, 0.70),
        "blood": 1.12,
        "arterial": 0.82,
        "gore": 1.24,
        "streak": 0.88,
        "pain": 1.08,
    },
    "arm": {
        "height_range": (0.30, 0.64),
        "blood": 0.86,
        "arterial": 0.94,
        "gore": 0.68,
        "streak": 1.06,
        "pain": 0.92,
    },
    "leg": {
        "height_range": (0.70, 1.00),
        "blood": 0.92,
        "arterial": 1.08,
        "gore": 0.78,
        "streak": 1.02,
        "pain": 0.96,
    },
}
# </POTBO_STAGE S1261>

# <POTBO_STAGE S1267>


def v53_context_enrich(context, entity_type="default"):
    global v53_last_zone, v53_last_tissue
    ctx = dict(context or {})
    tissue = v53_tissue_profile(entity_type)
    direction = ctx.get("direction", (1.0, 0.0))
    profile = str(ctx.get("profile", "slash"))
    speed = float(ctx.get("speed", 0.0))
    lethal = bool(ctx.get("lethal", False))
    zone = v53_zone_for_profile(profile, direction, lethal, speed)
    zone_values = v53_zone_values(zone)
    arterial_chance = v53_arterial_probability(tissue, zone, profile, speed, lethal)
    ctx["entity_type"] = str(entity_type)
    ctx["tissue"] = tissue
    ctx["zone"] = zone
    ctx["zone_values"] = zone_values
    ctx["arterial_chance"] = arterial_chance
    ctx["oxygenation"] = float(tissue.get("oxygenation", 0.62))
    ctx["blood_volume"] = float(tissue.get("blood_volume", 1.0))
    ctx["arterial_pressure"] = float(tissue.get("arterial_pressure", 0.86))
    ctx["clotting"] = float(tissue.get("clotting", 0.58))
    ctx["tissue_viscosity"] = float(tissue.get("viscosity", 1.0))
    v53_last_zone = zone
    v53_last_tissue = str(entity_type)
    return ctx
# </POTBO_STAGE S1267>

# <POTBO_STAGE S1271>


_v53_decal_parent = PersistentBloodDecal
# </POTBO_STAGE S1271>

# <POTBO_STAGE S1273>





_v53_blood_emit_original = kan_parcacigi_patlat


def kan_parcacigi_patlat(x, y, adet, guc=1.0, yon=None, arterial=False):
    ctx = v44_context_current() or {}
    tissue = ctx.get("tissue") if isinstance(ctx.get("tissue"), dict) else None
    zone_values = (
        ctx.get("zone_values") if isinstance(ctx.get("zone_values"), dict) else None
    )
    count = max(0, int(adet))
    power = float(guc)
    local_arterial = bool(arterial)
    if tissue is not None:
        volume = float(ctx.get("blood_volume", tissue.get("blood_volume", 1.0)))
        pressure = float(
            ctx.get(
                "arterial_pressure",
                tissue.get("arterial_pressure", 0.86),
            )
        )
        viscosity = float(ctx.get("tissue_viscosity", tissue.get("viscosity", 1.0)))
        count = int(round(count * v44_clamp(volume, 0.58, 1.42)))
        power *= v44_clamp(0.88 + pressure * 0.22, 0.86, 1.16)
        power *= v44_clamp(1.04 - (viscosity - 1.0) * 0.12, 0.90, 1.10)
        if zone_values is not None:
            count = int(
                round(
                    count
                    * v44_clamp(
                        zone_values.get("blood", 1.0),
                        0.68,
                        1.34,
                    )
                )
            )
            power *= v44_clamp(zone_values.get("streak", 1.0), 0.82, 1.22)
        if (
            not local_arterial
            and random.random() < float(ctx.get("arterial_chance", 0.0)) * 0.28
        ):
            local_arterial = True
    return _v53_blood_emit_original(
        x, y, count, power, yon=yon, arterial=local_arterial
    )
# </POTBO_STAGE S1273>

# <POTBO_STAGE S1275>

V54_BLADE_PROFILES = {
    "male_normal": {
        "blade_length_px": 49.0 + V44_SWORD_REACH_BONUS_PX,
        "effective_mass": 1.28,
        "arc_deg": 102.0,
        "active_start": 0.26,
        "active_peak": 0.54,
        "active_end": 0.82,
        "edge_retention": 0.88,
        "hand_speed": 0.82,
        "tip_bias": 1.06,
        "recovery_weight": 1.08,
        "blood_transfer": 1.00,
    },
    "male_heavy": {
        "blade_length_px": 64.0 + V44_SWORD_REACH_BONUS_PX,
        "effective_mass": 1.62,
        "arc_deg": 128.0,
        "active_start": 0.18,
        "active_peak": 0.47,
        "active_end": 0.78,
        "edge_retention": 0.92,
        "hand_speed": 0.76,
        "tip_bias": 1.12,
        "recovery_weight": 1.34,
        "blood_transfer": 1.18,
    },
    "female_normal": {
        "blade_length_px": 48.0 + V44_SWORD_REACH_BONUS_PX,
        "effective_mass": 0.94,
        "arc_deg": 116.0,
        "active_start": 0.22,
        "active_peak": 0.49,
        "active_end": 0.76,
        "edge_retention": 0.91,
        "hand_speed": 1.08,
        "tip_bias": 1.10,
        "recovery_weight": 0.88,
        "blood_transfer": 0.96,
    },
    "female_heavy": {
        "blade_length_px": 56.0 + V44_SWORD_REACH_BONUS_PX,
        "effective_mass": 1.12,
        "arc_deg": 124.0,
        "active_start": 0.20,
        "active_peak": 0.48,
        "active_end": 0.78,
        "edge_retention": 0.93,
        "hand_speed": 0.98,
        "tip_bias": 1.12,
        "recovery_weight": 1.02,
        "blood_transfer": 1.05,
    },
    "special_entry": {
        "blade_length_px": 60.0 + V44_SWORD_REACH_BONUS_PX,
        "effective_mass": 1.22,
        "arc_deg": 132.0,
        "active_start": 0.08,
        "active_peak": 0.23,
        "active_end": 0.36,
        "edge_retention": 0.96,
        "hand_speed": 1.34,
        "tip_bias": 1.16,
        "recovery_weight": 0.92,
        "blood_transfer": 1.12,
    },
    "special_mid": {
        "blade_length_px": 62.0 + V44_SWORD_REACH_BONUS_PX,
        "effective_mass": 1.30,
        "arc_deg": 146.0,
        "active_start": 0.30,
        "active_peak": 0.42,
        "active_end": 0.56,
        "edge_retention": 0.96,
        "hand_speed": 1.42,
        "tip_bias": 1.18,
        "recovery_weight": 0.98,
        "blood_transfer": 1.16,
    },
    "special_finish": {
        "blade_length_px": 65.0 + V44_SWORD_REACH_BONUS_PX,
        "effective_mass": 1.46,
        "arc_deg": 158.0,
        "active_start": 0.49,
        "active_peak": 0.62,
        "active_end": 0.76,
        "edge_retention": 0.98,
        "hand_speed": 1.48,
        "tip_bias": 1.20,
        "recovery_weight": 1.18,
        "blood_transfer": 1.24,
    },
}
# </POTBO_STAGE S1275>

# <POTBO_STAGE S1283>


def v54_blood_transfer(enemy=None):
    profile = v54_profile()
    edge = v54_edge_efficiency(enemy)
    speed = v44_attack_speed_estimate()
    speed_factor = v44_clamp(0.78 + speed / 1500.0, 0.82, 1.42)
    return float(profile["blood_transfer"]) * edge * speed_factor
# </POTBO_STAGE S1283>

# <POTBO_STAGE S1286>


def _v44_damage_context_for_enemy(enemy, amount, source):
    context = _v54_damage_context_original(enemy, amount, source)
    if _v44_is_player_melee_source(source):
        context["speed"] = float(v44_attack_speed_estimate())
        context["contact_quality"] = float(v54_contact_quality(enemy))
        context["edge_efficiency"] = float(v54_edge_efficiency(enemy))
        context["blood_transfer"] = float(v54_blood_transfer(enemy))
        context["shape"] = v44_impact_shape_from_speed(
            context["speed"],
            lethal=bool(context.get("lethal", False)),
            arterial=bool(context.get("arterial", False)),
        )
    return context


_v54_blood_emit_original = kan_parcacigi_patlat


def kan_parcacigi_patlat(x, y, adet, guc=1.0, yon=None, arterial=False):
    ctx = v44_context_current() or {}
    transfer = float(ctx.get("blood_transfer", 1.0))
    quality = float(ctx.get("contact_quality", 0.72))
    count = int(
        round(max(0, int(adet)) * v44_clamp(0.88 + transfer * 0.12, 0.86, 1.16))
    )
    power = float(guc) * v44_clamp(0.90 + quality * 0.16, 0.90, 1.08)
    return _v54_blood_emit_original(x, y, count, power, yon=yon, arterial=arterial)
# </POTBO_STAGE S1286>

# <POTBO_STAGE S1294>


def v55_nearby_wet_blood(pos, radius=V55_SMEAR_SOURCE_RADIUS):
    now = pygame.time.get_ticks()
    candidates = []
    for decal in _v40_blood_nearby(pos, radius):
        created = int(getattr(decal, "created_ms", now))
        dry = int(
            getattr(
                decal,
                "dry_after_ms",
                created + V43_BLOOD_DRY_MIN_MS,
            )
        )
        if now >= dry:
            continue
        distance = pygame.Vector2(float(decal.x), float(decal.y)).distance_to(pos)
        if distance <= radius:
            wet_left = v44_clamp01((dry - now) / max(1.0, dry - created))
            candidates.append((distance - wet_left * 5.0, decal, wet_left))
    if not candidates:
        return None
    candidates.sort(key=lambda item: item[0])
    return candidates[0]
# </POTBO_STAGE S1294>

# <POTBO_STAGE S1296>


def v55_spawn_smear(pos, velocity, transfer=0.5, source=None):
    global v55_smear_count
    if len(blood_decals) >= V40_BLOOD_GLOBAL_MAX:
        return None
    p = pygame.Vector2(pos)
    v = pygame.Vector2(velocity)
    speed = v.length()
    if speed < V55_SMEAR_MIN_SPEED:
        return None
    if v.length_squared() > 1e-6:
        offset = -v.normalize() * random.uniform(3.0, 8.0)
        p += offset
    safe = _v40_blood_safe_floor(p.x, p.y)
    if safe is None:
        return None
    scale = random.uniform(*V55_SMEAR_SCALE) * v44_clamp(
        0.65 + transfer * 0.62, 0.55, 1.20
    )
    rotation = v55_smear_rotation_from_velocity(v)
    decal = PersistentBloodDecal(
        safe.x,
        safe.y,
        scale=scale,
        rotation=rotation,
    )
    decal.v55_smear = True
    decal.v55_transfer = float(transfer)
    decal.v55_source = str(source or "movement")
    decal.v44_gloss *= 0.72
    decal.v53_spread *= 1.12
    blood_decals.append(decal)
    cell = _v40_blood_cell(decal.x, decal.y)
    v40_blood_grid.setdefault(cell, []).append(decal)
    v55_smear_count += 1
    return decal


def v55_player_blood_transfer_tick(dt, now):
    global v55_player_last_pos, v55_player_last_smear_ms, v55_player_transfer
    current = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    delta = current - v55_player_last_pos
    speed = delta.length() / max(1e-5, dt) if dt > 0.0 else 0.0
    wet = v55_nearby_wet_blood(current)
    if wet is not None:
        _distance, source, wetness = wet
        gain = (
            V55_TRANSFER_GAIN * wetness * max(0.2, float(getattr(source, "scale", 1.0)))
        )
        v55_player_transfer = min(
            V55_TRANSFER_MAX,
            v55_player_transfer + gain * max(0.35, dt * 12.0),
        )
    else:
        v55_player_transfer = max(
            0.0,
            v55_player_transfer - V55_TRANSFER_DECAY_PER_SEC * dt,
        )
    if (
        speed >= V55_SMEAR_MIN_SPEED
        and v55_player_transfer > 0.12
        and now >= v55_player_last_smear_ms
    ):
        v55_player_last_smear_ms = now + V55_SMEAR_PLAYER_INTERVAL_MS
        v55_spawn_smear(
            current,
            delta / max(dt, 1e-5),
            v55_player_transfer,
            source="player_boot",
        )
        v55_player_transfer *= 0.88
    v55_player_last_pos = current


def v55_enemy_blood_transfer_tick(enemy, dt, now):
    uid = str(getattr(enemy, "uid", id(enemy)))
    current = pygame.Vector2(float(enemy.x), float(enemy.y))
    state = v55_enemy_motion.get(uid)
    if state is None:
        v55_enemy_motion[uid] = {
            "pos": current,
            "next": now,
            "transfer": 0.0,
        }
        return
    previous = pygame.Vector2(state["pos"])
    delta = current - previous
    speed = delta.length() / max(1e-5, dt) if dt > 0.0 else 0.0
    wet = v55_nearby_wet_blood(current)
    transfer = float(state.get("transfer", 0.0))
    if wet is not None:
        _distance, source, wetness = wet
        transfer = min(
            V55_TRANSFER_MAX,
            transfer + V55_TRANSFER_GAIN * wetness * dt * 4.0,
        )
    else:
        transfer = max(
            0.0,
            transfer - V55_TRANSFER_DECAY_PER_SEC * dt * 0.72,
        )
    if (
        speed >= V55_SMEAR_MIN_SPEED
        and transfer > 0.16
        and now >= int(state.get("next", 0))
        and bool(getattr(enemy, "active", False))
    ):
        state["next"] = now + V55_SMEAR_ENEMY_INTERVAL_MS + random.randint(-25, 55)
        v55_spawn_smear(
            current,
            delta / max(dt, 1e-5),
            transfer,
            source=str(getattr(enemy, "tur", "enemy")),
        )
        transfer *= 0.86
    state["pos"] = current
    state["transfer"] = transfer


def v55_blood_motion_tick():
    now = pygame.time.get_ticks()
    dt = max(
        1.0 / 240.0,
        min(
            0.05,
            saat.get_time() / 1000.0 if saat.get_time() else 1.0 / FPS,
        ),
    )
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA or oyuncu_hp <= 0:
        return
    v55_player_blood_transfer_tick(dt, now)
    live_uids = set()
    for enemy in common_enemies:
        if not bool(getattr(enemy, "active", False)):
            continue
        uid = str(getattr(enemy, "uid", id(enemy)))
        live_uids.add(uid)
        v55_enemy_blood_transfer_tick(enemy, dt, now)
    for actor in (
        globals().get("tarkard_actor"),
        globals().get("torrmund_actor"),
    ):
        if actor is None or not bool(getattr(actor, "active", False)):
            continue
        uid = str(getattr(actor, "uid", id(actor)))
        live_uids.add(uid)
        v55_enemy_blood_transfer_tick(actor, dt, now)
    stale = [uid for uid in v55_enemy_motion if uid not in live_uids]
    for uid in stale[:16]:
        v55_enemy_motion.pop(uid, None)


def v55_pool_scan(now=None):
    global v55_pool_clusters, v55_pool_next_scan_ms
    if now is None:
        now = pygame.time.get_ticks()
    if now < v55_pool_next_scan_ms:
        return v55_pool_clusters
    v55_pool_next_scan_ms = int(now) + V55_POOL_SCAN_INTERVAL_MS
    clusters = []
    seen = set()
    visible = []
    margin = 120.0 / max(0.01, KAMERA_YAKINLASTIRMA)
    left = kamera_x - margin
    right = kamera_x + GENISLIK / max(0.01, KAMERA_YAKINLASTIRMA) + margin
    top = kamera_y - margin
    bottom = kamera_y + YUKSEKLIK / max(0.01, KAMERA_YAKINLASTIRMA) + margin
    for decal in blood_decals:
        if left <= decal.x <= right and top <= decal.y <= bottom:
            visible.append(decal)
    visible = visible[-220:]
    for decal in visible:
        marker = id(decal)
        if marker in seen:
            continue
        near = [
            other
            for other in visible
            if id(other) not in seen
            and pygame.Vector2(float(other.x), float(other.y)).distance_to(
                (decal.x, decal.y)
            )
            <= V55_POOL_CLUSTER_RADIUS
        ]
        if len(near) < V55_POOL_CLUSTER_MIN:
            continue
        for item in near:
            seen.add(id(item))
        total_mass = sum(
            max(
                0.1,
                float(
                    getattr(
                        item,
                        "v44_stain_mass",
                        getattr(item, "scale", 1.0),
                    )
                ),
            )
            for item in near
        )
        cx = sum(float(item.x) for item in near) / len(near)
        cy = sum(float(item.y) for item in near) / len(near)
        wet = sum(
            1 for item in near if int(now) < int(getattr(item, "dry_after_ms", 0))
        ) / len(near)
        clusters.append(
            {
                "x": cx,
                "y": cy,
                "mass": total_mass,
                "count": len(near),
                "wet": wet,
                "surface": v53_surface_at(cx, cy),
            }
        )
        if len(clusters) >= V55_POOL_VISIBLE_MAX:
            break
    v55_pool_clusters = clusters
    return clusters
# </POTBO_STAGE S1296>

# <POTBO_STAGE S1298>


def dunya_simulasyon_guncelle():
    result = _v55_world_sim_original()
    v55_blood_motion_tick()
    return result
# </POTBO_STAGE S1298>

# <POTBO_STAGE S1323>
V57_BLOOD_FLOW_SPEED_MAX = 0.08
V57_BLOOD_FATIGUE_SPEED_MAX = 0.07
# </POTBO_STAGE S1323>

# <POTBO_STAGE S1325>

v57_state = {
    "flow": 0.0,
    "fatigue": 0.0,
    "precision": 0.0,
    "contact_streak": 0,
    "whiff_streak": 0,
    "last_attack_active": False,
    "attack_started_ms": -10000,
    "attack_finished_ms": -10000,
    "last_contact_ms": -10000,
    "last_contact_attack_started_ms": -10000,
    "last_update_ms": pygame.time.get_ticks(),
    "last_direction": "",
    "repeat_direction_count": 0,
    "last_damage_scalar": 1.0,
    "last_blood_scalar": 1.0,
    "last_result": "idle",
}
# </POTBO_STAGE S1325>

# <POTBO_STAGE S1333>


def v57_blood_velocity_scalar():
    flow = v57_clamp01(v57_state.get("flow", 0.0))
    fatigue = v57_clamp01(v57_state.get("fatigue", 0.0))
    precision = v57_clamp01(v57_state.get("precision", 0.0))
    scalar = 1.0 + V57_BLOOD_FLOW_SPEED_MAX * flow * precision
    scalar -= V57_BLOOD_FATIGUE_SPEED_MAX * fatigue
    return max(0.88, min(1.12, scalar))
# </POTBO_STAGE S1333>

# <POTBO_STAGE S1335>


def v57_reset():
    now = pygame.time.get_ticks()
    v57_state.update(
        {
            "flow": 0.0,
            "fatigue": 0.0,
            "precision": 0.0,
            "contact_streak": 0,
            "whiff_streak": 0,
            "last_attack_active": False,
            "attack_started_ms": -10000,
            "attack_finished_ms": -10000,
            "last_contact_ms": -10000,
            "last_contact_attack_started_ms": -10000,
            "last_update_ms": now,
            "last_direction": "",
            "repeat_direction_count": 0,
            "last_damage_scalar": 1.0,
            "last_blood_scalar": 1.0,
            "last_result": "idle",
        }
    )
# </POTBO_STAGE S1335>

# <POTBO_STAGE S1337>



_v57_blood_emit_original = kan_parcacigi_patlat


def kan_parcacigi_patlat(x, y, adet, guc=1.0, yon=None, arterial=False):
    ctx = v44_context_current() or {}
    melee_ctx = bool(ctx.get("player_melee", False)) or bool(ctx.get("melee", False))
    scalar = v57_blood_velocity_scalar() if melee_ctx else 1.0
    v57_state["last_blood_scalar"] = scalar
    return _v57_blood_emit_original(
        x,
        y,
        adet,
        float(guc) * scalar,
        yon=yon,
        arterial=arterial,
    )
# </POTBO_STAGE S1337>

# <POTBO_STAGE S1345>


def v57_diagnostics():
    return {
        "version": V57_VERSION,
        "flow": round(float(v57_state.get("flow", 0.0)), 4),
        "fatigue": round(float(v57_state.get("fatigue", 0.0)), 4),
        "precision": round(float(v57_state.get("precision", 0.0)), 4),
        "contact_streak": int(v57_state.get("contact_streak", 0)),
        "whiff_streak": int(v57_state.get("whiff_streak", 0)),
        "repeat_direction_count": int(v57_state.get("repeat_direction_count", 0)),
        "last_damage_scalar": round(float(v57_state.get("last_damage_scalar", 1.0)), 4),
        "last_blood_scalar": round(float(v57_state.get("last_blood_scalar", 1.0)), 4),
        "last_result": str(v57_state.get("last_result", "idle")),
    }
# </POTBO_STAGE S1345>

# <POTBO_STAGE S1347>




V58_MIST_MAX = 150
# </POTBO_STAGE S1347>

# <POTBO_STAGE S1350>


def v58_color(arterial=False, dark_bias=0.0):
    palette = V44_ARTERIAL_PALETTE if arterial else V44_BLOOD_PALETTE
    index_bias = int(round(v58_clamp01(dark_bias) * (len(palette) - 1) * 0.55))
    upper = max(0, len(palette) - 1 - index_bias)
    idx = random.randint(0, upper) if upper > 0 else 0
    color = palette[idx]

    scalar = random.uniform(0.72, 0.98)
    return tuple(max(0, min(255, int(c * scalar))) for c in color)
# </POTBO_STAGE S1350>

# <POTBO_STAGE S1352>


def v58_event_shape(speed, arterial, context):
    if isinstance(context, dict):
        shape = str(context.get("shape", ""))
        if shape:
            return shape
    if arterial:
        return "arterial_jet"
    if speed >= V44_BLOOD_FAST_KILL_SPEED:
        return "longitudinal"
    if speed <= V44_BLOOD_SLOW_KILL_SPEED:
        return "radial_asymmetric"
    return "fan_asymmetric"
# </POTBO_STAGE S1352>

# <POTBO_STAGE S1354>


class V58BloodFilament:
    __slots__ = (
        "head",
        "tail",
        "vel",
        "tail_vel",
        "width",
        "color",
        "created_ms",
        "life_ms",
        "arterial",
        "specular",
        "alive",
        "curvature",
    )

    def __init__(self, x, y, direction, speed, arterial=False, energy=1.0):
        base = v58_safe_dir(direction)
        angle = (
            random.uniform(-13.0, 13.0)
            if speed >= V44_BLOOD_FAST_KILL_SPEED
            else random.uniform(-24.0, 24.0)
        )
        vec = v58_rotate(base, angle)
        local_speed = max(170.0, float(speed) * random.uniform(0.30, 0.64)) * v58_clamp(
            energy, 0.7, 1.5
        )
        self.head = pygame.Vector2(float(x), float(y))
        length = random.uniform(7.0, 18.0) * v58_clamp(local_speed / 430.0, 0.65, 1.45)
        self.tail = self.head - vec * length
        self.vel = vec * local_speed + pygame.Vector2(0.0, random.uniform(-25.0, 5.0))
        self.tail_vel = self.vel * random.uniform(0.78, 0.92)
        self.width = random.uniform(0.8, 2.2)
        self.color = v58_color(
            arterial=arterial,
            dark_bias=random.uniform(0.0, 0.55),
        )
        self.created_ms = pygame.time.get_ticks()
        self.life_ms = random.randint(*V58_FILAMENT_LIFE_MS)
        self.arterial = bool(arterial)
        self.specular = bool(
            local_speed >= V58_WHITE_SPECULAR_SPEED and random.random() < 0.58
        )
        self.alive = True
        self.curvature = random.uniform(-27.0, 27.0)

    def update(self, dt, now):
        age = int(now) - int(self.created_ms)
        if age >= self.life_ms:
            self.alive = False
            return
        normal = pygame.Vector2(-self.vel.y, self.vel.x)
        if normal.length_squared() > 1e-8:
            normal = normal.normalize()
        self.vel += normal * self.curvature * dt
        self.vel.y += V58_GRAVITY * dt
        self.tail_vel.y += V58_GRAVITY * 0.92 * dt
        drag = math.exp(-V58_AIR_DRAG * dt)
        self.vel *= drag
        self.tail_vel *= drag
        self.head += self.vel * dt
        self.tail += self.tail_vel * dt
        if not v58_world_visible(self.head.x, self.head.y, margin=180.0):
            self.alive = False

    def draw(self, surface, silhouette=False):
        if not self.alive:
            return
        if not (
            v58_world_visible(self.head.x, self.head.y)
            or v58_world_visible(self.tail.x, self.tail.y)
        ):
            return
        now = pygame.time.get_ticks()
        t = v58_clamp01((now - self.created_ms) / max(1.0, float(self.life_ms)))
        alpha = int(220 * (1.0 - t) ** 1.5)
        if alpha <= 2:
            return
        p1 = (
            dunya_ekran_x(self.tail.x),
            dunya_ekran_y(self.tail.y),
        )
        p2 = (
            dunya_ekran_x(self.head.x),
            dunya_ekran_y(self.head.y),
        )
        width = max(1, int(round(self.width * KAMERA_YAKINLASTIRMA)))

        min_x = min(p1[0], p2[0]) - 4
        min_y = min(p1[1], p2[1]) - 4
        max_x = max(p1[0], p2[0]) + 4
        max_y = max(p1[1], p2[1]) + 4
        w = max(8, max_x - min_x + 1)
        h = max(8, max_y - min_y + 1)
        if w > GENISLIK + 40 or h > YUKSEKLIK + 40:
            return
        layer = pygame.Surface((w, h), pygame.SRCALPHA)
        lp1 = (p1[0] - min_x, p1[1] - min_y)
        lp2 = (p2[0] - min_x, p2[1] - min_y)
        base = (4, 3, 4, min(alpha, 160)) if silhouette else (*self.color, alpha)
        pygame.draw.line(layer, base, lp1, lp2, width)
        pygame.draw.circle(layer, base, lp2, max(1, width))
        if self.specular and not silhouette and alpha > 90:
            dx = lp2[0] - lp1[0]
            dy = lp2[1] - lp1[1]
            sx = lp1[0] + dx * 0.52
            sy = lp1[1] + dy * 0.52
            ex = lp1[0] + dx * 0.82
            ey = lp1[1] + dy * 0.82
            pygame.draw.line(
                layer,
                (244, 238, 238, min(180, alpha)),
                (int(sx), int(sy)),
                (int(ex), int(ey)),
                1,
            )
        surface.blit(layer, (min_x, min_y))
# </POTBO_STAGE S1354>

# <POTBO_STAGE S1358>


_v58_blood_emit_original = kan_parcacigi_patlat


def kan_parcacigi_patlat(x, y, adet, guc=1.0, yon=None, arterial=False):
    ctx = v44_context_current() or {}
    direction = yon
    if direction is None and isinstance(ctx, dict):
        direction = ctx.get("direction", None)
    v58_spawn_morphology(
        x,
        y,
        max(0, int(adet)),
        float(guc),
        direction,
        bool(arterial),
        context=ctx,
    )
    return _v58_blood_emit_original(x, y, adet, guc, yon=yon, arterial=arterial)


_v58_kan_gore_update_original = kan_gore_guncelle


def kan_gore_guncelle():
    result = _v58_kan_gore_update_original()
    v58_update()
    return result


_v58_blood_draw_original = kan_lekelerini_ciz


def kan_lekelerini_ciz(silhouette=False):
    result = _v58_blood_draw_original(silhouette=silhouette)
    v58_draw(ekran, silhouette=silhouette)
    return result
# </POTBO_STAGE S1358>

# <POTBO_STAGE S1361>





V59_TECHNIQUES = {
    "measured_opening": {
        "branch": "shared",
        "level": 3,
        "cooldown_ms": 950,
        "damage": 1.025,
        "blood_speed": 1.03,
        "blood_count": 1.00,
        "condition": "fresh_contact",
        "tr": "Ölçülü Açılış",
        "en": "Measured Opening",
    },
    "edge_arrival": {
        "branch": "shared",
        "level": 5,
        "cooldown_ms": 760,
        "damage": 1.018,
        "blood_speed": 1.05,
        "blood_count": 1.02,
        "condition": "precision",
        "tr": "Kenar Varışı",
        "en": "Edge Arrival",
    },
    "alternate_line": {
        "branch": "shared",
        "level": 8,
        "cooldown_ms": 840,
        "damage": 1.022,
        "blood_speed": 1.04,
        "blood_count": 1.02,
        "condition": "alternate_direction",
        "tr": "Ters Hat",
        "en": "Alternate Line",
    },
    "second_intention": {
        "branch": "shared",
        "level": 12,
        "cooldown_ms": 1050,
        "damage": 1.032,
        "blood_speed": 1.03,
        "blood_count": 1.02,
        "condition": "second_contact",
        "tr": "İkinci Niyet",
        "en": "Second Intention",
    },
    "wound_read": {
        "branch": "shared",
        "level": 16,
        "cooldown_ms": 1250,
        "damage": 1.028,
        "blood_speed": 1.06,
        "blood_count": 1.05,
        "condition": "wounded_target",
        "tr": "Yara Okuması",
        "en": "Wound Read",
    },
    "guard_return": {
        "branch": "shared",
        "level": 22,
        "cooldown_ms": 1500,
        "damage": 1.045,
        "blood_speed": 1.05,
        "blood_count": 1.03,
        "condition": "riposte",
        "tr": "Muhafız Dönüşü",
        "en": "Guard Return",
    },
    "final_measure_shared": {
        "branch": "shared",
        "level": 34,
        "cooldown_ms": 1800,
        "damage": 1.055,
        "blood_speed": 1.08,
        "blood_count": 1.06,
        "condition": "execution",
        "tr": "Son Ölçü",
        "en": "Final Measure",
    },
    "male_weighted_entry": {
        "branch": "male",
        "level": 4,
        "cooldown_ms": 980,
        "damage": 1.035,
        "blood_speed": 1.06,
        "blood_count": 1.03,
        "condition": "heavy_contact",
        "tr": "Ağırlıklı Giriş",
        "en": "Weighted Entry",
    },
    "male_deep_arc": {
        "branch": "male",
        "level": 9,
        "cooldown_ms": 1150,
        "damage": 1.042,
        "blood_speed": 1.09,
        "blood_count": 1.05,
        "condition": "heavy_precision",
        "tr": "Derin Yay",
        "en": "Deep Arc",
    },
    "male_red_channel": {
        "branch": "male",
        "level": 13,
        "cooldown_ms": 1320,
        "damage": 1.035,
        "blood_speed": 1.11,
        "blood_count": 1.07,
        "condition": "longitudinal",
        "tr": "Kızıl Kanal",
        "en": "Red Channel",
    },
    "male_stagger_press": {
        "branch": "male",
        "level": 17,
        "cooldown_ms": 1380,
        "damage": 1.048,
        "blood_speed": 1.05,
        "blood_count": 1.03,
        "condition": "low_enemy_poise",
        "tr": "Denge Baskısı",
        "en": "Stagger Press",
    },
    "male_low_guard_cut": {
        "branch": "male",
        "level": 21,
        "cooldown_ms": 1450,
        "damage": 1.038,
        "blood_speed": 1.07,
        "blood_count": 1.08,
        "condition": "low_stamina_heavy",
        "tr": "Alçak Muhafız Kesisi",
        "en": "Low Guard Cut",
    },
    "male_counterweight": {
        "branch": "male",
        "level": 31,
        "cooldown_ms": 1700,
        "damage": 1.062,
        "blood_speed": 1.08,
        "blood_count": 1.04,
        "condition": "riposte_heavy",
        "tr": "Karşı Ağırlık",
        "en": "Counterweight",
    },
    "male_execution_step": {
        "branch": "male",
        "level": 37,
        "cooldown_ms": 2100,
        "damage": 1.072,
        "blood_speed": 1.12,
        "blood_count": 1.09,
        "condition": "execution_heavy",
        "tr": "İnfaz Adımı",
        "en": "Execution Step",
    },
    "male_final_commitment": {
        "branch": "male",
        "level": 46,
        "cooldown_ms": 2600,
        "damage": 1.085,
        "blood_speed": 1.14,
        "blood_count": 1.10,
        "condition": "master_heavy",
        "tr": "Son Taahhüt",
        "en": "Final Commitment",
    },
    "female_angle_entry": {
        "branch": "female",
        "level": 4,
        "cooldown_ms": 760,
        "damage": 1.026,
        "blood_speed": 1.06,
        "blood_count": 1.02,
        "condition": "cross_angle",
        "tr": "Açılı Giriş",
        "en": "Angle Entry",
    },
    "female_short_second": {
        "branch": "female",
        "level": 9,
        "cooldown_ms": 720,
        "damage": 1.030,
        "blood_speed": 1.07,
        "blood_count": 1.03,
        "condition": "quick_second",
        "tr": "Kısa İkinci",
        "en": "Short Second",
    },
    "female_flow_cut": {
        "branch": "female",
        "level": 13,
        "cooldown_ms": 820,
        "damage": 1.033,
        "blood_speed": 1.08,
        "blood_count": 1.04,
        "condition": "high_flow",
        "tr": "Akış Kesisi",
        "en": "Flow Cut",
    },
    "female_capillary_line": {
        "branch": "female",
        "level": 17,
        "cooldown_ms": 1100,
        "damage": 1.025,
        "blood_speed": 1.06,
        "blood_count": 1.08,
        "condition": "wounded_precision",
        "tr": "Kılcal Hat",
        "en": "Capillary Line",
    },
    "female_narrow_fan": {
        "branch": "female",
        "level": 21,
        "cooldown_ms": 1060,
        "damage": 1.032,
        "blood_speed": 1.09,
        "blood_count": 1.05,
        "condition": "fan_shape",
        "tr": "Dar Yelpaze",
        "en": "Narrow Fan",
    },
    "female_countertempo": {
        "branch": "female",
        "level": 31,
        "cooldown_ms": 1420,
        "damage": 1.052,
        "blood_speed": 1.07,
        "blood_count": 1.04,
        "condition": "riposte",
        "tr": "Karşı Tempo",
        "en": "Countertempo",
    },
    "female_last_opening": {
        "branch": "female",
        "level": 37,
        "cooldown_ms": 1780,
        "damage": 1.060,
        "blood_speed": 1.10,
        "blood_count": 1.07,
        "condition": "execution",
        "tr": "Son Açıklık",
        "en": "Last Opening",
    },
    "female_final_measure": {
        "branch": "female",
        "level": 46,
        "cooldown_ms": 2250,
        "damage": 1.072,
        "blood_speed": 1.12,
        "blood_count": 1.08,
        "condition": "master_flow",
        "tr": "Son Ölçüm",
        "en": "Final Measure",
    },
}
# </POTBO_STAGE S1361>

# <POTBO_STAGE S1367>

v59_state = {
    "cooldowns": {},
    "history": [],
    "active_id": None,
    "active_until": 0,
    "last_contact_ms": -10000,
    "previous_direction": "",
    "last_direction": "",
    "contact_index": 0,
    "last_damage": 1.0,
    "last_blood_speed": 1.0,
    "last_blood_count": 1.0,
    "trigger_count": 0,
}
# </POTBO_STAGE S1367>

# <POTBO_STAGE S1374>


def v59_technique_score(technique_id, definition, enemy, now, before_hp):
    if not v59_skill_available(definition):
        return -1.0
    ready = int(v59_state["cooldowns"].get(technique_id, 0))
    if now < ready:
        return -1.0
    if not v59_condition_met(definition.get("condition", ""), enemy, now, before_hp):
        return -1.0
    level_gap = max(0, int(oyuncu_level) - int(definition.get("level", 1)))
    damage = float(definition.get("damage", 1.0)) - 1.0
    blood = float(definition.get("blood_speed", 1.0)) - 1.0

    return 1.0 + damage * 6.0 + blood * 2.0 + min(0.18, level_gap * 0.002)
# </POTBO_STAGE S1374>

# <POTBO_STAGE S1376>


def v59_activate(technique_id, now=None):
    if now is None:
        now = pygame.time.get_ticks()
    definition = V59_TECHNIQUES.get(technique_id)
    if not definition:
        return None
    cooldown = int(definition.get("cooldown_ms", 1000))
    v59_state["cooldowns"][technique_id] = int(now) + cooldown
    v59_state["active_id"] = technique_id
    v59_state["active_until"] = int(now) + V59_TECHNIQUE_FLASH_MS
    v59_state["trigger_count"] = int(v59_state.get("trigger_count", 0)) + 1
    history = v59_state["history"]
    history.append((int(now), technique_id))
    if len(history) > V59_TECHNIQUE_HISTORY_LIMIT:
        del history[:-V59_TECHNIQUE_HISTORY_LIMIT]
    v59_state["last_damage"] = float(definition.get("damage", 1.0))
    v59_state["last_blood_speed"] = float(definition.get("blood_speed", 1.0))
    v59_state["last_blood_count"] = float(definition.get("blood_count", 1.0))
    return definition
# </POTBO_STAGE S1376>

# <POTBO_STAGE S1378>


def v59_reset():
    v59_state["cooldowns"].clear()
    v59_state["history"].clear()
    v59_state["active_id"] = None
    v59_state["active_until"] = 0
    v59_state["last_contact_ms"] = -10000
    v59_state["previous_direction"] = ""
    v59_state["last_direction"] = ""
    v59_state["contact_index"] = 0
    v59_state["last_damage"] = 1.0
    v59_state["last_blood_speed"] = 1.0
    v59_state["last_blood_count"] = 1.0
# </POTBO_STAGE S1378>

# <POTBO_STAGE S1380>



_v59_blood_emit_original = kan_parcacigi_patlat


def kan_parcacigi_patlat(x, y, adet, guc=1.0, yon=None, arterial=False):
    definition = v59_active_definition()
    if definition is None:
        return _v59_blood_emit_original(x, y, adet, guc, yon=yon, arterial=arterial)
    ctx = v44_context_current() or {}
    is_melee = bool(ctx.get("player_melee", False)) or bool(oyuncu_saldiriyor)
    if not is_melee:
        return _v59_blood_emit_original(x, y, adet, guc, yon=yon, arterial=arterial)
    count_scalar = float(definition.get("blood_count", 1.0))
    speed_scalar = float(definition.get("blood_speed", 1.0))
    count = max(0, int(round(int(adet) * count_scalar)))
    return _v59_blood_emit_original(
        x,
        y,
        count,
        float(guc) * speed_scalar,
        yon=yon,
        arterial=arterial,
    )
# </POTBO_STAGE S1380>

# <POTBO_STAGE S1385>


def v59_diagnostics():
    now = pygame.time.get_ticks()
    active = v59_state.get("active_id")
    cooldown_ready = 0
    cooldown_wait = 0
    for technique_id, definition in V59_TECHNIQUES.items():
        if not v59_skill_available(definition):
            continue
        if now >= int(v59_state["cooldowns"].get(technique_id, 0)):
            cooldown_ready += 1
        else:
            cooldown_wait += 1
    return {
        "version": V59_VERSION,
        "active": str(active) if active else "",
        "active_name": v59_name(active) if active else "",
        "trigger_count": int(v59_state.get("trigger_count", 0)),
        "history": [item[1] for item in v59_state.get("history", [])[-5:]],
        "ready": cooldown_ready,
        "cooldown": cooldown_wait,
        "last_damage": round(float(v59_state.get("last_damage", 1.0)), 4),
        "last_blood_speed": round(float(v59_state.get("last_blood_speed", 1.0)), 4),
        "last_blood_count": round(float(v59_state.get("last_blood_count", 1.0)), 4),
        "unlocked": len(v59_unlocked_summary()),
    }
# </POTBO_STAGE S1385>

# <POTBO_STAGE S1403>










V62_VERSION = "62.0"




V62_CLOT_MIN_AGE = 0.18
# </POTBO_STAGE S1403>

# <POTBO_STAGE S1405>
v62_stats = {
    "decal_draws": 0,
    "clot_draws": 0,
    "meniscus_draws": 0,
    "detail_skips": 0,
}
# </POTBO_STAGE S1405>

# <POTBO_STAGE S1407>


def v62_wetness(decal, now):
    created = int(getattr(decal, "created_ms", now))
    dry = int(
        getattr(
            decal,
            "dry_after_ms",
            created + V43_BLOOD_DRY_MIN_MS,
        )
    )
    if now <= created:
        return 1.0
    if now >= dry:
        return 0.0
    return 1.0 - v44_smoothstep((now - created) / max(1.0, float(dry - created)))


def v62_clot_age(decal, now):
    created = int(getattr(decal, "created_ms", now))
    dry = int(
        getattr(
            decal,
            "dry_after_ms",
            created + V43_BLOOD_DRY_MIN_MS,
        )
    )
    if dry <= created:
        return 1.0
    return v44_clamp01((now - created) / max(1.0, float(dry - created)))


def v62_screen_bounds(decal):
    sx = dunya_ekran_x(float(decal.x))
    sy = dunya_ekran_y(float(decal.y))
    scale = max(0.08, float(getattr(decal, "scale", 1.0))) * KAMERA_YAKINLASTIRMA
    if BLOOD_DECAL_SPRITELERI:
        src = BLOOD_DECAL_SPRITELERI[
            int(getattr(decal, "sprite_index", 0)) % len(BLOOD_DECAL_SPRITELERI)
        ]
        w = max(3, int(src.get_width() * scale))
        h = max(2, int(src.get_height() * scale))
    else:
        w = max(6, int(12 * scale))
        h = max(4, int(7 * scale))
    return pygame.Rect(int(sx - w / 2), int(sy - h / 2), w, h)


def v62_draw_microstructure(decal, silhouette=False):
    if silhouette or not v62_budget_take():
        return
    rect = v62_screen_bounds(decal)
    if rect.width < V62_DETAIL_MIN_SCREEN_W or rect.height < 4:
        return
    if (
        rect.right < 0
        or rect.left > GENISLIK
        or rect.bottom < 0
        or rect.top > YUKSEKLIK
    ):
        return
    now = pygame.time.get_ticks()
    wet = v62_wetness(decal, now)
    age = v62_clot_age(decal, now)
    seed = int(getattr(decal, "v44_seed", id(decal) & 0x7FFFFFFF))
    surface_name = str(getattr(decal, "v53_surface", "unknown"))
    absorption = float(getattr(decal, "v53_absorption", 0.52))
    gloss = float(getattr(decal, "v44_gloss", 0.55))
    layer = pygame.Surface(rect.size, pygame.SRCALPHA)


    if wet > 0.12 and rect.width >= 12:
        alpha = int(V62_MENISCUS_MAX_ALPHA * wet * gloss * (1.0 - absorption * 0.28))
        if alpha > 7:
            segments = 1 + int(v62_hash01(seed, 1) > 0.46)
            for idx in range(segments):
                u = 0.18 + v62_hash01(seed, idx, 5) * 0.56
                length = max(
                    2,
                    int(rect.width * (0.08 + v62_hash01(seed, idx, 7) * 0.16)),
                )
                x0 = int(rect.width * u - length / 2)
                y0 = max(
                    1,
                    int(rect.height * (0.23 + v62_hash01(seed, idx, 9) * 0.14)),
                )
                pygame.draw.line(
                    layer,
                    (251, 247, 246, alpha),
                    (x0, y0),
                    (x0 + length, max(1, y0 - 1)),
                    1,
                )
                v62_stats["meniscus_draws"] += 1


    if V62_CLOT_MIN_AGE <= age <= V62_CLOT_MAX_AGE:
        phase_in = v44_smoothstep((age - V62_CLOT_MIN_AGE) / 0.24)
        phase_out = 1.0 - v44_smoothstep(max(0.0, age - 0.67) / 0.21)
        clot_alpha = int(94 * phase_in * phase_out)
        count = V62_CLOT_COUNT[0] + int(
            v62_hash01(seed, 12) * (V62_CLOT_COUNT[1] - V62_CLOT_COUNT[0] + 1)
        )
        if surface_name in ("dirt", "mud"):
            count = max(1, count - 2)
        for idx in range(count):
            u = 0.18 + v62_hash01(seed, idx, 20) * 0.64
            v = 0.24 + v62_hash01(seed, idx, 21) * 0.52
            rw = max(
                1,
                int(rect.width * (0.025 + v62_hash01(seed, idx, 22) * 0.065)),
            )
            rh = max(
                1,
                int(rect.height * (0.04 + v62_hash01(seed, idx, 23) * 0.10)),
            )
            x = int(rect.width * u)
            y = int(rect.height * v)
            tone = int(8 + v62_hash01(seed, idx, 24) * 12)
            pygame.draw.ellipse(
                layer,
                (tone + 10, tone // 3, tone // 2, clot_alpha),
                (x - rw, y - rh, rw * 2, rh * 2),
            )
            v62_stats["clot_draws"] += 1


    if age > 0.34:
        edge_alpha = int(V62_EDGE_DARK_ALPHA * v44_smoothstep((age - 0.34) / 0.48))
        if edge_alpha > 5 and rect.width >= 12 and rect.height >= 6:
            pygame.draw.arc(
                layer,
                (20, 1, 4, edge_alpha),
                pygame.Rect(1, 1, rect.width - 2, rect.height - 2),
                math.radians(188),
                math.radians(318),
                1,
            )
            if v62_hash01(seed, 50) > 0.37:
                pygame.draw.arc(
                    layer,
                    (25, 1, 5, edge_alpha // 2),
                    pygame.Rect(2, 1, rect.width - 4, rect.height - 2),
                    math.radians(8),
                    math.radians(92),
                    1,
                )

    ekran.blit(layer, rect.topleft)
    v62_stats["decal_draws"] += 1


_v62_decal_parent = PersistentBloodDecal


class PersistentBloodDecal(_v62_decal_parent):
    def __init__(self, x, y, scale=None, rotation=None, sprite_index=None):
        super().__init__(
            x,
            y,
            scale=scale,
            rotation=rotation,
            sprite_index=sprite_index,
        )

        base_seed = int(getattr(self, "v44_seed", random.randrange(1, 2**30)))
        pos_seed = int(abs(float(x) * 73.0 + float(y) * 151.0))
        self.v62_seed = (base_seed ^ pos_seed) & 0x7FFFFFFF
        self.v44_seed = self.v62_seed

    def ciz(self, silhouette=False):
        result = super().ciz(silhouette=silhouette)
        v62_draw_microstructure(self, silhouette=silhouette)
        return result


def v62_diagnostics():
    return {
        "version": V62_VERSION,
        "detail_budget": int(v62_detail_draw_budget),
        "decal_draws": int(v62_stats.get("decal_draws", 0)),
        "clot_draws": int(v62_stats.get("clot_draws", 0)),
        "meniscus_draws": int(v62_stats.get("meniscus_draws", 0)),
        "detail_skips": int(v62_stats.get("detail_skips", 0)),
        "decal_class": PersistentBloodDecal.__name__,
    }
# </POTBO_STAGE S1407>

# <POTBO_STAGE S1409>










V63_VERSION = "63.0"
# </POTBO_STAGE S1409>

# <POTBO_STAGE S1420>


def v65_emit_jet(emitter, now, pressure, direction, secondary=False):
    count_base = random.randint(
        V44_PLAYER_DEATH_ARTERIAL_MIN_PARTICLES,
        V44_PLAYER_DEATH_ARTERIAL_MAX_PARTICLES,
    )
    if secondary:
        count = max(4, int(round(count_base * (0.34 + 0.22 * pressure))))
        speed = 430.0 + 260.0 * pressure
        power = 0.82 + 0.48 * pressure
        local_dir = direction.rotate(
            random.choice((-1, 1)) * random.uniform(12.0, V65_SECONDARY_JET_ANGLE)
        )
    else:
        count = max(7, int(round(count_base * (0.62 + 0.58 * pressure))))
        speed = 590.0 + 360.0 * pressure
        power = 1.00 + 0.92 * pressure
        local_dir = direction.rotate(
            random.uniform(-V65_PRIMARY_JET_ANGLE, V65_PRIMARY_JET_ANGLE)
        )
    context = v44_blood_spawn_context(
        profile=emitter.profile,
        lethal=True,
        source="death_artery",
        target="player",
        speed=speed,
        direction=local_dir,
        damage=0,
        arterial=True,
    )
    context["shape"] = "arterial_jet"
    context["arterial_pressure"] = pressure
    context["blood_volume"] = 1.0 + 0.16 * pressure
    context["tissue_viscosity"] = 0.92 + 0.08 * (1.0 - pressure)
    v44_context_push(context)
    try:
        emitted = kan_parcacigi_patlat(
            emitter.x + emitter.origin_jitter.x + random.uniform(-1.5, 1.5),
            emitter.y + emitter.origin_jitter.y + random.uniform(-1.0, 1.8),
            count,
            guc=power,
            yon=local_dir,
            arterial=True,
        )
    finally:
        v44_context_pop()
    v65_stats["last_pressure"] = pressure
    v65_stats["last_speed"] = speed
    v65_stats["last_angle"] = math.degrees(math.atan2(local_dir.y, local_dir.x))
    if secondary:
        v65_stats["secondary"] += 1
    return emitted
# </POTBO_STAGE S1420>

# <POTBO_STAGE S1423>


def v66_check_contracts():
    issues = []

    try:
        nr, nw, hr, hw = _v38_player_reach_values()
        if nr < 49 or hr < 64:
            issues.append(v66_issue("sword_reach_regression", (nr, hr)))
        if nw <= 0 or hw <= 0:
            issues.append(v66_issue("sword_width_invalid", (nw, hw)))
    except Exception as exc:
        issues.append(v66_issue("sword_reach_error", type(exc).__name__))

    keys = v66_test_keys_normalized()
    required = [str(key).replace(" ", "").upper() for key in V50_REQUIRED_TEST_KEYS]
    missing = [key for key in required if key not in keys]
    if missing:
        issues.append(v66_issue("test_panel_missing", ",".join(missing)))
    if len(keys) != len(set(keys)):
        issues.append(v66_issue("test_panel_duplicate", len(keys)))

    if len(V44_BLOOD_PALETTE) != len(set(V44_BLOOD_PALETTE)):
        issues.append(v66_issue("blood_palette_duplicate"))
    if max(max(color) for color in V44_BLOOD_PALETTE) > 150:
        issues.append(v66_issue("blood_palette_too_bright"))

    if int(KARAKTER_ONAY_GECIS_SURESI) < int(V60_CHARACTER_WAVEFORM_MS):
        issues.append(v66_issue("character_transition_cuts_audio"))
    if int(KARAKTER_ONAY_GECIS_SURESI) > 3400:
        issues.append(v66_issue("character_transition_excess_tail"))

    if V58_MIST_MAX > V44_BLOOD_MAX_PARTICLES:
        issues.append(v66_issue("mist_budget_unbounded"))
    if V63_TIERS["constrained"]["lobe"] >= V63_TIERS["high"]["lobe"]:
        issues.append(v66_issue("adaptive_budget_order"))

    if not callable(getattr(V44ArterialEmitter, "update", None)):
        issues.append(v66_issue("arterial_update_missing"))
    if not callable(getattr(PersistentBloodDecal, "ciz", None)):
        issues.append(v66_issue("decal_draw_missing"))
    return issues


def v66_repair_runtime():
    global v66_repairs
    repairs = 0

    numeric_pairs = (
        ("oyuncu_stamina", 0.0, float(oyuncu_max_stamina)),
        ("stamina_gorunen", 0.0, float(oyuncu_max_stamina)),
        ("mana_gorunen", 0.0, float(oyuncu_max_mana)),
        ("hp_gorunen", 0.0, float(oyuncu_max_hp)),
    )
    g = globals()
    for name, lo, hi in numeric_pairs:
        value = g.get(name)
        try:
            finite = math.isfinite(float(value))
        except Exception:
            finite = False
        if not finite:
            fallback = (
                lo if name != "hp_gorunen" else max(lo, min(hi, float(oyuncu_hp)))
            )
            g[name] = fallback
            repairs += 1
        elif float(value) < lo - 1.0 or float(value) > hi + 5.0:
            g[name] = max(lo, min(hi, float(value)))
            repairs += 1


    active_ids = {
        str(getattr(e, "uid", ""))
        for e in common_enemies
        if getattr(e, "active", False)
    }
    for mapping in (
        v45_bleed_state,
        v56_enemy_state,
        v61_reactions,
    ):
        for uid in list(mapping.keys()):
            entry = mapping.get(uid, {})
            enemy = entry.get("enemy") if isinstance(entry, dict) else None
            if uid not in active_ids and (
                enemy is None or not getattr(enemy, "active", False)
            ):
                mapping.pop(uid, None)
                repairs += 1
    v66_repairs += repairs
    return repairs


def v66_runtime_audit(force=False):
    global v66_next_audit_ms, v66_last_issues
    now = pygame.time.get_ticks()
    if not force and now < int(v66_next_audit_ms):
        return v66_history[-1] if v66_history else None
    v66_next_audit_ms = int(now) + V66_AUDIT_INTERVAL_MS
    issues = v66_check_contracts()
    repairs = v66_repair_runtime()
    record = {
        "ms": int(now),
        "issues": issues,
        "repair_count": int(repairs),
        "blood_particles": len(blood_particles),
        "blood_decals": len(blood_decals),
        "gore_chunks": len(gore_chunks),
        "enemy_count": len(common_enemies),
    }
    v66_last_issues = issues
    v66_history.append(record)
    return record
# </POTBO_STAGE S1423>

# <POTBO_STAGE S1443>


_v68_palette_original = v44_blood_palette_for


def v44_blood_palette_for(arterial=False, oxygenation=None, age01=0.0, clot=False):
    base = _v68_palette_original(
        arterial=arterial,
        oxygenation=oxygenation,
        age01=age01,
        clot=clot,
    )
    key = v68_context_signature_key()
    tone = v68_apply_signature(base, key)
    if clot:
        tone = tuple(max(0, int(channel * 0.78)) for channel in tone)
    elif age01 > 0.0:
        dark = 1.0 - 0.24 * v44_clamp01(age01)
        tone = tuple(max(0, int(channel * dark)) for channel in tone)
    return tone
# </POTBO_STAGE S1443>

# <POTBO_STAGE S1450>


def v70_final_contract():
    report = {
        "version": V70_VERSION,
        "blood_pipeline_procedural": BloodParticle is V44BloodParticle,
        "blood_palette_dark": max(max(c) for c in V44_BLOOD_PALETTE) <= 150,
        "blood_palette_varied": len(set(V44_BLOOD_PALETTE)) >= 10,
        "arterial_emitter_callable": callable(
            getattr(V44ArterialEmitter, "update", None)
        ),
        "measured_blade_speed": callable(v44_attack_speed_estimate),
        "skill_catalog_count": len(V52_SKILL_CATALOG),
        "technique_count": len(V59_TECHNIQUES),
        "selection_waveform_ms": int(V60_CHARACTER_WAVEFORM_MS),
        "selection_transition_ms": int(KARAKTER_ONAY_GECIS_SURESI),
        "adaptive_tiers": tuple(V63_TIERS.keys()),
    }
    keys = tuple(str(row[0]).replace(" ", "").upper() for row in v46_test_rows())
    report["test_keys"] = keys
    report["all_test_keys_visible"] = all(key in keys for key in V70_EXPECTED_TEST_KEYS)
    report["reach"] = v67_reach_contract()
    report["reach_checks"] = v69_reach_assertions()
    report["runtime_issues"] = v66_check_contracts()
    report["all_ok"] = bool(
        report["blood_pipeline_procedural"]
        and report["blood_palette_dark"]
        and report["blood_palette_varied"]
        and report["arterial_emitter_callable"]
        and report["all_test_keys_visible"]
        and all(report["reach_checks"].values())
        and not report["runtime_issues"]
        and report["selection_transition_ms"] >= report["selection_waveform_ms"]
    )
    return report
# </POTBO_STAGE S1450>

# <POTBO_STAGE S1452>


def v70_full_diagnostics():
    report = v70_refresh_startup_report()
    return {
        "version": V70_VERSION,
        "startup_ok": bool(v70_startup_ok),
        "contract": report,
        "blood": v58_diagnostics(),
        "blood_surface": v62_diagnostics(),
        "arterial": v65_diagnostics(),
        "combat": v57_diagnostics(),
        "techniques": v59_diagnostics(),
        "trajectory": v67_diagnostics(),
        "runtime": v66_diagnostics(),
    }
# </POTBO_STAGE S1452>

# <POTBO_STAGE S1454>


_v71_blood_emit_original = kan_parcacigi_patlat


def kan_parcacigi_patlat(x, y, adet, guc=1.0, yon=None, arterial=False):
    before = len(blood_particles)
    context = dict(v44_context_current() or {})
    shape = str(
        context.get("shape")
        or v44_impact_shape_from_speed(
            float(context.get("speed", 560.0 if arterial else 430.0)),
            lethal=bool(context.get("lethal", False)),
            arterial=bool(arterial or context.get("arterial", False)),
        )
    )
    result = _v71_blood_emit_original(x, y, adet, guc, yon=yon, arterial=arterial)
    after = len(blood_particles)
    if after > before:
        created = list(blood_particles[before:after])
        v71_measure_event(shape, created, context=context)
    return result
# </POTBO_STAGE S1454>

# <POTBO_STAGE S1460>


def v72_release_checks():
    checks = {}
    nr, nw, hr, hw = _v38_player_reach_values()
    checks["reach_bonus"] = int(V44_SWORD_REACH_BONUS_PX) == 6
    checks["normal_reach_valid"] = int(nr) >= 49 and int(nw) > 0
    checks["heavy_reach_valid"] = int(hr) >= int(nr) and int(hw) > 0
    checks["dark_blood"] = max(max(c) for c in V44_BLOOD_PALETTE) <= 150
    checks["blood_variants"] = len(set(V44_BLOOD_PALETTE)) >= 10
    checks["arterial_pressure_curve"] = len(V65_PRESSURE_CURVE) >= 6
    checks["fast_shape_measured"] = "longitudinal" in V71_EXPECTED
    checks["slow_shape_measured"] = "radial_asymmetric" in V71_EXPECTED
    checks["white_specular"] = (
        V44_BLOOD_WHITE_GLINT_ALPHA > 0 and V62_SPECULAR_MAX_ALPHA > 0
    )
    checks["skill_depth"] = len(V52_SKILL_CATALOG) >= 20 and len(V59_TECHNIQUES) >= 20
    checks["waveform_sync"] = int(V60_CHARACTER_WAVEFORM_MS) == 2500
    checks["transition_not_cut"] = int(KARAKTER_ONAY_GECIS_SURESI) >= int(
        V60_CHARACTER_WAVEFORM_MS
    )
    visible_keys = tuple(
        str(row[0]).replace(" ", "").upper() for row in v46_test_rows()
    )
    checks["test_panel_complete"] = all(
        key in visible_keys for key in V70_EXPECTED_TEST_KEYS
    )
    checks["adaptive_budget"] = set(V63_TIERS) == {
        "high",
        "balanced",
        "constrained",
    }
    checks["procedural_blood_pipeline"] = BloodParticle is V44BloodParticle
    return checks
# </POTBO_STAGE S1460>

# <POTBO_STAGE S1462>







def v72_release_summary_lines():
    """Developer console/debug export için kısa, hesaplanmış release özeti."""
    snap = v72_release_snapshot_refresh()
    reach = snap.get("reach", {})
    return [
        f"release={snap.get('target')} v{V72_VERSION}",
        f"checks={snap.get('passed')}/{snap.get('total')} ok={int(bool(snap.get('all_ok')))}",
        f"reach normal={reach.get('normal_reach_px')} heavy={reach.get('heavy_reach_px')} bonus={reach.get('added_px')}",
        f"skills passive={len(V52_SKILL_CATALOG)} conditional={len(V59_TECHNIQUES)}",
        f"blood particles={len(blood_particles)} decals={len(blood_decals)} metrology={len(v71_events)}",
        f"ui tests={len(v46_test_rows())} waveform={V60_CHARACTER_WAVEFORM_MS}ms",
    ]
# </POTBO_STAGE S1462>

# <POTBO_STAGE S1464>









V73_VERSION = "73.0"
# </POTBO_STAGE S1464>

# <POTBO_STAGE S1466>
V73_GORE_LANDING_SATELLITE_MAX = 4



V40_BLOOD_PER_CELL_MAX = max(int(V40_BLOOD_PER_CELL_MAX), 26)
V40_BLOOD_GLOBAL_MAX = max(int(V40_BLOOD_GLOBAL_MAX), 1240)
V40_BLOOD_VISIBLE_MAX = max(int(V40_BLOOD_VISIBLE_MAX), 360)
V42_BLOOD_VISIBLE_RECENT = max(int(V42_BLOOD_VISIBLE_RECENT), 230)
V42_BLOOD_VISIBLE_OLDER = max(
    0,
    int(V40_BLOOD_VISIBLE_MAX) - int(V42_BLOOD_VISIBLE_RECENT),
)
# </POTBO_STAGE S1466>

# <POTBO_STAGE S1469>
v73_stats = {
    "ground_conversion_decals": 0,
    "landing_satellites": 0,
    "gore_landing_decals": 0,
    "blast_deaths": 0,
    "blast_chunks": 0,
}
# </POTBO_STAGE S1469>

# <POTBO_STAGE S1471>


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
    """Düşük profilli zeminsel sıçrama.

    Her çağrı çok sayıda büyük decal üretmez. Ana yön çevresinde küçük, farklı boyutlu
    damlalar bırakır; az miktarda ters/yan saçılma steril fan görünümünü kırar.
    """
    global v73_stats
    count = max(0, int(count))
    if count <= 0:
        return 0
    base = v73_safe_direction(direction)
    created = 0
    lo_scale, hi_scale = (
        float(scale_range[0]),
        float(scale_range[1]),
    )
    lo_dist, hi_dist = (
        float(distance_range[0]),
        float(distance_range[1]),
    )
    for i in range(count):
        if random.random() < float(backscatter):
            angle = random.choice((-1.0, 1.0)) * random.uniform(78.0, 154.0)
        else:
            mode = -9.0 if (i % 3) else 12.0
            angle = random.triangular(-float(cone_deg), float(cone_deg), mode)
        d = base.rotate(angle)

        r01 = random.random() ** 1.55
        dist = lo_dist + (hi_dist - lo_dist) * r01
        lateral = random.uniform(-1.6, 1.6)
        tangent = pygame.Vector2(-d.y, d.x)
        p = pygame.Vector2(float(x), float(y)) + d * dist + tangent * lateral
        size = random.uniform(lo_scale, hi_scale)
        if i == 0 and count >= 4:
            size *= random.uniform(1.08, 1.24)
        decal = kan_lekesi_ekle(p.x, p.y, size)
        if decal is not None:
            try:
                decal.v73_ground_source = str(source)
            except Exception:
                pass
            created += 1
    return created





_v73_blood_emit_original = kan_parcacigi_patlat


def kan_parcacigi_patlat(x, y, adet, guc=1.0, yon=None, arterial=False):
    """Aynı kan hacmini daha zeminsel dağıtır.

    Arter jetinde havadaki sprite sayısı düşer. Kesilen miktarın küçük bir bölümü
    doğrudan düşük profilli zemin sıçramasına çevrilir; kalan hava damlaları da daha
    düşük vz ve biraz yüksek gravity ile daha erken yere ulaşır.
    """
    requested = max(0, int(adet))
    if requested <= 0:
        return _v73_blood_emit_original(x, y, 0, guc, yon=yon, arterial=arterial)

    context = dict(v44_context_current() or {})
    source = str(context.get("source", "")).lower()
    is_blast = any(
        token in source
        for token in (
            "blast",
            "explosion",
            "bomb",
            "grenade",
            "patlama",
        )
    )
    is_death_artery = bool(arterial and source == "death_artery")

    if is_death_artery:
        scalar = V73_DEATH_ARTERY_AIR_COUNT
    elif arterial:
        scalar = V73_ARTERIAL_AIR_COUNT
    elif is_blast:
        scalar = V73_BLAST_AIR_COUNT
    else:
        scalar = V73_NORMAL_AIR_COUNT

    air_count = max(1, int(round(requested * scalar)))
    converted = max(0, requested - air_count)
    before = len(blood_particles)
    result = _v73_blood_emit_original(x, y, air_count, guc, yon=yon, arterial=arterial)
    created = list(blood_particles[before:])


    for particle in created:
        if not hasattr(particle, "vz"):
            continue
        if is_blast:
            vz_scale = V73_BLAST_VZ_SCALE
        elif arterial:
            vz_scale = V73_ARTERIAL_VZ_SCALE
        else:
            vz_scale = V73_NORMAL_VZ_SCALE
        particle.vz *= vz_scale * random.uniform(0.92, 1.04)
        particle.z *= random.uniform(0.90, 1.00)
        if hasattr(particle, "gravity"):
            particle.gravity *= V73_GRAVITY_SCALE * random.uniform(0.97, 1.04)

        if arterial and hasattr(particle, "v"):
            particle.v *= random.uniform(0.90, 0.97)
        try:
            particle.v73_ground_weighted = True
        except Exception:
            pass

    if converted > 0:
        floor_count = min(
            V73_GROUND_CONVERSION_MAX,
            max(
                1,
                int(math.ceil(converted / float(V73_GROUND_CONVERSION_DIVISOR))),
            ),
        )
        base = v73_safe_direction(yon if yon is not None else (1.0, 0.0))
        power = max(0.45, min(2.4, float(guc)))
        if arterial:
            floor_count = min(V73_GROUND_CONVERSION_MAX, floor_count + 1)
        made = v73_ground_splatter(
            x,
            y,
            base,
            floor_count,
            scale_range=(0.14 * power, 0.36 * power),
            distance_range=(2.5, 12.0 + 8.0 * power),
            cone_deg=34.0 if arterial else 62.0,
            backscatter=0.08 if arterial else 0.14,
            source="air_conversion",
        )
        v73_stats["ground_conversion_decals"] += made
    return result




_v73_v44_particle_update_original = V44BloodParticle.guncelle
# </POTBO_STAGE S1471>

# <POTBO_STAGE S1473>





_v73_gore_chunk_update_original = GoreChunk.guncelle


def _v73_gore_chunk_update(self, dt, simdi):
    was_settled = bool(getattr(self, "settled", False))
    pre_bounces = int(getattr(self, "bounces", 0))
    pre_v = pygame.Vector2(getattr(self, "v", (0.0, 0.0)))
    pre_speed = pre_v.length()
    result = _v73_gore_chunk_update_original(self, dt, simdi)


    if (
        not was_settled
        and not bool(getattr(self, "settled", False))
        and int(getattr(self, "bounces", 0)) > pre_bounces
        and pre_speed > 105.0
        and random.random() < 0.32
    ):
        made = v73_ground_splatter(
            self.x,
            self.y,
            pre_v,
            1,
            scale_range=(0.16, 0.34),
            distance_range=(2.0, 8.0),
            cone_deg=72.0,
            backscatter=0.22,
            source="gore_bounce",
        )
        v73_stats["gore_landing_decals"] += made

    if not was_settled and bool(getattr(self, "settled", False)):
        blast = bool(getattr(self, "v73_blast_chunk", False))
        flesh = str(getattr(self, "kind", "")) in {
            "intestine",
            "liver",
            "organ_mass_a",
            "organ_mass_b",
            "organ_round_a",
            "organ_round_b",
            "flesh_shard_a",
            "flesh_shard_b",
        }
        count = 1 + int(pre_speed > 110.0) + int(pre_speed > 220.0)
        if blast and flesh:
            count += 1
        count = min(V73_GORE_LANDING_SATELLITE_MAX, count)
        made = v73_ground_splatter(
            self.x,
            self.y,
            pre_v if pre_v.length_squared() > 1e-8 else (1.0, 0.0),
            count,
            scale_range=(0.18, 0.50 if flesh else 0.38),
            distance_range=(
                2.0,
                min(20.0, 6.0 + pre_speed * 0.045),
            ),
            cone_deg=92.0,
            backscatter=0.24,
            source="gore_settle",
        )
        v73_stats["gore_landing_decals"] += made
    return result


GoreChunk.guncelle = _v73_gore_chunk_update





_v73_gore_death_original = gore_olum_patlamasi
# </POTBO_STAGE S1473>

# <POTBO_STAGE S1475>





def v73_blast_gore_burst(x, y, merkez_x, merkez_y, tier="core"):
    """Patlama öldürürse okunabilir ama kuvvetli parçalanma.

    Core çok parçalıdır; inner daha az parçayla gövde bütünlüğünü kısmen korur.
    70-90 anatomik obje yerine 18-44 fiziksel parça kullanılır; etkiyi asıl artıran
    şey daha iyi momentum, zeminsel kan ve landing izleridir.
    """
    tier = "core" if str(tier) == "core" else "inner"
    center = pygame.Vector2(float(merkez_x), float(merkez_y))
    victim = pygame.Vector2(float(x), float(y))
    away = victim - center
    if away.length_squared() <= 1e-8:
        away = pygame.Vector2(1.0, 0.0).rotate(random.uniform(0.0, 360.0))
    away = away.normalize()

    kinds = list(GORE_SPRITELERI.keys())
    preferred = [
        k
        for k in (
            "intestine",
            "liver",
            "organ_mass_a",
            "organ_mass_b",
            "flesh_shard_a",
            "flesh_shard_b",
            "organ_round_a",
            "organ_round_b",
            "ribcage",
            "spinal_cord",
            "skull",
            "leg",
            "foot",
            "bone_long_a",
            "bone_long_b",
            "bone_cluster_a",
            "bone_cluster_b",
        )
        if k in kinds
    ]
    if not preferred:
        preferred = kinds or ["liver", "intestine"]

    if tier == "core":
        count = random.randint(34, 44)
        readable = random.randint(9, 12)
        speed_lo, speed_hi = 255.0, 575.0
        lift_lo, lift_hi = 190.0, 430.0
        ground_count = random.randint(22, 30)
        air_blood = random.randint(70, 94)
        blood_power = random.uniform(1.48, 1.72)
    else:
        count = random.randint(18, 26)
        readable = random.randint(5, 7)
        speed_lo, speed_hi = 150.0, 365.0
        lift_lo, lift_hi = 110.0, 285.0
        ground_count = random.randint(12, 18)
        air_blood = random.randint(42, 58)
        blood_power = random.uniform(1.16, 1.38)

    for i in range(count):
        kind = (
            preferred[i % len(preferred)]
            if i < len(preferred)
            else random.choice(preferred)
        )
        small = i >= readable or random.random() < (0.20 if tier == "core" else 0.30)
        chunk = GoreChunk(
            kind,
            x,
            y,
            guc=random.uniform(1.05, 1.48 if tier == "core" else 1.26),
            small=small,
        )

        roll = random.random()
        if roll < 0.67:
            d = away.rotate(random.uniform(-72.0, 72.0))
        elif roll < 0.88:
            d = away.rotate(random.choice((-1.0, 1.0)) * random.uniform(74.0, 142.0))
        else:
            d = away.rotate(random.uniform(148.0, 212.0))
        d = v73_safe_direction(d)
        speed = random.uniform(speed_lo, speed_hi) * (0.78 if small else 1.0)
        chunk.v = d * speed
        chunk.vz = random.uniform(lift_lo, lift_hi) * (0.88 if small else 1.0)
        chunk.angular = (
            random.uniform(-860.0, 860.0)
            if tier == "core"
            else random.uniform(-640.0, 640.0)
        )
        chunk.v73_blast_chunk = True
        chunk.v73_blast_tier = tier
        gore_chunks.append(chunk)
        v73_stats["blast_chunks"] += 1


    context = v44_blood_spawn_context(
        profile="magic_heavy",
        lethal=True,
        source=f"blast_{tier}_v73",
        target="player",
        speed=420.0 if tier == "core" else 320.0,
        direction=away,
        damage=0,
        arterial=False,
    )
    context["shape"] = "radial_asymmetric"
    v44_context_push(context)
    try:
        kan_parcacigi_patlat(
            x,
            y - 7.0,
            air_blood,
            guc=blood_power,
            yon=away,
            arterial=False,
        )
    finally:
        v44_context_pop()

    made = v73_ground_splatter(
        x,
        y,
        away,
        ground_count,
        scale_range=(0.24, 0.86 if tier == "core" else 0.66),
        distance_range=(3.0, 56.0 if tier == "core" else 38.0),
        cone_deg=118.0 if tier == "core" else 98.0,
        backscatter=0.24,
        source=f"blast_{tier}",
    )
    v73_stats["ground_conversion_decals"] += made


    pool_seeds = random.randint(4, 7) if tier == "core" else random.randint(2, 4)
    for _ in range(pool_seeds):
        kan_lekesi_ekle(
            x + random.uniform(-11.0, 11.0),
            y + random.uniform(-8.0, 10.0),
            random.uniform(0.72, 1.28 if tier == "core" else 1.04),
        )
    return count


def gore_patlama_infazi(x, y, merkez_x, merkez_y):
    return v73_blast_gore_burst(x, y, merkez_x, merkez_y, tier="core")


def gore_patlama_birinci_katman_infazi(x, y, merkez_x, merkez_y):
    return v73_blast_gore_burst(x, y, merkez_x, merkez_y, tier="inner")
# </POTBO_STAGE S1475>

# <POTBO_STAGE S1478>


def oyuncu_kanli_hasar_kaydi(kaynak_x, kaynak_y, profil, hasar, kaynak_adi=""):
    global oyuncu_olum_turu, oyuncu_olum_alt_turu
    global oyuncu_olum_patlama_seed, oyuncu_olum_patlama_yonu
    global \
        oyuncu_olum_katil_uid, \
        oyuncu_olum_katil_tur, \
        oyuncu_olum_katil_kan_sonraki_ms
    global v44_player_death_arterial_done, v73_player_blast_fragmented

    result = _v73_player_damage_original(kaynak_x, kaynak_y, profil, hasar, kaynak_adi)
    if oyuncu_hp > 0:
        return result

    tier = v73_blast_source_tier(kaynak_adi, profil)
    if tier is None:
        return result




    v44_arterial_emitters.clear()
    v44_player_death_arterial_done = True

    oyuncu_olum_turu = "blast_core" if tier == "core" else "blast_inner"
    oyuncu_olum_alt_turu = oyuncu_olum_turu
    oyuncu_olum_patlama_seed = random.randint(1, 2_000_000)
    direction = pygame.Vector2(
        float(oyuncu_x) - float(kaynak_x),
        float(oyuncu_y) - float(kaynak_y),
    )
    if direction.length_squared() <= 1e-8:
        direction = pygame.Vector2(1.0, 0.0).rotate(random.uniform(0.0, 360.0))
    oyuncu_olum_patlama_yonu = direction.normalize()
    oyuncu_olum_katil_uid = ""
    oyuncu_olum_katil_tur = ""
    oyuncu_olum_katil_kan_sonraki_ms = 0




    already_routed = str(kaynak_adi or "").lower() in {
        "fire_magic_explosion_core",
        "fire_magic_explosion_inner",
    }
    if not v73_player_blast_fragmented and not already_routed:
        v73_blast_gore_burst(
            oyuncu_x,
            oyuncu_y - 8.0,
            kaynak_x,
            kaynak_y,
            tier=tier,
        )
        v73_player_blast_fragmented = True
        v73_stats["blast_deaths"] += 1
    elif already_routed:
        v73_player_blast_fragmented = True
        v73_stats["blast_deaths"] += 1
    return result
# </POTBO_STAGE S1478>

# <POTBO_STAGE S1480>


def v73_diagnostics():
    return {
        "version": V73_VERSION,
        "air_scalars": {
            "normal": V73_NORMAL_AIR_COUNT,
            "arterial": V73_ARTERIAL_AIR_COUNT,
            "death_artery": V73_DEATH_ARTERY_AIR_COUNT,
            "blast": V73_BLAST_AIR_COUNT,
        },
        "decal_budget": int(V40_BLOOD_GLOBAL_MAX),
        "visible_decal_budget": int(V40_BLOOD_VISIBLE_MAX),
        "stats": dict(v73_stats),
    }
# </POTBO_STAGE S1480>

# <POTBO_STAGE S1482>


















V74_VERSION = "74.0"



V74_COLLISION_BACKTRACE_PX = 180.0
# </POTBO_STAGE S1482>

# <POTBO_STAGE S1486>


def v74_create_persistent_decal(x, y, scale=None, rotation=None):
    """Tek bir kalıcı kan izi yaratır; merge, relocation ve lifetime yoktur."""
    if not v74_floor_clean(x, y):
        return None
    incoming = float(scale if scale is not None else random.uniform(0.28, 0.86))
    incoming = max(0.055, incoming)
    decal = PersistentBloodDecal(
        float(x),
        float(y),
        scale=incoming,
        rotation=rotation,
    )



    decal.v74_permanent = True
    decal.v74_fixed_geometry = (
        float(decal.x),
        float(decal.y),
        float(decal.scale),
        float(decal.rotation),
        int(decal.sprite_index),
    )
    if callable(globals().get("_v42_blood_render_key")):
        _v42_blood_render_key(decal)
    blood_decals.append(decal)
    cell = _v40_blood_cell(decal.x, decal.y)
    v40_blood_grid.setdefault(cell, []).append(decal)
    return decal



def _v74_decal_never_expired(self, simdi):
    return False


PersistentBloodDecal.expired = _v74_decal_never_expired





def kan_lekesi_ekle(x, y, scale=None):
    global v74_current_particle
    p = v74_current_particle
    primary = False
    safe = None

    if p is not None:
        try:
            primary = (
                abs(float(x) - float(p.x)) <= 0.05
                and abs(float(y) - float(p.y)) <= 0.05
            )
        except Exception:
            primary = False

    if primary:
        pid = id(p)
        last_clean = v74_particle_last_clean.get(pid)
        direction = getattr(p, "v", (0.0, 0.0))
        safe = v74_trace_clean_floor(x, y, direction=direction, last_clean=last_clean)
    elif v74_floor_clean(x, y):
        safe = pygame.Vector2(float(x), float(y))

    if safe is None:
        return None

    decal = v74_create_persistent_decal(safe.x, safe.y, scale=scale)
    if decal is not None and primary:
        v74_particle_primary_committed.add(id(p))
        v74_stats["particle_landings"] += 1
    return decal
# </POTBO_STAGE S1486>

# <POTBO_STAGE S1489>


def _v74_particle_update(self, dt):
    global v74_current_particle
    if not getattr(self, "active", False):
        return _v74_particle_update_original(self, dt)

    pid = id(self)
    if v74_floor_clean(getattr(self, "x", 0.0), getattr(self, "y", 0.0)):
        v74_particle_last_clean[pid] = (
            float(self.x),
            float(self.y),
        )

    pre_z = float(getattr(self, "z", 0.0))
    previous_current = v74_current_particle
    v74_current_particle = self
    try:
        result = _v74_particle_update_original(self, dt)
    finally:
        v74_current_particle = previous_current

    if getattr(self, "active", False):
        if v74_floor_clean(getattr(self, "x", 0.0), getattr(self, "y", 0.0)):
            v74_particle_last_clean[pid] = (
                float(self.x),
                float(self.y),
            )
        return result


    if pid not in v74_particle_primary_committed:
        safe = v74_trace_clean_floor(
            getattr(self, "x", 0.0),
            getattr(self, "y", 0.0),
            direction=getattr(self, "v", (0.0, 0.0)),
            last_clean=v74_particle_last_clean.get(pid),
        )
        if safe is not None:
            scale = max(
                0.055,
                float(getattr(self, "scale", 0.65))
                * (0.24 if getattr(self, "micro", False) else 0.58),
            )
            if v74_create_persistent_decal(safe.x, safe.y, scale) is not None:
                v74_stats["particle_landings"] += 1
                if float(getattr(self, "z", 0.0)) > 0.01 or pre_z > 1.5:
                    v74_stats["forced_air_expiry_landings"] += 1

    v74_particle_primary_committed.discard(pid)
    v74_particle_last_clean.pop(pid, None)
    return result
# </POTBO_STAGE S1489>

# <POTBO_STAGE S1491>


def _v74_mist_update(self, dt, now):
    was_alive = bool(self.alive)
    pre_pos = pygame.Vector2(self.pos)
    result = _v74_mist_update_original(self, dt, now)
    if was_alive and not self.alive:
        safe = v74_trace_clean_floor(
            self.pos.x,
            self.pos.y,
            direction=getattr(self, "vel", (0.0, 0.0)),
            last_clean=pre_pos if v74_floor_clean(pre_pos.x, pre_pos.y) else None,
        )
        if safe is not None:
            scale = max(
                0.055,
                min(
                    0.20,
                    float(self.radius) * random.uniform(0.070, 0.115),
                ),
            )
            if v74_create_persistent_decal(safe.x, safe.y, scale) is not None:
                v74_stats["mist_landings"] += 1
    return result


def _v74_filament_update(self, dt, now):
    was_alive = bool(self.alive)
    pre_head = pygame.Vector2(self.head)
    pre_tail = pygame.Vector2(self.tail)
    result = _v74_filament_update_original(self, dt, now)
    if was_alive and not self.alive:

        safe = v74_trace_clean_floor(
            self.head.x,
            self.head.y,
            direction=getattr(self, "vel", (0.0, 0.0)),
            last_clean=pre_head if v74_floor_clean(pre_head.x, pre_head.y) else None,
        )
        if safe is not None:
            scale = max(
                0.07,
                min(
                    0.34,
                    float(self.width) * random.uniform(0.11, 0.18),
                ),
            )
            if v74_create_persistent_decal(safe.x, safe.y, scale) is not None:
                v74_stats["filament_landings"] += 1
        if pre_head.distance_to(pre_tail) >= 8.0:
            tail_safe = v74_trace_clean_floor(
                self.tail.x,
                self.tail.y,
                direction=getattr(self, "tail_vel", (0.0, 0.0)),
                last_clean=pre_tail
                if v74_floor_clean(pre_tail.x, pre_tail.y)
                else None,
            )
            if tail_safe is not None:
                v74_create_persistent_decal(
                    tail_safe.x,
                    tail_safe.y,
                    max(
                        0.055,
                        min(
                            0.20,
                            float(self.width) * random.uniform(0.070, 0.11),
                        ),
                    ),
                )
    return result


def _v74_lobe_update(self, dt, now):
    was_alive = bool(self.alive)
    result = _v74_lobe_update_original(self, dt, now)
    if was_alive and not self.alive and v74_floor_clean(self.origin.x, self.origin.y):
        scale = max(
            0.10,
            min(
                0.48,
                float(self.radius) * random.uniform(0.030, 0.052),
            ),
        )
        if v74_create_persistent_decal(self.origin.x, self.origin.y, scale) is not None:
            v74_stats["lobe_landings"] += 1
    return result
# </POTBO_STAGE S1491>

# <POTBO_STAGE S1493>





def kan_lekelerini_ciz(silhouette=False):
    margin = V74_DEATH_DRAW_MARGIN / max(0.01, float(KAMERA_YAKINLASTIRMA))
    left = float(kamera_x) - margin
    top = float(kamera_y) - margin
    right = float(kamera_x) + GENISLIK / max(0.01, float(KAMERA_YAKINLASTIRMA)) + margin
    bottom = (
        float(kamera_y) + YUKSEKLIK / max(0.01, float(KAMERA_YAKINLASTIRMA)) + margin
    )
    cx0 = int(math.floor(left / V40_BLOOD_GRID_CELL))
    cx1 = int(math.floor(right / V40_BLOOD_GRID_CELL))
    cy0 = int(math.floor(top / V40_BLOOD_GRID_CELL))
    cy1 = int(math.floor(bottom / V40_BLOOD_GRID_CELL))

    visible = []
    seen = set()
    for cy in range(cy0, cy1 + 1):
        for cx in range(cx0, cx1 + 1):
            for decal in v40_blood_grid.get((cx, cy), ()):
                did = id(decal)
                if did in seen:
                    continue
                seen.add(did)
                if left <= float(decal.x) <= right and top <= float(decal.y) <= bottom:
                    visible.append(decal)



    visible.sort(
        key=lambda d: (
            int(getattr(d, "created_ms", 0)),
            _v42_blood_render_key(d),
        )
    )
    for decal in visible:
        decal.ciz(silhouette=silhouette)



    v58_draw(ekran, silhouette=silhouette)




_v74_camera_original = kamerayi_guncelle
# </POTBO_STAGE S1493>

# <POTBO_STAGE S1497>


def v74_diagnostics():
    return {
        "version": V74_VERSION,
        "persistent_decals": len(blood_decals),
        "collision_backtrace_px": V74_COLLISION_BACKTRACE_PX,
        "death_camera_frozen": v74_death_camera_anchor is not None,
        "stats": dict(v74_stats),
    }
# </POTBO_STAGE S1497>

# <POTBO_STAGE S1499>


























V75_VERSION = "75.0"

V75_BLOOD_FULL_DRY_MS = 20 * 60 * 1000
V75_BLOOD_POST_DRY_COLOR_MS = 16 * 60 * 1000
# </POTBO_STAGE S1499>

# <POTBO_STAGE S1501>



V75_RAT_BLOOD_GROUP_RADIUS = 34.0
V75_RAT_BLOOD_BITE_MIN = 0.00120
V75_RAT_BLOOD_BITE_MAX = 0.00155
V75_RAT_BLOOD_FEED_MIN_MS = 390
V75_RAT_BLOOD_FEED_MAX_MS = 520
V75_RAT_DRY_BLOOD_RATE = 0.64
# </POTBO_STAGE S1501>

# <POTBO_STAGE S1503>


V75_RAT_GORE_BITE_MIN = 0.0024
V75_RAT_GORE_BITE_MAX = 0.0036
V75_RAT_GORE_FEED_MIN_MS = 420
V75_RAT_GORE_FEED_MAX_MS = 560
# </POTBO_STAGE S1503>

# <POTBO_STAGE S1505>
v75_stats = {
    "blood_consumed": 0,
    "gore_consumed": 0,
    "maggots_eaten": 0,
    "maggot_spreads": 0,
    "maggot_blood_consumed": 0.0,
    "rat_blood_consumed": 0.0,
}


BLOOD_MAGGOT_MAX = V75_MAGGOT_MAX
BLOOD_MAGGOT_FIRST_MIN_MS = V75_MAGGOT_FIRST_MIN_MS
BLOOD_MAGGOT_FIRST_MAX_MS = V75_MAGGOT_FIRST_MAX_MS
BLOOD_MAGGOT_WAVE_MIN_MS = V75_MAGGOT_WAVE_MIN_MS
BLOOD_MAGGOT_WAVE_MAX_MS = V75_MAGGOT_WAVE_MAX_MS


def v75_blood_mass(decal):
    """Görsel geometriden bağımsız, ekosistemin tükettiği kan kütlesi."""
    mass = getattr(decal, "v75_ecology_mass", None)
    if mass is not None:
        return max(0.0, float(mass))
    scale = max(0.055, float(getattr(decal, "scale", 0.55)))
    stain = max(
        0.55,
        min(2.25, float(getattr(decal, "v42_stain_mass", 1.0))),
    )

    mass = (0.28 + scale * 0.52) * (0.72 + stain * 0.28)
    decal.v75_ecology_mass = float(mass)
    decal.v75_ecology_mass_initial = float(mass)
    decal.v75_ecology_consumed = False
    return float(mass)


def v75_set_blood_mass(decal, mass):
    mass = max(0.0, float(mass))
    decal.v75_ecology_mass = mass
    if not hasattr(decal, "v75_ecology_mass_initial"):
        decal.v75_ecology_mass_initial = max(mass, 0.001)
    if mass <= 0.0005:
        decal.v75_ecology_mass = 0.0
        decal.v75_ecology_consumed = True
    return decal.v75_ecology_mass


def v75_blood_is_dry(decal, now=None):
    if now is None:
        now = pygame.time.get_ticks()
    created = int(getattr(decal, "created_ms", now))
    return int(now) >= created + V75_BLOOD_FULL_DRY_MS



_v75_decal_init_original = PersistentBloodDecal.__init__


def _v75_decal_init(self, *args, **kwargs):
    _v75_decal_init_original(self, *args, **kwargs)
    created = int(getattr(self, "created_ms", pygame.time.get_ticks()))
    self.dry_after_ms = created + V75_BLOOD_FULL_DRY_MS


    self.fade_after_ms = self.dry_after_ms + V75_BLOOD_POST_DRY_COLOR_MS
    self.vanish_after_ms = 2**62
    self.maggot_next_ms = created + random.randint(
        V75_MAGGOT_FIRST_MIN_MS, V75_MAGGOT_FIRST_MAX_MS
    )
    self.maggot_waves = 0
    v75_blood_mass(self)


PersistentBloodDecal.__init__ = _v75_decal_init



def _v75_decal_never_expired(self, simdi):
    return False


PersistentBloodDecal.expired = _v75_decal_never_expired
# </POTBO_STAGE S1505>

# <POTBO_STAGE S1507>


def _v75_maggot_init(self, decal, simdi):
    _v75_maggot_init_original(self, decal, simdi)
    self.life_until = int(simdi) + random.randint(
        V75_MAGGOT_LIFE_MIN_MS, V75_MAGGOT_LIFE_MAX_MS
    )
    self.v75_feed_next_ms = int(simdi) + random.randint(700, 1500)
    self.v75_spread_next_ms = int(simdi) + random.randint(
        V75_MAGGOT_SPREAD_MIN_MS, V75_MAGGOT_SPREAD_MAX_MS
    )
    self.v75_spread_count = 0
# </POTBO_STAGE S1507>

# <POTBO_STAGE S1509>


def _v75_maggot_update(self, dt, simdi):
    source = getattr(self, "source_decal", None)
    if (
        source is None
        or source not in blood_decals
        or getattr(source, "v75_ecology_consumed", False)
    ):
        self.active = False
        return

    _v75_maggot_update_original(self, dt, simdi)
    if not self.active:
        return



    if oyuncu_hp <= 0:
        return



    if int(simdi) >= int(getattr(self, "v75_feed_next_ms", 0)):
        self.v75_feed_next_ms = int(simdi) + V75_MAGGOT_FEED_INTERVAL_MS
        mass = v75_blood_mass(source)
        if mass > 0.0:
            consumed = min(mass, random.uniform(0.00042, 0.00068))
            v75_set_blood_mass(source, mass - consumed)
            v75_stats["maggot_blood_consumed"] += consumed



    if int(simdi) >= int(getattr(self, "v75_spread_next_ms", 0)):
        self.v75_spread_next_ms = int(simdi) + random.randint(
            V75_MAGGOT_SPREAD_MIN_MS, V75_MAGGOT_SPREAD_MAX_MS
        )
        mass = v75_blood_mass(source)
        if mass > 0.10 and not v75_blood_is_dry(source, simdi):
            p = v75_maggot_spread_point(self)
            if p is not None:
                moved = min(
                    mass * random.uniform(0.018, 0.035),
                    random.uniform(0.012, 0.026),
                )
                if moved >= 0.006:

                    deposited = moved * 0.72
                    v75_set_blood_mass(source, mass - moved)
                    satellite = v74_create_persistent_decal(
                        p.x,
                        p.y,
                        scale=random.uniform(0.060, 0.115),
                        rotation=random.uniform(0.0, 360.0),
                    )
                    if satellite is not None:
                        satellite.v75_ecology_mass = deposited
                        satellite.v75_ecology_mass_initial = deposited
                        satellite.v75_ecology_consumed = False
                        satellite.v75_spread_origin = id(source)
                        self.v75_spread_count += 1
                        v75_stats["maggot_spreads"] += 1
                    else:

                        v75_set_blood_mass(
                            source,
                            v75_blood_mass(source) + moved,
                        )
# </POTBO_STAGE S1509>

# <POTBO_STAGE S1512>


def v75_rat_blood_group(center, radius=V75_RAT_BLOOD_GROUP_RADIUS):
    center = pygame.Vector2(center)
    out = []
    r2 = float(radius) ** 2
    for decal in _v40_blood_nearby(center, radius):
        if decal not in blood_decals or getattr(decal, "v75_ecology_consumed", False):
            continue
        dx = float(decal.x) - center.x
        dy = float(decal.y) - center.y
        if dx * dx + dy * dy <= r2 and v75_blood_mass(decal) > 0.0:
            out.append((dx * dx + dy * dy, decal))
    out.sort(key=lambda item: item[0])
    return [d for _, d in out]


def v75_consume_blood_group(rat, target, simdi):
    group = v75_rat_blood_group((target.x, target.y))
    if not group:
        return 0.0

    feeders = v75_local_feeding_rats(rat, "blood")
    crowd = 1.0 + V75_RAT_CROWD_DAMPING * max(0, feeders - 1)
    amount = random.uniform(V75_RAT_BLOOD_BITE_MIN, V75_RAT_BLOOD_BITE_MAX) / crowd


    if v75_blood_is_dry(target, simdi):
        amount *= V75_RAT_DRY_BLOOD_RATE

    remaining = amount
    consumed_total = 0.0

    for decal in group:
        if remaining <= 1e-9:
            break
        mass = v75_blood_mass(decal)
        take = min(mass, remaining)
        v75_set_blood_mass(decal, mass - take)
        consumed_total += take
        remaining -= take

    v75_stats["rat_blood_consumed"] += consumed_total
    return consumed_total


def v75_gore_mass(gore):
    mass = getattr(gore, "v75_ecology_mass", None)
    if mass is not None:
        return max(0.0, float(mass))
    kind = str(getattr(gore, "kind", ""))
    size_bonus = {
        "intestine": 1.25,
        "liver": 1.10,
        "organ_mass_a": 1.42,
        "organ_mass_b": 1.38,
        "organ_round_a": 0.82,
        "organ_round_b": 0.82,
        "flesh_shard_a": 0.62,
        "flesh_shard_b": 0.62,
    }.get(kind, 0.75)
    mass = max(
        0.35,
        size_bonus * (0.78 + max(0.08, float(getattr(gore, "scale", 0.4))) * 0.62),
    )
    gore.v75_ecology_mass = mass
    gore.v75_ecology_mass_initial = mass
    gore.v75_ecology_scale_initial = float(getattr(gore, "scale", 0.4))
    return mass


def _v75_rat_consume_tick(self, simdi):
    if not self._food_valid():
        return

    kind = self.food_kind
    obj = self.food_obj


    if kind == "maggot":
        if simdi < self.feed_tick_ms:
            return
        self.feed_tick_ms = int(simdi) + random.randint(520, 760)
        obj.active = False
        self.hunger = max(0.0, self.hunger - 0.30)
        self.feed_until = int(simdi) + 560
        self.food_obj = None
        self.food_kind = None
        v75_stats["maggots_eaten"] += 1
        return

    if kind == "gore":
        if simdi < self.feed_tick_ms:
            return
        self.feed_tick_ms = int(simdi) + random.randint(
            V75_RAT_GORE_FEED_MIN_MS, V75_RAT_GORE_FEED_MAX_MS
        )
        mass = v75_gore_mass(obj)
        feeders = v75_local_feeding_rats(self, "gore", radius=42.0)
        crowd = 1.0 + 0.58 * max(0, feeders - 1)
        take = min(
            mass,
            random.uniform(V75_RAT_GORE_BITE_MIN, V75_RAT_GORE_BITE_MAX) / crowd,
        )
        mass = max(0.0, mass - take)
        obj.v75_ecology_mass = mass
        self.hunger = max(0.0, self.hunger - 0.008)
        self.feed_until = int(simdi) + 300



        initial_mass = max(
            0.001,
            float(getattr(obj, "v75_ecology_mass_initial", mass + take)),
        )
        initial_scale = max(
            0.04,
            float(
                getattr(
                    obj,
                    "v75_ecology_scale_initial",
                    getattr(obj, "scale", 0.4),
                )
            ),
        )
        ratio = max(0.0, min(1.0, mass / initial_mass))
        obj.scale = max(
            0.045,
            initial_scale * (0.30 + 0.70 * math.sqrt(ratio)),
        )
        if mass <= 0.008:
            obj.v40_consumed = True
            self.food_obj = None
            self.food_kind = None
            v75_stats["gore_consumed"] += 1
        return

    if kind == "blood":
        if simdi < self.feed_tick_ms:
            return
        self.feed_tick_ms = int(simdi) + random.randint(
            V75_RAT_BLOOD_FEED_MIN_MS, V75_RAT_BLOOD_FEED_MAX_MS
        )
        consumed = v75_consume_blood_group(self, obj, simdi)
        self.hunger = max(0.0, self.hunger - 0.0035)
        self.feed_until = int(simdi) + 270
        if consumed <= 0.0 or getattr(obj, "v75_ecology_consumed", False):
            self.food_obj = None
            self.food_kind = None
        return
# </POTBO_STAGE S1512>

# <POTBO_STAGE S1514>




_v75_rat_find_food_original = AmbientRat._find_food


def _v75_rat_find_food(self, here, simdi):
    _v75_rat_find_food_original(self, here, simdi)
    if self.food_kind == "blood" and self.food_obj is not None:
        if (
            getattr(self.food_obj, "v75_ecology_consumed", False)
            or v75_blood_mass(self.food_obj) <= 0.0
        ):
            self.food_obj = None
            self.food_kind = None
# </POTBO_STAGE S1514>

# <POTBO_STAGE S1516>





def v75_cleanup_consumed_blood(simdi):
    global v75_cleanup_next_ms
    if int(simdi) < int(v75_cleanup_next_ms):
        return 0
    v75_cleanup_next_ms = int(simdi) + V75_ECOLOGY_CLEANUP_INTERVAL_MS
    if not blood_decals:
        return 0

    removed_ids = {
        id(d)
        for d in blood_decals
        if getattr(d, "v75_ecology_consumed", False) or v75_blood_mass(d) <= 0.0005
    }
    if not removed_ids:
        return 0

    before = len(blood_decals)
    blood_decals[:] = [d for d in blood_decals if id(d) not in removed_ids]
    removed = before - len(blood_decals)
    if removed:
        v75_stats["blood_consumed"] += removed
        for maggot in blood_maggots:
            source = getattr(maggot, "source_decal", None)
            if source is not None and id(source) in removed_ids:
                maggot.active = False
        _v40_blood_grid_rebuild()
    return removed


_v75_kan_gore_update_original = kan_gore_guncelle


def kan_gore_guncelle():
    result = _v75_kan_gore_update_original()


    if oyuncu_hp > 0:
        v75_cleanup_consumed_blood(pygame.time.get_ticks())
    return result


def v75_ecology_diagnostics():
    now = pygame.time.get_ticks()
    wet = 0
    dry = 0
    ecological_mass = 0.0
    for decal in blood_decals:
        ecological_mass += v75_blood_mass(decal)
        if v75_blood_is_dry(decal, now):
            dry += 1
        else:
            wet += 1
    return {
        "version": V75_VERSION,
        "dry_time_ms": V75_BLOOD_FULL_DRY_MS,
        "blood_decals": len(blood_decals),
        "wet_decals": wet,
        "dry_decals": dry,
        "blood_ecology_mass": round(ecological_mass, 4),
        "active_maggots": sum(1 for m in blood_maggots if getattr(m, "active", False)),
        "active_rats": sum(1 for r in ambient_rats if getattr(r, "active", False)),
        "stats": dict(v75_stats),
    }
# </POTBO_STAGE S1516>

# <POTBO_STAGE S1518>
















V76_VERSION = "76.0"




V76_BLOOD_WORM_PRIMARY = os.path.join(ASSETS, "ambient", "blood_worms.png")
if V76_BLOOD_WORM_PRIMARY in BLOOD_WORM_SHEET_ADAYLARI:
    BLOOD_WORM_SHEET_ADAYLARI.remove(V76_BLOOD_WORM_PRIMARY)
BLOOD_WORM_SHEET_ADAYLARI.insert(0, V76_BLOOD_WORM_PRIMARY)


if os.path.isfile(V76_BLOOD_WORM_PRIMARY):
    _v76_worm_frames = _v28_blood_worm_spriteleri_yukle()
    if _v76_worm_frames:
        BLOOD_WORM_SPRITELERI = _v76_worm_frames
# </POTBO_STAGE S1518>

# <POTBO_STAGE S1525>


def _v76_death_blood_draw():
    kan_lekelerini_ciz(silhouette=True)
    for particle in blood_particles:
        particle.ciz(silhouette=True)


def _v76_death_gore_draw():
    for chunk in sorted(gore_chunks, key=lambda g: g.y):
        chunk.ciz(silhouette=True)
# </POTBO_STAGE S1525>

# <POTBO_STAGE S1527>


def _v76_killer_draw(actor):
    if actor is None:
        return
    sil, rect = _v24_katil_siluet_surface_ve_rect(actor)
    if sil is not None and rect is not None:
        mask = pygame.mask.from_surface(sil, 1)
        flat = mask.to_surface(
            setcolor=(*V76_DEATH_BODY, 255),
            unsetcolor=(0, 0, 0, 0),
        ).convert_alpha()
        ekran.blit(flat, rect)


    if oyuncu_olum_turu == "fire":
        return
    point = _v24_katil_silah_kan_noktasi(actor)
    if point is None:
        return
    sx = float(dunya_ekran_x(point.x))
    sy = float(dunya_ekran_y(point.y))
    pygame.draw.line(
        ekran,
        V76_DEATH_BLOOD,
        (int(round(sx)), int(round(sy - 2))),
        (int(round(sx)), int(round(sy + 5))),
        max(1, int(round(2 * KAMERA_YAKINLASTIRMA))),
    )
    period = 820.0
    now = pygame.time.get_ticks()
    for i, phase in enumerate((0.0, 0.34, 0.68)):
        p = ((now / period) + phase) % 1.0
        ease = p * p
        y = sy + 5.0 + ease * 24.0
        x = sx + math.sin((p + i) * math.tau) * 1.3
        radius = 2 if p < 0.55 else 1
        pygame.draw.circle(
            ekran,
            V76_DEATH_BLOOD,
            (int(round(x)), int(round(y))),
            radius,
        )
# </POTBO_STAGE S1527>

# <POTBO_STAGE S1529>


def oyuncu_olum_sahnesi_ciz():
    ekran.fill(V76_DEATH_BLACK)
    killer = _v24_olum_katil_actor_bul()
    killer_behind = killer is not None and float(
        getattr(killer, "y", oyuncu_y)
    ) <= float(oyuncu_y)

    if killer_behind:
        _v76_killer_draw(killer)


    _v76_flat_layer(_v76_death_blood_draw, V76_DEATH_BLOOD)

    _v76_flat_layer(_v76_death_gore_draw, V76_DEATH_BODY)
    _v76_flat_layer(
        _v76_death_victim_draw,
        V76_DEATH_BODY,
        remove_black=True,
    )

    if killer is not None and not killer_behind:
        _v76_killer_draw(killer)


    if oyuncu_olum_cikis_orani(pygame.time.get_ticks()) > 0.0:
        ekran.fill(V76_DEATH_BLACK)
        return
    _v76_death_menu_draw()
# </POTBO_STAGE S1529>

# <POTBO_STAGE S1534>


def v76_diagnostics():
    return {
        "version": V76_VERSION,
        "worm_primary": V76_BLOOD_WORM_PRIMARY,
        "worm_frames": len(BLOOD_WORM_SPRITELERI),
        "combo_ui": False,
        "special_hit_counter": False,
        "combat_rhythm_hud": False,
        "death_palette": (
            V76_DEATH_BLACK,
            V76_DEATH_BLOOD,
            V76_DEATH_BODY,
        ),
    }
# </POTBO_STAGE S1534>

# <POTBO_STAGE S1536>
















V77_VERSION = "77.0"
# </POTBO_STAGE S1536>

# <POTBO_STAGE S1542>





def duraklatma_menusu_ciz():
    oyun_ekrani_ciz()
    koyu_kaplama(185)

    panel = pygame.Rect(GENISLIK // 2 - 330, 110, 660, 420)
    gotik_panel(panel, PARLAK_KIRMIZI, 245)

    yazi_yaz(
        t("pause_title"),
        panel.centerx,
        panel.y + 54,
        PARLAK_KIRMIZI,
        menu_baslik_font,
        True,
    )
    pygame.draw.line(
        ekran,
        KAN_KIRMIZISI,
        (panel.x + 62, panel.y + 96),
        (panel.right - 62, panel.y + 96),
        1,
    )

    for index, secenek in enumerate(duraklatma_secenekleri()):
        rect = pygame.Rect(
            panel.centerx - 170,
            panel.y + 126 + index * 62,
            340,
            36,
        )
        secili = index == duraklatma_index
        menu_susleme_ciz(rect, secili)
        yazi_yaz(
            secenek,
            rect.centerx,
            rect.centery,
            BEYAZ if secili else (155, 145, 150),
            menu_font if secili else normal_font,
            True,
        )
# </POTBO_STAGE S1542>

# <POTBO_STAGE S1544>


def _v77_death_blood_layer():
    kan_lekelerini_ciz(silhouette=True)
    for particle in blood_particles:
        if getattr(particle, "active", True):
            particle.ciz(silhouette=True)


def _v77_death_gore_layer():
    for chunk in sorted(gore_chunks, key=lambda g: g.y):
        chunk.ciz(silhouette=True)
# </POTBO_STAGE S1544>

# <POTBO_STAGE S1546>


def _v77_death_killer_draw(actor):
    if actor is None:
        return
    sil, rect = _v24_katil_siluet_surface_ve_rect(actor)
    if sil is not None and rect is not None:
        mask = pygame.mask.from_surface(sil, 1)
        flat = mask.to_surface(
            setcolor=(*V77_DEATH_BODY, 255),
            unsetcolor=(0, 0, 0, 0),
        ).convert_alpha()
        ekran.blit(flat, rect)


    if oyuncu_olum_turu == "fire":
        return
    point = _v24_katil_silah_kan_noktasi(actor)
    if point is None:
        return
    sx = float(dunya_ekran_x(point.x))
    sy = float(dunya_ekran_y(point.y))
    pygame.draw.line(
        ekran,
        V77_DEATH_BLOOD,
        (int(round(sx)), int(round(sy - 2))),
        (int(round(sx)), int(round(sy + 5))),
        max(1, int(round(2 * KAMERA_YAKINLASTIRMA))),
    )
    period = 820.0
    now = pygame.time.get_ticks()
    for i, phase in enumerate((0.0, 0.34, 0.68)):
        p = ((now / period) + phase) % 1.0
        y = sy + 5.0 + p * p * 24.0
        x = sx + math.sin((p + i) * math.tau) * 1.3
        pygame.draw.circle(
            ekran,
            V77_DEATH_BLOOD,
            (int(round(x)), int(round(y))),
            2 if p < 0.55 else 1,
        )
# </POTBO_STAGE S1546>

# <POTBO_STAGE S1549>


def oyuncu_olum_sahnesi_ciz():
    ekran.fill(V77_DEATH_BLACK)


    _v77_semantic_layer(_v77_death_blood_layer, V77_DEATH_BLOOD, 0.60)
    _v77_semantic_layer(_v77_death_gore_layer, V77_DEATH_BODY, 0.30)

    killer = _v24_olum_katil_actor_bul()
    killer_behind = killer is not None and float(
        getattr(killer, "y", oyuncu_y)
    ) <= float(oyuncu_y)
    if killer_behind:
        _v77_death_killer_draw(killer)

    victim_ok = _v77_semantic_layer(_v77_death_victim_layer, V77_DEATH_BODY, 0.30)
    if not victim_ok:
        _v77_death_fallback_victim()


    _v77_semantic_layer(_v77_death_fire_layer, V77_DEATH_BODY, 0.25)

    if killer is not None and not killer_behind:
        _v77_death_killer_draw(killer)

    if oyuncu_olum_baslangic_ms <= 0:
        return

    now = pygame.time.get_ticks()
    title_p = oyuncu_olum_baslik_fade_orani(now)
    _v34_gameover_music_tick(title_p, now)


    if oyuncu_olum_cikis_orani(now) > 0.0:
        ekran.fill(V77_DEATH_BLACK)
        return

    _v77_death_menu_draw(now)
# </POTBO_STAGE S1549>

# <POTBO_STAGE S1559>








def one_cikan_item_paneli_ciz():
    panel = hud_sag_rect()
    gotik_panel(panel, KAN_KIRMIZISI, 238)

    slot_boyut = 68
    bosluk = 12
    grup_w = slot_boyut * 5 + bosluk * 4
    q_boyut = slot_boyut
    ayirici_bosluk = 30
    toplam = grup_w + ayirici_bosluk + q_boyut
    baslangic_x = panel.centerx - toplam // 2
    y = panel.y + 41

    for i in range(5):
        rect = pygame.Rect(
            baslangic_x + i * (slot_boyut + bosluk),
            y,
            slot_boyut,
            slot_boyut,
        )
        slot_ciz(
            rect,
            secili=(i == envanter_secili_slot),
            numara=i + 1,
            item_index=one_cikan_slotlar[i],
        )

    ayir_x = baslangic_x + grup_w + ayirici_bosluk // 2
    pygame.draw.line(
        ekran,
        (94, 76, 84),
        (ayir_x, y - 4),
        (ayir_x, y + slot_boyut + 4),
        1,
    )

    q_hizli_slot_normalize_et()
    qx = baslangic_x + grup_w + ayirici_bosluk
    q_rect = pygame.Rect(qx, y, q_boyut, q_boyut)
    q_item = q_hizli_item_index
    q_debug_spell = bool(gelistirici_sonsuz_ates)
    q_is_magic = q_debug_spell or (
        isinstance(q_item, int)
        and 0 <= q_item < len(envanter_itemleri)
        and item_buyu_mu(envanter_itemleri[q_item])
    )
    _v78_slot_surface(
        q_rect,
        (210, 94, 30) if q_is_magic else PARLAK_KIRMIZI,
        False,
        False,
        q_is_magic,
    )
    yazi_yaz(
        "Q",
        q_rect.x + 11,
        q_rect.y + 10,
        (255, 177, 70) if q_is_magic else SARI,
        mini_font,
        True,
    )
    if q_debug_spell:
        item_ikonu_ciz("fire_magic", q_rect.inflate(-12, -12), False)
        spell_okulu_sembol_ciz(
            "IGNIS",
            pygame.Rect(q_rect.right - 23, q_rect.bottom - 23, 19, 19),
        )
        yazi_yaz(
            "∞",
            q_rect.centerx,
            q_rect.y + 12,
            (255, 238, 178),
            mini_font,
            True,
        )
    elif isinstance(q_item, int) and 0 <= q_item < len(envanter_itemleri):
        item = envanter_itemleri[q_item]
        if isinstance(item, dict):
            item_ikonu_ciz(item.get("id"), q_rect.inflate(-12, -12), False)
            if item.get("spell_school"):
                spell_okulu_sembol_ciz(
                    item.get("spell_school"),
                    pygame.Rect(
                        q_rect.right - 23,
                        q_rect.bottom - 23,
                        19,
                        19,
                    ),
                )

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
# </POTBO_STAGE S1559>

# <POTBO_STAGE S1561>


def duraklatma_menusu_ciz():
    oyun_ekrani_ciz()
    koyu_kaplama(185)
    panel = pygame.Rect(GENISLIK // 2 - 300, 148, 600, 412)
    gotik_panel(panel, PARLAK_KIRMIZI, 245)
    yazi_yaz(
        t("pause_title"),
        panel.centerx,
        panel.y + 58,
        PARLAK_KIRMIZI,
        menu_baslik_font,
        True,
    )
    pygame.draw.line(
        ekran,
        KAN_KIRMIZISI,
        (panel.x + 58, panel.y + 96),
        (panel.right - 58, panel.y + 96),
        1,
    )
    for index, secenek in enumerate(duraklatma_secenekleri()):
        rect = pygame.Rect(
            panel.centerx - 170,
            panel.y + 126 + index * 62,
            340,
            36,
        )
        secili = index == duraklatma_index
        menu_susleme_ciz(rect, secili)
        yazi_yaz(
            secenek,
            rect.centerx,
            rect.centery,
            BEYAZ if secili else (155, 145, 150),
            menu_font if secili else normal_font,
            True,
        )
# </POTBO_STAGE S1561>

# <POTBO_STAGE S1567>





v78_death_snapshot = {
    "start_ms": 0,
    "blood": [],
    "gore": [],
}


def _v78_capture_death_snapshot():
    global v78_death_snapshot
    now = pygame.time.get_ticks()
    blood = []
    center = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))

    for decal in list(blood_decals):
        try:
            pos = pygame.Vector2(
                float(getattr(decal, "x", oyuncu_x)),
                float(getattr(decal, "y", oyuncu_y)),
            )
        except Exception:
            continue
        d = pos - center
        if d.length() > 128.0:
            d.scale_to_length(128.0)
            pos = center + d
        radius = float(
            getattr(
                decal,
                "radius",
                getattr(decal, "r", getattr(decal, "size", 5.0)),
            )
        )
        blood.append(
            {
                "x": pos.x,
                "y": pos.y,
                "r": max(2.0, min(18.0, radius)),
                "kind": "pool",
            }
        )

    for particle in list(blood_particles):
        if not getattr(particle, "active", True):
            continue
        try:
            pos = pygame.Vector2(
                float(getattr(particle, "x", oyuncu_x)),
                float(getattr(particle, "y", oyuncu_y)),
            )
        except Exception:
            continue
        d = pos - center
        if d.length() > 110.0:
            d.scale_to_length(110.0)
            pos = center + d
        radius = float(
            getattr(
                particle,
                "radius",
                getattr(
                    particle,
                    "r",
                    getattr(particle, "size", 2.0),
                ),
            )
        )
        blood.append(
            {
                "x": pos.x,
                "y": pos.y,
                "r": max(1.0, min(7.0, radius)),
                "kind": "drop",
            }
        )

    blood.sort(key=lambda e: (pygame.Vector2(e["x"], e["y"]) - center).length())
    blood = blood[:220]

    gore = []
    for chunk in list(gore_chunks):
        try:
            pos = pygame.Vector2(
                float(getattr(chunk, "x", oyuncu_x)),
                float(getattr(chunk, "y", oyuncu_y)),
            )
        except Exception:
            continue
        d = pos - center
        if d.length() > 86.0:
            d.scale_to_length(86.0)
            pos = center + d
        w = float(
            getattr(
                chunk,
                "w",
                getattr(chunk, "width", getattr(chunk, "size", 10.0)),
            )
        )
        h = float(
            getattr(
                chunk,
                "h",
                getattr(chunk, "height", getattr(chunk, "size", 7.0)),
            )
        )
        gore.append(
            {
                "x": pos.x,
                "y": pos.y,
                "w": max(5.0, min(22.0, w)),
                "h": max(4.0, min(18.0, h)),
                "rot": float(
                    getattr(
                        chunk,
                        "rotation",
                        getattr(chunk, "angle", 0.0),
                    )
                ),
                "cls": chunk.__class__.__name__.lower(),
            }
        )
    gore.sort(key=lambda e: (pygame.Vector2(e["x"], e["y"]) - center).length())
    gore = gore[:28]


    if len(gore) < 10:
        for i in range(10 - len(gore)):
            ang = (i / max(1, 10)) * math.tau
            pos = center + pygame.Vector2(math.cos(ang), math.sin(ang)) * (
                18 + (i % 3) * 9
            )
            gore.append(
                {
                    "x": pos.x,
                    "y": pos.y,
                    "w": 11 + (i % 3) * 3,
                    "h": 7 + (i % 2) * 2,
                    "rot": i * 21.0,
                    "cls": "organ",
                }
            )

    v78_death_snapshot = {
        "start_ms": now,
        "blood": blood,
        "gore": gore,
    }
# </POTBO_STAGE S1567>

# <POTBO_STAGE S1569>


_v78_death_blood_original = _v77_death_blood_layer
_v78_death_gore_original = _v77_death_gore_layer
# </POTBO_STAGE S1569>

# <POTBO_STAGE S1571>


def _v77_death_blood_layer():
    if not v78_death_snapshot["blood"]:
        return _v78_death_blood_original()
    age = _v78_death_snapshot_age()
    keep = max(0.0, 1.0 - _v78_smoothstep01(age / 6.0))
    for i, e in enumerate(v78_death_snapshot["blood"]):
        if (i / max(1, len(v78_death_snapshot["blood"]))) > keep + 0.08:
            continue
        sx = int(round(dunya_ekran_x(e["x"])))
        sy = int(round(dunya_ekran_y(e["y"])))
        r = max(1, int(round(e["r"] * (0.72 + 0.28 * keep))))
        if e.get("kind") == "pool":
            pygame.draw.ellipse(
                ekran,
                V77_DEATH_BLOOD,
                pygame.Rect(sx - r * 2, sy - r, r * 4, r * 2),
            )
        else:
            pygame.draw.circle(ekran, V77_DEATH_BLOOD, (sx, sy), r)

    body_x = int(round(dunya_ekran_x(oyuncu_x)))
    body_y = int(round(dunya_ekran_y(oyuncu_y + 6)))
    core_r = max(10, int(round(18 * (0.55 + keep * 0.45))))
    pygame.draw.ellipse(
        ekran,
        V77_DEATH_BLOOD,
        pygame.Rect(
            body_x - core_r * 2,
            body_y - core_r,
            core_r * 4,
            core_r * 2,
        ),
    )


def _v77_death_gore_layer():
    if not v78_death_snapshot["gore"]:
        return _v78_death_gore_original()
    age = _v78_death_snapshot_age()
    keep = max(0.0, 1.0 - _v78_smoothstep01(age / 7.2))
    for i, e in enumerate(v78_death_snapshot["gore"]):
        if (i / max(1, len(v78_death_snapshot["gore"]))) > keep + 0.16:
            continue
        sx = int(round(dunya_ekran_x(e["x"])))
        sy = int(round(dunya_ekran_y(e["y"])))
        w = max(4, int(round(e["w"] * (0.84 + 0.16 * keep))))
        h = max(3, int(round(e["h"] * (0.84 + 0.16 * keep))))
        rect = pygame.Rect(sx - w // 2, sy - h // 2, w, h)
        pygame.draw.ellipse(ekran, V77_DEATH_BODY, rect)
        if "bone" in e.get("cls", ""):
            pygame.draw.line(
                ekran,
                V77_DEATH_BLACK,
                (rect.left + 2, rect.centery),
                (rect.right - 2, rect.centery),
                1,
            )

    cx = int(round(dunya_ekran_x(oyuncu_x)))
    cy = int(round(dunya_ekran_y(oyuncu_y - 6)))
    pygame.draw.ellipse(
        ekran,
        V77_DEATH_BODY,
        pygame.Rect(cx - 14, cy - 5, 20, 12),
    )
    pygame.draw.ellipse(
        ekran,
        V77_DEATH_BODY,
        pygame.Rect(cx + 2, cy + 1, 16, 9),
    )
# </POTBO_STAGE S1571>

# <POTBO_STAGE S1575>


def v78_diagnostics():
    return {
        "version": V78_VERSION,
        "developer_shortcut_panel": True,
        "pause_centered": True,
        "universal_ui": True,
        "sharp_hud_bars": True,
        "death_snapshot_blood": len(v78_death_snapshot.get("blood", [])),
        "death_snapshot_gore": len(v78_death_snapshot.get("gore", [])),
    }
# </POTBO_STAGE S1575>

# <POTBO_STAGE S1589>
V79_DEATH_BLOOD_FADE_START_MS = 4200
V79_DEATH_BLOOD_FADE_END_MS = 11200
V79_DEATH_GORE_FADE_START_MS = 5600
V79_DEATH_GORE_FADE_END_MS = 11800
# </POTBO_STAGE S1589>

# <POTBO_STAGE S1601>




def _v79_fade_progress(start_ms, end_ms):
    if oyuncu_olum_baslangic_ms <= 0:
        return 1.0
    age = pygame.time.get_ticks() - int(oyuncu_olum_baslangic_ms)
    if age <= start_ms:
        return 1.0
    if age >= end_ms:
        return 0.0
    return 1.0 - _v79_smootherstep(
        (age - start_ms) / max(1.0, float(end_ms - start_ms))
    )
# </POTBO_STAGE S1601>

# <POTBO_STAGE S1603>


def _v77_death_blood_layer():
    entries = v78_death_snapshot.get("blood", [])
    if not entries:
        return _v78_death_blood_original()
    progress = _v79_fade_progress(
        V79_DEATH_BLOOD_FADE_START_MS,
        V79_DEATH_BLOOD_FADE_END_MS,
    )
    if progress <= 0.0:
        return

    bounds = _v79_snapshot_bounds(entries, 34)
    local = pygame.Surface(bounds.size, pygame.SRCALPHA)
    for e in entries:
        sx = int(round(dunya_ekran_x(float(e["x"])))) - bounds.x
        sy = int(round(dunya_ekran_y(float(e["y"])))) - bounds.y
        base_r = max(1, int(round(float(e.get("r", 2.0)))))

        size_mul = 0.62 + 0.38 * _v79_smoothstep(progress)
        r = max(1, int(round(base_r * size_mul)))
        if e.get("kind") == "pool":
            pygame.draw.ellipse(
                local,
                V77_DEATH_BLOOD,
                pygame.Rect(
                    sx - r * 2,
                    sy - r,
                    max(2, r * 4),
                    max(2, r * 2),
                ),
            )
        else:
            pygame.draw.circle(local, V77_DEATH_BLOOD, (sx, sy), r)

    core_x = int(round(dunya_ekran_x(oyuncu_x))) - bounds.x
    core_y = int(round(dunya_ekran_y(oyuncu_y + 6))) - bounds.y
    core_r = max(8, int(round(18 * (0.70 + 0.30 * progress))))
    pygame.draw.ellipse(
        local,
        V77_DEATH_BLOOD,
        pygame.Rect(
            core_x - core_r * 2,
            core_y - core_r,
            core_r * 4,
            core_r * 2,
        ),
    )
    _v79_dither_blit(local, bounds.topleft, progress)


def _v77_death_gore_layer():
    entries = v78_death_snapshot.get("gore", [])
    if not entries:
        return _v78_death_gore_original()
    progress = _v79_fade_progress(
        V79_DEATH_GORE_FADE_START_MS, V79_DEATH_GORE_FADE_END_MS
    )
    if progress <= 0.0:
        return

    bounds = _v79_snapshot_bounds(entries, 30)
    local = pygame.Surface(bounds.size, pygame.SRCALPHA)
    for e in entries:
        sx = int(round(dunya_ekran_x(float(e["x"])))) - bounds.x
        sy = int(round(dunya_ekran_y(float(e["y"])))) - bounds.y
        w = max(
            4,
            int(round(float(e.get("w", 10.0)) * (0.76 + 0.24 * progress))),
        )
        h = max(
            3,
            int(round(float(e.get("h", 7.0)) * (0.76 + 0.24 * progress))),
        )
        rect = pygame.Rect(sx - w // 2, sy - h // 2, w, h)
        pygame.draw.ellipse(local, V77_DEATH_BODY, rect)
        if "bone" in str(e.get("cls", "")):
            pygame.draw.line(
                local,
                V77_DEATH_BLACK,
                (rect.left + 2, rect.centery),
                (rect.right - 2, rect.centery),
                1,
            )
    _v79_dither_blit(local, bounds.topleft, progress)
# </POTBO_STAGE S1603>

# <POTBO_STAGE S1609>





v80_death_fx = {
    "start_ms": 0,
    "emitters": [],
    "pools": [],
    "gore": [],
    "embers": [],
    "death_type": "blood",
}
# </POTBO_STAGE S1609>

# <POTBO_STAGE S1613>


def _v80_make_death_fx():
    global v80_death_fx
    center = pygame.Vector2(float(oyuncu_x), float(oyuncu_y - 12.0))
    base_world = pygame.Vector2(float(oyuncu_x), float(oyuncu_y - 10.0))
    f, side = _v80_player_basis()
    dtype = str(oyuncu_olum_turu)

    emitters = []
    pools = []
    embers = []
    gore = []

    def add_emitter(
        origin,
        direction,
        spread=18.0,
        speed=34.0,
        life=1150,
        branches=6,
        delay=0,
    ):
        direction = pygame.Vector2(direction)
        if direction.length_squared() <= 1e-6:
            direction = pygame.Vector2(f)
        direction = direction.normalize()
        emitters.append(
            {
                "origin": pygame.Vector2(origin),
                "dir": direction,
                "spread": float(spread),
                "speed": float(speed),
                "life": int(life),
                "branches": int(branches),
                "delay": int(delay),
            }
        )

    def add_pool(pos, rx, ry, delay, grow_ms=1300):
        pools.append(
            {
                "pos": pygame.Vector2(pos),
                "rx": float(rx),
                "ry": float(ry),
                "delay": int(delay),
                "grow_ms": int(grow_ms),
            }
        )


    if dtype == "blood":
        o1 = _v80_world_from_local(-2, -2, base_world)
        o2 = _v80_world_from_local(4, -7, base_world)
        add_emitter(
            o1,
            f.rotate(-10),
            spread=20,
            speed=36,
            life=1180,
            branches=7,
        )
        add_emitter(
            o2,
            f.rotate(18),
            spread=26,
            speed=31,
            life=1020,
            branches=5,
            delay=90,
        )
        for i, ang in enumerate((-18, -6, 8, 19)):
            pos = (
                o1 + f.rotate(ang) * (22 + i * 10) + pygame.Vector2(0.0, 6.0 + i * 1.4)
            )
            add_pool(
                pos,
                10 + i * 3.5,
                5 + i * 1.7,
                260 + i * 170,
                1250 + i * 180,
            )
        add_pool(
            _v80_world_from_local(1, 17, base_world),
            18,
            9,
            880,
            1600,
        )


    elif dtype in ("blast_core", "blast_inner", "blast_mid"):
        origins = [
            _v80_world_from_local(0, -4, base_world),
            _v80_world_from_local(-5, 1, base_world),
            _v80_world_from_local(5, 1, base_world),
        ]
        dirs = [f, f.rotate(-72), f.rotate(72)]
        speeds = [40.0, 34.0, 34.0]
        for i, (o, d, s) in enumerate(zip(origins, dirs, speeds)):
            add_emitter(
                o,
                d,
                spread=18 if i == 0 else 28,
                speed=s,
                life=1240 if i == 0 else 1100,
                branches=7 if i == 0 else 5,
                delay=i * 40,
            )
            for j in range(3):
                pos = o + d * (26 + j * 13) + pygame.Vector2(0.0, 5.0 + j * 1.5)
                add_pool(
                    pos,
                    8 + j * 3 + (2 if i == 0 else 0),
                    4 + j * 2,
                    220 + i * 70 + j * 160,
                    1180 + j * 160,
                )

        for i, d in enumerate(dirs):
            for j in range(3):
                pos = center + d * (14 + j * 12) + side * ((j - 1) * 7.0)
                gore.append(
                    {
                        "pos": pos,
                        "w": 10 + (j % 2) * 3,
                        "h": 7 + ((i + j) % 2) * 2,
                        "rot": d.angle_to(pygame.Vector2(1, 0)) + j * 17.0,
                    }
                )
                embers.append(
                    {
                        "pos": pos + d * 4.0,
                        "phase": i * 0.3 + j * 0.17,
                    }
                )


    elif dtype == "fire":
        o = _v80_world_from_local(0, -4, base_world)
        add_emitter(
            o,
            f.rotate(8),
            spread=12,
            speed=18,
            life=720,
            branches=3,
        )
        add_pool(
            _v80_world_from_local(0, 18, base_world),
            10,
            5,
            540,
            1320,
        )
        for i in range(8):
            embers.append(
                {
                    "pos": _v80_world_from_local(
                        (i % 3 - 1) * 6, -8 + i * 3, base_world
                    ),
                    "phase": i * 0.19,
                }
            )


    snap = (
        globals().get("v78_death_snapshot", {}).get("gore", [])
        if isinstance(globals().get("v78_death_snapshot", {}), dict)
        else []
    )
    for e in snap[:18]:
        try:
            pos = pygame.Vector2(
                float(e.get("x", oyuncu_x)),
                float(e.get("y", oyuncu_y)),
            )
        except Exception:
            continue
        d = pos - center
        if d.length() > 70.0:
            d.scale_to_length(70.0)
            pos = center + d
        gore.append(
            {
                "pos": pos,
                "w": max(6.0, min(18.0, float(e.get("w", 10.0)))),
                "h": max(4.0, min(14.0, float(e.get("h", 7.0)))),
                "rot": float(e.get("rot", 0.0)),
            }
        )

    v80_death_fx = {
        "start_ms": pygame.time.get_ticks(),
        "emitters": emitters,
        "pools": pools,
        "gore": gore,
        "embers": embers,
        "death_type": dtype,
    }
# </POTBO_STAGE S1613>

# <POTBO_STAGE S1617>


def oyuncu_olum_sahnesini_sifirla():
    global v80_death_fx
    v80_death_fx = {
        "start_ms": 0,
        "emitters": [],
        "pools": [],
        "gore": [],
        "embers": [],
        "death_type": "blood",
    }
    _v80_death_reset_original()



def _v77_death_blood_layer():
    age = _v80_death_age_ms()
    if age <= 0:
        return


    for pool in v80_death_fx.get("pools", []):
        t = _v80_clamp01((age - int(pool["delay"])) / max(1.0, float(pool["grow_ms"])))
        if t <= 0.0:
            continue
        p = _v80_smooth(t)
        _v80_draw_world_ellipse(
            pool["pos"],
            pool["rx"] * p,
            pool["ry"] * p,
            V77_DEATH_BLOOD,
        )


    for em in v80_death_fx.get("emitters", []):
        local_age = age - int(em.get("delay", 0))
        if local_age <= 0:
            continue
        t = _v80_clamp01(local_age / max(1.0, float(em["life"])))
        if t <= 0.0:
            continue
        origin = pygame.Vector2(em["origin"])
        base_dir = pygame.Vector2(em["dir"])
        branches = max(1, int(em.get("branches", 5)))
        spread = float(em.get("spread", 18.0))
        speed = float(em.get("speed", 30.0))

        for i in range(branches):
            if branches == 1:
                offset = 0.0
            else:
                offset = ((i / (branches - 1)) - 0.5) * spread
            d = base_dir.rotate(offset)
            length = speed * (0.28 + 0.92 * t) * (0.90 + (i % 3) * 0.06)
            grav = pygame.Vector2(0.0, 14.0 + 12.0 * t)
            prev = pygame.Vector2(origin)
            segments = 4
            for step in range(1, segments + 1):
                s = step / float(segments)
                pos = origin + d * (length * s) + grav * (s * s * t * 0.18)
                _v80_draw_world_line(
                    prev,
                    pos,
                    V77_DEATH_BLOOD,
                    1 + (1 if step < 3 and t < 0.8 else 0),
                )
                if step >= 2:
                    _v80_draw_world_circle(
                        pos,
                        1 if step < segments else 2,
                        V77_DEATH_BLOOD,
                    )
                prev = pos



def _v77_death_gore_layer():
    age = _v80_death_age_ms()
    if age <= 0:
        return
    grow = _v80_smooth(min(1.0, age / 520.0))
    flick = (pygame.time.get_ticks() // 90) % 3
    for idx, g in enumerate(v80_death_fx.get("gore", [])):
        pos = pygame.Vector2(g["pos"])
        w = max(4, int(round(float(g["w"]) * (0.72 + 0.28 * grow))))
        h = max(3, int(round(float(g["h"]) * (0.72 + 0.28 * grow))))
        sx = int(round(dunya_ekran_x(pos.x)))
        sy = int(round(dunya_ekran_y(pos.y)))
        rect = pygame.Rect(sx - w // 2, sy - h // 2, w, h)
        pygame.draw.ellipse(ekran, V77_DEATH_BODY, rect)
        pygame.draw.line(
            ekran,
            V77_DEATH_BLACK,
            (rect.left + 1, rect.centery),
            (rect.right - 1, rect.centery),
            1,
        )
        if v80_death_fx.get("death_type") in (
            "fire",
            "blast_core",
            "blast_inner",
            "blast_mid",
        ):
            if (idx + flick) % 2 == 0:
                pygame.draw.arc(
                    ekran,
                    V77_DEATH_BODY,
                    rect.inflate(6, 6),
                    0.0,
                    math.pi * 0.8,
                    1,
                )
            else:
                pygame.draw.arc(
                    ekran,
                    V77_DEATH_BLACK,
                    rect.inflate(4, 4),
                    math.pi * 0.15,
                    math.pi * 1.18,
                    1,
                )

    if v80_death_fx.get("death_type") in (
        "fire",
        "blast_core",
        "blast_inner",
        "blast_mid",
    ):
        for e in v80_death_fx.get("embers", []):
            phase = float(e.get("phase", 0.0))
            pulse = 0.5 + 0.5 * math.sin((age / 140.0) + phase * math.tau)
            p = pygame.Vector2(e["pos"])
            off = pygame.Vector2(
                math.sin(phase * 11.0 + age / 260.0),
                -abs(math.cos(phase * 7.0 + age / 210.0)),
            ) * (1.5 + pulse * 1.2)
            pos = p + off
            _v80_draw_world_circle(
                pos,
                1 if pulse < 0.75 else 2,
                V77_DEATH_BODY if pulse > 0.35 else V77_DEATH_BLACK,
            )
# </POTBO_STAGE S1617>

# <POTBO_STAGE S1626>


def _v81_draw_stain(drop, now):
    landing_time = int(drop["birth_ms"]) + int(drop["flight_ms"])
    grow = _v81_smooth((int(now) - landing_time) / max(1.0, float(drop["grow_ms"])))
    if grow <= 0.0:
        return
    pts = _v81_polygon_points(
        drop["landing"],
        drop["rx"],
        drop["ry"],
        drop["angle"],
        drop["shape"],
        0.18 + 0.82 * grow,
    )
    if len(pts) >= 3:
        pygame.draw.polygon(ekran, V77_DEATH_BLOOD, pts)
    if drop.get("satellite") and grow > 0.28:
        p = (
            pygame.Vector2(drop["landing"])
            + pygame.Vector2(float(drop["sat_dx"]), float(drop["sat_dy"])) * grow
        )
        _v80_draw_world_circle(
            p,
            max(1, int(round(float(drop["sat_r"]) * grow))),
            V77_DEATH_BLOOD,
        )

    if not drop.get("decal_added") and grow >= 0.18:


        scale = max(
            0.11,
            min(
                0.58,
                (float(drop["rx"]) + float(drop["ry"])) / 20.0,
            ),
        )
        decal = kan_lekesi_ekle(
            float(drop["landing"].x),
            float(drop["landing"].y),
            scale,
        )
        drop["decal_added"] = True
        drop["decal_committed"] = decal is not None
# </POTBO_STAGE S1626>

# <POTBO_STAGE S1628>


def _v77_death_blood_layer():
    if int(v81_death_blood.get("start_ms", 0)) <= 0:

        return

    now = pygame.time.get_ticks()


    for seep in v81_death_blood.get("seeps", []):
        _v81_draw_seep(seep, now)

    for drop in v81_death_blood.get("drops", []):
        pos, height, landed = _v81_drop_position(drop, now)
        if pos is None:
            continue
        if landed:
            _v81_draw_stain(drop, now)
            continue



        age = int(now) - int(drop["birth_ms"])
        flight = max(1, int(drop["flight_ms"]))
        p = _v81_clamp01(age / float(flight))
        sx = float(dunya_ekran_x(pos.x))
        sy = float(dunya_ekran_y(pos.y)) - float(height) * KAMERA_YAKINLASTIRMA
        prev_p = max(
            0.0,
            p - 0.045 - min(0.035, float(drop["size"]) * 0.008),
        )
        prev_ground = pygame.Vector2(drop["origin"]).lerp(
            pygame.Vector2(drop["landing"]), prev_p
        )
        prev_arc = float(drop["height"]) * 4.0 * prev_p * (1.0 - prev_p)
        px = float(dunya_ekran_x(prev_ground.x))
        py = float(dunya_ekran_y(prev_ground.y)) - prev_arc * KAMERA_YAKINLASTIRMA
        width = 1 if float(drop["size"]) < 1.9 else 2
        pygame.draw.line(
            ekran,
            V77_DEATH_BLOOD,
            (int(round(px)), int(round(py))),
            (int(round(sx)), int(round(sy))),
            width,
        )
        pygame.draw.circle(
            ekran,
            V77_DEATH_BLOOD,
            (int(round(sx)), int(round(sy))),
            max(1, int(round(float(drop["size"])))),
        )








_v81_katil_frame_original = _v30_katil_koreografi_frame
# </POTBO_STAGE S1628>

# <POTBO_STAGE S1630>


def _v30_olum_koreografi_guncelle(simdi):
    global oyuncu_olum_ikiye_bolundu
    if oyuncu_olum_baslangic_ms <= 0 or oyuncu_olum_turu not in (
        "blood",
        "blast_inner",
    ):
        return
    alt = str(oyuncu_olum_alt_turu or "")




    if alt not in (
        "crawler",
        "berserker",
        "torrmund_decap_cleave",
    ):
        return

    ready = _v32_katil_temasa_yaklastir(simdi)
    if ready <= 0:
        return
    elapsed = max(0, int(simdi) - int(ready))
    killer = _v24_olum_katil_actor_bul()
    if killer is not None:
        base = pygame.Vector2(
            oyuncu_x - float(killer.x),
            oyuncu_y - float(killer.y),
        )
    else:
        base = _v81_impact_direction()
    if base.length_squared() <= 1e-6:
        base = pygame.Vector2(1.0, 0.0)
    base = base.normalize()

    def hit(key, at_ms, actual_particles, gore_n, power, kind, index):
        if elapsed < int(at_ms) or key in oyuncu_olum_koreografi_vuruslari:
            return False
        oyuncu_olum_koreografi_vuruslari.add(key)



        kan_parcacigi_patlat(
            oyuncu_x,
            oyuncu_y - 10.0,
            int(actual_particles),
            float(power),
            yon=base.rotate(random.uniform(-18.0, 18.0)),
            arterial=True,
        )
        if gore_n > 0:
            _v30_kucuk_gore_jet(
                oyuncu_x,
                oyuncu_y - 9.0,
                int(gore_n),
                base,
                max(0.78, power * 0.70),
                True,
            )
        _v81_post_hit_blood(kind, index, base, simdi)
        kamera_hit_sarsintisi_baslat(3.2 + power * 2.6, int(82 + power * 44))
        return True

    if alt == "crawler":
        for i, at_ms in enumerate((70, 205, 340, 475, 610, 745)):
            hit(
                f"crawler_{i}",
                at_ms,
                random.randint(13, 18),
                random.randint(2, 4),
                0.98 + i * 0.025,
                "crawler",
                i,
            )

    elif alt == "berserker":
        for i, at_ms in enumerate((80, 235, 390, 545, 700, 855)):
            hit(
                f"bers_{i}",
                at_ms,
                random.randint(18, 24),
                random.randint(3, 5),
                1.20 + i * 0.035,
                "berserker",
                i,
            )

    elif alt == "torrmund_decap_cleave":
        if hit(
            "torrmund_second",
            1060,
            random.randint(34, 46),
            random.randint(12, 18),
            1.92,
            "torrmund_second",
            0,
        ):
            oyuncu_olum_ikiye_bolundu = True
# </POTBO_STAGE S1630>

# <POTBO_STAGE S1633>


def v81_diagnostics():
    return {
        "version": V81_VERSION,
        "postmortem_attackers": (
            "crawler",
            "berserker",
            "torrmund_decap_cleave",
        ),
        "max_death_droplets": V81_MAX_DROPLETS,
        "active_death_droplets": len(v81_death_blood.get("drops", [])),
        "active_wound_seeps": len(v81_death_blood.get("seeps", [])),
        "landing_creates_persistent_decal": True,
        "instant_death_puddle": False,
    }
# </POTBO_STAGE S1633>

# <POTBO_STAGE S1644>


def one_cikan_item_paneli_ciz():
    panel = hud_sag_rect()
    gotik_panel(panel, V81_HUD_PANEL_ACCENT, 242)

    slot_boyut = 68
    bosluk = 12
    grup_w = slot_boyut * 5 + bosluk * 4
    q_boyut = slot_boyut
    ayirici_bosluk = 30
    toplam = grup_w + ayirici_bosluk + q_boyut
    baslangic_x = panel.centerx - toplam // 2
    y = panel.y + 41

    pygame.draw.line(
        ekran,
        (118, 95, 102),
        (panel.x + 28, panel.y + 24),
        (panel.right - 28, panel.y + 24),
        1,
    )

    for i in range(5):
        rect = pygame.Rect(
            baslangic_x + i * (slot_boyut + bosluk),
            y,
            slot_boyut,
            slot_boyut,
        )
        _v81_feature_slot_draw(
            rect,
            i + 1,
            item_index=one_cikan_slotlar[i],
            selected=(i == envanter_secili_slot),
            magic=False,
            dragging=False,
        )

    ayir_x = baslangic_x + grup_w + ayirici_bosluk // 2
    pygame.draw.line(
        ekran,
        (94, 76, 84),
        (ayir_x, y - 4),
        (ayir_x, y + slot_boyut + 4),
        1,
    )

    q_hizli_slot_normalize_et()
    qx = baslangic_x + grup_w + ayirici_bosluk
    q_rect = pygame.Rect(qx, y, q_boyut, q_boyut)
    q_item = q_hizli_item_index
    q_debug_spell = bool(gelistirici_sonsuz_ates)
    q_is_magic = q_debug_spell or (
        isinstance(q_item, int)
        and 0 <= q_item < len(envanter_itemleri)
        and item_buyu_mu(envanter_itemleri[q_item])
    )
    _v81_feature_slot_draw(
        q_rect,
        "Q",
        item_index=None,
        selected=False,
        magic=q_is_magic,
        dragging=False,
    )
    if q_debug_spell:
        item_ikonu_ciz("fire_magic", q_rect.inflate(-12, -12), False)
        spell_okulu_sembol_ciz(
            "IGNIS",
            pygame.Rect(q_rect.right - 23, q_rect.bottom - 23, 19, 19),
        )
        yazi_yaz(
            "∞",
            q_rect.centerx,
            q_rect.y + 12,
            (255, 238, 178),
            mini_font,
            True,
        )
    elif isinstance(q_item, int) and 0 <= q_item < len(envanter_itemleri):
        item = envanter_itemleri[q_item]
        if isinstance(item, dict):
            item_ikonu_ciz(item.get("id"), q_rect.inflate(-12, -12), False)
            if item.get("spell_school"):
                spell_okulu_sembol_ciz(
                    item.get("spell_school"),
                    pygame.Rect(
                        q_rect.right - 23,
                        q_rect.bottom - 23,
                        19,
                        19,
                    ),
                )

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


def _v81_draw_pixel_drips_screen(sx, sy, seed, intensity=1.0, blood_color=None):
    if blood_color is None:
        blood_color = V77_DEATH_BLOOD
    rng = random.Random(int(seed) & 0x7FFFFFFF)
    stems = max(3, min(8, 3 + int(round(intensity * 3.2))))
    for i in range(stems):
        x = int(round(sx)) + rng.randint(-4, 4)
        y = int(round(sy)) + rng.randint(-2, 3)
        stem = rng.randint(6, 12) + int(round(intensity * rng.randint(2, 7)))
        prev = (x, y)
        curx = x
        for step in range(2, stem + 1, 2):
            curx += rng.choice((-1, 0, 0, 1))
            ny = y + step
            pygame.draw.line(ekran, blood_color, prev, (curx, ny), 1)
            if step > 2 and rng.random() < 0.55:
                pygame.draw.circle(ekran, blood_color, (curx, ny), 1)
            prev = (curx, ny)
        end_y = y + stem
        radius = 2 if rng.random() < 0.45 else 1
        pygame.draw.circle(ekran, blood_color, (curx, end_y), radius)
        floor_y = end_y + rng.randint(2, 5)
        smear_w = rng.randint(2, 5) + (1 if intensity > 1.05 else 0)
        for _ in range(rng.randint(1, 3)):
            dx = rng.randint(-4, 5)
            rr = 1 if rng.random() < 0.65 else 2
            pygame.draw.ellipse(
                ekran,
                blood_color,
                pygame.Rect(curx + dx - rr, floor_y - 1, smear_w, rr + 1),
            )
# </POTBO_STAGE S1644>

# <POTBO_STAGE S1646>


def _v81_player_blood_anchors():
    base = pygame.Vector2(float(oyuncu_x), float(oyuncu_y - 10.0))
    f, side = _v80_player_basis()
    return [
        base + side * 8.0 + f * 5.0,
        base - side * 9.0 + f * 4.0,
        base + f * 1.0,
    ]


def _v81_death_player_drips():
    if oyuncu_olum_turu == "fire":
        return
    anchors = _v81_player_blood_anchors()
    now = pygame.time.get_ticks() // 30
    for idx, pos in enumerate(anchors):
        sx, sy = _v81_world_to_screen(pos)
        _v81_draw_pixel_drips_screen(
            sx,
            sy + idx,
            now + idx * 137 + int(oyuncu_x * 3.0),
            intensity=1.05 + idx * 0.15,
        )
# </POTBO_STAGE S1646>

# <POTBO_STAGE S1648>


def _v80_make_death_fx():
    global v80_death_fx
    center = pygame.Vector2(float(oyuncu_x), float(oyuncu_y - 12.0))
    base_world = pygame.Vector2(float(oyuncu_x), float(oyuncu_y - 10.0))
    f, side = _v80_player_basis()
    dtype = str(oyuncu_olum_turu)

    emitters = []
    pools = []
    embers = []
    gore = []

    def add_emitter(
        origin,
        direction,
        spread=18.0,
        speed=34.0,
        life=1150,
        branches=6,
        delay=0,
    ):
        direction = pygame.Vector2(direction)
        if direction.length_squared() <= 1e-6:
            direction = pygame.Vector2(f)
        direction = direction.normalize()
        emitters.append(
            {
                "origin": pygame.Vector2(origin),
                "dir": direction,
                "spread": float(spread),
                "speed": float(speed),
                "life": int(life),
                "branches": int(branches),
                "delay": int(delay),
            }
        )

    def add_pool(pos, rx, ry, delay, grow_ms=1300):
        pools.append(
            {
                "pos": pygame.Vector2(pos),
                "rx": float(rx),
                "ry": float(ry),
                "delay": int(delay),
                "grow_ms": int(grow_ms),
            }
        )

    if dtype == "blood":
        o1 = _v80_world_from_local(-3, -3, base_world)
        o2 = _v80_world_from_local(5, -8, base_world)
        o3 = _v80_world_from_local(-8, -1, base_world)
        add_emitter(
            o1,
            f.rotate(-14),
            spread=30,
            speed=42,
            life=1420,
            branches=10,
        )
        add_emitter(
            o2,
            f.rotate(18),
            spread=34,
            speed=35,
            life=1260,
            branches=8,
            delay=58,
        )
        add_emitter(
            o3,
            f.rotate(-44),
            spread=18,
            speed=24,
            life=980,
            branches=5,
            delay=120,
        )
        add_emitter(
            _v80_world_from_local(7, -2, base_world),
            f.rotate(38),
            spread=14,
            speed=19,
            life=760,
            branches=3,
            delay=210,
        )
        for i, ang in enumerate((-24, -14, -3, 7, 18, 29)):
            pos = (
                o1
                + f.rotate(ang) * (18 + i * 8.5)
                + side * ((i % 2) * 2.8 - 1.4)
                + pygame.Vector2(0.0, 4.0 + i * 1.8)
            )
            add_pool(
                pos,
                8 + i * 2.4,
                4 + i * 1.2,
                180 + i * 130,
                1060 + i * 150,
            )
        add_pool(
            _v80_world_from_local(-4, 17, base_world),
            24,
            10,
            730,
            1700,
        )
        add_pool(
            _v80_world_from_local(9, 14, base_world),
            13,
            6,
            880,
            1580,
        )
        for i in range(9):
            spread_dir = f.rotate(-52 + i * 13.0)
            pos = center + spread_dir * (18 + i * 5.5) + side * ((i % 3) - 1) * 4.0
            gore.append(
                {
                    "pos": pos,
                    "w": 7 + (i % 3) * 2,
                    "h": 4 + ((i + 1) % 2) * 2,
                    "rot": spread_dir.angle_to(pygame.Vector2(1, 0)) + i * 9.0,
                }
            )

    elif dtype in ("blast_core", "blast_inner", "blast_mid"):
        origins = [
            _v80_world_from_local(0, -4, base_world),
            _v80_world_from_local(-5, 1, base_world),
            _v80_world_from_local(5, 1, base_world),
            _v80_world_from_local(1, -10, base_world),
        ]
        dirs = [f, f.rotate(-72), f.rotate(72), f.rotate(12)]
        speeds = [43.0, 35.0, 34.0, 28.0]
        for i, (o, d, s) in enumerate(zip(origins, dirs, speeds)):
            add_emitter(
                o,
                d,
                spread=18 if i == 0 else 29,
                speed=s,
                life=1320 if i == 0 else 1120,
                branches=8 if i == 0 else 5,
                delay=i * 34,
            )
            for j in range(4):
                pos = o + d * (24 + j * 12) + side * ((j - 1.5) * 5.0)
                add_pool(
                    pos,
                    8 + j * 3 + (2 if i == 0 else 0),
                    4 + j * 2,
                    180 + i * 65 + j * 120,
                    1140 + j * 140,
                )
        for i, d in enumerate(dirs):
            for j in range(4):
                pos = center + d * (14 + j * 11) + side * ((j - 1.5) * 7.0)
                gore.append(
                    {
                        "pos": pos,
                        "w": 10 + (j % 2) * 3,
                        "h": 7 + ((i + j) % 2) * 2,
                        "rot": d.angle_to(pygame.Vector2(1, 0)) + j * 17.0,
                    }
                )
                embers.append(
                    {
                        "pos": pos + d * 4.0,
                        "phase": i * 0.23 + j * 0.17,
                    }
                )

    elif dtype == "fire":
        o = _v80_world_from_local(0, -4, base_world)
        add_emitter(
            o,
            f.rotate(8),
            spread=12,
            speed=18,
            life=720,
            branches=3,
        )
        add_pool(
            _v80_world_from_local(0, 18, base_world),
            10,
            5,
            540,
            1320,
        )
        for i in range(8):
            embers.append(
                {
                    "pos": _v80_world_from_local(
                        (i % 3 - 1) * 6, -8 + i * 3, base_world
                    ),
                    "phase": i * 0.19,
                }
            )

    snap = (
        globals().get("v78_death_snapshot", {}).get("gore", [])
        if isinstance(globals().get("v78_death_snapshot", {}), dict)
        else []
    )
    for e in snap[:24]:
        try:
            pos = pygame.Vector2(
                float(e.get("x", oyuncu_x)),
                float(e.get("y", oyuncu_y)),
            )
        except Exception:
            continue
        d = pos - center
        if d.length() > 84.0:
            d.scale_to_length(84.0)
            pos = center + d
        gore.append(
            {
                "pos": pos,
                "w": max(6.0, min(18.0, float(e.get("w", 10.0)))),
                "h": max(4.0, min(14.0, float(e.get("h", 7.0)))),
                "rot": float(e.get("rot", 0.0)),
            }
        )

    v80_death_fx = {
        "start_ms": pygame.time.get_ticks(),
        "emitters": emitters,
        "pools": pools,
        "gore": gore,
        "embers": embers,
        "death_type": dtype,
    }


def _v77_death_blood_layer():
    age = _v80_death_age_ms()
    if age <= 0:
        return

    for idx, pool in enumerate(v80_death_fx.get("pools", [])):
        t = _v80_clamp01((age - int(pool["delay"])) / max(1.0, float(pool["grow_ms"])))
        if t <= 0.0:
            continue
        p = _v80_smooth(t)
        rx = pool["rx"] * p
        ry = pool["ry"] * (0.84 + 0.16 * p)
        _v81_irregular_pool_world(
            pool["pos"],
            rx,
            ry,
            V77_DEATH_BLOOD,
            idx * 163 + int(pool["rx"] * 13),
        )

    for em_index, em in enumerate(v80_death_fx.get("emitters", [])):
        local_age = age - int(em.get("delay", 0))
        if local_age <= 0:
            continue
        t = _v80_clamp01(local_age / max(1.0, float(em["life"])))
        if t <= 0.0:
            continue
        origin = pygame.Vector2(em["origin"])
        base_dir = pygame.Vector2(em["dir"])
        branches = max(1, int(em.get("branches", 5)))
        spread = float(em.get("spread", 18.0))
        speed = float(em.get("speed", 30.0))

        for i in range(branches):
            seed = em_index * 1009 + i * 97 + int(speed * 11)
            rng = random.Random(seed)
            if branches == 1:
                offset = 0.0
            else:
                offset = ((i / (branches - 1)) - 0.5) * spread + rng.uniform(-4.0, 4.0)
            d = base_dir.rotate(offset)
            side = pygame.Vector2(d.y, -d.x)
            length = speed * (0.24 + 0.98 * t) * rng.uniform(0.86, 1.13)
            grav = pygame.Vector2(0.0, 14.0 + 18.0 * t + rng.uniform(0.0, 4.0))
            prev = pygame.Vector2(origin)
            segments = 5 if speed < 26.0 else 6
            for step in range(1, segments + 1):
                s = step / float(segments)
                jitter = (
                    side
                    * math.sin((s * math.pi) + rng.uniform(-0.5, 0.5))
                    * (0.8 + 2.4 * s)
                )
                pos = origin + d * (length * s) + grav * (s * s * t * 0.20) + jitter
                width = 2 if step <= 2 and t < 0.72 and (i % 2 == 0) else 1
                _v80_draw_world_line(prev, pos, V77_DEATH_BLOOD, width)
                if step >= 2:
                    _v80_draw_world_circle(
                        pos,
                        1 if step < segments else 2,
                        V77_DEATH_BLOOD,
                    )
                    if step >= segments - 1:
                        blob = pos + pygame.Vector2(
                            rng.uniform(-1.5, 1.5),
                            rng.uniform(1.0, 3.2),
                        )
                        _v80_draw_world_ellipse(
                            blob,
                            1.0 + (0.35 if step == segments else 0.0),
                            1.0,
                            V77_DEATH_BLOOD,
                        )
                prev = pos


def _v77_death_killer_draw(actor):
    if actor is None:
        return
    sil, rect = _v24_katil_siluet_surface_ve_rect(actor)
    if sil is not None and rect is not None:
        rect = rect.copy()
        rect.x = int(_v81_clamp(rect.x, 12, GENISLIK - rect.width - 12))
        rect.y = int(_v81_clamp(rect.y, 28, YUKSEKLIK - rect.height - 26))
        _v81_death_ground_anchor(rect, blood=True)
        mask = pygame.mask.from_surface(sil, 1)
        flat = mask.to_surface(
            setcolor=(*V77_DEATH_BODY, 255),
            unsetcolor=(0, 0, 0, 0),
        ).convert_alpha()
        ekran.blit(flat, rect)

    if oyuncu_olum_turu == "fire":
        return
    point = _v24_katil_silah_kan_noktasi(actor)
    if point is None:
        return
    sx = float(dunya_ekran_x(point.x))
    sy = float(dunya_ekran_y(point.y))
    direction = str(getattr(actor, "direction", "right"))
    blade_offset = 5 if direction == "right" else -5
    pygame.draw.line(
        ekran,
        V77_DEATH_BLOOD,
        (int(round(sx - blade_offset)), int(round(sy - 1))),
        (int(round(sx + blade_offset)), int(round(sy + 1))),
        1,
    )
    pygame.draw.line(
        ekran,
        V77_DEATH_BLOOD,
        (int(round(sx)), int(round(sy - 2))),
        (int(round(sx)), int(round(sy + 7))),
        max(1, int(round(2 * KAMERA_YAKINLASTIRMA))),
    )
    seed = int(
        getattr(actor, "x", 0) * 13
        + getattr(actor, "y", 0) * 7
        + pygame.time.get_ticks() // 30
    )
    _v81_draw_pixel_drips_screen(sx, sy + 2, seed, intensity=1.35)
    _v81_draw_pixel_drips_screen(
        sx + blade_offset * 0.55,
        sy + 1,
        seed + 81,
        intensity=0.95,
    )
# </POTBO_STAGE S1648>

# <POTBO_STAGE S1650>


def oyuncu_olum_sahnesi_ciz():
    ekran.fill(V77_DEATH_BLACK)
    _v77_semantic_layer(_v77_death_blood_layer, V77_DEATH_BLOOD, 0.66)
    _v77_semantic_layer(_v77_death_gore_layer, V77_DEATH_BODY, 0.34)

    killer = _v24_olum_katil_actor_bul()
    killer_behind = killer is not None and float(
        getattr(killer, "y", oyuncu_y)
    ) <= float(oyuncu_y)
    if killer_behind:
        _v77_death_killer_draw(killer)

    victim_ok = _v77_semantic_layer(_v77_death_victim_layer, V77_DEATH_BODY, 0.34)
    if not victim_ok:
        _v77_death_fallback_victim()
    _v81_death_player_drips()

    _v77_semantic_layer(_v77_death_fire_layer, V77_DEATH_BODY, 0.25)

    if killer is not None and not killer_behind:
        _v77_death_killer_draw(killer)

    if oyuncu_olum_baslangic_ms <= 0:
        return
    now = pygame.time.get_ticks()
    title_p = oyuncu_olum_baslik_fade_orani(now)
    _v34_gameover_music_tick(title_p, now)
    if oyuncu_olum_cikis_orani(now) > 0.0:
        ekran.fill(V77_DEATH_BLACK)
        return
    _v77_death_menu_draw(now)
# </POTBO_STAGE S1650>

# <POTBO_STAGE S1652>


def oyun_ekrani_ciz():
    result = _v81_game_draw_original()
    if oyun_durumu == OYUN and oyuncu_hp > 0:
        oyuncu_paneli_ciz()
        one_cikan_item_paneli_ciz()
        gelistirici_test_paneli_ciz()
    return result
# </POTBO_STAGE S1652>

# <POTBO_STAGE S1666>


def one_cikan_item_paneli_ciz():
    panel = hud_sag_rect()
    gotik_panel(panel, V82_UI_ACCENT, 244)

    slot = 68
    gap = 12
    group_w = slot * 5 + gap * 4
    sep_gap = 30
    total = group_w + sep_gap + slot
    start_x = panel.centerx - total // 2
    y = panel.y + 41

    for i in range(5):
        r = pygame.Rect(start_x + i * (slot + gap), y, slot, slot)
        _v82_feature_slot(
            r,
            i + 1,
            one_cikan_slotlar[i],
            selected=(i == envanter_secili_slot),
            magic=False,
        )

    sep_x = start_x + group_w + sep_gap // 2
    pygame.draw.line(
        ekran,
        (96, 77, 84),
        (sep_x, y - 4),
        (sep_x, y + slot + 4),
        1,
    )

    q_hizli_slot_normalize_et()
    qx = start_x + group_w + sep_gap
    q_rect = pygame.Rect(qx, y, slot, slot)
    q_item = q_hizli_item_index
    q_debug = bool(gelistirici_sonsuz_ates)
    q_magic = q_debug or (
        isinstance(q_item, int)
        and 0 <= q_item < len(envanter_itemleri)
        and item_buyu_mu(envanter_itemleri[q_item])
    )
    _v82_feature_slot(q_rect, "Q", None, selected=False, magic=q_magic)
    if q_debug:
        item_ikonu_ciz("fire_magic", q_rect.inflate(-12, -12), False)
        spell_okulu_sembol_ciz(
            "IGNIS",
            pygame.Rect(q_rect.right - 23, q_rect.bottom - 23, 19, 19),
        )
        yazi_yaz(
            "∞",
            q_rect.centerx,
            q_rect.y + 12,
            (255, 238, 178),
            mini_font,
            True,
        )
    elif isinstance(q_item, int) and 0 <= q_item < len(envanter_itemleri):
        item = envanter_itemleri[q_item]
        if isinstance(item, dict):
            item_ikonu_ciz(item.get("id"), q_rect.inflate(-12, -12), False)
            if item.get("spell_school"):
                spell_okulu_sembol_ciz(
                    item.get("spell_school"),
                    pygame.Rect(
                        q_rect.right - 23,
                        q_rect.bottom - 23,
                        19,
                        19,
                    ),
                )

    if q_magic and not q_debug:
        kalan = max(
            0,
            FIRE_MAGIC_COOLDOWN_MS
            - (pygame.time.get_ticks() - fire_magic_son_kullanim),
        )
        if kalan > 0:
            oran = max(0.0, min(1.0, kalan / FIRE_MAGIC_COOLDOWN_MS))
            h = int(round((q_rect.height - 4) * oran))
            if h > 0:
                shade = pygame.Surface((q_rect.width - 4, h), pygame.SRCALPHA)
                shade.fill((0, 0, 0, 128))
                ekran.blit(shade, (q_rect.x + 2, q_rect.y + 2))
# </POTBO_STAGE S1666>

# <POTBO_STAGE S1671>


def _v81_death_player_drips():


    if oyuncu_olum_turu == "fire" or oyuncu_olum_baslangic_ms <= 0:
        return
    now = pygame.time.get_ticks()
    age = now - int(oyuncu_olum_baslangic_ms)
    if age < 620:
        return
    anchors = _v81_player_blood_anchors()
    for i, pos in enumerate(anchors[:2]):
        sx, sy = _v81_world_to_screen(pos)
        period = 1060 + i * 170
        phase = ((age + i * 370) % period) / float(period)
        y = sy + 3 + int(round((phase**1.75) * 17.0))
        x = sx + int(round(math.sin(phase * math.tau + i) * 1.2))
        pygame.draw.line(
            ekran,
            V77_DEATH_BLOOD,
            (sx, sy),
            (sx, min(y, sy + 6)),
            1,
        )
        pygame.draw.circle(
            ekran,
            V77_DEATH_BLOOD,
            (x, y),
            2 if phase < 0.46 else 1,
        )


def _v77_death_killer_draw(actor):
    if actor is None:
        return
    sil, rect = _v24_katil_siluet_surface_ve_rect(actor)
    if sil is not None and rect is not None:
        rect = rect.copy()
        rect.x = int(_v81_clamp(rect.x, 12, GENISLIK - rect.width - 12))
        rect.y = int(_v81_clamp(rect.y, 28, YUKSEKLIK - rect.height - 26))
        _v81_death_ground_anchor(rect, blood=True)
        mask = pygame.mask.from_surface(sil, 1)
        flat = mask.to_surface(
            setcolor=(*V77_DEATH_BODY, 255),
            unsetcolor=(0, 0, 0, 0),
        ).convert_alpha()
        ekran.blit(flat, rect)

    if oyuncu_olum_turu == "fire":
        return
    point = _v24_katil_silah_kan_noktasi(actor)
    if point is None:
        return
    sx = int(round(dunya_ekran_x(point.x)))
    sy = int(round(dunya_ekran_y(point.y)))
    now = pygame.time.get_ticks()
    direction = str(getattr(actor, "direction", "right"))
    sign = 1 if direction == "right" else -1


    pygame.draw.line(
        ekran,
        V77_DEATH_BLOOD,
        (sx - 5 * sign, sy),
        (sx + 6 * sign, sy + 2),
        2,
    )
    pygame.draw.circle(ekran, V77_DEATH_BLOOD, (sx + 3 * sign, sy + 2), 2)


    periods = (820, 1030, 1240, 1470)
    for i, period in enumerate(periods):
        p = ((now + i * 271) % period) / float(period)
        fall = 5.0 + 28.0 * (p**1.72)
        x = sx + int(round(math.sin(p * math.tau + i * 1.3) * (1.0 + i * 0.18)))
        y = sy + int(round(fall))
        tail = max(2, 5 - int(p * 4))
        pygame.draw.line(ekran, V77_DEATH_BLOOD, (x, y - tail), (x, y), 1)
        pygame.draw.circle(
            ekran,
            V77_DEATH_BLOOD,
            (x, y),
            2 if p < 0.44 and i < 2 else 1,
        )
        if i == 0 and p < 0.35:
            pygame.draw.circle(ekran, V77_DEATH_BODY, (x, y - 1), 1)
# </POTBO_STAGE S1671>

# <POTBO_STAGE S1680>





def oyun_ekrani_ciz():
    result = _v81_game_draw_original()
    if oyun_durumu == OYUN and oyuncu_hp > 0:
        _v82_hit_fx_draw()
        gelistirici_test_paneli_ciz()
        oyuncu_paneli_ciz()
        one_cikan_item_paneli_ciz()
    return result
# </POTBO_STAGE S1680>

# <POTBO_STAGE S1693>


def one_cikan_item_paneli_ciz():
    panel = hud_sag_rect()
    _v83_panel(panel, V83_UI_ACCENT, 244)
    slot_boyut = 68
    bosluk = 12
    grup_w = slot_boyut * 5 + bosluk * 4
    q_boyut = slot_boyut
    ayirici_bosluk = 30
    toplam = grup_w + ayirici_bosluk + q_boyut
    baslangic_x = panel.centerx - toplam // 2
    y = panel.y + 41

    for i in range(5):
        rect = pygame.Rect(
            baslangic_x + i * (slot_boyut + bosluk),
            y,
            slot_boyut,
            slot_boyut,
        )
        _v83_slot(
            rect,
            i + 1,
            item_index=one_cikan_slotlar[i],
            selected=(i == envanter_secili_slot),
            magic=False,
        )

    ayir_x = baslangic_x + grup_w + ayirici_bosluk // 2
    pygame.draw.line(
        ekran,
        (76, 60, 67),
        (ayir_x, y - 4),
        (ayir_x, y + slot_boyut + 4),
        1,
    )
    q_hizli_slot_normalize_et()
    qx = baslangic_x + grup_w + ayirici_bosluk
    q_rect = pygame.Rect(qx, y, q_boyut, q_boyut)
    q_item = q_hizli_item_index
    q_debug_spell = bool(gelistirici_sonsuz_ates)
    q_is_magic = q_debug_spell or (
        isinstance(q_item, int)
        and 0 <= q_item < len(envanter_itemleri)
        and item_buyu_mu(envanter_itemleri[q_item])
    )
    _v83_slot(
        q_rect,
        "Q",
        item_index=None,
        selected=False,
        magic=q_is_magic,
    )
    if q_debug_spell:
        item_ikonu_ciz("fire_magic", q_rect.inflate(-12, -12), False)
        spell_okulu_sembol_ciz(
            "IGNIS",
            pygame.Rect(q_rect.right - 23, q_rect.bottom - 23, 19, 19),
        )
        yazi_yaz(
            "∞",
            q_rect.centerx,
            q_rect.y + 12,
            (255, 238, 178),
            mini_font,
            True,
        )
    elif isinstance(q_item, int) and 0 <= q_item < len(envanter_itemleri):
        item = envanter_itemleri[q_item]
        if isinstance(item, dict):
            item_ikonu_ciz(item.get("id"), q_rect.inflate(-12, -12), False)
            if item.get("spell_school"):
                spell_okulu_sembol_ciz(
                    item.get("spell_school"),
                    pygame.Rect(
                        q_rect.right - 23,
                        q_rect.bottom - 23,
                        19,
                        19,
                    ),
                )
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
# </POTBO_STAGE S1693>

# <POTBO_STAGE S1695>


def kanli_darbe_efekti(x, y, profil="slash", lethal=False, yon=None):
    base = (
        pygame.Vector2(yon)
        if yon is not None
        else pygame.Vector2(
            random.uniform(-1.0, 1.0),
            random.uniform(-0.35, 0.35),
        )
    )
    if base.length_squared() <= 1e-6:
        base = pygame.Vector2(1.0, 0.0).rotate(random.uniform(-28.0, 28.0))
    base = base.normalize()
    _v83_kanli_darbe_efekti_original(x, y, profil, lethal, base)


    extra = random.randint(5, 8) if not lethal else random.randint(10, 16)
    kan_parcacigi_patlat(
        x + random.uniform(-1.5, 1.5),
        y + random.uniform(-2.0, 2.0),
        extra,
        0.82 if not lethal else 1.06,
        yon=base.rotate(random.uniform(-18.0, 18.0)),
        arterial=bool(lethal),
    )
    if not lethal:
        v73_ground_splatter(
            x,
            y + 1.0,
            base,
            random.randint(4, 7),
            scale_range=(0.14, 0.28),
            distance_range=(2.0, 18.0),
            cone_deg=84.0,
            backscatter=0.16,
            source="impact_followthrough",
        )
    else:
        v73_ground_splatter(
            x,
            y + 2.0,
            base,
            random.randint(10, 16),
            scale_range=(0.16, 0.48),
            distance_range=(4.0, 26.0),
            cone_deg=102.0,
            backscatter=0.24,
            source="lethal_followthrough",
        )
# </POTBO_STAGE S1695>

# <POTBO_STAGE S1703>


def _v77_death_killer_draw(actor):
    if actor is None:
        return
    sil, rect = _v24_katil_siluet_surface_ve_rect(actor)
    if sil is not None and rect is not None:
        rect = rect.copy()
        rect.x = int(_v83_clamp(rect.x, 12, GENISLIK - rect.width - 12))
        rect.y = int(_v83_clamp(rect.y, 28, YUKSEKLIK - rect.height - 26))
        mask = pygame.mask.from_surface(sil, 1)
        flat = mask.to_surface(
            setcolor=(*V77_DEATH_BODY, 255),
            unsetcolor=(0, 0, 0, 0),
        ).convert_alpha()
        ekran.blit(flat, rect)

    if oyuncu_olum_turu == "fire":
        return
    point = _v24_katil_silah_kan_noktasi(actor)
    if point is None:
        return
    sx = int(round(dunya_ekran_x(point.x)))
    sy = int(round(dunya_ekran_y(point.y)))
    now = pygame.time.get_ticks()
    direction = str(getattr(actor, "direction", "right"))
    sign = 1 if direction == "right" else -1
    pygame.draw.line(
        ekran,
        V77_DEATH_BLOOD,
        (sx - 5 * sign, sy),
        (sx + 6 * sign, sy + 2),
        2,
    )
    pygame.draw.circle(ekran, V77_DEATH_BLOOD, (sx + 3 * sign, sy + 2), 2)
    periods = (820, 1030, 1240, 1470)
    for i, period in enumerate(periods):
        p = ((now + i * 271) % period) / float(period)
        fall = 5.0 + 28.0 * (p**1.72)
        x = sx + int(round(math.sin(p * math.tau + i * 1.3) * (1.0 + i * 0.18)))
        y = sy + int(round(fall))
        tail = max(2, 5 - int(p * 4))
        pygame.draw.line(ekran, V77_DEATH_BLOOD, (x, y - tail), (x, y), 1)
        pygame.draw.circle(
            ekran,
            V77_DEATH_BLOOD,
            (x, y),
            2 if p < 0.44 and i < 2 else 1,
        )
# </POTBO_STAGE S1703>

# <POTBO_STAGE S1706>


def oyuncu_olum_sahnesi_ciz():
    ekran.fill(V77_DEATH_BLACK)
    _v77_death_blood_layer()
    _v77_death_gore_layer()

    killer = _v24_olum_katil_actor_bul()
    killer_behind = killer is not None and float(
        getattr(killer, "y", oyuncu_y)
    ) <= float(oyuncu_y)
    if killer_behind:
        _v77_death_killer_draw(killer)

    _v83_death_victim_layer()
    _v83_death_continuous_artery()
    _v81_death_player_drips()
    _v77_death_fire_layer()

    if killer is not None and not killer_behind:
        _v77_death_killer_draw(killer)

    if oyuncu_olum_baslangic_ms <= 0:
        return
    now = pygame.time.get_ticks()
    title_p = oyuncu_olum_baslik_fade_orani(now)
    _v34_gameover_music_tick(title_p, now)
    if oyuncu_olum_cikis_orani(now) > 0.0:
        ekran.fill(V77_DEATH_BLACK)
        return
    _v77_death_menu_draw(now)
# </POTBO_STAGE S1706>

# <POTBO_STAGE S1708>


def oyun_ekrani_ciz():
    result = _v83_game_draw_original()
    if oyun_durumu == OYUN and oyuncu_hp > 0:
        oyuncu_paneli_ciz()
        one_cikan_item_paneli_ciz()
        gelistirici_test_paneli_ciz()
    return result
# </POTBO_STAGE S1708>

# <POTBO_STAGE S1713>
V84_BLOOD_HOT = (151, 2, 25)
# </POTBO_STAGE S1713>

# <POTBO_STAGE S1720>
V84_EXECUTION_FINAL_GORE_MIN = 24
V84_EXECUTION_FINAL_GORE_MAX = 34
# </POTBO_STAGE S1720>

# <POTBO_STAGE S1771>


def v84_execution_cut_blood(target, index, angle, final=False):
    direction = pygame.Vector2(1.0, 0.0).rotate(float(angle))
    rng = random.Random(int(v84_execution_state.seed) + int(index) * 911)
    count = rng.randint(16, 24) if final else rng.randint(5, 10) + min(5, index // 2)
    power = rng.uniform(1.34, 1.58) if final else rng.uniform(0.70, 1.04)
    kan_parcacigi_patlat(
        float(target.x) + rng.uniform(-2.0, 2.0),
        float(target.y) - rng.uniform(7.0, 15.0),
        count,
        power,
        yon=direction,
        arterial=bool(final or index >= 8),
    )
    if "v73_ground_splatter" in globals():
        v73_ground_splatter(
            float(target.x),
            float(target.y) + 1.0,
            direction,
            rng.randint(4, 7) if not final else rng.randint(13, 18),
            scale_range=(0.13, 0.31) if not final else (0.18, 0.52),
            distance_range=(2.0, 19.0) if not final else (5.0, 35.0),
            cone_deg=72.0 if not final else 112.0,
            backscatter=0.12 if not final else 0.25,
            source="execution_cut_final" if final else "execution_cut",
        )
# </POTBO_STAGE S1771>

# <POTBO_STAGE S1773>


def v84_execution_spawn_final_gore(target, direction):
    gore_olum_patlamasi(
        float(target.x),
        float(target.y) - 8.0,
        "heavy_slash",
        yon=direction,
    )
    available = [
        key
        for key in (
            "intestine",
            "liver",
            "organ_mass_a",
            "organ_mass_b",
            "organ_round_a",
            "organ_round_b",
            "flesh_shard_a",
            "flesh_shard_b",
            "ribcage",
            "spinal_cord",
            "skull",
            "leg",
            "foot",
            "bone_long_a",
            "bone_long_b",
        )
        if key in GORE_SPRITELERI
    ]
    if not available:
        available = ["liver", "intestine"]
    rng = random.Random(v84_execution_state.seed ^ 0xF1A1)
    count = rng.randint(
        V84_EXECUTION_FINAL_GORE_MIN,
        V84_EXECUTION_FINAL_GORE_MAX,
    )
    base = v84_safe_vector(direction).normalize()
    for index in range(count):
        kind = available[index % len(available)]
        chunk = GoreChunk(
            kind,
            float(target.x),
            float(target.y) - rng.uniform(4.0, 13.0),
            guc=rng.uniform(0.92, 1.34),
            small=index >= 7,
        )
        vector = base.rotate(rng.uniform(-112.0, 112.0))
        if index % 7 == 0:
            vector *= -1.0
        vector = v84_safe_vector(vector).normalize()
        chunk.v = vector * rng.uniform(128.0, 345.0)
        chunk.vz = rng.uniform(118.0, 318.0)
        chunk.angular = rng.uniform(-780.0, 780.0)
        setattr(chunk, "v84_execution_chunk", True)
        gore_chunks.append(chunk)


def v84_execution_finalize(now, final_trace):
    global v84_execution_finishes
    state = v84_execution_state
    if state.final_applied or state.target is None:
        return
    target = state.target
    direction = pygame.Vector2(1.0, 0.0).rotate(final_trace.angle)
    state.final_applied = True
    target.hp = 0
    target.active = False
    target.attacking = False
    target.vx = 0.0
    target.vy = 0.0
    if hasattr(target, "dash_kind"):
        target.dash_kind = None
    if hasattr(target, "dash_until"):
        target.dash_until = 0
    if state.fracture is not None:
        state.fracture.release(
            impulse=direction,
            power=1.18,
            seed=state.seed,
        )
    v84_execution_spawn_final_gore(target, direction)
    v45_bleed_state.pop(v84_actor_uid(target), None)
    v84_poise_break_windows.pop(v84_actor_uid(target), None)
    v84_execution_windows.pop(v84_actor_uid(target), None)
    v84_execution_finishes += 1
    dunya_olayi_kaydet(
        "execution_finish",
        enemy=str(getattr(target, "tur", "enemy")),
        cuts=int(state.cuts_landed),
        fragments=len(state.fracture.fragments) if state.fracture else 0,
    )
    bildirim_goster(
        bt(
            f"{getattr(target, 'name', 'Hedef')} infaz edildi.",
            f"{getattr(target, 'name', 'Target')} was executed.",
        ),
        PARLAK_KIRMIZI,
    )
# </POTBO_STAGE S1773>

# <POTBO_STAGE S1787>


def v84_wound_emit(wound, now):
    actor = wound.actor
    if actor is None:
        return
    pressure = v84_clamp01(wound.pressure)
    count = max(2, int(round(2.0 + pressure * 6.0)))
    power = 0.46 + pressure * 0.62
    direction = v84_safe_vector(wound.direction).rotate(random.uniform(-15.0, 15.0))
    vertical = {
        "neck": 17.0,
        "gorget_gap": 18.0,
        "shoulder": 22.0,
        "pauldron_gap": 23.0,
        "chest": 17.0,
        "thorax": 14.0,
        "abdomen": 9.0,
        "armpit": 15.0,
        "arm": 14.0,
        "inner_elbow": 12.0,
        "thigh": 6.0,
        "hamstring": 5.0,
        "knee_gap": 4.0,
    }.get(wound.body_zone, 10.0)
    kan_parcacigi_patlat(
        float(actor.x) + random.uniform(-2.0, 2.0),
        float(actor.y) - vertical,
        count,
        power,
        yon=direction,
        arterial=pressure >= 0.72,
    )
    wound.emitted += count
    interval = int(820 - pressure * 470)
    wound.next_emit_ms = int(now) + random.randint(
        max(210, interval - 80),
        max(250, interval + 100),
    )
    wound.pressure *= 0.83
# </POTBO_STAGE S1787>

# <POTBO_STAGE S1805>


def v84_death_rivulets_draw(now):
    state = v84_death_state
    if not state.built or str(oyuncu_olum_turu) == "fire":
        return
    age = max(0, int(now) - int(state.created_ms))
    grow = v84_smootherstep(min(1.0, age / 2100.0))
    dry = 1.0 - v84_smoothstep(max(0.0, age - 9000.0) / 36000.0)
    rng = random.Random(state.seed ^ 0xD34D)
    origin = pygame.Vector2(
        float(oyuncu_x),
        float(oyuncu_y) + 2.0,
    )
    branch_count = 11 if state.profile == "heavy_slash" else 8
    if str(oyuncu_olum_turu) in ("blast_core", "blast_inner"):
        branch_count += 5
    for index in range(branch_count):
        angle = rng.uniform(-172.0, 172.0)
        if index < 3:
            angle = state.direction.as_polar()[1] + rng.uniform(-36.0, 36.0)
        direction = pygame.Vector2(1.0, 0.0).rotate(angle)
        length = rng.uniform(22.0, 92.0) * grow
        width = 1 + int(rng.random() < 0.40 and dry > 0.3)
        points = []
        normal = direction.rotate(90.0)
        bends = (
            rng.uniform(-6.0, 6.0),
            rng.uniform(-11.0, 11.0),
            rng.uniform(-8.0, 8.0),
        )
        segments = 6
        for step in range(segments + 1):
            t = step / float(segments)
            lateral = (
                math.sin(t * math.pi) * bends[0]
                + math.sin(t * math.pi * 2.0) * bends[1] * 0.35
                + t * bends[2] * 0.24
            )
            point = origin + direction * (length * t) + normal * lateral
            points.append(
                (
                    int(dunya_ekran_x(point.x)),
                    int(dunya_ekran_y(point.y)),
                )
            )
        if len(points) >= 2:
            pygame.draw.lines(
                ekran,
                V84_BLOOD,
                False,
                points,
                width + (1 if index < 2 else 0),
            )
        terminal = points[-1]
        shard = max(2, int(round(rng.uniform(2.0, 5.0) * grow)))
        pygame.draw.polygon(
            ekran,
            V84_BLOOD,
            (
                (terminal[0], terminal[1] - shard),
                (terminal[0] + shard * 2, terminal[1]),
                (terminal[0], terminal[1] + max(1, shard // 2)),
                (terminal[0] - shard, terminal[1]),
            ),
        )
# </POTBO_STAGE S1805>

# <POTBO_STAGE S1807>


def oyuncu_olum_sahnesi_ciz():
    ekran.fill(V84_BLACK)
    _v77_death_blood_layer()
    v84_death_rivulets_draw(pygame.time.get_ticks())
    _v77_death_gore_layer()

    killer = _v24_olum_katil_actor_bul()
    killer_behind = killer is not None and float(
        getattr(killer, "y", oyuncu_y)
    ) <= float(oyuncu_y)
    if killer_behind:
        _v77_death_killer_draw(killer)

    now = pygame.time.get_ticks()
    v84_death_victim_draw(now)
    v84_death_arterial_draw(now)
    _v83_death_continuous_artery()
    _v81_death_player_drips()
    _v77_death_fire_layer()

    if killer is not None and not killer_behind:
        _v77_death_killer_draw(killer)

    if oyuncu_olum_baslangic_ms <= 0:
        return
    title_progress = oyuncu_olum_baslik_fade_orani(now)
    _v34_gameover_music_tick(title_progress, now)
    if oyuncu_olum_cikis_orani(now) > 0.0:
        ekran.fill(V84_BLACK)
        return
    _v77_death_menu_draw(now)
# </POTBO_STAGE S1807>

# <POTBO_STAGE S1810>


def v84_execution_tableau_draw():
    state = v84_execution_state
    if not state.active:
        return
    ekran.fill(V84_BLACK)
    kan_lekelerini_ciz(silhouette=True)
    for chunk in sorted(gore_chunks, key=lambda item: item.y):
        chunk.ciz(silhouette=True)
    for particle in blood_particles:
        if getattr(particle, "active", False):
            particle.ciz(silhouette=True)

    target = state.target
    if target is not None and state.fracture is not None:
        anchor = (
            int(round(dunya_ekran_x(float(target.x)))),
            int(round(dunya_ekran_y(float(target.y)) + 2)),
        )
        state.fracture.draw(anchor)

    player = v84_player_silhouette()
    if player is not None:
        player_rect = player.get_rect(
            midbottom=(
                int(round(dunya_ekran_x(oyuncu_x))),
                int(round(dunya_ekran_y(oyuncu_y))),
            )
        )
        ekran.blit(player, player_rect)

    now = pygame.time.get_ticks()
    for trace in state.slashes:
        v84_execution_trace_draw(trace, now)
    v84_execution_threats_draw()



    total = V84_EXECUTION_BEAT_TIMES[-1] + V84_EXECUTION_END_LINGER_MS
    remaining = 1.0 - v84_clamp01(state.elapsed_ms / float(total))
    bar = pygame.Rect(GENISLIK // 2 - 132, 54, 264, 4)
    pygame.draw.rect(ekran, V84_BLOOD, bar)
    fill = pygame.Rect(
        bar.x,
        bar.y,
        int(round(bar.width * remaining)),
        bar.height,
    )
    if fill.width > 0:
        pygame.draw.rect(ekran, V84_BODY, fill)
    pygame.draw.line(
        ekran,
        V84_BODY,
        (bar.left - 14, bar.centery),
        (bar.left - 2, bar.centery),
        1,
    )
    pygame.draw.line(
        ekran,
        V84_BODY,
        (bar.right + 2, bar.centery),
        (bar.right + 14, bar.centery),
        1,
    )
# </POTBO_STAGE S1810>

# <POTBO_STAGE S1814>


def oyun_ekrani_ciz():
    result = _v84_game_draw_original()
    if v84_execution_state.active:
        v84_execution_tableau_draw()
        return result
    if oyun_durumu == OYUN and oyuncu_hp > 0:
        oyuncu_paneli_ciz()
        one_cikan_item_paneli_ciz()
        v84_combat_ui_draw()
        gelistirici_test_paneli_ciz()
    return result
# </POTBO_STAGE S1814>

# <POTBO_STAGE S1819>


def v84_palette_contract():
    palette = {
        V84_BLACK,
        V84_BLOOD,
        V84_BODY,
    }
    return {
        "three_core_colors": len(palette) == 3,
        "black_is_black": V84_BLACK == (0, 0, 0),
        "blood_darker_than_body": sum(V84_BLOOD) < sum(V84_BODY),
        "core_palette": tuple(sorted(palette)),
    }
# </POTBO_STAGE S1819>

# <POTBO_STAGE S1823>
V84_STARTUP_OK = all(
    (
        V84_STARTUP_CONTRACT["timing"]["strict_guard_in_range"],
        V84_STARTUP_CONTRACT["timing"]["standard_guard_in_range"],
        V84_STARTUP_CONTRACT["timing"]["riposte_window_in_range"],
        V84_STARTUP_CONTRACT["timing"]["execution_beats_monotonic"],
        V84_STARTUP_CONTRACT["timing"]["execution_accelerates"],
        V84_STARTUP_CONTRACT["palette"]["three_core_colors"],
        V84_STARTUP_CONTRACT["palette"]["blood_darker_than_body"],
    )
)














V85_VERSION = "85.0"
# </POTBO_STAGE S1823>

# <POTBO_STAGE S1831>


def v85_execution_cut_tissue(target, index, angle):
    keys = [
        key
        for key in (
            "flesh_shard_a",
            "flesh_shard_b",
            "organ_mass_a",
            "organ_round_a",
        )
        if key in GORE_SPRITELERI
    ]
    if not keys:
        keys = (
            "flesh_shard_a",
            "flesh_shard_b",
            "organ_mass_a",
            "organ_round_a",
        )
    rng = random.Random(v84_execution_state.seed ^ (index * 0xA511))
    chunk = GoreChunk(
        keys[index % len(keys)],
        float(target.x),
        float(target.y) - rng.uniform(7.0, 15.0),
        guc=rng.uniform(0.48, 0.78),
        small=True,
    )
    direction = pygame.Vector2(1.0, 0.0).rotate(angle + rng.uniform(64.0, 116.0))
    chunk.v = direction * rng.uniform(54.0, 132.0)
    chunk.vz = rng.uniform(48.0, 128.0)
    chunk.angular = rng.uniform(-420.0, 420.0)
    gore_chunks.append(chunk)
# </POTBO_STAGE S1831>

# <POTBO_STAGE S1836>


def v84_execution_tableau_draw():
    state = v84_execution_state
    if not state.active:
        return
    ekran.fill(V84_BLACK)


    kan_lekelerini_ciz(silhouette=True)
    for particle in blood_particles:
        if getattr(particle, "active", False):
            particle.ciz(silhouette=True)
    for chunk in sorted(gore_chunks, key=lambda item: item.y):
        chunk.ciz(silhouette=True)

    target = state.target
    if target is not None and state.fracture is not None:
        anchor = (
            int(round(dunya_ekran_x(float(target.x)))),
            int(round(dunya_ekran_y(float(target.y)) + 2)),
        )
        state.fracture.draw(anchor)

    now = pygame.time.get_ticks()
    v85_execution_motion_draw(now)
    player = v84_player_silhouette()
    if player is not None:
        player_rect = player.get_rect(
            midbottom=(
                int(round(dunya_ekran_x(oyuncu_x))),
                int(round(dunya_ekran_y(oyuncu_y))),
            )
        )
        ekran.blit(player, player_rect)

    for trace in state.slashes:
        v84_execution_trace_draw(trace, now)
    v84_execution_threats_draw()

    remaining = 1.0 - v84_clamp01(state.elapsed_ms / float(V85_EXECUTION_TOTAL_MS))
    bar = pygame.Rect(GENISLIK // 2 - 146, 52, 292, 5)
    pygame.draw.rect(ekran, V84_BLACK, bar.inflate(4, 4))
    pygame.draw.rect(ekran, V84_BLOOD, bar)
    fill = pygame.Rect(
        bar.x,
        bar.y,
        int(round(bar.width * remaining)),
        bar.height,
    )
    if fill.width > 0:
        pygame.draw.rect(ekran, V84_BODY, fill)
    pygame.draw.rect(ekran, V84_BODY, bar.inflate(2, 2), 1)

    if int(now) < int(v85_execution_flash_until_ms):
        duration = max(
            1,
            v85_execution_flash_until_ms - v85_execution_flash_started_ms,
        )
        p = v84_clamp01((int(now) - v85_execution_flash_started_ms) / duration)
        alpha = int(118 * (1.0 - p) ** 2)
        flash = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
        flash.fill((*V84_BODY_HOT, alpha))
        ekran.blit(flash, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)
# </POTBO_STAGE S1836>

# <POTBO_STAGE S1840>




V44_PLAYER_DEATH_ARTERIAL_DURATION_MS = V85_DEATH_ARTERIAL_MS
# </POTBO_STAGE S1840>

# <POTBO_STAGE S1842>
V44_BLOOD_PULSE_INTERVAL = (112, 176)
# </POTBO_STAGE S1842>

# <POTBO_STAGE S1858>


def v85_death_tissue_spawn(state):
    if state.tissue_spawned > 0 or state.variant == "fire":
        return
    keys = [
        key
        for key in (
            "flesh_shard_a",
            "flesh_shard_b",
            "organ_mass_a",
            "organ_mass_b",
            "organ_round_a",
            "organ_round_b",
            "intestine",
            "liver",
            "ribcage",
            "skull",
        )
        if key in GORE_SPRITELERI
    ]
    if not keys:


        keys = [
            "flesh_shard_a",
            "flesh_shard_b",
            "organ_mass_a",
            "organ_mass_b",
            "organ_round_a",
            "organ_round_b",
            "intestine",
            "liver",
            "ribcage",
            "skull",
        ]
    ranges = {
        "minor": (2, 5),
        "decap": (5, 9),
        "bisect": (8, 14),
        "torso": (9, 16),
        "shatter": (18, 27),
    }
    low, high = ranges.get(state.variant, (2, 5))
    rng = random.Random(state.seed ^ 0x71A585)
    count = rng.randint(low, high)
    base = v84_safe_vector(state.direction).normalize()
    for index in range(count):
        kind = keys[index % len(keys)]
        chunk = GoreChunk(
            kind,
            float(oyuncu_x) + rng.uniform(-4.0, 4.0),
            float(oyuncu_y) - rng.uniform(6.0, 17.0),
            guc=rng.uniform(0.62, 1.10 if state.variant == "minor" else 1.34),
            small=(state.variant == "minor" or index >= 6),
        )
        direction = base.rotate(rng.uniform(-118.0, 118.0))
        chunk.v = direction * rng.uniform(
            62.0, 214.0 if state.variant == "minor" else 338.0
        )
        chunk.vz = rng.uniform(62.0, 166.0 if state.variant == "minor" else 286.0)
        chunk.angular = rng.uniform(-620.0, 620.0)
        gore_chunks.append(chunk)
    state.tissue_spawned = count


_v85_gore_chunk_draw_original = GoreChunk.ciz
# </POTBO_STAGE S1858>

# <POTBO_STAGE S1860>


def _v85_gore_chunk_draw(self, silhouette=False):
    if GORE_SPRITELERI.get(self.kind) is not None:
        return _v85_gore_chunk_draw_original(self, silhouette)
    sx = float(dunya_ekran_x(self.x))
    ground_y = float(dunya_ekran_y(self.y))
    sy = ground_y - float(self.z) * KAMERA_YAKINLASTIRMA
    if sx < -100 or sx > GENISLIK + 100 or sy < -100 or sy > YUKSEKLIK + 100:
        return

    tissue = self.kind not in (
        "ribcage",
        "spinal_cord",
        "skull",
        "leg",
        "foot",
        "bone_long_a",
        "bone_long_b",
        "bone_cluster_a",
        "bone_cluster_b",
    )
    scale = max(0.46, min(1.32, float(self.scale))) * KAMERA_YAKINLASTIRMA
    center = (sx, sy)
    if self.z > 1.0:
        shadow = v85_local_shape_points(
            (sx, ground_y),
            ((-5.0, 0.0), (0.0, -1.8), (5.0, 0.0), (0.0, 1.8)),
            0.0,
            scale,
        )
        pygame.draw.polygon(ekran, (1, 1, 2), shadow)

    if self.kind == "intestine":
        vertices = (
            (-7.0, 1.0),
            (-4.0, -3.0),
            (0.0, 2.0),
            (4.0, -2.0),
            (7.0, 1.0),
        )
        points = v85_local_shape_points(center, vertices, self.rotation, scale)
        pygame.draw.lines(
            ekran,
            V84_BLOOD_HOT if silhouette else (139, 19, 39),
            False,
            points,
            max(2, int(round(3.0 * scale))),
        )
        pygame.draw.lines(
            ekran,
            V84_BODY_HOT if silhouette else (206, 61, 73),
            False,
            points[1:-1],
            1,
        )
        return

    if self.kind in (
        "bone_long_a",
        "bone_long_b",
        "spinal_cord",
        "leg",
    ):
        vertices = (
            (-8.0, -2.0),
            (6.0, -2.0),
            (9.0, 0.0),
            (6.0, 2.0),
            (-8.0, 2.0),
            (-10.0, 0.0),
        )
    elif self.kind in (
        "ribcage",
        "bone_cluster_a",
        "bone_cluster_b",
    ):
        vertices = (
            (-6.0, -4.0),
            (1.0, -5.0),
            (7.0, -1.0),
            (5.0, 4.0),
            (-2.0, 5.0),
            (-7.0, 1.0),
        )
    elif self.kind == "skull":
        vertices = (
            (-5.0, -5.0),
            (3.0, -5.0),
            (6.0, -1.0),
            (4.0, 5.0),
            (0.0, 3.0),
            (-5.0, 5.0),
            (-7.0, 0.0),
        )
    elif self.kind.startswith("flesh_shard"):
        vertices = (
            (-7.0, -1.0),
            (-2.0, -5.0),
            (6.0, -2.0),
            (4.0, 4.0),
            (-3.0, 5.0),
        )
    else:
        vertices = (
            (-6.0, -3.0),
            (-1.0, -6.0),
            (6.0, -3.0),
            (7.0, 2.0),
            (2.0, 6.0),
            (-5.0, 4.0),
            (-8.0, 0.0),
        )

    points = v85_local_shape_points(center, vertices, self.rotation, scale)
    if tissue:
        outer = V84_BLOOD if silhouette else (91, 3, 17)
        fill = V84_BODY_HOT if silhouette else (153, 20, 38)
        highlight = V84_BLOOD_HOT if silhouette else (211, 47, 59)
    else:
        outer = V84_BLOOD if silhouette else (67, 20, 25)
        fill = V84_BODY if silhouette else (174, 151, 136)
        highlight = V84_BODY_HOT if silhouette else (220, 199, 180)
    pygame.draw.polygon(ekran, outer, points)
    inset_scale = scale * 0.72
    inset = v85_local_shape_points(center, vertices, self.rotation, inset_scale)
    pygame.draw.polygon(ekran, fill, inset)
    if len(inset) >= 4:
        pygame.draw.line(ekran, highlight, inset[1], inset[2], 1)


GoreChunk.ciz = _v85_gore_chunk_draw
# </POTBO_STAGE S1860>

# <POTBO_STAGE S1869>


def oyuncu_olum_sahnesi_ciz():
    ekran.fill(V84_BLACK)



    kan_lekelerini_ciz(silhouette=True)
    for particle in blood_particles:
        if getattr(particle, "active", False):
            particle.ciz(silhouette=True)
    now = pygame.time.get_ticks()
    v85_death_ground_flows_draw(now)
    for chunk in sorted(gore_chunks, key=lambda item: item.y):
        chunk.ciz(silhouette=True)

    killer = _v24_olum_katil_actor_bul()
    killer_behind = killer is not None and float(
        getattr(killer, "y", oyuncu_y)
    ) <= float(oyuncu_y)
    if killer_behind:
        _v77_death_killer_draw(killer)

    v85_death_victim_draw(now)
    v85_death_arterial_core_draw(now)
    _v81_death_player_drips()
    _v77_death_fire_layer()

    if killer is not None and not killer_behind:
        _v77_death_killer_draw(killer)
    if oyuncu_olum_baslangic_ms <= 0:
        return

    title_progress = oyuncu_olum_baslik_fade_orani(now)
    _v34_gameover_music_tick(title_progress, now)
    v85_death_menu_draw(now)
    exit_progress = oyuncu_olum_cikis_orani(now)
    if exit_progress > 0.0:
        veil = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
        veil.fill((0, 0, 0, int(round(255 * exit_progress))))
        ekran.blit(veil, (0, 0))
# </POTBO_STAGE S1869>

# <POTBO_STAGE S1887>


def one_cikan_item_paneli_ciz():
    panel = hud_sag_rect()
    v85_hud_panel_draw(panel, V85_HUD_SELECTED)
    slot_size = 68
    gap = 12
    group_width = slot_size * 5 + gap * 4
    separator_gap = 30
    total = group_width + separator_gap + slot_size
    start_x = panel.centerx - total // 2
    y = panel.y + 41
    for index in range(5):
        rect = pygame.Rect(
            start_x + index * (slot_size + gap),
            y,
            slot_size,
            slot_size,
        )
        selected = index == envanter_secili_slot
        v85_slot_shell(rect, selected=selected)
        v85_slot_contents(rect, index + 1, one_cikan_slotlar[index])

    separator_x = start_x + group_width + separator_gap // 2
    pygame.draw.line(
        ekran,
        V85_HUD_EDGE,
        (separator_x, y - 5),
        (separator_x, y + slot_size + 5),
        1,
    )
    q_hizli_slot_normalize_et()
    q_rect = pygame.Rect(
        start_x + group_width + separator_gap,
        y,
        slot_size,
        slot_size,
    )
    q_item = q_hizli_item_index
    q_debug = bool(gelistirici_sonsuz_ates)
    q_magic = q_debug or (
        isinstance(q_item, int)
        and 0 <= q_item < len(envanter_itemleri)
        and item_buyu_mu(envanter_itemleri[q_item])
    )
    v85_slot_shell(q_rect, magic=q_magic)
    v85_slot_contents(q_rect, "Q", None if q_debug else q_item)
    if q_debug:
        item_ikonu_ciz("fire_magic", q_rect.inflate(-12, -12), False)
        spell_okulu_sembol_ciz(
            "IGNIS",
            pygame.Rect(q_rect.right - 23, q_rect.bottom - 23, 19, 19),
        )
        yazi_yaz(
            "∞",
            q_rect.centerx,
            q_rect.y + 12,
            (255, 238, 178),
            mini_font,
            True,
        )
    elif isinstance(q_item, int) and 0 <= q_item < len(envanter_itemleri):
        item = envanter_itemleri[q_item]
        if isinstance(item, dict) and item.get("spell_school"):
            spell_okulu_sembol_ciz(
                item.get("spell_school"),
                pygame.Rect(
                    q_rect.right - 23,
                    q_rect.bottom - 23,
                    19,
                    19,
                ),
            )
    if q_magic and not q_debug:
        remaining = max(
            0,
            FIRE_MAGIC_COOLDOWN_MS
            - (pygame.time.get_ticks() - fire_magic_son_kullanim),
        )
        if remaining > 0:
            ratio = v84_clamp01(remaining / max(1.0, FIRE_MAGIC_COOLDOWN_MS))
            height = int(round((q_rect.height - 4) * ratio))
            if height > 0:
                shade = pygame.Surface((q_rect.width - 4, height), pygame.SRCALPHA)
                shade.fill((0, 0, 0, 138))
                ekran.blit(
                    shade,
                    (q_rect.x + 2, q_rect.bottom - 2 - height),
                )
# </POTBO_STAGE S1887>

# <POTBO_STAGE S1898>


def v84_execution_tableau_draw():
    state = v84_execution_state
    if not state.active:
        return
    ekran.fill(V84_BLACK)
    kan_lekelerini_ciz(silhouette=True)
    for particle in blood_particles:
        if getattr(particle, "active", False):
            particle.ciz(silhouette=True)
    for chunk in sorted(gore_chunks, key=lambda item: item.y):
        chunk.ciz(silhouette=True)

    target = state.target
    if target is not None and state.fracture is not None:
        anchor = (
            int(round(dunya_ekran_x(float(target.x)))),
            int(round(dunya_ekran_y(float(target.y)) + 2)),
        )
        state.fracture.draw(anchor)

    now = pygame.time.get_ticks()
    v85_execution_motion_draw(now)
    player = v84_player_silhouette()
    if player is not None:
        player_rect = player.get_rect(
            midbottom=(
                int(round(dunya_ekran_x(oyuncu_x))),
                int(round(dunya_ekran_y(oyuncu_y))),
            )
        )
        ekran.blit(player, player_rect)

    for trace in state.slashes:
        v84_execution_trace_draw(trace, now)
    v84_execution_threats_draw()


    if int(now) < int(v85_execution_flash_until_ms):
        duration = max(
            1,
            v85_execution_flash_until_ms - v85_execution_flash_started_ms,
        )
        p = v84_clamp01((int(now) - v85_execution_flash_started_ms) / duration)
        alpha = int(118 * (1.0 - p) ** 2)
        flash = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
        flash.fill((*V84_BODY_HOT, alpha))
        ekran.blit(flash, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)
# </POTBO_STAGE S1898>

# <POTBO_STAGE S1912>


def v86_spawn_gore_chunks(state, direction, count, power, head=False):
    keys = [
        key
        for key in (
            "organ_round_a" if head else "organ_mass_a",
            "organ_round_b" if head else "organ_mass_b",
            "flesh_shard_a",
            "flesh_shard_b",
            "intestine",
            "liver",
            "skull" if head else "ribcage",
        )
        if key in GORE_SPRITELERI
    ]
    if not keys:
        keys = [
            "organ_round_a",
            "organ_mass_a",
            "flesh_shard_a",
            "flesh_shard_b",
            "intestine",
            "liver",
        ]
    rng = random.Random(state.seed ^ len(gore_chunks) * 0x86F1)
    base = v84_safe_vector(direction).normalize()
    for index in range(max(0, int(count))):
        chunk = GoreChunk(
            keys[index % len(keys)],
            float(state.body_anchor.x) + rng.uniform(-4.0, 4.0),
            float(state.body_anchor.y)
            - (rng.uniform(19.0, 29.0) if head else rng.uniform(7.0, 18.0)),
            guc=rng.uniform(0.70, 1.28) * float(power),
            small=index >= max(3, count // 3),
        )
        heading = base.rotate(rng.uniform(-106.0, 106.0))
        chunk.v = heading * rng.uniform(72.0, 260.0) * float(power)
        chunk.vz = rng.uniform(74.0, 246.0) * float(power)
        chunk.angular = rng.uniform(-690.0, 690.0)
        gore_chunks.append(chunk)


def v86_blood_event(
    state,
    direction,
    severity,
    zone="torso",
    tag=0,
    organs=1,
    arterial=False,
):
    direction = v84_safe_vector(direction).normalize()
    severity = max(0.45, float(severity) * state.intensity)
    y_offset = {
        "head": -26.0,
        "neck": -23.0,
        "torso": -13.0,
        "waist": -7.0,
        "legs": -2.0,
    }.get(str(zone), -12.0)
    origin = pygame.Vector2(
        float(state.body_anchor.x), float(state.body_anchor.y) + y_offset
    )
    particle_count = int(round(12 + 13 * severity))
    kan_parcacigi_patlat(
        origin.x,
        origin.y,
        particle_count,
        min(2.65, 0.70 + severity * 0.52),
        yon=direction.rotate(random.uniform(-13.0, 13.0)),
        arterial=bool(arterial),
    )
    analytic_count = min(34, int(round(8 + 10 * severity)))
    _v81_add_burst(
        origin,
        direction,
        analytic_count,
        intensity=min(2.1, 0.68 + severity * 0.42),
        spread_deg=42.0 + min(30.0, severity * 8.0),
        height=15.0 + severity * 5.0,
        distance_mul=0.86 + severity * 0.12,
        seep=True,
        tag=8600 + int(tag),
    )
    if arterial:
        _v81_add_arterial_sequence(
            origin,
            direction.rotate(random.uniform(-9.0, 9.0)),
            intensity=min(1.55, 0.66 + severity * 0.26),
            start_delay=0,
            height=19.0 + severity * 4.0,
            tag=8700 + int(tag),
        )
    if "v73_ground_splatter" in globals():
        v73_ground_splatter(
            origin.x,
            state.body_anchor.y + 1.0,
            direction,
            min(22, int(round(6 + severity * 5))),
            scale_range=(0.18, min(0.82, 0.34 + severity * 0.13)),
            distance_range=(2.0, min(68.0, 22.0 + severity * 14.0)),
            cone_deg=132.0,
            backscatter=0.32,
            source="v86_authored_death",
        )
    if organs > 0:
        v86_spawn_gore_chunks(
            state,
            direction,
            max(1, int(round(organs * min(2.2, state.intensity)))),
            min(1.45, 0.58 + severity * 0.20),
            head=zone in ("head", "neck"),
        )
# </POTBO_STAGE S1912>

# <POTBO_STAGE S1920>


def v86_death_scene_begin(killer, source_x, source_y, profile, damage, source_name):
    global oyuncu_hp, hp_gorunen
    global oyuncu_olum_baslangic_ms, oyuncu_olum_arter_sonraki_ms
    global oyuncu_olum_gore_uretildi, oyuncu_olum_turu
    global oyuncu_olum_alt_turu, oyuncu_olum_koreografi_seed
    global oyuncu_olum_patlama_seed, oyuncu_olum_patlama_yonu
    global oyuncu_olum_ates_seed
    global oyuncu_olum_katil_uid, oyuncu_olum_katil_tur
    global oyuncu_olum_katil_kan_sonraki_ms
    global oyuncu_hareket_ediyor, dash_aktif_bitis
    global dash_aktif_yonu, dash_aktif_son_ease, dash_tus_kilitli
    global oyuncu_zorlanmis_bitis
    global v81_death_blood, v73_player_blast_fragmented
    now = max(1, int(pygame.time.get_ticks()))
    state = v86_death_state
    state.reset()
    state.active = True
    state.started_ms = now
    state.last_tick_ms = now
    state.seed = random.randint(1, 2_000_000)
    state.killer = killer
    state.killer_uid = v84_actor_uid(killer)
    state.killer_type = str(getattr(killer, "tur", ""))
    state.profile = str(profile or "slash")
    state.source_name = str(source_name or "")
    state.source_position = pygame.Vector2(float(source_x), float(source_y))
    state.damage = max(1, int(damage))
    ratio = state.damage / max(1.0, float(oyuncu_max_hp))
    state.intensity = v84_clamp(0.82 + ratio * 1.55, 0.88, 2.20)
    state.one_shot = v86_was_one_shot(killer, now)
    state.death_kind = v86_death_kind(profile, source_name, killer)
    state.body_anchor = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    state.fall_target_rotation = -90.0 if float(source_x) <= float(oyuncu_x) else 90.0
    state.shockwave = any(
        token in str(source_name or "").lower()
        for token in ("shock", "wave", "explosion")
    )
    v86_initialize_body(state)

    oyuncu_hp = 0
    hp_gorunen = 0.0
    oyuncu_olum_baslangic_ms = now
    oyuncu_olum_arter_sonraki_ms = 2**31 - 1
    oyuncu_olum_gore_uretildi = True
    oyuncu_olum_koreografi_seed = state.seed
    oyuncu_olum_katil_uid = str(getattr(killer, "uid", "")) if killer else ""
    oyuncu_olum_katil_tur = state.killer_type
    oyuncu_olum_katil_kan_sonraki_ms = 0

    if state.death_kind == "fire":
        oyuncu_olum_turu = "fire"
        oyuncu_olum_alt_turu = "fire"
        oyuncu_olum_ates_seed = state.seed
        state.burning_root = True
    elif state.death_kind == "bomb":
        tier = v73_blast_source_tier(source_name, profile) or "core"
        oyuncu_olum_turu = "blast_core" if tier == "core" else "blast_inner"
        oyuncu_olum_alt_turu = oyuncu_olum_turu
        oyuncu_olum_patlama_seed = state.seed
        away = v84_safe_vector(
            state.body_anchor - state.source_position,
            _adefo_yon_vektoru(oyuncu_yonu),
        ).normalize()
        oyuncu_olum_patlama_yonu = away
        v73_player_blast_fragmented = True
    else:
        oyuncu_olum_turu = "blood"
        oyuncu_olum_alt_turu = state.death_kind



    v81_death_blood = {
        "start_ms": now,
        "seed": state.seed,
        "drops": [],
        "seeps": [],
        "burst_serial": 0,
    }
    v44_arterial_emitters.clear()
    v85_mortal_wound_state.reset()
    v84_death_state.reset()
    oyuncu_saldiri_durumunu_sifirla()
    oyuncu_hareket_hiz_vektoru.update(0.0, 0.0)
    oyuncu_hareket_ediyor = False
    oyuncu_zorlanmis_hiz.update(0.0, 0.0)
    oyuncu_zorlanmis_bitis = 0
    dash_aktif_bitis = 0
    dash_aktif_yonu = pygame.Vector2(0.0, 0.0)
    dash_aktif_son_ease = 0.0
    dash_tus_kilitli = True

    if killer is not None:
        try:
            killer.attacking = False
            killer.attack_connected = True
            killer.attack_damage_applied = True
            killer.vx = killer.vy = 0.0
        except (AttributeError, TypeError, ValueError):
            pass

    immediate_one_shot = state.one_shot and state.death_kind in (
        "tarkard",
        "torrmund",
    )
    if immediate_one_shot:
        state.ready_ms = now
        state.attack_ms = now + 220
        state.approach_target = (
            pygame.Vector2(float(killer.x), float(killer.y))
            if killer is not None
            else state.body_anchor.copy()
        )
    elif state.death_kind == "headsthrower":
        state.ready_ms = now
        state.attack_ms = now + V86_DEATH_FRONT_WAIT_MS
        state.approach_target = (
            pygame.Vector2(float(killer.x), float(killer.y))
            if killer is not None
            else state.body_anchor + pygame.Vector2(128.0, 0.0)
        )
    elif state.death_kind in ("fire", "bomb", "generic"):
        state.ready_ms = now
        state.attack_ms = now + (80 if state.death_kind == "bomb" else 300)
        state.approach_target = state.body_anchor.copy()
    else:
        state.approach_target = v86_killer_front_target(killer)
        if (
            killer is None
            or pygame.Vector2(float(killer.x), float(killer.y)).distance_to(
                state.approach_target
            )
            <= 3.0
        ):
            state.ready_ms = now
            state.attack_ms = now + V86_DEATH_FRONT_WAIT_MS

    dunya_olayi_kaydet(
        "authored_player_death",
        enemy=state.killer_type or state.death_kind,
        variant=state.death_kind,
        one_shot=bool(state.one_shot),
        damage=state.damage,
    )
    return True
# </POTBO_STAGE S1920>

# <POTBO_STAGE S1923>


def v86_eroding_hit(state, index, berserker=False):
    key = ("berserker" if berserker else "crawler", int(index))
    if key in state.events:
        return
    state.events.add(key)
    rng = random.Random(state.seed ^ index * 0x86C71 ^ (991 if berserker else 0))
    fraction = rng.uniform(0.043, 0.061) if berserker else rng.uniform(0.027, 0.043)
    mask = v86_bite_mask(state, fraction, rng)
    direction = v86_impact_direction(state, rng.uniform(-46.0, 46.0))
    if mask is not None:
        v86_launch_piece(
            state,
            mask,
            direction,
            rng.uniform(92.0, 178.0) if berserker else rng.uniform(54.0, 124.0),
            rng.uniform(92.0, 192.0) if berserker else rng.uniform(58.0, 142.0),
            rng.uniform(-610.0, 610.0),
        )
    severity = 1.18 + index * 0.032 if berserker else 0.87 + index * 0.024
    zone = ("neck", "torso", "waist", "torso")[index % 4]
    v86_blood_event(
        state,
        direction,
        severity,
        zone=zone,
        tag=index + (200 if berserker else 100),
        organs=2 if berserker or index % 3 == 1 else 1,
        arterial=index in ((0, 4, 9, 13) if berserker else (0, 5, 11, 16)),
    )
    state.body_rotation = rng.uniform(-4.8, 4.8) * (1.25 if berserker else 1.0)
    kamera_hit_sarsintisi_baslat(
        5.8 + (index % 3) * 0.7 if berserker else 4.2 + (index % 4) * 0.42,
        72 if berserker else 58,
    )


def v86_tripartite_tarkard(state, now):
    if "tarkard_tripartite" in state.events:
        return
    state.events.add("tarkard_tripartite")
    height = state.base_size[1]
    head = v86_take_mask(state, lambda _x, y: y < height * 0.25)
    torso = v86_take_mask(state, lambda _x, y: y < height * 0.69)
    legs = state.remaining_mask.copy() if state.remaining_mask is not None else None
    if state.remaining_mask is not None:
        state.remaining_mask.clear()
        v86_root_refresh(state)
    direction = v86_impact_direction(state)
    rng = random.Random(state.seed ^ 0x7A86)
    for index, (mask, angle, speed, lift) in enumerate(
        (
            (head, -27.0, 215.0, 225.0),
            (torso, 11.0, 154.0, 174.0),
            (legs, 37.0, 96.0, 118.0),
        )
    ):
        if mask is not None:
            v86_launch_piece(
                state,
                mask,
                direction.rotate(angle),
                speed * state.intensity,
                lift * min(1.45, state.intensity),
                rng.uniform(-520.0, 520.0),
                delay=index * 0.045,
            )
    v86_blood_event(
        state,
        direction,
        2.15,
        zone="torso",
        tag=410,
        organs=13,
        arterial=True,
    )
    v86_spawn_debris(
        state,
        state.body_anchor,
        direction,
        16,
        1.35 * state.intensity,
        "organ",
    )
    state.fully_fragmented = True
    v86_start_fall(state, now, 360, push=direction * 10.0)
    kamera_hit_sarsintisi_baslat(15.8, 360)


def v86_torrmund_waist_bisect(state, now):
    if "torrmund_waist" in state.events:
        return
    state.events.add("torrmund_waist")
    height = state.base_size[1]
    upper = v86_take_mask(state, lambda _x, y: y < height * 0.55)
    legs = state.remaining_mask.copy() if state.remaining_mask is not None else None
    if state.remaining_mask is not None:
        state.remaining_mask.clear()
        v86_root_refresh(state)
    direction = v86_impact_direction(state)
    rng = random.Random(state.seed ^ 0x7086)
    if upper is not None:
        v86_launch_piece(
            state,
            upper,
            direction.rotate(-18.0),
            148.0 * state.intensity,
            205.0 * min(1.45, state.intensity),
            rng.uniform(-390.0, 390.0),
            delay=0.0,
        )
    if legs is not None:
        v86_launch_piece(
            state,
            legs,
            direction.rotate(19.0),
            62.0 * state.intensity,
            91.0 * min(1.35, state.intensity),
            rng.uniform(-210.0, 210.0),
            delay=0.24,
        )
    v86_blood_event(
        state,
        direction,
        2.38,
        zone="waist",
        tag=510,
        organs=14,
        arterial=True,
    )
    v86_spawn_debris(
        state,
        state.body_anchor,
        direction,
        18,
        1.46 * state.intensity,
        "organ",
    )
    state.fully_fragmented = True
    kamera_hit_sarsintisi_baslat(17.2, 390)


def v86_torrmund_decap(state, now):
    if "torrmund_decap" in state.events:
        return
    state.events.add("torrmund_decap")
    height = state.base_size[1]
    head = v86_take_mask(state, lambda _x, y: y < height * 0.255)
    direction = v86_impact_direction(state).rotate(-13.0)
    if head is not None:
        v86_launch_piece(
            state,
            head,
            direction,
            245.0 * state.intensity,
            278.0 * min(1.45, state.intensity),
            -640.0 if direction.x < 0 else 640.0,
        )
    v86_blood_event(
        state,
        direction,
        2.12,
        zone="neck",
        tag=520,
        organs=7,
        arterial=True,
    )
    v86_start_fall(
        state,
        now + 90,
        470,
        push=direction * 7.0,
        rotation=state.fall_target_rotation,
    )
    kamera_hit_sarsintisi_baslat(14.0, 285)


def v86_torrmund_second_cleave(state, now):
    if "torrmund_second_cleave" in state.events:
        return
    state.events.add("torrmund_second_cleave")
    if state.remaining_mask is None or state.remaining_mask.count() <= 0:
        return
    width = state.base_size[0]
    left = v86_take_mask(state, lambda x, _y: x < width * 0.49)
    right = state.remaining_mask.copy()
    state.remaining_mask.clear()
    v86_root_refresh(state)
    direction = v86_impact_direction(state)
    if left is not None:
        v86_launch_piece(
            state,
            left,
            direction.rotate(-53.0),
            126.0 * state.intensity,
            146.0 * state.intensity,
            -410.0,
        )
    if right is not None:
        v86_launch_piece(
            state,
            right,
            direction.rotate(48.0),
            138.0 * state.intensity,
            154.0 * state.intensity,
            430.0,
            delay=0.035,
        )
    v86_blood_event(
        state,
        direction,
        2.28,
        zone="torso",
        tag=530,
        organs=11,
        arterial=True,
    )
    v86_spawn_debris(
        state,
        state.body_anchor,
        direction,
        14,
        1.38 * state.intensity,
        "organ",
    )
    state.fully_fragmented = True
    kamera_hit_sarsintisi_baslat(16.4, 340)
# </POTBO_STAGE S1923>

# <POTBO_STAGE S1925>


def v86_bomb_fragment(state, now):
    if "bomb_fragment" in state.events:
        return
    state.events.add("bomb_fragment")
    source_to_player = v84_safe_vector(
        state.body_anchor - state.source_position,
        pygame.Vector2(0.0, 1.0),
    ).normalize()
    count = int(round(v84_clamp(27 + state.intensity * 4.0, 29, 36)))
    whole = state.remaining_mask.copy()
    regions = v86_partition_mask(whole, count, state.seed ^ 0xB086)
    state.remaining_mask.clear()
    v86_root_refresh(state)
    rng = random.Random(state.seed ^ 0xB0A686)
    cone_centers = (-39.0, 0.0, 41.0)
    for index, region in enumerate(regions):
        center_angle = cone_centers[index % 3]
        direction = source_to_player.rotate(center_angle + rng.uniform(-13.0, 13.0))
        v86_launch_piece(
            state,
            region,
            direction,
            rng.uniform(205.0, 475.0) * state.intensity,
            rng.uniform(175.0, 390.0) * min(1.55, state.intensity),
            rng.uniform(-980.0, 980.0),
            delay=(index % 5) * 0.006,
            burning=True,
        )
    v86_blood_event(
        state,
        source_to_player,
        2.65,
        zone="torso",
        tag=710,
        organs=20,
        arterial=False,
    )
    v86_spawn_debris(
        state,
        state.body_anchor,
        source_to_player,
        28,
        1.64 * state.intensity,
        "organ",
        burning=True,
    )
    v86_spawn_gore_chunks(state, source_to_player, 24, 1.48 * state.intensity)
    state.fully_fragmented = True
    kamera_hit_sarsintisi_baslat(21.0, 560)


def v86_update_heads_thrower(state, now, dt):
    killer = state.killer
    attack = int(state.attack_ms)
    if attack <= 0:
        return
    first_launch = attack - 300
    if now >= first_launch and "heads_first_rock" not in state.events:
        state.events.add("heads_first_rock")
        start = (
            pygame.Vector2(float(killer.x), float(killer.y) - 24.0)
            if killer is not None
            else state.body_anchor + pygame.Vector2(130.0, -20.0)
        )
        state.rocks.append(
            V86DeathRock(start, state.body_anchor.copy(), first_launch, attack, 45.0)
        )
    if now >= attack and "heads_first_impact" not in state.events:
        state.events.add("heads_first_impact")
        v86_rock_shatter(state, second=False)
        direction = v86_impact_direction(state)
        rng = random.Random(state.seed ^ 0x8619)
        chip = v86_bite_mask(state, 0.024, rng)
        if chip is not None:
            v86_launch_piece(
                state, chip, direction, 96.0, 135.0, rng.uniform(-580.0, 580.0)
            )
        v86_blood_event(
            state,
            direction,
            1.12,
            zone="head",
            tag=620,
            organs=3,
            arterial=False,
        )
        if killer is not None:
            away = v84_safe_vector(
                pygame.Vector2(killer.x, killer.y) - state.body_anchor,
                pygame.Vector2(1.0, 0.0),
            ).normalize()
            state.approach_target = state.body_anchor + away * 164.0


    if killer is not None and attack <= now < attack + 520:
        current = pygame.Vector2(float(killer.x), float(killer.y))
        delta = state.approach_target - current
        if delta.length_squared() > 2.0:
            step = delta.normalize() * min(delta.length(), 196.0 * dt)
            killer.x += step.x
            killer.y += step.y
            killer.vx = step.x / max(dt, 1e-6)
            killer.vy = step.y / max(dt, 1e-6)
        v86_face_killer_to_player(killer)
    elif killer is not None and now >= attack + 520:
        killer.vx = 0.0
        killer.vy = 0.0

    second_launch = attack + 1120
    second_impact = attack + 1580
    if now >= second_launch and "heads_second_rock" not in state.events:
        state.events.add("heads_second_rock")
        start = (
            pygame.Vector2(float(killer.x), float(killer.y) - 24.0)
            if killer is not None
            else state.body_anchor + pygame.Vector2(154.0, -20.0)
        )
        state.rocks.append(
            V86DeathRock(
                start,
                state.body_anchor.copy(),
                second_launch,
                second_impact,
                61.0,
                second=True,
            )
        )
    if now >= second_impact and "heads_second_impact" not in state.events:
        state.events.add("heads_second_impact")
        v86_rock_shatter(state, second=True)
        v86_head_region_shatter(state, now)
# </POTBO_STAGE S1925>

# <POTBO_STAGE S1935>


def v86_death_fire_embers(state, now):
    if state.death_kind not in ("fire", "bomb"):
        return
    rng = random.Random(state.seed ^ (int(now) // 90))
    count = 8 if state.death_kind == "fire" else 12
    for index in range(count):
        origin = state.body_anchor + state.body_offset
        point = origin + pygame.Vector2(
            rng.uniform(-19.0, 19.0), rng.uniform(-14.0, 13.0)
        )
        sx = int(round(dunya_ekran_x(point.x)))
        sy = int(round(dunya_ekran_y(point.y) - rng.uniform(2.0, 18.0)))
        size = 1 if index % 3 else 2
        pygame.draw.polygon(
            ekran,
            V84_BODY_HOT if index % 2 else V84_BLOOD,
            (
                (sx, sy - size),
                (sx + size, sy),
                (sx, sy + size),
                (sx - size, sy),
            ),
        )
# </POTBO_STAGE S1935>

# <POTBO_STAGE S1939>


def oyuncu_olum_sahnesi_ciz():
    if not v86_death_state.active:
        return _v86_death_draw_original()
    state = v86_death_state
    now = pygame.time.get_ticks()
    ekran.fill(V84_BLACK)


    kan_lekelerini_ciz(silhouette=True)
    _v77_death_blood_layer()
    for particle in blood_particles:
        if getattr(particle, "active", False):
            particle.ciz(silhouette=True)
    for chunk in sorted(gore_chunks, key=lambda item: item.y):
        chunk.ciz(silhouette=True)

    killer = state.killer
    killer_behind = killer is not None and float(
        getattr(killer, "y", state.body_anchor.y)
    ) <= float(state.body_anchor.y + state.body_offset.y)
    if killer_behind:
        v86_killer_draw(killer, now)
    for index, rock in enumerate(state.rocks):
        v86_rock_draw(rock, now, index)
    v86_death_victim_draw(now)
    v86_death_fire_embers(state, now)
    if killer is not None and not killer_behind:
        v86_killer_draw(killer, now)

    if oyuncu_olum_baslangic_ms <= 0:
        return
    title_progress = oyuncu_olum_baslik_fade_orani(now)
    _v34_gameover_music_tick(title_progress, now)

    v85_death_menu_draw(now)
    exit_progress = oyuncu_olum_cikis_orani(now)
    if exit_progress > 0.0:
        veil = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
        veil.fill((0, 0, 0, int(round(255 * exit_progress))))
        ekran.blit(veil, (0, 0))
# </POTBO_STAGE S1939>

# <POTBO_STAGE S1965>





V87_PENDING_BLOOD_LIMIT = 960
v87_pending_blood_landings = []
v87_persistent_blood_stats = {
    "scheduled": 0,
    "committed": 0,
    "seep_committed": 0,
    "enemy_death_particles_shortened": 0,
}


def v87_schedule_blood_landings(
    ground_origin,
    direction,
    count,
    max_distance,
    scale_range,
    source,
    now=None,
    cone_deg=68.0,
    delay_range=(260, 860),
    seed=0,
):
    if now is None:
        now = pygame.time.get_ticks()
    count = max(0, int(count))
    if count <= 0:
        return 0
    origin = pygame.Vector2(ground_origin)
    base = v84_safe_vector(direction).normalize()
    rng = random.Random(
        int(seed) ^ int(now) * 1009 ^ int(origin.x * 31.0) ^ int(origin.y * 47.0)
    )
    made = 0
    for index in range(count):
        angle = rng.triangular(-float(cone_deg), float(cone_deg), 0.0)
        if index % 9 == 7:
            angle += rng.choice((-1.0, 1.0)) * rng.uniform(75.0, 118.0)
        heading = base.rotate(angle)
        distance = rng.triangular(
            2.0,
            max(3.0, float(max_distance)),
            max(3.0, float(max_distance) * 0.38),
        )
        tangent = pygame.Vector2(-heading.y, heading.x)
        landing = origin + heading * distance + tangent * rng.uniform(-2.4, 2.4)
        flight = rng.randint(int(delay_range[0]), int(delay_range[1]))
        item = {
            "due_ms": int(now) + flight,
            "origin": origin.copy(),
            "landing": landing,
            "direction": heading,
            "scale": rng.uniform(float(scale_range[0]), float(scale_range[1])),
            "source": str(source),
            "satellite": rng.random() < 0.36,
        }
        if len(v87_pending_blood_landings) >= V87_PENDING_BLOOD_LIMIT:


            oldest = min(
                v87_pending_blood_landings,
                key=lambda entry: int(entry["due_ms"]),
            )
            v87_pending_blood_landings.remove(oldest)
            v87_commit_blood_landing(oldest)
        v87_pending_blood_landings.append(item)
        made += 1
    v87_persistent_blood_stats["scheduled"] += made
    return made


def v87_commit_blood_landing(item):
    landing = pygame.Vector2(item["landing"])
    origin = pygame.Vector2(item["origin"])
    safe = v74_trace_clean_floor(
        landing.x,
        landing.y,
        direction=item.get("direction", (1.0, 0.0)),
        last_clean=origin if v74_floor_clean(origin.x, origin.y) else None,
    )
    if safe is None:
        return False
    decal = v74_create_persistent_decal(
        safe.x,
        safe.y,
        max(0.055, float(item.get("scale", 0.18))),
    )
    if decal is None:
        return False
    decal.v87_authored_source = str(item.get("source", "authored"))
    v87_persistent_blood_stats["committed"] += 1
    if item.get("satellite"):
        direction = v84_safe_vector(item.get("direction", (1.0, 0.0))).normalize()
        side = direction.rotate(90.0)
        satellite = (
            pygame.Vector2(safe)
            + direction * random.uniform(1.0, 4.0)
            + side * random.uniform(-2.4, 2.4)
        )
        if v74_floor_clean(satellite.x, satellite.y):
            drip = v74_create_persistent_decal(
                satellite.x,
                satellite.y,
                max(0.055, float(item.get("scale", 0.18)) * 0.28),
            )
            if drip is not None:
                drip.v87_authored_source = f"{item.get('source', 'authored')}_drip"
                v87_persistent_blood_stats["committed"] += 1
    return True


def v87_persistent_blood_update(now=None, force=False):
    if now is None:
        now = pygame.time.get_ticks()
    remaining = []
    for item in v87_pending_blood_landings:
        if force or int(now) >= int(item["due_ms"]):
            v87_commit_blood_landing(item)
        else:
            remaining.append(item)
    v87_pending_blood_landings[:] = remaining
# </POTBO_STAGE S1965>

# <POTBO_STAGE S1968>


_v87_blood_emit_original = kan_parcacigi_patlat
# </POTBO_STAGE S1968>

# <POTBO_STAGE S1970>


_v87_execution_cut_blood_original = v84_execution_cut_blood


def v84_execution_cut_blood(target, index, angle, final=False):
    before = len(blood_particles)
    result = _v87_execution_cut_blood_original(target, index, angle, final=final)
    direction = pygame.Vector2(1.0, 0.0).rotate(float(angle))
    for particle in blood_particles[before:]:
        if hasattr(particle, "v"):
            particle.v *= random.uniform(0.62, 0.76)
        particle.v87_enemy_death = True
    v87_schedule_blood_landings(
        (float(target.x), float(target.y) + 1.0),
        direction,
        13 if final else 3 + min(3, int(index) // 6),
        28.0 if final else 15.0,
        (0.16, 0.48) if final else (0.09, 0.27),
        "execution_final" if final else "execution_cut",
        now=int(
            getattr(
                v84_execution_state,
                "last_tick_ms",
                pygame.time.get_ticks(),
            )
        ),
        cone_deg=96.0 if final else 62.0,
        delay_range=(310, 920) if final else (230, 680),
        seed=int(v84_execution_state.seed) + int(index) * 887,
    )
    return result


_v87_death_blood_event_original = v86_blood_event


def v86_blood_event(
    state,
    direction,
    severity,
    zone="torso",
    tag=0,
    organs=1,
    arterial=False,
):
    result = _v87_death_blood_event_original(
        state,
        direction,
        severity,
        zone=zone,
        tag=tag,
        organs=organs,
        arterial=arterial,
    )
    scaled = max(0.45, float(severity) * float(state.intensity))
    v87_schedule_blood_landings(
        state.body_anchor,
        direction,
        min(13, 4 + int(round(scaled * 2.2)) + (3 if arterial else 0)),
        min(42.0, 17.0 + scaled * 7.0),
        (0.12, min(0.64, 0.25 + scaled * 0.10)),
        f"death_{state.death_kind}_{zone}",
        now=int(getattr(state, "last_tick_ms", pygame.time.get_ticks())),
        cone_deg=105.0 if arterial else 78.0,
        delay_range=(260, 980) if arterial else (230, 760),
        seed=int(state.seed) + int(tag) * 97,
    )
    return result
# </POTBO_STAGE S1970>

# <POTBO_STAGE S1972>


def _v81_draw_seep(seep, now):
    _v87_draw_seep_original(seep, now)
    if seep.get("v87_committed"):
        return
    age = int(now) - int(seep["birth_ms"])
    progress = _v81_smooth(age / max(1.0, float(seep["grow_ms"])))
    if progress < 0.24:
        return
    origin = pygame.Vector2(seep["origin"])
    radius = max(float(seep["rx"]), float(seep["ry"]))
    center = kan_lekesi_ekle(
        origin.x,
        origin.y,
        max(0.18, min(0.86, radius / 15.0)),
    )
    made = 1 if center is not None else 0
    made += v73_ground_splatter(
        origin.x,
        origin.y,
        pygame.Vector2(1.0, 0.0).rotate(math.degrees(float(seep["angle"]))),
        max(2, min(6, int(round(radius / 2.8)))),
        scale_range=(0.08, max(0.14, min(0.38, radius / 32.0))),
        distance_range=(1.0, max(4.0, min(13.0, radius * 0.72))),
        cone_deg=148.0,
        backscatter=0.38,
        source="v87_death_seep",
    )
    if made > 0:
        seep["v87_committed"] = True
        v87_persistent_blood_stats["seep_committed"] += made
# </POTBO_STAGE S1972>

# <POTBO_STAGE S1974>


def v84_execution_update(now=None):
    result = _v87_execution_update_original(now)
    v87_persistent_blood_update(now)
    return result
# </POTBO_STAGE S1974>

# <POTBO_STAGE S1976>


def v86_death_update(now=None):
    result = _v87_death_update_original(now)
    v87_persistent_blood_update(now)
    return result


_v87_gore_update_original = kan_gore_guncelle


def kan_gore_guncelle():
    result = _v87_gore_update_original()
    v87_persistent_blood_update(pygame.time.get_ticks())
    return result
# </POTBO_STAGE S1976>

# <POTBO_STAGE S1978>


def oyuncu_olum_sahnesini_sifirla():

    v87_persistent_blood_update(force=True)
    return _v87_death_reset_original()


def v87_diagnostics():
    return {
        "version": V87_VERSION,
        "execution_special_palette_exact": (
            V87_SPECIAL_CUT_DARK == (88, 0, 14)
            and V87_SPECIAL_CUT_RED == (226, 22, 48)
            and V87_SPECIAL_CUT_CORE == (255, 244, 247)
        ),
        "crawler_hit_step_ms": V86_CRAWLER_HIT_STEP_MS,
        "berserker_hit_step_ms": V86_BERSERKER_HIT_STEP_MS,
        "berserker_eight_way_direction": True,
        "embedded_ground_fire_frames": len(V87_GROUND_FIRE_SPRITES),
        "ground_fire_source_sha256": V87_GROUND_FIRE_ATLAS_SHA256,
        "pending_persistent_blood": len(v87_pending_blood_landings),
        "persistent_blood": dict(v87_persistent_blood_stats),
        "enemy_death_velocity_scale": (0.54, 0.68),
    }
# </POTBO_STAGE S1978>

# <POTBO_STAGE S1981>






















V88_VERSION = "88.0"










V88_EFFECTS_ROOT = os.path.join(ASSETS, "effects")
# </POTBO_STAGE S1981>

# <POTBO_STAGE S1983>
V88_DECAL_ROOT = os.path.join(V88_EFFECTS_ROOT, "decals")
V88_GORE_ROOT = os.path.join(V88_EFFECTS_ROOT, "gore")
# </POTBO_STAGE S1983>

# <POTBO_STAGE S1987>


def v88_effect_asset_candidates(filename, family):
    filename = str(filename)
    family = str(family)
    canonical = {
        "particles": V88_PARTICLE_ROOT,
        "decals": V88_DECAL_ROOT,
        "gore": V88_GORE_ROOT,
    }.get(family, V88_EFFECTS_ROOT)
    legacy = {
        "particles": BLOOD_PARTICLE_KLASORU,
        "decals": BLOOD_DECAL_KLASORU,
        "gore": GORE_KLASORU,
    }.get(family, BLOOD_EFFECT_KLASORU)
    return (
        os.path.join(canonical, filename),
        os.path.join(legacy, filename),
        os.path.join(V88_EFFECTS_ROOT, filename),
        os.path.join(BASE_DIR, filename),
        os.path.join(V88_REVIEW_ROOT, filename),
    )
# </POTBO_STAGE S1987>

# <POTBO_STAGE S1989>


def v88_reload_blood_assets():
    """Load the supplied six sprays and two decals from their canonical folders."""
    particles = []
    particle_paths = []
    for index in range(1, 7):
        path, image = v88_load_alpha_asset(
            v88_effect_asset_candidates(f"bleed{index}.png", "particles")
        )
        if image is not None:
            particles.append(image)
            particle_paths.append(path)

    decals = []
    decal_paths = []
    for filename in ("bloodsplat1.png", "bloodsplat2.png"):
        path, image = v88_load_alpha_asset(
            v88_effect_asset_candidates(filename, "decals")
        )
        if image is not None:
            image = v104_sadelestirilmis_kan_decal(image)
            decals.append(image)
            decal_paths.append(path)


    if len(particles) == 6:
        BLOOD_PARTICLE_SPRITELERI[:] = particles
        BLOOD_PARTICLE_YOLLARI[:] = particle_paths
        V88_ASSET_SELECTED["particles"] = list(particle_paths)
    else:
        V88_ASSET_SELECTED["particles"] = [
            path for path in BLOOD_PARTICLE_YOLLARI if os.path.isfile(path)
        ]

    if decals:
        BLOOD_DECAL_SPRITELERI[:] = decals
        BLOOD_DECAL_YOLLARI[:] = decal_paths
        V88_ASSET_SELECTED["decals"] = list(decal_paths)
        blood_decal_onbellegi.clear()
    else:
        V88_ASSET_SELECTED["decals"] = [
            path for path in BLOOD_DECAL_YOLLARI if os.path.isfile(path)
        ]


def v88_reload_gore_assets():
    """Load anatomy files and both supplied atlases without preview backgrounds."""
    direct = {
        "foot": "foot.png",
        "intestine": "intestine.png",
        "leg": "leg.png",
        "liver": "liver.png",
        "ribcage": "ribcage.png",
    }
    selected = {}
    for kind, filename in direct.items():
        path, image = v88_load_alpha_asset(
            v88_effect_asset_candidates(filename, "gore")
        )
        if image is None:
            continue
        GORE_SPRITELERI[kind] = image
        selected[kind] = path

    atlas_path, atlas = v88_load_alpha_asset(
        v88_effect_asset_candidates("blood_effects_sheet.png", "gore")
        + v88_effect_asset_candidates("blood_effects_sheet.png", "particles")
    )
    if atlas is not None:
        for kind, normalized_rect in GORE_ATLAS_NORMALIZE_CROPLARI.items():
            image = _v24_normalize_crop(atlas, normalized_rect)
            if image is not None:
                GORE_SPRITELERI[kind] = image
        V88_ASSET_SELECTED["gore_atlas"] = atlas_path

    extra_path, extra = v88_load_alpha_asset(
        v88_effect_asset_candidates("gore_effects.png", "gore")
    )
    if extra is not None:
        width, height = extra.get_size()
        for kind, normalized_rect in V28_EXTRA_GORE_CROPLARI.items():
            nx, ny, nw, nh = normalized_rect
            rect = pygame.Rect(
                int(round(nx * width)),
                int(round(ny * height)),
                max(1, int(round(nw * width))),
                max(1, int(round(nh * height))),
            ).clip(extra.get_rect())
            if rect.width <= 0 or rect.height <= 0:
                continue
            image = _v28_beyaz_fon_temizle(extra.subsurface(rect).copy())
            if image is not None:
                GORE_SPRITELERI[kind] = image
        V88_ASSET_SELECTED["extra_gore_atlas"] = extra_path

    V88_ASSET_SELECTED["gore"] = selected
# </POTBO_STAGE S1989>

# <POTBO_STAGE S1991>


v88_reload_blood_assets()
v88_reload_gore_assets()
# </POTBO_STAGE S1991>

# <POTBO_STAGE S2001>


def v88_unique_exact_actor(source_name, source_uid=""):
    """Resolve identity, never proximity; ambiguous same-type matches are rejected."""
    actors = v88_actor_pool(include_inactive=False)
    uid = str(source_uid or "")
    if uid:
        uid_matches = [
            actor for actor in actors if str(getattr(actor, "uid", "")) == uid
        ]
        if len(uid_matches) == 1:
            v88_attribution_stats["exact_fallback"] += 1
            return uid_matches[0]
        if len(uid_matches) > 1:
            v88_attribution_stats["ambiguous_rejected"] += 1
            return None

    source_key = v88_name_key(source_name)
    direct = []
    if source_key:
        for actor in actors:
            keys = {
                v88_name_key(getattr(actor, "uid", "")),
                v88_name_key(getattr(actor, "name", "")),
                v88_name_key(getattr(actor, "tur", "")),
            }
            keys.discard("")
            if source_key in keys:
                direct.append(actor)
        if len(direct) == 1:
            v88_attribution_stats["exact_fallback"] += 1
            return direct[0]
        if len(direct) > 1:
            v88_attribution_stats["ambiguous_rejected"] += 1
            return None

    type_hint = v88_source_type_hint(source_name)
    typed = [
        actor for actor in actors if str(getattr(actor, "tur", "")).lower() == type_hint
    ]
    if type_hint and len(typed) == 1:
        v88_attribution_stats["exact_fallback"] += 1
        return typed[0]
    if len(typed) > 1:
        v88_attribution_stats["ambiguous_rejected"] += 1
    return None
# </POTBO_STAGE S2001>

# <POTBO_STAGE S2022>


def v86_death_scene_begin(
    killer,
    source_x,
    source_y,
    profile,
    damage,
    source_name,
):
    result = _v88_death_scene_begin_original(
        killer,
        source_x,
        source_y,
        profile,
        damage,
        source_name,
    )
    if not result or not v86_death_state.active:
        return result

    state = v86_death_state



    state.v88_hit_scheduler_kind = ""
    state.v88_hits_done = 0
    state.v88_next_hit_ms = 0
    state.v88_last_hit_ms = 0
    state.v88_scheduler_complete_ms = 0
    state.v88_max_hits_in_one_update = 0
    if v88_death_blood_flows:
        v88_death_flows_update(force=True)
        v88_death_blood_flows.clear()
    event = v88_linked_lethal_event_for_scene(killer, source_name)
    state.v88_lethal_event_id = int(event.event_id) if event is not None else 0
    state.v88_provenance_id = int(event.provenance_id) if event is not None else 0
    state.v88_impact_linked = bool(event is not None and event.impact_already_landed)
    state.v88_source_kind = str(event.source_kind) if event is not None else "unscoped"
    state.v88_attack_started_ms = (
        int(event.attack_started_ms) if event is not None else 0
    )
    state.v88_attack_variant = str(event.attack_variant) if event is not None else ""

    if event is not None and not state.killer_type and event.attacker_type:
        state.killer_type = str(event.attacker_type)
        if event.attacker_type in {
            "crawler",
            "berserker",
            "headsthrower",
            "tarkard",
            "torrmund",
        }:
            state.death_kind = str(event.attacker_type)

    if not state.v88_impact_linked:
        return result

    now = int(state.started_ms)



    if state.death_kind == "tarkard":
        state.ready_ms = now
        state.attack_ms = now
        state.phase = "linked_tarkard_impact"
        state.approach_target = (
            pygame.Vector2(float(killer.x), float(killer.y))
            if killer is not None
            else state.body_anchor.copy()
        )
        v86_tripartite_tarkard(state, now)
    elif state.death_kind == "torrmund":
        state.ready_ms = now
        state.attack_ms = now
        state.phase = "linked_torrmund_impact"
        state.approach_target = (
            pygame.Vector2(float(killer.x), float(killer.y))
            if killer is not None
            else state.body_anchor.copy()
        )
        if state.one_shot:
            v86_torrmund_waist_bisect(state, now)
        else:
            v86_torrmund_decap(state, now)
    elif state.death_kind == "headsthrower" and (
        state.v88_source_kind == "projectile"
        or "rock" in str(source_name or "").lower()
    ):



        state.ready_ms = now
        state.attack_ms = now
        state.phase = "linked_heads_first_impact"
        if killer is not None:
            away = v84_safe_vector(
                pygame.Vector2(float(killer.x), float(killer.y)) - state.body_anchor,
                pygame.Vector2(1.0, 0.0),
            ).normalize()
            state.approach_target = state.body_anchor + away * 164.0
        v86_update_heads_thrower(state, now, 0.0)
    elif state.death_kind == "bomb":

        state.ready_ms = now
        state.attack_ms = now
        state.phase = "linked_blast_impact"
        v86_bomb_fragment(state, now)

    v88_enforce_death_physics_ownership()
    return result
# </POTBO_STAGE S2022>

# <POTBO_STAGE S2030>


v88_death_blood_flows = []
# </POTBO_STAGE S2030>

# <POTBO_STAGE S2036>


def v88_flow_find_feed_target(scene_seed, origin, direction):
    origin = pygame.Vector2(origin)
    best = None
    best_score = -1e9
    for flow in v88_death_blood_flows:
        if int(flow.scene_seed) != int(scene_seed):
            continue
        distance = flow.origin.distance_to(origin)
        alignment = v88_flow_angle_similarity(flow.direction, direction)
        if distance > 25.0 or alignment < 0.54:
            continue
        score = alignment * 100.0 - distance * 1.7
        if score > best_score:
            best = flow
            best_score = score
    return best
# </POTBO_STAGE S2036>

# <POTBO_STAGE S2038>


def v88_flow_add(state, direction, severity, zone, tag, arterial):
    if state is None or not getattr(state, "active", False):
        return None
    now = int(getattr(state, "last_tick_ms", pygame.time.get_ticks()))
    origin = v88_flow_ground_origin(state, zone)
    direction = v84_safe_vector(direction).normalize()
    scaled = max(0.45, float(severity) * float(state.intensity))
    target = v88_flow_find_feed_target(state.seed, origin, direction)
    if target is not None:
        target.feed(
            scaled * (1.18 if arterial else 0.88),
            direction,
            tag,
            now,
        )
        clear = v88_flow_clear_length(
            target.origin,
            target.direction,
            target.target_length,
        )
        target.target_length = min(target.target_length, clear)
        v88_flow_stats["fed"] += 1
        return target



    same_scene = [
        flow
        for flow in v88_death_blood_flows
        if int(flow.scene_seed) == int(state.seed)
    ]
    if len(same_scene) >= V88_DEATH_FLOW_LIMIT:
        target = max(
            same_scene,
            key=lambda flow: v88_flow_angle_similarity(flow.direction, direction),
        )
        target.feed(scaled, direction, tag, now)
        v88_flow_stats["fed"] += 1
        return target
    return v88_flow_create(state, origin, direction, scaled, tag, now)
# </POTBO_STAGE S2038>

# <POTBO_STAGE S2043>


def v88_flow_draw(flow, now):
    if flow.visible_length <= 0.25 or flow.visible_width <= 0.15:
        return
    outer = v88_flow_polygon(flow, samples=15, inset=0.0)
    if len(outer) >= 3:
        pygame.draw.polygon(ekran, V77_DEATH_BLOOD, outer)
    inner = v88_flow_polygon(
        flow,
        samples=15,
        inset=max(0.45, flow.visible_width * 0.18),
    )
    if len(inner) >= 3:
        pygame.draw.polygon(ekran, V84_BLOOD, inner)


    head = v88_flow_center(flow, 1.0)
    neck = v88_flow_center(flow, 0.91)
    pygame.draw.line(
        ekran,
        V84_BLOOD_HOT,
        v88_world_to_screen(neck),
        v88_world_to_screen(head),
        1,
    )
    branch_count = 1 + int(flow.mass >= 3.2) + int(flow.mass >= 7.0)
    for branch_index in range(branch_count):
        v88_flow_draw_branch(flow, branch_index)
# </POTBO_STAGE S2043>

# <POTBO_STAGE S2045>


def v88_flow_commit_stage(flow, stage, forced=False):
    stage = max(1, min(V88_DEATH_FLOW_COMMIT_STAGES, int(stage)))
    made = 0
    lane_count = 2 if stage in (2, 4, 6) or flow.mass >= 5.0 else 1
    for lane in range(lane_count):
        point = v88_flow_commit_point(flow, stage, lane)
        safe = v74_trace_clean_floor(
            point.x,
            point.y,
            direction=flow.direction,
            last_clean=flow.origin,
        )
        if safe is None:
            continue
        scale = v84_clamp(
            0.075 + flow.target_width * 0.018 + stage * 0.012 + lane * 0.018,
            0.08,
            0.48,
        )
        decal = v74_create_persistent_decal(
            safe.x,
            safe.y,
            scale,
            rotation=math.degrees(math.atan2(flow.direction.y, flow.direction.x)),
        )
        if decal is not None:
            decal.v88_flow_id = int(flow.flow_id)
            decal.v88_flow_stage = int(stage)
            made += 1
    if made:
        key = "forced_commits" if forced else "progressive_commits"
        v88_flow_stats[key] += made
    return made
# </POTBO_STAGE S2045>

# <POTBO_STAGE S2047>


def v88_death_flows_update(now=None, force=False):
    if now is None:
        now = pygame.time.get_ticks()
    for flow in v88_death_blood_flows:
        if force:
            flow.visible_length = float(flow.target_length)
            flow.visible_width = float(flow.target_width)
        else:
            flow.update(now)
        v88_flow_progressive_commit(flow, force=force)


def v88_death_flows_draw(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    scene_seed = int(getattr(v86_death_state, "seed", 0))
    for flow in v88_death_blood_flows:
        if scene_seed and int(flow.scene_seed) != scene_seed:
            continue
        v88_flow_draw(flow, now)


_v88_death_blood_event_original = v86_blood_event


def v86_blood_event(
    state,
    direction,
    severity,
    zone="torso",
    tag=0,
    organs=1,
    arterial=False,
):
    result = _v88_death_blood_event_original(
        state,
        direction,
        severity,
        zone=zone,
        tag=tag,
        organs=organs,
        arterial=arterial,
    )
    v88_flow_add(
        state,
        direction,
        severity,
        zone,
        tag,
        arterial,
    )
    return result





def _v81_draw_seep(seep, now):
    _v87_draw_seep_original(seep, now)
    if v86_death_state.active:
        return
    age = int(now) - int(seep["birth_ms"])
    progress = _v81_smooth(age / max(1.0, float(seep["grow_ms"])))
    target_stage = min(5, int(math.floor(progress * 5.0)))
    committed = int(seep.get("v88_committed_stage", 0))
    origin = pygame.Vector2(seep["origin"])
    direction = pygame.Vector2(1.0, 0.0).rotate(math.degrees(float(seep["angle"])))
    side = pygame.Vector2(-direction.y, direction.x)
    while committed < target_stage:
        committed += 1
        rng = random.Random(
            int(origin.x * 31.0) ^ int(origin.y * 47.0) ^ committed * 0x8158
        )
        point = (
            origin + direction * (1.6 + committed * 1.9) + side * rng.uniform(-2.1, 2.1)
        )
        safe = v74_trace_clean_floor(
            point.x,
            point.y,
            direction=direction,
            last_clean=origin,
        )
        if safe is not None:
            decal = v74_create_persistent_decal(
                safe.x,
                safe.y,
                0.07 + committed * 0.025,
                rotation=math.degrees(math.atan2(direction.y, direction.x)),
            )
            if decal is not None:
                decal.v88_progressive_seep = True
                v88_flow_stats["progressive_commits"] += 1
    seep["v88_committed_stage"] = committed


_v88_death_blood_layer_original = _v77_death_blood_layer


def _v77_death_blood_layer():
    _v88_death_blood_layer_original()
    v88_death_flows_draw(pygame.time.get_ticks())
# </POTBO_STAGE S2047>

# <POTBO_STAGE S2050>


def oyuncu_olum_sahnesini_sifirla():
    global v88_lethal_event
    if v88_death_blood_flows:



        v88_death_flows_update(force=True)
    result = _v88_death_reset_original()
    v88_death_blood_flows.clear()
    v88_damage_source_stack.clear()
    v88_lethal_event = None
    return result
# </POTBO_STAGE S2050>

# <POTBO_STAGE S2053>


def v88_blood_diagnostics():
    return {
        "flow_count": len(v88_death_blood_flows),
        "flow_limit": V88_DEATH_FLOW_LIMIT,
        "commit_stages": V88_DEATH_FLOW_COMMIT_STAGES,
        "grows_by_simulation": True,
        "single_drop_pool_spawn": False,
        "persistent_v74_commit": True,
        "pending_air_landings": len(v87_pending_blood_landings),
        "stats": dict(v88_flow_stats),
    }


def v88_diagnostics():
    return {
        "version": V88_VERSION,
        "assets": v88_asset_diagnostics(),
        "attribution": v88_attribution_diagnostics(),
        "death": v88_death_diagnostics(),
        "blood": v88_blood_diagnostics(),
        "preserved": {
            "dialogue_data": True,
            "settings_contract": True,
            "death_title_and_button_fades": True,
            "v74_blood_ecology": True,
            "v86_death_director": True,
            "v87_execution_landings": True,
        },
    }
# </POTBO_STAGE S2053>

# <POTBO_STAGE S2064>








V89_BLOOD_TILE_WORLD = 192.0
V89_BLOOD_TILE_PAD = 68.0
V89_BLOOD_TILE_CACHE_LIMIT = 96
V89_BLOOD_RESIDUE_MASS = 0.035
V89_BLOOD_TRANSIENT_LIMIT = 250
V89_BLOOD_BURST_LIMIT = 44
V89_BLOOD_ARTERIAL_BURST_LIMIT = 62

v89_blood_tile_cache = {}
v89_blood_tile_revision = {}
v89_blood_image_cache = {}
# </POTBO_STAGE S2064>

# <POTBO_STAGE S2067>
v89_rivulets = []
v89_rivulet_cell_next_ms = {}
# </POTBO_STAGE S2067>

# <POTBO_STAGE S2070>
v89_stats = {
    "tile_builds": 0,
    "tile_blits": 0,
    "air_particles_collapsed": 0,
    "permanent_landings_scheduled": 0,
    "footprints": 0,
    "rivulets": 0,
    "blood_scorched": 0,
    "maggots_born": 0,
    "maggots_burned": 0,
    "organs_burned": 0,
}


def v89_blood_tile_key_at(x, y):
    return (
        int(math.floor(float(x) / V89_BLOOD_TILE_WORLD)),
        int(math.floor(float(y) / V89_BLOOD_TILE_WORLD)),
    )


def v89_blood_tile_dirty_at(x, y):
    tile = v89_blood_tile_key_at(x, y)
    v89_blood_tile_revision[tile] = int(v89_blood_tile_revision.get(tile, 0)) + 1


def v89_blood_wetness(item, now=None):
    if now is None:
        now = pygame.time.get_ticks()
    if float(getattr(item, "v89_scorch", 0.0)) >= 0.70:
        return 0.0
    created = int(getattr(item, "created_ms", now))
    dry_after = int(getattr(item, "dry_after_ms", created + V75_BLOOD_FULL_DRY_MS))
    if dry_after <= created:
        return 0.0
    return 1.0 - v89_clamp01((int(now) - created) / float(dry_after - created))


def v89_blood_dry_stage(item, now=None):
    wetness = v89_blood_wetness(item, now)
    return max(0, min(5, int(round((1.0 - wetness) * 5.0))))


def v89_blood_next_visual_change(item, now):
    if float(getattr(item, "v89_scorch", 0.0)) >= 0.70:
        return 2**62
    created = int(getattr(item, "created_ms", now))
    dry_after = int(getattr(item, "dry_after_ms", created + V75_BLOOD_FULL_DRY_MS))
    span = max(1, dry_after - created)
    progress = v89_clamp01((int(now) - created) / float(span))
    bucket = min(5, int(progress * 6.0))
    if bucket >= 5 or int(now) >= dry_after:
        return 2**62
    return created + int(math.ceil(span * (bucket + 1) / 6.0)) + 1


def v89_decal_defaults(decal):
    if decal is None:
        return None
    decal.v74_permanent = True
    decal.v75_ecology_consumed = False
    decal.v89_scorch = max(0.0, float(getattr(decal, "v89_scorch", 0.0)))
    mass = max(
        V89_BLOOD_RESIDUE_MASS,
        float(getattr(decal, "v75_ecology_mass", v75_blood_mass(decal))),
    )
    decal.v75_ecology_mass = mass
    decal.v75_ecology_mass_initial = max(
        mass,
        float(getattr(decal, "v75_ecology_mass_initial", mass)),
    )
    decal.vanish_after_ms = 2**62
    return decal


def v89_decal_image(decal, now, silhouette, zoom):
    stage = v89_blood_dry_stage(decal, now)
    scorch_bucket = max(
        0,
        min(4, int(round(float(getattr(decal, "v89_scorch", 0.0)) * 4.0))),
    )
    if BLOOD_DECAL_SPRITELERI:
        source = BLOOD_DECAL_SPRITELERI[
            int(getattr(decal, "sprite_index", 0)) % len(BLOOD_DECAL_SPRITELERI)
        ]
        factor = max(0.055, float(getattr(decal, "scale", 0.55))) * float(zoom)
        raw_h = max(2, int(round(source.get_height() * factor)))
        height = max(2, int(round(raw_h / 2.0)) * 2)
        ratio = source.get_width() / max(1.0, float(source.get_height()))
        size = (max(2, int(round(height * ratio))), height)
        rotation = int(round(float(getattr(decal, "rotation", 0.0)) / 10.0)) * 10
        if silhouette:
            tone = (84, 0, 9)
        else:
            try:
                fresh = tuple(decal._v44_color(now))
            except (AttributeError, TypeError, ValueError):
                fresh = (116, 5, 18)
            dry_tone = (49, 17, 16)
            tone = v89_color_mix(fresh, dry_tone, stage / 5.0)
            tone = v89_color_mix(tone, (18, 10, 7), scorch_bucket / 4.0)
        tone_bucket = tuple(int(channel // 8 * 8) for channel in tone)
        key = (
            id(source),
            size,
            rotation,
            tone_bucket,
            bool(silhouette),
        )
        image = v89_blood_image_cache.get(key)
        if image is None:
            image = pygame.transform.scale(source, size).convert_alpha()
            tint = pygame.Surface(image.get_size(), pygame.SRCALPHA)
            tint.fill((*tone_bucket, 255))
            image.blit(tint, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            image = pygame.transform.rotate(image, rotation).convert_alpha()
            if len(v89_blood_image_cache) >= 1152:
                for old_key in list(v89_blood_image_cache)[:256]:
                    v89_blood_image_cache.pop(old_key, None)
            v89_blood_image_cache[key] = image
        return image

    radius = max(2, int(round(5.0 * float(getattr(decal, "scale", 0.55)) * zoom)))
    variant = int(getattr(decal, "v44_seed", id(decal))) % 12
    rotation = int(round(float(getattr(decal, "rotation", 0.0)) / 15.0)) * 15
    key = (
        "fallback",
        radius,
        stage,
        scorch_bucket,
        variant,
        rotation,
        bool(silhouette),
    )
    image = v89_blood_image_cache.get(key)
    if image is None:
        image = pygame.Surface((radius * 4 + 8, radius * 3 + 8), pygame.SRCALPHA)
        color = (84, 0, 9) if silhouette else v89_color_mix(
            (112, 0, 14), (24, 12, 9), max(stage / 5.0, scorch_bucket / 4.0)
        )
        rng = random.Random(variant * 917 + radius * 37)
        center = pygame.Vector2(image.get_width() * 0.5, image.get_height() * 0.5)
        main = pygame.Rect(0, 0, radius * 3, radius * 2)
        main.center = (int(center.x), int(center.y))
        pygame.draw.ellipse(image, (*color, 238), main)
        for _ in range(4):
            angle = rng.random() * math.tau
            distance = rng.uniform(radius * 0.55, radius * 1.25)
            lobe_radius = max(1, int(round(radius * rng.uniform(0.26, 0.62))))
            point = center + pygame.Vector2(math.cos(angle), math.sin(angle)) * distance
            pygame.draw.ellipse(
                image,
                (*color, rng.randint(205, 242)),
                (
                    int(point.x - lobe_radius),
                    int(point.y - lobe_radius * 0.72),
                    lobe_radius * 2,
                    max(2, int(lobe_radius * 1.44)),
                ),
            )
        for _ in range(2):
            point = center + pygame.Vector2(rng.uniform(-1.8, 1.8), rng.uniform(-1.1, 1.1)) * radius
            pygame.draw.circle(
                image,
                (*color, 212),
                (int(point.x), int(point.y)),
                max(1, radius // 4),
            )
        image = pygame.transform.rotate(image, rotation).convert_alpha()
        v89_blood_image_cache[key] = image
    return image
# </POTBO_STAGE S2070>

# <POTBO_STAGE S2072>


def v89_footprint_image(print_item, now, silhouette, zoom):
    stage = v89_blood_dry_stage(print_item, now)
    scorch = max(
        0,
        min(4, int(round(float(getattr(print_item, "v89_scorch", 0.0)) * 4.0))),
    )
    intensity_bucket = max(1, min(6, int(round(print_item.intensity * 6.0))))
    angle = int(round(print_item.angle / 12.0)) * 12
    key = (
        round(float(zoom), 3),
        angle,
        print_item.side,
        intensity_bucket,
        stage,
        scorch,
        bool(silhouette),
    )
    image = v89_footprint_image_cache.get(key)
    if image is not None:
        return image
    alpha = max(52, min(238, 44 + intensity_bucket * 32))
    if silhouette:
        color = (84, 0, 9)
    else:
        color = v89_color_mix((119, 2, 18), (48, 15, 14), stage / 5.0)
        color = v89_color_mix(color, (17, 10, 7), scorch / 4.0)
    base = pygame.Surface((12, 20), pygame.SRCALPHA)
    toe_x = 1 if print_item.side < 0 else 3
    pygame.draw.ellipse(base, (*color, alpha), (toe_x, 0, 8, 7))
    pygame.draw.rect(base, (*color, max(36, alpha - 16)), (3, 7, 6, 5))
    pygame.draw.ellipse(base, (*color, max(30, alpha - 28)), (2, 13, 8, 6))
    size = (
        max(4, int(round(base.get_width() * zoom))),
        max(7, int(round(base.get_height() * zoom))),
    )
    image = pygame.transform.scale(base, size)
    image = pygame.transform.rotate(image, -angle).convert_alpha()
    if len(v89_footprint_image_cache) >= 384:
        for old_key in list(v89_footprint_image_cache)[:96]:
            v89_footprint_image_cache.pop(old_key, None)
    v89_footprint_image_cache[key] = image
    return image


def v89_add_footprint(x, y, angle, side, intensity, now):
    if not v74_floor_clean(x, y):
        return None
    item = V89BloodFootprint(x, y, angle, side, intensity, now)
    tile = v89_blood_tile_key_at(x, y)
    v89_footprint_grid.setdefault(tile, []).append(item)
    v89_blood_tile_dirty_at(x, y)
    v89_stats["footprints"] += 1
    return item


def v89_wet_blood_contact(x, y, now):
    point = pygame.Vector2(float(x), float(y))
    strongest = 0.0
    for decal in _v40_blood_nearby(point, 24.0):
        wetness = v89_blood_wetness(decal, now)
        if wetness <= 0.06:
            continue
        radius = max(6.0, min(28.0, 7.0 + float(getattr(decal, "scale", 0.5)) * 12.0))
        if point.distance_squared_to((float(decal.x), float(decal.y))) <= radius * radius:
            nutrient = max(
                V89_BLOOD_RESIDUE_MASS,
                float(getattr(decal, "v75_ecology_mass", V89_BLOOD_RESIDUE_MASS)),
            )
            strongest = max(
                strongest,
                wetness * min(1.0, 0.35 + nutrient * 0.92),
            )
    return strongest


def v89_player_footprints_update(now):
    global v89_player_foot_last_pos, v89_player_foot_distance
    global v89_player_foot_side, v89_player_sole_load
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA or oyuncu_hp <= 0:
        v89_player_foot_last_pos = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
        v89_player_foot_distance = 0.0
        return
    current = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    if v89_player_foot_last_pos is None:
        v89_player_foot_last_pos = current
        return
    movement = current - v89_player_foot_last_pos
    distance = movement.length()
    v89_player_foot_last_pos = current
    if distance <= 0.02:
        return
    if distance > 72.0:
        v89_player_foot_distance = 0.0
        v89_player_sole_load = 0.0
        return
    direction = movement.normalize()
    contact = v89_wet_blood_contact(current.x, current.y, now)
    if contact > 0.06:
        v89_player_sole_load = max(v89_player_sole_load, contact)
    v89_player_foot_distance += distance
    spacing = 15.0
    while v89_player_foot_distance >= spacing:
        v89_player_foot_distance -= spacing
        if v89_player_sole_load <= 0.065:
            continue
        v89_player_foot_side = 1 - int(v89_player_foot_side)
        side = -1 if v89_player_foot_side == 0 else 1
        normal = direction.rotate(90.0)
        point = current + normal * (4.0 * side) - direction * 3.5
        angle = math.degrees(math.atan2(direction.y, direction.x)) + 90.0
        v89_add_footprint(
            point.x,
            point.y,
            angle,
            side,
            v89_player_sole_load,
            now,
        )
        v89_player_sole_load = max(
            0.0,
            v89_player_sole_load - (0.13 if contact > 0.06 else 0.18),
        )


class V89BloodRivulet:
    def __init__(self, origin, direction, scale, now, seed):
        self.origin = pygame.Vector2(origin)
        vector = pygame.Vector2(direction)
        if vector.length_squared() <= 1e-8:
            vector = pygame.Vector2(1.0, 0.0).rotate(float(seed % 360))
        self.direction = vector.normalize().rotate(((int(seed) % 17) - 8) * 1.8)
        self.scale = max(0.18, float(scale))
        self.start_ms = int(now)
        self.duration_ms = int(1050 + min(1900, self.scale * 980))
        self.length = min(52.0, 10.0 + self.scale * 27.0)
        self.width = min(5.4, 1.2 + self.scale * 2.4)
        self.seed = int(seed)
        self.stages = 7
        self.committed = 0
        self.active = True

    def point_at(self, fraction):
        fraction = v89_clamp01(fraction)
        side = self.direction.rotate(90.0)
        bend = math.sin(fraction * math.pi) * (((self.seed % 9) - 4) * 0.34)
        return self.origin + self.direction * (self.length * fraction) + side * bend

    def update(self, now):
        progress = v89_clamp01((int(now) - self.start_ms) / float(self.duration_ms))
        target_stage = min(self.stages, int(math.floor(progress * self.stages)) + 1)
        while self.committed < target_stage:
            index = self.committed
            fraction = index / max(1.0, float(self.stages - 1))
            point = self.point_at(fraction)
            if v74_floor_clean(point.x, point.y):
                decal = _v89_create_decal_raw(
                    point.x,
                    point.y,
                    max(0.07, self.scale * (0.30 - 0.14 * fraction)),
                    rotation=math.degrees(math.atan2(self.direction.y, self.direction.x)),
                )
                if decal is not None:
                    v89_decal_defaults(decal)
                    decal.v89_rivulet = True
                    v89_blood_tile_dirty_at(decal.x, decal.y)
            self.committed += 1
        if progress >= 1.0:
            self.active = False

    def draw(self, now, silhouette=False):
        progress = v89_clamp01((int(now) - self.start_ms) / float(self.duration_ms))
        samples = max(2, int(round(3 + progress * 7)))
        points = []
        for index in range(samples):
            fraction = progress * index / max(1.0, float(samples - 1))
            point = self.point_at(fraction)
            points.append((dunya_ekran_x(point.x), dunya_ekran_y(point.y)))
        color = (86, 0, 10) if silhouette else (101, 2, 15)
        width = max(1, int(round(self.width * KAMERA_YAKINLASTIRMA)))
        if len(points) >= 2:
            pygame.draw.lines(ekran, color, False, points, width)
        if points:
            pygame.draw.circle(ekran, color, points[-1], max(1, width // 2 + 1))


def v89_maybe_start_rivulet(decal, scale):
    if decal is None or len(v89_rivulets) >= 12 or float(scale) < 0.58:
        return
    now = pygame.time.get_ticks()
    cell = v89_blood_tile_key_at(decal.x, decal.y)
    if now < int(v89_rivulet_cell_next_ms.get(cell, 0)):
        return

    chance = min(0.52, 0.11 + float(scale) * 0.16)
    if random.random() > chance:
        return
    particle = globals().get("v74_current_particle")
    direction = getattr(particle, "v", None) if particle is not None else None
    if direction is None or pygame.Vector2(direction).length_squared() <= 1e-8:
        direction = pygame.Vector2(1.0, 0.0).rotate(random.uniform(0.0, 360.0))
    seed = int(float(decal.x) * 131 + float(decal.y) * 197 + now)
    v89_rivulets.append(
        V89BloodRivulet((decal.x, decal.y), direction, scale, now, seed)
    )
    v89_rivulet_cell_next_ms[cell] = now + 620
    v89_stats["rivulets"] += 1


_v89_create_decal_raw = v74_create_persistent_decal


def v74_create_persistent_decal(x, y, scale=None, rotation=None):
    decal = _v89_create_decal_raw(x, y, scale=scale, rotation=rotation)
    if decal is None:
        return None
    v89_decal_defaults(decal)
    v89_blood_tile_dirty_at(decal.x, decal.y)
    v89_maybe_start_rivulet(
        decal,
        float(scale if scale is not None else getattr(decal, "scale", 0.55)),
    )
    return decal


_v89_set_blood_mass_raw = v75_set_blood_mass


def v75_set_blood_mass(decal, mass):

    value = _v89_set_blood_mass_raw(
        decal,
        max(V89_BLOOD_RESIDUE_MASS, float(mass)),
    )
    decal.v75_ecology_consumed = False
    return value
# </POTBO_STAGE S2072>

# <POTBO_STAGE S2074>




V49_DECAL_HARD_LIMIT = 2**60


def v89_tile_objects(tile_x, tile_y):
    origin_x = tile_x * V89_BLOOD_TILE_WORLD
    origin_y = tile_y * V89_BLOOD_TILE_WORLD
    cell = float(V40_BLOOD_GRID_CELL)
    cx0 = int(math.floor(origin_x / cell))
    cx1 = int(math.floor((origin_x + V89_BLOOD_TILE_WORLD - 0.001) / cell))
    cy0 = int(math.floor(origin_y / cell))
    cy1 = int(math.floor((origin_y + V89_BLOOD_TILE_WORLD - 0.001) / cell))
    decals = []
    seen = set()
    for cy in range(cy0, cy1 + 1):
        for cx in range(cx0, cx1 + 1):
            for decal in v40_blood_grid.get((cx, cy), ()):
                did = id(decal)
                if did in seen:
                    continue
                if (
                    origin_x <= float(decal.x) < origin_x + V89_BLOOD_TILE_WORLD
                    and origin_y <= float(decal.y) < origin_y + V89_BLOOD_TILE_WORLD
                ):
                    seen.add(did)
                    decals.append(decal)
    footprints = list(v89_footprint_grid.get((tile_x, tile_y), ()))
    return decals, footprints


def v89_build_blood_tile(tile_x, tile_y, zoom, silhouette, now):
    origin_x = tile_x * V89_BLOOD_TILE_WORLD
    origin_y = tile_y * V89_BLOOD_TILE_WORLD
    extent = V89_BLOOD_TILE_WORLD + V89_BLOOD_TILE_PAD * 2.0
    size = max(2, int(math.ceil(extent * zoom)))
    surface = pygame.Surface((size, size), pygame.SRCALPHA).convert_alpha()
    decals, footprints = v89_tile_objects(tile_x, tile_y)
    objects = [
        (int(getattr(item, "created_ms", 0)), 0, item) for item in decals
    ] + [
        (int(getattr(item, "created_ms", 0)), 1, item) for item in footprints
    ]
    objects.sort(key=lambda row: (row[0], row[1]))
    next_refresh = 2**62
    for _created, kind, item in objects:
        if kind == 0:
            image = v89_decal_image(item, now, silhouette, zoom)
        else:
            image = v89_footprint_image(item, now, silhouette, zoom)
        local_x = (float(item.x) - origin_x + V89_BLOOD_TILE_PAD) * zoom
        local_y = (float(item.y) - origin_y + V89_BLOOD_TILE_PAD) * zoom
        surface.blit(image, image.get_rect(center=(int(round(local_x)), int(round(local_y)))))
        next_refresh = min(next_refresh, v89_blood_next_visual_change(item, now))
    v89_stats["tile_builds"] += 1
    return {
        "surface": surface,
        "revision": int(v89_blood_tile_revision.get((tile_x, tile_y), 0)),
        "next_refresh": int(next_refresh),
        "object_count": len(objects),
        "last_used": 0,
    }


def v89_blood_tile_get(tile_x, tile_y, zoom, silhouette, now):
    global v89_tile_use_serial
    tile = (tile_x, tile_y)
    key = (tile_x, tile_y, round(float(zoom), 3), bool(silhouette))
    decals, footprints = v89_tile_objects(tile_x, tile_y)
    object_count = len(decals) + len(footprints)
    entry = v89_blood_tile_cache.get(key)
    revision = int(v89_blood_tile_revision.get(tile, 0))
    if (
        entry is None
        or int(entry["revision"]) != revision
        or int(entry["object_count"]) != object_count
        or int(now) >= int(entry["next_refresh"])
    ):
        entry = v89_build_blood_tile(tile_x, tile_y, zoom, silhouette, now)
        v89_blood_tile_cache[key] = entry
    v89_tile_use_serial += 1
    entry["last_used"] = v89_tile_use_serial
    if len(v89_blood_tile_cache) > V89_BLOOD_TILE_CACHE_LIMIT:
        excess = len(v89_blood_tile_cache) - V89_BLOOD_TILE_CACHE_LIMIT
        oldest = sorted(
            v89_blood_tile_cache,
            key=lambda item: int(v89_blood_tile_cache[item]["last_used"]),
        )[:excess]
        for old_key in oldest:
            v89_blood_tile_cache.pop(old_key, None)
    return entry["surface"]


def kan_lekelerini_ciz(silhouette=False):
    zoom = max(0.01, float(KAMERA_YAKINLASTIRMA))
    now = pygame.time.get_ticks()
    left = float(kamera_x) - V89_BLOOD_TILE_PAD
    top = float(kamera_y) - V89_BLOOD_TILE_PAD
    right = float(kamera_x) + GENISLIK / zoom + V89_BLOOD_TILE_PAD
    bottom = float(kamera_y) + YUKSEKLIK / zoom + V89_BLOOD_TILE_PAD
    tx0 = int(math.floor(left / V89_BLOOD_TILE_WORLD))
    tx1 = int(math.floor(right / V89_BLOOD_TILE_WORLD))
    ty0 = int(math.floor(top / V89_BLOOD_TILE_WORLD))
    ty1 = int(math.floor(bottom / V89_BLOOD_TILE_WORLD))
    blits = []
    for tile_y in range(ty0, ty1 + 1):
        for tile_x in range(tx0, tx1 + 1):
            surface = v89_blood_tile_get(tile_x, tile_y, zoom, silhouette, now)
            world_x = tile_x * V89_BLOOD_TILE_WORLD - V89_BLOOD_TILE_PAD
            world_y = tile_y * V89_BLOOD_TILE_WORLD - V89_BLOOD_TILE_PAD
            destination = (
                int(round((world_x - float(kamera_x)) * zoom)),
                int(round((world_y - float(kamera_y)) * zoom)),
            )
            blits.append((surface, destination))
    if blits:
        ekran.blits(blits, doreturn=0)
        v89_stats["tile_blits"] += len(blits)
    for rivulet in v89_rivulets:
        if rivulet.active:
            rivulet.draw(now, silhouette=silhouette)
    v58_draw(ekran, silhouette=silhouette)


_v89_clear_blood_world_raw = kan_gore_dunyasini_temizle


def kan_gore_dunyasini_temizle():
    global v89_player_foot_last_pos, v89_player_foot_distance
    global v89_player_sole_load
    result = _v89_clear_blood_world_raw()
    v89_footprint_grid.clear()
    v89_rivulets.clear()
    v89_rivulet_cell_next_ms.clear()
    v89_blood_tile_cache.clear()
    v89_blood_tile_revision.clear()
    v89_player_foot_last_pos = None
    v89_player_foot_distance = 0.0
    v89_player_sole_load = 0.0
    return result
# </POTBO_STAGE S2074>

# <POTBO_STAGE S2076>
V89_FIRE_BLOOD_RADIUS = 34.0
# </POTBO_STAGE S2076>

# <POTBO_STAGE S2078>



BLOOD_MAGGOT_MAX = V89_MAGGOT_MAX
BLOOD_MAGGOT_FIRST_MIN_MS = 90_000
BLOOD_MAGGOT_FIRST_MAX_MS = 180_000
BLOOD_MAGGOT_WAVE_MIN_MS = 105_000
BLOOD_MAGGOT_WAVE_MAX_MS = 210_000
# </POTBO_STAGE S2078>

# <POTBO_STAGE S2082>


def v89_fire_affect_world(x, y, radius=V89_FIRE_BLOOD_RADIUS, now=None):
    if now is None:
        now = pygame.time.get_ticks()
    center = pygame.Vector2(float(x), float(y))
    radius = max(4.0, float(radius))
    radius2 = radius * radius



    for decal in _v40_blood_nearby(center, radius + 12.0):
        dx = float(decal.x) - center.x
        dy = float(decal.y) - center.y
        if dx * dx + dy * dy > radius2:
            continue
        previous = float(getattr(decal, "v89_scorch", 0.0))
        distance_ratio = math.sqrt(dx * dx + dy * dy) / max(1.0, radius)
        heat = max(0.025, 0.12 * (1.0 - 0.65 * distance_ratio))
        decal.v89_scorch = min(1.0, previous + heat)
        decal.dry_after_ms = min(int(getattr(decal, "dry_after_ms", now)), int(now))
        decal.fade_after_ms = max(int(now), int(getattr(decal, "fade_after_ms", now)))
        decal.vanish_after_ms = 2**62
        mass = max(
            V89_BLOOD_RESIDUE_MASS,
            float(getattr(decal, "v75_ecology_mass", v75_blood_mass(decal)))
            * (1.0 - heat * 0.52),
        )
        decal.v75_ecology_mass = mass
        decal.v75_ecology_consumed = False
        if previous < 0.70 <= decal.v89_scorch:
            v89_stats["blood_scorched"] += 1
        v89_blood_tile_dirty_at(decal.x, decal.y)

    tx0 = int(math.floor((center.x - radius) / V89_BLOOD_TILE_WORLD))
    tx1 = int(math.floor((center.x + radius) / V89_BLOOD_TILE_WORLD))
    ty0 = int(math.floor((center.y - radius) / V89_BLOOD_TILE_WORLD))
    ty1 = int(math.floor((center.y + radius) / V89_BLOOD_TILE_WORLD))
    for tile_y in range(ty0, ty1 + 1):
        for tile_x in range(tx0, tx1 + 1):
            for print_item in v89_footprint_grid.get((tile_x, tile_y), ()):
                if center.distance_squared_to((print_item.x, print_item.y)) > radius2:
                    continue
                print_item.v89_scorch = min(
                    1.0,
                    float(getattr(print_item, "v89_scorch", 0.0)) + 0.18,
                )
                print_item.dry_after_ms = min(int(print_item.dry_after_ms), int(now))
                v89_blood_tile_dirty_at(print_item.x, print_item.y)




    for maggot in blood_maggots:
        if not getattr(maggot, "active", False):
            continue
        if center.distance_squared_to((float(maggot.x), float(maggot.y))) <= radius2:
            maggot.active = False
            v89_stats["maggots_burned"] += 1
    for organ in gore_chunks:
        if getattr(organ, "v40_consumed", False):
            continue
        if str(getattr(organ, "kind", "")) not in V40_RAT_EDIBLE_GORE:
            continue
        if center.distance_squared_to((float(organ.x), float(organ.y))) > radius2:
            continue
        if not getattr(organ, "v89_charred", False):
            v89_stats["organs_burned"] += 1
        organ.v89_charred = True
        organ.v75_ecology_mass = max(
            0.06,
            v75_gore_mass(organ) * 0.82,
        )
# </POTBO_STAGE S2082>

# <POTBO_STAGE S2084>


def _v89_maggot_init(self, decal, simdi):
    _v89_maggot_init_raw(self, decal, simdi)
    self.v89_energy = random.uniform(0.0, 0.004)
    self.v89_food_kind = None
    self.v89_food_obj = None
    self.v89_feed_next_ms = int(simdi) + random.randint(520, 1200)
    self.v89_reproduce_next_ms = int(simdi) + random.randint(
        V89_MAGGOT_REPRODUCTION_MIN_MS,
        V89_MAGGOT_REPRODUCTION_MAX_MS,
    )
    self.v89_generation = int(getattr(self, "v89_generation", 0))


def v89_maggot_find_food(maggot, now):
    here = pygame.Vector2(float(maggot.x), float(maggot.y))
    best = None
    best_score = float("inf")
    for organ in gore_chunks[-180:]:
        if getattr(organ, "v40_consumed", False) or getattr(organ, "v89_charred", False):
            continue
        if str(getattr(organ, "kind", "")) not in V40_RAT_EDIBLE_GORE:
            continue
        position = pygame.Vector2(float(organ.x), float(organ.y))
        distance = here.distance_to(position)
        if distance <= 92.0 and distance * 0.58 < best_score:
            best = ("gore", organ, position)
            best_score = distance * 0.58
    for decal in _v40_blood_nearby(here, 62.0):
        if v89_blood_wetness(decal, now) <= 0.08:
            continue
        mass = float(getattr(decal, "v75_ecology_mass", v75_blood_mass(decal)))
        if mass <= V89_BLOOD_RESIDUE_MASS + 0.002:
            continue
        position = pygame.Vector2(float(decal.x), float(decal.y))
        distance = here.distance_to(position)
        score = distance + 12.0
        if distance <= 62.0 and score < best_score:
            best = ("blood", decal, position)
            best_score = score
    return best


def v89_maggot_feed(maggot, now):
    food = v89_maggot_find_food(maggot, now)
    if food is None:
        maggot.v89_food_kind = None
        maggot.v89_food_obj = None
        return 0.0
    kind, obj, position = food
    maggot.v89_food_kind = kind
    maggot.v89_food_obj = obj
    maggot.anchor_x = float(position.x)
    maggot.anchor_y = float(position.y)
    if pygame.Vector2(float(maggot.x), float(maggot.y)).distance_to(position) > 17.0:
        maggot.target = position
        maggot.next_target_ms = int(now) + 480
        return 0.0
    if kind == "blood":
        mass = float(getattr(obj, "v75_ecology_mass", v75_blood_mass(obj)))
        available = max(0.0, mass - V89_BLOOD_RESIDUE_MASS)
        consumed = min(available, random.uniform(0.0011, 0.0019))
        obj.v75_ecology_mass = max(V89_BLOOD_RESIDUE_MASS, mass - consumed)
        obj.v75_ecology_consumed = False
        v75_stats["maggot_blood_consumed"] += consumed
        return consumed
    mass = v75_gore_mass(obj)
    consumed = min(mass, random.uniform(0.0018, 0.0030))
    mass = max(0.0, mass - consumed)
    obj.v75_ecology_mass = mass
    initial = max(0.001, float(getattr(obj, "v75_ecology_mass_initial", mass + consumed)))
    initial_scale = max(
        0.04,
        float(getattr(obj, "v75_ecology_scale_initial", getattr(obj, "scale", 0.4))),
    )
    obj.scale = max(0.045, initial_scale * (0.26 + 0.74 * math.sqrt(mass / initial)))
    if mass <= 0.006:
        obj.v40_consumed = True
        maggot.v89_food_kind = None
        maggot.v89_food_obj = None
        v75_stats["gore_consumed"] += 1
    return consumed


def _v89_maggot_update(self, dt, simdi):
    if not getattr(self, "active", False):
        return
    _v89_maggot_motion_raw(self, dt, simdi)
    if not getattr(self, "active", False) or oyuncu_hp <= 0:
        return
    fire = v89_nearest_fire((self.x, self.y), 42.0)
    if fire is not None:
        self.active = False
        v89_stats["maggots_burned"] += 1
        return
    if int(simdi) >= int(getattr(self, "v89_feed_next_ms", 0)):
        self.v89_feed_next_ms = int(simdi) + V89_MAGGOT_FEED_INTERVAL_MS
        consumed = v89_maggot_feed(self, simdi)
        self.v89_energy = min(0.04, float(getattr(self, "v89_energy", 0.0)) + consumed)
    if (
        int(simdi) >= int(getattr(self, "v89_reproduce_next_ms", 0))
        and float(getattr(self, "v89_energy", 0.0)) >= 0.014
        and sum(1 for item in blood_maggots if getattr(item, "active", False))
        < V89_MAGGOT_MAX
    ):
        source = getattr(self, "source_decal", None)
        if source in blood_decals and v89_blood_wetness(source, simdi) > 0.06:
            child = BloodMaggot(source, simdi)
            child.x = float(self.x) + random.uniform(-3.0, 3.0)
            child.y = float(self.y) + random.uniform(-2.0, 2.0)
            child.v89_generation = int(getattr(self, "v89_generation", 0)) + 1
            blood_maggots.append(child)
            self.v89_energy *= 0.34
            v89_stats["maggots_born"] += 1
        self.v89_reproduce_next_ms = int(simdi) + random.randint(
            V89_MAGGOT_REPRODUCTION_MIN_MS,
            V89_MAGGOT_REPRODUCTION_MAX_MS,
        )
# </POTBO_STAGE S2084>

# <POTBO_STAGE S2087>


def _v89_rat_find_food(self, here, simdi):
    here = pygame.Vector2(here)
    if v89_nearest_fire(here, 118.0) is not None:
        self.food_kind = None
        self.food_obj = None
        return
    candidates = []
    for maggot in blood_maggots:
        if not getattr(maggot, "active", False):
            continue
        position = pygame.Vector2(float(maggot.x), float(maggot.y))
        distance = here.distance_to(position)
        if distance <= 470.0 and v89_nearest_fire(position, 56.0) is None:
            candidates.append((distance * 0.42, "maggot", maggot, position))
    for organ in gore_chunks[-180:]:
        if getattr(organ, "v40_consumed", False) or getattr(organ, "v89_charred", False):
            continue
        if str(getattr(organ, "kind", "")) not in V40_RAT_EDIBLE_GORE:
            continue
        position = pygame.Vector2(float(organ.x), float(organ.y))
        distance = here.distance_to(position)
        if distance <= 520.0 and v89_nearest_fire(position, 64.0) is None:
            candidates.append((distance * 0.70 + 18.0, "gore", organ, position))
    if not candidates:
        self.food_kind = None
        self.food_obj = None
        return
    candidates.sort(key=lambda item: item[0])
    best = candidates[0]
    self.food_kind = best[1]
    self.food_obj = best[2]
    self.last_food_pos = pygame.Vector2(best[3])
# </POTBO_STAGE S2087>

# <POTBO_STAGE S2091>


def _v89_ground_fire_update(self, simdi):
    result = _v89_ground_fire_update_raw(self, simdi)
    if getattr(self, "active", False) and int(simdi) >= int(
        getattr(self, "v89_ecology_next_ms", 0)
    ):
        self.v89_ecology_next_ms = int(simdi) + V89_FIRE_ECOLOGY_INTERVAL_MS
        v89_fire_affect_world(self.x, self.y, V89_FIRE_BLOOD_RADIUS, simdi)
    return result
# </POTBO_STAGE S2091>

# <POTBO_STAGE S2095>





_v89_blood_emit_raw = kan_parcacigi_patlat


def kan_parcacigi_patlat(x, y, adet, guc=1.0, yon=None, arterial=False):
    before = len(blood_particles)
    result = _v89_blood_emit_raw(
        x,
        y,
        adet,
        guc,
        yon=yon,
        arterial=arterial,
    )
    created = list(blood_particles[before:])
    per_burst = (
        V89_BLOOD_ARTERIAL_BURST_LIMIT if arterial else V89_BLOOD_BURST_LIMIT
    )
    available = max(0, V89_BLOOD_TRANSIENT_LIMIT - before)
    keep_count = min(len(created), per_burst, available)
    if len(created) <= keep_count:
        return result




    if keep_count > 0:
        kept = []
        for index in range(keep_count):
            source_index = min(
                len(created) - 1,
                int(round(index * (len(created) - 1) / max(1.0, keep_count - 1))),
            )
            kept.append(created[source_index])
    else:
        kept = []
    removed_count = len(created) - len(kept)
    blood_particles[before:] = kept

    direction = pygame.Vector2(yon) if yon is not None else pygame.Vector2()
    if direction.length_squared() <= 1e-8 and created:
        for particle in created:
            direction += pygame.Vector2(getattr(particle, "v", (0.0, 0.0)))
    if direction.length_squared() <= 1e-8:
        direction = pygame.Vector2(1.0, 0.0).rotate(random.uniform(0.0, 360.0))
    else:
        direction = direction.normalize()
    landing_count = min(18, max(1, int(math.ceil(removed_count / 6.0))))
    scheduled = v87_schedule_blood_landings(
        (float(x), float(y) + 3.0),
        direction,
        landing_count,
        min(44.0, 14.0 + max(0.5, float(guc)) * 18.0),
        (
            0.08,
            min(0.72, 0.20 + max(0.5, float(guc)) * 0.22),
        ),
        "v89_collapsed_air",
        now=pygame.time.get_ticks(),
        cone_deg=104.0 if arterial else 78.0,
        delay_range=(210, 820),
        seed=int(float(x) * 79 + float(y) * 137 + removed_count * 911),
    )
    v89_stats["air_particles_collapsed"] += removed_count
    v89_stats["permanent_landings_scheduled"] += scheduled
    return result


_v89_gore_update_raw = kan_gore_guncelle


def kan_gore_guncelle():
    result = _v89_gore_update_raw()
    now = pygame.time.get_ticks()
    for rivulet in list(v89_rivulets):
        rivulet.update(now)
    v89_rivulets[:] = [item for item in v89_rivulets if item.active]
    v89_player_footprints_update(now)
    return result





V89_BLOOD_SAVE_KEY = "blood_ecology_v89"


def v89_complete_active_rivulets():
    for rivulet in list(v89_rivulets):
        rivulet.update(rivulet.start_ms + rivulet.duration_ms + 1)
        rivulet.active = False
    v89_rivulets.clear()


def v89_blood_snapshot():
    v89_complete_active_rivulets()
    now = pygame.time.get_ticks()
    decals = []
    for decal in blood_decals:
        created = int(getattr(decal, "created_ms", now))
        dry_after = int(getattr(decal, "dry_after_ms", created + V75_BLOOD_FULL_DRY_MS))
        decals.append(
            [
                round(float(decal.x), 2),
                round(float(decal.y), 2),
                round(float(getattr(decal, "scale", 0.55)), 4),
                round(float(getattr(decal, "rotation", 0.0)), 1),
                int(getattr(decal, "sprite_index", 0)),
                max(0, int(now) - created),
                max(1, dry_after - created),
                round(float(getattr(decal, "v89_scorch", 0.0)), 3),
                round(
                    max(
                        V89_BLOOD_RESIDUE_MASS,
                        float(getattr(decal, "v75_ecology_mass", v75_blood_mass(decal))),
                    ),
                    4,
                ),
                int(getattr(decal, "v44_seed", 0)),
                round(float(getattr(decal, "v44_oxygenation", 0.46)), 3),
            ]
        )
    footprints = []
    for items in v89_footprint_grid.values():
        for print_item in items:
            created = int(print_item.created_ms)
            footprints.append(
                [
                    round(float(print_item.x), 2),
                    round(float(print_item.y), 2),
                    round(float(print_item.angle), 1),
                    int(print_item.side),
                    round(float(print_item.intensity), 3),
                    max(0, int(now) - created),
                    max(1, int(print_item.dry_after_ms) - created),
                    round(float(getattr(print_item, "v89_scorch", 0.0)), 3),
                ]
            )
    return {
        "version": V89_VERSION,
        "decals": decals,
        "footprints": footprints,
    }


def v89_restore_blood_snapshot(payload):
    if not isinstance(payload, dict):
        return False
    now = pygame.time.get_ticks()
    restored = 0
    for row in payload.get("decals", []):
        if not isinstance(row, (list, tuple)) or len(row) < 9:
            continue
        try:
            decal = _v89_create_decal_raw(
                float(row[0]),
                float(row[1]),
                float(row[2]),
                rotation=float(row[3]),
            )
        except (TypeError, ValueError):
            continue
        if decal is None:
            continue
        v89_decal_defaults(decal)
        decal.sprite_index = int(row[4])
        age = max(0, int(row[5]))
        dry_span = max(1, int(row[6]))
        decal.created_ms = int(now) - age
        decal.dry_after_ms = decal.created_ms + dry_span
        decal.fade_after_ms = decal.dry_after_ms + V75_BLOOD_POST_DRY_COLOR_MS
        decal.vanish_after_ms = 2**62
        decal.v89_scorch = v89_clamp01(row[7])
        decal.v75_ecology_mass = max(V89_BLOOD_RESIDUE_MASS, float(row[8]))
        decal.v75_ecology_mass_initial = max(
            decal.v75_ecology_mass,
            float(getattr(decal, "v75_ecology_mass_initial", decal.v75_ecology_mass)),
        )
        if len(row) > 9 and int(row[9]) != 0:
            decal.v44_seed = int(row[9])
            decal.v62_seed = int(row[9])
        if len(row) > 10:
            decal.v44_oxygenation = v89_clamp01(row[10])
            decal.v44_tone = v44_blood_palette_for(
                oxygenation=decal.v44_oxygenation
            )
        v89_blood_tile_dirty_at(decal.x, decal.y)
        restored += 1
    for row in payload.get("footprints", []):
        if not isinstance(row, (list, tuple)) or len(row) < 8:
            continue
        try:
            age = max(0, int(row[5]))
            dry_span = max(1, int(row[6]))
            item = V89BloodFootprint(
                float(row[0]),
                float(row[1]),
                float(row[2]),
                int(row[3]),
                float(row[4]),
                int(now) - age,
            )
            item.created_ms = int(now) - age
            item.dry_after_ms = item.created_ms + dry_span
            item.v89_scorch = v89_clamp01(row[7])
        except (TypeError, ValueError):
            continue
        tile = v89_blood_tile_key_at(item.x, item.y)
        v89_footprint_grid.setdefault(tile, []).append(item)
        v89_blood_tile_dirty_at(item.x, item.y)
    return restored > 0 or bool(payload.get("footprints"))
# </POTBO_STAGE S2095>

# <POTBO_STAGE S2097>


def oyun_kaydet(*args, **kwargs):
    result = _v89_save_game_raw(*args, **kwargs)
    if not result or not aktif_kayit:
        return result
    try:
        with open(aktif_kayit, "r", encoding="utf-8") as source:
            payload = json.load(source)
        payload[V89_BLOOD_SAVE_KEY] = v89_blood_snapshot()
        _v34_json_atomic_write(aktif_kayit, payload, indent=4)
    except (OSError, ValueError, TypeError) as exc:
        debug_log("V89 blood save failed:", exc)
        return False
    return True
# </POTBO_STAGE S2097>

# <POTBO_STAGE S2099>


def oyun_yukle(*args, **kwargs):
    preserve_gore = bool(kwargs.get("gore_koru", False))
    if len(args) >= 2:
        preserve_gore = bool(args[1])
    result = _v89_load_game_raw(*args, **kwargs)
    if not result or preserve_gore or not args:
        return result
    try:
        with open(args[0], "r", encoding="utf-8") as source:
            payload = json.load(source)
        v89_restore_blood_snapshot(payload.get(V89_BLOOD_SAVE_KEY, {}))
    except (OSError, ValueError, TypeError) as exc:
        debug_log("V89 blood load failed:", exc)
    return result
# </POTBO_STAGE S2099>

# <POTBO_STAGE S2108>


def one_cikan_item_paneli_ciz():
    panel = hud_sag_rect()
    v89_medieval_panel(panel, V89_UI_BLOOD)
    yazi_yaz(
        bt("HIZLI ERİŞİM", "QUICK BELT"),
        panel.centerx,
        panel.y + 18,
        V89_UI_PARCHMENT,
        mini_font,
        True,
    )
    slot_size = 56
    gap = 8
    separator = 18
    total = slot_size * 6 + gap * 4 + separator
    start_x = panel.centerx - total // 2
    y = panel.y + 46
    for index in range(5):
        rect = pygame.Rect(
            start_x + index * (slot_size + gap),
            y,
            slot_size,
            slot_size,
        )
        v85_slot_shell(rect, selected=index == envanter_secili_slot)
        v85_slot_contents(rect, index + 1, one_cikan_slotlar[index])
    separator_x = start_x + slot_size * 5 + gap * 4 + separator // 2
    pygame.draw.line(
        ekran,
        V89_UI_BRASS,
        (separator_x, y - 4),
        (separator_x, y + slot_size + 4),
        1,
    )
    q_rect = pygame.Rect(
        start_x + slot_size * 5 + gap * 4 + separator,
        y,
        slot_size,
        slot_size,
    )
    v89_q_slot_draw(q_rect)
# </POTBO_STAGE S2108>

# <POTBO_STAGE S2110>


def one_cikan_atama_penceresi_ciz(panel):
    if one_cikan_atama_item_index is None:
        return
    modal = pygame.Rect(panel.centerx - 300, panel.centery - 105, 600, 210)
    v89_medieval_panel(modal, V89_UI_BLOOD, 252)
    yazi_yaz(
        bt("KEMER SLOTLARINDAN BİRİNİ SEÇ", "CHOOSE A BELT SLOT"),
        modal.centerx,
        modal.y + 31,
        V89_UI_PARCHMENT,
        normal_font,
        True,
    )
    slot_size = 72
    gap = 24
    total = slot_size * 5 + gap * 4
    start_x = modal.centerx - total // 2
    y = modal.y + 84
    current = next(
        (index for index, value in enumerate(one_cikan_slotlar) if value == one_cikan_atama_item_index),
        None,
    )
    for index in range(5):
        rect = pygame.Rect(start_x + index * (slot_size + gap), y, slot_size, slot_size)
        v85_slot_shell(rect, selected=index == current)
        v85_slot_contents(rect, index + 1, one_cikan_slotlar[index])
# </POTBO_STAGE S2110>

# <POTBO_STAGE S2117>


def v89_smoke_test(output_prefix):
    global oyun_durumu, ekran
    started = pygame.time.get_ticks()
    print("[V89 SMOKE] seed")


    ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
    original_state = oyun_durumu
    center = pygame.Vector2(
        float(kamera_x) + GENISLIK / max(0.01, KAMERA_YAKINLASTIRMA) * 0.50,
        float(kamera_y) + YUKSEKLIK / max(0.01, KAMERA_YAKINLASTIRMA) * 0.56,
    )
    if not v74_floor_clean(center.x, center.y):
        for radius in range(24, 420, 18):
            candidate = pygame.Vector2(oyuncu_x, oyuncu_y) + pygame.Vector2(radius, 0).rotate(radius * 2.7)
            if v74_floor_clean(candidate.x, candidate.y):
                center = candidate
                break
    for index in range(220):
        angle = index * 137.507764
        radius = 5.0 + math.sqrt(index) * 5.6
        point = center + pygame.Vector2(radius, 0.0).rotate(angle)
        if not v74_floor_clean(point.x, point.y):
            continue
        decal = _v89_create_decal_raw(
            point.x,
            point.y,
            0.12 + (index % 9) * 0.075,
            rotation=angle,
        )
        if decal is not None:
            v89_decal_defaults(decal)
            decal.created_ms -= (index % 6) * 240_000
            decal.dry_after_ms = decal.created_ms + V75_BLOOD_FULL_DRY_MS
            v89_blood_tile_dirty_at(decal.x, decal.y)
    for index in range(14):
        point = center + pygame.Vector2(index * 13.0 - 82.0, 54.0 + (index % 2) * 7.0)
        v89_add_footprint(point.x, point.y, 90.0, -1 if index % 2 else 1, 0.92 - index * 0.05, pygame.time.get_ticks())



    snapshot = v89_blood_snapshot()
    persistence_before = (
        len(blood_decals),
        sum(len(items) for items in v89_footprint_grid.values()),
    )
    kan_gore_dunyasini_temizle()
    persistence_restored = v89_restore_blood_snapshot(snapshot)
    persistence_after = (
        len(blood_decals),
        sum(len(items) for items in v89_footprint_grid.values()),
    )

    stain_count_before_fire = len(blood_decals)
    v89_fire_affect_world(center.x + 42.0, center.y, 40.0, pygame.time.get_ticks())
    fire_preserved_stain_count = len(blood_decals) == stain_count_before_fire

    collapsed_before = v89_stats["air_particles_collapsed"]
    kan_parcacigi_patlat(
        center.x,
        center.y,
        180,
        guc=1.15,
        yon=(1.0, 0.0),
        arterial=True,
    )
    transient_budget_ok = len(blood_particles) <= V89_BLOOD_TRANSIENT_LIMIT
    collapse_exercised = v89_stats["air_particles_collapsed"] > collapsed_before

    print("[V89 SMOKE] render hud")
    ekran.fill((39, 31, 24))
    first_render_started = time.perf_counter()
    kan_lekelerini_ciz(False)
    first_blood_render_ms = (time.perf_counter() - first_render_started) * 1000.0


    ekran.fill((39, 31, 24))
    warm_render_started = time.perf_counter()
    kan_lekelerini_ciz(False)
    warm_blood_render_ms = (time.perf_counter() - warm_render_started) * 1000.0
    if V89_GROUND_FIRE_FRAMES:
        patch = GroundFirePatch(center.x + 42.0, center.y, pygame.time.get_ticks(), 0)
        patch.start_ms -= 320
        patch.ciz()
    oyuncu_paneli_ciz()
    one_cikan_item_paneli_ciz()
    hud_path = str(output_prefix) + "_hud.png"
    pygame.image.save(ekran, hud_path)

    print("[V89 SMOKE] render inventory")
    if V89_SMALL_FIRE_FRAMES:
        ITEM_RESIMLERI["fire_magic"] = V89_SMALL_FIRE_FRAMES[0]
    if not isinstance(envanter_itemleri[0], dict):
        envanter_itemleri[0] = fire_magic_olustur()
    one_cikan_slotlar[0] = 0
    oyun_durumu = ENVANTER
    envanter_ciz()
    inventory_path = str(output_prefix) + "_inventory.png"
    pygame.image.save(ekran, inventory_path)
    oyun_durumu = original_state

    print("[V89 SMOKE] diagnostics")
    diagnostic = v89_diagnostics()
    diagnostic["smoke"] = {
        "startup_ok": bool(V89_STARTUP_OK),
        "render_ms": pygame.time.get_ticks() - started,
        "first_blood_render_ms": round(first_blood_render_ms, 3),
        "warm_blood_render_ms": round(warm_blood_render_ms, 3),
        "hud_preview": hud_path,
        "inventory_preview": inventory_path,
        "blood_survives_cleanup": v75_cleanup_consumed_blood(pygame.time.get_ticks()) == 0,
        "snapshot_roundtrip": bool(
            persistence_restored and persistence_before == persistence_after
        ),
        "fire_preserves_stain_count": bool(fire_preserved_stain_count),
        "transient_budget_ok": bool(transient_budget_ok),
        "collapse_exercised": bool(collapse_exercised),
    }
    return diagnostic
# </POTBO_STAGE S2117>

# <POTBO_STAGE S2138>






V90_BASE_WALK_SPEED = float(OYUNCU_YURUYUS_HIZI)
# </POTBO_STAGE S2138>

# <POTBO_STAGE S2143>


@dataclass
class V90InjuryState:
    tissue: float = 0.0
    haemorrhage: float = 0.0
    shock: float = 0.0
    exertion: float = 0.0
    last_damage_ms: int = -10000
    next_bleed_ms: int = 0
    next_rivulet_ms: int = 0
    last_hp: float = 0.0
    effective_stamina_ratio: float = 1.0
    stamina_regen_multiplier: float = 1.0
    movement_multiplier: float = 1.0
    attack_time_multiplier: float = 1.0

    def reset(self):
        self.tissue = 0.0
        self.haemorrhage = 0.0
        self.shock = 0.0
        self.exertion = 0.0
        self.last_damage_ms = -10000
        self.next_bleed_ms = 0
        self.next_rivulet_ms = 0
        self.last_hp = float(oyuncu_hp)
        self.effective_stamina_ratio = 1.0
        self.stamina_regen_multiplier = 1.0
        self.movement_multiplier = 1.0
        self.attack_time_multiplier = 1.0
# </POTBO_STAGE S2143>

# <POTBO_STAGE S2145>
v90_injury_stats = {
    "damage_events": 0,
    "critical_drops": 0,
    "critical_rivulets": 0,
    "healing_relief": 0.0,
}
# </POTBO_STAGE S2145>

# <POTBO_STAGE S2148>


def v90_injury_severity():
    missing = 1.0 - v90_hp_ratio()
    return v90_clamp(
        missing * 0.46
        + v90_injury.tissue * 0.28
        + v90_injury.haemorrhage * 0.17
        + v90_injury.shock * 0.09
    )
# </POTBO_STAGE S2148>

# <POTBO_STAGE S2150>


def v90_injury_register_damage(actual_damage, profile, now=None):
    global oyuncu_stamina, stamina_son_harcama
    actual_damage = max(0.0, float(actual_damage))
    if actual_damage <= 0.0:
        return
    if now is None:
        now = pygame.time.get_ticks()
    tissue_factor, blood_factor, shock_factor = v90_profile_factors(profile)
    ratio = actual_damage / max(1.0, float(oyuncu_max_hp))
    v90_injury.tissue = v90_clamp(v90_injury.tissue + ratio * tissue_factor * 0.88)
    v90_injury.haemorrhage = v90_clamp(
        v90_injury.haemorrhage + ratio * blood_factor * 0.72
    )
    v90_injury.shock = v90_clamp(v90_injury.shock + ratio * shock_factor * 0.74)
    v90_injury.exertion = v90_clamp(v90_injury.exertion + ratio * 0.44)
    v90_injury.last_damage_ms = int(now)
    v90_injury.last_hp = float(oyuncu_hp)


    stamina_loss = actual_damage * (0.12 + 0.11 * shock_factor)
    oyuncu_stamina = max(0.0, float(oyuncu_stamina) - stamina_loss)
    stamina_son_harcama = int(now)
    v90_injury_stats["damage_events"] += 1


def v90_injury_relieve(healed_hp):
    healed_hp = max(0.0, float(healed_hp))
    if healed_hp <= 0.0:
        return
    ratio = healed_hp / max(1.0, float(oyuncu_max_hp))
    v90_injury.tissue = max(0.0, v90_injury.tissue - ratio * 0.56)
    v90_injury.haemorrhage = max(0.0, v90_injury.haemorrhage - ratio * 0.92)
    v90_injury.shock = max(0.0, v90_injury.shock - ratio * 0.74)
    v90_injury.exertion = max(0.0, v90_injury.exertion - ratio * 0.45)
    v90_injury.last_hp = float(oyuncu_hp)
    v90_injury_stats["healing_relief"] += ratio
# </POTBO_STAGE S2150>

# <POTBO_STAGE S2152>


def v90_critical_bleed(now):
    hp_ratio = v90_hp_ratio()
    critical = v90_clamp((0.28 - hp_ratio) / 0.24)
    blood_drive = max(critical, v90_injury.haemorrhage * 0.70)
    if oyuncu_hp <= 0 or blood_drive < 0.18 or int(now) < v90_injury.next_bleed_ms:
        return
    interval = int(round(820 - 470 * v90_clamp(blood_drive)))
    v90_injury.next_bleed_ms = int(now) + max(300, interval)
    movement = pygame.Vector2(oyuncu_hareket_hiz_vektoru)
    if movement.length_squared() > 9.0:
        direction = -movement.normalize()
    else:
        direction = pygame.Vector2(1.0, 0.0).rotate((int(now) // 37) % 360)
    count = 2 + int(round(blood_drive * 3.0))
    kan_parcacigi_patlat(
        oyuncu_x,
        oyuncu_y - 7.0,
        count,
        guc=0.34 + 0.28 * blood_drive,
        yon=direction,
        arterial=blood_drive > 0.72,
    )


    point = pygame.Vector2(oyuncu_x, oyuncu_y) + direction * 6.0
    if v74_floor_clean(point.x, point.y):
        decal = _v89_create_decal_raw(
            point.x,
            point.y,
            0.10 + blood_drive * 0.16,
            rotation=math.degrees(math.atan2(direction.y, direction.x)),
        )
        if decal is not None:
            v89_decal_defaults(decal)
            v89_blood_tile_dirty_at(decal.x, decal.y)
    v90_injury_stats["critical_drops"] += 1

    if (
        blood_drive > 0.64
        and int(now) >= v90_injury.next_rivulet_ms
        and len(v89_rivulets) < 12
    ):
        v90_injury.next_rivulet_ms = int(now) + 2600
        v89_rivulets.append(
            V89BloodRivulet(
                (point.x, point.y),
                direction,
                0.62 + blood_drive * 0.22,
                now,
                int(now) ^ int(oyuncu_x * 17) ^ int(oyuncu_y * 31),
            )
        )
        v90_injury_stats["critical_rivulets"] += 1
# </POTBO_STAGE S2152>

# <POTBO_STAGE S2164>
v90_embers = []
# </POTBO_STAGE S2164>

# <POTBO_STAGE S2167>


@dataclass
class V90Ember:
    x: float
    y: float
    vx: float
    vy: float
    born_ms: int
    ttl_ms: int
    size: float
    seed: int

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vx *= math.exp(-2.6 * dt)
        self.vy -= 18.0 * dt

    def alive(self, now):
        return int(now) - int(self.born_ms) <= int(self.ttl_ms)
# </POTBO_STAGE S2167>

# <POTBO_STAGE S2173>


def v90_spawn_embers(position, count=5, seed=0, force=None):
    position = pygame.Vector2(position)
    rng = random.Random(int(seed) ^ int(position.x * 43) ^ int(position.y * 79))
    base = pygame.Vector2(force) if force is not None else pygame.Vector2()
    for _ in range(max(0, int(count))):
        direction = pygame.Vector2(1.0, 0.0).rotate(rng.uniform(0.0, 360.0))
        speed = rng.uniform(12.0, 44.0)
        velocity = direction * speed + base
        v90_embers.append(
            V90Ember(
                position.x + rng.uniform(-4.0, 4.0),
                position.y + rng.uniform(-7.0, 3.0),
                velocity.x,
                velocity.y - rng.uniform(6.0, 22.0),
                pygame.time.get_ticks(),
                rng.randint(380, 820),
                rng.uniform(1.2, 3.8),
                rng.randrange(1, 2**30),
            )
        )
    if len(v90_embers) > 180:
        del v90_embers[:-180]
# </POTBO_STAGE S2173>

# <POTBO_STAGE S2183>


def v90_ash_draw(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    zoom = max(0.01, float(KAMERA_YAKINLASTIRMA))
    margin = 30.0 / zoom
    left = float(kamera_x) - margin
    top = float(kamera_y) - margin
    right = float(kamera_x) + GENISLIK / zoom + margin
    bottom = float(kamera_y) + YUKSEKLIK / zoom + margin
    for mark in v90_ash_marks:
        if not (left <= mark.x <= right and top <= mark.y <= bottom):
            continue
        age = max(0, int(now) - int(mark.born_ms))
        fade = 1.0
        if age > mark.ttl_ms - 7000:
            fade = v90_clamp((mark.ttl_ms - age) / 7000.0)
        cx = int(round(dunya_ekran_x(mark.x)))
        cy = int(round(dunya_ekran_y(mark.y)))
        rx = max(3, int(round(11.0 * mark.scale * zoom)))
        ry = max(2, int(round(4.5 * mark.scale * zoom)))
        fade_bucket = max(0, min(8, int(round(fade * 8.0))))
        ember_bucket = 6 if age >= 4800 else max(0, min(5, age // 800))
        key = (mark.seed % 12, rx, ry, fade_bucket, ember_bucket)
        layer = v90_ash_cache.get(key)
        if layer is None:
            rng = random.Random(mark.seed % 12)
            pad = 4
            layer = pygame.Surface(
                (rx * 2 + pad * 2, ry * 2 + pad * 2), pygame.SRCALPHA
            )
            local_cx = rx + pad
            local_cy = ry + pad
            points = []
            for index in range(10):
                angle = index * math.tau / 10.0
                irregular = rng.uniform(0.68, 1.18)
                points.append(
                    (
                        local_cx + math.cos(angle) * rx * irregular,
                        local_cy + math.sin(angle) * ry * irregular,
                    )
                )
            pygame.draw.polygon(
                layer,
                (21, 17, 15, int(106 * fade_bucket / 8.0)),
                points,
            )

            if ember_bucket < 6:
                ember_alpha = int(150 * (1.0 - ember_bucket / 6.0))
                for _ in range(2):
                    pygame.draw.circle(
                        layer,
                        (214, 53, 6, ember_alpha),
                        (
                            local_cx
                            + rng.randint(-max(1, rx // 2), max(1, rx // 2)),
                            local_cy
                            + rng.randint(-max(1, ry // 2), max(1, ry // 2)),
                        ),
                        1,
                    )
            if len(v90_ash_cache) >= 360:
                for old_key in list(v90_ash_cache)[:90]:
                    v90_ash_cache.pop(old_key, None)
            v90_ash_cache[key] = layer
        ekran.blit(layer, layer.get_rect(center=(cx, cy)))
# </POTBO_STAGE S2183>

# <POTBO_STAGE S2188>


_v90_blood_world_update_raw = kan_gore_guncelle
# </POTBO_STAGE S2188>

# <POTBO_STAGE S2191>


_v90_blood_draw_raw = kan_lekelerini_ciz


def kan_lekelerini_ciz(silhouette=False):
    result = _v90_blood_draw_raw(silhouette)
    if not silhouette:
        v90_ash_draw(pygame.time.get_ticks())
    return result


_v90_world_draw_raw = dunya_aktorlerini_derinlige_gore_ciz


def dunya_aktorlerini_derinlige_gore_ciz():
    result = _v90_world_draw_raw()
    v90_draco_draw(pygame.time.get_ticks())
    return result
# </POTBO_STAGE S2191>

# <POTBO_STAGE S2193>


def oyuncu_paneli_ciz():
    result = _v90_player_panel_raw()
    if oyuncu_hp <= 0:
        return result
    panel = hud_sol_rect()
    severity = v90_injury_severity()
    hp_ratio = v90_hp_ratio()
    if hp_ratio <= 0.20:
        label = bt("KRİTİK · KANAMA", "CRITICAL · BLEEDING")
        color = (255, 69, 45)
    elif severity >= 0.52:
        label = bt("AĞIR YARALI", "SEVERELY WOUNDED")
        color = (223, 86, 42)
    elif severity >= 0.22:
        label = bt("YARALI", "WOUNDED")
        color = (206, 142, 63)
    else:
        label = ""
        color = V89_UI_PARCHMENT
    if label:
        pulse = 0.82 + 0.18 * math.sin(pygame.time.get_ticks() * 0.010)
        pulse_color = tuple(max(0, min(255, int(channel * pulse))) for channel in color)
        text_width = mini_font.size(label)[0]
        text_x = panel.right - text_width - 21
        pygame.draw.rect(
            ekran,
            (59, 39, 25),
            pygame.Rect(text_x - 3, panel.y + 38, text_width + 6, 18),
        )
        yazi_yaz(
            label,
            text_x,
            panel.y + 41,
            pulse_color,
            mini_font,
            False,
        )



    bar = pygame.Rect(panel.x + 22, panel.y + 84, panel.width - 44, 12)
    cap_x = bar.x + int(round(bar.width * v90_injury.effective_stamina_ratio))
    pygame.draw.line(
        ekran,
        (244, 215, 150),
        (cap_x, bar.y - 2),
        (cap_x, bar.bottom + 2),
        2,
    )
    return result
# </POTBO_STAGE S2193>

# <POTBO_STAGE S2196>


def v90_injury_snapshot():
    return {
        "version": V90_VERSION,
        "tissue": round(v90_injury.tissue, 5),
        "haemorrhage": round(v90_injury.haemorrhage, 5),
        "shock": round(v90_injury.shock, 5),
        "exertion": round(v90_injury.exertion, 5),
    }


def v90_injury_restore(payload):
    v90_injury.reset()
    if not isinstance(payload, dict):
        v90_injury_recalculate()
        return False
    try:
        v90_injury.tissue = v90_clamp(payload.get("tissue", 0.0))
        v90_injury.haemorrhage = v90_clamp(payload.get("haemorrhage", 0.0))
        v90_injury.shock = v90_clamp(payload.get("shock", 0.0))
        v90_injury.exertion = v90_clamp(payload.get("exertion", 0.0))
    except (TypeError, ValueError):
        v90_injury.reset()
        return False
    v90_injury.last_hp = float(oyuncu_hp)
    v90_injury_recalculate()
    return True
# </POTBO_STAGE S2196>

# <POTBO_STAGE S2207>


def v90_smoke_test(output_prefix):
    global ekran, oyun_durumu, oyun_alt_durumu
    global oyuncu_x, oyuncu_y, oyuncu_yonu, oyuncu_hp, oyuncu_stamina
    global oyuncu_mana, q_hizli_item_index, kamera_x, kamera_y

    ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
    original_state = oyun_durumu
    original_substate = oyun_alt_durumu
    original_camera = (kamera_x, kamera_y)
    oyun_durumu = OYUN
    oyun_alt_durumu = HARITA
    kamera_x = 0.0
    kamera_y = 0.0
    oyuncu_x = 470.0
    oyuncu_y = 360.0
    oyuncu_yonu = "right"
    oyuncu_hp = max(1, int(round(float(oyuncu_max_hp) * 0.12)))
    oyuncu_stamina = float(oyuncu_max_stamina)
    oyuncu_mana = max(float(oyuncu_max_mana), float(V90_DRACO_MANA_COST + 10))

    v90_injury.reset()
    oyuncu_kanli_hasar_kaydi(
        oyuncu_x + 18.0,
        oyuncu_y,
        "heavy_slash",
        18,
        "v90_smoke",
    )
    canonical_damage_registered = bool(
        v90_injury.tissue > 0.0
        and v90_injury.haemorrhage > 0.0
        and v90_injury.shock > 0.0
    )
    v90_injury.tissue = 0.72
    v90_injury.haemorrhage = 0.82
    v90_injury.shock = 0.54
    v90_injury.exertion = 0.38
    v90_injury.last_hp = float(oyuncu_hp)
    v90_injury_recalculate()
    injury_metrics = {
        "movement_multiplier": round(v90_injury.movement_multiplier, 4),
        "attack_time_multiplier": round(v90_injury.attack_time_multiplier, 4),
        "effective_stamina_ratio": round(
            v90_injury.effective_stamina_ratio, 4
        ),
        "regen_multiplier": round(v90_injury.stamina_regen_multiplier, 4),
    }
    injury_snapshot = v90_injury_snapshot()
    snapshot_values = (
        v90_injury.tissue,
        v90_injury.haemorrhage,
        v90_injury.shock,
        v90_injury.exertion,
    )
    v90_injury.reset()
    injury_restored = v90_injury_restore(injury_snapshot)
    restored_values = (
        v90_injury.tissue,
        v90_injury.haemorrhage,
        v90_injury.shock,
        v90_injury.exertion,
    )
    blood_before = len(blood_decals)
    v90_injury.next_bleed_ms = 0
    v90_critical_bleed(pygame.time.get_ticks() + 10)
    critical_bleed_created = len(blood_decals) > blood_before

    envanter_itemleri[0] = draco_calcinans_olustur()
    q_hizli_item_index = 0
    mana_before_cast = float(oyuncu_mana)
    stamina_before_cast = float(oyuncu_stamina)
    cast_via_q = bool(q_hizli_itemi_kullan())
    cast_costs_applied = bool(
        float(oyuncu_mana) == mana_before_cast - V90_DRACO_MANA_COST
        and abs(
            float(oyuncu_stamina)
            - (stamina_before_cast - V90_DRACO_STAMINA_COST)
        )
        <= 0.001
    )
    v90_draco_state.reset()
    cooldown_denied = not bool(q_hizli_itemi_kullan())

    target = CommonEnemy(
        "v90_smoke_target",
        "berserker",
        oyuncu_x + 238.0,
        oyuncu_y,
    )
    target.max_hp = 600
    target.hp = 600
    target.aggro = False
    common_enemies.append(target)
    fires_before = len(player_magic_ground_fires)
    base = pygame.time.get_ticks() + 100
    v90_draco_state.begin(base)
    phases = {v90_draco_state.phase}
    for offset in range(16, 2900, 16):
        now = base + offset
        v90_draco_state.update(now)
        v90_calcinatio_update(now, 0.016)
        phases.add(v90_draco_state.phase)
    target_hp_after_rupture = int(target.hp)
    status = v90_calcinatio.get(v84_actor_uid(target))
    physical_before = v90_draco_stats["physical_triggers"]
    if status is not None:
        status.next_physical_ms = 0
        target.hasar_al(20, None)
    physical_triggered = v90_draco_stats["physical_triggers"] > physical_before
    calcinatio_before = v90_draco_stats["calcinatio_ticks"]
    if status is not None and v90_actor_alive(target):
        status.next_tick_ms = 0
        v90_calcinatio_update(base + 3000, 0.016)
    calcinatio_ticked = v90_draco_stats["calcinatio_ticks"] > calcinatio_before
    no_ground_fire = len(player_magic_ground_fires) == fires_before


    v90_calcinatio.clear()
    v90_embers.clear()
    v90_draco_state.active = True
    v90_draco_state.target = target
    v90_draco_state.target_uid = v84_actor_uid(target)
    v90_draco_state.direction = pygame.Vector2(1.0, 0.0)
    v90_draco_state.seed = 91337
    ekran.fill((17, 11, 9))
    phases_for_preview = (
        ("flight", "İLERLEYİŞ", 90),
        ("bite", "ISIRMA", 110),
        ("coil", "SARILMA", 245),
        ("collapse", "ÇÖKÜŞ", 105),
        ("silence", "SESSİZLİK", 250),
        ("rupture", "İÇTEN YANMA", 145),
    )
    now_preview = pygame.time.get_ticks()
    for index, (phase, label, phase_age) in enumerate(phases_for_preview):
        panel = pygame.Rect(12 + index * 210, 236, 202, 258)
        pygame.draw.rect(ekran, (31, 19, 15), panel)
        pygame.draw.rect(ekran, V89_UI_BRASS, panel, 1)
        screen_center = pygame.Vector2(panel.centerx, panel.centery + 18)
        target.x = kamera_x + screen_center.x / KAMERA_YAKINLASTIRMA
        target.y = kamera_y + (screen_center.y + 17) / KAMERA_YAKINLASTIRMA
        target.hp = max(1, target.hp)
        target.active = True
        center = v90_actor_center(target)
        actor_screen = (
            int(dunya_ekran_x(center.x)),
            int(dunya_ekran_y(center.y)),
        )
        body = pygame.Rect(0, 0, 28, 60)
        body.midbottom = (actor_screen[0], actor_screen[1] + 28)
        pygame.draw.rect(ekran, (25, 22, 24), body)
        pygame.draw.rect(ekran, (105, 78, 68), body, 2)
        v90_draco_state.phase = phase
        v90_draco_state.phase_started_ms = now_preview - phase_age
        v90_draco_state.position = center
        if phase == "flight":
            v90_draco_state.target = None
            v90_draco_state.target_uid = ""
            v90_draco_state.position = center - pygame.Vector2(18.0, 0.0)
            v90_draco_state.trail.clear()
            for trail_index in range(4):
                v90_draco_state.trail.append(
                    (
                        center - pygame.Vector2(25.0 + trail_index * 18.0, 0.0),
                        max(4, len(V90_DRACO_FRAMES) - 1 - trail_index % 2),
                        now_preview - 45 * trail_index,
                    )
                )
        else:
            v90_draco_state.target = target
            v90_draco_state.target_uid = v84_actor_uid(target)
        v90_draco_draw(now_preview)
        yazi_yaz(
            label,
            panel.centerx,
            panel.y + 22,
            V89_UI_PARCHMENT,
            mini_font,
            True,
        )
    preview_path = str(output_prefix) + "_draco_sequence.png"
    pygame.image.save(ekran, preview_path)


    envanter_itemleri[0] = draco_calcinans_olustur()
    q_hizli_item_index = 0
    oyun_durumu = ENVANTER
    envanter_ciz()
    inventory_path = str(output_prefix) + "_draco_inventory.png"
    pygame.image.save(ekran, inventory_path)

    oyun_durumu = OYUN
    ekran.fill((34, 25, 20))
    oyuncu_paneli_ciz()
    one_cikan_item_paneli_ciz()
    hud_path = str(output_prefix) + "_injury_hud.png"
    pygame.image.save(ekran, hud_path)

    common_enemies[:] = [
        actor for actor in common_enemies if actor is not target
    ]
    v90_draco_state.reset()
    v90_calcinatio.clear()
    v90_embers.clear()
    v90_ash_marks.clear()
    oyun_durumu = original_state
    oyun_alt_durumu = original_substate
    kamera_x, kamera_y = original_camera

    diagnostics = v90_diagnostics()
    diagnostics["smoke"] = {
        "startup_ok": bool(V90_STARTUP_OK),
        "injury_metrics": injury_metrics,
        "injury_penalties_active": bool(
            injury_metrics["movement_multiplier"] < 0.72
            and injury_metrics["attack_time_multiplier"] > 1.30
            and injury_metrics["effective_stamina_ratio"] < 0.78
        ),
        "canonical_damage_registered": canonical_damage_registered,
        "q_cast_succeeded": cast_via_q,
        "cast_costs_applied": cast_costs_applied,
        "cooldown_denied_second_cast": cooldown_denied,
        "injury_snapshot_roundtrip": bool(
            injury_restored
            and all(
                abs(a - b) <= 0.00002
                for a, b in zip(snapshot_values, restored_values)
            )
        ),
        "critical_bleed_created_permanent_decal": bool(critical_bleed_created),
        "phases_seen": sorted(phase for phase in phases if phase != "idle"),
        "required_phases_seen": all(
            phase in phases
            for phase in ("flight", "bite", "coil", "collapse", "silence", "rupture")
        ),
        "target_hp_after_rupture": target_hp_after_rupture,
        "calcinatio_created": status is not None,
        "calcinatio_tick_applied": bool(calcinatio_ticked),
        "physical_trigger_applied": bool(physical_triggered),
        "no_ground_fire_created": bool(no_ground_fire),
        "ash_trail_created": v90_draco_stats["ash_marks"] > 0,
        "sequence_preview": preview_path,
        "inventory_preview": inventory_path,
        "injury_hud_preview": hud_path,
    }
    return diagnostics
# </POTBO_STAGE S2207>

# <POTBO_STAGE S2216>


def oyuncu_paneli_ciz():
    result = _v91_player_panel_raw()
    if oyuncu_hp <= 0:
        return result
    panel = hud_sol_rect()
    severity = v90_injury_severity()
    hp_ratio = v90_hp_ratio()
    if hp_ratio <= 0.20:
        label = bt("KRİTİK · KANAMA", "CRITICAL · BLEEDING")
        color = V91_UI_RED_HOT
    elif severity >= 0.52:
        label = bt("AĞIR YARALI", "SEVERELY WOUNDED")
        color = (216, 79, 49)
    elif severity >= 0.22:
        label = bt("YARALI", "WOUNDED")
        color = V91_UI_GOLD
    else:
        label = ""
        color = V91_UI_WHITE
    if label:
        text_width = mini_font.size(label)[0]
        box = pygame.Rect(
            panel.right - text_width - 25, panel.y + 37, text_width + 10, 19
        )
        pygame.draw.rect(ekran, V91_UI_BLACK, box)
        pygame.draw.rect(ekran, V91_UI_RED, box, 1)
        yazi_yaz(label, box.centerx, box.centery, color, mini_font, True)

    bar = pygame.Rect(panel.x + 22, panel.y + 84, panel.width - 44, 12)
    cap_x = bar.x + int(round(bar.width * v90_injury.effective_stamina_ratio))
    pygame.draw.line(
        ekran, V91_UI_BLACK, (cap_x, bar.y - 2), (cap_x, bar.bottom + 2), 4
    )
    pygame.draw.line(
        ekran, V91_UI_WHITE, (cap_x, bar.y - 2), (cap_x, bar.bottom + 2), 1
    )
    return result
# </POTBO_STAGE S2216>

# <POTBO_STAGE S2236>


def _v91_draco_bind_target(self, actor, now):
    result = _v91_draco_bind_raw(self, actor, now)
    center = v90_actor_center(actor)
    v90_spawn_embers(
        center,
        18,
        self.seed ^ int(now) ^ 0xB17E,
        -self.direction * 18.0,
    )
    kamera_hit_sarsintisi_baslat(
        9.5 if az_hareket else 13.0, 210
    )
    return result
# </POTBO_STAGE S2236>

# <POTBO_STAGE S2242>





V89_BLOOD_TRANSIENT_LIMIT = 112
V89_BLOOD_BURST_LIMIT = 16
V89_BLOOD_ARTERIAL_BURST_LIMIT = 24
V37_MAX_VISIBLE_GORE = 44
V49_BLOOD_HARD_LIMIT = 128


V49_DECAL_HARD_LIMIT = 10**9
V49_GORE_HARD_LIMIT = 140
# </POTBO_STAGE S2242>

# <POTBO_STAGE S2245>

v91_blood_stats = {
    "requested_air": 0,
    "emitted_air": 0,
    "near_landings": 0,
    "gore_compacted": 0,
    "injury_drops": 0,
}

_v91_blood_emit_raw = kan_parcacigi_patlat


def kan_parcacigi_patlat(
    x, y, adet, guc=1.0, yon=None, arterial=False
):
    requested = max(0, int(adet))
    cap = 22 if arterial else 15
    emitted = min(requested, cap)
    compact_power = min(
        float(guc), 0.94 if arterial else 0.76
    )
    before = len(blood_particles)
    result = _v91_blood_emit_raw(
        x,
        y,
        emitted,
        compact_power,
        yon=yon,
        arterial=arterial,
    )
    created = list(blood_particles[before:])
    max_planar = 132.0 if arterial else 104.0
    max_vertical = 138.0 if arterial else 112.0
    for particle in created:
        velocity = getattr(particle, "v", None)
        if (
            velocity is not None
            and velocity.length_squared()
            > max_planar * max_planar
        ):
            velocity.scale_to_length(max_planar)
        if hasattr(particle, "vz"):
            particle.vz = min(
                float(particle.vz), max_vertical
            )
        if hasattr(particle, "gravity"):
            particle.gravity = max(
                470.0, float(particle.gravity)
            )
        if hasattr(particle, "scale"):
            particle.scale *= 0.78
    omitted = max(0, requested - emitted)
    if omitted > 0:
        direction = (
            pygame.Vector2(yon)
            if yon is not None
            else pygame.Vector2(1.0, 0.0)
        )
        if direction.length_squared() <= 1e-8:
            direction = pygame.Vector2(
                1.0, 0.0
            ).rotate(random.uniform(0.0, 360.0))
        else:
            direction = direction.normalize()
        count = min(
            8, max(1, int(math.ceil(omitted / 8.0)))
        )
        scheduled = v87_schedule_blood_landings(
            (float(x), float(y) + 2.0),
            direction,
            count,
            min(
                27.0,
                9.0
                + max(0.4, compact_power) * 16.0,
            ),
            (
                0.07,
                min(
                    0.42,
                    0.16 + compact_power * 0.20,
                ),
            ),
            "v91_near_source",
            now=pygame.time.get_ticks(),
            cone_deg=78.0 if arterial else 62.0,
            delay_range=(150, 520),
            seed=int(
                float(x) * 83
                + float(y) * 149
                + requested * 599
            ),
        )
        v91_blood_stats["near_landings"] += int(
            scheduled
        )
    v91_blood_stats["requested_air"] += requested
    v91_blood_stats["emitted_air"] += len(created)
    return result


def v91_decal_contact_color(decal, now):
    stage = v89_blood_dry_stage(decal, now)
    scorch = max(
        0.0,
        min(
            1.0,
            float(
                getattr(decal, "v89_scorch", 0.0)
            ),
        ),
    )
    try:
        fresh = tuple(decal._v44_color(now))[:3]
    except (AttributeError, TypeError, ValueError):
        fresh = (116, 5, 18)
    color = v89_color_mix(
        fresh, (49, 17, 16), stage / 5.0
    )
    color = v89_color_mix(
        color, (18, 10, 7), scorch
    )


    return tuple(
        int(channel // 8 * 8) for channel in color
    )


def v91_blood_contact_sample(x, y, now):
    point = pygame.Vector2(float(x), float(y))
    best = None
    best_score = 0.0
    for decal in _v40_blood_nearby(point, 25.0):
        wetness = v89_blood_wetness(decal, now)
        if wetness <= 0.015:
            continue
        radius = max(
            6.0,
            min(
                28.0,
                7.0
                + float(getattr(decal, "scale", 0.5))
                * 12.0,
            ),
        )
        distance2 = point.distance_squared_to(
            (float(decal.x), float(decal.y))
        )
        if distance2 > radius * radius:
            continue
        nutrient = max(
            V89_BLOOD_RESIDUE_MASS,
            float(
                getattr(
                    decal,
                    "v75_ecology_mass",
                    V89_BLOOD_RESIDUE_MASS,
                )
            ),
        )
        score = wetness * min(
            1.0, 0.35 + nutrient * 0.92
        )
        if score > best_score:
            best_score = score
            best = (
                score,
                v91_decal_contact_color(decal, now),
                wetness,
            )
    return best


def v89_wet_blood_contact(x, y, now):
    sample = v91_blood_contact_sample(x, y, now)
    return (
        float(sample[0])
        if sample is not None
        else 0.0
    )


def v89_add_footprint(
    x,
    y,
    angle,
    side,
    intensity,
    now,
    color=None,
    freshness=1.0,
):
    if not v74_floor_clean(x, y):
        return None
    item = V89BloodFootprint(
        x, y, angle, side, intensity, now
    )
    item.v91_color = (
        tuple(color[:3])
        if color is not None
        else (112, 0, 16)
    )
    item.v91_source_freshness = v89_clamp01(
        freshness
    )


    item.dry_after_ms = int(now) + int(
        8_000
        + 48_000 * item.v91_source_freshness
    )
    tile = v89_blood_tile_key_at(x, y)
    v89_footprint_grid.setdefault(tile, []).append(
        item
    )
    v89_blood_tile_dirty_at(x, y)
    v89_stats["footprints"] += 1
    return item


def v89_footprint_image(
    print_item, now, silhouette, zoom
):
    stage = v89_blood_dry_stage(print_item, now)
    scorch = max(
        0,
        min(
            4,
            int(
                round(
                    float(
                        getattr(
                            print_item,
                            "v89_scorch",
                            0.0,
                        )
                    )
                    * 4.0
                )
            ),
        ),
    )
    intensity_bucket = max(
        1,
        min(
            6,
            int(round(print_item.intensity * 6.0)),
        ),
    )
    angle = int(round(print_item.angle / 12.0)) * 12
    source_color = tuple(
        getattr(
            print_item, "v91_color", (112, 0, 16)
        )
    )[:3]
    color_bucket = tuple(
        int(value // 8 * 8)
        for value in source_color
    )
    key = (
        "v91",
        round(float(zoom), 3),
        angle,
        print_item.side,
        intensity_bucket,
        stage,
        scorch,
        bool(silhouette),
        color_bucket,
    )
    image = v89_footprint_image_cache.get(key)
    if image is not None:
        return image
    alpha = max(
        58, min(238, 50 + intensity_bucket * 31)
    )
    if silhouette:
        color = V91_DEATH_BLOOD
    else:
        color = v89_color_mix(
            color_bucket, (42, 14, 14), stage / 5.0
        )
        color = v89_color_mix(
            color, (17, 9, 7), scorch / 4.0
        )
    base = pygame.Surface(
        (12, 20), pygame.SRCALPHA
    )
    toe_x = 1 if print_item.side < 0 else 3
    pygame.draw.ellipse(
        base, (*color, alpha), (toe_x, 0, 8, 7)
    )
    pygame.draw.rect(
        base,
        (*color, max(40, alpha - 16)),
        (3, 7, 6, 5),
    )
    pygame.draw.ellipse(
        base,
        (*color, max(34, alpha - 28)),
        (2, 13, 8, 6),
    )
    size = (
        max(4, int(round(12 * zoom))),
        max(7, int(round(20 * zoom))),
    )
    image = pygame.transform.scale(base, size)
    image = pygame.transform.rotate(
        image, -angle
    ).convert_alpha()
    if len(v89_footprint_image_cache) >= 420:
        for old in list(
            v89_footprint_image_cache
        )[:105]:
            v89_footprint_image_cache.pop(old, None)
    v89_footprint_image_cache[key] = image
    return image
# </POTBO_STAGE S2245>

# <POTBO_STAGE S2247>


def v89_player_footprints_update(now):
    global v89_player_foot_last_pos
    global v89_player_foot_distance
    global v89_player_foot_side
    global v89_player_sole_load
    global v91_player_sole_color
    global v91_player_sole_freshness
    if (
        oyun_durumu != OYUN
        or oyun_alt_durumu != HARITA
        or oyuncu_hp <= 0
    ):
        v89_player_foot_last_pos = pygame.Vector2(
            float(oyuncu_x), float(oyuncu_y)
        )
        v89_player_foot_distance = 0.0
        return
    current = pygame.Vector2(
        float(oyuncu_x), float(oyuncu_y)
    )
    if v89_player_foot_last_pos is None:
        v89_player_foot_last_pos = current
        return
    movement = current - v89_player_foot_last_pos
    distance = movement.length()
    v89_player_foot_last_pos = current
    if distance <= 0.02:
        return
    if distance > 72.0:
        v89_player_foot_distance = 0.0
        v89_player_sole_load = 0.0
        v91_player_sole_freshness = 0.0
        return
    direction = movement.normalize()
    sample = v91_blood_contact_sample(
        current.x, current.y, now
    )
    if sample is not None:
        contact, color, freshness = sample
        if contact > 0.035:
            v89_player_sole_load = max(
                v89_player_sole_load, contact
            )
            v91_player_sole_color = tuple(color)
            v91_player_sole_freshness = float(
                freshness
            )
    v89_player_foot_distance += distance
    while v89_player_foot_distance >= 15.0:
        v89_player_foot_distance -= 15.0
        if v89_player_sole_load <= 0.045:
            continue
        v89_player_foot_side = (
            1 - int(v89_player_foot_side)
        )
        side = (
            -1 if v89_player_foot_side == 0 else 1
        )
        normal = direction.rotate(90.0)
        point = (
            current
            + normal * (4.0 * side)
            - direction * 3.5
        )
        angle = (
            math.degrees(
                math.atan2(direction.y, direction.x)
            )
            + 90.0
        )
        v89_add_footprint(
            point.x,
            point.y,
            angle,
            side,
            v89_player_sole_load,
            now,
            color=v91_player_sole_color,
            freshness=v91_player_sole_freshness,
        )


        loss = (
            0.10
            + (1.0 - v91_player_sole_freshness)
            * 0.24
        )
        v89_player_sole_load = max(
            0.0, v89_player_sole_load - loss
        )
        v91_player_sole_freshness = max(
            0.0, v91_player_sole_freshness - 0.08
        )


_v91_blood_snapshot_raw = v89_blood_snapshot


def v89_blood_snapshot():
    payload = _v91_blood_snapshot_raw()
    live = [
        item
        for items in v89_footprint_grid.values()
        for item in items
    ]
    for row, item in zip(
        payload.get("footprints", []), live
    ):
        row.append(
            list(
                tuple(
                    getattr(
                        item,
                        "v91_color",
                        (112, 0, 16),
                    )
                )[:3]
            )
        )
        row.append(
            round(
                float(
                    getattr(
                        item,
                        "v91_source_freshness",
                        1.0,
                    )
                ),
                3,
            )
        )
    payload["version"] = V91_VERSION
    return payload


_v91_restore_blood_raw = v89_restore_blood_snapshot


def v89_restore_blood_snapshot(payload):
    before_ids = {
        id(item)
        for items in v89_footprint_grid.values()
        for item in items
    }
    result = _v91_restore_blood_raw(payload)
    created = [
        item
        for items in v89_footprint_grid.values()
        for item in items
        if id(item) not in before_ids
    ]
    rows = [
        row
        for row in payload.get("footprints", [])
        if isinstance(row, (list, tuple))
        and len(row) >= 8
    ]
    for item, row in zip(created, rows):
        if (
            len(row) > 8
            and isinstance(row[8], (list, tuple))
            and len(row[8]) >= 3
        ):
            item.v91_color = tuple(
                max(0, min(255, int(value)))
                for value in row[8][:3]
            )
        else:
            item.v91_color = (112, 0, 16)
        item.v91_source_freshness = v89_clamp01(
            row[9] if len(row) > 9 else 1.0
        )
        v89_blood_tile_dirty_at(item.x, item.y)
    return result


def v90_critical_bleed(now):
    hp_ratio = v90_hp_ratio()
    critical = v90_clamp(
        (0.28 - hp_ratio) / 0.24
    )
    blood_drive = max(
        critical, v90_injury.haemorrhage * 0.70
    )
    if (
        oyuncu_hp <= 0
        or blood_drive < 0.18
        or int(now) < v90_injury.next_bleed_ms
    ):
        return
    v90_injury.next_bleed_ms = int(now) + max(
        330, int(round(790 - 410 * blood_drive))
    )
    movement = pygame.Vector2(
        oyuncu_hareket_hiz_vektoru
    )
    direction = (
        -movement.normalize()
        if movement.length_squared() > 9.0
        else pygame.Vector2(1.0, 0.0).rotate(
            (int(now) // 37) % 360
        )
    )
    rng = random.Random(
        int(now)
        ^ int(oyuncu_x * 31)
        ^ int(oyuncu_y * 67)
    )
    count = (
        1
        + int(blood_drive > 0.56)
        + int(blood_drive > 0.84)
    )
    for _index in range(count):
        point = (
            pygame.Vector2(
                float(oyuncu_x), float(oyuncu_y)
            )
            + direction.rotate(
                rng.uniform(-32.0, 32.0)
            )
            * rng.uniform(3.0, 11.0)
        )
        if not v74_floor_clean(point.x, point.y):
            continue
        decal = _v89_create_decal_raw(
            point.x,
            point.y,
            rng.uniform(0.045, 0.105),
            rotation=math.degrees(
                math.atan2(direction.y, direction.x)
            ),
        )
        if decal is None:
            continue
        v89_decal_defaults(decal)
        decal.v44_oxygenation = 0.04
        decal.v44_tone = v44_blood_palette_for(
            oxygenation=0.04
        )
        decal.v91_injury_drop = True
        v89_blood_tile_dirty_at(decal.x, decal.y)
        v91_blood_stats["injury_drops"] += 1
    v90_injury_stats["critical_drops"] += 1


_v91_world_update_raw = kan_gore_guncelle


def kan_gore_guncelle():
    result = _v91_world_update_raw()


    for chunk in gore_chunks:
        if getattr(chunk, "settled", False):
            continue
        if not getattr(
            chunk, "v91_compacted", False
        ):
            if hasattr(chunk, "v"):
                chunk.v *= 0.40
            if hasattr(chunk, "vz"):
                chunk.vz *= 0.58
            if hasattr(chunk, "angular"):
                chunk.angular *= 0.58
            chunk.v91_compacted = True
            v91_blood_stats[
                "gore_compacted"
            ] += 1
        velocity = getattr(chunk, "v", None)
        if (
            velocity is not None
            and velocity.length_squared()
            > 74.0 * 74.0
        ):
            velocity.scale_to_length(74.0)
        if hasattr(chunk, "vz"):
            chunk.vz = min(float(chunk.vz), 138.0)
    state = v86_death_state
    for item in list(
        getattr(state, "debris", [])
    ) + list(getattr(state, "pieces", [])):
        if (
            getattr(item, "settled", False)
            or getattr(
                item, "v91_compacted", False
            )
        ):
            continue
        velocity = getattr(item, "velocity", None)
        if velocity is not None:
            velocity *= 0.42
        if hasattr(item, "vz"):
            item.vz *= 0.62
        if hasattr(item, "angular_velocity"):
            item.angular_velocity *= 0.62
        item.v91_compacted = True
    if len(v87_pending_blood_landings) > 180:
        del v87_pending_blood_landings[:-180]
    return result
# </POTBO_STAGE S2247>

# <POTBO_STAGE S2251>


def oyuncu_olum_sahnesi_ciz():
    if not v86_death_state.active:
        return _v91_death_draw_fallback()
    state = v86_death_state
    now = pygame.time.get_ticks()
    ekran.fill(V91_DEATH_BLACK)

    def draw_blood():
        kan_lekelerini_ciz(silhouette=True)
        _v77_death_blood_layer()
        for particle in blood_particles:
            if getattr(particle, "active", False):
                particle.ciz(silhouette=True)
        for chunk in sorted(
            gore_chunks, key=lambda item: item.y
        ):
            chunk.ciz(silhouette=True)

    blood = v91_capture_death_layer(
        "blood",
        now // 80,
        draw_blood,
        V91_DEATH_BLOOD,
    )
    ekran.blit(blood, (0, 0))

    def draw_body():
        global v86_ground_shadow
        shadow_raw = v86_ground_shadow
        burning_root = bool(state.burning_root)
        piece_burning = [
            bool(piece.burning)
            for piece in state.pieces
        ]
        debris_burning = [
            bool(item.burning)
            for item in state.debris
        ]
        v86_ground_shadow = (
            lambda *args, **kwargs: None
        )
        state.burning_root = False
        for piece in state.pieces:
            piece.burning = False
        for item in state.debris:
            item.burning = False
        try:
            killer = state.killer
            killer_behind = (
                killer is not None
                and float(
                    getattr(
                        killer,
                        "y",
                        state.body_anchor.y,
                    )
                )
                <= float(
                    state.body_anchor.y
                    + state.body_offset.y
                )
            )
            if killer_behind:
                v86_killer_draw(killer, now)
            for index, rock in enumerate(
                state.rocks
            ):
                v86_rock_draw(rock, now, index)
            v86_death_victim_draw(now)
            if killer is not None and not killer_behind:
                v86_killer_draw(killer, now)
        finally:
            state.burning_root = burning_root
            for piece, burning in zip(
                state.pieces, piece_burning
            ):
                piece.burning = burning
            for item, burning in zip(
                state.debris, debris_burning
            ):
                item.burning = burning
            v86_ground_shadow = shadow_raw

    body = v91_capture_death_layer(
        "body",
        now // 50,
        draw_body,
        V91_DEATH_BODY,
    )
    ekran.blit(body, (0, 0))

    if state.death_kind in ("fire", "bomb"):
        flames = v91_death_flame_cluster(
            state.seed,
            now // 82,
            KAMERA_YAKINLASTIRMA,
        )
        if flames is not None:
            anchor = v86_body_anchor_screen(state)
            ekran.blit(
                flames,
                flames.get_rect(
                    center=(
                        int(anchor.x),
                        int(anchor.y - 18),
                    )
                ),
            )

    if oyuncu_olum_baslangic_ms <= 0:
        return
    title_progress = oyuncu_olum_baslik_fade_orani(
        now
    )
    _v34_gameover_music_tick(title_progress, now)

    def draw_ui():
        v85_death_menu_draw(now)

    ui = v91_capture_death_layer(
        "ui", now // 65, draw_ui, V91_DEATH_BODY
    )
    ekran.blit(ui, (0, 0))


    if oyuncu_olum_cikis_orani(now) >= 0.52:
        ekran.fill(V91_DEATH_BLACK)
# </POTBO_STAGE S2251>

# <POTBO_STAGE S2264>


def one_cikan_item_paneli_ciz():
    if oyuncu_hp <= 0:
        return
    panel = hud_sag_rect()
    yazi_yaz(
        bt("ENVANTER / HIZLI ERİŞİM", "INVENTORY / QUICK ACCESS"),
        panel.centerx,
        panel.y + 16,
        V91_UI_WHITE,
        mini_font,
        True,
    )
    slot_size = 57
    gap = 14
    separator = 24
    total = slot_size * 6 + gap * 4 + separator
    start_x = panel.centerx - total // 2
    y = panel.y + 45
    for index in range(5):
        rect = pygame.Rect(start_x + index * (slot_size + gap), y, slot_size, slot_size)
        v85_slot_shell(rect, selected=index == envanter_secili_slot)
        v85_slot_contents(rect, index + 1, one_cikan_slotlar[index])
    separator_x = start_x + slot_size * 5 + gap * 4 + separator // 2
    pygame.draw.line(
        ekran,
        V91_UI_GREY,
        (separator_x, y - 4),
        (separator_x, y + slot_size + 4),
        1,
    )
    q_rect = pygame.Rect(
        start_x + slot_size * 5 + gap * 4 + separator,
        y,
        slot_size,
        slot_size,
    )
    v89_q_slot_draw(q_rect)
# </POTBO_STAGE S2264>

# <POTBO_STAGE S2274>


def v89_footprint_image(print_item, now, silhouette, zoom):
    stage = v89_blood_dry_stage(print_item, now)
    scorch = max(0, min(4, int(round(float(getattr(print_item, "v89_scorch", 0.0)) * 4))))
    intensity_bucket = max(1, min(6, int(round(print_item.intensity * 6.0))))
    angle = int(round(print_item.angle / 9.0)) * 9
    source_color = tuple(getattr(print_item, "v91_color", (112, 0, 16)))[:3]
    color_bucket = tuple(int(value // 8 * 8) for value in source_color)
    key = (
        "v92_small",
        round(float(zoom), 3),
        angle,
        print_item.side,
        intensity_bucket,
        stage,
        scorch,
        bool(silhouette),
        color_bucket,
    )
    cached = v89_footprint_image_cache.get(key)
    if cached is not None:
        return cached
    alpha = max(54, min(224, 46 + intensity_bucket * 29))
    color = V91_DEATH_BLOOD if silhouette else v89_color_mix(
        v89_color_mix(color_bucket, (42, 14, 14), stage / 5.0),
        (17, 9, 7),
        scorch / 4.0,
    )
    base = pygame.Surface((8, 14), pygame.SRCALPHA)
    toe_x = 0 if print_item.side < 0 else 2
    pygame.draw.ellipse(base, (*color, alpha), (toe_x, 0, 6, 5))
    pygame.draw.rect(base, (*color, max(34, alpha - 22)), (2, 5, 4, 4))
    pygame.draw.ellipse(base, (*color, max(28, alpha - 34)), (1, 9, 6, 5))
    size = (max(3, int(round(8 * zoom))), max(5, int(round(14 * zoom))))
    image = pygame.transform.scale(base, size)
    image = pygame.transform.rotate(image, -angle).convert_alpha()
    if len(v89_footprint_image_cache) >= 420:
        for old in list(v89_footprint_image_cache)[:105]:
            v89_footprint_image_cache.pop(old, None)
    v89_footprint_image_cache[key] = image
    return image


def v89_player_footprints_update(now):
    global v89_player_foot_last_pos, v89_player_foot_distance, v89_player_foot_side
    global v89_player_sole_load, v91_player_sole_color, v91_player_sole_freshness
    global v92_next_footprint_distance
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA or oyuncu_hp <= 0:
        v89_player_foot_last_pos = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
        v89_player_foot_distance = 0.0
        return
    current = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    if v89_player_foot_last_pos is None:
        v89_player_foot_last_pos = current
        return
    movement = current - v89_player_foot_last_pos
    distance = movement.length()
    v89_player_foot_last_pos = current
    if distance <= 0.02:
        return
    if distance > 86.0:
        v89_player_foot_distance = 0.0
        v89_player_sole_load = 0.0
        v91_player_sole_freshness = 0.0
        return
    direction = movement.normalize()
    sample = v91_blood_contact_sample(current.x, current.y, now)
    if sample is not None:
        contact, color, freshness = sample
        if contact > 0.035:
            v89_player_sole_load = max(v89_player_sole_load, contact)
            v91_player_sole_color = tuple(color)
            v91_player_sole_freshness = float(freshness)
    v89_player_foot_distance += distance
    dash_like = bool(oyuncu_dash_aktif_mi(now) or gelistirici_x_skill_aktif_mi(now))
    while v89_player_foot_distance >= v92_next_footprint_distance:
        v89_player_foot_distance -= v92_next_footprint_distance
        v92_next_footprint_distance = v92_foot_rng.uniform(
            10.5 if dash_like else 12.0,
            22.0 if dash_like else 18.5,
        )
        if v89_player_sole_load <= 0.045:
            continue
        if dash_like and v92_foot_rng.random() < 0.23:

            continue
        if v92_foot_rng.random() > 0.12:
            v89_player_foot_side = 1 - int(v89_player_foot_side)
        side = -1 if v89_player_foot_side == 0 else 1
        normal = direction.rotate(90.0)
        lateral = (3.1 + v92_foot_rng.uniform(-1.6, 1.8)) * side
        backward = v92_foot_rng.uniform(1.0, 6.0)
        point = current + normal * lateral - direction * backward
        angle = math.degrees(math.atan2(direction.y, direction.x)) + 90.0
        angle += v92_foot_rng.uniform(-11.0 if dash_like else -7.0, 11.0 if dash_like else 7.0)
        v89_add_footprint(
            point.x,
            point.y,
            angle,
            side,
            v89_player_sole_load * v92_foot_rng.uniform(0.78, 1.0),
            now,
            color=v91_player_sole_color,
            freshness=v91_player_sole_freshness,
        )
        loss = 0.10 + (1.0 - v91_player_sole_freshness) * 0.24
        v89_player_sole_load = max(0.0, v89_player_sole_load - loss)
        v91_player_sole_freshness = max(0.0, v91_player_sole_freshness - 0.08)
# </POTBO_STAGE S2274>

# <POTBO_STAGE S2281>


_v92_spawn_embers_raw = v90_spawn_embers


def v90_spawn_embers(position, count=5, seed=0, force=None):
    before = len(v90_embers)
    result = _v92_spawn_embers_raw(position, max(1, int(round(count * 1.65))), seed, force)
    now = pygame.time.get_ticks()
    for ember in v90_embers[before:]:
        ember.ttl_ms = int(max(720, ember.ttl_ms * 1.85))
        ember.size = min(4.4, ember.size * 0.90)
        ember.born_ms = min(ember.born_ms, now)
    if len(v90_embers) > 260:
        del v90_embers[:-260]
    return result
# </POTBO_STAGE S2281>

# <POTBO_STAGE S2283>


def v90_draco_draw(now=None):
    result = _v92_draco_draw_raw(now)
    if now is None:
        now = pygame.time.get_ticks()



    for ember in v90_embers:
        age = max(0, int(now) - int(ember.born_ms))
        fade = 1.0 - v90_clamp(age / max(1.0, float(ember.ttl_ms)))
        if fade <= 0.0:
            continue
        sx = int(dunya_ekran_x(ember.x))
        sy = int(dunya_ekran_y(ember.y))
        rng = random.Random(int(ember.seed) ^ 0xE6B392)
        radius = 1 if ember.size < 2.6 else 2
        hot = (255, int(128 + 92 * fade), int(22 + 42 * fade), int(215 * fade))
        fleck = pygame.Surface((9, 9), pygame.SRCALPHA)
        pygame.draw.circle(fleck, hot, (4, 4), radius)
        if rng.random() < 0.58:
            dx = rng.choice((-2, -1, 1, 2))
            dy = rng.choice((-3, -2, 2))
            pygame.draw.circle(fleck, (255, 84, 8, int(120 * fade)), (4 + dx, 4 + dy), 1)
        ekran.blit(fleck, fleck.get_rect(center=(sx, sy)))
    return result
# </POTBO_STAGE S2283>

# <POTBO_STAGE S2285>


def _v92_draco_update(self, now):
    global V90_DRACO_MAX_TRAVEL
    old_limit = V90_DRACO_MAX_TRAVEL


    V90_DRACO_MAX_TRAVEL = 100000.0
    try:
        result = _v92_draco_update_raw(self, now)
    finally:
        V90_DRACO_MAX_TRAVEL = old_limit
    if self.active and self.phase == "flight":
        sx = dunya_ekran_x(self.position.x)
        sy = dunya_ekran_y(self.position.y)
        margin = 96
        if sx < -margin or sx > GENISLIK + margin or sy < -margin or sy > YUKSEKLIK + margin:
            self.phase_set("dissipate", now)
            self.v92_left_screen = True
            v90_spawn_embers(self.position, 24, self.seed ^ int(now) ^ 0xD12A, -self.direction * 18.0)
            v90_draco_stats["misses"] += 1
    return result
# </POTBO_STAGE S2285>

# <POTBO_STAGE S2303>


def oyun_ekrani_ciz():
    result = _v92_game_draw_raw()


    if v92_chain_state.active and v92_chain_state.execution:
        v92_chain_execution_draw()
    return result
# </POTBO_STAGE S2303>

# <POTBO_STAGE S2309>


def oyuncu_kanli_hasar_kaydi(kaynak_x, kaynak_y, profil, hasar, kaynak_adi=""):
    global oyuncu_hp
    protection = max(0.0, min(0.32, float(v92_armor_rating)))
    if v92_armor_weight == "light":
        protection *= 0.88
    elif v92_armor_weight == "heavy":
        protection = min(0.38, protection + 0.055)
    original = max(0, int(hasar))
    adjusted = max(1, int(round(float(original) * (1.0 - protection)))) if original > 0 else original




    refund = max(0, original - adjusted)
    if refund > 0:
        oyuncu_hp = min(int(oyuncu_max_hp), int(oyuncu_hp) + refund)
    return _v92_player_damage_raw(kaynak_x, kaynak_y, profil, adjusted, kaynak_adi)
# </POTBO_STAGE S2309>

# <POTBO_STAGE S2331>


def v92_chain_execution_draw():
    state = v92_chain_state
    if not state.active or not state.execution:
        return
    now = pygame.time.get_ticks()
    elapsed = max(0, now - state.started_ms)
    p = min(1.0, elapsed / max(1.0, state.duration_ms))
    ekran.fill((0, 0, 0))

    for index, (actor, silhouette, center) in enumerate(state.silhouettes):
        if silhouette is None:
            continue
        tint = pygame.mask.from_surface(silhouette, 1).to_surface(
            setcolor=(158, 8, 25, 255), unsetcolor=(0, 0, 0, 0)
        ).convert_alpha()
        sx, sy = int(dunya_ekran_x(center.x)), int(dunya_ekran_y(center.y))
        ekran.blit(tint, tint.get_rect(center=(sx, sy)))
    player = v84_player_silhouette()
    if player is not None:
        darker = pygame.mask.from_surface(player, 1).to_surface(
            setcolor=(151, 18, 34, 255), unsetcolor=(0, 0, 0, 0)
        ).convert_alpha()
        ekran.blit(darker, darker.get_rect(midbottom=(int(dunya_ekran_x(oyuncu_x)), int(dunya_ekran_y(oyuncu_y)))))

    trace_progress = min(1.0, p / 0.46)
    visible_segments = int(math.ceil(trace_progress * max(1, len(state.points) - 1)))
    for i in range(min(visible_segments, len(state.points) - 1)):
        a = state.points[i]
        b = state.points[i + 1]
        pygame.draw.line(
            ekran,
            (222, 13, 38),
            (int(dunya_ekran_x(a.x)), int(dunya_ekran_y(a.y))),
            (int(dunya_ekran_x(b.x)), int(dunya_ekran_y(b.y))),
            3,
        )
    for head in state.heads:
        image = pygame.transform.rotate(head.image, head.rotation)
        mask = pygame.mask.from_surface(image, 1)
        image = mask.to_surface(setcolor=(186, 9, 31, 255), unsetcolor=(0, 0, 0, 0)).convert_alpha()
        sx = int(dunya_ekran_x(head.position.x))
        sy = int(dunya_ekran_y(head.position.y) - max(0.0, head.z))
        ekran.blit(image, image.get_rect(center=(sx, sy)))

    for particle in blood_particles:
        if getattr(particle, "active", False):
            try:
                particle.ciz(silhouette=True)
            except Exception:
                pass
    for chunk in gore_chunks:
        try:
            chunk.ciz(silhouette=True)
        except Exception:
            pass
# </POTBO_STAGE S2331>

# <POTBO_STAGE S2348>


def v55_pool_scan(now=None):
    global v55_pool_clusters, v55_pool_next_scan_ms
    if now is None:
        now = pygame.time.get_ticks()
    if int(now) < int(v55_pool_next_scan_ms):
        return v55_pool_clusters
    v55_pool_next_scan_ms = int(now) + V55_POOL_SCAN_INTERVAL_MS

    margin = 120.0 / max(0.01, KAMERA_YAKINLASTIRMA)
    left = kamera_x - margin
    right = kamera_x + GENISLIK / max(0.01, KAMERA_YAKINLASTIRMA) + margin
    top = kamera_y - margin
    bottom = kamera_y + YUKSEKLIK / max(0.01, KAMERA_YAKINLASTIRMA) + margin
    visible = [
        decal
        for decal in blood_decals[-320:]
        if left <= float(decal.x) <= right and top <= float(decal.y) <= bottom
    ][-160:]
    if not visible:
        v55_pool_clusters = []
        return v55_pool_clusters

    cell = max(8.0, float(V55_POOL_CLUSTER_RADIUS))
    grid = {}
    for decal in visible:
        key = (int(math.floor(float(decal.x) / cell)), int(math.floor(float(decal.y) / cell)))
        grid.setdefault(key, []).append(decal)

    seen = set()
    clusters = []
    radius2 = float(V55_POOL_CLUSTER_RADIUS) ** 2
    for decal in visible:
        marker = id(decal)
        if marker in seen:
            continue
        gx = int(math.floor(float(decal.x) / cell))
        gy = int(math.floor(float(decal.y) / cell))
        near = []
        for yy in range(gy - 1, gy + 2):
            for xx in range(gx - 1, gx + 2):
                for other in grid.get((xx, yy), ()):
                    other_id = id(other)
                    if other_id in seen:
                        continue
                    dx = float(other.x) - float(decal.x)
                    dy = float(other.y) - float(decal.y)
                    if dx * dx + dy * dy <= radius2:
                        near.append(other)
        if len(near) < V55_POOL_CLUSTER_MIN:
            continue
        for item in near:
            seen.add(id(item))
        total_mass = sum(
            max(0.1, float(getattr(item, "v44_stain_mass", getattr(item, "scale", 1.0))))
            for item in near
        )
        cx = sum(float(item.x) for item in near) / len(near)
        cy = sum(float(item.y) for item in near) / len(near)
        wet = sum(1 for item in near if int(now) < int(getattr(item, "dry_after_ms", 0))) / len(near)
        clusters.append(
            {
                "x": cx,
                "y": cy,
                "mass": total_mass,
                "count": len(near),
                "wet": wet,
                "surface": v53_surface_at(cx, cy),
            }
        )
        if len(clusters) >= V55_POOL_VISIBLE_MAX:
            break
    v55_pool_clusters = clusters
    return clusters






def kan_gore_guncelle():
    result = _v91_world_update_raw()
    for chunk in gore_chunks[-72:]:
        if getattr(chunk, "settled", False):
            continue
        if not getattr(chunk, "v91_compacted", False):
            if hasattr(chunk, "v"):
                chunk.v *= 0.40
            if hasattr(chunk, "vz"):
                chunk.vz *= 0.58
            if hasattr(chunk, "angular"):
                chunk.angular *= 0.58
            chunk.v91_compacted = True
            v91_blood_stats["gore_compacted"] += 1
        velocity = getattr(chunk, "v", None)
        if velocity is not None and velocity.length_squared() > 74.0 * 74.0:
            velocity.scale_to_length(74.0)
        if hasattr(chunk, "vz"):
            chunk.vz = min(float(chunk.vz), 138.0)
    state = v86_death_state
    for collection in (getattr(state, "debris", ()), getattr(state, "pieces", ())):
        for item in collection:
            if getattr(item, "settled", False) or getattr(item, "v91_compacted", False):
                continue
            velocity = getattr(item, "velocity", None)
            if velocity is not None:
                velocity *= 0.42
            if hasattr(item, "vz"):
                item.vz *= 0.62
            if hasattr(item, "angular_velocity"):
                item.angular_velocity *= 0.62
            item.v91_compacted = True
    if len(v87_pending_blood_landings) > 150:
        del v87_pending_blood_landings[:-150]
    return result
# </POTBO_STAGE S2348>

# <POTBO_STAGE S2383>


def _v95_draco_update(self, now):
    result = _v95_draco_update_previous(self, now)
    if self.active and self.phase == "cast":
        last_cast = int(getattr(self, "v95_last_cast_ember_ms", 0))
        if int(now) - last_cast >= 58:
            setattr(self, "v95_last_cast_ember_ms", int(now))
            v90_spawn_embers(
                self.position - self.direction * 6.0,
                1,
                self.seed ^ int(now),
                -self.direction * 8.0,
            )
    elif self.active and self.phase == "flight":
        last = int(getattr(self, "v95_last_silhouette_ms", 0))
        if int(now) - last >= 24:
            setattr(self, "v95_last_silhouette_ms", int(now))
            if V95_DRACO_FLIGHT_INDICES:
                idx = V95_DRACO_FLIGHT_INDICES[
                    (int(now) // 64) % len(V95_DRACO_FLIGHT_INDICES)
                ]
                self.trail.append(
                    (
                        pygame.Vector2(self.position) - self.direction * 8.0,
                        idx,
                        int(now),
                    )
                )
    return result
# </POTBO_STAGE S2383>

# <POTBO_STAGE S2387>


v95_ember_sprite_cache = {}
# </POTBO_STAGE S2387>

# <POTBO_STAGE S2391>






V37_MAX_VISIBLE_GORE = min(int(V37_MAX_VISIBLE_GORE), 36)
V40_BLOOD_VISIBLE_MAX = min(int(V40_BLOOD_VISIBLE_MAX), 240)
if "V42_BLOOD_VISIBLE_RECENT" in globals():
    V42_BLOOD_VISIBLE_RECENT = min(int(V42_BLOOD_VISIBLE_RECENT), 128)
if "V42_BLOOD_VISIBLE_OLDER" in globals():
    V42_BLOOD_VISIBLE_OLDER = max(
        0,
        int(V40_BLOOD_VISIBLE_MAX) - int(V42_BLOOD_VISIBLE_RECENT),
    )
# </POTBO_STAGE S2391>

# <POTBO_STAGE S2399>





def one_cikan_item_paneli_ciz():
    if oyuncu_hp <= 0:
        return
    panel = hud_sag_rect()
    slot_size = 84
    gap = 12
    separator = 30
    total = slot_size * 6 + gap * 4 + separator
    start_x = panel.centerx - total // 2
    y = panel.centery - slot_size // 2

    for index in range(5):
        rect = pygame.Rect(start_x + index * (slot_size + gap), y, slot_size, slot_size)
        v85_slot_shell(rect, selected=index == envanter_secili_slot)
        v85_slot_contents(rect, index + 1, one_cikan_slotlar[index])

    separator_x = start_x + slot_size * 5 + gap * 4 + separator // 2
    pygame.draw.line(
        ekran,
        V91_UI_GREY,
        (separator_x, y - 3),
        (separator_x, y + slot_size + 3),
        1,
    )

    q_rect = pygame.Rect(
        start_x + slot_size * 5 + gap * 4 + separator,
        y,
        slot_size,
        slot_size,
    )
    v89_q_slot_draw(q_rect)
# </POTBO_STAGE S2399>

# <POTBO_STAGE S2502>









V105_VERSION = "105.0"
# </POTBO_STAGE S2502>

# <POTBO_STAGE S2508>






def v89_maybe_start_rivulet(decal, scale):
    return None


def _v105_rivulet_update(self, now):
    self.active = False
    return None


def _v105_rivulet_draw(self, now, silhouette=False):
    return None


V89BloodRivulet.update = _v105_rivulet_update
V89BloodRivulet.draw = _v105_rivulet_draw
v89_rivulets.clear()
v89_rivulet_cell_next_ms.clear()
# </POTBO_STAGE S2508>

# <POTBO_STAGE S2510>


def v89_tile_objects(tile_x, tile_y):
    decals, footprints = _v105_tile_objects_previous(tile_x, tile_y)


    decals = [d for d in decals if not bool(getattr(d, "v89_rivulet", False))]
    return decals, footprints


v105_rivulet_cleanup_next_ms = 0


def v105_prune_historical_rivulets(now):
    global v105_rivulet_cleanup_next_ms
    if int(now) < int(v105_rivulet_cleanup_next_ms):
        return
    v105_rivulet_cleanup_next_ms = int(now) + 1800
    bad_ids = {id(d) for d in blood_decals if bool(getattr(d, "v89_rivulet", False))}
    if not bad_ids:
        return
    blood_decals[:] = [d for d in blood_decals if id(d) not in bad_ids]
    for cell in list(v40_blood_grid.keys()):
        bucket = v40_blood_grid.get(cell, [])
        if not bucket:
            v40_blood_grid.pop(cell, None)
            continue
        bucket[:] = [d for d in bucket if id(d) not in bad_ids]
        if not bucket:
            v40_blood_grid.pop(cell, None)
    v89_blood_tile_cache.clear()
    v89_blood_tile_revision.clear()







V105_MAGGOT_FIRST_MIN_MS = 45_000
# </POTBO_STAGE S2510>

# <POTBO_STAGE S2512>
BLOOD_MAGGOT_FIRST_MIN_MS = V105_MAGGOT_FIRST_MIN_MS
BLOOD_MAGGOT_FIRST_MAX_MS = V105_MAGGOT_FIRST_MAX_MS
BLOOD_MAGGOT_WAVE_MIN_MS = 90_000
BLOOD_MAGGOT_WAVE_MAX_MS = 160_000

_v105_decal_init_previous = PersistentBloodDecal.__init__


def _v105_decal_init(self, *args, **kwargs):
    _v105_decal_init_previous(self, *args, **kwargs)
    created = int(getattr(self, "created_ms", pygame.time.get_ticks()))


    self.maggot_next_ms = created + random.randint(
        V105_MAGGOT_FIRST_MIN_MS,
        V105_MAGGOT_FIRST_MAX_MS,
    )


PersistentBloodDecal.__init__ = _v105_decal_init


def _v28_maggot_dalgalari_uret(simdi):
    """Sprite-only larvae spawn with the old bounded scan architecture."""
    global blood_maggot_scan_next_ms, blood_maggot_scan_cursor
    if not BLOOD_WORM_SPRITELERI or not blood_decals:
        return
    if int(simdi) < int(blood_maggot_scan_next_ms):
        return
    blood_maggot_scan_next_ms = int(simdi) + 900

    remaining = BLOOD_MAGGOT_MAX - sum(
        1 for maggot in blood_maggots if getattr(maggot, "active", False)
    )
    if remaining <= 0:
        return

    count = len(blood_decals)
    scan_count = min(count, 56)
    for offset in range(scan_count):
        idx = (blood_maggot_scan_cursor + offset) % count
        decal = blood_decals[idx]
        if bool(getattr(decal, "v89_rivulet", False)):
            continue
        if int(simdi) < int(getattr(decal, "maggot_next_ms", 10**18)):
            continue
        already = any(
            getattr(m, "active", False)
            and getattr(m, "source_decal", None) is decal
            for m in blood_maggots
        )
        if not already and random.random() < 0.58:
            blood_maggots.append(BloodMaggot(decal, simdi))
            remaining -= 1
        decal.maggot_waves = int(getattr(decal, "maggot_waves", 0)) + 1
        decal.maggot_next_ms = int(simdi) + random.randint(
            BLOOD_MAGGOT_WAVE_MIN_MS,
            BLOOD_MAGGOT_WAVE_MAX_MS,
        )
        if remaining <= 0:
            break
    blood_maggot_scan_cursor = (
        blood_maggot_scan_cursor + scan_count
    ) % max(1, count)



def _v105_maggot_sprite_draw(self):
    if not getattr(self, "active", False) or not BLOOD_WORM_SPRITELERI:
        return
    sx = dunya_ekran_x(float(self.x))
    sy = dunya_ekran_y(float(self.y))
    if sx < -32 or sx > GENISLIK + 32 or sy < -32 or sy > YUKSEKLIK + 32:
        return
    now = pygame.time.get_ticks()
    frame_ms = 105
    idx = ((now + int(getattr(self, "frame_seed", 0))) // frame_ms) % len(
        BLOOD_WORM_SPRITELERI
    )
    frame = BLOOD_WORM_SPRITELERI[idx]
    factor = max(0.18, float(getattr(self, "scale_factor", 0.28))) * KAMERA_YAKINLASTIRMA
    size = (
        max(2, int(round(frame.get_width() * factor))),
        max(2, int(round(frame.get_height() * factor))),
    )
    velocity = pygame.Vector2(getattr(self, "v", (0.0, 0.0)))
    flip_x = velocity.x < -0.2
    key = ("blood_maggot_v105_sprite", id(frame), size, flip_x)
    img = sprite_olcek_onbellegi.get(key)
    if img is None:
        img = pygame.transform.scale(frame, size)
        if flip_x:
            img = pygame.transform.flip(img, True, False)
        sprite_olcek_onbellegi[key] = img
    ekran.blit(img, img.get_rect(center=(int(sx), int(sy))))
# </POTBO_STAGE S2512>

# <POTBO_STAGE S2514>





def _v105_blood_particle_sprite_draw(self, silhouette=False):
    if not getattr(self, "active", False):
        return
    sx = dunya_ekran_x(float(self.x))
    sy = dunya_ekran_y(float(self.y)) - float(getattr(self, "z", 0.0)) * KAMERA_YAKINLASTIRMA
    if sx < -80 or sx > GENISLIK + 80 or sy < -80 or sy > YUKSEKLIK + 80:
        return

    if not BLOOD_PARTICLE_SPRITELERI:


        radius = max(1, min(3, int(round(1.25 * float(getattr(self, "scale", 0.7))))))
        pygame.draw.circle(
            ekran,
            (92, 0, 12) if silhouette else (132, 4, 22),
            (int(sx), int(sy)),
            radius,
        )
        return

    src = BLOOD_PARTICLE_SPRITELERI[
        int(getattr(self, "sprite_index", 0)) % len(BLOOD_PARTICLE_SPRITELERI)
    ]
    zoom = max(0.50, float(KAMERA_YAKINLASTIRMA))
    scale = max(0.24, min(1.05, float(getattr(self, "scale", 0.70))))

    target_h = max(3, min(11, int(round(src.get_height() * scale * zoom * 0.58))))
    ratio = src.get_width() / max(1.0, float(src.get_height()))
    target_w = max(3, min(13, int(round(target_h * ratio))))

    velocity = pygame.Vector2(getattr(self, "v", (0.0, 0.0)))
    angle = 0
    if velocity.length_squared() > 4.0:
        angle = int(round(-math.degrees(math.atan2(velocity.y, velocity.x)) / 12.0)) * 12
    key = (
        "blood_particle_v105_sprite",
        id(src),
        (target_w, target_h),
        angle,
        bool(silhouette),
    )
    img = sprite_olcek_onbellegi.get(key)
    if img is None:
        img = pygame.transform.scale(src, (target_w, target_h))
        if silhouette:
            mask = pygame.mask.from_surface(img)
            img = mask.to_surface(
                setcolor=(102, 0, 12, 245),
                unsetcolor=(0, 0, 0, 0),
            ).convert_alpha()
        if angle:
            img = pygame.transform.rotate(img, angle)
        sprite_olcek_onbellegi[key] = img
    ekran.blit(img, img.get_rect(center=(int(sx), int(sy))))


V44BloodParticle.ciz = _v105_blood_particle_sprite_draw
BloodParticle.ciz = _v105_blood_particle_sprite_draw






def v105_blood_body_anchor(x, y, context):
    if not context:
        return float(x), float(y)
    target_name = str(context.get("target", "")).lower()
    candidates = []
    for actor in common_enemies:
        if actor is not None:
            candidates.append(actor)
    if tarkard_actor is not None:
        candidates.append(tarkard_actor)
    if torrmund_actor is not None:
        candidates.append(torrmund_actor)

    best = None
    best_score = 10**9
    for actor in candidates:
        try:
            ax = float(actor.x)
            ay = float(actor.y)
        except (TypeError, ValueError, AttributeError):
            continue
        dx = abs(float(x) - ax)
        dy = abs(float(y) - ay)
        if dx > 44.0 or dy > 22.0:
            continue
        score = dx * 1.25 + dy
        if score < best_score:
            best_score = score
            best = actor

    if best is not None:
        kind = str(getattr(best, "tur", target_name)).lower()
        lift = {
            "crawler": 15.0,
            "berserker": 28.0,
            "headsthrower": 29.0,
            "heads_thrower": 29.0,
            "tarkard": 34.0,
            "torrmund": 38.0,
        }.get(kind, 26.0)
        return float(x), float(best.y) - lift

    if target_name == "player" and abs(float(x) - float(oyuncu_x)) <= 42.0 and abs(float(y) - float(oyuncu_y)) <= 24.0:
        return float(x), float(oyuncu_y) - 26.0
    return float(x), float(y)


_v105_blood_emit_previous = kan_parcacigi_patlat


def kan_parcacigi_patlat(x, y, adet, guc=1.0, yon=None, arterial=False):
    context = dict(v44_context_current() or {})
    spawn_x, spawn_y = v105_blood_body_anchor(x, y, context)
    before = len(blood_particles)
    result = _v105_blood_emit_previous(
        spawn_x,
        spawn_y,
        adet,
        guc,
        yon=yon,
        arterial=arterial,
    )
    created = blood_particles[before:]


    for particle in created:
        if hasattr(particle, "z"):
            particle.z += random.uniform(5.0, 11.0) if context else 0.0
        if hasattr(particle, "vz") and context:
            particle.vz *= random.uniform(0.88, 1.02)
    return result







_v105_gore_init_previous = GoreChunk.__init__


def _v105_gore_init(self, kind, x, y, guc=1.0, small=False):
    _v105_gore_init_previous(self, kind, x, y, guc=guc, small=small)
    context = dict(v44_context_current() or {})
    direction = context.get("direction")
    if direction is not None:
        try:
            base = pygame.Vector2(direction)
        except Exception:
            base = pygame.Vector2(1.0, 0.0)
        if base.length_squared() > 1e-8:
            base = base.normalize().rotate(random.uniform(-58.0, 58.0))
            if random.random() < 0.13:
                base *= -1.0
            speed = random.uniform(82.0, 176.0) * max(0.70, min(1.55, float(guc)))
            self.v = base * speed


    self.z = max(float(getattr(self, "z", 0.0)), random.uniform(19.0, 34.0))
    self.vz = max(float(getattr(self, "vz", 0.0)), random.uniform(120.0, 225.0) * max(0.72, min(1.40, float(guc))))
    self.angular = max(-560.0, min(560.0, float(getattr(self, "angular", 0.0)) * 1.16))


GoreChunk.__init__ = _v105_gore_init


def v105_gore_motion_soft_cap(chunk):
    if getattr(chunk, "settled", False):
        return
    velocity = getattr(chunk, "v", None)
    if velocity is not None and velocity.length_squared() > 205.0 * 205.0:
        velocity.scale_to_length(205.0)
    if hasattr(chunk, "vz"):
        chunk.vz = max(-360.0, min(float(chunk.vz), 275.0))
    if hasattr(chunk, "angular"):
        chunk.angular = max(-620.0, min(620.0, float(chunk.angular)))





def kan_gore_guncelle():
    result = _v91_world_update_raw()
    now = pygame.time.get_ticks()
    v105_prune_historical_rivulets(now)
    for chunk in gore_chunks[-72:]:
        v105_gore_motion_soft_cap(chunk)
    state = v86_death_state
    for collection in (getattr(state, "debris", ()), getattr(state, "pieces", ())):
        for item in collection[-48:] if isinstance(collection, list) else collection:
            if getattr(item, "settled", False):
                continue
            velocity = getattr(item, "velocity", None)
            if velocity is not None and velocity.length_squared() > 240.0 * 240.0:
                velocity.scale_to_length(240.0)
            if hasattr(item, "vz"):
                item.vz = max(-390.0, min(float(item.vz), 300.0))
            if hasattr(item, "angular_velocity"):
                item.angular_velocity = max(-700.0, min(700.0, float(item.angular_velocity)))
    if len(v87_pending_blood_landings) > 150:
        del v87_pending_blood_landings[:-150]
    return result
# </POTBO_STAGE S2514>

# <POTBO_STAGE S2519>




def v90_critical_bleed(now):
    condition = v106_player_condition()
    if condition == "healthy" or oyuncu_hp <= 0:
        return
    if int(now) < int(getattr(v90_injury, "next_bleed_ms", 0)):
        return

    if condition == "critical":
        interval = random.randint(280, 430)
        count = 2 if random.random() < 0.38 else 1
    else:
        interval = random.randint(720, 1050)
        count = 1
    v90_injury.next_bleed_ms = int(now) + interval

    movement = pygame.Vector2(oyuncu_hareket_hiz_vektoru)
    for _ in range(count):


        planar = pygame.Vector2(random.uniform(-4.0, 4.0), random.uniform(-2.0, 2.0))
        if movement.length_squared() > 9.0:
            planar -= movement * random.uniform(0.05, 0.12)
        drop = BloodParticle(
            float(oyuncu_x) + random.uniform(-5.0, 5.0),
            float(oyuncu_y) + random.uniform(-2.0, 2.0),
            planar,
            guc=0.38 if condition == "wounded" else 0.46,
            arterial=False,
        )
        drop.z = random.uniform(24.0, 34.0) if condition == "wounded" else random.uniform(28.0, 39.0)
        drop.vz = random.uniform(-18.0, 8.0)
        drop.gravity = random.uniform(300.0, 390.0)
        drop.scale = random.uniform(0.28, 0.46) if condition == "wounded" else random.uniform(0.34, 0.54)
        blood_particles.append(drop)
    v90_injury_stats["critical_drops"] = int(v90_injury_stats.get("critical_drops", 0)) + count
# </POTBO_STAGE S2519>

# <POTBO_STAGE S2555>


_v106_world_draw_previous = dunya_aktorlerini_derinlige_gore_ciz


def dunya_aktorlerini_derinlige_gore_ciz():
    result = _v106_world_draw_previous()
    v106_corona_draw(pygame.time.get_ticks())
    return result
# </POTBO_STAGE S2555>

# <POTBO_STAGE S2573>









V108_TOP_UI_NAMES = (
    "oyuncu_paneli_ciz",
    "one_cikan_item_paneli_ciz",
    "gelistirici_test_paneli_ciz",
    "seviye_animasyonu_ciz",
    "oyuncu_bayginlik_ui_ciz",
    "oyuncu_olum_ui_ciz",
    "diyalog_ciz",
    "kayit_animasyonu_ciz",
    "bildirim_ciz",
    "onemli_item_penceresi_ciz",
)
# </POTBO_STAGE S2573>

# <POTBO_STAGE S2576>


def oyun_ekrani_ciz():
    saved = {}
    g = globals()
    for name in V108_TOP_UI_NAMES:
        fn = g.get(name)
        if callable(fn):
            saved[name] = fn
            g[name] = _v108_ui_noop
    try:
        result = _v108_game_draw_raw()
    finally:
        for name, fn in saved.items():
            g[name] = fn


    if oyuncu_hp > 0:
        saved.get("seviye_animasyonu_ciz", _v108_ui_noop)()
        saved.get("oyuncu_paneli_ciz", _v108_ui_noop)()
        saved.get("one_cikan_item_paneli_ciz", _v108_ui_noop)()
        saved.get("gelistirici_test_paneli_ciz", _v108_ui_noop)()
        saved.get("oyuncu_bayginlik_ui_ciz", _v108_ui_noop)()

    saved.get("kayit_animasyonu_ciz", _v108_ui_noop)()

    if fps_goster:
        yazi_yaz(f"FPS: {int(saat.get_fps())}", 1170, 660, SARI, mini_font)

    if yeni_item_sahnesi_musait_mi() and not onemli_item_kuyrugu:
        saved.get("bildirim_ciz", _v108_ui_noop)()

    if oyun_alt_durumu in (DIYALOG, DIYALOG_SECIM):
        saved.get("diyalog_ciz", _v108_ui_noop)()

    if onemli_item_penceresi_acik_mi():
        saved.get("onemli_item_penceresi_ciz", _v108_ui_noop)()

    if oyuncu_hp <= 0:
        saved.get("oyuncu_olum_ui_ciz", _v108_ui_noop)()
    return result
# </POTBO_STAGE S2576>

# <POTBO_STAGE S2627>


_v110_world_draw_raw = dunya_aktorlerini_derinlige_gore_ciz
# </POTBO_STAGE S2627>

# <POTBO_STAGE S2663>


def v115_spawn_scorch(center, seed=0):
    center = pygame.Vector2(center)
    rng = random.Random(int(seed) ^ 0x15C0)
    cracks = []
    for _ in range(rng.randint(3, 5)):
        angle = rng.uniform(0.0, math.tau)
        length = rng.uniform(10.0, 28.0)
        end = pygame.Vector2(
            center.x + math.cos(angle) * length,
            center.y + math.sin(angle) * length * rng.uniform(0.25, 0.55),
        )
        cracks.append(
            v110_polyline_points(
                center,
                end,
                jitter=3.4,
                segments=rng.randint(2, 3),
                seed=rng.randint(0, 10**6),
            )
        )
    blots = []
    for _ in range(rng.randint(3, 4)):
        blots.append(
            {
                "ox": rng.uniform(-12.0, 12.0),
                "oy": rng.uniform(-5.0, 5.0),
                "rx": rng.uniform(6.0, 15.0),
                "ry": rng.uniform(3.0, 8.0),
                "a": rng.randint(56, 104),
            }
        )
    embers = []
    for _ in range(rng.randint(7, 11)):
        embers.append(
            {
                "x": center.x + rng.uniform(-7.0, 7.0),
                "y": center.y + rng.uniform(-2.0, 2.0),
                "vx": rng.uniform(-8.0, 8.0),
                "vy": rng.uniform(-18.0, -9.0),
                "life": rng.randint(420, V115_FULMEN_EMBER_LIFETIME_MS),
                "age": rng.randint(0, 110),
                "r": rng.uniform(1.2, 2.6),
            }
        )
    now = pygame.time.get_ticks()
    return {
        "center": center,
        "born": int(now),
        "expire": int(now + V115_FULMEN_SCORCH_LIFETIME_MS),
        "cracks": cracks,
        "blots": blots,
        "embers": embers,
    }
# </POTBO_STAGE S2663>

# <POTBO_STAGE S2666>

def dunya_simulasyon_guncelle():
    result = _v115_world_sim_raw()
    v115_update_scars(pygame.time.get_ticks())
    return result


_v115_world_draw_raw = dunya_aktorlerini_derinlige_gore_ciz

def dunya_aktorlerini_derinlige_gore_ciz():
    result = _v115_world_draw_raw()
    v115_draw_scars()
    return result
# </POTBO_STAGE S2666>

# <POTBO_STAGE S2669>



def v115_spawn_scorch(center, seed=0):
    center = pygame.Vector2(center)
    rng = random.Random(int(seed) ^ 0x15C0)
    cracks = []
    for _ in range(rng.randint(4, 6)):
        angle = rng.uniform(0.0, math.tau)
        length = rng.uniform(12.0, 34.0)
        end = pygame.Vector2(
            center.x + math.cos(angle) * length,
            center.y + math.sin(angle) * length * rng.uniform(0.25, 0.55),
        )
        cracks.append(
            v110_polyline_points(
                center,
                end,
                jitter=3.6,
                segments=rng.randint(2, 4),
                seed=rng.randint(0, 10**6),
            )
        )
    blots = []
    for _ in range(rng.randint(4, 6)):
        blots.append(
            {
                "ox": rng.uniform(-15.0, 15.0),
                "oy": rng.uniform(-6.0, 6.0),
                "rx": rng.uniform(7.0, 18.0),
                "ry": rng.uniform(3.0, 9.0),
                "a": rng.randint(62, 108),
            }
        )
    embers = []
    for _ in range(rng.randint(10, 16)):
        embers.append(
            {
                "x": center.x + rng.uniform(-9.0, 9.0),
                "y": center.y + rng.uniform(-3.0, 2.0),
                "vx": rng.uniform(-11.0, 11.0),
                "vy": rng.uniform(-28.0, -12.0),
                "life": rng.randint(900, V115_FULMEN_EMBER_LIFETIME_MS),
                "age": rng.randint(0, 140),
                "r": rng.uniform(1.3, 3.0),
                "drift": rng.uniform(0.6, 1.7),
            }
        )
    now = pygame.time.get_ticks()
    return {
        "center": center,
        "born": int(now),
        "expire": int(now + V115_FULMEN_SCORCH_LIFETIME_MS),
        "cracks": cracks,
        "blots": blots,
        "embers": embers,
    }
# </POTBO_STAGE S2669>

