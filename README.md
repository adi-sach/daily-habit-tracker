# Daily Habit Tracker

#### Video Demo:  https://youtu.be/H07Lo5bcVhs

#### Description:
The Daily Habit Tracker is a web-based application built using Flask and SQLite that allows users to track the completion of their daily habits. The goal of this project is to provide a simple, reliable, and easy-to-use system for monitoring daily routines.

The application allows users to add habits that they want to perform daily, such as exercising, reading, or studying. Once a habit is added, it appears on the home page every day. Each habit can be marked as completed for the current day using a single button. Importantly, the completion status of habits automatically resets every day without requiring any manual action from the user.

This behavior is achieved through the project’s database design. The application uses two database tables: one to store habits permanently, and another to store daily completion logs. Habits are stored in a table called `habits`, which contains the habit name and a unique identifier. Daily completion is tracked in a separate table called `habit_logs`, which stores the habit identifier, the date, and whether the habit was completed. By associating completion data with a specific date, the application can determine whether a habit has been completed on the current day simply by checking for a matching log entry.

On the homepage, the application performs a database query that retrieves all habits and joins them with today’s log entries. If a habit does not have a log entry for the current date, it is automatically considered “Not Completed”. This design eliminates the need for scheduled resets or background tasks and keeps the logic simple and robust.

The project also includes a history page that allows users to view past habit completion records. This page reads directly from the `habit_logs` table and displays the habit name, date, and completion status.

In the future, the application can be extended with an analysis page to make habit tracking more interactive and insightful. This page could aggregate data from the `habit_logs` table to calculate metrics such as completion percentages, weekly and monthly consistency, and habit streaks. Using SQL aggregation queries combined with Python logic, the app could generate summaries showing which habits are performed most consistently and which ones need improvement. Visualizations such as bar charts or line graphs could be added using libraries like Chart.js to help users better understand their progress over time.

Additional improvements could include filtering history by date range, displaying streak counts for each habit, and providing reminders or motivational messages based on user performance. User authentication could also be introduced to support multiple users, allowing each user to maintain their own set of habits and logs securely. Other enhancements might include editing or deleting habits, exporting habit data, and adding mobile-friendly optimizations.

The application uses Flask for routing and request handling, SQLite for persistent data storage, and the CS50 SQL library to simplify database interactions and improve readability. HTML templates are rendered using Jinja, and Bootstrap is used for basic styling to ensure the interface is clean and user-friendly.

Overall, this project demonstrates core web development concepts including Flask routing, form handling, SQL database design, relational queries, and template rendering. The focus of the project is correctness, clarity, and maintainability, while still allowing clear pathways for future expansion and increased interactivity.
