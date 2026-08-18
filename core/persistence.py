






# <POTBO_STAGE S0012>
otomatik_kayit = True
# </POTBO_STAGE S0012>

# <POTBO_STAGE S0018>

AYAR_DOSYASI = os.path.join(USER_DATA_DIR, "settings.json")

SON_KAYIT_DOSYASI = os.path.join(SAVES, "last_save.json")

_legacy_settings = os.path.join(BASE_DIR, "settings.json")
if not os.path.exists(AYAR_DOSYASI) and os.path.isfile(_legacy_settings):
    try:
        os.makedirs(USER_DATA_DIR, exist_ok=True)
        shutil.copy2(_legacy_settings, AYAR_DOSYASI)
    except OSError:
        pass
# </POTBO_STAGE S0018>

# <POTBO_STAGE S0085>
LOAD_GAME = "load_game"
# </POTBO_STAGE S0085>

# <POTBO_STAGE S0088>
KAYIT_ADI = "kayit_adi"
# </POTBO_STAGE S0088>

# <POTBO_STAGE S0091>
KAYIT_SIL_ONAY = "kayit_sil_onay"
# </POTBO_STAGE S0091>

# <POTBO_STAGE S0100>
load_index = 0


load_game_donus_durumu = ANA_MENU
# </POTBO_STAGE S0100>

# <POTBO_STAGE S0104>
kayit_sil_onay_index = 1
# </POTBO_STAGE S0104>

# <POTBO_STAGE S0106>
silinecek_kayit_yolu = None
# </POTBO_STAGE S0106>

# <POTBO_STAGE S0115>

kayit_adi_girdisi = ""
kayit_mesaji = ""
# </POTBO_STAGE S0115>

# <POTBO_STAGE S0119>
son_otomatik_kayit = 0
otomatik_kayit_araligi = 300000

aktif_kayit = None
# </POTBO_STAGE S0119>

# <POTBO_STAGE S0130>
kayit_animasyon_bitis = 0
# </POTBO_STAGE S0130>

# <POTBO_STAGE S0245>


def tus_girdisi_kabul(olay):
    """Menülerde OS key-repeat ve çok hızlı çift basmayı dengeler."""
    if olay.type != pygame.KEYDOWN or oyun_durumu == KAYIT_ADI:
        return True

    if getattr(olay, "repeat", False):
        return False

    simdi = pygame.time.get_ticks()
    yon_tuslari = set(
        ui_yukari_tuslari() + ui_asagi_tuslari() + ui_sol_tuslari() + ui_sag_tuslari()
    )
    modal_tuslari = {
        pygame.K_RETURN,
        pygame.K_KP_ENTER,
        pygame.K_ESCAPE,
        pygame.K_SPACE,
    }
    modal_tuslari.update(tus_atamalari.values())
    modal_tuslari.update(GELISTIRICI_TEST_TUSLARI)

    if olay.key in yon_tuslari:
        bekleme = TUS_BEKLEME_YON
    elif olay.key in modal_tuslari:
        bekleme = TUS_BEKLEME_MODAL
    else:
        bekleme = TUS_BEKLEME_AKSIYON

    son = son_tus_zamanlari.get(olay.key, -10000)
    if simdi - son < bekleme:
        return False

    son_tus_zamanlari[olay.key] = simdi
    return True
# </POTBO_STAGE S0245>

# <POTBO_STAGE S0305>







def ayarlari_yukle():
    global dil
    global ana_ses
    global muzik_sesi
    global efekt_sesi
    global diyalog_sesi
    global tam_ekran
    global fps_goster
    global parlaklik
    global ekran_sarsintisi
    global etkilesim_ipuclari
    global otomatik_kayit
    global hasar_sayilari
    global az_hareket
    global metin_hizi
    global tus_atamalari

    try:


        veri = None
        son_hata = None
        for aday in (AYAR_DOSYASI, AYAR_DOSYASI + ".bak"):
            if not os.path.isfile(aday):
                continue
            try:
                with open(aday, "r", encoding="utf-8") as dosya:
                    aday_veri = json.load(dosya)
                if isinstance(aday_veri, dict):
                    veri = aday_veri
                    break
            except (
                json.JSONDecodeError,
                OSError,
                UnicodeError,
                TypeError,
                ValueError,
            ) as exc:
                son_hata = exc
        if veri is None:
            if son_hata is not None:
                raise ValueError(str(son_hata))
            raise FileNotFoundError(AYAR_DOSYASI)

        yuklenen_dil = veri.get("language", dil)
        dil = yuklenen_dil if yuklenen_dil in ("TR", "EN") else "TR"

        ana_ses = max(0, min(100, int(veri.get("master_volume", ana_ses))))
        muzik_sesi = max(
            0,
            min(100, int(veri.get("music_volume", muzik_sesi))),
        )
        efekt_sesi = max(
            0,
            min(100, int(veri.get("effect_volume", efekt_sesi))),
        )
        diyalog_sesi = max(
            0,
            min(
                100,
                int(veri.get("dialogue_volume", diyalog_sesi)),
            ),
        )

        tam_ekran = bool(veri.get("fullscreen", tam_ekran))
        fps_goster = bool(veri.get("show_fps", fps_goster))
        parlaklik = max(50, min(120, int(veri.get("brightness", parlaklik))))
        ekran_sarsintisi = bool(veri.get("screen_shake", ekran_sarsintisi))
        etkilesim_ipuclari = bool(veri.get("interaction_prompts", etkilesim_ipuclari))
        otomatik_kayit = bool(veri.get("autosave", otomatik_kayit))
        hasar_sayilari = bool(veri.get("damage_numbers", hasar_sayilari))
        az_hareket = bool(veri.get("reduced_motion", az_hareket))

        yuklenen_metin_hizi = str(veri.get("text_speed", metin_hizi))
        metin_hizi = (
            yuklenen_metin_hizi
            if yuklenen_metin_hizi in ("yavas", "normal", "hizli")
            else "normal"
        )

        yuklenen_tuslar = veri.get("key_bindings", {})
        if isinstance(yuklenen_tuslar, dict):
            tus_atamalari = dict(VARSAYILAN_TUS_ATAMALARI)
            for eylem in VARSAYILAN_TUS_ATAMALARI:
                if eylem in yuklenen_tuslar:
                    try:
                        tus_atamalari[eylem] = int(yuklenen_tuslar[eylem])
                    except (TypeError, ValueError):
                        pass
            tus_atamalarini_dogrula()

    except (
        FileNotFoundError,
        json.JSONDecodeError,
        OSError,
        TypeError,
        ValueError,
    ):
        tus_atamalarini_dogrula()


def ayarlari_kaydet():
    npc_ses_seviyesini_guncelle()
    ui_ses_seviyesini_guncelle()

    veri = {
        "language": dil,
        "master_volume": ana_ses,
        "music_volume": muzik_sesi,
        "effect_volume": efekt_sesi,
        "dialogue_volume": diyalog_sesi,
        "fullscreen": tam_ekran,
        "show_fps": fps_goster,
        "brightness": parlaklik,
        "screen_shake": ekran_sarsintisi,
        "interaction_prompts": etkilesim_ipuclari,
        "autosave": otomatik_kayit,
        "damage_numbers": hasar_sayilari,
        "reduced_motion": az_hareket,
        "text_speed": metin_hizi,
        "key_bindings": {eylem: int(tus) for eylem, tus in tus_atamalari.items()},
    }

    try:
        with open(AYAR_DOSYASI, "w", encoding="utf-8") as dosya:
            json.dump(veri, dosya, ensure_ascii=False, indent=4)
    except OSError:
        pass
# </POTBO_STAGE S0305>

# <POTBO_STAGE S0308>


def benzersiz_kayit_yolu(temiz_ad):
    """Var olan bir kaydı asla ezmeden yeni bir JSON yolu üretir."""
    temel = temiz_ad or "save"
    aday = os.path.join(SAVES, temel + ".json")
    sira = 2

    while os.path.exists(aday):
        aday = os.path.join(SAVES, f"{temel}_{sira}.json")
        sira += 1

    return aday


def bildirim_goster(metin, renk=BEYAZ, kenar_rengi=None, tur="genel"):
    global bildirim_aktif_baslangic
    if tur not in ("item", "level"):
        return
    metin = str(metin).strip()
    if not metin:
        return
    kayit = {
        "text": metin,
        "color": renk,
        "border": kenar_rengi or renk,
    }
    kuyruk_bostu = not bildirim_kuyrugu
    bildirim_kuyrugu.append(kayit)
    del bildirim_kuyrugu[:-5]
    if kuyruk_bostu:

        bildirim_aktif_baslangic = (
            pygame.time.get_ticks() if yeni_item_sahnesi_musait_mi() else 0
        )
# </POTBO_STAGE S0308>

# <POTBO_STAGE S0321>


def son_kaydi_yukle():
    try:
        with open(SON_KAYIT_DOSYASI, "r", encoding="utf-8") as dosya:
            veri = json.load(dosya)

        yol = veri.get("path")

        if yol and os.path.exists(yol):
            return oyun_yukle(yol)

    except (FileNotFoundError, json.JSONDecodeError, OSError):
        pass

    return False


def kayitlari_listele():
    sonuc = []

    try:
        for dosya_adi in os.listdir(SAVES):
            if not dosya_adi.endswith(".json"):
                continue

            if dosya_adi == "last_save.json":
                continue

            sonuc.append(os.path.join(SAVES, dosya_adi))

    except OSError:
        return []

    sonuc.sort(key=os.path.getmtime, reverse=True)

    return sonuc







def menu_secenekleri():
    return [
        t("continue"),
        t("new_game"),
        t("load_game"),
        t("settings"),
        t("credits"),
        t("quit"),
    ]
# </POTBO_STAGE S0321>

# <POTBO_STAGE S0323>


def menu_secimini_calistir():
    global oyun_durumu
    global menu_mesaji
    global load_game_donus_durumu

    global karakter_secim_index
    global oyuncu_adi
    global karakter_cinsiyet

    global karakter_mesaji

    global kayit_adi_girdisi
    global kayit_mesaji

    global cikis_index
    global ayarlar_donus_durumu
    global ayar_index
    global ayar_kategori_index
    global ayar_odak
    global cikis_donus_durumu




    if menu_index == 0:
        if son_kaydi_yukle():
            loading_baslat()
        else:
            menu_mesaji = t("no_continue")

    elif menu_index == 1:
        kayit_adi_girdisi = ""
        kayit_mesaji = ""
        oyun_durumu = KAYIT_ADI

    elif menu_index == 2:
        load_game_donus_durumu = ANA_MENU
        oyun_durumu = LOAD_GAME

    elif menu_index == 3:
        ayarlar_donus_durumu = ANA_MENU
        ayar_kategori_index = 0
        ayar_index = 0
        ayar_odak = "kategori"
        oyun_durumu = AYARLAR

    elif menu_index == 4:
        oyun_durumu = CREDITS

    elif menu_index == 5:
        cikis_index = 1
        cikis_donus_durumu = ANA_MENU
        oyun_durumu = CIKIS_ONAY
# </POTBO_STAGE S0323>

# <POTBO_STAGE S0325>


def kayit_adi_onayla():
    global oyun_durumu
    global oyuncu_adi
    global karakter_secim_index
    global karakter_cinsiyet
    global karakter_mesaji
    global kayit_mesaji

    temiz = dosya_adi_temizle(kayit_adi_girdisi)

    if not temiz:
        kayit_mesaji = t("save_name_empty")
        return

    oyuncu_adi = kayit_adi_girdisi.strip()
    karakter_secim_index = 0
    karakter_cinsiyet = "male"
    karakter_mesaji = ""
    kayit_mesaji = ""
    oyun_durumu = KARAKTER_OLUSTUR
# </POTBO_STAGE S0325>

# <POTBO_STAGE S0355>


def ganimeti_al():
    """
    Ganimet tek seferde toplu verilmez:
    1. E: Aurum Potabile
    2. E: Quinta Essentia
    3. E: 31 coin
    """
    global oyuncu_altin
    global ganimet_alindi
    global ganimet_asamasi

    if not npc_intro_tamamlandi or ganimet_alindi:
        return

    if ganimet_asamasi == 0:
        if not envantere_item_ekle(aurum_potabile_olustur(), kazanimi_goster=True):
            return
        ganimet_asamasi = 1
        item_alindi_bildirimi("Aurum Potabile", 1)
        dunya_pickup_sesi_cal("liquid")
        return

    if ganimet_asamasi == 1:
        if not envantere_item_ekle(quinta_essentia_olustur(), kazanimi_goster=True):
            return
        ganimet_asamasi = 2
        item_alindi_bildirimi("Quinta Essentia", 1)
        dunya_pickup_sesi_cal("liquid")
        return

    if ganimet_asamasi == 2:
        oyuncu_altin += 31
        ganimet_asamasi = 3
        ganimet_alindi = True
        item_alindi_bildirimi(bt("Coin", "Coin"), 31)
        dunya_pickup_sesi_cal("coin")
        oyun_kaydet()
# </POTBO_STAGE S0355>

# <POTBO_STAGE S0470>






def kayit_sil_onay_ciz():
    standart_onay_penceresi_ciz(t("delete_save_confirm"), kayit_sil_onay_index, "menu")
# </POTBO_STAGE S0470>

# <POTBO_STAGE S0474>


def ayar_etiketi(ayar):
    etiketler = {
        "language": bt("DİL", "LANGUAGE"),
        "autosave": bt("OTOMATİK KAYIT", "AUTOSAVE"),
        "interaction_prompts": bt("ETKİLEŞİM İŞARETLERİ", "INTERACTION PROMPTS"),
        "fullscreen": bt("TAM EKRAN", "FULLSCREEN"),
        "brightness": bt("PARLAKLIK", "BRIGHTNESS"),
        "fps": bt("FPS GÖSTER", "SHOW FPS"),
        "master": bt("ANA SES", "MASTER VOLUME"),
        "music": bt("MÜZİK", "MUSIC"),
        "effect": bt("EFEKTLER", "EFFECTS"),
        "dialogue": bt("KONUŞMA", "DIALOGUE"),
        "screen_shake": bt("EKRAN SARSINTISI", "SCREEN SHAKE"),
        "damage_numbers": bt("HASAR SAYILARI", "DAMAGE NUMBERS"),
        "reduced_motion": bt("AZALTILMIŞ HAREKET", "REDUCED MOTION"),
        "text_speed": bt("METİN HIZI", "TEXT SPEED"),
        "bind_move_up": bt("YUKARI", "MOVE UP"),
        "bind_move_down": bt("AŞAĞI", "MOVE DOWN"),
        "bind_move_left": bt("SOL", "MOVE LEFT"),
        "bind_move_right": bt("SAĞ", "MOVE RIGHT"),
        "bind_attack": bt("SALDIRI", "ATTACK"),
        "bind_block": bt("SAVUNMA", "BLOCK"),
        "bind_dash": bt("DASH", "DASH"),
        "bind_interact": bt("ETKİLEŞİM", "INTERACT"),
        "bind_inventory": bt("ENVANTER", "INVENTORY"),
        "bind_quick_use": bt("HIZLI KULLAN 1-5", "QUICK USE 1-5"),
        "bind_q_quick_use": bt("Q HIZLI SLOT", "Q QUICK SLOT"),
        "bind_save": bt("KAYDET", "SAVE"),
        "bind_pause": bt("DURAKLAT", "PAUSE"),
        "bind_reset": bt("VARSAYILANLARA DÖN", "RESTORE DEFAULTS"),
        "back": bt("GERİ", "BACK"),
    }
    return etiketler.get(ayar, str(ayar).upper())
# </POTBO_STAGE S0474>

# <POTBO_STAGE S0476>


def ayar_degeri(ayar):
    if ayar == "language":
        return "TÜRKÇE" if dil == "TR" else "ENGLISH"
    if ayar == "master":
        return f"%{ana_ses}"
    if ayar == "music":
        return f"%{muzik_sesi}"
    if ayar == "effect":
        return f"%{efekt_sesi}"
    if ayar == "dialogue":
        return f"%{diyalog_sesi}"
    if ayar == "brightness":
        return f"%{parlaklik}"
    if ayar == "fullscreen":
        return acik_kapali(tam_ekran)
    if ayar == "fps":
        return acik_kapali(fps_goster)
    if ayar == "screen_shake":
        return acik_kapali(ekran_sarsintisi)
    if ayar == "interaction_prompts":
        return acik_kapali(etkilesim_ipuclari)
    if ayar == "autosave":
        return acik_kapali(otomatik_kayit)
    if ayar == "damage_numbers":
        return acik_kapali(hasar_sayilari)
    if ayar == "reduced_motion":
        return acik_kapali(az_hareket)
    if ayar == "text_speed":
        adlar = {
            "yavas": bt("YAVAŞ", "SLOW"),
            "normal": bt("NORMAL", "NORMAL"),
            "hizli": bt("HIZLI", "FAST"),
        }
        return adlar[metin_hizi]
    if ayar.startswith("bind_") and ayar != "bind_reset":
        eylem = ayar[5:]
        if tus_atama_bekleniyor == eylem:
            return bt("TUŞ BEKLENİYOR", "WAITING FOR KEY")
        return tus_gorunen_adi(eylem)
    return ""
# </POTBO_STAGE S0476>

# <POTBO_STAGE S0487>


def ayari_degistir(yon):
    global dil
    global ana_ses
    global muzik_sesi
    global efekt_sesi
    global diyalog_sesi
    global tam_ekran
    global fps_goster
    global parlaklik
    global ekran_sarsintisi
    global etkilesim_ipuclari
    global otomatik_kayit
    global hasar_sayilari
    global az_hareket
    global metin_hizi
    global oyun_durumu

    secenekler = ayar_secenekleri()
    if not secenekler:
        return

    ayar = secenekler[max(0, min(len(secenekler) - 1, ayar_index))]

    if ayar == "language":
        dil = "EN" if dil == "TR" else "TR"
    elif ayar == "master":
        ana_ses = max(0, min(100, ana_ses + yon * 5))
    elif ayar == "music":
        muzik_sesi = max(0, min(100, muzik_sesi + yon * 5))
    elif ayar == "effect":
        efekt_sesi = max(0, min(100, efekt_sesi + yon * 5))
    elif ayar == "dialogue":
        diyalog_sesi = max(0, min(100, diyalog_sesi + yon * 5))
    elif ayar == "brightness":
        parlaklik = max(50, min(120, parlaklik + yon * 5))
    elif ayar == "fullscreen":
        tam_ekran = not tam_ekran
        ekran_olustur()
    elif ayar == "fps":
        fps_goster = not fps_goster
    elif ayar == "screen_shake":
        ekran_sarsintisi = not ekran_sarsintisi
    elif ayar == "interaction_prompts":
        etkilesim_ipuclari = not etkilesim_ipuclari
    elif ayar == "autosave":
        otomatik_kayit = not otomatik_kayit
    elif ayar == "damage_numbers":
        hasar_sayilari = not hasar_sayilari
    elif ayar == "reduced_motion":
        az_hareket = not az_hareket
    elif ayar == "text_speed":
        metin_hizi = dongulu_deger(["yavas", "normal", "hizli"], metin_hizi, yon)
    elif ayar == "back":
        v37_settings_back_schedule()
        return

    button_click_sesi_cal("menu1")
    ayarlari_kaydet()







def load_game_ciz():
    dosyalar = kayitlari_listele()[:7]

    varsayilan_gotik_arka_plan()

    koyu_kaplama(180)

    yazi_yaz(
        t("load_title"),
        GENISLIK // 2,
        100,
        PARLAK_KIRMIZI,
        menu_baslik_font,
        True,
    )

    if not dosyalar:
        panel = pygame.Rect(350, 275, 580, 150)

        gotik_panel(panel)

        yazi_yaz(
            t("no_save"),
            panel.centerx,
            panel.centery,
            GRI,
            menu_font,
            True,
        )

    else:
        for index, yol in enumerate(dosyalar):
            ad = os.path.splitext(os.path.basename(yol))[0]

            rect = pygame.Rect(350, 165 + index * 65, 580, 50)

            secili = index == load_index
            rect = buton_click_anim_rect(rect, secili)

            pygame.draw.rect(
                ekran,
                (45, 4, 13) if secili else KOYU_PANEL,
                rect,
                border_radius=0,
            )

            pygame.draw.rect(
                ekran,
                PARLAK_KIRMIZI if secili else (60, 55, 68),
                rect,
                2 if secili else 1,
                border_radius=0,
            )

            yazi_yaz(
                ad,
                rect.centerx,
                rect.centery,
                BEYAZ if secili else ACIK_GRI,
                normal_font,
                True,
            )
# </POTBO_STAGE S0487>

# <POTBO_STAGE S0528>


def _stage1__oyuncu_olum_menu_layer_ciz():
    """Game-over başlık + butonlarını alpha uygulanabilir ayrı yüzeye çizer."""
    global ekran
    gercek_ekran = ekran
    layer = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    ekran = layer
    try:
        title = t("game_over_title")
        title_s = gameover_font.render(title, True, (230, 10, 30))
        ekran.blit(
            title_s,
            title_s.get_rect(center=(GENISLIK // 2, 142)),
        )



        secenekler = [
            t("restart"),
            t("load_game"),
            t("main_menu"),
            t("quit"),
        ]
        for i, metin in enumerate(secenekler):
            rect = pygame.Rect(GENISLIK // 2 - 170, 414 + i * 58, 340, 34)
            secili = i == oyuncu_olum_menu_index
            menu_susleme_ciz(rect, secili)
            yazi_yaz(
                metin,
                rect.centerx,
                rect.centery,
                BEYAZ if secili else (155, 145, 150),
                menu_font if secili else normal_font,
                True,
            )
    finally:
        ekran = gercek_ekran
    return layer
# </POTBO_STAGE S0528>

# <POTBO_STAGE S0539>


def kayit_animasyonu_ciz():
    if pygame.time.get_ticks() >= kayit_animasyon_bitis:
        return
    merkez = (34, YUKSEKLIK - 34)
    aci = (pygame.time.get_ticks() * 0.38) % 360
    pygame.draw.circle(ekran, (7, 6, 10), merkez, 18)
    pygame.draw.circle(ekran, KOYU_KIRMIZI, merkez, 18, 2)
    for i in range(8):
        a = math.radians(aci + i * 45)
        x = merkez[0] + math.cos(a) * 11
        y = merkez[1] + math.sin(a) * 11
        pygame.draw.circle(ekran, PARLAK_KIRMIZI, (int(x), int(y)), 2)
# </POTBO_STAGE S0539>

# <POTBO_STAGE S0615>





def _oyuncu_olum_menu_layer_ciz():
    global ekran
    gercek_ekran = ekran
    layer = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
    simdi = pygame.time.get_ticks()
    title_alpha = oyuncu_olum_baslik_fade_orani(simdi)
    button_alpha = oyuncu_olum_menu_fade_orani(simdi)


    if title_alpha > 0.0:
        title_s = gameover_font.render(t("game_over_title"), True, (230, 10, 30))
        title_s.set_alpha(int(round(255 * title_alpha)))
        layer.blit(
            title_s,
            title_s.get_rect(center=(GENISLIK // 2, 142)),
        )

    if button_alpha > 0.0:
        buttons = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
        ekran = buttons
        try:
            secenekler = [
                t("restart"),
                t("load_game"),
                t("main_menu"),
                t("quit"),
            ]
            for i, metin in enumerate(secenekler):
                rect = pygame.Rect(GENISLIK // 2 - 170, 414 + i * 58, 340, 34)
                secili = i == oyuncu_olum_menu_index
                menu_susleme_ciz(rect, secili)
                yazi_yaz(
                    metin,
                    rect.centerx,
                    rect.centery,
                    BEYAZ if secili else (155, 145, 150),
                    menu_font if secili else normal_font,
                    True,
                )
        finally:
            ekran = gercek_ekran
        buttons.set_alpha(int(round(255 * button_alpha)))
        layer.blit(buttons, (0, 0))

    return layer
# </POTBO_STAGE S0615>

# <POTBO_STAGE S0676>





_v33_oyun_yukle = oyun_yukle


def oyun_yukle(*args, **kwargs):
    """Load sonrası eski/bozuk konum static geometry içindeyse otomatik kurtarır."""
    result = _v33_oyun_yukle(*args, **kwargs)
    try:
        _v34_player_depenetrate(False)
    except Exception as exc:
        debug_log("V34 load depenetration skipped:", exc)
    return result
# </POTBO_STAGE S0676>

# <POTBO_STAGE S0688>
v34_last_save_error = ""
v34_atomic_save_count = 0
# </POTBO_STAGE S0688>

# <POTBO_STAGE S0697>





def _v34_json_atomic_write(path, payload, indent=4):
    """JSON dosyasını sibling temp dosyaya yazıp os.replace ile atomik commit eder."""
    path = os.path.abspath(path)
    directory = os.path.dirname(path) or BASE_DIR
    os.makedirs(directory, exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=indent)
        f.flush()
        try:
            os.fsync(f.fileno())
        except OSError:
            pass
    os.replace(tmp, path)


def _v34_save_allowed_now():
    simdi = pygame.time.get_ticks()
    if oyuncu_hp <= 0:
        return False
    if gelistirici_x_skill_aktif_mi(simdi):
        return False
    if simdi < oyuncu_zorlanmis_bitis:
        return False


    if oyuncu_dash_aktif_mi(simdi):
        return False
    if oyuncu_saldiriyor and oyuncu_saldiri_modu == "hold_release":
        return False
    return True





_v34a_oyun_kaydet_guarded = oyun_kaydet


def oyun_kaydet():
    global v34_last_save_error
    if not _v34_save_allowed_now():
        return False
    try:
        result = _v34a_oyun_kaydet_guarded()
        v34_last_save_error = ""

        return True if result is None else bool(result)
    except OSError as exc:
        v34_last_save_error = str(exc)
        debug_log("V34 save error:", exc)
        return False
# </POTBO_STAGE S0697>

# <POTBO_STAGE S0758>
V34F_BACKUP_SUFFIX = ".bak"
# </POTBO_STAGE S0758>

# <POTBO_STAGE S0764>
V34F_SAVE_MIN_BYTES = 2
V34F_SAVE_MAX_BYTES = 12 * 1024 * 1024
V34F_SAVE_BACKUP_MAX_BYTES = 12 * 1024 * 1024
# </POTBO_STAGE S0764>

# <POTBO_STAGE S0766>

v34f_backup_write_count = 0
v34f_backup_restore_count = 0
v34f_backup_skip_count = 0
# </POTBO_STAGE S0766>

# <POTBO_STAGE S0768>
v34f_last_backup_error = ""
# </POTBO_STAGE S0768>

# <POTBO_STAGE S0776>


def _v34f_file_size_safe(path, maximum=V34F_SAVE_MAX_BYTES):
    try:
        size = os.path.getsize(path)
    except OSError:
        return False
    return V34F_SAVE_MIN_BYTES <= int(size) <= int(maximum)


def _v34f_read_json(path, maximum=V34F_SAVE_MAX_BYTES):
    """Unbounded/corrupt JSON'u save recovery yoluna sokmadan güvenli okuyucu."""
    if not path or not os.path.isfile(path):
        return None
    if not _v34f_file_size_safe(path, maximum):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            payload = json.load(f)
    except (
        OSError,
        UnicodeError,
        json.JSONDecodeError,
        ValueError,
        TypeError,
    ):
        return None
    return payload if _v34f_is_plain_json_object(payload) else None
# </POTBO_STAGE S0776>

# <POTBO_STAGE S0778>


def _v34f_backup_path(path):
    return os.path.abspath(path) + V34F_BACKUP_SUFFIX
# </POTBO_STAGE S0778>

# <POTBO_STAGE S0780>


def _v34f_backup_existing_valid_json(path):
    """Yalnız parse edilebilen mevcut dosyayı backup eder; corruption kopyalanmaz."""
    global v34f_backup_write_count, v34f_backup_skip_count, v34f_last_backup_error
    path = os.path.abspath(path)
    if not os.path.isfile(path):
        return False
    payload = _v34f_read_json(path, V34F_SAVE_BACKUP_MAX_BYTES)
    if payload is None:
        v34f_backup_skip_count += 1
        return False
    try:
        with open(path, "rb") as f:
            raw = f.read(V34F_SAVE_BACKUP_MAX_BYTES + 1)
        if not raw or len(raw) > V34F_SAVE_BACKUP_MAX_BYTES:
            v34f_backup_skip_count += 1
            return False
        _v34f_write_bytes_atomic(_v34f_backup_path(path), raw)
        v34f_backup_write_count += 1
        v34f_last_backup_error = ""
        return True
    except OSError as exc:
        v34f_last_backup_error = str(exc)
        _v34f_report_issue("backup_write_failed", exc, False, "warning")
        return False





_v34f_previous_json_atomic_write = _v34_json_atomic_write


def _v34_json_atomic_write(path, payload, indent=4):
    _v34f_backup_existing_valid_json(path)
    _v34f_previous_json_atomic_write(path, payload, indent=indent)





def ayarlari_kaydet():
    """Settings için de temp + fsync + replace + valid backup kontratı."""
    npc_ses_seviyesini_guncelle()
    ui_ses_seviyesini_guncelle()
    payload = {
        "language": dil,
        "master_volume": int(ana_ses),
        "music_volume": int(muzik_sesi),
        "effect_volume": int(efekt_sesi),
        "dialogue_volume": int(diyalog_sesi),
        "fullscreen": bool(tam_ekran),
        "show_fps": bool(fps_goster),
        "brightness": int(parlaklik),
        "screen_shake": bool(ekran_sarsintisi),
        "interaction_prompts": bool(etkilesim_ipuclari),
        "autosave": bool(otomatik_kayit),
        "damage_numbers": bool(hasar_sayilari),
        "reduced_motion": bool(az_hareket),
        "text_speed": str(metin_hizi),
        "key_bindings": {eylem: int(tus) for eylem, tus in tus_atamalari.items()},
    }
    try:
        _v34_json_atomic_write(AYAR_DOSYASI, payload, indent=4)
        return True
    except OSError as exc:
        _v34f_report_issue("settings_save_failed", exc, False, "warning")
        return False





def _v34f_save_payload_plausible(payload):
    """Version-spanning load'u bozmadan yalnız bariz yanlış JSON'u reddeder."""
    if not isinstance(payload, dict):
        return False


    known = {
        "name",
        "player_name",
        "level",
        "gold",
        "x",
        "y",
        "inventory",
        "common_enemies",
        "quests",
        "gender",
        "strength",
        "hp",
        "max_hp",
    }
    if not any(key in payload for key in known):
        return False
    return True


def _v34f_restore_backup_to_main(path):
    global v34f_backup_restore_count, v34f_last_restore_error
    path = os.path.abspath(path)
    backup = _v34f_backup_path(path)
    payload = _v34f_read_json(backup, V34F_SAVE_BACKUP_MAX_BYTES)
    if not _v34f_save_payload_plausible(payload):
        return False
    try:

        if os.path.isfile(path):
            try:
                with open(path, "rb") as f:
                    bad = f.read(V34F_SAVE_BACKUP_MAX_BYTES + 1)
                if bad and len(bad) <= V34F_SAVE_BACKUP_MAX_BYTES:
                    _v34f_write_bytes_atomic(_v34f_corrupt_path(path), bad)
            except OSError:
                pass

        _v34f_previous_json_atomic_write(path, payload, indent=4)
        v34f_backup_restore_count += 1
        v34f_last_restore_error = ""
        _v34f_report_issue(
            "save_restored_from_backup",
            os.path.basename(path),
            True,
            "warning",
        )
        return True
    except OSError as exc:
        v34f_last_restore_error = str(exc)
        _v34f_report_issue("save_restore_failed", exc, False, "error")
        return False


_v34f_previous_oyun_yukle = oyun_yukle


def oyun_yukle(dosya_yolu, *args, **kwargs):
    """Ana save parse edilemiyorsa son valid .bak'ı ana dosyaya restore edip yükler."""
    global v34f_corrupt_file_count
    path = os.path.abspath(dosya_yolu)
    payload = _v34f_read_json(path)
    if payload is None or not _v34f_save_payload_plausible(payload):
        v34f_corrupt_file_count += 1
        restored = _v34f_restore_backup_to_main(path)
        if not restored:
            _v34f_report_issue(
                "save_invalid_no_backup",
                os.path.basename(path),
                False,
                "error",
            )
    result = _v34f_previous_oyun_yukle(path, *args, **kwargs)

    try:
        _v34f_reset_transient_combat_state(after_load=True)
        _v34_player_depenetrate(False)
    except Exception as exc:
        _v34f_report_issue("post_load_sanitize_failed", exc, False, "warning")
    return result
# </POTBO_STAGE S0780>

# <POTBO_STAGE S0803>


def _v34f_save_path_contract():
    problems = []
    for label, path in (("base", BASE_DIR), ("saves", SAVES)):
        if not path:
            problems.append(label + ":empty")
            continue
        try:
            os.makedirs(path, exist_ok=True)
        except OSError:
            problems.append(label + ":unwritable")
    return problems
# </POTBO_STAGE S0803>

# <POTBO_STAGE S0806>





def v34f_runtime_audit_tick(force=False):
    global \
        v34f_last_audit_ms, \
        v34f_audit_count, \
        v34f_audit_last_ok, \
        v34f_audit_last_summary
    simdi = _v34f_now()
    if not force and simdi - v34f_last_audit_ms < V34F_AUDIT_INTERVAL_MS:
        return v34f_audit_last_summary
    v34f_last_audit_ms = simdi
    v34f_audit_count += 1

    issues_before = len(v34f_issues)
    if not _v34f_player_coordinates_valid():
        _v34f_repair_player_coordinates()
    _v34f_repair_resource_invariants()

    phase_ok, phase_detail = _v34f_special_phase_contract()
    if not phase_ok:
        _v34f_report_issue(
            "special_phase_contract",
            phase_detail,
            False,
            "error",
        )

    keybind_problems = _v34f_keybind_contract()
    if keybind_problems:
        _v34f_report_issue(
            "keybind_contract",
            ",".join(keybind_problems),
            False,
            "warning",
        )

    save_problems = _v34f_save_path_contract()
    if save_problems:
        _v34f_report_issue(
            "save_path_contract",
            ",".join(save_problems),
            False,
            "error",
        )

    special_problems = _v34f_special_runtime_contract()
    if special_problems:
        _v34f_report_issue(
            "special_runtime_contract",
            ",".join(special_problems),
            False,
            "error",
        )

    static_valid = True
    if oyun_durumu == OYUN and oyun_alt_durumu == HARITA and oyuncu_hp > 0:
        try:
            static_valid = bool(
                _v34_static_position_valid(float(oyuncu_x), float(oyuncu_y))
            )
        except Exception:
            static_valid = False
        if not static_valid and not gelistirici_x_skill_aktif_mi(simdi):
            recovered = False
            try:
                recovered = bool(_v34_player_depenetrate(False))
            except Exception:
                recovered = False
            _v34f_report_issue(
                "player_static_overlap",
                "depenetration",
                recovered,
                "warning",
            )

    new_issues = len(v34f_issues) - issues_before
    v34f_audit_last_ok = new_issues <= 0 and phase_ok and not special_problems
    v34f_audit_last_summary = {
        "version": V34F_VERSION,
        "time": simdi,
        "ok": bool(v34f_audit_last_ok),
        "phase_ok": bool(phase_ok),
        "static_valid": bool(static_valid),
        "issues_total": len(v34f_issues),
        "fixes_total": int(v34f_audit_fix_count),
        "frame_p95_ms": round(_v34f_frame_percentile(0.95), 2),
        "fx_quality": round(float(v34_fx_quality), 3),
        "special_active": bool(gelistirici_x_skill_aktif_mi(simdi)),
        "special_hits": int(gelistirici_x_skill_vurus_maskesi),
        "backup_writes": int(v34f_backup_write_count),
        "backup_restores": int(v34f_backup_restore_count),
    }
    return dict(v34f_audit_last_summary)
# </POTBO_STAGE S0806>

# <POTBO_STAGE S0811>





def _v34f_startup_self_check():
    """Import/startup anında filesystem'e test dosyası yazmadan pure contract kontrolü."""
    phase_ok, phase_detail = _v34f_special_phase_contract()
    if not phase_ok:
        _v34f_report_issue(
            "startup_special_phase",
            phase_detail,
            False,
            "error",
        )
    keybind_problems = _v34f_keybind_contract()
    if keybind_problems:
        _v34f_report_issue(
            "startup_keybind",
            ",".join(keybind_problems),
            False,
            "warning",
        )
    try:
        os.makedirs(SAVES, exist_ok=True)
    except OSError as exc:
        _v34f_report_issue("startup_save_dir", exc, False, "error")
    return phase_ok and not keybind_problems
# </POTBO_STAGE S0811>

# <POTBO_STAGE S0874>


def _v37_main_confirm_execute(index):
    global oyun_durumu, oyun_alt_durumu
    idx = int(index)
    if idx == 0:
        npc_sesi_durdur()
        if ana_menu_onay_donus_durumu == OYUN and oyuncu_hp <= 0:
            oyuncu_olum_sahnesini_sifirla()
        else:
            oyun_kaydet()
        oyun_alt_durumu = HARITA
        oyun_durumu = ANA_MENU
    else:
        oyun_durumu = ana_menu_onay_donus_durumu
# </POTBO_STAGE S0874>

# <POTBO_STAGE S0876>


def _v37_delete_confirm_execute(index):
    global silinecek_kayit_yolu, load_index, oyun_durumu
    idx = int(index)
    if idx == 0:
        if silinecek_kayit_yolu and os.path.exists(silinecek_kayit_yolu):
            try:
                os.remove(silinecek_kayit_yolu)
            except OSError:
                pass
            try:
                yedek_yol = silinecek_kayit_yolu + V34F_BACKUP_SUFFIX
                if os.path.isfile(yedek_yol):
                    os.remove(yedek_yol)
            except OSError:
                pass
        load_index = 0
    silinecek_kayit_yolu = None
    oyun_durumu = LOAD_GAME
# </POTBO_STAGE S0876>

# <POTBO_STAGE S0880>


def _v37_load_game_execute(path):
    if path and oyun_yukle(path):
        loading_baslat()


def v37_load_game_schedule(path):
    button_click_sesi_cal("menu1")
    return v37_ui_action_schedule(
        lambda path=str(path): _v37_load_game_execute(path),
        "load_game",
    )
# </POTBO_STAGE S0880>

# <POTBO_STAGE S0883>


def _v37_quit_confirm_execute(index):
    global oyun_durumu
    idx = int(index)
    if idx == 0:
        npc_sesi_durdur()
        oyun_kaydet()
        ayarlari_kaydet()
        pygame.quit()
        raise SystemExit()
    oyun_durumu = DURAKLATMA
# </POTBO_STAGE S0883>

# <POTBO_STAGE S1063>


_v39_oyun_yukle_original = oyun_yukle
# </POTBO_STAGE S1063>

# <POTBO_STAGE S1528>


def _v76_death_menu_draw():

    now = pygame.time.get_ticks()
    if oyuncu_olum_menu_fade_orani(now) < 0.985:
        return
    if oyuncu_olum_cikis_orani(now) > 0.0:
        return

    title = gameover_font.render(t("game_over_title"), False, V76_DEATH_BODY)
    ekran.blit(title, title.get_rect(center=(GENISLIK // 2, 132)))
    options = [
        t("restart"),
        t("load_game"),
        t("main_menu"),
        t("quit"),
    ]
    for i, text in enumerate(options):
        selected = i == oyuncu_olum_menu_index
        label = f"> {text} <" if selected else text
        font = gameover_secim_font if selected else normal_font
        surf = font.render(label, False, V76_DEATH_BODY)
        ekran.blit(
            surf,
            surf.get_rect(center=(GENISLIK // 2, 454 + i * 48)),
        )
# </POTBO_STAGE S1528>

# <POTBO_STAGE S1540>






for _v77_lang in ("TR", "EN"):
    for _v77_key in (
        "menu_help",
        "create_help",
        "settings_help",
        "load_help",
        "delete_help",
        "game_menu",
        "controls",
    ):
        if _v77_key in METINLER[_v77_lang]:
            METINLER[_v77_lang][_v77_key] = ""
# </POTBO_STAGE S1540>

# <POTBO_STAGE S1548>


def _v77_death_menu_draw(now):


    title_p = oyuncu_olum_baslik_fade_orani(now)
    menu_p = oyuncu_olum_menu_fade_orani(now)

    if title_p > 0.02:
        title = gameover_font.render(t("game_over_title"), False, V77_DEATH_BODY)
        ekran.blit(title, title.get_rect(center=(GENISLIK // 2, 142)))

    if menu_p > 0.02:
        options = [
            t("restart"),
            t("load_game"),
            t("main_menu"),
            t("quit"),
        ]
        for i, text in enumerate(options):
            rect = pygame.Rect(GENISLIK // 2 - 170, 414 + i * 58, 340, 34)
            selected = i == oyuncu_olum_menu_index
            _v77_death_button(rect, selected)
            font = menu_font if selected else normal_font
            surf = font.render(text, False, V77_DEATH_BODY)
            ekran.blit(surf, surf.get_rect(center=rect.center))
# </POTBO_STAGE S1548>

# <POTBO_STAGE S1573>


def _v77_death_menu_draw(now):
    title_p = oyuncu_olum_baslik_fade_orani(now)
    menu_p = oyuncu_olum_menu_fade_orani(now)
    if title_p > 0.02:
        title = gameover_font.render(t("game_over_title"), False, V77_DEATH_BODY)
        ekran.blit(title, title.get_rect(center=(GENISLIK // 2, 146)))
    if menu_p > 0.02:
        options = [
            t("restart"),
            t("load_game"),
            t("main_menu"),
            t("quit"),
        ]
        for i, text in enumerate(options):
            rect = pygame.Rect(GENISLIK // 2 - 170, 410 + i * 58, 340, 36)
            selected = i == oyuncu_olum_menu_index
            _v78_death_button(rect, selected)
            font = menu_font if selected else normal_font
            surf = font.render(text, False, V77_DEATH_BODY)
            ekran.blit(surf, surf.get_rect(center=rect.center))
# </POTBO_STAGE S1573>

# <POTBO_STAGE S1599>


def _v79_death_menu_content(now):

    scratch = pygame.Surface((440, 260), pygame.SRCALPHA)
    global ekran
    old = ekran
    ekran = scratch
    try:
        options = [
            t("restart"),
            t("load_game"),
            t("main_menu"),
            t("quit"),
        ]
        for i, text in enumerate(options):
            local_rect = pygame.Rect(50, 10 + i * 58, 340, 36)
            selected = i == oyuncu_olum_menu_index
            _v78_death_button(local_rect, selected)
            font = menu_font if selected else normal_font
            surf = font.render(text, False, V77_DEATH_BODY)
            scratch.blit(surf, surf.get_rect(center=local_rect.center))
    finally:
        ekran = old
    return scratch
# </POTBO_STAGE S1599>

# <POTBO_STAGE S1704>


def _v83_death_menu_draw(now):
    title_p = oyuncu_olum_baslik_fade_orani(now)
    menu_p = oyuncu_olum_menu_fade_orani(now)
    if title_p > 0.02:
        title = gameover_font.render(t("game_over_title"), False, V77_DEATH_BODY)
        title_rect = title.get_rect(center=(GENISLIK // 2, 136))
        ekran.blit(title, title_rect)

    if menu_p > 0.02:
        options = [
            t("restart"),
            t("load_game"),
            t("main_menu"),
            t("quit"),
        ]
        panel = pygame.Rect(GENISLIK // 2 - 235, 390, 470, 260)
        pygame.draw.rect(ekran, V77_DEATH_BLACK, panel)
        line_inset = 54
        pygame.draw.line(
            ekran,
            V77_DEATH_BODY,
            (panel.left + line_inset, panel.top),
            (panel.right - line_inset, panel.top),
            1,
        )
        pygame.draw.line(
            ekran,
            V77_DEATH_BODY,
            (panel.left + line_inset, panel.bottom),
            (panel.right - line_inset, panel.bottom),
            1,
        )
        for i, text in enumerate(options):
            rect = pygame.Rect(GENISLIK // 2 - 170, 410 + i * 56, 340, 34)
            selected = i == oyuncu_olum_menu_index
            _v77_death_button(rect, selected)
            font = menu_font if selected else normal_font
            surf = font.render(text, False, V77_DEATH_BODY)
            ekran.blit(surf, surf.get_rect(center=rect.center))
# </POTBO_STAGE S1704>

# <POTBO_STAGE S1767>


def v84_execution_save_target_state(target):
    names = (
        "active",
        "attacking",
        "attack_connected",
        "attack_damage_applied",
        "recovery_until",
        "hit_stun_until",
        "stagger_until",
        "vx",
        "vy",
        "dash_kind",
        "dash_until",
    )
    return {name: getattr(target, name) for name in names if hasattr(target, name)}
# </POTBO_STAGE S1767>

# <POTBO_STAGE S1769>


def v84_execution_start(target=None, override=True, source="ctrl_y"):
    global v84_execution_total
    global oyuncu_savunuyor
    if v84_execution_state.active:
        return False
    if oyun_durumu != OYUN or oyun_alt_durumu != HARITA:
        return False
    if oyuncu_hp <= 0 or oyun_sinematik_kilitli_mi():
        return False
    if oyuncu_kontrol_kilitli_mi(pygame.time.get_ticks()):
        return False
    if target is None:
        target = v84_execution_target_select(override=override)
    if target is None:
        bildirim_goster(
            bt(
                "İnfaz menzilinde canlı hedef yok.",
                "No living target is within execution range.",
            ),
            GRI,
        )
        return False
    if not override and not v84_execution_naturally_eligible(target):
        return False

    now = pygame.time.get_ticks()
    seed = (
        sum(ord(char) for char in v84_actor_uid(target)) * 131
        + int(now)
        + v84_execution_total * 977
    ) & 0x7FFFFFFF
    silhouette = v84_actor_silhouette(target)
    saved = v84_execution_save_target_state(target)
    was_active = bool(getattr(target, "active", False))
    v84_execution_suspend_target(target)
    points = v84_execution_choreography(target, seed)

    oyuncu_saldiri_durumunu_sifirla()
    oyuncu_savunuyor = False
    v51_riposte_clear()
    v84_riposte_state.clear()
    state = v84_execution_state
    state.active = True
    state.target = target
    state.target_uid = v84_actor_uid(target)
    state.source = str(source)
    state.seed = int(seed)
    state.elapsed_ms = 0.0
    state.last_tick_ms = int(now)
    state.next_beat_index = 0
    state.target_was_active = was_active
    state.target_saved_state = saved
    state.player_start = pygame.Vector2(oyuncu_x, oyuncu_y)
    state.player_hp_at_start = int(oyuncu_hp)
    state.fracture = V84FractureField(
        silhouette,
        max_fragments=V84_EXECUTION_MAX_FRAGMENTS,
    )
    state.slashes = []
    state.choreography_points = points
    state.final_applied = False
    state.interrupted = False
    state.interrupt_reason = ""
    state.cuts_landed = 0
    v84_execution_total += 1
    dunya_olayi_kaydet(
        "execution_start",
        enemy=str(getattr(target, "tur", "enemy")),
        override=bool(override),
        source=str(source),
    )
    return True
# </POTBO_STAGE S1769>

# <POTBO_STAGE S1796>


_v84_save_original = oyun_kaydet


def oyun_kaydet(*args, **kwargs):
    if v84_execution_state.active:



        return False
    return _v84_save_original(*args, **kwargs)


_v84_load_original = oyun_yukle


def oyun_yukle(*args, **kwargs):
    v84_transient_reset(restore_execution_target=True)
    result = _v84_load_original(*args, **kwargs)
    v84_transient_reset(restore_execution_target=False)
    return result
# </POTBO_STAGE S1796>

# <POTBO_STAGE S1988>


def v88_load_alpha_asset(paths):
    path = v88_first_existing(paths)
    if not path:
        return "", None
    image = _v19_alpha_gorsel_yukle(path)
    if image is None or image.get_width() <= 0 or image.get_height() <= 0:
        return "", None
    return path, image
# </POTBO_STAGE S1988>

# <POTBO_STAGE S2060>


def v89_load_ground_fire_frames():
    if not os.path.isfile(V89_GROUND_FIRE_PATH):
        return []
    try:
        sheet = pygame.image.load(V89_GROUND_FIRE_PATH).convert_alpha()
    except pygame.error:
        return []
    if sheet.get_width() < 130 or sheet.get_height() < 108:
        return []
    frames = []
    for spec in V89_GROUND_FIRE_RECTS:
        area = pygame.Rect(spec).clip(sheet.get_rect())
        if area.width <= 0 or area.height <= 0:
            continue
        frame = sheet.subsurface(area).copy().convert_alpha()
        bounds = frame.get_bounding_rect(min_alpha=2)
        if bounds.width <= 1 or bounds.height <= 1:
            continue
        bounds = bounds.inflate(2, 2).clip(frame.get_rect())
        frames.append(frame.subsurface(bounds).copy().convert_alpha())
    return frames


def v89_load_small_fire_frames():
    if not os.path.isfile(V89_SMALL_FIRE_PATH):
        return []
    try:
        sheet = pygame.image.load(V89_SMALL_FIRE_PATH).convert_alpha()
    except pygame.error:
        return []
    frame_size = 16
    if sheet.get_height() != frame_size or sheet.get_width() < frame_size:
        return []
    frames = []
    for x in range(0, sheet.get_width() - frame_size + 1, frame_size):
        frame = sheet.subsurface((x, 0, frame_size, frame_size)).copy().convert_alpha()
        if frame.get_bounding_rect(min_alpha=2).width > 0:
            frames.append(frame)
    return frames


V89_GROUND_FIRE_FRAMES = v89_load_ground_fire_frames()
# </POTBO_STAGE S2060>

# <POTBO_STAGE S2062>

V89_SMALL_FIRE_FRAMES = v89_load_small_fire_frames()
# </POTBO_STAGE S2062>

# <POTBO_STAGE S2096>


_v89_save_game_raw = oyun_kaydet
# </POTBO_STAGE S2096>

# <POTBO_STAGE S2098>


_v89_load_game_raw = oyun_yukle
# </POTBO_STAGE S2098>

# <POTBO_STAGE S2142>
V90_INJURY_SAVE_KEY = "somatic_injury_v90"
# </POTBO_STAGE S2142>

# <POTBO_STAGE S2197>


_v90_save_game_raw = oyun_kaydet


def oyun_kaydet(*args, **kwargs):
    result = _v90_save_game_raw(*args, **kwargs)
    if not result or not aktif_kayit:
        return result
    try:
        with open(aktif_kayit, "r", encoding="utf-8") as source:
            payload = json.load(source)
        payload[V90_INJURY_SAVE_KEY] = v90_injury_snapshot()
        _v34_json_atomic_write(aktif_kayit, payload, indent=4)
    except (OSError, ValueError, TypeError) as exc:
        debug_log("V90 injury save failed:", exc)
        return False
    return True


_v90_load_game_raw = oyun_yukle
# </POTBO_STAGE S2197>

# <POTBO_STAGE S2260>


def _v92_load_alpha(path):
    if not path or not os.path.isfile(path):
        return None
    try:
        return pygame.image.load(path).convert_alpha()
    except pygame.error:
        return None
# </POTBO_STAGE S2260>

# <POTBO_STAGE S2296>




for _lang in ("TR", "EN"):
    for _key in (
        "menu_help",
        "create_help",
        "settings_help",
        "load_help",
        "delete_help",
        "game_menu",
        "controls",
    ):
        if _key in METINLER[_lang]:
            METINLER[_lang][_key] = ""
# </POTBO_STAGE S2296>

# <POTBO_STAGE S2334>






V92_SAVE_KEY = "systems_v92"
# </POTBO_STAGE S2334>

# <POTBO_STAGE S2336>


_v92_save_raw = oyun_kaydet


def oyun_kaydet(*args, **kwargs):
    result = _v92_save_raw(*args, **kwargs)
    if not result or not aktif_kayit:
        return result
    try:
        with open(aktif_kayit, "r", encoding="utf-8") as handle:
            payload = json.load(handle)
        payload[V92_SAVE_KEY] = v92_save_payload()
        _v34_json_atomic_write(aktif_kayit, payload, indent=4)
    except (OSError, ValueError, TypeError) as exc:
        debug_log("V92 save failed:", exc)
        return False
    return True


_v92_load_raw = oyun_yukle


def oyun_yukle(*args, **kwargs):
    result = _v92_load_raw(*args, **kwargs)
    if not result:
        return result
    path = args[0] if args else kwargs.get("dosya_yolu")
    try:
        with open(path, "r", encoding="utf-8") as handle:
            payload = json.load(handle)
        v92_restore_payload(payload.get(V92_SAVE_KEY, {}))
    except (OSError, ValueError, TypeError):
        v92_restore_payload({})
    v92_chain_state.reset()
    return result
# </POTBO_STAGE S2336>

# <POTBO_STAGE S2372>



METINLER["TR"]["save_name_help"] = "Kayıt adını yaz; SPACE veya ENTER ile onayla. Boşluk kullanılamaz."
METINLER["EN"]["save_name_help"] = "Type a save name; confirm with SPACE or ENTER. Spaces are not allowed."
# </POTBO_STAGE S2372>

# <POTBO_STAGE S2377>






def _v95_idle_crop(path, reference_size, pixel_rect):
    sheet = _v94_load_alpha(path)
    if sheet is None:
        return None
    ref_w, ref_h = reference_size
    x, y, w, h = pixel_rect


    return _v94_normalized_crop(
        sheet,
        float(x) / float(ref_w),
        float(y) / float(ref_h),
        float(w) / float(ref_w),
        float(h) / float(ref_h),
    )
# </POTBO_STAGE S2377>

# <POTBO_STAGE S2420>


def _v98_load_trimmed_alpha(candidates):
    path = mevcut_ilk_dosya(candidates)
    if not path:
        return None
    try:
        image = pygame.image.load(path).convert_alpha()
    except (pygame.error, OSError):
        return None
    bounds = image.get_bounding_rect(min_alpha=4)
    if bounds.width <= 0 or bounds.height <= 0:
        return None
    return image.subsurface(bounds).copy().convert_alpha()


V98_HEALTH_ICON = _v98_load_trimmed_alpha(V98_HEALTH_ICON_ADAYLARI)
V98_MANA_ICON = _v98_load_trimmed_alpha(V98_MANA_ICON_ADAYLARI)
V98_STAMINA_ICON = _v98_load_trimmed_alpha(V98_STAMINA_ICON_ADAYLARI)
# </POTBO_STAGE S2420>

# <POTBO_STAGE S2482>


def _v102_load_first_icon(paths):
    for path in paths:
        if not path or not os.path.isfile(path):
            continue
        try:
            image = pygame.image.load(path).convert_alpha()
        except (pygame.error, OSError):
            continue
        image = _v102_trim_alpha(image)
        if image is not None:
            return image
    return None
# </POTBO_STAGE S2482>

# <POTBO_STAGE S2484>

for _skill_id, _extra_paths in V102_SKILL_PATH_EXTRAS.items():
    if _skill_id in V100_SKILL_META:
        old = tuple(V100_SKILL_META[_skill_id].get("paths", ()))
        merged = []
        for p in tuple(_extra_paths) + old:
            if p not in merged:
                merged.append(p)
        V100_SKILL_META[_skill_id]["paths"] = tuple(merged)
        loaded = _v102_load_first_icon(merged)
        if loaded is not None:
            V100_SKILL_ICONS[_skill_id] = loaded
# </POTBO_STAGE S2484>

# <POTBO_STAGE S2486>

V102_UPGRADE_ICONS = {
    kind: _v102_load_first_icon(paths)
    for kind, paths in V102_UPGRADE_ICON_PATHS.items()
}


def _v102_upgrade_icon_reload(kind):
    image = _v102_load_first_icon(V102_UPGRADE_ICON_PATHS.get(kind, ()))
    if image is not None:
        V102_UPGRADE_ICONS[kind] = image
    return image
# </POTBO_STAGE S2486>

# <POTBO_STAGE S2533>
v107_corona_asset_reload_attempted = False
# </POTBO_STAGE S2533>

# <POTBO_STAGE S2540>


def v107_corona_asset_ensure_loaded():
    global V106_CORONA_FRAMES, v107_corona_asset_reload_attempted
    if V106_CORONA_FRAMES:
        return True


    V106_CORONA_FRAMES = v106_corona_frames_load(force_resolve=True)
    v107_corona_asset_reload_attempted = True
    v106_corona_transform_cache.clear()
    return bool(V106_CORONA_FRAMES)
# </POTBO_STAGE S2540>

# <POTBO_STAGE S2612>


def v110_load_alpha(path):
    if not path or not os.path.isfile(path):
        return None
    try:
        return pygame.image.load(path).convert_alpha()
    except (pygame.error, OSError):
        return None
# </POTBO_STAGE S2612>

# <POTBO_STAGE S2675>


def oyun_kaydet():


    if not _v34_save_allowed_now():
        return False
    if getattr(v84_execution_state, "active", False):
        return False

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


    veri[V89_BLOOD_SAVE_KEY] = v89_blood_snapshot()
    veri[V90_INJURY_SAVE_KEY] = v90_injury_snapshot()
    veri[V92_SAVE_KEY] = v92_save_payload()
    pygame.event.pump()

    try:


        _v34_json_atomic_write(aktif_kayit, veri, indent=4)
        pygame.event.pump()
        _v34_json_atomic_write(SON_KAYIT_DOSYASI, {"path": aktif_kayit}, indent=4)
        kayit_animasyon_bitis = pygame.time.get_ticks() + 1500
        return True

    except OSError as exc:
        debug_log("Save write failed:", exc)
        return False
# </POTBO_STAGE S2675>

