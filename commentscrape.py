import praw
from urllib.request import urlopen
from random import randint
import re
## by hammed: reddit extract images from links in comments 

##
# create reddit app from your reddit account to get credentials 
reddit = praw.Reddit(client_id= '',
                        client_secret=	'',
                        username='',
                        password='',
                        user_agent='')


sub = reddit.subreddit('photoshopbattles') #r/photoshopbatles

hots = sub.top("day",limit=15)

for x in hots:
    if not x.stickied:
        
                
            file1 = open("comments.txt", "r+") 
        # read file content 
            readfile = file1.read() 
        # check if url has been downloaded
            
            Comments = x.comments.list()
            print(10*'__')
            print("post:{} [authour:{}]".format(x.title,x.author)) 
            
            for _, comment in zip(range(10), Comments):
                if comment.author not in ["AutoModerator","ApiContraption", None]: # dont scrape posts by Mod-bots
                    if "https:" in comment.body:
                        # print(5* '-','\n',comment.author,comment.body)
                        ## use regex to extract links from comments
                        url = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+', comment.body)
                        ## download comments as fake images
                        link=''.join(url)
                        try:
                            contents = urlopen(link).read()
                        except:
                            print("did not download")
                            pass
                        
                        if link[-3:] in ["jpg","jpeg","png"]:
                            if link in readfile:
                                print("already downloaded")
                                
                            else:
                                file1.write('\n'+20*'__')
                                file1.write(f"\n{x.title}: '\n'{link}: --- [{comment.author}] --- {comment.body}")
                            #save file
                                with open('fake/{} _-_{}.{}'.format(comment.author,randint(1,1000),link[-3:]), 'wb') as f:
                                    f.write(contents)

                                print("downloaded")
                    
            # closing a file 
            file1.close()