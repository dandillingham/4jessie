CREATE TABLE person (
	id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	dob TEXT,
	mummy TEXT,
        daddy TEXT 
);
CREATE TABLE sibling(
        id INTEGER PRIMARY KEY,
        person_id INTEGER, 
        name TEXT NOT NULL,
        FOREIGN KEY (person_id)
           REFERENCES person (person_id)
); 

