'''

manual database to store data, real fast/hacky

'''
#imports
from posts import Post
from posts import Location
import time


class DB(object):

    def __init__(self):
        self.data = dict()
        self.user_data = dict()
        self.last_gen = 0

    def find_at(self,lat,long):
        ret = []
        loca = Location(lat,long,0,int(time.time()))
        model = Post(0,loca,'','','')
        for post in self.data.values():
            if(self.equal_enough(model,post)):
                ret.append(post)
        return ret

    #usef for finding "close enough to be the same general area" locations, ignore alt
    def equal_enough(self,a,b):
        return True

    def add(self,id,obj):
        self.data[id] = obj

    def dump(self):
        for post in self.data.values():
            print post.id
            print post.owner_display_name
            print post.location.timestamp
            if len(post.post_content) > 40:
                str_out = post.post_content[0:39]
            else:
                str_out = post.post_content
            print str_out

    def gen_id(self):
        self.last_gen = 1 + self.last_gen
        return self.last_gen

    def get_user(self,user):
        usr = self.user_data[user]
        return usr