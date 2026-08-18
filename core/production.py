
# <POTBO_STAGE S9000>

STUDIO_NAME = "Agraphon Studios"
GAME_TITLE = "Path of the Bloodied One"
GELISTIRICI_MODU = os.environ.get("PATH_BLOODIED_DEV", "1").strip().lower() not in {"0", "false", "no", "off"}



PRECIOSA_SHEET_YOLU = os.path.join(ASSETS, "characters", "preciosa_spriteSheet.png")
PRECIOSA_LOCOMOTION_RECTLERI = [
    (10, 11, 35, 49), (52, 12, 40, 48), (101, 12, 33, 48),
    (149, 11, 30, 49), (187, 13, 27, 47), (223, 13, 35, 47),
    (276, 11, 33, 49), (319, 13, 36, 49), (362, 13, 33, 49),
]
PRECIOSA_NORMAL_ATTACK_RECTLERI = [
    (9, 75, 36, 49), (53, 88, 38, 46),
    (109, 80, 34, 48), (148, 92, 48, 43),
    (212, 88, 36, 48), (254, 73, 36, 60),
]

preciosa_sheet = resim_yukle(PRECIOSA_SHEET_YOLU)
_p_loco_raw = _adefonsus_sheet_karelerini_cikar(preciosa_sheet, PRECIOSA_LOCOMOTION_RECTLERI)
_p_attack_raw = _adefonsus_sheet_karelerini_cikar(preciosa_sheet, PRECIOSA_NORMAL_ATTACK_RECTLERI)
_p_loco_down = _adefo_grubu(_p_loco_raw, 0, 3, 4)
_p_loco_left = _adefo_grubu(_p_loco_raw, 3, 3, 4)
_p_loco_up = _adefo_grubu(_p_loco_raw, 6, 3, 4)
_p_atk_down = _adefo_grubu(_p_attack_raw, 0, 2, 5)
_p_atk_left = _adefo_grubu(_p_attack_raw, 2, 2, 5)
_p_atk_up = _adefo_grubu(_p_attack_raw, 4, 2, 5)


def _preciosa_hold_grubu(loco, attack):
    if not loco or not attack:
        return []


    return _kareleri_ortak_canvas_yap([loco[0], loco[0], attack[-1]], padding=6)


_p_hold_down = _preciosa_hold_grubu(_p_loco_down, _p_atk_down)
_p_hold_left = _preciosa_hold_grubu(_p_loco_left, _p_atk_left)
_p_hold_up = _preciosa_hold_grubu(_p_loco_up, _p_atk_up)
PRECIOSA_SPRITELERI = {
    "down": {"idle": _p_loco_down[:1], "walk": _p_loco_down[:1] + _p_loco_down[1:2] + _p_loco_down[:1] + _p_loco_down[2:3], "attack": _p_atk_down, "hold": _p_hold_down},
    "left": {"idle": _p_loco_left[:1], "walk": _p_loco_left[:1] + _p_loco_left[1:2] + _p_loco_left[:1] + _p_loco_left[2:3], "attack": _p_atk_left, "hold": _p_hold_left},
    "up": {"idle": _p_loco_up[:1], "walk": _p_loco_up[:1] + _p_loco_up[1:2] + _p_loco_up[:1] + _p_loco_up[2:3], "attack": _p_atk_up, "hold": _p_hold_up},
}
PRECIOSA_YENI_SHEET_AKTIF = all(
    PRECIOSA_SPRITELERI[y][a]
    for y in ("down", "left", "up")
    for a in ("idle", "walk", "attack", "hold")
)




if PRECIOSA_YENI_SHEET_AKTIF:
    kadin_animasyonlari = {
        "idle": list(PRECIOSA_SPRITELERI["down"]["idle"]),
        "walk": list(PRECIOSA_SPRITELERI["down"]["walk"]),
        "attack": list(PRECIOSA_SPRITELERI["down"]["attack"]),
    }


def oyuncu_yeni_sheet_aktif_mi():
    if karakter_cinsiyet == "female":
        return bool(PRECIOSA_YENI_SHEET_AKTIF)
    return bool(ADEFONSUS_YENI_SHEET_AKTIF)


def preciosa_yon_animasyon_kareleri(animasyon_adi, yon=None):
    yon = oyuncu_yonu if yon is None else str(yon)
    kaynak = "up" if yon == "up" else ("left" if yon in ("left", "right") else "down")
    veri = PRECIOSA_SPRITELERI.get(kaynak, PRECIOSA_SPRITELERI["down"])
    if animasyon_adi == "hold_charge":
        return veri.get("hold", [])[:2]
    if animasyon_adi == "hold_release":
        hold = veri.get("hold", [])
        return hold[2:3] if len(hold) >= 3 else hold[-1:]
    return veri.get(animasyon_adi, [])


_prod_aktif_animasyon_onceki = aktif_animasyon_kareleri
def aktif_animasyon_kareleri(animasyon_adi):
    if karakter_cinsiyet == "female" and PRECIOSA_YENI_SHEET_AKTIF:
        kareler = temiz_kareler(preciosa_yon_animasyon_kareleri(animasyon_adi, oyuncu_yonu))
        if kareler:
            return kareler
        if animasyon_adi in ("hold_charge", "hold_release"):
            kareler = temiz_kareler(preciosa_yon_animasyon_kareleri("attack", oyuncu_yonu))
            if kareler:
                return kareler
    return _prod_aktif_animasyon_onceki(animasyon_adi)


def oyuncu_render_flip_gerekli_mi(yon=None):
    yon = oyuncu_yonu if yon is None else str(yon)
    if karakter_cinsiyet == "female" and PRECIOSA_YENI_SHEET_AKTIF:
        return yon == "right"
    return bool(adefonsus_render_flip_gerekli_mi(yon))


def oyuncu_sprite_ciz():
    global animasyon_index
    global animasyon_zamani

    oyuncu_ekran_x = dunya_ekran_x(oyuncu_x)
    oyuncu_ekran_y = dunya_ekran_y(oyuncu_y)


    karakter_zemin_golgesi_ciz(
        oyuncu_ekran_x,
        oyuncu_ekran_y - 3,
        34 * KAMERA_YAKINLASTIRMA,
        7 * KAMERA_YAKINLASTIRMA,
        68,
    )

    yeni_karakter = oyuncu_yeni_sheet_aktif_mi()
    if oyuncu_savunuyor:

        animasyon_adi = "hold_charge" if yeni_karakter else "idle"
    elif gelistirici_x_skill_aktif_mi():


        animasyon_adi = "hold_release" if yeni_karakter else "attack"
    elif oyuncu_saldiriyor:
        if yeni_karakter and oyuncu_saldiri_modu in (
            "press",
            "charge",
        ):
            animasyon_adi = "hold_charge"
        elif yeni_karakter and oyuncu_saldiri_modu == "hold_release":
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

    if yeni_karakter and animasyon_adi == "hold_charge":


        if oyuncu_savunuyor:
            animasyon_index = 0



        elif oyuncu_saldiri_modu == "press" or len(kareler) == 1:
            animasyon_index = 0
        else:
            gecen = max(0, simdi - adefo_hold_charge_baslangic_ms)
            animasyon_index = int(gecen // ADEFO_HOLD_CHARGE_FRAME_MS) % min(
                2, len(kareler)
            )

    elif yeni_karakter and animasyon_adi == "hold_release":

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


            hiz_orani = min(
                1.0,
                oyuncu_hareket_hiz_vektoru.length() / max(1.0, OYUNCU_YURUYUS_HIZI),
            )
            taban = 92 if yeni_karakter else 140
            gecikme = int(round(taban + (1.0 - hiz_orani) * 48))
        else:
            gecikme = 240

        if simdi - animasyon_zamani >= gecikme:
            animasyon_zamani = simdi
            animasyon_index = (animasyon_index + 1) % len(kareler)

    kare = kareler[animasyon_index % len(kareler)]

    if karakter_cinsiyet == "male":
        if yeni_karakter:
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
        if animasyon_adi == "hold_release":
            taban_yukseklik = 66
        elif animasyon_adi in ("attack", "hold_charge"):
            taban_yukseklik = 64
        else:
            taban_yukseklik = 58

    hedef_yukseklik = int(round(taban_yukseklik * KAMERA_YAKINLASTIRMA))


    if animasyon_adi == "idle" and not oyuncu_saldiriyor:
        nefes = 0.5 + 0.5 * math.sin(simdi * 0.0026)
        if nefes > 0.58:
            hedef_yukseklik += 1


    oyuncu_flip = bool(yeni_karakter and oyuncu_render_flip_gerekli_mi(oyuncu_yonu))
    onbellek_anahtari = (
        id(kare),
        hedef_yukseklik,
        "player_right_flip" if oyuncu_flip else "normal",
    )

    olcekli_kare = sprite_olcek_onbellegi.get(onbellek_anahtari)
    if olcekli_kare is None:
        oran = hedef_yukseklik / max(1, kare.get_height())
        hedef_genislik = max(1, int(round(kare.get_width() * oran)))
        olcekli_kare = pygame.transform.scale(kare, (hedef_genislik, hedef_yukseklik))
        if oyuncu_flip:
            olcekli_kare = pygame.transform.flip(olcekli_kare, True, False)
        sprite_olcek_onbellegi[onbellek_anahtari] = olcekli_kare

    rect = olcekli_kare.get_rect(midbottom=(oyuncu_ekran_x, oyuncu_ekran_y))
    ekran.blit(olcekli_kare, rect)



    if yeni_karakter and oyuncu_saldiriyor and oyuncu_saldiri_modu == "charge":
        charge_gecen = max(0, simdi - adefo_hold_charge_baslangic_ms)
        faz = (charge_gecen // ADEFO_HOLD_FLASH_MS) % 2
        if faz == 0:
            sprite_maskeli_parlama_ciz(olcekli_kare, rect, (238, 238, 238), 96)

    oyuncu_sprite_parlamasi_ciz(olcekli_kare, rect)
    fire_magic_burn_overlay_oyuncu_ciz(olcekli_kare, rect)




PRECIOSA_NORMAL_SURE_MS = 215

def _adefo_normal_saldiriyi_commit_et(simdi):
    global oyuncu_saldiri_modu, oyuncu_saldiri_sure_ms
    global saldiri_baslangic, son_saldiri_zamani, animasyon_index
    global ADEFO_HOLD_GECIS_YAPILDI
    oyuncu_saldiri_modu = "normal"
    oyuncu_saldiri_sure_ms = (PRECIOSA_NORMAL_SURE_MS if karakter_cinsiyet == "female" else ADEFO_NORMAL_SURE_MS)
    ADEFO_HOLD_GECIS_YAPILDI = True
    saldiri_baslangic = int(simdi)
    son_saldiri_zamani = int(simdi)
    animasyon_index = 0
    dunya_olayi_kaydet("attack", mode="normal")


def adefonsus_charge_yon_guncelle():
    global oyuncu_yonu, adefo_hold_charge_yonu
    if not oyuncu_yeni_sheet_aktif_mi() or not oyuncu_saldiriyor or oyuncu_saldiri_modu not in ("press", "charge"):
        return
    try:
        tuslar = pygame.key.get_pressed()
    except pygame.error:
        return
    dx = int(bool(tuslar[tus_atamasi("move_right")])) - int(bool(tuslar[tus_atamasi("move_left")]))
    dy = int(bool(tuslar[tus_atamasi("move_down")])) - int(bool(tuslar[tus_atamasi("move_up")]))
    if dx == 0 and dy == 0:
        return
    if abs(dy) > abs(dx):
        oyuncu_yonu = "down" if dy > 0 else "up"
    elif dx != 0:
        oyuncu_yonu = "right" if dx > 0 else "left"
    adefo_hold_charge_yonu = oyuncu_yonu


def adefonsus_saldiri_tusu_birakildi(simdi=None):
    global v44_last_player_swing_release_ms, v44_last_player_attack_mode
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if not oyuncu_saldiriyor or not oyuncu_yeni_sheet_aktif_mi():
        return False
    if "v44_last_player_swing_release_ms" in globals():
        v44_last_player_swing_release_ms = int(simdi)
    if oyuncu_saldiri_modu == "press":
        gecen = int(simdi) - int(adefo_saldiri_tusu_baslangic_ms)
        if gecen >= ADEFO_HOLD_ESIK_MS and _adefo_hold_charge_baslat(simdi):
            _adefo_hold_release_baslat(simdi)
        else:
            _adefo_normal_saldiriyi_commit_et(simdi)
        ok = True
    elif oyuncu_saldiri_modu == "charge":
        _adefo_hold_release_baslat(simdi)
        ok = True
    else:
        ok = False
    if "v44_last_player_attack_mode" in globals():
        v44_last_player_attack_mode = str(oyuncu_saldiri_modu)
    return ok


def oyuncu_saldiri_gecislerini_guncelle(simdi=None):
    global stamina_son_harcama
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if not oyuncu_saldiriyor or not oyuncu_yeni_sheet_aktif_mi():
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
    elif oyuncu_saldiri_modu == "charge":
        if not oyuncu_saldiri_tusu_basili_mi():
            _adefo_hold_release_baslat(simdi)


_prod_hit_window_onceki = oyuncu_saldiri_vurus_penceresi_aktif_mi
def oyuncu_saldiri_vurus_penceresi_aktif_mi(simdi=None):
    if not oyuncu_saldiriyor:
        return False
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if oyuncu_yeni_sheet_aktif_mi():
        if oyuncu_saldiri_modu in ("press", "charge"):
            return False
        sure = max(1.0, float(oyuncu_aktif_saldiri_suresi_ms()))
        ilerleme = (simdi - saldiri_baslangic) / sure
        if oyuncu_saldiri_modu == "hold_release":
            return 0.04 <= ilerleme <= 0.70
        return (0.20 <= ilerleme <= 0.70) if karakter_cinsiyet == "female" else (0.28 <= ilerleme <= 0.72)
    return _prod_hit_window_onceki(simdi)


_prod_hit_rect_onceki = oyuncu_saldiri_vurus_rect
def oyuncu_saldiri_vurus_rect():
    if oyuncu_yeni_sheet_aktif_mi() and oyuncu_saldiri_modu in ("press", "charge"):
        return pygame.Rect(int(round(oyuncu_x)), int(round(oyuncu_y)), 1, 1)
    if oyuncu_saldiri_modu != "hold_release":
        return _prod_hit_rect_onceki()
    nr, nw, hr, hw = _v38_player_reach_values()
    if karakter_cinsiyet == "female":
        reach = max(nr, int(round(hr * 0.88)))
        width = max(nw, int(round(hw * 0.90)))
    else:
        reach, width = hr, hw
    cx = int(round(oyuncu_x)); cy = int(round(oyuncu_y - 18)); back = 2
    if oyuncu_yonu == "left": return pygame.Rect(cx - reach, cy - width // 2, reach + back, width)
    if oyuncu_yonu == "right": return pygame.Rect(cx - back, cy - width // 2, reach + back, width)
    if oyuncu_yonu == "up": return pygame.Rect(cx - width // 2, cy - reach, width, reach + back)
    return pygame.Rect(cx - width // 2, cy - back, width, reach + back)




_prod_free_move_onceki = oyuncu_serbest_hareket_guncelle
def oyuncu_serbest_hareket_guncelle():
    global V90_BASE_WALK_SPEED
    onceki = float(V90_BASE_WALK_SPEED)
    if karakter_cinsiyet == "female":
        V90_BASE_WALK_SPEED = onceki * 1.08
    try:
        return _prod_free_move_onceki()
    finally:
        V90_BASE_WALK_SPEED = onceki


_prod_footstep_onceki = adefonsus_footstep_guncelle
def adefonsus_footstep_guncelle():


    if karakter_cinsiyet == "female" and adefonsus_footstep_kanali is not None and adefonsus_footstep_sesi is not None:
        simdi = pygame.time.get_ticks()
        hiz = oyuncu_hareket_hiz_vektoru.length() if isinstance(oyuncu_hareket_hiz_vektoru, pygame.Vector2) else 0.0
        aktif = bool(oyun_durumu == OYUN and oyun_alt_durumu == HARITA and oyuncu_hp > 0 and oyuncu_hareket_ediyor and hiz >= OYUNCU_YURUYUS_HIZI * 0.16 and not oyun_sinematik_kilitli_mi() and not oyuncu_dash_aktif_mi(simdi))
        if aktif:
            hiz_orani = max(0.30, min(1.0, hiz / max(1.0, OYUNCU_YURUYUS_HIZI)))
            adefonsus_footstep_kanali.set_volume(_v35_footstep_ses_orani() * (0.48 + 0.36 * hiz_orani))
            if not adefonsus_footstep_kanali.get_busy():
                adefonsus_footstep_kanali.play(adefonsus_footstep_sesi, loops=-1, fade_ms=35)
        elif adefonsus_footstep_kanali.get_busy():
            adefonsus_footstep_kanali.fadeout(70)
        return
    return _prod_footstep_onceki()









AGRAPHON_TEST_SPELLS = {
    pygame.K_1: ("fire_magic", fire_magic_olustur, "Sphaera Exothermica"),
    pygame.K_2: ("draco_calcinans", draco_calcinans_olustur, "Draco Calcinans"),
    pygame.K_3: ("corona_aetherica", corona_aetherica_olustur, "Corona Aetherica"),
    pygame.K_4: ("fulmen_caeruleum", fulmen_caeruleum_olustur, "Fulmen Caeruleum"),
}
AGRAPHON_TEST_PANEL_VISIBLE = False
GELISTIRICI_TEST_TUSLARI.update({
    pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
    pygame.K_u, pygame.K_i, pygame.K_o, pygame.K_QUOTE,
})


def _agraphon_modifier_mask(olay):
    mask = int(getattr(olay, "mod", 0) or 0)
    try:
        mask |= int(pygame.key.get_mods())
    except pygame.error:
        pass
    return mask


def _agraphon_ctrl_held(olay):
    return bool(_agraphon_modifier_mask(olay) & pygame.KMOD_CTRL)


def _agraphon_panel_shortcut(olay):
    mask = _agraphon_modifier_mask(olay)
    if olay.key == pygame.K_QUOTE:
        return True
    if str(getattr(olay, "unicode", "")) == '"':
        return True
    return olay.key == pygame.K_2 and bool(mask & pygame.KMOD_SHIFT)


def _agraphon_test_item_index(item_id):
    for index, item in enumerate(envanter_itemleri):
        if isinstance(item, dict) and item.get("id") == item_id:
            return index
    return None


def _agraphon_test_spell_grant(item_id, factory, display_name):
    global fire_magic_son_kullanim, fire_magic_cast_lock_until
    global v90_draco_last_cast_ms, v106_corona_last_cast_ms
    global v107_corona_test_cast_ready, v110_fulmen_last_cast_ms

    index = _agraphon_test_item_index(item_id)
    if index is None:
        item = factory()
        if not envantere_item_ekle(item, kazanimi_goster=False):
            try:
                envanter_itemleri.append(item)
            except Exception:
                bildirim_goster(bt("Test büyüsü verilemedi.", "Could not grant test spell."), V91_UI_RED_HOT)
                return True
        index = _agraphon_test_item_index(item_id)

    if index is None:
        bildirim_goster(bt("Test büyüsü verilemedi.", "Could not grant test spell."), V91_UI_RED_HOT)
        return True

    V108_DEV_UNLIMITED_SPELLS.add(str(item_id))
    itemi_q_hizli_slota_ata(index)

    if item_id == "fire_magic":
        fire_magic_son_kullanim = -1000000
        fire_magic_cast_lock_until = 0
    elif item_id == "draco_calcinans":
        v90_draco_last_cast_ms = -1000000
    elif item_id == "corona_aetherica":
        v106_corona_last_cast_ms = -1000000
        v107_corona_test_cast_ready = True
    elif item_id == "fulmen_caeruleum":
        v110_fulmen_last_cast_ms = -1000000

    bildirim_goster(f"{display_name} → Q · ∞ · 0 mana", V91_UI_GOLD)
    return True


def _agraphon_test_potions_grant():
    health_ok = envantere_item_ekle(can_iksiri_olustur(), kazanimi_goster=False)
    mana_ok = envantere_item_ekle(quinta_essentia_olustur(), kazanimi_goster=False)
    if health_ok and mana_ok:
        bildirim_goster(bt("Can İksiri +1 · Quinta Essentia +1", "Health Potion +1 · Quinta Essentia +1"), V91_UI_GOLD)
    elif health_ok:
        bildirim_goster(bt("Can İksiri +1 · Mana iksiri için envanter dolu.", "Health Potion +1 · Inventory full for mana potion."), V91_UI_RED_HOT)
    elif mana_ok:
        bildirim_goster(bt("Quinta Essentia +1 · Can iksiri için envanter dolu.", "Quinta Essentia +1 · Inventory full for health potion."), V91_UI_RED_HOT)
    else:
        bildirim_goster(bt("Envanter dolu.", "Inventory is full."), V91_UI_RED_HOT)
    return True


def gelistirici_test_girdisi_uygula(olay):
    global oyuncu_altin, AGRAPHON_TEST_PANEL_VISIBLE

    if not GELISTIRICI_MODU or olay.type != pygame.KEYDOWN or not _agraphon_ctrl_held(olay):
        return False

    if _agraphon_panel_shortcut(olay):
        AGRAPHON_TEST_PANEL_VISIBLE = not AGRAPHON_TEST_PANEL_VISIBLE
        bildirim_goster(
            bt(
                "Test kısayol paneli açık." if AGRAPHON_TEST_PANEL_VISIBLE else "Test kısayol paneli kapalı.",
                "Test shortcut panel opened." if AGRAPHON_TEST_PANEL_VISIBLE else "Test shortcut panel closed.",
            ),
            V91_UI_GOLD,
        )
        return True

    spell = AGRAPHON_TEST_SPELLS.get(olay.key)
    if spell is not None:
        return _agraphon_test_spell_grant(*spell)

    if olay.key == pygame.K_u:
        oyuncu_altin += 1000
        bildirim_goster("+1000 Coin", V91_UI_GOLD)
        return True

    if olay.key == pygame.K_i:
        old_level = int(oyuncu_level)
        target_level = min(MAKSIMUM_LEVEL, old_level + 10)
        oyuncu_level_ayarla(target_level, bildirim=False)
        gained = max(0, int(oyuncu_level) - old_level)
        bildirim_goster(bt(f"+{gained} seviye · Lv.{oyuncu_level}", f"+{gained} levels · Lv.{oyuncu_level}"), V91_UI_GOLD)
        return True

    if olay.key == pygame.K_o:
        return _agraphon_test_potions_grant()

    return False


def gelistirici_test_paneli_ciz():
    if not GELISTIRICI_MODU or not AGRAPHON_TEST_PANEL_VISIBLE or oyun_durumu != OYUN:
        return None

    rows = (
        ("CTRL+1", "Sphaera Exothermica → Q · ∞ · 0 mana"),
        ("CTRL+2", "Draco Calcinans → Q · ∞ · 0 mana"),
        ("CTRL+3", "Corona Aetherica → Q · ∞ · 0 mana"),
        ("CTRL+4", "Fulmen Caeruleum → Q · ∞ · 0 mana"),
        ("CTRL+U", bt("+1000 Coin", "+1000 Coin")),
        ("CTRL+I", bt("+10 seviye", "+10 levels")),
        ("CTRL+O", bt("+1 Can İksiri · +1 Mana İksiri", "+1 Health Potion · +1 Mana Potion")),
        ('CTRL+"', bt("paneli aç / kapat", "toggle panel")),
    )
    width = 520
    line_h = 24
    rect = pygame.Rect(GENISLIK - width - 16, 16, width, 58 + line_h * len(rows))
    v89_medieval_panel(rect, V91_UI_RED, 242)
    yazi_yaz(bt("TEST KISAYOLLARI", "TEST SHORTCUTS"), rect.x + 16, rect.y + 14, V91_UI_WHITE, normal_font)
    y = rect.y + 48
    for key, description in rows:
        yazi_yaz(key, rect.x + 16, y, V91_UI_GOLD, mini_font)
        yazi_yaz(description, rect.x + 132, y, ACIK_GRI, mini_font)
        y += line_h
    return rect


splash_ekrani_goster()
# </POTBO_STAGE S9000>
