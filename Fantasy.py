from book import Book

class fantasy(Book):
    def __init__(self, name, ISBN, rent_num=2):
        super().__init__(name, ISBN, "판타지(이세계)", rent_num)

    def read(self):
        print(f"[{self.name}] 거대한 세계관과 마법의 세계에 빠져듭니다.")

    def provide_preview(self, hero=None, heroin=None):
        if heroin and hero:
            print(f"[{hero}와 {heroin}의] 마법과 끝없는 모험의 이야기! (ISBN: {self.ISBN})")
        elif hero:
            print(f"[주인공 {hero}의] 이세계 구원 모험기! (ISBN: {self.ISBN})")
        else:
            super().provide_preview(hero, heroin)
