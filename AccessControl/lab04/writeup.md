# Lab: User Role Can Be Modified in User Profile

I completed this lab by logging in with the provided credentials `wiener:peter` and testing the account profile functionality. When updating the email address, I noticed that the request used JSON and that the server accepted additional user-controlled fields. I modified the email change request by adding `"roleid": 2`, which changed my account from a normal user into an admin user. After confirming that the response showed admin access, I visited the `/admin` panel. From there, I sent a request to delete the `carlos` user, which solved the lab.

Source: https://portswigger.net/web-security/access-control/lab-user-role-can-be-modified-in-user-profile
