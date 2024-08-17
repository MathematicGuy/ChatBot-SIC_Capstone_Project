## How To Train Model


**I. Add your story to stories.py**

**Example:**

```yaml

- story: cyberpunk 
  steps:
  - intent: mega_corporation
  - action: utter_cyberpunk
```

**II. Add your story to domain.yml**

Add 'mega_corporation' to intents

Responses:

```yaml
utter_cyberpunk:
  - text: "They are evil, control controlling the world, and I love it!"
```


## Shell Command
Run this before call use Front-end
```shell
rasa run --enable-api --cors "*"
```

Start actions.py

```shell
rasa run actions --debug
```

Rasa interactive cmd: allow you to control the action of the bot

```shell  
rasa interactive
```

# System Design
Virtual Assitant: "1 Chatbot for PDF Analysis", "1 Chatbot for finding document PDF"
MongoDB/SQLServer: Read & Write Data.
Hệ thống tìm kiếm tài liệu khoa học. Lấy Data từ MongoDB. 
python

PDF (tài liệu khọc học)
Data (SQL) - 5 cột, tên tác, tên tài liệu, năm xuất bản, tóm tắt, link tài liệu.
SQL - 5 cột, tên tác, tên tài liệu, năm xuất bản, tóm tắt, link tài liệu.


vd: người dùng muốn tra cứu tài liệu về SVM, hệ thống sẽ trả về các tài liệu liên quan đến SVM.
Mô Hình Học Máy: RASA/HuggingFaceCommunity Chatbot



