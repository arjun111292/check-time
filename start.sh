if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TELEZEN/jennie-multiple-pic-test.git /jennie-multiple-pic-test
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /jennie-multiple-pic-test
fi
cd /jennie-multiple-pic-test
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
