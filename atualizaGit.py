
import git 
caminho = input("Entre com o caminho para Atualizacao: ")
comandoGitPull = "git pull"
comandoFinder = "cd /"
comandoFinderLocaliza = comandoFinder+caminho
g = git.cmd.Git(comandoFinderLocaliza)
g.pull()
