import facebook
import urllib

######################################################

## ## functions
def frinedToPhoto(friends):
    PhotoLst = []
    for friend in friends:
        photoLst.append(extractImg(friends))
    return PhotoLst

def extractImg(me) :
    ## useing the api to get profile picture from a friend type
    s
def extractImg(friends):
    ## useing the api to get profile picture from a friend type.
    s
def bestMatch( myPhoto , PhotoLst ):
    ## find the best match
    s
def makePage(myPhoto , result ):
    ##  make the final page that will be shown on success.
    s
def post(page):
    ## post the final page on the users wall.
    s
#################################################### ## 

def main():
    graph = facebook.GraphAPI(oauth_access_token)
    profile = graph.get_object("me")
    friends = graph.get_connections("me", "friends")
    graph = facebook.GraphAPI(access_token='your_token', version='2.2') ## the access token 
    friends = graph.get_connections(id='me', connection_name='friends') ## all the firends
    find 
    myPhoto = 0# the main user profile pic.
    PhotoLst = frinedToPhoto(friends)
    result = bestMatch( myPhoto , PhotoLst )
    page = makePage(myPhoto , result )
    post(page)     
