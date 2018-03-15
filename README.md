## Don't forget to include in pelicanconf.py
```
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".hg", ".git", ".bzr"]
```

## Publish Locally
```
$ cd moonshot_landing
$ pelican content --debug --autoreload  --output output --settings pelicanconf.py
$ pelican content --output output --settings pelicanconf.py
$ cd output
$ python -m pelican.server
```

In case python -m pelican.server is not working(can change port and ip address)
```
$ python -m http.server 8888 --bind 127.0.0.1
```

## Deploy Online
Generate static html files
```
$ cd moonshot_landing
$ pelican content --output output --settings publishconf.py
```

## Push Output to GitHub from the output folder
```
$ cd output
$ git add .
$ git commit -m "Commit message"
$ git push origin gh-pages --force
```

## Push source code to GitHub
```
$ cd moonshot_landing
$ git add .
$ git commit -m "Commit message"
$ git push origin source
