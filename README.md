# 🌱 **Plant Watering Bot README** 🌱

This repository contains code for a simple bot that waters a plant upon receiving a command in Twitch chat. The bot interacts with an Arduino board connected to your computer via USB, which controls the watering mechanism.

## 🛠️ **Prerequisites**

Before running the bot, ensure you have the following installed:

- Python 3.x
- [TwitchIO](https://github.com/TwitchIO/TwitchIO) library
- Arduino IDE for uploading code to the Arduino board

## 🌿 **Hardware Setup**

1. Connect your Arduino board to your computer using a USB cable.
2. Connect a water pump or any watering mechanism to one of the digital pins of the Arduino board. I used pin A1 but it can be changed in the arduino code.

## ⚙️ **Arduino Setup**

1. Open the Arduino IDE and upload the provided Arduino sketch (`plant_watering.ino`) to your Arduino board.

## 📜 **Circuit Diagram**

![Plant Watering Circuit Diagram](https://i.imgur.com/vZlY5bS.png)

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
2. Run the Python script `twitch2_working.py`:

   ```
   python twitch2_working.py
   ```

3. Your bot should now be running and ready to respond to commands in your Twitch chat.

## 🌊 **Usage**

To water the plant, type the following command in your Twitch chat:

```
!water
```

The bot will respond with a confirmation message and trigger the watering mechanism.



## 📝 **Notes**

- Make sure your Arduino board is properly connected and recognized by your computer before running the bot.
- If the Arduino is correctly receiving the serial message, there should be a led on the board that lights up.
- Ensure your Twitch bot has appropriate permissions to send messages in your channel.
