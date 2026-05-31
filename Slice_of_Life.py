from book import Book

class slice_of_Life(Book): # 클래스명 공백/특수문자 지양
    def __init__(self, name, ISBN, rent_num=2):
        super().__init__(name, ISBN, "일상(코미디)", rent_num)

    def read(self):
        print(f"[{self.name}] 편안하게 웃으며 일상의 소소함을 즐깁니다.")
        
    def provide_preview(self, hero=None, heroin=None):
        if hero:
            print(f"[{hero}의] 편안하고 소소한 일상 이야기! (ISBN: {self.ISBN})")
        elif heroin:
            print(f"주인공은 나다! [주인공 {heroin}의] 왁자지껄 코미디! (ISBN: {self.ISBN})")
        else:
            super().provide_preview(hero, heroin)