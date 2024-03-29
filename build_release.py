# %%

from datetime import datetime
import time

# version = datetime.today().strftime('%Y%m%d')
import shutil
import os
from distutils.dir_util import copy_tree
from distutils.dir_util import remove_tree
from shutil import copyfile

version = "v3.4.3"

# %%
try:
    remove_tree("./dist/yujoy")
except:
    os.makedirs("./dist/yujoy")

# %%
# Copy yujoy
shutil.copyfile(
    "./beta/schema/yuhao/yujoy.full.dict.yaml", f"./dist/yujoy.full.dict.yaml"
)

shutil.copyfile("./image/yujoy.png", f"./dist/yujoy/yujoy_{version}.png")
shutil.copyfile("./beta/readme.md", f"./dist/yujoy/readme.txt")
copy_tree("./beta/mabiao/", "./dist/yujoy/mabiao/")
copy_tree("./beta/schema/", "./dist/yujoy/schema/")

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
# shutil.make_archive(f"./dist/yuhao_joy_{version}", "zip", "./dist/yujoy")
shutil.make_archive(f"./dist/卿雲爛兮_{version}", "zip", "./dist/yujoy")
# %%
# copyfile(f"./dist/yuhao_joy_{version}.zip", f"../yuhao/dist/yuhao_joy_{version}.zip")
# copyfile(f"./dist/yuhao_joy_{version}.zip", f"../yuhao/dist/卿雲爛兮_{version}.zip")
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
    f"../yuhao/dist/hamster/卿雲爛兮_{version}", "zip", "./dist/yujoy/schema"
)

copy_tree("./dist/yujoy/schema", "../rime-yujoy/")

# %%
# try:
#     remove_tree("./dist/yujoy/mabiao")
#     os.remove(f"./dist/yujoy/yujoy_{version}.png")
#     remove_tree("./dist/yujoy/schema")
# except:
#     print("Delete incomplete")
# time.sleep(5)
# try:
#     remove_tree("./dist/yujoy/mabiao")
#     os.remove(f"./dist/yujoy/yujoy_{version}.png")
#     remove_tree("./dist/yujoy/schema")
# except:
#     print("Delete incomplete")
# %%
