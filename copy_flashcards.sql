truncate top1000;
# После FROM в одинарных кавычках надо прописать полный путь до файла
COPY top1000(eng, rus) FROM '../flashcards.csv' WITH (FORMAT csv);
