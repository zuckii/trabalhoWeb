CREATE TABLE IF NOT EXISTS Usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Genero (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Filmes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    genero_id INTEGER NOT NULL,
    imagem TEXT,
    FOREIGN KEY (genero_id) REFERENCES Genero(id)
);

CREATE TABLE IF NOT EXISTS Avaliacao (
    usuario_id INTEGER NOT NULL,
    filme_id INTEGER NOT NULL,
    nota INTEGER CHECK(nota BETWEEN 0 AND 5),
    comentario TEXT,
    PRIMARY KEY (usuario_id, filme_id),
    FOREIGN KEY (usuario_id) REFERENCES Usuario(id),
    FOREIGN KEY (filme_id) REFERENCES Filmes(id)
);
