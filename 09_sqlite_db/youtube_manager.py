import sqlite3

conn = sqlite3.connect("youtube_manager.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               duration TEXT NOT NULL
    )
''')


def list_videos():
    cursor.execute("SELECT * FROM Videos")
    for video in cursor.fetchall():
        print(video)
    
def add_video():
    name = input("Enter Video Name : ")
    duration = input("Enter Video Duration : ")

    cursor.execute("INSERT INTO Videos (name,duration) VALUES (?,?)", (name,duration))
    conn.commit()
    

def update_video():
    videoId = input("Enter Video Id To Update : ")
    name = input("Enter New Video Name : ")
    duration = input("Enter New Video Duration : ")
    cursor.execute("UPDATE Videos SET name = ?, duration = ? WHERE id = ?", (name,duration,videoId))
    conn.commit()
    

def delete_video():
    videoId = input("Enter Video Id To Delete : ")
    conn.execute("DELETE FROM Videos WHERE id = ?",(videoId,))


def main():
    while(True):
        print("\n 📽️ Youtube Manager App")
        print("1. List videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit ")

        choice = input("\n Enter Your Choice  :  ")

        if(choice == '1'):
            list_videos()
        elif(choice == '2'):
            add_video()
        elif(choice == '3'):
            update_video()
        elif(choice == '4'):
            delete_video()
        elif(choice == '5'):
            break
        else:
            print("Invalid Choice \n")
    conn.close()



if __name__ == '__main__':
    main()