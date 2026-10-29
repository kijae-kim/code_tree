secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class Secret:
    def __init__(self, secret_code, meeting_point, time):
        self.secret = secret_code
        self.meeting = meeting_point
        self.time = time


secret1 = Secret(secret_code, meeting_point, time)
print("secret code :", secret1.secret)
print("meeting point :", secret1.meeting)
print("time :", secret1.time)