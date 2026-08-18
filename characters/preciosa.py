# Path of the Bloodied One — categorized source stages
#
# This file is intentionally executed by core/bootstrap.py in original source order.
# Keeping one shared runtime namespace avoids gameplay regressions while the former
# 90k-line monolith is physically separated by responsibility. Do not import this
# file directly; edit the stage code normally and launch root main.py.

# <POTBO_STAGE S0020>

KADIN_LOADING_YOLU = os.path.join(ASSETS, "backgrounds", "loading_female.png")
# </POTBO_STAGE S0020>

# <POTBO_STAGE S0025>

KADIN_SHEET_YOLU = os.path.join(ASSETS, "characters", "female_sheet.png")
# </POTBO_STAGE S0025>

# <POTBO_STAGE S0057>

PRECIOSA_PORTRE_YOLU = os.path.join(ASSETS, "portraits", "preciosa.png")
# </POTBO_STAGE S0057>

# <POTBO_STAGE S0064>

PRECIOSA_KART_ADAYLARI = [
    os.path.join(ASSETS, "portraits", "preciosa_card.jpeg"),
    os.path.join(ASSETS, "portraits", "preciosa_card.jpg"),
    os.path.join(BASE_DIR, "2.jpeg"),
    PRECIOSA_PORTRE_YOLU,
]
# </POTBO_STAGE S0064>

# <POTBO_STAGE S0066>

PRECIOSA_KART_YOLU = mevcut_ilk_dosya(PRECIOSA_KART_ADAYLARI)
# </POTBO_STAGE S0066>

# <POTBO_STAGE S0079>

KADIN_IPUCLARI = {
    "TR": [
        (
            "Preciosa'nın en büyük avantajı hızıdır. Uzun saldırı zincirleri yapmak yerine "
            "kısa ve kontrollü vuruşlarla rakibin açığını beklemek, hem mana tasarrufu sağlar "
            "hem de kritik vuruş ihtimalini yükseltir."
        ),
        (
            "Hızlı karakterler sürekli saldırmak zorunda değildir. Düşmanın hareketini gözlemleyip "
            "tam saldırı anında yana kaçmak, Preciosa'nın karşı saldırı bonusundan daha fazla "
            "yararlanmasını sağlayabilir."
        ),
        (
            "Mana miktarın yüksek olsa bile bütün yetenekleri arka arkaya kullanma. "
            "Bazı düşmanlar ikinci aşamada daha saldırgan hale gelir; güçlü büyülerini ve "
            "özel saldırılarını savaşın bu bölümü için saklamak daha güvenlidir."
        ),
        (
            "Preciosa'nın hafif zırhı hareket kabiliyetini artırır ancak ağır darbeler karşısında "
            "daha az koruma sağlar. Büyük düşmanların önünde sabit durmak yerine çevrelerinde "
            "hareket ederek saldırı yönlerini bozmayı dene."
        ),
        (
            "Kritik vuruş oranını artıran eşyalar Preciosa için sıradan hasar eşyalarından "
            "daha değerli olabilir. Hızlı saldırılar sayesinde küçük bir kritik oran artışı bile "
            "uzun savaşlarda büyük bir toplam hasar farkı oluşturur."
        ),
        (
            "Bazı gizli geçitler yalnızca belirli açılardan fark edilir. Mağaralarda duvarların "
            "kenarlarını, kırık sütunları ve farklı renkteki zemin taşlarını dikkatlice incele; "
            "nadir eşyalar çoğu zaman ana yolun dışında saklanır."
        ),
        (
            "NPC'lerle yalnızca bir kez konuşup geçme. Görev tamamlandıktan, önemli bir eşya "
            "bulduktan veya yeni bir bölgeye ulaştıktan sonra aynı karaktere dönmek, farklı "
            "diyaloglar ve ek ödüller açabilir."
        ),
        (
            "Canın azaldığında saldırı hızına güvenip risk alma. Güvenli bir mesafe oluşturmak, "
            "düşmanın saldırı düzenini yeniden okumak ve iyileşmek için doğru anı beklemek "
            "çoğu zaman savaşı kazanmanın en sağlam yoludur."
        ),
        (
            "Preciosa ile oynarken hareket, saldırının bir parçasıdır. Bir vuruştan sonra aynı "
            "noktada kalmak yerine yön değiştirerek ilerlemek, düşmanın seni hedeflemesini zorlaştırır "
            "ve yeni bir kritik saldırı açısı oluşturur."
        ),
    ],
    "EN": [
        (
            "Preciosa's greatest advantage is speed. Instead of using long attack chains, "
            "wait for an opening and strike with short, controlled combinations to conserve mana "
            "and improve your chance of landing critical hits."
        ),
        (
            "A fast character does not need to attack constantly. Watch the enemy's movement and "
            "dodge sideways at the exact moment of impact to create a safer opportunity for "
            "Preciosa's counterattack."
        ),
        (
            "Even with a large mana pool, avoid using every ability at once. Some enemies become "
            "more aggressive during later phases, so saving powerful spells and special attacks "
            "can make the final part of a fight much easier."
        ),
        (
            "Preciosa's lighter armor improves mobility but provides less protection against "
            "heavy blows. Keep moving around large enemies instead of standing directly in front "
            "of them, and force them to change their attack direction."
        ),
        (
            "Items that improve critical chance can be more valuable to Preciosa than ordinary "
            "damage upgrades. Her rapid attacks allow even a small critical increase to create "
            "a major difference during longer encounters."
        ),
        (
            "Some hidden passages can only be noticed from certain angles. Inspect cave walls, "
            "broken pillars and unusually colored floor tiles carefully, because rare items are "
            "often hidden away from the main route."
        ),
        (
            "Do not speak to an NPC only once. Returning after completing a quest, finding an "
            "important item or entering a new region can unlock different dialogue and additional rewards."
        ),
        (
            "When health is low, do not rely on attack speed and take unnecessary risks. Create "
            "distance, study the enemy's pattern again and wait for a safe opportunity to recover."
        ),
        (
            "Movement is part of every attack when playing Preciosa. Change direction after each "
            "strike instead of remaining in the same position, making it harder for enemies to target you."
        ),
    ],
}
# </POTBO_STAGE S0079>

# <POTBO_STAGE S0221>

kadin_loading_arka_plan = resim_yukle(KADIN_LOADING_YOLU, (GENISLIK, YUKSEKLIK), False)
# </POTBO_STAGE S0221>

# <POTBO_STAGE S0224>

kadin_sheet = resim_yukle(KADIN_SHEET_YOLU)
# </POTBO_STAGE S0224>

# <POTBO_STAGE S0280>

preciosa_portre = resim_yukle(PRECIOSA_PORTRE_YOLU)
# </POTBO_STAGE S0280>

# <POTBO_STAGE S0285>

preciosa_kart_portre = (
    resim_yukle(PRECIOSA_KART_YOLU) if PRECIOSA_KART_YOLU else preciosa_portre
)
# </POTBO_STAGE S0285>

# <POTBO_STAGE S0293>

# Kadın sheet: 4 sütun × 3 satır
kadin_kareleri = sheet_parcala(kadin_sheet, 4, 3)
# </POTBO_STAGE S0293>

# <POTBO_STAGE S0334>


# =========================================================
# LOADING
# =========================================================


def loading_baslat():
    global oyun_durumu
    global loading_baslangic
    global loading_ipucu
    global loading_tamamlandi

    simdi = pygame.time.get_ticks()
    # Loading ekranı kendi başına fade/siyah bekleme kullanmaz.
    loading_baslangic = simdi

    if karakter_cinsiyet == "female":
        loading_ipucu = random.choice(KADIN_IPUCLARI[dil])
    else:
        loading_ipucu = random.choice(IPUCLARI[dil])

    loading_tamamlandi = False

    oyun_durumu = LOADING
# </POTBO_STAGE S0334>

# <POTBO_STAGE S1052>
KADIN_IPUCLARI = {
    "TR": [
        "Preciosa hız değil düzen ister; hız onun sonucu olur.",
        "Açıyı al, sonra vur. Tersi çoğu kez israf olur.",
        "Mana bittiğinde stil değil niyet ortaya çıkar.",
        "Kısa geri çekilme, panik değil yeniden ölçümdür.",
        "Kitleyi yakarken güvenli çıkışını da önceden çiz.",
        "Baskı, aynı yere gitmek değil aynı niyeti korumaktır.",
        "İsabetsiz bir büyü, sessiz bir itiraf gibidir.",
        "Zayıf hedefe değil, açık veren hedefe git.",
    ],
    "EN": [
        "Preciosa does not seek speed first; speed emerges from order.",
        "Take the angle, then strike. Reversing it is usually waste.",
        "When mana runs dry, intent remains after style is gone.",
        "A short retreat is measurement, not panic.",
        "When you burn a group, draw your safe exit first.",
        "Pressure is not repeating a path; it is repeating an intention.",
        "A missed spell is a quiet confession.",
        "Do not chase the weak target; chase the exposed one.",
    ],
}
# </POTBO_STAGE S1052>

# <POTBO_STAGE S1105>

KADIN_IPUCLARI = {
    "TR": [
        "Preciosa hız değil düzen ister; hız onun sonucu olur.",
        "Açıyı al, sonra vur. Tersi çoğu kez israf olur.",
        "Mana bittiğinde stil değil niyet ortaya çıkar.",
        "Kısa geri çekilme, panik değil yeniden ölçümdür.",
        "Kitleyi yakarken güvenli çıkışını da önceden çiz.",
        "Baskı, aynı yere gitmek değil aynı niyeti korumaktır.",
        "İsabetsiz bir büyü, sessiz bir itiraf gibidir.",
        "Zayıf hedefe değil, açık veren hedefe git.",
        "İlk açıklık yem olabilir; ikinci açıklık çoğu kez gerçektir.",
        "Mana fazlası hata hakkı değildir, başka bir rota satın alır.",
        "Düz çizgide hızlısın; çapraz çizgide tehlikelisin.",
        "Bir adım geri bazen iki saldırıyı aynı anda bozar.",
        "Büyüyü en uzağa değil, kaçışını kapatmayacak yere bırak.",
        "Rakibin dönüşü de saldırının bir parçasıdır.",
        "Hızlı olmak, erken davranmak değildir.",
        "Kritik vuruş şans değil; doğru açıya daha çok kez ulaşmaktır.",
        "Ağır rakibin ritmini boz; ağırlığını onun yerine sen taşıma.",
        "Q bir çözüm olabilir. Her sorun Q istemez.",
        "Stamina korunursa hareket seçenekleri de korunur.",
        "Bir büyüden sonra aynı çizgide kalma.",
        "Farelerin kaçtığı yön bazen yaklaşan tehlikeyi senden önce bilir.",
        "Kanlı alan yalnız geçmişi değil, oradaki ekosistemi de değiştirir.",
    ],
    "EN": [
        "Preciosa does not seek speed first; speed emerges from order.",
        "Take the angle, then strike. Reversing it is usually waste.",
        "When mana runs dry, intent remains after style is gone.",
        "A short retreat is measurement, not panic.",
        "When you burn a group, draw your safe exit first.",
        "Pressure is not repeating a path; it is repeating an intention.",
        "A missed spell is a quiet confession.",
        "Do not chase the weak target; chase the exposed one.",
        "The first opening may be bait; the second is often real.",
        "Extra mana is not permission to fail; it buys another route.",
        "You are fast in a straight line and dangerous on an oblique one.",
        "One step back can break two attacks at once.",
        "Place the spell where it will not close your own escape.",
        "An enemy's turn is part of the attack.",
        "Being fast is not the same as acting early.",
        "A critical hit is less luck than reaching the right angle more often.",
        "Break a heavy enemy's rhythm; do not carry their weight for them.",
        "Q can be an answer. Not every problem asks for Q.",
        "Preserved stamina means preserved movement options.",
        "Do not stay on the same line after casting.",
        "The direction rats flee can reveal danger before you see it.",
        "A bloody place changes more than its history; it changes its ecology.",
    ],
}
# </POTBO_STAGE S1105>

# <POTBO_STAGE S1107>


def loading_baslat():
    global oyun_durumu, loading_baslangic, loading_ipucu, loading_tamamlandi
    simdi = pygame.time.get_ticks()
    loading_baslangic = simdi
    pool = KADIN_IPUCLARI[dil] if karakter_cinsiyet == "female" else IPUCLARI[dil]
    adaylar = [hint for hint in pool if hint not in v42_recent_loading_hints]
    if not adaylar:
        adaylar = list(pool)
        v42_recent_loading_hints.clear()
    loading_ipucu = random.choice(adaylar)
    v42_recent_loading_hints.append(loading_ipucu)
    loading_tamamlandi = False
    oyun_durumu = LOADING
# </POTBO_STAGE S1107>

# <POTBO_STAGE S1520>

KADIN_IPUCLARI = {
    "TR": [
        "Preciosa ile aynı çizgide uzun süre kalma; açı değiştir.",
        "Staminayı sıfırlama; son kısmını dash için sakla.",
        "Düşmanın hazırlık animasyonunu görünce yana çık.",
        "K ile savun; ağır darbeyi mümkünse dash ile kaçır.",
        "Büyü kullandıktan sonra aynı noktada bekleme.",
        "Q hızlı slot büyüler içindir.",
        "Ateş büyüsünü kullanırken kendi çıkış yolunu açık bırak.",
        "Heads Thrower'a düz bir atış hattı bırakma.",
        "Zor bir savaştan önce F5 ile kaydet.",
        "Kan 20 dakikada tamamen kurur; kendi kendine silinmez.",
        "Kurtçuklar ıslak kanla beslenip çoğalır; fareler onları avlar.",
        "Yerdeki organlar fareleri bölgeye çekebilir.",
    ],
    "EN": [
        "With Preciosa, do not stay on one line for long; change the angle.",
        "Do not empty your stamina; keep the last part for a dash.",
        "Move sideways as soon as you read an enemy's wind-up.",
        "Guard with K; evade heavy blows with a dash when possible.",
        "Do not remain in the same spot after casting a spell.",
        "The Q quick slot is used for spells.",
        "Keep your own escape route open when using fire.",
        "Do not give Heads Thrower a clean firing lane.",
        "Save with F5 before a difficult fight.",
        "Blood fully dries in 20 minutes and does not vanish by itself.",
        "Maggots feed and breed on wet blood; rats hunt the maggots.",
        "Organs left on the ground can attract rats to the area.",
    ],
}
# </POTBO_STAGE S1520>

# <POTBO_STAGE S1539>

KADIN_IPUCLARI = {
    "TR": [
        (
            "Preciosa'nın gelişimi düz önden hasardan çok açı ve tempo ödüllendirir. Hafif çapraz girişler ilerleyen seviyelerde ek değer kazanır; hedefe tam yapışmak yerine kılıcın orta-uç bölümünü koruyacak mesafeyi dolaşarak bul."
        ),
        (
            "Preciosa'nın mana yenilenme gecikmesi daha kısadır. Bu avantaj büyüleri arka arkaya boşaltmak için değil, kısa bir konum değişiminden sonra yeniden büyü tehdidi kurabilmek için değerlidir."
        ),
        (
            "Savunmayı darbeden hemen önce açarsan frontal temasta parry oluşabilir. Başarılı parry saldırganı kısa süre kilitler ve yaklaşık 0,7 saniyelik riposte penceresi verir; Preciosa'nın hızlı toparlanması bu pencereyi iyi kullanır."
        ),
        (
            "Seviye 9 civarında hızlı ikinci temas ve daha kısa tempo aralıkları önem kazanmaya başlar. İlk vuruştan sonra rakibin içine koşmak yerine küçük bir açı değiştirip ikinci temiz teması kurmak daha güvenlidir."
        ),
        (
            "Seviye 13 ve sonrasında akış odaklı teknikler ardışık temiz vuruşlardan daha çok yararlanır. Zinciri korumak için her vuruşu mümkün olan en erken anda değil, recovery'nin izin verdiği anda bağla."
        ),
        (
            "Hemoraji tick'leri hedefi öldüremez ve 1 HP'de durur. Preciosa ile kanayan bir hedefi bitirirken uzun bir büyü animasyonuna girmek yerine kısa ve temiz bir melee açıklığı çoğu zaman daha güvenlidir."
        ),
        (
            "Ateş patlamasının merkezinde kalmak ile dış halkayı kullanmak farklı sonuç verir. Kalabalığı yalnız dağıtmak istiyorsan dış halka yeterli olabilir; böylece kendi kaçış hattını kapatmadan alan kazanırsın."
        ),
        (
            "Parry yön bağımlıdır. Hızlı olduğun için düşmanın arkasına veya yanına geçmek kolaydır ama savunma anında tehdide dönük değilsen mükemmel zamanlama bile riposte üretmez."
        ),
        (
            "Preciosa ilerleyen seviyelerde kılıç ucundaki temas cezasını daha iyi tolere eder. Bu yine de maksimum menzilden rastgele savurmak anlamına gelmez; hafif çapraz ve kontrollü uç teması en iyi sonucu verir."
        ),
        (
            "Kan 20 dakikada kurur ve kendiliğinden kaybolmaz. Kurtçukların belirdiği eski bir kan alanı, fareler gelmezse uzun süre canlı bir mikro-ekosistem olarak kalabilir ve kanı yakın noktalara taşıyabilir."
        ),
        (
            "Fareler yalnız dekor değildir: kurtçukları önceleyerek kanın çevreye yayılmasını baskılar, ardından organ ve kan kütlesini yavaşça azaltırlar. Farelerin kaybolduğu bir alanda kan temizliğinin belirgin biçimde yavaşlaması normaldir."
        ),
        (
            "Heads Thrower'a karşı hızını düz çizgide mesafe kapatmak için harcamak zorunda değilsin. Önce atış hattını araziyle kesip sonra çapraz yaklaşmak, açık alanda doğrudan koşmaktan daha az risklidir."
        ),
        (
            "Düşük canlı hedefe karşı ilerleyen seviyelerde 'Son Açıklık' benzeri execution teknikleri devreye girer. Bonus gerçek temas ister; hızlı karakter olman, kılıcın hedefin yanından geçmesini telafi etmez."
        ),
        (
            "Preciosa'nın güçlü tarafı sürekli hareket etmek değil, hareketle saldırı geometrisini değiştirmektir. Aynı düşmana iki kez aynı çizgiden girmek yerine ikinci girişte açıyı değiştirerek hem saldırı hattını hem kaçış hattını yenile."
        ),
    ],
    "EN": [
        (
            "Preciosa's progression rewards angle and tempo more than simple frontal damage. Slightly oblique entries gain more value later on, so circle into a distance that keeps contact around the middle-to-outer part of the blade."
        ),
        (
            "Preciosa has a shorter mana-regeneration delay. That advantage is more useful for rebuilding spell pressure after a brief reposition than for emptying every spell back-to-back."
        ),
        (
            "Opening guard immediately before a frontal impact can produce a parry. A successful parry briefly locks the attacker and creates roughly a 0.7-second riposte window, which Preciosa's quick recovery can exploit well."
        ),
        (
            "Around level 9, fast second contact and tighter tempo windows begin to matter more. Instead of running into the target after the first hit, make a small angle change and establish a second clean contact."
        ),
        (
            "From level 13 onward, flow-oriented techniques benefit more from consecutive clean strikes. Preserve the chain by linking attacks when recovery permits, not simply at the earliest possible input."
        ),
        (
            "Hemorrhage ticks cannot kill and stop at 1 HP. Against a bleeding target, a short clean melee opening is often safer than committing to a long cast purely to finish the last point of health."
        ),
        (
            "The center and edge of a fire explosion have different jobs. If you only need to separate a group, the outer ring may be enough and can gain space without closing your own escape route."
        ),
        (
            "Parry is direction-dependent. Speed makes it easy to move around a target, but if you are not facing the threat when the hit arrives, perfect timing still will not create a riposte."
        ),
        (
            "At later levels, Preciosa becomes more tolerant of contact near the blade tip. That does not make maximum-range swings free; controlled, slightly oblique tip contact is still the better geometry."
        ),
        (
            "Blood dries in 20 minutes and never disappears merely because it is old. A field with mature maggots can remain a living micro-ecology for a long time if rats do not arrive to suppress it."
        ),
        (
            "Rats are mechanical actors, not decoration: they prioritize maggots, reducing further blood spread, then slowly consume organs and blood mass. Cleanup should therefore slow noticeably where rats are absent."
        ),
        (
            "Against Heads Thrower, speed does not have to mean charging down a straight line. Break the firing lane with terrain first, then approach diagonally; it is safer than crossing open ground directly."
        ),
        (
            "Later execution techniques reward contact against critically wounded targets. The reward still requires a real hit, so character speed cannot compensate for the blade passing beside the target."
        ),
        (
            "Preciosa's strength is not movement for its own sake; movement changes attack geometry. Avoid entering the same enemy twice on the same line—change the second angle so both your strike line and escape line are renewed."
        ),
    ],
}
# </POTBO_STAGE S1539>

# <POTBO_STAGE S1551>


def v77_diagnostics():
    return {
        "version": V77_VERSION,
        "death_palette": (
            V77_DEATH_BLACK,
            V77_DEATH_BLOOD,
            V77_DEATH_BODY,
        ),
        "death_tableau_preserved": True,
        "static_control_guides": False,
        "developer_shortcut_panel": False,
        "hint_count_male": len(IPUCLARI["TR"]),
        "hint_count_female": len(KADIN_IPUCLARI["TR"]),
    }
# </POTBO_STAGE S1551>

# <POTBO_STAGE S1563>
KADIN_IPUCLARI["TR"] = [
    "Hız, saldırının yerine geçmez. Vur-kaç ritmini korursan daha az bedel ödersin.",
    "Aynı yerde kalma. Her vuruştan sonra küçük bir yön değişikliği yeni bir açıklık yaratır.",
    "Düşmanın yanına çıkmak çoğu zaman önünde kalmaktan daha güvenlidir.",
    "Bütün kaynaklarını ilk anda harcama. Zor savaşların sonu çoğu kez daha tehlikelidir.",
    "Kalabalıkta tek bir hedefe takılma. Sana en yakın tehdidi temizleyip alan aç.",
    "Büyük düşmana karşı sabit durma. Çevresinde dolaşmak doğrudan çarpışmaktan iyidir.",
    "Gizli yerleri aceleyle geçme. Duvar kenarları ve kırık yapılar çoğu zaman bir şey saklar.",
    "Canın azken uzaklaş ve nefes al. Güvenli fırsat gelmeden baskıyı sürdürme.",
    "Hareketin amaçlı olsun. Boş kaçış yerine yeni saldırı çizgisi kur.",
]
KADIN_IPUCLARI["EN"] = [
    "Speed is not a substitute for judgment. A hit-and-move rhythm usually costs less.",
    "Do not stay in one place. A small direction change after each hit creates a new opening.",
    "Standing at an enemy's side is often safer than staying in front of them.",
    "Do not spend every resource at once. The final part of a difficult fight is often the most dangerous.",
    "Do not tunnel on one target in a crowd. Clear the nearest threat and create space first.",
    "Do not stand still against larger enemies. Moving around them is better than meeting them head-on.",
    "Do not rush past suspicious spaces. Wall edges and broken structures often hide something.",
    "When health is low, step away and breathe. Do not force pressure before a safe chance appears.",
    "Move with intention. Escape should create the next attack line, not just distance.",
]
# </POTBO_STAGE S1563>

# <POTBO_STAGE S2113>
v89_replace_ecology_hints(KADIN_IPUCLARI)
# </POTBO_STAGE S2113>

# <POTBO_STAGE S2435>

# ---------------------------------------------------------
# LOADING HINTS
# Final hint pool: concise, actionable and tied to systems that actually exist.
# Female pool contains the same core rules plus Preciosa-specific advice because
# the loading screen selects KADIN_IPUCLARI exclusively for her.
# ---------------------------------------------------------
V99_COMMON_HINTS_TR = [
    "E yalnızca dünya etkileşimi içindir: NPC'lerle konuşur, nesneleri toplar ve diyalogları ilerletir. Menü onayı için ENTER veya SPACE kullan.",
    "1-5 tuşları öne çıkan envanter slotunu seçer; F seçili slottaki eşyayı kullanır. Q ise bağımsız hızlı eşya veya büyü slotudur.",
    "Büyüler yalnızca Q hızlı slotundan kullanılır. Savaş öncesinde kullanacağın büyünün Q'ya bağlı olduğunu kontrol et.",
    "F5 ile güvenli anlarda kayıt al. Zor bir çatışmadan, alışverişten veya önemli bir geliştirmeden sonra kaydetmek ilerleme kaybını önler.",
    "Stamina yalnız saldırı için değildir; dash, savunma ve ağır teknikler de aynı kaynağı tüketir. Barı tamamen boşaltmak kaçış seçeneğini elinden alır.",
    "Yaralandıkça kullanılabilir stamina kapasiten ve yenilenme hızın düşer. Stamina barındaki kapasite işareti, o anda erişebileceğin gerçek üst sınırı gösterir.",
    "Canın kritik seviyedeyken saldırı temposunu düşür. Ağır yaralar hareketini, stamina ekonomini ve saldırı ritmini doğrudan zayıflatır.",
    "K ile savun. Saldırı geldiği anda savunmaya geçmek, sürekli blok tutmaktan daha az stamina harcatır ve karşı saldırı için daha iyi bir pencere bırakır.",
    "Normal dash için SHIFT ile birlikte bir hareket yönü kullan. Dash'i yalnız mesafe kazanmak için değil, düşmanın saldırı çizgisinden çıkmak için zamanla.",
    "Bir düşmanın saldırı hazırlığını gördüğünde hemen saldırıya yüklenme. Startup hareketini okuyup yana çıkmak çoğu zaman bloklamaktan daha güvenlidir.",
    "Zırhlı hedeflere rastgele saldırı zinciri uygulama. Temiz bir temas, boşluğa savrulan birkaç vuruştan daha değerlidir.",
    "Berserker kısa dash'lerle mesafeyi kapatabilir. Düz geri kaçmak yerine çapraz hareket ederek saldırı koridorunu boz.",
    "Uzak saldırı kullanan düşmanlara düz bir çizgide koşma. Küçük yön değişiklikleri mermilerin önüne geçmesini zorlaştırır.",
    "Kalabalıkta en düşük canlı hedefe değil, sana en yakın ve saldırıya hazır tehdide öncelik ver. Alan açmak toplam hasardan daha değerlidir.",
    "Sphaera Exothermica'nın patlama merkezinde hasar ve itme daha güçlüdür. Dış bölgeyi alan açmak, merkezi ise bitirici vuruş için kullan.",
    "Sphaera Exothermica'nın patladığı yerde kalan alevler sana da zarar verebilir. Büyüyü kendi kaçış yolunun üzerine bırakma.",
    "Draco Calcinans tek bir hedefe odaklanır; hedefi yakalayıp sarar ve ardından yoğun ısı uygular. Kalabalık kontrolü için değil, önemli bir hedefi baskılamak için kullan.",
    "Mana yenilenmesini beklerken Q'ya tekrar basmak kaynak üretmez. Büyüler arasında konum değiştirerek melee veya savunma temposuna dön.",
    "Hanus ile pazarlık yaparken ilk rakamı doğru kabul etme. İkna seçenekleri fiyatı düşürebilir; Hanus bazen anlaşmayı kendi lehine çevirmeye çalışır.",
    "Reinald eşya satmaz; teknik öğretir ve kalıcı geliştirmeler yapar. Altın harcamadan önce hangi kaynağın seni gerçekten sınırladığını belirle.",
    "Decussatio Rubra, Reinald'da beş eğitim tamamlandıktan sonra açılır. J'yi basılı tutup R ile tekniği hazırla.",
    "Catena Decollationis, beş eğitim tamamlandıktan sonra açılır. Birbirine yakın en az iki hedef varken J'yi basılı tutup SHIFT'e bas; hareket tuşu gerekmez.",
    "Catena için J'yi çok kısa tutup bırakma. Kombinasyon, ağır saldırı şarj eşiğine ulaştığında devreye girer.",
    "Catena hedefleri baktığın yönde arar. Teknik başlamıyorsa önce hedefe dön; ardından J + SHIFT kombinasyonunu kullan.",
    "Ağır saldırı hazırlarken yönünü önceden seç. Release başladıktan sonra karakterin hamlesi commitment taşır ve son anda keskin yön değiştiremez.",
    "Düşmanı ateş alanına itmek güçlüdür; fakat aynı ateş alanına kendin girmek de hasar verir. Patlama sonrasında zemini tekrar oku.",
    "Kanlı bölgeler zamanla çevredeki küçük canlıların davranışını etkileyebilir. Eski bir savaş alanına döndüğünde çevre önceki hâliyle aynı olmayabilir.",
    "Envanteri TAB ile aç. Savaş ortasında hangi slotta ne olduğunu aramak yerine, tehlikeli bölgeye girmeden önce 1-5 ve Q düzenini hazırla.",
    "Savunma, dash ve büyü aynı savaş ekonomisinin parçalarıdır. Bir kaynağı tamamen tüketen kombinasyon, sonraki saldırıya karşı seni savunmasız bırakabilir.",
    "Düşman yere serilmeden önce saldırı animasyonunu bitirmek zorunda değildir. HP kadar beden hareketini de takip et; tehdidin bittiğinden emin ol.",
]
# </POTBO_STAGE S2435>

# <POTBO_STAGE S2438>

V99_PRECIOSA_HINTS_TR = [
    "Preciosa'nın gücü yalnız hız değildir; kısa saldırı, açı değişimi ve yeniden giriş ritmidir. Aynı çizgide uzun süre kalma.",
    "Preciosa'nın mana ekonomisi daha rahattır; bunu büyü spam'i için değil, kısa bir konum değişiminden sonra yeniden büyü tehdidi kurmak için kullan.",
    "Preciosa ile rakibin önünde kalmak yerine hafif çapraz açı ara. Yan çizgi hem kaçışı kolaylaştırır hem de temiz temas ihtimalini artırır.",
    "Savunmayı darbeden hemen önce açmak, uygun açıda parry fırsatı yaratabilir. Tehdide dönük değilsen iyi zamanlama tek başına yetmez.",
    "Başarılı parry sonrasında karşı saldırı penceresi kısadır. Uzun kombinasyon yerine güvenli ve temiz bir riposte tercih et.",
    "Preciosa ile her vuruştan sonra küçük bir yön değişikliği yap. Hızını yalnız kaçmak için değil, ikinci açıklığı üretmek için kullan.",
    "Mana avantajın olsa bile kaçış için stamina bırak. Büyü kullandıktan sonra aynı çizgide kalmak, hızlı karakterin en büyük avantajını boşa çıkarır.",
    "Kalabalıkta Sphaera'nın dış halkası çoğu zaman yeterlidir. Merkezi zorlamak yerine alan açıp yeni bir saldırı açısı kurabilirsin.",
]

V99_PRECIOSA_HINTS_EN = [
    "Preciosa's strength is not speed alone; it is the rhythm of short attacks, angle changes and re-entry. Do not remain on one line for long.",
    "Preciosa has a more forgiving mana economy. Use it to rebuild spell pressure after a short reposition, not to spam every spell immediately.",
    "With Preciosa, look for a shallow diagonal angle instead of remaining directly in front of the target. Side lines improve both escape and clean contact.",
    "Guarding just before impact can create a parry opportunity at the correct angle. Good timing is not enough if you are facing away from the threat.",
    "The counter window after a successful parry is short. Prefer one clean riposte over a long, risky combination.",
    "Make a small direction change after each hit with Preciosa. Use speed to create the second opening, not only to run away.",
    "Even with a mana advantage, preserve stamina for escape. Remaining on the same line after casting wastes the main benefit of a fast character.",
    "In crowds, the outer ring of Sphaera is often enough. Create space first instead of forcing yourself into the blast center.",
]
# </POTBO_STAGE S2438>

# <POTBO_STAGE S2440>

KADIN_IPUCLARI = {
    "TR": V99_COMMON_HINTS_TR + V99_PRECIOSA_HINTS_TR,
    "EN": V99_COMMON_HINTS_EN + V99_PRECIOSA_HINTS_EN,
}
# </POTBO_STAGE S2440>

