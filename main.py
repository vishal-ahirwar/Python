
class User:
    def __init__(self, Id, UserName, Password):
        self.ID = Id
        self.USERNAME = UserName
        self.PASSWORD = Password
        self.Followers = 0
        self.Following = 0

    def ShowProfile(self):
        print(f"\nAbout {self.USERNAME} : ")
        print(
            f"User Name : {self.USERNAME}\nID : {self.ID}\nPassword : {self.PASSWORD}\nFollowers : {self.Followers}\nFollowing : {self.Following}")

    def Follow(self, User):
        self.Followers += 1
        User.Following += 1


VishalX = User("0001XID", "VishalX@0001XID", "MyPassword0001")
Rohan = User("0002XID", "Rohan@2XID", "Roahnpwd12")

VishalX.ShowProfile()
Rohan.ShowProfile()
for _ in range(0,10):
    VishalX.Follow(Rohan)
    Rohan.Follow(VishalX)

VishalX.ShowProfile()
Rohan.ShowProfile()

input("Press Any Key to Continue...")
