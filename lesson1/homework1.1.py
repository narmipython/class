class Book:
    def __int__(self,color,title,paper,letters,price,author,verb,adverb,painting,questions):
        self.color = color
        self.title = title
        self.paper = paper
        self.letters = letters
        self.price = price
        self.author = author
        self.verb = verb
        self.adverb = adverb
        self.painting = painting
        self.questions = questions
    def __str__(self):
        return f"color-{self.color}\n" \
               f"title-{self.title}\n" \
               f"paper-{self.paper}\n" \
               f"letters-{self.letters}\n" \
               f"price-{self.price}\n" \
               f"author-{self.author}\n" \
               f"verb-{self.verb}\n" \
               f"adverb-{self.adverb}\n" \
               f"painting-{self.painting}\n" \
               f"questions-{self.questions}"

book1 = Book(color"=green",title="Mincraft",paper="A4",letters="small",price="$10"")
book2 = Book(color"=black",title="Mincraft-mobs",paper="A4",letters="Big",price="$160")
book3 = Book(color"=blue",title="Mincraft-servive",paper="A4",letters="Big",price="$159")
book4 = Book(color"=pink",title="Mincraft-blocks",paper="A8",letters="Big",price="$150")
book5 = Book(color"=red",title="Mincraft-swords",paper="A9",letters="Big",price="$150")
book6 = Book(color"=white",title="Mincraft-cheats",paper="A1",letters="Big",price="$150")
book7 = Book(color"=gray",title="Mincraft-paper",paper="A10",letters="Big",price="$150")
book8 = Book(color"=gray and blue",title="Mincraft-hacks",paper="A5",letters="Big",price="$150")
book9 = Book(color"=black and white",title="Mincraft-command blocks",paper="A2",letters="Big",price="$15")
book10 = Book(color"=blue and pink",title="Mincraft-mods",paper="A3",letters="Big",price="$10")
def run(self):
    return f"{self.letters}can be readed in a book"
def change_painting(self):
    return f"{self.letters}can change painting"
print(book1.read)
print(book2.read)
print(book3.read)
print(book4.read)
print(book5.read)
print(book6.read)
print(book7.read)
print(book8.read)
print(book9.read)
print(book10.read)



