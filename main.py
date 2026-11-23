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


class QuizGame:
    def __init__(self):
        # 게임이 가진 데이터(속성)
        self.quizzes = [
            Quiz("영화 '기생충'의 감독은?", ["박찬욱", "봉준호", "김기덕", "이창동"], 2),
            Quiz("영화 '올드보이'에서 주인공이 갇혀 지낸 기간은?", ["5년", "10년", "15년", "20년"], 3),
            Quiz("영화 '극한직업'에서 형사들이 위장 창업한 가게는?", ["피자집", "치킨집", "중국집", "분식집"], 2),
            Quiz("영화 '베테랑'에서 악역 조태오를 연기한 배우는?", ["유아인", "강동원", "조승우", "정우성"], 1),
            Quiz("영화 '범죄도시'에서 마석도 형사를 연기한 배우는?", ["하정우", "김우빈", "이정재", "마동석"], 4),
        ]
        self.best_score = None

    def show_menu(self):
        print("========================================")
        print("         🎯 나만의 퀴즈 게임 🎯")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")

    def play_quiz(self):
        score = 0
        for quiz in self.quizzes:
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

        print(f"🏆 결과: {len(self.quizzes)}문제 중 {score}문제 정답!")
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")

    def add_quiz(self):
        question = input("문제를 입력하세요: ").strip()
        if question == "":
            print("⚠️ 문제를 입력해야 합니다. 추가를 취소합니다.")
            return

        choices = []
        for i in range(4):
            c = input(f"선택지 {i + 1}: ").strip()
            if c == "":
                print("⚠️ 선택지를 입력해야 합니다. 추가를 취소합니다.")
                return
            choices.append(c)

        answer_input = input("정답 번호 (1-4): ").strip()
        if answer_input not in ["1", "2", "3", "4"]:
            print("⚠️ 정답은 1~4 중에 입력하세요. 추가를 취소합니다.")
            return
        answer = int(answer_input)

        self.quizzes.append(Quiz(question, choices, answer))
        print("✅ 퀴즈가 추가되었습니다!")

    def show_list(self):
        if len(self.quizzes) == 0:
            print("📭 등록된 퀴즈가 없습니다.")
            return
        print(f"📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)
        for i in range(len(self.quizzes)):
            print(f"[{i + 1}] {self.quizzes[i].question}")
        print("-" * 40)

    def check_score(self):
        if self.best_score is None:
            print("📊 아직 퀴즈를 푼 적이 없습니다.")
        else:
            print(f"🏆 최고 점수: {self.best_score}문제 정답")

    def run(self):
        while True:
            self.show_menu()
            choice = input("선택: ").strip()
            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.show_list()
            elif choice == "4":
                self.check_score()
            elif choice == "5":
                print("종료합니다")
                break
            else:
                print("⚠️ 잘못된 입력입니다. 1-5 사이 숫자를 입력하세요.")


# 프로그램 시작
game = QuizGame()
game.run()