from abc import ABC, abstractmethod

class PessoaJuridica():
    pass
class Fornecedores(PessoaJuridica):
    pass
class EmpresaJr(PessoaJuridica):
    pass


class PessoaFisica(ABC):
    pass

class Professor(PessoaFisica):
    pass

class Aluno(PessoaFisica):
    pass

class Técnico(PessoaFisica):
    pass

class Curso():
    pass

class Disciplina():
    pass

