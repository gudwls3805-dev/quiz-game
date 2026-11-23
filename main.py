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


def add_quiz(quizzes):
    question = input("문제를 입력하세요: ").strip()
    if question == "":
        print("⚠️ 문제를 입력해야 합니다. 추가를 취소합니다.")
        return

    choices = []                      # 선택지를 담을 빈 리스트
    for i in range(4):                # 4번 반복해서 선택지 4개 받기
        c = input(f"선택지 {i + 1}: ").strip()
        if c == "":
            print("⚠️ 선택지를 입력해야 합니다. 추가를 취소합니다.")
            return
        choices.append(c)             # 리스트 끝에 추가

    answer_input = input("정답 번호 (1-4): ").strip()
    if answer_input not in ["1", "2", "3", "4"]:
        print("⚠️ 정답은 1~4 중에 입력하세요. 추가를 취소합니다.")
        return
    answer = int(answer_input)

    new_quiz = Quiz(question, choices, answer)   # 입력값으로 Quiz 객체 생성
    quizzes.append(new_quiz)                     # 퀴즈 목록에 추가
    print("✅ 퀴즈가 추가되었습니다!")


def show_list(quizzes):
    if len(quizzes) == 0:                 # 퀴즈가 없으면
        print("📭 등록된 퀴즈가 없습니다.")
        return

    print(f"📋 등록된 퀴즈 목록 (총 {len(quizzes)}개)")
    print("-" * 40)
    for i in range(len(quizzes)):
        print(f"[{i + 1}] {quizzes[i].question}")
    print("-" * 40)

best_score = None   # None = "아직 값 없음" (= 아직 안 풂)
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
        score = play_quiz(quizzes)
        if best_score is None or score > best_score:
            best_score = score
            print("🎉 새로운 최고 점수입니다!")
    elif choice == "2":
        add_quiz(quizzes)
    elif choice == "3":
        show_list(quizzes)
    elif choice == "4":
        if best_score is None:
            print("📊 아직 퀴즈를 푼 적이 없습니다.")
        else:
            print(f"🏆 최고 점수: {best_score}문제 정답")
    elif choice == "5":
        print("종료합니다")
        break
    else:
        print("⚠️ 잘못된 입력입니다. 1-5 사이 숫자를 입력하세요.")