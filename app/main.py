import argparse
import os
import sys
import json
import subprocess

from openai import OpenAI

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("OPENROUTER_BASE_URL", default="https://openrouter.ai/api/v1")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("-p", required=True)
    args = p.parse_args()

    if not API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY is not set")

    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    read_tool = {
        'type' : 'function', 'function' : {
            'name' : 'Read', 'description' : 'Read and return the contents of a file', 'parameters' : {
                'type' : 'object', 'properties' : {
                    'file_path' : {
                        'type' : 'string', 'description' : 'Path to the file to read'
                    }
                }, 'required' : ['file_path']
            }
        }    
    }

    write_tool = {
        "type": "function",
        "function": {
            "name": "Write",
            "description": "Write content to a file",
            "parameters": {
            "type": "object",
            "required": ["file_path", "content"],
            "properties": {
                "file_path": {
                "type": "string",
                "description": "The path of the file to write to"
                },
                "content": {
                "type": "string",
                "description": "The content to write to the file"
                    }
                }
            }
        }
    }

    bash_tool = {
        "type": "function",
        "function": {
            "name": "Bash",
            "description": "Execute a shell command",
            "parameters": {
            "type": "object",
            "required": ["command"],
            "properties": {
                "command": {
                "type": "string",
                "description": "The command to execute"
                    }
                }
            }
        }
    }

    messages = [{"role": "user", "content": args.p}]
    while(True):
        
        chat = client.chat.completions.create(
            model= "anthropic/claude-haiku-4.5",
            messages= messages,
            tools = [read_tool, write_tool, bash_tool]
        )

        if not chat.choices or len(chat.choices) == 0:
            raise RuntimeError("no choices in response")
        
        assisstant_message = chat.choices[0].message
        messages.append({
            'role' : 'assistant',
            'content' : assisstant_message.content,
            'tool_calls' : assisstant_message.tool_calls
        })

        tool_calls = assisstant_message.tool_calls
        if tool_calls:
            for tool_call in tool_calls:
                if tool_call.function.name == 'Read':
                    file_path = json.loads(tool_call.function.arguments)['file_path']
                    with open(file_path) as file:
                        content = file.read()
                
                if tool_call.function.name == 'Write':
                    function_args = json.loads(tool_call.function.arguments)
                    file_path = function_args['file_path']
                    content = function_args['content']
                    with open(file_path, 'w') as file:
                        file.write(content)

                if tool_call.function.name == 'Bash':
                    command = json.loads(tool_call.function.arguments)['command']
                    result = subprocess.run(command, shell=True, capture_output=True, text=True)
                    content = result.stdout if result.returncode == 0 else result.stderr

                messages.append({
                    'role': 'tool', 'tool_call_id' : tool_call.id, 'content' : content 
                })

        else:
            print(assisstant_message.content)
            break

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)
    


if __name__ == "__main__":
    main()
