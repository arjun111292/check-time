if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TELEZEN/Jennie-tr-real-test.git /Jennie-tr-real-test
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Jennie-tr-real-test
fi
cd /Jennie-tr-real-test
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
