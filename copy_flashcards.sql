truncate top1000;
COPY top1000(eng, rus) FROM 'D:/RIKAS/PostgreSQL/git/flashcards.csv' WITH (FORMAT csv);
select * from top1000 limit 12;