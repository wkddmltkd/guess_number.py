import random

def play_game():
    number = random.randint(1, 10)
    attempts = 0
    max_attempts = 5

    print("\n🎮 숫자 맞추기 게임 (1~10)")
    print(f"기회는 {max_attempts}번 입니다!")

    while attempts < max_attempts:
        guess = int(input("숫자 입력: "))
        attempts += 1

        if guess == number:
            print(f"🎉 정답입니다! {attempts}번 만에 맞췄어요!")
            return
        elif guess < number:
            print("⬆ 더 큰 숫자입니다.")
        else:
            print("⬇ 더 작은 숫자입니다.")

    print(f"❌ 실패! 정답은 {number}였습니다.")

while True:
    play_game()
    again = input("다시 하시겠습니까? (y/n): ")

    if again.lower() != 'y':
        print("게임 종료!")
        break
