from utils.utils import func

func = func()
if __name__ == "__main__":
    try:
        func.login()
        print("ログインが完了しました")
    except:
        print("再度ログインを実行します")
        func.login()
    
    try:
        print("いいねを開始します")
        func.good()
        print("終了しました")
    except:
        print("再度実行します")
        func.login()

    
