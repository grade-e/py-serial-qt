# main.py - 메인 실행 파일
# Person 클래스를 사용하여 동작을 실행합니다.

from src.my_module import Person  # my_class.py에서 Person 클래스를 임포트

# 이 파일을 직접 실행했을 때만 아래 코드가 동작하도록 함
if __name__ == "__main__":
    # Person 객체 생성 및 사용 예시
    person = Person("Alice", 30)             # 이름이 "Alice", 나이 30인 Person 인스턴스 생성
    print(person.hello())                    # 인사 메서드 호출 결과 출력 -> "Hello, my name is Alice."
    print(f"현재 나이: {person.age}")          # 현재 나이 출력 -> "현재 나이: 30"
    
    person.have_birthday()                   # 생일이 지나 한 살 증가
    print(f"새로운 나이: {person.age}")       # 증가된 나이 출력 -> "새로운 나이: 31"