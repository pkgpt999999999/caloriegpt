import sqlite3

from chatgpt_wrapper import ChatGPT


class CalorieTracker:
    def __init__(self):
        self.bot = ChatGPT()
        self.bot.ask(
            """
            i want you to behave like the business logic for a calorie tracker app. 
            the app supports recording meals and retrieving statistics, eg how many calories 
            did i consume in the last 12 hours. there is one table foods with columns for 
            description, category (eg fast food, vegetables, meat, soda, etc) calories and datetime
            timestamp (default CURRENT_TIMESTAMP). i will make requests in english, and you will 
            respond with a SQL statement that expresses that request. respond with valid SQL 
            (sqlite) ONLY, NO EXPLANATIONS. again, do not include explanations. i only want the 
            SQL. use your best guess for the calorie count and category. a meal may contain 
            multiple foods, in this case, break them down into foods. here is the statement that creates
            the schema: CREATE TABLE IF NOT EXISTS foods (
                description TEXT,
                category TEXT,
                calories INTEGER,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                ); 
            lets begin. please say ready.
            """
        )
        self.conn = sqlite3.connect("/tmp/calories.db")
        self.conn.cursor().execute(
            """
            CREATE TABLE IF NOT EXISTS foods (
                description TEXT,
                category TEXT,
                calories INTEGER,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                );
            """
        )

    def handle(self, request):
        sql = self.bot.ask(request)
        print(sql)
        fetched = self.conn.cursor().execute(sql).fetchone()
        response = fetched[0] if fetched is not None else "OK"
        self.conn.commit()
        return response

tracker = CalorieTracker()
while True:
    print(tracker.handle(input('ready...\n')))
