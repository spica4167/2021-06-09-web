# 돈 입력 함수
def input_money():
    return int(input("돈을 입력: "))

# 돈 뻥티기 함수
def money_pung(m):
    return m * 5
            
# 이메일 패스워드 체크
# 만약 이메일 'a@a.com'이고 패스워드가 '123'이면 로그인 성공, 아니면 가입된 이메일이 없거나 패스워드가 다릅니다.
def logincheck(email, pswd):
    if email == 'a@a.com' and pswd == '123':
        return "로그인 성공"
    else:
        return "가입된 이메일이 없거나 패스워드가 다릅니다."

