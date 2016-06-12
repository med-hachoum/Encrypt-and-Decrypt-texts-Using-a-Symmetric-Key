# windtalker simple cryptographer : Encrypt and Decrypt Data Using a Symmetric Key
# To use this code, you need to pip install windtalker


from windtalker.symmetric import SymmtricCipher

print ('''
_/﹋\_
(҂`_´)           ╔═══════ೋღღೋ ═══════╗
<,︻╦╤─ ҉ - - -   windtalker cryptography
_/﹋\_           ╚═══════ೋღღೋ ═══════╝
''')


# encryption, view of your friend
cipher = SymmtricCipher(password="MyPassword")
message = "Your text !"
crypted_message = cipher.encrypt_text(message)
print(crypted_message)

# Decryption, view of your friend
new_cipher = SymmtricCipher(password="MyPassword")
decrypted_message = new_cipher.decrypt_text(crypted_message)

print(decrypted_message)
