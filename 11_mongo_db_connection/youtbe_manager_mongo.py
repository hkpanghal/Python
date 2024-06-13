from pymongo import MongoClient # type: ignore
from bson import ObjectId # type: ignore

client =  MongoClient("localhost",27017)
db = client["pytube"]
video_collection = db["videos"]

def list_all_videos():
    print("\n")
    print("_" * 100)
    for video in video_collection.find():
        print(f"_id : {video["_id"]} , {video["name"]} , {video["time"]}")
    print("\n")
    print("_" * 100)

def add_video():

    name = input("Enter video name : ")
    time = input("Enter video time : ")

    video_collection.insert_one({"name":name,"time":time})

    


def update_video_details():
    list_all_videos()
    _id = input("Enter video _id : ")
    name = input("Enter video new name : ")
    time = input("Enter video new time : ")

    video_collection.update_one({"_id":ObjectId(_id)},{"$set":{"name":name,"time":time}})



def delete_video():
    list_all_videos()
    _id = input("Enter video _id : ")
    video_collection.delete_one({"_id":ObjectId(_id)})



def main():
    
    while(True):
        print("\n || Youtube video manager app ||")
        print("1. List all videos ")
        print("2. Add videos ")
        print("3. Update video details ")
        print("4. Delete video ")
        print("5. Exit \n ")

        choice = input("Enter your choice  :  ")

        match choice:
            case '1':
                list_all_videos()
            case '2':
                add_video()
            case '3':
                update_video_details()
            case '4':
                delete_video()
            case '5':
                break
            case _:
                print("Invalid Choice")



if __name__ == "__main__":
    main()

