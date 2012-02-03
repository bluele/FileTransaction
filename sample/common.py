# -*- coding: utf-8 -*-

from filetransaction import ftopen

with ftopen("./sample/test.txt", "wb") as f:
    f.write("python!\n")
    # 補足されない例外が発生したらファイルの作成はキャンセルされる
    raise Exception("Any Exception occur.")
    f.write("perl!\n")
