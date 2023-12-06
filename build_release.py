# %%

from datetime import datetime
import time

# version = datetime.today().strftime('%Y%m%d')
import shutil
import os
from distutils.dir_util import copy_tree
from distutils.dir_util import remove_tree
from shutil import copyfile

version = "v3.3.0"

# %%
try:
    remove_tree("./dist/yujoy")
except:
    os.makedirs("./dist/yujoy")

# %%
# Copy yujoy
# shutil.copyfile("./image/yujoy.png", f"./dist/yujoy/yujoy_{version}.png")
shutil.copyfile("./beta/readme.md", f"./dist/yujoy/readme.txt")
copy_tree("./beta/mabiao/", "./dist/yujoy/mabiao/")
copy_tree("./beta/schema/", "./dist/yujoy/schema/")
copy_tree("../yuhao/beta/schema/lua/", "./dist/yujoy/hotfix/lua/")
copy_tree("./beta/hotfix/", "./dist/yujoy/hotfix/")

# %%
# copy yuhao
copy_tree("../yuhao/beta/schema/lua/", "./dist/yujoy/schema/lua/")
for file_name in [
    "default.yaml",
    "key_bindings.yaml",
    "punctuation.yaml",
    # "rime.lua",
    "yuhao.symbols.yaml",
    "symbols.yaml",
    "yuhao_pinyin.dict.yaml",
    "yuhao_pinyin.schema.yaml",
    "yuhao/yuhao.extended.dict.yaml",
    "yuhao/yuhao.private.dict.yaml",
    # "yuhao/yuhao.symbols.dict.yaml",
]:
    copyfile(f"../yuhao/beta/schema/{file_name}", f"./dist/yujoy/schema/{file_name}")

# %%
shutil.make_archive(f"./dist/yuhao_joy_{version}", "zip", "./dist/yujoy")
# %%
copyfile(f"./dist/yuhao_joy_{version}.zip", f"../yuhao/dist/yuhao_joy_{version}.zip")
copyfile(f"./dist/yuhao_joy_{version}.zip", f"../yuhao/dist/宇浩卿雲_{version}.zip")
# %%
# %%
# Remove unrelated files
for file_name in [
    "default.yaml",
    "key_bindings.yaml",
    "punctuation.yaml",
    "symbols.yaml",
]:
    os.remove("./dist/yujoy/schema/" + file_name)

shutil.make_archive(
    f"../yuhao/dist/hamster/yuhao_joy_{version}", "zip", "./dist/yujoy/schema"
)

# %%
try:
    remove_tree("./dist/yujoy")
except:
    print("Delete incomplete")
time.sleep(5)
try:
    remove_tree("./dist/yujoy")
except:
    print("Delete incomplete")
# %%
