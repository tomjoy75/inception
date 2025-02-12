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
SELECT COUNT(*) FROM cancer WHERE region = 'North America' AND race = 'Asian'; -- Combinaison North America and Asian
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
1'01'35