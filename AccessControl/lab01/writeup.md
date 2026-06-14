# Lab: Unprotected Admin Functionality

I completed this lab by first checking the site's `robots.txt` file, which exposed the hidden `/administrator-panel` path through a `Disallow` entry. After discovering that route, I visited the administrator panel directly and confirmed that it was accessible without authentication. This showed that the application had an access control flaw because sensitive admin functionality was exposed to unauthenticated users. I then used the delete function on the panel to remove the `carlos` user, which solved the lab. To automate the process, I wrote a Python script that requests `/administrator-panel`, checks for a successful response, and then sends a request to `/delete?username=carlos`.

Source: https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality
