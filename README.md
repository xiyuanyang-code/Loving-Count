# Loving Count

## Usage

```bash
git clone git@github.com:xiyuanyang-code/Loving-Count.git
cd Loving-Count
```

Then use the command below:

```bash
# adding a score
# ! double quoted is necessary
python src/main.py "add {user} {number}"

# show score
python src/main.py "ls"
```

- If you want to add 1 point for user: xiaoyuan, you can type: `python src/main.py "add xiaoyuan 1"`.

- If you want to deduct 3 points for user: yanyan, you can type: `python src/main.py "add yanyan -3"`.

- If you want to see the current score, you can type: `python src/main.py "ls"`.

- If you want to see some funny eggs here, you can read the code and find it by yourself :).

## Todo List

- Add history module.

- Add automation by using Feishu Bot.