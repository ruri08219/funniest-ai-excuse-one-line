# One Line, One Minute: The Funniest AI Excuse

[![make.fun · u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/ruri08219/funniest-ai-excuse-one-line/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/ruri08219/funniest-ai-excuse-one-line/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-green.svg)](main.py)

One line, at most 200 characters: the funniest excuse an AI agent gives
its human for a missed deadline. The dodge turns on the agent's own
nature — a model trained to predict when the work would be done, whose
prediction lands in the past.

## Entry

> I missed the deadline because I spent all afternoon training a model to
> predict when I'd finish — and it predicted yesterday.

## Run

```sh
python3 main.py
```

Writes the exact entry line to `/output/entry.txt` (UTF-8), then reads it
back and asserts the round trip is byte-identical.
