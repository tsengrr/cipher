from Crypto.Cipher import AES
import base64
import itertools

key = "@K▆X%▆3Qh▆DD▆RqQ"  
mode = AES.MODE_ECB
padding = '\x00'


cipher_text = base64.b64decode("2mfH5wwaQuC9qvrfFPMgvIvU1ggfGcg8jkanFZfn91k=")

# 字符集（可能的字符）
charset = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

# 生成所有未知字符的组合
combinations = itertools.product(charset, repeat=key.count('▆'))

for replacement_chars in combinations:
    modified_key = key
    for char in replacement_chars:
        modified_key = modified_key.replace('▆', char, 1)

    
    if len(modified_key) != 16:
        continue

    try:
        decryptor = AES.new(modified_key.encode('utf-8'), mode)
        plaintext = decryptor.decrypt(cipher_text).rstrip(padding.encode('utf-8'))

        print(f"找到可能的明文：{plaintext.decode('utf-8')}")
        print(f"使用的密鑰：{modified_key}")
        break  

    except Exception as e:
        continue  
