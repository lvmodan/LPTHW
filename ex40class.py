#!/usr/bin/env python
# coding=utf-8
class song(object):
    def __init__(self, lyric):
        self.lyric = lyric

    def sing_me_a_song(self):
        for line in self.lyric:
            print line

dog_sing = song(["wang, wang, wang"])
cat_sing = song(['miao, miao, miao'])

dog_sing.sing_me_a_song()
cat_sing.sing_me_a_song()
