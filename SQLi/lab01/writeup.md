# PortSwigger SQL Injection Lab — Retrieve Hidden Data

This lab demonstrates a basic SQL injection vulnerability in a product category filter. The application builds a SQL query using the `category` parameter, so injecting a condition like `' OR 1=1--` changes the logic of the `WHERE` clause. I also wrote a small Python script, `sqli-lab-01.py`, that takes the lab URL and payload as command-line arguments, sends the injected request with `requests.get()`, and checks the response to see whether the hidden products were revealed. While testing it, I ran into a proxy connection issue because the script was configured to send traffic through Burp Suite, but the proxy was not accepting connections. The main lesson is that user input should never be directly inserted into SQL queries; prepared statements/parameterized queries are needed to keep data separate from SQL logic.

Source: https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data
