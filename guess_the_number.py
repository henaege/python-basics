import random

def play():
  target_number = random.randint(1, 10)
  player_guess = 0
  guess_count = 5
  print "I am thinking of a number between 1 and 10."
  while player_guess != target_number and guess_count > 0:
      print "You have {} guesses left.".format(guess_count)
      player_guess = input("What's the number? ")
      if int(player_guess) < target_number:
          print "{} is too low.".format(player_guess)
      elif int(player_guess) > target_number:
          print "{} is too high.".format(player_guess)
      else:
          print "Yes! You Win!"
      guess_count -= 1
      if guess_count == 0:
        print "Sorry, you did not successfully guess the number :-("

# def play_again():
#     replay = raw_input("Would you like to play again (Y or N)? ")
#     if replay == "y":
#       play()
#     elif replay == "n":
#       print "Bye!"
#     else:
#       print "Please type {} or {} to continue.".format("Y", "N")

play()
# play_again()