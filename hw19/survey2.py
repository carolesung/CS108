#!/usr/bin/python3

# File: survey.py
# Date: Mar 28 2018
# Name: Carole (Chia Jung) Sung
# Description: A Python web application that will generate a HTML form.

import time
import cgi
import cgitb; cgitb.enable()
import smtplib


print("Content-Type: text/html")
print()

######################
def doHTMLHead(title):
    """HTML headers"""
    print("""
<html>
<body>
<h1>%s</h1>

<p>
""" % title)

#####################
def doHTMLTail():
    """HTML tags"""
    print("""
<p>
This page was generated at %s.
</body>
</html>"""%time.ctime())
    
#######################
def printSurveyForm():
    """Actual code that displays HTML page."""


    print("""
<form method="post":>

Welcome to our survey! Please take a moment to fill out the following questions:
<p>
<table style="width:80%">
	<tr>
		<td><b>Your name (optional):</b></td>
		<td><input type="text" name="name"></td>
	</tr>
	<tr>
		<td><b>Hometown:</b></td>
		<td><input type="text" name="hometown"></td>
	</tr>
	<tr>
		<td><b>State:</b></td>
		<td><select name="state">
				<option value="AL">Alabama</option>
				<option value="AK">Alaska</option>
				<option value="AZ">Arizona</option>
				<option value="AR">Arkansas</option>
				<option value="CA">California</option>
				<option value="CO">Colorado</option>
				<option value="CT">Connecticut</option>
				<option value="DE">Delaware</option>
				<option value="DC">District Of Columbia</option>
				<option value="FL">Florida</option>
				<option value="GA">Georgia</option>
				<option value="HI">Hawaii</option>
				<option value="ID">Idaho</option>
				<option value="IL">Illinois</option>
				<option value="IN">Indiana</option>
				<option value="IA">Iowa</option>
				<option value="KS">Kansas</option>
				<option value="KY">Kentucky</option>
				<option value="LA">Louisiana</option>
				<option value="ME">Maine</option>
				<option value="MD">Maryland</option>
				<option value="MA">Massachusetts</option>
				<option value="MI">Michigan</option>
				<option value="MN">Minnesota</option>
				<option value="MS">Mississippi</option>
				<option value="MO">Missouri</option>
				<option value="MT">Montana</option>
				<option value="NE">Nebraska</option>
				<option value="NV">Nevada</option>
				<option value="NH">New Hampshire</option>
				<option value="NJ">New Jersey</option>
				<option value="NM">New Mexico</option>
				<option value="NY">New York</option>
				<option value="NC">North Carolina</option>
				<option value="ND">North Dakota</option>
				<option value="OH">Ohio</option>
				<option value="OK">Oklahoma</option>
				<option value="OR">Oregon</option>
				<option value="PA">Pennsylvania</option>
				<option value="RI">Rhode Island</option>
				<option value="SC">South Carolina</option>
				<option value="SD">South Dakota</option>
				<option value="TN">Tennessee</option>
				<option value="TX">Texas</option>
				<option value="UT">Utah</option>
				<option value="VT">Vermont</option>
				<option value="VA">Virginia</option>
				<option value="WA">Washington</option>
				<option value="WV">West Virginia</option>
				<option value="WI">Wisconsin</option>
				<option value="WY">Wyoming</option>	
				<option value="Other">US Outlying Territories</option>
			</select>
			</td>

	</tr>
	<tr></tr>
	<tr>
		<td><b>What is your age group?</b></td>
		<td><input type="radio" name="age" value="under 20"> Under 20<br>
		<input type="radio" name="age" value="21-30"> 21-30<br>
		<input type="radio" name="age" value="31-40"> 31-40<br>
		<input type="radio" name="age" value="41-50"> 41-50<br>
		<input type="radio" name="age" value="over 50"> Over 50</td>
	</tr>
	<tr></tr>
	<tr>
		<td><b>How many miles do you run per week?</b></td>
		<td><input type="radio" name="miles" value="fewer than 10"> Fewer than 10<br>
		<input type="radio" name="miles" value="11-20"> 11-20<br>
		<input type="radio" name="miles" value="21-30"> 21-30<br>
		<input type="radio" name="miles" value="over 30"> Over 30</td><br>
	</tr>
	<tr></tr>
	<tr>
		<td><b>Which of the following events have you run in the last 12 months? (Select all that apply)</b></td>
		<td><input type="checkbox" name="events" value="5km"> 5km<br>
		<input type="checkbox" name="events" value = "10km"> 10km<br>
		<input type="checkbox" name="events" value = "1/2 marathon"> 1/2 marathon<br>
		<input type="checkbox" name="events" value = "50km"> 50km<br>
		<input type="text" name="events"> Other</td>
		
	</tr>
	<tr></tr>
	<tr>
		<td><b>Which of the following events do you prefer? (Select all that apply)</b></td>
		<td><input type="checkbox" name="preferredevents" value="5km"> 5km<br>
		<input type="checkbox" name="preferredevents" value = "10km"> 10km<br>
		<input type="checkbox" name="preferredevents" value = "1/2 marathon"> 1/2 marathon<br>
		<input type="checkbox" name="preferredevents" value = "50km"> 50km<br>
		<input type="text" name="preferredevents"> Other</td></td>
		
	</tr>
	<tr></tr>
	<tr>
		<td><b>What topics would you like to see discussed in our blog?</b></td>
		<td><textarea name = "othercomments" rows="4" cols = "50"></textarea></td>
	</tr>
	<tr></tr>

</table>
	<input type="hidden" name="mailto" value="carole07@bu.edu">
	<input type="submit" name="Submit">
</form>""")
    
####################
    
def printConfirmationPage(name,hometown,state,age,miles,events,preferredevents,other):
    """Displays a summary.confirmation to the user as a webpage"""
    
    print("Name:",name,"<br>")
    print("Hometown:",hometown,"<br>")
    print("State:",state,"<br>")
    print("Age Group:",age,"<br>")
    print("Miles run per week:",miles,"<br>")
    print("Events run in the last 12 months:",events,"<br>")
    print("Events preferred:",preferredevents,"<br>")
    print("Additional comments:",other)
    print("""
<form>
    <input type="submit" value = "Start Over">
</form>""")
    
###################
def sendConfirmationEmail(sender,recipient,msg):
    """ Connect up to the SMTP server and send the message from the sender to the recipient
"""

    smtp = smtplib.SMTP()

    smtp.connect("acs-smtp.bu.edu",25)
    r = smtp.helo("USERNAME")
    print("Connected to the SMTP server.")

    r = smtp.sendmail(sender, recipient, msg)
    print("Email was sent to %s" %recipient)

    smtp.quit()
    print("Disconnected from SMTP server")   
    
#############
if __name__ == "__main__": 
    form = cgi.FieldStorage()

    doHTMLHead("A quick survey...")
    if "hometown" in form and "state" in form and "age" in form and "miles" in form and "events" in form and "preferredevents" in form and "othercomments" in form: 
        hometown = form["hometown"].value
        state = form["state"].value
        age = form["age"].value
        miles = form["miles"].value
        events = form.getlist("events")
        preferredevents = form.getlist("preferredevents")
        othercomments = form["othercomments"].value
        if "name" in form:
            n = form["name"].value
            printConfirmationPage(n,hometown,state,age,miles,events,preferredevents,othercomments)
            msg = n+hometown+state+age+miles+str(events)+str(preferredevents)+othercomments
        else:
            printConfirmationPage("N/A",hometown,state,age,miles,events,preferredevents,othercomments)
            msg = hometown + state +age+ miles+str(events)+str(preferredevents)+othercomments
        
        sendConfirmationEmail("carole07@bu.edu","carole07@bu.edu",msg)
    else:
        printSurveyForm()
    
    doHTMLTail()
    
