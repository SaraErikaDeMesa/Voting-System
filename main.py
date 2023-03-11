# take input of names of nominee
nominee1 = input("Enter the name of 1st nominee ")
nominee2 = input("Enter the name of 2nd nominee ")


#initialize vote count to 0
nom1_votes = 0
nom2_votes = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

no_of_voter = len(voter_id)

while True:
    if voter_id == []: #check when voter list id is complete
        print("Voting session is over!")
        if nom1_votes > nom2_votes:
            percent = (nom1_votes/no_of_voter)*100
            print(nominee1, "has won the elecetion with ", percent,"%")
            break
        elif nom2_votes > nom1_votes:
            percent = (nom2_votes/no_of_voter)*100
            print(nominee2, "has won the elecetion with ", percent,"%")
            break
        else:
            print("There is a Tie!")
            break





    voter = int(input("Enter your voter id: "))
    if voter in voter_id:
        print("You are a voter ")
        print(".....................................")
        voter_id.remove(voter) #will remove so that again same voter cant vote
        print("-------------------------------------")
        print("To give vote to ",nominee1, "Press 1 ")
        print("To give vote to ",nominee2, "Press 2 ")
        print("-------------------------------------")
        vote = int(input("Enter your vote: "))
        if vote == 1:
            nom1_votes += 1
            print(nominee1, "Thank you, your vote is counted!")
        elif vote == 2:
            nom2_votes += 1
            print(nominee2, "Thank you, your vote is counted!")
        elif vote > 2:
            print("Error. Try again!")
        else:
            print("You are not a voter OR have already voted")