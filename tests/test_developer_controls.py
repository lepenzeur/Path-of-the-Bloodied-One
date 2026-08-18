from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION = (ROOT / "core" / "production.py").read_text(encoding="utf-8")
RUNTIME = (ROOT / "gameplay" / "runtime.py").read_text(encoding="utf-8")
SPLASH = (ROOT / "ui" / "splash.py").read_text(encoding="utf-8")
BOOTSTRAP = (ROOT / "core" / "bootstrap.py").read_text(encoding="utf-8")


def test_shortcuts_are_enabled_and_explicit():
    assert 'os.environ.get("PATH_BLOODIED_DEV", "1")' in PRODUCTION
    for token in (
        'pygame.K_1: ("fire_magic", fire_magic_olustur, "Sphaera Exothermica")',
        'pygame.K_2: ("draco_calcinans", draco_calcinans_olustur, "Draco Calcinans")',
        'pygame.K_3: ("corona_aetherica", corona_aetherica_olustur, "Corona Aetherica")',
        'pygame.K_4: ("fulmen_caeruleum", fulmen_caeruleum_olustur, "Fulmen Caeruleum")',
        'if olay.key == pygame.K_u:',
        'oyuncu_altin += 1000',
        'if olay.key == pygame.K_i:',
        'target_level = min(MAKSIMUM_LEVEL, old_level + 10)',
        'if olay.key == pygame.K_o:',
    ):
        assert token in PRODUCTION


def test_quote_panel_contract():
    assert 'AGRAPHON_TEST_PANEL_VISIBLE = False' in PRODUCTION
    assert 'pygame.K_QUOTE' in PRODUCTION
    assert 'olay.key == pygame.K_2 and bool(mask & pygame.KMOD_SHIFT)' in PRODUCTION
    assert 'def gelistirici_test_paneli_ciz()' in PRODUCTION
    assert 'TEST KISAYOLLARI' in PRODUCTION


def test_test_spells_are_unlimited_and_zero_cost_authorized():
    assert 'V108_DEV_UNLIMITED_SPELLS.add(str(item_id))' in PRODUCTION
    assert 'fire_magic_son_kullanim = -1000000' in PRODUCTION
    assert 'v90_draco_last_cast_ms = -1000000' in PRODUCTION
    assert 'v106_corona_last_cast_ms = -1000000' in PRODUCTION
    assert 'v110_fulmen_last_cast_ms = -1000000' in PRODUCTION


def test_shortcuts_run_before_generic_key_filter():
    dev_pos = RUNTIME.index('gelistirici_test_girdisi_uygula(olay)')
    filter_pos = RUNTIME.index('not tus_girdisi_kabul(olay)')
    assert dev_pos < filter_pos


def test_splash_runs_only_after_initialization_layer():
    s0496 = SPLASH.split('# <POTBO_STAGE S0496>', 1)[1].split('# </POTBO_STAGE S0496>', 1)[0]
    assert 'splash_ekrani_goster()' not in s0496
    assert PRODUCTION.rfind('splash_ekrani_goster()') > PRODUCTION.rfind('def gelistirici_test_paneli_ciz')
    assert '_agraphon_boot_pump()' in BOOTSTRAP
