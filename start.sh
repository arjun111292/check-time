if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TELEZEN/filter-main.git /filter-main
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /filter-main
fi
cd /filter-main
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
