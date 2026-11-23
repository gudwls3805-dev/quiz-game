class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self):
        print(self.question)
        for i in range(len(self.choices)):
            print(f"{i + 1}. {self.choices[i]}")

    def is_correct(self, user_answer):
        return user_answer == self.answer




while True:
    print("========================================")
    print("         🎯 나만의 퀴즈 게임 🎯")
    print("========================================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("========================================")

    choice = input("선택: ").strip()

    if choice == "1":
        print("퀴즈 풀기 (준비 중)")
    elif choice == "2":
        print("퀴즈 추가 (준비 중)")
    elif choice == "3":
        print("퀴즈 목록 (준비 중)")
    elif choice == "4":
        print("점수 확인 (준비 중)")
    elif choice == "5":
        print("종료합니다")
        break
    else:
        print("⚠️ 잘못된 입력입니다. 1-5 사이 숫자를 입력하세요.")