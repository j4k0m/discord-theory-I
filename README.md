# discord-theory-I
Part1: My attempt to reverse the Discord nitro token generation function.

The Nitro generation tools thing is common in Discord now, but none of the tools actually works, so I decided to take it to the next level, and reverse the actual tokens in hopes of finding a better way of generation.

## Introducation:
If you are not familiar with Discord, nitro is a kind of membership, you pay to get access and do some cool things on Discord, like get a GIF profile picture or upload large size photos and videos, and in order to get it you must either buy it directly or having someone offer it to you, in the second case it would be something like this:
```
https://discord.gift/hNN5SBsnHTPFFh3Z
```
The Discord Gift URL followed by a 16-length code will redirect you to the claim page.

## First look:
At first sight it looks like Base64 encoded, using Burp Suite Decoder we will be able to get this result:
```
00000000	84	d3	79	48	1b	27	1d	33	c5	16	1d	d9	--	--	--	--	ÓyH'3ÅÙ
```
After searching for what each byte in a 12-byte string is, I was able to sort each character and see what the code actually consisted of, 4 extended characters and 8 printable/non-printable characters, you can check https://www.rapidtables.com/code/text/ascii-table.html to know more about those type of characters.
- Extanded:
```
0x84 0xd3 0xc5 0xd9
```
- Printable/Non-Printable:
```
0x79 0x48 0x1b 0x27 0x1d 0x33 0x16 0x1d
```
