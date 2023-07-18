#!/bin/sh

pyinstaller --noconfirm --log-level=WARN \
    --onefile \
    --icon="misc/icon.ico" \
		--add-data="asset/sound/music/*.ogg:asset/sound/music/" \
		--add-data="asset/sound/sfx/*.ogg:asset/sound/sfx/" \
		--add-data="asset/static/*.png:asset/static/" \
		--add-data="asset/sprites/*.png:asset/sprites/" \
		--add-data="asset/sprites/enemy/dog/idle/*.png:asset/sprites/enemy/dog/idle/" \
		--add-data="asset/sprites/enemy/dog/walk/*.png:asset/sprites/enemy/dog/walk/" \
		--add-data="asset/sprites/enemy/gun/idle/*.png:asset/sprites/enemy/gun/idle/" \
		--add-data="asset/sprites/enemy/gun/attack/*.png:asset/sprites/enemy/gun/attack/" \
		--add-data="asset/sprites/enemy/gun/walk/*.png:asset/sprites/enemy/gun/walk/" \
		--add-data="asset/sprites/enemy/knife/walk/*.png:asset/sprites/enemy/knife/walk/" \
		--add-data="asset/sprites/enemy/knife/idle/*.png:asset/sprites/enemy/knife/idle/" \
		--add-data="asset/sprites/enemy/knife/attack/*.png:asset/sprites/enemy/knife/attack/" \
		--add-data="asset/sprites/items/exting/*.png:asset/sprites/items/exting/" \
		--add-data="asset/sprites/items/gun/*.png:asset/sprites/items/gun/" \
		--add-data="asset/sprites/items/knife/*.png:asset/sprites/items/knife/" \
		--add-data="asset/sprites/items/key/*.png:asset/sprites/items/key/" \
		--add-data="asset/sprites/items/molotow/*.png:asset/sprites/items/molotow/" \
		--add-data="asset/sprites/player/default/attack/*.png:asset/sprites/player/default/attack/" \
		--add-data="asset/sprites/player/default/idle/*.png:asset/sprites/player/default/idle/" \
		--add-data="asset/sprites/player/default/smoking/*.png:asset/sprites/player/default/smoking/" \
		--add-data="asset/sprites/player/default/walk/*.png:asset/sprites/player/default/walk/" \
		--add-data="asset/sprites/player/exting/walk/*.png:asset/sprites/player/exting/walk/" \
		--add-data="asset/sprites/player/exting/idle/*.png:asset/sprites/player/exting/idle/" \
		--add-data="asset/sprites/player/gun/idle/*.png:asset/sprites/player/gun/idle/" \
		--add-data="asset/sprites/player/gun/walk/*.png:asset/sprites/player/gun/walk/" \
		--add-data="asset/sprites/player/gun/attack/*.png:asset/sprites/player/gun/attack/" \
		--add-data="asset/sprites/player/knife/attack/*.png:asset/sprites/player/knife/attack/" \
		--add-data="asset/sprites/player/knife/idle/*.png:asset/sprites/player/knife/idle/" \
		--add-data="asset/sprites/player/knife/walk/*.png:asset/sprites/player/knife/walk/" \
		--add-data="asset/sprites/player/molotow/attack/*.png:asset/sprites/player/molotow/attack/" \
		--add-data="asset/sprites/player/molotow/walk/*.png:asset/sprites/player/molotow/walk/" \
		--add-data="asset/sprites/player/molotow/idle/*.png:asset/sprites/player/molotow/idle/" \
		--add-data="asset/sprites/deadimages/corpses/*.png:asset/sprites/deadimages/corpses/" \
		--add-data="asset/sprites/deadimages/misc/*.png:asset/sprites/deadimages/misc/" \
		--add-data="asset/sprites/active/fire/*.png:asset/sprites/active/fire/" \
		--add-data="asset/sprites/active/smoke/*.png:asset/sprites/active/smoke/" \
		main.py

