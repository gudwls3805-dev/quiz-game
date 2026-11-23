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


quizzes = [
    Quiz("영화 '기생충'의 감독은?", ["박찬욱", "봉준호", "김기덕", "이창동"], 2),
    Quiz("영화 '올드보이'에서 주인공이 갇혀 지낸 기간은?", ["5년", "10년", "15년", "20년"], 3),
    Quiz("영화 '극한직업'에서 형사들이 위장 창업한 가게는?", ["피자집", "치킨집", "중국집", "분식집"], 2),
    Quiz("영화 '베테랑'에서 악역 조태오를 연기한 배우는?", ["유아인", "강동원", "조승우", "정우성"], 1),
    Quiz("영화 '범죄도시'에서 마석도 형사를 연기한 배우는?", ["하정우", "김우빈", "이정재", "마동석"], 4),
]


def play_quiz(quizzes):
    score = 0

    for quiz in quizzes:
        quiz.show()
        user_input = input("정답 입력: ").strip()

        if user_input not in ["1", "2", "3", "4"]:
            print("⚠️ 1~4 중에 입력하세요. 오답 처리합니다.")
            continue

        user_answer = int(user_input)

        if quiz.is_correct(user_answer):
            print("✅ 정답입니다!")
            score += 1
        else:
            print("❌ 오답입니다.")
        print("-" * 40)

    print(f"🏆 결과: {len(quizzes)}문제 중 {score}문제 정답!")
    return score


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
        play_quiz(quizzes)
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