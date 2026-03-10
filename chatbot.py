import random

class TechSupportChatbot:
    def __init__(self):
        self.responses = {
            "hata": ["Hangi hata kodunu alıyorsunuz?", "Lütfen hata mesajının ekran görüntüsünü paylaşın.", "Sistemi yeniden başlatmayı denediniz mi?"],
            "şifre": ["Şifre sıfırlama işlemi için 'Ayarlar' sekmesine gidin.", "Yeni şifreniz en az 8 karakter olmalıdır."],
            "bağlantı": ["İnternet bağlantınızı kontrol edin.", "Proxy ayarlarınızın doğru olduğundan emin olun."],
            "selam": ["Merhaba, size nasıl yardımcı olabilirim?", "Teknik destek merkezine hoş geldiniz!"],
            "çıkış": ["İyi günler dilerim.", "Tekrar görüşmek üzere!"]
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        return "Üzgünüm, bunu tam olarak anlayamadım. Lütfen farklı bir şekilde sorabilir misiniz?"

if __name__ == "__main__":
    bot = TechSupportChatbot()
    print("Sidal AI Chatbot - Teknik Destek (Çıkmak için 'çıkış' yazın)")
    while True:
        user_msg = input("Siz: ")
        if user_msg == "çıkış":
            print("Bot:", bot.get_response("çıkış"))
            break
        print("Bot:", bot.get_response(user_msg))
