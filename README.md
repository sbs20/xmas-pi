# Xmas PI

Merry Chrstmas!!

This is a simple project containing a python script which cycles through a few
patterns. Install python 2 and gpiozero:

```
sudo apt install python python-gpiozero
```

Then mark `xmas.py` as executable
```
chmod +x xmas.py
```

Then run
```
./xmas.py
```

`ctrl-c` to exit

If you want to run it in the background then
```
./xmas.py &
```

To kill the background process, find it then kill the pid
```
ps ax | grep xmas.py
kill nnnnn
```

I may add a proper start and stop mechanism for next Christmas.
