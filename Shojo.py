from book import Book

class shojo(Book):
    def __init__(self, name, ISBN, rent_num=2): # self 추가
        super().__init__(name, ISBN, "순정(소녀)", rent_num)

    def read(self): # 추상 메서드 구현
        print(f"[{self.name}] 설레는 마음으로 감정선을 따라 읽습니다.")

    def provide_preview(self, hero=None, heroin=None):
        if heroin and hero:
            print(f"[{hero}와 {heroin}의] 로맨스, 감정 위주의 달달한 러브스토리! (ISBN: {self.ISBN})")
        elif hero:
            print(f"[주인공 {hero}의] 달달한 로맨스 러브스토리! 과연, 히로인은 누굴까! (ISBN: {self.ISBN})")
        else:
            super().provide_preview(hero, heroin) # attack -> provide_preview로 수정