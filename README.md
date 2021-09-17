# discord-theory-I

## *PART: I*

My attempt to reverse the Discord nitro token generation function.

The Nitro generation tools thing is common in Discord now, but none of the tools actually works, so I decided to take it to the next level, and reverse the actual tokens in hopes of finding a better way of generation.

```diff
- NOTE: This is just for research, I will and I hope no one uses it for bad purposes.
```
## Introduction:

If you are not familiar with Discord, nitro is a kind of membership, you pay to get access and do some cool things on Discord, like get a GIF profile picture or upload large size photos and videos, and in order to get it you must either buy it directly or having someone offer it to you, in the second case it would be something like this: [`https://discord.gift/hNN5SBsnHTPFFh3Z`](https://discord.gift/hNN5SBsnHTPFFh3Z)

The Discord Gift URL followed by a 16-length code will redirect you to the claim page.

## First look:

At first sight it looks like Base64 encoded, using Burp Suite Decoder we will be able to get this result:

```markdown
00000000 84 d3 79 48 1b 27 1d 33 c5 16 1d d9 -- -- -- -- �ÓyH�'�3Å��Ù
```

After searching for what each byte in a 12-byte string is, I was able to sort each character and see what the code actually consisted of, 4 extended characters and 8 printable/non-printable characters, you can check [`https://www.rapidtables.com/code/text/ascii-table.html`](https://www.rapidtables.com/code/text/ascii-table.html) to know more about those type of characters.

- Extended:

    ```markdown
    0x84 0xd3 0xc5 0xd9
    ```

- Printable/Non-Printable:

    ```markdown
    0x79 0x48 0x1b 0x27 0x1d 0x33 0x16 0x1d
    ```

Doing this over and over again will take a lot of time, so I coded this function that automates the work, feel free to use it:

```python
import re, base64

def sorting(code):
    list = [ord(chr(eval(j))) for j in ['0x'+ i for i in re.findall('..', base64.b64decode(code).hex())]]
    ex = []
    no = []
    for i in list:
        if i >= 0 and i <= 127:
            no.append(i)
        elif i >= 128 and i <= 255:
            ex.append(i)
    print(f"Extended: {' '.join(map(hex, ex))}")
    print(f"Normal: {' '.join(map(hex, no))}")
    print(f"Extended: {len(ex)}, Normal: {len(no)}")
```

## Finding a Pattern:

In order to find a pattern, I used the function above to sort different valid codes, and the result I got is:

```php
Extended: 0x8e 0xf0 0x8f 0xcb 0xe0 0xba 0xe3
Normal: 0x5f 0x2d 0x59 0x5e 0x4a
Extended: 7, Normal: 5

Extended: 0xc2 0xeb 0xe1 0xe1
Normal: 0x62 0x75 0x70 0x1c 0x40 0x37 0x77 0x14    
Extended: 4, Normal: 8

Extended: 0xac 0xb0 0x9b
Normal: 0x28 0x72 0x5c 0x30 0x4 0x75 0x72 0x1c 0x6c
Extended: 3, Normal: 9

Extended: 0xbb 0xa1 0xf9 0x96 0xf5
Normal: 0x71 0x72 0x1d 0x49 0x20 0x1 0x14
Extended: 5, Normal: 7

Extended: 0xbf 0x96 0xf2 0xb3 0xb0 0x9d 0x8a       
Normal: 0x3b 0x4 0x5b 0x4c 0x5c
Extended: 7, Normal: 5

Extended: 0xd0 0xf1 0x91 0xa9
Normal: 0x65 0x5b 0x17 0x6a 0x1d 0x50 0x70 0x3d    
Extended: 4, Normal: 8
```

From this I was able to know a few rules that must be followed in creating the code:

- Extended characters can be lower or higher than normal (printable / non-printable) characters.
- There are no duplicate characters.
- There is a pattern with 3,4,5,7,8,9.

Looking at the numbers we can see a pattern, if we choose 3 extended characters from the other side, we'll have a 9 normal characters, it's something like [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher), and to simplify it:

![image](https://user-images.githubusercontent.com/48088579/133827790-e5ff9ede-ad38-4d47-9e0b-9c819b484a2f.png)


Putting everything together, we can create a function that generates valid instructions for our code:

```python
import random

_map = [3, 4, 5, 7, 8, 9]

def generate_map():
    e = random.choice(_map)
    if e >= 3 and e <= 5:
        n = _map[::-1][0:3][_map[0:3].index(e)]
    else:
        n = _map[0:3][_map[::-1][0:3].index(e)]
    return {"Extended": e, "Normal": n}
```
An example:
```python
PS C:\Users\ayman\Desktop\discord-theory> python .\generate_map.py
{'Extended': 5, 'Normal': 7}
PS C:\Users\ayman\Desktop\discord-theory> 
```
Note that I've seen some 24-length nitro codes, but I'm assuming you can just find the right map to generate this type of codes.
