# redditSavedDownloader

Script to export your saved submissions AND comments to a .txt file

# Notes
- "ids.txt", "comments.txt" and "submissions.txt" will be created in the same directory as this script
- "comments.txt" will contain all saved comments
- "submissions.txt" will contain all saved submissions

# Usage
- Create a script at https://old.reddit.com/prefs/apps/    
- Download/Copy rs.py and place it in a directory (it will create files in there)    
- Edit rs.py with your credentials at the top of the script    
- To run the script open a command prompt and cd to the directory where rs.py is, type

`python rs.py`

- and press enter.

# Important
If you decide to re-run the script it will only add posts and comments to "submission.txt" and "comments.txt" that AREN'T IN "ids.txt", so either you delete/move to another directory all 3 .txt or you leave all 3 there.
