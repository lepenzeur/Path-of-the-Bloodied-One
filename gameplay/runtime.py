# Path of the Bloodied One — categorized source stages
#
# This file is intentionally executed by core/bootstrap.py in original source order.
# Keeping one shared runtime namespace avoids gameplay regressions while the former
# 90k-line monolith is physically separated by responsibility. Do not import this
# file directly; edit the stage code normally and launch root main.py.

# <POTBO_STAGE S2676>

# =========================================================
# END V117
# =========================================================

while calisiyor:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            calisiyor = False

        if olay.type == pygame.KEYDOWN and not tus_girdisi_kabul(olay):
            continue

        # -------------------------------------------------
        # ANA MENÜ
        # -------------------------------------------------

        if oyun_durumu == ANA_MENU:
            if olay.type == pygame.KEYDOWN:
                if olay.key in ui_yukari_tuslari():
                    menu_index = (menu_index - 1) % 6

                elif olay.key in ui_asagi_tuslari():
                    menu_index = (menu_index + 1) % 6

                elif olay.key in buton_onay_tuslari():
                    button_click_sesi_cal()
                    menu_secimini_calistir()

        # -------------------------------------------------
        # KARAKTER OLUŞTURMA
        # -------------------------------------------------

        elif oyun_durumu == KARAKTER_OLUSTUR:
            if olay.type == pygame.KEYDOWN:
                # Onay animasyonu başladıktan sonra geçiş bitene kadar yeni girdi alınmaz.
                if karakter_onay_gecisi_aktif:
                    continue

                if olay.key == pygame.K_ESCAPE:
                    oyun_durumu = KAYIT_ADI

                elif olay.key in ui_sol_tuslari() + ui_yukari_tuslari():
                    karakter_cinsiyet = "male"
                    karakter_secim_index = 0

                elif olay.key in ui_sag_tuslari() + ui_asagi_tuslari():
                    karakter_cinsiyet = "female"
                    karakter_secim_index = 1

                elif olay.key in buton_onay_tuslari():
                    # V40: Character Select bir UI butonu değildir. Enter seçim kilidini
                    # doğrudan başlatır; generic buttonClick sesi/animasyonu kullanılmaz.
                    karakter_onay_gecisini_baslat()

        # -------------------------------------------------
        # KAYIT ADI
        # -------------------------------------------------

        elif oyun_durumu == KAYIT_ADI:
            if olay.type == pygame.KEYDOWN:
                if olay.key == pygame.K_ESCAPE:
                    oyun_durumu = ANA_MENU

                elif olay.key == pygame.K_BACKSPACE:
                    kayit_adi_girdisi = kayit_adi_girdisi[:-1]

                elif olay.key in (pygame.K_SPACE, pygame.K_RETURN, pygame.K_KP_ENTER):
                    kayit_adi_onayla()

                elif (
                    olay.unicode.isprintable()
                    and not olay.unicode.isspace()
                    and len(kayit_adi_girdisi) < 20
                ):
                    kayit_adi_girdisi += olay.unicode

        # -------------------------------------------------
        # ÇIKIŞ ONAY
        # -------------------------------------------------

        elif oyun_durumu == CIKIS_ONAY:
            if olay.type == pygame.KEYDOWN:
                if olay.key in (
                    ui_yukari_tuslari()
                    + ui_asagi_tuslari()
                    + ui_sol_tuslari()
                    + ui_sag_tuslari()
                ):
                    cikis_index = 1 - cikis_index

                elif olay.key == pygame.K_ESCAPE:
                    oyun_durumu = cikis_donus_durumu

                elif olay.key in buton_onay_tuslari():
                    v37_exit_confirm_schedule(cikis_index)

        # -------------------------------------------------
        # LOADING
        # -------------------------------------------------

        elif oyun_durumu == LOADING:
            # Loading tamamlanmadan hiçbir tuş işlem yapmaz.
            # ESC dahil hiçbir tuş ana menüye döndürmez.
            if olay.type == pygame.KEYDOWN:
                if loading_tamamlandi:
                    oyun_durumu = OYUN

        # -------------------------------------------------
        # OYUN
        # -------------------------------------------------

        elif oyun_durumu == OYUN:
            if olay.type == pygame.KEYDOWN:
                # Geliştirici CTRL testleri normal oyuncu inputundan önce ele alınır;
                # coin/level/toggle kontrolleri transient kalır ve save'i değiştirmez.
                if gelistirici_test_girdisi_uygula(olay):
                    continue

                # Ölüm ekranı kendi input modalıdır; pause/attack/envanter buraya sızmaz.
                if oyuncu_hp <= 0:
                    if oyuncu_olum_menu_hazir_mi():
                        if olay.key in ui_yukari_tuslari():
                            oyuncu_olum_menu_index = (oyuncu_olum_menu_index - 1) % 4
                        elif olay.key in ui_asagi_tuslari():
                            oyuncu_olum_menu_index = (oyuncu_olum_menu_index + 1) % 4
                        elif olay.key in buton_onay_tuslari():
                            # Ölüm menüsü de aynı click -> action kontratını kullanır.
                            v37_death_action_schedule(oyuncu_olum_menu_index)
                    continue

                if oyuncu_kontrol_kilitli_mi() and olay.key != tus_atamasi("pause"):
                    continue

                if onemli_item_penceresi_acik_mi():
                    # Progress dolmadan girdiyi yut; dolduktan sonra herhangi bir tuş ilerletir.
                    if onemli_item_girdisi_hazir_mi():
                        onemli_item_penceresini_ilerlet()
                    continue

                if onemli_item_on_sunum_bekliyor_mu():
                    continue

                if olay.key == tus_atamasi("pause"):
                    if oyun_alt_durumu not in (
                        DIYALOG,
                        DIYALOG_SECIM,
                    ):
                        duraklatma_index = 0
                        oyun_durumu = DURAKLATMA

                elif (
                    olay.key == pygame.K_r
                    and oyun_alt_durumu == HARITA
                    and gelistirici_x_skill_aktif
                    and oyuncu_saldiriyor
                    and oyuncu_saldiri_modu in ("press", "charge")
                ):
                    # R normal dash değildir. Ctrl+U açıkken hold-charge içindeyse yalnız
                    # special move kombinasyonunu arm eder; hareket R KEYUP'ta başlar.
                    gelistirici_x_skill_r_baslat(pygame.time.get_ticks())

                elif olay.key == tus_atamasi("save"):
                    oyun_kaydet()

                elif olay.key == tus_atamasi("inventory"):
                    # Envanter bağımsız bir modal durumdur. Açılırken önceki
                    # taşıma/aksiyon oturumları temizlenir; oyun girdileri durur.
                    envanter_aksiyon_acik = False
                    envanter_aksiyon_item_index = None
                    envanter_aksiyon_kaynagi = "grid"
                    envanter_tasima_kaynagi = None
                    one_cikan_tasima_kaynagi = None
                    oyun_durumu = ENVANTER

                elif olay.key == tus_atamasi("quick_use"):
                    secili_one_cikan_itemi_kullan()

                elif olay.key == tus_atamasi("q_quick_use"):
                    q_hizli_itemi_kullan()

                elif olay.key in (
                    pygame.K_1,
                    pygame.K_2,
                    pygame.K_3,
                    pygame.K_4,
                    pygame.K_5,
                ):
                    envanter_secili_slot = olay.key - pygame.K_1

                elif olay.key == tus_atamasi("attack") and oyun_alt_durumu == HARITA:
                    simdi = pygame.time.get_ticks()

                    if v106_corona_active_orbs():
                        v106_corona_fire_next(simdi)
                    elif karakter_cinsiyet == "male" and ADEFONSUS_YENI_SHEET_AKTIF:
                        # KEYDOWN yalnız press/charge adayını başlatır. Quick tap
                        # KEYUP'ta normal ikili animasyona, hold ise charge-release'e gider.
                        adefonsus_saldiri_baslat(simdi)
                    elif (
                        not oyuncu_saldiriyor
                        and not oyuncu_savunuyor
                        and simdi - son_saldiri_zamani >= saldiri_bekleme_suresi
                    ):
                        if oyuncu_stamina < SALDIRI_STAMINA_MALIYETI:
                            hud_uyari_baslat("stamina")
                        else:
                            oyuncu_stamina = max(
                                0.0,
                                oyuncu_stamina - SALDIRI_STAMINA_MALIYETI,
                            )
                            stamina_son_harcama = simdi
                            oyuncu_saldiriyor = True
                            oyuncu_saldiri_modu = "normal"
                            oyuncu_saldiri_sure_ms = saldiri_suresi
                            ADEFO_HOLD_GECIS_YAPILDI = False
                            dunya_olayi_kaydet("attack", mode="normal")
                            saldiri_baslangic = simdi
                            son_saldiri_zamani = simdi
                            animasyon_index = 0

                elif oyun_alt_durumu == DIYALOG:
                    if olay.key in ONAY_TUSLARI + (tus_atamasi("interact"),):
                        if diyalog_tamamlandi:
                            diyalog_ilerlet()
                        else:
                            diyalog_yazisini_tamamla()

                elif oyun_alt_durumu == DIYALOG_SECIM:
                    secim_sayisi = aktif_diyalog_secim_sayisi()

                    if secim_sayisi <= 0:
                        oyun_alt_durumu = HARITA

                    elif olay.key in ui_yukari_tuslari():
                        diyalog_secim_index = (diyalog_secim_index - 1) % secim_sayisi

                    elif olay.key in ui_asagi_tuslari():
                        diyalog_secim_index = (diyalog_secim_index + 1) % secim_sayisi

                    elif olay.key in ONAY_TUSLARI + (tus_atamasi("interact"),):
                        diyalog_secimini_onayla()

                elif oyun_alt_durumu == HARITA and olay.key == tus_atamasi("interact"):
                    oyuncu_etkilesim_yap()

            elif olay.type == pygame.KEYUP:
                # KEYUP ayrı işlenir; input debounce yalnız KEYDOWN içindir.
                # Böylece hold release auto-repeat veya menu debounce yüzünden kaybolmaz.
                if (
                    olay.key == pygame.K_r
                    and oyun_alt_durumu == HARITA
                    and gelistirici_x_skill_r_basildi
                ):
                    gelistirici_x_skill_r_birak(pygame.time.get_ticks())
                elif (
                    olay.key == tus_atamasi("attack")
                    and oyun_alt_durumu == HARITA
                    and karakter_cinsiyet == "male"
                    and ADEFONSUS_YENI_SHEET_AKTIF
                ):
                    adefonsus_saldiri_tusu_birakildi(pygame.time.get_ticks())

        # -------------------------------------------------
        # MERCHANT
        # -------------------------------------------------

        elif oyun_durumu == MERCHANT:
            v92_merchant_handle_event(olay)

        # -------------------------------------------------
        # BLACKSMITH
        # -------------------------------------------------

        elif oyun_durumu == BLACKSMITH:
            v92_blacksmith_handle_event(olay)

        # V92 keeps the inherited merchant state machine below for reference,
        # but its event branch is intentionally unreachable.
        elif False and oyun_durumu == MERCHANT:
            merchant_fade_bitti = (
                pygame.time.get_ticks() - merchant_acilis_zamani
                >= MERCHANT_ACILIS_FADE_SURESI
            )
            if (
                olay.type == pygame.KEYDOWN
                and merchant_fade_bitti
                and not merchant_kapanis_isteniyor
                and not merchant_kapanis_zamani
            ):
                # Merchant diyaloğunda ENTER ve SPACE artık aynı davranır:
                # yazı akıyorsa tamamlar, tamamlandıysa sonraki satıra geçer.
                if merchant_modal is None and olay.key in ONAY_TUSLARI:
                    if not merchant_yazi_tamamlandi:
                        merchant_diyalog_tamamla()
                        continue
                    if merchant_diyalog_index + 1 < len(merchant_diyalog_kuyrugu):
                        merchant_diyalog_sonraki()
                        continue
                    # Diyalog kuyruğu bittiyse aynı tuş aşağıdaki gerçek butonu onaylar.

                if merchant_modal == "price":
                    if olay.key == pygame.K_ESCAPE:
                        merchant_modal = None
                        merchant_bekleyen_islem = None
                    elif olay.key == pygame.K_BACKSPACE:
                        merchant_fiyat_girdisi = merchant_fiyat_girdisi[:-1]
                    elif olay.key in (
                        pygame.K_RETURN,
                        pygame.K_KP_ENTER,
                    ):
                        merchant_satis_onayi_baslat()
                    elif olay.unicode.isdigit() and len(merchant_fiyat_girdisi) < 7:
                        merchant_fiyat_girdisi += olay.unicode

                elif merchant_modal == "confirm":
                    if olay.key in (
                        ui_sol_tuslari()
                        + ui_sag_tuslari()
                        + ui_yukari_tuslari()
                        + ui_asagi_tuslari()
                    ):
                        merchant_onay_index = 1 - merchant_onay_index
                    elif olay.key == pygame.K_ESCAPE:
                        merchant_modal = None
                        merchant_bekleyen_islem = None
                    elif olay.key in buton_onay_tuslari():
                        if merchant_onay_index == 0:
                            merchant_islemi_uygula()
                        else:
                            button_click_sesi_cal("merchant2")
                            merchant_modal = None
                            merchant_bekleyen_islem = None

                elif olay.key == pygame.K_ESCAPE:
                    if merchant_sayfa == "menu":
                        merchant_kapat()
                    else:
                        merchant_alt_menu_geri()
                elif olay.key in ui_yukari_tuslari():
                    if merchant_sayfa == "menu":
                        merchant_menu_index = (merchant_menu_index - 1) % 3
                    else:
                        liste = merchant_aktif_liste()
                        if liste:
                            merchant_index = (merchant_index - 1) % len(liste)
                elif olay.key in ui_asagi_tuslari():
                    if merchant_sayfa == "menu":
                        merchant_menu_index = (merchant_menu_index + 1) % 3
                    else:
                        liste = merchant_aktif_liste()
                        if liste:
                            merchant_index = (merchant_index + 1) % len(liste)
                elif olay.key in buton_onay_tuslari():
                    if merchant_sayfa == "menu":
                        button_click_sesi_cal()
                    merchant_onayla()

        # -------------------------------------------------
        # ENVANTER
        # -------------------------------------------------

        elif oyun_durumu == ENVANTER:
            if olay.type == pygame.KEYDOWN:
                if gelistirici_test_girdisi_uygula(olay):
                    continue
                if olay.key == tus_atamasi("inventory") and not envanter_aksiyon_acik:
                    oyun_durumu = OYUN
                    continue
                # Aksiyon penceresi tam modaldır. Arkadaki grid, hızlı slotlar
                # ve oyun dünyası bu pencere kapanana kadar girdi almaz.
                if envanter_aksiyon_acik:
                    aksiyonlar = envanter_aksiyonlari(
                        envanter_aksiyon_item_index,
                        envanter_aksiyon_kaynagi,
                    )
                    aksiyon_sayisi = max(1, len(aksiyonlar))
                    if olay.key in (
                        pygame.K_ESCAPE,
                        pygame.K_BACKSPACE,
                    ):
                        envanter_aksiyon_acik = False
                        envanter_aksiyon_item_index = None
                        envanter_aksiyon_kaynagi = "grid"
                    elif olay.key in ui_yukari_tuslari():
                        envanter_aksiyon_index = (
                            envanter_aksiyon_index - 1
                        ) % aksiyon_sayisi
                    elif olay.key in ui_asagi_tuslari():
                        envanter_aksiyon_index = (
                            envanter_aksiyon_index + 1
                        ) % aksiyon_sayisi
                    elif olay.key in envanter_onay_tuslari():
                        button_click_sesi_cal()
                        item_index = envanter_aksiyon_item_index
                        kaynak = envanter_aksiyon_kaynagi
                        aksiyon = (
                            aksiyonlar[envanter_aksiyon_index % len(aksiyonlar)][0]
                            if aksiyonlar
                            else None
                        )

                        if aksiyon == "use":
                            secili_itemi_kullan(item_index)
                        elif aksiyon == "bind_q":
                            if q_hizli_item_index == item_index:
                                q_hizli_slotu_temizle()
                            else:
                                itemi_q_hizli_slota_ata(item_index)
                        elif aksiyon == "drop":
                            secili_itemi_at(item_index)
                        elif aksiyon == "unfeature":
                            secili_one_cikandan_cikar(envanter_secili_slot)
                        elif aksiyon == "feature":
                            one_cikan_atama_item_index = item_index
                        elif aksiyon == "move":
                            if kaynak == "featured":
                                one_cikan_tasimayi_baslat(envanter_secili_slot)
                            else:
                                envanter_tasimayi_baslat(item_index)

                        envanter_aksiyon_acik = False
                        envanter_aksiyon_item_index = None
                        envanter_aksiyon_kaynagi = "grid"

                # Grid itemini featured slota atama modu: yalnız 1-5 hedef seçer.
                elif one_cikan_atama_item_index is not None:
                    if olay.key in (
                        pygame.K_ESCAPE,
                        pygame.K_BACKSPACE,
                    ):
                        one_cikan_atama_item_index = None
                    elif olay.key in (
                        pygame.K_1,
                        pygame.K_2,
                        pygame.K_3,
                        pygame.K_4,
                        pygame.K_5,
                    ):
                        hedef_slot = olay.key - pygame.K_1
                        if secili_itemi_one_cikana_ata(
                            one_cikan_atama_item_index,
                            hedef_slot,
                        ):
                            envanter_secili_slot = hedef_slot
                            button_click_sesi_cal()
                        one_cikan_atama_item_index = None

                # Öne çıkan slot taşıma modu da modaldır. Yalnızca hedef slot
                # seçimi, onay ve iptal girdileri kabul edilir.
                elif one_cikan_tasima_kaynagi is not None:
                    if olay.key in (
                        pygame.K_ESCAPE,
                        pygame.K_BACKSPACE,
                    ):
                        one_cikan_tasima_kaynagi = None

                    elif olay.key in (
                        pygame.K_1,
                        pygame.K_2,
                        pygame.K_3,
                        pygame.K_4,
                        pygame.K_5,
                    ):
                        envanter_secili_slot = olay.key - pygame.K_1

                    elif olay.key in ui_sol_tuslari():
                        envanter_secili_slot = (envanter_secili_slot - 1) % 5

                    elif olay.key in ui_sag_tuslari():
                        envanter_secili_slot = (envanter_secili_slot + 1) % 5

                    elif olay.key in envanter_onay_tuslari() + (
                        tus_atamasi("quick_use"),
                    ):
                        one_cikan_slotlari_takasla(
                            one_cikan_tasima_kaynagi,
                            envanter_secili_slot,
                        )

                # Ana 30'lu grid taşıma modu. Hızlı slot ve oyun girdileri
                # hedef yerleştirilene veya işlem iptal edilene kadar kapalıdır.
                elif envanter_tasima_kaynagi is not None:
                    if olay.key in (
                        pygame.K_ESCAPE,
                        pygame.K_BACKSPACE,
                    ):
                        envanter_tasima_kaynagi = None

                    elif olay.key in ui_sol_tuslari():
                        col = envanter_imlec % 6
                        if col > 0:
                            envanter_imlec -= 1

                    elif olay.key in ui_sag_tuslari():
                        col = envanter_imlec % 6
                        if col < 5:
                            envanter_imlec += 1

                    elif olay.key in (pygame.K_UP, pygame.K_w):
                        row = envanter_imlec // 6
                        if row > 0:
                            envanter_imlec -= 6

                    elif olay.key in (
                        pygame.K_DOWN,
                        pygame.K_s,
                    ):
                        row = envanter_imlec // 6
                        if row < 4:
                            envanter_imlec += 6

                    elif olay.key in envanter_onay_tuslari():
                        envanter_itemlerini_takasla(
                            envanter_tasima_kaynagi,
                            envanter_imlec,
                        )

                else:
                    if olay.key in (
                        pygame.K_ESCAPE,
                        tus_atamasi("inventory"),
                    ):
                        oyun_durumu = OYUN

                    elif olay.key in (
                        pygame.K_1,
                        pygame.K_2,
                        pygame.K_3,
                        pygame.K_4,
                        pygame.K_5,
                    ):
                        # 1-5 yalnızca işlem yapılacak öne çıkan slotu seçer.
                        envanter_secili_slot = olay.key - pygame.K_1

                    elif olay.key in ui_sol_tuslari():
                        col = envanter_imlec % 6
                        if col > 0:
                            envanter_imlec -= 1

                    elif olay.key in ui_sag_tuslari():
                        col = envanter_imlec % 6
                        if col < 5:
                            envanter_imlec += 1

                    elif olay.key in (pygame.K_UP, pygame.K_w):
                        row = envanter_imlec // 6
                        if row > 0:
                            envanter_imlec -= 6

                    elif olay.key in (
                        pygame.K_DOWN,
                        pygame.K_s,
                    ):
                        row = envanter_imlec // 6
                        if row < 4:
                            envanter_imlec += 6

                    elif olay.key in envanter_onay_tuslari():
                        if envanter_itemleri[envanter_imlec] is not None:
                            envanter_aksiyon_menusunu_ac(envanter_imlec, "grid")

                    elif olay.key == tus_atamasi("q_quick_use"):
                        # Envanter açıkken Q doğrudan imleçteki kullanılabilir eşyayı
                        # bağımsız altıncı hızlı slota bağlar / bağlıysa çıkarır.
                        item = envanter_itemleri[envanter_imlec]
                        if isinstance(item, dict) and item_q_hizli_kullanima_uygun_mu(
                            item
                        ):
                            if q_hizli_item_index == envanter_imlec:
                                q_hizli_slotu_temizle()
                            else:
                                itemi_q_hizli_slota_ata(envanter_imlec)
                            button_click_sesi_cal()
                        else:
                            bildirim_goster(
                                bt(
                                    "Bu eşya Q hızlı kullanımına uygun değil.",
                                    "This item is not eligible for Q quick-use.",
                                )
                            )

                    elif olay.key == tus_atamasi("quick_use"):
                        # Hızlı-kullan tuşu envanter açıkken bağlamsal menüyü açar.
                        # Seçili öne çıkan slot için bağlamsal menüyü açar.
                        item_index = secili_one_cikan_item_index()
                        if not envanter_aksiyon_menusunu_ac(item_index, "featured"):
                            bildirim_goster(
                                bt(
                                    "Seçili öne çıkan slot boş.",
                                    "The selected featured slot is empty.",
                                )
                            )

        # -------------------------------------------------
        # DURAKLATMA MENÜSÜ
        # -------------------------------------------------

        elif oyun_durumu == DURAKLATMA:
            if olay.type == pygame.KEYDOWN:
                if olay.key in ui_yukari_tuslari():
                    duraklatma_index = (duraklatma_index - 1) % len(
                        duraklatma_secenekleri()
                    )

                elif olay.key in ui_asagi_tuslari():
                    duraklatma_index = (duraklatma_index + 1) % len(
                        duraklatma_secenekleri()
                    )

                elif olay.key in (
                    pygame.K_ESCAPE,
                    tus_atamasi("pause"),
                ):
                    oyun_durumu = OYUN

                elif olay.key in buton_onay_tuslari():
                    v37_pause_action_schedule(duraklatma_index)

        # -------------------------------------------------
        # OYUNDAN ÇIKIŞ ONAYI (ORTAK TASARIM)
        # -------------------------------------------------

        elif oyun_durumu == OYUNDAN_CIKIS_ONAY:
            if olay.type == pygame.KEYDOWN:
                if olay.key in (
                    ui_yukari_tuslari()
                    + ui_asagi_tuslari()
                    + ui_sol_tuslari()
                    + ui_sag_tuslari()
                ):
                    oyundan_cikis_onay_index = 1 - oyundan_cikis_onay_index

                elif olay.key == pygame.K_ESCAPE:
                    oyun_durumu = DURAKLATMA

                elif olay.key in buton_onay_tuslari():
                    v37_quit_confirm_schedule(oyundan_cikis_onay_index)

        # -------------------------------------------------
        # ANA MENÜYE DÖNÜŞ ONAYI
        # -------------------------------------------------

        elif oyun_durumu == ANA_MENU_ONAY:
            if olay.type == pygame.KEYDOWN:
                if olay.key in (
                    ui_yukari_tuslari()
                    + ui_asagi_tuslari()
                    + ui_sol_tuslari()
                    + ui_sag_tuslari()
                ):
                    ana_menu_onay_index = 1 - ana_menu_onay_index

                elif olay.key == pygame.K_ESCAPE:
                    oyun_durumu = ana_menu_onay_donus_durumu

                elif olay.key in buton_onay_tuslari():
                    v37_main_confirm_schedule(ana_menu_onay_index)

        # -------------------------------------------------
        # KAYIT SİLME ONAYI
        # -------------------------------------------------

        elif oyun_durumu == KAYIT_SIL_ONAY:
            if olay.type == pygame.KEYDOWN:
                if olay.key in (
                    ui_yukari_tuslari()
                    + ui_asagi_tuslari()
                    + ui_sol_tuslari()
                    + ui_sag_tuslari()
                ):
                    kayit_sil_onay_index = 1 - kayit_sil_onay_index

                elif olay.key == pygame.K_ESCAPE:
                    silinecek_kayit_yolu = None
                    oyun_durumu = LOAD_GAME

                elif olay.key in buton_onay_tuslari():
                    v37_delete_confirm_schedule(kayit_sil_onay_index)

        # -------------------------------------------------
        # AYARLAR
        # -------------------------------------------------

        elif oyun_durumu == AYARLAR:
            if olay.type == pygame.KEYDOWN:
                # Yeniden atama sırasında bir sonraki klavye girdisi doğrudan yakalanır.
                # Mouse olayı bu sisteme hiçbir noktada girmez.
                if tus_atama_bekleniyor is not None:
                    tus_atama_uygula(olay.key)
                    continue

                kategoriler = ayar_kategorileri()

                if ayar_odak == "kategori":
                    if olay.key in ui_yukari_tuslari():
                        ayar_kategori_index = (ayar_kategori_index - 1) % len(
                            kategoriler
                        )
                        ayar_index = 0
                    elif olay.key in ui_asagi_tuslari():
                        ayar_kategori_index = (ayar_kategori_index + 1) % len(
                            kategoriler
                        )
                        ayar_index = 0
                    elif olay.key in ui_sag_tuslari() or olay.key in ONAY_TUSLARI:
                        ayar_odak = "secenek"
                        ayar_index = 0
                        button_click_sesi_cal("menu1")
                    elif olay.key in ui_sol_tuslari() or olay.key == pygame.K_ESCAPE:
                        ayarlari_kaydet()
                        button_click_sesi_cal("menu1")
                        oyun_durumu = ayarlar_donus_durumu

                else:
                    secenekler = ayar_secenekleri()
                    secili_ayar = secili_ayar_anahtari()

                    if olay.key in ui_yukari_tuslari():
                        ayar_index = (ayar_index - 1) % len(secenekler)
                    elif olay.key in ui_asagi_tuslari():
                        ayar_index = (ayar_index + 1) % len(secenekler)
                    elif secili_ayar and secili_ayar.startswith("bind_"):
                        if olay.key in ONAY_TUSLARI:
                            if secili_ayar == "bind_reset":
                                tus_atamalari_varsayilana_don()
                            else:
                                tus_atama_baslat(secili_ayar)
                        elif olay.key == pygame.K_ESCAPE:
                            ayar_odak = "kategori"
                            button_click_sesi_cal("menu1")
                    elif olay.key in ui_sol_tuslari():
                        ayari_degistir(-1)
                    elif olay.key in ui_sag_tuslari():
                        ayari_degistir(1)
                    elif olay.key in ONAY_TUSLARI:
                        ayari_degistir(1)
                    elif olay.key == pygame.K_ESCAPE:
                        ayar_odak = "kategori"
                        button_click_sesi_cal("menu1")

        # -------------------------------------------------
        # LOAD GAME
        # -------------------------------------------------

        elif oyun_durumu == LOAD_GAME:
            if olay.type == pygame.KEYDOWN:
                dosyalar = kayitlari_listele()[:7]

                if olay.key == pygame.K_ESCAPE:
                    oyun_durumu = load_game_donus_durumu

                elif dosyalar:
                    if olay.key in ui_yukari_tuslari():
                        load_index = (load_index - 1) % len(dosyalar)

                    elif olay.key in ui_asagi_tuslari():
                        load_index = (load_index + 1) % len(dosyalar)

                    elif olay.key in ONAY_TUSLARI:
                        v37_load_game_schedule(dosyalar[load_index])

                    elif olay.key == pygame.K_DELETE:
                        silinecek_kayit_yolu = dosyalar[load_index]
                        kayit_sil_onay_index = 1
                        oyun_durumu = KAYIT_SIL_ONAY

        # -------------------------------------------------
        # CREDITS
        # -------------------------------------------------

        elif oyun_durumu == CREDITS:
            if olay.type == pygame.KEYDOWN:
                if olay.key in (
                    pygame.K_ESCAPE,
                    pygame.K_RETURN,
                    pygame.K_SPACE,
                ):
                    oyun_durumu = ANA_MENU

    # V37: click feedback state değişiminden önce birkaç frame görünür.
    v37_ui_transition_tick()

    # Seçim değişikliklerini olaylar işlendiği anda seslendir.
    secim_sesi_guncelle()

    # Karakter kartı onay/fade zaman çizelgesini güncelle.
    karakter_onay_gecisini_guncelle()

    # New-item kartı temiz haritada hazırlanır; ses bir saniye önce başlar.
    onemli_item_gosterimini_guncelle()

    # V34 quality orchestrator: pause compensation, buffered input, transient FX budget.
    v34_quality_tick()

    # V100: execution cutscenes own an independent clock. Main gameplay simulation
    # is frozen by oyun_sinematik_kilitli_mi(), but the authored scene still advances.
    v100_cinematic_update(pygame.time.get_ticks())

    # =====================================================
    # OYUNCU HAREKETİ
    # =====================================================

    oyuncu_hareket_ediyor = False

    if (
        oyun_durumu == OYUN
        and oyun_alt_durumu == HARITA
        and oyuncu_hp > 0
        and not oyun_sinematik_kilitli_mi()
    ):
        oyuncu_savunma_guncelle()

    if (
        oyun_durumu == OYUN
        and oyun_alt_durumu == HARITA
        and oyuncu_hp > 0
        and not oyun_sinematik_kilitli_mi()
    ):
        oyuncu_zorlanmis_hareket_guncelle()
        oyuncu_serbest_hareket_guncelle()

    if oyun_durumu == OYUN and not oyun_sinematik_kilitli_mi():
        stamina_guncelle()

    if (
        oyun_durumu == OYUN
        and oyun_alt_durumu == HARITA
        and oyuncu_hp > 0
        and not oyun_sinematik_kilitli_mi()
    ):
        simdi_combat = pygame.time.get_ticks()
        if oyuncu_saldiriyor:
            oyuncu_saldiri_gecislerini_guncelle(simdi_combat)
            # Heavy release hareketi enemy update'ten önce çözülür. Böylece aynı
            # frame'deki hitbox, ekranda görülen yeni oyuncu konumuyla eşleşir.
            if oyuncu_saldiri_modu == "hold_release":
                adefonsus_hold_dash_guncelle(simdi_combat)
        common_enemy_guncelle()

    if oyun_durumu == OYUN and oyun_alt_durumu == HARITA:
        kan_gore_guncelle()
        oyuncu_olum_durumu_guncelle()

    # ses katmanı: hareket çözüldükten sonra footstep phase'i, state değiştikten
    # sonra da harita ambience'i güncellenir. Boş kılıç swing'i burada ses üretmez.
    adefonsus_footstep_guncelle()
    map_ambience_guncelle()

    # Her kare çalışan arka plan veri katmanı; modal/sinematik durumlarda
    # aktif zamanı ilerletmez ve sıçrayan delta-time üretmez.
    dunya_simulasyon_guncelle()

    if oyuncu_saldiriyor:
        simdi_saldiri = pygame.time.get_ticks()
        sureli_faz = not (
            karakter_cinsiyet == "male"
            and ADEFONSUS_YENI_SHEET_AKTIF
            and oyuncu_saldiri_modu in ("press", "charge")
        )
        if (
            sureli_faz
            and simdi_saldiri - saldiri_baslangic >= oyuncu_aktif_saldiri_suresi_ms()
        ):
            oyuncu_saldiri_durumunu_sifirla()

    if (
        oyun_durumu == OYUN
        and otomatik_kayit
        and aktif_kayit
        and not oyun_sinematik_kilitli_mi()
    ):
        simdi = pygame.time.get_ticks()
        if simdi - son_otomatik_kayit >= otomatik_kayit_araligi:
            if oyun_kaydet():
                son_otomatik_kayit = simdi

    # =====================================================
    # EKRAN ÇİZİMİ
    # =====================================================

    if oyun_durumu == ANA_MENU:
        ana_menu_ciz()

    elif oyun_durumu == KARAKTER_OLUSTUR:
        karakter_olusturma_ciz()

    elif oyun_durumu == KAYIT_ADI:
        kayit_adi_ekrani_ciz()

    elif oyun_durumu == CIKIS_ONAY:
        cikis_onay_ciz()

    elif oyun_durumu == LOADING:
        loading_ekrani_ciz()

    elif oyun_durumu == OYUN:
        oyun_ekrani_ciz()

    elif oyun_durumu == MERCHANT:
        merchant_ekrani_ciz()

    elif oyun_durumu == BLACKSMITH:
        blacksmith_ekrani_ciz()

    elif oyun_durumu == ENVANTER:
        envanter_ciz()

    elif oyun_durumu == DURAKLATMA:
        duraklatma_menusu_ciz()

    elif oyun_durumu == OYUNDAN_CIKIS_ONAY:
        oyundan_cikis_onay_ciz()

    elif oyun_durumu == ANA_MENU_ONAY:
        ana_menu_onay_ciz()

    elif oyun_durumu == AYARLAR:
        ayarlar_ciz()

    elif oyun_durumu == LOAD_GAME:
        load_game_ciz()

    elif oyun_durumu == KAYIT_SIL_ONAY:
        kayit_sil_onay_ciz()

    elif oyun_durumu == CREDITS:
        credits_ciz()

    parlaklik_kaplamasi_ciz()

    pygame.display.flip()

    saat.tick(FPS)

# =========================================================
# KAPATMA
# =========================================================

ayarlari_kaydet()

pygame.quit()

sys.exit()

# </POTBO_STAGE S2676>

