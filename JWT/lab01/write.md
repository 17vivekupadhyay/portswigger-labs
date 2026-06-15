# Lab: JWT Authentication Bypass via Unverified Signature

I completed this lab by logging in with the provided credentials `wiener:peter` and inspecting the session cookie. The session value was a JWT, so I decoded it using `jwt.io` and found that the payload contained a `sub` claim set to my username. Because the server did not properly verify the JWT signature, I changed the `sub` value from `wiener` to `administrator` and re-encoded the token. I then used the modified JWT in the session cookie to access the `/admin` panel. From there, I sent the request to delete the `carlos` user, which solved the lab.

Sources:
- https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-unverified-signature
- https://www.jwt.io/
