# SQL
from : [CS50](https://cs50.harvard.edu/x/2025/weeks/7/)
## CRUD

| CRUD | SQL |
| :-------------- | --------------:|
|CREATE |   CREATE, INSERT|
|READ   |   SELECT|
|UPDATE |   UPDATE |
|DELETE |   DELETE, DROP |

`CREATE TABLE table (column type, ...);`

### Importing a CSV

```bash 
sqlite3 example.db
sqlite> .mode csv                   #Configure CSV Mode 
sqlite> .import example.csv example #Import CSV File into a table
sqlite> .schema                     #Show architecture of DB
sqlite> .mode box                   #Show as a tab
# Also .mode table, .mode markdown, .mode csv
sqlite> .quit
```

### Beginning manipulating data

```sql
SELECT * FROM example;                      -- Select all from "example" table in example.db
SELECT Region FROM example;                 -- Select only the Region column
SELECT COUNT(*) FROM example;               -- Show the number of rows
SELECT DISTINCT Region FROM example;        -- Show the different regions of example
SELECT COUNT(DISTINCT Region) FROM example; -- Number of different regions
SELECT COUNT(*) FROM example WHERE region = 'Europe'; -- Number of rows in Europe 
--!!! For Text use only ' and not "
SELECT COUNT(*) FROM example WHERE region = 'North America' AND race = 'Asian'; -- Combinaison North America and Asian
-- For escaping ', use ''
SELECT COUNT(*) FROM example WHERE region LIKE 'North A%' AND race = 'Asian'; -- Combinaison North America and Asian
SELECT region, COUNT(*) FROM example GROUP BY region ORDER BY COUNT(*); -- Select all the regions and for each show the count (ordered)
-- ORDER BY #VAR [ASC...DESC]
SELECT region, COUNT(*) AS n FROM example GROUP BY region ORDER BY n DESC; -- Same as prev, but with an alias
"  "                            "                       "    LIMIT 1;      -- Just show the first result

```

### Builtin Formulas

```sql
AVG
COUNT
DISTINCT
LOWER
MAX
MIN
UPPER
GROUP BY
LIKE
LIMIT
ORDER BY
WHERE
...
```

### Changing Data
`INSERT INTO table (column, ...) VALUES(value, ...);` \
`DELETE FROM table WHERE condition;` \
`UPDATE table SET column = value WHERE condition;` \
*example*
```sql
sqlite> INSERT INTO cancer (region, race) VALUES('Mars', NULL); -- when empty us NULL
sqlite> SELECT region, race, age, COUNT(region) AS n FROM cancer GROUP BY race ORDER by n DESC;
┌───────────────┬──────────┬─────┬───────┐
│    Region     │   Race   │ Age │   n   │
├───────────────┼──────────┼─────┼───────┤
│ North America │ White    │ 80  │ 44887 │
│ North America │ Black    │ 34  │ 18005 │
│ Latin America │ Asian    │ 72  │ 13502 │
│ Europe        │ Hispanic │ 41  │ 9040  │
│ Europe        │ Other    │ 71  │ 4511  │
│ Mars          │          │     │ 1     │
└───────────────┴──────────┴─────┴───────┘
sqlite> DELETE FROM cancer WHERE race IS NULL; -- to select the condition NULL, use IS NULL
sqlite> SELECT region, race, age, COUNT(region) AS n FROM cancer GROUP BY race ORDER by n DESC;
┌───────────────┬──────────┬─────┬───────┐
│    Region     │   Race   │ Age │   n   │
├───────────────┼──────────┼─────┼───────┤
│ North America │ White    │ 80  │ 44887 │
│ North America │ Black    │ 34  │ 18005 │
│ Latin America │ Asian    │ 72  │ 13502 │
│ Europe        │ Hispanic │ 41  │ 9040  │
│ Europe        │ Other    │ 71  │ 4511  │
└───────────────┴──────────┴─────┴───────┘
UPDATE cancer SET race = 'Weird and strange', region = 'nowhere' WHERE region = 'Latin America';
```
### Example of Create
```sql
sqlite> .schema shows
CREATE TABLE shows (
    id INTEGER,
    title TEXT NOT NULL,
    year NUMERIC,
    episodes INTEGER,
    PRIMARY KEY(id)
);
sqlite> .schema ratings
CREATE TABLE ratings (
    show_id INTEGER NOT NULL,
    rating REAL NOT NULL,
    votes INTEGER NOT NULL,
    FOREIGN KEY(show_id) REFERENCES shows(id)
);
```
1'26'35
