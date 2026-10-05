# Função para criptografar uma mensagem empurrando as letras
def criptografar(texto, chave=3):
    mensagem_oculta = ""
    for letra in texto:
        if letra.isalpha():  # Verifica se é uma letra do alfabeto
            # Define se a letra é maiúscula ou minúscula
            base = ord('A') if letra.isupper() else ord('a')
            # Faz o cálculo de rotação (Cifra de César)
            nova_letra = chr((ord(letra) - base + chave) % 26 + base)
            mensagem_oculta += nova_letra
        else:
            mensagem_oculta += letra  # Mantém espaços e pontuações iguais
    return mensagem_oculta

# Função para descriptografar (faz o processo inverso)
def descriptografar(texto_criptografado, chave=3):
    return criptografar(texto_criptografado, -chave)

# --- Testando a Criptografia ---
print("--- TESTE DE CRIPTOGRAFIA ---")
mensagem_original = "Alura Start Ensino Medio"
print(f"Mensagem Original: {mensagem_original}")

# Criptografando
secreto = criptografar(mensagem_original)
print(f"Mensagem Criptografada: {secreto}")

# Descriptografando
revelado = descriptografar(secreto)
print(f"Mensagem Revelada: {revelado}\n")
