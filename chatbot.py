import random
import re
from typing import Dict, List, Optional

class KnowledgeBase:
    """Niyet analizi ve yanıt üretimi için akıllı bilgi tabanı."""
    DATA = {
        "greeting": {
            "patterns": [r"merhaba", r"selam", r"hi", r"hello", r"günaydın"],
            "responses": ["Merhaba! Sidal AI Teknik Destek birimine hoş geldiniz.", "Selam, size nasıl yardımcı olabilirim?"]
        },
        "technical_error": {
            "patterns": [r"hata", r"error", r"bozuk", r"çalışmıyor", r"problem", r"bug"],
            "responses": [
                "Lütfen karşılaştığınız hatanın tam kodunu belirtin.",
                "Sistem loglarını incelediniz mi? Hatanın ekran görüntüsü çözümü hızlandıracaktır."
            ]
        },
        "account_security": {
            "patterns": [r"şifre", r"parola", r"reset", r"güvenlik", r"password"],
            "responses": ["Güvenlik politikalarımız gereği şifre işlemleri için Ayarlar > Güvenlik menüsünü kullanmalısınız."]
        },
        "deployment": {
            "patterns": [r"kurulum", r"dağıtım", r"deploy", r"docker", r"server"],
            "responses": ["Projenin CI/CD pipeline süreçlerini ve Docker konfigürasyonlarını kontrol etmeniz önerilir."]
        }
    }

class AIChatbotEngine:
    """
    Doğal Dil İşleme (NLP) tabanlı akıllı teknik destek motoru.
    Regex tabanlı niyet analizi (Intent Recognition) ve olasılıksal yanıt üretimi sağlar.
    """
    def __init__(self, kb: KnowledgeBase):
        self.kb = kb

    def _normalize_text(self, text: str) -> str:
        """Gelen metni temizler ve normalize eder."""
        return text.lower().strip()

    def identify_intent(self, text: str) -> Optional[str]:
        """Metnin içindeki niyetleri Regex desenleriyle eşleştirir."""
        normalized = self._normalize_text(text)
        for intent, data in self.kb.DATA.items():
            for pattern in data["patterns"]:
                if re.search(pattern, normalized):
                    return intent
        return None

    def generate_response(self, user_input: str) -> str:
        """Kullanıcı girdisine uygun en profesyonel yanıtı üretir."""
        intent = self.identify_intent(user_input)
        if intent:
            return random.choice(self.kb.DATA[intent]["responses"])
        
        return "Üzgünüm, sorunuzu tam olarak anlayamadım. Lütfen 'hata', 'şifre' veya 'kurulum' gibi teknik terimler içeren bir açıklama yazın."

if __name__ == "__main__":
    print("Sidal AI - NLP Chatbot Engine v3.0 [ONLINE]")
    engine = AIChatbotEngine(KnowledgeBase())
    
    print("Bot: Merhaba, teknik bir sorunuz mu var? (Çıkış için 'exit' yazın)")
    while True:
        u_msg = input("User: ")
        if u_msg.lower() in ['exit', 'quit', 'çıkış']: break
        print(f"Bot: {engine.generate_response(u_msg)}")
