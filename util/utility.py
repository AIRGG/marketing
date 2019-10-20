import hmac
import hashlib 
import binascii

def create_sha256_signature(key, message):
    byte_key = binascii.unhexlify(key)
    message = message.encode()
    return hmac.new(byte_key, message, hashlib.sha256).hexdigest()

def sha256(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

text=hex(229521378423901)+'MyLocal_1234'
# print(create_sha256_signature('E49756B4C8FAB4E48222AaE7F3B97CC5', text))
print(sha256('151118..,,GALUHBismillahLogin'))
# print(sha256('BISMILLAH'))