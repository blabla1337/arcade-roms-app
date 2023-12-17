# Iconic Arcade App

For adding new roms to your Iconic Arcade you can start a web application where you can upload your roms.

First download the start_app.sh and make sure the Iconic Arcade is turned on and connected to the network.

Now we run the script:

```
./start_app.sh
```

You will be prompted with a password to enter, default installation uses: linux

```
gibson@macbook# ./start_app.sh
# batocera.local:22 SSH-2.0-dropbear_2022.83
# batocera.local:22 SSH-2.0-dropbear_2022.83
# batocera.local:22 SSH-2.0-dropbear_2022.83
# batocera.local:22 SSH-2.0-dropbear_2022.83
# batocera.local:22 SSH-2.0-dropbear_2022.83
Pseudo-terminal will not be allocated because stdin is not a terminal.
root@batocera.local's password: 
```

After this the script will continue to setup the application and start it.
Now you can go to your browser and use the application to upload your roms.

```
http://batocera.local:5000/
```
