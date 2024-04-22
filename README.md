# 🌱 **Plant Watering Bot README** 🌱

This repository contains code for a simple bot that waters a plant upon receiving a command in Twitch chat. The bot interacts with an Arduino board connected to your computer via USB, which controls the watering mechanism.

## 🛠️ **Prerequisites**

Before running the bot, ensure you have the following installed:

- Python 3.x
- [TwitchIO](https://github.com/TwitchIO/TwitchIO) library
- Arduino IDE for uploading code to the Arduino board

## 🌿 **Hardware Setup**

1. Connect your Arduino board to your computer using a USB cable.
2. Connect a water pump or any watering mechanism to one of the digital pins of the Arduino board. In this example, we'll use pin A1.
3. Optionally, connect an LED to pin A0 to indicate when the plant is being watered.

## ⚙️ **Arduino Setup**

1. Open the Arduino IDE and upload the provided Arduino sketch (`plant_watering.ino`) to your Arduino board.

## 🐍 **Python Setup**

1. Install the required Python dependencies by running:

   ```
   pip install twitchio
   ```

2. Set up your Twitch Bot credentials by creating a `.env` file in the project directory. Add the following lines to the `.env` file:

   ```
   TMI_TOKEN=[OAUTH TOKEN HERE https://twitchapps.com/tmi/]
   CLIENT_ID=[CLIENT_ID TOKEN HERE https://dev.twitch.tv/console/apps/create]
   BOT_NICK=examplename
   BOT_PREFIX=!
   CHANNEL=examplechannel
   SERIAL_PORT=COM7
   ```

   Replace `[OAUTH TOKEN HERE]` and `[CLIENT_ID TOKEN HERE]` with your actual Twitch OAuth token and client ID token, respectively. Also, adjust `examplename`, `examplechannel`, and `COM7` with your desired bot name, Twitch channel name, and serial port, respectively.

## 🚀 **Running the Bot**

1. Ensure your Arduino board is connected to your computer.
2. Run the Python script `bot.py`:

   ```
   python bot.py
   ```

3. Your bot should now be running and ready to respond to commands in your Twitch chat.

## 🌊 **Usage**

To water the plant, type the following command in your Twitch chat:

```
!water
```

The bot will respond with a confirmation message and trigger the watering mechanism.

## 📜 **Circuit Diagram**

![Plant Watering Circuit Diagram](https://i.imgur.com/vZlY5bS.png)

## 📝 **Notes**

- Make sure your Arduino board is properly connected and recognized by your computer before running the bot.
- Adjust the pin numbers in the Arduino sketch and Python script if you've connected the watering mechanism or LED to different pins.
- Ensure your Twitch bot has appropriate permissions to send messages in your channel.
