import json

def convert_to_json(jsonl_file):
    conversations = []
    with open(jsonl_file, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            input_text = data["fanyi"].strip()
            input_text = input_text.replace('注释','')
            if input_text:  # 如果input字段不为空
                conversation = {
                    "input": input_text,
                    "output": data["content"]
                }
                conversations.append({"conversation": [conversation]})
    return conversations

def write_to_json(output_file, conversations):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(conversations, f, ensure_ascii=False, indent=4)

def main(jsonl_file, output_file):
    conversations = convert_to_json(jsonl_file)
    write_to_json(output_file, conversations)

if __name__ == "__main__":
    jsonl_file = "dugushici-com-70k.json"
    output_file = "output4.json"
    main(jsonl_file, output_file)
