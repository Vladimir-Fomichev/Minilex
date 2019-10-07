CREATE TABLE top1000
(id smallserial PRIMARY KEY,
eng VARCHAR (50),
rus VARCHAR (60),
score smallint DEFAULT 0);
# После FROM в одинарных кавычках надо прописать полный путь до файла
COPY top1000(eng, rus) FROM '../flashcards.csv' WITH (FORMAT csv);
