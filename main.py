import json   # ← 맨 위에 추가 (JSON 저장/불러오기 도구)


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

    def to_dict(self):                      # ← 새로 추가
        # Quiz 객체를 저장 가능한 dict로 변환
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }


class QuizGame:
    def __init__(self):
        self.quizzes = [
            Quiz("영화 '기생충'의 감독은?", ["박찬욱", "봉준호", "김기덕", "이창동"], 2),
            Quiz("영화 '올드보이'에서 주인공이 갇혀 지낸 기간은?", ["5년", "10년", "15년", "20년"], 3),
            Quiz("영화 '극한직업'에서 형사들이 위장 창업한 가게는?", ["피자집", "치킨집", "중국집", "분식집"], 2),
            Quiz("영화 '베테랑'에서 악역 조태오를 연기한 배우는?", ["유아인", "강동원", "조승우", "정우성"], 1),
            Quiz("영화 '범죄도시'에서 마석도 형사를 연기한 배우는?", ["하정우", "김우빈", "이정재", "마동석"], 4),
        ]
        self.best_score = None

    def save(self):                         # ← 새로 추가: 저장
        quiz_list = []
        for q in self.quizzes:
            quiz_list.append(q.to_dict())   # 객체 → dict
        data = {"quizzes": quiz_list, "best_score": self.best_score}
        try:
            with open("state.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except OSError:
            print("⚠️ 저장 중 오류가 발생했습니다.")

    def load(self):                         # ← 새로 추가: 불러오기
        try:
            with open("state.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            new_quizzes = []
            for d in data["quizzes"]:       # dict → 다시 Quiz 객체
                new_quizzes.append(Quiz(d["question"], d["choices"], d["answer"]))
            self.quizzes = new_quizzes
            self.best_score = data["best_score"]
            print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score})")
        except FileNotFoundError:
            print("📄 저장 파일이 없어 기본 퀴즈로 시작합니다.")
        except (json.JSONDecodeError, KeyError):
            print("⚠️ 저장 파일이 손상되어 기본 퀴즈로 복구합니다.")

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
        self.save()                         # ← 추가: 점수 저장

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
        self.save()                         # ← 추가: 추가 후 저장

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
        self.load()                         # ← 추가: 시작할 때 불러오기
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


game = QuizGame()
game.run()