import requests,urllib
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from termcolor import colored


APP_ACCESS_TOKEN = '5698649413.276436a.79e5fcd89001466eacb46433ade04899'
BASE_URL = 'https://api.instagram.com/v1/'

#to get own info declare a function.

def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print (colored('User does not exist!','red'))
    else:
        print (colored('Status code other than 200 received!','red'))

#to get id of user by username declare a function.

def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print (colored('Status code other than 200 received!','red'))
        exit()
#function declaration o get info of a user by username.

def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print (colored('User does not exist!','red'))
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print (colored('There is no data for this user!','red'))
    else:
        print (colored('Status code other than 200 received!','red'))

#function declaration to get your own recent post.

def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print (colored('Your image has been downloaded!','green'))
        else:
            print (colored('Post does not exist!','red'))
    else:
        print (colored('Status code other than 200 received!','red'))

#function declaration to get the recent post of a user by user name.

def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print (colored('User does not exist!','red'))
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print (colored('Your image has been downloaded!','green'))
        else:
            print (colored('Post does not exist!','red'))
    else:
        print (colored('Status code other than 200 received!','red'))

#function declaration to get id of recent post of a user by username.

def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print (colored('User does not exist!','red'))
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print (colored('There is no recent post of the user!','red'))
            exit()
    else:
        print (colored('Status code other than 200 received!','red'))
        exit()

#function declaration to like the recent post of a user.

def like_a_post(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print (colored('Like was successful!','green'))
    else:
        print (colored('Your like was unsuccessful. Try again!','red'))


#function declaration to get the recent media like by user

def recent_media_liked():
    #media_id=get_post_id(insta_username)
    request_url = (BASE_URL + "users/self/media/liked?access_token=%s") % (APP_ACCESS_TOKEN)
    print 'GET request url:%s' % (request_url)
    liked_media = requests.get(request_url).json()
    if (liked_media['meta']['code'] == 200):
        if len(liked_media['data']):
            image_name=liked_media['data'][0]['id']+'.jpeg'
            image_url=liked_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url,image_name)
            print(colored("your image has been downloaded.",'green'))
            return liked_media['data'][0]['id']
        else:
            print (colored("there is no recent post.",'red'))
    else:
        print (colored("status code other than 200 received!",'red'))
    return None


# function declaration to get the list of user who like posts
def get_like_list(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + "media/%s/likes?access_token=%s") % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url:%s' % (request_url)
    like_list = requests.get(request_url).json()
    if (like_list['meta']['code'] == 200):
        if (like_list['data']):
            for a in range(0, len(like_list['data'])):
             print like_list['data'][a]['username']
        else:
         print(colored("like doesn't exsist.",'red'))
    else:
     print(colored("status code other than 200.",'red'))


#function declaration to make the comment on the recent post of the user.

def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print(colored("Successfully added a new comment!",'green'))
    else:
        print (colored("Unable to add comment. Try again!",'red'))


#function declaration to get the comment list.

def get_comment_list(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + "media/%s/comments?access_token=%s") % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url:%s' % (request_url)
    comments_list = requests.get(request_url).json()
    if (comments_list['meta']['code'] == 200):
        if (comments_list['data']):
            for a in range(0, len(comments_list['data'])):
                print comments_list['data'][a]['from']['username']+':',
                print comments_list['data'][a]['text']
        else:
            print(colored("comment doesn't exsist."))
    else:
        print(colored("status code other than 200.",'red'))


#function declaration to make delete negative comments from the recent post of the other users.

def delete_negative_comment(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            #Here is the implementation of how to delete the negative comments :)
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, APP_ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        print (colored('Comment successfully deleted!\n','green'))
                    else:
                        print (colored('Unable to delete comment!','red'))
                else:
                    print 'Positive comment : %s\n' % (comment_text)
        else:
            print (colored('There are no existing comments on the post!','red'))
    else:
        print (colored('Status code other than 200 received!','red'))



#function declaration to iterate through the negative comments on posts.

def iterate_through_negative_comments(media_id):
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()
    if comment_info['meta']['code']==200:
        if len(comment_info['data']):
            for i in range(0,len(comment_info['data'])):
                comment_id=comment_info['data'][i]['id']
                comment_text=comment_info['data'][i]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                else:
                    print 'possitive comment : %s'% (comment_text)
        else:
            print (colored('There are no existing comments on the post!','red'))
    else:
        print (colored('Status code other than 200 received!','red'))


#   function declaration to get minimum likes


def min_likes_on_post(insta_username):
    user_id=get_user_id(insta_username)
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:                                                             # check for status code of the request
        if len(user_media['data']):
            like=[]
            i=0
            while(i<len(user_media['data'])):
                likes_on_post=user_media['data'][i]['likes']['count']
                like.append(likes_on_post)
                i=i+1
            min_like=min(like)
            j=0
            while(j<len(like)):
               if(like[j]==min_like):
                    image_name = user_media['data'][j]['id'] + '.jpeg'
                    image_url = user_media['data'][j]['images']['standard_resolution']['url']
                    urllib.urlretrieve(image_url, image_name)                                               # image url is retrieved
                    print 'GET image_url is :%s' % (image_url)
                    print (colored('Your image has been downloaded! By clicking above link you can view you the image with minimum number of likes','green'))
               j=j+1
        else:
            print (colored('This account has zero post','red'))
            exit()

    else:
        print (colored('Status code other than 200 received!','red'))
        exit()








#put your choice,what do you want to.

def start_bot():
    while True:
        print '\n'
        print 'Hey! Welcome to instaBot!'
        print 'Here are your menu options:'
        print 'My sandbox users are:'
        print '1. astha_rc_\n'
        print '2. itzz_mehakk\n'
        print '3. selfie_queen.__\n'
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        print "c.Get your own recent post\n"
        print "d.Get the recent post of a user by username\n"
        print "e.Get the id of post of user by username\n"
        print "f.Get the recent media like by user\n "
        print "g.Get a list of people who have liked the recent post of own post\n"
        print "h.Like the recent post of a user\n"
        print "i.Get a list of comments on the recent post of own post\n"
        print "j.Make a comment on the recent post of a user\n"
        print "k.Delete negative comments from the recent post of a user\n"
        print "l.Iterate through the negative comments.\n"
        print "m.Minimum like on post\n"
        print "n.Exit\n"

        choice=raw_input("Enter you choice: ")
        if choice=="a":
            self_info()
        elif choice=="b":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice=="c":
            get_own_post()
        elif choice=="d":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice=="e":
            insta_username = raw_input("Enter the username of the user: ")
            get_post_id(insta_username)
        elif choice == "f":
            #insta_username = raw_input("Enter the username of the user: ")
            recent_media_liked()
        elif choice == "g":
            insta_username = raw_input("Enter the user name of the user:")
            get_like_list(insta_username)
        elif choice=="h":
            insta_username = raw_input("Enter the username of the user: ")
            like_a_post(insta_username)
        elif choice=="i":
            insta_username = raw_input("Enter the username of the user: ")
            get_comment_list(insta_username)
        elif choice=="j":
            insta_username = raw_input("Enter the username of the user: ")
            post_a_comment(insta_username)
        elif choice=="k":
            insta_username = raw_input("Enter the username of the user: ")
            delete_negative_comment(insta_username)
        elif choice=="l":
            insta_username = raw_input("Enter the username of the user: ")
            media_id=get_post_id(insta_username)
            iterate_through_negative_comments(media_id)
        elif choice=="m":
            insta_username = raw_input("Enter the username of the user: ")
            min_likes_on_post(insta_username)
        elif choice=="n":
            exit()
        else:
            print "wrong choice"

start_bot()                                                        #function calling
