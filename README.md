Calorie tracker app built with ChatGPT + SQLite

Example usage:

```
peterkuimelis@PETER-KUIMELIS foobar % python3 calorie_tracker.py
ready...
shrimp fried rice and 12oz can of coke
INSERT INTO foods (description, category, calories)
VALUES ("shrimp fried rice", "Chinese food", 400),
       ("12oz can of coke", "Soda", 140);
OK
ready...
slice of pizza
INSERT INTO foods (description, category, calories)
VALUES ("slice of pizza", "Fast food", 280);
OK
ready...
2 cuties
INSERT INTO foods (description, category, calories)
VALUES ("cuties", "Fruit", 60);
OK
ready...
glass of water
INSERT INTO foods (description, category, calories)
VALUES ("glass of water", "Drink", 0);
OK
ready...
dumplings
INSERT INTO foods (description, category, calories)
VALUES ("dumplings", "Chinese food", 200);
OK
ready...
how many times did i have ethnic food in the last day?
SELECT COUNT(*)
FROM foods
WHERE category IN ('Chinese food', 'Mexican food', 'Indian food', 'Thai food', 'Other ethnic food')
AND timestamp >= datetime('now', '-1 day');
2
ready...
how many of my calories came from fast food?
SELECT SUM(calories)
FROM foods
WHERE category = 'Fast food';
280
ready...
how many glasses of water did i drink today?
SELECT COUNT(*)
FROM foods
WHERE description = 'glass of water'
AND timestamp >= datetime('now', 'start of day');
1
ready...
1 apple
INSERT INTO foods (description, category, calories)
VALUES ("apple", "Fruit", 95);
OK
ready...
1 piece of asparagus
INSERT INTO foods (description, category, calories)
VALUES ("asparagus", "Vegetable", 20);
OK
ready...
did i get more calories from fruits or veggies today?
SELECT SUM(CASE WHEN category IN ('Fruit', 'Vegetable') THEN calories ELSE 0 END) AS "calories_from_fruits_veggies",
       SUM(CASE WHEN category NOT IN ('Fruit', 'Vegetable') THEN calories ELSE 0 END) AS "calories_from_other"
FROM foods
WHERE timestamp >= datetime('now', 'start of day');
175
```
