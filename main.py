import hashlib
from re import A

myText = input("Insira a frase descriptografada: ")

SHA256 = hashlib.sha256(myText.encode('utf-8')).hexdigest()
MD5 = hashlib.md5(myText.encode('utf-8')).hexdigest()

inputSHA256 = input("Insira a frase criptografado em SHA256: ")

inputMD5 = input("Insira a frase criptografado em MD5: ")

print("\nFrase original e suas criptografias corretas: ")
print("\"" + myText + "\" - " + SHA256 + " - " + MD5)

if inputSHA256 == SHA256 and inputMD5 == MD5:
  print("\nAs 2 criptografias inseridas estão corretas\n")

if inputSHA256 == SHA256 and inputMD5 != MD5:
  print("\nApenas a criptografia SHA256 está correta")
  print("\nCriptografia inserida MD5: " + inputMD5)
  print("\nCriptografia correta MD5: " + MD5)

if inputSHA256 != SHA256 and inputMD5 == MD5:
  print("\nApenas a criptografia MD5 está correta")
  print("\nCriptografia inserida SHA256: " + inputSHA256)
  print("\nCriptografia correta SHA256: " + SHA256)

if inputSHA256 != SHA256 and inputMD5 != MD5:
  print("\nAs 2 criptografias estão incorretas")
  print("\nCriptografia inserida SHA256: " + inputSHA256)
  print("\nCriptografia correta SHA256: " + SHA256)
  print("\nCriptografia inserida MD5: " + inputMD5)
  print("\nCriptografia correta MD5: " + MD5)
