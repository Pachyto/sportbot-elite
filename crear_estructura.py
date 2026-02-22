import os

# Define la estructura
folders = [
    "scripts/utils",
    "src/layouts",
    "src/components",
    "src/pages/ligas",
    "src/pages/partidos",
    "src/pages/jugadores",
    "src/content/ligas",
    "src/content/partidos",
    "src/content/jugadores",
    "n8n",
    "public/assets"
]

files = [
    ".env",
    "config.json",
    "README.md",
    "scripts/bot_deportivo_local.py",
    "scripts/requirements.txt",
    "scripts/utils/api_client.py",
    "scripts/utils/odds_comparator.py",
    "scripts/utils/content_writer.py",
    "src/layouts/Layout.astro",
    "src/components/AffiliateWidget.astro",
    "src/components/AmazonProducts.astro",
    "src/components/AdSlot.astro",
    "src/components/OddsComparator.astro",
    "src/components/MatchCard.astro",
    "n8n/sportbot_workflow.json"
]

# Crea las carpetas
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Carpeta creada: {folder}")

# Crea los archivos vacíos
for file in files:
    with open(file, 'w') as f:
        pass
    print(f"Archivo creado: {file}")

print("\n✅ ¡Estructura completa creada con éxito!")