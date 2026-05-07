# rbr-bonus

A Python script that automatically collects your timed bonus in [Rocket Bot Royale](https://rocketbotroyale.winterpixel.io/) using the [`rbrapi`](https://pypi.org/project/rbrapi/) library. Runs on a schedule (github actions) so you basically never miss a bonus

## How It Works

The script logs into your Rocket Bot Royale account using credentials stored as environment variables, then attempts to collect the timed bonus. 

## Setup 

### 1. Clone the repository

```bash
git clone https://github.com/TheTwixBar/rbr-bonus.git
cd rbr-bonus
```

### 2. Install dependencies

```bash
pip install rbrapi
```

### 3. Set environment variables

The script reads your credentials from environment variables:

| Variable | Description |
|---|---|
| `RBR_EMAIL` | Your Rocket Bot Royale account email |
| `RBR_PASSWORD` | Your Rocket Bot Royale account password |

For local use:

```bash
export RBR_EMAIL="your@email.com"
export RBR_PASSWORD="yourpassword"
```

### 4. Run the script

```bash
python collect_bonus.py
```

## GitHub Actions (Automated)

This repo includes a GitHub Actions workflow that runs the script on a schedule automatically.

To use it with your own fork:

1. Fork this repository
2. Go to **Settings → Secrets and variables → Actions**
3. Add two repository secrets: `RBR_EMAIL` and `RBR_PASSWORD`: it has to be exactly that name!
4. The workflow will handle the rest

## Dependencies

- Python 3.x
- [`rbrapi`](https://pypi.org/project/rbrapi/)

## License

do whatever you want with it. no attribution needed. 
