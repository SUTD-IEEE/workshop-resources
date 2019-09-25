<Kivy Workshop 2>:

* Topics covered:
    - Basic widgets
        @ Button
        @ Label
        @ TextInput
        @ canvas
        @ Image & AsyncImage

* All the answers for the activities in the slides can be found in this folder!

* Revisit our lesson slide here: "https://docs.google.com/presentation/d/1w9VClXwsn2ZAcuNcnGYzkiUq_cAte6xNaarOhlpzpog/edit?usp=sharing"

* Kivy cheatsheet (updated along with the workshop) can be found here: "https://drive.google.com/open?id=1snMi0Knj8DfZujRDCKw51qrulriz9SmPfpJZdB8vb_o"


#######################################################################################################################################################


<Add color code and auto-fill for your .kv file in PyCharm>

1. Find "PyCharm_kv_completion.jar" in "Kivy Workshop 1" folder. (just go to the parent folder and go to "Kivy_Workshop_1")
2. Open PyCharm. Under "File" -> "Import Settings..."
3. Select this .jar file
4. Click "OK" all the way and restart PyCharm


#######################################################################################################################################################


<Solution to PyCharm cannot run kivy on some Windows>

Follow the instruction here to see if it works!
https://github.com/kivy/kivy/wiki/Setting-Up-Kivy-with-various-popular-IDE's

And a post on Reddit here for reference:
https://www.reddit.com/r/kivy/comments/8abti3/difficulty_with_initial_set_up/

Install kivy based on official documentation on your system, then in PyCharm create a new interpreter environment in the Project setting --
project interpreter -- gear button -- "add" -- "system inpterpreter" -- select python 3+ interpreter -- click ok

You should see kivy packages appear in the package list. If not, click "+" sign at the side of the package list -- search "kivy" -- install and apply

If still cannot, have to Goolge or bring the issue up to IEEE Family chat!

#######################################################################################################################################################

*** Always add the empty "__init__.py" file under the directory which contains they .py file with classes you want to refer to in another .py file. Simply from <python_file_name> import <class_name> will create the reference!


#######################################################################################################################################################

Join our Telegram Chat for more resources and materials!

"https://t.me/joinchat/Im0hDFEzJX4byuTGlP4HQQ"