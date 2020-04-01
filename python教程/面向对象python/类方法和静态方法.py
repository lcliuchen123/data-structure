
class Game():
    top_score = 0

    def __init__(self,play_name):
        self.play_name = play_name

    # 既不需要访问类属性，也不需要访问类方法
    @staticmethod
    def show_help():
        print("help")

    #    类属性
    @classmethod
    def show_top_score(cls):
        print(cls.top_score)

    # 实例属性
    def start_game(self):
        print("start")

Game.show_help()
Game.show_top_score()