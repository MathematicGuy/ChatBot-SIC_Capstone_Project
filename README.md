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
- text: "How do you feel about mega corporations?"
```


## Shell Command

Run this before call use Front-end
```shell
rasa run --enable-api --cors "*"
```

