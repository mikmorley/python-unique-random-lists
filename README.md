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