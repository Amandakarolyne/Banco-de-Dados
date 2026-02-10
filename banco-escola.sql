-- Criação do banco de dados "escola"
CREATE DATABASE escola;

-- Selecionar o banco de dados "escola"
USE escola;

-- Tabela de alunos
CREATE TABLE alunos (
    aluno_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

-- Tabela de professores
CREATE TABLE professores (
    professor_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

-- Tabela de disciplinas
CREATE TABLE disciplinas (
    disciplina_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

-- Tabela de matrículas
CREATE TABLE matriculas (
    matricula_id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_id INT,
    disciplina_id INT,
    FOREIGN KEY (aluno_id) REFERENCES alunos(aluno_id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplinas(disciplina_id)
);

-- Tabela de turmas
CREATE TABLE turmas (
    turma_id INT AUTO_INCREMENT PRIMARY KEY,
    disciplina_id INT,
    professor_id INT,
    FOREIGN KEY (disciplina_id) REFERENCES disciplinas(disciplina_id),
    FOREIGN KEY (professor_id) REFERENCES professores(professor_id)
);
