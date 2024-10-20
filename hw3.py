from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# 設置一個明文和金鑰
plaintext = b'security'
key = get_random_bytes(8)  # 隨機產生金鑰
cipher = DES.new(key, DES.MODE_ECB)

key2 = (int.from_bytes(key, 'big') + 1).to_bytes(8, 'big')  # 在最後一個bit上加1
cipher2 = DES.new(key2, DES.MODE_ECB)

ciphertext1 = cipher.encrypt(plaintext)
ciphertext2 = cipher2.encrypt(plaintext)

print("金鑰相差一bit")
diff_bits = sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(ciphertext1, ciphertext2))
print(f"密文差異的bit數：{diff_bits}，差異比例：{diff_bits/64:.2%}\n")

plaintext2 = (int.from_bytes(plaintext, 'big') + 1).to_bytes(8, 'big')  # 在最後一個bit上加1

ciphertext1 = cipher.encrypt(plaintext)
ciphertext3 = cipher.encrypt(plaintext2)

print("明文相差一bit")
diff_bits = sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(ciphertext1, ciphertext3))
print(f"密文差異的bit數：{diff_bits}，差異比例：{diff_bits/64:.2%}\n")