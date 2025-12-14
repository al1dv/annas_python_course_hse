### slide 16
import json

#открытие файла
with open('data.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# Итерирация по ключам верхнего уровня
print("Ключи верхнего уровня:")
for key in config.keys():
    print(key)
    
#Итерирация по значениям словаря departments
print("Ключи по значениям словаря departments:")
for employees in config['departments'].values():
    print(employees)

print("Ключ-значение словаря departments:")
for key, value in config['departments'].items():
    print(f"{key}: {value}")

config['departments']['dev'].append('David')
print(config['departments'])

config["budget"] =  int(config["budget"] * 1.1)
print(config["budget"])

#Запись
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=4)

### slides 17-19
config = {
    "model_name": "bert-base-uncased",
    "batch_size": 32,
    "max_length": 128,
    "learning_rate": 2e-5,
    "epochs": 3,
    "labels": ["positive", "negative", "neutral"]
}
learning_rate1 = config["learning_rate"]
learning_rate2 = config.get("learning_rate")

config["early_stopping"] = True
config["batch_size"] = 64

for key, value in config.items():
  if isinstance(value, (int, float)):
    print(key, value)

copied_file = config.copy()
copied_file["batch_size"] = 8
copied_file["epochs"] = 1
print(copied_file)

### slide 20
api_response = {
    "text": "I really enjoyed the movie, the acting was amazing!",
    "sentiment": {
        "label": "positive",
        "score": 0.95,
        "confidence": "high"
    },
    "entities": [
        {"entity": "movie", "type": "ENTERTAINMENT", "confidence": 0.89},
        {"entity": "acting", "type": "SKILL", "confidence": 0.92}
    ],
    "language": "en",
    "processed_in": 0.45
}
sentiment_score = api_response["sentiment"], ["score"]
print(sentiment_score)

for entity in api_response["entities"]:
        print(entity)

best_confidence = max(api_response["entities"], 
                            key=lambda x: x["confidence"])
print(best_confidence)

api_response["model_version"] = "2.1.0"

string_fields = {}
for key, value in api_response.items():
    if isinstance(value, str):
        print(f"{key} - {value}")

### slides 21-22
pipeline_config = {
    "steps": {
        "tokenization": {"enabled": True, "method": "word"},
        "stopwords": {"enabled": True, "language": "english", "custom_words": []},
        "stemming": {"enabled": False, "algorithm": "porter"},
        "normalization": {"enabled": True, "lowercase": True, "remove_punct": True}
    },
    "input_encoding": "utf-8",
    "output_format": "tokens"
}

pipeline_config['steps']['stemming']['enabled'] = True
pipeline_config['steps']['stopwords']['custom_words'].append('numbers')

main_steps_in_pipe = {}
for key, value in pipeline_config['steps'].items():
  if (value['enabled'] == True):
    main_steps_in_pipe[key] = value
print(main_steps_in_pipe)

pipeline_config['output_format'] = "vectors"
print(pipeline_config)

simplified_content = pipeline_config.copy()
simplified_content['steps'] = main_steps_in_pipe
print(simplified_content)

### slide 23
models_stats = {
    "bert-base": {
        "accuracy": 0.92,
        "f1_score": 0.91,
        "inference_time": 120,
        "size_mb": 440
    },
    "distilbert": {
        "accuracy": 0.89,
        "f1_score": 0.88,
        "inference_time": 65,
        "size_mb": 250
    },
    "roberta-large": {
        "accuracy": 0.94,
        "f1_score": 0.93,
        "inference_time": 210,
        "size_mb": 1600
    }
}

model = max(models_stats.items(),
            key = lambda item: item[1].get("accuracy", 0))
print(model)

inference = []
for key, value in models_stats.items():
  it = value.get('inference_time')
  inference.append(it)
print(inference)

average_time = sum(inference)/len(inference)
print(average_time)

metrics = {}
for key, value in models_stats.items():
  new_accuracy = value.get("accuracy")
  new_f1_score = value.get("f1_score")
  metrics[key] = {"accuracy": new_accuracy,
                  "f1_score": new_f1_score}
print(metrics)

models_stats["albert-base"] = {
    "accuracy": 0.87,
    "f1_score": 0.86,
    "inference_time": 55,
    "size_mb": 180
}

mini_models = []
for key, value in models_stats.items():
  size = value.get('size_mb')
  if size < 500:
    mini_models.append(key)
print(mini_models)
print(models_stats)

### slide 24
import json

with open('nlp_service_config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
    print(config)
    summarization = {'path': '/models/supersummarization',
                     'max_input_length': 512,
                     'supported_languages': ['en', 'es', 'fr']}

config['models']['summarization'] = summarization

config["rate_limit"] *= 1.5

config['models']['sentiment']['supported_languages'].append('ru')

fixation = config['server'].copy()

print(fixation)
print(config)

with open('data_update.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=2)