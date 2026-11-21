<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![project_license][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!-- <a href="https://github.com/henryhuyvu/experimental-robotics">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

<h3 align="center">Experimental Robotics</h3>

  <p align="center">
    Exploratory integration of sensors and hardware for mobile systems.
    <br />
    <a href="https://github.com/henryhuyvu/experimental-robotics"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/henryhuyvu/experimental-robotics">View Demo</a>
    &middot;
    <a href="https://github.com/henryhuyvu/experimental-robotics/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/henryhuyvu/experimental-robotics/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#requirements">Requirements</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

  <a href="https://github.com/henryhuyvu/experimental-robotics">
    <img src="images/Differential wheeled robot - Front right.png" alt="Logo" width="400" height="380">
  </a>

The ideas embedded into this project formed over many years, propelled by various efforts and interests in building electro-mechanical tools.

Technology has certainly changed the way humans interact with the environment. A consequence of the constantly improving technologies around us have positioned consumer electronics to be fairly inexpensive and quite accessible as compared to decades past.

My intention with this project shifted toward building a safe and remotely operable locomotive platform that serves as a testbed for mounting an assortment of sensors and electronics to collect data and interact with the local environment.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Visual Studio Code][Visual Studio Code.com]][Visual Studio Code-url]
* [![Raspberry Pi][Raspberry Pi.com]][Raspberry Pi-url]
* [![Python][Python.com]][Python-url]
* ![JavaScript][JavaScript.com]
* ![HTML][HTML.com]

And supported by a range of open and closed source LLMs via local hosting and API calls:
* ![Ollama]
* ![Claude]
* ![ChatGPT]
* ![Google Gemini]
* ![Qwen]
* ![Mistral AI]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
This project was built upon electronics that I was either familiar with and have readily available, had salvaged from other devices, or purchased with the intention of eventually making use of such parts.

The following is my approach to this build. Any alternative components you may want to use will need to be accounted for and adapted as required.

### Requirements
#### Hardware
* Raspberry Pi Pico 2 W
* Raspberry Pi Zero 2 W
* Raspberry Pi Camera Module 2 NoIR
* TB6612FNG motor driver (2x)
* JGA25-371 DC Gearmotor with Encoder (2x)
* 3C LiPo battery
* LiPo Battery Voltage Tester / Low Voltage Buzzer Alarm
* 5V, 500mA Step-Down Voltage Regulator D24V5F5
* 5V, 3A Portable Battery

##### Structural Parts
* 3D Printed. CAD files to be added.

##### Wiring Diagram(s)
* To be added.

#### Software
* VSCode
* Raspberry Pi OS Lite
* Python
* MicroPython
* JavaScript

### Installation
1. Clone the repo in your directory of choice
   ```sh
   git clone https://github.com/henryhuyvu/experimental-robotics.git
   ```
2. Install the MicroPico Extension through VSCode. This will enable the MicroPico commands in which a Raspberry Pi Pico connected to your computer can be accessed via VSCode, and files can be loaded onto and executed by the Pico.
3. Initialize the Pico with MicroPython as guided [here](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html).
4. Upload the `/pico/boot.py` and `/pico/main.py` scripts onto the Pico device.
5. Create and store a `config.json` file on the Pico with information on your local WiFi access information as follows:
    ```json
    {
        "WIFI_SSID": "Your-WiFi-Name",
        "WIFI_PASSWORD": "Your-Wifi-Password", 
    }
    ```
6. Initialize your Raspberry Pi Zero 2 W with the Raspberry Pi OS Lite (32-bit). Enter your WiFi info so that the system can automatically connect. At some point, you will also need to enable the Raspberry Pi Camera as well as SSH for the Zero device.
7. Copy all files in the `/zero` directory onto the Zero device.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Usage
The Zero is the main point of control for the device. When powered on, SSH into the Zero and launch the `web_server.py` script by navigating to the directory with that file and running `python web_server.py`. This will launch a locally hosted web page at the IP address of the Zero, on port 3000.

If all is working, this webpage will show a camera feed and a few on-screen buttons for controlling the motion of the device. Alternatively, use the WASD keys to move the device.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap
Additional electronic components I will want to attach onto the system are:

- [ ] IR LEDs
- [ ] Tilting servo motor(s) for the Pi Camera
- [ ] Stereo MEMs microphones
- [ ] Mono speakers

The software side of things can have many improvements:
- [ ] Secure remote access
- [ ] SQL data storage and Event management
- [ ] Updated control scheme with dynamic response.
- [ ] Edge or cloud computing.
- [ ] Image recognition
- [ ] Human pose estimation


<!-- See the [open issues](https://github.com/henryhuyvu/experimental-robotics/issues) for a full list of proposed features (and known issues). -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p\>



<!-- ### Top contributors:

<a href="https://github.com/henryhuyvu/experimental-robotics/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=henryhuyvu/experimental-robotics" alt="contrib.rocks image" />
</a> -->



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

<!-- Henry Vu - vuhenry0@proton.me -->

Project Link: [https://github.com/henryhuyvu/experimental-robotics](https://github.com/henryhuyvu/experimental-robotics)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/github/license/henryhuyvu/experimental-robotics.svg?style=for-the-badge
[license-url]: https://github.com/henryhuyvu/experimental-robotics/blob/main/LICENSE

<!-- Shields.io badges. You can a comprehensive list with many more badges at: https://github.com/inttter/md-badges -->
[Visual Studio Code.com]: https://custom-icon-badges.demolab.com/badge/Visual%20Studio%20Code-0078d7.svg?logo=visualstudiocode&logoColor=white
[Visual Studio Code-url]: https://code.visualstudio.com/

[Raspberry Pi.com]: https://img.shields.io/badge/Raspberry_Pi-cd2355.svg?logo=raspberrypi
[Raspberry Pi-url]: https://www.raspberrypi.com/

[Python.com]: https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff
[Python-url]: https://www.python.org/

[JavaScript.com]: https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=000

[HTML.com]: https://img.shields.io/badge/HTML-%23E34F26.svg?logo=html5&logoColor=white 

<!-- AI tools -->

[ChatGPT]: https://custom-icon-badges.demolab.com/badge/ChatGPT-74aa9c?logo=openai&logoColor=white

[Claude]: https://img.shields.io/badge/Claude-D97757?logo=claude&logoColor=fff

[Google Gemini]: https://img.shields.io/badge/Google%20Gemini-886FBF?logo=googlegemini&logoColor=fff

[Mistral AI]: https://img.shields.io/badge/Mistral%20AI-FA520F?logo=mistral-ai&logoColor=fff

[Ollama]: https://img.shields.io/badge/Ollama-fff?logo=ollama&logoColor=000

[Qwen]: https://custom-icon-badges.demolab.com/badge/Qwen-605CEC?logo=qwen&logoColor=fff
