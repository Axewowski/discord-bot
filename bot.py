import os

token = os.environ.get("DISCORD_TOKEN")

if token:
    print("✅ Zmienna środowiskowa 'DISCORD_TOKEN' została odczytana!")
    print("Przykładowy fragment tokena:", token[:10], "...")
else:
    print("❌ Nie udało się odczytać zmiennej środowiskowej 'DISCORD_TOKEN'")
