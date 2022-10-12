from curses.ascii import islower
from dataclasses import dataclass
from attr import field

from more_itertools import ilen


@dataclass
class KonohaPhrase:
    phrase: str

    def __post_init__(self):
        self._uppercase_count = 0
        self._lowercase_count = 0
        self._numeric_count = 0
        self._space_count = 0
        self._other_count = 0

        for c in self.phrase:
            if c.isupper():
                self._uppercase_count += 1
            elif c.islower():
                self._lowercase_count += 1
            elif c.isnumeric():
                self._numeric_count += 1
            elif c.isspace():
                self._space_count += 1
            else:
                self._other_count += 1


    def uppercase_count(self):
        return self._uppercase_count

    def lowercase_count(self):
        return self._lowercase_count

    def numeric_count(self):
        return self._numeric_count

    def space_count(self):
        return self._space_count

    def other_count(self):
        return self._other_count

    def konoha_count(self):
        return self.phrase.lower().count('konoha')

    def treat_phrase(self):
        return ''.join(c for c in self.phrase if (c.isalnum() or c.isspace()))