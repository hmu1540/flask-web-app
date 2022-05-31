DROP TABLE IF EXISTS user; 
/* Be careful before dropping a table. Deleting a table will result in loss of complete information stored in the table! */

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);