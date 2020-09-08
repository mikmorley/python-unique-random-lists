# Python Unique Random List Generator

## Description
Generates lists of unique random (alphanumeric|alpha|numeric) strings from argument defined specifications. Purpose to be used as auxilary unique random string generation, or stand alone unique list generation for data population. Each value generated is unique within the outputted list.

**Author:** Michael Morley (https://michael.morley.cloud)

## Usage

```
python random-lists.py --count <number> --length <number> --uppercase <y/n> --lowercase <y/n> --numbers <y/n>
```

The following arguments must be defined:

- `--count` Total count of unique random strings to be generated.
- `--length` The length of each unique random string.
- `--uppercase` Defines if random string should include Uppercase letters. y/n
- `--lowercase` Defines if random string should include Lowercase letters. y/n
- `--numbers` Defines if random string should include Numbers. y/n

### Examples
Generating a unique random list of 10 x 24 bit **lowercase** alphanumeric strings:

```
~/python-unique-random-lists$ python random-lists.py --count 10 --length 24 --uppercase n --lowercase y --numbers y
uwyrfs1ce1f4iwp5lu96m8s7
h19pmtvoge1266flct1xd5p1
1hjh60equoygr4ph3xqlu4aw
aqrcc4pmppqgowd532582nuu
1s6z3s7dsgof56rykxy0o7sh
02o58m83saq9a2ncvo9ukh0p
uhqtobjndkterrta5h2ruioz
gkztihidjwj8rj4otdp1ziav
jz8vlqbjovukl9qvq7imo01b
k199n3tyaeq3thv5n9t7ap8j
```

Generating a unique random list of 8 x 6 bit **uppercase** alphanumeric strings:

```
~/python-unique-random-lists$ python random-lists.py --count 8 --length 6 --uppercase y --lowercase n --numbers y
KXN87F
8KHU6U
SBEAHW
HD35OA
WQ7FW3
GHBXIE
ZGGG9L
BHH2HS
```

Generating a unique random list of 20 x 32 bit **numbers** strings:

```
~/python-unique-random-lists$ python random-lists.py --count 20 --length 32 --uppercase n --lowercase n --numbers y
27756443649597453186159388159992
91178778433790435326680545156246
42715778602980314223648153053500
87845631721083594656463793559368
76069833316469702128577438159385
69587429152067598743895495399552
51401615291546516164470336363532
85152468444702315784042549317744
22910112646888912342771840087885
94548958570521095958686600846437
25715442940523329524506424504201
36657180595839112860751751268793
06801304647429105852233372906117
28897690558271126424749705873690
69762251779998735189213061326269
15825308953789844208112991618432
16804890659822884943696325175050
02355145364609947747876222501697
15716518520013563691211846308614
52587265736309625531942623281463
```

Generating a **large** unique random list of 10000 x 64 bit alphanumber strings:

```
~/python-unique-random-lists$ python random-lists.py --count 100 --length 64 --uppercase y --lowercase y --numbers y
F3wqh1dhCAd3yaSJ3PtHHZTQUUPgRAA5YFe7U4C36uNSPyqlXwdO6S1LbuRJ2cr9
h3wY92PAcO1XwIG7yNrNijmmqUytcfYWfL8cdxBJnunF1a9esfci6xIcfO6E1oDv
JOuazuaIfpHQ04TwZyIHGH2oIs0Dl1o6dGSChMimemfoHq7qxyYGEXAJ3kI4rvXr
AZUqNStHRYq9nL2wm1rLo0gNGtyWYzKcyNFSLrOmHzwzr21oCIjzogOq9i9RIDYG
[...]
mULXcMIBU2H22WDWeqMZPvBo9modUNNLlmN3q2oWLA224RoKQ8LyKyOJgWs2wFOB
jJP4YTUvveRs9gcTSj4mT35NAb8TbQT4pz7dfYyC4Dteiqd6tpyTQCBk5b0ulHJN
yJS8IY9X7PgVgW9kFzUjs1dJYoQB8GQ3Z1rEzbanskETAdMHWWFXzmEZmFxTMXRD
DVhhICjVuTZxaAgYYyeCfNy6lGtbVZK7Lf1j51nnQdfLWq9GZhGajcvsl2cLoKk2
1OMo5cA5iSwwQklFewdE2qcGWDyDx3hTmsTgNQCYTEyW8yzTqUnUAboqtMCGjjPv
```