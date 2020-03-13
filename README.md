# Protobuf 分析與重建案例
=======
Protobuf 分析練習用樣本

請與 [Protobuf 分析與重建案例分享](https://blog.keniver.com/2020/03/protobuf-analysis-and-rebuild/) 一起服用

### 檔案內容
#### exported.config
從設備匯出的設定檔（分析目標）

#### config.proto
分析後重建的 Protobuf 結構描述檔案

#### config_pb2.py
config.proto 編譯結果

#### config_reader.py
讀取 exported1.config 的範例程式

#### build.sh
將 config.proto 編譯為 config_pb2.py
