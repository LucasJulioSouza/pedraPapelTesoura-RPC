import Pyro4

@Pyro4.expose
class JogoRPC:
    def __init__(self):
        self.opcoes = ["pedra", "papel", "tesoura"]

    def jogar(self, jogador1, jogador2):
        if jogador1 not in self.opcoes or jogador2 not in self.opcoes:
            return "Opção inválida. Escolha entre pedra, papel ou tesoura."
        
        if jogador1 == jogador2:
            return "Empate!"

        if (jogador1 == "pedra" and jogador2 == "tesoura") or \
           (jogador1 == "papel" and jogador2 == "pedra") or \
           (jogador1 == "tesoura" and jogador2 == "papel"):
            return "Jogador 1 vence!"
        else:
            return "Jogador 2 vence!"

daemon = Pyro4.Daemon()
uri = daemon.register(JogoRPC)

print("Aguardando conexões na porta 9090...")
daemon.requestLoop()
