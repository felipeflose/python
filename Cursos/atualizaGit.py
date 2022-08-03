
import git

caminho = input("Entre com o caminho para Atualizacao: ")
comandoFinderLocaliza = caminho
g = git.cmd.Git(comandoFinderLocaliza)
g.pull()
