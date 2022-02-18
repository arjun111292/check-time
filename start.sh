if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TELEZEN/PIC_TESTER.git /PIC_TESTER
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /PIC_TESTER
fi
cd /PIC_TESTER
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
