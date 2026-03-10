import random
import re
import string

class AIChatbot:
    """Niyet analizi ve benzerlik tabanlı akıllı teknik destek botu."""
    def __init__(self):
        # Bilgi tabanı (Knowledge Base)
        self.knowledge_base = {
            "selam": {
                "keywords": ["merhaba", "selam", "hi", "hey"],
                "responses": ["Merhaba! Sidal AI Teknik Destek birimine hoş geldiniz.", "Selam, size nasıl yardımcı olabilirim?"]
            },
            "hata_kodlari": {
                "keywords": ["hata", "error", "404", "500", "problem", "bozuk"],
                "responses": [
                    "Sistemde karşılaştığınız hatanın tam kodunu veya ekran görüntüsünü paylaşabilir misiniz?",
                    "Hata genellikle yapılandırma dosyalarından kaynaklanır. Logları kontrol ettiniz mi?"
                ]
            },
            "sifre_islemleri": {
                "keywords": ["şifre", "parola", "reset", "unuttum", "password"],
                "responses": ["Şifre sıfırlama talebiniz için 'Ayarlar > Güvenlik' sekmesini ziyaret edebilirsiniz."]
            },
            "servis_durumu": {
                "keywords": ["durum", "aktif", "çalışıyor mu", "kapalı", "online"],
                "responses": ["Şu an tüm servislerimiz aktif olarak hizmet vermektedir. Güncel durum: Online."]
            }
        }

    def _preprocess(self, text):
        """Gelen metni temizler."""
        text = text.lower().strip()
        text = "".join([char for char in text if char not in string.punctuation])
        return text

    def get_response(self, user_input):
        cleaned_input = self._preprocess(user_input)
        
        # 1. Anahtar Kelime Eşleştirme (Keyword Matching)
        best_match = None
        max_matches = 0
        
        for category, data in self.knowledge_base.items():
            matches = sum(1 for word in data["keywords"] if word in cleaned_input)
            if matches > max_matches:
                max_matches = matches
                best_match = category
        
        # 2. Yanıt Üretme
        if best_match:
            return random.choice(self.knowledge_base[best_match]["responses"])
        
        # 3. Bilinmeyen Durum
        return "Üzgünüm, bu konudaki bilginiz sistemimde kayıtlı değil. Lütfen 'hata', 'şifre' veya 'durum' gibi anahtar kelimelerle sorunuzu tekrar iletin."

if __name__ == "__main__":
    bot = AIChatbot()
    print("Sidal AI Technical Support Bot v2.0 Aktif.")
    print("(Çıkmak için 'q' veya 'çıkış' yazın)\n")
    
    while True:
        user_msg = input("Sidal User: ")
        if user_msg.lower() in ['q', 'çıkış']:
            print("Bot: İyi günler dilerim!")
            break
            
        response = bot.get_response(user_msg)
        print(f"Bot: {response}\n")
