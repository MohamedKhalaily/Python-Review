def creat_youtube_video(title, description):
	youtube_video={"title":title,"description":description,"likes":0,"dislikes":0,"comments":{}}
	return youtube_video
def like(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"]=youtube_video["likes"]+1
	return youtube_video

def dislike(youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"]=youtube_video["dislikes"]+1
	return youtube_video

def add_comment(youtube_video, username, comment_text):
	youtube_video["comments"]["username"]= comment_text

new_youtube_video = creat_youtube_video("rani the 7lo", "rani teatching u how to become beautiful")
print(new_youtube_video)






