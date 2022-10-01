class Regina:
    def __init__(self, brown_hair, brown_eyes,loves_soon, work):
        self.brown_hair = brown_eyes
        self.brown_eyes = brown_eyes
        self.love_soon = loves_soon
        self.work = work

    def mother_hobby(self, read):
        return f"Love read - {read}"


    def __str__(self):
        return f"brown hair - {self.brown_hair}\n" \
               f"brown eyes - {self.brown_eyes}\n" \
               f"love soon - {self.love_soon}\n" \
               f"work - {self.work}"
mama = Regina(brown_hair=True, brown_eyes=True, loves_soon="TAMIR,IMRAN", work=True)
print(mama.mother_hobby("books"))
print(mama)

class Imran(Regina):

    def __init__(self, brown_hair, brown_eyes, loves_soon, work,sport):
        super().__init__(brown_hair, brown_eyes, loves_soon, work)
        self.sport = sport

    def imran_hobby(selfself, tv):
            return f"love tv show - {tv}"
    def __str__(self):

      return super(Imran, self).__str__()+f"\nSport - {self.sport}"



imran = Imran(brown_hair=True, brown_eyes=True, loves_soon="Imran don't have children", work=False,
              sport="Thai Boxing")

print(imran.mother_hobby("books"))
print(imran.imran_hobby("watch TV"))
print(imran)

class Said(Imran):
    def __init__(self, brown_hair, brown_eyes, loves_soon, work, sport,height):
        super().__init__(brown_hair, brown_eyes, loves_soon, work, sport)
        self.height = height
    def __str__(self):
        return super(Said, self).__str__()+f"\nheight - {self.height}"

said = Said(brown_hair=False, brown_eyes=True, loves_soon="don't soon", work=False,
            sport="Karate",height=1.90)
print(said.mother_hobby("books"))
print(said.imran_hobby("watch Tv"))
print(said)


