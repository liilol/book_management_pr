from book import Book

class shonen(Book): # 클래스명 대문자 권장
    def __init__(self, name, ISBN, rent_num=2): # self 추가
        super().__init__(name, ISBN, "소년", rent_num)

    def read(self):
        print(f"[{self.name}] 뜨거운 열정과 액션에 몰입하여 읽습니다.")

    def provide_preview(self, hero=None, heroin=None):
        if heroin and hero:
            print(f"[{hero}와 {heroin}의] 액션, 모험 위주의 활극! (ISBN: {self.ISBN})")
        else:
            super().provide_preview(hero, heroin)
