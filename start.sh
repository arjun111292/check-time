if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TELEZEN/jennie-tr-test2.git /jennie-tr-test2
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /jennie-tr-test2
fi
cd /jennie-tr-test2
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
