import asyncio
from bot import Bot
from pyrogram import idle  # import the idle helper

class MyBot(Bot):
    async def run_async(self):
        # Start the bot (await the coroutine)
        await self.start()
        print("Bot is running. Press Ctrl+C to stop.")
        # Wait until you stop the bot (idle() is a helper function that blocks until interrupted)
        await idle()
        # Stop the bot gracefully
        await self.stop()

if __name__ == "__main__":
    asyncio.run(MyBot().run_async())
