import praw
import sys
import os

#replace with your credentials
#reddit authorized instance
reddit = praw.Reddit(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    password="ACCOUNT_PASSWORD",
    user_agent="USER_AGENT eg: 'Saved posts downloader v1.0.0 by /u/user'",
    username="ACCOUNT_USERNAME",
    ratelimit_seconds=600
)

#write IDs to "ids.txt" yes or no
writeYN = 0
while writeYN != "y" and writeYN != "n":
    print("Write IDs?\ny/n")
    writeYN = input()
    writeYN = writeYN.lower()

try:
    create = open("ids.txt", "x")
except FileExistsError:
    pass

try:
    create = open("newids.txt", "x")
    create.close()
except FileExistsError:
    pass

if writeYN == "y":
    print("Extracting saved posts...")
    for item in reddit.user.me().saved(limit=None):
        skip = False
        id = item.id
        with open("ids.txt", "r") as d:
            #check for duplicates
            while True:
                #read each line
                next_line = d.readline()
                #execute when file has no other lines
                if not next_line:
                    #if the item is not duplicate
                    if skip == False:
                        #write id
                        with open("ids.txt", "a") as s:
                            s.write(f"{id}\n")
                        with open("newids.txt", "a") as t:
                            t.write(f"{id}\n")
                    #exit while loop
                    break

                #strip file line
                lineid = next_line.strip("\n ")

                #check duplicate
                if id == lineid:
                    skip = True

elif writeYN == "n":
    sys.exit()

print("Press ENTER to download saved submissions")
input()

#read line by line "ids.txt"
with open("newids.txt",'r') as f:
    while True:
        next_line = f.readline()
        if not next_line:
            break
        id = next_line.strip("\n ")

        #check for blank lines
        if id != "":

            #if ID is from comment execute this
            try:
                comment = reddit.comment(id)
                body = comment.body
                permalink = comment.permalink
                with open("comments.txt", "a", encoding="utf-8") as c:
                    c.write(f"Permalink: {permalink}\nBody:\n{body}\n\n" + 50*"-+" + "\n\n")
        
            #if ID is not from comment (submissions of any kind) execute this
            except:
                submission = reddit.submission(id)
                title = submission.title
                selftext = submission.selftext
                permalink = submission.permalink
                with open("submissions.txt", "a", encoding="utf-8") as p:
                    p.write(f"Title: {title}\nPermalink: {permalink}\nSelftext:\n{selftext}\n\n" + 50*"-+" + "\n\n")

os.remove("newids.txt")
print("Finished Downloading!")



#"ids.txt", "comments.txt" and "submissions.txt" will be created in the same directory as this script
#"comments.txt" will contin all saved comments
#"submissions.txt" will contain all saved submissions