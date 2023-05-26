
# Voice-Based Assistant 

This is a Python program that functions as a virtual assistant, capable of performing various tasks based on voice commands.

## Features

- Greet the user based on the time of day (morning, afternoon, or evening).
- Accept voice commands and convert them into text.
- Search and retrieve information from Wikipedia.
- Open popular websites such as YouTube, Google, and GeekforGeeks.
- Play music from a specified directory.
- Provide the current time.
- Open Any Application.

## Prerequisites

To run the Voice-Based Assistant program, you need to have the following:

- Python 3 installed on your machine.
- portaudio module on your machine in case of linux
- Required Python packages: pyttsx3, speech_recognition, wikipedia.

You can install the required packages using the following command:

```shell
sudo apt install portaudio19-dev //for linux or Macos 
```

```shell
pip install pyttsx3 speechrecognition wikipedia pyaudio
```

## Usage

1. Clone the repository or download the source code.
2. Install the required packages (if not already installed) using the above command.
3. Run the Python script:

   ```shell
   python assistant.py
   ```

4. The assistant will greet you based on the time of day and will be ready to receive your voice commands.
5. Speak your command clearly into the microphone.
6. The assistant will process the command and perform the corresponding action.

## Customization

- Voice Selection: You can customize the voice used by the assistant by modifying the `setProperty` function call in the code. For example, to use a different voice, change `voices[0].id` to `voices[1].id` or any other available voice index.
- Music Directory: If you want to play music, make sure to update the `music_dir` variable in the code to point to the directory where your music files are located.
- Chrome Browser Path: If you want to open Google Chrome, ensure that the `path` variable in the code points to the correct path where the Chrome browser executable is installed.
- you can also do 

## Contributing

Contributions to Voice-Based Assistant are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- This program was developed as a learning exercise and is inspired by various virtual assistant projects on youtube and blogs over internet.

Feel free to modify and customize the README file based on your preferences and additional information you want to provide.
