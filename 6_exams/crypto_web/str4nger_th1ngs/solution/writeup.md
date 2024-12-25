# 🔑 Write-Up

To complete this challenge, we need to decrypt using various encryptions:

1. First of all we need to decrypt the morse code, which give us
```plain
GREAT  YOU VE CLEARED THE FIRST STEP  I HAD TO ENCRYPT THE MESSAGE TO PREVENT IT FROM BEING INTERCEPTED  CONTINUE TO DECRYPT
```
2. Then we need to decrypt the second line of the file. We can using a online tool to figure out witch encryption it has and is base64, so we decrypt it and we get:

```plain
Fbzrguvat jrveq vf tbvat ba ng gur yvoenel. V znantrq gb unpx vagb n Ehffvna sbez V sbhaq ba gur yvoenel'f jrofvgr. V guvax gurl'er hfvat gur yvoenel nf n pbire sbe zber Zvaqsynlre erfrnepu. V’z tbaan tvir lbh gur pbbeqvangrf bs gur frperg cnffntr, gryy Zvxr gb pbzr urer!

45.41130017965508%2C%2011.887730729281115%2019-16-18-9-20-26%7B20-8-5%2016-12-1-14-11%E2%80%9919%203-15-14-19-20-1-14-20%209-19%2020-8-5%2011-5-25%7D 

29656C626174726F666D6F632074656720646E61206B6E696C20656874206574736170282041396C6578776A41595A593D763F68637461772F6D6F632E65627574756F792E7777772F2F3A7370747468202165697A755320796C65766F6C20796D20646E6120656D2079622064656D726F6672657020676E6F73207373656C646E65206E61206576726573656420756F79202C7261662073696874207469206564616D20657627756F792066492021736E6F6974616C75746172676E6F43
```

We see that there are 3 differents type of encryption:
1. The first one is a substitution cipher, so we have to brute force trying to change letters by letters the text. After do that we get

```plain
SOMETHING WEIRD IS GOING ON AT THE LIBRARY. 
I MANAGED TO HACK INTO A RUSSIAN FORM I FOUND ON THE LIBRARY'S WEBSITE. 
I THINK THEY'RE USING THE LIBRARY AS A COVER FOR MORE MINDFLAYER RESEARCH. 
I’M GONNA GIVE YOU THE COORDINATES OF THE SECRET MASSAGE, TELL MIKE TO COME HERE!

```

2. The second seems to be coordinates. But if we look carefully, we may notice a pattern where there are "number-number-munber". This could be a "numbers to letters cipher", where every number leads to its position in the alphabet:

```plain
SPRITZTHEPLANKCONSTANTISTHEKEY
```

3. This one is optional (since we've  already found the flag), but who cares. It seems a hex encryption so

```plain
)elbatrofmoc teg dna knil eht etsap( A9lexwjAYZY=v?hctaw/moc.ebutuoy.www//:sptth !eizuS ylevol ym dna em yb demrofrep gnos sseldne na evresed uoy ,raf siht ti edam ev'uoy fI !snoitalutargnoC
```

we clearly notice that the text is revesed so 
```plain
Congratulations! If you've made it this far, you deserve an endless song performed by me and my lovely Suzie! https://www.youtube.com/watch?v=YZYAjwxel9A (paste the link and get comfortable)
```

That was worth it!


### 🚩 Flag

```plaintext
SPRITZTHEPLANKCONSTANTISTHEKEY
```