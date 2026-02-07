import json
import zipfile

# Define a Windows-themed Scratch 3.0 project JSON with desktop simulation
project = {
    "targets": [
        {
            "isStage": True,
            "name": "Stage",
            "variables": {
                "window_open": ["window_open", False]
            },
            "lists": {},
            "broadcasts": {},
            "blocks": {},
            "comments": {},
            "currentCostume": 0,
            "costumes": [
                {
                    "name": "Windows Desktop",
                    "dataFormat": "svg",
                    "assetId": "cd21514d0531fdffb22204e0ec5ed84a",  # Placeholder, use a solid color or known backdrop
                    "md5ext": "cd21514d0531fdffb22204e0ec5ed84a.svg",
                    "rotationCenterX": 240,
                    "rotationCenterY": 180
                }
            ],
            "sounds": [],
            "volume": 100,
            "layerOrder": 0,
            "tempo": 60,
            "videoTransparency": 50,
            "videoState": "off",
            "textToSpeechLanguage": None
        },
        {
            "isStage": False,
            "name": "Taskbar",
            "variables": {},
            "lists": {},
            "broadcasts": {},
            "blocks": {},
            "comments": {},
            "currentCostume": 0,
            "costumes": [
                {
                    "name": "taskbar",
                    "bitmapResolution": 1,
                    "dataFormat": "svg",
                    "assetId": "bcf454acf82e4504149f7ffe07081dbc",  # Placeholder
                    "md5ext": "bcf454acf82e4504149f7ffe07081dbc.svg",
                    "rotationCenterX": 240,
                    "rotationCenterY": 10
                }
            ],
            "sounds": [],
            "volume": 100,
            "layerOrder": 1,
            "visible": True,
            "x": 0,
            "y": -170,
            "size": 100,
            "direction": 90,
            "draggable": False,
            "rotationStyle": "don't rotate"
        },
        {
            "isStage": False,
            "name": "Start Button",
            "variables": {},
            "lists": {},
            "broadcasts": {},
            "blocks": {
                "when_clicked": {
                    "opcode": "event_whenthisspriteclicked",
                    "next": "show_menu",
                    "parent": None,
                    "inputs": {},
                    "fields": {},
                    "shadow": False,
                    "topLevel": True,
                    "x": 10,
                    "y": 10
                },
                "show_menu": {
                    "opcode": "looks_show",
                    "next": None,
                    "parent": "when_clicked",
                    "inputs": {},
                    "fields": {},
                    "shadow": False,
                    "topLevel": False
                }
            },
            "comments": {},
            "currentCostume": 0,
            "costumes": [
                {
                    "name": "start",
                    "bitmapResolution": 1,
                    "dataFormat": "svg",
                    "assetId": "b7853f557e4426412e64bb3da6531a99",  # Placeholder
                    "md5ext": "b7853f557e4426412e64bb3da6531a99.svg",
                    "rotationCenterX": 20,
                    "rotationCenterY": 20
                }
            ],
            "sounds": [],
            "volume": 100,
            "layerOrder": 2,
            "visible": True,
            "x": -220,
            "y": -170,
            "size": 50,
            "direction": 90,
            "draggable": False,
            "rotationStyle": "don't rotate"
        },
        {
            "isStage": False,
            "name": "My Computer Icon",
            "variables": {},
            "lists": {},
            "broadcasts": {},
            "blocks": {
                "when_clicked": {
                    "opcode": "event_whenthisspriteclicked",
                    "next": "open_window",
                    "parent": None,
                    "inputs": {},
                    "fields": {},
                    "shadow": False,
                    "topLevel": True,
                    "x": 50,
                    "y": 50
                },
                "open_window": {
                    "opcode": "event_broadcast",
                    "next": None,
                    "parent": "when_clicked",
                    "inputs": {
                        "BROADCAST_INPUT": [1, "open_window"]
                    },
                    "fields": {},
                    "shadow": False,
                    "topLevel": False
                }
            },
            "comments": {},
            "currentCostume": 0,
            "costumes": [
                {
                    "name": "computer",
                    "bitmapResolution": 1,
                    "dataFormat": "svg",
                    "assetId": "bcf454acf82e4504149f7ffe07081dbc",  # Placeholder
                    "md5ext": "bcf454acf82e4504149f7ffe07081dbc.svg",
                    "rotationCenterX": 30,
                    "rotationCenterY": 30
                }
            ],
            "sounds": [],
            "volume": 100,
            "layerOrder": 3,
            "visible": True,
            "x": -100,
            "y": 100,
            "size": 60,
            "direction": 90,
            "draggable": False,
            "rotationStyle": "don't rotate"
        },
        {
            "isStage": False,
            "name": "Window",
            "variables": {},
            "lists": {},
            "broadcasts": {},
            "blocks": {
                "when_receive": {
                    "opcode": "event_whenbroadcastreceived",
                    "next": "show_window",
                    "parent": None,
                    "inputs": {},
                    "fields": {
                        "BROADCAST_OPTION": ["open_window", None]
                    },
                    "shadow": False,
                    "topLevel": True,
                    "x": 100,
                    "y": 100
                },
                "show_window": {
                    "opcode": "looks_show",
                    "next": "say_content",
                    "parent": "when_receive",
                    "inputs": {},
                    "fields": {},
                    "shadow": False,
                    "topLevel": False
                },
                "say_content": {
                    "opcode": "looks_say",
                    "next": None,
                    "parent": "show_window",
                    "inputs": {
                        "MESSAGE": [1, "Welcome to My Computer!"]
                    },
                    "fields": {},
                    "shadow": False,
                    "topLevel": False
                }
            },
            "comments": {},
            "currentCostume": 0,
            "costumes": [
                {
                    "name": "window",
                    "bitmapResolution": 1,
                    "dataFormat": "svg",
                    "assetId": "b7853f557e4426412e64bb3da6531a99",  # Placeholder
                    "md5ext": "b7853f557e4426412e64bb3da6531a99.svg",
                    "rotationCenterX": 100,
                    "rotationCenterY": 80
                }
            ],
            "sounds": [],
            "volume": 100,
            "layerOrder": 4,
            "visible": False,
            "x": 0,
            "y": 0,
            "size": 100,
            "direction": 90,
            "draggable": True,
            "rotationStyle": "don't rotate"
        }
    ],
    "monitors": [],
    "extensions": [],
    "meta": {
        "semver": "3.0.0",
        "vm": "0.2.0",
        "agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
}

# Create the SB3 file (ZIP archive)
with zipfile.ZipFile('projeto_scratch.sb3', 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.writestr('project.json', json.dumps(project, indent=2))

print("Arquivo SB3 gerado com sucesso: projeto_scratch.sb3")
print("Este projeto simula um desktop Windows com barra de tarefas, botão iniciar, ícones e janelas interativas.")
print("Abra o arquivo no Scratch ou em um editor compatível para visualizar o projeto.")
