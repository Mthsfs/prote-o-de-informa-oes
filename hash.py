import hashlib

# Função para gerar o hash SHA-256 de uma palavra/senha
def gerar_hash(texto):
    # Converte o texto em bytes e aplica o algoritmo SHA-256
    texto_em_bytes = texto.encode('utf-8')
    hash_objeto = hashlib.sha256(texto_em_bytes)
    # Retorna o hash formatado em formato hexadecimal (letras e números)
    return hash_objeto.hexdigest()

# --- Testando o Hash ---
print("--- TESTE DE SEGURANÇA COM HASH ---")
senha_usuario = "minhaSenhaSuperSegura123"

# Gerando o hash da senha original
hash_da_senha = gerar_hash(senha_usuario)
print(f"Senha: {senha_usuario}")
print(f"Hash gerado (SHA-256): {hash_da_senha}")

# Simulando uma tentativa de login
print("\n--- SIMULANDO LOGIN ---")
senha_digitada = input("Digite sua senha para entrar: ")

if gerar_hash(senha_digitada) == hash_da_senha:
    print("🔓 Acesso Permitido! A senha está correta.")
else:
    print("❌ Acesso Negado! Senha incorreta.")
