https://realpython.com/blog/python/flask-by-example-part-1-project-setup/

sudo apt-get install git
git init
sudo apt-get install python-virtualenv
virtualenv --python=/usr/bin/python3.6.3 venv or (virtualenv -p python3 envname) then source envname/bin/activate

source venv/bin/activate (deactivate to turn off, source venv/bin/activate to turn on)
pip install Flask==0.10.1
pip freeze > requirements.txt (freeze requirements)

https://devcenter.heroku.com/articles/getting-started-with-python
https://toolbelt.heroku.com/
sudo apt install ruby
gem install heroku
sudo ln -s /usr/local/heroku/bin/heroku /usr/bin/heroku
wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh

asdfASDF@

npm install -g heroku-cli


heroku login

touch Procfile

$ pip install gunicorn==19.4.5
$ pip freeze > requirements.txt


place: python-3.5.1 into runtime.txt

Commit your changes in git (and optionally push to Github), then create two new Heroku apps.

1.git init
2.git config user.name "someone"
3.git config user.email "someone@someplace.com"
4.git add *
5.git commit -m "some init msg"


heroku create whalehunter-pro
heroku create whalehunter-stage


git remote add pro git@heroku.com:whalehunter-pro.git
git remote add stage git@heroku.com:whalehunter-stage.git



git commit -m "initial commit"
# heroku git:remote -a whalehunter

sudo .git/config -> changed the project name in [remote "heroku"] to the name given by heroku.

https://devcenter.heroku.com/articles/keys
ssh-keygen -t rsa
heroku keys:add

Now we can push both of our apps live to Heroku.

(if something goes wrong with production environment fatal: remote pro already exists: git remote rm pro)


For staging: git push stage master
For production: git push pro master


(envname) x@x:~/Desktop/WhaleHunter$ heroku git:remote -a whalehunter-pro
This is the legacy Heroku CLI. Please install the new CLI from https://cli.heroku.com
set git remote heroku to https://git.heroku.com/whalehunter-pro.git


Deploy your application

Commit your code to the repository and deploy it to Heroku using Git.


(run this part if get the packages error )
$ git add .
$ git commit -am "make it better"
$ git push heroku master








when working with new files, recommit:

git commit -m "initial commit"
git config --global user.email "you@example.com"


git add .

git config --global user.name "Your Name"
git push origin master

git add Optimization/language/languageUpdate.php
git add email_test.php



To start over / with new files:

git init
git add .
git commit -m "note"
git remote add pro git@heroku.com:whalehunter-pro.git (pro is the name here)
ssh-keygen -t rsa
heroku keys:add
git push pro master
git push heroku master


for new one:
heroku login
$ cd my-project/
$ git init
$ git add .
$ git commit -am "make it better"
$ git remote add pro git@heroku.com:front_end-pro.git (pro is the name here)

$ heroku keys:add
ssh-keygen -t rsa
$ git push pro master

$ git:remote -a frontend-pro

$ git commit -am "make it better"
$ git push heroku master



git commit -m "my first commit"
heroku create
git push heroku master





