Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> phoneNumbers = {}
>>> phoneNumbers["Papa John's"]='(617) 247-7120
SyntaxError: EOL while scanning string literal
>>> phoneNumbers["Papa John's"]='(617) 247-7120'
>>> print phoneNUmbers
SyntaxError: Missing parentheses in call to 'print'
>>> print(phoneNumbers)
{"Papa John's": '(617) 247-7120'}
>>> phoneNumbers["T.Anthony's"] = "(617) 734-7708"
>>> print(phoneNumbers)
{"T.Anthony's": '(617) 734-7708', "Papa John's": '(617) 247-7120'}
>>> phoneNumbers["Bertucci's"]="(123) 456-789"
>>> phoneNumbers["University Grill"] = "(617) 247-7120"
>>> print(phoneNumbers)
{"T.Anthony's": '(617) 734-7708', "Bertucci's": '(123) 456-789', 'University Grill': '(617) 247-7120', "Papa John's": '(617) 247-7120'}
>>> phoneNumbers["Papa John's"]= "(234) 567-890"
>>> print(phoneNumbers)
{"T.Anthony's": '(617) 734-7708', "Bertucci's": '(123) 456-789', 'University Grill': '(617) 247-7120', "Papa John's": '(234) 567-890'}
>>> key = "T.Anthony's"
>>> print("too long", key,"=",phoneNumbers[key])
too long T.Anthony's = (617) 734-7708
>>> key = phoneNumbers.keys()
>>> print(key)
dict_keys(["T.Anthony's", "Bertucci's", 'University Grill', "Papa John's"])
>>> key.sort()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    key.sort()
AttributeError: 'dict_keys' object has no attribute 'sort'
>>> key = list(phoneNumbers.keys())
>>> key.sort()
>>> print(key)
["Bertucci's", "Papa John's", "T.Anthony's", 'University Grill']
>>> for k in key:
	print("# for", k, "=", phoneNumbers[key])

	
Traceback (most recent call last):
  File "<pyshell#23>", line 2, in <module>
    print("# for", k, "=", phoneNumbers[key])
TypeError: unhashable type: 'list'
>>> for k in key:
	print("# for", k, "=", phoneNumbers[k])

	
# for Bertucci's = (123) 456-789
# for Papa John's = (234) 567-890
# for T.Anthony's = (617) 734-7708
# for University Grill = (617) 247-7120
>>> del phoneNumbers["University Grill"]
>>> print(phoneNumbers)
{"T.Anthony's": '(617) 734-7708', "Bertucci's": '(123) 456-789', "Papa John's": '(234) 567-890'}
>>> phoneNumbers.has_key("Papa John's")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    phoneNumbers.has_key("Papa John's")
AttributeError: 'dict' object has no attribute 'has_key'
>>> "Papa John's" in phoneNumbers
True
>>> "hello" in phoneNumbers
False
>>> "University Grill" in phoneNumbers
False
>>> 
