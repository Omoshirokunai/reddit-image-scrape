import praw
from urllib.request import urlopen
from random import randint

# create reddit app from your reddit account to get credentials 
reddit = praw.Reddit(client_id= '...',
                        client_secret=	'',
                        username='',
                        password='',
                        user_agent='')

sub = reddit.subreddit('pics')

hots = sub.top("month",limit=10)

# submission = next(x for x in reddit.subreddit('photoshopbattles').hot() 
#                 if not x.stickied)
# print(submission.title)

for x in hots:
        if not x.stickied:
        
                ## download posts as original images
                url = x.url
                try:
                        contents = urlopen(url).read()
                except:
                        print("did not download")
                file1 = open("visited.txt", "r+") 
        # read file content 
                readfile = file1.read() 
        # check if url has been downloaded
                if url in readfile:
                        print("already downloaded")
                else:
                        print("title:{} [authour:{}], \n upvotes:{}, \n downvotes:{}, \n visited:{}"
                .format(x.title,
                        x.author,
                        x.ups,
                        x.downs,
                        x.visited)) 
                        print("downloading")
                        try:
                                # file1.write('\n'+20*'__')
                                file1.write(f"\n {url}: [{x.author}] --:{x.title}")
                
                        except:
                                pass
                        
                        #save file
                        # with open('fake/{} _-_{}.{}'.format(x.author,randint(1,1000),url[-3:]), 'wb') as f:
                        #         f.write(contents)
                        #save file
                        with open('original/{} -_-{}.{}'.format(x.author,randint(1,1000),url[-3:]), 'wb') as f:
                                f.write(contents)
                        
                # closing a file 
                file1.close()

        
