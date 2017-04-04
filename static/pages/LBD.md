=====================
HIGOR : ecbdi07

Clicar no + verde

Nome conexao : eclbdi07
Nome usuario : eclbdi07
senha : aluno
Host: oracle.decom.cefetmg.br
porta:1521

SID : xe

-- MAPEAMENTO DO MER DE BANCO PARA M

# H1 -- 1) TABELA BANCO

BANCO(Codigo,Nome,Endereco) PK = Codigo

create table Banco (
	Codigo number(5) primary key,
	Nome varchar2(30) not null,
	Endereco varchar2(50) not null
);

insert into Banco value(
	1,'Banco', 'Rua A , n1' 
);

select * from Banco;

-- 2)Tabela agencia bancaria

create table Agencia_bancaria(
	CodBan number(5) references Banco(Codigo), 
	Endereco varchar2(50) not null,
	NumAgencia number(5),
	primary key (CodBan NumAgencia)
);

insert into Agencia_bancaria value( 2,100,'Rua a, n2') -- ERRO, nao existe o banco 2

insert into Agencia_bancaria value(1,100,'Rua a, n2') -- Banco 1 existe, sucesso
insert into Agencia_bancaria value(1,100,'Rua a, n2') -- ERRO, Agencia ja exista


create table Conta (
	NumConta
)