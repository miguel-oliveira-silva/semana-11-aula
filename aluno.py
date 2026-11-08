class AlunoClass:
  def __init__(self, nome, sobrenome, nota):    
    self.nome = nome;
    self.sobrenome = sobrenome;
    self.nota = nota;

  def mostrarAluno(self):
    return 'Aluno: ' + self.nome + ' ' + self.sobrenome + ' - Nota: ' + str(self.nota);    

  def salvar(self, conexao, colecao):    
    aluno = self.__dict__.copy()
    resultado = conexao[colecao].insert_one(aluno)
    return resultado.acknowledged