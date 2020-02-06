# Bash script that will generate a random base56 string.

## Why would I need this?

If you need to generate random strings from the command line and you need to avoid ambiguous characters like:

```
0 (ZERO)
O (CAPITAL OH)
o (LOWERCASE OH)
I (CAPITAL EYE)
l (LOWERCASE EL)
1 (ONE)
```

## Usage:

```
bash b56.sh <#> 
```

Example:

```
bash b56.sh 12
xbBTpAb5MMF7
```
