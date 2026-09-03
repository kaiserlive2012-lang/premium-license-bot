import bot
import asyncio

if __name__ == "__main__":
    try:
        asyncio.run(bot.main())
    except (KeyboardInterrupt, SystemExit):
        pass
