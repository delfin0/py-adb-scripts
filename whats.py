from hex import type_phone

message = '           ILUMINATI RS. ODDDDDDDDDEEEEEEEEXXXXXXXXX.'
# Replace spaces by empty character, so we can send that in WhatsApp.
message = message.replace(' ', '-')

print(message)
chars = [char for char in message]

type_phone(characters=chars, cord=[1000, 1200], delay=0)
# 1000, 2100 (click button without keyboard)
