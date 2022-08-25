SELECT * FROM "Products";

SELECT "Name", "ID" FROM "Products";

SELECT * FROM "Products" WHERE "ID"=10;

SELECT * FROM "Products" WHERE "Inventory"= 0;

SELECT * FROM "Products" WHERE "Price" > 45;

SELECT * FROM "Products" WHERE "Inventory" !=0;

SELECT * FROM "Products" WHERE "Inventory" > 50 AND "Price" > 20;

SELECT * FROM "Products" WHERE "ID"= 1 OR "ID"= 2 or "ID"=3;

SELECT * FROM "Products" WHERE "ID" IN (1,2,3);

SELECT * FROM "Products" WHERE "Name" LIKE "TV%";

SELECT * FROM "Products" WHERE "Name" LIKE "%s";

SELECT * FROM "Products" ORDER BY "Price";


SELECT * FROM "Products" WHERE "Price" > 20 ORDER BY "created_at" DESC;

SELECT * FROM "Products" WHERE "Price" > 20 ORDER BY "created_at" DESC LIMIT 5;

SELECT * FROM "Products" ORDER BY "ID" LIMIT 5 OFFSET 2;

INSERT INTO "Products" ("Name", "Price", "Inventory") VALUES ('Tortilla', 4, 2500);

INSERT INTO "Products" ("Name", "Price", "Inventory") VALUES ('Laptop', 400, 25), ('Manga', 2, 169) RETURNING *;

DELETE FROM "Products" WHERE "ID"= 10;

DELETE FROM "Products" WHERE "ID"= 11 RETURNING *;

UPDATE "Products" SET "Name"= 'Flour Tortilla', "Price"= 40 WHERE "ID"= 28;

