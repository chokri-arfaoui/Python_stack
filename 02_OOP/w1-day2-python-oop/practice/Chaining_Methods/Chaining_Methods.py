class User:
    def __init__(self, first_name,last_name,email, age,is_rewards_member ,gold_card_points) :
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_rewards_member=False
        self.gold_card_points = 0

    def display_info(self):
        print(f"my first_name is : = {self.first_name}\nmy last_name is : = {self.last_name}\nmy email is : = {self.email}\nmy age is : = {self.age}\nis_rewards_member: = {self.is_rewards_member}\ngold_card_points : = {self.gold_card_points}")
        return(self)
    
    
    
    def enroll(self):
        if self.is_rewards_member==False:
            print( f" {self.first_name} : welcome you are our new member")
            self.is_rewards_member=True
            self.gold_card_points = 200
        else:
            print(f" {self.first_name} : you are already member ")
        return(self)
        
        
    
    def spend_points(self, amount):
        if self.gold_card_points>=amount:
            self.gold_card_points-=amount 
            print(f"your new gold_card_points is equal to : ={self.gold_card_points}")
        else :
            print("you have no enough points !!")
        return(self)

        
    
alex = User("alex","Joe","alex-1234@gmail.com","34","is_rewards_member","gold_card_points")
Jane = User("Jane","morgan","jane-8534@gmail.com", "25","is_rewards_member","gold_card_points")
Marlin= User("Marlin","Moor","malin-3254@gmail.com","55","is_rewards_member","gold_card_points")

alex.display_info().enroll().spend_points(50).display_info()
print("----------------------------")
Jane.display_info().enroll().spend_points(80).display_info()
print("----------------------------")
Marlin.display_info().enroll().spend_points(40).display_info()