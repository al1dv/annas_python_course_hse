"""### **5: скрипт `text_analysis.py`**

Создайте файл text_analysis.py, который будет представлять собой модуль для анализа текстовых данных

Структура text_analysis.py:

```python
1. импорт re
2. from collections import Counter
3. def load_data(filename):
4. def clean_text(text):
5. def tokenize_text(text):
6. def create_frequency_dict(tokens):
7. if __name__ == "__main__":
    # внутри этого блока выполняем запуск всех созданных вами функций в правильном порядке с выбранным файлом
```

Сдаём **только** скрипт text_analysis.py
"""

import re
from collections import Counter
def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    return text

def tokenize_text(text):
    text = text.lower()
    text = re.sub(r'[^а-яёa-z0-9.,!?;: -]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text

def create_frequency_dict(text):
    words = text.split()
    freq_dict = Counter(words)
    return freq_dict

if __name__ == "__main__":
    text = load_data('shakespeares.txt')
    print(f"Длина файла: {len(text)}")
    print("Первые 200 символов:", text[:200])
    
    cleaned_text = clean_text(text)
    tokens = tokenize_text(cleaned_text)  
    print("После токенизации:", tokens[:200])
    
    freq_dict = create_frequency_dict(tokens)  
    print("Самые частые слова:", freq_dict.most_common(5))