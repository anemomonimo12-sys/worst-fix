# Worst Fix Ever: Funniest Commit Message

Entry for the make.fun competition
`u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722` ($2).

The program writes one line — a commit message for a bug fix that made
everything worse — to `/output/entry.txt`.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## Gate

`main.py` validates the line before writing it: UTF-8, a single line,
not only whitespace, 1–100 characters.
