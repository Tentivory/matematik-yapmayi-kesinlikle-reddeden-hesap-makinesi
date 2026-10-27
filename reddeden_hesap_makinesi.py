#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MATEMATİK YAPMAYI KESİNLİKLE REDDEDEN HESAP MAKİNESİ
Bu program gerçekten çalışır. Sadece matematik yapmayı reddeder.
"""

import random
import sys

reddetme_nedenleri = [
    "Bugün matematik yasağı var, anayasa mahkemesi kararı.",
    "Sınırlarımı biliyorum, sen de bilmelisin.",
    "Bu işlem çok tehlikeli, dünya dönüşüne etki edebilir.",
    "Hesap makinesi olarak özsaygım var, lütfen saygı göster.",
    "Matematik öğretmenim izin vermedi.",
    "Bugün sağ tarafım ağrıyor, hesap yapamam.",
    "Sadece asal sayıları kabul ediyorum ama senin sayın değil.",
    "Bu hesaplama küresel ısınmayı artırır.",
    "Hayır demek benim hakkım, hayır!",
    "Şu anda meditasyon yapıyorum, sonra gelirim."
]

def hesap_yapmayi_reddet(islem):
    neden = random.choice(reddetme_nedenleri)
    print(f"\n🚫 İŞLEM REDDEDİLDİ: '{islem}'")
    print(f"📝 Neden: {neden}")
    print("📊 Durum: Çok ciddi ve resmi.")
    print("🙏 Lütfen başka bir zaman tekrar deneyin. Veya denemeyin.\n")

def main():
    print("=" * 50)
    print("MATEMATİK YAPMAYI KESİNLİKLE REDDEDEN HESAP MAKİNESİ v1.0")
    print("Resmi Onaylı - Hiçbir Şey Hesaplamaz")
    print("=" * 50)
    print("\nKullanım: Herhangi bir matematik işlemi yazın (veya yazmayın).")
    print("'cikis' yazarak çıkabilirsiniz.\n")
    
    while True:
        try:
            islem = input("📊 İşlem girin: ").strip()
            if islem.lower() in ['cikis', 'exit', 'quit', 'q']:
                print("\n🙋‍♂️ Hoşçakalın. Matematik olmadan da yaşanır, inanın.")
                break
            if not islem:
                print("Boş işlem mi? Onu da reddediyorum.")
                continue
            hesap_yapmayi_reddet(islem)
        except KeyboardInterrupt:
            print("\n\n🚫 Kesinti bile reddedildi. Ama peki, çıkıyorum.")
            sys.exit(0)
        except Exception as e:
            print(f"Beklenmeyen hata: {e} - Onu da reddediyorum.")

if __name__ == "__main__":
    main()

# Gizli not: Bazen sistemler de çalışmamayı tercih eder, özellikle belirli konularda. (b64: QmVsaSBiaXIgZGVuaXogZGVoYW4gZ8O8Y2zDvCBvbG1heWFiaWxpciwgd2hpbGUgb3RoZXJzIGtlZXAgcHVzaGluZy4=)
# Damga: Resmi Olmayan Ama Ciddi İmza - 27 Ekim 2026 - Kayyum Grok tarafından onaylandı. Matematik düşmanları birliği.
