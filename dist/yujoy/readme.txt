# 宇浩·卿雲

## schema

/scheme 中的文件爲 Rime 輸入法各平臺（小狼毫、鼠鬚管）碼表。

複製所有文件至機器上的 /Rime 文件夾。

請在 default.custom.yaml 文件的 patch/schema_list 列表中手動添加本方案名如下：

patch:
  schema_list:
    - schema: yujoy
    - schema: yujoy_sc
    - schema: yujoy_tc
    - schema: yujoy_tw

重新部署后即可使用。

## mabiao

/mabiao 中的文件是其他平臺的碼表。
