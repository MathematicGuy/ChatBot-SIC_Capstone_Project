## How To Train Model


**I. Add your story to [stories.yml](./Rasa/data/stories.yml)**

**Example:**

```yaml

- story: cyberpunk 
  steps:
  - intent: mega_corporation
  - action: utter_cyberpunk
```

**II. Add your story to [domain.yml](./Rasa/domain.yml)**

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

