"""
每次使用类名新建对象__new__()和__init__都会被调用
要想__init__里的初始化只执行一次,可以设置个类标记如init_flag

"""


class MusicPlayer:
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if not MusicPlayer.init_flag:
            MusicPlayer.init_flag = True
            print("init called")


music_player1 = MusicPlayer()
music_player2 = MusicPlayer()

print(music_player1)
print(music_player2)
