# List of directories
directories = [
    "/Users/colincasey/Dropbox/Phys 431/431 Labs",
    "/Users/colincasey/Dropbox/Phys 431/431 Labs/ZZZ Spectra stuff for Emission Lab",
    "/Users/colincasey/Dropbox/Phys 431/431 Labs Online",
    "/Users/colincasey/Dropbox/Phys 350/350 Labs Online",
    "/Users/colincasey/Dropbox/Phys 350/350 Labs rewrite - DO NOT USE",
    "/Users/colincasey/Dropbox/Phys 350/350 Labs CC",
    "/Users/colincasey/Dropbox/Phys 350/350 Labs",
    "/Users/colincasey/Dropbox/Phys 360/360 Online Labs",
    "/Users/colincasey/Dropbox/Phys 360/360 Labs to rewrite - DO NOT USE",
    "/Users/colincasey/Dropbox/Phys 360/360 Labs Revised",
    "/Users/colincasey/Dropbox/Phys 421/421 Online labs",
    "/Users/colincasey/Dropbox/Phys 421/421 Labs",
    "/Users/colincasey/Dropbox/Phys 411/411 Labs Revised",
    "/Users/colincasey/Dropbox/Phys 411/411 Labs Online",
    "411/411 Labs to sort"
]

# String to be removed
remove_string = "/Users/colincasey/Dropbox/Phys"

# Iterate over the directories and replace the remove_string with an empty string
cleaned_directories = [directory.replace(remove_string, "") for directory in directories]

# Print the cleaned directories
for directory in cleaned_directories:
    print(directory)
