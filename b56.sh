#!/bin/bash

: '
Does not include
0 (ZERO)
O (CAPITAL OH)
o (LOWERCASE OH)
I (CAPITAL EYE)
l (LOWERCASE EL)
1 (ONE)
'

cat /dev/urandom | tr -dc 'a-km-np-zA-HJ-NP-Z2-9' | fold -w $1 | head -n 1


