# redditSavedDownloader

Script to export your saved submissions AND comments

# Notes
- "ids.txt", "comments.txt" and "submissions.txt" will be created in the same directory as this script
- "comments.txt" will contin all saved comments
- "submissions.txt" will contin all saved submissions
- if you want to re-run the program after saving more submission/comments, delete/move to another directory "ids.txt", "submissions.txt" and "comments.txt" and select y, not deleting the files will result in duplicates
- deduplication WIP

# Usage
Create a script at https://old.reddit.com/prefs/apps/    
Download rs.py    
Edit rs.py with your credentials    
To run the script open a command prompt and cd to the directory where rs.py is, then type

py -3 rs.py

and press enter.    
If it's the first time you run the script select y, read the notes above.
