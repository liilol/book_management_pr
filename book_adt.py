from abc import ABC, abstractmethod

class BookADT(ABC):
    """Person의 Abstract Data Type (ADT) specification"""

    @property
    @abstractmethod
    def name(self):
        """책 이름에 접근하는 추상 프로퍼티"""
        pass

    @property
    @abstractmethod
    def ISBN(self):
        """책 ISBN에 접근하는 추상 프로퍼티"""
        pass
    
    @property
    @abstractmethod
    def genre(self):
        """책 장르에 접근하는 추상 프로퍼티"""
        pass
    
    @property
    @abstractmethod
    def rent_num(self):
        """책 장르에 접근하는 추상 프로퍼티"""
        pass
    

    @abstractmethod
    def introduce(self):
        """객체의 상태(이름, ISBN, 대여수)를 외부에 알리는 연산"""
        pass

    @abstractmethod
    def rantal(self, have):
        """객체의 대출 수를 증가시키는 연산"""
        pass 

    @abstractmethod
    def read(self):
        """객체의 특성에 맞게 읽는 동작을 수행하는 연산"""
        pass