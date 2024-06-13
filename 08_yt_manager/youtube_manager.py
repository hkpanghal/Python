import json


def load_data():
    try:
        with open("youtube.txt",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_video_helper(videos):
    
    with open("youtube.txt",'w') as file:
        json.dump(videos,file)


def list_all_videos(videos):
    print("\n")
    print("_" * 100)
    for index,video in enumerate(videos,start=1):
        print(f"{index}.  {video["name"]} , {video["time"]}")
    print("\n")
    print("_" * 100)

def add_video(videos):
    name = input("Enter video name : ")
    time = input("Enter video time : ")

    videos.append({"name":name,"time":time})
    save_video_helper(videos)


def update_video_details(videos):
    list_all_videos(videos)

    index = int(input("Enter video number to be updated : "))
    if(1<= index <= len(videos)):
        name = input("Enter new name : ")
        time = input("Enter time time : ")
        videos[index-1] = {"name":name,"time":time}
        save_video_helper(videos)
    else:
        print("Invalid number provided")

def delete_video(videos):
    list_all_videos(videos)

    index = int(input("Enter video number to be deleted : 5"))
    if(1<= index <= len(videos)):
        del videos[index-1]
        save_video_helper(videos)
    else:
        print("Invalid number provided")



def main():
    videos = load_data()
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
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video_details(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()

