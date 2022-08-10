import praw

#replace with your credentials
#reddit authorized instance
reddit = praw.Reddit(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    username = "USERNAME",
    user_agent="USER_AGENT",
    password = "PASSWORD",
)

#write IDs to "ids.txt" yes or no
writeYN = input("Write IDs?\ny/n\n")
if writeYN == "y" or "Y":
    with open("ids.txt", "a+") as d:
        for item in reddit.user.me().saved(limit=None):
            id = item.id
            d.write(id + "\n")
    d.close

print("\n\nDownloading from extracted IDs")
input("\nEnter to continue")
print("\nWorking...")

#read line by line "ids.txt"
file = open("ids.txt",'r')
while True:
    next_line = file.readline()
    if not next_line:
        break
    id = next_line.strip()

    #check for blank lines
    if id != "":

        #if ID is from comment execute this
        try:
            comment = reddit.comment(id)
            body = comment.body
            permalink = comment.permalink
            c = open("comments.txt", "a", encoding="utf-8")
            c.write("Permalink: " + permalink +"\nBody:\n" + body + "\n\n" + 50*"-+" + "\n\n")
            c.close
    
        #if ID is not from comment (submissions of any kind) execute this
        except:
            submission = reddit.submission(id)
            title = submission.title
            selftext = submission.selftext
            permalink = submission.permalink
            p = open("submissions.txt", "a", encoding="utf-8")
            p.write("Title: " + title + "\n" + "Permalink: : " + permalink + "\nSelftext:\n" + selftext + "\n\n" + 50*"-+" + "\n\n")
            p.close
print("\n\nFinished Downloading!")
file.close()

#"ids.txt", "comments.txt" and "submissions.txt" will be created in the same directory as this script
#"comments.txt" will contin all saved comments
#"submissions.txt" will contin all saved submissions
#if you want to re-run the program after saving more submission/comments, delete "ids.txt" and select y, writing ids without deleting the files will result in duplicates
#deduplication WIP