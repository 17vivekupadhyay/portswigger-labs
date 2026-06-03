# PortSwigger SQL Injection Lab — Login Bypass

This lab demonstrates a SQL injection vulnerability in a login form. The application appears to build a SQL query using the `username` and `password` fields, so injecting a payload like `administrator'--` into the username changes the query logic and comments out the password check. 

I wrote a Python script, `sqli-lab-02.py`, that takes the lab URL and payload as command-line arguments, creates a session, grabs the CSRF token from the login page, and submits the injected login request with `requests.post()`. One struggle I ran into was realizing that the login form required a valid CSRF token, so I had to first send a GET request to `/login`, parse the token with BeautifulSoup, and include it in the POST request. The main lesson is that authentication logic should never directly trust user-controlled input, and SQL queries should use prepared statements/parameterized queries to prevent attackers from changing the query structure.

Source: https://portswigger.net/web-security/sql-injection/lab-login-bypass
