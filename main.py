from Shojo import shojo
from Shonen import shonen
from Fantasy import fantasy
from Slice_of_Life import slice_of_Life
 
 
if __name__ == "__main__":
    # 인스턴스 생성
    p1 = shojo("너에게 닿기를", "979-114", 5)
    p2 = shonen("이니셜 D", "979-113", 3)
    p3 = fantasy("이 멋진 세계에 축복을!", "978-892", 10)
    p4 = slice_of_Life("유루캠프", "978-483", 2)
 
    books = [p1, p2, p3, p4]
    print("--- 1. 도서 기본 정보 및 읽기 테스트 ---")
    for b in books:
        b.introduce()  # 공통 정보 출력
        b.read()       # 장르별로 다르게 오버라이딩된 기능 실행
        print("-" * 30)
        
    print("--- 2. 책 프리뷰 ---")
    for c in books:
        c.provide_preview()
 
    print("\n--- 3. 주인공 프리뷰 ---")
    p1.provide_preview(hero="카제하야 쇼타") 
    p1.provide_preview(hero="카제하야 쇼타", heroin="쿠로누마 사와코")
    print("--")   
    p2.provide_preview(hero="후지와라 분타")
    p1.provide_preview(hero="후지와라 분타", heroin="모기 나츠키")    
    print("---")
    p3.provide_preview(hero="카즈마")    
    p1.provide_preview(hero="카즈마", heroin="아쿠아")    
    print("---")
    
    p4.provide_preview(hero="나데시코")
    p1.provide_preview(hero="나데시코", heroin="린")    
    print("---")       
 
    print("\n--- 4. 히로인 프리뷰 ---")
    p1.provide_preview(heroin="쿠로누마 사와코")   
    p2.provide_preview(heroin="모기 나츠키")    
    p3.provide_preview(heroin="아쿠아")      
    p4.provide_preview(heroin="린")      
