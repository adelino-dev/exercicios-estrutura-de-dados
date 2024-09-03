def ehPalindroma(palavra):
  inversa = ""
  for i in range(1, len(palavra)+1):
      inversa += palavra[-i]

  return inversa == palavra

if __name__ == "__main__":
  palavra = input("Palavra:")
  if ehPalindroma(palavra) == True:
      print("É palindroma.")
  else:
      print("NÃO é palindroma.")