CREATE TABLE Pieces(
    id SERIAL PRIMARY KEY,
    title TEXT,
    included BOOLEAN
);

CREATE TABLE Links(
    id SERIAL PRIMARY KEY,
    piece_id INTEGER REFERENCES Pieces(id) ON DELETE CASCADE,
    link TEXT
);
