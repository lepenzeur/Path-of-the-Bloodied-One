# Asset provenance / release gate

All art, audio, fonts and other packaged media in the current development build are treated as **temporary development assets**. Agraphon Studios has explicitly designated them for replacement before any public/commercial release.

The supplied `assets/characters/preciosa_spriteSheet.png` is used only for Preciosa's in-game gameplay animation pipeline. It does **not** replace her existing character illustrations. The original `assets/portraits/preciosa.png` and `assets/portraits/preciosa_card.jpeg` remain the presentation artwork used by the game, including the character-card and loading presentation paths.

`ASSET_PROVENANCE.csv` inventories every packaged asset with a SHA-256 digest. Every current asset is marked `TEMP_DEV_ONLY`; production art must be original or properly licensed before release.
