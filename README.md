# CS-340

) Writing maintainable, readable, and adaptable programs

I write programs to be maintainable, readable, and adaptable by separating concerns and keeping each part focused on one job. The database operations live in a dedicated CRUD Python module, while the dashboard handles user interaction and visualization. I use clear function names, docstrings, and small units of logic so changes are localized and easy to test. Connection details are parameterized which allows the same code to run in different environments without edits. Reusing the CRUD module from Project One to power the widgets in Project Two reduced duplication and improved testability. The module can be imported by other tools in the future such as command line utilities, scheduled jobs, or additional dashboards.

2) Approach to problem solving as a computer scientist

I approached the problem like a computer scientist by working in short iterations and validating every assumption early. I clarified the required filters, tables, maps, and charts, then defined a firm boundary between the data layer and the user interface. I verified basic queries before adding interactivity so that data defects could not hide behind user interface issues. Compared with earlier assignments I relied more on modular design, logging, and small integration checks which made bugs easier to reproduce and fix. In future projects I would use environment variables for configuration, seed scripts to create a consistent starting state, and automated tests for common queries.

3) What computer scientists do and why it matters

Computer scientists turn goals into dependable systems that help people make decisions. In this project the work for Grazioso Salvare converts rescue criteria into precise database queries and presents results in a clear dashboard. This shortens the path from data to action which saves time and improves placement outcomes. Good data modeling, clean interfaces, and maintainable code directly support the mission of the organization and allow it to scale its impact.
