vagrant box add ubuntu/xenial64
vagrant init ubuntu/xenial64

# Building vagrant environment
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install postgresql libpq-dev
sudo su - postgres
  createdb django_hoc_db
  createuser -P djangodbm
    fred
  psql
    GRANT ALL PRIVILEGES ON DATABASE django_hoc_db to djangodbm;
    ALTER USER djangodbm CREATEDB;
    \q
  exit
cd /vagrant
sudo -u postgres pg_restore --verbose --clean --no-acl --no-owner -d django_hoc_db db/django-hoc-b004.dump
sudo apt-get install python3-dev
curl https://bootstrap.pypa.io/get-pip.py | sudo python3
sudo pip3 install virtualenv
virtualenv ~/vagrant-venv
source ~/vagrant-venv/bin/activate
sudo apt-get install gcc
pip install django-toolbelt
pip install django-dotenv
cat vagrant-user/.bashrc_append >> ~/.bashrc
cp vagrant-user/.bash_hoc ~/.
cp -pr vagrant-user/.ssh ~/.
chmod go-rwx ~/.ssh ~/.ssh/id_rsa
# install heroku toolbelt
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
# cache Heroku API token in ~/.netrc
heroku pg:backups -a django-hoc

python manage.py migrate

# Build a vagrant box
vagrant package default --output django_hoc.box

# Update Vagrantfile with:
# config.vm.network "forwarded_port", guest: 8000, host: 8000
# config.vm.box = "django_hoc"

# create new app
mkdir -p django-hoc-$i; (cd django-hoc-$i; git init; heroku apps:create django-hoc-$i; heroku sharing:add dudek@pobox.com; heroku addons:add heroku-postgresql:hobby-dev; heroku pg:wait; heroku addons:add pgbackups; heroku pgbackups:restore --confirm django-hoc-$i DATABASE http://django-hoc-00.herokuapp.com/static/django_hoc_db.dump)

for i in '02' '03' '04' '05' '06' '07' '08' '09' '10'; do echo $i; mkdir -p django-hoc-$i; (cd django-hoc-$i; git init; heroku apps:create django-hoc-$i; heroku sharing:add dudek@pobox.com; heroku addons:add heroku-postgresql:hobby-dev; heroku pg:wait; heroku addons:add pgbackups; heroku pgbackups:restore --confirm django-hoc-$i DATABASE http://django-hoc-00.herokuapp.com/static/django_hoc_db.dump); done

Once you have downloaded these files and installed VirtualBox and Vagrant, then you need to do the following:

To install:
1. Install VirtualBox
2. Install Vagrant
3. Import the vagrant box for django_hox:
  vagrant box add django_hoc ./django_hoc.box
4. Clone the github repository:
  git clone https://github.com/glendudek/django_hoc.git django
5. Add the heroku app remote:
  cd django; git remote add heroku git@heroku.com:django-hoc-##.git

To test the install:
6. cd django
7. Bring up the vagrant image:
  vagrant up
8. Log in to the vagrant image:
  vagrant ssh
9. Run the server locally:
  ./runserver
10. Connect to the local server from a browser:
  http://localhost:8000
11. Push application to heroku:
  git push heroku master
12. Connect to the application at heroku from a browser:
  http://django-hoc-##.herokuapp.com

To install:
1. Install VirtualBox
2. Install Vagrant
3. Import the vagrant box for django_hox: vagrant box add django_hoc ./django_hoc.box
4. Clone the github repository: git clone https://github.com/glendudek/django_hoc.git django
5. Add the heroku app remote: git remote add heroku git@heroku.com:django-hoc-##.git

To test the install:
6. cd django
7. Bring up the vagrant image: vagrant up
8. Log in to the vagrant image: vagrant ssh
9. Run the server locally: ./runserver
10. Connect to the local server from a browser: http://localhost:8000
11. Push application to heroku: git push heroku master
12. Connect to the application at heroku from a browser: http://django-hoc-##.herokuapp.com

vagrant up
# Log in to the Vagrant/VirtualBox virtual machine
vagrant ssh
# Run the server locally
./runserver
# At this point you can connect to the application from a local Safari or Chrome browser at 
# Copy and restart the application at heroku - respond "yes" to add heroku to the list of known hosts

# At this point you can connect to the application at Heroku from any browser at django-hoc-##.herokuapp.com/polls

# misc (obsolete?)
install python3
install pip
  python3 get-pip.py
install virtualenv
  sudo pip3 install virtualenv

https://devcenter.heroku.com/articles/getting-started-with-django

venv/bin/activate

foreman start

# set up local postgresql database
sudo su - postgres
createdb django_hoc_db
createuser -P djangodbm
  fred
psql
  GRANT ALL PRIVILEGES ON DATABASE django_hoc_db to djangodbm;
  ALTER USER djangodbm CREATEDB;

echo 'DATABASE_URL="postgres://djangodbm:fred@localhost/django_hoc_db"' > .env

pip install django-dotenv
pip freeze > requirements.txt
# add to manage.py
  import dotenv
  dotenv.read_dotenv()
