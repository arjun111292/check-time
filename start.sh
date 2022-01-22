if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TELEZEN/Ercel-monore.git /Ercel-monore
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Ercel-monore
fi
cd /Ercel-monore
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
