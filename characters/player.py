






# <POTBO_STAGE S0116>

karakter_secim_index = 0
oyuncu_adi = ""
karakter_cinsiyet = "male"
# </POTBO_STAGE S0116>

# <POTBO_STAGE S0121>

oyuncu_level = 1
oyuncu_altin = 23

oyuncu_guc = 5
# </POTBO_STAGE S0121>

# <POTBO_STAGE S0123>

oyuncu_hp = 100
oyuncu_max_hp = 100

oyuncu_mana = 50
oyuncu_max_mana = 50
# </POTBO_STAGE S0123>

# <POTBO_STAGE S0128>
oyuncu_parlama_turu = None
oyuncu_parlama_baslangic = 0
oyuncu_parlama_bitis = 0
# </POTBO_STAGE S0128>

# <POTBO_STAGE S0137>
oyuncu_fire_burn_next_tick = 0
# </POTBO_STAGE S0137>

# <POTBO_STAGE S0139>
oyuncu_fire_burn_source = ""
# </POTBO_STAGE S0139>

# <POTBO_STAGE S0141>
oyuncu_zorlanmis_hiz = pygame.Vector2(0.0, 0.0)
oyuncu_zorlanmis_bitis = 0
oyuncu_zorlanmis_son_guncelleme = pygame.time.get_ticks()
oyuncu_agir_darbe_bagisiklik_bitis = 0
# </POTBO_STAGE S0141>

# <POTBO_STAGE S0143>
oyuncu_kesik_efekti_acisi = -18.0
oyuncu_son_infaz_kaynagi = ""
# </POTBO_STAGE S0143>

# <POTBO_STAGE S0151>
oyuncu_olum_arter_sonraki_ms = 0
# </POTBO_STAGE S0151>

# <POTBO_STAGE S0153>
oyuncu_olum_ikiye_bolundu = False



oyuncu_olum_kesim_acisi = 22.0
oyuncu_olum_kesim_ofset_orani = 0.52
oyuncu_son_darbe_profili = "slash"
oyuncu_son_darbe_kaynagi = ""
# </POTBO_STAGE S0153>

# <POTBO_STAGE S0155>
oyuncu_olum_katil_tur = ""
# </POTBO_STAGE S0155>

# <POTBO_STAGE S0157>
oyuncu_olum_ates_seed = 0


oyuncu_olum_patlama_seed = 0
oyuncu_olum_patlama_yonu = pygame.Vector2(1.0, 0.0)


oyuncu_olum_alt_turu = ""
oyuncu_olum_koreografi_seed = 0
oyuncu_olum_koreografi_vuruslari = set()
# </POTBO_STAGE S0157>

# <POTBO_STAGE S0159>
oyuncu_olum_cikis_baslangic_ms = 0
oyuncu_olum_cikis_hedefi = None
# </POTBO_STAGE S0159>

# <POTBO_STAGE S0166>
oyuncu_y = 585.0
# </POTBO_STAGE S0166>

# <POTBO_STAGE S0169>

oyuncu_hizi = 4.0
oyuncu_yonu = "right"




OYUNCU_YURUYUS_HIZI = oyuncu_hizi * FPS
OYUNCU_HIZLANMA = 1080.0
OYUNCU_YAVASLAMA = 1420.0
OYUNCU_DONUS_IVMESI = 1680.0
oyuncu_hareket_hiz_vektoru = pygame.Vector2(0.0, 0.0)
oyuncu_hareket_son_guncelleme = pygame.time.get_ticks()

oyuncu_hareket_ediyor = False
# </POTBO_STAGE S0169>

# <POTBO_STAGE S0299>


def aktif_animasyonlar():
    """
    Eski çağrılar için korunur.
    """
    if karakter_cinsiyet == "male":
        return erkek_animasyonlari

    return kadin_animasyonlari
# </POTBO_STAGE S0299>

# <POTBO_STAGE S0318>


def oyuncu_level_ayarla(yeni_level, bildirim=True):
    """Her gerçek level-up doğrudan stat büyütür; 10. seviye ağır gruba yaklaşır."""
    global oyuncu_level
    eski_level = max(1, min(MAKSIMUM_LEVEL, int(oyuncu_level)))
    hedef = max(1, min(MAKSIMUM_LEVEL, int(yeni_level)))
    if hedef > eski_level:
        oyuncu_seviye_kazanclarini_uygula(eski_level, hedef)
    oyuncu_level = hedef
    if bildirim and oyuncu_level > eski_level:
        seviye_atladi_bildirimi(oyuncu_level)
# </POTBO_STAGE S0318>

# <POTBO_STAGE S0339>


def _stage1_oyuncu_sprite_parlamasi_ciz(sprite, rect):
    """
    İksir geri bildirimi kutu/halo değildir: yalnız oyuncu sprite'ının opak pikselleri
    0.43 saniyelik kırmızı-beyaz bir içim flaşı taşır. Kısa beyaz vuruşlar "şişe
    ağza gitti" anını, kırmızı bölüm ise can/beden etkisini okunur kılar.
    """
    simdi = pygame.time.get_ticks()
    if sprite is None or rect is None or simdi >= oyuncu_parlama_bitis:
        return

    bas = int(oyuncu_parlama_baslangic or (oyuncu_parlama_bitis - 430))
    toplam = max(1, oyuncu_parlama_bitis - bas)
    p = max(0.0, min(1.0, (simdi - bas) / float(toplam)))
    fade = math.sin(math.pi * p) ** 0.72



    faz = int(min(3, p * 4.0))
    if faz in (0, 2):
        renk = (248, 244, 238)
        alfa = int(132 * fade)
    else:
        renk = (225, 30, 38)
        alfa = int(118 * fade)
    sprite_maskeli_parlama_ciz(sprite, rect, renk, alfa)


oyuncu_sprite_parlamasi_ciz = _stage1_oyuncu_sprite_parlamasi_ciz
# </POTBO_STAGE S0339>

# <POTBO_STAGE S0358>


def level_test_arttir():
    if oyuncu_level >= MAKSIMUM_LEVEL:
        bildirim_goster(
            bt("MAKSİMUM SEVİYE: 50", "MAXIMUM LEVEL: 50"),
            level_rengi(MAKSIMUM_LEVEL),
            level_rengi(MAKSIMUM_LEVEL),
        )
        return

    oyuncu_level_ayarla(oyuncu_level + 1, True)
# </POTBO_STAGE S0358>

# <POTBO_STAGE S0381>


def oyuncu_ayak_noktalari(x, y):
    """
    Ayak tabanını tek nokta yerine kısa bir elips gibi örnekler. Böylece
    karakterin omzu veya kılıcı değil, zemine temas eden bölümü çarpışır.
    """
    yaricap_x = 11
    ust_y = y - 12
    orta_y = y - 7
    alt_y = y - 2

    return [
        (x, ust_y),
        (x - 7, ust_y + 2),
        (x + 7, ust_y + 2),
        (x - yaricap_x, orta_y),
        (x - 5, orta_y),
        (x, orta_y),
        (x + 5, orta_y),
        (x + yaricap_x, orta_y),
        (x - 8, alt_y),
        (x, alt_y),
        (x + 8, alt_y),
    ]
# </POTBO_STAGE S0381>

# <POTBO_STAGE S0401>


def eadric_yakin_mi():
    """Eadric etkileşimi sprite ayağı etrafında toleranslı bir elips kullanır."""
    dx = (float(oyuncu_x) - float(npc_x)) / 82.0
    dy = (float(oyuncu_y) - float(npc_y)) / 62.0
    return dx * dx + dy * dy <= 1.0
# </POTBO_STAGE S0401>

# <POTBO_STAGE S0498>


def oyuncu_parlama_baslat(tur):
    global oyuncu_parlama_turu, oyuncu_parlama_baslangic, oyuncu_parlama_bitis
    simdi = pygame.time.get_ticks()
    oyuncu_parlama_turu = tur
    oyuncu_parlama_baslangic = simdi
    oyuncu_parlama_bitis = simdi + 430
# </POTBO_STAGE S0498>

# <POTBO_STAGE S0509>


oyuncu_olum_sahnesini_sifirla = _stage1_oyuncu_olum_sahnesini_sifirla
# </POTBO_STAGE S0509>

# <POTBO_STAGE S0512>


def oyuncu_olum_cikis_orani(simdi=None):
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if oyuncu_olum_cikis_baslangic_ms <= 0:
        return 0.0
    p = max(
        0.0,
        min(
            1.0,
            (int(simdi) - int(oyuncu_olum_cikis_baslangic_ms))
            / max(1.0, float(OLU_CIKIS_FADE_MS)),
        ),
    )
    return p * p * (3.0 - 2.0 * p)
# </POTBO_STAGE S0512>

# <POTBO_STAGE S0520>


_v30_oyuncu_ozel_ceset_ciz = _stage1__v30_oyuncu_ozel_ceset_ciz
# </POTBO_STAGE S0520>

# <POTBO_STAGE S0524>


_oyuncu_yatay_siluet_ciz = _stage1__oyuncu_yatay_siluet_ciz
# </POTBO_STAGE S0524>

# <POTBO_STAGE S0526>


_v26_oyuncu_patlama_siluet_parcalari_ciz = (
    _stage1__v26_oyuncu_patlama_siluet_parcalari_ciz
)
# </POTBO_STAGE S0526>

# <POTBO_STAGE S0531>


oyuncu_olum_sahnesi_ciz = _stage1_oyuncu_olum_sahnesi_ciz
# </POTBO_STAGE S0531>

# <POTBO_STAGE S0534>


def oyuncu_kesik_efekti_ciz():
    """Sprite gerektirmeyen kısa slash feedback'i; oyun dünyasını kapatmaz."""
    simdi = pygame.time.get_ticks()
    if simdi >= oyuncu_kesik_efekti_bitis:
        return
    kalan = max(
        0.0,
        min(1.0, (oyuncu_kesik_efekti_bitis - simdi) / 520.0),
    )
    alfa = int(210 * min(1.0, kalan * 1.8))
    katman = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    merkez = pygame.Vector2(GENISLIK * 0.5, YUKSEKLIK * 0.48)
    uzun = min(GENISLIK, YUKSEKLIK) * 0.62
    yon = pygame.Vector2(1.0, 0.0).rotate(oyuncu_kesik_efekti_acisi)
    dik = pygame.Vector2(-yon.y, yon.x)
    a = merkez - yon * uzun * 0.5
    b = merkez + yon * uzun * 0.5
    pygame.draw.line(katman, (235, 232, 236, alfa), a, b, 5)
    pygame.draw.line(
        katman,
        (126, 8, 20, int(alfa * 0.72)),
        a + dik * 7,
        b + dik * 7,
        3,
    )
    ekran.blit(katman, (0, 0))
# </POTBO_STAGE S0534>

# <POTBO_STAGE S0556>

_v31_olum_reset = oyuncu_olum_sahnesini_sifirla
# </POTBO_STAGE S0556>

# <POTBO_STAGE S0559>


def _stage2_oyuncu_olum_sahnesini_sifirla():
    global \
        V32_OLUM_KATIL_READY_MS, \
        V32_OLUM_KATIL_LAST_UPDATE_MS, \
        V32_OLUM_KATIL_CONTACT
    _v31_olum_reset()
    V32_OLUM_KATIL_READY_MS = 0
    V32_OLUM_KATIL_LAST_UPDATE_MS = 0
    V32_OLUM_KATIL_CONTACT = False


oyuncu_olum_sahnesini_sifirla = _stage2_oyuncu_olum_sahnesini_sifirla
# </POTBO_STAGE S0559>

# <POTBO_STAGE S0571>


_v30_oyuncu_ozel_ceset_ciz = _stage2__v30_oyuncu_ozel_ceset_ciz
# </POTBO_STAGE S0571>

# <POTBO_STAGE S0574>


def _v26_oyuncu_patlama_siluet_parcalari_ciz():
    if oyuncu_olum_turu == "blast_core":
        _v32_patlama_siluet_parcalari_ciz("blast_core")


def _v30_patlama_birinci_katman_siluet_ciz():
    if oyuncu_olum_turu == "blast_inner":
        _v32_patlama_siluet_parcalari_ciz("blast_inner")
# </POTBO_STAGE S0574>

# <POTBO_STAGE S0578>


_v32_olum_reset_v33 = oyuncu_olum_sahnesini_sifirla
# </POTBO_STAGE S0578>

# <POTBO_STAGE S0580>


oyuncu_olum_sahnesini_sifirla = _stage3_oyuncu_olum_sahnesini_sifirla
# </POTBO_STAGE S0580>

# <POTBO_STAGE S0586>


def _v33_rock_impact(self, simdi):
    once_hp = int(oyuncu_hp)
    _v32_rock_impact_v33(self, simdi)
    if int(oyuncu_hp) > 0 and int(oyuncu_hp) < once_hp:
        _v33_oyuncu_kucuk_sektir(self.x, self.y, 82.0, 118)
# </POTBO_STAGE S0586>

# <POTBO_STAGE S0603>


oyuncu_olum_sahnesi_ciz = _stage2_oyuncu_olum_sahnesi_ciz
# </POTBO_STAGE S0603>

# <POTBO_STAGE S0610>


def oyuncu_olum_baslik_fade_orani(simdi=None):
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if oyuncu_olum_baslangic_ms <= 0:
        return 0.0
    gecen = int(simdi) - int(oyuncu_olum_baslangic_ms) - V34_DEATH_TITLE_DELAY_MS
    if gecen <= 0:
        return 0.0
    return _v34_smoothstep01(gecen / max(1.0, float(V34_DEATH_TITLE_FADE_MS)))
# </POTBO_STAGE S0610>

# <POTBO_STAGE S0612>


_v33_olum_reset_v34 = oyuncu_olum_sahnesini_sifirla
# </POTBO_STAGE S0612>

# <POTBO_STAGE S0621>
V34_PLAYER_SAFE_MARGIN_X = 14.0
V34_PLAYER_SAFE_MARGIN_TOP = 16.0
V34_PLAYER_SAFE_MARGIN_BOTTOM = 10.0
# </POTBO_STAGE S0621>

# <POTBO_STAGE S0626>

v34_last_safe_player_pos = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
# </POTBO_STAGE S0626>

# <POTBO_STAGE S0628>
v34_player_was_invalid = False
v34_player_recovery_count = 0
# </POTBO_STAGE S0628>

# <POTBO_STAGE S0631>
v34_special_last_pos = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
# </POTBO_STAGE S0631>

# <POTBO_STAGE S0648>


def _v34_player_position_valid(x, y, dynamic=True, baseline=None, exclude=None):
    if not _v34_static_position_valid(
        x,
        y,
        allow_static_escape=baseline is not None,
        baseline=baseline,
    ):
        return False
    if dynamic and not _v34_dynamic_position_valid(
        x, y, baseline=baseline, exclude=exclude
    ):
        return False
    return True
# </POTBO_STAGE S0648>

# <POTBO_STAGE S0653>


_v33_oyuncu_serbest_hareket_guncelle = oyuncu_serbest_hareket_guncelle


def oyuncu_serbest_hareket_guncelle():
    _v33_oyuncu_serbest_hareket_guncelle()
    _v34_player_safety_tick()
# </POTBO_STAGE S0653>

# <POTBO_STAGE S0659>


def _v34_special_register_trail(simdi, pos, phase="move"):
    global v34_special_last_afterimage_ms
    pos = pygame.Vector2(pos)
    v34_special_trail.append((int(simdi), pos.copy(), str(phase)))
    if (
        int(simdi) - v34_special_last_afterimage_ms
        >= V34_SPECIAL_AFTERIMAGE_INTERVAL_MS
    ):
        v34_special_last_afterimage_ms = int(simdi)
        v34_special_afterimages.append(
            (
                int(simdi),
                pos.copy(),
                str(oyuncu_yonu),
                str(phase),
            )
        )
# </POTBO_STAGE S0659>

# <POTBO_STAGE S0663>


def _v34_special_set_facing(delta):
    global oyuncu_yonu
    delta = pygame.Vector2(delta)
    if abs(delta.x) > abs(delta.y):
        oyuncu_yonu = "right" if delta.x > 0 else "left"
    elif abs(delta.y) > 1e-6:
        oyuncu_yonu = "down" if delta.y > 0 else "up"
# </POTBO_STAGE S0663>

# <POTBO_STAGE S0675>


def oyun_ekrani_ciz():
    _v33_oyun_ekrani_ciz()
    if oyuncu_hp <= 0:
        return
    _v34_special_ready_prompt_ciz()
# </POTBO_STAGE S0675>

# <POTBO_STAGE S0684>
V34_MAX_PLAYER_PROJECTILES = 64
V34_MAX_PLAYER_EXPLOSIONS = 48
# </POTBO_STAGE S0684>

# <POTBO_STAGE S0701>
V34_CROWD_PLAYER_PUSH = 4.2
# </POTBO_STAGE S0701>

# <POTBO_STAGE S0705>
v34_crowd_player_separations = 0
# </POTBO_STAGE S0705>

# <POTBO_STAGE S0708>
v34_last_player_hit_given_ms = 0
v34_last_player_hit_taken_ms = 0
# </POTBO_STAGE S0708>

# <POTBO_STAGE S0753>


def _v34_special_register_trail(simdi, pos, phase="move"):
    global v34_special_last_afterimage_ms
    pos = pygame.Vector2(pos)
    v34_special_trail.append((int(simdi), pos.copy(), str(phase)))
    quality = max(V34_FX_QUALITY_MIN, min(1.0, float(v34_fx_quality)))
    interval = int(V34_SPECIAL_AFTERIMAGE_INTERVAL_MS / quality)
    if int(simdi) - v34_special_last_afterimage_ms >= interval:
        v34_special_last_afterimage_ms = int(simdi)
        v34_special_afterimages.append(
            (
                int(simdi),
                pos.copy(),
                str(oyuncu_yonu),
                str(phase),
            )
        )
# </POTBO_STAGE S0753>

# <POTBO_STAGE S0756>


def oyun_ekrani_ciz():
    _v34e_oyun_ekrani_ciz()
    if oyuncu_hp <= 0:
        return
    _v34_interaction_target_marker_ciz()
# </POTBO_STAGE S0756>

# <POTBO_STAGE S0762>
V34F_PLAYER_COORD_ABS_LIMIT = 1000000.0
# </POTBO_STAGE S0762>

# <POTBO_STAGE S0782>


_v34f_previous_locomotion_reset = oyuncu_locomotion_durumunu_sifirla
# </POTBO_STAGE S0782>

# <POTBO_STAGE S0789>





def _v34f_special_started(simdi):
    global v34f_special_started_seen, v34f_special_last_serial_seen
    global v34f_special_last_center, v34f_special_last_exit
    global v34f_post_special_recovery_until

    v34f_special_started_seen = True
    v34f_special_last_serial_seen = int(v34_special_move_serial)
    v34f_special_last_exit = None
    v34f_post_special_recovery_until = 0
    if v34_special_locked_center is not None:
        v34f_special_last_center = pygame.Vector2(v34_special_locked_center)
    else:
        v34f_special_last_center = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    for i in range(3):
        v34f_special_hit_positions[i] = None
        v34f_special_hit_times[i] = 0
        v34f_special_hit_directions[i] = pygame.Vector2(1.0, 0.0)
    _v34f_special_capture_target_anchor()
# </POTBO_STAGE S0789>

# <POTBO_STAGE S0800>


def oyun_ekrani_ciz():
    _v34f_previous_game_draw()
    if oyuncu_hp <= 0:
        return
    _v34f_special_master_vfx_ciz()





def _v34f_player_coordinates_valid():
    x = _v34f_finite(oyuncu_x, float("nan"))
    y = _v34f_finite(oyuncu_y, float("nan"))
    if not math.isfinite(x) or not math.isfinite(y):
        return False
    return (
        abs(x) <= V34F_PLAYER_COORD_ABS_LIMIT and abs(y) <= V34F_PLAYER_COORD_ABS_LIMIT
    )
# </POTBO_STAGE S0800>

# <POTBO_STAGE S0822>




V35_PLAYER_NORMAL_REACH = 52
V35_PLAYER_NORMAL_WIDTH = 42
V35_PLAYER_HEAVY_REACH = 78
V35_PLAYER_HEAVY_WIDTH = 50
# </POTBO_STAGE S0822>

# <POTBO_STAGE S0857>


def _v34_special_register_trail(simdi, pos, phase="move"):
    """V36: trail'i her simulation frame'inde değil örnekleyerek saklar.

    Hareketin kendisi bu fonksiyona bağlı değildir; yalnız çizilecek geçmiş noktalar
    tutulur. Slash fazlarında daha sık, setup/recovery'de daha seyrek örnek alınır.
    """
    global v34_special_last_afterimage_ms, v36_special_last_trail_ms
    simdi = int(simdi)
    pos = pygame.Vector2(pos)
    phase = str(phase)
    trail_interval = 18 if "slash" in phase else 30
    if (
        simdi - int(v36_special_last_trail_ms) >= trail_interval
        or not v34_special_trail
    ):
        v36_special_last_trail_ms = simdi
        v34_special_trail.append((simdi, pos.copy(), phase))

    quality = max(0.42, min(1.0, float(v34_fx_quality)))
    after_interval = max(52, int(V34_SPECIAL_AFTERIMAGE_INTERVAL_MS / quality))
    if simdi - int(v34_special_last_afterimage_ms) >= after_interval:
        v34_special_last_afterimage_ms = simdi
        v34_special_afterimages.append((simdi, pos.copy(), str(oyuncu_yonu), phase))
# </POTBO_STAGE S0857>

# <POTBO_STAGE S0903>
V34_MAX_PLAYER_PROJECTILES = 36
V34_MAX_PLAYER_EXPLOSIONS = 24
# </POTBO_STAGE S0903>

# <POTBO_STAGE S0923>





_v37_player_safety_tick_original = _v34_player_safety_tick
# </POTBO_STAGE S0923>

# <POTBO_STAGE S0981>







V38_PLAYER_NORMAL_REACH_STRICT = 43
V38_PLAYER_NORMAL_WIDTH_STRICT = 34
V38_PLAYER_NORMAL_REACH_STANDARD = 48
V38_PLAYER_NORMAL_WIDTH_STANDARD = 38
V38_PLAYER_HEAVY_REACH_STRICT = 58
V38_PLAYER_HEAVY_WIDTH_STRICT = 40
V38_PLAYER_HEAVY_REACH_STANDARD = 64
V38_PLAYER_HEAVY_WIDTH_STANDARD = 44
# </POTBO_STAGE S0981>

# <POTBO_STAGE S1047>

V38_PLAYER_NORMAL_REACH_STRICT = 39
V38_PLAYER_NORMAL_WIDTH_STRICT = 32
V38_PLAYER_NORMAL_REACH_STANDARD = 44
V38_PLAYER_NORMAL_WIDTH_STANDARD = 36
V38_PLAYER_HEAVY_REACH_STRICT = 55
V38_PLAYER_HEAVY_WIDTH_STRICT = 38
V38_PLAYER_HEAVY_REACH_STANDARD = 60
V38_PLAYER_HEAVY_WIDTH_STANDARD = 42
# </POTBO_STAGE S1047>

# <POTBO_STAGE S1054>


def v39_character_signature():
    return V39_CHARACTER_SIGNATURES.get(
        karakter_cinsiyet, V39_CHARACTER_SIGNATURES["male"]
    )
# </POTBO_STAGE S1054>

# <POTBO_STAGE S1057>


_v39_level_gain_original = oyuncu_seviye_kazanclarini_uygula
# </POTBO_STAGE S1057>

# <POTBO_STAGE S1126>
V44_PLAYER_DEATH_ARTERIAL_PULSES = (
    1.00,
    0.97,
    0.90,
    0.82,
    0.74,
    0.63,
    0.52,
    0.39,
)
V44_PLAYER_DEATH_ARTERIAL_DURATION_MS = 1250
V44_PLAYER_DEATH_ARTERIAL_MIN_PARTICLES = 20
V44_PLAYER_DEATH_ARTERIAL_MAX_PARTICLES = 34
# </POTBO_STAGE S1126>

# <POTBO_STAGE S1133>
v44_player_death_arterial_done = False
v44_last_player_swing_start_ms = 0
v44_last_player_swing_release_ms = 0
# </POTBO_STAGE S1133>

# <POTBO_STAGE S1138>


def v44_player_facing_vector():
    return v44_direction_name_vector(oyuncu_yonu)
# </POTBO_STAGE S1138>

# <POTBO_STAGE S1149>


class V44ArterialEmitter:
    """Ölüm sonrası nabız ritminde azalan arter fışkırması."""

    def __init__(
        self,
        x,
        y,
        direction,
        started_ms=None,
        profile="heavy_slash",
    ):
        self.x = float(x)
        self.y = float(y)
        self.direction = v44_safe_vec(direction).normalize()
        self.started_ms = int(
            started_ms if started_ms is not None else pygame.time.get_ticks()
        )
        self.next_pulse_ms = self.started_ms
        self.pulse_index = 0
        self.profile = str(profile)
        self.active = True
        self.seed = random.randrange(1, 2**30)
        self.side_bias = random.uniform(-8.0, 8.0)
        self.origin_jitter = pygame.Vector2(
            random.uniform(-2.0, 2.0), random.uniform(-2.0, 2.0)
        )

    def update(self, now):
        if not self.active:
            return
        age = int(now) - self.started_ms
        if age > V44_PLAYER_DEATH_ARTERIAL_DURATION_MS:
            self.active = False
            return
        while (
            self.pulse_index < len(V44_PLAYER_DEATH_ARTERIAL_PULSES)
            and int(now) >= self.next_pulse_ms
        ):
            strength = float(V44_PLAYER_DEATH_ARTERIAL_PULSES[self.pulse_index])
            count = int(
                round(
                    random.randint(
                        V44_PLAYER_DEATH_ARTERIAL_MIN_PARTICLES,
                        V44_PLAYER_DEATH_ARTERIAL_MAX_PARTICLES,
                    )
                    * (0.70 + 0.48 * strength)
                )
            )
            direction = self.direction.rotate(
                self.side_bias + random.uniform(-5.0, 5.0)
            )
            context = v44_blood_spawn_context(
                profile=self.profile,
                lethal=True,
                source="death_artery",
                target="player",
                speed=760.0 * (0.78 + 0.34 * strength),
                direction=direction,
                damage=0,
                arterial=True,
            )
            v44_context_push(context)
            try:
                kan_parcacigi_patlat(
                    self.x + self.origin_jitter.x,
                    self.y + self.origin_jitter.y,
                    count,
                    guc=1.20 + 0.74 * strength,
                    yon=direction,
                    arterial=True,
                )
            finally:
                v44_context_pop()
            self.pulse_index += 1
            self.next_pulse_ms += random.randint(*V44_BLOOD_PULSE_INTERVAL)


def v44_player_death_arterial_start(source_x, source_y, profile="heavy_slash"):
    global v44_player_death_arterial_done
    if v44_player_death_arterial_done:
        return False
    if str(oyuncu_olum_turu) == "fire":
        return False
    source = pygame.Vector2(float(source_x), float(source_y))
    player = pygame.Vector2(float(oyuncu_x), float(oyuncu_y - 12.0))
    direction = player - source
    if direction.length_squared() <= 1e-6:
        direction = v44_player_facing_vector().rotate(180.0)
    direction = direction.normalize().rotate(random.uniform(-16.0, 16.0))
    emitter = V44ArterialEmitter(
        oyuncu_x,
        oyuncu_y - 18.0,
        direction,
        pygame.time.get_ticks(),
        profile=profile,
    )
    v44_arterial_emitters.append(emitter)
    v44_player_death_arterial_done = True
    return True
# </POTBO_STAGE S1149>

# <POTBO_STAGE S1152>


_v44_player_death_reset_original = oyuncu_olum_sahnesini_sifirla


def oyuncu_olum_sahnesini_sifirla():
    global v44_player_death_arterial_done
    v44_player_death_arterial_done = False
    v44_arterial_emitters.clear()
    return _v44_player_death_reset_original()
# </POTBO_STAGE S1152>

# <POTBO_STAGE S1154>



_v44_player_reach_original = _v38_player_reach_values


def _v38_player_reach_values():
    nr, nw, hr, hw = _v44_player_reach_original()
    return (
        int(nr + V44_SWORD_REACH_BONUS_PX),
        int(nw + V44_SWORD_WIDTH_BONUS_PX),
        int(hr + V44_SWORD_REACH_BONUS_PX),
        int(hw + V44_SWORD_WIDTH_BONUS_PX),
    )
# </POTBO_STAGE S1154>

# <POTBO_STAGE S1156>


def _v44_is_player_melee_source(source):
    if bool(getattr(source, "is_player_magic", False)):
        return False
    if source is None:
        return True
    if source == "player":
        return True
    return False


def _v44_source_position(source):
    if _v44_is_player_melee_source(source):
        return pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    return pygame.Vector2(
        float(getattr(source, "x", oyuncu_x)),
        float(getattr(source, "y", oyuncu_y)),
    )
# </POTBO_STAGE S1156>

# <POTBO_STAGE S1175>


def v45_contact_distance(enemy):
    return pygame.Vector2(float(enemy.x), float(enemy.y)).distance_to(
        (oyuncu_x, oyuncu_y)
    )
# </POTBO_STAGE S1175>

# <POTBO_STAGE S1185>
v46_character_last_gender = karakter_cinsiyet
# </POTBO_STAGE S1185>

# <POTBO_STAGE S1187>


def v46_character_selection_energy(cinsiyet, onay_animasyonu):
    now = pygame.time.get_ticks()
    target = 1.0 if cinsiyet == karakter_cinsiyet else 0.0
    current = float(v46_character_card_energy.get(cinsiyet, 0.0))
    dt = min(
        0.05,
        max(
            1.0 / 240.0,
            saat.get_time() / 1000.0 if saat.get_time() else 1.0 / FPS,
        ),
    )

    speed = 1.0 - math.exp(-7.4 * dt)
    current += (target - current) * speed
    if onay_animasyonu:
        elapsed = now - int(karakter_onay_gecisi_baslangic)
        current += v46_envelope_value(elapsed) * 0.22
    current = v44_clamp(current, 0.0, 1.18)
    v46_character_card_energy[cinsiyet] = current
    return current
# </POTBO_STAGE S1187>

# <POTBO_STAGE S1206>
v48_character_switch_from = karakter_cinsiyet
v48_character_switch_to = karakter_cinsiyet
v48_character_last_seen = karakter_cinsiyet
# </POTBO_STAGE S1206>

# <POTBO_STAGE S1208>


def v48_character_motion_update():
    global v48_character_switch_progress, v48_character_switch_from
    global \
        v48_character_switch_to, \
        v48_character_last_seen, \
        v48_character_switch_started_ms
    now = pygame.time.get_ticks()
    if karakter_cinsiyet != v48_character_last_seen:
        v48_character_switch_from = v48_character_last_seen
        v48_character_switch_to = karakter_cinsiyet
        v48_character_last_seen = karakter_cinsiyet
        v48_character_switch_started_ms = now
        v48_character_switch_progress = 0.0
    elapsed = now - int(v48_character_switch_started_ms)
    v48_character_switch_progress = v44_clamp01(elapsed / 360.0)
    return v44_smootherstep(v48_character_switch_progress)
# </POTBO_STAGE S1208>

# <POTBO_STAGE S1214>


def v49_repair_nonfinite_actor(actor):
    global v49_runtime_repairs
    if actor is None:
        return False
    changed = False
    if hasattr(actor, "x") and not v49_numeric_finite(actor.x):
        actor.x = float(oyuncu_x) + random.uniform(-80.0, 80.0)
        changed = True
    if hasattr(actor, "y") and not v49_numeric_finite(actor.y):
        actor.y = float(oyuncu_y) + random.uniform(-80.0, 80.0)
        changed = True
    if changed:
        v49_runtime_repairs += 1
    return changed
# </POTBO_STAGE S1214>

# <POTBO_STAGE S1265>


def v53_tissue_profile(entity_type):
    key = str(entity_type or "default")
    if key == "player":
        key = "player_female" if karakter_cinsiyet == "female" else "player_male"
    return dict(V53_TISSUE_PROFILES.get(key, V53_TISSUE_PROFILES["default"]))
# </POTBO_STAGE S1265>

# <POTBO_STAGE S1288>
V55_SMEAR_PLAYER_INTERVAL_MS = 150
# </POTBO_STAGE S1288>

# <POTBO_STAGE S1291>

v55_player_last_pos = pygame.Vector2(oyuncu_x, oyuncu_y)
v55_player_last_smear_ms = 0
v55_player_transfer = 0.0
# </POTBO_STAGE S1291>

# <POTBO_STAGE S1303>
v56_last_player_pos = pygame.Vector2(oyuncu_x, oyuncu_y)
v56_player_velocity = pygame.Vector2(0.0, 0.0)
# </POTBO_STAGE S1303>

# <POTBO_STAGE S1306>


def v56_player_motion_tick(now=None):
    global v56_last_player_pos, v56_player_velocity, v56_last_tick_ms
    if now is None:
        now = pygame.time.get_ticks()
    dt = max(
        1e-4,
        min(0.05, (int(now) - int(v56_last_tick_ms)) / 1000.0),
    )
    current = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    raw = (current - v56_last_player_pos) / dt
    blend = 1.0 - math.exp(-12.0 * dt)
    v56_player_velocity += (raw - v56_player_velocity) * blend
    v56_last_player_pos = current
    v56_last_tick_ms = int(now)
    return pygame.Vector2(v56_player_velocity)
# </POTBO_STAGE S1306>

# <POTBO_STAGE S1308>


def v56_actor_to_player(actor, predicted=False):
    player = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    if predicted:
        cfg = v56_cfg(actor)
        player += pygame.Vector2(v56_player_velocity) * (
            float(cfg["prediction_ms"]) / 1000.0
        )
    return player - pygame.Vector2(float(actor.x), float(actor.y))
# </POTBO_STAGE S1308>

# <POTBO_STAGE S1310>


def v56_distance(actor):
    return pygame.Vector2(float(actor.x), float(actor.y)).distance_to(
        (oyuncu_x, oyuncu_y)
    )
# </POTBO_STAGE S1310>

# <POTBO_STAGE S1313>


def v56_lane_target(actor, base_target, now=None, predicted_player=None):
    if now is None:
        now = pygame.time.get_ticks()
    state = v56_state(actor)
    cfg = v56_cfg(actor)
    if predicted_player is None:
        predicted_player = pygame.Vector2(
            float(oyuncu_x), float(oyuncu_y)
        ) + v56_player_velocity * (float(cfg["prediction_ms"]) / 1000.0)
    player = pygame.Vector2(predicted_player)
    actor_pos = pygame.Vector2(float(actor.x), float(actor.y))
    radial = actor_pos - player
    if radial.length_squared() <= 1e-6:
        radial = pygame.Vector2(1.0, 0.0)
    radial = radial.normalize()
    tangent = radial.rotate(90.0)

    if int(now) >= int(state.get("lane_hold_until", 0)):

        side_to_player = tangent.dot(v56_player_velocity)
        if abs(side_to_player) > 12.0:
            state["lane_sign"] = -1.0 if side_to_player > 0.0 else 1.0
        elif random.random() < 0.20:
            state["lane_sign"] *= -1.0
        state["lane_hold_until"] = int(now) + random.randint(320, 620)

    ideal = float(cfg["ideal_range"])
    side = float(cfg["side_step"]) * float(state.get("lane_sign", 1.0))
    candidate = player + radial * ideal + tangent * side
    if common_enemy_statik_konum_gecerli_mi(
        str(getattr(actor, "tur", "crawler")),
        candidate.x,
        candidate.y,
        navigation=True,
    ):
        return candidate
    return pygame.Vector2(base_target)
# </POTBO_STAGE S1313>

# <POTBO_STAGE S1329>


def v57_hp_ratio():
    return v57_clamp01(float(oyuncu_hp) / max(1.0, float(oyuncu_max_hp)))
# </POTBO_STAGE S1329>

# <POTBO_STAGE S1340>


def oyuncu_olum_sahnesini_sifirla():
    v57_reset()
    return _v57_death_reset_original()
# </POTBO_STAGE S1340>

# <POTBO_STAGE S1359>


_v58_death_reset_original = oyuncu_olum_sahnesini_sifirla


def oyuncu_olum_sahnesini_sifirla():
    v58_reset()
    return _v58_death_reset_original()
# </POTBO_STAGE S1359>

# <POTBO_STAGE S1370>


def v59_cross_quality(enemy):
    facing = v44_player_facing_vector()
    delta = pygame.Vector2(
        float(getattr(enemy, "x", oyuncu_x)) - float(oyuncu_x),
        float(getattr(enemy, "y", oyuncu_y)) - float(oyuncu_y),
    )
    if delta.length_squared() <= 1e-8:
        return 0.0
    facing = facing.normalize()
    delta = delta.normalize()
    cross = abs(facing.x * delta.y - facing.y * delta.x)

    return max(0.0, 1.0 - abs(cross - 0.38) / 0.38)
# </POTBO_STAGE S1370>

# <POTBO_STAGE S1381>


_v59_death_reset_original = oyuncu_olum_sahnesini_sifirla


def oyuncu_olum_sahnesini_sifirla():
    v59_reset()
    return _v59_death_reset_original()
# </POTBO_STAGE S1381>

# <POTBO_STAGE S1416>


_v64_player_panel_original = oyuncu_paneli_ciz
# </POTBO_STAGE S1416>

# <POTBO_STAGE S1419>


def v65_pulse_pressure(emitter, now):
    age = max(0, int(now) - int(emitter.started_ms))
    t = age / max(1.0, float(V44_PLAYER_DEATH_ARTERIAL_DURATION_MS))
    curve = v65_curve_sample(t)

    index_factor = max(0.18, 1.0 - int(emitter.pulse_index) * 0.105)
    return max(V65_MIN_PRESSURE, min(1.0, curve * index_factor))


def v65_pulse_direction(emitter, pressure):
    age = max(0, pygame.time.get_ticks() - int(emitter.started_ms))
    t = v44_clamp01(age / max(1.0, float(V44_PLAYER_DEATH_ARTERIAL_DURATION_MS)))
    gravity_tilt = V65_GRAVITY_TILT_DEG * v44_smoothstep(t)
    pulse_wobble = (
        math.sin((int(emitter.pulse_index) + 1) * 1.73 + emitter.seed * 0.00001) * 4.2
    )
    return emitter.direction.rotate(
        float(emitter.side_bias)
        + pulse_wobble
        + gravity_tilt * (1.0 if emitter.direction.x >= 0 else -1.0)
    )
# </POTBO_STAGE S1419>

# <POTBO_STAGE S1421>


def _v65_arterial_update(self, now):
    if not self.active:
        return
    age = int(now) - int(self.started_ms)
    if age > V44_PLAYER_DEATH_ARTERIAL_DURATION_MS or self.pulse_index >= len(
        V44_PLAYER_DEATH_ARTERIAL_PULSES
    ):
        self.active = False
        return

    emitted_this_frame = 0
    while (
        self.active and int(now) >= int(self.next_pulse_ms) and emitted_this_frame < 2
    ):
        pressure = v65_pulse_pressure(self, now)
        direction = v65_pulse_direction(self, pressure)
        v65_emit_jet(self, now, pressure, direction, secondary=False)
        if pressure > 0.28 and random.random() < V65_SECONDARY_CHANCE * pressure:
            v65_emit_jet(
                self,
                now,
                pressure * 0.72,
                direction,
                secondary=True,
            )
        self.pulse_index += 1
        v65_stats["pulses"] += 1
        emitted_this_frame += 1
        if self.pulse_index >= len(V44_PLAYER_DEATH_ARTERIAL_PULSES):
            self.active = False
            break
        interval_idx = min(self.pulse_index - 1, len(V65_HEARTBEAT_MS) - 1)
        interval = int(V65_HEARTBEAT_MS[interval_idx])
        interval += random.randint(-9, 13)
        self.next_pulse_ms += max(64, interval)
# </POTBO_STAGE S1421>

# <POTBO_STAGE S1428>


def v67_clear_trajectory():
    global \
        v67_last_measured_speed, \
        v67_last_tangent, \
        v67_last_curvature, \
        v67_last_arc_length
    v67_tip_history.clear()
    v67_last_measured_speed = 0.0
    v67_last_tangent = v44_player_facing_vector()
    v67_last_curvature = 0.0
    v67_last_arc_length = 0.0
# </POTBO_STAGE S1428>

# <POTBO_STAGE S1431>


def v67_measured_direction():
    if v67_last_tangent.length_squared() <= 1e-7:
        return v44_player_facing_vector()
    return v67_last_tangent.normalize()
# </POTBO_STAGE S1431>

# <POTBO_STAGE S1434>


def v67_reach_contract():
    nr, nw, hr, hw = _v38_player_reach_values()
    return {
        "normal_reach_px": int(nr),
        "normal_width_px": int(nw),
        "heavy_reach_px": int(hr),
        "heavy_width_px": int(hw),
        "added_px": float(V44_SWORD_REACH_BONUS_PX),
        "visual_cm_proxy": round(
            float(V44_SWORD_REACH_BONUS_PX) / max(0.001, V67_REACH_REFERENCE_PX),
            2,
        ),
    }
# </POTBO_STAGE S1434>

# <POTBO_STAGE S1448>


def v69_reach_assertions():
    nr, nw, hr, hw = _v38_player_reach_values()
    checks = {
        "normal_positive": nr > 0 and nw > 0,
        "heavy_positive": hr > 0 and hw > 0,
        "heavy_not_shorter": hr >= nr,
        "one_cm_proxy_applied": int(V44_SWORD_REACH_BONUS_PX) == 6,
        "narrow_width_preserved": nw <= max(24, nr // 2),
    }
    return checks
# </POTBO_STAGE S1448>

# <POTBO_STAGE S1468>

v73_player_blast_fragmented = False
# </POTBO_STAGE S1468>

# <POTBO_STAGE S1479>


_v73_death_reset_original = oyuncu_olum_sahnesini_sifirla


def oyuncu_olum_sahnesini_sifirla():
    global v73_player_blast_fragmented
    v73_player_blast_fragmented = False
    return _v73_death_reset_original()
# </POTBO_STAGE S1479>

# <POTBO_STAGE S1495>


_v74_death_reset_original = oyuncu_olum_sahnesini_sifirla
# </POTBO_STAGE S1495>

# <POTBO_STAGE S1526>


def _v76_death_victim_draw():
    if oyuncu_olum_turu == "blast_core":
        _v26_oyuncu_patlama_siluet_parcalari_ciz()
    elif oyuncu_olum_turu == "blast_inner":
        _v30_patlama_birinci_katman_siluet_ciz()
    else:

        _oyuncu_yatay_siluet_ciz()
# </POTBO_STAGE S1526>

# <POTBO_STAGE S1531>


def oyun_ekrani_ciz():
    if oyuncu_hp <= 0:
        oyuncu_olum_sahnesi_ciz()
        return
    return _v76_game_draw_original()
# </POTBO_STAGE S1531>

# <POTBO_STAGE S1533>


def parlaklik_kaplamasi_ciz():
    if oyun_durumu == OYUN and oyuncu_hp <= 0:
        return
    return _v76_brightness_original()
# </POTBO_STAGE S1533>

# <POTBO_STAGE S1545>


def _v77_death_victim_layer():
    if oyuncu_olum_turu == "blast_core":
        _v26_oyuncu_patlama_siluet_parcalari_ciz()
    elif oyuncu_olum_turu == "blast_inner":
        _v30_patlama_birinci_katman_siluet_ciz()
    else:
        _oyuncu_yatay_siluet_ciz()


def _v77_death_fire_layer():
    if oyuncu_olum_turu == "fire":
        _v25_oyuncu_olum_ates_ciz()


def _v77_death_fallback_victim():
    """Semantic layer beklenmedik biçimde reddedilirse en azından cesedi güvenle korur."""
    sil = _v30_oyuncu_base_siluet()
    if sil is None:
        return
    mask = pygame.mask.from_surface(sil, 1)
    if mask.count() <= 0:
        return
    flat = mask.to_surface(
        setcolor=(*V77_DEATH_BODY, 255),
        unsetcolor=(0, 0, 0, 0),
    ).convert_alpha()
    _v30_yatan_siluet_yerlestir(flat)
# </POTBO_STAGE S1545>

# <POTBO_STAGE S1568>


_v78_death_state_original = oyuncu_olum_durumu_guncelle


def oyuncu_olum_durumu_guncelle():
    once = int(oyuncu_olum_baslangic_ms)
    _v78_death_state_original()
    if oyuncu_hp <= 0 and oyuncu_olum_baslangic_ms > 0:
        if once <= 0 or not v78_death_snapshot["blood"]:
            _v78_capture_death_snapshot()
# </POTBO_STAGE S1568>

# <POTBO_STAGE S1570>


def _v78_death_snapshot_age():
    if oyuncu_olum_baslangic_ms <= 0:
        return 0.0
    start = int(v78_death_snapshot.get("start_ms") or oyuncu_olum_baslangic_ms)
    return max(0.0, (pygame.time.get_ticks() - start) / 1000.0)
# </POTBO_STAGE S1570>

# <POTBO_STAGE S1581>






OYUNCU_YURUYUS_HIZI = 258.0
OYUNCU_HIZLANMA = 1480.0
OYUNCU_YAVASLAMA = 1810.0
OYUNCU_DONUS_IVMESI = 2260.0
# </POTBO_STAGE S1581>

# <POTBO_STAGE S1592>


def oyuncu_olum_baslik_fade_orani(simdi=None):
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if oyuncu_olum_baslangic_ms <= 0:
        return 0.0
    elapsed = int(simdi) - int(oyuncu_olum_baslangic_ms) - V79_DEATH_TITLE_DELAY_MS
    if elapsed <= 0:
        return 0.0
    return _v79_smootherstep(elapsed / max(1.0, float(V79_DEATH_TITLE_FADE_MS)))
# </POTBO_STAGE S1592>

# <POTBO_STAGE S1595>


_v79_scene_reset_original = oyuncu_olum_sahnesini_sifirla
# </POTBO_STAGE S1595>

# <POTBO_STAGE S1598>


def _v79_draw_death_title(now):
    p = oyuncu_olum_baslik_fade_orani(now)
    if p <= 0.0:
        return
    title = _v79_title_surface(t("game_over_title"))
    rect = title.get_rect(center=(GENISLIK // 2, 146))
    _v79_dither_blit(title, rect.topleft, p)
# </POTBO_STAGE S1598>

# <POTBO_STAGE S1616>


_v80_death_update_original = oyuncu_olum_durumu_guncelle


def oyuncu_olum_durumu_guncelle():
    had_started = int(oyuncu_olum_baslangic_ms)
    _v80_death_update_original()
    if oyuncu_hp <= 0 and oyuncu_olum_baslangic_ms > 0:
        if had_started <= 0 or int(v80_death_fx.get("start_ms", 0)) <= 0:
            _v80_make_death_fx()


_v80_death_reset_original = oyuncu_olum_sahnesini_sifirla
# </POTBO_STAGE S1616>

# <POTBO_STAGE S1621>


def _v81_wound_origin(lateral=0.0, forward=0.0):
    f, side = _v81_body_basis()
    return (
        pygame.Vector2(float(oyuncu_x), float(oyuncu_y - 10.0))
        + side * float(lateral)
        + f * float(forward)
    )
# </POTBO_STAGE S1621>

# <POTBO_STAGE S1632>


_v81_death_reset_original = oyuncu_olum_sahnesini_sifirla


def oyuncu_olum_sahnesini_sifirla():
    global v81_death_blood
    v81_death_blood = {
        "start_ms": 0,
        "seed": 0,
        "drops": [],
        "seeps": [],
        "burst_serial": 0,
    }
    _v81_death_reset_original()
# </POTBO_STAGE S1632>

# <POTBO_STAGE S1702>


def _v80_make_death_fx():
    global v80_death_fx
    _v83_death_fx_original()
    if not isinstance(v80_death_fx, dict):
        return
    if str(v80_death_fx.get("death_type", "")) != "blood":
        return
    f, side = _v80_player_basis()
    center = pygame.Vector2(float(oyuncu_x), float(oyuncu_y) - 12.0)
    extra_emitters = [
        {
            "origin": center + side * -5.0,
            "dir": f.rotate(-12.0),
            "spread": 18.0,
            "speed": 28.0,
            "life": 1480,
            "branches": 6,
            "delay": 90,
        },
        {
            "origin": center + side * 3.0,
            "dir": f.rotate(14.0),
            "spread": 16.0,
            "speed": 24.0,
            "life": 1720,
            "branches": 5,
            "delay": 260,
        },
        {
            "origin": center + side * -2.0,
            "dir": f.rotate(30.0),
            "spread": 12.0,
            "speed": 19.0,
            "life": 1980,
            "branches": 4,
            "delay": 520,
        },
    ]
    v80_death_fx.setdefault("emitters", []).extend(extra_emitters)
# </POTBO_STAGE S1702>

# <POTBO_STAGE S1729>


def v84_actor_distance(actor, point=None):
    if actor is None:
        return float("inf")
    if point is None:
        point = (oyuncu_x, oyuncu_y)
    return pygame.Vector2(
        float(getattr(actor, "x", 0.0)),
        float(getattr(actor, "y", 0.0)),
    ).distance_to(point)
# </POTBO_STAGE S1729>

# <POTBO_STAGE S1759>


def v84_face_actor(actor):
    global oyuncu_yonu
    if actor is None:
        return
    delta = pygame.Vector2(
        float(getattr(actor, "x", oyuncu_x)) - float(oyuncu_x),
        float(getattr(actor, "y", oyuncu_y)) - float(oyuncu_y),
    )
    oyuncu_yonu = v84_direction_name(delta)
# </POTBO_STAGE S1759>

# <POTBO_STAGE S1778>


_v84_control_lock_original = oyuncu_kontrol_kilitli_mi
# </POTBO_STAGE S1778>

# <POTBO_STAGE S1780>


_v84_free_move_original = oyuncu_serbest_hareket_guncelle
# </POTBO_STAGE S1780>

# <POTBO_STAGE S1797>


_v84_death_reset_original = oyuncu_olum_sahnesini_sifirla
# </POTBO_STAGE S1797>

# <POTBO_STAGE S1803>


_v84_death_state_reset_original = oyuncu_olum_sahnesini_sifirla


def oyuncu_olum_sahnesini_sifirla():
    v84_death_state.reset()
    return _v84_death_state_reset_original()


_v84_death_tick_original = oyuncu_olum_durumu_guncelle


def oyuncu_olum_durumu_guncelle():
    result = _v84_death_tick_original()
    state = v84_death_state
    if state.built and state.fracture is not None and oyuncu_hp <= 0:
        now = pygame.time.get_ticks()
        dt = max(
            0.0,
            min(
                0.05,
                (int(now) - int(state.last_tick_ms)) / 1000.0,
            ),
        )
        state.last_tick_ms = int(now)
        state.fracture.update(dt)
    return result
# </POTBO_STAGE S1803>

# <POTBO_STAGE S1841>
V44_PLAYER_DEATH_ARTERIAL_PULSES = (
    1.00,
    0.98,
    0.95,
    0.91,
    0.87,
    0.82,
    0.77,
    0.72,
    0.66,
    0.60,
    0.54,
    0.48,
    0.42,
    0.36,
    0.30,
    0.25,
    0.20,
    0.16,
    0.12,
)
# </POTBO_STAGE S1841>

# <POTBO_STAGE S1843>
V44_PLAYER_DEATH_ARTERIAL_MIN_PARTICLES = 16
V44_PLAYER_DEATH_ARTERIAL_MAX_PARTICLES = 28
# </POTBO_STAGE S1843>

# <POTBO_STAGE S1855>


_v85_arterial_start_original = v44_player_death_arterial_start


def v44_player_death_arterial_start(source_x, source_y, profile="heavy_slash"):
    ok = _v85_arterial_start_original(source_x, source_y, profile)
    if not ok or not v44_arterial_emitters:
        return ok
    state = v84_death_state
    zone = (
        state.artery_zone
        if getattr(state, "built", False)
        else v85_mortal_wound_state.artery_zone
    )
    emitter = v44_arterial_emitters[-1]
    if zone == "neck":
        emitter.x = float(oyuncu_x)
        emitter.y = float(oyuncu_y) - 25.0
    elif zone == "shoulder":
        sign = -1.0 if oyuncu_yonu in ("left", "up") else 1.0
        emitter.x = float(oyuncu_x) + sign * 7.0
        emitter.y = float(oyuncu_y) - 17.0
    else:
        emitter.x = float(oyuncu_x)
        emitter.y = float(oyuncu_y) - 12.0
    return ok
# </POTBO_STAGE S1855>

# <POTBO_STAGE S1863>


_v85_death_tick_original = oyuncu_olum_durumu_guncelle


def oyuncu_olum_durumu_guncelle():
    result = _v85_death_tick_original()
    state = v84_death_state
    if state.built and oyuncu_hp <= 0:
        now = pygame.time.get_ticks()
        scene_start = int(oyuncu_olum_baslangic_ms or state.created_ms)
        age = max(0, int(now) - scene_start)
        if age >= V85_DEATH_RELEASE_MS:
            v85_death_release(state)
    return result
# </POTBO_STAGE S1863>

# <POTBO_STAGE S1865>


def v85_death_artery_origin(state):
    if state.artery_zone == "neck":
        return pygame.Vector2(float(oyuncu_x), float(oyuncu_y) - 25.0)
    if state.artery_zone == "shoulder":
        sign = -1.0 if oyuncu_yonu in ("left", "up") else 1.0
        return pygame.Vector2(float(oyuncu_x) + sign * 7.0, float(oyuncu_y) - 17.0)
    return pygame.Vector2(float(oyuncu_x), float(oyuncu_y) - 12.0)
# </POTBO_STAGE S1865>

# <POTBO_STAGE S1867>


def v85_death_intact_body_draw(anchor, rotation):
    silhouette = _v30_oyuncu_base_siluet()
    if silhouette is None:
        _v77_death_fallback_victim()
        return
    image = pygame.transform.rotate(silhouette, float(rotation))
    rect = image.get_rect(
        center=(
            int(anchor[0]),
            int(anchor[1] - image.get_height() * 0.16),
        )
    )
    ekran.blit(image, rect)


def v85_death_victim_draw(now):
    state = v84_death_state
    if not state.built or state.variant == "fire":
        _v77_death_victim_layer()
        return
    scene_start = int(oyuncu_olum_baslangic_ms or state.created_ms)
    age = max(0, int(now) - scene_start)
    fall = v84_smootherstep(age / float(V85_DEATH_COLLAPSE_MS))
    rotation = state.rotation_sign * 90.0 * fall
    anchor = pygame.Vector2(v85_death_body_anchor())
    anchor.y += 5.0 * fall
    if state.fracture is None:
        v85_death_intact_body_draw(anchor, rotation)
    else:
        state.fracture.draw(anchor, base_rotation=rotation)
# </POTBO_STAGE S1867>

# <POTBO_STAGE S1870>


_v85_control_lock_original = oyuncu_kontrol_kilitli_mi


def oyuncu_kontrol_kilitli_mi(simdi=None):
    if v85_mortal_wound_state.active:
        return True
    return _v85_control_lock_original(simdi)


_v85_free_move_original = oyuncu_serbest_hareket_guncelle


def oyuncu_serbest_hareket_guncelle():
    if v85_mortal_wound_state.active:
        return
    return _v85_free_move_original()
# </POTBO_STAGE S1870>

# <POTBO_STAGE S1872>


_v85_death_reset_original = oyuncu_olum_sahnesini_sifirla


def oyuncu_olum_sahnesini_sifirla():
    v85_mortal_wound_state.reset()
    v84_death_state.reset()
    return _v85_death_reset_original()
# </POTBO_STAGE S1872>

# <POTBO_STAGE S1908>

v86_player_hit_history = {}
# </POTBO_STAGE S1908>

# <POTBO_STAGE S1915>


def v86_face_killer_to_player(killer):
    if killer is None:
        return
    delta = pygame.Vector2(
        float(oyuncu_x) - float(killer.x),
        float(oyuncu_y) - float(killer.y),
    )
    direction = v84_direction_name(delta)
    killer.direction = direction
    if hasattr(killer, "visual_direction") and abs(delta.x) > 0.5:
        killer.visual_direction = "right" if delta.x >= 0.0 else "left"
# </POTBO_STAGE S1915>

# <POTBO_STAGE S1919>


def v86_initialize_body(state):
    surface = _v30_oyuncu_base_siluet()
    if surface is None:
        surface = pygame.Surface((38, 66), pygame.SRCALPHA)
        pygame.draw.polygon(
            surface,
            (*V84_BODY, 255),
            ((19, 1), (34, 19), (31, 65), (7, 65), (4, 19)),
        )
    state.base_size = tuple(surface.get_size())
    state.remaining_mask = pygame.mask.from_surface(surface, 1)
    state.original_pixels = int(state.remaining_mask.count())
    v86_root_refresh(state)
# </POTBO_STAGE S1919>

# <POTBO_STAGE S1936>


_v86_death_tick_original = oyuncu_olum_durumu_guncelle
# </POTBO_STAGE S1936>

# <POTBO_STAGE S1938>


_v86_death_draw_original = oyuncu_olum_sahnesi_ciz
# </POTBO_STAGE S1938>

# <POTBO_STAGE S1940>


_v86_death_reset_original = oyuncu_olum_sahnesini_sifirla


def oyuncu_olum_sahnesini_sifirla():
    global v86_guard_intent_until_ms
    v86_death_state.reset()
    v86_player_hit_history.clear()
    v86_guard_intent_until_ms = -10000
    return _v86_death_reset_original()
# </POTBO_STAGE S1940>

# <POTBO_STAGE S1977>


_v87_death_reset_original = oyuncu_olum_sahnesini_sifirla
# </POTBO_STAGE S1977>

# <POTBO_STAGE S2015>


_v88_heavy_player_hit_original = oyuncu_agir_darbe_uygula
# </POTBO_STAGE S2015>

# <POTBO_STAGE S2049>


_v88_death_reset_original = oyuncu_olum_sahnesini_sifirla
# </POTBO_STAGE S2049>

# <POTBO_STAGE S2069>
v89_player_foot_last_pos = None
v89_player_foot_distance = 0.0
v89_player_foot_side = 0
v89_player_sole_load = 0.0
# </POTBO_STAGE S2069>

# <POTBO_STAGE S2147>


def v90_hp_ratio():
    return v90_clamp(float(oyuncu_hp) / max(1.0, float(oyuncu_max_hp)))
# </POTBO_STAGE S2147>

# <POTBO_STAGE S2155>


_v90_free_move_raw = oyuncu_serbest_hareket_guncelle
# </POTBO_STAGE S2155>

# <POTBO_STAGE S2187>


_v90_control_lock_raw = oyuncu_kontrol_kilitli_mi


def oyuncu_kontrol_kilitli_mi(simdi=None):
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if (
        v90_draco_state.active
        and v90_draco_state.phase == "cast"
        and int(simdi) - int(v90_draco_state.phase_started_ms) < V90_DRACO_CAST_MS
    ):
        return True
    return _v90_control_lock_raw(simdi)
# </POTBO_STAGE S2187>

# <POTBO_STAGE S2192>


_v90_player_panel_raw = oyuncu_paneli_ciz
# </POTBO_STAGE S2192>

# <POTBO_STAGE S2215>


_v91_player_panel_raw = oyuncu_paneli_ciz
# </POTBO_STAGE S2215>

# <POTBO_STAGE S2246>


v91_player_sole_color = (112, 0, 16)
v91_player_sole_freshness = 0.0
# </POTBO_STAGE S2246>

# <POTBO_STAGE S2250>


_v91_death_draw_fallback = oyuncu_olum_sahnesi_ciz
# </POTBO_STAGE S2250>

# <POTBO_STAGE S2252>


_v91_death_reset_raw = oyuncu_olum_sahnesini_sifirla


def oyuncu_olum_sahnesini_sifirla():
    v91_death_layer_cache.clear()
    v91_death_flame_cache.clear()
    return _v91_death_reset_raw()
# </POTBO_STAGE S2252>

# <POTBO_STAGE S2268>


_v92_level_gain_raw = oyuncu_seviye_kazanclarini_uygula
# </POTBO_STAGE S2268>

# <POTBO_STAGE S2270>



_v92_free_move_raw = oyuncu_serbest_hareket_guncelle
# </POTBO_STAGE S2270>

# <POTBO_STAGE S2322>


def v92_chain_targets(direction):
    direction = pygame.Vector2(direction)
    if direction.length_squared() <= 1e-8:
        direction = pygame.Vector2(1.0, 0.0)
    direction = direction.normalize()
    side = direction.rotate(90.0)
    origin = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    candidates = []
    for actor in v90_hostiles():
        delta = v90_actor_center(actor) - origin
        forward = delta.dot(direction)
        lateral = abs(delta.dot(side))
        if forward < 24.0 or forward > V92_CHAIN_MAX_FORWARD or lateral > V92_CHAIN_MAX_LATERAL:
            continue
        candidates.append((forward, lateral, actor))
    candidates.sort(key=lambda row: (row[0], row[1]))
    selected = []
    last_point = origin
    for _forward, _lateral, actor in candidates:
        point = v90_actor_center(actor)
        if not selected or point.distance_to(last_point) <= V92_CHAIN_LINK_RANGE:
            selected.append(actor)
            last_point = point
    return selected
# </POTBO_STAGE S2322>

# <POTBO_STAGE S2328>


_v92_control_lock_raw = oyuncu_kontrol_kilitli_mi


def oyuncu_kontrol_kilitli_mi(simdi=None):
    if v92_chain_state.active:
        return True
    return _v92_control_lock_raw(simdi)
# </POTBO_STAGE S2328>

# <POTBO_STAGE S2367>






_v94_death_scene_previous = oyuncu_olum_sahnesi_ciz
# </POTBO_STAGE S2367>

# <POTBO_STAGE S2442>


_v99_free_move_raw = oyuncu_serbest_hareket_guncelle
# </POTBO_STAGE S2442>

# <POTBO_STAGE S2480>















V102_VERSION = "102.0"
# </POTBO_STAGE S2480>

# <POTBO_STAGE S2518>


def v106_player_condition_label():
    condition = v106_player_condition()
    return {
        "healthy": bt("SAĞLIKLI", "HEALTHY"),
        "wounded": bt("YARALI", "WOUNDED"),
        "critical": bt("KRİTİK", "CRITICAL"),
    }[condition]
# </POTBO_STAGE S2518>

# <POTBO_STAGE S2526>


def v106_double_power_cost():
    lv = max(1, int(oyuncu_level))
    x = lv - 1
    return max(240, int(round(240 + 58 * x + 4.6 * x * x)))
# </POTBO_STAGE S2526>

# <POTBO_STAGE S2543>


def v106_corona_orb_position(core_id, now):
    base = v106_corona_phase_angle(now)
    angle = base + int(core_id) * (math.tau / 3.0) - math.pi * 0.5
    radius = V106_CORONA_ORBIT_RADIUS
    return pygame.Vector2(
        float(oyuncu_x) + math.cos(angle) * radius,
        float(oyuncu_y) + math.sin(angle) * radius * 0.62,
    )
# </POTBO_STAGE S2543>

# <POTBO_STAGE S2568>


def v106_corona_orb_position(core_id, now):
    age = max(0.0, (int(now) - int(v106_corona.started_ms)) / 1000.0)
    base = v106_corona_phase_angle(now)
    cid = int(core_id)
    angle = base + cid * (math.tau / 3.0) - math.pi * 0.5
    violence = min(1.0, age / 0.55)
    radius = V106_CORONA_ORBIT_RADIUS + math.sin(age * 29.0 + cid * 2.1) * 2.4 * violence
    vertical = 0.62 + math.sin(age * 17.0 + cid) * 0.018 * violence
    return pygame.Vector2(
        float(oyuncu_x) + math.cos(angle) * radius,
        float(oyuncu_y) + math.sin(angle) * radius * vertical,
    )
# </POTBO_STAGE S2568>

# <POTBO_STAGE S2591>
_v109_player_flash_raw = oyuncu_parlama_baslat
# </POTBO_STAGE S2591>

