from utils import custom_print, bg_colors
from bot.online.OnlineBot import OnlineBot

def main():
    custom_print("Triggering the bots", bg_colors.OKGREEN)

    online_bot = OnlineBot()

if __name__ == "__main__":
    main()