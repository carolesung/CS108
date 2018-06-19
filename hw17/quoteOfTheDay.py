#!/usr/bin/python3

# File: quoteOfTheDay.py
# Name: Carole (Chia Jung) Sung
# Date: Mar 22 2018
# Description: A Python web application that will generate HTML output.
# The output of the program will be a Quote of the Day application where each
# time the page loads, a diff quote and picture will be randomly generated.

import random

quotelst = [["Would I rather be feared or loved? Easy, both. I want people to be afraid of how much they love me."]]
quotelst.append(["I'm not superstitious, but I am a little stitious"])
quotelst.append(["'You miss 100% of the shots you dont take. -Wayne Gretzky'"])
quotelst.append(["Am I a hero? I really can't say, but yes."])
quotelst.append(["The only time I set the bar low is for limbo."])
quotelst.append(["That's what she said!"])
quotelst.append(["I love inside jokes. Love to be a part of one someday."])
quotelst.append(["It's never too early for ice cream."])
quotelst.append(["Webster's Dictionary defines wedding as the fusing of two metals with a hot torch."])
quotelst.append(["If I had a gun with two bullets and I was in a room with Hitler, Bin Laden and Toby, I would shoot Toby twice."])
quotelst.append(["The worst thing about prison was the Dementors."])
quotelst.append(["You should never settle for who you are."])

urllst = [["https://bit.ly/2ubTD4Z"]]
urllst.append(["https://bit.ly/2G3g0Lw"])
urllst.append(["https://bit.ly/2ubNMwz"])
urllst.append(["http://bzfd.it/2fJKzdw"])
urllst.append(["https://bit.ly/2pwDrqf"])

if __name__ == "__main__":
    # HTTP headers
    print("Content-type: text/html")
    print()

    randQuote  = random.randint(0,11)
    randURL = random.randint(0,4)
    
    print("""
<html>
<head>
<title>Quote of the Day</title>
</head>

<body>

<center>
<h1>Quote of the Day</h1>

<p>
<img src="%s", width="450", height="300">
</p>

<p>
<fontsize="6">%s - Michael Scott</font>
</p>
<p>
The Office
</p>

</center>
</body>
</html>""" %(urllst[randURL][0],quotelst[randQuote][0]))







    
    
