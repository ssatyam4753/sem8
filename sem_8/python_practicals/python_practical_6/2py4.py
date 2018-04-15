from Crypto.PublicKey import RSA
key = RSA.generate(2048)

binPrivKey = key.exportKey('DER')
binPubKey =  key.publickey().exportKey('DER')

privKeyObj = RSA.importKey(binPrivKey)
pubKeyObj =  RSA.importKey(binPubKey)

msg = "attack at dawn"
public_key = key.publickey()
enc_data = public_key.encrypt('abcdefgh', 32)

#emsg = pubKeyObj.encrypt(msg,32)
print(enc_data)
dmsg = privKeyObj.decrypt(emsg)
print(dmsg)
