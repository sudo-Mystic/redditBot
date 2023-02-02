import os
import praw
from nsetools import Nse
nse = Nse()


def main():
    reddit = praw.Reddit(client_id=os.environ['clientid'],
                         client_secret=os.environ['clientsecret'],
                         user_agent=os.environ['useragent'],
                         username=os.environ['username'],
                         password=os.environ['password'])
    subreddit = reddit.subreddit("checkingmybot")
    commands = {
        "help": show_help,
        "marketaction": marketaction,
        "sob": sob,
    }

    for comment in subreddit.stream.comments(skip_existing=True):
        if comment.body.lower().startswith("!adani"):
          print("Replying to", comment.author, "on the post",
                  comment.submission, "in the r/",comment.subreddit)
          if len(comment.body.lower().strip().split(" ")) > 1:
            cmd = comment.body.lower().strip().split(" ")[1]
            func = commands.get(cmd)
            if func:
                response = func()
                comment.reply(response)
            
        
          else:
            comment.reply("Not a valid command. Type !adani help for a list of available commands.")
            continue


def show_help():
    return "##List of available commands:\n" \
           "- !adani help - show this message\n" \
           "- !adani marketaction - checkout what indian market doing\n" \
           "- !adani sob - see what mr. adani companies doing \n\n *if you have any issue then talk to my dad u/Mystic1869*" 

def marketaction():
  response = "###Adani Groop\n|Index  | Points  | Change    |\n|:-----------:|:------------:|:------------:|\n|NIFTY 50  |{}|{}  \n|NIFTY BANK|{}|{}  \n| NIFTY IT |{}|{}\n\n^(Last Updated ~ 10 min ago)".format(nse.get_index_quote("nifty 50")['lastPrice'], nse.get_index_quote("nifty 50")['change'], nse.get_index_quote("nifty bank")['lastPrice'], nse.get_index_quote("nifty bank")['change'], nse.get_index_quote("nifty it")['lastPrice'], nse.get_index_quote("nifty it")['change'])

  return response 

def sob():
  ADANIENT = nse.get_quote('ADANIENT')
  ADANIGREEN = nse.get_quote('ADANIGREEN')
  ADANIPORTS = nse.get_quote('ADANIPORTS')
  ADANIPOWER = nse.get_quote('ADANIPOWER')
  ADANITRANS = nse.get_quote('ADANITRANS')
  ATGL = nse.get_quote('ATGL')
  AWL = nse.get_quote('AWL')

  response = f"###Market Action \n\n|Name       | Price     | Change|  \n|:-----------:|:-------:|:-------:|  \n|{ADANIENT['companyName']}           |{ADANIENT['averagePrice']}       |{ADANIENT['change']}       |  \n |{ADANIGREEN['companyName']}           |{ADANIGREEN['averagePrice']}       |{ADANIGREEN['change']}       | \n| {ADANIPORTS['companyName']}          |{ADANIPORTS['averagePrice']}      |{ADANIPORTS['change']}       |\n|{ADANIPOWER['companyName']}           |{ADANIPOWER['averagePrice']}      |{ADANIPOWER['change']}       | \n |{ADANITRANS['companyName']}           |{ADANITRANS['averagePrice']}       |{ADANITRANS['change']}       | \n | {ATGL['companyName']}          |{ATGL['averagePrice']}       |{ATGL['change']}       | \n|{AWL['companyName']}           |{AWL['averagePrice']}       |{AWL['change']}       |  \n\n^(Last Updated -idk)\n "
  
  return response


if __name__ == "__main__":
    main()