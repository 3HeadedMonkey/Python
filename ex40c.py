class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song([ "Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bullets_on_parade = Song([  "They rall around tha family",
                            "With pockets full of shells"])

monitoring_bad_habits = Song(["I keep taling to myself",
                                "Songs my authors that I barely know",
                                "'Portugal. Da man'? What the hell is ",
                                "Even that name"])

happy_bday.sing_me_a_song()

bullets_on_parade.sing_me_a_song()

monitoring_bad_habits.sing_me_a_song()

 
