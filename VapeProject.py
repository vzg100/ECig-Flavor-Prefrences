from bs4 import BeautifulSoup
import os
import operator
import praw
import time
#left file paths blank for security reasons 
d = ""
o = ""
uAgent = ""
#Sets up reddit comment scraper
bot = praw.Reddit(user_agent = uAgent, client_secret ="", client_id="", usename="");
searchSubs = ['vapeheads', 'ShakeAndVape', 'vaping101', 'juiceswap', 'EJuicePorn']
#scrapes comments and saves them 
for i in searchSubs:
    subreddit = bot.subreddit(i)
    name = "output"+i+".csv"
    output = open(name, "w")
    for submission in subreddit.submissions():
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            print(comment.body)
            s = str(comment.body)
            s.strip(",")
            output.write(s+",")
    output.close()
        


def collect_files(directory):
    files = []
    f = open(directory)
    for line in f:
        files.append(line)

    return files

def clean_text(s: str):
    s = s.lower()
    t=""
    for i in s:
        if i in "qwertyuiopasdfghjklzxcvbnm ":
            t += i
    return t

class Scraper:
    """scrapes flavor pages collected"""
    def __init__(self, directory: str, outputfile: str):
        print("Started")
        
        self.directory = directory
        self.outputfile = outputfile
        self.flavors = []

    def scanner(self):
        print("scanning")
        files = collect_files(self.directory)

        for file in files:
            try:
                soup = BeautifulSoup(open("flavors"+file[1:-1]))
                print(soup)
                for link in soup.find_all("a"):

                    if "flavor" in link.get("href"):
                        print(link)
                        self.flavors.append(link.text)
                        print(link.text)
            except:
                pass


    def save(self):
        print("Saving")
        f = open(self.outputfile, "w")
        for i in self.flavors:
            print(i)
            f.write(i+"\n")
        f.close()




def cleaner(inp: str, output: str):
    f = open(inp)
    o = open(output, "w+")
    for line in f:
        t = ""
        line = line.lower()


        for i in line:
            if i in "qwertyuiopasdfghjklzxcvbnm ":
                t+=i
        if t == "" or t == " ":
            pass
        else:
            o.write(t+"\n")
    f.close()
    o.close()


class Recipe_scraper:
    """Scrapes recipe pages for flavors used -- really should have just made this an extra method"""
    def __init__(self, directory: str, outputfile: str):
        print("Started")
        
        self.directory = directory
        self.outputfile = outputfile
        self.flavors = {}

    def scanner(self):

        files = collect_files(self.directory)
        for file in files:
            file = file.strip("\n")
            f = open(file)
            try:

                soup = BeautifulSoup(open(file), "lxml") 
                for link in soup.find_all("a"):

                    if "flavor" in link.get("href"):
                        t = link.text
                        t = clean_text(t)
                        if t in self.flavors.keys():
                            self.flavors[t] = self.flavors[t]+1
                        else:
                            self.flavors[t] = 1

                         
            except:
                pass

        self.flavors = sorted(self.flavors.items(), key=operator.itemgetter(1))
        print(self.flavors)
    def save(self):
        print("Saving")
        f = open(self.outputfile, "w")
        for i in self.flavors:
            print(i)
            f.write(str(i)+"\n")
        f.close()




def cleaner(inp: str, output: str):
    f = open(inp)
    o = open(output, "w+")
    for line in f:
        t = ""
        line = line.lower()


        for i in line:
            if i in "qwertyuiopasdfghjklzxcvbnm ":
                t+=i
        if t == "" or t == " ":
            pass
        else:
            o.write(t+"\n")
    f.close()
    o.close()

