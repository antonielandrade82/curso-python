import sys
import platform
from datetime import datetime

print("🚀 Python funcionando!")

print("\n📌 Informações do ambiente:")
print(f"Versão do Python: {sys.version.split()[0]}")
print(f"Executável: {sys.executable}")
print(f"Sistema: {platform.system()} {platform.release()}")

print("\n⏰ Data e hora atual:")
print(datetime.now())

nome = input("\n👤 Qual seu nome? ")
print(f"\n✅ Olá, {nome}! Ambiente Python OK 🎉")
