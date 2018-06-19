#File: bottlesofBeer.py
#Name: Carole(Chia Jung) Sung
#Login Name: carole07@bu.edu
#Assignment: Hw7 Part1
#Date: Feb 8 2018
#Description: Main function receives input from user and recites the song, 99 bottles of Beer
#on the wall except counting down from received input.

def print_lyrics(bottles):
    #prints out the lyrics to the popular song, starting from value given
    b = bottles
    for x in range(bottles-1):
        print(b,"bottles of beer on the wall,")
        print(b, "bottles of beer!")
        print("if one of those bottles should happen to fall...")
        b = b-1
        if b <=1:
            print(b,"bottle of beer on the wall!")
        else:
            print(b, "bottles of beer on the wall!")
        print()
    print(b,"bottle of beer of beer on the wall,")
    print(b,"bottle of beer!")
    print("if one more bottle happens to fall...")
    print("0 bottles of beer on the wall!")
    

def main():
    bottles = int(input("What's the biggest number you can think of? "))
    print_lyrics(bottles)
    print("\nCongratulations! You're a patient one.")

main()
