import os

# 要檢查的檔案路徑
filepath = "/etc/motd"

# 檢查檔案是否存在
if os.path.isfile(filepath):
    print("檔案存在。")
else:
    print("檔案不存在。")

# 檢查是否為連結檔
if os.path.islink(filepath):
    print("連結檔。")
else:
    print("非連結檔。")

# 要檢查的目錄路徑
folderpath = "/var/log"

# 檢查目錄是否存在
if os.path.isdir(folderpath):
    print("目錄存在。")
else:
    print("目錄不存在。")


# 要檢查的檔案路徑
filepath = "/etc/motd"

# 檢查路徑是否存在
if os.path.exists(filepath):
    print("路徑存在。")
else:
    print("路徑不存在。")


# 要開啟的檔案路徑
filepath = "/etc/not-exists"

# 使用 try 開啟
try:
    f = open(filepath, 'r')
    content = f.read()
    f.close()
# 檔案不存在的例外處理
except FileNotFoundError:
    print("檔案不存在。")
# 路徑為目錄的例外處理
except IsADirectoryError:
    print("該路徑為目錄")

folderpath = "/etc/gtwang/my_folder"
try:
    os.makedirs(folderpath)
except FileExistsError:
    print("檔案已存在。")
# 權限不足的例外處理
except PermissionError:
    print("權限不足。")
