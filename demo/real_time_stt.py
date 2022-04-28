{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pipwin in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (0.5.2)\n",
      "Requirement already satisfied: docopt in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from pipwin) (0.6.2)\n",
      "Requirement already satisfied: pyprind in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from pipwin) (2.11.3)\n",
      "Requirement already satisfied: beautifulsoup4>=4.9.0 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from pipwin) (4.10.0)\n",
      "Requirement already satisfied: packaging in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from pipwin) (21.3)\n",
      "Requirement already satisfied: js2py in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from pipwin) (0.71)\n",
      "Requirement already satisfied: six in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from pipwin) (1.16.0)\n",
      "Requirement already satisfied: requests in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from pipwin) (2.27.1)\n",
      "Requirement already satisfied: pySmartDL>=1.3.1 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from pipwin) (1.3.4)\n",
      "Requirement already satisfied: soupsieve>1.2 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from beautifulsoup4>=4.9.0->pipwin) (2.3.1)\n",
      "Requirement already satisfied: pyjsparser>=2.5.1 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from js2py->pipwin) (2.7.1)\n",
      "Requirement already satisfied: tzlocal>=1.2 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from js2py->pipwin) (4.2)\n",
      "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from packaging->pipwin) (3.0.7)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from requests->pipwin) (3.3)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from requests->pipwin) (2.0.12)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from requests->pipwin) (2021.10.8)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from requests->pipwin) (1.26.8)\n",
      "Requirement already satisfied: pytz-deprecation-shim in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from tzlocal>=1.2->js2py->pipwin) (0.1.0.post0)\n",
      "Requirement already satisfied: tzdata in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from pytz-deprecation-shim->tzlocal>=1.2->js2py->pipwin) (2022.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install pipwin"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pipwin/command.py:66: UserWarning: Found a non Windows system. Package installation might not work.\n",
      "  warn(\"Found a non Windows system. Package installation might not work.\")\n",
      "Traceback (most recent call last):\n",
      "  File \"/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/packaging/requirements.py\", line 102, in __init__\n",
      "    req = REQUIREMENT.parseString(requirement_string)\n",
      "  File \"/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pyparsing/core.py\", line 1134, in parse_string\n",
      "    raise exc.with_traceback(None)\n",
      "pyparsing.exceptions.ParseException: Expected string_end, found '‑'  (at char 7), (line:1, col:8)\n",
      "\n",
      "During handling of the above exception, another exception occurred:\n",
      "\n",
      "Traceback (most recent call last):\n",
      "  File \"/Library/Frameworks/Python.framework/Versions/3.10/bin/pipwin\", line 8, in <module>\n",
      "    sys.exit(main())\n",
      "  File \"/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pipwin/command.py\", line 91, in main\n",
      "    for package in _package_names(args):\n",
      "  File \"/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pipwin/command.py\", line 43, in _package_names\n",
      "    yield Requirement(args[\"<package>\"].lower())\n",
      "  File \"/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/packaging/requirements.py\", line 104, in __init__\n",
      "    raise InvalidRequirement(\n",
      "packaging.requirements.InvalidRequirement: Parse error at \"'‑0.2.11‑'\": Expected string_end\n"
     ]
    }
   ],
   "source": [
    "!pipwin install PyAudio‑0.2.11‑cp38‑cp38‑win_amd64.whl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'pyaudio'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m/Users/toto/Documents/en_stt_wavtovec2/demo/real_time_stt.ipynb Cell 3'\u001b[0m in \u001b[0;36m<cell line: 5>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      <a href='vscode-notebook-cell:/Users/toto/Documents/en_stt_wavtovec2/demo/real_time_stt.ipynb#ch0000002?line=2'>3</a>\u001b[0m \u001b[39mimport\u001b[39;00m \u001b[39mbase64\u001b[39;00m\n\u001b[1;32m      <a href='vscode-notebook-cell:/Users/toto/Documents/en_stt_wavtovec2/demo/real_time_stt.ipynb#ch0000002?line=3'>4</a>\u001b[0m \u001b[39mimport\u001b[39;00m \u001b[39masyncio\u001b[39;00m\n\u001b[0;32m----> <a href='vscode-notebook-cell:/Users/toto/Documents/en_stt_wavtovec2/demo/real_time_stt.ipynb#ch0000002?line=4'>5</a>\u001b[0m \u001b[39mimport\u001b[39;00m \u001b[39mpyaudio\u001b[39;00m\n\u001b[1;32m      <a href='vscode-notebook-cell:/Users/toto/Documents/en_stt_wavtovec2/demo/real_time_stt.ipynb#ch0000002?line=5'>6</a>\u001b[0m \u001b[39mimport\u001b[39;00m \u001b[39mwebsockets\u001b[39;00m\n\u001b[1;32m      <a href='vscode-notebook-cell:/Users/toto/Documents/en_stt_wavtovec2/demo/real_time_stt.ipynb#ch0000002?line=7'>8</a>\u001b[0m SAMPLE_RATE\u001b[39m=\u001b[39m\u001b[39m16000\u001b[39m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'pyaudio'"
     ]
    }
   ],
   "source": [
    "import json\n",
    "\n",
    "import base64\n",
    "import asyncio\n",
    "import pyaudio\n",
    "import websockets\n",
    "\n",
    "SAMPLE_RATE=16000\n",
    "FRAMES_PER_BUFFER = 3200\n",
    "API_KEY = '<your AssemblyAI Key goes here>'\n",
    "ASSEMBLYAI_ENDPOINT =  f'wss://api.assemblyai.com/v2/realtime/ws?sample_rate={SAMPLE_RATE}'\n",
    "\n",
    "\n",
    "p = pyaudio.PyAudio()\n",
    "audio_stream = p.open(\n",
    "   frames_per_buffer=FRAMES_PER_BUFFER,\n",
    "   rate=SAMPLE_RATE,\n",
    "   format=pyaudio.paInt16,\n",
    "   channels=1,\n",
    "   input=True,\n",
    ")\n",
    "\n",
    "async def speech_to_text():\n",
    "    \"\"\"\n",
    "    Asynchronous function used to perfrom real-time speech-to-text using AssemblyAI API\n",
    "    \"\"\"\n",
    "    async with websockets.connect(\n",
    "           ASSEMBLYAI_ENDPOINT,\n",
    "           ping_interval=5,\n",
    "           ping_timeout=20,\n",
    "           extra_headers=(('Authorization', API_KEY), ),\n",
    "    ) as ws_connection:\n",
    "        await asyncio.sleep(0.5)\n",
    "        await ws_connection.recv()\n",
    "        print('Websocket connection initialised')\n",
    "        \n",
    "        async def send_data():\n",
    "            \"\"\"\n",
    "            Asynchronous function used for sending data\n",
    "            \"\"\"\n",
    "            while True:\n",
    "                try:\n",
    "                    data = audio_stream.read(FRAMES_PER_BUFFER)\n",
    "                    data = base64.b64encode(data).decode('utf-8')\n",
    "                    await ws_connection.send(json.dumps({'audio_data': str(data)}))\n",
    "                except Exception as e:\n",
    "                    print(f'Something went wrong. Error code was {e.code}')\n",
    "                    break\n",
    "                await asyncio.sleep(0.5)\n",
    "            return True\n",
    "       \n",
    "        async def receive_data():\n",
    "            \"\"\"\n",
    "            Asynchronous function used for receiving data\n",
    "            \"\"\"\n",
    "            while True:\n",
    "                try:\n",
    "                    received_msg = await ws_connection.recv()\n",
    "                    print(json.loads(received_msg)['text'])\n",
    "                except Exception as e:\n",
    "                    print(f'Something went wrong. Error code was {e.code}')\n",
    "                    break\n",
    "                    \n",
    "        data_sent, data_received = await asyncio.gather(send_data(), receive_data())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "interpreter": {
   "hash": "31f2aee4e71d21fbe5cf8b01ff0e069b9275f58929596ceb00d14d90e3e16cd6"
  },
  "kernelspec": {
   "display_name": "Python 3.8.9 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.9"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
