"""
每次使用类名新建对象__new__()和__init__都会被调用：
    1. __new__():创建对象
    2.__init__():对创建的对象进行初始化

要想__init__里的初始化只执行一次,可以设置个类标记如init_flag

"""


class MusicPlayer:
    instance = None
    init_flag = False

    @classmethod  # 不会调用 __init__()
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if not MusicPlayer.init_flag:
            MusicPlayer.init_flag = True
            print("init called")


music_instance = MusicPlayer.get_instance()
music_player1 = MusicPlayer()
music_player2 = MusicPlayer()

print(music_instance)
print(music_player1)
print(music_player2)
