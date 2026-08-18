# Path of the Bloodied One — categorized source stages
#
# This file is intentionally executed by core/bootstrap.py in original source order.
# Keeping one shared runtime namespace avoids gameplay regressions while the former
# 90k-line monolith is physically separated by responsibility. Do not import this
# file directly; edit the stage code normally and launch root main.py.

# <POTBO_STAGE S0013>
hasar_sayilari = True
# </POTBO_STAGE S0013>

# <POTBO_STAGE S0024>

ERKEK_YON_DOSYALARI = {
    "idle_down": os.path.join(ERKEK_YON_KLASORU, "male_idle_down.png"),
    "idle_left": os.path.join(ERKEK_YON_KLASORU, "male_idle_left.png"),
    "idle_right": os.path.join(ERKEK_YON_KLASORU, "male_idle_right.png"),
    "idle_up": os.path.join(ERKEK_YON_KLASORU, "male_idle_up.png"),
    "walk_down_01": os.path.join(ERKEK_YON_KLASORU, "male_walk_down_01.png"),
    "walk_down_02": os.path.join(ERKEK_YON_KLASORU, "male_walk_down_02.png"),
    "walk_left_01": os.path.join(ERKEK_YON_KLASORU, "male_walk_left_01.png"),
    "walk_left_02": os.path.join(ERKEK_YON_KLASORU, "male_walk_left_02.png"),
    "walk_right_01": os.path.join(ERKEK_YON_KLASORU, "male_walk_right_01.png"),
    "walk_right_02": os.path.join(ERKEK_YON_KLASORU, "male_walk_right_02.png"),
    "walk_up_01": os.path.join(ERKEK_YON_KLASORU, "male_walk_up_01.png"),
    "walk_up_02": os.path.join(ERKEK_YON_KLASORU, "male_walk_up_02.png"),
    # Aşağı saldırı
    "attack_down_01": os.path.join(ERKEK_YON_KLASORU, "male_attack_down_01.png"),
    "attack_down_02": os.path.join(ERKEK_YON_KLASORU, "male_attack_down_02.png"),
    # Sol saldırı
    "attack_left_01": os.path.join(ERKEK_YON_KLASORU, "male_attack_left_01.png"),
    # Sağ saldırı
    "attack_right_01": os.path.join(ERKEK_YON_KLASORU, "male_attack_right_01.png"),
    # Yukarı saldırı
    "attack_up_01": os.path.join(ERKEK_YON_KLASORU, "male_attack_up_01.png"),
    "attack_up_02": os.path.join(ERKEK_YON_KLASORU, "male_attack_up_02.png"),
}
# </POTBO_STAGE S0024>

# <POTBO_STAGE S0078>


# =========================================================
# İPUÇLARI
# =========================================================
IPUCLARI = {
    "TR": [
        (
            "Kritik vuruşlar yalnızca daha fazla hasar vermez. "
            "Bazı ağır zırhlı düşmanların savunmasını kısa süreliğine kırarak "
            "bir sonraki saldırının çok daha etkili olmasını sağlar."
        ),
        (
            "Mağaralarda yalnızca ana yolu takip etme. "
            "Karanlık duvarların, kırık sütunların ve kullanılmayan geçitlerin yakınında "
            "gizli sandıklar, iksirler veya özel konuşmalar bulunabilir."
        ),
        (
            "Mana iksirlerini ilk fırsatta tüketmek yerine zor savaşlar için sakla. "
            "Özellikle boss karşılaşmalarında doğru zamanda kullanılan tek bir yetenek, "
            "uzun bir savaşın sonucunu tamamen değiştirebilir."
        ),
        (
            "Bazı düşmanlar saldırmadan önce çok kısa bir hazırlık hareketi yapar. "
            "Bu işareti öğrenirsen saldırının yönünü önceden tahmin edebilir ve "
            "hasar almadan doğru konuma geçebilirsin."
        ),
        (
            "NPC'lerin ilk söyledikleri her zaman bütün gerçeği anlatmaz. "
            "Aynı karakterle farklı zamanlarda yeniden konuşmak, yeni görevlerin ve "
            "gizli hikâye parçalarının açılmasını sağlayabilir."
        ),
        (
            "Canın azaldığında paniğe kapılıp sürekli saldırma. "
            "Geri çekilmek, düşmanın saldırı düzenini izlemek ve doğru anı beklemek "
            "çoğu zaman daha güçlü ekipmandan daha değerlidir."
        ),
        (
            "Adefonsus ağır saldırılarda ve dayanıklılıkta üstündür. "
            "Yavaş hareket etmesine rağmen doğru zamanlanmış bir saldırıyla "
            "düşmanların dengesini bozabilir ve savaşın kontrolünü ele geçirebilir."
        ),
        (
            "Preciosa hızlı saldırılar ve mana kullanımı konusunda avantajlıdır. "
            "Hareket halinde kalmak, kısa saldırılar yapmak ve rakibin açık verdiği "
            "anlarda kritik vuruş denemek onun için en etkili yöntemdir."
        ),
        (
            "İlerlemeni kaybetmemek için yalnızca bölüm sonunda değil, "
            "önemli bir eşya bulduktan veya zor bir düşmanı yendikten sonra da "
            "F5 tuşuyla kayıt yapmayı unutma."
        ),
    ],
    "EN": [
        (
            "Critical hits do more than deal extra damage. "
            "They can briefly break the defense of heavily armored enemies, "
            "making your next attack significantly more effective."
        ),
        (
            "Do not follow only the main path through caves. "
            "Hidden chests, potions and special conversations may be found near "
            "dark walls, ruined pillars and unused passages."
        ),
        (
            "Save mana potions for difficult encounters instead of using them immediately. "
            "During boss fights, one ability used at the correct moment can completely "
            "change the outcome of a long battle."
        ),
        (
            "Some enemies perform a short preparation movement before attacking. "
            "Learn these signs to predict the direction of an attack and move into "
            "a safe position before taking damage."
        ),
        (
            "An NPC's first words may not reveal the whole truth. "
            "Speaking to the same character again at different moments can unlock "
            "new quests and hidden pieces of the story."
        ),
        (
            "When your health is low, do not panic and attack continuously. "
            "Retreating, watching the enemy's pattern and waiting for the right moment "
            "is often more valuable than stronger equipment."
        ),
        (
            "Adefonsus excels at heavy attacks and endurance. "
            "Although he moves slowly, a well-timed strike can break an enemy's balance "
            "and give him control of the fight."
        ),
        (
            "Preciosa is strongest when using fast attacks and mana-based abilities. "
            "Keep moving, use short combinations and aim for critical strikes "
            "whenever the enemy leaves an opening."
        ),
        (
            "Do not save only at the end of a level. "
            "Press F5 after finding an important item or defeating a difficult enemy "
            "so that your progress is not lost."
        ),
    ],
}
# </POTBO_STAGE S0078>

# <POTBO_STAGE S0122>
oyuncu_hasari = 10
# </POTBO_STAGE S0122>

# <POTBO_STAGE S0124>

oyuncu_stamina = 100.0
oyuncu_max_stamina = 100.0
stamina_gorunen = 100.0
# </POTBO_STAGE S0124>

# <POTBO_STAGE S0126>
stamina_son_harcama = -10000
stamina_son_guncelleme = pygame.time.get_ticks()
STAMINA_YENILENME_GECIKMESI = 650
STAMINA_YENILENME_HIZI = 24.0
stamina_uyari_bitis = 0
# </POTBO_STAGE S0126>

# <POTBO_STAGE S0132>
# Aynı hedef, üst üste duran 30 ayrı alev patch'inden aynı karede 30 kez hasar almaz.
# Cooldown hedef bazlıdır; başka bir alev alanına yürümek yine temas olarak sayılır.
fire_ground_touch_cooldowns = {}
# </POTBO_STAGE S0132>

# <POTBO_STAGE S0136>
gelistirici_x_skill_r_basildi = False
gelistirici_x_skill_baslangic_ms = 0
gelistirici_x_skill_bitis_ms = 0
gelistirici_x_skill_hedef = None
gelistirici_x_skill_yol = []
gelistirici_x_skill_vurus_maskesi = 0
gelistirici_x_skill_iz_bitis = 0
GELISTIRICI_X_SKILL_SURE_MS = 2300
GELISTIRICI_X_SKILL_YARI_CAP = 116.0
GELISTIRICI_X_SKILL_TETIK_MENZILI = 390.0
# Special move üç AYRI fiziksel vuruştur. Hasar da üç bağımsız temas olarak uygulanır:
# 1) hedefin içinden geçen düz giriş, 2) / dash, 3) \ dash.
# Son vuruş biraz daha ağırdır; ancak hiçbir slash yalnız VFX olarak sayılmaz.
GELISTIRICI_X_SKILL_HASAR_CARPANLARI = (0.90, 1.15, 1.35)
# Fazlar: düz giriş/HIT-1 -> alt-sol kurulum -> / HIT-2 -> üst switch -> \ HIT-3 -> recovery.
# Toplam kontrol kaybı 2.3 saniyedir. Dash'ler hızlıdır; aradaki kısa kurulum ve
# recovery, komut verildikten sonra tekniğin tamamlanmasını izleme hissi bırakır.
GELISTIRICI_X_SKILL_ENTRY_BITIS = 0.24
GELISTIRICI_X_SKILL_KURULUM_BITIS = 0.34
GELISTIRICI_X_SKILL_SLASH1_BITIS = 0.52
GELISTIRICI_X_SKILL_SWITCH_BITIS = 0.62
GELISTIRICI_X_SKILL_SLASH2_BITIS = 0.80
combat_impact_fx = []
# Self-hit yanma state'i. Save'e yazılmaz; transient combat durumudur.
oyuncu_fire_burn_until = 0
# </POTBO_STAGE S0136>

# <POTBO_STAGE S0138>
oyuncu_fire_burn_tick_damage = 0
# </POTBO_STAGE S0138>

# <POTBO_STAGE S0148>

# Savunma zinciri. Orta sınıf iki, ağır sınıf bir darbeyi karşılar; ardından
# aynı guard zincirinde yeni temas doğrudan hasara geçer.
oyuncu_savunuyor = False
savunma_zincir_vurus = 0
savunma_son_temasi = -10000
savunma_son_guncelleme = pygame.time.get_ticks()
SAVUNMA_TUTMA_STAMINA_SANIYE = 20.0
SAVUNMA_ZINCIR_SIFIRLAMA_MS = 1350
SAVUNMA_STAMINA_MALIYETI = {
    "light": 24.0,
    "medium": 38.0,
    "heavy": 62.0,
}
SAVUNMA_ZINCIR_LIMITI = {"light": 3, "medium": 2, "heavy": 1}
# </POTBO_STAGE S0148>

# <POTBO_STAGE S0170>
oyuncu_saldiriyor = False
# Saldırı ve dash stamina dengesi. Dash artık aynı frame'de teleport değildir;
# kısa süreye yayılan ease-out hareketidir. Cooldown yalnız yeni dash'i engeller,
# yürüyüş input'unu asla kilitlemez.
SALDIRI_STAMINA_MALIYETI = 20
DASH_STAMINA_MALIYETI = 40
DASH_MESAFESI = 112.0
DASH_ADIMI = 5.0
DASH_SURESI_MS = 165
DASH_BEKLEME_SURESI = 650
son_dash_zamani = -10000
dash_tus_kilitli = False
dash_aktif_baslangic = 0
dash_aktif_bitis = 0
dash_aktif_yonu = pygame.Vector2(0.0, 0.0)
dash_aktif_son_ease = 0.0

saldiri_baslangic = 0
saldiri_suresi = 430
saldiri_bekleme_suresi = 500
son_saldiri_zamani = -10000
# </POTBO_STAGE S0170>

# <POTBO_STAGE S0172>
oyuncu_saldiri_sure_ms = saldiri_suresi
# </POTBO_STAGE S0172>

# <POTBO_STAGE S0188>

VARSAYILAN_TUS_ATAMALARI = {
    "move_up": pygame.K_w,
    "move_down": pygame.K_s,
    "move_left": pygame.K_a,
    "move_right": pygame.K_d,
    "attack": pygame.K_j,
    "block": pygame.K_k,
    "dash": pygame.K_LSHIFT,
    "interact": pygame.K_e,
    "inventory": pygame.K_TAB,
    "quick_use": pygame.K_f,
    "q_quick_use": pygame.K_q,
    "save": pygame.K_F5,
    "pause": pygame.K_ESCAPE,
}
# </POTBO_STAGE S0188>

# <POTBO_STAGE S0272>
_bers_attack = {}
# </POTBO_STAGE S0272>

# <POTBO_STAGE S0294>


def animasyonlari_olustur(kareler, cinsiyet):
    if not kareler:
        return {"idle": [], "walk": [], "attack": []}

    if cinsiyet == "male":
        return {
            "idle": kareler[0:6],
            "walk": kareler[6:12],
            "attack": kareler[12:24],
        }

    return {
        "idle": kareler[0:4],
        "walk": kareler[4:8],
        "attack": kareler[8:12],
    }
# </POTBO_STAGE S0294>

# <POTBO_STAGE S0296>


def erkek_yon_animasyonlari():
    """
    Erkek karakterin dört yöne ait idle, yürüyüş ve saldırı
    karelerini döndürür.
    """

    return {
        "down": {
            "idle": [erkek_yon_resimleri.get("idle_down")],
            "walk": [
                erkek_yon_resimleri.get("walk_down_01"),
                erkek_yon_resimleri.get("walk_down_02"),
            ],
            "attack": [
                erkek_yon_resimleri.get("idle_down"),
                erkek_yon_resimleri.get("attack_down_01"),
                erkek_yon_resimleri.get("attack_down_02"),
                erkek_yon_resimleri.get("idle_down"),
            ],
        },
        "left": {
            "idle": [erkek_yon_resimleri.get("idle_left")],
            "walk": [
                erkek_yon_resimleri.get("walk_left_01"),
                erkek_yon_resimleri.get("walk_left_02"),
            ],
            "attack": [
                erkek_yon_resimleri.get("idle_left"),
                erkek_yon_resimleri.get("attack_left_01"),
                erkek_yon_resimleri.get("idle_left"),
            ],
        },
        "right": {
            "idle": [erkek_yon_resimleri.get("idle_right")],
            "walk": [
                erkek_yon_resimleri.get("walk_right_01"),
                erkek_yon_resimleri.get("walk_right_02"),
            ],
            "attack": [
                erkek_yon_resimleri.get("idle_right"),
                erkek_yon_resimleri.get("attack_right_01"),
                erkek_yon_resimleri.get("idle_right"),
            ],
        },
        "up": {
            "idle": [erkek_yon_resimleri.get("idle_up")],
            "walk": [
                erkek_yon_resimleri.get("walk_up_01"),
                erkek_yon_resimleri.get("walk_up_02"),
            ],
            "attack": [
                erkek_yon_resimleri.get("idle_up"),
                erkek_yon_resimleri.get("attack_up_01"),
                erkek_yon_resimleri.get("attack_up_02"),
                erkek_yon_resimleri.get("idle_up"),
            ],
        },
    }
# </POTBO_STAGE S0296>

# <POTBO_STAGE S0315>


def _seviye_kazanci(level):
    """10'da ~1045 temel HP; 25'ten sonra büyüme kontrollü biçimde sürer."""
    level = int(level)
    if level <= 10:
        return {
            "hp": 105,
            "damage": 13,
            "strength": 2,
            "mana": 8,
            "stamina": 4.0,
        }
    if level <= 25:
        return {
            "hp": 68,
            "damage": 9,
            "strength": 1,
            "mana": 6,
            "stamina": 3.0,
        }
    return {
        "hp": 82,
        "damage": 10,
        "strength": 1,
        "mana": 7,
        "stamina": 3.5,
    }


def oyuncu_seviye_kazanclarini_uygula(eski_level, yeni_level):
    global oyuncu_guc, oyuncu_hasari
    global oyuncu_hp, oyuncu_max_hp, oyuncu_mana, oyuncu_max_mana
    global oyuncu_stamina, oyuncu_max_stamina
    if yeni_level <= eski_level:
        return
    hp_artis = hasar_artis = guc_artis = mana_artis = 0
    stamina_artis = 0.0
    for lv in range(int(eski_level) + 1, int(yeni_level) + 1):
        k = _seviye_kazanci(lv)
        hp_artis += k["hp"]
        hasar_artis += k["damage"]
        guc_artis += k["strength"]
        mana_artis += k["mana"]
        stamina_artis += k["stamina"]
    oyuncu_max_hp += hp_artis
    oyuncu_hp = min(oyuncu_max_hp, oyuncu_hp + hp_artis)
    oyuncu_hasari += hasar_artis
    oyuncu_guc += guc_artis
    oyuncu_max_mana += mana_artis
    oyuncu_mana = min(oyuncu_max_mana, oyuncu_mana + mana_artis)
    oyuncu_max_stamina += stamina_artis
    oyuncu_stamina = min(oyuncu_max_stamina, oyuncu_stamina + stamina_artis)
# </POTBO_STAGE S0315>

# <POTBO_STAGE S0391>


# =========================================================
# OYUN İÇİ PANEL
# =========================================================


def gotik_bicak_bari_ciz(
    rect,
    oran,
    dolgu_rengi,
    arka_rengi,
    vurgu_rengi,
    metin="",
    uyari=False,
    dis_sus=False,
    tier=0,
):
    """Health/mana için asimetrik bıçak formu.

    Sol üst uç sivridir; sol alt kontur yalnız kısa bir bevel ile gövdeye bağlanır.
    Sağ üst uç en ileri noktadır, sağ alt uç belirgin biçimde geride ve yine keskindir.
    Bu geometri can ve mana için aynıdır. Her 10 level'da çerçeveye küçük metal
    dişler eklenir; stamina bu fonksiyonu kullanmaz ve bilinçli olarak sade kalır.
    """
    oran = max(0.0, min(1.0, float(oran)))
    tier = max(0, min(5, int(tier)))
    rect = pygame.Rect(rect)
    sallanti = int(round(math.sin(pygame.time.get_ticks() * 0.08) * 2)) if uyari else 0
    rect = rect.move(sallanti, 0)
    x, y, w, h = rect
    r = x + w
    b = y + h

    # daha agresif bıçak geometrisi: eğimler uzatıldı, sağ üst spear-tip daha
    # ileri okunur, sağ alt uç belirgin biçimde geride ikinci keskin nokta olur.
    # Sol alt yalnız küçük bir bevel taşır; barın genel geometrisi keskin tutulur.
    alt_geri = max(18, min(30, h + 7))
    sol_bevel = max(3, h // 6)
    dis = [
        (x, y + max(2, h // 5)),  # sol üst sivri burun
        (x + 21, y),
        (r - 25, y),
        (r, y + max(3, h // 4)),  # sağ üst en ileri uç
        (r - 8, y + max(5, h // 2)),
        (r - alt_geri, b),  # sağ alt geride, fakat keskin
        (x + 16, b),
        (x + 7, b - 1),
        (x + 2, b - sol_bevel),
    ]

    if dis_sus:
        pygame.draw.polygon(ekran, (5, 4, 6), [(px, py + 2) for px, py in dis])
    pygame.draw.polygon(ekran, (3, 3, 4), dis)

    inset = 2 if h >= 10 else 1
    ix, iy = x + inset, y + inset
    ir, ib = r - inset, b - inset
    i_alt_geri = max(13, alt_geri - inset)
    ic = [
        (ix, iy + max(2, (ib - iy) // 5)),
        (ix + 19, iy),
        (ir - 23, iy),
        (ir, iy + max(3, (ib - iy) // 4)),
        (ir - 7, iy + max(4, (ib - iy) // 2)),
        (ir - i_alt_geri, ib),
        (ix + 15, ib),
        (ix + 7, ib - 1),
        (ix + 2, ib - max(2, sol_bevel - 1)),
    ]
    pygame.draw.polygon(ekran, arka_rengi, ic)

    # Dolgu da aynı bıçak poligonu içinde clip edilir; böylece oran azalırken
    # sağ uç geometrisi bozulmaz, yalnız görünür dolgu genişliği kısalır.
    yerel = pygame.Surface((w, h), pygame.SRCALPHA)
    yerel_ic = [(px - x, py - y) for px, py in ic]
    pygame.draw.polygon(yerel, (*dolgu_rengi, 255), yerel_ic)
    fill_w = int(round(w * oran))
    if fill_w > 0:
        ekran.blit(
            yerel,
            rect.topleft,
            area=pygame.Rect(0, 0, min(w, fill_w), h),
        )

    if oran > 0.0 and h >= 7:
        hi_end = min(ir - 17, ix + max(1, int((ir - ix) * oran)))
        if hi_end > ix + 10:
            pygame.draw.line(
                ekran,
                vurgu_rengi,
                (ix + 12, iy),
                (hi_end, iy),
                1,
            )

    cerceve = PARLAK_KIRMIZI if uyari else (92 + tier * 12, 78, 82)
    pygame.draw.lines(ekran, cerceve, True, dis, 2 if tier >= 3 else 1)

    # Onluk level eşiklerinde yalnız çerçeve ihtişamı artar; barın okunabilir
    # bıçak silueti ve dolgu oranı değişmez.
    for i in range(tier):
        px = x + 34 + i * 27
        if px + 12 >= r - 28:
            break
        ust = [(px, y), (px + 6, y - 5 - i), (px + 12, y)]
        pygame.draw.polygon(ekran, (70 + i * 18, 7, 17), ust)
        pygame.draw.lines(ekran, (145, 30, 43), True, ust, 1)

    if metin and h >= 14:
        yazi_yaz(
            metin,
            rect.centerx,
            rect.centery,
            BEYAZ,
            mini_font,
            True,
        )


def sade_stamina_bari_ciz(rect, oran, uyari=False):
    """Health barın hemen altında duran düz, ince ve dekorasyonsuz stamina."""
    oran = max(0.0, min(1.0, float(oran)))
    rect = pygame.Rect(rect)
    if uyari:
        rect = rect.move(
            int(round(math.sin(pygame.time.get_ticks() * 0.08) * 2)),
            0,
        )
    pygame.draw.rect(ekran, (24, 21, 5), rect)
    if oran > 0.0:
        dolu = pygame.Rect(
            rect.x,
            rect.y,
            int(round(rect.width * oran)),
            rect.height,
        )
        pygame.draw.rect(ekran, (236, 205, 40), dolu)
        if dolu.width > 4:
            pygame.draw.line(
                ekran,
                (255, 241, 123),
                (dolu.x + 2, dolu.y),
                (dolu.right - 2, dolu.y),
                1,
            )
    pygame.draw.rect(
        ekran,
        PARLAK_KIRMIZI if uyari else (70, 67, 54),
        rect,
        1,
    )
# </POTBO_STAGE S0391>

# <POTBO_STAGE S0421>


oyuncu_kanli_hasar_kaydi = _stage1_oyuncu_kanli_hasar_kaydi
# </POTBO_STAGE S0421>

# <POTBO_STAGE S0425>


def oyuncu_saldiri_tusu_basili_mi():
    try:
        basili = pygame.key.get_pressed()
        return bool(basili[tus_atamasi("attack")])
    except (IndexError, TypeError, pygame.error):
        return False
# </POTBO_STAGE S0425>

# <POTBO_STAGE S0501>


def combat_impact_spawn(x, y, tur="slash", guc=1.0, yon=None):
    v = pygame.Vector2(yon or (1.0, 0.0))
    if v.length_squared() <= 1e-6:
        v = pygame.Vector2(1.0, 0.0)
    combat_impact_fx.append(
        {
            "x": float(x),
            "y": float(y),
            "start": pygame.time.get_ticks(),
            "life": int(150 + 55 * min(2.5, guc)),
            "type": str(tur),
            "power": float(guc),
            "angle": math.degrees(math.atan2(v.y, v.x)),
        }
    )
    if len(combat_impact_fx) > 48:
        del combat_impact_fx[:-48]
# </POTBO_STAGE S0501>

# <POTBO_STAGE S0511>


def oyuncu_olum_cikis_baslat(hedef):
    global oyuncu_olum_cikis_baslangic_ms, oyuncu_olum_cikis_hedefi
    if oyuncu_olum_cikis_baslangic_ms > 0:
        return False
    oyuncu_olum_cikis_hedefi = str(hedef)
    oyuncu_olum_cikis_baslangic_ms = pygame.time.get_ticks()
    oyuncu_saldiri_durumunu_sifirla()
    return True
# </POTBO_STAGE S0511>

# <POTBO_STAGE S0538>


def stamina_guncelle():
    global oyuncu_stamina, stamina_son_guncelleme
    global stamina_gorunen, mana_gorunen, hp_gorunen
    simdi = pygame.time.get_ticks()
    dt = max(
        0.0,
        min(0.05, (simdi - stamina_son_guncelleme) / 1000.0),
    )
    stamina_son_guncelleme = simdi
    if (
        not oyuncu_kontrol_kilitli_mi(simdi)
        and simdi - stamina_son_harcama >= STAMINA_YENILENME_GECIKMESI
    ):
        oyuncu_stamina = min(
            oyuncu_max_stamina,
            oyuncu_stamina + STAMINA_YENILENME_HIZI * dt,
        )
    oran = min(1.0, dt * 11.0)
    stamina_gorunen += (oyuncu_stamina - stamina_gorunen) * oran
    mana_gorunen += (oyuncu_mana - mana_gorunen) * oran
    hp_gorunen += (oyuncu_hp - hp_gorunen) * oran
# </POTBO_STAGE S0538>

# <POTBO_STAGE S0540>


def oyuncu_locomotion_durumunu_sifirla():
    global oyuncu_hareket_hiz_vektoru, oyuncu_hareket_son_guncelleme
    global dash_tus_kilitli, dash_aktif_baslangic, dash_aktif_bitis
    global dash_aktif_yonu, dash_aktif_son_ease, son_dash_zamani
    oyuncu_hareket_hiz_vektoru = pygame.Vector2(0.0, 0.0)
    oyuncu_hareket_son_guncelleme = pygame.time.get_ticks()
    dash_tus_kilitli = False
    dash_aktif_baslangic = 0
    dash_aktif_bitis = 0
    dash_aktif_yonu = pygame.Vector2(0.0, 0.0)
    dash_aktif_son_ease = 0.0
    son_dash_zamani = -10000
    gelistirici_x_skill_sifirla(True)


def oyuncu_dash_aktif_mi(simdi=None):
    if simdi is None:
        simdi = pygame.time.get_ticks()
    return dash_aktif_bitis > int(simdi) and dash_aktif_yonu.length_squared() > 0.0


def gelistirici_x_skill_aktif_mi(simdi=None):
    if simdi is None:
        simdi = pygame.time.get_ticks()
    return (
        gelistirici_x_skill_baslangic_ms > 0
        and int(simdi) < gelistirici_x_skill_bitis_ms
    )


def gelistirici_x_skill_sifirla(tam_reset=False):
    global gelistirici_x_skill_r_basildi, gelistirici_x_skill_baslangic_ms
    global gelistirici_x_skill_bitis_ms, gelistirici_x_skill_hedef
    global gelistirici_x_skill_yol, gelistirici_x_skill_vurus_maskesi
    gelistirici_x_skill_r_basildi = False
    gelistirici_x_skill_baslangic_ms = 0
    gelistirici_x_skill_bitis_ms = 0
    gelistirici_x_skill_vurus_maskesi = 0
    if tam_reset:
        gelistirici_x_skill_hedef = None
        gelistirici_x_skill_yol = []
# </POTBO_STAGE S0540>

# <POTBO_STAGE S0546>


def _gelistirici_x_skill_ease_out(t):
    t = max(0.0, min(1.0, float(t)))
    return 1.0 - (1.0 - t) ** 4


def _gelistirici_x_skill_smooth(t):
    t = max(0.0, min(1.0, float(t)))
    return t * t * (3.0 - 2.0 * t)


def _gelistirici_x_skill_bezier(a, control, b, t):
    t = _gelistirici_x_skill_smooth(t)
    inv = 1.0 - t
    return a * (inv * inv) + control * (2.0 * inv * t) + b * (t * t)


def gelistirici_x_skill_guncelle(simdi=None):
    """Karakter bedenini üç vuruşun tamamında sürer: düz HIT -> / HIT -> \\ HIT."""
    global oyuncu_x, oyuncu_y, oyuncu_yonu
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if not gelistirici_x_skill_aktif_mi(simdi) or len(gelistirici_x_skill_yol) < 6:
        if (
            gelistirici_x_skill_baslangic_ms
            and int(simdi) >= gelistirici_x_skill_bitis_ms
        ):
            gelistirici_x_skill_sifirla(False)
        return False

    p = max(
        0.0,
        min(
            1.0,
            (int(simdi) - gelistirici_x_skill_baslangic_ms)
            / float(GELISTIRICI_X_SKILL_SURE_MS),
        ),
    )
    bas, entry, p1, p2, p3, p4 = gelistirici_x_skill_yol
    e0 = GELISTIRICI_X_SKILL_ENTRY_BITIS
    e_setup = GELISTIRICI_X_SKILL_KURULUM_BITIS
    e1 = GELISTIRICI_X_SKILL_SLASH1_BITIS
    e2 = GELISTIRICI_X_SKILL_SWITCH_BITIS
    e3 = GELISTIRICI_X_SKILL_SLASH2_BITIS

    if p < e0:
        # HIT-1 — DÜZ GİRİŞ: karakter hedef merkezinin içinden geçerek ileri çıkar.
        # Temas, beden segmentinin hedef merkezini geçtiği gerçek geometrik anda oluşur.
        tloc = _gelistirici_x_skill_ease_out(p / max(0.001, e0))
        pos = bas.lerp(entry, tloc)
        yon_farki = entry - bas
        if gelistirici_x_skill_hedef is not None:
            merkez = pygame.Vector2(
                float(gelistirici_x_skill_hedef.x),
                float(gelistirici_x_skill_hedef.y),
            )
            toplam = max(1e-6, (entry - bas).length())
            hit_t = max(0.0, min(1.0, (merkez - bas).length() / toplam))
            if tloc >= hit_t:
                _gelistirici_x_skill_vur(0, yon_farki)
    elif p < e_setup:
        # Kontrol oyuncuda değildir; karakter '/' çizgisinin alt-sol başlangıcına kayar.
        tloc = (p - e0) / max(0.001, e_setup - e0)
        merkez = pygame.Vector2(
            float(gelistirici_x_skill_hedef.x),
            float(gelistirici_x_skill_hedef.y),
        )
        dis = entry - merkez
        if dis.length_squared() <= 1e-6:
            dis = pygame.Vector2(-1.0, 1.0)
        control = merkez + dis.normalize() * (GELISTIRICI_X_SKILL_YARI_CAP * 1.10)
        pos = _gelistirici_x_skill_bezier(entry, control, p1, tloc)
        yon_farki = p1 - entry
    elif p < e1:
        # / : alt-sol -> üst-sağ. Karakter çizginin kendisini dash olarak kat eder.
        tloc = _gelistirici_x_skill_ease_out((p - e_setup) / max(0.001, e1 - e_setup))
        pos = p1.lerp(p2, tloc)
        yon_farki = p2 - p1
        if tloc >= 0.50:
            _gelistirici_x_skill_vur(1, yon_farki)
    elif p < e2:
        # İkinci kesiye hazırlık: hedefin üst tarafında çok kısa, hasarsız switch.
        tloc = (p - e1) / max(0.001, e2 - e1)
        merkez = pygame.Vector2(
            float(gelistirici_x_skill_hedef.x),
            float(gelistirici_x_skill_hedef.y),
        )
        control = merkez + pygame.Vector2(0.0, -GELISTIRICI_X_SKILL_YARI_CAP * 1.34)
        pos = _gelistirici_x_skill_bezier(p2, control, p3, tloc)
        yon_farki = p3 - p2
    elif p < e3:
        # \\ : üst-sol -> alt-sağ. İkinci dash X'i kapatır.
        tloc = _gelistirici_x_skill_ease_out((p - e2) / max(0.001, e3 - e2))
        pos = p3.lerp(p4, tloc)
        yon_farki = p4 - p3
        if tloc >= 0.50:
            _gelistirici_x_skill_vur(2, yon_farki)
    else:
        # Yaklaşık son üçte birlik bölüm recovery/commitment'tır; kontrol hemen dönmez.
        pos = pygame.Vector2(p4)
        yon_farki = p4 - p3

    oyuncu_x, oyuncu_y = float(pos.x), float(pos.y)
    if abs(yon_farki.x) > abs(yon_farki.y):
        oyuncu_yonu = "right" if yon_farki.x > 0 else "left"
    elif abs(yon_farki.y) > 1e-6:
        oyuncu_yonu = "down" if yon_farki.y > 0 else "up"

    if p >= 1.0:
        gelistirici_x_skill_sifirla(False)
    return True


def _gelistirici_x_skill_cizgi_progress(simdi, faz_bas, faz_son):
    if gelistirici_x_skill_baslangic_ms <= 0:
        return 1.0
    p = (int(simdi) - int(gelistirici_x_skill_baslangic_ms)) / float(
        GELISTIRICI_X_SKILL_SURE_MS
    )
    return max(
        0.0,
        min(1.0, (p - faz_bas) / max(0.001, faz_son - faz_bas)),
    )
# </POTBO_STAGE S0546>

# <POTBO_STAGE S0548>


def gelistirici_x_skill_efekt_ciz():
    """Yalnız iki gerçek kesme dash'ini çizer: önce '/', sonra '\\'."""
    simdi = pygame.time.get_ticks()
    if simdi >= gelistirici_x_skill_iz_bitis or len(gelistirici_x_skill_yol) < 6:
        return

    _, _, p1, p2, p3, p4 = gelistirici_x_skill_yol
    prog1 = _gelistirici_x_skill_cizgi_progress(
        simdi,
        GELISTIRICI_X_SKILL_KURULUM_BITIS,
        GELISTIRICI_X_SKILL_SLASH1_BITIS,
    )
    prog2 = _gelistirici_x_skill_cizgi_progress(
        simdi,
        GELISTIRICI_X_SKILL_SWITCH_BITIS,
        GELISTIRICI_X_SKILL_SLASH2_BITIS,
    )

    if simdi <= gelistirici_x_skill_bitis_ms:
        alpha1 = 218 if prog1 < 1.0 else 176
        alpha2 = 232
    else:
        fade = max(
            0.0,
            min(
                1.0,
                (gelistirici_x_skill_iz_bitis - simdi) / 230.0,
            ),
        )
        alpha1 = int(185 * fade)
        alpha2 = int(225 * fade)

    katman = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    _gelistirici_x_skill_kesik_ciz(katman, p1, p2, prog1, alpha1)
    _gelistirici_x_skill_kesik_ciz(
        katman, p3, p4, prog2, alpha2, cekirdek=(255, 228, 232)
    )
    if prog1 >= 0.52 and prog2 >= 0.52 and gelistirici_x_skill_hedef is not None:
        cx = int(round(dunya_ekran_x(gelistirici_x_skill_hedef.x)))
        cy = int(round(dunya_ekran_y(gelistirici_x_skill_hedef.y - 12.0)))
        pygame.draw.circle(
            katman,
            (255, 246, 248, min(220, alpha2)),
            (cx, cy),
            5,
            1,
        )
        pygame.draw.circle(
            katman,
            (220, 24, 48, min(170, alpha2)),
            (cx, cy),
            10,
            1,
        )
    ekran.blit(katman, (0, 0))
# </POTBO_STAGE S0548>

# <POTBO_STAGE S0557>
_v31_kanli_hasar_kaydi = oyuncu_kanli_hasar_kaydi
# </POTBO_STAGE S0557>

# <POTBO_STAGE S0561>


oyuncu_kanli_hasar_kaydi = _stage2_oyuncu_kanli_hasar_kaydi
# </POTBO_STAGE S0561>

# <POTBO_STAGE S0581>


# ---------------------------------------------------------
# PLAYER DAMAGE FLASH -- potion flaşıyla ayrık renk dili
# ---------------------------------------------------------
_v32_kanli_hasar_kaydi_v33 = oyuncu_kanli_hasar_kaydi


def oyuncu_kanli_hasar_kaydi(kaynak_x, kaynak_y, profil, hasar, kaynak_adi=""):
    if int(hasar) > 0:
        oyuncu_parlama_baslat("damage")
    return _v32_kanli_hasar_kaydi_v33(kaynak_x, kaynak_y, profil, hasar, kaynak_adi)


def oyuncu_sprite_parlamasi_ciz(sprite, rect):
    """Potion = eski beyaz/kırmızı; damage = kısa, koyu kan kırmızısı iç flaş."""
    simdi = pygame.time.get_ticks()
    if sprite is None or rect is None or simdi >= oyuncu_parlama_bitis:
        return
    bas = int(oyuncu_parlama_baslangic or (oyuncu_parlama_bitis - 430))
    toplam = max(1, oyuncu_parlama_bitis - bas)
    p = max(0.0, min(1.0, (simdi - bas) / float(toplam)))
    fade = math.sin(math.pi * p) ** 0.72

    if str(oyuncu_parlama_turu) == "damage":
        # Potabile'nin parlak içim dilinden bilinçli biçimde daha koyu.
        pulse = 0.72 + 0.28 * (0.5 + 0.5 * math.sin(p * math.tau * 2.0))
        sprite_maskeli_parlama_ciz(sprite, rect, (118, 4, 20), int(162 * fade * pulse))
        return

    faz = int(min(3, p * 4.0))
    if faz in (0, 2):
        renk = (248, 244, 238)
        alfa = int(132 * fade)
    else:
        renk = (225, 30, 38)
        alfa = int(118 * fade)
    sprite_maskeli_parlama_ciz(sprite, rect, renk, alfa)
# </POTBO_STAGE S0581>

# <POTBO_STAGE S0584>


def _v33_common_saldiri_baslat(self, simdi):
    _v32_common_saldiri_baslat_v33(self, simdi)
    self.attack_player_hit_slots = set()
# </POTBO_STAGE S0584>

# <POTBO_STAGE S0623>
V34_DASH_TRAIL_MAX = 14
# </POTBO_STAGE S0623>

# <POTBO_STAGE S0630>
v34_special_effect_radius = GELISTIRICI_X_SKILL_YARI_CAP
# </POTBO_STAGE S0630>

# <POTBO_STAGE S0633>
v34_dash_trail = deque(maxlen=V34_DASH_TRAIL_MAX)
# </POTBO_STAGE S0633>

# <POTBO_STAGE S0640>
v34_dash_last_pos = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
v34_dash_last_active = False
# </POTBO_STAGE S0640>

# <POTBO_STAGE S0650>


def _v34_segment_static_clear(a, b, step=V34_SCRIPT_STEP):
    """Oyuncu footprint'ini bir scripted segment boyunca map/static blocker'a taşır."""
    a = pygame.Vector2(a)
    b = pygame.Vector2(b)
    delta = b - a
    length = delta.length()
    if length <= 1e-6:
        return _v34_static_position_valid(a.x, a.y)
    n = max(1, int(math.ceil(length / max(1.0, float(step)))))
    for i in range(n + 1):
        p = a.lerp(b, i / n)
        if not _v34_static_position_valid(p.x, p.y):
            return False
    return True
# </POTBO_STAGE S0650>

# <POTBO_STAGE S0654>


# ---------------------------------------------------------
# DASH FEEL: normal dash'e hafif beden izi eklenir.
# ---------------------------------------------------------
_v33_oyuncu_dash_guncelle = oyuncu_dash_guncelle


def oyuncu_dash_guncelle(simdi=None):
    global v34_dash_last_pos, v34_dash_last_active
    if simdi is None:
        simdi = pygame.time.get_ticks()
    before = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    moved = _v33_oyuncu_dash_guncelle(simdi)
    after = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    active = oyuncu_dash_aktif_mi(simdi)
    if moved or active:
        if not v34_dash_trail or after.distance_to(v34_dash_trail[-1][1]) >= 6.0:
            v34_dash_trail.append((int(simdi), after.copy()))
    elif v34_dash_last_active:
        v34_dash_trail.append((int(simdi), after.copy()))
    v34_dash_last_pos = after
    v34_dash_last_active = active
    return moved
# </POTBO_STAGE S0654>

# <POTBO_STAGE S0662>


def _gelistirici_x_skill_vur(slot, yon=None):
    """V34: üç guaranteed presentation hit; ilk iki hit koreografiyi erken öldürmez."""
    global gelistirici_x_skill_vurus_maskesi
    slot = max(0, min(2, int(slot)))
    bit = 1 << slot
    if gelistirici_x_skill_vurus_maskesi & bit:
        return False
    gelistirici_x_skill_vurus_maskesi |= bit

    hedef = gelistirici_x_skill_hedef
    center = (
        pygame.Vector2(v34_special_effect_center)
        if v34_special_effect_center is not None
        else pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    )
    if hedef is not None:
        center = pygame.Vector2(
            float(getattr(hedef, "x", center.x)),
            float(getattr(hedef, "y", center.y)),
        )

    if yon is None or pygame.Vector2(yon).length_squared() <= 1e-6:
        defaults = (
            pygame.Vector2(1.0, 0.0),
            pygame.Vector2(1.0, -1.0),
            pygame.Vector2(1.0, 1.0),
        )
        yon = defaults[slot]
    yon = pygame.Vector2(yon)
    if yon.length_squared() > 1e-6:
        yon = yon.normalize()

    carpan = GELISTIRICI_X_SKILL_HASAR_CARPANLARI[slot]
    requested_damage = max(1, int(round(float(oyuncu_hasari) * float(carpan))))
    applied_damage = 0
    target_alive = hedef is not None and int(getattr(hedef, "hp", 0)) > 0

    if hedef is not None:
        # İlk iki hit hedefi 1 HP altında bırakmaz. Bu, special move'un üç gerçek
        # temasının da okunmasını garanti eder. Üçüncü hit normal ölüm kurallarını çözer.
        hp_before = max(0, int(getattr(hedef, "hp", 0)))
        if hp_before > 0:
            if V34_SPECIAL_FIRST_TWO_HITS_NONLETHAL and slot < 2:
                applied_damage = min(requested_damage, max(0, hp_before - 1))
            else:
                applied_damage = requested_damage
            if applied_damage > 0:
                try:
                    hedef.hasar_al(applied_damage, kaynak="player")
                except TypeError:
                    hedef.hasar_al(applied_damage)

    # Target ilk iki darbede 1 HP'ye inse veya üçüncü darbede ölse bile impact
    # sunumu her slotta çalışır; koreografi asla "bir vurup bırakmış" görünmez.
    silah_temas_sesi_cal(
        str(getattr(hedef, "tur", "crawler")) if hedef is not None else "crawler"
    )
    powers = (1.92, 2.48, 3.18)
    shakes = ((5.4, 108), (7.8, 148), (11.6, 220))
    combat_impact_spawn(
        center.x,
        center.y - 14.0,
        "slash_heavy",
        powers[slot],
        yon,
    )
    kamera_hit_sarsintisi_baslat(shakes[slot][0], shakes[slot][1])
    _v34_special_hit_feedback(slot, center, yon)

    if slot == 2:
        # Final keside daha geniş ikinci impact halkası teknik kapanışını okutur.
        combat_impact_spawn(center.x, center.y - 14.0, "shock_heavy", 1.48, yon)

    dunya_olayi_kaydet(
        "developer_x_special_hit",
        index=slot + 1,
        damage=applied_damage,
        requested_damage=requested_damage,
        target_alive_before=target_alive,
        serial=v34_special_move_serial,
    )
    return True


def _v34_special_phase_values(p):
    """Special move ritmi: hareket + mikro-impact hold'ları.

    2.3 saniyelik toplam kontrol kilidi korunur; hızlı dash'ler daha kısa aralıklarda,
    vuruş sonrası mikro duraklar ise tekniğe ağırlık veren ayrı fazlardadır.
    """
    # entry dash / hit1 pause / setup / slash1 / hit2 pause / switch / slash2 /
    # hit3 pause / settling / recovery
    return {
        "entry_end": 0.205,
        "hit1_hold_end": 0.235,
        "setup_end": 0.330,
        "slash1_end": 0.455,
        "hit2_hold_end": 0.495,
        "switch_end": 0.585,
        "slash2_end": 0.715,
        "hit3_hold_end": 0.765,
        "settle_end": 0.845,
    }
# </POTBO_STAGE S0662>

# <POTBO_STAGE S0664>


def gelistirici_x_skill_guncelle(simdi=None):
    """V34 authored motion director: body gerçekten entry -> / -> \\ rotasını kat eder."""
    global oyuncu_x, oyuncu_y, v34_special_last_pos, v34_special_exit_safe_pos
    global v34_special_recovery_grace_until

    if simdi is None:
        simdi = pygame.time.get_ticks()
    simdi = int(simdi)
    if not gelistirici_x_skill_aktif_mi(simdi) or len(gelistirici_x_skill_yol) < 6:
        if gelistirici_x_skill_baslangic_ms and simdi >= gelistirici_x_skill_bitis_ms:
            # Final pozisyonu dynamic body ile çakışıyorsa oyuncuyu en yakın güvenli
            # noktaya çıkar. Static invalidity zaten scripted resolver tarafından engellenir.
            _v34_player_depenetrate(False)
            gelistirici_x_skill_sifirla(False)
        return False

    total = max(1.0, float(GELISTIRICI_X_SKILL_SURE_MS))
    p = max(
        0.0,
        min(
            1.0,
            (simdi - gelistirici_x_skill_baslangic_ms) / total,
        ),
    )
    bas, entry, p1, p2, p3, p4 = [pygame.Vector2(x) for x in gelistirici_x_skill_yol]
    center = (
        pygame.Vector2(v34_special_locked_center)
        if v34_special_locked_center is not None
        else (p1 + p2 + p3 + p4) * 0.25
    )
    radius = float(v34_special_effect_radius)
    setup_control, switch_control = _v34_special_path_controls(
        [bas, entry, p1, p2, p3, p4], center, radius
    )
    phase = _v34_special_phase_values(p)

    entry_end = phase["entry_end"]
    hit1_hold_end = phase["hit1_hold_end"]
    setup_end = phase["setup_end"]
    slash1_end = phase["slash1_end"]
    hit2_hold_end = phase["hit2_hold_end"]
    switch_end = phase["switch_end"]
    slash2_end = phase["slash2_end"]
    hit3_hold_end = phase["hit3_hold_end"]
    settle_end = phase["settle_end"]

    phase_name = "recovery"
    if p < entry_end:
        t = _gelistirici_x_skill_ease_out(p / entry_end)
        desired = bas.lerp(entry, t)
        delta = entry - bas
        phase_name = "entry"
        # Hit tam body segmenti target center'dan geçtiğinde.
        seg = entry - bas
        denom = max(1e-6, seg.length_squared())
        hit_t = max(0.0, min(1.0, (center - bas).dot(seg) / denom))
        if t >= hit_t:
            _gelistirici_x_skill_vur(0, delta)
    elif p < hit1_hold_end:
        desired = entry
        delta = entry - bas
        phase_name = "hit1_hold"
    elif p < setup_end:
        t = (p - hit1_hold_end) / max(0.001, setup_end - hit1_hold_end)
        desired = _gelistirici_x_skill_bezier(entry, setup_control, p1, t)
        delta = p1 - entry
        phase_name = "setup"
    elif p < slash1_end:
        t = _gelistirici_x_skill_ease_out(
            (p - setup_end) / max(0.001, slash1_end - setup_end)
        )
        desired = p1.lerp(p2, t)
        delta = p2 - p1
        phase_name = "slash1"
        if t >= 0.50:
            _gelistirici_x_skill_vur(1, delta)
    elif p < hit2_hold_end:
        desired = p2
        delta = p2 - p1
        phase_name = "hit2_hold"
    elif p < switch_end:
        t = (p - hit2_hold_end) / max(0.001, switch_end - hit2_hold_end)
        desired = _gelistirici_x_skill_bezier(p2, switch_control, p3, t)
        delta = p3 - p2
        phase_name = "switch"
    elif p < slash2_end:
        t = _gelistirici_x_skill_ease_out(
            (p - switch_end) / max(0.001, slash2_end - switch_end)
        )
        desired = p3.lerp(p4, t)
        delta = p4 - p3
        phase_name = "slash2"
        if t >= 0.50:
            _gelistirici_x_skill_vur(2, delta)
    elif p < hit3_hold_end:
        desired = p4
        delta = p4 - p3
        phase_name = "hit3_hold"
    elif p < settle_end:
        # Finalde 12 px kadar yön boyunca "settle"; rigid stop hissini azaltır.
        t = _gelistirici_x_skill_smooth(
            (p - hit3_hold_end) / max(0.001, settle_end - hit3_hold_end)
        )
        d = p4 - p3
        if d.length_squared() <= 1e-6:
            d = pygame.Vector2(1.0, 0.0)
        d = d.normalize()
        settle = p4 + d * 12.0
        if not _v34_static_position_valid(settle.x, settle.y):
            settle = p4
        desired = p4.lerp(settle, t)
        delta = d
        phase_name = "settle"
    else:
        d = p4 - p3
        if d.length_squared() <= 1e-6:
            d = pygame.Vector2(1.0, 0.0)
        d = d.normalize()
        settle = p4 + d * 12.0
        if not _v34_static_position_valid(settle.x, settle.y):
            settle = p4
        desired = settle
        delta = d
        phase_name = "recovery"

    actual = _v34_special_scripted_position_apply(
        desired, previous=v34_special_last_pos
    )
    _v34_special_set_facing(delta)
    if actual.distance_to(v34_special_last_pos) > 0.5:
        _v34_special_register_trail(simdi, actual, phase_name)
    v34_special_last_pos = actual.copy()

    # Special aktifken her frame tüm alternatif movement kanallarını bastır.
    oyuncu_hareket_hiz_vektoru.update(0.0, 0.0)
    oyuncu_zorlanmis_hiz.update(0.0, 0.0)

    if p >= 1.0:
        v34_special_exit_safe_pos = actual.copy()
        _v34_player_depenetrate(False)
        gelistirici_x_skill_sifirla(False)
    return True
# </POTBO_STAGE S0664>

# <POTBO_STAGE S0666>


def _v34_special_speed_lines_ciz(katman, simdi):
    if not gelistirici_x_skill_aktif_mi(simdi) or len(gelistirici_x_skill_yol) < 6:
        return
    elapsed = (simdi - gelistirici_x_skill_baslangic_ms) / max(
        1.0, float(GELISTIRICI_X_SKILL_SURE_MS)
    )
    phase = _v34_special_phase_values(elapsed)
    active_slash = None
    if phase["setup_end"] <= elapsed <= phase["slash1_end"]:
        active_slash = (
            pygame.Vector2(gelistirici_x_skill_yol[2]),
            pygame.Vector2(gelistirici_x_skill_yol[3]),
        )
    elif phase["switch_end"] <= elapsed <= phase["slash2_end"]:
        active_slash = (
            pygame.Vector2(gelistirici_x_skill_yol[4]),
            pygame.Vector2(gelistirici_x_skill_yol[5]),
        )
    if active_slash is None:
        return
    a, b = active_slash
    d = b - a
    if d.length_squared() <= 1e-6:
        return
    d = d.normalize()
    normal = pygame.Vector2(-d.y, d.x)
    center = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    seed = (simdi // 17) + v34_special_move_serial * 101
    rng = random.Random(seed)
    for i in range(9):
        back = rng.uniform(22.0, 86.0)
        side = rng.uniform(-38.0, 38.0)
        length = rng.uniform(18.0, 46.0)
        w0 = center - d * back + normal * side
        w1 = w0 - d * length
        s0 = _v34_world_to_screen_vec(w0, -10.0)
        s1 = _v34_world_to_screen_vec(w1, -10.0)
        alpha = rng.randint(38, 88)
        pygame.draw.line(katman, (248, 222, 228, alpha), s0, s1, 1)
# </POTBO_STAGE S0666>

# <POTBO_STAGE S0669>


def _v34_special_cinema_bars_ciz(simdi):
    if not gelistirici_x_skill_aktif_mi(simdi):
        return
    p = max(
        0.0,
        min(
            1.0,
            (simdi - gelistirici_x_skill_baslangic_ms)
            / max(1.0, float(GELISTIRICI_X_SKILL_SURE_MS)),
        ),
    )
    edge = min(1.0, p / 0.08, (1.0 - p) / 0.10 if p > 0.90 else 1.0)
    h = int(V34_SPECIAL_CINEMA_BAR_MAX * max(0.0, edge))
    if h <= 0:
        return
    overlay = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    pygame.draw.rect(overlay, (0, 0, 0, 150), (0, 0, GENISLIK, h))
    pygame.draw.rect(overlay, (0, 0, 0, 150), (0, YUKSEKLIK - h, GENISLIK, h))
    ekran.blit(overlay, (0, 0))
# </POTBO_STAGE S0669>

# <POTBO_STAGE S0672>


_v33_gelistirici_x_skill_efekt_ciz = gelistirici_x_skill_efekt_ciz


def gelistirici_x_skill_efekt_ciz():
    """Mevcut X slash çizgilerine body trail, afterimage ve impact crescendo ekler."""
    simdi = pygame.time.get_ticks()
    katman = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    _v34_special_afterimages_ciz(katman, simdi)
    _v34_special_trail_ciz(katman, simdi)
    _v34_special_speed_lines_ciz(katman, simdi)
    ekran.blit(katman, (0, 0))

    # Eski iki slash çizgisi korunur; V34 beden hareketini onunla aynı geometriye bağlar.
    _v33_gelistirici_x_skill_efekt_ciz()

    top = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    _v34_special_impact_ring_ciz(top, simdi)
    _v34_special_finish_pulse_ciz(top, simdi)
    ekran.blit(top, (0, 0))
    _v34_special_screen_flash_ciz(simdi)
    _v34_special_cinema_bars_ciz(simdi)
    _v34_special_hit_counter_ciz(simdi)
# </POTBO_STAGE S0672>

# <POTBO_STAGE S0679>
V34_DASH_BUFFER_MS = 150
# </POTBO_STAGE S0679>

# <POTBO_STAGE S0682>
V34_MAX_COMBAT_IMPACTS = 180
# </POTBO_STAGE S0682>

# <POTBO_STAGE S0686>

v34_attack_buffer_until = 0
v34_dash_buffer_until = 0
v34_dash_buffer_direction = pygame.Vector2(0.0, 0.0)
# </POTBO_STAGE S0686>

# <POTBO_STAGE S0689>
v34_input_buffer_attack_count = 0
v34_input_buffer_dash_count = 0


# ---------------------------------------------------------
# SPECIAL RESET HYGIENE
# ---------------------------------------------------------
_v34a_gelistirici_x_skill_sifirla = gelistirici_x_skill_sifirla
# </POTBO_STAGE S0689>

# <POTBO_STAGE S0692>


_v34a_oyuncu_dash_yap = oyuncu_dash_yap


def oyuncu_dash_yap(dx, dy):
    """Attack recovery sırasında dash komutunu kısa süre buffer'lar."""
    global v34_dash_buffer_until, v34_dash_buffer_direction, v34_input_buffer_dash_count
    simdi = pygame.time.get_ticks()
    direction = pygame.Vector2(float(dx), float(dy))
    if direction.length_squared() <= 1e-6:
        return False

    if gelistirici_x_skill_aktif_mi(simdi) or oyuncu_hp <= 0:
        return False

    if oyuncu_saldiriyor and oyuncu_saldiri_modu in (
        "normal",
        "hold_release",
    ):
        v34_dash_buffer_until = max(
            v34_dash_buffer_until,
            int(simdi) + V34_DASH_BUFFER_MS,
        )
        v34_dash_buffer_direction = direction.normalize()
        v34_input_buffer_dash_count += 1
        return False

    ok = _v34a_oyuncu_dash_yap(dx, dy)
    if ok:
        v34_dash_buffer_until = 0
        v34_dash_buffer_direction.update(0.0, 0.0)
    return ok
# </POTBO_STAGE S0692>

# <POTBO_STAGE S0699>


# =========================================================
# END V34B
# =========================================================


# =========================================================
# V34C COMBAT READABILITY / CROWD SEPARATION / SESSION FEEL
# =========================================================
# Amaç yalnız daha fazla efekt değil; oyuncunun neden hasar aldığını, saldırısının
# zincir halinde bağlanıp bağlanmadığını ve kalabalıkta neden sıkıştığını daha iyi
# anlatan sistemik geri bildirimler eklemektir.

V34_COMBO_WINDOW_MS = 1450
V34_COMBO_FADE_MS = 520
V34_DAMAGE_EDGE_MS = 420
V34_DAMAGE_EDGE_STRONG_MS = 150
# </POTBO_STAGE S0699>

# <POTBO_STAGE S0703>
V34_COMBAT_CALM_RESET_MS = 2600

v34_combo_count = 0
v34_combo_damage = 0
v34_combo_last_hit_ms = 0
v34_combo_window_until = 0
v34_combo_fade_until = 0
v34_combo_kill_flash_until = 0
v34_combo_best = 0
v34_combo_serial = 0
v34_damage_feedback_until = 0
v34_damage_feedback_started = 0
v34_damage_feedback_strong_until = 0
v34_damage_feedback_direction = pygame.Vector2(0.0, 1.0)
v34_damage_feedback_profile = ""
v34_damage_feedback_amount = 0
v34_damage_feedback_source = ""
# </POTBO_STAGE S0703>

# <POTBO_STAGE S0707>
v34_last_combat_activity_ms = 0
# </POTBO_STAGE S0707>

# <POTBO_STAGE S0709>
v34_combat_focus = 0.0
v34_combat_focus_last_tick = pygame.time.get_ticks()


def _v34_source_is_player_damage(source):
    if source is None or source == "player":
        return True
    return bool(getattr(source, "is_player_magic", False))


def _v34_combo_register_hit(damage, killed=False):
    global v34_combo_count, v34_combo_damage, v34_combo_last_hit_ms
    global v34_combo_window_until, v34_combo_fade_until, v34_combo_kill_flash_until
    global \
        v34_combo_best, \
        v34_combo_serial, \
        v34_last_combat_activity_ms, \
        v34_last_player_hit_given_ms
    simdi = pygame.time.get_ticks()
    if simdi > v34_combo_window_until:
        v34_combo_count = 0
        v34_combo_damage = 0
        v34_combo_serial += 1
    v34_combo_count += 1
    v34_combo_damage += max(0, int(damage))
    v34_combo_last_hit_ms = simdi
    v34_combo_window_until = simdi + V34_COMBO_WINDOW_MS
    v34_combo_fade_until = v34_combo_window_until + V34_COMBO_FADE_MS
    v34_combo_best = max(v34_combo_best, v34_combo_count)
    if killed:
        v34_combo_kill_flash_until = simdi + 420
    v34_last_combat_activity_ms = simdi
    v34_last_player_hit_given_ms = simdi
# </POTBO_STAGE S0709>

# <POTBO_STAGE S0711>


def _v34_damage_register(source_x, source_y, profile, amount, source_name=""):
    global v34_damage_feedback_until, v34_damage_feedback_started
    global v34_damage_feedback_strong_until, v34_damage_feedback_direction
    global \
        v34_damage_feedback_profile, \
        v34_damage_feedback_amount, \
        v34_damage_feedback_source
    global v34_last_combat_activity_ms, v34_last_player_hit_taken_ms
    simdi = pygame.time.get_ticks()
    source = pygame.Vector2(float(source_x), float(source_y))
    player = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    incoming = source - player
    if incoming.length_squared() <= 1e-6:
        incoming = pygame.Vector2(0.0, -1.0)
    else:
        incoming = incoming.normalize()
    v34_damage_feedback_direction = incoming
    v34_damage_feedback_profile = str(profile or "")
    v34_damage_feedback_amount = max(0, int(amount))
    v34_damage_feedback_source = str(source_name or "")
    v34_damage_feedback_started = simdi
    v34_damage_feedback_until = simdi + V34_DAMAGE_EDGE_MS
    v34_damage_feedback_strong_until = simdi + V34_DAMAGE_EDGE_STRONG_MS
    v34_last_combat_activity_ms = simdi
    v34_last_player_hit_taken_ms = simdi


_v34c_oyuncu_kanli_hasar_kaydi = oyuncu_kanli_hasar_kaydi


def oyuncu_kanli_hasar_kaydi(kaynak_x, kaynak_y, profil, hasar, kaynak_adi=""):
    result = _v34c_oyuncu_kanli_hasar_kaydi(
        kaynak_x, kaynak_y, profil, hasar, kaynak_adi
    )
    if int(hasar) > 0:
        _v34_damage_register(kaynak_x, kaynak_y, profil, hasar, kaynak_adi)
    return result


def _v34_damage_edge_geometry(direction, thickness=20):
    """Incoming world direction'ı ekran kenarı bandına çevirir."""
    d = pygame.Vector2(direction)
    if d.length_squared() <= 1e-6:
        d = pygame.Vector2(0.0, -1.0)
    d = d.normalize()
    # Kaynak oyuncunun sağındaysa sağ kenar yanar; yukarıdaysa üst kenar.
    if abs(d.x) >= abs(d.y):
        if d.x > 0:
            return pygame.Rect(GENISLIK - thickness, 0, thickness, YUKSEKLIK), "right"
        return pygame.Rect(0, 0, thickness, YUKSEKLIK), "left"
    if d.y > 0:
        return pygame.Rect(0, YUKSEKLIK - thickness, GENISLIK, thickness), "bottom"
    return pygame.Rect(0, 0, GENISLIK, thickness), "top"


def _v34_damage_feedback_ciz():
    simdi = pygame.time.get_ticks()
    if simdi >= v34_damage_feedback_until or oyuncu_hp <= 0:
        return
    total = max(
        1,
        v34_damage_feedback_until - v34_damage_feedback_started,
    )
    p = max(
        0.0,
        min(1.0, (simdi - v34_damage_feedback_started) / total),
    )
    fade = (1.0 - p) ** 2
    strong = 1.0 if simdi < v34_damage_feedback_strong_until else 0.58
    amount_scale = min(
        1.0,
        max(
            0.25,
            v34_damage_feedback_amount / max(1.0, float(oyuncu_max_hp) * 0.35),
        ),
    )
    alpha = int((58 + 88 * amount_scale) * fade * strong)
    thickness = int(14 + 22 * amount_scale)
    rect, side = _v34_damage_edge_geometry(v34_damage_feedback_direction, thickness)
    overlay = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    pygame.draw.rect(overlay, (178, 10, 28, alpha), rect)

    # Kenardan içeri doğru ikinci yumuşak band.
    soft = thickness * 3
    if side == "right":
        rect2 = pygame.Rect(GENISLIK - soft, 0, soft, YUKSEKLIK)
    elif side == "left":
        rect2 = pygame.Rect(0, 0, soft, YUKSEKLIK)
    elif side == "bottom":
        rect2 = pygame.Rect(0, YUKSEKLIK - soft, GENISLIK, soft)
    else:
        rect2 = pygame.Rect(0, 0, GENISLIK, soft)
    pygame.draw.rect(overlay, (118, 4, 18, int(alpha * 0.30)), rect2)
    ekran.blit(overlay, (0, 0))
# </POTBO_STAGE S0711>

# <POTBO_STAGE S0713>


def _v34_combat_focus_tick():
    """Savaş yoğunluğunu 0..1 arası düşük geçişli sinyal olarak tutar."""
    global v34_combat_focus, v34_combat_focus_last_tick
    simdi = pygame.time.get_ticks()
    dt = max(
        0.0,
        min(0.08, (simdi - v34_combat_focus_last_tick) / 1000.0),
    )
    v34_combat_focus_last_tick = simdi
    recent = simdi - v34_last_combat_activity_ms < V34_COMBAT_CALM_RESET_MS
    target = 1.0 if recent else 0.0
    speed = 4.8 if target > v34_combat_focus else 1.6
    k = 1.0 - math.exp(-speed * dt)
    v34_combat_focus += (target - v34_combat_focus) * k
    v34_combat_focus = max(0.0, min(1.0, v34_combat_focus))
# </POTBO_STAGE S0713>

# <POTBO_STAGE S0721>


def v34_quality_tick():
    _v34c_quality_tick()
    _v34_combat_focus_tick()
# </POTBO_STAGE S0721>

# <POTBO_STAGE S0736>


def _v34_fix_player_numbers():
    global oyuncu_x, oyuncu_y, oyuncu_hp, oyuncu_mana, oyuncu_stamina
    fixed = False
    if not _v34_value_is_finite(oyuncu_x) or not _v34_value_is_finite(oyuncu_y):
        safe = (
            pygame.Vector2(v34_last_safe_player_pos)
            if v34_last_safe_player_pos is not None
            else pygame.Vector2(175.0, 585.0)
        )
        oyuncu_x = float(safe.x)
        oyuncu_y = float(safe.y)
        _v34_watchdog_note("non-finite player coordinates restored")
        fixed = True
    hp = max(0, min(int(oyuncu_max_hp), int(oyuncu_hp)))
    mana = max(0, min(int(oyuncu_max_mana), int(oyuncu_mana)))
    stamina = max(
        0.0,
        min(float(oyuncu_max_stamina), float(oyuncu_stamina)),
    )
    if hp != oyuncu_hp:
        oyuncu_hp = hp
        fixed = True
    if mana != oyuncu_mana:
        oyuncu_mana = mana
        fixed = True
    if abs(stamina - float(oyuncu_stamina)) > 1e-6:
        oyuncu_stamina = stamina
        fixed = True
    return fixed


def _v34_fix_transient_states(simdi):
    global dash_aktif_bitis, dash_aktif_yonu, dash_aktif_son_ease, dash_tus_kilitli
    global gelistirici_x_skill_r_basildi, v34_attack_buffer_until, v34_dash_buffer_until
    fixed = False
    if dash_aktif_bitis and simdi >= dash_aktif_bitis:
        if dash_aktif_yonu.length_squared() > 0.0 or dash_aktif_son_ease != 0.0:
            dash_aktif_bitis = 0
            dash_aktif_yonu.update(0.0, 0.0)
            dash_aktif_son_ease = 0.0
            fixed = True
    if gelistirici_x_skill_r_basildi:
        valid_arm = (
            gelistirici_x_skill_aktif
            and oyuncu_saldiriyor
            and oyuncu_saldiri_modu == "charge"
            and not gelistirici_x_skill_aktif_mi(simdi)
        )
        if not valid_arm:
            gelistirici_x_skill_r_basildi = False
            fixed = True
    if v34_attack_buffer_until and simdi > v34_attack_buffer_until + 500:
        v34_attack_buffer_until = 0
        fixed = True
    if v34_dash_buffer_until and simdi > v34_dash_buffer_until + 500:
        v34_dash_buffer_until = 0
        v34_dash_buffer_direction.update(0.0, 0.0)
        fixed = True
    return fixed
# </POTBO_STAGE S0736>

# <POTBO_STAGE S0739>


def v34_state_watchdog_tick():
    global v34_watchdog_last_tick, v34_focus_lost_since, v34_focus_recovery_count
    simdi = pygame.time.get_ticks()
    if simdi - v34_watchdog_last_tick < V34_WATCHDOG_INTERVAL_MS:
        return
    v34_watchdog_last_tick = simdi

    focused = True
    try:
        focused = bool(pygame.key.get_focused())
    except pygame.error:
        pass
    if not focused:
        if v34_focus_lost_since <= 0:
            v34_focus_lost_since = simdi
    elif v34_focus_lost_since > 0:
        v34_focus_lost_since = 0
        v34_focus_recovery_count += 1
        # Pencere odağı geri geldiğinde held-state latch'leri bırak. Fiziksel tuşlar
        # bir sonraki frame yeniden okunur; phantom dash/block kalmaz.
        global dash_tus_kilitli
        dash_tus_kilitli = False

    any_fix = False
    any_fix |= _v34_fix_player_numbers()
    any_fix |= _v34_fix_transient_states(simdi)
    any_fix |= _v34_fix_special_linger(simdi)
    any_fix |= _v34_fix_actor_numbers()
    if any_fix:
        _v34_watchdog_note("state invariant repaired")
# </POTBO_STAGE S0739>

# <POTBO_STAGE S0742>


# =========================================================
# END V34D
# =========================================================


# =========================================================
# V34E CINEMATIC ARMOR / INTERACTION RESOLVER / ADAPTIVE FX QUALITY
# =========================================================
# Son kullanıcıya doğrudan hissedilen üç iyileştirme:
# 1) authored special move ölümcül bir dış darbeyle yarıda kesilmez; hasar alınır ama
#    ilk iki slash tamamlanmadan HP 0'a inemez,
# 2) E etkileşimi sabit priority zinciri yerine gerçekten en yakın uygun hedefi seçer,
# 3) uzun savaşlarda FPS düşerse yalnız dekoratif V34 efektleri otomatik hafifler.

V34_SPECIAL_CINEMATIC_ARMOR_END = 0.78
# </POTBO_STAGE S0742>

# <POTBO_STAGE S0744>


def v34_special_cinematic_armor_active(simdi=None):
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if not gelistirici_x_skill_aktif_mi(simdi):
        return False
    elapsed = (int(simdi) - int(gelistirici_x_skill_baslangic_ms)) / max(
        1.0, float(GELISTIRICI_X_SKILL_SURE_MS)
    )
    return 0.0 <= elapsed < V34_SPECIAL_CINEMATIC_ARMOR_END


_v34e_oyuncu_kanli_hasar_kaydi = oyuncu_kanli_hasar_kaydi
# </POTBO_STAGE S0744>

# <POTBO_STAGE S0754>


def _v34_special_speed_lines_ciz(katman, simdi):
    if not gelistirici_x_skill_aktif_mi(simdi) or len(gelistirici_x_skill_yol) < 6:
        return
    elapsed = (simdi - gelistirici_x_skill_baslangic_ms) / max(
        1.0, float(GELISTIRICI_X_SKILL_SURE_MS)
    )
    phase = _v34_special_phase_values(elapsed)
    active_slash = None
    if phase["setup_end"] <= elapsed <= phase["slash1_end"]:
        active_slash = (
            pygame.Vector2(gelistirici_x_skill_yol[2]),
            pygame.Vector2(gelistirici_x_skill_yol[3]),
        )
    elif phase["switch_end"] <= elapsed <= phase["slash2_end"]:
        active_slash = (
            pygame.Vector2(gelistirici_x_skill_yol[4]),
            pygame.Vector2(gelistirici_x_skill_yol[5]),
        )
    if active_slash is None:
        return
    a, b = active_slash
    d = b - a
    if d.length_squared() <= 1e-6:
        return
    d = d.normalize()
    normal = pygame.Vector2(-d.y, d.x)
    center = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    seed = (simdi // 17) + v34_special_move_serial * 101
    rng = random.Random(seed)
    line_count = max(3, int(round(9 * max(0.42, v34_fx_quality))))
    for _ in range(line_count):
        back = rng.uniform(22.0, 86.0)
        side = rng.uniform(-38.0, 38.0)
        length = rng.uniform(18.0, 46.0)
        w0 = center - d * back + normal * side
        w1 = w0 - d * length
        s0 = _v34_world_to_screen_vec(w0, -10.0)
        s1 = _v34_world_to_screen_vec(w1, -10.0)
        alpha = rng.randint(38, 88)
        pygame.draw.line(katman, (248, 222, 228, alpha), s0, s1, 1)
# </POTBO_STAGE S0754>

# <POTBO_STAGE S0783>


def oyuncu_locomotion_durumunu_sifirla():
    _v34f_previous_locomotion_reset()
    _v34f_reset_transient_combat_state(after_load=False)
# </POTBO_STAGE S0783>

# <POTBO_STAGE S0786>


def _v34f_special_target_commit_tick(simdi=None):
    """Authored move boyunca hedefin AI/knockback ile X merkezinden kaçmasını engeller."""
    global v34f_special_target_snap_count, v34_special_effect_center
    if simdi is None:
        simdi = _v34f_now()
    if not gelistirici_x_skill_aktif_mi(simdi):
        return
    target = gelistirici_x_skill_hedef
    if target is None:
        return
    if v34f_special_target_anchor is None:
        _v34f_special_capture_target_anchor()
    if v34f_special_target_anchor is None:
        return

    anchor = pygame.Vector2(v34f_special_target_anchor)
    current = pygame.Vector2(
        _v34f_finite(getattr(target, "x", anchor.x), anchor.x),
        _v34f_finite(getattr(target, "y", anchor.y), anchor.y),
    )
    drift = current.distance_to(anchor)
    if drift > V34F_SPECIAL_TARGET_MAX_DRIFT:
        # Snap yerine güçlü lerp: frame-frame okunduğunda beden "teleport" etmez.
        corrected = current.lerp(anchor, V34F_SPECIAL_TARGET_SNAP_SPEED)
        try:
            target.x = float(corrected.x)
            target.y = float(corrected.y)
            v34f_special_target_snap_count += 1
        except Exception:
            pass
    try:
        target.vx = 0.0
        target.vy = 0.0
        target.attacking = False
        lock_until = int(gelistirici_x_skill_bitis_ms) + V34F_SPECIAL_TARGET_LOCK_PAD_MS
        target.hit_stun_until = max(
            int(getattr(target, "hit_stun_until", 0)),
            lock_until,
        )
        target.recovery_until = max(
            int(getattr(target, "recovery_until", 0)),
            lock_until,
        )
    except Exception:
        pass
    v34_special_effect_center = anchor.copy()


# ---------------------------------------------------------
# SPECIAL INPUT QUARANTINE
# ---------------------------------------------------------
def _v34f_special_input_quarantine(simdi=None):
    """Special aktifken tüm player-driven locomotion kanallarını her frame nötralize eder."""
    global v34f_special_input_quarantine_frames
    global oyuncu_savunuyor, oyuncu_zorlanmis_bitis
    global dash_aktif_bitis, dash_aktif_son_ease, dash_tus_kilitli
    global v34_attack_buffer_until, v34_dash_buffer_until

    if simdi is None:
        simdi = _v34f_now()
    if not gelistirici_x_skill_aktif_mi(simdi):
        return False
    v34f_special_input_quarantine_frames += 1
    oyuncu_hareket_hiz_vektoru.update(0.0, 0.0)
    oyuncu_zorlanmis_hiz.update(0.0, 0.0)
    oyuncu_zorlanmis_bitis = 0
    oyuncu_savunuyor = False
    dash_aktif_bitis = 0
    dash_aktif_son_ease = 0.0
    try:
        dash_aktif_yonu.update(0.0, 0.0)
    except Exception:
        pass
    dash_tus_kilitli = True
    v34_attack_buffer_until = 0
    v34_dash_buffer_until = 0
    v34_dash_buffer_direction.update(0.0, 0.0)
    return True
# </POTBO_STAGE S0786>

# <POTBO_STAGE S0791>


def v34f_special_lifecycle_tick():
    global v34f_special_was_active
    simdi = _v34f_now()
    active = bool(gelistirici_x_skill_aktif_mi(simdi))
    if active and not v34f_special_was_active:
        _v34f_special_started(simdi)
    if active:
        _v34f_special_target_commit_tick(simdi)
        _v34f_special_input_quarantine(simdi)
    if v34f_special_was_active and not active:
        _v34f_special_finished(simdi)
    v34f_special_was_active = active
# </POTBO_STAGE S0791>

# <POTBO_STAGE S0793>


# Special update focus dışındayken body'yi ilerletmez. Regain'de yukarıdaki timeline
# shift nedeniyle kaldığı authored frame'den devam eder.
_v34f_previous_special_update = gelistirici_x_skill_guncelle


def gelistirici_x_skill_guncelle(simdi=None):
    if simdi is None:
        simdi = _v34f_now()
    try:
        focused = bool(pygame.key.get_focused())
    except Exception:
        focused = True
    if gelistirici_x_skill_aktif_mi(simdi) and not focused:
        _v34f_special_input_quarantine(simdi)
        return True
    return _v34f_previous_special_update(simdi)
# </POTBO_STAGE S0793>

# <POTBO_STAGE S0797>


def _v34f_special_vignette_ciz(simdi):
    active = gelistirici_x_skill_aktif_mi(simdi)
    echo_active = bool(v34f_special_echoes) and simdi - v34f_special_finished_ms < 360
    if not active and not echo_active:
        return
    if az_hareket:
        max_alpha = int(V34F_SPECIAL_VIGNETTE_MAX_ALPHA * 0.52)
    else:
        max_alpha = V34F_SPECIAL_VIGNETTE_MAX_ALPHA
    if active:
        p = max(
            0.0,
            min(
                1.0,
                (simdi - gelistirici_x_skill_baslangic_ms)
                / max(1.0, float(GELISTIRICI_X_SKILL_SURE_MS)),
            ),
        )
        envelope = min(1.0, p / 0.12, (1.0 - p) / 0.12 if p > 0.88 else 1.0)
    else:
        envelope = max(
            0.0,
            1.0 - (simdi - v34f_special_finished_ms) / 360.0,
        )
    alpha = int(max_alpha * max(0.0, envelope))
    if alpha <= 0:
        return
    layer = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    # Dört kenardan içeri yumuşak basamaklar; pahalı per-pixel radial shader yok.
    steps = 7
    for i in range(steps):
        k = (steps - i) / steps
        a = int(alpha * k * k * 0.30)
        inset_x = int(i * GENISLIK * 0.018)
        inset_y = int(i * YUKSEKLIK * 0.020)
        rect = pygame.Rect(
            inset_x,
            inset_y,
            GENISLIK - inset_x * 2,
            YUKSEKLIK - inset_y * 2,
        )
        pygame.draw.rect(layer, (0, 0, 0, a), rect, max(2, int(18 * k)))
    ekran.blit(layer, (0, 0))
# </POTBO_STAGE S0797>

# <POTBO_STAGE S0802>


def _v34f_resource_snapshot():
    return {
        "hp": (
            _v34f_finite(oyuncu_hp),
            _v34f_finite(oyuncu_max_hp, 1.0),
        ),
        "mana": (
            _v34f_finite(oyuncu_mana),
            _v34f_finite(oyuncu_max_mana, 1.0),
        ),
        "stamina": (
            _v34f_finite(oyuncu_stamina),
            _v34f_finite(oyuncu_max_stamina, 1.0),
        ),
    }


def _v34f_repair_resource_invariants():
    global oyuncu_hp, oyuncu_max_hp, oyuncu_mana, oyuncu_max_mana
    global oyuncu_stamina, oyuncu_max_stamina, hp_gorunen, mana_gorunen, stamina_gorunen
    fixed = False

    raw_max_hp = _v34f_finite(oyuncu_max_hp, float("nan"))
    raw_max_mana = _v34f_finite(oyuncu_max_mana, float("nan"))
    raw_max_stamina = _v34f_finite(oyuncu_max_stamina, float("nan"))
    max_hp = max(1.0, raw_max_hp if math.isfinite(raw_max_hp) else 1.0)
    max_mana = max(
        0.0,
        raw_max_mana if math.isfinite(raw_max_mana) else 0.0,
    )
    max_stamina = max(
        1.0,
        raw_max_stamina if math.isfinite(raw_max_stamina) else 1.0,
    )
    if not math.isfinite(raw_max_hp) or max_hp != raw_max_hp:
        oyuncu_max_hp = max_hp
        fixed = True
    if not math.isfinite(raw_max_mana) or max_mana != raw_max_mana:
        oyuncu_max_mana = max_mana
        fixed = True
    if not math.isfinite(raw_max_stamina) or max_stamina != raw_max_stamina:
        oyuncu_max_stamina = max_stamina
        fixed = True

    raw_hp = _v34f_finite(oyuncu_hp, float("nan"))
    raw_mana = _v34f_finite(oyuncu_mana, float("nan"))
    raw_stamina = _v34f_finite(oyuncu_stamina, float("nan"))
    hp = _v34f_clamp(
        raw_hp if math.isfinite(raw_hp) else max_hp,
        0.0,
        max_hp * V34F_RESOURCE_OVERFLOW_FACTOR,
    )
    mana = _v34f_clamp(
        raw_mana if math.isfinite(raw_mana) else max_mana,
        0.0,
        max_mana * V34F_RESOURCE_OVERFLOW_FACTOR if max_mana > 0 else 0.0,
    )
    stamina = _v34f_clamp(
        raw_stamina if math.isfinite(raw_stamina) else max_stamina,
        0.0,
        max_stamina * V34F_RESOURCE_OVERFLOW_FACTOR,
    )
    if not math.isfinite(raw_hp) or hp != raw_hp:
        oyuncu_hp = hp
        fixed = True
    if not math.isfinite(raw_mana) or mana != raw_mana:
        oyuncu_mana = mana
        fixed = True
    if not math.isfinite(raw_stamina) or stamina != raw_stamina:
        oyuncu_stamina = stamina
        fixed = True

    # UI interpolant'ları NaN olursa draw math'ini zehirleyebilir; gerçek resource'a döndür.
    if not math.isfinite(_v34f_finite(hp_gorunen, float("nan"))):
        hp_gorunen = float(oyuncu_hp)
        fixed = True
    if not math.isfinite(_v34f_finite(mana_gorunen, float("nan"))):
        mana_gorunen = float(oyuncu_mana)
        fixed = True
    if not math.isfinite(_v34f_finite(stamina_gorunen, float("nan"))):
        stamina_gorunen = float(oyuncu_stamina)
        fixed = True
    if fixed:
        _v34f_report_issue(
            "resource_invariant_repaired",
            "player resources normalized",
            True,
            "warning",
        )
    return fixed


# ---------------------------------------------------------
# SPECIAL PHASE CONTRACT AUDIT
# ---------------------------------------------------------
def _v34f_special_phase_contract():
    try:
        phase = _v34_special_phase_values(0.0)
    except Exception as exc:
        return False, f"phase function failed: {exc}"
    keys = (
        "entry_end",
        "hit1_hold_end",
        "setup_end",
        "slash1_end",
        "hit2_hold_end",
        "switch_end",
        "slash2_end",
        "hit3_hold_end",
        "settle_end",
    )
    values = []
    for key in keys:
        if key not in phase:
            return False, f"missing {key}"
        value = _v34f_finite(phase[key], -1.0)
        values.append(value)
    if any(v <= 0.0 or v >= 1.0 for v in values):
        return False, "phase outside (0,1)"
    if any(values[i] >= values[i + 1] for i in range(len(values) - 1)):
        return False, "phase order is not strictly increasing"
    if GELISTIRICI_X_SKILL_SURE_MS < 900:
        return False, "special duration unexpectedly short"
    return True, "ok"


def _v34f_keybind_contract():
    problems = []
    required = (
        "up",
        "down",
        "left",
        "right",
        "attack",
        "block",
        "interact",
        "dash",
        "pause",
    )
    for action in required:
        if action not in tus_atamalari:
            problems.append("missing:" + action)
            continue
        try:
            value = int(tus_atamalari[action])
        except Exception:
            problems.append("invalid:" + action)
            continue
        if value < 0:
            problems.append("negative:" + action)
    return problems
# </POTBO_STAGE S0802>

# <POTBO_STAGE S0809>


# ---------------------------------------------------------
# PLAYER CONTROL RETURN GUARD
# ---------------------------------------------------------
def _v34f_post_special_control_tick():
    global v34f_post_special_recovery_until, dash_tus_kilitli, oyuncu_savunuyor
    simdi = _v34f_now()
    if v34f_post_special_recovery_until <= 0:
        return
    if simdi < v34f_post_special_recovery_until:
        # Kısa landing recovery sırasında momentum sıfırdır; normal movement input'u
        # gelistirici_x_skill bitince ana loop'a geri dönse bile ilk frame snap üretmez.
        oyuncu_hareket_hiz_vektoru.update(0.0, 0.0)
        oyuncu_savunuyor = False
        return
    v34f_post_special_recovery_until = 0
    try:
        keys = pygame.key.get_pressed()
        if not bool(keys[tus_atamasi("dash")]):
            dash_tus_kilitli = False
    except Exception:
        dash_tus_kilitli = False
    _v34f_special_completion_check()
# </POTBO_STAGE S0809>

# <POTBO_STAGE S0814>

# ---------------------------------------------------------
# MOVEMENT / RANGE RETUNE
# ---------------------------------------------------------
# Normal dash yaklaşık %25 daha uzun; süre çok az uzadığı için hissedilen hız da artar.
DASH_MESAFESI = 140.0
DASH_SURESI_MS = 172
# </POTBO_STAGE S0814>

# <POTBO_STAGE S0817>
GELISTIRICI_X_SKILL_YARI_CAP = 132.0
GELISTIRICI_X_SKILL_TETIK_MENZILI = 450.0
GELISTIRICI_X_SKILL_HASAR_CARPANLARI = (1.05, 1.48, 1.90)
# </POTBO_STAGE S0817>

# <POTBO_STAGE S0827>
v35_hold_dash_distance_scale = 1.0
# </POTBO_STAGE S0827>

# <POTBO_STAGE S0833>
V35_FLOW_DASH_STAMINA_DISCOUNT = 0.055
V35_FLOW_DASH_COOLDOWN_DISCOUNT = 0.035
v35_combat_flow = 0.0
# </POTBO_STAGE S0833>

# <POTBO_STAGE S0835>


def _v35_register_player_melee_hit(amount=1.0):
    global v35_combat_flow, v35_flow_last_hit_ms, v35_flow_last_decay_ms
    global v35_flow_pulse_until, v35_flow_best, v35_flow_hits
    simdi = pygame.time.get_ticks()
    if simdi - v35_flow_last_hit_ms > V35_FLOW_WINDOW_MS:
        v35_combat_flow = 0.0
    v35_combat_flow = min(V35_FLOW_MAX, v35_combat_flow + max(0.25, float(amount)))
    v35_flow_last_hit_ms = simdi
    v35_flow_last_decay_ms = simdi
    v35_flow_pulse_until = simdi + 160
    v35_flow_best = max(v35_flow_best, v35_combat_flow)
    v35_flow_hits += 1


def v35_combat_flow_tick():
    global v35_combat_flow, v35_flow_last_decay_ms
    if v35_combat_flow <= 0.0:
        return
    simdi = pygame.time.get_ticks()
    if simdi - v35_flow_last_hit_ms <= V35_FLOW_WINDOW_MS:
        return
    if v35_flow_last_decay_ms <= 0:
        v35_flow_last_decay_ms = simdi
    steps = (simdi - v35_flow_last_decay_ms) // V35_FLOW_DECAY_STEP_MS
    if steps <= 0:
        return
    v35_combat_flow = max(0.0, v35_combat_flow - float(steps))
    v35_flow_last_decay_ms += int(steps) * V35_FLOW_DECAY_STEP_MS
# </POTBO_STAGE S0835>

# <POTBO_STAGE S0837>


_v35_dash_yap_original = oyuncu_dash_yap


def oyuncu_dash_yap(dx, dy):
    """Flow yalnız stamina/cooldown ekonomisini hafifçe rahatlatır; mesafe taban V35'tir."""
    global oyuncu_stamina, son_dash_zamani
    before_stamina = float(oyuncu_stamina)
    ok = _v35_dash_yap_original(dx, dy)
    if not ok:
        return False
    flow = max(0.0, min(V35_FLOW_MAX, float(v35_combat_flow)))
    if flow > 0.0:
        spent = max(0.0, before_stamina - float(oyuncu_stamina))
        refund = spent * min(0.20, flow * V35_FLOW_DASH_STAMINA_DISCOUNT)
        oyuncu_stamina = min(
            float(oyuncu_max_stamina),
            float(oyuncu_stamina) + refund,
        )
        cooldown_credit = int(
            DASH_BEKLEME_SURESI * min(0.11, flow * V35_FLOW_DASH_COOLDOWN_DISCOUNT)
        )
        son_dash_zamani = max(-10000, int(son_dash_zamani) - cooldown_credit)
    return True
# </POTBO_STAGE S0837>

# <POTBO_STAGE S0841>


def _v35_special_motion_direction(simdi):
    if not gelistirici_x_skill_aktif_mi(simdi) or len(gelistirici_x_skill_yol) < 6:
        return pygame.Vector2(0.0, 0.0)
    p = max(
        0.0,
        min(
            1.0,
            (simdi - gelistirici_x_skill_baslangic_ms)
            / max(1.0, float(GELISTIRICI_X_SKILL_SURE_MS)),
        ),
    )
    path = [pygame.Vector2(v) for v in gelistirici_x_skill_yol]
    phase = _v34_special_phase_values(p)
    if p < phase["entry_end"]:
        return path[1] - path[0]
    if phase["setup_end"] <= p < phase["slash1_end"]:
        return path[3] - path[2]
    if phase["switch_end"] <= p < phase["slash2_end"]:
        return path[5] - path[4]
    return pygame.Vector2(0.0, 0.0)
# </POTBO_STAGE S0841>

# <POTBO_STAGE S0849>


def v34_quality_tick():
    _v35_quality_tick_original()
    v35_combat_flow_tick()
# </POTBO_STAGE S0849>

# <POTBO_STAGE S0860>


def _v36_special_phase_progress(simdi, start_key, end_key):
    if gelistirici_x_skill_baslangic_ms <= 0:
        return 0.0
    p = (int(simdi) - int(gelistirici_x_skill_baslangic_ms)) / max(
        1.0, float(GELISTIRICI_X_SKILL_SURE_MS)
    )
    phase = _v34_special_phase_values(p)
    a = float(phase[start_key])
    b = float(phase[end_key])
    raw = max(0.0, min(1.0, (p - a) / max(0.001, b - a)))
    return 1.0 - (1.0 - raw) ** 3
# </POTBO_STAGE S0860>

# <POTBO_STAGE S0896>


def _v34_damage_feedback_ciz():
    now = pygame.time.get_ticks()
    if now >= v34_damage_feedback_until or oyuncu_hp <= 0:
        return
    total = max(
        1,
        v34_damage_feedback_until - v34_damage_feedback_started,
    )
    p = max(
        0.0,
        min(1.0, (now - v34_damage_feedback_started) / total),
    )
    fade = (1.0 - p) ** 2
    strong = 1.0 if now < v34_damage_feedback_strong_until else 0.58
    amount_scale = min(
        1.0,
        max(
            0.25,
            v34_damage_feedback_amount / max(1.0, float(oyuncu_max_hp) * 0.35),
        ),
    )
    alpha = int((58 + 88 * amount_scale) * fade * strong)
    thickness = int(14 + 22 * amount_scale)
    _, side = _v34_damage_edge_geometry(v34_damage_feedback_direction, thickness)
    soft = max(thickness + 2, thickness * 3)

    if side in ("left", "right"):
        layer = pygame.Surface((soft, YUKSEKLIK), pygame.SRCALPHA)
        if side == "left":
            pygame.draw.rect(
                layer,
                (178, 10, 28, alpha),
                (0, 0, thickness, YUKSEKLIK),
            )
            pygame.draw.rect(
                layer,
                (118, 4, 18, int(alpha * 0.30)),
                (0, 0, soft, YUKSEKLIK),
            )
            pos = (0, 0)
        else:
            pygame.draw.rect(
                layer,
                (178, 10, 28, alpha),
                (soft - thickness, 0, thickness, YUKSEKLIK),
            )
            pygame.draw.rect(
                layer,
                (118, 4, 18, int(alpha * 0.30)),
                (0, 0, soft, YUKSEKLIK),
            )
            pos = (GENISLIK - soft, 0)
    else:
        layer = pygame.Surface((GENISLIK, soft), pygame.SRCALPHA)
        if side == "top":
            pygame.draw.rect(
                layer,
                (178, 10, 28, alpha),
                (0, 0, GENISLIK, thickness),
            )
            pygame.draw.rect(
                layer,
                (118, 4, 18, int(alpha * 0.30)),
                (0, 0, GENISLIK, soft),
            )
            pos = (0, 0)
        else:
            pygame.draw.rect(
                layer,
                (178, 10, 28, alpha),
                (0, soft - thickness, GENISLIK, thickness),
            )
            pygame.draw.rect(
                layer,
                (118, 4, 18, int(alpha * 0.30)),
                (0, 0, GENISLIK, soft),
            )
            pos = (0, YUKSEKLIK - soft)
    ekran.blit(layer, pos)
# </POTBO_STAGE S0896>

# <POTBO_STAGE S0901>
V34_MAX_COMBAT_IMPACTS = 72
# </POTBO_STAGE S0901>

# <POTBO_STAGE S0911>
v37_special_damage_context = False
# </POTBO_STAGE S0911>

# <POTBO_STAGE S0914>


_v37_special_hit_original = _gelistirici_x_skill_vur


def _gelistirici_x_skill_vur(slot, yon=None):
    global v37_special_damage_context
    once = v37_special_damage_context
    v37_special_damage_context = True
    try:
        return _v37_special_hit_original(slot, yon)
    finally:
        v37_special_damage_context = once
# </POTBO_STAGE S0914>

# <POTBO_STAGE S0924>


def _v34_player_safety_tick():
    # Path preflight + sparse sanity check special sırasında yeterlidir.
    if gelistirici_x_skill_aktif_mi():
        return
    return _v37_player_safety_tick_original()


_v37_stamina_guncelle_original = stamina_guncelle


def stamina_guncelle():
    # Authored control-lock sırasında stamina regen/cost timeline'a gizlice karışmasın.
    if gelistirici_x_skill_aktif_mi():
        return
    return _v37_stamina_guncelle_original()
# </POTBO_STAGE S0924>

# <POTBO_STAGE S0928>


def v34_crowd_separation_tick():
    if gelistirici_x_skill_aktif_mi():
        return
    return _v37_crowd_separation_original()
# </POTBO_STAGE S0928>

# <POTBO_STAGE S0930>


def v34_state_watchdog_tick():
    if gelistirici_x_skill_aktif_mi():
        return
    return _v37_state_watchdog_original()
# </POTBO_STAGE S0930>

# <POTBO_STAGE S0932>


def v34f_runtime_audit_tick(force=False):
    if gelistirici_x_skill_aktif_mi() and not force:
        return dict(v34f_audit_last_summary)
    return _v37_runtime_audit_original(force)


def v34_quality_tick():
    """V37 tek kalite orkestratörü.

    Önceki V34C/D/E/F/V35 wrapper zincirini tek fonksiyonda aynı sırayla yürütür.
    Böylece aynı frame'de birden fazla wrapper katmanının birbirine dolanması önlenir.
    """
    global v37_special_previous_active

    # V34B temel oturum işleri.
    v34_special_pause_tick()
    v34_input_buffer_guncelle()
    v34_fx_budget_guncelle()

    # V34C-D-E combat/readability güvenlikleri.
    _v34_combat_focus_tick()
    v34_state_watchdog_tick()
    v34_fx_quality_tick()

    # V34F session hardening. V37 wrapper'ları special sırasında pahalı auditleri zaten erteler.
    v34f_frame_health_tick()
    v34f_focus_safety_tick()
    v34f_special_lifecycle_tick()
    _v34f_post_special_control_tick()
    v34f_runtime_audit_tick(False)

    # V35 combat flow en son çözülür; böylece bu frame'deki hit/state bilgisi günceldir.
    v35_combat_flow_tick()

    now = pygame.time.get_ticks()
    active = gelistirici_x_skill_aktif_mi(now)
    if v37_special_previous_active and not active:
        # AI authored sequence bittikten aynı frame'de oyuncunun üstüne saldırmasın.
        grace = now + V37_SPECIAL_AI_RECOVERY_MS
        for actor in _v34_actor_list():
            try:
                actor.recovery_until = max(
                    int(getattr(actor, "recovery_until", 0)),
                    grace,
                )
                actor.hit_stun_until = max(
                    int(getattr(actor, "hit_stun_until", 0)),
                    now + 55,
                )
                actor.attacking = False
            except Exception:
                pass
    v37_special_previous_active = bool(active)
# </POTBO_STAGE S0932>

# <POTBO_STAGE S0936>
v38_combat_precision = "strict"  # strict | standard
v38_fire_self_damage = True
# </POTBO_STAGE S0936>

# <POTBO_STAGE S0939>
V38_COMBAT_PRECISIONS = ("strict", "standard")
# </POTBO_STAGE S0939>

# <POTBO_STAGE S0949>

# Normal kullanım mana odaklıdır; tüm stamina'yı sıfırlamak kaldırıldı.
V38_FIRE_CAST_STAMINA_COST = 10.0
# </POTBO_STAGE S0949>

# <POTBO_STAGE S0951>
V38_FIRE_DAMAGE_PRESSURE = 510.0
V38_FIRE_DAMAGE_THERMAL = 155.0
V38_FIRE_DAMAGE_RADIUS = 214.0
# </POTBO_STAGE S0951>

# <POTBO_STAGE S0954>

# Owner safety: kendi patlaması yalnız gerçekten yakınsa hissedilir.
V38_FIRE_SELF_DAMAGE_RADIUS = 118.0
# </POTBO_STAGE S0954>

# <POTBO_STAGE S0956>
V38_FIRE_SELF_DAMAGE_SCALE = 0.31
V38_FIRE_SELF_DAMAGE_MAX_HP_FRACTION = 0.58
# </POTBO_STAGE S0956>

# <POTBO_STAGE S0958>
V38_FIRE_SELF_MIN_DAMAGE = 2
# </POTBO_STAGE S0958>

# <POTBO_STAGE S0963>


def _v38_knockback_at(distance, exposure=1.0):
    d = max(0.0, float(distance))
    if d > V38_FIRE_DAMAGE_RADIUS:
        return 0.0
    p = _v38_pressure_field(d)
    e = _v38_clamp01(exposure)
    return V38_FIRE_KNOCKBACK_BASE * (p**0.72) * (0.22 + 0.78 * e)
# </POTBO_STAGE S0963>

# <POTBO_STAGE S0966>


def _v38_self_burn_at(distance, exposure=1.0):
    if not v38_fire_self_damage or not gelistirici_yanma_efekti_aktif:
        return 0
    d = max(0.0, float(distance))
    if d > V38_FIRE_SELF_BURN_RADIUS:
        return 0
    return int(round(_v38_burn_total_at(d, exposure) * V38_FIRE_SELF_BURN_SCALE))
# </POTBO_STAGE S0966>

# <POTBO_STAGE S0982>


def _v38_player_reach_values():
    strict = v38_combat_precision == "strict"
    if strict:
        return (
            V38_PLAYER_NORMAL_REACH_STRICT,
            V38_PLAYER_NORMAL_WIDTH_STRICT,
            V38_PLAYER_HEAVY_REACH_STRICT,
            V38_PLAYER_HEAVY_WIDTH_STRICT,
        )
    return (
        V38_PLAYER_NORMAL_REACH_STANDARD,
        V38_PLAYER_NORMAL_WIDTH_STANDARD,
        V38_PLAYER_HEAVY_REACH_STANDARD,
        V38_PLAYER_HEAVY_WIDTH_STANDARD,
    )
# </POTBO_STAGE S0982>

# <POTBO_STAGE S0985>


# ---------------------------------------------------------
# SPECIAL: FASTER SMOOTHER TIMELINE + 3 PHYSICAL STAMINA COSTS
# ---------------------------------------------------------
GELISTIRICI_X_SKILL_SURE_MS = 1360
GELISTIRICI_X_SKILL_YARI_CAP = 132.0
GELISTIRICI_X_SKILL_TETIK_MENZILI = 450.0
# </POTBO_STAGE S0985>

# <POTBO_STAGE S0988>

V38_SPECIAL_STAMINA_PER_HIT = 18.0
V38_SPECIAL_TOTAL_STAMINA = V38_SPECIAL_STAMINA_PER_HIT * 3.0
# </POTBO_STAGE S0988>

# <POTBO_STAGE S0991>
v38_special_stamina_paid_mask = 0
v38_special_stamina_start = 0.0
v38_special_stamina_spent = 0.0


def _gelistirici_x_skill_ease_out(t):
    """Symmetric rational S-curve: smooth endpoints, fast middle transit.

    f(t)=t²/(t²+(1-t)²). İlk/son türev yumuşak, orta bölge hızlıdır; authored dash
    teleport gibi başlamaz fakat cubic ease-out kadar uzun kuyruk bırakmaz.
    """
    t = _v38_clamp01(t)
    a = t * t
    b = (1.0 - t) * (1.0 - t)
    return a / max(1e-9, a + b)
# </POTBO_STAGE S0991>

# <POTBO_STAGE S0993>


_v38_special_r_arm_original = gelistirici_x_skill_r_baslat
_v38_special_r_release_original = gelistirici_x_skill_r_birak
_v38_special_hit_original = _gelistirici_x_skill_vur
_v38_special_reset_original = gelistirici_x_skill_sifirla
# </POTBO_STAGE S0993>

# <POTBO_STAGE S0995>


def gelistirici_x_skill_r_birak(simdi=None):
    """Start başarısız olursa refund exploit olmasın; normal hold maliyeti geri yazılır."""
    global oyuncu_stamina, v38_special_arm_refund_active
    if simdi is None:
        simdi = pygame.time.get_ticks()
    ok = _v38_special_r_release_original(simdi)
    if ok:
        v38_special_arm_refund_active = False
        return True
    if v38_special_arm_refund_active:
        oyuncu_stamina = max(0.0, float(oyuncu_stamina) - V38_SPECIAL_PREP_REFUND)
        v38_special_arm_refund_active = False
    return False


def _v38_special_pay_hit(slot, simdi):
    global oyuncu_stamina, stamina_son_harcama
    global v38_special_stamina_paid_mask, v38_special_stamina_spent
    slot = max(0, min(2, int(slot)))
    bit = 1 << slot
    if v38_special_stamina_paid_mask & bit:
        return 0.0
    cost = min(
        float(V38_SPECIAL_STAMINA_PER_HIT),
        max(0.0, float(oyuncu_stamina)),
    )
    oyuncu_stamina = max(0.0, float(oyuncu_stamina) - cost)
    stamina_son_harcama = int(simdi)
    v38_special_stamina_paid_mask |= bit
    v38_special_stamina_spent += cost
    return cost
# </POTBO_STAGE S0995>

# <POTBO_STAGE S0997>


def gelistirici_x_skill_sifirla(tam_reset=False):
    global v38_special_arm_refund_active, v38_special_stamina_paid_mask
    global v38_special_stamina_spent
    # Arm edilmiş fakat start edilmemiş state başka bir modal/reset ile kesildiyse
    # refund normal hold maliyetini bedavaya çevirmesin.
    global oyuncu_stamina
    if v38_special_arm_refund_active and not gelistirici_x_skill_aktif_mi():
        oyuncu_stamina = max(0.0, float(oyuncu_stamina) - V38_SPECIAL_PREP_REFUND)
    v38_special_arm_refund_active = False
    _v38_special_reset_original(tam_reset)
    if tam_reset:
        v38_special_stamina_paid_mask = 0
        v38_special_stamina_spent = 0.0
# </POTBO_STAGE S0997>

# <POTBO_STAGE S1000>


# ---------------------------------------------------------
# THERMAL COLOR / MATERIAL RESPONSE
# ---------------------------------------------------------
# Ateşin "bilimsel" görünmesi yalnız hasar eğrisinden ibaret değildir. Aşağıdaki
# dönüşüm yaklaşık black-body renk sıcaklığı üretir. Bu Planck integralini her frame
# çözmek yerine Tanner-Helland tipi log/power yaklaşımının oyun için sadeleştirilmiş
# biçimidir. Sonuç yalnız glow tonuna gider; sprite atlasının orijinal rengini bozmaz.


def _v38_blackbody_rgb(temp_k):
    t = max(1000.0, min(40000.0, float(temp_k))) / 100.0
    if t <= 66.0:
        r = 255.0
        g = 99.4708025861 * math.log(max(1.0, t)) - 161.1195681661
        if t <= 19.0:
            b = 0.0
        else:
            b = 138.5177312231 * math.log(max(1.0, t - 10.0)) - 305.0447927307
    else:
        r = 329.698727446 * ((t - 60.0) ** -0.1332047592)
        g = 288.1221695283 * ((t - 60.0) ** -0.0755148492)
        b = 255.0
    return (
        max(0, min(255, int(round(r)))),
        max(0, min(255, int(round(g)))),
        max(0, min(255, int(round(b)))),
    )
# </POTBO_STAGE S1000>

# <POTBO_STAGE S1006>


# Temperature-aware glow cache. Projectile calls two-argument helper in the earlier
# V38 block; this redefinition keeps that signature and derives temperature bucket from
# intensity. It is deliberately quantized so cache cardinality stays tiny.
def _v38_glow_surface(radius, intensity_bucket):
    radius = max(4, int(radius))
    bucket = max(0, min(10, int(intensity_bucket)))
    temp_bucket = max(0, min(7, int(round(bucket * 0.7))))
    key = (radius, bucket, temp_bucket)
    cached = v38_fire_glow_cache.get(key)
    if cached is not None:
        return cached
    size = radius * 2 + 8
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    c = size // 2
    strength = bucket / 10.0
    rgb = _v38_blackbody_rgb(_v38_temperature_from_bucket(temp_bucket))
    # Dış katmanda turuncu/kırmızı baskın, çekirdekte RGB black-body tonuna yaklaşır.
    for i, frac in enumerate((1.0, 0.72, 0.46, 0.24)):
        rr = max(1, int(radius * frac))
        mix = i / 3.0
        color = (
            int(round(255 * (1.0 - mix) + rgb[0] * mix)),
            int(round(62 * (1.0 - mix) + rgb[1] * mix)),
            int(round(8 * (1.0 - mix) + rgb[2] * mix)),
        )
        alpha = int((10 + 40 * strength) * (1.0 - i * 0.13))
        pygame.draw.circle(surf, (*color, alpha), (c, c), rr)
    v38_fire_glow_cache[key] = surf
    _v38_cache_limit(v38_fire_glow_cache, 96)
    return surf
# </POTBO_STAGE S1006>

# <POTBO_STAGE S1010>


# ---------------------------------------------------------
# FIRE QUALITY PRESETS
# ---------------------------------------------------------
# Quality ayarı mekanik sistemlere dokunmaz. Buradaki değerler yalnız render/spawn
# yoğunluğunu belirler; aynı save üç profilde de aynı damage/position sonucunu üretir.
V38_FIRE_QUALITY_PRESETS = {
    "low": {
        "density": 0.55,
        "projectile_ghosts": 1,
        "ground_fire_scale": 0.65,
        "pressure_ring": False,
        "thermal_glow": True,
        "cache_limit": 72,
    },
    "balanced": {
        "density": 1.00,
        "projectile_ghosts": 2,
        "ground_fire_scale": 1.00,
        "pressure_ring": True,
        "thermal_glow": True,
        "cache_limit": 96,
    },
    "high": {
        "density": 1.35,
        "projectile_ghosts": 3,
        "ground_fire_scale": 1.25,
        "pressure_ring": True,
        "thermal_glow": True,
        "cache_limit": 128,
    },
}
# </POTBO_STAGE S1010>

# <POTBO_STAGE S1013>


def v38_special_stamina_contract():
    return {
        "per_hit": V38_SPECIAL_STAMINA_PER_HIT,
        "total": V38_SPECIAL_TOTAL_STAMINA,
        "prep_refund": V38_SPECIAL_PREP_REFUND,
        "three_equal": abs(
            V38_SPECIAL_TOTAL_STAMINA - 3.0 * V38_SPECIAL_STAMINA_PER_HIT
        )
        < 1e-6,
        "affordable_at_default_max": V38_SPECIAL_TOTAL_STAMINA <= 100.0,
        "more_than_one_normal_attack": V38_SPECIAL_TOTAL_STAMINA
        > SALDIRI_STAMINA_MALIYETI,
        "less_than_two_full_dashes": V38_SPECIAL_TOTAL_STAMINA
        < DASH_STAMINA_MALIYETI * 2.0,
    }
# </POTBO_STAGE S1013>

# <POTBO_STAGE S1021>


def _v38_special_contract():
    phases = _v34_special_phase_values(0.5)
    ordered = [
        phases["entry_end"],
        phases["hit1_hold_end"],
        phases["setup_end"],
        phases["slash1_end"],
        phases["hit2_hold_end"],
        phases["switch_end"],
        phases["slash2_end"],
        phases["hit3_hold_end"],
        phases["settle_end"],
    ]
    return {
        "ordered": all(ordered[i] < ordered[i + 1] for i in range(len(ordered) - 1)),
        "inside_unit_interval": ordered[0] > 0.0 and ordered[-1] < 1.0,
        "three_equal_costs": abs(
            V38_SPECIAL_TOTAL_STAMINA - V38_SPECIAL_STAMINA_PER_HIT * 3.0
        )
        < 1e-6,
        "duration_fast": 1050 <= GELISTIRICI_X_SKILL_SURE_MS <= 1500,
    }
# </POTBO_STAGE S1021>

# <POTBO_STAGE S1024>


V38_TUNING_GETTERS = {
    "V38_FIRE_CORE_TEMPERATURE_K": lambda: V38_FIRE_CORE_TEMPERATURE_K,
    "V38_FIRE_THERMAL_COOLING_K": lambda: V38_FIRE_THERMAL_COOLING_K,
    "V38_FIRE_PROJECTILE_V0": lambda: V38_FIRE_PROJECTILE_V0,
    "V38_FIRE_PROJECTILE_VINF": lambda: V38_FIRE_PROJECTILE_VINF,
    "V38_FIRE_PROJECTILE_DRAG_K": lambda: V38_FIRE_PROJECTILE_DRAG_K,
    "V38_FIRE_PROJECTILE_MAX_TRAVEL": lambda: V38_FIRE_PROJECTILE_MAX_TRAVEL,
    "V38_FIRE_PROJECTILE_TTL_MS": lambda: V38_FIRE_PROJECTILE_TTL_MS,
    "V38_FIRE_PROJECTILE_RADIUS": lambda: V38_FIRE_PROJECTILE_RADIUS,
    "V38_FIRE_PRESSURE_SIGMA": lambda: V38_FIRE_PRESSURE_SIGMA,
    "V38_FIRE_THERMAL_R50": lambda: V38_FIRE_THERMAL_R50,
    "V38_FIRE_DAMAGE_PRESSURE": lambda: V38_FIRE_DAMAGE_PRESSURE,
    "V38_FIRE_DAMAGE_THERMAL": lambda: V38_FIRE_DAMAGE_THERMAL,
    "V38_FIRE_DAMAGE_RADIUS": lambda: V38_FIRE_DAMAGE_RADIUS,
    "V38_FIRE_THERMAL_RADIUS": lambda: V38_FIRE_THERMAL_RADIUS,
    "V38_FIRE_KNOCKBACK_BASE": lambda: V38_FIRE_KNOCKBACK_BASE,
    "V38_FIRE_BURN_BASE": lambda: V38_FIRE_BURN_BASE,
    "V38_FIRE_SELF_DAMAGE_RADIUS": lambda: V38_FIRE_SELF_DAMAGE_RADIUS,
    "V38_FIRE_SELF_DAMAGE_SCALE": lambda: V38_FIRE_SELF_DAMAGE_SCALE,
    "V38_FIRE_SELF_DAMAGE_MAX_HP_FRACTION": lambda: V38_FIRE_SELF_DAMAGE_MAX_HP_FRACTION,
    "V38_FIRE_SELF_BURN_RADIUS": lambda: V38_FIRE_SELF_BURN_RADIUS,
    "V38_FIRE_CAST_STAMINA_COST": lambda: V38_FIRE_CAST_STAMINA_COST,
    "V38_PLAYER_NORMAL_REACH_STRICT": lambda: V38_PLAYER_NORMAL_REACH_STRICT,
    "V38_PLAYER_HEAVY_REACH_STRICT": lambda: V38_PLAYER_HEAVY_REACH_STRICT,
    "GELISTIRICI_X_SKILL_SURE_MS": lambda: GELISTIRICI_X_SKILL_SURE_MS,
    "V38_SPECIAL_STAMINA_PER_HIT": lambda: V38_SPECIAL_STAMINA_PER_HIT,
}
# </POTBO_STAGE S1024>

# <POTBO_STAGE S1030>


def v38_diagnostics():
    data = _v38_diagnostics_base()
    section = data.setdefault("v38", {})
    section["equation_catalog"] = v38_equation_catalog_validate()
    section["material_summary"] = v38_runtime_balance_summary()
    section["contact_contract"] = v38_contact_contract()
    section["special_stamina_contract"] = v38_special_stamina_contract()
    section["tuning_bounds_ok"] = v38_tuning_bounds_ok()
    section["cross_system_ok"] = v38_cross_system_ok()
    return data


# ---------------------------------------------------------
# SPECIAL ARM AFFORDABILITY FINAL GUARD
# ---------------------------------------------------------
# R basıldığı frame press->charge geçişi de gerçekleşebildiği için ilk precheck'te
# hold ek maliyetinin henüz düşülmemiş olması olasıdır. Bu son guard refund sonrasında
# gerçek kullanılabilir stamina'yı tekrar doğrular; böylece 54 stamina kontratı kesin.
_v38_special_r_arm_stage1 = gelistirici_x_skill_r_baslat
# </POTBO_STAGE S1030>

# <POTBO_STAGE S1033>

# ---------------------------------------------------------
# HUMAN-READABLE REFERENCE CURVES
# ---------------------------------------------------------
# Bu küçük tablo debug/denge notudur; runtime combat kararında kullanılmaz. Sayılar
# fonksiyonlardan üretildiği için formül değişirse tablo elle güncellenmek zorunda değildir.
V38_REFERENCE_DISTANCES = (
    0.0,
    24.0,
    48.0,
    72.0,
    96.0,
    120.0,
    144.0,
    168.0,
    192.0,
    214.0,
)
# </POTBO_STAGE S1033>

# <POTBO_STAGE S1035>


def v38_reference_interpretation():
    return {
        "0-48": bt(
            "Basınç çekirdeği: ağır doğrudan hasar ve belirgin impulse.",
            "Pressure core: heavy direct damage and strong impulse.",
        ),
        "48-96": bt(
            "İç cephe: basınç hızla düşerken ısıl doz hâlâ yüksektir.",
            "Inner front: pressure falls quickly while thermal dose remains high.",
        ),
        "96-144": bt(
            "Isıl kuşak: doğrudan hasar azalır; burn göreli olarak önem kazanır.",
            "Thermal band: direct damage declines; burn becomes relatively more important.",
        ),
        "144-214": bt(
            "Dış kuyruk: yalnız düşük artık etki; kendi oyuncu hasarı çoktan sıfırdır.",
            "Outer tail: only low residual effect; owner damage is already zero.",
        ),
        "214+": bt(
            "Mekanik blast hasarı yok; yalnız görsel efekt veya zemin yangını kalabilir.",
            "No mechanical blast damage; only visuals or residual ground fire may remain.",
        ),
    }
# </POTBO_STAGE S1035>

# <POTBO_STAGE S1037>


# Final sanity flags. Bunların herhangi biri False ise dosya açılmayı yine sürdürür;
# geliştirici diagnostics üzerinden hangi varsayımın kırıldığını görebilir.
V38_REFERENCE_OK = (
    len(V38_REFERENCE_CURVES) == len(V38_REFERENCE_DISTANCES)
    and V38_REFERENCE_CURVES[0]["generic_damage"]
    > V38_REFERENCE_CURVES[-1]["generic_damage"]
    and V38_REFERENCE_CURVES[0]["pressure"] > V38_REFERENCE_CURVES[-1]["pressure"]
    and V38_REFERENCE_CURVES[0]["thermal"] > V38_REFERENCE_CURVES[-1]["thermal"]
)
# </POTBO_STAGE S1037>

# <POTBO_STAGE S1039>


# V38 final build metadata.
V38_BUILD_PROFILE = {
    "focus": "thermochemical_fire_and_contact_integrity",
    "line_target": 35000,
    "fire_model": "continuous_pressure_plus_thermal",
    "projectile_model": "exponential_drag_and_cooling",
    "melee_model": "strict_capsule_contact",
    "special_model": "three_physical_dash_hits",
    "special_stamina_model": "18x3_on_contact",
    "owner_fire_model": "short_radius_bounded_self_damage",
    "optimization": "cached_fire_surfaces_and_bounded_transients",
}
# </POTBO_STAGE S1039>

# <POTBO_STAGE S1041>


# =========================================================
# END V38
# =========================================================


# =========================================================
# V39 - FIRE VISUAL / CHARACTER SELECT / COMBAT FEEL
# =========================================================
V39_VERSION = "39.0"
# </POTBO_STAGE S1041>

# <POTBO_STAGE S1045>
saldiri_suresi = 368
saldiri_bekleme_suresi = 430
# </POTBO_STAGE S1045>

# <POTBO_STAGE S1056>


def yeni_oyun_baslat(loadinge_gec=True):
    global oyuncu_level, oyuncu_guc, oyuncu_hasari
    global oyuncu_hp, oyuncu_max_hp, oyuncu_mana, oyuncu_max_mana
    global oyuncu_stamina, oyuncu_max_stamina
    global stamina_gorunen, mana_gorunen, hp_gorunen
    ok = _v39_yeni_oyun_baslat_original(loadinge_gec)
    if not ok:
        return False
    sig = v39_character_signature()
    oyuncu_max_hp += sig["vigor"] * 2
    oyuncu_hp = oyuncu_max_hp
    oyuncu_max_mana += sig["focus"] * 2
    oyuncu_mana = oyuncu_max_mana
    oyuncu_max_stamina += sig["poise"] * 1.6
    oyuncu_stamina = oyuncu_max_stamina
    oyuncu_hasari += max(1, sig["power"] // 3)
    oyuncu_guc += max(0, sig["power"] // 4)
    stamina_gorunen = float(oyuncu_stamina)
    mana_gorunen = float(oyuncu_mana)
    hp_gorunen = float(oyuncu_hp)
    return True
# </POTBO_STAGE S1056>

# <POTBO_STAGE S1058>


def oyuncu_seviye_kazanclarini_uygula(eski_level, yeni_level):
    global oyuncu_hp, oyuncu_max_hp, oyuncu_mana, oyuncu_max_mana
    global oyuncu_stamina, oyuncu_max_stamina, oyuncu_hasari
    _v39_level_gain_original(eski_level, yeni_level)
    fark = max(0, int(yeni_level) - int(eski_level))
    if fark <= 0:
        return
    sig = v39_character_signature()
    hp_artis = fark * max(1, sig["vigor"] // 2)
    mana_artis = fark * max(1, sig["focus"] // 3)
    stamina_artis = fark * (0.55 + sig["poise"] * 0.08)
    power_artis = fark * (0.20 + sig["power"] * 0.04)
    oyuncu_max_hp += hp_artis
    oyuncu_hp = min(oyuncu_max_hp, oyuncu_hp + hp_artis)
    oyuncu_max_mana += mana_artis
    oyuncu_mana = min(oyuncu_max_mana, oyuncu_mana + mana_artis)
    oyuncu_max_stamina += stamina_artis
    oyuncu_stamina = min(oyuncu_max_stamina, oyuncu_stamina + stamina_artis)
    oyuncu_hasari += int(round(power_artis))
# </POTBO_STAGE S1058>

# <POTBO_STAGE S1061>
_v39_stamina_guncelle_original = stamina_guncelle


def stamina_guncelle():
    global oyuncu_stamina, oyuncu_mana
    global stamina_gorunen, mana_gorunen, hp_gorunen, _v39_resource_tick_ms
    once = int(_v39_resource_tick_ms)
    simdi = pygame.time.get_ticks()
    dt = max(0.0, min(0.05, (simdi - once) / 1000.0))
    _v39_resource_tick_ms = simdi
    _v39_stamina_guncelle_original()
    if dt <= 0.0:
        return
    sig = v39_character_signature()
    if not oyuncu_kontrol_kilitli_mi(simdi):
        if simdi - stamina_son_harcama >= STAMINA_YENILENME_GECIKMESI:
            bonus_stamina = (
                0.34 * sig["poise"] + (0.26 if karakter_cinsiyet == "female" else 0.0)
            ) * dt
            oyuncu_stamina = min(
                float(oyuncu_max_stamina),
                float(oyuncu_stamina) + bonus_stamina,
            )
        mana_delay = 360 if karakter_cinsiyet == "female" else 520
        if simdi - stamina_son_harcama >= mana_delay and float(oyuncu_mana) < float(
            oyuncu_max_mana
        ):
            mana_bonus = (0.48 + 0.09 * sig["focus"]) * dt
            oyuncu_mana = min(
                float(oyuncu_max_mana),
                float(oyuncu_mana) + mana_bonus,
            )
    oran = min(1.0, dt * 11.0)
    stamina_gorunen += (oyuncu_stamina - stamina_gorunen) * oran
    mana_gorunen += (oyuncu_mana - mana_gorunen) * oran
    hp_gorunen += (oyuncu_hp - hp_gorunen) * oran
# </POTBO_STAGE S1061>

# <POTBO_STAGE S1067>


def sprite_maskeli_parlama_ciz(sprite, rect, renk, alfa):
    """Hold-to-attack flaşı her frame copy üretmesin; alpha kovalarıyla cache'lensin."""
    if sprite is None or rect is None or alfa <= 0:
        return
    renk = tuple(max(0, min(255, int(v))) for v in renk[:3])
    base_key = (id(sprite), renk)
    katman = sprite_parlama_mask_onbellegi.get(base_key)
    if katman is None:
        mask = pygame.mask.from_surface(sprite, 1)
        katman = mask.to_surface(
            setcolor=(*renk, 255), unsetcolor=(0, 0, 0, 0)
        ).convert_alpha()
        sprite_parlama_mask_onbellegi[base_key] = katman
    alpha_bucket = max(8, min(255, int(round(alfa / 16.0)) * 16))
    draw = sprite_parlama_alpha_onbellegi.get((base_key, alpha_bucket))
    if draw is None:
        draw = katman.copy()
        draw.set_alpha(alpha_bucket)
        sprite_parlama_alpha_onbellegi[(base_key, alpha_bucket)] = draw
        if len(sprite_parlama_alpha_onbellegi) > 96:
            for _ in range(min(24, len(sprite_parlama_alpha_onbellegi))):
                sprite_parlama_alpha_onbellegi.pop(
                    next(iter(sprite_parlama_alpha_onbellegi)),
                    None,
                )
    ekran.blit(draw, rect, special_flags=pygame.BLEND_RGBA_ADD)
# </POTBO_STAGE S1067>

# <POTBO_STAGE S1077>

V40_CHARACTER_PROFILE = {
    "TR": {
        "male": [
            "Guard kırıldıktan sonra baskısı büyür; yüksek poise ile takası sürdürür.",
            "Yara oranı arttıkça commitment hasarı hafif yükselir; stamina zayıflığı belirginleşir.",
            "Düz hat ve dar koridor ustasıdır; uzun reset yerine alanı zorla kapatır.",
        ],
        "female": [
            "İkinci açıklığı okur; tempo ve açı avantajı ham hızdan daha değerlidir.",
            "Mana verimi yüksektir; hareketi ve büyüyü aynı ekonomi içinde kullanır.",
            "Çapraz giriş, kısa reset ve menzil manipülasyonuyla aşırı uzayan saldırıyı cezalandırır.",
        ],
    },
    "EN": {
        "male": [
            "Pressure grows after a guard break; high poise lets him remain in the trade.",
            "Wounds slightly harden commitment damage while stamina weakness becomes clearer.",
            "He controls straight lanes and tight corridors instead of relying on long resets.",
        ],
        "female": [
            "She reads the second opening; tempo and angle matter more than raw speed.",
            "Her mana economy is stronger, linking movement and spell use into one resource plan.",
            "Oblique entries, short resets and range manipulation punish overextension.",
        ],
    },
}
# </POTBO_STAGE S1077>

# <POTBO_STAGE S1096>


def ayar_etiketi(ayar):
    if ayar == "bind_interact":
        return bt("DÜNYA ETKİLEŞİMİ", "WORLD INTERACT")
    if ayar == "bind_quick_use":
        return bt("ÖNE ÇIKANI KULLAN", "USE FEATURED")
    if ayar == "bind_q_quick_use":
        return bt("HIZLI EŞYA / BÜYÜ", "QUICK ITEM / SPELL")
    if ayar == "bind_attack":
        return bt("SALDIRI / HOLD", "ATTACK / HOLD")
    return _v41_ayar_etiketi_original(ayar)
# </POTBO_STAGE S1096>

# <POTBO_STAGE S1098>


# Geliştirici special bildirimi normal tuş şemasına karışmasın; yalnız Ctrl+U ile
# açıldığında bir kez kombinasyonu söyler. R hâlâ ayrılmış ve normal dash değildir.
_v41_gelistirici_test_girdisi_original = gelistirici_test_girdisi_uygula
# </POTBO_STAGE S1098>

# <POTBO_STAGE S1134>
v44_last_player_attack_mode = "normal"
# </POTBO_STAGE S1134>

# <POTBO_STAGE S1141>


def v44_attack_energy_estimate(mode=None, damage=None):
    speed = v44_attack_speed_estimate(mode)
    if damage is None:
        try:
            damage = oyuncu_saldiri_hasar_miktari()
        except Exception:
            damage = max(1, oyuncu_hasari)
    mass_proxy = 1.24 if karakter_cinsiyet == "male" else 0.86
    if str(mode or oyuncu_saldiri_modu) == "hold_release":
        mass_proxy *= 1.42
    return max(
        0.1,
        mass_proxy * speed * max(1.0, float(damage)) / 1000.0,
    )
# </POTBO_STAGE S1141>

# <POTBO_STAGE S1160>

V45_COMBO_WINDOW_MS = 560
V45_COMBO_RESET_MS = 880
V45_COMBO_MAX = 4
V45_COMBO_DAMAGE = (1.00, 1.045, 1.085, 1.13)
V45_COMBO_STAMINA_REFUND = (0.0, 0.8, 1.4, 2.0)
# </POTBO_STAGE S1160>

# <POTBO_STAGE S1163>
V45_EXECUTION_HP_RATIO = 0.18
V45_EXECUTION_DAMAGE_BONUS = 1.10
# </POTBO_STAGE S1163>

# <POTBO_STAGE S1165>
V45_SKILL_FLASH_MS = 150

v45_combo_count = 0
v45_combo_last_hit_ms = -10000
v45_combo_last_attack_ms = -10000
# </POTBO_STAGE S1165>

# <POTBO_STAGE S1167>
v45_combo_last_mode = "normal"
# </POTBO_STAGE S1167>

# <POTBO_STAGE S1170>
v45_last_damage_multiplier = 1.0
v45_last_skill_label = ""
v45_last_skill_until = 0
v45_combat_telemetry_enabled = False
# </POTBO_STAGE S1170>

# <POTBO_STAGE S1172>


def v45_skill_unlocked(skill_id):
    cfg = V45_SKILL_DEFINITIONS.get(str(skill_id), {})
    return int(oyuncu_level) >= int(cfg.get("unlock_level", 9999))


def v45_skill_name(skill_id):
    cfg = V45_SKILL_DEFINITIONS.get(str(skill_id), {})
    return str(cfg.get("name_tr" if dil == "TR" else "name_en", skill_id))


def v45_skill_flash(skill_id):
    global v45_last_skill_label, v45_last_skill_until
    v45_last_skill_label = v45_skill_name(skill_id)
    v45_last_skill_until = pygame.time.get_ticks() + V45_SKILL_FLASH_MS
# </POTBO_STAGE S1172>

# <POTBO_STAGE S1174>


def v45_attack_reach_current():
    nr, _nw, hr, _hw = _v38_player_reach_values()
    return float(hr if oyuncu_saldiri_modu == "hold_release" else nr)
# </POTBO_STAGE S1174>

# <POTBO_STAGE S1176>


def v45_sweetspot_factor(enemy):
    reach = max(1.0, v45_attack_reach_current())
    distance = v45_contact_distance(enemy)
    ratio = distance / reach
    if V45_SWEETSPOT_INNER <= ratio <= V45_SWEETSPOT_OUTER:
        center = (V45_SWEETSPOT_INNER + V45_SWEETSPOT_OUTER) * 0.5
        half = max(
            0.001,
            (V45_SWEETSPOT_OUTER - V45_SWEETSPOT_INNER) * 0.5,
        )
        quality = 1.0 - abs(ratio - center) / half
        return 1.0 + (V45_SWEETSPOT_BONUS - 1.0) * v44_smoothstep(quality)
    if ratio < V45_SWEETSPOT_INNER:
        t = v44_clamp01(ratio / max(0.001, V45_SWEETSPOT_INNER))
        return V45_HILT_PENALTY + (1.0 - V45_HILT_PENALTY) * t
    over = v44_clamp01(
        (ratio - V45_SWEETSPOT_OUTER) / max(0.001, 1.10 - V45_SWEETSPOT_OUTER)
    )
    return 1.0 + (V45_TIP_PENALTY - 1.0) * over


def v45_alignment_factor(enemy):
    facing = v44_player_facing_vector().normalize()
    to_target = pygame.Vector2(
        float(enemy.x) - float(oyuncu_x),
        float(enemy.y) - float(oyuncu_y),
    )
    if to_target.length_squared() <= 1e-6:
        return 1.0
    to_target = to_target.normalize()
    dot = max(-1.0, min(1.0, facing.dot(to_target)))
    alignment = max(0.0, dot)
    mastery = 1.0 if v45_skill_unlocked("edge_control") else 0.45
    return 1.0 + V45_ALIGNMENT_BONUS_MAX * (alignment**2.2) * mastery


def v45_cross_angle_factor(enemy):
    if not v45_skill_unlocked("edge_control"):
        return 1.0
    facing = v44_player_facing_vector().normalize()
    to_target = pygame.Vector2(float(enemy.x) - oyuncu_x, float(enemy.y) - oyuncu_y)
    if to_target.length_squared() <= 1e-6:
        return 1.0
    to_target = to_target.normalize()
    cross = abs(facing.x * to_target.y - facing.y * to_target.x)
    # Tam yan temas ödüllendirilmez; hafif çapraz açı temiz slicing için ideal.
    ideal = 0.38
    quality = max(0.0, 1.0 - abs(cross - ideal) / ideal)
    return 1.0 + V45_CROSS_ANGLE_BONUS * quality


def v45_execution_factor(enemy):
    if not v45_skill_unlocked("execution_read"):
        return 1.0
    ratio = float(getattr(enemy, "hp", 0)) / max(
        1.0, float(getattr(enemy, "max_hp", 1))
    )
    if ratio > V45_EXECUTION_HP_RATIO:
        return 1.0
    quality = 1.0 - ratio / max(0.001, V45_EXECUTION_HP_RATIO)
    return 1.0 + (V45_EXECUTION_DAMAGE_BONUS - 1.0) * v44_smoothstep(quality)


def v45_combo_factor(stage):
    idx = max(0, min(len(V45_COMBO_DAMAGE) - 1, int(stage) - 1))
    return float(V45_COMBO_DAMAGE[idx]) if v45_skill_unlocked("tempo_chain") else 1.0


def v45_melee_multiplier(enemy, stage):
    global v45_last_sweetspot, v45_last_alignment, v45_last_damage_multiplier
    sweet = v45_sweetspot_factor(enemy)
    align = v45_alignment_factor(enemy)
    cross = v45_cross_angle_factor(enemy)
    execution = v45_execution_factor(enemy)
    combo = v45_combo_factor(stage)
    heavy = 1.025 if oyuncu_saldiri_modu == "hold_release" else 1.0
    final = sweet * align * cross * execution * combo * heavy
    final = v44_clamp(final, 0.84, 1.42)
    v45_last_sweetspot = sweet
    v45_last_alignment = align * cross
    v45_last_damage_multiplier = final
    return final
# </POTBO_STAGE S1176>

# <POTBO_STAGE S1196>


# =========================================================
# V47 - COMBAT TELEMETRY / HIT FEEDBACK / ATTACK POLISH
# =========================================================
V47_VERSION = "47.0"
# </POTBO_STAGE S1196>

# <POTBO_STAGE S1198>
V47_COMBO_TEXT_MS = 520
# </POTBO_STAGE S1198>

# <POTBO_STAGE S1221>
V51_PARRY_STAMINA_REFUND = 4.0
V51_PARRY_ATTACKER_STUN_LIGHT_MS = 360
V51_PARRY_ATTACKER_STUN_MEDIUM_MS = 430
V51_PARRY_ATTACKER_STUN_HEAVY_MS = 500
# </POTBO_STAGE S1221>

# <POTBO_STAGE S1223>
V51_RIPOSTE_DAMAGE_BONUS = 1.16
# </POTBO_STAGE S1223>

# <POTBO_STAGE S1226>
V51_RIPOSTE_STAMINA_REFUND = 3.0
# </POTBO_STAGE S1226>

# <POTBO_STAGE S1228>
V51_ATTACK_BUFFER_MS = 135
V51_ATTACK_RECOVERY_SOFTEN = 0.92

v51_block_started_ms = -10000
v51_block_last_state = False
# </POTBO_STAGE S1228>

# <POTBO_STAGE S1230>
v51_attack_buffer_until = 0
# </POTBO_STAGE S1230>

# <POTBO_STAGE S1232>


def v51_parry_active(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    if not oyuncu_savunuyor:
        return False
    elapsed = int(now) - int(v51_block_started_ms)
    return 0 <= elapsed <= V51_PARRY_WINDOW_MS + V51_PARRY_LATE_GRACE_MS


def v51_parry_quality(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    elapsed = max(0, int(now) - int(v51_block_started_ms))
    if elapsed <= V51_PARRY_WINDOW_MS:
        return 1.0 - 0.28 * v44_smoothstep(elapsed / max(1.0, V51_PARRY_WINDOW_MS))
    grace = elapsed - V51_PARRY_WINDOW_MS
    return max(
        0.0,
        0.72 * (1.0 - grace / max(1.0, V51_PARRY_LATE_GRACE_MS)),
    )


def v51_parry_stun_for(class_name):
    if class_name == "heavy":
        return V51_PARRY_ATTACKER_STUN_HEAVY_MS
    if class_name == "medium":
        return V51_PARRY_ATTACKER_STUN_MEDIUM_MS
    return V51_PARRY_ATTACKER_STUN_LIGHT_MS
# </POTBO_STAGE S1232>

# <POTBO_STAGE S1235>


_v51_block_update_original = oyuncu_savunma_guncelle


def oyuncu_savunma_guncelle():
    global v51_block_started_ms, v51_block_last_state, v51_guard_release_until
    before = bool(oyuncu_savunuyor)
    result = _v51_block_update_original()
    after = bool(oyuncu_savunuyor)
    now = pygame.time.get_ticks()
    if after and not before:
        v51_block_started_ms = now
    elif before and not after:
        v51_guard_release_until = now + V51_GUARD_RELEASE_LOCK_MS
    v51_block_last_state = after
    if v51_riposte_armed and now > v51_riposte_until:
        v51_riposte_clear()
    return result


_v51_guard_hit_original = oyuncu_savunma_darbe_karsila


def oyuncu_savunma_darbe_karsila(kaynak_turu, kaynak_x, kaynak_y, attacker=None):
    global oyuncu_stamina, v51_parry_last_ms, v51_parry_source, v51_last_parry_quality
    now = pygame.time.get_ticks()
    parry = v51_parry_active(now) and _savunma_kaynagi_onden_mi(kaynak_x, kaynak_y)
    if not parry:
        return _v51_guard_hit_original(kaynak_turu, kaynak_x, kaynak_y, attacker)

    quality = v51_parry_quality(now)
    class_name = _savunma_sinifi(kaynak_turu)
    if quality <= 0.0:
        return _v51_guard_hit_original(kaynak_turu, kaynak_x, kaynak_y, attacker)

    # Parent guard mekanizması gerçek stamina/temas kontratını uygular.
    before_stamina = float(oyuncu_stamina)
    success = _v51_guard_hit_original(kaynak_turu, kaynak_x, kaynak_y, attacker)
    if not success:
        return False

    refund = min(
        V51_PARRY_STAMINA_REFUND * quality,
        max(0.0, before_stamina - float(oyuncu_stamina)) * 0.72
        + V51_PARRY_STAMINA_REFUND,
    )
    oyuncu_stamina = min(
        float(oyuncu_max_stamina),
        float(oyuncu_stamina) + refund,
    )
    v51_parry_last_ms = now
    v51_parry_source = str(kaynak_turu)
    v51_last_parry_quality = quality
    v51_parry_feedback(kaynak_x, kaynak_y, class_name, quality)
    v51_riposte_arm(str(kaynak_turu))

    if attacker is not None:
        stun = v51_parry_stun_for(class_name)
        try:
            attacker.attacking = False
            attacker.attack_connected = True
            attacker.attack_damage_applied = True
            attacker.recovery_until = max(
                int(getattr(attacker, "recovery_until", 0)),
                now + stun,
            )
            attacker.hit_stun_until = max(
                int(getattr(attacker, "hit_stun_until", 0)),
                now + stun,
            )
            attacker.stagger_until = max(
                int(getattr(attacker, "stagger_until", 0)),
                now + int(stun * 0.70),
            )
            attacker.vx *= -0.34
            attacker.vy *= -0.34
        except Exception:
            pass
    return True
# </POTBO_STAGE S1235>

# <POTBO_STAGE S1241>


# =========================================================
# END V51
# =========================================================


# =========================================================
# V52 - SKILL MATRIX / CHARACTER-SPECIFIC COMBAT IDENTITY
# =========================================================
V52_VERSION = "52.0"
# </POTBO_STAGE S1241>

# <POTBO_STAGE S1243>

v52_skill_cache_key = None
v52_skill_cache = {}
# </POTBO_STAGE S1243>

# <POTBO_STAGE S1245>


def v52_skill_branch_active(branch):
    branch = str(branch)
    if branch == "shared":
        return True
    return branch == str(karakter_cinsiyet)


def v52_unlocked_skill_ids(level=None, gender=None):
    if level is None:
        level = oyuncu_level
    if gender is None:
        gender = karakter_cinsiyet
    level = int(level)
    gender = str(gender)
    out = []
    for skill_id, cfg in V52_SKILL_CATALOG.items():
        branch = str(cfg.get("branch", "shared"))
        if branch not in ("shared", gender):
            continue
        if level >= int(cfg.get("level", 9999)):
            out.append(skill_id)
    out.sort(
        key=lambda sid: (
            int(V52_SKILL_CATALOG[sid]["level"]),
            sid,
        )
    )
    return tuple(out)


def v52_effect_totals(force=False):
    global v52_skill_cache_key, v52_skill_cache, v52_last_unlocked
    key = (int(oyuncu_level), str(karakter_cinsiyet))
    if not force and key == v52_skill_cache_key:
        return dict(v52_skill_cache)
    totals = {}
    unlocked = v52_unlocked_skill_ids(*key)
    for skill_id in unlocked:
        cfg = V52_SKILL_CATALOG[skill_id]
        for effect, value in cfg.get("effects", {}).items():
            totals[effect] = float(totals.get(effect, 0.0)) + float(value)
    for effect, bounds in V52_EFFECT_LIMITS.items():
        if effect in totals:
            totals[effect] = v44_clamp(totals[effect], bounds[0], bounds[1])
    v52_skill_cache_key = key
    v52_skill_cache = dict(totals)
    v52_last_unlocked = unlocked
    return dict(totals)
# </POTBO_STAGE S1245>

# <POTBO_STAGE S1247>


def v52_skill_name(skill_id):
    cfg = V52_SKILL_CATALOG.get(str(skill_id), {})
    return str(cfg.get("name_tr" if dil == "TR" else "name_en", skill_id))


def v52_recent_skill_names(limit=5):
    unlocked = v52_unlocked_skill_ids()
    return [v52_skill_name(sid) for sid in unlocked[-max(0, int(limit)) :]]


def v52_attack_energy_multiplier(mode=None):
    if mode is None:
        mode = oyuncu_saldiri_modu
    result = 1.0
    if str(mode) == "hold_release":
        result += v52_effect("heavy_energy")
    return result


def v52_damage_multiplier(mode=None):
    if mode is None:
        mode = oyuncu_saldiri_modu
    result = 1.0
    if str(mode) == "hold_release":
        result += v52_effect("heavy_damage")
    result += (
        v52_effect("combo_damage")
        * max(0, int(v45_combo_count) - 1)
        / max(1, V45_COMBO_MAX - 1)
    )
    return v44_clamp(result, 1.0, 1.18)
# </POTBO_STAGE S1247>

# <POTBO_STAGE S1250>


def v52_stamina_refund_bonus():
    return float(v52_effect("stamina_refund"))


def v52_execution_bonus():
    return float(v52_effect("execution"))
# </POTBO_STAGE S1250>

# <POTBO_STAGE S1253>


# V44 energy estimate now reads character skill transfer.
_v52_attack_energy_original = v44_attack_energy_estimate


def v44_attack_energy_estimate(mode=None, damage=None):
    return _v52_attack_energy_original(mode, damage) * v52_attack_energy_multiplier(
        mode
    )
# </POTBO_STAGE S1253>

# <POTBO_STAGE S1255>


# Parry window includes small branch bonuses.
def v51_parry_active(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    if not oyuncu_savunuyor:
        return False
    elapsed = int(now) - int(v51_block_started_ms)
    window = V51_PARRY_WINDOW_MS + v52_parry_window_bonus_ms()
    return 0 <= elapsed <= window + V51_PARRY_LATE_GRACE_MS


def v51_parry_quality(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    elapsed = max(0, int(now) - int(v51_block_started_ms))
    window = V51_PARRY_WINDOW_MS + v52_parry_window_bonus_ms()
    if elapsed <= window:
        return 1.0 - 0.28 * v44_smoothstep(elapsed / max(1.0, window))
    grace = elapsed - window
    return max(
        0.0,
        0.72 * (1.0 - grace / max(1.0, V51_PARRY_LATE_GRACE_MS)),
    )
# </POTBO_STAGE S1255>

# <POTBO_STAGE S1257>


# Skill strip: ağır UI'ye küçük, pasif bilgi; yeni modal/menu açmaz.
def v52_skill_strip_ciz():
    if oyun_durumu != OYUN or oyuncu_hp <= 0:
        return
    names = v52_recent_skill_names(3)
    if not names:
        return
    rect = pygame.Rect(16, YUKSEKLIK - 82, 370, 50)
    surf = pygame.Surface(rect.size, pygame.SRCALPHA)
    surf.fill((5, 4, 7, 146))
    pygame.draw.rect(surf, (69, 45, 51, 180), surf.get_rect(), 1)
    ekran.blit(surf, rect)
    yazi_yaz(
        bt("AKTİF TEKNİKLER", "ACTIVE TECHNIQUES"),
        rect.x + 10,
        rect.y + 8,
        GRI,
        mini_font,
    )
    label = "  •  ".join(names)
    max_width = rect.width - 20
    while len(label) > 4 and mini_font.size(label)[0] > max_width:
        label = label[:-2]
    if label != "  •  ".join(names):
        label = label.rstrip() + "…"
    yazi_yaz(label, rect.x + 10, rect.y + 28, ACIK_GRI, mini_font)
# </POTBO_STAGE S1257>

# <POTBO_STAGE S1259>


# Developer diagnostics expose every active passive and aggregate; no extra key required.
def v52_diagnostics():
    return {
        "version": V52_VERSION,
        "gender": str(karakter_cinsiyet),
        "level": int(oyuncu_level),
        "unlocked": v52_unlocked_skill_ids(),
        "effects": v52_effect_totals(),
        "recent": v52_recent_skill_names(5),
        "catalog_count": len(V52_SKILL_CATALOG),
    }
# </POTBO_STAGE S1259>

# <POTBO_STAGE S1268>


_v53_damage_context_original = _v44_damage_context_for_enemy


def _v44_damage_context_for_enemy(enemy, amount, source):
    context = _v53_damage_context_original(enemy, amount, source)
    return v53_context_enrich(context, getattr(enemy, "tur", "default"))
# </POTBO_STAGE S1268>

# <POTBO_STAGE S1277>


def v54_profile_key():
    if gelistirici_x_skill_aktif_mi():
        # Special has its own three-hit phase; velocity proxy uses strongest middle profile.
        return "special_mid"
    heavy = str(oyuncu_saldiri_modu) == "hold_release"
    if karakter_cinsiyet == "female":
        return "female_heavy" if heavy else "female_normal"
    return "male_heavy" if heavy else "male_normal"
# </POTBO_STAGE S1277>

# <POTBO_STAGE S1279>


def v54_attack_progress(now=None):
    global v54_last_progress
    if now is None:
        now = pygame.time.get_ticks()
    if not oyuncu_saldiriyor:
        v54_last_progress = 0.0
        return 0.0
    start = int(saldiri_baslangic)
    duration = max(1, int(oyuncu_aktif_saldiri_suresi_ms()))
    progress = v44_clamp01((int(now) - start) / float(duration))
    v54_last_progress = progress
    return progress


def v54_charge_scalar():
    if str(oyuncu_saldiri_modu) != "hold_release":
        return 1.0
    held = max(
        0,
        int(v44_last_player_swing_release_ms) - int(v44_last_player_swing_start_ms),
    )
    charge = v44_clamp01((held - 160.0) / 920.0)
    return 1.0 + 0.22 * v44_smoothstep(charge)


def v54_angular_velocity_deg_s(profile, progress):
    duration_ms = max(1.0, float(oyuncu_aktif_saldiri_suresi_ms()))
    curve = (
        V54_HEAVY_CURVE_SAMPLES
        if str(oyuncu_saldiri_modu) == "hold_release"
        else V54_SWING_CURVE_SAMPLES
    )
    normalized_speed = v54_curve_eval(curve, progress)
    # arc/duration is the average; curve peak scales instantaneous speed.
    average = float(profile["arc_deg"]) / (duration_ms / 1000.0)
    return (
        average
        * normalized_speed
        * 1.86
        * float(profile["hand_speed"])
        * v54_charge_scalar()
    )
# </POTBO_STAGE S1279>

# <POTBO_STAGE S1281>


def v54_instantaneous_velocity(now=None):
    global \
        v54_last_profile, \
        v54_last_velocity, \
        v54_last_angular_velocity, \
        v54_last_tip_velocity
    key = v54_profile_key()
    profile = V54_BLADE_PROFILES[key]
    progress = v54_attack_progress(now)
    angular = v54_angular_velocity_deg_s(profile, progress)
    tip = v54_tip_velocity_px_s(profile, angular)
    # Hand translation and body step contribute additional linear velocity.
    body = 52.0 if karakter_cinsiyet == "female" else 44.0
    if str(oyuncu_saldiri_modu) == "hold_release":
        body += 62.0
    velocity = tip + body
    if gelistirici_x_skill_aktif_mi():
        velocity *= 1.12
    v54_last_profile = key
    v54_last_angular_velocity = angular
    v54_last_tip_velocity = tip
    v54_last_velocity = velocity
    return velocity


_v54_attack_speed_original = v44_attack_speed_estimate


def v44_attack_speed_estimate(mode=None):
    # When attack is actually active, use instantaneous blade-tip kinematics.
    if oyuncu_saldiriyor and mode is None:
        speed = v54_instantaneous_velocity()
        if speed > 40.0:
            return v44_clamp(speed, 180.0, 1120.0)
    return _v54_attack_speed_original(mode)


def v54_contact_window_quality(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    profile = v54_profile()
    p = v54_attack_progress(now)
    start = float(profile["active_start"])
    peak = float(profile["active_peak"])
    end = float(profile["active_end"])
    if p < start or p > end:
        return 0.0
    if p <= peak:
        q = (p - start) / max(1e-9, peak - start)
    else:
        q = (end - p) / max(1e-9, end - peak)
    return v44_smootherstep(q)


def v54_contact_quality(enemy=None):
    global v54_last_contact_quality
    time_q = v54_contact_window_quality()
    speed = v44_attack_speed_estimate()
    speed_q = v44_clamp01((speed - 220.0) / 650.0)
    if enemy is not None:
        sweet = v45_sweetspot_factor(enemy)
        distance_q = v44_clamp((sweet - 0.84) / 0.27, 0.0, 1.0)
    else:
        distance_q = 0.72
    quality = 0.18 + 0.42 * time_q + 0.24 * speed_q + 0.16 * distance_q
    v54_last_contact_quality = v44_clamp01(quality)
    return v54_last_contact_quality
# </POTBO_STAGE S1281>

# <POTBO_STAGE S1285>


# Blood context reads instantaneous motion and edge efficiency before V44/V53 emitter.
_v54_damage_context_original = _v44_damage_context_for_enemy
# </POTBO_STAGE S1285>

# <POTBO_STAGE S1312>


def v56_attack_ready(actor, now=None):
    if now is None:
        now = pygame.time.get_ticks()
    state = v56_state(actor)
    cfg = v56_cfg(actor)
    dist = v56_update_closing(actor, state)
    cooldown = int(actor.cfg.get("attack_cooldown_ms", 1000)) + v56_repeat_penalty(
        actor, state
    )
    if int(now) - int(getattr(actor, "last_attack_ms", -100000)) < cooldown:
        return False
    if int(now) < int(getattr(actor, "recovery_until", 0)):
        return False
    if bool(getattr(actor, "attacking", False)):
        return False
    if dist > float(cfg["commit_range"]):
        return False
    if not v56_angle_ready(actor):
        return False
    # Hedef hızla uzaklaşıyorsa edge-of-range swing'e commit etme.
    if (
        dist > float(cfg["ideal_range"])
        and float(state.get("closing_rate", 0.0)) < -1.4
    ):
        return False
    return True
# </POTBO_STAGE S1312>

# <POTBO_STAGE S1315>


def _v43_inward_melee_slot(actor, target, simdi, player_prediction):
    v56_player_motion_tick(simdi)
    base = _v56_inward_slot_original(actor, target, simdi, player_prediction)
    if not _v43_melee_attack_ready(actor, simdi):
        return v56_lane_target(actor, base, simdi, player_prediction)
    if v56_attack_ready(actor, simdi):
        return pygame.Vector2(base)
    return v56_lane_target(actor, base, simdi, player_prediction)
# </POTBO_STAGE S1315>

# <POTBO_STAGE S1317>


if _v56_common_attack_update_original is not None:

    def _v56_common_attack_update(self, simdi):
        state = v56_state(self)
        before_attacking = bool(getattr(self, "attacking", False))
        before_connected = bool(getattr(self, "attack_connected", False))
        result = _v56_common_attack_update_original(self, simdi)
        after_attacking = bool(getattr(self, "attacking", False))
        last_attack = int(getattr(self, "last_attack_ms", -10000))
        if last_attack != int(state.get("last_attack_seen", -10000)):
            if last_attack - int(state.get("last_commit_ms", -10000)) < 1800:
                state["repeat_count"] = min(4, int(state.get("repeat_count", 0)) + 1)
            else:
                state["repeat_count"] = 1
            state["last_attack_seen"] = last_attack
            state["last_commit_ms"] = last_attack
        if (
            before_attacking
            and not after_attacking
            and not bool(getattr(self, "attack_connected", False))
            and not before_connected
        ):
            state["last_miss_ms"] = int(simdi)
            state["lane_sign"] *= -1.0
            state["lane_hold_until"] = int(simdi) + int(v56_cfg(self)["reposition_ms"])
        return result

    CommonEnemy._saldiri_guncelle = _v56_common_attack_update


_v56_attack_ready_original = _v43_melee_attack_ready


def _v43_melee_attack_ready(actor, simdi):
    # Tactical readiness now includes original cooldown contract + range/facing discipline.
    if not _v56_attack_ready_original(actor, simdi):
        return False
    state = v56_state(actor)
    cfg = v56_cfg(actor)
    if int(simdi) - int(state.get("last_miss_ms", -10000)) < int(cfg["miss_grace_ms"]):
        return False
    return True
# </POTBO_STAGE S1317>

# <POTBO_STAGE S1320>

# Bu katman saldırıların yalnız hasar sayısından ibaret kalmasını engeller. Whiff,
# temiz temas, art arda aynı açıdan vurma ve stamina durumu kısa süreli combat
# ritmine çevrilir. Etkiler küçük tutulur; asıl amaç timing ve ağırlık hissidir.
V57_FLOW_DECAY_PER_SEC = 0.44
# </POTBO_STAGE S1320>

# <POTBO_STAGE S1322>
V57_FLOW_DAMAGE_MAX = 0.045
V57_FATIGUE_DAMAGE_MAX = 0.055
# </POTBO_STAGE S1322>

# <POTBO_STAGE S1328>


def v57_stamina_ratio():
    return v57_clamp01(float(oyuncu_stamina) / max(1.0, float(oyuncu_max_stamina)))
# </POTBO_STAGE S1328>

# <POTBO_STAGE S1330>


def v57_attack_direction():
    return str(oyuncu_yonu or "down")


def v57_attack_precision():
    """Attack phase + blade contact quality'den 0..1 hassasiyet üretir."""
    progress = 0.5
    try:
        progress = float(v54_attack_progress())
    except Exception:
        pass
    # Temiz kesme bölgesi animasyonun ortasına yakın. Hold-release daha geniş pencere.
    width = V57_PRECISION_WIDTH + (
        0.08 if oyuncu_saldiri_modu == "hold_release" else 0.0
    )
    phase_quality = 1.0 - min(
        1.0,
        abs(progress - V57_PRECISION_CENTER) / max(0.05, width),
    )
    contact = (
        float(v54_last_contact_quality)
        if "v54_last_contact_quality" in globals()
        else 0.72
    )
    alignment = float(v45_last_alignment) if "v45_last_alignment" in globals() else 1.0
    alignment_quality = v57_clamp01((alignment - 0.82) / 0.34)
    return v57_clamp01(0.52 * phase_quality + 0.33 * contact + 0.15 * alignment_quality)
# </POTBO_STAGE S1330>

# <POTBO_STAGE S1332>


def v57_flow_damage_scalar():
    flow = v57_clamp01(v57_state.get("flow", 0.0))
    fatigue = v57_clamp01(v57_state.get("fatigue", 0.0))
    stamina = v57_stamina_ratio()
    precision = v57_clamp01(v57_state.get("precision", 0.0))
    positive = V57_FLOW_DAMAGE_MAX * flow * (0.35 + 0.65 * precision)
    negative = V57_FATIGUE_DAMAGE_MAX * fatigue * (1.0 - 0.35 * stamina)
    repeat = v57_repeat_direction_penalty()
    return max(0.90, min(1.075, 1.0 + positive - negative - repeat))
# </POTBO_STAGE S1332>

# <POTBO_STAGE S1334>


def v57_attack_started(now):
    v57_state["attack_started_ms"] = int(now)
    v57_state["last_contact_attack_started_ms"] = -10000
    v57_state["precision"] = v57_attack_precision()
    v57_state["last_result"] = "committed"


def v57_attack_finished(now):
    start = int(v57_state.get("attack_started_ms", -10000))
    contact_attack = int(v57_state.get("last_contact_attack_started_ms", -10000))
    contacted = contact_attack == start and start > 0
    v57_state["attack_finished_ms"] = int(now)
    if contacted:
        v57_state["whiff_streak"] = 0
        v57_state["last_result"] = "contact"
    else:
        v57_state["whiff_streak"] = min(8, int(v57_state.get("whiff_streak", 0)) + 1)
        v57_state["contact_streak"] = 0
        fatigue_add = V57_WHIFF_FATIGUE * (
            1.0 + 0.08 * min(4, v57_state["whiff_streak"] - 1)
        )
        if oyuncu_saldiri_modu == "hold_release":
            fatigue_add *= 1.22
        v57_state["fatigue"] = v57_clamp01(
            float(v57_state.get("fatigue", 0.0)) + fatigue_add
        )
        v57_state["flow"] = v57_clamp01(float(v57_state.get("flow", 0.0)) - 0.10)
        v57_state["last_result"] = "whiff"


def v57_record_contact(enemy, amount, before_hp, now=None):
    if now is None:
        now = pygame.time.get_ticks()
    start = int(v57_state.get("attack_started_ms", -10000))
    v57_state["last_contact_attack_started_ms"] = start
    v57_state["last_contact_ms"] = int(now)
    v57_state["contact_streak"] = min(12, int(v57_state.get("contact_streak", 0)) + 1)
    v57_state["whiff_streak"] = 0
    precision = v57_attack_precision()
    v57_state["precision"] = precision
    heavy = oyuncu_saldiri_modu == "hold_release"
    flow_add = V57_HEAVY_HIT_FLOW if heavy else V57_CLEAN_HIT_FLOW
    flow_add *= 0.70 + 0.50 * precision
    v57_state["flow"] = v57_clamp01(float(v57_state.get("flow", 0.0)) + flow_add)
    v57_state["fatigue"] = v57_clamp01(
        float(v57_state.get("fatigue", 0.0)) - V57_HIT_FATIGUE_RELIEF
    )

    direction = v57_attack_direction()
    previous = str(v57_state.get("last_direction", ""))
    if (
        previous == direction
        and now - int(v57_state.get("last_contact_ms_before", -10000))
        <= V57_REPEAT_ANGLE_WINDOW_MS
    ):
        v57_state["repeat_direction_count"] = min(
            5,
            int(v57_state.get("repeat_direction_count", 0)) + 1,
        )
    else:
        v57_state["repeat_direction_count"] = 1
    v57_state["last_direction"] = direction
    v57_state["last_contact_ms_before"] = int(now)
    killed = float(before_hp) > 0.0 and float(getattr(enemy, "hp", 0.0)) <= 0.0
    v57_state["last_result"] = "kill" if killed else "clean_hit"


def v57_update(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    previous = int(v57_state.get("last_update_ms", now))
    dt = max(0.0, min(0.05, (int(now) - previous) / 1000.0))
    v57_state["last_update_ms"] = int(now)
    active = v57_attack_active()
    was_active = bool(v57_state.get("last_attack_active", False))
    if active and not was_active:
        v57_attack_started(now)
    elif not active and was_active:
        v57_attack_finished(now)
    v57_state["last_attack_active"] = active

    if dt <= 0.0:
        return
    # Dövüş dışına çıkınca flow hızlı, fatigue daha yavaş çözülür.
    since_contact = int(now) - int(v57_state.get("last_contact_ms", -10000))
    flow_decay = V57_FLOW_DECAY_PER_SEC * (1.15 if since_contact > 1100 else 0.45)
    fatigue_decay = V57_FATIGUE_DECAY_PER_SEC * (1.35 if not active else 0.48)
    v57_state["flow"] = v57_clamp01(float(v57_state.get("flow", 0.0)) - flow_decay * dt)
    v57_state["fatigue"] = v57_clamp01(
        float(v57_state.get("fatigue", 0.0)) - fatigue_decay * dt
    )

    if active:
        live_precision = v57_attack_precision()
        smoothing = min(1.0, dt * 10.0)
        v57_state["precision"] = v57_lerp(
            v57_state.get("precision", 0.0),
            live_precision,
            smoothing,
        )
    elif since_contact > V57_RECOVERY_WINDOW_MS:
        v57_state["precision"] = max(
            0.0,
            float(v57_state.get("precision", 0.0)) - dt * 1.9,
        )
# </POTBO_STAGE S1334>

# <POTBO_STAGE S1339>


# Yeni oyun/yükleme/ölüm resetlerinde önceki combat temposu sızmasın.
_v57_death_reset_original = oyuncu_olum_sahnesini_sifirla
# </POTBO_STAGE S1339>

# <POTBO_STAGE S1363>
V59_EXECUTION_RATIO = 0.23
# </POTBO_STAGE S1363>

# <POTBO_STAGE S1365>
V59_LOW_STAMINA = 0.34
# </POTBO_STAGE S1365>

# <POTBO_STAGE S1368>


def v59_skill_available(definition):
    branch = str(definition.get("branch", "shared"))
    if int(oyuncu_level) < int(definition.get("level", 1)):
        return False
    if branch == "shared":
        return True
    return branch == str(karakter_cinsiyet)
# </POTBO_STAGE S1368>

# <POTBO_STAGE S1371>


def v59_current_shape():
    ctx = v44_context_current() or {}
    shape = str(ctx.get("shape", "")) if isinstance(ctx, dict) else ""
    if shape:
        return shape
    speed = float(v44_attack_speed_estimate())
    return v44_impact_shape_from_speed(speed, lethal=False, arterial=False)
# </POTBO_STAGE S1371>

# <POTBO_STAGE S1373>


def v59_condition_met(condition, enemy, now, before_hp):
    condition = str(condition)
    ratio = v59_target_ratio(enemy)
    precision = float(v57_state.get("precision", 0.0))
    flow = float(v57_state.get("flow", 0.0))
    stamina = v57_stamina_ratio()
    heavy = oyuncu_saldiri_modu == "hold_release"
    direction = v57_attack_direction()
    last_contact = int(v59_state.get("last_contact_ms", -10000))
    elapsed = int(now) - last_contact
    shape = v59_current_shape()
    riposte = v59_riposte_active(now)

    if condition == "fresh_contact":
        return elapsed > 1050
    if condition == "precision":
        return precision >= V59_PRECISION_THRESHOLD
    if condition == "alternate_direction":
        previous = str(v59_state.get("last_direction", ""))
        return bool(previous and previous != direction and elapsed <= 900)
    if condition == "second_contact":
        return int(v59_state.get("contact_index", 0)) >= 1 and elapsed <= 760
    if condition == "wounded_target":
        return ratio <= V59_WOUNDED_RATIO
    if condition == "riposte":
        return riposte
    if condition == "execution":
        return ratio <= V59_EXECUTION_RATIO
    if condition == "heavy_contact":
        return heavy
    if condition == "heavy_precision":
        return heavy and precision >= 0.66
    if condition == "longitudinal":
        return heavy and shape == "longitudinal"
    if condition == "low_enemy_poise":
        poise = float(getattr(enemy, "v56_poise", getattr(enemy, "poise", 0.5)))
        return heavy and poise <= 0.48
    if condition == "low_stamina_heavy":
        return heavy and stamina <= V59_LOW_STAMINA
    if condition == "riposte_heavy":
        return heavy and riposte
    if condition == "execution_heavy":
        return heavy and ratio <= V59_EXECUTION_RATIO
    if condition == "master_heavy":
        return heavy and precision >= 0.70 and flow >= 0.42 and ratio <= 0.52
    if condition == "cross_angle":
        return not heavy and v59_cross_quality(enemy) >= 0.68
    if condition == "quick_second":
        return not heavy and 0 < elapsed <= V59_QUICK_SECOND_MS
    if condition == "high_flow":
        return not heavy and flow >= V59_HIGH_FLOW
    if condition == "wounded_precision":
        return ratio <= V59_WOUNDED_RATIO and precision >= 0.68
    if condition == "fan_shape":
        return shape in ("fan_asymmetric", "radial_asymmetric")
    if condition == "master_flow":
        return not heavy and flow >= 0.66 and precision >= 0.68 and elapsed <= 620
    return False
# </POTBO_STAGE S1373>

# <POTBO_STAGE S1384>


def v59_unlocked_summary():
    rows = []
    for technique_id, definition in V59_TECHNIQUES.items():
        if v59_skill_available(definition):
            rows.append(
                {
                    "id": technique_id,
                    "name": v59_name(technique_id),
                    "condition": str(definition.get("condition", "")),
                    "cooldown_ms": int(definition.get("cooldown_ms", 0)),
                }
            )
    return rows
# </POTBO_STAGE S1384>

# <POTBO_STAGE S1393>


def v61_contact_depth(enemy):
    contact = (
        float(v54_last_contact_quality)
        if "v54_last_contact_quality" in globals()
        else 0.70
    )
    precision = (
        float(v57_state.get("precision", 0.0)) if "v57_state" in globals() else 0.5
    )
    sweet = float(v45_last_sweetspot) if "v45_last_sweetspot" in globals() else 1.0
    sweet_quality = max(0.0, min(1.0, (sweet - 0.82) / 0.34))
    armor = v61_armor(enemy)
    depth = contact * 0.48 + precision * 0.34 + sweet_quality * 0.18
    depth *= 1.0 - armor * 0.35
    if oyuncu_saldiri_modu == "hold_release":
        depth += 0.08 * (1.0 - armor * 0.30)
    return max(0.0, min(1.0, depth))
# </POTBO_STAGE S1393>

# <POTBO_STAGE S1395>


def v61_blade_impulse(enemy, damage):
    speed = max(90.0, float(v44_attack_speed_estimate()))
    depth = v61_contact_depth(enemy)
    profile = v54_profile() if "v54_profile" in globals() else {"effective_mass": 0.8}
    blade_mass = max(0.25, float(profile.get("effective_mass", 0.8)))
    target_mass = max(0.45, v61_mass(enemy))
    armor = v61_armor(enemy)
    zone = v61_zone()
    zone_factor = float(V61_ZONE_POISE.get(zone, 1.0))
    kinetic_proxy = (speed / V61_IMPULSE_REFERENCE) * blade_mass / target_mass
    damage_term = max(0.55, min(1.45, float(damage) / 35.0))
    impulse = kinetic_proxy * (0.42 + 0.58 * depth) * damage_term * zone_factor
    impulse *= 1.0 - armor * 0.42
    return max(0.0, min(2.6, impulse)), depth, zone, armor


def v61_apply_reaction(enemy, damage, before_hp, now=None):
    if now is None:
        now = pygame.time.get_ticks()
    if float(getattr(enemy, "hp", 0.0)) >= float(before_hp):
        return None
    impulse, depth, zone, armor = v61_blade_impulse(enemy, damage)
    kind = v61_reaction_kind(depth)
    uid = str(getattr(enemy, "uid", id(enemy)))

    # Original hasar_al poise'i damage ile zaten düşürdü; burada yalnız kinematik fark
    # eklenir. Extra miktar küçük ve armor/mass ile güçlü biçimde sınırlandırılmıştır.
    max_poise = float(getattr(enemy, "cfg", {}).get("poise_max", 0.0))
    poise_extra = max_poise * max(0.0, impulse - 0.48) * 0.11
    if max_poise > 0 and float(getattr(enemy, "hp", 0.0)) > 0:
        enemy.poise = float(getattr(enemy, "poise", max_poise)) - poise_extra

    stun_extra = int(
        round(
            V61_EXTRA_STUN_MIN_MS
            + (V61_EXTRA_STUN_MAX_MS - V61_EXTRA_STUN_MIN_MS)
            * max(0.0, min(1.0, impulse / 1.65))
        )
    )
    if kind == "glance":
        stun_extra = int(stun_extra * 0.35)
    elif kind == "deep":
        stun_extra = int(stun_extra * 1.16)
    enemy.hit_stun_until = max(
        int(getattr(enemy, "hit_stun_until", 0)),
        int(now) + stun_extra,
    )

    staggered = False
    if (
        max_poise > 0
        and float(getattr(enemy, "hp", 0.0)) > 0
        and float(getattr(enemy, "poise", max_poise)) <= 0.0
    ):
        base_stagger = int(getattr(enemy, "cfg", {}).get("stagger_ms", 300))
        extension = min(
            V61_STAGGER_EXTENSION_MAX_MS,
            int(round(max(0.0, impulse - 0.8) * 85.0)),
        )
        enemy.stagger_until = max(
            int(getattr(enemy, "stagger_until", 0)),
            int(now) + base_stagger + extension,
        )
        enemy.hit_stun_until = max(int(enemy.hit_stun_until), int(enemy.stagger_until))
        enemy.recovery_until = max(
            int(getattr(enemy, "recovery_until", 0)),
            int(enemy.stagger_until),
        )
        enemy.attacking = False
        enemy.poise = max_poise
        staggered = True

    # Çok derin ağır temas ufak ekstra momentum üretir; mevcut knockback'in yerine geçmez.
    if depth >= V61_DEPTH_DEEP and impulse > 0.9:
        delta = pygame.Vector2(
            float(getattr(enemy, "x", oyuncu_x)) - float(oyuncu_x),
            float(getattr(enemy, "y", oyuncu_y)) - float(oyuncu_y),
        )
        if delta.length_squared() > 1e-7:
            delta = delta.normalize()
            kick = min(V61_KNOCKBACK_MAX, (impulse - 0.8) * 11.0)
            enemy.vx = float(getattr(enemy, "vx", 0.0)) + delta.x * kick
            enemy.vy = float(getattr(enemy, "vy", 0.0)) + delta.y * kick

    reaction = {
        "uid": uid,
        "kind": kind,
        "depth": depth,
        "impulse": impulse,
        "poise_extra": poise_extra,
        "stun_extra_ms": stun_extra,
        "zone": zone,
        "armor": armor,
        "staggered": staggered,
        "until": int(now) + 360,
    }
    v61_reactions[uid] = reaction
    v61_last.update(reaction)
    return reaction
# </POTBO_STAGE S1395>

# <POTBO_STAGE S1398>


# Blood context contact depth'i görür: deep -> biraz daha çizgisel/hızlı, glance -> dağınık.
_v61_damage_context_original = _v44_damage_context_for_enemy


def _v44_damage_context_for_enemy(enemy, amount, source):
    ctx = _v61_damage_context_original(enemy, amount, source)
    if _v44_is_player_melee_source(source):
        depth = v61_contact_depth(enemy)
        kind = v61_reaction_kind(depth)
        ctx["contact_depth"] = depth
        ctx["contact_kind"] = kind
        ctx["armor_response"] = v61_armor(enemy)
        if kind == "deep":
            ctx["speed"] = float(ctx.get("speed", v44_attack_speed_estimate())) * 1.055
        elif kind == "glance":
            ctx["speed"] = float(ctx.get("speed", v44_attack_speed_estimate())) * 0.91
        ctx["shape"] = v44_impact_shape_from_speed(
            float(ctx.get("speed", v44_attack_speed_estimate())),
            lethal=bool(ctx.get("lethal", False)),
            arterial=bool(ctx.get("arterial", False)),
        )
    return ctx
# </POTBO_STAGE S1398>

# <POTBO_STAGE S1426>
v67_last_attack_id = -1
# </POTBO_STAGE S1426>

# <POTBO_STAGE S1430>


def v67_measured_speed_available():
    return bool(
        oyuncu_saldiriyor
        and len(v67_tip_history) >= 3
        and v67_last_measured_speed > 0.0
    )
# </POTBO_STAGE S1430>

# <POTBO_STAGE S1432>


_v67_attack_speed_original = v44_attack_speed_estimate


def v44_attack_speed_estimate(mode=None):
    analytic = float(_v67_attack_speed_original(mode))
    if not v67_measured_speed_available():
        return analytic
    measured = float(v67_last_measured_speed)
    # İlk iki frame ölçümü jitter'a açık; history doldukça measured tarafına ağırlık artar.
    confidence = v44_clamp01((len(v67_tip_history) - 2) / 7.0)
    blend = V67_SPEED_BLEND * confidence
    return v44_clamp(
        analytic * (1.0 - blend) + measured * blend,
        V67_SPEED_MIN,
        V67_SPEED_MAX,
    )


_v67_damage_context_original = _v44_damage_context_for_enemy


def _v44_damage_context_for_enemy(enemy, amount, source):
    context = _v67_damage_context_original(enemy, amount, source)
    if _v44_is_player_melee_source(source) and v67_measured_speed_available():
        direction = v67_measured_direction()
        measured_speed = float(v44_attack_speed_estimate())
        context["direction"] = tuple(direction)
        context["speed"] = measured_speed
        context["blade_curvature"] = float(v67_last_curvature)
        context["blade_arc_length"] = float(v67_last_arc_length)
        context["shape"] = v44_impact_shape_from_speed(
            measured_speed,
            lethal=bool(context.get("lethal", False)),
            arterial=bool(context.get("arterial", False)),
        )
    return context
# </POTBO_STAGE S1432>

# <POTBO_STAGE S1435>


def v67_diagnostics():
    return {
        "version": V67_VERSION,
        "samples": len(v67_tip_history),
        "measured_speed": round(float(v67_last_measured_speed), 2),
        "effective_speed": round(float(v44_attack_speed_estimate()), 2),
        "tangent": (
            round(float(v67_last_tangent.x), 4),
            round(float(v67_last_tangent.y), 4),
        ),
        "curvature_rad": round(float(v67_last_curvature), 5),
        "arc_length_px": round(float(v67_last_arc_length), 2),
        "reach": v67_reach_contract(),
    }
# </POTBO_STAGE S1435>

# <POTBO_STAGE S1444>


# Damage context target türü/uid'sini palette katmanına taşı.
_v68_damage_context_original = _v44_damage_context_for_enemy
# </POTBO_STAGE S1444>

# <POTBO_STAGE S1456>


def v71_telemetry_line_ciz():
    if not (GELISTIRICI_MODU and v45_combat_telemetry_enabled and v71_events):
        return
    event = v71_last
    text = mini_font.render(
        f"splat {event['shape']}  n={event['count']}  A={event['anisotropy']:.2f}  spread={event['spread_deg']:.0f}°  asym={event['asymmetry']:.2f}",
        True,
        (221, 208, 212) if event.get("quality_ok", True) else (245, 184, 91),
    )
    x = GENISLIK - text.get_width() - 22
    y = 172
    bg = pygame.Surface(
        (text.get_width() + 10, text.get_height() + 5),
        pygame.SRCALPHA,
    )
    bg.fill((5, 3, 6, 180))
    bg.blit(text, (5, 2))
    ekran.blit(bg, (x - 5, y))
# </POTBO_STAGE S1456>

# <POTBO_STAGE S1458>
V72_RELEASE_TARGET = "blood-combat-ui-polish"
# </POTBO_STAGE S1458>

# <POTBO_STAGE S1477>


_v73_player_damage_original = oyuncu_kanli_hasar_kaydi
# </POTBO_STAGE S1477>

# <POTBO_STAGE S1538>

# ---------------------------------------------------------
# LOADING HINTS: KONTROL EZBERİ DEĞİL, GERÇEK SİSTEM BİLGİSİ
# ---------------------------------------------------------
IPUCLARI = {
    "TR": [
        (
            "Savunmayı darbeden hemen önce başlatmak normal bloktan farklıdır. Önden gelen bir teması bu kısa pencerede karşılamak "
            "saldırganı kısa süre sendeletir ve yaklaşık 0,7 saniyelik riposte fırsatı açar; sonraki temiz yakın dövüş vuruşu daha değerlidir."
        ),
        (
            "Kılıcın hasarı yalnız hedefe değmesine bağlı değildir. Hedef gövdene fazla yapışırsa kabza bölgesinde kalırsın; orta-uç mesafesinde ve hedefe düzgün hizalanmış temas genellikle daha iyi hasar üretir."
        ),
        (
            "Seviye 7'den sonra aynı hedefe doğru ritimde bağlanan vuruşlar Tempo Zinciri biriktirir. Rastgele spam yapmak yerine recovery sonuna yakın yeni saldırıyı bağlamak zinciri ve stamina ekonomisini daha güvenilir tutar."
        ),
        (
            "Seviye 10'dan sonra kesici temaslar hemoraji biriktirebilir. Dört veya daha fazla birikim varken ağır kesik yapmak birikimin bir bölümünü anlık rupture hasarına çevirir; ağır vuruşu yalnız ilk fırsatta harcamak her zaman iyi değildir."
        ),
        (
            "Hemoraji tick'leri hedefi tek başına öldürmez; canı en fazla 1'e kadar indirebilir. Kanaması çok olan bir düşmanı uzaktan beklemek yerine son fiziksel teması güvenli bir açıklıkta sen vermelisin."
        ),
        (
            "Ağır saldırının asıl değeri yalnız ham hasar değildir; poise baskısı da daha yüksektir. Dayanıklı bir düşmana karşı hafif vuruşlarla açıklık hazırlayıp ağır darbeyi dengesini bozabilecek anda kullanmak daha verimlidir."
        ),
        (
            "Parry yalnız saldırı gerçekten ön taraftan geliyorsa çalışır. Bir düşmanın çevresinde dönerken K'ya güvenmek yerine önce gövdeni tehdide çevir; aksi halde zamanlama doğru olsa bile normal darbeyi yiyebilirsin."
        ),
        (
            "Heads Thrower düz ve okunabilir bir atış hattı ister. Araya kaya, duvar veya başka bir engel sokmak sadece mesafe açmaktan daha değerlidir; hat bozulduğunda yaklaşmak için daha güvenli bir pencere oluşur."
        ),
        (
            "Ateş patlamasında merkez ile dış halka aynı şey değildir. Merkeze yakın temas daha ağır hasar ve itme üretirken dış halka daha çok düzen bozmak içindir; kalabalığı dağıtmak istiyorsan her zaman tam merkeze nişanlamak gerekmez."
        ),
        (
            "Kan 20 dakikada tamamen kurur fakat kuruması onu yok etmez. Eski bir kan alanı temiz kalıyorsa bunun nedeni zaman değil ekosistemdir: kurtçuklar kanı tüketip yakın çevreye taşıyabilir, fareler ise kurtçukları, organları ve kanı azaltır."
        ),
        (
            "Yerdeki kanın yayılması yeni kan üretmez. Kurtçuğun başka noktaya taşıdığı küçük iz kaynak lekedeki gerçek kütleden eksilir; bu yüzden çok sayıda kurtçuk bir alanı büyütür gibi görünse de toplam kan kütlesi sınırsız artmaz."
        ),
        (
            "Düşmanın saldırı animasyonunda hazırlık ve recovery iki ayrı fırsattır. Hazırlık sırasında açgözlü saldırmak yerine yönü oku; vuruş boşa çıktıktan sonraki recovery, özellikle ağır düşmanlarda çok daha güvenli karşılık penceresidir."
        ),
        (
            "Düşük canlı hedeflerde ilerleyen seviyelerde temiz temas ayrıca ödüllendirilir. Ancak bu bonus hitbox'ı büyütmez; hedefin yanında savurmak yerine gerçek kılıç temasını korumak hâlâ gerekir."
        ),
        (
            "Aynı noktada sürekli dövüşmek çevreyi mekanik olarak değiştirir. Çok kan ve organ zamanla kurtçuk/fare davranışını o bölgeye çeker; uzun bir çatışmadan sonra geri döndüğünde sahnenin aynı kalmasını bekleme."
        ),
    ],
    "EN": [
        (
            "Starting guard just before impact is different from ordinary blocking. Catching a frontal hit inside that short window briefly staggers the attacker and opens roughly a 0.7-second riposte window for a stronger clean melee response."
        ),
        (
            "Sword damage is not determined only by whether the hitbox touches. Crowding the target puts contact near the hilt; aligned contact around the middle-to-outer reach generally produces a better strike."
        ),
        (
            "After level 7, well-timed consecutive hits on the same target build Tempo Chain. Linking the next input near the end of recovery is more reliable than random spam and preserves the stamina economy of the chain."
        ),
        (
            "After level 10, slashing contact can build hemorrhage. With four or more stacks, a heavy cut can rupture part of that buildup into immediate damage, so spending every heavy attack as soon as possible is not always optimal."
        ),
        (
            "Hemorrhage ticks cannot kill a target by themselves; they stop at 1 HP. A heavily bleeding enemy still needs a final physical contact, so finish it during a safe opening rather than waiting at range."
        ),
        (
            "The value of a heavy attack is not only raw damage; it also applies greater poise pressure. Against durable enemies, light contact can create the opening and the heavy strike can be saved for the moment it can actually break balance."
        ),
        (
            "A parry only works when the attack is genuinely coming from the front. When circling an enemy, turn your body toward the threat before relying on guard timing or a correctly timed input can still fail as a parry."
        ),
        (
            "Heads Thrower wants a clean firing lane. Breaking that lane with terrain is often more valuable than merely increasing distance, because the broken line gives you a safer approach window."
        ),
        (
            "The center and outer ring of a fire explosion serve different purposes. Near-center contact produces stronger damage and displacement, while the edge is better for disrupting a formation without committing to the center."
        ),
        (
            "Blood fully dries in 20 minutes, but drying never deletes it. If an old blood field becomes cleaner, ecology did the work: maggots consume and redistribute blood, while rats reduce maggots, organs and blood."
        ),
        (
            "Blood spread by maggots is not created from nothing. Every small stain carried elsewhere subtracts real mass from the source stain, so the visible area can widen without the total blood mass growing indefinitely."
        ),
        (
            "Enemy wind-up and recovery are different opportunities. Reading the direction during wind-up is safer than greedily attacking into it; the recovery after a missed heavy action is usually the better counter window."
        ),
        (
            "At later levels, clean contact against critically wounded targets receives an additional execution reward. The bonus never enlarges the hitbox, so real blade contact still matters."
        ),
        (
            "Repeated fighting in one location changes that location mechanically. Heavy blood and organ accumulation influences maggot and rat activity, so returning to an old battlefield can produce a different local ecology."
        ),
    ],
}
# </POTBO_STAGE S1538>

# <POTBO_STAGE S1562>


# İpuçları sade, oyuna dönük ve teknik olmayan hale getirildi.
IPUCLARI["TR"] = [
    "Düşmanın ilk hamlesini izle. Birçok saldırı, hasardan önce niyetini gösterir.",
    "Staminan düşerken açgözlü oynama. Bir adım geri çekilmek çoğu zaman ikinci bir darbiden daha değerlidir.",
    "Dar alanlarda aynı yönden inat etme. Açı değiştirirsen hem vurmak hem kaçmak kolaylaşır.",
    "Zırhlı düşmana sabırla yaklaş. Kör bir saldırı zinciri yerine doğru açıklığı bekle.",
    "Canın azken panikleme. Savunup tempo düşürmek savaşı geri çevirebilir.",
    "Bir düşmanı yendikten sonra çevreyi kontrol et. Ödüller ve gizli yollar çoğu kez dövüşten sonra fark edilir.",
    "Uzak saldırı yapan düşmanlara düz koşma. Kısa yön değişiklikleri hayatta tutar.",
    "Güvende olduğunda kaydet. Özellikle zor bir karşılaşmadan sonra bunu erteleme.",
    "Her düşman aynı cesarete sahip değildir. Korkanları sıkıştır, saldırganlara ise ritim bozarak cevap ver.",
]
IPUCLARI["EN"] = [
    "Watch the enemy's first move. Many attacks reveal their intent before the hit lands.",
    "Do not get greedy when stamina is low. One step back is often worth more than a second swing.",
    "Do not insist on the same angle in narrow spaces. A small change of line makes both offense and escape easier.",
    "Approach armored enemies with patience. Wait for a real opening instead of forcing a full attack chain.",
    "Do not panic when health is low. Slowing the pace and defending can turn a fight around.",
    "Check the area after a hard fight. Rewards and hidden paths are often easier to notice afterward.",
    "Do not run straight at ranged enemies. Short changes of direction keep you alive.",
    "Save while you are safe, especially after difficult encounters.",
    "Not every enemy is equally brave. Corner the fearful ones, and break the rhythm of the aggressive ones.",
]
# </POTBO_STAGE S1562>

# <POTBO_STAGE S1565>


def _v78_common_hasar(self, miktar, kaynak=None):
    before_hp = float(getattr(self, "hp", 0.0))
    before_vx = float(getattr(self, "vx", 0.0))
    before_vy = float(getattr(self, "vy", 0.0))
    result = _v78_common_hasar_original(self, miktar, kaynak)
    if float(getattr(self, "hp", before_hp)) < before_hp:
        scale = float(V78_RECOIL_SCALE.get(str(getattr(self, "tur", "")), 0.32))
        dx = float(getattr(self, "vx", 0.0)) - before_vx
        dy = float(getattr(self, "vy", 0.0)) - before_vy
        self.vx = before_vx + dx * scale
        self.vy = before_vy + dy * scale
        if scale > 0.10 and abs(dx) + abs(dy) < 7.0:
            src_x = (
                float(getattr(kaynak, "x", oyuncu_x))
                if kaynak is not None and hasattr(kaynak, "x")
                else float(oyuncu_x)
            )
            src_y = (
                float(getattr(kaynak, "y", oyuncu_y))
                if kaynak is not None and hasattr(kaynak, "y")
                else float(oyuncu_y)
            )
            d = pygame.Vector2(
                float(getattr(self, "x", oyuncu_x)) - src_x,
                float(getattr(self, "y", oyuncu_y)) - src_y,
            )
            if d.length_squared() <= 1e-7:
                d = pygame.Vector2(1.0, 0.0)
            d = d.normalize() * (10.0 + 18.0 * scale)
            self.vx += d.x
            self.vy += d.y
    return result
# </POTBO_STAGE S1565>

# <POTBO_STAGE S1577>


# =========================================================
# END V78
# =========================================================


# =========================================================
# V79 - RUNTIME FIX / HEAVY UI / FASTER COMBAT / DEATH SYNC
# =========================================================
V79_VERSION = "79.0"
# </POTBO_STAGE S1577>

# <POTBO_STAGE S1582>

DASH_MESAFESI = 146.0
DASH_SURESI_MS = 108
DASH_ADIMI = 3.75
DASH_BEKLEME_SURESI = 560
# </POTBO_STAGE S1582>

# <POTBO_STAGE S1584>
saldiri_suresi = 334
saldiri_bekleme_suresi = 365
# </POTBO_STAGE S1584>

# <POTBO_STAGE S1631>


# Ölüm başlarken gerçek AI saldırısı kesilir. Bundan sonra görülen tekrar darbeler yalnız
# yukarıdaki authored ölüm koreografisidir; combat AI ikinci kez hasar çözmez.
_v81_death_update_original = oyuncu_olum_durumu_guncelle


def oyuncu_olum_durumu_guncelle():
    before = int(oyuncu_olum_baslangic_ms)
    _v81_death_update_original()
    if oyuncu_hp <= 0 and oyuncu_olum_baslangic_ms > 0 and before <= 0:
        killer = _v24_olum_katil_actor_bul()
        if killer is not None:
            try:
                killer.attacking = False
                killer.attack_damage_applied = True
                killer.attack_connected = True
                killer.vx = 0.0
                killer.vy = 0.0
            except Exception:
                pass
        _v81_reset_death_blood()
# </POTBO_STAGE S1631>

# <POTBO_STAGE S1637>
V81_STAMINA_HEIGHT = 5
# </POTBO_STAGE S1637>

# <POTBO_STAGE S1642>


def _v81_stamina_bar(rect, ratio, fill, back, border, warning=False):
    rect = pygame.Rect(rect)
    ratio = _v79_clamp01(ratio)
    pygame.draw.rect(ekran, (2, 2, 3), rect.inflate(4, 4))
    pygame.draw.rect(ekran, back, rect)
    fill_w = int(round(rect.width * ratio))
    if fill_w > 0:
        pygame.draw.rect(
            ekran,
            fill,
            pygame.Rect(rect.x, rect.y, fill_w, rect.height),
        )
        pygame.draw.line(
            ekran,
            (245, 223, 92),
            (rect.left, rect.top),
            (rect.left + max(0, fill_w - 1), rect.top),
            1,
        )
    for x in range(rect.left + 12, rect.right, 12):
        pygame.draw.line(
            ekran,
            (26, 24, 10),
            (x, rect.top),
            (x, rect.bottom - 1),
            1,
        )
    pygame.draw.rect(ekran, PARLAK_KIRMIZI if warning else border, rect, 1)
# </POTBO_STAGE S1642>

# <POTBO_STAGE S1657>
saldiri_suresi = 298
saldiri_bekleme_suresi = 390
SALDIRI_STAMINA_MALIYETI = 18
STAMINA_YENILENME_GECIKMESI = 540
STAMINA_YENILENME_HIZI = 28.0
# </POTBO_STAGE S1657>

# <POTBO_STAGE S1659>
V82_STAMINA_H = 3
# </POTBO_STAGE S1659>

# <POTBO_STAGE S1663>


def _v82_stamina_bar(rect, ratio, warning=False):
    rect = pygame.Rect(rect)
    ratio = _v82_clamp01(ratio)
    pygame.draw.rect(ekran, (3, 3, 3), rect.inflate(2, 2))
    pygame.draw.rect(ekran, (37, 33, 8), rect)
    fw = int(round(rect.width * ratio))
    if fw > 0:
        pygame.draw.rect(
            ekran,
            (224, 197, 48),
            pygame.Rect(rect.x, rect.y, fw, rect.height),
        )
    edge = PARLAK_KIRMIZI if warning else (105, 96, 54)
    pygame.draw.line(
        ekran,
        edge,
        (rect.left, rect.top - 1),
        (rect.right, rect.top - 1),
        1,
    )
    # Sadece uçlarda küçük end-cap: stamina artık ağır bir üçüncü zırh barı gibi görünmez.
    pygame.draw.line(
        ekran,
        edge,
        (rect.left, rect.top - 2),
        (rect.left, rect.bottom + 1),
        1,
    )
    pygame.draw.line(
        ekran,
        edge,
        (rect.right - 1, rect.top - 2),
        (rect.right - 1, rect.bottom + 1),
        1,
    )
# </POTBO_STAGE S1663>

# <POTBO_STAGE S1673>


# ---------------------------------------------------------
# COMBAT: her melee temasını ayırt edilebilir kıl
# ---------------------------------------------------------
def _v82_is_player_melee_source(source):
    if bool(getattr(source, "is_player_magic", False)):
        return False
    try:
        return bool(_v44_is_player_melee_source(source)) and bool(oyuncu_saldiriyor)
    except Exception:
        return bool(oyuncu_saldiriyor) and (source is None or source == "player")
# </POTBO_STAGE S1673>

# <POTBO_STAGE S1678>


def _v82_common_hasar(self, miktar, kaynak=None):
    player_melee = _v82_is_player_melee_source(kaynak)
    before = float(getattr(self, "hp", 0.0))
    result = _v82_common_hasar_original(self, miktar, kaynak)
    after = float(getattr(self, "hp", before))
    if player_melee and after < before:
        heavy = str(oyuncu_saldiri_modu) == "hold_release"
        kind, depth, _armor = _v82_hit_kind(self, lethal=after <= 0.0, heavy=heavy)
        dealt = max(1, int(round(before - after)))
        _v82_spawn_hit_fx(self, kind, depth, dealt)
        _v82_apply_hit_feedback(self, kind, dealt)
    return result
# </POTBO_STAGE S1678>

# <POTBO_STAGE S1685>
saldiri_suresi = 286
saldiri_bekleme_suresi = 364
SALDIRI_STAMINA_MALIYETI = 15
STAMINA_YENILENME_GECIKMESI = 430
STAMINA_YENILENME_HIZI = 34.0
# </POTBO_STAGE S1685>

# <POTBO_STAGE S1687>
V83_STAMINA_H = 2
# </POTBO_STAGE S1687>

# <POTBO_STAGE S1691>


def _v83_stamina_bar(rect, ratio, warning=False):
    rect = pygame.Rect(rect)
    ratio = _v82_clamp01(ratio)
    pygame.draw.rect(ekran, (28, 24, 8), rect)
    fw = int(round(rect.width * ratio))
    if fw > 0:
        pygame.draw.rect(
            ekran,
            (224, 196, 46),
            pygame.Rect(rect.x, rect.y, fw, rect.height),
        )
    edge = PARLAK_KIRMIZI if warning else (104, 96, 54)
    pygame.draw.line(
        ekran,
        edge,
        (rect.left, rect.top - 1),
        (rect.right - 1, rect.top - 1),
        1,
    )
    pygame.draw.line(
        ekran,
        edge,
        (rect.left, rect.bottom),
        (rect.right - 1, rect.bottom),
        1,
    )
# </POTBO_STAGE S1691>

# <POTBO_STAGE S1694>


# --- combat blood / feedback ---------------------------------------------
_v83_kanli_darbe_efekti_original = kanli_darbe_efekti
# </POTBO_STAGE S1694>

# <POTBO_STAGE S1711>


# =========================================================
# END V83
# =========================================================


# =========================================================
# V84 - EXECUTION STANCE / PERFECT GUARD / WOUND ECOLOGY
# =========================================================
#
# V84 is deliberately the final authority for guard contact, riposte ownership,
# execution choreography, wound ecology and the three-colour death tableau.  Older
# layers remain available as implementation primitives, but their broad parry and
# binary split decisions are not allowed to leak through this contract.
#
# The system is data driven for three reasons:
#   1. combat timings can be audited without running a full asset build,
#   2. every hostile actor follows the same rules without type-specific shortcuts,
#   3. transient cinematic state is isolated from persistent save state.
# =========================================================

V84_VERSION = "84.0"
# </POTBO_STAGE S1711>

# <POTBO_STAGE S1717>
V84_RIPOSTE_ATTACK_MS = 350
V84_RIPOSTE_STAMINA_SCALE = 0.55
# </POTBO_STAGE S1717>

# <POTBO_STAGE S1719>
V84_EXECUTION_NATURAL_HP_RATIO = 0.24
V84_EXECUTION_NATURAL_RANGE = 116.0
V84_EXECUTION_OVERRIDE_RANGE = 480.0
V84_EXECUTION_END_LINGER_MS = 560
V84_EXECUTION_MAX_FRAGMENTS = 38
V84_EXECUTION_TRACE_LIFE_MS = 330
V84_EXECUTION_INTERRUPT_DAMAGE_RATIO = 0.055
# </POTBO_STAGE S1719>

# <POTBO_STAGE S1722>

# The interval curve is authored, not random.  It starts readable and accelerates
# until individual cuts collapse into a single perceived burst.  Angle, length and
# body crossing vary per target; rhythm never does.
V84_EXECUTION_BEAT_TIMES = (
    150,
    370,
    555,
    710,
    836,
    940,
    1028,
    1104,
    1172,
    1234,
    1292,
    1348,
    1428,
)

V84_EXECUTION_ANGLE_FAMILIES = (
    (-34.0, 27.0, -18.0, 39.0, -48.0, 12.0, 56.0),
    (31.0, -26.0, 17.0, -42.0, 51.0, -9.0, -58.0),
    (-18.0, 44.0, -52.0, 8.0, 30.0, -37.0, 61.0),
)
# </POTBO_STAGE S1722>

# <POTBO_STAGE S1727>


def v84_actor_alive(actor, include_suspended=True):
    if actor is None:
        return False
    hp = int(getattr(actor, "hp", 0))
    if hp <= 0:
        return False
    if bool(getattr(actor, "active", False)):
        return True
    if include_suspended and v84_execution_state.active:
        return actor is v84_execution_state.target
    return False
# </POTBO_STAGE S1727>

# <POTBO_STAGE S1731>


def v84_actor_frame(actor, now=None):
    if actor is None:
        return None
    if now is None:
        now = pygame.time.get_ticks()
    frame = None
    try:
        _, frame = actor._animasyon_kare(int(now))
    except (
        AttributeError,
        IndexError,
        KeyError,
        TypeError,
        ValueError,
    ):
        frame = None
    if frame is not None:
        return frame
    try:
        frames = actor._attack_frames()
    except (AttributeError, TypeError):
        frames = []
    if frames:
        return frames[0]
    return None
# </POTBO_STAGE S1731>

# <POTBO_STAGE S1735>


class V84FractureField:
    def __init__(self, surface, max_fragments=V84_EXECUTION_MAX_FRAGMENTS):
        if surface is None:
            surface = pygame.Surface((48, 68), pygame.SRCALPHA)
            pygame.draw.polygon(
                surface,
                (*V84_BODY, 255),
                ((24, 0), (46, 20), (39, 67), (9, 67), (2, 20)),
            )
        self.size = tuple(surface.get_size())
        self.max_fragments = max(2, int(max_fragments))
        root_mask = pygame.mask.from_surface(surface, 1)
        root = V84Fragment(root_mask, self.size)
        root.refresh_surface()
        self.fragments = [root]
        self.cut_count = 0
        self.released = False
        self.release_age = 0.0

    def _side_masks(self, point, normal):
        width, height = self.size
        rectangle = [
            (-2.0, -2.0),
            (width + 2.0, -2.0),
            (width + 2.0, height + 2.0),
            (-2.0, height + 2.0),
        ]
        positive = v84_clip_halfplane(
            rectangle,
            point,
            normal,
            True,
        )
        negative = v84_clip_halfplane(
            rectangle,
            point,
            normal,
            False,
        )
        return (
            v84_polygon_mask(self.size, positive),
            v84_polygon_mask(self.size, negative),
        )

    def cut(self, angle_deg, offset_ratio=0.0, gap_px=0.9):
        if self.released:
            return 0
        if len(self.fragments) >= self.max_fragments:
            return 0
        width, height = self.size
        direction = pygame.Vector2(1.0, 0.0).rotate(float(angle_deg))
        normal = direction.rotate(90.0)
        center = pygame.Vector2(width * 0.5, height * 0.5)
        line_point = center + normal * (float(offset_ratio) * min(width, height))
        positive_mask, _negative_mask = self._side_masks(
            line_point,
            normal,
        )
        next_fragments = []
        made = 0
        for fragment in self.fragments:
            if len(next_fragments) + (len(self.fragments) - made) >= self.max_fragments:
                next_fragments.append(fragment)
                continue
            positive = fragment.mask.overlap_mask(
                positive_mask,
                (0, 0),
            )
            # The line belongs to the positive half.  Deriving the second child by
            # subtraction guarantees exact pixel conservation and prevents a
            # one-pixel duplicate seam from gaining mass after many cuts.
            negative = fragment.mask.copy()
            negative.erase(positive, (0, 0))
            positive_count = int(positive.count())
            negative_count = int(negative.count())
            total = max(1, fragment.pixel_count())
            minimum = max(5, int(total * 0.055))
            if positive_count < minimum or negative_count < minimum:
                next_fragments.append(fragment)
                continue
            child_a = V84Fragment(
                positive,
                self.size,
                tone=fragment.tone,
                gap=pygame.Vector2(fragment.gap) + normal * float(gap_px),
            )
            child_b = V84Fragment(
                negative,
                self.size,
                tone=fragment.tone,
                gap=pygame.Vector2(fragment.gap) - normal * float(gap_px),
            )
            child_a.refresh_surface()
            child_b.refresh_surface()
            next_fragments.extend((child_a, child_b))
            made += 1
        self.fragments = next_fragments[: self.max_fragments]
        self.cut_count += int(made > 0)
        return made

    def release(self, impulse=(1.0, 0.0), power=1.0, seed=0):
        if self.released:
            return
        self.released = True
        rng = random.Random(int(seed) ^ 0x5A17)
        width, height = self.size
        center = pygame.Vector2(width * 0.5, height * 0.5)
        base = v84_safe_vector(impulse).normalize()
        for index, fragment in enumerate(self.fragments):
            radial = fragment.centroid() - center
            if radial.length_squared() <= 1e-8:
                radial = base.rotate(rng.uniform(-95.0, 95.0))
            else:
                radial = radial.normalize()
            blend = v84_safe_vector(radial * 0.66 + base * 0.34).normalize()
            speed = rng.uniform(54.0, 142.0) * float(power)
            fragment.velocity = blend * speed
            fragment.velocity.y -= rng.uniform(54.0, 132.0) * float(power)
            fragment.angular_velocity = rng.uniform(-390.0, 390.0)
            fragment.rotation = rng.uniform(-2.5, 2.5)
            fragment.released = True
            fragment.position = pygame.Vector2(0.0, 0.0)

    def update(self, dt):
        if self.released:
            self.release_age += float(dt)
        for fragment in self.fragments:
            fragment.update(dt)

    def draw(self, anchor_midbottom):
        for fragment in self.fragments:
            fragment.draw(anchor_midbottom)

    def diagnostics(self):
        return {
            "fragments": len(self.fragments),
            "cuts": int(self.cut_count),
            "released": bool(self.released),
            "pixels": sum(fragment.pixel_count() for fragment in self.fragments),
        }
# </POTBO_STAGE S1735>

# <POTBO_STAGE S1741>
v84_execution_windows = {}
# </POTBO_STAGE S1741>

# <POTBO_STAGE S1743>
v84_execution_state = V84ExecutionState()
v84_execution_post_fragments = []
v84_execution_last_end_ms = -10000
v84_execution_total = 0
v84_execution_interruptions = 0
v84_execution_finishes = 0
# </POTBO_STAGE S1743>

# <POTBO_STAGE S1745>
v84_combat_last_tick_ms = pygame.time.get_ticks()


def v84_perfect_guard_window_ms():
    if str(v38_combat_precision) == "strict":
        return V84_PERFECT_GUARD_STRICT_MS
    return V84_PERFECT_GUARD_STANDARD_MS


def v84_perfect_guard_front_dot():
    if str(v38_combat_precision) == "strict":
        return V84_PERFECT_GUARD_FRONT_DOT_STRICT
    return V84_PERFECT_GUARD_FRONT_DOT_STANDARD
# </POTBO_STAGE S1745>

# <POTBO_STAGE S1749>


def v84_perfect_guard_possible(
    source_type,
    source_x,
    source_y,
    attacker,
    now=None,
):
    if now is None:
        now = pygame.time.get_ticks()
    if oyuncu_hp <= 0 or not oyuncu_savunuyor:
        return False
    if v84_execution_state.active:
        return False
    if v84_guard_quality(now) <= 0.0:
        return False
    if not v84_source_in_front(source_x, source_y):
        return False
    return v84_direct_melee_source(
        source_type,
        source_x,
        source_y,
        attacker,
    )
# </POTBO_STAGE S1749>

# <POTBO_STAGE S1752>


def v84_apply_poise_damage(actor, amount, now, stagger_ms):
    if actor is None:
        return False
    maximum = v84_actor_poise_max(actor)
    if maximum <= 0.0:
        return False
    current = v84_clamp(
        float(getattr(actor, "poise", maximum)),
        0.0,
        maximum,
    )
    current -= max(0.0, float(amount))
    broken = current <= 0.0
    actor.poise = max(0.0, current)
    actor.last_poise_hit_ms = int(now)
    if broken:
        v84_mark_poise_break(actor, now, stagger_ms)
        actor.attacking = False
        if hasattr(actor, "dash_kind"):
            actor.dash_kind = None
        if hasattr(actor, "dash_until"):
            actor.dash_until = 0
        actor.vx = float(getattr(actor, "vx", 0.0)) * -0.16
        actor.vy = float(getattr(actor, "vy", 0.0)) * -0.16
    return broken
# </POTBO_STAGE S1752>

# <POTBO_STAGE S1754>


def v84_execution_naturally_eligible(actor, now=None):
    if actor is None or not v84_actor_alive(actor):
        return False
    if now is None:
        now = pygame.time.get_ticks()
    hp = float(getattr(actor, "hp", 0.0))
    maximum = max(1.0, float(getattr(actor, "max_hp", 1.0)))
    if hp / maximum > V84_EXECUTION_NATURAL_HP_RATIO:
        return False
    if not v84_actor_poise_broken(actor, now):
        return False
    return v84_actor_distance(actor) <= V84_EXECUTION_NATURAL_RANGE
# </POTBO_STAGE S1754>

# <POTBO_STAGE S1758>


# V51 delegated to the base guard after deciding its own broad parry.  V84 keeps
# that base handler for ordinary held K, thereby removing projectile parries and
# global riposte ownership without rewriting the stable stamina-chain logic.
_v84_normal_guard_handler = globals().get(
    "_v51_guard_hit_original",
    oyuncu_savunma_darbe_karsila,
)


def oyuncu_savunma_darbe_karsila(
    kaynak_turu,
    kaynak_x,
    kaynak_y,
    attacker=None,
):
    global v84_normal_guard_total
    now = pygame.time.get_ticks()
    if v84_perfect_guard_possible(
        kaynak_turu,
        kaynak_x,
        kaynak_y,
        attacker,
        now,
    ):
        return v84_perfect_guard_apply(
            kaynak_turu,
            kaynak_x,
            kaynak_y,
            attacker,
            now,
        )
    result = _v84_normal_guard_handler(
        kaynak_turu,
        kaynak_x,
        kaynak_y,
        attacker,
    )
    if result:
        v84_normal_guard_total += 1
    return result


_v84_guard_update_original = oyuncu_savunma_guncelle


def oyuncu_savunma_guncelle():
    result = _v84_guard_update_original()
    now = pygame.time.get_ticks()
    if v84_riposte_state.target is not None and not v84_riposte_active(now):
        if not v84_riposte_state.committed:
            v84_riposte_state.clear()
    stale_poise = [
        uid
        for uid, until in v84_poise_break_windows.items()
        if int(until) < int(now) - 1000
    ]
    for uid in stale_poise:
        v84_poise_break_windows.pop(uid, None)
    stale_execution = [
        uid for uid, until in v84_execution_windows.items() if int(until) < int(now)
    ]
    for uid in stale_execution:
        v84_execution_windows.pop(uid, None)
    return result
# </POTBO_STAGE S1758>

# <POTBO_STAGE S1761>


def v84_riposte_profile(actor):
    return V84_RIPOSTE_PROFILES.get(
        str(getattr(actor, "tur", "")),
        {
            "damage": 1.38,
            "poise": 0.52,
            "stagger_ms": 360,
            "armor": "unknown",
        },
    )
# </POTBO_STAGE S1761>

# <POTBO_STAGE S1766>


def v84_execution_choreography(target, seed):
    rng = random.Random(int(seed) ^ 0x7EC7)
    family = V84_EXECUTION_ANGLE_FAMILIES[int(seed) % len(V84_EXECUTION_ANGLE_FAMILIES)]
    points = []
    for index in range(len(V84_EXECUTION_BEAT_TIMES) + 1):
        base_angle = family[index % len(family)]
        orbit = base_angle * 2.15 + index * 23.0
        orbit += rng.uniform(-8.0, 8.0)
        distance = rng.uniform(48.0, 68.0)
        point = v84_execution_safe_point(
            target,
            pygame.Vector2(1.0, 0.0).rotate(orbit),
            distance,
        )
        points.append(point)
    return points
# </POTBO_STAGE S1766>

# <POTBO_STAGE S1768>


def v84_execution_suspend_target(target):
    target.active = False
    target.attacking = False
    if hasattr(target, "attack_connected"):
        target.attack_connected = True
    if hasattr(target, "attack_damage_applied"):
        target.attack_damage_applied = True
    if hasattr(target, "dash_kind"):
        target.dash_kind = None
    if hasattr(target, "dash_until"):
        target.dash_until = 0
    target.vx = 0.0
    target.vy = 0.0
# </POTBO_STAGE S1768>

# <POTBO_STAGE S1770>


def v84_execution_trace_prune(now):
    state = v84_execution_state
    state.slashes[:] = [
        trace
        for trace in state.slashes
        if int(now) - int(trace.created_ms) <= V84_EXECUTION_TRACE_LIFE_MS
    ]


def v84_execution_cut_parameters(index, state):
    rng = random.Random(int(state.seed) ^ ((int(index) + 1) * 0x45D9F3B))
    family = V84_EXECUTION_ANGLE_FAMILIES[
        int(state.seed) % len(V84_EXECUTION_ANGLE_FAMILIES)
    ]
    base = float(family[index % len(family)])
    angle = base + rng.uniform(-9.0, 9.0)
    length = rng.uniform(0.82, 1.18)
    offset = rng.uniform(-0.19, 0.19)
    if index < 3:
        offset *= 0.55
        length = max(1.02, length)
    elif index >= len(V84_EXECUTION_BEAT_TIMES) - 3:
        offset *= 1.16
    return angle, length, offset
# </POTBO_STAGE S1770>

# <POTBO_STAGE S1774>


def v84_execution_restore_target_after_interrupt(now):
    state = v84_execution_state
    target = state.target
    if target is None:
        return
    saved = state.target_saved_state
    target.active = (
        bool(saved.get("active", state.target_was_active))
        and int(getattr(target, "hp", 0)) > 0
    )
    target.attacking = False
    target.attack_connected = True
    target.attack_damage_applied = True
    target.vx = 0.0
    target.vy = 0.0
    target.recovery_until = max(
        int(saved.get("recovery_until", 0)),
        int(now) + 360,
    )
    target.hit_stun_until = max(
        int(saved.get("hit_stun_until", 0)),
        int(now) + 240,
    )
    max_hp = max(1, int(getattr(target, "max_hp", 1)))
    chip = min(
        max(0, int(getattr(target, "hp", 0)) - 1),
        max(
            1,
            int(round(max_hp * V84_EXECUTION_INTERRUPT_DAMAGE_RATIO)),
        )
        * max(1, state.cuts_landed),
    )
    if chip > 0:
        target.hp = max(1, int(target.hp) - chip)
        if hasattr(target, "hp_trail_hold_until"):
            target.hp_trail_hold_until = int(now) + 260
    setattr(
        target,
        "v84_execution_interrupted_until",
        int(now) + 900,
    )
# </POTBO_STAGE S1774>

# <POTBO_STAGE S1776>


def v84_execution_player_position(elapsed_ms):
    state = v84_execution_state
    points = state.choreography_points
    if not points:
        return pygame.Vector2(state.player_start)
    times = (0,) + V84_EXECUTION_BEAT_TIMES
    elapsed = float(elapsed_ms)
    segment = 0
    for index in range(1, len(times)):
        if elapsed <= times[index]:
            segment = index - 1
            break
    else:
        return pygame.Vector2(points[-1])
    start_time = float(times[segment])
    end_time = float(times[segment + 1])
    local = (elapsed - start_time) / max(1.0, end_time - start_time)
    local = v84_smootherstep(local)
    start = points[min(segment, len(points) - 1)]
    end = points[min(segment + 1, len(points) - 1)]
    return pygame.Vector2(start).lerp(end, local)
# </POTBO_STAGE S1776>

# <POTBO_STAGE S1779>


def oyuncu_kontrol_kilitli_mi(simdi=None):
    if v84_execution_state.active:
        return True
    return _v84_control_lock_original(simdi)
# </POTBO_STAGE S1779>

# <POTBO_STAGE S1781>


def oyuncu_serbest_hareket_guncelle():
    if v84_execution_state.active:
        return
    return _v84_free_move_original()
# </POTBO_STAGE S1781>

# <POTBO_STAGE S1795>


_v84_player_damage_original = oyuncu_kanli_hasar_kaydi


def oyuncu_kanli_hasar_kaydi(
    kaynak_x,
    kaynak_y,
    profil,
    hasar,
    kaynak_adi="",
):
    result = _v84_player_damage_original(
        kaynak_x,
        kaynak_y,
        profil,
        hasar,
        kaynak_adi,
    )
    if v84_execution_state.active and int(hasar) > 0:
        v84_execution_interrupt("player_death" if oyuncu_hp <= 0 else "incoming_hit")
    return result
# </POTBO_STAGE S1795>

# <POTBO_STAGE S1798>


def oyuncu_olum_sahnesini_sifirla():
    v84_transient_reset(restore_execution_target=True)
    return _v84_death_reset_original()
# </POTBO_STAGE S1798>

# <POTBO_STAGE S1802>


_v84_death_damage_original = oyuncu_kanli_hasar_kaydi


def oyuncu_kanli_hasar_kaydi(
    kaynak_x,
    kaynak_y,
    profil,
    hasar,
    kaynak_adi="",
):
    result = _v84_death_damage_original(
        kaynak_x,
        kaynak_y,
        profil,
        hasar,
        kaynak_adi,
    )
    if oyuncu_hp <= 0:
        v84_death_prepare(
            kaynak_x,
            kaynak_y,
            profil,
            kaynak_adi,
        )
    return result
# </POTBO_STAGE S1802>

# <POTBO_STAGE S1818>


def v84_timing_contract():
    intervals = [
        V84_EXECUTION_BEAT_TIMES[index] - V84_EXECUTION_BEAT_TIMES[index - 1]
        for index in range(1, len(V84_EXECUTION_BEAT_TIMES))
    ]
    early = intervals[:5]
    late = intervals[-5:]
    return {
        "strict_guard_in_range": (120 <= V84_PERFECT_GUARD_STRICT_MS <= 160),
        "standard_guard_in_range": (120 <= V84_PERFECT_GUARD_STANDARD_MS <= 160),
        "riposte_window_in_range": (600 <= V84_RIPOSTE_WINDOW_MS <= 800),
        "execution_beats_monotonic": all(
            current > previous
            for previous, current in zip(
                V84_EXECUTION_BEAT_TIMES,
                V84_EXECUTION_BEAT_TIMES[1:],
            )
        ),
        "execution_accelerates": (
            sum(late) / max(1, len(late)) < sum(early) / max(1, len(early))
        ),
        "intervals_ms": tuple(intervals),
    }
# </POTBO_STAGE S1818>

# <POTBO_STAGE S1824>

# Three readable crossings, ten compressed asymmetric crossings, then a long
# retreat and one terminal crossing.  These are impact times, not arbitrary
# animation frames.
V84_EXECUTION_BEAT_TIMES = (
    340,
    900,
    1385,
    1754,
    1822,
    1890,
    1958,
    2026,
    2094,
    2162,
    2230,
    2298,
    2366,
    5310,
)
V84_EXECUTION_END_LINGER_MS = 720
V84_EXECUTION_TRACE_LIFE_MS = 390
V84_EXECUTION_MAX_FRAGMENTS = 30
V85_EXECUTION_TOTAL_MS = V84_EXECUTION_BEAT_TIMES[-1] + V84_EXECUTION_END_LINGER_MS
V85_EXECUTION_DASH_SEGMENTS = (
    (80, 600, 0, 1, "dash_flat"),
    (690, 1110, 1, 2, "dash_diagonal"),
    (1190, 1580, 2, 3, "dash_reverse"),
)
V85_EXECUTION_BURST_START_MS = 1718
V85_EXECUTION_BURST_STEP_MS = 68
V85_EXECUTION_BURST_TRAVEL_MS = 72
V85_EXECUTION_REPOSITION_START_MS = 2400
V85_EXECUTION_REPOSITION_END_MS = 2840
V85_EXECUTION_RETREAT_END_MS = 5140
V85_EXECUTION_FINAL_END_MS = 5480
V85_EXECUTION_AFTERIMAGE_INTERVAL_MS = 24
V85_EXECUTION_TRAIL_LIFE_MS = 245
V85_EXECUTION_BURST_ANGLES = (
    29.0,
    -47.0,
    57.0,
    -24.0,
    68.0,
    -38.0,
    14.0,
    -62.0,
    43.0,
    -31.0,
)

v85_execution_flash_started_ms = 0
v85_execution_flash_until_ms = 0


def v85_ease_out(value):
    return _gelistirici_x_skill_ease_out(v84_clamp01(value))
# </POTBO_STAGE S1824>

# <POTBO_STAGE S1830>


_v85_execution_start_original = v84_execution_start


def v84_execution_start(target=None, override=True, source="ctrl_y"):
    ok = _v85_execution_start_original(target, override, source)
    if not ok:
        return False
    state = v84_execution_state
    state.motion_trail = []
    state.last_motion_record_ms = int(state.last_tick_ms)
    state.last_player_position = pygame.Vector2(state.player_start)
    state.motion_phase = "entry"
    state.detached_fragments = 0
    state.final_dash_started = False
    state.final_dash_impact = False
    if state.fracture is not None:
        state.fracture.max_fragments = V84_EXECUTION_MAX_FRAGMENTS
    return True


def v85_execution_segment_position(elapsed, start_ms, end_ms, start, end, ease):
    local = (float(elapsed) - float(start_ms)) / max(1.0, float(end_ms - start_ms))
    return pygame.Vector2(start).lerp(pygame.Vector2(end), ease(local))


def v84_execution_player_position(elapsed_ms):
    state = v84_execution_state
    points = state.choreography_points
    if len(points) < 17:
        return pygame.Vector2(state.player_start)
    elapsed = float(elapsed_ms)

    for (
        start_ms,
        end_ms,
        start_index,
        end_index,
        phase,
    ) in V85_EXECUTION_DASH_SEGMENTS:
        if elapsed < start_ms:
            return pygame.Vector2(points[start_index])
        if elapsed <= end_ms:
            state.motion_phase = phase
            return v85_execution_segment_position(
                elapsed,
                start_ms,
                end_ms,
                points[start_index],
                points[end_index],
                v85_ease_out,
            )

    for index in range(10):
        start_ms = V85_EXECUTION_BURST_START_MS + index * V85_EXECUTION_BURST_STEP_MS
        end_ms = start_ms + V85_EXECUTION_BURST_TRAVEL_MS
        start_index = 3 + index
        end_index = 4 + index
        if elapsed < start_ms:
            return pygame.Vector2(points[start_index])
        if elapsed <= end_ms:
            state.motion_phase = "burst"
            return v85_execution_segment_position(
                elapsed,
                start_ms,
                end_ms,
                points[start_index],
                points[end_index],
                v85_ease_out,
            )
    if elapsed < V85_EXECUTION_REPOSITION_START_MS:
        state.motion_phase = "burst_hold"
        return pygame.Vector2(points[13])
    if elapsed <= V85_EXECUTION_REPOSITION_END_MS:
        state.motion_phase = "reposition"
        local = (elapsed - V85_EXECUTION_REPOSITION_START_MS) / max(
            1.0,
            V85_EXECUTION_REPOSITION_END_MS - V85_EXECUTION_REPOSITION_START_MS,
        )
        target = pygame.Vector2(state.target.x, state.target.y)
        start = pygame.Vector2(points[13])
        end = pygame.Vector2(points[14])
        radial = v84_safe_vector(start - target).normalize()
        control = target + radial.rotate(78.0) * 104.0
        return _gelistirici_x_skill_bezier(start, control, end, local)
    if elapsed <= V85_EXECUTION_RETREAT_END_MS:
        state.motion_phase = "retreat"
        return v85_execution_segment_position(
            elapsed,
            V85_EXECUTION_REPOSITION_END_MS,
            V85_EXECUTION_RETREAT_END_MS,
            points[14],
            points[15],
            v84_smootherstep,
        )
    if elapsed <= V85_EXECUTION_FINAL_END_MS:
        state.motion_phase = "final_dash"
        state.final_dash_started = True
        return v85_execution_segment_position(
            elapsed,
            V85_EXECUTION_RETREAT_END_MS,
            V85_EXECUTION_FINAL_END_MS,
            points[15],
            points[16],
            v85_ease_out,
        )
    state.motion_phase = "aftermath"
    return pygame.Vector2(points[16])


def v84_execution_cut_parameters(index, state):
    rng = random.Random(int(state.seed) ^ ((int(index) + 1) * 0x85D9F3B))
    target = state.target
    center = pygame.Vector2(float(target.x), float(target.y))
    points = state.choreography_points
    if index == 0:
        motion = pygame.Vector2(points[1]) - pygame.Vector2(points[0])
        angle = motion.as_polar()[1]
        return angle, 1.16, rng.uniform(-0.025, 0.025)
    if index == 1:
        motion = pygame.Vector2(points[2]) - pygame.Vector2(points[1])
        return (
            motion.as_polar()[1],
            1.20,
            rng.uniform(-0.08, 0.08),
        )
    if index == 2:
        motion = pygame.Vector2(points[3]) - pygame.Vector2(points[2])
        return (
            motion.as_polar()[1],
            1.22,
            rng.uniform(-0.08, 0.08),
        )
    if 3 <= index <= 12:
        start = pygame.Vector2(points[index])
        end = pygame.Vector2(points[index + 1])
        motion = end - start
        angle = motion.as_polar()[1] + rng.uniform(-4.8, 4.8)
        return (
            angle,
            rng.uniform(0.92, 1.18),
            rng.uniform(-0.17, 0.17),
        )
    motion = pygame.Vector2(points[16]) - pygame.Vector2(points[15])
    if motion.length_squared() <= 1e-8:
        motion = center - pygame.Vector2(points[15])
    return (
        motion.as_polar()[1],
        1.48,
        rng.uniform(-0.035, 0.035),
    )
# </POTBO_STAGE S1830>

# <POTBO_STAGE S1833>


def v85_execution_record_motion(state, now, position):
    trail = getattr(state, "motion_trail", None)
    if trail is None:
        state.motion_trail = []
        trail = state.motion_trail
    last = int(getattr(state, "last_motion_record_ms", 0))
    interval = (
        V85_EXECUTION_AFTERIMAGE_INTERVAL_MS
        if state.motion_phase in ("burst", "final_dash")
        else 46
    )
    if int(now) - last >= interval:
        trail.append(
            (
                int(now),
                pygame.Vector2(position),
                str(state.motion_phase),
            )
        )
        state.last_motion_record_ms = int(now)
    cutoff = int(now) - V85_EXECUTION_TRAIL_LIFE_MS
    trail[:] = [sample for sample in trail if sample[0] >= cutoff]
# </POTBO_STAGE S1833>

# <POTBO_STAGE S1838>
V85_MORTAL_ATTACK_RESTART_MS = 120
# </POTBO_STAGE S1838>

# <POTBO_STAGE S1850>


def v85_mortal_attack_restart(now):
    state = v85_mortal_wound_state
    killer = state.killer
    if killer is None or state.attack_restarted:
        return
    state.attack_restarted = True
    try:
        killer.attacking = False
        killer._saldiri_baslat(int(now))
    except (AttributeError, TypeError, ValueError):
        try:
            killer.attacking = True
            killer.attack_started_ms = int(now)
            killer.attack_connected = False
            killer.attack_damage_applied = False
        except (AttributeError, TypeError, ValueError):
            pass
# </POTBO_STAGE S1850>

# <POTBO_STAGE S1853>


_v85_player_damage_original = oyuncu_kanli_hasar_kaydi
# </POTBO_STAGE S1853>

# <POTBO_STAGE S1877>


def v85_hold_cross_update(now=None):
    global oyuncu_yonu
    if now is None:
        now = pygame.time.get_ticks()
    state = v85_hold_cross_state
    if not state.active:
        return False
    if int(saldiri_baslangic) != int(state.attack_id):
        state.reset(int(saldiri_baslangic))
        return False
    progress = (int(now) - int(state.hit_ms)) / max(1.0, float(V85_HOLD_CROSS_MS))
    desired = state.start.lerp(state.exit, v84_smootherstep(progress))
    previous = pygame.Vector2(float(oyuncu_x), float(oyuncu_y))
    try:
        actual = _v34_special_scripted_position_apply(desired, previous=previous)
    except (NameError, TypeError, ValueError):
        actual = previous
    movement = pygame.Vector2(actual) - previous
    if movement.length_squared() > 0.04:
        oyuncu_yonu = v84_direction_name(movement)
    if progress >= 1.0 or pygame.Vector2(actual).distance_to(state.exit) <= 1.5:
        state.active = False
    return True
# </POTBO_STAGE S1877>

# <POTBO_STAGE S1888>


def v84_timing_contract():
    burst = V84_EXECUTION_BEAT_TIMES[3:13]
    burst_intervals = tuple(b - a for a, b in zip(burst, burst[1:]))
    return {
        "strict_guard_in_range": 120 <= V84_PERFECT_GUARD_STRICT_MS <= 160,
        "standard_guard_in_range": 120 <= V84_PERFECT_GUARD_STANDARD_MS <= 160,
        "riposte_window_in_range": 600 <= V84_RIPOSTE_WINDOW_MS <= 800,
        "execution_beats_monotonic": all(
            current > previous
            for previous, current in zip(
                V84_EXECUTION_BEAT_TIMES,
                V84_EXECUTION_BEAT_TIMES[1:],
            )
        ),
        "three_readable_openers": V84_EXECUTION_BEAT_TIMES[:3] == (340, 900, 1385),
        "ten_hit_burst": len(burst) == 10,
        "burst_is_ultrafast": bool(burst_intervals) and max(burst_intervals) <= 70,
        "retreat_ms": V85_EXECUTION_RETREAT_END_MS - V85_EXECUTION_REPOSITION_END_MS,
        "final_after_retreat": V84_EXECUTION_BEAT_TIMES[-1]
        > V85_EXECUTION_RETREAT_END_MS,
        "intervals_ms": tuple(
            current - previous
            for previous, current in zip(
                V84_EXECUTION_BEAT_TIMES,
                V84_EXECUTION_BEAT_TIMES[1:],
            )
        ),
    }
# </POTBO_STAGE S1888>

# <POTBO_STAGE S1892>


# =========================================================
# END V85
# =========================================================


# =========================================================
# V86 - RHYTHMIC X EXECUTION / RESPONSIVE GUARD
# =========================================================
# The three opening attacks deliberately breathe: a measured placement, an
# X-special-speed crossing, then a held stance.  The compressed middle is not a
# single saw-line.  Every one of its eighteen physical attacks owns an irregular
# crossed trace while still applying exactly one cut and one damage event.

V86_VERSION = "86.0"

V86_EXECUTION_OPENERS = (
    {
        "stage_start": 0,
        "stage_end": 300,
        "dash_start": 300,
        "dash_end": 408,
        "impact": 372,
        "pose_end": 720,
        "phase": "dash_flat",
    },
    {
        "stage_start": 720,
        "stage_end": 1030,
        "dash_start": 1030,
        "dash_end": 1130,
        "impact": 1092,
        "pose_end": 1450,
        "phase": "dash_diagonal",
    },
    {
        "stage_start": 1450,
        "stage_end": 1760,
        "dash_start": 1760,
        "dash_end": 1860,
        "impact": 1822,
        "pose_end": 2180,
        "phase": "dash_reverse",
    },
)
V86_EXECUTION_BURST_COUNT = 18
V86_EXECUTION_BURST_START_MS = 2210
V86_EXECUTION_BURST_STEP_MS = 70
V86_EXECUTION_BURST_TRAVEL_MS = 66
V86_EXECUTION_BURST_IMPACT_OFFSET_MS = 35
V86_EXECUTION_REPOSITION_START_MS = 3510
V86_EXECUTION_REPOSITION_END_MS = 4050
V86_EXECUTION_RETREAT_END_MS = 6350
V86_EXECUTION_FINAL_END_MS = 6710
V86_EXECUTION_FINAL_IMPACT_MS = 6555
V86_EXECUTION_TOTAL_MS = V86_EXECUTION_FINAL_IMPACT_MS + 720
V86_EXECUTION_BURST_ANGLES = (
    31.0,
    -52.0,
    67.0,
    -23.0,
    46.0,
    -71.0,
    18.0,
    -39.0,
    74.0,
    -29.0,
    55.0,
    -63.0,
    12.0,
    -44.0,
    69.0,
    -17.0,
    38.0,
    -58.0,
)

V84_EXECUTION_BEAT_TIMES = (
    tuple(opener["impact"] for opener in V86_EXECUTION_OPENERS)
    + tuple(
        V86_EXECUTION_BURST_START_MS
        + index * V86_EXECUTION_BURST_STEP_MS
        + V86_EXECUTION_BURST_IMPACT_OFFSET_MS
        for index in range(V86_EXECUTION_BURST_COUNT)
    )
    + (V86_EXECUTION_FINAL_IMPACT_MS,)
)
V84_EXECUTION_END_LINGER_MS = 720
V84_EXECUTION_TRACE_LIFE_MS = 510
V84_EXECUTION_MAX_FRAGMENTS = 40

# Compatibility names are intentionally updated as well.  Older diagnostics and
# helpers may inspect these values, but the functions below are the final motion
# authority.
V85_EXECUTION_TOTAL_MS = V86_EXECUTION_TOTAL_MS
V85_EXECUTION_BURST_START_MS = V86_EXECUTION_BURST_START_MS
V85_EXECUTION_BURST_STEP_MS = V86_EXECUTION_BURST_STEP_MS
V85_EXECUTION_BURST_TRAVEL_MS = V86_EXECUTION_BURST_TRAVEL_MS
V85_EXECUTION_REPOSITION_START_MS = V86_EXECUTION_REPOSITION_START_MS
V85_EXECUTION_REPOSITION_END_MS = V86_EXECUTION_REPOSITION_END_MS
V85_EXECUTION_RETREAT_END_MS = V86_EXECUTION_RETREAT_END_MS
V85_EXECUTION_FINAL_END_MS = V86_EXECUTION_FINAL_END_MS
V85_EXECUTION_AFTERIMAGE_INTERVAL_MS = 22
V85_EXECUTION_TRAIL_LIFE_MS = 280
# </POTBO_STAGE S1892>

# <POTBO_STAGE S1894>


def v84_execution_player_position(elapsed_ms):
    state = v84_execution_state
    points = state.choreography_points
    expected = 7 + V86_EXECUTION_BURST_COUNT + 3
    if len(points) < expected:
        return pygame.Vector2(state.player_start)
    elapsed = float(elapsed_ms)

    for opener_index, opener in enumerate(V86_EXECUTION_OPENERS):
        previous_index = 0 if opener_index == 0 else opener_index * 2
        stage_index = opener_index * 2 + 1
        exit_index = opener_index * 2 + 2
        if elapsed <= opener["stage_end"]:
            state.motion_phase = f"opener_{opener_index + 1}_slow"
            return v85_execution_segment_position(
                elapsed,
                opener["stage_start"],
                opener["stage_end"],
                points[previous_index],
                points[stage_index],
                v84_smootherstep,
            )
        if elapsed <= opener["dash_end"]:
            state.motion_phase = opener["phase"]
            return v85_execution_segment_position(
                elapsed,
                opener["dash_start"],
                opener["dash_end"],
                points[stage_index],
                points[exit_index],
                v85_ease_out,
            )
        if elapsed < opener["pose_end"]:
            state.motion_phase = f"opener_{opener_index + 1}_pose"
            return pygame.Vector2(points[exit_index])

    burst_first_point = 6
    for index in range(V86_EXECUTION_BURST_COUNT):
        start_ms = V86_EXECUTION_BURST_START_MS + index * V86_EXECUTION_BURST_STEP_MS
        end_ms = start_ms + V86_EXECUTION_BURST_TRAVEL_MS
        start_index = burst_first_point + index
        end_index = start_index + 1
        if elapsed < start_ms:
            state.motion_phase = "burst_hold"
            return pygame.Vector2(points[start_index])
        if elapsed <= end_ms:
            state.motion_phase = "burst"
            return v85_execution_segment_position(
                elapsed,
                start_ms,
                end_ms,
                points[start_index],
                points[end_index],
                v85_ease_out,
            )

    burst_end_index = 6 + V86_EXECUTION_BURST_COUNT
    behind_index = burst_end_index + 1
    retreat_index = burst_end_index + 2
    final_index = burst_end_index + 3
    if elapsed < V86_EXECUTION_REPOSITION_START_MS:
        state.motion_phase = "burst_hold"
        return pygame.Vector2(points[burst_end_index])
    if elapsed <= V86_EXECUTION_REPOSITION_END_MS:
        state.motion_phase = "reposition"
        local = (elapsed - V86_EXECUTION_REPOSITION_START_MS) / max(
            1.0,
            V86_EXECUTION_REPOSITION_END_MS - V86_EXECUTION_REPOSITION_START_MS,
        )
        target = pygame.Vector2(state.target.x, state.target.y)
        start = pygame.Vector2(points[burst_end_index])
        end = pygame.Vector2(points[behind_index])
        radial = v84_safe_vector(start - target).normalize()
        control = target + radial.rotate(82.0) * 108.0
        return _gelistirici_x_skill_bezier(start, control, end, local)
    if elapsed <= V86_EXECUTION_RETREAT_END_MS:
        state.motion_phase = "retreat"
        return v85_execution_segment_position(
            elapsed,
            V86_EXECUTION_REPOSITION_END_MS,
            V86_EXECUTION_RETREAT_END_MS,
            points[behind_index],
            points[retreat_index],
            v84_smootherstep,
        )
    if elapsed <= V86_EXECUTION_FINAL_END_MS:
        state.motion_phase = "final_dash"
        state.final_dash_started = True
        return v85_execution_segment_position(
            elapsed,
            V86_EXECUTION_RETREAT_END_MS,
            V86_EXECUTION_FINAL_END_MS,
            points[retreat_index],
            points[final_index],
            v85_ease_out,
        )
    state.motion_phase = "aftermath"
    return pygame.Vector2(points[final_index])


def v84_execution_cut_parameters(index, state):
    rng = random.Random(int(state.seed) ^ ((int(index) + 1) * 0x86D9F3B))
    points = state.choreography_points
    if index < 3:
        start_index = index * 2 + 1
        end_index = index * 2 + 2
        motion = pygame.Vector2(points[end_index]) - pygame.Vector2(points[start_index])
        return (
            motion.as_polar()[1],
            1.18 + index * 0.035,
            rng.uniform(-0.075, 0.075),
        )
    burst_last = 3 + V86_EXECUTION_BURST_COUNT
    if index < burst_last:
        burst_index = index - 3
        start_index = 6 + burst_index
        end_index = start_index + 1
        motion = pygame.Vector2(points[end_index]) - pygame.Vector2(points[start_index])
        return (
            motion.as_polar()[1] + rng.uniform(-6.0, 6.0),
            rng.uniform(0.96, 1.24),
            rng.uniform(-0.19, 0.19),
        )
    retreat_index = 7 + V86_EXECUTION_BURST_COUNT + 1
    final_index = retreat_index + 1
    motion = pygame.Vector2(points[final_index]) - pygame.Vector2(points[retreat_index])
    return (
        motion.as_polar()[1],
        1.55,
        rng.uniform(-0.035, 0.035),
    )
# </POTBO_STAGE S1894>

# <POTBO_STAGE S1896>


def v84_execution_apply_cut(index, now):
    global v85_execution_flash_started_ms
    global v85_execution_flash_until_ms
    state = v84_execution_state
    target = state.target
    if target is None or state.fracture is None:
        return
    angle, length_scale, offset = v84_execution_cut_parameters(index, state)
    final_index = len(V84_EXECUTION_BEAT_TIMES) - 1
    final = index == final_index
    made = v85_fracture_cut_one(
        state.fracture,
        angle,
        offset,
        0.58 + min(1.38, index * 0.062),
        state.seed + index * 991,
        detach=not final,
    )
    state.detached_fragments = int(getattr(state, "detached_fragments", 0)) + int(made)
    trace = v86_execution_trace(target, state, index, angle, length_scale, now, final)

    # Eighteen rapid attacks are eighteen irregular Xs.  The companion stroke is
    # visual only: it enriches the silhouette without double-damaging or cutting
    # twice during one authored physical attack.
    if 3 <= index < 3 + V86_EXECUTION_BURST_COUNT:
        rng = random.Random(state.seed ^ (index * 0xB16B00B5))
        cross_angle = angle + rng.choice((-1.0, 1.0)) * rng.uniform(69.0, 111.0)
        cross = v86_execution_trace(
            target,
            state,
            index,
            cross_angle,
            length_scale * rng.uniform(0.73, 0.96),
            now,
            False,
        )
        trace.v86_pair = id(cross)
        cross.v86_pair = id(trace)
        cross.v86_cross = True

    state.cuts_landed += 1
    v84_execution_cut_blood(target, index, angle, final=final)
    if not final:
        v85_execution_cut_tissue(target, index, angle)
    shake = 2.8 + min(4.1, index * 0.22)
    duration = 78 + min(60, index * 4)
    if 3 <= index < 3 + V86_EXECUTION_BURST_COUNT:
        shake = 3.9 + (index % 4) * 0.46
        duration = 56
    if final:
        shake = 12.4
        duration = 300
        v85_execution_flash_started_ms = int(now)
        v85_execution_flash_until_ms = int(now) + 205
        state.final_dash_impact = True
    kamera_hit_sarsintisi_baslat(shake, duration)
    if final:
        v84_execution_finalize(now, trace)
# </POTBO_STAGE S1896>

# <POTBO_STAGE S1900>
V84_RIPOSTE_ATTACK_MS = 320
SAVUNMA_TUTMA_STAMINA_SANIYE = 17.0
# </POTBO_STAGE S1900>

# <POTBO_STAGE S1902>


def v84_perfect_guard_possible(
    source_type,
    source_x,
    source_y,
    attacker,
    now=None,
):
    if now is None:
        now = pygame.time.get_ticks()
    guard_intent = bool(oyuncu_savunuyor) or int(now) <= int(v86_guard_intent_until_ms)
    if oyuncu_hp <= 0 or not guard_intent:
        return False
    if v84_execution_state.active:
        return False
    if v84_guard_quality(now) <= 0.0:
        return False
    if not v84_source_in_front(source_x, source_y):
        return False
    return v84_direct_melee_source(
        source_type,
        source_x,
        source_y,
        attacker,
    )
# </POTBO_STAGE S1902>

# <POTBO_STAGE S1905>


# =========================================================
# END V86 EXECUTION / GUARD
# =========================================================


# =========================================================
# V86 - ENEMY-AUTHORED 3/4-TOP-DOWN DEATH DIRECTOR
# =========================================================
# This renderer never draws fracture seams or holds pieces together with gaps.
# An intact remainder and independently cropped solid pieces are the only body
# primitives.  Their x/y motion lives on the map plane; z is merely flight above
# that plane.  Consequently a fallen body lies across the floor instead of
# dropping toward the bottom edge like a platform-game object.

V86_DEATH_FRONT_WAIT_MS = 1000
# </POTBO_STAGE S1905>

# <POTBO_STAGE S1921>


# The former V85 mortal-follow-through delayed HP=0 and replayed one generic hit.
# V86 records inherited hit feedback as nonlethal, restores zero immediately, then
# starts the correct authored director.  This removes the unwanted shared prelude
# without bypassing established damage flash, telemetry or ordinary blood ecology.
_v86_player_damage_original = oyuncu_kanli_hasar_kaydi


def oyuncu_kanli_hasar_kaydi(kaynak_x, kaynak_y, profil, hasar, kaynak_adi=""):
    global oyuncu_hp, hp_gorunen, v85_forcing_final_hit
    now = pygame.time.get_ticks()
    killer = v85_direct_killer(kaynak_x, kaynak_y, kaynak_adi)
    if oyuncu_hp > 0:
        result = _v86_player_damage_original(
            kaynak_x, kaynak_y, profil, hasar, kaynak_adi
        )
        if int(hasar) > 0:
            v86_history_record(killer, hasar, now)
        return result
    if v86_death_state.active:
        return 0

    actual_damage = max(1, int(hasar))
    saved_hp = int(oyuncu_hp)
    oyuncu_hp = max(actual_damage + 2, int(oyuncu_max_hp) + 1)
    v85_mortal_wound_state.reset()
    v85_forcing_final_hit = False
    try:
        result = _v86_player_damage_original(
            kaynak_x, kaynak_y, profil, hasar, kaynak_adi
        )
    finally:
        oyuncu_hp = min(0, saved_hp)
        hp_gorunen = 0.0
        v85_mortal_wound_state.reset()
        v85_forcing_final_hit = False
    v86_death_scene_begin(
        killer,
        kaynak_x,
        kaynak_y,
        profil,
        actual_damage,
        kaynak_adi,
    )
    return result
# </POTBO_STAGE S1921>

# <POTBO_STAGE S1945>

# Exact three-layer language used by gelistirici_x_skill_efekt_ciz().
V87_SPECIAL_CUT_DARK = (88, 0, 14)
# </POTBO_STAGE S1945>

# <POTBO_STAGE S1947>
V87_EXECUTION_CUT_REVEAL_MS = 56
V87_EXECUTION_CUT_HOLD_MS = 148
V87_EXECUTION_SPARK_LIFE_MS = 115
V87_EXECUTION_SLASH_LAYER_SIZE = 360
v87_execution_slash_layer = pygame.Surface(
    (V87_EXECUTION_SLASH_LAYER_SIZE, V87_EXECUTION_SLASH_LAYER_SIZE),
    pygame.SRCALPHA,
).convert_alpha()
# </POTBO_STAGE S1947>

# <POTBO_STAGE S1957>


def v87_execution_cut_alpha(age, life):
    if age < 0 or age > life:
        return 0.0
    if age <= V87_EXECUTION_CUT_HOLD_MS:
        return 1.0
    return (
        v84_clamp01(
            1.0
            - (age - V87_EXECUTION_CUT_HOLD_MS)
            / max(1.0, life - V87_EXECUTION_CUT_HOLD_MS)
        )
        ** 1.45
    )
# </POTBO_STAGE S1957>

# <POTBO_STAGE S1960>


def v87_repeating_attack_progress(local_ms, step_ms, impact_ms):
    phase = max(0.0, min(1.0, float(local_ms) / max(1.0, step_ms)))
    impact_phase = float(impact_ms) / max(1.0, float(step_ms))
    if phase <= impact_phase:
        return 0.70 * v84_smootherstep(phase / max(0.01, impact_phase))
    recovery = (phase - impact_phase) / max(0.01, 1.0 - impact_phase)
    return 0.70 + 0.30 * v84_smoothstep(recovery)
# </POTBO_STAGE S1960>

# <POTBO_STAGE S1973>


_v87_execution_update_original = v84_execution_update
# </POTBO_STAGE S1973>

# <POTBO_STAGE S1994>


v88_damage_serial = 0
v88_damage_source_stack = []
v88_recent_damage_events = []
# </POTBO_STAGE S1994>

# <POTBO_STAGE S1996>


def v88_next_damage_serial():
    global v88_damage_serial
    v88_damage_serial += 1
    return int(v88_damage_serial)
# </POTBO_STAGE S1996>

# <POTBO_STAGE S2002>


def v88_current_damage_source():
    return v88_damage_source_stack[-1] if v88_damage_source_stack else None
# </POTBO_STAGE S2002>

# <POTBO_STAGE S2004>


def v88_call_with_damage_source(provenance, callback, *args, **kwargs):
    v88_damage_source_stack.append(provenance)
    if provenance.source_kind == "projectile":
        v88_attribution_stats["scoped_projectile"] += 1
    elif provenance.source_kind == "melee":
        v88_attribution_stats["scoped_melee"] += 1
    try:
        return callback(*args, **kwargs)
    finally:
        # Nested combat callbacks are legal.  Remove the exact record even if a
        # defensive wrapper raised after another source was pushed.
        if v88_damage_source_stack and v88_damage_source_stack[-1] is provenance:
            v88_damage_source_stack.pop()
        else:
            try:
                v88_damage_source_stack.remove(provenance)
            except ValueError:
                pass


def v88_lethal_event_matches_call(event, source_x, source_y, source_name):
    if event is None:
        return False
    current = v88_current_damage_source()
    if current is not None and int(current.event_id) == int(event.provenance_id):
        return True
    if v88_name_key(event.source_name) != v88_name_key(source_name):
        return False
    point = pygame.Vector2(float(source_x), float(source_y))
    return point.distance_squared_to(event.source_position) <= 4.0
# </POTBO_STAGE S2004>

# <POTBO_STAGE S2006>


_v88_player_damage_original = oyuncu_kanli_hasar_kaydi


def oyuncu_kanli_hasar_kaydi(
    kaynak_x,
    kaynak_y,
    profil,
    hasar,
    kaynak_adi="",
):
    global v88_lethal_event
    v88_record_damage_for_diagnostics(
        kaynak_x,
        kaynak_y,
        profil,
        hasar,
        kaynak_adi,
    )
    newly_frozen = False
    if (
        int(hasar) > 0
        and int(oyuncu_hp) <= 0
        and not bool(v86_death_state.active)
        and v88_lethal_event is None
    ):
        v88_lethal_event = v88_build_lethal_event(
            kaynak_x,
            kaynak_y,
            profil,
            hasar,
            kaynak_adi,
        )
        newly_frozen = True
        v88_attribution_stats["lethal_frozen"] += 1
    elif bool(v86_death_state.active) and int(hasar) > 0:
        v88_attribution_stats["post_lethal_rejected"] += 1

    result = _v88_player_damage_original(
        kaynak_x,
        kaynak_y,
        profil,
        hasar,
        kaynak_adi,
    )
    # A defensive rollback only applies if an inherited guard converted the
    # apparent lethal contact back into a living state and no director claimed it.
    if newly_frozen and not v86_death_state.active and int(oyuncu_hp) > 0:
        v88_lethal_event = None
    return result
# </POTBO_STAGE S2006>

# <POTBO_STAGE S2008>


def _v88_common_attack_update(self, simdi):
    provenance = v88_make_damage_source(self, "melee", self)
    return v88_call_with_damage_source(
        provenance,
        _v88_common_attack_update_original,
        self,
        simdi,
    )
# </POTBO_STAGE S2008>

# <POTBO_STAGE S2014>


def v88_enforce_death_physics_ownership():
    """Once death starts, combat knockback can no longer move the victim state."""
    global oyuncu_zorlanmis_bitis, oyuncu_zorlanmis_son_guncelleme
    global oyuncu_hareket_ediyor, dash_aktif_bitis, dash_aktif_son_ease
    global dash_tus_kilitli
    if not bool(v86_death_state.active):
        return False
    oyuncu_zorlanmis_hiz.update(0.0, 0.0)
    oyuncu_zorlanmis_bitis = 0
    oyuncu_zorlanmis_son_guncelleme = int(pygame.time.get_ticks())
    oyuncu_hareket_hiz_vektoru.update(0.0, 0.0)
    oyuncu_hareket_ediyor = False
    dash_aktif_yonu.update(0.0, 0.0)
    dash_aktif_bitis = 0
    dash_aktif_son_ease = 0.0
    dash_tus_kilitli = True
    return True
# </POTBO_STAGE S2014>

# <POTBO_STAGE S2017>


_v88_execution_player_hit_original = oyuncu_infaz_darbesi_uygula
# </POTBO_STAGE S2017>

# <POTBO_STAGE S2024>


def v88_repeating_death_scheduler_reset(state, attack, kind):
    spec = v88_repeating_death_spec(kind)
    state.v88_hit_scheduler_kind = str(kind)
    state.v88_hits_done = 0
    state.v88_next_hit_ms = int(attack) + int(spec["impact_ms"])
    state.v88_last_hit_ms = 0
    state.v88_scheduler_complete_ms = 0
    state.v88_max_hits_in_one_update = 0


def v88_repeating_death_scheduler_ready(state, attack, kind):
    if (
        str(getattr(state, "v88_hit_scheduler_kind", "")) != str(kind)
        or not hasattr(state, "v88_next_hit_ms")
        or int(getattr(state, "v88_next_hit_ms", 0)) <= 0
    ):
        v88_repeating_death_scheduler_reset(state, attack, kind)
# </POTBO_STAGE S2024>

# <POTBO_STAGE S2120>


# =========================================================
# END V89
# =========================================================


# =========================================================
# V90 - SOMATIC INJURY / DRACO CALCINANS
# =========================================================

V90_VERSION = "90.0"
# </POTBO_STAGE S2120>

# <POTBO_STAGE S2128>
V90_DRACO_STAMINA_COST = 14.0
# </POTBO_STAGE S2128>

# <POTBO_STAGE S2139>
V90_BASE_ATTACK_COST = float(SALDIRI_STAMINA_MALIYETI)
# </POTBO_STAGE S2139>

# <POTBO_STAGE S2141>
V90_BASE_ATTACK_COOLDOWN = int(saldiri_bekleme_suresi)
V90_BASE_DASH_COST = float(DASH_STAMINA_MALIYETI)
V90_BASE_DASH_DISTANCE = float(DASH_MESAFESI)
V90_BASE_GUARD_DRAIN = float(SAVUNMA_TUTMA_STAMINA_SANIYE)
# </POTBO_STAGE S2141>

# <POTBO_STAGE S2144>


v90_injury = V90InjuryState(last_hp=float(oyuncu_hp))
# </POTBO_STAGE S2144>

# <POTBO_STAGE S2151>


def v90_injury_recalculate():
    hp_ratio = v90_hp_ratio()
    critical = v90_smoothstep(v90_clamp((0.34 - hp_ratio) / 0.26))
    low_stamina = 1.0 - v90_clamp(
        float(oyuncu_stamina) / max(1.0, float(oyuncu_max_stamina))
    )
    severity = v90_injury_severity()
    v90_injury.effective_stamina_ratio = v90_clamp(
        1.0
        - v90_injury.tissue * 0.22
        - v90_injury.shock * 0.15
        - critical * 0.10,
        0.56,
        1.0,
    )
    v90_injury.stamina_regen_multiplier = v90_clamp(
        1.0
        - severity * 0.54
        - critical * 0.25
        - v90_injury.exertion * 0.18,
        0.18,
        1.0,
    )
    v90_injury.movement_multiplier = v90_clamp(
        1.0
        - v90_injury.tissue * 0.18
        - critical * 0.29
        - v90_injury.shock * 0.08
        - max(0.0, low_stamina - 0.72) * 0.16,
        0.52,
        1.0,
    )
    v90_injury.attack_time_multiplier = v90_clamp(
        1.0
        + v90_injury.tissue * 0.22
        + critical * 0.35
        + v90_injury.shock * 0.09
        + max(0.0, low_stamina - 0.68) * 0.18,
        1.0,
        1.62,
    )
# </POTBO_STAGE S2151>

# <POTBO_STAGE S2154>


_v90_player_damage_raw = oyuncu_kanli_hasar_kaydi


def oyuncu_kanli_hasar_kaydi(kaynak_x, kaynak_y, profil, hasar, kaynak_adi=""):
    result = _v90_player_damage_raw(
        kaynak_x,
        kaynak_y,
        profil,
        hasar,
        kaynak_adi,
    )
    # Every combat resolver subtracts HP immediately before publishing this
    # canonical damage event; `hasar` is therefore the post-mitigation amount.
    # Comparing HP around the event would always yield zero.
    if int(hasar) > 0 and int(oyuncu_hp) > 0:
        v90_injury_register_damage(int(hasar), profil)
    return result


_v90_stamina_update_raw = stamina_guncelle


def stamina_guncelle():
    global oyuncu_stamina
    before = float(oyuncu_stamina)
    _v90_stamina_update_raw()
    gained = max(0.0, float(oyuncu_stamina) - before)
    if gained > 0.0:
        oyuncu_stamina = before + gained * v90_injury.stamina_regen_multiplier
    v90_injury_recalculate()
    oyuncu_stamina = min(
        float(oyuncu_stamina),
        float(oyuncu_max_stamina) * v90_injury.effective_stamina_ratio,
    )
# </POTBO_STAGE S2154>

# <POTBO_STAGE S2156>


def oyuncu_serbest_hareket_guncelle():
    global OYUNCU_YURUYUS_HIZI
    previous = float(OYUNCU_YURUYUS_HIZI)
    OYUNCU_YURUYUS_HIZI = V90_BASE_WALK_SPEED * v90_injury.movement_multiplier
    try:
        return _v90_free_move_raw()
    finally:
        OYUNCU_YURUYUS_HIZI = previous


_v90_attack_duration_raw = oyuncu_aktif_saldiri_suresi_ms


def oyuncu_aktif_saldiri_suresi_ms():
    duration = int(_v90_attack_duration_raw())
    if duration >= 10**8:
        return duration
    return max(1, int(round(duration * v90_injury.attack_time_multiplier)))


_v90_attack_damage_raw = oyuncu_saldiri_hasar_miktari


def oyuncu_saldiri_hasar_miktari():
    # "Heavy" here means laboured commitment, not the implausible reward of
    # becoming stronger while exsanguinating.
    scalar = 1.0 - 0.10 * v90_injury_severity()
    return max(1, int(round(_v90_attack_damage_raw() * scalar)))
# </POTBO_STAGE S2156>

# <POTBO_STAGE S2158>


_v90_dash_raw = oyuncu_dash_yap


def oyuncu_dash_yap(dx, dy):
    global DASH_STAMINA_MALIYETI, DASH_MESAFESI
    previous_cost = float(DASH_STAMINA_MALIYETI)
    previous_distance = float(DASH_MESAFESI)
    DASH_STAMINA_MALIYETI = (
        V90_BASE_DASH_COST * (1.0 + 0.30 * v90_injury_severity())
    )
    DASH_MESAFESI = V90_BASE_DASH_DISTANCE * (
        0.86 + 0.14 * v90_injury.movement_multiplier
    )
    try:
        result = _v90_dash_raw(dx, dy)
    finally:
        DASH_STAMINA_MALIYETI = previous_cost
        DASH_MESAFESI = previous_distance
    if result:
        v90_injury.exertion = v90_clamp(v90_injury.exertion + 0.12)
    return result
# </POTBO_STAGE S2158>

# <POTBO_STAGE S2160>


def secili_itemi_kullan(item_index):
    before = float(oyuncu_hp)
    result = _v90_item_use_raw(item_index)
    healed = max(0.0, float(oyuncu_hp) - before)
    if healed > 0.0:
        v90_injury_relieve(healed)
    return result
# </POTBO_STAGE S2160>

# <POTBO_STAGE S2201>


# Correct dash exertion accounting even though the inherited dash function
# intentionally returns None on success.
_v90_dash_cost_wrapper = oyuncu_dash_yap


def oyuncu_dash_yap(dx, dy):
    before = float(oyuncu_stamina)
    result = _v90_dash_cost_wrapper(dx, dy)
    if float(oyuncu_stamina) < before - 0.01:
        v90_injury.exertion = v90_clamp(v90_injury.exertion + 0.12)
    return result
# </POTBO_STAGE S2201>

# <POTBO_STAGE S2266>


# ---------------------------------------------------------
# Level progression replaces the level-unlocked passive-technique strip.
# The old mechanics remain callable but contribute no level-derived bonuses.
# ---------------------------------------------------------
def v52_unlocked_skill_ids(level=None, gender=None):
    return tuple()


def v52_effect_totals(force=False):
    global v52_skill_cache_key, v52_skill_cache, v52_last_unlocked
    v52_skill_cache_key = (int(oyuncu_level), str(karakter_cinsiyet))
    v52_skill_cache = {}
    v52_last_unlocked = tuple()
    return {}


def v52_recent_skill_names(limit=5):
    return []


def v52_skill_strip_ciz():
    return None
# </POTBO_STAGE S2266>

# <POTBO_STAGE S2271>


def oyuncu_serbest_hareket_guncelle():
    global V90_BASE_WALK_SPEED
    # V90's injury wrapper derives the live walking speed from this baseline, so
    # V92 scales that canonical baseline instead of fighting the wrapper one frame
    # later.  The temporary change also means wounds still multiply correctly.
    base = float(V90_BASE_WALK_SPEED)
    # ~20% maximum level contribution before equipment; noticeable, not absurd.
    level_mult = min(1.20, 1.0 + float(v92_level_stats.get("speed", 0.0)))
    equipment_mult = v92_equipment_speed_multiplier()
    V90_BASE_WALK_SPEED = base * level_mult * equipment_mult
    try:
        return _v92_free_move_raw()
    finally:
        V90_BASE_WALK_SPEED = base
# </POTBO_STAGE S2271>

# <POTBO_STAGE S2308>


_v92_player_damage_raw = oyuncu_kanli_hasar_kaydi
# </POTBO_STAGE S2308>

# <POTBO_STAGE S2311>


# ---------------------------------------------------------
# Decussatio Rubra: the existing three-cut X special becomes a learned skill.
# If its complete three-hit prediction is lethal, it hands the target to the
# authored execution director. Range remains intentionally short.
# ---------------------------------------------------------
V92_X_SPECIAL_NAME = "Decussatio Rubra"
# </POTBO_STAGE S2311>

# <POTBO_STAGE S2313>

_v92_x_release_raw = gelistirici_x_skill_r_birak
# </POTBO_STAGE S2313>

# <POTBO_STAGE S2315>


# ---------------------------------------------------------
# Catena Decollationis: J + dash attacks sequential targets in the facing cone.
# Aligned targets produce a straight line; diagonal arrangements naturally build
# a zig-zag polyline. If every predicted hit is lethal, the scene becomes a
# black/red decapitation tableau with fast cuts and slow-flying heads.
# ---------------------------------------------------------
V92_CHAIN_NAME = "Catena Decollationis"
# </POTBO_STAGE S2315>

# <POTBO_STAGE S2317>
V92_CHAIN_EXECUTION_MS = 1420
# </POTBO_STAGE S2317>

# <POTBO_STAGE S2320>


@dataclass
class V92ChainState:
    active: bool = False
    execution: bool = False
    started_ms: int = 0
    last_ms: int = 0
    targets: list = field(default_factory=list)
    points: list = field(default_factory=list)
    hit_mask: int = 0
    damage: int = 0
    duration_ms: int = 0
    heads: list = field(default_factory=list)
    silhouettes: list = field(default_factory=list)
    start_player: pygame.Vector2 = field(default_factory=pygame.Vector2)
    final_player: pygame.Vector2 = field(default_factory=pygame.Vector2)

    def reset(self):
        self.active = False
        self.execution = False
        self.started_ms = 0
        self.last_ms = 0
        self.targets = []
        self.points = []
        self.hit_mask = 0
        self.damage = 0
        self.duration_ms = 0
        self.heads = []
        self.silhouettes = []
        self.start_player = pygame.Vector2()
        self.final_player = pygame.Vector2()
# </POTBO_STAGE S2320>

# <POTBO_STAGE S2326>


def v92_chain_update(now=None):
    global oyuncu_x, oyuncu_y
    state = v92_chain_state
    if not state.active:
        return
    if now is None:
        now = pygame.time.get_ticks()
    elapsed = max(0, int(now) - int(state.started_ms))
    duration = max(1, int(state.duration_ms))
    p = min(1.0, elapsed / duration)
    motion_p = min(1.0, p / (0.43 if state.execution else 0.78))
    pos = v92_chain_polyline_position(motion_p)
    oyuncu_x, oyuncu_y = float(pos.x), float(pos.y)
    # Hits are distributed over the fast motion segment in target order.
    for index in range(len(state.targets)):
        threshold = (index + 1) / (len(state.targets) + 1) * (0.40 if state.execution else 0.72)
        if p >= threshold:
            v92_chain_hit_target(index, now)
    dt = max(0.0, min(0.05, (int(now) - int(state.last_ms)) / 1000.0))
    state.last_ms = int(now)
    # Heads live in deliberate slow motion relative to the cut.
    head_dt = dt * (0.24 if state.execution else 1.0)
    for head in state.heads:
        head.position += head.velocity * head_dt
        head.z += head.vz * head_dt
        head.vz -= 150.0 * head_dt
        head.velocity *= math.exp(-0.85 * head_dt)
        head.rotation += head.angular * head_dt
    if p >= 1.0:
        oyuncu_x, oyuncu_y = float(state.final_player.x), float(state.final_player.y)
        dunya_olayi_kaydet("special_chain_end", targets=len(state.targets), execution=state.execution)
        state.reset()
# </POTBO_STAGE S2326>

# <POTBO_STAGE S2330>


_v92_dash_raw = oyuncu_dash_yap


def oyuncu_dash_yap(dx, dy):
    keys = pygame.key.get_pressed()
    attack_held = bool(keys[tus_atamasi("attack")])
    if attack_held and v92_training.get("catena_decollationis", 0) >= 5:
        started = v92_chain_start(dx, dy)
        if started:
            return True
    return _v92_dash_raw(dx, dy)
# </POTBO_STAGE S2330>

# <POTBO_STAGE S2340>

# =========================================================
# END V92
# =========================================================


# =========================================================
# V94 - INPUT / TIMING / SKILLS / PERFORMANCE HOTFIX
# This layer is intentionally placed BEFORE the blocking main loop.
# =========================================================
V94_VERSION = "94.0"
# </POTBO_STAGE S2340>

# <POTBO_STAGE S2344>

# More aggressive cosmetic budgets. Combat hit resolution is untouched.
V63_TIER_HYSTERESIS_MS = 520
# </POTBO_STAGE S2344>

# <POTBO_STAGE S2360>


# ---------------------------------------------------------
# Learned skills: HOLD means HOLD. Catena requires 5 trainings, a real charged J,
# at least two chainable living targets, and a short recovery window. Otherwise
# the input falls through to an ordinary dash.
# ---------------------------------------------------------
V92_CHAIN_EXECUTION_MS = 1180
# </POTBO_STAGE S2360>

# <POTBO_STAGE S2363>


_v94_x_arm_previous = gelistirici_x_skill_r_baslat


def gelistirici_x_skill_r_baslat(simdi=None):
    if simdi is None:
        simdi = pygame.time.get_ticks()
    if v92_training.get("decussatio_rubra", 0) < 5 or not _v94_hold_ready(simdi):
        return False
    return _v94_x_arm_previous(simdi)
# </POTBO_STAGE S2363>

# <POTBO_STAGE S2366>


# Robust dash wrapper: does not trigger Catena merely because J happened to be down.
# The normal dash remains authoritative unless the learned, charged skill actually starts.
_v94_dash_previous = _v92_dash_raw


def oyuncu_dash_yap(dx, dy):
    if v92_training.get("catena_decollationis", 0) >= 5 and _v94_hold_ready():
        if v92_chain_start(dx, dy):
            return True
    return _v94_dash_previous(dx, dy)


def v92_chain_update(now=None):
    global oyuncu_x, oyuncu_y
    state = v92_chain_state
    if not state.active:
        return
    if now is None:
        now = pygame.time.get_ticks()
    elapsed = max(0, int(now) - int(state.started_ms))
    duration = max(1, int(state.duration_ms))
    p = min(1.0, elapsed / duration)
    motion_window = 0.29 if state.execution else 0.60
    motion_p = min(1.0, p / motion_window)
    pos = v92_chain_polyline_position(motion_p)
    oyuncu_x, oyuncu_y = float(pos.x), float(pos.y)
    hit_window = 0.27 if state.execution else 0.56
    for index in range(len(state.targets)):
        threshold = (index + 1) / (len(state.targets) + 1) * hit_window
        if p >= threshold:
            v92_chain_hit_target(index, now)
    dt = max(0.0, min(0.05, (int(now) - int(state.last_ms)) / 1000.0))
    state.last_ms = int(now)
    head_dt = dt * (0.17 if state.execution else 0.82)
    for head in state.heads:
        head.position += head.velocity * head_dt
        head.z += head.vz * head_dt
        head.vz -= 150.0 * head_dt
        head.velocity *= math.exp(-0.85 * head_dt)
        head.rotation += head.angular * head_dt
    if p >= 1.0:
        oyuncu_x, oyuncu_y = float(state.final_player.x), float(state.final_player.y)
        dunya_olayi_kaydet("special_chain_end", targets=len(state.targets), execution=state.execution)
        state.reset()
# </POTBO_STAGE S2366>

# <POTBO_STAGE S2417>

# ---------------------------------------------------------
# STATUS ICON ASSETS
# Kullanıcının istediği canonical yollar:
#   assets/ui/health_icon.png
#   assets/ui/mana_icon.png
#   assets/ui/stamina_icon.png
# Proje kökündeki ui/ klasörü de güvenli fallback'tir.
# ---------------------------------------------------------
V98_HEALTH_ICON_ADAYLARI = (
    os.path.join(ASSETS, "ui", "health_icon.png"),
    os.path.join(BASE_DIR, "ui", "health_icon.png"),
)
# </POTBO_STAGE S2417>

# <POTBO_STAGE S2419>
V98_STAMINA_ICON_ADAYLARI = (
    os.path.join(ASSETS, "ui", "stamina_icon.png"),
    os.path.join(BASE_DIR, "ui", "stamina_icon.png"),
)
# </POTBO_STAGE S2419>

# <POTBO_STAGE S2431>


# ---------------------------------------------------------
# FIREBALL TRAIL - yalnız görsel, hasar vermez.
# Ateş topu ilerledikçe aynı universal ateşten kısa ömürlü izler bırakır.
# ---------------------------------------------------------
class V98ProjectileTrailFire:
    __slots__ = ("x", "y", "start_ms", "duration_ms", "phase", "scale")

    def __init__(self, x, y, simdi, seed=0):
        self.x = float(x)
        self.y = float(y)
        self.start_ms = int(simdi)
        rng = random.Random(int(seed) * 7919 + int(x * 17) + int(y * 23))
        self.duration_ms = rng.randint(420, 680)
        self.phase = rng.randrange(0, 4)
        self.scale = rng.uniform(0.62, 0.90)

    def aktif_mi(self, simdi):
        return int(simdi) - self.start_ms < self.duration_ms

    def ciz(self):
        frames = V98_UNIVERSAL_FIRE_FRAMES
        if not frames:
            return
        now = pygame.time.get_ticks()
        age = max(0, now - self.start_ms)
        progress = max(0.0, min(1.0, age / max(1.0, float(self.duration_ms))))
        fade_in = min(1.0, progress / 0.08)
        fade_out = max(0.0, (1.0 - progress) ** 0.72)
        alpha = int(round(225 * fade_in * fade_out))
        if alpha <= 0:
            return
        sequence = (0, 1, 2, 1) if len(frames) >= 3 else tuple(range(len(frames)))
        index = sequence[((age // 78) + self.phase) % len(sequence)] % len(frames)
        frame = frames[index]
        height = int(round(22 * self.scale * KAMERA_YAKINLASTIRMA))
        image = _v98_fire_frame_image(frame, height, alpha)
        if image is None:
            return
        sx = int(round(dunya_ekran_x(self.x)))
        sy = int(round(dunya_ekran_y(self.y) + 2))
        ekran.blit(image, image.get_rect(midbottom=(sx, sy)))
# </POTBO_STAGE S2431>

# <POTBO_STAGE S2443>
v99_catena_combo_latched = False
# </POTBO_STAGE S2443>

# <POTBO_STAGE S2453>


# =========================================================
# V100 - EXECUTION CONTRACT / PASSIVE SKILL BELT /
#        UNIVERSAL NEGOTIATION / CINEMATIC CLOCK /
#        CLEAN FIREBALL PRESENTATION
# =========================================================
V100_VERSION = "100.0"
# </POTBO_STAGE S2453>

# <POTBO_STAGE S2455>

# ---------------------------------------------------------
# SKILL METADATA + ICONS
# Skill slots are informational only. They never cast/activate a technique.
# ---------------------------------------------------------
V100_SKILL_META = {
    "decussatio_rubra": {
        "name": "Decussatio Rubra",
        "shortcut": bt("J basılı tut + R", "Hold J + R"),
        "description": bt(
            "Tüm gücü tek bir hedefe yönelten acımasız bir kılıç tekniğidir. "
            "Kullanıcı rakibine hızla yaklaşır ve peş peşe üç ağır kesik indirir. "
            "Ölümün eşiğindeki düşmanlara karşı uygulandığında saldırı bir infaza dönüşebilir.",
            "A ruthless sword technique that directs all force into a single target. "
            "The user closes rapidly and lands three heavy cuts in succession. "
            "Against an enemy whose death is already certain, the attack can become an execution.",
        ),
        "paths": (
            os.path.join(ASSETS, "ui", "skills", "decussatio_rubra.png"),
            os.path.join(ASSETS, "skills", "decussatio_rubra.png"),
            os.path.join(BASE_DIR, "decussatio_rubra.png"),
        ),
    },
    "catena_decollationis": {
        "name": "Catena Decollationis",
        "shortcut": bt("J basılı tut + SHIFT", "Hold J + SHIFT"),
        "description": bt(
            "Birden fazla düşmanı tek bir saldırı akışına bağlayan ileri seviye kılıç tekniğidir. "
            "Kullanıcı hedefler arasında hızla ilerleyerek karşısına çıkan düşmanları art arda keser. "
            "Birbirine yakın düşmanlara karşı kullanıldığında saldırı zinciri uzar ve ölümcül bir seri hâline gelir.",
            "An advanced sword technique that binds multiple enemies into one attack flow. "
            "The user moves rapidly between targets and cuts them in sequence. "
            "Against enemies positioned close together, the chain extends into a lethal series.",
        ),
        "paths": (
            os.path.join(ASSETS, "ui", "skills", "catena_decollationis.png"),
            os.path.join(ASSETS, "skills", "catena_decollationis.png"),
            os.path.join(BASE_DIR, "catena_decollationis.png"),
        ),
    },
}


def _v100_skill_image_load(paths):
    for path in paths:
        if not path or not os.path.isfile(path):
            continue
        try:
            image = pygame.image.load(path).convert_alpha()
        except (pygame.error, OSError):
            continue
        bounds = image.get_bounding_rect(min_alpha=2)
        if bounds.width > 0 and bounds.height > 0:
            return image.subsurface(bounds).copy().convert_alpha()
    return None


V100_SKILL_ICONS = {
    skill_id: _v100_skill_image_load(meta["paths"])
    for skill_id, meta in V100_SKILL_META.items()
}


def v100_skill_learned(skill_id):
    return int(v92_training.get(skill_id, 0)) >= 5
# </POTBO_STAGE S2455>

# <POTBO_STAGE S2457>


def _v101_skill_fallback_surface(skill_id, size):
    """Gerçek PNG yoksa metin değil, sade bir skill glifi üret."""
    size = max(16, int(size))
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    gold = (255, 190, 38, 255)
    hot = (255, 111, 18, 255)
    white = (255, 246, 214, 255)
    pad = max(3, int(round(size * 0.17)))
    thick = max(2, int(round(size * 0.075)))

    if skill_id == "decussatio_rubra":
        # Decussatio: iki çapraz kesik + merkezden geçen yatay kesik.
        pygame.draw.line(surf, hot, (pad, pad), (size - pad, size - pad), thick + 2)
        pygame.draw.line(surf, hot, (size - pad, pad), (pad, size - pad), thick + 2)
        pygame.draw.line(surf, gold, (pad - 1, size // 2), (size - pad + 1, size // 2), thick + 2)
        pygame.draw.line(surf, white, (pad + 2, pad + 2), (size - pad - 2, size - pad - 2), max(1, thick // 2))
        pygame.draw.line(surf, white, (size - pad - 2, pad + 2), (pad + 2, size - pad - 2), max(1, thick // 2))
        pygame.draw.line(surf, white, (pad + 2, size // 2), (size - pad - 2, size // 2), max(1, thick // 2))
    else:
        # Catena: birbirine bağlanan üç kısa kesik. Gerçek
        # catena_decollationis.png geldiğinde bu fallback otomatik bırakılır.
        pts = [
            (pad, int(size * 0.38)),
            (int(size * 0.34), int(size * 0.52)),
            (int(size * 0.50), int(size * 0.43)),
            (int(size * 0.66), int(size * 0.58)),
            (size - pad, int(size * 0.48)),
        ]
        pygame.draw.lines(surf, hot, False, pts, thick + 3)
        pygame.draw.lines(surf, gold, False, pts, thick + 1)
        pygame.draw.lines(surf, white, False, pts, max(1, thick // 2))
    return surf
# </POTBO_STAGE S2457>

# <POTBO_STAGE S2462>


# ---------------------------------------------------------
# INVENTORY BELT: 1-5 + Q on the left, five passive skill slots on the right.
# Skill slots are display-only and therefore have no cursor/confirm semantics.
# ---------------------------------------------------------
def v100_skill_belt_draw(start_x, y, slot_size=58, gap=10):
    learned = [
        skill_id
        for skill_id in ("decussatio_rubra", "catena_decollationis")
        if v100_skill_learned(skill_id)
    ]
    for index in range(5):
        rect = pygame.Rect(
            int(start_x + index * (slot_size + gap)),
            int(y),
            int(slot_size),
            int(slot_size),
        )
        v85_slot_shell(rect, selected=False, transfer=False)
        if index < len(learned):
            v100_skill_icon_draw(learned[index], rect.inflate(-8, -8))
# </POTBO_STAGE S2462>

# <POTBO_STAGE S2465>


# ---------------------------------------------------------
# CATENA DECOLLATIONIS: at least TWO living, chainable targets are mandatory.
# If every linked target is guaranteed to die from its Catena hit, the attack
# becomes a red/black decapitation cutscene. Otherwise it remains normal damage.
# ---------------------------------------------------------
V92_CHAIN_EXECUTION_MS = 2280
# </POTBO_STAGE S2465>

# <POTBO_STAGE S2468>


def v92_chain_update(now=None):
    global oyuncu_x, oyuncu_y
    state = v92_chain_state
    if not state.active:
        return
    if now is None:
        now = pygame.time.get_ticks()
    elapsed = max(0, int(now) - int(state.started_ms))
    duration = max(1, int(state.duration_ms))
    p = min(1.0, elapsed / duration)

    # Execution traversal is extremely fast; the remainder is reserved for the
    # decapitated heads to travel in deliberate slow motion and settle.
    motion_window = 0.20 if state.execution else 0.58
    hit_window = 0.18 if state.execution else 0.54
    motion_p = min(1.0, p / motion_window)
    pos = v92_chain_polyline_position(motion_p)
    oyuncu_x, oyuncu_y = float(pos.x), float(pos.y)

    for index in range(len(state.targets)):
        threshold = (index + 1) / (len(state.targets) + 1) * hit_window
        if p >= threshold:
            v92_chain_hit_target(index, now)

    dt = max(0.0, min(0.05, (int(now) - int(state.last_ms)) / 1000.0))
    state.last_ms = int(now)
    head_dt = dt * (0.25 if state.execution else 0.82)
    for head in state.heads:
        if getattr(head, "v100_grounded", False):
            head.velocity *= math.exp(-5.0 * head_dt)
            head.angular *= math.exp(-4.0 * head_dt)
            head.rotation += head.angular * head_dt
            continue
        head.position += head.velocity * head_dt
        head.z += head.vz * head_dt
        head.vz -= 150.0 * head_dt
        head.velocity *= math.exp(-0.82 * head_dt)
        head.rotation += head.angular * head_dt
        if head.z <= 0.0 and head.vz < 0.0:
            head.z = 0.0
            head.vz = 0.0
            head.velocity *= 0.34
            head.angular *= 0.42
            setattr(head, "v100_grounded", True)

    if p >= 1.0:
        oyuncu_x, oyuncu_y = float(state.final_player.x), float(state.final_player.y)
        dunya_olayi_kaydet(
            "special_chain_end",
            targets=len(state.targets),
            execution=state.execution,
        )
        state.reset()
# </POTBO_STAGE S2468>

# <POTBO_STAGE S2470>


def oyun_sinematik_kilitli_mi():
    return bool(
        v84_execution_state.active
        or v92_chain_state.active
        or _v100_cinematic_lock_base()
    )


def v100_cinematic_update(now=None):
    if now is None:
        now = pygame.time.get_ticks()
    # Only one authored execution owns player motion at a time.
    if v84_execution_state.active:
        v84_execution_update(now)
    elif v92_chain_state.active:
        v92_chain_update(now)
# </POTBO_STAGE S2470>

# <POTBO_STAGE S2501>


# Keyboard-only game: mouse motion/button events are pure queue noise.
for _v103_mouse_event in (
    pygame.MOUSEMOTION,
    pygame.MOUSEBUTTONDOWN,
    pygame.MOUSEBUTTONUP,
):
    pygame.event.set_blocked(_v103_mouse_event)
# </POTBO_STAGE S2501>

# <POTBO_STAGE S2524>


# ---------------------------------------------------------
# LEVEL-UP: current resources do not refill.
# The inherited level curve still increases maximum bars and combat progression,
# but the exact pre-level HP/mana/stamina are restored afterwards.
# ---------------------------------------------------------
_v106_level_gain_previous = oyuncu_seviye_kazanclarini_uygula


def oyuncu_seviye_kazanclarini_uygula(eski_level, yeni_level):
    global oyuncu_hp, oyuncu_mana, oyuncu_stamina
    hp_before = float(oyuncu_hp)
    mana_before = float(oyuncu_mana)
    stamina_before = float(oyuncu_stamina)
    result = _v106_level_gain_previous(eski_level, yeni_level)
    if int(yeni_level) > int(eski_level):
        oyuncu_hp = min(float(oyuncu_max_hp), hp_before)
        oyuncu_mana = min(float(oyuncu_max_mana), mana_before)
        oyuncu_stamina = min(float(oyuncu_max_stamina), stamina_before)
    return result
# </POTBO_STAGE S2524>

# <POTBO_STAGE S2530>


_v106_stamina_update_previous = stamina_guncelle
# </POTBO_STAGE S2530>

# <POTBO_STAGE S2536>
V106_CORONA_CONTACT_DAMAGE = 18
# </POTBO_STAGE S2536>

# <POTBO_STAGE S2566>
V106_CORONA_CONTACT_DAMAGE = 29
# </POTBO_STAGE S2566>

# <POTBO_STAGE S2596>
_v109_stamina_update_raw = stamina_guncelle
# </POTBO_STAGE S2596>

