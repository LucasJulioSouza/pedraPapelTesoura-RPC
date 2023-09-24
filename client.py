import Pyro4

uri = "PYRO:obj_123@127.0.0.1:9090"  # Substitua pelo URI correto do servidor

with Pyro4.Proxy(uri) as jogo_rpc:
    jogador1 = input("Jogador 1, escolha entre pedra, papel ou tesoura: ").lower()
    jogador2 = input("Jogador 2, escolha entre pedra, papel ou tesoura: ").lower()

    resultado = jogo_rpc.jogar(jogador1, jogador2)
    print(resultado)
