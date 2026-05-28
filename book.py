from book_adt import BookADT


class Book(BookADT):
    def __init__(self, name, ISBN, genre, rent_num = 0):
        """생성자: Book 객체의 초기 상태(데이터)를 설정"""
        self.__name = name
        self.__ISBN = ISBN
        self.__genre = genre
        self._rent_num = rent_num

    # --- Properties (Getters) ---
    @property
    def name(self): return self.__name

    @property
    def ISBN(self): return self.__ISBN

    @property
    def genre(self): return self.__genre

    @property
    def rent_num(self): return self._rent_num

    # --- Properties (Setters) ---
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            print(f"[에러] 유효하지 않은 이름입니다: {value}")
        else:
            self.__name = value

    @ISBN.setter
    def ISBN(self, value):
        print(f"[경고] {self.name}의 ISBN {self.ISBN}에서 {value}(으)로 변경합니다.")
        self.__ISBN = value

    @genre.setter
    def genre(self, value):
        if not isinstance(value, str) or len(value) == 0:
            print(f"[에러] 유효하지 않은 장르입니다: {value}")
        else:
            self.__genre = value

    @rent_num.setter
    def rent_num(self, value):
        if value < 0:
            self._rent_num = 0
            print(f"[{self.name}] 의 현제 귄수가 부족하여 대출할수 없습니다.")
        else:
            self._rent_num = value

    def introduce(self):
        print(f"- Name: {self.name}({self.genre}), ISBN: {self.ISBN}, 도서관 보유수: {self._rent_num}")

    def rentaling(self, have = 0):
        self.__rent_num += have
        print(f"도서관에서 {have}만큼 구메하여 {self.name} 책의 총 {self.rent_num}권이 되었습니다.")

    def rantal(self, amount=1):
        """대출 처리: 보유 권수를 줄임"""
        self.rent_num -= amount
    def read(self):
        """기본 읽기 동작"""
        print(f"'{self.name}' 도서를 읽기 시작합니다.")

    # [오버로딩 (Overloading) 구현]
    # 매개변수(weapon, spell)의 입력 여부에 따라 내부에서 분기 처리
    
    def provide_preview(self, hero = None, heroin = None):
        if hero and heroin:
            print(f"[{hero}와 {heroin}의] '{self.genre}' 이야기! (ISBN: {self.ISBN})")
        elif hero:
            print(f"[{hero}의] '{self.genre}' 이야기! (ISBN: {self.ISBN})")
        else:
            print(f"[아무도 모르는...] '{self.genre}' 이야기! (ISBN: {self.ISBN})")