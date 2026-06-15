# Lab: User ID Controlled by Request Parameter

I completed this lab by logging in with the provided credentials `wiener:peter` and accessing the normal account page. The application used an `id` parameter in the `/my-account` URL to decide which user's account details to display. I changed the parameter from my own username to `carlos`, which allowed me to access Carlos's account page without proper authorization. This exposed Carlos's API key, showing a horizontal privilege escalation vulnerability because one user could access another user's data by modifying a request parameter. I then submitted Carlos's API key to solve the lab.

Source: https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter
