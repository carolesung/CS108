#!/usr/bin/python3
# File: webcalc.py
# Name: Carole (Chia Jung) Sung
# Description: A python web application with form data

import time
import cgi #Common Gateway Interface
import cgitb; cgitb.enable() #CGI traceback

# We must specify the content type and this must be the very first print statement
print("Content-Type: text/html")
print()

###########################
def doHTMLHead(title):
    print("""
<html>
<body>
<h1>%s</h1>

<p>
""" % title)

#############################
def doHTMLTail():

    print("""
<p>
This page was generated at %s.
</body>
</html> """%time.ctime())

##############################
def printCalculatorForm(firstOperand = "", secondOperand = "", operator = ""):
    """This function will present an input form for the calculator.
    If firstOperand, secondOperand, operator are provided, we can prefill the form.
    Otherwise, the default parameters will "pre-fill" the form with no data."""

    print("""
<form method="post":>
    <b>Enter first operand:</b>
    <input type="text" name="firstOperand" value ="%s"><br>
    <b>Enter second operand:</b>
    <input type="text" name="secondOperand" value="%s"><br>
    <b>Select operation: </b>
    <select name="operator">"""%(firstOperand, secondOperand))

    #We want to make one (and only one) option selected
    if operator == "+":
        print("""
<option value="+" selected>+</option>
<option value="-">-</option>
<option value="/">/</option>
<option value="*">*</option>""")
    elif operator == "-":
        print("""
<option value="+">+</option>
<option value="-" selected>-</option>
<option value="/">/</option>
<option value="*">*</option>""")
    elif operator == "/":
        print("""
<option value="+">+</option>
<option value="-">-</option>
<option value="/" selected>/</option>
<option value="*">*</option>""")
    elif operator == "*":
        print("""
<option value="+">+</option>
<option value="-">-</option>
<option value="/">/</option>
<option value="*" selected>*</option>""")
    else: # if "" is the operator
        print("""
<option value="+">+</option>
<option value="-">-</option>
<option value="/">/</option>
<option value="*">*</option>""")
    print("""</select>
<p>
<input type="submit" value="Calculate!">
</form>""")

## end: def printForm(firstOperand = "", secondOperand = "", operator = "")
    
###################################

def doCalc(firstOperand, secondOperand, operator):
    """
    The doCalc function is going to do the actual math processing.
    Just call it from the __main__ section below, passing in the parameters
    for operands and operators.

    This function can be called with no parameters, or with actual parameters.
    If actual parameters are passed in, it will pre-fill form fields with those values"""

    if operator == "+":
        result = firstOperand + secondOperand
        print("%s plus %s equals %s" %(firstOperand, secondOperand, result))
    elif operator == "-":
        result = firstOperand - secondOperand
        print("%s minus %s equals %s" %(firstOperand, secondOperand, result))
    elif operator == "*":
        result = firstOperand * secondOperand
        print("%s times %s equals %s"%(firstOperand, secondOperand, result))
    elif operator == "/":
        if secondOperand == 0:
            print("Cannot divide by zero, you doofus!")
        else:
            result = float(firstOperand)/secondOperand
            print("%.2f divided by %.2f equals %.2f"% (firstOperand, secondOperand,result))

            if type(firstOperand) == int and type(secondOperand)== int:
                print("<br><i>With integer division...</i>")
                result = firstOperand/secondOperand
                print("%d divided by %d equals %d" %(firstOperand,secondOperand,result))
                remainder = firstOperand % secondOperand
                print("With a remainder of %d"%remainder)
    else:
        print("%s is not a valid operator. You suck." % operator)
    # always show this button, which will send the user back to the start page
    print("""
<form>
    <input type="submit" value="Start Over">
</form>
""")
## end: def doCalc(firstOperand,secondOperand, operator):
    
#########################################################
if __name__ == "__main__":
    
    #access the form data:
    form = cgi.FieldStorage()
    
    doHTMLHead("A quick calculator...")


    if "firstOperand" in form and "secondOperand" in form and "operator" in form:
        #read the form data into python variables:
        firstOperand = form["firstOperand"].value
        secondOperand = form["secondOperand"].value
        operator = form["operator"].value

        #treat operands as numeric:
        firstOperand = int(firstOperand)
        secondOperand = int(secondOperand)
        doCalc(firstOperand, secondOperand, operator)
    else:
        printCalculatorForm()
        
    doHTMLTail()




