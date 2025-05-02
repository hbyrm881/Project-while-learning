# Basit bir chatbot başlangıcı

def chatbot_response(soru):
    # Kullanıcının sorusuna göre yanıtlar
    if "nasılsın" in soru.lower():
        return "Ben bir yapay zeka modeliyim, ama gayet iyi sayılırım!"
    elif "saat kaç" in soru.lower():
        from datetime import datetime
        now = datetime.now()
        return f"Şu anda saat: {now.hour}:{now.minute}"
    elif "teşekkür ederim" in soru.lower():
        return "Rica ederim! Yardımcı olabildiysem ne mutlu."
    else:
        return "Bu konuda emin değilim, başka bir şey sormak ister misin?"

# Kullanıcı ile etkileşim
while True:
    user_input = input("Bir şey sor: ")
    if user_input.lower() in ["çık", "bye", "görüşürüz"]:
        print("Görüşmek üzere!")
        break
    response = chatbot_response(user_input)
    print(response)