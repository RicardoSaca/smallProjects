#py -m webbrowser -n "https://gmail.com"
#py -m webbrowser -t "https://outlook.office.com"
#py -m webbrowser -t "https://canvas.instructure.com/courses/2813620"
#py -m webbrowser -t "https://sakai.providence.edu/"

import webbrowser

webbrowser.open_new_tab("https://gmail.com" )
webbrowser.open_new_tab("https://outlook.office.com")
webbrowser.open_new("https://canvas.instructure.com/courses/2813620")
webbrowser.open_new("https://sakai.providence.edu/")
