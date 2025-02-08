from bot import Bot

class MyBot(Bot):
    def run(self):
        # Call start() without any additional parameters.
        self.start()
        self.idle()
        self.stop()

if __name__ == "__main__":
    MyBot().run()
