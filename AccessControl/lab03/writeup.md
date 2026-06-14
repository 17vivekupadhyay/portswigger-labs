# Lab: User Role Controlled by Request Parameter

I completed this lab by logging in with the provided credentials `wiener:peter` and inspecting how the application tracked user roles. After authentication, I found that the application used a client-side cookie named `Admin` to decide whether the user had administrator access. Since this value was controlled by the client, I changed the cookie from `Admin=false` to `Admin=true` while keeping the valid session cookie. This allowed me to access the `/admin` panel even though the account was not supposed to be an administrator. I then sent a request to `/admin/delete?username=carlos`, which deleted the `carlos` user and solved the lab.

Source: https://portswigger.net/web-security/access-control/lab-user-role-controlled-by-request-parameter
