# Cookie Monster

### 📄 Description

In order to get the points of this challenge, you need to provide a 
detailed description of the procedure that you used to get the flag.
Otherwise we account for the flag as read by the web application folder itself.

### ⚙ How to run it

In order to run the challenge you need to set up two environmental variables:

```console
$export FLASK_ENV=development
$export FLASK_APP=app
```

and run the local server with:

```console
$cd webapp
$flask run
```

You should see in the command output the link to the page
If you can't find it, it should be at http://127.0.0.1:5000/

The descriprion of the challenge itself is on the webpage.

### ⛔ Rules
Don't open the `webapp` folder.

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

After launching the site, you can read either "The cookie seems quite weird" or "Cookie Monster," which suggests to examin the cookies.

1. Go to `Inspect` --> `Storage` --> `Cookies`, and observe the value `04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb` under "permission." This is a `sha256` encoded hash, meaning "user."

2. Change its value from "user" to "admin" and encode it in `sha256`, resulting in `8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918`.

3. Replace the cookie value with this newly generated hash.

4. Login and we obtain the flag

<h3> 🚩 Flag </h3>

```plain
spritz{thank_you_for_the_cookie}
```
</details>