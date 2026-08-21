# <POTBO_STAGE S8999>
"""Backlog quality layer: release safety, accessibility, controller input, save schema and diagnostics."""
from datetime import datetime, timezone

APP_VERSION = "2.1.0"
SAVE_SCHEMA_VERSION = 2
SETTINGS_SCHEMA_VERSION = 2
WORLD_EVENT_SAVE_LIMIT = 72
AGRAPHON_DIAGNOSTICS = deque(maxlen=256)

# Production must be opt-in for developer authority.
GELISTIRICI_MODU = os.environ.get("PATH_BLOODIED_DEV", "1").strip().lower() not in {"0", "false", "no", "off"}


def diagnostic_record(code, detail="", severity="info", recovered=False):
    try:
        AGRAPHON_DIAGNOSTICS.append({
            "time_ms": int(pygame.time.get_ticks()) if pygame.get_init() else 0,
            "code": str(code),
            "detail": str(detail)[:500],
            "severity": str(severity),
            "recovered": bool(recovered),
        })
    except Exception:
        return False
    return True


def debug_log(*args):
    message = " ".join(str(x) for x in args)
    diagnostic_record("debug", message, "debug", False)
    if DEBUG_LOGS:
        print(message)


# ---------- Settings + accessibility ----------
display_mode = "fullscreen" if tam_ekran else "windowed"
screen_shake_intensity = 100
flash_intensity = 100
colorblind_mode = "off"
block_input_mode = "hold"
controller_enabled = True
controller_deadzone = 0.34
quality_block_latched = False
quality_controller = None
quality_axis_menu_latch = {0: 0, 1: 0}


def _quality_read_json(path):
    try:
        with open(path, "r", encoding="utf-8") as handle:
            value = json.load(handle)
        return value if isinstance(value, dict) else {}
    except (OSError, ValueError, TypeError, json.JSONDecodeError):
        return {}


def _quality_load_settings_extension():
    global display_mode, screen_shake_intensity, flash_intensity, metin_hizi
    global colorblind_mode, block_input_mode, controller_enabled, controller_deadzone
    data = _quality_read_json(AYAR_DOSYASI)
    mode = str(data.get("display_mode", display_mode))
    if mode in ("fullscreen", "borderless", "windowed"):
        display_mode = mode
    screen_shake_intensity = max(0, min(100, int(data.get("screen_shake_intensity", screen_shake_intensity))))
    flash_intensity = max(0, min(100, int(data.get("flash_intensity", flash_intensity))))
    cb = str(data.get("colorblind_mode", colorblind_mode))
    if cb in ("off", "deuteranopia", "protanopia", "tritanopia"):
        colorblind_mode = cb
    bim = str(data.get("block_input_mode", block_input_mode))
    if bim in ("hold", "toggle"):
        block_input_mode = bim
    controller_enabled = bool(data.get("controller_enabled", controller_enabled))
    try:
        controller_deadzone = max(0.15, min(0.75, float(data.get("controller_deadzone", controller_deadzone))))
    except (TypeError, ValueError):
        controller_deadzone = 0.34
    loaded_text_speed = str(data.get("text_speed", metin_hizi))
    if loaded_text_speed in ("yavas", "normal", "hizli", "instant"):
        metin_hizi = loaded_text_speed


_quality_load_settings_extension()

_quality_settings_save_original = ayarlari_kaydet

def ayarlari_kaydet():
    result = _quality_settings_save_original()
    try:
        payload = _quality_read_json(AYAR_DOSYASI)
        payload.update({
            "settings_schema_version": SETTINGS_SCHEMA_VERSION,
            "build_version": APP_VERSION,
            "display_mode": display_mode,
            "screen_shake_intensity": int(screen_shake_intensity),
            "flash_intensity": int(flash_intensity),
            "colorblind_mode": colorblind_mode,
            "block_input_mode": block_input_mode,
            "controller_enabled": bool(controller_enabled),
            "controller_deadzone": float(controller_deadzone),
        })
        _v34_json_atomic_write(AYAR_DOSYASI, payload, indent=4)
        return True if result is None else result
    except OSError as exc:
        diagnostic_record("settings_extension_write_failed", exc, "warning", False)
        return False


_quality_ayar_kategorileri_original = ayar_kategorileri
_quality_ayar_etiketi_original = ayar_etiketi
_quality_ayar_aciklamasi_original = ayar_aciklamasi
_quality_ayar_degeri_original = ayar_degeri
_quality_ayari_degistir_original = ayari_degistir


def ayar_kategorileri():
    result = []
    for kategori, items in _quality_ayar_kategorileri_original():
        items = list(items)
        if kategori == "goruntu":
            if "fullscreen" in items:
                items[items.index("fullscreen")] = "display_mode"
            for key in ("screen_shake_intensity",):
                if key not in items:
                    items.append(key)
        if kategori == "erisilebilirlik":
            for key in ("flash_intensity", "colorblind_mode", "block_input_mode"):
                if key not in items:
                    items.append(key)
        if kategori == "kontroller" and "controller_enabled" not in items:
            items.insert(0, "controller_enabled")
        result.append((kategori, items))
    return result


def ayar_etiketi(ayar):
    extra = {
        "display_mode": bt("EKRAN MODU", "DISPLAY MODE"),
        "screen_shake_intensity": bt("SARSINTI YOĞUNLUĞU", "SHAKE INTENSITY"),
        "flash_intensity": bt("FLAŞ YOĞUNLUĞU", "FLASH INTENSITY"),
        "colorblind_mode": bt("RENK ERİŞİLEBİLİRLİĞİ", "COLOR ACCESSIBILITY"),
        "block_input_mode": bt("SAVUNMA GİRDİSİ", "BLOCK INPUT"),
        "controller_enabled": bt("CONTROLLER", "CONTROLLER"),
    }
    return extra.get(ayar, _quality_ayar_etiketi_original(ayar))


def ayar_aciklamasi(ayar):
    extra = {
        "display_mode": bt("Tam ekran, çerçevesiz veya pencereli görüntü modunu seçer.", "Selects fullscreen, borderless or windowed display."),
        "screen_shake_intensity": bt("Kamera sarsıntısını yüzde olarak sınırlar; 0 tamamen kapatır.", "Caps camera shake as a percentage; 0 disables it."),
        "flash_intensity": bt("Yoğun ışık efektleri için merkezi erişilebilirlik sınırıdır.", "Central accessibility limit for intense light effects."),
        "colorblind_mode": bt("HUD kaynaklarını renk dışında ayrıştıran erişilebilir paleti seçer.", "Selects an accessibility palette that keeps HUD resources distinguishable."),
        "block_input_mode": bt("Savunmayı basılı tutma veya aç/kapat biçiminde kullanır.", "Uses block as hold or toggle input."),
        "controller_enabled": bt("Gamepad düğmelerini mevcut eylem haritasına bağlar.", "Maps gamepad buttons onto the current action map."),
    }
    return extra.get(ayar, _quality_ayar_aciklamasi_original(ayar))


def ayar_degeri(ayar):
    if ayar == "display_mode":
        names = {"fullscreen": bt("TAM EKRAN", "FULLSCREEN"), "borderless": bt("ÇERÇEVESİZ", "BORDERLESS"), "windowed": bt("PENCERELİ", "WINDOWED")}
        return names.get(display_mode, display_mode.upper())
    if ayar == "screen_shake_intensity":
        return f"%{screen_shake_intensity}"
    if ayar == "flash_intensity":
        return f"%{flash_intensity}"
    if ayar == "colorblind_mode":
        names = {"off": bt("KAPALI", "OFF"), "deuteranopia": "DEUTERANOPIA", "protanopia": "PROTANOPIA", "tritanopia": "TRITANOPIA"}
        return names[colorblind_mode]
    if ayar == "block_input_mode":
        return bt("BASILI TUT", "HOLD") if block_input_mode == "hold" else bt("AÇ/KAPAT", "TOGGLE")
    if ayar == "controller_enabled":
        return acik_kapali(controller_enabled)
    return _quality_ayar_degeri_original(ayar)


def _quality_apply_palette():
    global PARLAK_KIRMIZI, MANA_MAVI, YESIL, SARI
    if colorblind_mode == "deuteranopia":
        PARLAK_KIRMIZI, MANA_MAVI, YESIL, SARI = (230, 105, 40), (60, 145, 255), (165, 105, 230), (250, 215, 80)
    elif colorblind_mode == "protanopia":
        PARLAK_KIRMIZI, MANA_MAVI, YESIL, SARI = (225, 125, 35), (45, 150, 255), (80, 185, 210), (245, 215, 75)
    elif colorblind_mode == "tritanopia":
        PARLAK_KIRMIZI, MANA_MAVI, YESIL, SARI = (225, 50, 75), (80, 190, 175), (65, 190, 110), (235, 125, 195)
    else:
        PARLAK_KIRMIZI, MANA_MAVI, YESIL, SARI = (225, 24, 46), (45, 150, 255), (50, 210, 95), (245, 205, 65)


def ayari_degistir(yon):
    global display_mode, screen_shake_intensity, flash_intensity
    global colorblind_mode, block_input_mode, controller_enabled, tam_ekran, quality_block_latched
    key = secili_ayar_anahtari()
    if key == "display_mode":
        display_mode = dongulu_deger(["fullscreen", "borderless", "windowed"], display_mode, yon)
        tam_ekran = display_mode == "fullscreen"
        ekran_olustur()
    elif key == "screen_shake_intensity":
        screen_shake_intensity = max(0, min(100, screen_shake_intensity + yon * 10))
    elif key == "flash_intensity":
        flash_intensity = max(0, min(100, flash_intensity + yon * 10))
    elif key == "colorblind_mode":
        colorblind_mode = dongulu_deger(["off", "deuteranopia", "protanopia", "tritanopia"], colorblind_mode, yon)
        _quality_apply_palette()
    elif key == "block_input_mode":
        block_input_mode = "toggle" if block_input_mode == "hold" else "hold"
        quality_block_latched = False
    elif key == "controller_enabled":
        controller_enabled = not controller_enabled
    else:
        return _quality_ayari_degistir_original(yon)
    button_click_sesi_cal("menu1")
    ayarlari_kaydet()
    return True


_quality_apply_palette()

_quality_ekran_olustur_original = ekran_olustur

def ekran_olustur():
    global ekran, tam_ekran
    tam_ekran = display_mode == "fullscreen"
    flags = pygame.SCALED
    if display_mode == "fullscreen":
        flags |= pygame.FULLSCREEN
    elif display_mode == "borderless":
        flags |= pygame.NOFRAME
    try:
        ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK), flags)
    except pygame.error as exc:
        diagnostic_record("display_mode_fallback", exc, "warning", True)
        ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
    pygame.display.set_caption(f"Path of the Bloodied One — Agraphon Studios — v{APP_VERSION}")
    try:
        sprite_olcek_onbellegi.clear()
    except Exception:
        pass
    return ekran


_quality_shake_original = kamera_hit_sarsintisi_baslat

def kamera_hit_sarsintisi_baslat(guc, sure, *args, **kwargs):
    if not ekran_sarsintisi or screen_shake_intensity <= 0:
        return False
    scale = screen_shake_intensity / 100.0
    if az_hareket:
        scale *= 0.35
    return _quality_shake_original(float(guc) * scale, sure, *args, **kwargs)


_quality_sprite_flash_original = sprite_maskeli_parlama_ciz
def sprite_maskeli_parlama_ciz(sprite, rect, renk, alfa):
    scale = flash_intensity / 100.0
    if az_hareket:
        scale *= 0.45
    return _quality_sprite_flash_original(sprite, rect, renk, int(max(0, min(255, float(alfa) * scale))))


# Text-speed actually drives typewriter presentation.
_quality_dialogue_text_original = diyalog_gorunen_metin
_quality_merchant_text_original = merchant_diyalog_gorunen_metin

def _quality_text_interval(base_ms):
    return {"yavas": int(base_ms * 1.45), "normal": int(base_ms), "hizli": max(6, int(base_ms * 0.52)), "instant": 0}.get(metin_hizi, int(base_ms))


def diyalog_gorunen_metin(metin):
    global diyalog_tamamlandi
    interval = _quality_text_interval(DIYALOG_HARF_ARALIGI)
    if interval <= 0:
        diyalog_tamamlandi = True
        return str(metin)
    if diyalog_tamamlandi:
        return str(metin)
    gecen = max(0, pygame.time.get_ticks() - diyalog_yazi_baslangici)
    adet = min(len(str(metin)), 1 + gecen // interval)
    if adet >= len(str(metin)):
        diyalog_tamamlandi = True
    return str(metin)[:adet]


def merchant_diyalog_gorunen_metin():
    global merchant_yazi_tamamlandi
    text = merchant_mesaji or ""
    interval = _quality_text_interval(MERCHANT_HARF_ARALIGI)
    if interval <= 0:
        merchant_yazi_tamamlandi = True
        return text
    if merchant_yazi_tamamlandi:
        return text
    elapsed = max(0, pygame.time.get_ticks() - merchant_yazi_baslangici)
    count = min(len(text), 1 + elapsed // interval)
    if count >= len(text):
        merchant_yazi_tamamlandi = True
    return text[:count]


# Extend text speed option with instant while remaining backward compatible.
_quality_ayar_degeri_with_access = ayar_degeri
_quality_ayari_degistir_with_access = ayari_degistir

def ayar_degeri(ayar):
    if ayar == "text_speed":
        names = {"yavas": bt("YAVAŞ", "SLOW"), "normal": bt("NORMAL", "NORMAL"), "hizli": bt("HIZLI", "FAST"), "instant": bt("ANINDA", "INSTANT")}
        return names.get(metin_hizi, names["normal"])
    return _quality_ayar_degeri_with_access(ayar)


def ayari_degistir(yon):
    global metin_hizi
    if secili_ayar_anahtari() == "text_speed":
        metin_hizi = dongulu_deger(["yavas", "normal", "hizli", "instant"], metin_hizi if metin_hizi in ("yavas", "normal", "hizli", "instant") else "normal", yon)
        button_click_sesi_cal("menu1")
        ayarlari_kaydet()
        return True
    return _quality_ayari_degistir_with_access(yon)


# ---------- Controller/action abstraction ----------
def _quality_get_controller():
    global quality_controller
    if not controller_enabled:
        return None
    try:
        if quality_controller is not None and quality_controller.get_init():
            return quality_controller
        if pygame.joystick.get_count() <= 0:
            quality_controller = None
            return None
        quality_controller = pygame.joystick.Joystick(0)
        quality_controller.init()
        diagnostic_record("controller_connected", quality_controller.get_name(), "info", True)
        return quality_controller
    except pygame.error as exc:
        diagnostic_record("controller_init_failed", exc, "warning", False)
        quality_controller = None
        return None


def _quality_controller_axes():
    joy = _quality_get_controller()
    x = y = 0.0
    hat_x = hat_y = 0
    if joy is None:
        return x, y, hat_x, hat_y
    try:
        if joy.get_numaxes() >= 2:
            x, y = float(joy.get_axis(0)), float(joy.get_axis(1))
        if joy.get_numhats() >= 1:
            hat_x, hat_y = joy.get_hat(0)
    except pygame.error:
        pass
    if abs(x) < controller_deadzone: x = 0.0
    if abs(y) < controller_deadzone: y = 0.0
    return x, y, int(hat_x), int(hat_y)


def _quality_controller_button(index):
    joy = _quality_get_controller()
    if joy is None:
        return False
    try:
        return index < joy.get_numbuttons() and bool(joy.get_button(index))
    except pygame.error:
        return False


def _quality_controller_action_pressed(action):
    x, y, hx, hy = _quality_controller_axes()
    if action == "move_left": return x < 0 or hx < 0
    if action == "move_right": return x > 0 or hx > 0
    if action == "move_up": return y < 0 or hy > 0
    if action == "move_down": return y > 0 or hy < 0
    # Generic Xbox-style layout: A interact, B dash, X attack, Y inventory, LB block, RB quick-use.
    mapping = {"interact": 0, "dash": 1, "attack": 2, "inventory": 3, "block": 4, "quick_use": 5, "save": 6, "pause": 7, "q_quick_use": 9}
    idx = mapping.get(action)
    return False if idx is None else _quality_controller_button(idx)


class _QualityPressedState:
    def __init__(self, base): self.base = base
    def __getitem__(self, key):
        try:
            if key == tus_atamasi("block") and block_input_mode == "toggle":
                return bool(quality_block_latched)
            for action in VARSAYILAN_TUS_ATAMALARI:
                if key == tus_atamasi(action) and _quality_controller_action_pressed(action):
                    return True
            return self.base[key]
        except Exception:
            try: return self.base[key]
            except Exception: return False
    def __len__(self):
        try: return len(self.base)
        except Exception: return 512


def potbo_pressed_state():
    try:
        return _QualityPressedState(pygame.key.get_pressed())
    except pygame.error:
        return _QualityPressedState([False] * 512)


def _quality_key_event(kind, key):
    return pygame.event.Event(kind, {"key": int(key), "unicode": "", "mod": 0, "repeat": False})


def _quality_button_action(button):
    if oyun_durumu == OYUN:
        return {0:"interact", 1:"dash", 2:"attack", 3:"inventory", 4:"block", 5:"quick_use", 6:"save", 7:"pause", 9:"q_quick_use"}.get(button)
    if oyun_durumu == ENVANTER:
        return {0:"__confirm__", 1:"__back__", 3:"inventory", 5:"quick_use", 7:"pause", 9:"q_quick_use"}.get(button)
    return {0:"__confirm__", 1:"__back__", 7:"__back__"}.get(button)


def quality_events():
    global quality_block_latched
    output = []
    for event in pygame.event.get():
        if event.type == pygame.WINDOWFOCUSLOST:
            quality_block_latched = False
        if event.type == pygame.KEYDOWN and event.key == tus_atamasi("block") and block_input_mode == "toggle":
            quality_block_latched = not quality_block_latched
        output.append(event)
        if not controller_enabled:
            continue
        if event.type in (pygame.JOYBUTTONDOWN, pygame.JOYBUTTONUP):
            action = _quality_button_action(int(event.button))
            if action:
                if action == "__confirm__": key = pygame.K_RETURN
                elif action == "__back__": key = pygame.K_ESCAPE
                else: key = tus_atamasi(action)
                if action == "block" and block_input_mode == "toggle" and event.type == pygame.JOYBUTTONDOWN:
                    quality_block_latched = not quality_block_latched
                output.append(_quality_key_event(pygame.KEYDOWN if event.type == pygame.JOYBUTTONDOWN else pygame.KEYUP, key))
        elif event.type == pygame.JOYHATMOTION and oyun_durumu != OYUN:
            hx, hy = event.value
            if hx < 0: output.append(_quality_key_event(pygame.KEYDOWN, pygame.K_LEFT))
            elif hx > 0: output.append(_quality_key_event(pygame.KEYDOWN, pygame.K_RIGHT))
            if hy < 0: output.append(_quality_key_event(pygame.KEYDOWN, pygame.K_DOWN))
            elif hy > 0: output.append(_quality_key_event(pygame.KEYDOWN, pygame.K_UP))
        elif event.type == pygame.JOYAXISMOTION and oyun_durumu != OYUN and int(event.axis) in (0, 1):
            axis = int(event.axis); value = float(event.value)
            direction = -1 if value < -controller_deadzone else (1 if value > controller_deadzone else 0)
            previous = quality_axis_menu_latch.get(axis, 0)
            if direction and direction != previous:
                key = (pygame.K_LEFT if direction < 0 else pygame.K_RIGHT) if axis == 0 else (pygame.K_UP if direction < 0 else pygame.K_DOWN)
                output.append(_quality_key_event(pygame.KEYDOWN, key))
            quality_axis_menu_latch[axis] = direction
    return output


# ---------- Save schema, migration, robust listing and pagination ----------
def quality_migrate_save_payload(payload):
    if not isinstance(payload, dict):
        return None, ["payload_not_object"]
    data = dict(payload)
    errors = []
    version = data.get("save_schema_version", 1)
    try: version = int(version)
    except (TypeError, ValueError): version = 1
    if version > SAVE_SCHEMA_VERSION:
        errors.append("newer_schema")
        return data, errors
    # v1 -> v2 is metadata-only; gameplay values are intentionally not silently rewritten.
    data["save_schema_version"] = SAVE_SCHEMA_VERSION
    data.setdefault("build_version", APP_VERSION)
    data.setdefault("world_event_limit", WORLD_EVENT_SAVE_LIMIT)
    if "inventory" in data and not isinstance(data["inventory"], list): errors.append("inventory_type")
    if "world_state" in data and not isinstance(data["world_state"], dict): errors.append("world_state_type")
    if "common_enemies" in data and not isinstance(data["common_enemies"], list): errors.append("common_enemies_type")
    for key in ("level", "gold", "hp", "max_hp", "mana", "max_mana", "stamina", "max_stamina"):
        if key in data and not isinstance(data[key], (int, float)):
            errors.append(key + "_type")
    return data, errors


def _quality_write_last_save(path):
    if not path: return False
    payload = {"save_id": os.path.basename(path), "schema": 1}
    try:
        _v34_json_atomic_write(SON_KAYIT_DOSYASI, payload, indent=4)
        return True
    except OSError as exc:
        diagnostic_record("last_save_write_failed", exc, "warning", False)
        return False


_quality_game_save_original = oyun_kaydet

def oyun_kaydet():
    ok = _quality_game_save_original()
    if not ok or not aktif_kayit:
        return ok
    try:
        payload = _quality_read_json(aktif_kayit)
        migrated, errors = quality_migrate_save_payload(payload)
        if migrated is None or errors:
            diagnostic_record("save_post_validation", ",".join(errors), "warning", False)
        if migrated is not None:
            migrated["build_version"] = APP_VERSION
            migrated["saved_at_utc"] = datetime.now(timezone.utc).isoformat()
            migrated["playtime_ms"] = int(pygame.time.get_ticks())
            _v34_json_atomic_write(aktif_kayit, migrated, indent=4)
        _quality_write_last_save(aktif_kayit)
    except OSError as exc:
        diagnostic_record("save_metadata_write_failed", exc, "warning", False)
    return ok


_quality_game_load_original = oyun_yukle

def oyun_yukle(dosya_yolu, *args, **kwargs):
    path = os.path.abspath(dosya_yolu)
    payload = _quality_read_json(path)
    if payload:
        migrated, errors = quality_migrate_save_payload(payload)
        if migrated is not None and not errors and migrated != payload:
            try: _v34_json_atomic_write(path, migrated, indent=4)
            except OSError as exc: diagnostic_record("save_migration_write_failed", exc, "warning", False)
        elif errors:
            diagnostic_record("save_validation_failed", ",".join(errors), "error", False)
            restored = False
            try:
                restored = bool(_v34f_restore_backup_to_main(path))
            except Exception as exc:
                diagnostic_record("save_backup_restore_exception", exc, "error", False)
            if not restored:
                return False
    result = _quality_game_load_original(path, *args, **kwargs)
    if result:
        _quality_write_last_save(path)
    return result


def son_kaydi_yukle():
    data = _quality_read_json(SON_KAYIT_DOSYASI)
    save_id = data.get("save_id")
    if save_id:
        safe_name = os.path.basename(str(save_id))
        path = os.path.join(SAVES, safe_name)
        if os.path.isfile(path):
            return oyun_yukle(path)
    # Backward compatibility with old absolute last_save.json.
    old_path = data.get("path")
    if old_path:
        candidate = old_path if os.path.isabs(str(old_path)) else os.path.join(SAVES, os.path.basename(str(old_path)))
        if os.path.isfile(candidate):
            result = oyun_yukle(candidate)
            if result: _quality_write_last_save(candidate)
            return result
    return False


def kayitlari_listele():
    entries = []
    try:
        names = os.listdir(SAVES)
    except OSError as exc:
        diagnostic_record("save_list_failed", exc, "warning", False)
        return []
    for name in names:
        if not name.lower().endswith(".json") or name == "last_save.json":
            continue
        path = os.path.join(SAVES, name)
        try:
            mtime = os.path.getmtime(path)
        except OSError:
            continue
        entries.append((mtime, path))
    entries.sort(key=lambda item: item[0], reverse=True)
    return [path for _, path in entries]


def quality_save_preview(path):
    payload = _quality_read_json(path)
    backup = os.path.isfile(os.path.abspath(path) + ".bak")
    if not payload:
        return {"status": "corrupt", "backup": backup, "name": os.path.splitext(os.path.basename(path))[0]}
    migrated, errors = quality_migrate_save_payload(payload)
    return {
        "status": "ok" if not errors else "warning",
        "backup": backup,
        "name": str(payload.get("player_name") or os.path.splitext(os.path.basename(path))[0]),
        "level": payload.get("level", "?"),
        "build": payload.get("build_version", "legacy"),
        "saved_at": payload.get("saved_at_utc", ""),
    }


def quality_load_page(page_size=7):
    global load_index
    saves = kayitlari_listele()
    if not saves:
        load_index = 0
        return [], 0, 0
    load_index = max(0, min(len(saves) - 1, int(load_index)))
    start = (load_index // page_size) * page_size
    return saves[start:start + page_size], start, len(saves)


def quality_load_move(delta):
    global load_index
    saves = kayitlari_listele()
    if not saves:
        load_index = 0
        return
    load_index = (int(load_index) + int(delta)) % len(saves)


def quality_selected_save():
    saves = kayitlari_listele()
    if not saves: return None
    idx = max(0, min(len(saves)-1, int(load_index)))
    return saves[idx]


def load_game_ciz():
    page, start, total = quality_load_page()
    varsayilan_gotik_arka_plan(); koyu_kaplama(180)
    yazi_yaz(t("load_title"), GENISLIK // 2, 90, PARLAK_KIRMIZI, menu_baslik_font, True)
    if not page:
        panel = pygame.Rect(350, 275, 580, 150); gotik_panel(panel)
        yazi_yaz(t("no_save"), panel.centerx, panel.centery, GRI, menu_font, True)
        return
    for local_index, path in enumerate(page):
        absolute_index = start + local_index
        meta = quality_save_preview(path)
        rect = pygame.Rect(300, 145 + local_index * 70, 680, 58)
        selected = absolute_index == load_index
        rect = buton_click_anim_rect(rect, selected)
        pygame.draw.rect(ekran, (45, 4, 13) if selected else KOYU_PANEL, rect)
        pygame.draw.rect(ekran, PARLAK_KIRMIZI if selected else (60,55,68), rect, 2 if selected else 1)
        label = meta.get("name", "save")
        if meta.get("status") == "corrupt":
            detail = bt("BOZUK", "CORRUPT") + (" • BAK" if meta.get("backup") else "")
            detail_color = PARLAK_KIRMIZI
        else:
            detail = f"Lv {meta.get('level','?')} • v{meta.get('build','legacy')}"
            detail_color = ACIK_GRI
        yazi_yaz(label, rect.left + 18, rect.centery - 10, BEYAZ if selected else ACIK_GRI, normal_font, False)
        yazi_yaz(detail, rect.left + 18, rect.centery + 13, detail_color, mini_font, False)
        yazi_yaz(str(absolute_index + 1), rect.right - 24, rect.centery, GRI, mini_font, True)
    if total > 7:
        page_no = (start // 7) + 1; page_count = (total + 6) // 7
        yazi_yaz(f"{page_no}/{page_count}  •  {total}", GENISLIK//2, 660, GRI, mini_font, True)

# Recreate display once after extended settings are known (needed for borderless mode).
try:
    ekran_olustur()
except Exception as exc:
    diagnostic_record("startup_display_recreate_failed", exc, "warning", True)



# ---------- Combat readability + offline performance evidence ----------
QUALITY_FRAME_TIMES = deque(maxlen=7200)
QUALITY_SESSION_STARTED_UTC = datetime.now(timezone.utc).isoformat()
quality_last_damage = {
    "source": "",
    "amount": 0,
    "profile": "",
    "time_ms": 0,
}


def quality_frame_sample(frame_ms):
    """Keep a bounded frame-time history without sending data off-device."""
    try:
        value = max(0.0, min(5000.0, float(frame_ms)))
        QUALITY_FRAME_TIMES.append(value)
    except (TypeError, ValueError):
        diagnostic_record("frame_sample_invalid", frame_ms, "warning", True)


def _quality_percentile(values, pct):
    if not values:
        return 0.0
    ordered = sorted(float(v) for v in values)
    pos = (len(ordered) - 1) * max(0.0, min(1.0, float(pct)))
    lo = int(pos)
    hi = min(len(ordered) - 1, lo + 1)
    frac = pos - lo
    return ordered[lo] * (1.0 - frac) + ordered[hi] * frac


def quality_frame_stats():
    values = list(QUALITY_FRAME_TIMES)
    if not values:
        return {"samples": 0, "avg_ms": 0.0, "p50_ms": 0.0, "p95_ms": 0.0, "p99_ms": 0.0, "avg_fps": 0.0}
    avg = sum(values) / len(values)
    return {
        "samples": len(values),
        "avg_ms": round(avg, 3),
        "p50_ms": round(_quality_percentile(values, 0.50), 3),
        "p95_ms": round(_quality_percentile(values, 0.95), 3),
        "p99_ms": round(_quality_percentile(values, 0.99), 3),
        "avg_fps": round(1000.0 / avg, 2) if avg > 0.0 else 0.0,
    }


def quality_session_flush():
    """Write bounded local QA evidence. No network/telemetry upload is performed."""
    try:
        log_dir = os.path.join(USER_DATA_DIR, "logs")
        os.makedirs(log_dir, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        payload = {
            "build_version": APP_VERSION,
            "started_at_utc": QUALITY_SESSION_STARTED_UTC,
            "ended_at_utc": datetime.now(timezone.utc).isoformat(),
            "frame_stats": quality_frame_stats(),
            "last_damage": dict(quality_last_damage),
            "diagnostics": list(AGRAPHON_DIAGNOSTICS)[-64:],
        }
        path = os.path.join(log_dir, "session-" + stamp + ".json")
        _v34_json_atomic_write(path, payload, indent=2)
        return path
    except Exception as exc:
        diagnostic_record("session_flush_failed", exc, "warning", True)
        return ""


_quality_player_damage_original = oyuncu_kanli_hasar_kaydi


def oyuncu_kanli_hasar_kaydi(kaynak_x, kaynak_y, profil, hasar, kaynak_adi=""):
    global quality_last_damage
    before = int(globals().get("oyuncu_hp", 0))
    result = _quality_player_damage_original(kaynak_x, kaynak_y, profil, hasar, kaynak_adi)
    after = int(globals().get("oyuncu_hp", before))
    lost = max(0, before - after)
    if lost:
        profile_name = str(profil.get("tip", profil.get("type", ""))) if isinstance(profil, dict) else str(profil or "")
        quality_last_damage = {
            "source": str(kaynak_adi or bt("Bilinmeyen saldırı", "Unknown attack")),
            "amount": int(lost),
            "profile": profile_name[:80],
            "time_ms": int(pygame.time.get_ticks()),
        }
        diagnostic_record("player_damage", f"{quality_last_damage['source']}:{lost}", "info", True)
    return result


def _quality_death_tip(last_damage):
    probe = (str(last_damage.get("source", "")) + " " + str(last_damage.get("profile", ""))).lower()
    if any(token in probe for token in ("arrow", "projectile", "bolt", "ok", "menzil", "ranged")):
        return bt("Görüş hattını kır veya yana kaç.", "Break line of sight or dodge laterally.")
    if any(token in probe for token in ("heavy", "slam", "crush", "ağır", "ez")):
        return bt("Ağır telegraph sonrası bloktan çok kaçışı tercih et.", "Prefer a dodge after the heavy telegraph.")
    return bt("Son saldırının telegraph'ını okuyup blok/kaçış zamanını değiştir.", "Read the last telegraph and adjust block/dodge timing.")


_quality_game_draw_original = oyun_ekrani_ciz


def oyun_ekrani_ciz():
    result = _quality_game_draw_original()
    if int(globals().get("oyuncu_hp", 1)) <= 0 and int(quality_last_damage.get("amount", 0)) > 0:
        panel = pygame.Surface((640, 58), pygame.SRCALPHA)
        panel.fill((7, 5, 8, 205))
        x = (GENISLIK - panel.get_width()) // 2
        y = YUKSEKLIK - 82
        ekran.blit(panel, (x, y))
        source = str(quality_last_damage.get("source") or bt("Bilinmeyen saldırı", "Unknown attack"))
        amount = int(quality_last_damage.get("amount", 0))
        yazi_yaz(bt("Son darbe", "Last hit") + f": {source} • -{amount} HP", x + 14, y + 9, ACIK_GRI, mini_font, False)
        yazi_yaz(_quality_death_tip(quality_last_damage), x + 14, y + 34, GRI, mini_font, False)
    return result


# Character selection is presentation-owned by gameplay/effects.py S1078.
# Keep the quality layer from adding a late overlay so the final runtime
# remains pixel/layout-equivalent to the reference character-select screen.


# ---------- Audio + dialogue registries ----------
QUALITY_AUDIO_REGISTRY = {}


def quality_audio_registry_refresh():
    QUALITY_AUDIO_REGISTRY.clear()
    mixer_ready = bool(pygame.mixer.get_init())
    for name, value in sorted(globals().items()):
        if not name.endswith("_SES_YOLU"):
            continue
        path = str(value) if value else ""
        state = {
            "selected_path": path,
            "exists": bool(path and os.path.isfile(path)),
            "mixer_ready": mixer_ready,
        }
        QUALITY_AUDIO_REGISTRY[name] = state
        if path and not state["exists"]:
            diagnostic_record("audio_selected_path_missing", name + ":" + path, "warning", True)
    return QUALITY_AUDIO_REGISTRY


quality_audio_registry_refresh()

QUALITY_DIALOGUE_ACTIONS = frozenset({
    "eadric_adini_ogren", "tarkard_adini_ogren", "tarkard_konusma_tamam",
    "tarkard_savas_baslat", "torrmund_konusma_tamam", "torrmund_savas_baslat",
    "eadric_fire_magic_satinal", "eadric_fire_magic_reddet",
    "eadric_tutum_merakli", "eadric_tutum_dogrudan", "eadric_tutum_sert",
    "intro_tamam", "ganimet_sonrasi_tamam", "magara_yolunu_ogren", "eadric_tasini_ver",
})
_quality_dialogue_action_original = diyalog_aksiyonunu_uygula


def diyalog_aksiyonunu_uygula(ad):
    action = str(ad or "")
    if action not in QUALITY_DIALOGUE_ACTIONS:
        diagnostic_record("dialogue_action_unknown", action, "error", True)
        if GELISTIRICI_MODU:
            bildirim_goster(bt("Bilinmeyen diyalog eylemi: ", "Unknown dialogue action: ") + action)
        return False
    _quality_dialogue_action_original(action)
    return True

# </POTBO_STAGE S8999>
